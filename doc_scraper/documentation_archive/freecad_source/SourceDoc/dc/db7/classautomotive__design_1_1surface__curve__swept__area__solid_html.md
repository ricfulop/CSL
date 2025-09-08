---
url: https://freecad.github.io/SourceDoc/dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html
scraped_at: 2025-09-08T15:13:28.173420
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [surface_curve_swept_area_solid](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html)

[List of all members](../../d4/da1/classautomotive__design_1_1surface__curve__swept__area__solid-members.html) | Public Member Functions | Public Attributes

automotive_design.surface_curve_swept_area_solid Class Reference

##  Public Member Functions  
  
---  
def | [directrix](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#ae7fe06f6cec0b36710b82f9b118871ca) ()  
def | [end_param](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a62e7d8718cda5b22dc9811a0c7d29b32) ()  
def | [reference_surface](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a200b08500b668a3732721dfae9fbf985) ()  
def | [start_param](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#afea659f5663f80d4cb2e01e924196bb6) ()  
def | [wr1](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.swept_area_solid](../../d9/d56/classautomotive__design_1_1swept__area__solid.html)  
def | [swept_area](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#a34733853b458d9d5121fac66b63dce35) ()  
def | [wr1](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#af06ba2d89fb93f3538bd0cfb3899ca7d) (self)  
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
[directrix](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a7533268eedb317dbcbe2c34010d179f3)  
|
[end_param](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a746a88ebdac006164435a69a8e2f2a26)  
|
[reference_surface](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#ad857df9c7a3dc15675e966d3a2e5324b)  
|
[start_param](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a49ba01660ca0a385adb0b284508ca03b)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.swept_area_solid](../../d9/d56/classautomotive__design_1_1swept__area__solid.html)  
|
[swept_area](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#a88b9dee12a1622f6dcae61055453a815)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity surface_curve_swept_area_solid definition.
    
        :param directrix
        :type directrix:curve
    
        :param start_param
        :type start_param:REAL
    
        :param end_param
        :type end_param:REAL
    
        :param reference_surface
        :type reference_surface:surface

## Member Function Documentation

## ◆ directrix()

def automotive_design.surface_curve_swept_area_solid.directrix  | ( | | ) |   
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

def automotive_design.surface_curve_swept_area_solid.end_param  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve_swept_area_solid._end_param,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_disk_solid._end_param,
automotive_design.surface_curve_swept_area_solid._end_param, and
automotive_design.swept_disk_solid._end_param.

## ◆ reference_surface()

def automotive_design.surface_curve_swept_area_solid.reference_surface  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve_swept_area_solid._reference_surface,
and automotive_design.surface_curve_swept_area_solid._reference_surface.

Referenced by
[automotive_design.surface_curve_swept_area_solid.wr1()](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773).

## ◆ start_param()

def automotive_design.surface_curve_swept_area_solid.start_param  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve_swept_area_solid._start_param,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_disk_solid._start_param,
automotive_design.surface_curve_swept_area_solid._start_param, and
automotive_design.swept_disk_solid._start_param.

## ◆ wr1()

def automotive_design.surface_curve_swept_area_solid.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.swept_area_solid](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#af06ba2d89fb93f3538bd0cfb3899ca7d).

Reimplemented in
[automotive_design.ruled_surface_swept_area_solid](../../da/dd8/classautomotive__design_1_1ruled__surface__swept__area__solid.html#a7146ef05ee5c0d08da8d6d3916b66510).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_surface.basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.point_on_surface.basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve_on_surface.basis_surface(),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve.basis_surface(),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.pcurve.basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.degenerate_pcurve.basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_bounded_surface.basis_surface,
[automotive_design.offset_surface.basis_surface](../../df/d73/classautomotive__design_1_1offset__surface.html#aa72ec368edcce7f74718dc18a9d3be7d),
[automotive_design.point_on_surface.basis_surface](../../d1/d03/classautomotive__design_1_1point__on__surface.html#a3ec7b3f54324d01811620d9f0e920391),
[automotive_design.composite_curve_on_surface.basis_surface()](../../d9/d62/classautomotive__design_1_1composite__curve__on__surface.html#a0cc000cde500f2c0eb2286391e0c1f37),
[automotive_design.surface_curve.basis_surface()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a4124fffa9d613bb72525c9f8ed586d85),
[automotive_design.pcurve.basis_surface](../../d4/d4b/classautomotive__design_1_1pcurve.html#a0448d2b4e9bea68fa8ef372c62736f24),
[automotive_design.rectangular_trimmed_surface.basis_surface](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#aed9764c3a03e2191bba3317e28371b00),
[automotive_design.degenerate_pcurve.basis_surface](../../de/d21/classautomotive__design_1_1degenerate__pcurve.html#a42e73f451fd2ed80e05db5b64c59fc70),
[automotive_design.curve_bounded_surface.basis_surface](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#a398fae2bacfa1b9854cddf04a8cef43a),
[config_control_design.offset_surface.basis_surface](../../de/d83/classconfig__control__design_1_1offset__surface.html#aa6314357180ffcf0ac76e5c30a32e562),
[config_control_design.point_on_surface.basis_surface](../../de/d9d/classconfig__control__design_1_1point__on__surface.html#ad76843c75f55e71afc83016a05fbf691),
[config_control_design.composite_curve_on_surface.basis_surface()](../../da/d0c/classconfig__control__design_1_1composite__curve__on__surface.html#ac2894f2e56864a54058ce357445f8914),
[config_control_design.surface_curve.basis_surface()](../../db/d04/classconfig__control__design_1_1surface__curve.html#abfa790ac414a75af3b6ed8c093208a5a),
[config_control_design.pcurve.basis_surface](../../d8/d67/classconfig__control__design_1_1pcurve.html#a5fd85c1443902391b7d328216cece85b),
[config_control_design.rectangular_trimmed_surface.basis_surface](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a2cc8169c38c15fa8b3097b45f5bab005),
[config_control_design.degenerate_pcurve.basis_surface](../../d3/d07/classconfig__control__design_1_1degenerate__pcurve.html#acb5d040c5ad86be353cd2c8de85bb0ce),
[config_control_design.curve_bounded_surface.basis_surface](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a41f3f9de2d93a5bbb4cd209533394602),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve_swept_area_solid.directrix,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.swept_disk_solid.directrix,
[automotive_design.surface_curve_swept_area_solid.directrix](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a7533268eedb317dbcbe2c34010d179f3),
[automotive_design.swept_disk_solid.directrix](../../d1/dcf/classautomotive__design_1_1swept__disk__solid.html#af700ad3fddeadac6b4d785b351ab2388),
[ifc2x3.ifcsweptdisksolid.directrix](../../dc/dda/classifc2x3_1_1ifcsweptdisksolid.html#a0948677ba2ba52a155384d2da85c128c),
[ifc2x3.ifcsurfacecurvesweptareasolid.directrix](../../dc/da0/classifc2x3_1_1ifcsurfacecurvesweptareasolid.html#a30cf806ebba5f24090c338ae717f5b66),
[ifc4.ifcsweptdisksolid.directrix](../../db/da3/classifc4_1_1ifcsweptdisksolid.html#ab72f69e2766da1d02c52b3434a145f07),
[ifc4.ifcsurfacecurvesweptareasolid.directrix](../../de/dbb/classifc4_1_1ifcsurfacecurvesweptareasolid.html#a325c699931e25c4eb1b17ff58886695e),
[ifc4.ifcfixedreferencesweptareasolid.directrix](../../d0/dbf/classifc4_1_1ifcfixedreferencesweptareasolid.html#a957f84cd270c1a18f3eb0735f0c06ec2),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve_swept_area_solid.reference_surface,
and
[automotive_design.surface_curve_swept_area_solid.reference_surface](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#ad857df9c7a3dc15675e966d3a2e5324b).

## Member Data Documentation

## ◆ directrix

automotive_design.surface_curve_swept_area_solid.directrix  
---  
  
Referenced by
[ifc4.ifcsweptdisksolid.directrixbounded()](../../db/da3/classifc4_1_1ifcsweptdisksolid.html#a9d399b972971be01f86426be2a55589d),
[ifc4.ifcsurfacecurvesweptareasolid.directrixbounded()](../../de/dbb/classifc4_1_1ifcsurfacecurvesweptareasolid.html#a9deea2d819e28d506a9f00b58776dcaa),
[ifc4.ifcfixedreferencesweptareasolid.directrixbounded()](../../d0/dbf/classifc4_1_1ifcfixedreferencesweptareasolid.html#afd33274a270cf318e6655ea49061347d),
and
[automotive_design.surface_curve_swept_area_solid.wr1()](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773).

## ◆ end_param

automotive_design.surface_curve_swept_area_solid.end_param  
---  
  
## ◆ reference_surface

automotive_design.surface_curve_swept_area_solid.reference_surface  
---  
  
Referenced by
[automotive_design.surface_curve_swept_area_solid.wr1()](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773).

## ◆ start_param

automotive_design.surface_curve_swept_area_solid.start_param  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

