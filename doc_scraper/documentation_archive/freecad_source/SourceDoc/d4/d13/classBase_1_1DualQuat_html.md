---
url: https://freecad.github.io/SourceDoc/d4/d13/classBase_1_1DualQuat.html
scraped_at: 2025-09-08T15:16:02.791804
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [DualQuat](../../d4/d13/classBase_1_1DualQuat.html)

[List of all members](../../df/d1a/classBase_1_1DualQuat-members.html) | Public Member Functions | Static Public Member Functions | Public Attributes

Base::DualQuat Class Reference

The [DualQuat](../../d4/d13/classBase_1_1DualQuat.html "The DualQuat class
represents a dual quaternion, as a quaternion of dual number components.")
class represents a dual quaternion, as a quaternion of dual number components.
[More...](../../d4/d13/classBase_1_1DualQuat.html#details)

`#include <DualQuaternion.h>`

##  Public Member Functions  
  
---  
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | [conj](../../d4/d13/classBase_1_1DualQuat.html#a7c0cd20685b8952925c16d40f15020c1) () const  
| conjugate
[More...](../../d4/d13/classBase_1_1DualQuat.html#a7c0cd20685b8952925c16d40f15020c1)  
  
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | [dual](../../d4/d13/classBase_1_1DualQuat.html#a224c123d9815f260a401c3b04484d552) () const  
| return a real-only quaternion made from dual part of this quaternion.
[More...](../../d4/d13/classBase_1_1DualQuat.html#a224c123d9815f260a401c3b04484d552)  
  
|
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html#ad774d86ebeca5ca3c3f58e84d569f2bf)
()  
| default constructor: init with zeros
[More...](../../d4/d13/classBase_1_1DualQuat.html#ad774d86ebeca5ca3c3f58e84d569f2bf)  
  
|
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html#a95f3b6bb5074451c395580255dbb46cd)
(double
[x](../../d4/d13/classBase_1_1DualQuat.html#af0a8c368d6987ed9fc05dd1b594da78f),
double
[y](../../d4/d13/classBase_1_1DualQuat.html#a4fb8157ef0805ba6011343b2a0c7eb7c),
double
[z](../../d4/d13/classBase_1_1DualQuat.html#a2299a66bb636cd1ec8f243e00ea97015),
double
[w](../../d4/d13/classBase_1_1DualQuat.html#ae9de981d482e291defa8eee4cf6487f1))  
|
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html#ad3252d9ac872f1d100ab4587c2459d05)
(double
[x](../../d4/d13/classBase_1_1DualQuat.html#af0a8c368d6987ed9fc05dd1b594da78f),
double
[y](../../d4/d13/classBase_1_1DualQuat.html#a4fb8157ef0805ba6011343b2a0c7eb7c),
double
[z](../../d4/d13/classBase_1_1DualQuat.html#a2299a66bb636cd1ec8f243e00ea97015),
double
[w](../../d4/d13/classBase_1_1DualQuat.html#ae9de981d482e291defa8eee4cf6487f1),
double dx, double dy, double dz, double dw)  
|
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html#a9368c9d9ad2deef202fbd31774f51824)
([DualNumber](../../db/d4b/classBase_1_1DualNumber.html)
[x](../../d4/d13/classBase_1_1DualQuat.html#af0a8c368d6987ed9fc05dd1b594da78f),
[DualNumber](../../db/d4b/classBase_1_1DualNumber.html)
[y](../../d4/d13/classBase_1_1DualQuat.html#a4fb8157ef0805ba6011343b2a0c7eb7c),
[DualNumber](../../db/d4b/classBase_1_1DualNumber.html)
[z](../../d4/d13/classBase_1_1DualQuat.html#a2299a66bb636cd1ec8f243e00ea97015),
[DualNumber](../../db/d4b/classBase_1_1DualNumber.html)
[w](../../d4/d13/classBase_1_1DualQuat.html#ae9de981d482e291defa8eee4cf6487f1))  
|
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html#ab1eceeb6f38d30713b5d129ed8e3f41e)
([DualQuat](../../d4/d13/classBase_1_1DualQuat.html) re,
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) du)  
| Builds a dual quaternion from real and dual parts provided as pure real
quaternions.
[More...](../../d4/d13/classBase_1_1DualQuat.html#ab1eceeb6f38d30713b5d129ed8e3f41e)  
  
double | [length](../../d4/d13/classBase_1_1DualQuat.html#a2159882655ac1ce9747da227e0ce40c0) () const  
| magnitude of the quaternion
[More...](../../d4/d13/classBase_1_1DualQuat.html#a2159882655ac1ce9747da227e0ce40c0)  
  
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | [operator-](../../d4/d13/classBase_1_1DualQuat.html#af2b8fdfb2ee513b898d2dae2242b45b9) () const  
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | [pow](../../d4/d13/classBase_1_1DualQuat.html#a6744d98c253f5310ed8f421c54286ea4) (double t, [bool](../../d9/db9/classbool.html) shorten=true) const  
| ScLERP. t=0.0 returns identity, t=1.0 returns this. t can also be outside of
0..1 bounds.
[More...](../../d4/d13/classBase_1_1DualQuat.html#a6744d98c253f5310ed8f421c54286ea4)  
  
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | [real](../../d4/d13/classBase_1_1DualQuat.html#a27d1d5fb87cb51eff9fcbc1a30426058) () const  
| return a copy with dual part zeroed out
[More...](../../d4/d13/classBase_1_1DualQuat.html#a27d1d5fb87cb51eff9fcbc1a30426058)  
  
double | [theta](../../d4/d13/classBase_1_1DualQuat.html#afaacd34fe231ad51c33082007bd96d29) () const  
| angle of rotation represented by this quaternion, in radians
[More...](../../d4/d13/classBase_1_1DualQuat.html#afaacd34fe231ad51c33082007bd96d29)  
  
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | [vec](../../d4/d13/classBase_1_1DualQuat.html#a89ff334d37263baf291c9a6427a46a3e) () const  
| return vector part (with scalar part zeroed out)
[More...](../../d4/d13/classBase_1_1DualQuat.html#a89ff334d37263baf291c9a6427a46a3e)  
  
  
##  Static Public Member Functions  
  
---  
static double | [dot](../../d4/d13/classBase_1_1DualQuat.html#a0c22769417ed2aa342f20281cf3fa570) ([DualQuat](../../d4/d13/classBase_1_1DualQuat.html) a, [DualQuat](../../d4/d13/classBase_1_1DualQuat.html) b)  
| dot product between real (rotation) parts of two dual quaternions (to
determine if one of them should be negated for shortest interpolation)
[More...](../../d4/d13/classBase_1_1DualQuat.html#a0c22769417ed2aa342f20281cf3fa570)  
  
static [DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | [identity](../../d4/d13/classBase_1_1DualQuat.html#ae20d1b0e1817e4f3bd826d290d2b9cc9) ()  
| returns dual quaternion for identity placement
[More...](../../d4/d13/classBase_1_1DualQuat.html#ae20d1b0e1817e4f3bd826d290d2b9cc9)  
  
  
##  Public Attributes  
  
---  
[DualNumber](../../db/d4b/classBase_1_1DualNumber.html) | [w](../../d4/d13/classBase_1_1DualQuat.html#ae9de981d482e291defa8eee4cf6487f1)  
[DualNumber](../../db/d4b/classBase_1_1DualNumber.html) | [x](../../d4/d13/classBase_1_1DualQuat.html#af0a8c368d6987ed9fc05dd1b594da78f)  
[DualNumber](../../db/d4b/classBase_1_1DualNumber.html) | [y](../../d4/d13/classBase_1_1DualQuat.html#a4fb8157ef0805ba6011343b2a0c7eb7c)  
[DualNumber](../../db/d4b/classBase_1_1DualNumber.html) | [z](../../d4/d13/classBase_1_1DualQuat.html#a2299a66bb636cd1ec8f243e00ea97015)  
  
## Detailed Description

The [DualQuat](../../d4/d13/classBase_1_1DualQuat.html "The DualQuat class
represents a dual quaternion, as a quaternion of dual number components.")
class represents a dual quaternion, as a quaternion of dual number components.

Dual quaternions are useful for placement interpolation, see pow method.

[Rotation](../../d4/d18/classBase_1_1Rotation.html) is stored as non-dual part
of DualQ. Translation is encoded into dual part of
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html "The DualQuat class
represents a dual quaternion, as a quaternion of dual number components."):
[DualQuat.dual()](../../d4/d13/classBase_1_1DualQuat.html#a224c123d9815f260a401c3b04484d552
"return a real-only quaternion made from dual part of this quaternion.") = 0.5
* t * r, where t is quaternion with x,y,z of translation and w of 0, and r is
the rotation quaternion.

## Constructor & Destructor Documentation

## ◆ DualQuat() [1/5]

Base::DualQuat::DualQuat  | ( | | ) |   
---|---|---|---|---  
  
default constructor: init with zeros

## ◆ DualQuat() [2/5]

Base::DualQuat::DualQuat  | ( | [DualNumber](../../db/d4b/classBase_1_1DualNumber.html) | _x_ ,   
---|---|---|---  
|  | [DualNumber](../../db/d4b/classBase_1_1DualNumber.html) | _y_ ,   
|  | [DualNumber](../../db/d4b/classBase_1_1DualNumber.html) | _z_ ,   
|  | [DualNumber](../../db/d4b/classBase_1_1DualNumber.html) | _w_  
| ) | |   
  
## ◆ DualQuat() [3/5]

Base::DualQuat::DualQuat  | ( | double  | _x_ ,   
---|---|---|---  
|  | double  | _y_ ,   
|  | double  | _z_ ,   
|  | double  | _w_ ,   
|  | double  | _dx_ ,   
|  | double  | _dy_ ,   
|  | double  | _dz_ ,   
|  | double  | _dw_  
| ) | |   
  
## ◆ DualQuat() [4/5]

Base::DualQuat::DualQuat  | ( | double  | _x_ ,   
---|---|---|---  
|  | double  | _y_ ,   
|  | double  | _z_ ,   
|  | double  | _w_  
| ) | |   
  
## ◆ DualQuat() [5/5]

Base::DualQuat::DualQuat  | ( | [Base::DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | _re_ ,   
---|---|---|---  
|  | [Base::DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | _du_  
| ) | |   
  
Builds a dual quaternion from real and dual parts provided as pure real
quaternions.

References
[dual()](../../d4/d13/classBase_1_1DualQuat.html#a224c123d9815f260a401c3b04484d552),
and
[length()](../../d4/d13/classBase_1_1DualQuat.html#a2159882655ac1ce9747da227e0ce40c0).

## Member Function Documentation

## ◆ conj()

[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) Base::DualQuat::conj  | ( | | ) |  const  
---|---|---|---|---  
  
conjugate

Referenced by
[Base::Placement::fromDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f).

## ◆ dot()

| double Base::DualQuat::dot  | ( | [Base::DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | _a_ ,   
---|---|---|---  
|  | [Base::DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | _b_  
| ) | |   
static  
  
dot product between real (rotation) parts of two dual quaternions (to
determine if one of them should be negated for shortest interpolation)

## ◆ dual()

[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) Base::DualQuat::dual  | ( | | ) |  const  
---|---|---|---|---  
  
return a real-only quaternion made from dual part of this quaternion.

Referenced by
[DualQuat()](../../d4/d13/classBase_1_1DualQuat.html#ab1eceeb6f38d30713b5d129ed8e3f41e),
[Base::Placement::fromDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f),
and
[pow()](../../d4/d13/classBase_1_1DualQuat.html#a6744d98c253f5310ed8f421c54286ea4).

## ◆ identity()

| static [DualQuat](../../d4/d13/classBase_1_1DualQuat.html) Base::DualQuat::identity  | ( | | ) |   
---|---|---|---|---  
static  
  
returns dual quaternion for identity placement

## ◆ length()

double Base::DualQuat::length  | ( | | ) |  const  
---|---|---|---|---  
  
magnitude of the quaternion

Referenced by
[DualQuat()](../../d4/d13/classBase_1_1DualQuat.html#ab1eceeb6f38d30713b5d129ed8e3f41e),
[PathScripts.PathStock.StockFromBase::execute()](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#a9fa59e6edf99801ba45c953b49561ae2),
[PathScripts.PathDressupDogbone.ObjectDressup::execute()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a039b27cd647d900f54eb26078667be9b),
[PathScripts.PathFeatureExtensions.Extension::getSubLink()](../../d7/d86/classPathScripts_1_1PathFeatureExtensions_1_1Extension.html#a39e2f64b82ca08c5145654ac03f10cd8),
[PathScripts.PathFeatureExtensions.Extension::getWire()](../../d7/d86/classPathScripts_1_1PathFeatureExtensions_1_1Extension.html#a97954317b571ddd2f898d82a86db87ea),
and
[Mod.PartDesign.Scripts.FilletArc.Vector::norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20).

## ◆ operator-()

[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) Base::DualQuat::operator-  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ pow()

[Base::DualQuat](../../d4/d13/classBase_1_1DualQuat.html) Base::DualQuat::pow  | ( | double  | _t_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _shorten_ = `true`  
| ) | |  const  
  
ScLERP. t=0.0 returns identity, t=1.0 returns this. t can also be outside of
0..1 bounds.

References
[Base::DualNumber::du](../../db/d4b/classBase_1_1DualNumber.html#acc3a34e051cc668a60b0bca9d3f0387b),
[dual()](../../d4/d13/classBase_1_1DualQuat.html#a224c123d9815f260a401c3b04484d552),
[real()](../../d4/d13/classBase_1_1DualQuat.html#a27d1d5fb87cb51eff9fcbc1a30426058),
[theta()](../../d4/d13/classBase_1_1DualQuat.html#afaacd34fe231ad51c33082007bd96d29),
[vec()](../../d4/d13/classBase_1_1DualQuat.html#a89ff334d37263baf291c9a6427a46a3e),
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c),
and
[w](../../d4/d13/classBase_1_1DualQuat.html#ae9de981d482e291defa8eee4cf6487f1).

## ◆ real()

[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) Base::DualQuat::real  | ( | | ) |  const  
---|---|---|---|---  
  
return a copy with dual part zeroed out

Referenced by
[Base::Placement::fromDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f),
and
[pow()](../../d4/d13/classBase_1_1DualQuat.html#a6744d98c253f5310ed8f421c54286ea4).

## ◆ theta()

double Base::DualQuat::theta  | ( | | ) |  const  
---|---|---|---|---  
  
angle of rotation represented by this quaternion, in radians

References
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[Mod.PartDesign.fcgear.fcgear.FCWireBuilder::arc()](../../d6/d0e/classMod_1_1PartDesign_1_1fcgear_1_1fcgear_1_1FCWireBuilder.html#a23a65f6983a2fa28aac49668b782b19b),
[Mod.PartDesign.fcgear.svggear.SVGWireBuilder::arc()](../../d2/d6c/classMod_1_1PartDesign_1_1fcgear_1_1svggear_1_1SVGWireBuilder.html#ad4f4352ca80c25500b945c5e7932fecf),
[Mod.PartDesign.fcsprocket.fcsprocket.FCWireBuilder::arc()](../../d9/de8/classMod_1_1PartDesign_1_1fcsprocket_1_1fcsprocket_1_1FCWireBuilder.html#aa0fe071898e6dbe2daea20f4c5a38f1b),
[Mod.PartDesign.fcgear.fcgear.FCWireBuilder::curve()](../../d6/d0e/classMod_1_1PartDesign_1_1fcgear_1_1fcgear_1_1FCWireBuilder.html#ae927782fbe7d9185a5a8ccb8055a0331),
[Mod.PartDesign.fcgear.svggear.SVGWireBuilder::curve()](../../d2/d6c/classMod_1_1PartDesign_1_1fcgear_1_1svggear_1_1SVGWireBuilder.html#a0b5b80d45a1454dcfbeb4d096304ee8c),
[Mod.PartDesign.fcsprocket.fcsprocket.FCWireBuilder::curve()](../../d9/de8/classMod_1_1PartDesign_1_1fcsprocket_1_1fcsprocket_1_1FCWireBuilder.html#ab0dacd0e51c96c96ca587478c6e5def9),
[Mod.PartDesign.fcgear.fcgear.FCWireBuilder::line()](../../d6/d0e/classMod_1_1PartDesign_1_1fcgear_1_1fcgear_1_1FCWireBuilder.html#aa77dabed8ed68c6b1c21fbb8721bfa21),
[Mod.PartDesign.fcgear.svggear.SVGWireBuilder::line()](../../d2/d6c/classMod_1_1PartDesign_1_1fcgear_1_1svggear_1_1SVGWireBuilder.html#af6706636a7ff50d57c6cc9841bf6a85e),
[Mod.PartDesign.fcsprocket.fcsprocket.FCWireBuilder::line()](../../d9/de8/classMod_1_1PartDesign_1_1fcsprocket_1_1fcsprocket_1_1FCWireBuilder.html#a18dee1cb605b4acd0e3893fbba20f9cc),
[Mod.PartDesign.fcgear.svggear.SVGWireBuilder::move()](../../d2/d6c/classMod_1_1PartDesign_1_1fcgear_1_1svggear_1_1SVGWireBuilder.html#a342c4d964cc30d676cb9e54321bc05fa),
and
[pow()](../../d4/d13/classBase_1_1DualQuat.html#a6744d98c253f5310ed8f421c54286ea4).

## ◆ vec()

[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) Base::DualQuat::vec  | ( | | ) |  const  
---|---|---|---|---  
  
return vector part (with scalar part zeroed out)

Referenced by
[pow()](../../d4/d13/classBase_1_1DualQuat.html#a6744d98c253f5310ed8f421c54286ea4).

## Member Data Documentation

## ◆ w

[DualNumber](../../db/d4b/classBase_1_1DualNumber.html) Base::DualQuat::w  
---  
  
Referenced by
[Mod.PartDesign.WizardShaft.Shaft.Shaft::equilibrium()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#abf673f8921374b011ced4c4a770d44e6),
[Base::Placement::fromDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f),
[pow()](../../d4/d13/classBase_1_1DualQuat.html#a6744d98c253f5310ed8f421c54286ea4),
[Mod.PartDesign.WizardShaft.Shaft.Shaft::showDiagram()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#ac648180672c3434f2214d26ff3bd2cde),
and
[Base::Placement::toDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a700572ce02a191128a6c097d2212562d).

## ◆ x

[DualNumber](../../db/d4b/classBase_1_1DualNumber.html) Base::DualQuat::x  
---  
  
Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector::add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[DraftGui.DraftToolBar::changeXValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a2264e5b2058aeec75cb9044b36485378),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[PathScripts.PathInspect.GCodeEditorDialog::cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[Mod.PartDesign.Scripts.FilletArc.Vector::cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[PathScripts.PostUtils.GCodeEditorDialog::done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Mod.PartDesign.Scripts.FilletArc.Vector::dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[Base::Placement::fromDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f),
[Mod.PartDesign.Scripts.FilletArc.Vector::length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Mod.PartDesign.Scripts.FilletArc.Vector::mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector::norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[PathScripts.PathDressupHoldingTags.Tag::originAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aa1cbd48305f117e5197555822fd45f3f),
[DraftGui.DraftToolBar::pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[DraftGui.DraftToolBar::reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[Mod.PartDesign.Scripts.FilletArc.Vector::sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[Base::Placement::toDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a700572ce02a191128a6c097d2212562d),
[DraftGui.DraftToolBar::update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar::update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar::updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
[DraftGui.DraftToolBar::validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
and
[automotive_design.right_angular_wedge::wr1()](../../d4/df4/classautomotive__design_1_1right__angular__wedge.html#a08ba5a830562d7f45bb10fe924c7b534).

## ◆ y

[DualNumber](../../db/d4b/classBase_1_1DualNumber.html) Base::DualQuat::y  
---  
  
Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector::add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[DraftGui.DraftToolBar::changeYValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a245f69442c47aa69844d30313e68b2b7),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[PathScripts.PathInspect.GCodeEditorDialog::cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[Mod.PartDesign.Scripts.FilletArc.Vector::cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[PathScripts.PostUtils.GCodeEditorDialog::done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Mod.PartDesign.Scripts.FilletArc.Vector::dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[Base::Placement::fromDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f),
[Mod.PartDesign.Scripts.FilletArc.Vector::length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Mod.PartDesign.Scripts.FilletArc.Vector::mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector::norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[PathScripts.PathDressupHoldingTags.Tag::originAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aa1cbd48305f117e5197555822fd45f3f),
[DraftGui.DraftToolBar::pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[DraftGui.DraftToolBar::reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[Mod.PartDesign.Scripts.FilletArc.Vector::sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[Base::Placement::toDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a700572ce02a191128a6c097d2212562d),
[DraftGui.DraftToolBar::update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar::update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar::updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
and
[DraftGui.DraftToolBar::validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de).

## ◆ z

[DualNumber](../../db/d4b/classBase_1_1DualNumber.html) Base::DualQuat::z  
---  
  
Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector::add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[automotive_design.revolved_area_solid::axis_line()](../../d4/ded/classautomotive__design_1_1revolved__area__solid.html#ae7714359aef57b10dc9d110c4c95109c),
[automotive_design.surface_of_revolution::axis_line()](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#ac11430bfca20d807bd7fbb1de4555324),
[automotive_design.revolved_face_solid::axis_line()](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a88ba8cae1c9e693beda33bf96a0423ca),
[ifc4.ifcrevolvedareasolid::axisdirectioninxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a34e620e30709c7c4e2c619daa7704ece),
[ifc2x3.ifcsurfaceofrevolution::axisline()](../../db/d1b/classifc2x3_1_1ifcsurfaceofrevolution.html#a0689126db6a08f9f1183f65515b53370),
[ifc2x3.ifcrevolvedareasolid::axisline()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#ad7a180e86495ea93d5acb25ffcc33ffa),
[ifc4.ifcsurfaceofrevolution::axisline()](../../d4/de7/classifc4_1_1ifcsurfaceofrevolution.html#adf527bd278ddce78734fc2b01bec7b37),
[ifc4.ifcrevolvedareasolid::axisline()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a45efcb80c8963331649e13f991ec7534),
[PathScripts.PathDressupHoldingTags.Tag::bottom()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aaae502deebbb0cc7adf2f1dd338d9ac8),
[DraftGui.DraftToolBar::changeZValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a33ea2715914aa73b36107598fe5702c5),
[PathScripts.PathDressupTag.TagSolid::cloneAt()](../../d2/dc0/classPathScripts_1_1PathDressupTag_1_1TagSolid.html#a0da4c220cd1980731ce8fbb646cc8e13),
[PathScripts.PathDressupHoldingTags.Tag::createSolidsAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a2cb6cc02ae81caafbb137dfe20ebfdd8),
[Mod.PartDesign.Scripts.FilletArc.Vector::cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[Mod.PartDesign.Scripts.FilletArc.Vector::dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[Base::Placement::fromDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f),
[Mod.PartDesign.Scripts.FilletArc.Vector::length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Mod.PartDesign.Scripts.FilletArc.Vector::mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector::norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[DraftGui.DraftToolBar::pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[DraftGui.DraftToolBar::reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[importSH3D.SH3DHandler::startElement()](../../d8/de6/classimportSH3D_1_1SH3DHandler.html#a9a512563447c10428d4e0e65fbbc95f7),
[Mod.PartDesign.Scripts.FilletArc.Vector::sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[Base::Placement::toDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a700572ce02a191128a6c097d2212562d),
[PathScripts.PathDressupHoldingTags.Tag::top()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#abe7b229a9b4e1207f20627c3546cfe1c),
[DraftGui.DraftToolBar::update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar::update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar::updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
[DraftGui.DraftToolBar::validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
and
[ifc2x3.ifcrevolvedareasolid::wr32()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a2d005a905b9bcd1b1d7fc934f7085073).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/DualQuaternion.h
  * FreeCAD/src/Base/DualQuaternion.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

