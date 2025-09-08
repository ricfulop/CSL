---
url: https://freecad.github.io/SourceDoc/dd/d68/structClipperLib_1_1IntPoint.html
scraped_at: 2025-09-08T15:19:12.559772
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ClipperLib](../../df/db2/namespaceClipperLib.html)
  * [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html)

[List of all members](../../d9/da1/structClipperLib_1_1IntPoint-members.html) | Public Member Functions | Public Attributes | Friends

ClipperLib::IntPoint Struct Reference

`#include <clipper.hpp>`

##  Public Member Functions  
  
---  
|
[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html#a819e71f9269e99f151a3a99c4283cd43)
([cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
x=0,
[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
y=0)  
  
##  Public Attributes  
  
---  
[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | [X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6)  
[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | [Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425)  
  
##  Friends  
  
---  
[bool](../../d9/db9/classbool.html) | [operator!=](../../dd/d68/structClipperLib_1_1IntPoint.html#aa37b2afb6cbc44cb9cd13ecc009decfb) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &a, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &b)  
[bool](../../d9/db9/classbool.html) | [operator==](../../dd/d68/structClipperLib_1_1IntPoint.html#a6afef09ee09723a387e3046287e2635b) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &a, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &b)  
  
## Constructor & Destructor Documentation

## ◆ IntPoint()

ClipperLib::IntPoint::IntPoint  | ( | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _x_ = `0`,   
---|---|---|---  
|  | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _y_ = `0`  
| ) | |   
  
## Friends And Related Function Documentation

## ◆ operator!=

| [bool](../../d9/db9/classbool.html) operator!=  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _a_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _b_  
| ) | |   
friend  
  
## ◆ operator==

| [bool](../../d9/db9/classbool.html) operator==  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _a_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _b_  
| ) | |   
friend  
  
## Member Data Documentation

## ◆ X

[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
ClipperLib::IntPoint::X  
---  
  
Referenced by
[ClipperLib::ClipperOffset::AddPath()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a0cd68e3690072f510924a5b25291043b),
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[AdaptivePath::BoundBox::AddPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a47b23bb75413d049f127728ad178ea76),
[ClipperLib::Area()](../../df/db2/namespaceClipperLib.html#ae138536c4535e0a97e2e5787ae41bac3),
[AdaptivePath::BoundBox::BoundBox()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#abe92c0b8410f953628b1e2a3010af556),
[AdaptivePath::Circle2CircleIntersect()](../../d5/d7f/namespaceAdaptivePath.html#aa4cc9428e38c16e83c2a1a8dfa7259ba),
[ClipperLib::ClipperOffset::Clear()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#ab444433587b6a3f6c89655938d889c7d),
[ClipperLib::ClipperOffset::ClipperOffset()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a45b4750989901db0c3865c374abdfcdc),
[AdaptivePath::DirectionV()](../../d5/d7f/namespaceAdaptivePath.html#a6e0b5d3a809d33ef38b51885367e5805),
[ClipperLib::DistanceFromLineSqrd()](../../df/db2/namespaceClipperLib.html#ac57923512d57903663fed9778585ca18),
[AdaptivePath::DistancePointToLineSegSquared()](../../d5/d7f/namespaceAdaptivePath.html#aba8ae65365f5e2bbb8523972dcfd5fb2),
[AdaptivePath::DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1),
[ClipperLib::DistanceSqrd()](../../df/db2/namespaceClipperLib.html#ab3ea29b9e123ab56ede03ce6946c9e7d),
[ClipperLib::E2InsertsBeforeE1()](../../df/db2/namespaceClipperLib.html#ae002e65db41b2e12c6a29b6c53d95e3d),
[ClipperLib::FindNextLocMin()](../../df/db2/namespaceClipperLib.html#a6c2a946a9f927bfd364c95b561d4191c),
[ClipperLib::GetBottomPt()](../../df/db2/namespaceClipperLib.html#ad7895448ee9b2d2499a57addd49b2192),
[AdaptivePath::ClearedArea::GetBoundedClearedAreaClipped()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a396af78fc129b33fe0c3730caadc9503),
[AdaptivePath::ClearedArea::GetBoundedClearedPaths()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a68e1a211be4683c860dba6ec244abc36),
[AdaptivePath::EngagePoint::getCurrentDir()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a64238fcdbfa9f4bf6a2fc4f000405339),
[AdaptivePath::EngagePoint::getCurrentPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a4a25dac76882d1527f13a9f4683024a2),
[ClipperLib::GetDx()](../../df/db2/namespaceClipperLib.html#adb890cca4fa2a71731b91968cf4ff49d),
[ClipperLib::GetHorzDirection()](../../df/db2/namespaceClipperLib.html#a3a6a98076d47afe4c2e033833ae89bf5),
[ClipperLib::GetLowermostRec()](../../df/db2/namespaceClipperLib.html#a3b36c0993f124dd3235ed1dd468d4192),
[ClipperLib::GetOverlapSegment()](../../df/db2/namespaceClipperLib.html#a8817de6dc5a080ead872b1373074c07f),
[PathMachineState.MachineState::getPosition()](../../d4/d53/classPathMachineState_1_1MachineState.html#a2fada51e2c794c0b9c3a81bf2b7fec7d),
[PathMachineState.MachineState::getState()](../../d4/d53/classPathMachineState_1_1MachineState.html#a4a75b28afb6ba79346109b31fa976aec),
[ClipperLib::GetUnitNormal()](../../df/db2/namespaceClipperLib.html#a5a62f42148b8b9991da9cfe8cb9cb065),
[AdaptivePath::IntersectionPoint()](../../d5/d7f/namespaceAdaptivePath.html#ac652f5c393ef400162a3673caf7da369),
[ClipperLib::IntersectPoint()](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a),
[ClipperLib::JoinHorz()](../../df/db2/namespaceClipperLib.html#acd026a4d43018ae65b8d253fbf44b680),
[AdaptivePath::Line2CircleIntersect()](../../d5/d7f/namespaceAdaptivePath.html#a162b44dbc1289576521d7d3e3084562f),
[ClipperLib::PointInPolygon()](../../df/db2/namespaceClipperLib.html#ac7314f2a1f45c627bac20e9ba2a68212),
[ClipperLib::PointsAreClose()](../../df/db2/namespaceClipperLib.html#a52757887bc031d0052ae95dccb83cd2c),
[AdaptivePath::PointSideOfLine()](../../d5/d7f/namespaceAdaptivePath.html#a443621d89fda38d492b838c7914e3dc7),
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0),
[ClipperLib::Pt2IsBetweenPt1AndPt3()](../../df/db2/namespaceClipperLib.html#a0a448254ee6419dfde0a539080502d88),
[ClipperLib::RangeTest()](../../df/db2/namespaceClipperLib.html#add09a980dfa1da81e1693a55cd912908),
[AdaptivePath::BoundBox::SetFirstPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a33a37a0cdf8b16dbd473f595ba0984eb),
[AdaptivePath::SetSegmentLength()](../../d5/d7f/namespaceAdaptivePath.html#aace2cca9424c6fa5bb3f7302878b0a29),
[ClipperLib::SlopesEqual()](../../df/db2/namespaceClipperLib.html#a052da0ab7e1690b61e36e007769df9f8),
[ClipperLib::SlopesNearCollinear()](../../df/db2/namespaceClipperLib.html#a6a8d461810e4bcb5c67bf8e3026839b6),
[AdaptivePath::SmoothPaths()](../../d5/d7f/namespaceAdaptivePath.html#a08e27d008713754b5d5efca8ef13b962),
[ClipperLib::TopX()](../../df/db2/namespaceClipperLib.html#a63e0b77cf7232cbd4f9909b25bd300be),
and
[ClipperLib::TranslatePath()](../../df/db2/namespaceClipperLib.html#a3c34a4a0ea91a10f729e5ceb6cc33714).

## ◆ Y

[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
ClipperLib::IntPoint::Y  
---  
  
Referenced by
[ClipperLib::ClipperOffset::AddPath()](../../d6/d79/classClipperLib_1_1ClipperOffset.html#a0cd68e3690072f510924a5b25291043b),
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[AdaptivePath::BoundBox::AddPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a47b23bb75413d049f127728ad178ea76),
[ClipperLib::Area()](../../df/db2/namespaceClipperLib.html#ae138536c4535e0a97e2e5787ae41bac3),
[AdaptivePath::BoundBox::BoundBox()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#abe92c0b8410f953628b1e2a3010af556),
[AdaptivePath::Circle2CircleIntersect()](../../d5/d7f/namespaceAdaptivePath.html#aa4cc9428e38c16e83c2a1a8dfa7259ba),
[AdaptivePath::DirectionV()](../../d5/d7f/namespaceAdaptivePath.html#a6e0b5d3a809d33ef38b51885367e5805),
[ClipperLib::DistanceFromLineSqrd()](../../df/db2/namespaceClipperLib.html#ac57923512d57903663fed9778585ca18),
[AdaptivePath::DistancePointToLineSegSquared()](../../d5/d7f/namespaceAdaptivePath.html#aba8ae65365f5e2bbb8523972dcfd5fb2),
[AdaptivePath::DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1),
[ClipperLib::DistanceSqrd()](../../df/db2/namespaceClipperLib.html#ab3ea29b9e123ab56ede03ce6946c9e7d),
[ClipperLib::E2InsertsBeforeE1()](../../df/db2/namespaceClipperLib.html#ae002e65db41b2e12c6a29b6c53d95e3d),
[ClipperLib::FindNextLocMin()](../../df/db2/namespaceClipperLib.html#a6c2a946a9f927bfd364c95b561d4191c),
[ClipperLib::GetBottomPt()](../../df/db2/namespaceClipperLib.html#ad7895448ee9b2d2499a57addd49b2192),
[AdaptivePath::ClearedArea::GetBoundedClearedAreaClipped()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a396af78fc129b33fe0c3730caadc9503),
[AdaptivePath::ClearedArea::GetBoundedClearedPaths()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a68e1a211be4683c860dba6ec244abc36),
[AdaptivePath::EngagePoint::getCurrentDir()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a64238fcdbfa9f4bf6a2fc4f000405339),
[AdaptivePath::EngagePoint::getCurrentPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a4a25dac76882d1527f13a9f4683024a2),
[ClipperLib::GetDx()](../../df/db2/namespaceClipperLib.html#adb890cca4fa2a71731b91968cf4ff49d),
[ClipperLib::GetLowermostRec()](../../df/db2/namespaceClipperLib.html#a3b36c0993f124dd3235ed1dd468d4192),
[ClipperLib::GetOverlapSegment()](../../df/db2/namespaceClipperLib.html#a8817de6dc5a080ead872b1373074c07f),
[PathMachineState.MachineState::getPosition()](../../d4/d53/classPathMachineState_1_1MachineState.html#a2fada51e2c794c0b9c3a81bf2b7fec7d),
[PathMachineState.MachineState::getState()](../../d4/d53/classPathMachineState_1_1MachineState.html#a4a75b28afb6ba79346109b31fa976aec),
[ClipperLib::GetUnitNormal()](../../df/db2/namespaceClipperLib.html#a5a62f42148b8b9991da9cfe8cb9cb065),
[AdaptivePath::IntersectionPoint()](../../d5/d7f/namespaceAdaptivePath.html#ac652f5c393ef400162a3673caf7da369),
[ClipperLib::IntersectListSort()](../../df/db2/namespaceClipperLib.html#aeb44a42315262aee3bfbecbc6a1eac77),
[ClipperLib::IntersectPoint()](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a),
[ClipperLib::JoinHorz()](../../df/db2/namespaceClipperLib.html#acd026a4d43018ae65b8d253fbf44b680),
[AdaptivePath::Line2CircleIntersect()](../../d5/d7f/namespaceAdaptivePath.html#a162b44dbc1289576521d7d3e3084562f),
[ClipperLib::PointInPolygon()](../../df/db2/namespaceClipperLib.html#ac7314f2a1f45c627bac20e9ba2a68212),
[ClipperLib::PointsAreClose()](../../df/db2/namespaceClipperLib.html#a52757887bc031d0052ae95dccb83cd2c),
[AdaptivePath::PointSideOfLine()](../../d5/d7f/namespaceAdaptivePath.html#a443621d89fda38d492b838c7914e3dc7),
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0),
[ClipperLib::Pt2IsBetweenPt1AndPt3()](../../df/db2/namespaceClipperLib.html#a0a448254ee6419dfde0a539080502d88),
[ClipperLib::RangeTest()](../../df/db2/namespaceClipperLib.html#add09a980dfa1da81e1693a55cd912908),
[AdaptivePath::BoundBox::SetFirstPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a33a37a0cdf8b16dbd473f595ba0984eb),
[AdaptivePath::SetSegmentLength()](../../d5/d7f/namespaceAdaptivePath.html#aace2cca9424c6fa5bb3f7302878b0a29),
[ClipperLib::SlopesEqual()](../../df/db2/namespaceClipperLib.html#a052da0ab7e1690b61e36e007769df9f8),
[ClipperLib::SlopesNearCollinear()](../../df/db2/namespaceClipperLib.html#a6a8d461810e4bcb5c67bf8e3026839b6),
[AdaptivePath::SmoothPaths()](../../d5/d7f/namespaceAdaptivePath.html#a08e27d008713754b5d5efca8ef13b962),
[ClipperLib::TopX()](../../df/db2/namespaceClipperLib.html#a63e0b77cf7232cbd4f9909b25bd300be),
and
[ClipperLib::TranslatePath()](../../df/db2/namespaceClipperLib.html#a3c34a4a0ea91a10f729e5ceb6cc33714).

* * *

The documentation for this struct was generated from the following file:

  * FreeCAD/src/Mod/Path/libarea/clipper.hpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

