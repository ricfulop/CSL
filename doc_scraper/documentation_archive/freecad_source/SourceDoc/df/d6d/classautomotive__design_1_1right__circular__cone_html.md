---
url: https://freecad.github.io/SourceDoc/df/d6d/classautomotive__design_1_1right__circular__cone.html
scraped_at: 2025-09-08T15:12:03.754918
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [right_circular_cone](../../df/d6d/classautomotive__design_1_1right__circular__cone.html)

[List of all members](../../db/d85/classautomotive__design_1_1right__circular__cone-members.html) | Public Member Functions | Public Attributes

automotive_design.right_circular_cone Class Reference

##  Public Member Functions  
  
---  
def | [height](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a1c1f25121065a84fd196956dcc5a88ee) ()  
def | [position](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a10c3ad5e2b6d9ed341802bd2dee9eea0) ()  
def | [radius](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a016ff9e81c04acd307a53260fe07a5e6) ()  
def | [semi_angle](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a611a9905e8dc0d468462bf3749d3d3a2) ()  
def | [wr1](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a231e69feda1a220e5d54e58e6778f657) (self)  
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
[height](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a34f0c858590fbc8e4c6574ccc3c329f0)  
|
[position](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a547e98bec455202f8e93775979287e6d)  
|
[radius](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a83d51f10db69d15d870d1087a70c0e9c)  
|
[semi_angle](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a95b00fe97ff20130ca703c6c78f8252b)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity right_circular_cone definition.
    
        :param position
        :type position:axis1_placement
    
        :param height
        :type height:positive_length_measure
    
        :param radius
        :type radius:length_measure
    
        :param semi_angle
        :type semi_angle:plane_angle_measure

## Member Function Documentation

## ◆ height()

def automotive_design.right_circular_cone.height  | ( | | ) |   
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

def automotive_design.right_circular_cone.position  | ( | | ) |   
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

def automotive_design.right_circular_cone.radius  | ( | | ) |   
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

## ◆ semi_angle()

def automotive_design.right_circular_cone.semi_angle  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cone._semi_angle,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.conical_surface._semi_angle,
automotive_design.right_circular_cone._semi_angle,
automotive_design.conical_surface._semi_angle, and
config_control_design.conical_surface._semi_angle.

## ◆ wr1()

def automotive_design.right_circular_cone.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

