---
url: https://freecad.github.io/SourceDoc/d1/dcf/classautomotive__design_1_1swept__disk__solid.html
scraped_at: 2025-09-08T15:13:56.234974
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [swept_disk_solid](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html)

[List of all members](../../da/d6d/classautomotive__design_1_1swept__disk__solid-members.html) | Public Member Functions | Public Attributes

automotive_design.swept_disk_solid Class Reference

##  Public Member Functions  
  
---  
def | [directrix](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#a8b58e53b05b419e2c1907fde8ad67de8) ()  
def | [end_param](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#a44388906df5239b72737b7eee56eaf3b) ()  
def | [inner_radius](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#ad3e9e9e51a139e2c2e55259e91e98ea5) ()  
def | [radius](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#aa43af8c94b6c1df755e2bbedb05be317) ()  
def | [start_param](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#a9d0bea01a54662ec3e57daa8a178d32e) ()  
def | [wr1](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#a3832c993dfe6479fb3d5b7ab64ec3157) (self)  
def | [wr2](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#aa258ef0e990771d90d8941d05e7bccec) (self)  
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
[dim](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#af9ac341b894f3d55683a1c25778712ce)  
|
[directrix](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#af700ad3fddeadac6b4d785b351ab2388)  
|
[end_param](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#a8ceebe02408312bcc116e3a561476f58)  
|
[inner_radius](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#a37138f2311d6337a2570d00f977baefd)  
|
[radius](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#a1c08444aa3b7f5442a520a1b6c24dc72)  
|
[start_param](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#a8a107611546b5d979fc56f8e3bc01277)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity swept_disk_solid definition.
    
        :param directrix
        :type directrix:curve
    
        :param radius
        :type radius:positive_length_measure
    
        :param inner_radius
        :type inner_radius:positive_length_measure
    
        :param start_param
        :type start_param:REAL
    
        :param end_param
        :type end_param:REAL

## Member Function Documentation

## ◆ directrix()

def automotive_design.swept_disk_solid.directrix  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve_swept_area_solid._directrix,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_disk_solid._directrix,
automotive_design.surface_curve_swept_area_solid._directrix,
automotive_design.swept_disk_solid._directrix,
ifc2x3.ifcsweptdisksolid._directrix,
ifc2x3.ifcsurfacecurvesweptareasolid._directrix,
ifc4.ifcsweptdisksolid._directrix,
ifc4.ifcsurfacecurvesweptareasolid._directrix, and
ifc4.ifcfixedreferencesweptareasolid._directrix.

Referenced by
[ifc4.ifcsweptdisksolid.directrixbounded()](../../db/da3/classifc4_1_1ifcsweptdisksolid.html#a9d399b972971be01f86426be2a55589d),
[ifc4.ifcsurfacecurvesweptareasolid.directrixbounded()](../../de/dbb/classifc4_1_1ifcsurfacecurvesweptareasolid.html#a9deea2d819e28d506a9f00b58776dcaa),
[ifc4.ifcfixedreferencesweptareasolid.directrixbounded()](../../d0/dbf/classifc4_1_1ifcfixedreferencesweptareasolid.html#afd33274a270cf318e6655ea49061347d),
and
[automotive_design.surface_curve_swept_area_solid.wr1()](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773).

## ◆ end_param()

def automotive_design.swept_disk_solid.end_param  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve_swept_area_solid._end_param,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_disk_solid._end_param,
automotive_design.surface_curve_swept_area_solid._end_param, and
automotive_design.swept_disk_solid._end_param.

## ◆ inner_radius()

def automotive_design.swept_disk_solid.inner_radius  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_disk_solid._inner_radius,
and automotive_design.swept_disk_solid._inner_radius.

Referenced by
[automotive_design.swept_disk_solid.wr2()](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#aa258ef0e990771d90d8941d05e7bccec).

## ◆ radius()

def automotive_design.swept_disk_solid.radius  | ( | | ) |   
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

## ◆ start_param()

def automotive_design.swept_disk_solid.start_param  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve_swept_area_solid._start_param,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_disk_solid._start_param,
automotive_design.surface_curve_swept_area_solid._start_param, and
automotive_design.swept_disk_solid._start_param.

## ◆ wr1()

def automotive_design.swept_disk_solid.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

## ◆ wr2()

def automotive_design.swept_disk_solid.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_disk_solid.inner_radius,
[automotive_design.swept_disk_solid.inner_radius](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#a37138f2311d6337a2570d00f977baefd),
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

## ◆ dim

automotive_design.swept_disk_solid.dim  
---  
  
Referenced by
[ifc4.ifccartesiantransformationoperator3d.axis3is3d()](../../d0/d2f/classifc4_1_1ifccartesiantransformationoperator3d.html#ad896e8cc3cd14db5cdcec81e4786eec1),
[ifc4.ifcaxis2placement3d.axisis3d()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#ab2f3c3d035505e73f4c12cbceeeae151),
[ifc2x3.ifcsweptsurface.dim()](../../d6/df8/classifc2x3_1_1ifcsweptsurface.html#a5eb3187a1e204615771d1c71c0e05346),
[ifc2x3.ifcplacement.dim()](../../dd/dfd/classifc2x3_1_1ifcplacement.html#ac4dbcef9f43207432d3fa6d838dbdfb7),
[ifc2x3.ifccartesiantransformationoperator.dim()](../../d8/d5d/classifc2x3_1_1ifccartesiantransformationoperator.html#ad46e1f75ce8f2e0d1937c900059809bb),
[ifc2x3.ifccurveboundedplane.dim()](../../d2/dff/classifc2x3_1_1ifccurveboundedplane.html#a4b77cf901367c1cd92ffe6ef787c2f69),
[ifc2x3.ifccompositecurvesegment.dim()](../../dd/d6e/classifc2x3_1_1ifccompositecurvesegment.html#a6014167f48b54f55af87dec16702de32),
[ifc2x3.ifcgeometricset.dim()](../../dc/dab/classifc2x3_1_1ifcgeometricset.html#af569a780b93b69b4dce81b08ddd66f89),
[ifc2x3.ifcrectangulartrimmedsurface.dim()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a9864cd346a9caa1e4e8cf5a282192889),
[ifc2x3.ifcbooleanresult.dim()](../../dd/d21/classifc2x3_1_1ifcbooleanresult.html#aa2c029e00fa7348f4841b70fb651f921),
[ifc2x3.ifcelementarysurface.dim()](../../dc/d78/classifc2x3_1_1ifcelementarysurface.html#aa9fc1e4bb64357615bba0ad16fa6bc10),
[ifc2x3.ifcpointoncurve.dim()](../../d4/dfb/classifc2x3_1_1ifcpointoncurve.html#a97ff0b230b758d8c719d3dbe23a653a8),
[ifc2x3.ifcpointonsurface.dim()](../../d0/d83/classifc2x3_1_1ifcpointonsurface.html#a470f7e831cabe7ab72d99a5afbcb5906),
[ifc2x3.ifcvector.dim()](../../d3/d7f/classifc2x3_1_1ifcvector.html#acba206090ebaf1068c18b522050ab356),
[ifc4.ifccompositecurvesegment.dim()](../../da/d5c/classifc4_1_1ifccompositecurvesegment.html#af5316372982441eb627ec543094e86aa),
[ifc4.ifcplacement.dim()](../../d4/da3/classifc4_1_1ifcplacement.html#a4ff119d99b8ac53bebec7145128d0452),
[ifc4.ifccartesiantransformationoperator.dim()](../../d4/d39/classifc4_1_1ifccartesiantransformationoperator.html#a0a344ffdcb72a602de421822f59573dc),
[ifc4.ifcgeometricset.dim()](../../d1/d95/classifc4_1_1ifcgeometricset.html#a795b14ef2879e9acc0c066d66e122b9b),
[ifc4.ifcbooleanresult.dim()](../../d0/d2c/classifc4_1_1ifcbooleanresult.html#aa87cd3a0d4ac5e137c88d13ce336ba19),
[ifc4.ifcpointoncurve.dim()](../../d3/d46/classifc4_1_1ifcpointoncurve.html#ab0edcecba3e98c552d95d8ec2cbfd963),
[ifc4.ifcpointonsurface.dim()](../../d5/df4/classifc4_1_1ifcpointonsurface.html#a400416d6b069afa2e89e5d43ec6a37f1),
[ifc4.ifcvector.dim()](../../d0/d94/classifc4_1_1ifcvector.html#a472491a5b13134e67210054e2ac45890),
[ifc4.ifcaxis2placement3d.refdiris3d()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#a2249e08fb14d97b33009f9638979ba10),
[ifc4.ifcfillareastylehatching.refhatchline2d()](../../d3/d40/classifc4_1_1ifcfillareastylehatching.html#a775eb971d46de59a558c12d4cbf073d2),
[automotive_design.axis2_placement_3d.wr2()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a53e4146e50cdc12f6f425f5ae2a015e7),
[config_control_design.axis2_placement_3d.wr2()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8510a502b056a9261c4b9cf7323f51b4),
[ifc2x3.ifcaxis2placement3d.wr2()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#aab8fcc584ec7c8fa06ffd345c95b8663),
[ifc2x3.ifcfillareastylehatching.wr23()](../../da/d61/classifc2x3_1_1ifcfillareastylehatching.html#a8a321538b336a12f4d031b3c01cb3784),
[automotive_design.axis2_placement_3d.wr3()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#aef9f7d5b239a07bf44a95014ce73b61d),
[config_control_design.axis2_placement_3d.wr3()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#aea36ab2e3de9512bb5d028dfeaea109b),
[ifc2x3.ifcaxis2placement3d.wr3()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#a6df2d82e8ad19735331147ae1689c8be),
and
[ifc2x3.ifccartesiantransformationoperator3d.wr4()](../../de/d03/classifc2x3_1_1ifccartesiantransformationoperator3d.html#a68b1818b4a81ee6941337c29f3f4d8d7).

## ◆ directrix

automotive_design.swept_disk_solid.directrix  
---  
  
Referenced by
[ifc4.ifcsweptdisksolid.directrixbounded()](../../db/da3/classifc4_1_1ifcsweptdisksolid.html#a9d399b972971be01f86426be2a55589d),
[ifc4.ifcsurfacecurvesweptareasolid.directrixbounded()](../../de/dbb/classifc4_1_1ifcsurfacecurvesweptareasolid.html#a9deea2d819e28d506a9f00b58776dcaa),
[ifc4.ifcfixedreferencesweptareasolid.directrixbounded()](../../d0/dbf/classifc4_1_1ifcfixedreferencesweptareasolid.html#afd33274a270cf318e6655ea49061347d),
and
[automotive_design.surface_curve_swept_area_solid.wr1()](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773).

## ◆ end_param

automotive_design.swept_disk_solid.end_param  
---  
  
## ◆ inner_radius

automotive_design.swept_disk_solid.inner_radius  
---  
  
Referenced by
[automotive_design.swept_disk_solid.wr2()](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#aa258ef0e990771d90d8941d05e7bccec).

## ◆ radius

automotive_design.swept_disk_solid.radius  
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

## ◆ start_param

automotive_design.swept_disk_solid.start_param  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

