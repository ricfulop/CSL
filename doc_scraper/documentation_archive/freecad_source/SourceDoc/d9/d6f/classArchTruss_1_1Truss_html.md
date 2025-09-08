---
url: https://freecad.github.io/SourceDoc/d9/d6f/classArchTruss_1_1Truss.html
scraped_at: 2025-09-08T14:58:37.424243
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchTruss](../../d5/d20/namespaceArchTruss.html)
  * [Truss](../../d9/d6f/classArchTruss_1_1Truss.html)

[List of all members](../../da/d83/classArchTruss_1_1Truss-members.html) | Public Member Functions | Public Attributes

ArchTruss.Truss Class Reference

##  Public Member Functions  
  
---  
def | [execute](../../d9/d6f/classArchTruss_1_1Truss.html#a9d12be1826d5cef997f94a1cd7a982f5) (self, obj)  
def | [makeRod](../../d9/d6f/classArchTruss_1_1Truss.html#a338dddf795b964965b1d547cf7419c1f) (self, profile, p1, p2)  
def | [makeTruss](../../d9/d6f/classArchTruss_1_1Truss.html#aef44ace1794de6d0243ba909e224023c) (self, obj, v0, v1)  
def | [onChanged](../../d9/d6f/classArchTruss_1_1Truss.html#ad5bacb59d6610e87c0aad5a4dc7f8987) (self, obj, prop)  
def | [onDocumentRestored](../../d9/d6f/classArchTruss_1_1Truss.html#abf7290b67c66f8b38f2f24c3a913eb7d) (self, obj)  
def | [setProperties](../../d9/d6f/classArchTruss_1_1Truss.html#a90f32bb2105867d75078e021f1ba771c) (self, obj)  
![-](../../closed.png) Public Member Functions inherited from
[ArchComponent.Component](../../de/d87/classArchComponent_1_1Component.html)  
def | [applyShape](../../de/d87/classArchComponent_1_1Component.html#ac8174503690f56dcf8b6d8e324fadbc5) (self, obj, shape, placement, allowinvalid=False, allownosolid=False)  
def | [clone](../../de/d87/classArchComponent_1_1Component.html#ab93810706664c124d35dc837d91372b4) (self, obj)  
def | [computeAreas](../../de/d87/classArchComponent_1_1Component.html#af23d0698caaa5c6ec694c0a8b4f8f3e6) (self, obj)  
def | [execute](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0) (self, obj)  
def | [getExtrusionData](../../de/d87/classArchComponent_1_1Component.html#abe6b1db0166c4b8edb14db2440ab4919) (self, obj)  
def | [getHosts](../../de/d87/classArchComponent_1_1Component.html#a4c7fe364d25e6d931fab1823ea024975) (self, obj)  
def | [getMovableChildren](../../de/d87/classArchComponent_1_1Component.html#acf355ffe37a4948f43d6a19688f8ff9b) (self, obj)  
def | [getParentHeight](../../de/d87/classArchComponent_1_1Component.html#ab220dba4a4f79ceab3c92e55185e5fe5) (self, obj)  
def | [getSiblings](../../de/d87/classArchComponent_1_1Component.html#a381a9402b9f978bf0f83f309988052d3) (self, obj)  
def | [hideSubobjects](../../de/d87/classArchComponent_1_1Component.html#a043037f6b8940a7430671daa9815752a) (self, obj, prop)  
def | [isIdentity](../../de/d87/classArchComponent_1_1Component.html#a21fbace2d08d1a4f696bbddba0963672) (self, placement)  
def | [isStandardCase](../../de/d87/classArchComponent_1_1Component.html#af2c3c0a1f335c71dcac25ba7ef6260da) (self, obj)  
def | [onBeforeChange](../../de/d87/classArchComponent_1_1Component.html#a7aadae31ca64581e8cc1c31fe086736b) (self, obj, prop)  
def | [onChanged](../../de/d87/classArchComponent_1_1Component.html#ac10328dd9515bdac2dd7e11861c4609e) (self, obj, prop)  
def | [onDocumentRestored](../../de/d87/classArchComponent_1_1Component.html#a6265ff6904fa2e9eb9ac4ee3dfcfaa67) (self, obj)  
def | [processSubShapes](../../de/d87/classArchComponent_1_1Component.html#a34cd7509406ea5e01a1d72b41e900742) (self, obj, base, placement=None)  
def | [rebase](../../de/d87/classArchComponent_1_1Component.html#a3ca88a3aab563db817a7bb54fbd16eaa) (self, shape, hint=None)  
def | [setProperties](../../de/d87/classArchComponent_1_1Component.html#a83f183119924946069f3b00947ec9793) (self, obj)  
def | [spread](../../de/d87/classArchComponent_1_1Component.html#a9aa897ac64c7072468e23fee445dd2df) (self, obj, shape, placement=None)  
![-](../../closed.png) Public Member Functions inherited from
[ArchIFC.IfcProduct](../../d9/db7/classArchIFC_1_1IfcProduct.html)  
def | [getIfcSchema](../../d9/db7/classArchIFC_1_1IfcProduct.html#a29f8b58103b9a31db34fc38480a831c9) (self)  
![-](../../closed.png) Public Member Functions inherited from
[ArchIFC.IfcRoot](../../d4/da7/classArchIFC_1_1IfcRoot.html)  
def | [addIfcAttribute](../../d4/da7/classArchIFC_1_1IfcRoot.html#ab7c9808570241f10e88758d133847126) (self, obj, attribute)  
def | [addIfcAttributes](../../d4/da7/classArchIFC_1_1IfcRoot.html#aa5ebaf1c079500bd27c59afbb27d3187) (self, ifcTypeSchema, obj)  
def | [addIfcAttributeValueExpressions](../../d4/da7/classArchIFC_1_1IfcRoot.html#a906dec9543d3dbf5d07d4d06bb03ea71) (self, obj, attribute)  
def | [getCanonicalisedIfcTypes](../../d4/da7/classArchIFC_1_1IfcRoot.html#a8db35c1d257efce75535aa22f5423d72) (self)  
def | [getIfcAttributeSchema](../../d4/da7/classArchIFC_1_1IfcRoot.html#a2ab9341d531f46f4e2cfc298b88653f5) (self, ifcTypeSchema, name)  
def | [getIfcSchema](../../d4/da7/classArchIFC_1_1IfcRoot.html#a1abc46a43fd39bed50ffd2fe0329cccf) (self)  
def | [getIfcTypeSchema](../../d4/da7/classArchIFC_1_1IfcRoot.html#a7f15ded5bae325bfd4f920d1533e5a5e) (self, IfcType)  
def | [getObjIfcComplexAttribute](../../d4/da7/classArchIFC_1_1IfcRoot.html#abd6e51a58b1c8aed5893cd0cf43f63bb) (self, obj, attributeName)  
def | [migrateDeprecatedAttributes](../../d4/da7/classArchIFC_1_1IfcRoot.html#a503f3b8410e6533d4185e24102637af2) (self, obj)  
def | [onChanged](../../d4/da7/classArchIFC_1_1IfcRoot.html#abde72ec687dc6401837824722d16d9ea) (self, obj, prop)  
def | [purgeUnusedIfcAttributesFromPropertiesList](../../d4/da7/classArchIFC_1_1IfcRoot.html#a3d4b25db8f94b4810f5fcef008b021ab) (self, ifcTypeSchema, obj)  
def | [setObjIfcAttributeValue](../../d4/da7/classArchIFC_1_1IfcRoot.html#a5f1380f722823e4fac892a1a05076256) (self, obj, attributeName, value)  
def | [setObjIfcComplexAttributeValue](../../d4/da7/classArchIFC_1_1IfcRoot.html#a320c53d77ddddee77dcd33ecbb0fcb44) (self, obj, attributeName, value)  
def | [setProperties](../../d4/da7/classArchIFC_1_1IfcRoot.html#a085b21fd2e99fa8a5ac287d97fbe7fa2) (self, obj)  
def | [setupIfcAttributes](../../d4/da7/classArchIFC_1_1IfcRoot.html#af4c72df4764acc9c3f0edd77cce20627) (self, obj)  
def | [setupIfcComplexAttributes](../../d4/da7/classArchIFC_1_1IfcRoot.html#a6f01e2ef7ddbae31c1816317023b9d68) (self, obj)  
  
##  Public Attributes  
  
---  
|
[Type](../../d9/d6f/classArchTruss_1_1Truss.html#a1660bf4d5d226841974b618b2eec7c95)  
![-](../../closed.png) Public Attributes inherited from
[ArchComponent.Component](../../de/d87/classArchComponent_1_1Component.html)  
|
[flatarea](../../de/d87/classArchComponent_1_1Component.html#ae720ca998b1a9025db9befc4a76e86f6)  
|
[oldPlacement](../../de/d87/classArchComponent_1_1Component.html#af40cf016bc380869efd09f5aa6ea3414)  
|
[Subvolume](../../de/d87/classArchComponent_1_1Component.html#a84bce77b75fe58fef743b31b1b150894)  
|
[Type](../../de/d87/classArchComponent_1_1Component.html#a4a5c3bb5d5f50162eca9c62b01ec1e32)  
  
## Member Function Documentation

## ◆ execute()

def ArchTruss.Truss.execute  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Method run when the object is recomputed.
    
    If the object is a clone, just copy the shape it's cloned from.
    
    Process subshapes of the object to add additions, and subtract
    subtractions from the object's shape.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    

Reimplemented from
[ArchComponent.Component](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0).

References
[ArchComponent.Component.applyShape()](../../de/d87/classArchComponent_1_1Component.html#ac8174503690f56dcf8b6d8e324fadbc5),
[Gui::ViewProviderIndex.clone()](../../d7/d9c/classGui_1_1ViewProviderIndex.html#aef5850a15ecf9f15ee1571b49c9fa3b9),
[zipios::BasicEntry.clone()](../../dc/d7d/classzipios_1_1BasicEntry.html#a9c274a7b57d0519253fe2b2d12a75a92),
[zipios::CollectionCollection.clone()](../../da/d40/classzipios_1_1CollectionCollection.html#a99ed2bc3edc3c1e5bb692781deb747dd),
[zipios::DirectoryCollection.clone()](../../d7/dbb/classzipios_1_1DirectoryCollection.html#aef7e94a08e1e5b8f002bc3be80a371da),
[zipios::ZipFile.clone()](../../d7/da4/classzipios_1_1ZipFile.html#ab016b034e27e2b1ba35142339d7db9dc),
[zipios::ZipLocalEntry.clone()](../../db/d3e/classzipios_1_1ZipLocalEntry.html#ab3a48c212501d253c318398db1ce9565),
[zipios::ZipCDirEntry.clone()](../../dd/d8d/classzipios_1_1ZipCDirEntry.html#a1cf55834ff50567843ea304927aec3ac),
[zipios::FileCollection.clone()](../../d1/d24/classzipios_1_1FileCollection.html#aeb132836833244acd41c559e1ba43d52),
[zipios::FileEntry.clone()](../../d9/d9c/classzipios_1_1FileEntry.html#a4061f768d90cec253d9a5c0cbc443449),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunctionSegment.clone()](../../d4/dac/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunctionSegment.html#a1354b5f743c2a57fa99cd802c4de9cfe),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.clone()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#ad92aa172c3deeaae22d2c9a323401581),
[ArchComponent.Component.clone()](../../de/d87/classArchComponent_1_1Component.html#ab93810706664c124d35dc837d91372b4),
[Part::Geometry.clone()](../../dc/df0/classPart_1_1Geometry.html#ad3be5f91131b02a9de99c83ef228ff53),
[Part::Geom2dPoint.clone()](../../d8/da9/classPart_1_1Geom2dPoint.html#aaaf4b2a388061f35865d6897e9081bb1),
[Part::Geom2dBezierCurve.clone()](../../d6/d50/classPart_1_1Geom2dBezierCurve.html#a82e08091c20c89225e4c726a9a48c3ca),
[Part::Geom2dBSplineCurve.clone()](../../dd/d59/classPart_1_1Geom2dBSplineCurve.html#a8d579a5140bc7731e83797828c63dc0f),
[Part::Geom2dCircle.clone()](../../d7/d4e/classPart_1_1Geom2dCircle.html#aae1e984e0f44acd16f4a59c613869f5f),
[Part::Geom2dArcOfCircle.clone()](../../de/d96/classPart_1_1Geom2dArcOfCircle.html#ab4dc84218ef0e67b7336ca7c09bf6f28),
[Part::Geom2dEllipse.clone()](../../db/db9/classPart_1_1Geom2dEllipse.html#a95ee3092c00dc91bc399b80e71a48e12),
[Part::Geom2dArcOfEllipse.clone()](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a89677aaa4fde4b370382b278ebf79fa0),
[Part::Geom2dHyperbola.clone()](../../d2/d95/classPart_1_1Geom2dHyperbola.html#a4da85b1f81ef8d35f7f47d4caddae2eb),
[Part::Geom2dArcOfHyperbola.clone()](../../dc/db7/classPart_1_1Geom2dArcOfHyperbola.html#a82b00ad89419ba8b74e21821176f0c05),
[Part::Geom2dParabola.clone()](../../d9/dff/classPart_1_1Geom2dParabola.html#acfd6a2ff4167b8d792220e4c442b5b02),
[Part::Geom2dArcOfParabola.clone()](../../d3/d95/classPart_1_1Geom2dArcOfParabola.html#abfac2e13d4a19e38643860054abcc3cf),
[Part::Geom2dLine.clone()](../../d2/d27/classPart_1_1Geom2dLine.html#a9272e2293131de4c2489989d870fd79b),
[Part::Geom2dLineSegment.clone()](../../df/ded/classPart_1_1Geom2dLineSegment.html#acf8cb720d25c40198e31d23be3fe1c71),
[Part::Geom2dOffsetCurve.clone()](../../d5/de5/classPart_1_1Geom2dOffsetCurve.html#a56b93f9fffb293a45292c7f213c801e9),
[Part::Geom2dTrimmedCurve.clone()](../../d8/da3/classPart_1_1Geom2dTrimmedCurve.html#a310737389c4e759c81782cbe02931153),
[Part::Geometry2d.clone()](../../d1/dad/classPart_1_1Geometry2d.html#ab3c7fdc2ef02c31130ca16adb9ba902f),
[Part::Geom2dConic.clone()](../../d8/d0d/classPart_1_1Geom2dConic.html#a7ab379470b34fda16d0c548a7667b539),
[Part::Geom2dArcOfConic.clone()](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html#af4125da0d13cfb8e0116cdeb2912ca71),
[PathTests.TestPathHelix.TestPathHelix.clone](../../d1/db0/classPathTests_1_1TestPathHelix_1_1TestPathHelix.html#afd98c1d369bc590c551b9ba37f62187f),
[Sketcher::Constraint.clone()](../../d6/def/classSketcher_1_1Constraint.html#ad70b52b49bc522b68eb48e969691b608),
[Sketcher::ExternalGeometryFacade.clone()](../../dd/d90/classSketcher_1_1ExternalGeometryFacade.html#aab93c0fd119a772b715452cac6f68371),
[Sketcher::GeometryFacade.clone()](../../d1/d73/classSketcher_1_1GeometryFacade.html#a9131fb2720921d0c9d68418634332d17),
[TechDraw::CosmeticVertex.clone()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a5a3a77432ca3ad0b30292e4080676229),
[TechDraw::CosmeticEdge.clone()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a37ae3ac809adc02b39554195495b2e59),
[TechDraw::CenterLine.clone()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a6dfa88a33924e240922b5643a8475ef1),
[TechDraw::GeomFormat.clone()](../../d7/d64/classTechDraw_1_1GeomFormat.html#ade8ce89cc1d68c0374c996ffe64d55ce),
[ArchTruss.Truss.makeTruss()](../../d9/d6f/classArchTruss_1_1Truss.html#aef44ace1794de6d0243ba909e224023c),
and
[ArchComponent.Component.processSubShapes()](../../de/d87/classArchComponent_1_1Component.html#a34cd7509406ea5e01a1d72b41e900742).

Referenced by
[draftobjects.facebinder.Facebinder.addSubobjects()](../../d9/d57/classdraftobjects_1_1facebinder_1_1Facebinder.html#a50c77c202a034ce7109bb93322ff6e4e),
[PathScripts.PathDressupDogbone.ObjectDressup.boneStateList()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#af7788dd97e3ca711047ebc4472cf9f21),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[PathScripts.PathDressupHoldingTags.ObjectTagDressup.generateTags()](../../de/dd2/classPathScripts_1_1PathDressupHoldingTags_1_1ObjectTagDressup.html#a0937c170df6457d4d7aa799c876584ae),
[ArchPanel.PanelCut.getWires()](../../d6/dbd/classArchPanel_1_1PanelCut.html#a61534af5c2a0125dde05e08a22025195),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[Mod.PartDesign.Scripts.DistanceBolt.DistanceBolt.onChanged()](../../d8/d9d/classMod_1_1PartDesign_1_1Scripts_1_1DistanceBolt_1_1DistanceBolt.html#a5899c4fe94fa654ae168588d09ec3674),
[Mod.PartDesign.Scripts.Epitrochoid.Epitrochoid.onChanged()](../../da/d92/classMod_1_1PartDesign_1_1Scripts_1_1Epitrochoid_1_1Epitrochoid.html#a666d03d55a3758fd5b580ecdf83ff046),
[Mod.PartDesign.Scripts.Parallelepiped.Parallelepiped.onChanged()](../../da/db1/classMod_1_1PartDesign_1_1Scripts_1_1Parallelepiped_1_1Parallelepiped.html#a7d58a665dbdb613ccf9830254b6b3a28),
[Mod.PartDesign.Scripts.Parallelepiped.BoxCylinder.onChanged()](../../dc/dc9/classMod_1_1PartDesign_1_1Scripts_1_1Parallelepiped_1_1BoxCylinder.html#a32f2314f8a81f2034ba5fb8902079e75),
[Mod.PartDesign.Scripts.Spring.MySpring.onChanged()](../../d3/d4c/classMod_1_1PartDesign_1_1Scripts_1_1Spring_1_1MySpring.html#a45b49877108608c2473da154cbf7980d),
[FeaturePython.DistanceBolt.onChanged()](../../d9/d7d/classFeaturePython_1_1DistanceBolt.html#a644c14797e2ed9043537de3c86f7fdf1),
[PathScripts.PathStock.StockFromBase.onChanged()](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#a2c3dfa73d2881d73e95ac79cb572e9b9),
[PathScripts.PathStock.StockCreateBox.onChanged()](../../d9/dd6/classPathScripts_1_1PathStock_1_1StockCreateBox.html#ae190342a16a7a1c726c7748b85bc36d7),
[PathScripts.PathStock.StockCreateCylinder.onChanged()](../../da/de2/classPathScripts_1_1PathStock_1_1StockCreateCylinder.html#aaee43a8f62bd342d2b16ff4268dd33c9),
[draftobjects.draftlink.DraftLink.onDocumentRestored()](../../d6/d1d/classdraftobjects_1_1draftlink_1_1DraftLink.html#ac93069a613e26475296ba7eba274a783),
[draftobjects.patharray.PathArray.onDocumentRestored()](../../de/dbe/classdraftobjects_1_1patharray_1_1PathArray.html#a6a3f3b5a3444a8e2bc12d61152100fd5),
and
[draftobjects.pathtwistedarray.PathTwistedArray.onDocumentRestored()](../../da/d1a/classdraftobjects_1_1pathtwistedarray_1_1PathTwistedArray.html#a780c1e365112f239b177875caa78103b).

## ◆ makeRod()

def ArchTruss.Truss.makeRod  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _profile_ ,   
|  |  | _p1_ ,   
|  |  | _p2_  
| ) | |   
      
    
    makes a rod by extruding profile between p1 and p2

Referenced by
[ArchTruss.Truss.makeTruss()](../../d9/d6f/classArchTruss_1_1Truss.html#aef44ace1794de6d0243ba909e224023c).

## ◆ makeTruss()

def ArchTruss.Truss.makeTruss  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _v0_ ,   
|  |  | _v1_  
| ) | |   
  
References
[ArchTruss.Truss.makeRod()](../../d9/d6f/classArchTruss_1_1Truss.html#a338dddf795b964965b1d547cf7419c1f).

Referenced by
[ArchTruss.Truss.execute()](../../d9/d6f/classArchTruss_1_1Truss.html#a9d12be1826d5cef997f94a1cd7a982f5).

## ◆ onChanged()

def ArchTruss.Truss.onChanged  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _prop_  
| ) | |   
      
    
    Method called when the object has a property changed.
    
    If "Placement" has changed, move any children components that have been
    set to move with their host, such that they stay in the same location
    to this component.
    
    Also call ArchIFC.IfcProduct.onChanged().
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    prop: string
        The name of the property that has changed.
    

Reimplemented from
[ArchComponent.Component](../../de/d87/classArchComponent_1_1Component.html#ac10328dd9515bdac2dd7e11861c4609e).

References
[ArchComponent.Component.onChanged()](../../de/d87/classArchComponent_1_1Component.html#ac10328dd9515bdac2dd7e11861c4609e).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft.attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire.execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[ArchBuildingPart.ViewProviderBuildingPart.updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut.updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet.updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel.updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer.updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ onDocumentRestored()

def ArchTruss.Truss.onDocumentRestored  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Method run when the document is restored. Re-add the Arch component properties.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    

Reimplemented from
[ArchComponent.Component](../../de/d87/classArchComponent_1_1Component.html#a6265ff6904fa2e9eb9ac4ee3dfcfaa67).

References
[ArchComponent.Component.onDocumentRestored()](../../de/d87/classArchComponent_1_1Component.html#a6265ff6904fa2e9eb9ac4ee3dfcfaa67),
ArchAxis._Axis.setProperties(), ArchAxisSystem._AxisSystem.setProperties(),
ArchBuilding._Building.setProperties(),
[ArchBuildingPart.BuildingPart.setProperties()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a01e29cb1d764fda7df9055fe009dbf35),
[ArchComponent.Component.setProperties()](../../de/d87/classArchComponent_1_1Component.html#a83f183119924946069f3b00947ec9793),
[ArchCurtainWall.CurtainWall.setProperties()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a1c7351250cd02e8b790e5ed84ebe7553),
ArchEquipment._Equipment.setProperties(), ArchFence._Fence.setProperties(),
ArchFloor._Floor.setProperties(), ArchFrame._Frame.setProperties(),
[ArchGrid.ArchGrid.setProperties()](../../d7/d52/classArchGrid_1_1ArchGrid.html#a229519e55602df9a0561e406eccbcd43),
[ArchIFC.IfcRoot.setProperties()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a085b21fd2e99fa8a5ac287d97fbe7fa2),
ArchMaterial._ArchMaterial.setProperties(), ArchPanel._Panel.setProperties(),
[ArchPanel.PanelView.setProperties()](../../dd/da0/classArchPanel_1_1PanelView.html#a4d88fc678e1545b9d6758274b79ff6de),
[ArchPanel.PanelCut.setProperties()](../../d6/dbd/classArchPanel_1_1PanelCut.html#ab647ec1cd91fa4c50475f46c709f2283),
[ArchPanel.PanelSheet.setProperties()](../../dc/d22/classArchPanel_1_1PanelSheet.html#a6f1bddeabda97604ae78d870456ce30c),
ArchPipe._ArchPipe.setProperties(),
ArchPipe._ArchPipeConnector.setProperties(),
ArchPrecast._Precast.setProperties(),
ArchPrecast._PrecastBeam.setProperties(),
ArchPrecast._PrecastIbeam.setProperties(),
ArchPrecast._PrecastPillar.setProperties(),
ArchPrecast._PrecastPanel.setProperties(),
ArchPrecast._PrecastSlab.setProperties(),
ArchPrecast._PrecastStairs.setProperties(),
ArchProject._Project.setProperties(), ArchRebar._Rebar.setProperties(),
[ArchReference.ArchReference.setProperties()](../../d3/d06/classArchReference_1_1ArchReference.html#a41a26333eb23a48bdb3271bed98296e5),
ArchRoof._Roof.setProperties(), ArchSchedule._ArchSchedule.setProperties(),
ArchSectionPlane._SectionPlane.setProperties(),
ArchSectionPlane._ArchDrawingView.setProperties(),
ArchSite._Site.setProperties(), ArchSpace._Space.setProperties(),
ArchStairs._Stairs.setProperties(), ArchStructure._Structure.setProperties(),
[ArchTruss.Truss.setProperties()](../../d9/d6f/classArchTruss_1_1Truss.html#a90f32bb2105867d75078e021f1ba771c),
ArchWall._Wall.setProperties(), ArchWindow._Window.setProperties(),
[draftobjects.hatch.Hatch.setProperties()](../../db/d7f/classdraftobjects_1_1hatch_1_1Hatch.html#a48c378dffc98e6b9f7ecac53074128da),
[draftobjects.shape2dview.Shape2DView.setProperties()](../../dc/d42/classdraftobjects_1_1shape2dview_1_1Shape2DView.html#aa3d3c084e10c9697c432ccf1ddee8928),
ArchAxis._ViewProviderAxis.setProperties(),
[ArchBuildingPart.ViewProviderBuildingPart.setProperties()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a16972577fb2b2bebf116c298b7f0f9da),
[ArchComponent.ViewProviderComponent.setProperties()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#abbd3e374ae515673bada8f848fbc98af),
ArchFence._ViewProviderFence.setProperties(),
[ArchPanel.ViewProviderPanelCut.setProperties()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a728ad185d4b895a95966a464948c1027),
[ArchPanel.ViewProviderPanelSheet.setProperties()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a36bba4eebef09728a582d6a4b3b71150),
ArchRebar._ViewProviderRebar.setProperties(),
[ArchReference.ViewProviderArchReference.setProperties()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#a7f9d1dadc048dd8e345d54d9b06629c9),
ArchSectionPlane._ViewProviderSectionPlane.setProperties(),
ArchSite._ViewProviderSite.setProperties(),
ArchSpace._ViewProviderSpace.setProperties(), and
ArchStructure._ViewProviderStructure.setProperties().

## ◆ setProperties()

def ArchTruss.Truss.setProperties  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Give the component its component specific properties, such as material.
    
    You can learn more about properties here:
    https://wiki.freecadweb.org/property
    

Reimplemented from
[ArchComponent.Component](../../de/d87/classArchComponent_1_1Component.html#a83f183119924946069f3b00947ec9793).

References
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4).

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[ArchBuildingPart.BuildingPart.onDocumentRestored()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a8029b4336a228315b03abd4cbe009001),
[ArchCurtainWall.CurtainWall.onDocumentRestored()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a95c6772213f7a083a0dd81eef6163150),
[ArchGrid.ArchGrid.onDocumentRestored()](../../d7/d52/classArchGrid_1_1ArchGrid.html#af3945be9606a8a88bdfdeb840068ca5d),
[ArchPanel.PanelView.onDocumentRestored()](../../dd/da0/classArchPanel_1_1PanelView.html#a6e956704109979457399259409b3c12e),
[ArchPanel.PanelCut.onDocumentRestored()](../../d6/dbd/classArchPanel_1_1PanelCut.html#a81bcbc2154418c01c75c606932184aee),
[ArchPanel.PanelSheet.onDocumentRestored()](../../dc/d22/classArchPanel_1_1PanelSheet.html#afb1ed907e00ab4c552d73f932a3beb6e),
[ArchTruss.Truss.onDocumentRestored()](../../d9/d6f/classArchTruss_1_1Truss.html#abf7290b67c66f8b38f2f24c3a913eb7d),
[draftobjects.hatch.Hatch.onDocumentRestored()](../../db/d7f/classdraftobjects_1_1hatch_1_1Hatch.html#a5f4a52b199d98d8ef1bf681170a39214),
[draftobjects.shape2dview.Shape2DView.onDocumentRestored()](../../dc/d42/classdraftobjects_1_1shape2dview_1_1Shape2DView.html#aeb419e3492426690e6df5043bdd8fbf3),
[ArchBuildingPart.ViewProviderBuildingPart.onDocumentRestored()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a77d1c4103e062b3ee3d06a348b25310f),
[ArchPanel.ViewProviderPanelCut.onDocumentRestored()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a97810dc3b020c64a4352d53c96ee8500),
and
[ArchPanel.ViewProviderPanelSheet.onDocumentRestored()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a4b5aa2a21de0a9ebd24cb59e54e54994).

## Member Data Documentation

## ◆ Type

ArchTruss.Truss.Type  
---  
  
Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftobjects.draft_annotation.DraftAnnotation.add_missing_properties_0v19()](../../d4/dca/classdraftobjects_1_1draft__annotation_1_1DraftAnnotation.html#a345b51b0cfae010e7e5574f0a84dd2f3),
[ArchStructure.StructSelectionObserver.addSelection()](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#ac984e4631db3078ffee1dc0fee52df74),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchComponent.Component.execute()](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0),
[draftobjects.layer.LayerContainer.execute()](../../de/d4d/classdraftobjects_1_1layer_1_1LayerContainer.html#a960d8cd7f03fe7426f8cac669671b513),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[draftobjects.layer.Layer.set_properties()](../../d0/ddc/classdraftobjects_1_1layer_1_1Layer.html#aa6a95fe93a36b884d61ef2c668de002e),
and
[ArchReference.ArchReference.setProperties()](../../d3/d06/classArchReference_1_1ArchReference.html#a41a26333eb23a48bdb3271bed98296e5).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchTruss.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