References
[Ui_SphereWidget.radius](../../db/dd0/classUi__SphereWidget.html#a88f752e48e1af271730a941d5ba9462e),
[PartGui::Ui_DlgPartCylinder.radius](../../d9/d4f/classPartGui_1_1Ui__DlgPartCylinder.html#a48d2352d7ad2d074de20556d41f50b25),
[e57::CylindricalRepresentation.radius](../../d0/d5a/structe57_1_1CylindricalRepresentation.html#a6bd9a444cf2eb94ab430560f5a783d70),
[DraftGui.DraftToolBar.radius](../../d0/d91/classDraftGui_1_1DraftToolBar.html#afa8b634cd4aa5fdf1048aeda13e25459),
[draftguitools.gui_snapper.Snapper.radius](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a24680f6d6458cb7c9f16fabdd23ff55e),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.polar_complex_number_literal.radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.spherical_surface.radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_disk_solid.radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cylinder.radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.circle.radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cone.radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.sphere.radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.cylindrical_surface.radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.solid_with_constant_radius_edge_blend.radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.conical_surface.radius,
[automotive_design.spherical_surface.radius](../../d3/d4f/classautomotive__design_1_1spherical__surface.html#af2f981c84b733d4468800e233015275b),
[automotive_design.swept_disk_solid.radius](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#a1c08444aa3b7f5442a520a1b6c24dc72),
[automotive_design.right_circular_cylinder.radius](../../d8/d7e/classautomotive__design_1_1right__circular__cylinder.html#a6ea218f6d7eb98b05a68c6750f3dab5a),
[automotive_design.circle.radius](../../d9/d9f/classautomotive__design_1_1circle.html#abde1324aba1bbb357facc1529667bb88),
[automotive_design.right_circular_cone.radius](../../df/d6d/classautomotive__design_1_1right__circular__cone.html#a83d51f10db69d15d870d1087a70c0e9c),
[automotive_design.sphere.radius](../../d6/de4/classautomotive__design_1_1sphere.html#aff34d8f732f5a2961129dfa2c7341495),
[automotive_design.cylindrical_surface.radius](../../d2/d63/classautomotive__design_1_1cylindrical__surface.html#aaa4d34eb90c57e9bfa8c7fba6a4cf60b),
[automotive_design.conical_surface.radius](../../dc/df7/classautomotive__design_1_1conical__surface.html#a3bb6625178c54ad441fe8c6b030037b7),
[config_control_design.spherical_surface.radius](../../dd/d4b/classconfig__control__design_1_1spherical__surface.html#a5706d8e0b6a35f0eb1e627952cb45428),
[config_control_design.circle.radius](../../d0/d85/classconfig__control__design_1_1circle.html#ac95e83b7c476f8bb7d38d23999ad6c35),
[config_control_design.cylindrical_surface.radius](../../d8/d7e/classconfig__control__design_1_1cylindrical__surface.html#a335d741dc94b26fc4e99b90e736792f2),
[config_control_design.conical_surface.radius](../../de/d42/classconfig__control__design_1_1conical__surface.html#adb9eeafbcd91cb82f700dd35838d1919),
[ifc2x3.ifccranerailashapeprofiledef.radius](../../d5/de3/classifc2x3_1_1ifccranerailashapeprofiledef.html#a0657134a0165ca64ba58b4865aaa50e1),
[ifc2x3.ifcroundededgefeature.radius](../../d0/d61/classifc2x3_1_1ifcroundededgefeature.html#abd729dc18a1b652fdd36d6f34a9aa932),
[ifc2x3.ifcrightcircularcylinder.radius](../../df/dc6/classifc2x3_1_1ifcrightcircularcylinder.html#aa7d1ec4aa5a18bda1e52503927dc6a1b),
[ifc2x3.ifccircleprofiledef.radius](../../dd/dfb/classifc2x3_1_1ifccircleprofiledef.html#a2d77821c7735e9fadc47f07a843d2c53),
[ifc2x3.ifccranerailfshapeprofiledef.radius](../../d7/dbb/classifc2x3_1_1ifccranerailfshapeprofiledef.html#a5a7f359329f8df1bfa38d2c03bd80d5e),
[ifc2x3.ifclightsourcepositional.radius](../../d8/db0/classifc2x3_1_1ifclightsourcepositional.html#a75d0066f25ce34f5f422b004103e42ef),
[ifc2x3.ifcsweptdisksolid.radius](../../dc/dda/classifc2x3_1_1ifcsweptdisksolid.html#a232fbbf5352e98b5b6805f25222d26f4),
[ifc2x3.ifccircle.radius](../../d4/db0/classifc2x3_1_1ifccircle.html#a75a6d0d1e403e771b09e120e54d21e2a),
[ifc2x3.ifcsphere.radius](../../d5/d4f/classifc2x3_1_1ifcsphere.html#a5f103f64c2fbd9d4c47f2c4a0dc6139e),
[ifc4.ifcsweptdisksolid.radius](../../db/da3/classifc4_1_1ifcsweptdisksolid.html#a47263675de09ec23b3ada766acb37483),
[ifc4.ifcrightcircularcylinder.radius](../../da/d9b/classifc4_1_1ifcrightcircularcylinder.html#a968a8ba24a9fe0b47cb26b33bbe5b41c),
[ifc4.ifccircleprofiledef.radius](../../d6/de0/classifc4_1_1ifccircleprofiledef.html#afa830f7b7cf16c36a3af23b7364e18d6),
[ifc4.ifclightsourcepositional.radius](../../d7/d8e/classifc4_1_1ifclightsourcepositional.html#a0f4214cd03416c42311f7c6d4de70f80),
[ifc4.ifccircle.radius](../../da/d34/classifc4_1_1ifccircle.html#a44cdb141c421d5642993a165082484cc),
[ifc4.ifccylindricalsurface.radius](../../d6/dc1/classifc4_1_1ifccylindricalsurface.html#a66513173c6abd2c44afb56fa1f7adb50),
[ifc4.ifcsphere.radius](../../d6/d96/classifc4_1_1ifcsphere.html#a94b2532de4bc39df51146f8dd32a81a0),
[Inspection::DistanceInspection.radius](../../dc/dab/structInspection_1_1DistanceInspection.html#a398c2aef762846d55382ff33e14c5492),
[Measure::Measurement.radius()](../../d6/d84/classMeasure_1_1Measurement.html#aad95ee25271e89c1fe3618604b5a07af),
MeshCore::CylinderSurfaceFit.radius, MeshCore::SphereSurfaceFit.radius,
[Part::TangentialArc.radius()](../../d2/d99/classPart_1_1TangentialArc.html#ae221ac7e00a1f55faf301d2e4ed53288),
[PartGui::DimensionAngular.radius](../../d5/d06/classPartGui_1_1DimensionAngular.html#af2f175f74ee239d1a37fab9710675216),
[PartGui::ArcEngine.radius](../../d8/d2e/classPartGui_1_1ArcEngine.html#a28070c7754384a359577a6df15e68b7b),
[geoff_geometry::Circle.radius](../../d7/dec/classgeoff__geometry_1_1Circle.html#a9415ca28442f76d5894b2333a84f05cd),
[geoff_geometry::Span.radius](../../d9/d68/classgeoff__geometry_1_1Span.html#aa4ae33c23cd67c24ae651d592cc38634),
[PathScripts.PathDressupAxisMap.TaskPanel.radius](../../dd/de9/classPathScripts_1_1PathDressupAxisMap_1_1TaskPanel.html#a9a3ef599290f59b34c8196079589d0a2),
[PathScripts.PathDressupHoldingTags.Tag.radius](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a22b02ed6292cce9bc80b4ad754e9a3f5),
[PathScripts.PathDressupTag.TagSolid.radius](../../d2/dc0/classPathScripts_1_1PathDressupTag_1_1TagSolid.html#ab867650ad4ac395c55275c2bba9968ee),
[PathScripts.PathOp.ObjectOp.radius](../../d0/dec/classPathScripts_1_1PathOp_1_1ObjectOp.html#a89800023dca7c4b2a343789769c5029c),
[PathScripts.PathSurface.ObjectSurface.radius](../../dd/d92/classPathScripts_1_1PathSurface_1_1ObjectSurface.html#a360bc48666222c5098564d54dcc67fa5),
[PathScripts.PathSurfaceSupport.ProcessSelectedFaces.radius](../../d4/d8d/classPathScripts_1_1PathSurfaceSupport_1_1ProcessSelectedFaces.html#a4ea838e9fbb6b0267a05532d3743bcfd),
[PathScripts.PathWaterline.ObjectWaterline.radius](../../db/dcc/classPathScripts_1_1PathWaterline_1_1ObjectWaterline.html#a36639b358d3eb1a80fe75df20ef191ef),
[cSimTool.radius](../../d3/d31/classcSimTool.html#aa425f0ab9b916fb9b6d084b570fb6361),
KDL::Path_Circle.radius, KDL::Path_RoundedComposite.radius,
ObjectObserver.radius,
[SketcherGui::DrawSketchHandler3PointArc.radius](../../d3/d84/classSketcherGui_1_1DrawSketchHandler3PointArc.html#aecce5700a4e4462dccd7ba831162c8cf),
[SketcherGui::DrawSketchHandler3PointCircle.radius](../../db/dbc/classSketcherGui_1_1DrawSketchHandler3PointCircle.html#a334c13685f508215695c88f24d06e74e),
[SketcherGui::DrawSketchHandlerOblong.radius](../../dc/dac/classSketcherGui_1_1DrawSketchHandlerOblong.html#ab61fd58c93a4435406ef8f1852e5922f),
[TechDraw::arcPoints.radius](../../d5/d2f/structTechDraw_1_1arcPoints.html#a6cfd713b0993823c6e13bde2aee7b2a9),
and
[TechDraw::Circle.radius](../../d3/d63/classTechDraw_1_1Circle.html#a14059b6675a56fcfb0918e8623738604).

## Member Data Documentation

## ◆ height

automotive_design.right_circular_cone.height  
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

automotive_design.right_circular_cone.position  
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

automotive_design.right_circular_cone.radius  
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

## ◆ semi_angle

automotive_design.right_circular_cone.semi_angle  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

