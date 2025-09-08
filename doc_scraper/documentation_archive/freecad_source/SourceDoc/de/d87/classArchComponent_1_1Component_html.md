---
url: https://freecad.github.io/SourceDoc/de/d87/classArchComponent_1_1Component.html
scraped_at: 2025-09-08T14:57:34.232421
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchComponent](../../da/d62/namespaceArchComponent.html)
  * [Component](../../de/d87/classArchComponent_1_1Component.html)

[List of all members](../../d8/de9/classArchComponent_1_1Component-members.html) | Public Member Functions | Public Attributes

ArchComponent.Component Class Reference

##  Public Member Functions  
  
---  
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
[flatarea](../../de/d87/classArchComponent_1_1Component.html#ae720ca998b1a9025db9befc4a76e86f6)  
|
[oldPlacement](../../de/d87/classArchComponent_1_1Component.html#af40cf016bc380869efd09f5aa6ea3414)  
|
[Subvolume](../../de/d87/classArchComponent_1_1Component.html#a84bce77b75fe58fef743b31b1b150894)  
|
[Type](../../de/d87/classArchComponent_1_1Component.html#a4a5c3bb5d5f50162eca9c62b01ec1e32)  
  
## Detailed Description

    
    
    The Arch Component object.
    
    Acts as a base for all other Arch objects, such as Arch walls and Arch
    structures. Its properties and behaviours are common to all Arch objects.
    
    You can learn more about Arch Components, and the purpose of Arch
    Components here: https://wiki.freecadweb.org/Arch_Component
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The object to turn into an Arch Component
    

## Member Function Documentation

## ◆ applyShape()

def ArchComponent.Component.applyShape  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _shape_ ,   
|  |  | _placement_ ,   
|  |  | _allowinvalid_ = `False`,   
|  |  | _allownosolid_ = `False`  
| ) | |   
      
    
    Check the given shape, then assign it to the object.
    
    Check if the shape is valid, isn't null, and if it has volume. Remove
    redundant edges from the shape. Spread the shape to the "Axis" with
    method .spread().
    
    Set the object's Shape and Placement to the values given, if
    successful.
    
    Finally, run .computeAreas() method, to calculate the horizontal and
    vertical area of the shape.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    shape: <Part.Shape>
        The shape to check and apply to the object.
    placement: <Base.Placement>
        The placement to apply to the object.
    allowinvalid: bool, optional
        Whether to allow invalid shapes, or to throw an error.
    allownosolid: bool, optional
        Whether to allow non-solid shapes, or to throw an error.
    

References
[ArchComponent.Component.computeAreas()](../../de/d87/classArchComponent_1_1Component.html#af23d0698caaa5c6ec694c0a8b4f8f3e6),
ArchEquipment._Equipment.computeAreas(), ArchRoof._Roof.computeAreas(),
ArchSite._Site.computeAreas(), ArchWindow._Window.computeAreas(),
[Base::Placement.isIdentity()](../../d1/d10/classBase_1_1Placement.html#adaa1d82cad90e3d7438e55d51ef57fc8),
[Base::Rotation.isIdentity()](../../d4/d18/classBase_1_1Rotation.html#a969256cb1d71bfa521429992f930a5ea),
[ArchComponent.Component.isIdentity()](../../de/d87/classArchComponent_1_1Component.html#a21fbace2d08d1a4f696bbddba0963672),
and
[ArchComponent.Component.spread()](../../de/d87/classArchComponent_1_1Component.html#a9aa897ac64c7072468e23fee445dd2df).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
and
[ArchTruss.Truss.execute()](../../d9/d6f/classArchTruss_1_1Truss.html#a9d12be1826d5cef997f94a1cd7a982f5).

## ◆ clone()

def ArchComponent.Component.clone  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    If the object is a clone, copy the shape.
    
    If the object is a clone according to the "CloneOf" property, copy the
    object's shape and several properties relating to shape, such as
    "Length" and "Thickness".
    
    Only perform the copy if this object and the object it's a clone of are
    of the same type, or if the object has the type "Component" or
    "BuildingPart".
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    
    Returns
    -------
    bool
        True if the copy occurs, False if otherwise.
    

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchComponent.Component.execute()](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0),
[ArchCurtainWall.CurtainWall.execute()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a9bcd979b923081e0898b56f0191d1cb4),
[ArchTruss.Truss.execute()](../../d9/d6f/classArchTruss_1_1Truss.html#a9d12be1826d5cef997f94a1cd7a982f5),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.integrated()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#afa19ecd592715c309fe11b98ba09c52f),
and
[PathTests.TestPathHelix.TestPathHelix.test04()](../../d1/db0/classPathTests_1_1TestPathHelix_1_1TestPathHelix.html#a066e090f9091bd970c6c42068313d441).

## ◆ computeAreas()

def ArchComponent.Component.computeAreas  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Compute the area properties of the object's shape.
    
    Compute the vertical area, horizontal area, and perimeter length of
    the object's shape.
    
    The vertical area is the surface area of the faces perpendicular to the
    ground.
    
    The horizontal area is the area of the shape, when projected onto a
    hyperplane across the XY axes, IE: the area when viewed from a bird's
    eye view.
    
    The perimeter length is the length of the outside edges of this bird's
    eye view.
    
    Assign these values to the object's "VerticalArea", "HorizontalArea",
    and "PerimeterLength" properties.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    

Referenced by
[ArchComponent.Component.applyShape()](../../de/d87/classArchComponent_1_1Component.html#ac8174503690f56dcf8b6d8e324fadbc5),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
and
[ArchRoof.makeRoof()](../../d4/d2a/namespaceArchRoof.html#ad19f0e53e9c0a79c7ac5d7cf86f73c65).

## ◆ execute()

def ArchComponent.Component.execute  | ( |  | _self_ ,   
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
    

Reimplemented in
[ArchCurtainWall.CurtainWall](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a9bcd979b923081e0898b56f0191d1cb4),
and
[ArchTruss.Truss](../../d9/d6f/classArchTruss_1_1Truss.html#a9d12be1826d5cef997f94a1cd7a982f5).

References
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
[Sketcher::Constraint.clone()](../../d6/def/classSketcher_1_1Constraint.html#ad70b52b49bc522b68eb48e969691b608),
[Sketcher::ExternalGeometryFacade.clone()](../../dd/d90/classSketcher_1_1ExternalGeometryFacade.html#aab93c0fd119a772b715452cac6f68371),
[Sketcher::GeometryFacade.clone()](../../d1/d73/classSketcher_1_1GeometryFacade.html#a9131fb2720921d0c9d68418634332d17),
[TechDraw::CosmeticVertex.clone()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a5a3a77432ca3ad0b30292e4080676229),
[TechDraw::CosmeticEdge.clone()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a37ae3ac809adc02b39554195495b2e59),
[TechDraw::CenterLine.clone()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a6dfa88a33924e240922b5643a8475ef1),
[TechDraw::GeomFormat.clone()](../../d7/d64/classTechDraw_1_1GeomFormat.html#ade8ce89cc1d68c0374c996ffe64d55ce),
[Part::Geometry2d.clone()](../../d1/dad/classPart_1_1Geometry2d.html#ab3c7fdc2ef02c31130ca16adb9ba902f),
[Part::Geom2dConic.clone()](../../d8/d0d/classPart_1_1Geom2dConic.html#a7ab379470b34fda16d0c548a7667b539),
[Part::Geom2dArcOfConic.clone()](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html#af4125da0d13cfb8e0116cdeb2912ca71),
[PathTests.TestPathHelix.TestPathHelix.clone](../../d1/db0/classPathTests_1_1TestPathHelix_1_1TestPathHelix.html#afd98c1d369bc590c551b9ba37f62187f),
[ArchComponent.Component.processSubShapes()](../../de/d87/classArchComponent_1_1Component.html#a34cd7509406ea5e01a1d72b41e900742),
[ArchComponent.Component.spread()](../../de/d87/classArchComponent_1_1Component.html#a9aa897ac64c7072468e23fee445dd2df),
[App::FeaturePythonPyT< FeaturePyT
>.Type](../../d5/df9/classApp_1_1FeaturePythonPyT.html#a30564b7cd97268ab1c5ec82087341bb3),
[App::Part.Type](../../da/d8d/classApp_1_1Part.html#a0a40cb4c87c3b600ff21bbc2073a9b58),
[App::PropertyData::PropertySpec.Type](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#a6244b48b04beb90601c0eab74414ac4f),
[Base::PyObjectBase.Type](../../d0/d61/classBase_1_1PyObjectBase.html#aa40cc61e3f6a68dd6fb81745b5fc20de),
[Base::Type.Type()](../../dc/dee/classBase_1_1Type.html#a26ce658f5055f20610491addb5983ad6),
Py::Type.Type(),
[Gui::SelectionChanges.Type](../../d5/d50/classGui_1_1SelectionChanges.html#a14bc5c24e02146dec9aadcbde50d3651),
ArchAxis._Axis.Type, ArchAxisSystem._AxisSystem.Type,
ArchBuilding._Building.Type,
[ArchBuildingPart.BuildingPart.Type](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#acaa6f58401fab574a68e9a88c7a18e75),
[ArchComponent.Component.Type](../../de/d87/classArchComponent_1_1Component.html#a4a5c3bb5d5f50162eca9c62b01ec1e32),
ArchEquipment._Equipment.Type, ArchFence._Fence.Type, ArchFloor._Floor.Type,
ArchFrame._Frame.Type,
[ArchGrid.ArchGrid.Type](../../d7/d52/classArchGrid_1_1ArchGrid.html#a2b579984d85ef9ff4d312b9f7a311fef),
ArchMaterial._ArchMaterialContainer.Type, ArchMaterial._ArchMaterial.Type,
ArchMaterial._ArchMultiMaterial.Type, ArchPanel._Panel.Type,
[ArchPanel.PanelView.Type](../../dd/da0/classArchPanel_1_1PanelView.html#ac870d9fd722704e5618157a816ba2e03),
[ArchPanel.PanelCut.Type](../../d6/dbd/classArchPanel_1_1PanelCut.html#a0a2977f3f7ff28a9200a96c93e3903ee),
[ArchPanel.PanelSheet.Type](../../dc/d22/classArchPanel_1_1PanelSheet.html#a029f7be79c7aecc3314076236b5105d7),
ArchPipe._ArchPipe.Type, ArchPipe._ArchPipeConnector.Type,
ArchPrecast._Precast.Type, ArchProject._Project.Type, ArchRebar._Rebar.Type,
[ArchReference.ArchReference.Type](../../d3/d06/classArchReference_1_1ArchReference.html#a02e4ee0ba8acff45b12557cdf006e337),
ArchRoof._Roof.Type, ArchSchedule._ArchSchedule.Type,
ArchSectionPlane._SectionPlane.Type, ArchSectionPlane._ArchDrawingView.Type,
ArchSite._Site.Type, ArchSpace._Space.Type, ArchStairs._Stairs.Type,
ArchStructure._Structure.Type, ArchStructure._StructuralSystem.Type,
[ArchTruss.Truss.Type](../../d9/d6f/classArchTruss_1_1Truss.html#a1660bf4d5d226841974b618b2eec7c95),
ArchWall._Wall.Type, ArchWindow._Window.Type,
[draftobjects.base.DraftObject.Type](../../d1/d64/classdraftobjects_1_1base_1_1DraftObject.html#a5ea27fe2e4a784618bb15cce5fed29da),
[draftobjects.draft_annotation.DraftAnnotation.Type](../../d4/dca/classdraftobjects_1_1draft__annotation_1_1DraftAnnotation.html#aa4ff69b2beeff361d3fc7cbbb5525877),
[draftobjects.hatch.Hatch.Type](../../db/d7f/classdraftobjects_1_1hatch_1_1Hatch.html#a475adff5eebedba71f542ec42a2b2613),
[draftobjects.layer.Layer.Type](../../d0/ddc/classdraftobjects_1_1layer_1_1Layer.html#a87de9038f1943ab0652620c09f76999f),
[draftobjects.layer.LayerContainer.Type](../../de/d4d/classdraftobjects_1_1layer_1_1LayerContainer.html#a64993d18819511ef6653e8818afb886d),
[draftobjects.wpproxy.WorkingPlaneProxy.Type](../../d1/d19/classdraftobjects_1_1wpproxy_1_1WorkingPlaneProxy.html#a2084c6e0721cfd8e5f050fbdc3540141),
[femobjects.constant_vacuumpermittivity.ConstantVacuumPermittivity.Type](../../d6/db6/classfemobjects_1_1constant__vacuumpermittivity_1_1ConstantVacuumPermittivity.html#a003dafc798992d429951717bf69a479c),
[femobjects.constraint_bodyheatsource.ConstraintBodyHeatSource.Type](../../d7/d28/classfemobjects_1_1constraint__bodyheatsource_1_1ConstraintBodyHeatSource.html#ab94186d5a2fa03dc2b09e454661dd6c5),
[femobjects.constraint_centrif.ConstraintCentrif.Type](../../d8/dc4/classfemobjects_1_1constraint__centrif_1_1ConstraintCentrif.html#a8a65cc6e8fdc11a99e7e0dbfd9480a51),
[femobjects.constraint_electrostaticpotential.ConstraintElectrostaticPotential.Type](../../d9/db9/classfemobjects_1_1constraint__electrostaticpotential_1_1ConstraintElectrostaticPotential.html#ae442a4db8cf082a04c42a0e4fed213fd),
[femobjects.constraint_flowvelocity.ConstraintFlowVelocity.Type](../../d5/dc9/classfemobjects_1_1constraint__flowvelocity_1_1ConstraintFlowVelocity.html#af7e4d0e2423972ba96660cde7425c481),
[femobjects.constraint_initialflowvelocity.ConstraintInitialFlowVelocity.Type](../../de/d2d/classfemobjects_1_1constraint__initialflowvelocity_1_1ConstraintInitialFlowVelocity.html#aeecfd1ce5578c520a890f3c02f3be48d),
[femobjects.constraint_sectionprint.ConstraintSectionPrint.Type](../../de/d31/classfemobjects_1_1constraint__sectionprint_1_1ConstraintSectionPrint.html#abf70ff34ebe0f11df556c2d8e39de37a),
[femobjects.constraint_selfweight.ConstraintSelfWeight.Type](../../d1/d49/classfemobjects_1_1constraint__selfweight_1_1ConstraintSelfWeight.html#ad4f9e756e3f3ed3684882549f2e998fd),
[femobjects.constraint_tie.ConstraintTie.Type](../../d8/df5/classfemobjects_1_1constraint__tie_1_1ConstraintTie.html#ac695ceed59e47822e7b489af984705ca),
[femobjects.element_fluid1D.ElementFluid1D.Type](../../df/d16/classfemobjects_1_1element__fluid1D_1_1ElementFluid1D.html#a6a1f92e36bfaa2fede1c04a65d173112),
[femobjects.element_geometry1D.ElementGeometry1D.Type](../../d0/d4f/classfemobjects_1_1element__geometry1D_1_1ElementGeometry1D.html#aa49316cb0d3742daf112a4319bafe3fe),
[femobjects.element_geometry2D.ElementGeometry2D.Type](../../d1/d6f/classfemobjects_1_1element__geometry2D_1_1ElementGeometry2D.html#aec4e8219d3c239d7967d8e58fa79b1ad),
[femobjects.element_rotation1D.ElementRotation1D.Type](../../d8/d0c/classfemobjects_1_1element__rotation1D_1_1ElementRotation1D.html#a31e57a2998752501d0e5b59510a3f4d3),
[femobjects.material_common.MaterialCommon.Type](../../db/dfc/classfemobjects_1_1material__common_1_1MaterialCommon.html#a6a59fa9434a44b1c8c7c3c8d970a58c8),
[femobjects.material_mechanicalnonlinear.MaterialMechanicalNonlinear.Type](../../dd/de0/classfemobjects_1_1material__mechanicalnonlinear_1_1MaterialMechanicalNonlinear.html#a1081a3956f0b3f397de6b094762f8c9d),
[femobjects.material_reinforced.MaterialReinforced.Type](../../da/de9/classfemobjects_1_1material__reinforced_1_1MaterialReinforced.html#a5435f0ba45bb61fa825c29fd6aaeb043),
[femobjects.mesh_boundarylayer.MeshBoundaryLayer.Type](../../de/d8e/classfemobjects_1_1mesh__boundarylayer_1_1MeshBoundaryLayer.html#a44c98ddcafd39b00595a179ce79c919d),
[femobjects.mesh_gmsh.MeshGmsh.Type](../../d0/d6a/classfemobjects_1_1mesh__gmsh_1_1MeshGmsh.html#accca355b99808987e89a50dc0a7a8abb),
[femobjects.mesh_group.MeshGroup.Type](../../db/d27/classfemobjects_1_1mesh__group_1_1MeshGroup.html#a4205607b5781b420c1cf795bfc18ae1e),
[femobjects.mesh_region.MeshRegion.Type](../../d9/d54/classfemobjects_1_1mesh__region_1_1MeshRegion.html#acd98c4198b934d280996601aacf4f698),
[femobjects.mesh_result.MeshResult.Type](../../d3/dc5/classfemobjects_1_1mesh__result_1_1MeshResult.html#a5e0ad65a89b84fc7c666d52dcad8c26a),
[femobjects.result_mechanical.ResultMechanical.Type](../../df/d8e/classfemobjects_1_1result__mechanical_1_1ResultMechanical.html#ae31e12f1d2e8388b73c421c5b4fa5a75),
[femobjects.solver_ccxtools.SolverCcxTools.Type](../../d6/d04/classfemobjects_1_1solver__ccxtools_1_1SolverCcxTools.html#afc7312b45245fcfb8b13fce99bc42883),
[femsolver.calculix.solver.Proxy.Type](../../d1/d64/classfemsolver_1_1calculix_1_1solver_1_1Proxy.html#a0dda3e478bc2f2e7a7c213757b477c94),
[femsolver.elmer.equations.elasticity.Proxy.Type](../../d1/d26/classfemsolver_1_1elmer_1_1equations_1_1elasticity_1_1Proxy.html#a827374b372394f6a55715d8000d91a11),
[femsolver.elmer.equations.electricforce.Proxy.Type](../../df/d18/classfemsolver_1_1elmer_1_1equations_1_1electricforce_1_1Proxy.html#a424b9d54098cca5b041b985285d846ea),
[femsolver.elmer.equations.electrostatic.Proxy.Type](../../d6/de7/classfemsolver_1_1elmer_1_1equations_1_1electrostatic_1_1Proxy.html#a7abadb440f9efb90383a3bce2bf40bd9),
[femsolver.elmer.equations.flow.Proxy.Type](../../d7/df7/classfemsolver_1_1elmer_1_1equations_1_1flow_1_1Proxy.html#a17792067859e79de47ee42476bdca7af),
[femsolver.elmer.equations.flux.Proxy.Type](../../d7/d6e/classfemsolver_1_1elmer_1_1equations_1_1flux_1_1Proxy.html#ade7473658051685426681928fc8573f6),
[femsolver.elmer.equations.heat.Proxy.Type](../../d6/d2e/classfemsolver_1_1elmer_1_1equations_1_1heat_1_1Proxy.html#a8fe59b519933d43683f8778dad3de91b),
[femsolver.elmer.solver.Proxy.Type](../../d1/d12/classfemsolver_1_1elmer_1_1solver_1_1Proxy.html#a29077c596586ad78d325b35980a32a82),
[femsolver.mystran.solver.Proxy.Type](../../d5/d4c/classfemsolver_1_1mystran_1_1solver_1_1Proxy.html#abdcd60e96f9af34af791155ec54f2f6f),
[femsolver.z88.solver.Proxy.Type](../../da/df7/classfemsolver_1_1z88_1_1solver_1_1Proxy.html#adadcfae624495e13f9216a7bec1937b5),
[FemGui::FemSelectionGate.Type](../../dd/de5/classFemGui_1_1FemSelectionGate.html#a73acc6174efc0f8d14d733b9b2fdc775),
[Import::FeatureImportIges.Type()](../../d7/dac/classImport_1_1FeatureImportIges.html#ae6b12eca169b5640871542c5749285a4),
[Import::FeatureImportStep.Type()](../../da/dde/classImport_1_1FeatureImportStep.html#ad67e186d8b9e9429b29b2c399214d1f0),
[BOPTools.JoinFeatures.FeatureConnect.Type](../../d0/d85/classBOPTools_1_1JoinFeatures_1_1FeatureConnect.html#a085878c3a06ffcc56f72411ea7b999b6),
[BOPTools.JoinFeatures.FeatureEmbed.Type](../../d7/d55/classBOPTools_1_1JoinFeatures_1_1FeatureEmbed.html#a1a5451e074efffe4a5b3fbd7e13b3211),
[BOPTools.JoinFeatures.FeatureCutout.Type](../../da/d9a/classBOPTools_1_1JoinFeatures_1_1FeatureCutout.html#a0f6002e45db975e0c036d9091841017a),
[BOPTools.SplitFeatures.FeatureBooleanFragments.Type](../../dc/d6e/classBOPTools_1_1SplitFeatures_1_1FeatureBooleanFragments.html#ac69fc844a4b5e6fb9c42b39b5b768ad8),
[BOPTools.SplitFeatures.FeatureSlice.Type](../../d1/d28/classBOPTools_1_1SplitFeatures_1_1FeatureSlice.html#a233fc62ef4b1c01e2b8f35fd8184ae2c),
[BOPTools.SplitFeatures.FeatureXOR.Type](../../da/dc0/classBOPTools_1_1SplitFeatures_1_1FeatureXOR.html#ae6a2dd3e1299c54cf3f63a779e19f740),
CompoundTools.CompoundFilter._CompoundFilter.Type,
JoinFeatures._PartJoinFeature.Type,
[PartDesign::Boolean.Type](../../d2/d81/classPartDesign_1_1Boolean.html#abaa8fc572b875da05542f6cdcfb43b87),
[PartDesign::FeatureExtrude.Type](../../da/d12/classPartDesign_1_1FeatureExtrude.html#ab2d0f58f67fe1b39c32a8ba2a195d66c),
Mod.PartDesign.InvoluteGearFeature._InvoluteGear.Type,
[Mod.PartDesign.SprocketFeature.Sprocket.Type](../../d6/df0/classMod_1_1PartDesign_1_1SprocketFeature_1_1Sprocket.html#af1b6d3a276a2e1a68b0343018f61d490),
[Path::Tool.Type](../../dd/dfe/classPath_1_1Tool.html#a1a5c4a64ea8594cbc421bad861f7a55c),
[Robot::Waypoint.Type](../../d1/dc7/classRobot_1_1Waypoint.html#ad99104e4ef2eb005f6f1569be5339591),
[Sketcher::ConstraintIds.Type](../../d0/d44/structSketcher_1_1ConstraintIds.html#a53ec9e04ffffd30aba48f6594e78b612),
[Sketcher::Constraint.Type](../../d6/def/classSketcher_1_1Constraint.html#a9190f836a1069a4d68d7d06fa51bf8f1),
[SketcherGui::AutoConstraint.Type](../../d3/db2/structSketcherGui_1_1AutoConstraint.html#aeab32f95e6eabfc8d7350fab4f2637db),
[Spreadsheet_legacy.Spreadsheet.Type](../../d2/d6d/classSpreadsheet__legacy_1_1Spreadsheet.html#af352de8d6ea6ae08c1a29bae9f20e2e5),
[Spreadsheet_legacy.SpreadsheetController.Type](../../d1/d38/classSpreadsheet__legacy_1_1SpreadsheetController.html#a3b6ea54bbf3ed2ea79305e7d66679b6d),
[Spreadsheet_legacy.SpreadsheetPropertyController.Type](../../d5/d01/classSpreadsheet__legacy_1_1SpreadsheetPropertyController.html#a2a485827317092e4c630f20a69466c1a),
[TechDraw::DrawProjGroupItem.Type](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a952de556951509da8740b0bf924fdf8e),
[TechDraw::DrawViewDimension.Type](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aae98f71f065fb355c0e9145f363c4b3d),
[TechDrawGui::QGCustomBorder.Type](../../d5/d7b/classTechDrawGui_1_1QGCustomBorder.html#a34a214b82406103046843f78a562a163a599ae99463247ae65be81a5fa7f34aa4),
[TechDrawGui::QGCustomClip.Type](../../db/d33/classTechDrawGui_1_1QGCustomClip.html#ac734f647650f53acc8a42125c8a0bb70a6c691532e5cd18fef6598b7084cbec4d),
[TechDrawGui::QGCustomImage.Type](../../d5/d80/classTechDrawGui_1_1QGCustomImage.html#ab1970a1e546a68598947d99573a86352a0cb5d62da4ef545552b6c316ca2fef12),
[TechDrawGui::QGCustomLabel.Type](../../d4/dec/classTechDrawGui_1_1QGCustomLabel.html#a12fc2c36c627d584a8c907ad71623d0ea9d2484267356f0519f2bac2b8b5e58fb),
[TechDrawGui::QGCustomRect.Type](../../d9/d78/classTechDrawGui_1_1QGCustomRect.html#aec720a2da3d8cec0f8c9a2823782bef0ac701148347fcabef101d37476fe60018),
[TechDrawGui::QGCustomSvg.Type](../../d4/d3c/classTechDrawGui_1_1QGCustomSvg.html#a906be3c8ad0886baf69b9286d4c1af4eae43649273dcd5ae22e012ef67af4b748),
[TechDrawGui::QGCustomText.Type](../../d8/d42/classTechDrawGui_1_1QGCustomText.html#a5e6e8209f3bfb21d1e06e21f0544bdacab31562c88940d9d5b974a32d039ed948),
[TechDrawGui::QGDisplayArea.Type](../../d4/da6/classTechDrawGui_1_1QGDisplayArea.html#a77aadc72052fa76e7621af0c504e1a86a9e04344dc341a437bd4df79fd7ff135f),
[TechDrawGui::QGMarker.Type](../../d8/de2/classTechDrawGui_1_1QGMarker.html#a9dee446914eeaae77b5d1a2dd4bf3e94a77ce0f76e7105fdb2e3ab4ac7a9c8b73),
[TechDrawGui::QGEPath.Type](../../d9/da7/classTechDrawGui_1_1QGEPath.html#a5d2bb9a49bf6c87130c3754de1b25356a9f81c65b47e399fb60c1cbfcfee11226),
[TechDrawGui::QGIArrow.Type](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#a8472ba969a65f8f973cc6ea9c9ce59a8ab799fe719ee151f8b9e3158ff3c57981),
[TechDrawGui::QGICaption.Type](../../d2/d68/classTechDrawGui_1_1QGICaption.html#a71703f39a9ad603870b6d8a5428ecb78aea045d6a58a1631e10a5df93401319cf),
[TechDrawGui::QGICenterLine.Type](../../d5/d69/classTechDrawGui_1_1QGICenterLine.html#a7322222d95ff78d312cece7a55be3f25ae857eca9df729ff51b256590a2dd8291),
[TechDrawGui::QGICMark.Type](../../d0/de9/classTechDrawGui_1_1QGICMark.html#aed3d772f8585ca030aec5aa4a46344bda96268001ffdbc0977f1387a74af61da2),
[TechDrawGui::QGIDecoration.Type](../../d7/dcd/classTechDrawGui_1_1QGIDecoration.html#acb742c749b524dfcb7f6e20ec60eb032a97ac081e4c8a90800b45458fc6f6dc00),
[TechDrawGui::QGIDimLines.Type](../../d2/d30/classTechDrawGui_1_1QGIDimLines.html#a9576de78ac8decae7b7a64fe80a739c2a4bcf5bff761700ebcc64de8a18fede05),
[TechDrawGui::QGIDrawingTemplate.Type](../../d3/d23/classTechDrawGui_1_1QGIDrawingTemplate.html#a73c70815ccc1451ccfb0ca443dc2dcb0a2b107fff323f9d9bb924730331593d22),
[TechDrawGui::QGIEdge.Type](../../dd/d6c/classTechDrawGui_1_1QGIEdge.html#aed397ffd157f476375472bf2bda49711a543d53e7ac49ec5c6b369a2a2c550d34),
[TechDrawGui::QGIFace.Type](../../d9/d59/classTechDrawGui_1_1QGIFace.html#ae21480fdaab7b3295cf9988c30e4cfeba530da8179c89e6929a2a9c1438d18afe),
[TechDrawGui::QGIGhostHighlight.Type](../../d1/d6a/classTechDrawGui_1_1QGIGhostHighlight.html#ac2315f6f8da71e123de6a808202c7460a659fe1f1eb97f2e7268812826a1ae6f9),
[TechDrawGui::QGIHighlight.Type](../../df/dee/classTechDrawGui_1_1QGIHighlight.html#a12a75f3803b101bd7a11d84c38aa9cdda1faaa60152d143c1abfefb423a81a664),
[TechDrawGui::QGILeaderLine.Type](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#ab6a8a830c63d6958b68e6ccf90202876a91233b24fd3b76a8b7b01a4231dc8216),
[TechDrawGui::QGIMatting.Type](../../d2/d0e/classTechDrawGui_1_1QGIMatting.html#af7c3fa816a92bf1317a318e587b9540fa003d89c4fddf536c33ffdd7c6813ed54),
[TechDrawGui::QGIPrimPath.Type](../../dd/dc6/classTechDrawGui_1_1QGIPrimPath.html#a1edb8eca4ab12c4d7bda827df9e5f26ba0c2976410ae0147267f5ff0e700ed82a),
[TechDrawGui::QGIProjGroup.Type](../../db/d20/classTechDrawGui_1_1QGIProjGroup.html#ab7031a8b6f56d526d52a958eb074a6fba69c179233f383c04a24ab1062f50455c),
[TechDrawGui::QGIRichAnno.Type](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#aefe95fc9b872ebf9260cf93418aee72bab3d0618783c6370f020d006aa3d35c65),
[TechDrawGui::QGISectionLine.Type](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#ab646fb03b45180b28ca8086338baa676a4624d0454c209045d7a6dd399da6eaa7),
[TechDrawGui::QGISVGTemplate.Type](../../d4/d36/classTechDrawGui_1_1QGISVGTemplate.html#a1766596c75248c888c21476b9b0fab5ea57eca51f45938727163020df6c28f08a),
[TechDrawGui::QGITemplate.Type](../../d5/d8e/classTechDrawGui_1_1QGITemplate.html#a636a084d979e88901c8e73799e718799a92a78b30aacebea31bf40b89471a7658),
[TechDrawGui::QGITile.Type](../../d6/d9b/classTechDrawGui_1_1QGITile.html#a0288420d7caf083efd206b026de96b86aa98b6d33f579d065156cb5ee2f6d9338),
[TechDrawGui::QGIVertex.Type](../../d0/d7d/classTechDrawGui_1_1QGIVertex.html#a7806bd155e1bf9713ad3061fae7e7ea9ac2b29cff0f277dc429c686c39b52e78b),
[TechDrawGui::QGIView.Type](../../d1/d99/classTechDrawGui_1_1QGIView.html#a95a4fdb35cd4b584aadbcaab7992b1f2aaef695b1dc11c7fa20ad2a3aaaf03fdd),
[TechDrawGui::QGIViewAnnotation.Type](../../d4/d5b/classTechDrawGui_1_1QGIViewAnnotation.html#ade42c83a994c527913805923c14afa16a34117b672c1e35526efcd04fe332b097),
[TechDrawGui::QGIBalloonLabel.Type](../../dc/d5c/classTechDrawGui_1_1QGIBalloonLabel.html#ac20842d970d6918ab9bd53c2616c493aa156b22e7be0aefbfda1d59449bec70bf),
[TechDrawGui::QGIViewBalloon.Type](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a14cd65d5c6968300e021fde990578185a075fc86b328acc99fa015675e9539193),
[TechDrawGui::QGIViewClip.Type](../../d4/dcc/classTechDrawGui_1_1QGIViewClip.html#ad1b0ac4caaa861b7fe05debaccc627efa12f85250d7cea3d542e8d1d5a2ce1666),
[TechDrawGui::QGIViewCollection.Type](../../d0/dd1/classTechDrawGui_1_1QGIViewCollection.html#a31e27d058688ebd167e49555c5fddc75a9cb796498477560f3da6ca2e0ce91783),
[TechDrawGui::QGIDatumLabel.Type](../../d7/d0c/classTechDrawGui_1_1QGIDatumLabel.html#a7d7a967a9868b24cbd063acaad009306a93aceb84dc2cff89c264c7fa48671aa0),
[TechDrawGui::QGIViewDimension.Type](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#ad0b101d699bb7c6238fe11c663339bc5a46d1e488a429a0b726abb7b75fb6117e),
[TechDrawGui::QGIViewImage.Type](../../d9/ddb/classTechDrawGui_1_1QGIViewImage.html#ae55d41b24d6e2374786b75849aa938d1a4f92ffa9b6de2576b27f896245e24477),
[TechDrawGui::QGIViewPart.Type](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a9205a836ddc11b3738074507eb8d2bb8aa55000633f8c330ae41fbc73f25e3f51),
[TechDrawGui::QGIViewSection.Type](../../d7/d73/classTechDrawGui_1_1QGIViewSection.html#a6f792c7a034bdd41f7fe5d84a3339a8fa82967530b4c864bbb426e508dc1eff9a),
[TechDrawGui::QGIViewSpreadsheet.Type](../../d5/d05/classTechDrawGui_1_1QGIViewSpreadsheet.html#a3fd77e4b77ec1fea324573c3ed528aa7a9b2902c31348ed5f1ef7d26b3568956b),
[TechDrawGui::QGIViewSymbol.Type](../../d1/da0/classTechDrawGui_1_1QGIViewSymbol.html#a4e1c28ebfa04186445e971f034f7e9f9ad8b091fc538b2964070ef3aa8baad53b),
[TechDrawGui::QGIWeldSymbol.Type](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a9bbb2171e64f2adde7f10221cdfffd80af334738f577ec2a4c6f30b8a1a39c1a6),
[TechDrawGui::QGMText.Type](../../d4/d28/classTechDrawGui_1_1QGMText.html#a2aa57280a268eecc5ce2105cf895afbea3070b7ecb7b2442b979c2effcd34eb89),
[TechDrawGui::QGTracker.Type](../../da/d66/classTechDrawGui_1_1QGTracker.html#ab082bbe3fddfe49c01ed28dc1f2cae68a6aaeeb54f94dce879a2fabe9423802ec),
[TechDrawGui::TemplateTextField.Type](../../d9/d4e/classTechDrawGui_1_1TemplateTextField.html#a936b5453c53b94a9ce7e73cd69eff97cadc2d7f6db209109574d318866c11f6ab),
[DocumentObject.DocumentObject.Type()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#adf8fab4998d6834dcde65aa6adcb188f),
and
[DocumentObject.ViewProvider.Type()](../../d8/dd7/classDocumentObject_1_1ViewProvider.html#a0dae9452ad6b57ed3616a5b113eea97a).

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

## ◆ getExtrusionData()

def ArchComponent.Component.getExtrusionData  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Get the object's extrusion data.
    
    Recursively scrape the Bases of the object, until a Base that is
    derived from a <Part::Extrusion> is found. From there, copy the
    extrusion to the (0,0,0) origin.
    
    With this copy, get the <Part.Face> the shape was originally
    extruded from, the <Base.Vector> of the extrusion, and the
    <Base.Placement> needed to move the copy back to its original
    location/orientation. Return this data as a tuple.
    
    If an object derived from a <Part::Multifuse> is encountered, return
    this data as a tuple containing lists. The lists will contain the same
    data as above, from each of the objects within the multifuse.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    
    Returns
    -------
    tuple
        Tuple containing:
    
        1) The <Part.Face> the object was extruded from.
        2) The <Base.Vector> of the extrusion.
        3) The <Base.Placement> of the extrusion.
    

References
[ArchCommands.getExtrusionData()](../../d4/d52/namespaceArchCommands.html#ab65511367c7ab694de78f77c4da6453a),
[Base::Placement.isIdentity()](../../d1/d10/classBase_1_1Placement.html#adaa1d82cad90e3d7438e55d51ef57fc8),
[Base::Rotation.isIdentity()](../../d4/d18/classBase_1_1Rotation.html#a969256cb1d71bfa521429992f930a5ea),
[ArchComponent.Component.isIdentity()](../../de/d87/classArchComponent_1_1Component.html#a21fbace2d08d1a4f696bbddba0963672),
and
[ArchComponent.Component.rebase()](../../de/d87/classArchComponent_1_1Component.html#a3ca88a3aab563db817a7bb54fbd16eaa).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
and
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92).

## ◆ getHosts()

def ArchComponent.Component.getHosts  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Return the objects that have this one as host,
    that is, objects with a "Host" property pointing
    at this object, or a "Hosts" property containing
    this one.
    
    Returns
    -------
    list of <Arch._Structure>
        The Arch Structures hosting this component.
    

## ◆ getMovableChildren()

def ArchComponent.Component.getMovableChildren  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Find the component's children set to move with their host.
    
    In this case, children refer to Additions, Subtractions, and objects
    linked to this object that refer to it as a host in the "Host" or
    "Hosts" properties. Objects are set to move with their host via the
    MoveWithHost property.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    
    Returns
    -------
    list of <App::FeaturePython>
        List of child objects set to move with their host.
    

Referenced by
[ArchComponent.Component.onChanged()](../../de/d87/classArchComponent_1_1Component.html#ac10328dd9515bdac2dd7e11861c4609e).

## ◆ getParentHeight()

def ArchComponent.Component.getParentHeight  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Get a height value from hosts.
    
    Recursively crawl hosts until a Floor or BuildingPart is found, then
    return the value of its Height property.
    
    Parameters
    ---------
    obj: <App::FeaturePython>
        The component object.
    
    Returns
    -------
    <App::PropertyLength>
        The Height value of the found Floor or BuildingPart.
    

References
[ArchComponent.Component.getParentHeight()](../../de/d87/classArchComponent_1_1Component.html#ab220dba4a4f79ceab3c92e55185e5fe5).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
and
[ArchComponent.Component.getParentHeight()](../../de/d87/classArchComponent_1_1Component.html#ab220dba4a4f79ceab3c92e55185e5fe5).

## ◆ getSiblings()

def ArchComponent.Component.getSiblings  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Find objects that have the same Base object, and type.
    
    Look to base object, and find other objects that are based off this
    base object. If these objects are the same type, return them.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    
    Returns
    -------
    list of <App::FeaturePython>
        List of objects that have the same Base and type as this component.
    

## ◆ hideSubobjects()

def ArchComponent.Component.hideSubobjects  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _prop_  
| ) | |   
      
    
    Hides Additions and Subtractions of this Component when that list changes.
    
    Intended to be used in conjunction with the .onChanged() method, to
    access the property that has changed.
    
    When an object loses or gains an Addition, this method hides all
    Additions.  When it gains or loses a Subtraction, this method hides all
    Subtractions.
    
    Does not effect objects of type Window, or clones of Windows.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    prop: string
        The name of the property that has changed.
    

References
[ArchComponent.Component.onChanged()](../../de/d87/classArchComponent_1_1Component.html#ac10328dd9515bdac2dd7e11861c4609e).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c).

## ◆ isIdentity()

def ArchComponent.Component.isIdentity  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _placement_  
| ) | |   
      
    
    Check if a placement is *almost* zero.
    
    Check if a <Base.Placement>'s displacement from (0,0,0) is almost zero,
    and if the angle of its rotation about its axis is almost zero.
    
    Parameters
    ----------
    placement: <Base.Placement>
        The placement to examine.
    
    Returns
    -------
    bool
        Returns true if angle and displacement are almost zero, false it
        otherwise.
    

Referenced by
[ArchComponent.Component.applyShape()](../../de/d87/classArchComponent_1_1Component.html#ac8174503690f56dcf8b6d8e324fadbc5),
[ArchComponent.Component.getExtrusionData()](../../de/d87/classArchComponent_1_1Component.html#abe6b1db0166c4b8edb14db2440ab4919),
and
[ArchComponent.Component.processSubShapes()](../../de/d87/classArchComponent_1_1Component.html#a34cd7509406ea5e01a1d72b41e900742).

## ◆ isStandardCase()

def ArchComponent.Component.isStandardCase  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Determine if the component is a standard case of its IFC type.
    
    Not all IFC types have a standard case.
    
    If an object is a standard case or not varies between the different
    types. Each type has its own rules to define what is a standard case.
    
    Rotated objects, or objects with Additions or Subtractions are not
    standard cases.
    
    All objects whose IfcType is suffixed with the string " Sandard Case"
    are automatically a standard case.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    
    Returns
    -------
    bool
        Whether the object is a standard case or not.
    

## ◆ onBeforeChange()

def ArchComponent.Component.onBeforeChange  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _prop_  
| ) | |   
      
    
    Method called before the object has a property changed.
    
    Specifically, this method is called before the value changes.
    
    If "Placement" has changed, record the old placement, so that
    .onChanged() can compare between the old and new placement, and move
    its children accordingly.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    prop: string
        The name of the property that has changed.
    

References
[ArchComponent.Component.onChanged()](../../de/d87/classArchComponent_1_1Component.html#ac10328dd9515bdac2dd7e11861c4609e).

Referenced by
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
and
[PathScripts.PathGui.QuantitySpinBox.updateProperty()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a8b9b202d7b495b666cb1f6b41ab2beb4).

## ◆ onChanged()

def ArchComponent.Component.onChanged  | ( |  | _self_ ,   
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
[ArchIFC.IfcRoot](../../d4/da7/classArchIFC_1_1IfcRoot.html#abde72ec687dc6401837824722d16d9ea).

Reimplemented in
[ArchCurtainWall.CurtainWall](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#acbae8cc86609f0e9ef6cfe9a7078901f),
and
[ArchTruss.Truss](../../d9/d6f/classArchTruss_1_1Truss.html#ad5bacb59d6610e87c0aad5a4dc7f8987).

References
[ArchComponent.Component.getMovableChildren()](../../de/d87/classArchComponent_1_1Component.html#acf355ffe37a4948f43d6a19688f8ff9b),
[ArchBuildingPart.BuildingPart.oldPlacement](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#ab79c2f0834e4bc22884ca808ae639f91),
[ArchComponent.Component.oldPlacement](../../de/d87/classArchComponent_1_1Component.html#af40cf016bc380869efd09f5aa6ea3414),
and
[DraftVecUtils.tup()](../../dc/dc3/group__DRAFTVECUTILS.html#gada8f1f6ff2e9aca9a3ff9384ae3bbd27).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
[draftviewproviders.view_base.ViewProviderDraft.attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchEquipment.createMeshView()](../../db/d00/namespaceArchEquipment.html#a7325bf277971b5b271fa96eebb2d83c7),
[draftobjects.wire.Wire.execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[ArchComponent.Component.hideSubobjects()](../../de/d87/classArchComponent_1_1Component.html#a043037f6b8940a7430671daa9815752a),
[ArchComponent.Component.onBeforeChange()](../../de/d87/classArchComponent_1_1Component.html#a7aadae31ca64581e8cc1c31fe086736b),
[ArchCurtainWall.CurtainWall.onChanged()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#acbae8cc86609f0e9ef6cfe9a7078901f),
[ArchTruss.Truss.onChanged()](../../d9/d6f/classArchTruss_1_1Truss.html#ad5bacb59d6610e87c0aad5a4dc7f8987),
[ArchWindow.recolorize()](../../d3/db7/namespaceArchWindow.html#a8a46c0e437e0f7099531f4bf88290aed),
[ArchSpace.removeSpaceBoundaries()](../../d8/d6a/namespaceArchSpace.html#aca020b8800ac48fabbf4fce2a0f16cee),
[ArchBuildingPart.ViewProviderBuildingPart.updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut.updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet.updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel.updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer.updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ onDocumentRestored()

def ArchComponent.Component.onDocumentRestored  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Method run when the document is restored. Re-add the Arch component properties.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    

Reimplemented in
[ArchCurtainWall.CurtainWall](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a95c6772213f7a083a0dd81eef6163150),
and
[ArchTruss.Truss](../../d9/d6f/classArchTruss_1_1Truss.html#abf7290b67c66f8b38f2f24c3a913eb7d).

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
[ArchEquipment.createMeshView()](../../db/d00/namespaceArchEquipment.html#a7325bf277971b5b271fa96eebb2d83c7),
[ArchFrame.makeFrame()](../../d8/db6/namespaceArchFrame.html#a43a080855e00e52afc61334b48c48290),
[ArchPipe.makePipeConnector()](../../de/d7d/namespaceArchPipe.html#ad0045d91c1268a704a446908729aaa5f),
[ArchStairs.makeRailing()](../../dc/d06/namespaceArchStairs.html#a37c92f2db600fd86adc3ac386c6fa211),
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d),
[ArchRoof.makeRoof()](../../d4/d2a/namespaceArchRoof.html#ad19f0e53e9c0a79c7ac5d7cf86f73c65),
[ArchCurtainWall.CurtainWall.onDocumentRestored()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a95c6772213f7a083a0dd81eef6163150),
[ArchTruss.Truss.onDocumentRestored()](../../d9/d6f/classArchTruss_1_1Truss.html#abf7290b67c66f8b38f2f24c3a913eb7d),
[ArchWindow.recolorize()](../../d3/db7/namespaceArchWindow.html#a8a46c0e437e0f7099531f4bf88290aed),
and
[ArchSpace.removeSpaceBoundaries()](../../d8/d6a/namespaceArchSpace.html#aca020b8800ac48fabbf4fce2a0f16cee).

## ◆ processSubShapes()

def ArchComponent.Component.processSubShapes  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _base_ ,   
|  |  | _placement_ = `None`  
| ) | |   
      
    
    Add Additions and Subtractions to a base shape.
    
    If Additions exist, fuse them to the base shape. If no base is
    provided, just fuse other additions to the first addition.
    
    If Subtractions exist, cut them from the base shape. Roofs and Windows
    are treated uniquely, as they define their own Shape to subtract from
    parent shapes using their .getSubVolume() methods.
    
    TODO determine what the purpose of the placement argument is.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    base: <Part.Shape>, optional
        The base shape to add Additions and Subtractions to.
    placement: <Base.Placement>, optional
        Prior to adding or subtracting subshapes, the <Base.Placement> of
        the subshapes are multiplied by the inverse of this parameter.
    
    Returns
    -------
    <Part.Shape>
        The base shape, with the additions and subtractions performed.
    

References
[Base::Placement.isIdentity()](../../d1/d10/classBase_1_1Placement.html#adaa1d82cad90e3d7438e55d51ef57fc8),
[Base::Rotation.isIdentity()](../../d4/d18/classBase_1_1Rotation.html#a969256cb1d71bfa521429992f930a5ea),
[ArchComponent.Component.isIdentity()](../../de/d87/classArchComponent_1_1Component.html#a21fbace2d08d1a4f696bbddba0963672),
and
[ArchWall.mergeShapes()](../../d2/d8e/namespaceArchWall.html#a0bc98e20a1b6fe7063e5f4bb4462288b).

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchStructure.StructSelectionObserver.addSelection()](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#ac984e4631db3078ffee1dc0fee52df74),
[ArchComponent.Component.execute()](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0),
and
[ArchTruss.Truss.execute()](../../d9/d6f/classArchTruss_1_1Truss.html#a9d12be1826d5cef997f94a1cd7a982f5).

## ◆ rebase()

def ArchComponent.Component.rebase  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _shape_ ,   
|  |  | _hint_ = `None`  
| ) | |   
      
    
    Copy a shape to the (0,0,0) origin.
    
    Create a copy of a shape, such that its center of mass is in the
    (0,0,0) origin.
    
    TODO Determine the way the shape is rotated by this method.
    
    Return the copy of the shape, and the <Base.Placement> needed to move
    the copy back to its original location/orientation.
    
    Parameters
    ----------
    shape: <Part.Shape>
        The shape to copy.
    hint: <Base.Vector>, optional
        If the angle between the normal vector of the shape, and the hint
        vector is greater than 90 degrees, the normal will be reversed
        before being rotated.
    

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchComponent.Component.getExtrusionData()](../../de/d87/classArchComponent_1_1Component.html#abe6b1db0166c4b8edb14db2440ab4919),
and
[exportIFC.getRepresentation()](../../d8/d5d/namespaceexportIFC.html#ab7e3a822724c9bbdbb26e769f5e89bef).

## ◆ setProperties()

def ArchComponent.Component.setProperties  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Give the component its component specific properties, such as material.
    
    You can learn more about properties here:
    https://wiki.freecadweb.org/property
    

Reimplemented from
[ArchIFC.IfcRoot](../../d4/da7/classArchIFC_1_1IfcRoot.html#a085b21fd2e99fa8a5ac287d97fbe7fa2).

Reimplemented in
[ArchCurtainWall.CurtainWall](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a1c7351250cd02e8b790e5ed84ebe7553),
and
[ArchTruss.Truss](../../d9/d6f/classArchTruss_1_1Truss.html#a90f32bb2105867d75078e021f1ba771c).

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

## ◆ spread()

def ArchComponent.Component.spread  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _shape_ ,   
|  |  | _placement_ = `None`  
| ) | |   
      
    
    Copy the object to its Axis's points.
    
    If the object has the "Axis" property assigned, create a copy of the
    shape for each point on the object assigned as the "Axis".  Translate
    each of these copies equal to the displacement of the points from the
    (0,0,0) origin.
    
    If the object's "Axis" is unassigned, return the original shape
    unchanged.
    
    Parameters
    ----------
    obj: <App::FeaturePython>
        The component object.
    shape: <Part.Shape>
        The shape to copy.
    placement:
        Does nothing.
    
    Returns
    -------
    <Part.Shape>
        The shape, either spread to the axis points, or unchanged.
    

Referenced by
[ArchComponent.Component.applyShape()](../../de/d87/classArchComponent_1_1Component.html#ac8174503690f56dcf8b6d8e324fadbc5),
and
[ArchComponent.Component.execute()](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0).

## Member Data Documentation

## ◆ flatarea

ArchComponent.Component.flatarea  
---  
  
Referenced by
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd).

## ◆ oldPlacement

ArchComponent.Component.oldPlacement  
---  
  
Referenced by
[ArchComponent.Component.onChanged()](../../de/d87/classArchComponent_1_1Component.html#ac10328dd9515bdac2dd7e11861c4609e).

## ◆ Subvolume

ArchComponent.Component.Subvolume  
---  
  
## ◆ Type

ArchComponent.Component.Type  
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

  * FreeCAD/src/Mod/Arch/ArchComponent.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

