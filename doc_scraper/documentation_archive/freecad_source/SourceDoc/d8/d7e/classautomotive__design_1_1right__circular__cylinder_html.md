---
url: https://freecad.github.io/SourceDoc/d8/d7e/classautomotive__design_1_1right__circular__cylinder.html
scraped_at: 2025-09-08T15:12:04.744665
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [right_circular_cylinder](../../d8/d7e/classautomotive__design_1_1right__circular__cylinder.html)

[List of all members](../../d5/dc3/classautomotive__design_1_1right__circular__cylinder-members.html) | Public Member Functions | Public Attributes

automotive_design.right_circular_cylinder Class Reference

##  Public Member Functions  
  
---  
def | [height](../../d8/d7e/classautomotive__design_1_1right__circular__cylinder.html#ace2a04309b5cb42b26e7b062a1e2744c) ()  
def | [position](../../d8/d7e/classautomotive__design_1_1right__circular__cylinder.html#ac6608dec82a6ea2068c738fcc7968ae7) ()  
def | [radius](../../d8/d7e/classautomotive__design_1_1right__circular__cylinder.html#a5f5d58d288befe5b281e7e97ed4dda59) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html)  
def | [dim](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#aef245618450610e88788dcaea46ad742) ()  
def | [wr1](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[height](../../d8/d7e/classautomotive__design_1_1right__circular__cylinder.html#a0ab2b7155e6edfd85cbb48b5f8d84e75)  
|
[position](../../d8/d7e/classautomotive__design_1_1right__circular__cylinder.html#a34c5b7a7d572e1ec84faeaace7314208)  
|
[radius](../../d8/d7e/classautomotive__design_1_1right__circular__cylinder.html#a6ea218f6d7eb98b05a68c6750f3dab5a)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity right_circular_cylinder definition.
    
        :param position
        :type position:axis1_placement
    
        :param height
        :type height:positive_length_measure
    
        :param radius
        :type radius:positive_length_measure

## Member Function Documentation

## ◆ height()

def automotive_design.right_circular_cylinder.height  | ( | | ) |   
---|---|---|---|---  
  
References Gui::Dialog::DlgSettingsImageImp._height, Image::ImageBase._height,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cylinder._height,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cone._height,
automotive_design.right_circular_cylinder._height,
automotive_design.right_circular_cone._height, ifc2x3.ifcpixeltexture._height,
ifc2x3.ifcrightcircularcylinder._height, ifc2x3.ifcrectangularpyramid._height,
ifc2x3.ifcchamferedgefeature._height, ifc2x3.ifcrightcircularcone._height,
ifc4.ifcpixeltexture._height, ifc4.ifcrightcircularcylinder._height,
ifc4.ifcrectangularpyramid._height, and ifc4.ifcrightcircularcone._height.

Referenced by
[ArchGrid.ArchGridTaskPanel.accept()](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#a23ff3b0364933d45bb693ce9f5397568),
[PathScripts.PathInspect.GCodeEditorDialog.cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[PathScripts.PathDressupHoldingTags.Tag.createSolidsAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a2cb6cc02ae81caafbb137dfe20ebfdd8),
[PathScripts.PathStock.StockFromBase.execute()](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#a9fa59e6edf99801ba45c953b49561ae2),
[ifc4.ifcpixeltexture.minpixelint()](../../d0/d7e/classifc4_1_1ifcpixeltexture.html#aadfb141497cf94e67fa347ab5acb72eb),
[ArchGrid.ArchGridTaskPanel.setHeight()](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#abb8ad578f81bb81467e2e8da9f86f217),
[ifc4.ifcpixeltexture.sizeofpixellist()](../../d0/d7e/classifc4_1_1ifcpixeltexture.html#adb5f9eaece157872487934db6f87331b),
[ifc2x3.ifcpixeltexture.wr22()](../../d8/df5/classifc2x3_1_1ifcpixeltexture.html#a8384e107408418f1c00b74d4481b727c),
and
[ifc2x3.ifcpixeltexture.wr24()](../../d8/df5/classifc2x3_1_1ifcpixeltexture.html#a38bd431505957dc2191835b49e774750).

## ◆ position()

def automotive_design.right_circular_cylinder.position  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.conic._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_positional._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.elementary_surface._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cylinder._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_angular_wedge._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cone._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_spot._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.block._position,
automotive_design.conic._position,
automotive_design.light_source_positional._position,
automotive_design.elementary_surface._position,
automotive_design.right_circular_cylinder._position,
automotive_design.right_angular_wedge._position,
automotive_design.torus._position,
automotive_design.right_circular_cone._position,
automotive_design.light_source_spot._position,
automotive_design.block._position, config_control_design.conic._position,
config_control_design.elementary_surface._position,
ifc2x3.ifcsweptsurface._position, ifc2x3.ifcparameterizedprofiledef._position,
ifc2x3.ifcsweptareasolid._position, ifc2x3.ifccsgprimitive3d._position,
ifc2x3.ifcconic._position, ifc2x3.ifcpolygonalboundedhalfspace._position,
ifc2x3.ifcelementarysurface._position,
ifc2x3.ifclightsourcepositional._position,
ifc2x3.ifclightsourcegoniometric._position, ifc4.ifcsweptsurface._position,
ifc4.ifcparameterizedprofiledef._position, ifc4.ifcsweptareasolid._position,
ifc4.ifccsgprimitive3d._position, ifc4.ifcconic._position,
ifc4.ifcpolygonalboundedhalfspace._position,
ifc4.ifcelementarysurface._position, ifc4.ifclightsourcepositional._position,
ifc4.ifclightsourcegoniometric._position, and
ifc4.ifcrecurrencepattern._position.

Referenced by
[WorkingPlane.Plane.alignToPointAndAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab85860830e3debec48d3cdb58d30621a),
[WorkingPlane.Plane.alignToPointAndAxis_SVG()](../../d3/d93/classWorkingPlane_1_1Plane.html#a53cb561d317b813ea9a22ef8e319104d),
[WorkingPlane.Plane.copy()](../../d3/d93/classWorkingPlane_1_1Plane.html#ad5a25c4e17593442d7a38bd51cf7167a),
[ifc2x3.ifcsweptsurface.dim()](../../d6/df8/classifc2x3_1_1ifcsweptsurface.html#a5eb3187a1e204615771d1c71c0e05346),
[ifc2x3.ifcelementarysurface.dim()](../../dc/d78/classifc2x3_1_1ifcelementarysurface.html#aa9fc1e4bb64357615bba0ad16fa6bc10),
[WorkingPlane.Plane.getGlobalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1b8410be9ee2eefb1e5c3902d4d1a230),
[WorkingPlane.Plane.getLocalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab4027587aa29bc4393a52df8159376e1),
[WorkingPlane.Plane.getParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a22bffbf8caab92f815500ed57b857427),
[WorkingPlane.Plane.getPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#aeb4cd9d5da24076f5984cfd0994ed75f),
[WorkingPlane.Plane.offsetToPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#accc43f410bbe85c53bfad80b68903c6c),
[WorkingPlane.Plane.projectPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1918c0d5d231f78520826f24326111e6),
[WorkingPlane.Plane.restore()](../../d3/d93/classWorkingPlane_1_1Plane.html#abe9dafedd4a855a65c40666b5391f4a3),
[WorkingPlane.Plane.save()](../../d3/d93/classWorkingPlane_1_1Plane.html#a5f765f888050e49b7ee71785e689d0fd),
[WorkingPlane.Plane.setFromParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a417c10c501c570723b1c6b471da3fa13),
and
[WorkingPlane.Plane.setFromPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab9f10a2a72fa2ba198adbfad26ec26c2).

## ◆ radius()

def automotive_design.right_circular_cylinder.radius  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.polar_complex_number_literal._radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.spherical_surface._radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_disk_solid._radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cylinder._radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.circle._radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cone._radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.sphere._radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.cylindrical_surface._radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.solid_with_constant_radius_edge_blend._radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.conical_surface._radius,
automotive_design.spherical_surface._radius,
automotive_design.swept_disk_solid._radius,
automotive_design.right_circular_cylinder._radius,
automotive_design.circle._radius,
automotive_design.right_circular_cone._radius,
automotive_design.sphere._radius,
automotive_design.cylindrical_surface._radius,
automotive_design.conical_surface._radius,
config_control_design.spherical_surface._radius,
config_control_design.circle._radius,
config_control_design.cylindrical_surface._radius,
config_control_design.conical_surface._radius,
ifc2x3.ifccranerailashapeprofiledef._radius,
ifc2x3.ifcroundededgefeature._radius, ifc2x3.ifcrightcircularcylinder._radius,
ifc2x3.ifccircleprofiledef._radius,
ifc2x3.ifccranerailfshapeprofiledef._radius,
ifc2x3.ifclightsourcepositional._radius, ifc2x3.ifcsweptdisksolid._radius,
ifc2x3.ifccircle._radius, ifc2x3.ifcsphere._radius,
ifc4.ifcsweptdisksolid._radius, ifc4.ifcrightcircularcylinder._radius,
ifc4.ifccircleprofiledef._radius, ifc4.ifclightsourcepositional._radius,
ifc4.ifccircle._radius, ifc4.ifccylindricalsurface._radius, and
ifc4.ifcsphere._radius.

Referenced by
[PathScripts.PathPocketBase.ObjectPocket.areaOpAreaParams()](../../d8/dbc/classPathScripts_1_1PathPocketBase_1_1ObjectPocket.html#ad9458b6e2356189cc5d915c2fd887ed5),
[PathScripts.PathProfile.ObjectProfile.areaOpAreaParams()](../../d2/d5f/classPathScripts_1_1PathProfile_1_1ObjectProfile.html#a62e7d3b5a94122bdf85036fa2e878e38),
[PathScripts.PathPocketBase.ObjectPocket.areaOpPathParams()](../../d8/dbc/classPathScripts_1_1PathPocketBase_1_1ObjectPocket.html#a4abd936d9ad2725022480dd7c9c26a63),
[PathScripts.PathAreaOp.ObjectOp.areaOpSetDefaultValues()](../../d5/d6f/classPathScripts_1_1PathAreaOp_1_1ObjectOp.html#aaa23efe9cdcaa343258c134e508ce994),
[DraftGui.DraftToolBar.changeRadiusValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a0ef6b940ec7a95b7f33740ae2e0856b4),
[PathScripts.PathDressupHoldingTags.Tag.createSolidsAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a2cb6cc02ae81caafbb137dfe20ebfdd8),
[PathScripts.PathSurface.ObjectSurface.deleteOpVariables()](../../dd/d92/classPathScripts_1_1PathSurface_1_1ObjectSurface.html#a240019cfd9a52ff94df0746540208747),
[PathScripts.PathWaterline.ObjectWaterline.deleteOpVariables()](../../db/dcc/classPathScripts_1_1PathWaterline_1_1ObjectWaterline.html#aa4ff91eb5fcd21c7d2c7698dc21e8402),
[PathScripts.PathOp.ObjectOp.execute()](../../d0/dec/classPathScripts_1_1PathOp_1_1ObjectOp.html#a07461f6a75265c6a72c07da6d78b06cf),
[PathScripts.PathDressupAxisMap.TaskPanel.getFields()](../../dd/de9/classPathScripts_1_1PathDressupAxisMap_1_1TaskPanel.html#a546edd51390be5e9a80243290709c8e2),
[ifc4.ifcsweptdisksolid.innerradiussize()](../../db/da3/classifc4_1_1ifcsweptdisksolid.html#a78e157dac1b9298dbad0802a43463b6d),
[draftguitools.gui_snapper.Snapper.off()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#abd73f787754ba838ce877bfcd2bbd59b),
[PathScripts.PathSurfaceSupport.ProcessSelectedFaces.preProcessModel()](../../d4/d8d/classPathScripts_1_1PathSurfaceSupport_1_1ProcessSelectedFaces.html#a7a7041d238bd3f9dcbf75e9bd11c0aa8),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[draftguitools.gui_snapper.Snapper.showradius()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a1ed50b99d563b6151a072a5898acf9cb),
[draftguitools.gui_snapper.Snapper.snapToCrossExtensions()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#acee40380387892206a064e5b4b878275),
[draftguitools.gui_snapper.Snapper.snapToExtensions()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ae1f59975a9ed59a52c5c72b11a89e8c3),
[draftguitools.gui_snapper.Snapper.snapToGrid()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ad33d36f945a15ec39fba7d0d5184dfbc),
[draftguitools.gui_snapper.Snapper.snapToHold()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a6db0f4aacea9c6e9501927b7c0e3235c),
[draftguitools.gui_snapper.Snapper.snapToPolar()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a5a30c9877875867157703325b090e21f),
[PathScripts.PathDressupAxisMap.TaskPanel.updateUI()](../../dd/de9/classPathScripts_1_1PathDressupAxisMap_1_1TaskPanel.html#a7abdbeead552f7fe20880fb9a3ca7504),
[DraftGui.DraftToolBar.validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
[automotive_design.right_circular_cone.wr1()](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a231e69feda1a220e5d54e58e6778f657),
[automotive_design.conical_surface.wr1()](../../dc/df7/classautomotive__design_1_1conical__surface.html#a19c197ff42456946d7c183cd71926c0d),
[config_control_design.conical_surface.wr1()](../../de/d42/classconfig__control__design_1_1conical__surface.html#a92e0d1af17bf8d262fe664d42024cc3e),
[automotive_design.swept_disk_solid.wr2()](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#aa258ef0e990771d90d8941d05e7bccec),
and
[ifc2x3.ifcsweptdisksolid.wr2()](../../dc/dda/classifc2x3_1_1ifcsweptdisksolid.html#a6869d9bbbf5d694082cb197313cf7335).

## Member Data Documentation

## ◆ height

automotive_design.right_circular_cylinder.height  
---  
  
Referenced by
[ArchGrid.ArchGridTaskPanel.accept()](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#a23ff3b0364933d45bb693ce9f5397568),
[PathScripts.PathInspect.GCodeEditorDialog.cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[PathScripts.PathDressupHoldingTags.Tag.createSolidsAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a2cb6cc02ae81caafbb137dfe20ebfdd8),
[PathScripts.PathStock.StockFromBase.execute()](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#a9fa59e6edf99801ba45c953b49561ae2),
[ifc4.ifcpixeltexture.minpixelint()](../../d0/d7e/classifc4_1_1ifcpixeltexture.html#aadfb141497cf94e67fa347ab5acb72eb),
[ArchGrid.ArchGridTaskPanel.setHeight()](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#abb8ad578f81bb81467e2e8da9f86f217),
[ifc4.ifcpixeltexture.sizeofpixellist()](../../d0/d7e/classifc4_1_1ifcpixeltexture.html#adb5f9eaece157872487934db6f87331b),
[ifc2x3.ifcpixeltexture.wr22()](../../d8/df5/classifc2x3_1_1ifcpixeltexture.html#a8384e107408418f1c00b74d4481b727c),
and
[ifc2x3.ifcpixeltexture.wr24()](../../d8/df5/classifc2x3_1_1ifcpixeltexture.html#a38bd431505957dc2191835b49e774750).

## ◆ position

automotive_design.right_circular_cylinder.position  
---  
  
Referenced by
[WorkingPlane.Plane.alignToPointAndAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab85860830e3debec48d3cdb58d30621a),
[WorkingPlane.Plane.alignToPointAndAxis_SVG()](../../d3/d93/classWorkingPlane_1_1Plane.html#a53cb561d317b813ea9a22ef8e319104d),
[WorkingPlane.Plane.copy()](../../d3/d93/classWorkingPlane_1_1Plane.html#ad5a25c4e17593442d7a38bd51cf7167a),
[ifc2x3.ifcsweptsurface.dim()](../../d6/df8/classifc2x3_1_1ifcsweptsurface.html#a5eb3187a1e204615771d1c71c0e05346),
[ifc2x3.ifcelementarysurface.dim()](../../dc/d78/classifc2x3_1_1ifcelementarysurface.html#aa9fc1e4bb64357615bba0ad16fa6bc10),
[WorkingPlane.Plane.getGlobalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1b8410be9ee2eefb1e5c3902d4d1a230),
[WorkingPlane.Plane.getLocalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab4027587aa29bc4393a52df8159376e1),
[WorkingPlane.Plane.getParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a22bffbf8caab92f815500ed57b857427),
[WorkingPlane.Plane.getPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#aeb4cd9d5da24076f5984cfd0994ed75f),
[WorkingPlane.Plane.offsetToPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#accc43f410bbe85c53bfad80b68903c6c),
[WorkingPlane.Plane.projectPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1918c0d5d231f78520826f24326111e6),
[WorkingPlane.Plane.restore()](../../d3/d93/classWorkingPlane_1_1Plane.html#abe9dafedd4a855a65c40666b5391f4a3),
[WorkingPlane.Plane.save()](../../d3/d93/classWorkingPlane_1_1Plane.html#a5f765f888050e49b7ee71785e689d0fd),
[WorkingPlane.Plane.setFromParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a417c10c501c570723b1c6b471da3fa13),
and
[WorkingPlane.Plane.setFromPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab9f10a2a72fa2ba198adbfad26ec26c2).

## ◆ radius

automotive_design.right_circular_cylinder.radius  
---  
  
Referenced by
[PathScripts.PathPocketBase.ObjectPocket.areaOpAreaParams()](../../d8/dbc/classPathScripts_1_1PathPocketBase_1_1ObjectPocket.html#ad9458b6e2356189cc5d915c2fd887ed5),
[PathScripts.PathProfile.ObjectProfile.areaOpAreaParams()](../../d2/d5f/classPathScripts_1_1PathProfile_1_1ObjectProfile.html#a62e7d3b5a94122bdf85036fa2e878e38),
[PathScripts.PathPocketBase.ObjectPocket.areaOpPathParams()](../../d8/dbc/classPathScripts_1_1PathPocketBase_1_1ObjectPocket.html#a4abd936d9ad2725022480dd7c9c26a63),
[PathScripts.PathAreaOp.ObjectOp.areaOpSetDefaultValues()](../../d5/d6f/classPathScripts_1_1PathAreaOp_1_1ObjectOp.html#aaa23efe9cdcaa343258c134e508ce994),
[DraftGui.DraftToolBar.changeRadiusValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a0ef6b940ec7a95b7f33740ae2e0856b4),
[PathScripts.PathDressupHoldingTags.Tag.createSolidsAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a2cb6cc02ae81caafbb137dfe20ebfdd8),
[PathScripts.PathSurface.ObjectSurface.deleteOpVariables()](../../dd/d92/classPathScripts_1_1PathSurface_1_1ObjectSurface.html#a240019cfd9a52ff94df0746540208747),
[PathScripts.PathWaterline.ObjectWaterline.deleteOpVariables()](../../db/dcc/classPathScripts_1_1PathWaterline_1_1ObjectWaterline.html#aa4ff91eb5fcd21c7d2c7698dc21e8402),
[PathScripts.PathOp.ObjectOp.execute()](../../d0/dec/classPathScripts_1_1PathOp_1_1ObjectOp.html#a07461f6a75265c6a72c07da6d78b06cf),
[PathScripts.PathDressupAxisMap.TaskPanel.getFields()](../../dd/de9/classPathScripts_1_1PathDressupAxisMap_1_1TaskPanel.html#a546edd51390be5e9a80243290709c8e2),
[ifc4.ifcsweptdisksolid.innerradiussize()](../../db/da3/classifc4_1_1ifcsweptdisksolid.html#a78e157dac1b9298dbad0802a43463b6d),
[draftguitools.gui_snapper.Snapper.off()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#abd73f787754ba838ce877bfcd2bbd59b),
[PathScripts.PathSurfaceSupport.ProcessSelectedFaces.preProcessModel()](../../d4/d8d/classPathScripts_1_1PathSurfaceSupport_1_1ProcessSelectedFaces.html#a7a7041d238bd3f9dcbf75e9bd11c0aa8),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[draftguitools.gui_snapper.Snapper.showradius()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a1ed50b99d563b6151a072a5898acf9cb),
[draftguitools.gui_snapper.Snapper.snapToCrossExtensions()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#acee40380387892206a064e5b4b878275),
[draftguitools.gui_snapper.Snapper.snapToExtensions()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ae1f59975a9ed59a52c5c72b11a89e8c3),
[draftguitools.gui_snapper.Snapper.snapToGrid()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ad33d36f945a15ec39fba7d0d5184dfbc),
[draftguitools.gui_snapper.Snapper.snapToHold()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a6db0f4aacea9c6e9501927b7c0e3235c),
[draftguitools.gui_snapper.Snapper.snapToPolar()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a5a30c9877875867157703325b090e21f),
[PathScripts.PathDressupAxisMap.TaskPanel.updateUI()](../../dd/de9/classPathScripts_1_1PathDressupAxisMap_1_1TaskPanel.html#a7abdbeead552f7fe20880fb9a3ca7504),
[DraftGui.DraftToolBar.validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
[automotive_design.right_circular_cone.wr1()](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a231e69feda1a220e5d54e58e6778f657),
[automotive_design.conical_surface.wr1()](../../dc/df7/classautomotive__design_1_1conical__surface.html#a19c197ff42456946d7c183cd71926c0d),
[config_control_design.conical_surface.wr1()](../../de/d42/classconfig__control__design_1_1conical__surface.html#a92e0d1af17bf8d262fe664d42024cc3e),
[automotive_design.swept_disk_solid.wr2()](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#aa258ef0e990771d90d8941d05e7bccec),
and
[ifc2x3.ifcsweptdisksolid.wr2()](../../dc/dda/classifc2x3_1_1ifcsweptdisksolid.html#a6869d9bbbf5d694082cb197313cf7335).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

