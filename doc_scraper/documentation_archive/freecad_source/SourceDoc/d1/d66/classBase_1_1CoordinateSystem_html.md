---
url: https://freecad.github.io/SourceDoc/d1/d66/classBase_1_1CoordinateSystem.html
scraped_at: 2025-09-08T15:15:59.773127
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [CoordinateSystem](../../d1/d66/classBase_1_1CoordinateSystem.html)

[List of all members](../../d6/d06/classBase_1_1CoordinateSystem-members.html) | Public Member Functions

Base::CoordinateSystem Class Reference

Describes a right-handed coordinate system in 3D space.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#details)

`#include <CoordinateSystem.h>`

##  Public Member Functions  
  
---  
|
[CoordinateSystem](../../d1/d66/classBase_1_1CoordinateSystem.html#a9766023795a2cac640751f0b9688cc50)
()  
| Construct a default coordinate system with position in (0,0,0), with X axis
(1,0,0), with Y axis (0,1,0) and Z axis (0,0,1)
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#a9766023795a2cac640751f0b9688cc50)  
  
[Placement](../../d1/d10/classBase_1_1Placement.html) | [displacement](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970) (const [CoordinateSystem](../../d1/d66/classBase_1_1CoordinateSystem.html) &cs) const  
| This computes the displacement from this coordinate system to the given
coordinate system _cs_.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970)  
  
