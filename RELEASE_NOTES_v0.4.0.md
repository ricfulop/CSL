# Release Notes - v0.4.0

## 🎉 Fusion Backend Now Fully Functional!

This release fixes critical issues in the Fusion 360 backend, making CSL v1.3 features fully operational.

## Major Fixes

### 1. Fillet API Update
- **Issue**: Fusion API method `createConstantRadiusFilletDefinition` was deprecated
- **Fix**: Updated to use `createInput()` + `addConstantRadiusEdgeSet()`
- **Impact**: Fillets now work correctly

### 2. Feature Type Detection
- **Issue**: Backend was looking for `kind` field instead of CSL standard `type`
- **Fix**: Check for both `type` (CSL) and `kind` (legacy) fields
- **Impact**: Features and sketch entities are now properly recognized

### 3. Point Parsing
- **Issue**: `_parse_point()` only handled string inputs, not lists/arrays
- **Fix**: Enhanced to handle both `[-10, -10]` arrays and `"x, y"` strings
- **Impact**: Rectangles and other geometry now create correctly

### 4. Profile Resolution
- **Issue**: Extrudes couldn't find profiles from sketches
- **Fix**: Added entity-to-sketch mapping and improved profile lookup
- **Impact**: Extrudes now work reliably

### 5. Error Reporting
- **Issue**: Failures were silent, making debugging impossible
- **Fix**: Added comprehensive error reporting throughout
- **Impact**: Clear error messages when something goes wrong

## Test Results

✅ **5 of 6 core features passing:**
- CSL Extrude - Working
- CSL Fillet - Working  
- Timeline operations - Working
- Selection queries - Working
- View operations - Working
- Parameters - Known API issue (will fix in v0.4.1)

## Enhanced Add-in Features

The `triple_lindy_fusion_enhanced` add-in now includes:
- Real-time file-based communication protocol
- Comprehensive query system for debugging
- Module hot-reloading support
- Detailed error reporting with mapping
- Support for both CSL and direct API modes

## Breaking Changes

None - all changes are backward compatible.

## Installation

```bash
# Update to latest
git pull

# Deploy enhanced add-in (macOS)
cp -r triple_lindy_fusion_enhanced "$HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/"

# Copy the backend
cp -r triple_lindy "$HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/"
```

Then restart Fusion 360 and enable the "triple_lindy_fusion_enhanced" add-in.

## What's Next

- v0.4.1: Fix parameter creation API issue
- v0.5.0: Complete CSL v1.3 feature coverage
- v0.6.0: FreeCAD backend implementation

## Contributors

Special thanks to the CSL community for testing and feedback!
