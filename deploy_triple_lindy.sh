#!/bin/bash
# Deploy Triple Lindy Enhanced to Fusion 360 AddIns directory

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Triple Lindy Enhanced Deployment Script${NC}"
echo -e "${GREEN}========================================${NC}"

# Source and destination paths
SOURCE_DIR="./triple_lindy_fusion_enhanced"
ADDINS_DIR="$HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns"
DEST_DIR="$ADDINS_DIR/triple_lindy_fusion_enhanced"

# Check if source exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${RED}Error: Source directory not found: $SOURCE_DIR${NC}"
    exit 1
fi

# Create AddIns directory if it doesn't exist
if [ ! -d "$ADDINS_DIR" ]; then
    echo -e "${YELLOW}Creating AddIns directory...${NC}"
    mkdir -p "$ADDINS_DIR"
fi

# Backup existing add-in if it exists
if [ -d "$DEST_DIR" ]; then
    BACKUP_DIR="${DEST_DIR}_backup_$(date +%Y%m%d_%H%M%S)"
    echo -e "${YELLOW}Backing up existing add-in to: ${BACKUP_DIR}${NC}"
    mv "$DEST_DIR" "$BACKUP_DIR"
fi

# Copy the add-in
echo -e "${GREEN}Deploying add-in to: $DEST_DIR${NC}"
cp -r "$SOURCE_DIR" "$DEST_DIR"

# Verify deployment
if [ -f "$DEST_DIR/triple_lindy_fusion_enhanced.py" ] && [ -f "$DEST_DIR/triple_lindy_fusion_enhanced.manifest" ]; then
    echo -e "${GREEN}✅ Deployment successful!${NC}"
    echo ""
    echo -e "${YELLOW}Next steps:${NC}"
    echo "1. Open Fusion 360"
    echo "2. Go to: Utilities → Add-Ins → Scripts and Add-Ins"
    echo "3. Under 'Add-Ins' tab, find 'triple_lindy_fusion_enhanced'"
    echo "4. If already running: Stop → Run"
    echo "5. If not listed: Use 'Add Existing Add-In' and browse to:"
    echo "   $DEST_DIR"
    echo ""
    echo -e "${GREEN}Test the fix:${NC}"
    echo "   python test_triple_lindy_fix.py"
else
    echo -e "${RED}❌ Deployment failed - files not found in destination${NC}"
    exit 1
fi
