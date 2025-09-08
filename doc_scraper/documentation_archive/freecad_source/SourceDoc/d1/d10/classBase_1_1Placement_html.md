---
url: https://freecad.github.io/SourceDoc/d1/d10/classBase_1_1Placement.html
scraped_at: 2025-09-08T15:16:52.025582
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Placement](../../d1/d10/classBase_1_1Placement.html)

[List of all members](../../df/d0d/classBase_1_1Placement-members.html) | Public Member Functions | Static Public Member Functions

Base::Placement Class Reference

The [Placement](../../d1/d10/classBase_1_1Placement.html "The Placement
class.") class. [More...](../../d1/d10/classBase_1_1Placement.html#details)

`#include <Placement.h>`

##  Public Member Functions  
  
---  
void | [fromMatrix](../../d1/d10/classBase_1_1Placement.html#a4ddd9ad8b2ce05003b4cfe79b3c253df) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &m)  
const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | [getPosition](../../d1/d10/classBase_1_1Placement.html#aa0992c263f42f61da22594eb7f4a9a13) () const  
const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | [getRotation](../../d1/d10/classBase_1_1Placement.html#af5b5009ff533f306ed03d5259bfb6797) () const  
[Placement](../../d1/d10/classBase_1_1Placement.html) | [inverse](../../d1/d10/classBase_1_1Placement.html#a882753578fa58a54d0e4d05764a33ed3) () const  
void | [invert](../../d1/d10/classBase_1_1Placement.html#ab10df03b87ef69b5ba4a2de73de1973a) ()  
[bool](../../d9/db9/classbool.html) | [isIdentity](../../d1/d10/classBase_1_1Placement.html#adaa1d82cad90e3d7438e55d51ef57fc8) () const  
void | [move](../../d1/d10/classBase_1_1Placement.html#a2d5da9e5288f05ed57ec84686b9ca946) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &MovVec)  
void | [multVec](../../d1/d10/classBase_1_1Placement.html#a7d3c9f9cb3aee926050a6000c5acbb09) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &src, [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &dst) const  
[bool](../../d9/db9/classbool.html) | [operator!=](../../d1/d10/classBase_1_1Placement.html#a061e44a4e2a49663060121938241f4aa) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &) const  
[Placement](../../d1/d10/classBase_1_1Placement.html) | [operator*](../../d1/d10/classBase_1_1Placement.html#a46792b39b8afa493143661399e19eca2) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &p) const  
[Placement](../../d1/d10/classBase_1_1Placement.html) & | [operator*=](../../d1/d10/classBase_1_1Placement.html#a07aba252f6a688da5331d3e9b77667c6) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &p)  
| Operators.
[More...](../../d1/d10/classBase_1_1Placement.html#a07aba252f6a688da5331d3e9b77667c6)  
  
[Placement](../../d1/d10/classBase_1_1Placement.html) & | [operator=](../../d1/d10/classBase_1_1Placement.html#a2797f6ae15202d31b2e9e44458625df2) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &)  
[bool](../../d9/db9/classbool.html) | [operator==](../../d1/d10/classBase_1_1Placement.html#a158a295bac1ca2166099a84a8c46460a) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &) const  
|
[Placement](../../d1/d10/classBase_1_1Placement.html#aa0020a3dd0bedb34998968adfacf8a4e)
()  
| default constructor
[More...](../../d1/d10/classBase_1_1Placement.html#aa0020a3dd0bedb34998968adfacf8a4e)  
  
|
[Placement](../../d1/d10/classBase_1_1Placement.html#a94c0cf87ac294b9c4456a39fce51798d)
(const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &matrix)  
|
[Placement](../../d1/d10/classBase_1_1Placement.html#ad151d5fc265a235d5e2ad6dfe9f1bb30)
(const [Placement](../../d1/d10/classBase_1_1Placement.html) &)  
|
[Placement](../../d1/d10/classBase_1_1Placement.html#a2ab8e2898db6b8ba744950ea09babfee)
(const
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e)
&Pos, const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &Rot)  
|
[Placement](../../d1/d10/classBase_1_1Placement.html#a59e327790fad30aa82b89b9c909984aa)
(const
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e)
&Pos, const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &Rot, const
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e)
&Cnt)  
[Placement](../../d1/d10/classBase_1_1Placement.html) | [pow](../../d1/d10/classBase_1_1Placement.html#a109a0d383d74255f0ae18f12b5861bca) (double t, [bool](../../d9/db9/classbool.html) shorten=true) const  
void | [setPosition](../../d1/d10/classBase_1_1Placement.html#ab00ab60207fc5238bf8a32f8b82a4680) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &Pos)  
void | [setRotation](../../d1/d10/classBase_1_1Placement.html#a117076943ff6c2198add937ace8860b0) (const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &Rot)  
[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | [toDualQuaternion](../../d1/d10/classBase_1_1Placement.html#a700572ce02a191128a6c097d2212562d) () const  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [toMatrix](../../d1/d10/classBase_1_1Placement.html#a17b561d4e993495387875c0aed589c4e) () const  
|
[~Placement](../../d1/d10/classBase_1_1Placement.html#aaadf83b8ab93285273e8d18ca63e8ebd)
()  
| Destruction.
[More...](../../d1/d10/classBase_1_1Placement.html#aaadf83b8ab93285273e8d18ca63e8ebd)  
  
  
##  Static Public Member Functions  
  
---  
static [Placement](../../d1/d10/classBase_1_1Placement.html) | [fromDualQuaternion](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f) ([DualQuat](../../d4/d13/classBase_1_1DualQuat.html) qq)  
| specialty constructors
[More...](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f)  
  
static [Placement](../../d1/d10/classBase_1_1Placement.html) | [sclerp](../../d1/d10/classBase_1_1Placement.html#af9f3428f4cec9051afe44b46d90e6a4a) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &p0, const [Placement](../../d1/d10/classBase_1_1Placement.html) &p1, double t, [bool](../../d9/db9/classbool.html) shorten=true)  
static [Placement](../../d1/d10/classBase_1_1Placement.html) | [slerp](../../d1/d10/classBase_1_1Placement.html#a62fed3e2fa2d1a68e5d57bc4b89103f9) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &p0, const [Placement](../../d1/d10/classBase_1_1Placement.html) &p1, double t)  
  
## Detailed Description

The [Placement](../../d1/d10/classBase_1_1Placement.html "The Placement
class.") class.

## Constructor & Destructor Documentation

## ◆ Placement() [1/5]

Placement::Placement  | ( | void  | | ) |   
---|---|---|---|---|---  
  
default constructor

Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[fromDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f),
[PartDesign::ProfileBased::getProfileNormal()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#af389a14c1da76e8ce4aa4dd5dc874540),
[PartDesign::ProfileBased::getReversedAngle()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a3b3aa636b6181cd9edacd1f7b1412f0b),
[slerp()](../../d1/d10/classBase_1_1Placement.html#a62fed3e2fa2d1a68e5d57bc4b89103f9),
and
[PartDesign::ShapeBinder::updatedShape()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a126f8b03ab46e56d65b7fbd3d41b98e8).

## ◆ Placement() [2/5]

Placement::Placement  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _that_| ) |   
---|---|---|---|---|---  
  
## ◆ Placement() [3/5]

Placement::Placement  | ( | const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _matrix_| ) |   
---|---|---|---|---|---  
  
References
[fromMatrix()](../../d1/d10/classBase_1_1Placement.html#a4ddd9ad8b2ce05003b4cfe79b3c253df).

## ◆ Placement() [4/5]

Placement::Placement  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _Pos_ ,   
---|---|---|---  
|  | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _Rot_  
| ) | |   
  
## ◆ Placement() [5/5]

Placement::Placement  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _Pos_ ,   
---|---|---|---  
|  | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _Rot_ ,   
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _Cnt_  
| ) | |   
  
## ◆ ~Placement()

Base::Placement::~Placement  | ( | | ) |   
---|---|---|---|---  
  
Destruction.

## Member Function Documentation

## ◆ fromDualQuaternion()

| [Placement](../../d1/d10/classBase_1_1Placement.html) Placement::fromDualQuaternion  | ( | [DualQuat](../../d4/d13/classBase_1_1DualQuat.html) | _qq_| ) |   
---|---|---|---|---|---  
static  
  
specialty constructors

References
[Base::DualQuat::conj()](../../d4/d13/classBase_1_1DualQuat.html#a7c0cd20685b8952925c16d40f15020c1),
[Base::DualQuat::dual()](../../d4/d13/classBase_1_1DualQuat.html#a224c123d9815f260a401c3b04484d552),
[Placement()](../../d1/d10/classBase_1_1Placement.html#aa0020a3dd0bedb34998968adfacf8a4e),
[Base::DualNumber::re](../../db/d4b/classBase_1_1DualNumber.html#ab26956904e8b78d862b574cbdcbe6113),
[Base::DualQuat::real()](../../d4/d13/classBase_1_1DualQuat.html#a27d1d5fb87cb51eff9fcbc1a30426058),
[Base::DualQuat::w](../../d4/d13/classBase_1_1DualQuat.html#ae9de981d482e291defa8eee4cf6487f1),
[Base::DualQuat::x](../../d4/d13/classBase_1_1DualQuat.html#af0a8c368d6987ed9fc05dd1b594da78f),
[Base::DualQuat::y](../../d4/d13/classBase_1_1DualQuat.html#a4fb8157ef0805ba6011343b2a0c7eb7c),
and
[Base::DualQuat::z](../../d4/d13/classBase_1_1DualQuat.html#a2299a66bb636cd1ec8f243e00ea97015).

Referenced by
[pow()](../../d1/d10/classBase_1_1Placement.html#a109a0d383d74255f0ae18f12b5861bca).

## ◆ fromMatrix()

void Placement::fromMatrix  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _m_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Part::Reverse::execute()](../../d4/d24/classPart_1_1Reverse.html#a22150a83fa78387e05f60dd1e08d31f8),
[Mesh::Feature::onChanged()](../../dd/dce/classMesh_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Points::Feature::onChanged()](../../d8/de3/classPoints_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Part::Feature::onChanged()](../../d7/d7e/classPart_1_1Feature.html#a17178c5bf097534e84b20380ad13563b),
[Placement()](../../d1/d10/classBase_1_1Placement.html#a94c0cf87ac294b9c4456a39fce51798d),
and
[App::PropertyPlacement::setPyObject()](../../da/d51/classApp_1_1PropertyPlacement.html#a30868378554db499b38da470bfa520d7).

## ◆ getPosition()

const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & Base::Placement::getPosition  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[Import::ExportOCAF::createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[Part::Tools::fromPlacement()](../../d9/d36/classPart_1_1Tools.html#a545eed1fde2f3eae32b94b5d24f6e960),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[Part::Datum::getBasePoint()](../../db/d0b/classPart_1_1Datum.html#a616fe8e09f6a099b06a100535175c50c),
[Part::Feature::getLocation()](../../d7/d7e/classPart_1_1Feature.html#a84164b4adfe9b6ecef87da8d7aa1ac9d),
[Part::FeatureReference::getLocation()](../../d2/da1/classPart_1_1FeatureReference.html#aee6f4d426e17d5a0193108fd06f7309c),
[PartDesign::Point::getPoint()](../../da/d0d/classPartDesign_1_1Point.html#a425bd8831010df262ca4482511fca22a),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
[PartGui::Location::Location()](../../db/d6f/classPartGui_1_1Location.html#a2f77946d77e8f18590ccf3f7e73a18b4),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[Path::Toolpath::recalculate()](../../d6/d0c/classPath_1_1Toolpath.html#a6fcb5afb3f1023ef686cd87b4f69c0f9),
[Part::Geometry::rotate()](../../dc/df0/classPart_1_1Geometry.html#a3c7ebf21592da6737fccb28bf9508a75),
[Robot::Robot6Axis::Save()](../../dc/d5f/classRobot_1_1Robot6Axis.html#a7cf092c9dc75bf16fe3b6a01d9fa03d4),
[Robot::Waypoint::Save()](../../d1/dc7/classRobot_1_1Waypoint.html#a2d0f51a0e8e89f1148887af8e2eb0537),
[Import::ExportOCAF::saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[RobotGui::ViewProviderRobotObject::setDragger()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a7a94208ad67ec05ebc9013cac68d34f4),
[SketcherGui::ViewProviderSketch::setEditViewer()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a7ecefc8f26a51435051a12a6fb73f333),
[Path::Command::setFromPlacement()](../../d7/d2e/classPath_1_1Command.html#a62372d49bbf1003cc81fe7035c7b592e),
[Part::TopoShape::setShapePlacement()](../../d8/ded/classPart_1_1TopoShape.html#a8ae38d04353d5ccc4c60beaad3a4a497),
[Robot::Robot6Axis::setTo()](../../dc/d5f/classRobot_1_1Robot6Axis.html#aab85201da375f6505bb724ce7bdcd640),
[slerp()](../../d1/d10/classBase_1_1Placement.html#a62fed3e2fa2d1a68e5d57bc4b89103f9),
[Robot::toFrame()](../../da/d93/namespaceRobot.html#a1811898b0051d5279cc7467b03bac0be),
[Gui::View3DInventorViewer::toggleClippingPlane()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ae41b2cfdc548e959d744937ff7a85317),
[Path::Command::transform()](../../d7/d2e/classPath_1_1Command.html#a86423c625f09285dd820b578462c199e),
[Point3D::UpdateCmd()](../../d5/d01/structPoint3D.html#aed6a7225b9616e32f4c86b174c640028),
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
[RobotGui::ViewProviderTrajectory::updateData()](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#a653032eb34a2fc66e326c0d0e9066287),
[Gui::ViewProviderLink::updateDraggingPlacement()](../../d6/d59/classGui_1_1ViewProviderLink.html#a30d3a1d233bff54143b068d64af490eb),
[Gui::ViewProviderDragger::updateTransform()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5f8676364e82e30b6e558c8f25e06b88),
[RobotGui::TaskTrajectoryDressUpParameter::viewPlacement()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#acf61f87e511a7480c2dfa829800e17cc),
[Gui::View3DInventorPy::viewPosition()](../../d3/df7/classGui_1_1View3DInventorPy.html#aa0c6354d70103dbcf7f4fddc2c12265d),
[Path::PathSegmentWalker::walk()](../../d0/d7b/classPath_1_1PathSegmentWalker.html#a2d2253be4424a16caf28ec136b658dc6),
and
[Points::PcdWriter::write()](../../df/dc2/classPoints_1_1PcdWriter.html#a29a665c849f6da4f82ba12eb6bf06095).

## ◆ getRotation()

const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & Base::Placement::getRotation  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Import::ExportOCAF::createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[Part::Tools::fromPlacement()](../../d9/d36/classPart_1_1Tools.html#a545eed1fde2f3eae32b94b5d24f6e960),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[PartDesign::Line::getDirection()](../../d0/d2a/classPartDesign_1_1Line.html#af89a81d14e0ccb27353122f43844600c),
[Part::Feature::getLocation()](../../d7/d7e/classPart_1_1Feature.html#a84164b4adfe9b6ecef87da8d7aa1ac9d),
[Part::FeatureReference::getLocation()](../../d2/da1/classPart_1_1FeatureReference.html#aee6f4d426e17d5a0193108fd06f7309c),
[PartDesign::Plane::getNormal()](../../df/df0/classPartDesign_1_1Plane.html#ad208270773ba2e063212171e36895e6e),
[PartDesign::ProfileBased::getProfileNormal()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#af389a14c1da76e8ce4aa4dd5dc874540),
[PartDesign::ProfileBased::getReversedAngle()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a3b3aa636b6181cd9edacd1f7b1412f0b),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[PartDesign::CoordinateSystem::getXAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a04498f548e650362eb2c094f89f5470b),
[PartDesign::CoordinateSystem::getYAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a38beb2d58454d7cb970b4dfb222fe8d3),
[PartDesign::CoordinateSystem::getZAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a4b9edd67bb7f8c895a9f5bd726fb92e2),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
[Attacher::AttachEngine::placementFactory()](../../d2/d85/classAttacher_1_1AttachEngine.html#a0eff77539401a8d4a04554a970bd85b4),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[Part::Geometry::rotate()](../../dc/df0/classPart_1_1Geometry.html#a3c7ebf21592da6737fccb28bf9508a75),
[Robot::Robot6Axis::Save()](../../dc/d5f/classRobot_1_1Robot6Axis.html#a7cf092c9dc75bf16fe3b6a01d9fa03d4),
[Robot::Waypoint::Save()](../../d1/dc7/classRobot_1_1Waypoint.html#a2d0f51a0e8e89f1148887af8e2eb0537),
[Import::ExportOCAF::saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[RobotGui::ViewProviderRobotObject::setDragger()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a7a94208ad67ec05ebc9013cac68d34f4),
[SketcherGui::ViewProviderSketch::setEditViewer()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a7ecefc8f26a51435051a12a6fb73f333),
[Path::Command::setFromPlacement()](../../d7/d2e/classPath_1_1Command.html#a62372d49bbf1003cc81fe7035c7b592e),
[Part::TopoShape::setShapePlacement()](../../d8/ded/classPart_1_1TopoShape.html#a8ae38d04353d5ccc4c60beaad3a4a497),
[Robot::Robot6Axis::setTo()](../../dc/d5f/classRobot_1_1Robot6Axis.html#aab85201da375f6505bb724ce7bdcd640),
[slerp()](../../d1/d10/classBase_1_1Placement.html#a62fed3e2fa2d1a68e5d57bc4b89103f9),
[Robot::toFrame()](../../da/d93/namespaceRobot.html#a1811898b0051d5279cc7467b03bac0be),
[Gui::View3DInventorViewer::toggleClippingPlane()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ae41b2cfdc548e959d744937ff7a85317),
[Path::Command::transform()](../../d7/d2e/classPath_1_1Command.html#a86423c625f09285dd820b578462c199e),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
[Gui::ViewProviderLink::updateDraggingPlacement()](../../d6/d59/classGui_1_1ViewProviderLink.html#a30d3a1d233bff54143b068d64af490eb),
[Gui::ViewProviderDragger::updateTransform()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5f8676364e82e30b6e558c8f25e06b88),
[RobotGui::TaskTrajectoryDressUpParameter::viewPlacement()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#acf61f87e511a7480c2dfa829800e17cc),
[Gui::View3DInventorPy::viewPosition()](../../d3/df7/classGui_1_1View3DInventorPy.html#aa0c6354d70103dbcf7f4fddc2c12265d),
[Points::PlyWriter::write()](../../d4/d57/classPoints_1_1PlyWriter.html#afcad40b7eec0e6e291d5bb1ffc6b0014),
and
[Points::PcdWriter::write()](../../df/dc2/classPoints_1_1PcdWriter.html#a29a665c849f6da4f82ba12eb6bf06095).

## ◆ inverse()

[Placement](../../d1/d10/classBase_1_1Placement.html) Placement::inverse  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[Sketcher::SketchAnalysis::getOpenVertices()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#ab5e084231887ad48de90a03ec8aa3f62),
[Gui::ViewProviderLink::initDraggingPlacement()](../../d6/d59/classGui_1_1ViewProviderLink.html#a1386127ddc37cfa7078215b347149a71),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[Robot::Simulation::reset()](../../de/d71/classRobot_1_1Simulation.html#a25a74df026be6c3d7cfc0afc4dbdaddb),
[sclerp()](../../d1/d10/classBase_1_1Placement.html#af9f3428f4cec9051afe44b46d90e6a4a),
[RobotGui::ViewProviderRobotObject::setAxisTo()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#aed595606c9254fe301f2c69741204058),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[Robot::Simulation::setToTime()](../../de/d71/classRobot_1_1Simulation.html#aede0681765a560eb8e4e3c640fc72b55),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
and
[PartDesign::ShapeBinder::updatedShape()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a126f8b03ab46e56d65b7fbd3d41b98e8).

## ◆ invert()

void Placement::invert  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[PathScripts.PathDressupLeadInOut.ObjectDressup::getLeadEnd()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#ac4be8c95d4aa1440fb03c096c4e44e57),
[PathScripts.PathDressupLeadInOut.ObjectDressup::getLeadStart()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#a2d9de34620ee069b425e7f99f0efe9da),
[MeshGui::ViewProviderMesh::partMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a252f3b9789355271cbc9ff56a65ba495),
[MeshGui::ViewProviderMesh::segmMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#af03a51bed2f5b62f24d2aecf1e03c4b4),
and
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f).

## ◆ isIdentity()

[bool](../../d9/db9/classbool.html) Placement::isIdentity  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[ArchComponent.Component::applyShape()](../../de/d87/classArchComponent_1_1Component.html#ac8174503690f56dcf8b6d8e324fadbc5),
[ArchComponent.Component::getExtrusionData()](../../de/d87/classArchComponent_1_1Component.html#abe6b1db0166c4b8edb14db2440ab4919),
[ArchComponent.Component::processSubShapes()](../../de/d87/classArchComponent_1_1Component.html#a34cd7509406ea5e01a1d72b41e900742),
[Points::AscWriter::write()](../../d1/d45/classPoints_1_1AscWriter.html#a0be300b10580fe3f4666bddb84d4d8bd),
[Points::PlyWriter::write()](../../d4/d57/classPoints_1_1PlyWriter.html#afcad40b7eec0e6e291d5bb1ffc6b0014),
and
[Points::PcdWriter::write()](../../df/dc2/classPoints_1_1PcdWriter.html#a29a665c849f6da4f82ba12eb6bf06095).

## ◆ move()

void Placement::move  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _MovVec_| ) |   
---|---|---|---|---|---  
  
Referenced by
[draftguitools.gui_circulararray.CircularArray::Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
and
[draftguitools.gui_polararray.PolarArray::Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6).

## ◆ multVec()

void Placement::multVec  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _src_ ,   
---|---|---|---  
|  | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _dst_  
| ) | |  const  
  
Referenced by
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[Sketcher::SketchAnalysis::getOpenVertices()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#ab5e084231887ad48de90a03ec8aa3f62),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[PathGui::ViewProviderPath::recomputeBoundingBox()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a4a681a533fc16dba93a80bc3fdfc21c3),
[Points::PlyWriter::write()](../../d4/d57/classPoints_1_1PlyWriter.html#afcad40b7eec0e6e291d5bb1ffc6b0014),
and
[Points::PcdWriter::write()](../../df/dc2/classPoints_1_1PcdWriter.html#a29a665c849f6da4f82ba12eb6bf06095).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) Placement::operator!=  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator*()

[Placement](../../d1/d10/classBase_1_1Placement.html) Placement::operator*  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _p_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator*=()

[Placement](../../d1/d10/classBase_1_1Placement.html) & Placement::operator*=  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _p_| ) |   
---|---|---|---|---|---  
  
Operators.

## ◆ operator=()

[Placement](../../d1/d10/classBase_1_1Placement.html) & Placement::operator=  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _New_| ) |   
---|---|---|---|---|---  
  
## ◆ operator==()

[bool](../../d9/db9/classbool.html) Placement::operator==  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
## ◆ pow()

[Placement](../../d1/d10/classBase_1_1Placement.html) Placement::pow  | ( | double  | _t_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _shorten_ = `true`  
| ) | |  const  
  
References
[fromDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a2d1b64e6bae074f5c7568397ae65ef6f),
[pow()](../../d1/d10/classBase_1_1Placement.html#a109a0d383d74255f0ae18f12b5861bca),
and
[toDualQuaternion()](../../d1/d10/classBase_1_1Placement.html#a700572ce02a191128a6c097d2212562d).

Referenced by
[pow()](../../d1/d10/classBase_1_1Placement.html#a109a0d383d74255f0ae18f12b5861bca),
and
[sclerp()](../../d1/d10/classBase_1_1Placement.html#af9f3428f4cec9051afe44b46d90e6a4a).

## ◆ sclerp()

| [Placement](../../d1/d10/classBase_1_1Placement.html) Placement::sclerp  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _p0_ ,   
---|---|---|---  
|  | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _p1_ ,   
|  | double  | _t_ ,   
|  | [bool](../../d9/db9/classbool.html) | _shorten_ = `true`  
| ) | |   
static  
  
References
[inverse()](../../d1/d10/classBase_1_1Placement.html#a882753578fa58a54d0e4d05764a33ed3),
and
[pow()](../../d1/d10/classBase_1_1Placement.html#a109a0d383d74255f0ae18f12b5861bca).

## ◆ setPosition()

void Base::Placement::setPosition  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _Pos_| ) |   
---|---|---|---|---|---  
  
Referenced by
[PathSimulator::PathSim::ApplyCommand()](../../d4/d82/classPathSimulator_1_1PathSim.html#a3bd3bbe370b27eabfceed51d07afef05),
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Gui::ManualAlignment::computeAlignment()](../../d7/d97/classGui_1_1ManualAlignment.html#aff085ba77f9c444b8aada36102b3879b),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
and
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e).

## ◆ setRotation()

void Base::Placement::setRotation  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _Rot_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
and
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e).

## ◆ slerp()

| [Placement](../../d1/d10/classBase_1_1Placement.html) Placement::slerp  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _p0_ ,   
---|---|---|---  
|  | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _p1_ ,   
|  | double  | _t_  
| ) | |   
static  
  
References
[getPosition()](../../d1/d10/classBase_1_1Placement.html#aa0992c263f42f61da22594eb7f4a9a13),
[getRotation()](../../d1/d10/classBase_1_1Placement.html#af5b5009ff533f306ed03d5259bfb6797),
[Placement()](../../d1/d10/classBase_1_1Placement.html#aa0020a3dd0bedb34998968adfacf8a4e),
and
[Base::Rotation::slerp()](../../d4/d18/classBase_1_1Rotation.html#ad8eeefc5709d927b052bf0199c49be3c).

## ◆ toDualQuaternion()

[DualQuat](../../d4/d13/classBase_1_1DualQuat.html) Placement::toDualQuaternion  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Base::DualNumber::re](../../db/d4b/classBase_1_1DualNumber.html#ab26956904e8b78d862b574cbdcbe6113),
[Base::DualQuat::w](../../d4/d13/classBase_1_1DualQuat.html#ae9de981d482e291defa8eee4cf6487f1),
[Base::DualQuat::x](../../d4/d13/classBase_1_1DualQuat.html#af0a8c368d6987ed9fc05dd1b594da78f),
[Base::DualQuat::y](../../d4/d13/classBase_1_1DualQuat.html#a4fb8157ef0805ba6011343b2a0c7eb7c),
and
[Base::DualQuat::z](../../d4/d13/classBase_1_1DualQuat.html#a2299a66bb636cd1ec8f243e00ea97015).

Referenced by
[pow()](../../d1/d10/classBase_1_1Placement.html#a109a0d383d74255f0ae18f12b5861bca).

## ◆ toMatrix()

[Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) Placement::toMatrix  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Gui::Dialog::TransformStrategy::acceptDataTransform()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a7eef0b122a11900cca84fcf149180e90),
[Gui::Dialog::TransformStrategy::applyViewTransform()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a3b0ef5872b6be50f8e2cb58b460113f3),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[App::GeoFeatureGroupExtension::extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[App::OriginGroupExtension::extensionGetSubObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11),
[Part::Datum::getSubObject()](../../db/d0b/classPart_1_1Datum.html#ac5c48627e7edd4fde0e66a86603a0ca8),
[Part::Feature::getSubObject()](../../d7/d7e/classPart_1_1Feature.html#adf8612028b19407896b5ba0e1fab0d5d),
[PartDesign::Body::getSubObject()](../../dd/db8/classPartDesign_1_1Body.html#aecc131a5ce7f03c5041a475003456b38),
[PartDesign::CoordinateSystem::getSubObject()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#aeb5d09866ebc21adafb8ee43acc9205b),
[PartDesign::SubShapeBinder::getSubObject()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#afb7e01deac9646afcd5dc1b2aa07042b),
[TechDraw::ShapeExtractor::getXShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4e820635335afa9ce7506faaf4274cbd),
[Gui::ViewProviderLink::initDraggingPlacement()](../../d6/d59/classGui_1_1ViewProviderLink.html#a1386127ddc37cfa7078215b347149a71),
[Gui::Dialog::Transform::on_applyButton_clicked()](../../d0/d8f/classGui_1_1Dialog_1_1Transform.html#aa736a36e69d76427b945f434e46f3a2a),
[Mesh::Feature::onChanged()](../../dd/dce/classMesh_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Points::Feature::onChanged()](../../d8/de3/classPoints_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Part::Feature::onChanged()](../../d7/d7e/classPart_1_1Feature.html#a17178c5bf097534e84b20380ad13563b),
[MeshGui::ViewProviderMesh::partMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a252f3b9789355271cbc9ff56a65ba495),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[Gui::Dialog::TransformStrategy::resetViewTransform()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#af5a0cbfc3f8a966c735d6a8ea0ddc451),
[MeshGui::ViewProviderMesh::segmMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#af03a51bed2f5b62f24d2aecf1e03c4b4),
[Gui::ViewProviderDragger::setEditViewer()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5746c8658c714b1910627ea804ca2353),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[Data::ComplexGeoData::setPlacement()](../../d8/daf/classData_1_1ComplexGeoData.html#a10256d4773fd4bca781076692aea8ae0),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f),
[Gui::ViewProviderLink::updateDraggingPlacement()](../../d6/d59/classGui_1_1ViewProviderLink.html#a30d3a1d233bff54143b068d64af490eb),
and
[Points::AscWriter::write()](../../d1/d45/classPoints_1_1AscWriter.html#a0be300b10580fe3f4666bddb84d4d8bd).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Placement.h
  * FreeCAD/src/Base/Placement.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