const [Axis](../../d5/d61/classBase_1_1Axis.html) & | [getAxis](../../d1/d66/classBase_1_1CoordinateSystem.html#a14b60fc3ef1276a05610aabf2fdaf7ff) () const  
const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | [getPosition](../../d1/d66/classBase_1_1CoordinateSystem.html#a108f999612bca7e5d1801c50f2b43ca1) () const  
const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | [getXDirection](../../d1/d66/classBase_1_1CoordinateSystem.html#a5411b47f44226b6b0c9b273ebb12af62) () const  
const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | [getYDirection](../../d1/d66/classBase_1_1CoordinateSystem.html#ac5333856ee66349124c9a9ad10767113) () const  
const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | [getZDirection](../../d1/d66/classBase_1_1CoordinateSystem.html#a3b7f6d8490f9655c7926da54ce24d75e) () const  
void | [setAxes](../../d1/d66/classBase_1_1CoordinateSystem.html#aa739d8948fc7bc060cd5fdbc22f90d93) (const [Axis](../../d5/d61/classBase_1_1Axis.html) &, const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &xd)  
| Sets the main axis.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#aa739d8948fc7bc060cd5fdbc22f90d93)  
  
void | [setAxes](../../d1/d66/classBase_1_1CoordinateSystem.html#a006615426d148976eccccb6678e528b7) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &n, const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &xd)  
| Sets the main axis.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#a006615426d148976eccccb6678e528b7)  
  
void | [setAxis](../../d1/d66/classBase_1_1CoordinateSystem.html#a4a3c51368ce5415605774a396139b8f0) (const [Axis](../../d5/d61/classBase_1_1Axis.html) &v)  
| Sets the main axis.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#a4a3c51368ce5415605774a396139b8f0)  
  
void | [setPlacement](../../d1/d66/classBase_1_1CoordinateSystem.html#aab4206e93f3d31f3e8db6fc5aab88132) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &p)  
| Set the placement _p_ to the coordinate system.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#aab4206e93f3d31f3e8db6fc5aab88132)  
  
void | [setPosition](../../d1/d66/classBase_1_1CoordinateSystem.html#a5c5d9569aa680aacd7d8a38bcfb20d44) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &p)  
void | [setXDirection](../../d1/d66/classBase_1_1CoordinateSystem.html#a7f2a242ff6094d1743686222ed37192d) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &)  
| The passed vector must not be parallel to the main axis.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#a7f2a242ff6094d1743686222ed37192d)  
  
void | [setYDirection](../../d1/d66/classBase_1_1CoordinateSystem.html#ad0bcb826af0de6e8e256cae84dccbd26) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &)  
| The passed vector must not be parallel to the main axis.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#ad0bcb826af0de6e8e256cae84dccbd26)  
  
void | [setZDirection](../../d1/d66/classBase_1_1CoordinateSystem.html#a4ba812b2a2c9a9446afd938c8672c97c) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &)  
| Sets the main axis.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#a4ba812b2a2c9a9446afd938c8672c97c)  
  
void | [transform](../../d1/d66/classBase_1_1CoordinateSystem.html#a984ab79fb043dbec652ab6fb372bf4ad) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &p)  
| Apply the placement _p_ to the coordinate system.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#a984ab79fb043dbec652ab6fb372bf4ad)  
  
void | [transform](../../d1/d66/classBase_1_1CoordinateSystem.html#a657dcb4562b4fc19a0db0f2724b7f31d) (const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &r)  
| Apply the rotation _r_ to the coordinate system.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#a657dcb4562b4fc19a0db0f2724b7f31d)  
  
void | [transformTo](../../d1/d66/classBase_1_1CoordinateSystem.html#a558771f4a8922fe4ae72c200222de704) ([Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &p)  
| Transform the point _p_ to be in this coordinate system.
[More...](../../d1/d66/classBase_1_1CoordinateSystem.html#a558771f4a8922fe4ae72c200222de704)  
  
|
[~CoordinateSystem](../../d1/d66/classBase_1_1CoordinateSystem.html#a00742877a364fbc15b69aab14196f40e)
()  
  
## Detailed Description

Describes a right-handed coordinate system in 3D space.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ CoordinateSystem()

CoordinateSystem::CoordinateSystem  | ( | | ) |   
---|---|---|---|---  
  
Construct a default coordinate system with position in (0,0,0), with X axis
(1,0,0), with Y axis (0,1,0) and Z axis (0,0,1)

## ◆ ~CoordinateSystem()

CoordinateSystem::~CoordinateSystem  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ displacement()

[Placement](../../d1/d10/classBase_1_1Placement.html) CoordinateSystem::displacement  | ( | const [CoordinateSystem](../../d1/d66/classBase_1_1CoordinateSystem.html) & | _cs_| ) |  const  
---|---|---|---|---|---  
  
This computes the displacement from this coordinate system to the given
coordinate system _cs_.

References
[Base::Axis::getBase()](../../d5/d61/classBase_1_1Axis.html#a62b47dae4e268abd7864512238e9c99a),
[Base::Axis::getDirection()](../../d5/d61/classBase_1_1Axis.html#a6308021e5e03eb134158c93ab63b6a67),
[getPosition()](../../d1/d66/classBase_1_1CoordinateSystem.html#a108f999612bca7e5d1801c50f2b43ca1),
[getXDirection()](../../d1/d66/classBase_1_1CoordinateSystem.html#a5411b47f44226b6b0c9b273ebb12af62),
[getZDirection()](../../d1/d66/classBase_1_1CoordinateSystem.html#a3b7f6d8490f9655c7926da54ce24d75e),
[Base::Rotation::multVec()](../../d4/d18/classBase_1_1Rotation.html#a3cdb5a5eb357dd8a1c974f7374fe4a87),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[draftguitools.gui_stretch.Stretch::doStretch()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#ad50fddc20a1db1ac28f2b7dabd455dfc).

## ◆ getAxis()

const [Axis](../../d5/d61/classBase_1_1Axis.html) & Base::CoordinateSystem::getAxis  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getPosition()

const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & Base::CoordinateSystem::getPosition  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[displacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970).

## ◆ getXDirection()

const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & Base::CoordinateSystem::getXDirection  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[displacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970).

## ◆ getYDirection()

const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & Base::CoordinateSystem::getYDirection  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getZDirection()

const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & Base::CoordinateSystem::getZDirection  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[displacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970).

## ◆ setAxes() [1/2]

void CoordinateSystem::setAxes  | ( | const [Axis](../../d5/d61/classBase_1_1Axis.html) & | _v_ ,   
---|---|---|---  
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _xd_  
| ) | |   
  
Sets the main axis.

X and Y dir are adjusted accordingly. The main axis must not be parallel to
_xd_

References [Base::Vector3< double
>::epsilon()](../../d1/d13/classBase_1_1Vector3.html#afc0aba7a73e8528bb4a5ffa9d7c1429a),
[Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[Base::Axis::setBase()](../../d5/d61/classBase_1_1Axis.html#aee269e870703d1ba8e019352cd1ef446),
[Base::Axis::setDirection()](../../d5/d61/classBase_1_1Axis.html#a1541dfba8e577785325efffbe5c6d01b),
and [Base::Vector3< _Precision
>::Sqr()](../../d1/d13/classBase_1_1Vector3.html#a80a17d5af270b4bbb5b85c9ca9caa1e8).

Referenced by
[setAxis()](../../d1/d66/classBase_1_1CoordinateSystem.html#a4a3c51368ce5415605774a396139b8f0),
and
[setZDirection()](../../d1/d66/classBase_1_1CoordinateSystem.html#a4ba812b2a2c9a9446afd938c8672c97c).

## ◆ setAxes() [2/2]

void CoordinateSystem::setAxes  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _n_ ,   
---|---|---|---  
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _xd_  
| ) | |   
  
Sets the main axis.

X and Y dir are adjusted accordingly. The main axis _n_ must not be parallel
to _xd_

References [Base::Vector3< double
>::epsilon()](../../d1/d13/classBase_1_1Vector3.html#afc0aba7a73e8528bb4a5ffa9d7c1429a),
[Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[Base::Axis::setDirection()](../../d5/d61/classBase_1_1Axis.html#a1541dfba8e577785325efffbe5c6d01b),
and [Base::Vector3< _Precision
>::Sqr()](../../d1/d13/classBase_1_1Vector3.html#a80a17d5af270b4bbb5b85c9ca9caa1e8).

## ◆ setAxis()

void CoordinateSystem::setAxis  | ( | const [Axis](../../d5/d61/classBase_1_1Axis.html) & | _v_| ) |   
---|---|---|---|---|---  
  
Sets the main axis.

X and Y dir are adjusted accordingly. The main axis _v_ must not be parallel
to the X axis

References
[setAxes()](../../d1/d66/classBase_1_1CoordinateSystem.html#aa739d8948fc7bc060cd5fdbc22f90d93).

## ◆ setPlacement()

void CoordinateSystem::setPlacement  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _p_| ) |   
---|---|---|---|---|---  
  
Set the placement _p_ to the coordinate system.

References
[Base::Axis::setBase()](../../d5/d61/classBase_1_1Axis.html#aee269e870703d1ba8e019352cd1ef446),
and
[Base::Axis::setDirection()](../../d5/d61/classBase_1_1Axis.html#a1541dfba8e577785325efffbe5c6d01b).

## ◆ setPosition()

void Base::CoordinateSystem::setPosition  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _p_| ) |   
---|---|---|---|---|---  
  
## ◆ setXDirection()

void CoordinateSystem::setXDirection  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _dir_| ) |   
---|---|---|---|---|---  
  
The passed vector must not be parallel to the main axis.

References [Base::Vector3< double
>::epsilon()](../../d1/d13/classBase_1_1Vector3.html#afc0aba7a73e8528bb4a5ffa9d7c1429a),
[Base::Axis::getDirection()](../../d5/d61/classBase_1_1Axis.html#a6308021e5e03eb134158c93ab63b6a67),
[Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
and [Base::Vector3< _Precision
>::Sqr()](../../d1/d13/classBase_1_1Vector3.html#a80a17d5af270b4bbb5b85c9ca9caa1e8).

## ◆ setYDirection()

void CoordinateSystem::setYDirection  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _dir_| ) |   
---|---|---|---|---|---  
  
The passed vector must not be parallel to the main axis.

References [Base::Vector3< double
>::epsilon()](../../d1/d13/classBase_1_1Vector3.html#afc0aba7a73e8528bb4a5ffa9d7c1429a),
[Base::Axis::getDirection()](../../d5/d61/classBase_1_1Axis.html#a6308021e5e03eb134158c93ab63b6a67),
[Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
and [Base::Vector3< _Precision
>::Sqr()](../../d1/d13/classBase_1_1Vector3.html#a80a17d5af270b4bbb5b85c9ca9caa1e8).

## ◆ setZDirection()

void CoordinateSystem::setZDirection  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _dir_| ) |   
---|---|---|---|---|---  
  
Sets the main axis.

X and Y dir are adjusted accordingly. The main axis must not be parallel to
the X axis

References
[setAxes()](../../d1/d66/classBase_1_1CoordinateSystem.html#aa739d8948fc7bc060cd5fdbc22f90d93).

## ◆ transform() [1/2]

void CoordinateSystem::transform  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _p_| ) |   
---|---|---|---|---|---  
  
Apply the placement _p_ to the coordinate system.

Referenced by
[importSVG.svgHandler::applyTrans()](../../dc/d45/classimportSVG_1_1svgHandler.html#a38ca516f06b0765c43bc94623af7b74c),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[importSVG.svgHandler::endElement()](../../dc/d45/classimportSVG_1_1svgHandler.html#a1bd77a0a99233ef4a9075eefc2da04f3),
[ArchSite.Compass::locate()](../../d9/d61/classArchSite_1_1Compass.html#ab97b56e1db99fff1ca2d03d1819a0da5),
[ArchSite.Compass::rotate()](../../d9/d61/classArchSite_1_1Compass.html#a265d59029ed54f579ec07d75beadffc0),
and
[ArchSite.Compass::scale()](../../d9/d61/classArchSite_1_1Compass.html#a6bd34d985770e9ec9970bee17031d98b).

## ◆ transform() [2/2]

void CoordinateSystem::transform  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _r_| ) |   
---|---|---|---|---|---  
  
Apply the rotation _r_ to the coordinate system.

References
[Base::Axis::getDirection()](../../d5/d61/classBase_1_1Axis.html#a6308021e5e03eb134158c93ab63b6a67),
and
[Base::Axis::setDirection()](../../d5/d61/classBase_1_1Axis.html#a1541dfba8e577785325efffbe5c6d01b).

Referenced by
[importSVG.svgHandler::applyTrans()](../../dc/d45/classimportSVG_1_1svgHandler.html#a38ca516f06b0765c43bc94623af7b74c),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[importSVG.svgHandler::endElement()](../../dc/d45/classimportSVG_1_1svgHandler.html#a1bd77a0a99233ef4a9075eefc2da04f3),
[ArchSite.Compass::locate()](../../d9/d61/classArchSite_1_1Compass.html#ab97b56e1db99fff1ca2d03d1819a0da5),
[ArchSite.Compass::rotate()](../../d9/d61/classArchSite_1_1Compass.html#a265d59029ed54f579ec07d75beadffc0),
and
[ArchSite.Compass::scale()](../../d9/d61/classArchSite_1_1Compass.html#a6bd34d985770e9ec9970bee17031d98b).

## ◆ transformTo()

void CoordinateSystem::transformTo  | ( | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _p_| ) |   
---|---|---|---|---|---  
  
Transform the point _p_ to be in this coordinate system.

References
[Base::Axis::getBase()](../../d5/d61/classBase_1_1Axis.html#a62b47dae4e268abd7864512238e9c99a).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/CoordinateSystem.h
  * FreeCAD/src/Base/CoordinateSystem.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

