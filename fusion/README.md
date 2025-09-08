# Fusion 360 Development Resources

This directory contains critical documentation and resources for Fusion 360 API development, particularly for CSL backend integration.

## 📚 Documentation

### [FUSION_360_API_GUIDE.md](./FUSION_360_API_GUIDE.md)
Comprehensive guide covering:
- Core API structure and namespaces
- Critical issues and their solutions
- Modern API patterns (2020+)
- Feature implementation (sketches, extrudes, chamfers, fillets)
- Testing and debugging techniques
- Quick reference for common errors

## 🔧 Key Discoveries

### Critical Fixes Implemented
1. **Dry-run mode resolution** - FusionBackendWithContext override
2. **Modern chamfer API** - createInput2() method
3. **Unit conversion bug** - Fixed double mm→cm conversion
4. **IR structure compatibility** - CSL v1.3 format handling
5. **Edge selection strategies** - Avoid corner conflicts

## 🚀 Quick Start for Agents

If you're an AI agent working on Fusion 360 integration:

1. **Read the API Guide first**: [FUSION_360_API_GUIDE.md](./FUSION_360_API_GUIDE.md)
2. **Check utility scripts**:
   - `verify_addin_status.py` - Check add-in status
   - `clear_design.py` - Clear Fusion design
   - `test_chamfer_only.py` - Test chamfer features
3. **Use the deployment script**: `deploy_triple_lindy.sh`

## ⚠️ Common Pitfalls

- Fusion API uses **centimeters** internally (not mm)
- Add-ins cache Python modules (requires force reload)
- Chamfer/fillet all edges causes corner conflicts
- CSL v1.3 nests features in root object
- `createInput()` is deprecated for chamfers (use `createInput2()`)

## 📖 External Resources

- [Official Fusion 360 API Documentation](https://help.autodesk.com/view/fusion360/ENU/)
- [API Reference](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/API_intro.htm)

## 🔄 Version Control

All fixes have been tested and committed:
- Commit: `434f070` - Fix CSL backend Fusion 360 integration
- Date: 2024-12-30
- Status: Fully functional chamfer and fillet features

---

**For detailed implementation guidance, always refer to [FUSION_360_API_GUIDE.md](./FUSION_360_API_GUIDE.md)**
