---
url: https://freecad.github.io/SourceDoc/de/db4/classBase_1_1BoundBox2d.html
scraped_at: 2025-09-08T15:15:44.713329
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html)

[List of all members](../../d1/d97/classBase_1_1BoundBox2d-members.html) | Public Member Functions | Public Attributes

Base::BoundBox2d Class Reference

[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html "BoundBox2d.").
[More...](../../de/db4/classBase_1_1BoundBox2d.html#details)

`#include <Tools2D.h>`

##  Public Member Functions  
  
---  
void | [Add](../../de/db4/classBase_1_1BoundBox2d.html#a431c0efe7a152057de5551473e1ce330) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v)  
|
[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html#a19cdb15662c3680e8f8673d8cc2f013f)
()  
|
[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html#a1d5324900b20727904080d1210959d09)
(const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) &rclBB)  
|
[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html#ac658a30733b340a80b1e2a815ccc66b3)
(double fX1, double fY1, double fX2, double fY2)  
[bool](../../d9/db9/classbool.html) | [Contains](../../de/db4/classBase_1_1BoundBox2d.html#afb5c026976e2e965c7dbd4ef4e95c5b9) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v) const  
[bool](../../d9/db9/classbool.html) | [Contains](../../de/db4/classBase_1_1BoundBox2d.html#a1689b66487df7a59438a26af41fe64de) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &v, double tolerance) const  
[Vector2d](../../db/da7/classBase_1_1Vector2d.html) | [GetCenter](../../de/db4/classBase_1_1BoundBox2d.html#a3e7c7493e50ed63343f1ff47baeeb388) () const  
double | [Height](../../de/db4/classBase_1_1BoundBox2d.html#a71abc93de414c38e8fedb6c432e0e204) () const  
[bool](../../d9/db9/classbool.html) | [Intersect](../../de/db4/classBase_1_1BoundBox2d.html#a0cd94604ba2095974529665dfaec46df) (const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) &rclBB) const  
[bool](../../d9/db9/classbool.html) | [Intersect](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329) (const [Line2d](../../d1/d69/classBase_1_1Line2d.html) &rclLine) const  
| BOUNDBOX2d.
[More...](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329)  
  
[bool](../../d9/db9/classbool.html) | [Intersect](../../de/db4/classBase_1_1BoundBox2d.html#a06385687a9da411a4fa8863de43c2926) (const [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) &rclPoly) const  
[bool](../../d9/db9/classbool.html) | [IsEqual](../../de/db4/classBase_1_1BoundBox2d.html#ad50960f7b511f1d5aee4b2dd0e670d4e) (const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) &, double tolerance) const  
[bool](../../d9/db9/classbool.html) | [IsValid](../../de/db4/classBase_1_1BoundBox2d.html#ad5a43aa399a47a616d17d1f8c3fb3b5b) ()  
[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) & | [operator=](../../de/db4/classBase_1_1BoundBox2d.html#aa633e218e804dc58fa1e509d9863753c) (const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) &rclBB)  
[bool](../../d9/db9/classbool.html) | [operator==](../../de/db4/classBase_1_1BoundBox2d.html#a43d01028568f9315acd9d513478eaeec) (const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) &rclBB) const  
void | [SetVoid](../../de/db4/classBase_1_1BoundBox2d.html#a04f0131a87de65c00a2de633e6255e61) ()  
double | [Width](../../de/db4/classBase_1_1BoundBox2d.html#a2ac4f7f142c631813a6ecc93882cc362) () const  
  
##  Public Attributes  
  
---  
double | [MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1)  
double | [MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80)  
double | [MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36)  
double | [MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133)  
  
## Detailed Description

[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html "BoundBox2d.").

Two dimensional bounding box.

## Constructor & Destructor Documentation

## ◆ BoundBox2d() [1/3]

Base::BoundBox2d::BoundBox2d  | ( | | ) |   
---|---|---|---|---  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

## ◆ BoundBox2d() [2/3]

Base::BoundBox2d::BoundBox2d  | ( | const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) & | _rclBB_| ) |   
---|---|---|---|---|---  
  
## ◆ BoundBox2d() [3/3]

Base::BoundBox2d::BoundBox2d  | ( | double  | _fX1_ ,   
---|---|---|---  
|  | double  | _fY1_ ,   
|  | double  | _fX2_ ,   
|  | double  | _fY2_  
| ) | |   
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

## Member Function Documentation

## ◆ Add()

void Base::BoundBox2d::Add  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |   
---|---|---|---|---|---  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

Referenced by
[Reen::ParameterCorrection::GetUVParameters()](../../dd/d71/classReen_1_1ParameterCorrection.html#a028ded344bc8a4f83fea1f6e6a7c8364),
and [Base::BoundBox3< _Precision
>::ProjectBox()](../../d8/d12/classBase_1_1BoundBox3.html#a4d8b86292716416ed2151d4190291ad1).

## ◆ Contains() [1/2]

[bool](../../d9/db9/classbool.html) Base::BoundBox2d::Contains  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |  const  
---|---|---|---|---|---  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

Referenced by
[MeshCore::MeshAlgorithm::CheckFacets()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#ac8032a5a0a06cee43035edcb9253b731),
[Base::Line2d::Contains()](../../d1/d69/classBase_1_1Line2d.html#a6327c8680eb946c971868a31229cb959),
[Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a06385687a9da411a4fa8863de43c2926),
and
[TechDraw::DrawUtil::mergeBoundedPoint()](../../da/d23/classTechDraw_1_1DrawUtil.html#a7c994218556d818794a2eff2e0725440).

## ◆ Contains() [2/2]

[bool](../../d9/db9/classbool.html) Base::BoundBox2d::Contains  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_ ,   
---|---|---|---  
|  | double  | _tolerance_  
| ) | |  const  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133),
and
[draftutils.utils::tolerance()](../../de/d75/group__draftutils.html#ga1f502535eabb15dc7272a379b2ce858e).

## ◆ GetCenter()

[Vector2d](../../db/da7/classBase_1_1Vector2d.html) Base::BoundBox2d::GetCenter  | ( | | ) |  const  
---|---|---|---|---  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

Referenced by
[TechDrawGui::QGIViewDimension::constructDimensionArc()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a46189f004d7a87822d44aaf7d34824c0),
[TechDrawGui::QGIViewDimension::constructDimensionLine()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#aba70a6532f229c80844d4c191794e088),
[TechDrawGui::QGIViewDimension::drawAngle()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a27c4e7cb613ec0563614d25f802cf6e9),
[TechDrawGui::QGIViewDimension::drawDiameter()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4f99cea83cd1e147dee58d5e4d2c9a65),
[TechDrawGui::QGIViewDimension::drawDistanceExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4c326f29804428bfd7c9760856dc4f38),
[TechDrawGui::QGIViewDimension::drawDistanceOverride()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#acb3689d2c898c66fe3fde8dd3fbc3978),
[TechDrawGui::QGIViewDimension::drawRadiusExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a042db9b374ca5344728e534fef6cc4c4),
[TechDrawGui::QGIViewDimension::getAsmeRefJointPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#aebbc23e649a5dbca08e595a2141bb8dd),
and
[TechDrawGui::QGIViewDimension::getAsmeRefOutsetPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a23966e91bf179c155286a1d6e44247b7).

## ◆ Height()

double Base::BoundBox2d::Height  | ( | | ) |  const  
---|---|---|---|---  
  
References
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[TechDrawGui::QGIViewDimension::drawAngle()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a27c4e7cb613ec0563614d25f802cf6e9),
[TechDrawGui::QGIViewDimension::drawDiameter()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4f99cea83cd1e147dee58d5e4d2c9a65),
[TechDrawGui::QGIViewDimension::drawDistanceExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4c326f29804428bfd7c9760856dc4f38),
[TechDrawGui::QGIViewDimension::drawDistanceOverride()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#acb3689d2c898c66fe3fde8dd3fbc3978),
and
[TechDrawGui::QGIViewDimension::drawRadiusExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a042db9b374ca5344728e534fef6cc4c4).

## ◆ Intersect() [1/3]

[bool](../../d9/db9/classbool.html) BoundBox2d::Intersect  | ( | const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) & | _rclBB_| ) |  const  
---|---|---|---|---|---  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

## ◆ Intersect() [2/3]

[bool](../../d9/db9/classbool.html) BoundBox2d::Intersect  | ( | const [Line2d](../../d1/d69/classBase_1_1Line2d.html) & | _rclLine_| ) |  const  
---|---|---|---|---|---  
  
BOUNDBOX2d.

References
[Base::Line2d::clV1](../../d1/d69/classBase_1_1Line2d.html#a10884a03dec4bc93c74ab8ad7c2b3d60),
[Base::Line2d::clV2](../../d1/d69/classBase_1_1Line2d.html#ae368828e435ebf6acc77c1cf10cd09ce),
[Base::Line2d::IntersectAndContain()](../../d1/d69/classBase_1_1Line2d.html#afd22687bb810c2f174f65d1f96361bda),
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133),
[Base::Vector2d::x](../../db/da7/classBase_1_1Vector2d.html#a3315b37d53044b7356de30337675eb59),
and
[Base::Vector2d::y](../../db/da7/classBase_1_1Vector2d.html#a939f494d2b0c0395a9003e30d4c07887).

Referenced by
[MeshCore::MeshAlgorithm::CheckFacets()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#ac8032a5a0a06cee43035edcb9253b731),
[MeshCore::MeshTrimming::CheckFacets()](../../d3/da1/classMeshCore_1_1MeshTrimming.html#a94a5bf3ea3f16d468c08906a5dcbb472),
and
[Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a06385687a9da411a4fa8863de43c2926).

## ◆ Intersect() [3/3]

[bool](../../d9/db9/classbool.html) BoundBox2d::Intersect  | ( | const [Polygon2d](../../d0/dfa/classBase_1_1Polygon2d.html) & | _rclPoly_| ) |  const  
---|---|---|---|---|---  
  
References
[Base::Line2d::clV1](../../d1/d69/classBase_1_1Line2d.html#a10884a03dec4bc93c74ab8ad7c2b3d60),
[Base::Line2d::clV2](../../d1/d69/classBase_1_1Line2d.html#ae368828e435ebf6acc77c1cf10cd09ce),
[Base::Polygon2d::Contains()](../../d0/dfa/classBase_1_1Polygon2d.html#ae1505348f7365e85a8a9d724dd2a7475),
[Contains()](../../de/db4/classBase_1_1BoundBox2d.html#afb5c026976e2e965c7dbd4ef4e95c5b9),
[Base::Polygon2d::GetCtVectors()](../../d0/dfa/classBase_1_1Polygon2d.html#ae3d3b22f23505533cd9379ce3b00e3eb),
[Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329),
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

## ◆ IsEqual()

[bool](../../d9/db9/classbool.html) Base::BoundBox2d::IsEqual  | ( | const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) & | _b_ ,   
---|---|---|---  
|  | double  | _tolerance_  
| ) | |  const  
  
References
[Base::Vector2d::IsEqual()](../../db/da7/classBase_1_1Vector2d.html#a61ca0b11ad1e5e4bb0c1fa11630be960),
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133),
and
[draftutils.utils::tolerance()](../../de/d75/group__draftutils.html#ga1f502535eabb15dc7272a379b2ce858e).

## ◆ IsValid()

[bool](../../d9/db9/classbool.html) Base::BoundBox2d::IsValid  | ( | | ) |   
---|---|---|---|---  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

## ◆ operator=()

[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) & Base::BoundBox2d::operator=  | ( | const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) & | _rclBB_| ) |   
---|---|---|---|---|---  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) Base::BoundBox2d::operator==  | ( | const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) & | _rclBB_| ) |  const  
---|---|---|---|---|---  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

## ◆ SetVoid()

void Base::BoundBox2d::SetVoid  | ( | | ) |   
---|---|---|---|---  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

Referenced by [Base::BoundBox3< _Precision
>::ProjectBox()](../../d8/d12/classBase_1_1BoundBox3.html#a4d8b86292716416ed2151d4190291ad1).

## ◆ Width()

double Base::BoundBox2d::Width  | ( | | ) |  const  
---|---|---|---|---  
  
References
[MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
and
[MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[TechDrawGui::QGIViewDimension::constructDimensionArc()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a46189f004d7a87822d44aaf7d34824c0),
[TechDrawGui::QGIViewDimension::constructDimensionLine()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#aba70a6532f229c80844d4c191794e088),
[ArchPanel.CommandPanel::getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[ArchPanel.CommandPanel::setWidth()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a32bea4e80ff9a4e8e91d89aead1d88e1),
and
[ArchPanel.CommandPanel::update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c).

## Member Data Documentation

## ◆ MaxX

double Base::BoundBox2d::MaxX  
---  
  
Referenced by
[Add()](../../de/db4/classBase_1_1BoundBox2d.html#a431c0efe7a152057de5551473e1ce330),
[BoundBox2d()](../../de/db4/classBase_1_1BoundBox2d.html#a19cdb15662c3680e8f8673d8cc2f013f),
[Base::Line2d::CalcBoundBox()](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516),
[Base::Polygon2d::CalcBoundBox()](../../d0/dfa/classBase_1_1Polygon2d.html#a28a51cc5d29213d6e4b9305d658fbd24),
[Contains()](../../de/db4/classBase_1_1BoundBox2d.html#afb5c026976e2e965c7dbd4ef4e95c5b9),
[TechDrawGui::QGIViewDimension::getAsmeRefJointPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#aebbc23e649a5dbca08e595a2141bb8dd),
[TechDrawGui::QGIViewDimension::getAsmeRefOutsetPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a23966e91bf179c155286a1d6e44247b7),
[GetCenter()](../../de/db4/classBase_1_1BoundBox2d.html#a3e7c7493e50ed63343f1ff47baeeb388),
[TechDrawGui::QGIViewDimension::getIsoRefOutsetPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a17f2bd3ac40a1c7b49360e4ecf519297),
[Reen::ParameterCorrection::GetUVParameters()](../../dd/d71/classReen_1_1ParameterCorrection.html#a028ded344bc8a4f83fea1f6e6a7c8364),
[Base::BoundBox3< _Precision
>::Intersect()](../../d8/d12/classBase_1_1BoundBox3.html#a57f8a89fa940fae5c0921ee09686e7a1),
[Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329),
[IsEqual()](../../de/db4/classBase_1_1BoundBox2d.html#ad50960f7b511f1d5aee4b2dd0e670d4e),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#a93832ed4c78a3bfb5807a312f12bd5c2),
[IsValid()](../../de/db4/classBase_1_1BoundBox2d.html#ad5a43aa399a47a616d17d1f8c3fb3b5b),
[operator=()](../../de/db4/classBase_1_1BoundBox2d.html#aa633e218e804dc58fa1e509d9863753c),
[operator==()](../../de/db4/classBase_1_1BoundBox2d.html#a43d01028568f9315acd9d513478eaeec),
[SetVoid()](../../de/db4/classBase_1_1BoundBox2d.html#a04f0131a87de65c00a2de633e6255e61),
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f),
and
[Width()](../../de/db4/classBase_1_1BoundBox2d.html#a2ac4f7f142c631813a6ecc93882cc362).

## ◆ MaxY

double Base::BoundBox2d::MaxY  
---  
  
Referenced by
[Add()](../../de/db4/classBase_1_1BoundBox2d.html#a431c0efe7a152057de5551473e1ce330),
[BoundBox2d()](../../de/db4/classBase_1_1BoundBox2d.html#a19cdb15662c3680e8f8673d8cc2f013f),
[Base::Line2d::CalcBoundBox()](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516),
[Base::Polygon2d::CalcBoundBox()](../../d0/dfa/classBase_1_1Polygon2d.html#a28a51cc5d29213d6e4b9305d658fbd24),
[Contains()](../../de/db4/classBase_1_1BoundBox2d.html#afb5c026976e2e965c7dbd4ef4e95c5b9),
[GetCenter()](../../de/db4/classBase_1_1BoundBox2d.html#a3e7c7493e50ed63343f1ff47baeeb388),
[Reen::ParameterCorrection::GetUVParameters()](../../dd/d71/classReen_1_1ParameterCorrection.html#a028ded344bc8a4f83fea1f6e6a7c8364),
[Height()](../../de/db4/classBase_1_1BoundBox2d.html#a71abc93de414c38e8fedb6c432e0e204),
[Base::BoundBox3< _Precision
>::Intersect()](../../d8/d12/classBase_1_1BoundBox3.html#a57f8a89fa940fae5c0921ee09686e7a1),
[Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329),
[IsEqual()](../../de/db4/classBase_1_1BoundBox2d.html#ad50960f7b511f1d5aee4b2dd0e670d4e),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#a93832ed4c78a3bfb5807a312f12bd5c2),
[IsValid()](../../de/db4/classBase_1_1BoundBox2d.html#ad5a43aa399a47a616d17d1f8c3fb3b5b),
[operator=()](../../de/db4/classBase_1_1BoundBox2d.html#aa633e218e804dc58fa1e509d9863753c),
[operator==()](../../de/db4/classBase_1_1BoundBox2d.html#a43d01028568f9315acd9d513478eaeec),
[SetVoid()](../../de/db4/classBase_1_1BoundBox2d.html#a04f0131a87de65c00a2de633e6255e61),
and
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f).

## ◆ MinX

double Base::BoundBox2d::MinX  
---  
  
Referenced by
[Add()](../../de/db4/classBase_1_1BoundBox2d.html#a431c0efe7a152057de5551473e1ce330),
[BoundBox2d()](../../de/db4/classBase_1_1BoundBox2d.html#a19cdb15662c3680e8f8673d8cc2f013f),
[Base::Line2d::CalcBoundBox()](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516),
[Base::Polygon2d::CalcBoundBox()](../../d0/dfa/classBase_1_1Polygon2d.html#a28a51cc5d29213d6e4b9305d658fbd24),
[Contains()](../../de/db4/classBase_1_1BoundBox2d.html#afb5c026976e2e965c7dbd4ef4e95c5b9),
[TechDrawGui::QGIViewDimension::getAsmeRefJointPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#aebbc23e649a5dbca08e595a2141bb8dd),
[TechDrawGui::QGIViewDimension::getAsmeRefOutsetPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a23966e91bf179c155286a1d6e44247b7),
[GetCenter()](../../de/db4/classBase_1_1BoundBox2d.html#a3e7c7493e50ed63343f1ff47baeeb388),
[TechDrawGui::QGIViewDimension::getIsoRefOutsetPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a17f2bd3ac40a1c7b49360e4ecf519297),
[Reen::ParameterCorrection::GetUVParameters()](../../dd/d71/classReen_1_1ParameterCorrection.html#a028ded344bc8a4f83fea1f6e6a7c8364),
[Base::BoundBox3< _Precision
>::Intersect()](../../d8/d12/classBase_1_1BoundBox3.html#a57f8a89fa940fae5c0921ee09686e7a1),
[Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329),
[IsEqual()](../../de/db4/classBase_1_1BoundBox2d.html#ad50960f7b511f1d5aee4b2dd0e670d4e),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#a93832ed4c78a3bfb5807a312f12bd5c2),
[IsValid()](../../de/db4/classBase_1_1BoundBox2d.html#ad5a43aa399a47a616d17d1f8c3fb3b5b),
[operator=()](../../de/db4/classBase_1_1BoundBox2d.html#aa633e218e804dc58fa1e509d9863753c),
[operator==()](../../de/db4/classBase_1_1BoundBox2d.html#a43d01028568f9315acd9d513478eaeec),
[SetVoid()](../../de/db4/classBase_1_1BoundBox2d.html#a04f0131a87de65c00a2de633e6255e61),
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f),
and
[Width()](../../de/db4/classBase_1_1BoundBox2d.html#a2ac4f7f142c631813a6ecc93882cc362).

## ◆ MinY

double Base::BoundBox2d::MinY  
---  
  
Referenced by
[Add()](../../de/db4/classBase_1_1BoundBox2d.html#a431c0efe7a152057de5551473e1ce330),
[BoundBox2d()](../../de/db4/classBase_1_1BoundBox2d.html#a19cdb15662c3680e8f8673d8cc2f013f),
[Base::Line2d::CalcBoundBox()](../../d1/d69/classBase_1_1Line2d.html#ac67a75e9c6476cbebed194d8e66c8516),
[Base::Polygon2d::CalcBoundBox()](../../d0/dfa/classBase_1_1Polygon2d.html#a28a51cc5d29213d6e4b9305d658fbd24),
[Contains()](../../de/db4/classBase_1_1BoundBox2d.html#afb5c026976e2e965c7dbd4ef4e95c5b9),
[GetCenter()](../../de/db4/classBase_1_1BoundBox2d.html#a3e7c7493e50ed63343f1ff47baeeb388),
[TechDrawGui::QGIViewDimension::getIsoRefOutsetPoint()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a17f2bd3ac40a1c7b49360e4ecf519297),
[Reen::ParameterCorrection::GetUVParameters()](../../dd/d71/classReen_1_1ParameterCorrection.html#a028ded344bc8a4f83fea1f6e6a7c8364),
[Height()](../../de/db4/classBase_1_1BoundBox2d.html#a71abc93de414c38e8fedb6c432e0e204),
[Base::BoundBox3< _Precision
>::Intersect()](../../d8/d12/classBase_1_1BoundBox3.html#a57f8a89fa940fae5c0921ee09686e7a1),
[Intersect()](../../de/db4/classBase_1_1BoundBox2d.html#a2bdb07ef91c340dc5fd1f4371f1e1329),
[IsEqual()](../../de/db4/classBase_1_1BoundBox2d.html#ad50960f7b511f1d5aee4b2dd0e670d4e),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#a93832ed4c78a3bfb5807a312f12bd5c2),
[IsValid()](../../de/db4/classBase_1_1BoundBox2d.html#ad5a43aa399a47a616d17d1f8c3fb3b5b),
[operator=()](../../de/db4/classBase_1_1BoundBox2d.html#aa633e218e804dc58fa1e509d9863753c),
[operator==()](../../de/db4/classBase_1_1BoundBox2d.html#a43d01028568f9315acd9d513478eaeec),
[SetVoid()](../../de/db4/classBase_1_1BoundBox2d.html#a04f0131a87de65c00a2de633e6255e61),
and
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Tools2D.h
  * FreeCAD/src/Base/Tools2D.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

