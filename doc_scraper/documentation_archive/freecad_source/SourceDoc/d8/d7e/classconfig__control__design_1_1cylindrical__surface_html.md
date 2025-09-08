---
url: https://freecad.github.io/SourceDoc/d8/d7e/classconfig__control__design_1_1cylindrical__surface.html
scraped_at: 2025-09-08T15:21:14.068300
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [cylindrical_surface](../../d8/d7e/classconfig__control__design_1_1cylindrical__surface.html)

[List of all members](../../db/daa/classconfig__control__design_1_1cylindrical__surface-members.html) | Public Member Functions | Public Attributes

config_control_design.cylindrical_surface Class Reference

##  Public Member Functions  
  
---  
def | [radius](../../d8/d7e/classconfig__control__design_1_1cylindrical__surface.html#ad3578df3ea8b58d915f8edfb8f24c236) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.elementary_surface](../../d1/d48/classconfig__control__design_1_1elementary__surface.html)  
def | [position](../../d1/d48/classconfig__control__design_1_1elementary__surface.html#a9c3e462ddcea690d63e805d417fe1adc) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html)  
def | [dim](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#aac385fb99d009b699d0d77f10ebdc5f1) ()  
def | [wr1](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
  
##  Public Attributes  
  
---  
|
[radius](../../d8/d7e/classconfig__control__design_1_1cylindrical__surface.html#a335d741dc94b26fc4e99b90e736792f2)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.elementary_surface](../../d1/d48/classconfig__control__design_1_1elementary__surface.html)  
|
[position](../../d1/d48/classconfig__control__design_1_1elementary__surface.html#a6c61fb6f8f3e65f2afad3b47ad97afd9)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity cylindrical_surface definition.
    
        :param radius
        :type radius:positive_length_measure

## Member Function Documentation

## ◆ radius()

def config_control_design.cylindrical_surface.radius  | ( | | ) |   
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

## ◆ radius

config_control_design.cylindrical_surface.radius  
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

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

