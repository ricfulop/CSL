---
url: https://freecad.github.io/SourceDoc/db/da7/classBase_1_1Vector2d.html
scraped_at: 2025-09-08T15:18:08.355596
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Vector2d](../../db/da7/classBase_1_1Vector2d.html)

[List of all members](../../dc/d2d/classBase_1_1Vector2d-members.html) | Public Member Functions | Static Public Member Functions | Public Attributes

Base::Vector2d Class Reference

The vector class for 2D calculations.
[More...](../../db/da7/classBase_1_1Vector2d.html#details)

`#include <Tools2D.h>`

##  Public Member Functions  
  
---  
double | [Angle](../../db/da7/classBase_1_1Vector2d.html#a777eb66e1a13c9c2ac0a6f36185053df) () const  
double | [Distance](../../db/da7/classBase_1_1Vector2d.html#ac38b8dc15164591bc08bbc30e8c47f98) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v) const  
double | [GetAngle](../../db/da7/classBase_1_1Vector2d.html#a73af20f3c649efaba063eade062d8f26) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v) const  
[bool](../../d9/db9/classbool.html) | [IsEqual](../../db/da7/classBase_1_1Vector2d.html#a61ca0b11ad1e5e4bb0c1fa11630be960) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v, double tolerance=0.0) const  
[bool](../../d9/db9/classbool.html) | [IsNull](../../db/da7/classBase_1_1Vector2d.html#a54fb065048001c7be6023e6a430f5ac9) (double tolerance=0.0) const  
double | [Length](../../db/da7/classBase_1_1Vector2d.html#a4a196e3b30ef1eaf4069e6ee7984798d) () const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [Negate](../../db/da7/classBase_1_1Vector2d.html#a08f0f62d8e275931aadc51005f42507a) ()  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [Normalize](../../db/da7/classBase_1_1Vector2d.html#ad86e1f342407f62d1eb78bfd5b112ec6) ()  
double | [operator*](../../db/da7/classBase_1_1Vector2d.html#a92cf7f5fc55cd747a5af3bac0875a0a4) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v) const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [operator*](../../db/da7/classBase_1_1Vector2d.html#a001624961eb15177f1f6e62bc27cb026) (double c) const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [operator*=](../../db/da7/classBase_1_1Vector2d.html#a4dba4a923daabbcf3ec6d887729d436a) (double c)  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [operator+](../../db/da7/classBase_1_1Vector2d.html#a004aaafde16eb2d8db7840995af06398) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v) const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [operator+](../../db/da7/classBase_1_1Vector2d.html#aa0ab72b34a8f044aadeeca44984d1994) (void) const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [operator+=](../../db/da7/classBase_1_1Vector2d.html#a6b7ed09e042c9281cde2788b713dfac0) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v)  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [operator-](../../db/da7/classBase_1_1Vector2d.html#acdfebdbb05267bc4da1f4da8ba46f8e7) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v) const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [operator-](../../db/da7/classBase_1_1Vector2d.html#a0a93fb5aba4eef1bff6ec281b9ba6851) (void) const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [operator-=](../../db/da7/classBase_1_1Vector2d.html#a8bd01dbac2631506ab79c2bb3af9153c) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v)  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [operator/](../../db/da7/classBase_1_1Vector2d.html#aa5c0ce56de204c9ab083935ae99069db) (double c) const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [operator/=](../../db/da7/classBase_1_1Vector2d.html#a9a90a53c9eb4989f7d9ac4b6b4d630b7) (double c)  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [operator=](../../db/da7/classBase_1_1Vector2d.html#a91569254be0f6a21e63d007ba1fb8561) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v)  
[bool](../../d9/db9/classbool.html) | [operator==](../../db/da7/classBase_1_1Vector2d.html#aa0236de0ba836de5600966373eec648b) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v) const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [Perpendicular](../../db/da7/classBase_1_1Vector2d.html#abdb2e2cf8278b63d20016982f23909f7) ([bool](../../d9/db9/classbool.html) clockwise=false) const  
void | [ProjectToLine](../../db/da7/classBase_1_1Vector2d.html#ac3bb85302e3998e6accd8ee2410e5167) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &point, const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &line)  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [Rotate](../../db/da7/classBase_1_1Vector2d.html#ad179b1450fd24d8c7b653bae51fa687e) (double angle)  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [Scale](../../db/da7/classBase_1_1Vector2d.html#afbfecdf255d0ae54e409725200ab4dd2) (double factor)  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [Set](../../db/da7/classBase_1_1Vector2d.html#aff76c9ab82fe3e317215e24517823a0f) (double [x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59), double [y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887))  
double | [Sqr](../../db/da7/classBase_1_1Vector2d.html#ab9309067af7b8ac86de3d71cab544c22) () const  
|
[Vector2d](../../db/da7/classBase_1_1Vector2d.html#a4fdef02fa5030071c97223ac62a1c7c8)
()  
| INLINES.
[More...](../../db/da7/classBase_1_1Vector2d.html#a4fdef02fa5030071c97223ac62a1c7c8)  
  
|
[Vector2d](../../db/da7/classBase_1_1Vector2d.html#a2b8c9ec8db0de4247f8ad55772e41f9d)
(const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v)  
|
[Vector2d](../../db/da7/classBase_1_1Vector2d.html#aae56b13eebed56ab1d06158cb211fa3c)
(double
[x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59),
double
[y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887))  
|
[Vector2d](../../db/da7/classBase_1_1Vector2d.html#a1eb27c1d83781e3ee49d7b611e310c39)
(float
[x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59),
float
[y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887))  
  
##  Static Public Member Functions  
  
---  
static [Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [FromPolar](../../db/da7/classBase_1_1Vector2d.html#a51412e53ba53b0d46c4e1cff6736f16f) (double r, double fi)  
  
##  Public Attributes  
  
---  
double | [x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59)  
double | [y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887)  
  
## Detailed Description

The vector class for 2D calculations.

## Constructor & Destructor Documentation

## ◆ Vector2d() [1/4]

Base::Vector2d::Vector2d  | ( | | ) |   
---|---|---|---|---  
  
INLINES.

Referenced by
[FromPolar()](../../db/da7/classBase_1_1Vector2d.html#a51412e53ba53b0d46c4e1cff6736f16f),
[operator*()](../../db/da7/classBase_1_1Vector2d.html#a001624961eb15177f1f6e62bc27cb026),
[operator+()](../../db/da7/classBase_1_1Vector2d.html#aa0ab72b34a8f044aadeeca44984d1994),
[operator-()](../../db/da7/classBase_1_1Vector2d.html#a0a93fb5aba4eef1bff6ec281b9ba6851),
[operator/()](../../db/da7/classBase_1_1Vector2d.html#aa5c0ce56de204c9ab083935ae99069db),
and
[Perpendicular()](../../db/da7/classBase_1_1Vector2d.html#abdb2e2cf8278b63d20016982f23909f7).

## ◆ Vector2d() [2/4]

Base::Vector2d::Vector2d  | ( | float  | _x_ ,   
---|---|---|---  
|  | float  | _y_  
| ) | |   
  
## ◆ Vector2d() [3/4]

Base::Vector2d::Vector2d  | ( | double  | _x_ ,   
---|---|---|---  
|  | double  | _y_  
| ) | |   
  
## ◆ Vector2d() [4/4]

Base::Vector2d::Vector2d  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |   
---|---|---|---|---|---  
  
## Member Function Documentation

## ◆ Angle()

double Base::Vector2d::Angle  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[TechDrawGui::QGIViewDimension::computeLineAndLabelAngles()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a7acfb439e8a3f9b9a24413a12e4cb08b),
[TechDrawGui::QGIViewDimension::drawAngle()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a27c4e7cb613ec0563614d25f802cf6e9),
[TechDrawGui::QGIViewDimension::drawDiameter()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4f99cea83cd1e147dee58d5e4d2c9a65),
and
[TechDrawGui::QGIViewDimension::drawRadiusExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a042db9b374ca5344728e534fef6cc4c4).

## ◆ Distance()

double Base::Vector2d::Distance  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[IsEqual()](../../db/da7/classBase_1_1Vector2d.html#a61ca0b11ad1e5e4bb0c1fa11630be960),
[SketcherGui::DrawSketchHandlerExtend::mouseMove()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#aa7a93c3f3980309d65e4b1ecc9a559d0),
and
[SketcherGui::DrawSketchHandlerExtend::releaseButton()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#a3e947849d6dc89b7f93e87a1ebd9b160).

## ◆ FromPolar()

| [Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::Vector2d::FromPolar  | ( | double  | _r_ ,   
---|---|---|---  
|  | double  | _fi_  
| ) | |   
static  
  
References
[Vector2d()](../../db/da7/classBase_1_1Vector2d.html#a4fdef02fa5030071c97223ac62a1c7c8).

Referenced by
[TechDrawGui::QGIViewDimension::computeExtensionLinePoints()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#afb98d02f6637af9cf0c5a82c2e4c6afa),
[TechDrawGui::QGIViewDimension::computePerpendicularIntersection()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a939cb4effdcb5f1bd2f385e53da1cab3),
[TechDrawGui::QGIViewDimension::drawAngle()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a27c4e7cb613ec0563614d25f802cf6e9),
[TechDrawGui::QGIViewDimension::drawDiameter()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4f99cea83cd1e147dee58d5e4d2c9a65),
[TechDrawGui::QGIViewDimension::drawDimensionArc()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#af1760b7b3a78c954bd8de2b2eaf635e2),
[TechDrawGui::QGIViewDimension::drawDimensionLine()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#afcd07a590840903b52211038bcacb308),
[TechDrawGui::QGIViewDimension::drawDistanceExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4c326f29804428bfd7c9760856dc4f38),
[TechDrawGui::QGIViewDimension::drawDistanceOverride()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#acb3689d2c898c66fe3fde8dd3fbc3978),
[TechDrawGui::QGIViewDimension::drawRadiusExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a042db9b374ca5344728e534fef6cc4c4),
[TechDrawGui::QGIViewDimension::drawSingleLine()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a9ad734618a1aa07c34d77858a4f8e4a9),
[TechDraw::DrawUtil::findCircularArcRectangleIntersections()](../../da/d23/classTechDraw_1_1DrawUtil.html#a0f1ebe99b85e862fe7c7be25f6546bab),
[TechDraw::DrawUtil::findLineRectangleIntersections()](../../da/d23/classTechDraw_1_1DrawUtil.html#afe4bd4ad20f063579af79eaf37cd0447),
and
[TechDraw::DrawUtil::findLineSegmentRectangleIntersections()](../../da/d23/classTechDraw_1_1DrawUtil.html#a936a1e95590b4ca555ff0f176d83bbd0).

## ◆ GetAngle()

double Vector2d::GetAngle  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |  const  
---|---|---|---|---|---  
  
References
[Length()](../../db/da7/classBase_1_1Vector2d.html#a4a196e3b30ef1eaf4069e6ee7984798d).

Referenced by
[SketcherGui::DrawSketchHandlerExtend::mouseMove()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#aa7a93c3f3980309d65e4b1ecc9a559d0).

## ◆ IsEqual()

[bool](../../d9/db9/classbool.html) Base::Vector2d::IsEqual  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_ ,   
---|---|---|---  
|  | double  | _tolerance_ = `0.0`  
| ) | |  const  
  
References
[Distance()](../../db/da7/classBase_1_1Vector2d.html#ac38b8dc15164591bc08bbc30e8c47f98),
and
[draftutils.utils::tolerance()](../../de/d75/group__draftutils.html#ga1f502535eabb15dc7272a379b2ce858e).

Referenced by
[Base::BoundBox2d::IsEqual()](../../de/db4/classBase_1_1BoundBox2d.html#ad50960f7b511f1d5aee4b2dd0e670d4e).

## ◆ IsNull()

[bool](../../d9/db9/classbool.html) Base::Vector2d::IsNull  | ( | double  | _tolerance_ = `0.0`| ) |  const  
---|---|---|---|---|---  
  
References
[draftutils.utils::tolerance()](../../de/d75/group__draftutils.html#ga1f502535eabb15dc7272a379b2ce858e).

## ◆ Length()

double Base::Vector2d::Length  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[TechDrawGui::QGIViewDimension::computeExtensionLinePoints()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#afb98d02f6637af9cf0c5a82c2e4c6afa),
[TechDrawGui::QGIViewDimension::computeLineAndLabelAngles()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a7acfb439e8a3f9b9a24413a12e4cb08b),
[TechDrawGui::QGIViewDimension::drawAngle()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a27c4e7cb613ec0563614d25f802cf6e9),
[TechDrawGui::QGIViewDimension::drawDiameter()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4f99cea83cd1e147dee58d5e4d2c9a65),
[TechDrawGui::QGIViewDimension::drawRadiusExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a042db9b374ca5344728e534fef6cc4c4),
[GetAngle()](../../db/da7/classBase_1_1Vector2d.html#a73af20f3c649efaba063eade062d8f26),
[ArchPanel.CommandPanel::getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[SketcherGui::DrawSketchHandlerExtend::mouseMove()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#aa7a93c3f3980309d65e4b1ecc9a559d0),
[SketcherGui::DrawSketchHandlerRegularPolygon::mouseMove()](../../db/d5f/classSketcherGui_1_1DrawSketchHandlerRegularPolygon.html#a010ff1a06ded66c0c89b32b6c7031408),
[Normalize()](../../db/da7/classBase_1_1Vector2d.html#ad86e1f342407f62d1eb78bfd5b112ec6),
[ProjectToLine()](../../db/da7/classBase_1_1Vector2d.html#ac3bb85302e3998e6accd8ee2410e5167),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
[ArchPanel.CommandPanel::setLength()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a324c9bdbfec0dd8eacfb7d0cea302998),
[Part::Geom2dEllipse::setMajorAxisDir()](../../db/db9/classPart_1_1Geom2dEllipse.html#ab86edac2a0463fa7e361dfdf20932ef2),
[Part::Geom2dArcOfEllipse::setMajorAxisDir()](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a59dbac2571cbe34a7fb325a433ef9e32),
and
[ArchPanel.CommandPanel::update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c).

## ◆ Negate()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2d::Negate  | ( | | ) |   
---|---|---|---|---  
  
References
[x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59),
and
[y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887).

## ◆ Normalize()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2d::Normalize  | ( | | ) |   
---|---|---|---|---  
  
References
[Length()](../../db/da7/classBase_1_1Vector2d.html#a4a196e3b30ef1eaf4069e6ee7984798d).

Referenced by
[Base::Line2d::FromPos()](../../d1/d69/classBase_1_1Line2d.html#a6a9d25de5ddb351d022bc8c4baf4da94),
[ProjectToLine()](../../db/da7/classBase_1_1Vector2d.html#ac3bb85302e3998e6accd8ee2410e5167),
[SketcherGui::DrawSketchHandlerArcOfEllipse::releaseButton()](../../d4/d0e/classSketcherGui_1_1DrawSketchHandlerArcOfEllipse.html#ae0f1ecd2fac7f0ee7d7b57610009dc1d),
and
[SketcherGui::DrawSketchHandlerArcOfHyperbola::releaseButton()](../../d0/dcd/classSketcherGui_1_1DrawSketchHandlerArcOfHyperbola.html#a691e8ff0661b5c0f36bd5ad8c8fe8fa3).

## ◆ operator*() [1/2]

double Base::Vector2d::operator*  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |  const  
---|---|---|---|---|---  
  
References
[x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59).

## ◆ operator*() [2/2]

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::Vector2d::operator*  | ( | double  | _c_| ) |  const  
---|---|---|---|---|---  
  
References
[Vector2d()](../../db/da7/classBase_1_1Vector2d.html#a4fdef02fa5030071c97223ac62a1c7c8).

## ◆ operator*=()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2d::operator*=  | ( | double  | _c_| ) |   
---|---|---|---|---|---  
  
## ◆ operator+() [1/2]

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::Vector2d::operator+  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |  const  
---|---|---|---|---|---  
  
References
[Vector2d()](../../db/da7/classBase_1_1Vector2d.html#a4fdef02fa5030071c97223ac62a1c7c8).

## ◆ operator+() [2/2]

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::Vector2d::operator+  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
References
[Vector2d()](../../db/da7/classBase_1_1Vector2d.html#a4fdef02fa5030071c97223ac62a1c7c8).

## ◆ operator+=()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2d::operator+=  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |   
---|---|---|---|---|---  
  
References
[x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59).

## ◆ operator-() [1/2]

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::Vector2d::operator-  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |  const  
---|---|---|---|---|---  
  
References
[Vector2d()](../../db/da7/classBase_1_1Vector2d.html#a4fdef02fa5030071c97223ac62a1c7c8).

## ◆ operator-() [2/2]

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::Vector2d::operator-  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
References
[Vector2d()](../../db/da7/classBase_1_1Vector2d.html#a4fdef02fa5030071c97223ac62a1c7c8).

## ◆ operator-=()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2d::operator-=  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |   
---|---|---|---|---|---  
  
References
[x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59).

## ◆ operator/()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::Vector2d::operator/  | ( | double  | _c_| ) |  const  
---|---|---|---|---|---  
  
References
[Vector2d()](../../db/da7/classBase_1_1Vector2d.html#a4fdef02fa5030071c97223ac62a1c7c8).

## ◆ operator/=()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2d::operator/=  | ( | double  | _c_| ) |   
---|---|---|---|---|---  
  
## ◆ operator=()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2d::operator=  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |   
---|---|---|---|---|---  
  
References
[x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) Base::Vector2d::operator==  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |  const  
---|---|---|---|---|---  
  
## ◆ Perpendicular()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::Vector2d::Perpendicular  | ( | [bool](../../d9/db9/classbool.html) | _clockwise_ = `false`| ) |  const  
---|---|---|---|---|---  
  
References
[Vector2d()](../../db/da7/classBase_1_1Vector2d.html#a4fdef02fa5030071c97223ac62a1c7c8).

Referenced by
[TechDrawGui::QGIViewDimension::drawDistanceExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4c326f29804428bfd7c9760856dc4f38),
and
[Base::Vector2dPy::perpendicular()](../../dd/dff/classBase_1_1Vector2dPy.html#aa699cf47abedf46be4bb3e180e04cc50).

## ◆ ProjectToLine()

void Vector2d::ProjectToLine  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _point_ ,   
---|---|---|---  
|  | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _line_  
| ) | |   
  
References
[Length()](../../db/da7/classBase_1_1Vector2d.html#a4a196e3b30ef1eaf4069e6ee7984798d),
[Normalize()](../../db/da7/classBase_1_1Vector2d.html#ad86e1f342407f62d1eb78bfd5b112ec6),
and
[Scale()](../../db/da7/classBase_1_1Vector2d.html#afbfecdf255d0ae54e409725200ab4dd2).

Referenced by
[SketcherGui::DrawSketchHandlerExtend::mouseMove()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#aa7a93c3f3980309d65e4b1ecc9a559d0).

## ◆ Rotate()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2d::Rotate  | ( | double  | _angle_| ) |   
---|---|---|---|---|---  
  
References
[x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59).

## ◆ Scale()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2d::Scale  | ( | double  | _factor_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ProjectToLine()](../../db/da7/classBase_1_1Vector2d.html#ac3bb85302e3998e6accd8ee2410e5167),
[SketcherGui::DrawSketchHandlerArcOfEllipse::releaseButton()](../../d4/d0e/classSketcherGui_1_1DrawSketchHandlerArcOfEllipse.html#ae0f1ecd2fac7f0ee7d7b57610009dc1d),
and
[SketcherGui::DrawSketchHandlerArcOfHyperbola::releaseButton()](../../d0/dcd/classSketcherGui_1_1DrawSketchHandlerArcOfHyperbola.html#a691e8ff0661b5c0f36bd5ad8c8fe8fa3).

## ◆ Set()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2d::Set  | ( | double  | _x_ ,   
---|---|---|---  
|  | double  | _y_  
| ) | |   
  
References
[x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59),
and
[y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887).

## ◆ Sqr()

double Base::Vector2d::Sqr  | ( | | ) |  const  
---|---|---|---|---  
  
References
[y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887).

## Member Data Documentation

## ◆ x

double Base::Vector2d::x  
---  
  
Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector::add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[Base::Line2d::CalcBoundBox()](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516),
[DraftGui.DraftToolBar::changeXValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a2264e5b2058aeec75cb9044b36485378),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[PathScripts.PathInspect.GCodeEditorDialog::cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[Base::Polygon2d::Contains()](../../d0/dfa/classBase_1_1Polygon2d.html#ae1505348f7365e85a8a9d724dd2a7475),
[Mod.PartDesign.Scripts.FilletArc.Vector::cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[PathScripts.PostUtils.GCodeEditorDialog::done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Mod.PartDesign.Scripts.FilletArc.Vector::dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[TechDrawGui::QGIViewDimension::drawDiameter()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4f99cea83cd1e147dee58d5e4d2c9a65),
[TechDrawGui::QGIViewDimension::drawRadiusExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a042db9b374ca5344728e534fef6cc4c4),
[TechDrawGui::QGIViewDimension::drawSingleArc()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a96562f1133006c5609b7fdd76619795c),
[TechDraw::DrawUtil::findCircleRectangleIntersections()](../../da/d23/classTechDraw_1_1DrawUtil.html#a3131c96006ff34b898481ff4c11d1139),
[TechDraw::DrawUtil::findLineRectangleIntersections()](../../da/d23/classTechDraw_1_1DrawUtil.html#afe4bd4ad20f063579af79eaf37cd0447),
[Base::Line2d::FromPos()](../../d1/d69/classBase_1_1Line2d.html#a6a9d25de5ddb351d022bc8c4baf4da94),
[Part::Geom2dLine::Geom2dLine()](../../d2/d27/classPart_1_1Geom2dLine.html#a70317eb2a8996b65f910b81ee4e8667d),
[Part::Geom2dCircle::getCircleCenter()](../../d7/d4e/classPart_1_1Geom2dCircle.html#a29a53d81475c29517ede323102cc941f),
[SketcherGui::GetPointAngle()](../../d6/d44/namespaceSketcherGui.html#adfb290f8e21ec6cb1d75d1f2da6cbcc3),
[Base::BoundBox2d::Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329),
[Base::Line2d::Intersect()](../../d1/d69/classBase_1_1Line2d.html#a6387b9d36d8bb717c7d643792e8fe3e7),
[TechDraw::DrawUtil::Intersect2d()](../../da/d23/classTechDraw_1_1DrawUtil.html#ab1cc61e0a03c4ad0e1a10afa83b43013),
[Mod.PartDesign.Scripts.FilletArc.Vector::length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[DrawSketchHandlerBSplineInsertKnot::mouseMove()](../../d2/df2/classDrawSketchHandlerBSplineInsertKnot.html#a60d07ab6b604aef8674f849e380898ec),
[SketcherGui::DrawSketchHandlerArc::mouseMove()](../../d4/d83/classSketcherGui_1_1DrawSketchHandlerArc.html#a996bf20b0122549af4a1f6bec8314cdc),
[SketcherGui::DrawSketchHandler3PointArc::mouseMove()](../../d3/d84/classSketcherGui_1_1DrawSketchHandler3PointArc.html#a395c9d42eac9d3651c3b17db1ae6ae1b),
[SketcherGui::DrawSketchHandlerArcOfEllipse::mouseMove()](../../d4/d0e/classSketcherGui_1_1DrawSketchHandlerArcOfEllipse.html#a0066acc2d24ed7398dd3c557b5b13e0b),
[SketcherGui::DrawSketchHandlerArcOfHyperbola::mouseMove()](../../d0/dcd/classSketcherGui_1_1DrawSketchHandlerArcOfHyperbola.html#a1a9a79680a0d823af85d44bba75cb9cd),
[SketcherGui::DrawSketchHandlerArcOfParabola::mouseMove()](../../d3/dd4/classSketcherGui_1_1DrawSketchHandlerArcOfParabola.html#a1cd702b187dd64ee9cb2ae44b3581ae0),
[SketcherGui::DrawSketchHandlerCircle::mouseMove()](../../db/daa/classSketcherGui_1_1DrawSketchHandlerCircle.html#a278e68c21de5eb48d5b6630585cbda4a),
[SketcherGui::DrawSketchHandler3PointCircle::mouseMove()](../../db/dbc/classSketcherGui_1_1DrawSketchHandler3PointCircle.html#a88cd5dcc9c560273103490af37517125),
[SketcherGui::DrawSketchHandlerExtend::mouseMove()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#aa7a93c3f3980309d65e4b1ecc9a559d0),
[SketcherGui::DrawSketchHandlerLineSet::mouseMove()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a113e395cf71488043942d51f78b7d167),
[SketcherGui::DrawSketchHandlerRegularPolygon::mouseMove()](../../db/d5f/classSketcherGui_1_1DrawSketchHandlerRegularPolygon.html#a010ff1a06ded66c0c89b32b6c7031408),
[SketcherGui::DrawSketchHandlerBox::mouseMove()](../../dc/d09/classSketcherGui_1_1DrawSketchHandlerBox.html#ae295740b717a66626e91c022fefa4c14),
[SketcherGui::DrawSketchHandlerOblong::mouseMove()](../../dc/dac/classSketcherGui_1_1DrawSketchHandlerOblong.html#a243ac1fe30bd2f2468bff2adc6df82a0),
[SketcherGui::DrawSketchHandlerSlot::mouseMove()](../../d5/dd5/classSketcherGui_1_1DrawSketchHandlerSlot.html#af5798e2a9cf64e884e8a84f78aeeb716),
[SketcherGui::DrawSketchHandlerTrimming::mouseMove()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a206e252777274a73c12e2a6b51f0ecc9),
[Mod.PartDesign.Scripts.FilletArc.Vector::mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Negate()](../../db/da7/classBase_1_1Vector2d.html#a08f0f62d8e275931aadc51005f42507a),
[Mod.PartDesign.Scripts.FilletArc.Vector::norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[operator*()](../../db/da7/classBase_1_1Vector2d.html#a92cf7f5fc55cd747a5af3bac0875a0a4),
[operator+=()](../../db/da7/classBase_1_1Vector2d.html#a6b7ed09e042c9281cde2788b713dfac0),
[operator-=()](../../db/da7/classBase_1_1Vector2d.html#a8bd01dbac2631506ab79c2bb3af9153c),
[operator=()](../../db/da7/classBase_1_1Vector2d.html#a91569254be0f6a21e63d007ba1fb8561),
[PathScripts.PathDressupHoldingTags.Tag::originAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aa1cbd48305f117e5197555822fd45f3f),
[DraftGui.DraftToolBar::pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[SketcherGui::DrawSketchHandlerArc::pressButton()](../../d4/d83/classSketcherGui_1_1DrawSketchHandlerArc.html#a3f7c69856adb0d4585957d666e1aafd0),
[SketcherGui::DrawSketchHandlerBox::pressButton()](../../dc/d09/classSketcherGui_1_1DrawSketchHandlerBox.html#a21b674fd10a007a790962dfd983ac4a6),
[DrawSketchHandlerGenConstraint::releaseButton()](../../d7/dc2/classDrawSketchHandlerGenConstraint.html#a8c9d15e5c489ccb3f06cacaae622f0f3),
[DrawSketchHandlerCoincident::releaseButton()](../../d1/da0/classDrawSketchHandlerCoincident.html#a0aa30cef84692d6048db1607abb8b77f),
[DrawSketchHandlerCopy::releaseButton()](../../d0/d19/classDrawSketchHandlerCopy.html#ae8955bcf2ad603ca908dbde0ca52042a),
[DrawSketchHandlerRectangularArray::releaseButton()](../../db/da6/classDrawSketchHandlerRectangularArray.html#acad62cdf5d8d411d55beff22a12fac28),
[SketcherGui::DrawSketchHandlerArc::releaseButton()](../../d4/d83/classSketcherGui_1_1DrawSketchHandlerArc.html#ab283932a602b4b135259d8ec565cbe1a),
[SketcherGui::DrawSketchHandler3PointArc::releaseButton()](../../d3/d84/classSketcherGui_1_1DrawSketchHandler3PointArc.html#ad9123e0df6dfcbca72fb0a45e63bb822),
[SketcherGui::DrawSketchHandlerArcOfEllipse::releaseButton()](../../d4/d0e/classSketcherGui_1_1DrawSketchHandlerArcOfEllipse.html#ae0f1ecd2fac7f0ee7d7b57610009dc1d),
[SketcherGui::DrawSketchHandler3PointCircle::releaseButton()](../../db/dbc/classSketcherGui_1_1DrawSketchHandler3PointCircle.html#a3393a6d51aed0b745e44e60f55e4c96a),
[SketcherGui::DrawSketchHandlerExtend::releaseButton()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#a3e947849d6dc89b7f93e87a1ebd9b160),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[SketcherGui::DrawSketchHandlerLineSet::releaseButton()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a040aa2a8cc28c52db550115a16ef693c),
[SketcherGui::DrawSketchHandlerPoint::releaseButton()](../../df/da1/classSketcherGui_1_1DrawSketchHandlerPoint.html#a733f6bcea854c88e77f73e0a1b377f53),
[SketcherGui::DrawSketchHandlerRegularPolygon::releaseButton()](../../db/d5f/classSketcherGui_1_1DrawSketchHandlerRegularPolygon.html#a676a473ddbfd8fd7f2e214ffc43352b5),
[SketcherGui::DrawSketchHandlerBox::releaseButton()](../../dc/d09/classSketcherGui_1_1DrawSketchHandlerBox.html#a1ee8ff08af23b1ad1d9fd48170889315),
[SketcherGui::DrawSketchHandlerOblong::releaseButton()](../../dc/dac/classSketcherGui_1_1DrawSketchHandlerOblong.html#a8e2b792d2ce80795c2808e6276bdd6dc),
[SketcherGui::DrawSketchHandlerSlot::releaseButton()](../../d5/dd5/classSketcherGui_1_1DrawSketchHandlerSlot.html#aa93e01a33ed89216e53c3c8886b21a35),
[SketcherGui::DrawSketchHandlerSplitting::releaseButton()](../../d1/d6f/classSketcherGui_1_1DrawSketchHandlerSplitting.html#a0766956ef48057437eca84c83e1b3521),
[SketcherGui::DrawSketchHandlerTrimming::releaseButton()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a19ae638451e1d23b50c23409a6eeded1),
[SketcherGui::DrawSketchHandlerArcOfHyperbola::releaseButton()](../../d0/dcd/classSketcherGui_1_1DrawSketchHandlerArcOfHyperbola.html#a691e8ff0661b5c0f36bd5ad8c8fe8fa3),
[SketcherGui::DrawSketchHandlerArcOfParabola::releaseButton()](../../d3/dd4/classSketcherGui_1_1DrawSketchHandlerArcOfParabola.html#a17a69b223beded8cad2a7319ef4cffe6),
[DraftGui.DraftToolBar::reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[Rotate()](../../db/da7/classBase_1_1Vector2d.html#ad179b1450fd24d8c7b653bae51fa687e),
[Part::Geom2dLineSegment::Save()](../../df/ded/classPart_1_1Geom2dLineSegment.html#af2f3e338722ce52e89ce1624e57e4d31),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
[Set()](../../db/da7/classBase_1_1Vector2d.html#aff76c9ab82fe3e317215e24517823a0f),
[Part::Geom2dLine::setLine()](../../d2/d27/classPart_1_1Geom2dLine.html#ab6b1c62a2e617a97fddb2563baa1e3fa),
[Part::Geom2dConic::setLocation()](../../d8/d0d/classPart_1_1Geom2dConic.html#a7125e32c5f5118d476d697f4f6b57475),
[Part::Geom2dArcOfConic::setLocation()](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html#a11033c68167a7ca410b8a878ca221379),
[Part::Geom2dEllipse::setMajorAxisDir()](../../db/db9/classPart_1_1Geom2dEllipse.html#ab86edac2a0463fa7e361dfdf20932ef2),
[Part::Geom2dArcOfEllipse::setMajorAxisDir()](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a59dbac2571cbe34a7fb325a433ef9e32),
[SketcherGui::EditModeCoinManager::setPositionText()](../../de/dc2/classSketcherGui_1_1EditModeCoinManager.html#a5d244ec783b62bea8ffc6d4f1e6e8cee),
[Mod.PartDesign.Scripts.FilletArc.Vector::sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[DraftGui.DraftToolBar::update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar::update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar::updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
[DraftGui.DraftToolBar::validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
and
[automotive_design.right_angular_wedge::wr1()](../../d4/df4/classautomotive__design_1_1right__angular__wedge.html#a08ba5a830562d7f45bb10fe924c7b534).

## ◆ y

double Base::Vector2d::y  
---  
  
Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector::add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[Base::Line2d::CalcBoundBox()](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516),
[DraftGui.DraftToolBar::changeYValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a245f69442c47aa69844d30313e68b2b7),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[PathScripts.PathInspect.GCodeEditorDialog::cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[Base::Polygon2d::Contains()](../../d0/dfa/classBase_1_1Polygon2d.html#ae1505348f7365e85a8a9d724dd2a7475),
[Mod.PartDesign.Scripts.FilletArc.Vector::cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[PathScripts.PostUtils.GCodeEditorDialog::done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Mod.PartDesign.Scripts.FilletArc.Vector::dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[TechDrawGui::QGIViewDimension::drawDiameter()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4f99cea83cd1e147dee58d5e4d2c9a65),
[TechDrawGui::QGIViewDimension::drawSingleArc()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a96562f1133006c5609b7fdd76619795c),
[TechDraw::DrawUtil::findCircleRectangleIntersections()](../../da/d23/classTechDraw_1_1DrawUtil.html#a3131c96006ff34b898481ff4c11d1139),
[TechDraw::DrawUtil::findLineRectangleIntersections()](../../da/d23/classTechDraw_1_1DrawUtil.html#afe4bd4ad20f063579af79eaf37cd0447),
[Base::Line2d::FromPos()](../../d1/d69/classBase_1_1Line2d.html#a6a9d25de5ddb351d022bc8c4baf4da94),
[Part::Geom2dLine::Geom2dLine()](../../d2/d27/classPart_1_1Geom2dLine.html#a70317eb2a8996b65f910b81ee4e8667d),
[TechDrawGui::QGIViewDimension::getAsmeRefJointPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#aebbc23e649a5dbca08e595a2141bb8dd),
[TechDrawGui::QGIViewDimension::getAsmeRefOutsetPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a23966e91bf179c155286a1d6e44247b7),
[Part::Geom2dCircle::getCircleCenter()](../../d7/d4e/classPart_1_1Geom2dCircle.html#a29a53d81475c29517ede323102cc941f),
[SketcherGui::GetPointAngle()](../../d6/d44/namespaceSketcherGui.html#adfb290f8e21ec6cb1d75d1f2da6cbcc3),
[Base::BoundBox2d::Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329),
[Base::Line2d::Intersect()](../../d1/d69/classBase_1_1Line2d.html#a6387b9d36d8bb717c7d643792e8fe3e7),
[TechDraw::DrawUtil::Intersect2d()](../../da/d23/classTechDraw_1_1DrawUtil.html#ab1cc61e0a03c4ad0e1a10afa83b43013),
[Mod.PartDesign.Scripts.FilletArc.Vector::length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[DrawSketchHandlerBSplineInsertKnot::mouseMove()](../../d2/df2/classDrawSketchHandlerBSplineInsertKnot.html#a60d07ab6b604aef8674f849e380898ec),
[SketcherGui::DrawSketchHandlerArc::mouseMove()](../../d4/d83/classSketcherGui_1_1DrawSketchHandlerArc.html#a996bf20b0122549af4a1f6bec8314cdc),
[SketcherGui::DrawSketchHandler3PointArc::mouseMove()](../../d3/d84/classSketcherGui_1_1DrawSketchHandler3PointArc.html#a395c9d42eac9d3651c3b17db1ae6ae1b),
[SketcherGui::DrawSketchHandlerArcOfEllipse::mouseMove()](../../d4/d0e/classSketcherGui_1_1DrawSketchHandlerArcOfEllipse.html#a0066acc2d24ed7398dd3c557b5b13e0b),
[SketcherGui::DrawSketchHandlerArcOfHyperbola::mouseMove()](../../d0/dcd/classSketcherGui_1_1DrawSketchHandlerArcOfHyperbola.html#a1a9a79680a0d823af85d44bba75cb9cd),
[SketcherGui::DrawSketchHandlerArcOfParabola::mouseMove()](../../d3/dd4/classSketcherGui_1_1DrawSketchHandlerArcOfParabola.html#a1cd702b187dd64ee9cb2ae44b3581ae0),
[SketcherGui::DrawSketchHandlerCircle::mouseMove()](../../db/daa/classSketcherGui_1_1DrawSketchHandlerCircle.html#a278e68c21de5eb48d5b6630585cbda4a),
[SketcherGui::DrawSketchHandler3PointCircle::mouseMove()](../../db/dbc/classSketcherGui_1_1DrawSketchHandler3PointCircle.html#a88cd5dcc9c560273103490af37517125),
[SketcherGui::DrawSketchHandlerExtend::mouseMove()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#aa7a93c3f3980309d65e4b1ecc9a559d0),
[SketcherGui::DrawSketchHandlerLineSet::mouseMove()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a113e395cf71488043942d51f78b7d167),
[SketcherGui::DrawSketchHandlerRegularPolygon::mouseMove()](../../db/d5f/classSketcherGui_1_1DrawSketchHandlerRegularPolygon.html#a010ff1a06ded66c0c89b32b6c7031408),
[SketcherGui::DrawSketchHandlerBox::mouseMove()](../../dc/d09/classSketcherGui_1_1DrawSketchHandlerBox.html#ae295740b717a66626e91c022fefa4c14),
[SketcherGui::DrawSketchHandlerOblong::mouseMove()](../../dc/dac/classSketcherGui_1_1DrawSketchHandlerOblong.html#a243ac1fe30bd2f2468bff2adc6df82a0),
[SketcherGui::DrawSketchHandlerSlot::mouseMove()](../../d5/dd5/classSketcherGui_1_1DrawSketchHandlerSlot.html#af5798e2a9cf64e884e8a84f78aeeb716),
[SketcherGui::DrawSketchHandlerTrimming::mouseMove()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a206e252777274a73c12e2a6b51f0ecc9),
[Mod.PartDesign.Scripts.FilletArc.Vector::mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Negate()](../../db/da7/classBase_1_1Vector2d.html#a08f0f62d8e275931aadc51005f42507a),
[Mod.PartDesign.Scripts.FilletArc.Vector::norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[PathScripts.PathDressupHoldingTags.Tag::originAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aa1cbd48305f117e5197555822fd45f3f),
[DraftGui.DraftToolBar::pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[SketcherGui::DrawSketchHandlerArc::pressButton()](../../d4/d83/classSketcherGui_1_1DrawSketchHandlerArc.html#a3f7c69856adb0d4585957d666e1aafd0),
[SketcherGui::DrawSketchHandlerBox::pressButton()](../../dc/d09/classSketcherGui_1_1DrawSketchHandlerBox.html#a21b674fd10a007a790962dfd983ac4a6),
[DrawSketchHandlerGenConstraint::releaseButton()](../../d7/dc2/classDrawSketchHandlerGenConstraint.html#a8c9d15e5c489ccb3f06cacaae622f0f3),
[DrawSketchHandlerCoincident::releaseButton()](../../d1/da0/classDrawSketchHandlerCoincident.html#a0aa30cef84692d6048db1607abb8b77f),
[DrawSketchHandlerCopy::releaseButton()](../../d0/d19/classDrawSketchHandlerCopy.html#ae8955bcf2ad603ca908dbde0ca52042a),
[DrawSketchHandlerRectangularArray::releaseButton()](../../db/da6/classDrawSketchHandlerRectangularArray.html#acad62cdf5d8d411d55beff22a12fac28),
[SketcherGui::DrawSketchHandlerArc::releaseButton()](../../d4/d83/classSketcherGui_1_1DrawSketchHandlerArc.html#ab283932a602b4b135259d8ec565cbe1a),
[SketcherGui::DrawSketchHandler3PointArc::releaseButton()](../../d3/d84/classSketcherGui_1_1DrawSketchHandler3PointArc.html#ad9123e0df6dfcbca72fb0a45e63bb822),
[SketcherGui::DrawSketchHandlerArcOfEllipse::releaseButton()](../../d4/d0e/classSketcherGui_1_1DrawSketchHandlerArcOfEllipse.html#ae0f1ecd2fac7f0ee7d7b57610009dc1d),
[SketcherGui::DrawSketchHandler3PointCircle::releaseButton()](../../db/dbc/classSketcherGui_1_1DrawSketchHandler3PointCircle.html#a3393a6d51aed0b745e44e60f55e4c96a),
[SketcherGui::DrawSketchHandlerExtend::releaseButton()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#a3e947849d6dc89b7f93e87a1ebd9b160),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[SketcherGui::DrawSketchHandlerLineSet::releaseButton()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a040aa2a8cc28c52db550115a16ef693c),
[SketcherGui::DrawSketchHandlerPoint::releaseButton()](../../df/da1/classSketcherGui_1_1DrawSketchHandlerPoint.html#a733f6bcea854c88e77f73e0a1b377f53),
[SketcherGui::DrawSketchHandlerRegularPolygon::releaseButton()](../../db/d5f/classSketcherGui_1_1DrawSketchHandlerRegularPolygon.html#a676a473ddbfd8fd7f2e214ffc43352b5),
[SketcherGui::DrawSketchHandlerBox::releaseButton()](../../dc/d09/classSketcherGui_1_1DrawSketchHandlerBox.html#a1ee8ff08af23b1ad1d9fd48170889315),
[SketcherGui::DrawSketchHandlerOblong::releaseButton()](../../dc/dac/classSketcherGui_1_1DrawSketchHandlerOblong.html#a8e2b792d2ce80795c2808e6276bdd6dc),
[SketcherGui::DrawSketchHandlerSlot::releaseButton()](../../d5/dd5/classSketcherGui_1_1DrawSketchHandlerSlot.html#aa93e01a33ed89216e53c3c8886b21a35),
[SketcherGui::DrawSketchHandlerSplitting::releaseButton()](../../d1/d6f/classSketcherGui_1_1DrawSketchHandlerSplitting.html#a0766956ef48057437eca84c83e1b3521),
[SketcherGui::DrawSketchHandlerTrimming::releaseButton()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a19ae638451e1d23b50c23409a6eeded1),
[SketcherGui::DrawSketchHandlerArcOfHyperbola::releaseButton()](../../d0/dcd/classSketcherGui_1_1DrawSketchHandlerArcOfHyperbola.html#a691e8ff0661b5c0f36bd5ad8c8fe8fa3),
[SketcherGui::DrawSketchHandlerArcOfParabola::releaseButton()](../../d3/dd4/classSketcherGui_1_1DrawSketchHandlerArcOfParabola.html#a17a69b223beded8cad2a7319ef4cffe6),
[DraftGui.DraftToolBar::reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[Part::Geom2dLineSegment::Save()](../../df/ded/classPart_1_1Geom2dLineSegment.html#af2f3e338722ce52e89ce1624e57e4d31),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
[Set()](../../db/da7/classBase_1_1Vector2d.html#aff76c9ab82fe3e317215e24517823a0f),
[Part::Geom2dLine::setLine()](../../d2/d27/classPart_1_1Geom2dLine.html#ab6b1c62a2e617a97fddb2563baa1e3fa),
[Part::Geom2dConic::setLocation()](../../d8/d0d/classPart_1_1Geom2dConic.html#a7125e32c5f5118d476d697f4f6b57475),
[Part::Geom2dArcOfConic::setLocation()](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html#a11033c68167a7ca410b8a878ca221379),
[Part::Geom2dEllipse::setMajorAxisDir()](../../db/db9/classPart_1_1Geom2dEllipse.html#ab86edac2a0463fa7e361dfdf20932ef2),
[Part::Geom2dArcOfEllipse::setMajorAxisDir()](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a59dbac2571cbe34a7fb325a433ef9e32),
[SketcherGui::EditModeCoinManager::setPositionText()](../../de/dc2/classSketcherGui_1_1EditModeCoinManager.html#a5d244ec783b62bea8ffc6d4f1e6e8cee),
[Sqr()](../../db/da7/classBase_1_1Vector2d.html#ab9309067af7b8ac86de3d71cab544c22),
[Mod.PartDesign.Scripts.FilletArc.Vector::sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[DraftGui.DraftToolBar::update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar::update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar::updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
and
[DraftGui.DraftToolBar::validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Tools2D.h
  * FreeCAD/src/Base/Tools2D.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

