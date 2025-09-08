---
url: https://freecad.github.io/SourceDoc/db/d4c/classautomotive__design_1_1b__spline__curve.html
scraped_at: 2025-09-08T15:00:40.941849
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [b_spline_curve](../../db/d4c/classautomotive__design_1_1b__spline__curve.html)

[List of all members](../../dc/de7/classautomotive__design_1_1b__spline__curve-members.html) | Public Member Functions | Public Attributes

automotive_design.b_spline_curve Class Reference

##  Public Member Functions  
  
---  
def | [closed_curve](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#a20fe5e443d32eefa0e55497631e9e4a5) ()  
def | [control_points](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#acbf0cabc6f76eb9030141e621e3e2483) ()  
def | [control_points_list](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#a410b30a6e6fb2664a43027298cc9fef7) ()  
def | [curve_form](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#a4d6801c9b43ba3c54bc19d99c8e7f448) ()  
def | [degree](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac48dfdd6a0c241ad5db2fcaf6cd7026c) ()  
def | [self_intersect](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ad431fc576d8ea2e49a77ad5e6e1cb48b) ()  
def | [upper_index_on_control_points](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac9ccc74fa6ffcfcf3ed810f6f700abe1) ()  
def | [wr1](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#a829091a18fd135e17b2b1ac639c5e510) (self)  
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
[closed_curve](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#a7cbedcbd75d0cbe968812bee57d63912)  
|
[control_points_list](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac4a7bc236467fb08ef8a1f49f94a437f)  
|
[curve_form](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#a831b89acf0f1f672db8cd72163721f36)  
|
[degree](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#a20bd85d7ccb670d8ef67bcd45ccc72be)  
|
[self_intersect](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#a7f28e170bdae25309ba19d71019f9502)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity b_spline_curve definition.
    
        :param degree
        :type degree:INTEGER
    
        :param control_points_list
        :type control_points_list:LIST(2,None,'cartesian_point', scope = schema_scope)
    
        :param curve_form
        :type curve_form:b_spline_curve_form
    
        :param closed_curve
        :type closed_curve:LOGICAL
    
        :param self_intersect
        :type self_intersect:LOGICAL
    
        :param upper_index_on_control_points
        :type upper_index_on_control_points:INTEGER
    
        :param control_points
        :type control_points:ARRAY(0,upper_index_on_control_points,'cartesian_point', scope = schema_scope)

## Member Function Documentation

## ◆ closed_curve()

def automotive_design.b_spline_curve.closed_curve  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve._closed_curve,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.fill_area_style_tile_coloured_region._closed_curve,
automotive_design.b_spline_curve._closed_curve, and
config_control_design.b_spline_curve._closed_curve.

Referenced by
[automotive_design.composite_curve.wr1()](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6c06ad45cd7346e7624b280655556968),
and
[config_control_design.composite_curve.wr1()](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a7adb0598ad5498f569df00d0632714ec).

## ◆ control_points()

def automotive_design.b_spline_curve.control_points  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface.control_points_list,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve.control_points_list,
[automotive_design.b_spline_surface.control_points_list](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a79feb58cf5e62987a2bbc4dd64715672),
[automotive_design.b_spline_curve.control_points_list](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac4a7bc236467fb08ef8a1f49f94a437f),
[config_control_design.b_spline_surface.control_points_list](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a32ded8f4c1082d4f1e122440c1d43309),
[config_control_design.b_spline_curve.control_points_list](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a11d6438f4c597f87addccd7bad9abc47),
[automotive_design.list_to_array()](../../d4/ddf/namespaceautomotive__design.html#ab7dc76b598137ee186868173eef1e979),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve.upper_index_on_control_points(),
[automotive_design.b_spline_curve.upper_index_on_control_points()](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac9ccc74fa6ffcfcf3ed810f6f700abe1),
and
[config_control_design.b_spline_curve.upper_index_on_control_points()](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a13bfc700bf2396e0a4181b01ffe784d7).

## ◆ control_points_list()

def automotive_design.b_spline_curve.control_points_list  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._control_points_list,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve._control_points_list,
automotive_design.b_spline_surface._control_points_list,
automotive_design.b_spline_curve._control_points_list,
config_control_design.b_spline_surface._control_points_list, and
config_control_design.b_spline_curve._control_points_list.

Referenced by
[automotive_design.b_spline_surface.control_points()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a4b5e27a8ac216b8362c4ff04e69219cf),
[automotive_design.b_spline_curve.control_points()](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#acbf0cabc6f76eb9030141e621e3e2483),
[config_control_design.b_spline_surface.control_points()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a7f30f922cfccbabe89073ee253a944c8),
[config_control_design.b_spline_curve.control_points()](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#ab3065fdf6d422ab74c91e79564ce1f38),
[automotive_design.b_spline_surface.u_upper()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#af78bd95b1f90d7f7b2b8fce1fc4056a5),
[config_control_design.b_spline_surface.u_upper()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#ab949a61fc35271f21ccf0ff96cf04d34),
[automotive_design.b_spline_curve.upper_index_on_control_points()](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac9ccc74fa6ffcfcf3ed810f6f700abe1),
[config_control_design.b_spline_curve.upper_index_on_control_points()](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a13bfc700bf2396e0a4181b01ffe784d7),
[automotive_design.b_spline_surface.v_upper()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a3849c73666331d9d738eb5da58282f7e),
and
[config_control_design.b_spline_surface.v_upper()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a07480bbc0bba2230d560575ab0a41c2b).

## ◆ curve_form()

def automotive_design.b_spline_curve.curve_form  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve._curve_form,
automotive_design.b_spline_curve._curve_form, and
config_control_design.b_spline_curve._curve_form.

## ◆ degree()

def automotive_design.b_spline_curve.degree  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve._degree,
automotive_design.b_spline_curve._degree,
config_control_design.b_spline_curve._degree, ifc2x3.ifcbsplinecurve._degree,
and ifc4.ifcbsplinecurve._degree.

Referenced by
[draftguitools.gui_beziers.BezCurve.action()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#ae90c7f6298d0843cb57ac2f622639277),
[draftguitools.gui_beziers.CubicBezCurve.action()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#acd8ada0e97a9f8e643473d35198fcb2d),
[ifc4.ifcbsplinecurvewithknots.consistentbspline()](../../d9/ddd/classifc4_1_1ifcbsplinecurvewithknots.html#a553ce6d5c93ac3e63ae4bc1e6e867f77),
[draftguitools.gui_beziers.CubicBezCurve.drawUpdate()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#a07bb52edac47d574d81021580bed29fa),
[draftguitools.gui_beziers.BezCurve.finish()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a6b4598d09cb7c1f0b06fe1b96cc9096f),
[draftguitools.gui_beziers.CubicBezCurve.finish()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#abadcbdae43b1e54d516d249c71fc0991),
[draftguitools.gui_trackers.bezcurveTracker.recompute()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#abb21c673d4078ec0eafdaa2ce727520d),
[draftguitools.gui_beziers.BezCurve.undolast()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#ad854156c386141afae3f075e17ca8353),
[draftguitools.gui_beziers.CubicBezCurve.undolast()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#af9cfc192da6c19230fa4477a2e3d1915),
[draftguitools.gui_trackers.bezcurveTracker.update()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#a768d7d59cf62a7cfe8fbdc4486a17a63),
[draftguitools.gui_beziers.BezCurve.updateShape()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a17001d6d2b71e61a07739e823b6395ea),
[draftguitools.gui_beziers.CubicBezCurve.updateShape()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#a95913c90c546e4fe4d147e1b52c23ebf),
[automotive_design.b_spline_curve_with_knots.wr1()](../../d3/d16/classautomotive__design_1_1b__spline__curve__with__knots.html#a6eb502dab95aeaba15aa7808ecb10e06),
and
[config_control_design.b_spline_curve_with_knots.wr1()](../../d2/dc3/classconfig__control__design_1_1b__spline__curve__with__knots.html#a670e34aa43e8c3d276bf8a7df99f1d94).

## ◆ self_intersect()

def automotive_design.b_spline_curve.self_intersect  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_surface._self_intersect,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._self_intersect,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve._self_intersect,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_curve_3d._self_intersect,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve._self_intersect,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_curve_2d._self_intersect,
automotive_design.offset_surface._self_intersect,
automotive_design.b_spline_surface._self_intersect,
automotive_design.b_spline_curve._self_intersect,
automotive_design.offset_curve_3d._self_intersect,
automotive_design.composite_curve._self_intersect,
automotive_design.offset_curve_2d._self_intersect,
config_control_design.offset_surface._self_intersect,
config_control_design.b_spline_surface._self_intersect,
config_control_design.b_spline_curve._self_intersect,
config_control_design.offset_curve_3d._self_intersect, and
config_control_design.composite_curve._self_intersect.

## ◆ upper_index_on_control_points()

def automotive_design.b_spline_curve.upper_index_on_control_points  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface.control_points_list,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve.control_points_list,
[automotive_design.b_spline_surface.control_points_list](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a79feb58cf5e62987a2bbc4dd64715672),
[automotive_design.b_spline_curve.control_points_list](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac4a7bc236467fb08ef8a1f49f94a437f),
[config_control_design.b_spline_surface.control_points_list](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a32ded8f4c1082d4f1e122440c1d43309),
and
[config_control_design.b_spline_curve.control_points_list](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a11d6438f4c597f87addccd7bad9abc47).

Referenced by
[automotive_design.b_spline_curve.control_points()](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#acbf0cabc6f76eb9030141e621e3e2483),
[config_control_design.b_spline_curve.control_points()](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#ab3065fdf6d422ab74c91e79564ce1f38),
[automotive_design.rational_b_spline_curve.weights()](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#ab91315101d34e8a211b983234fbeec25),
[config_control_design.rational_b_spline_curve.weights()](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#a4efaf8a6ec31baf9094c93b5a1712542),
[automotive_design.b_spline_curve_with_knots.wr1()](../../d3/d16/classautomotive__design_1_1b__spline__curve__with__knots.html#a6eb502dab95aeaba15aa7808ecb10e06),
and
[config_control_design.b_spline_curve_with_knots.wr1()](../../d2/dc3/classconfig__control__design_1_1b__spline__curve__with__knots.html#a670e34aa43e8c3d276bf8a7df99f1d94).

## ◆ wr1()

def automotive_design.b_spline_curve.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

Reimplemented in
[automotive_design.rational_b_spline_curve](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#a5e3d80b5dcfe98ab3c9d3354fbe52d62),
and
[automotive_design.b_spline_curve_with_knots](../../d3/d16/classautomotive__design_1_1b__spline__curve__with__knots.html#a6eb502dab95aeaba15aa7808ecb10e06).

## Member Data Documentation

## ◆ closed_curve

automotive_design.b_spline_curve.closed_curve  
---  
  
Referenced by
[automotive_design.composite_curve.wr1()](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6c06ad45cd7346e7624b280655556968),
and
[config_control_design.composite_curve.wr1()](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a7adb0598ad5498f569df00d0632714ec).

## ◆ control_points_list

automotive_design.b_spline_curve.control_points_list  
---  
  
Referenced by
[automotive_design.b_spline_surface.control_points()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a4b5e27a8ac216b8362c4ff04e69219cf),
[automotive_design.b_spline_curve.control_points()](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#acbf0cabc6f76eb9030141e621e3e2483),
[config_control_design.b_spline_surface.control_points()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a7f30f922cfccbabe89073ee253a944c8),
[config_control_design.b_spline_curve.control_points()](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#ab3065fdf6d422ab74c91e79564ce1f38),
[automotive_design.b_spline_surface.u_upper()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#af78bd95b1f90d7f7b2b8fce1fc4056a5),
[config_control_design.b_spline_surface.u_upper()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#ab949a61fc35271f21ccf0ff96cf04d34),
[automotive_design.b_spline_curve.upper_index_on_control_points()](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac9ccc74fa6ffcfcf3ed810f6f700abe1),
[config_control_design.b_spline_curve.upper_index_on_control_points()](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a13bfc700bf2396e0a4181b01ffe784d7),
[automotive_design.b_spline_surface.v_upper()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a3849c73666331d9d738eb5da58282f7e),
and
[config_control_design.b_spline_surface.v_upper()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a07480bbc0bba2230d560575ab0a41c2b).

## ◆ curve_form

automotive_design.b_spline_curve.curve_form  
---  
  
## ◆ degree

automotive_design.b_spline_curve.degree  
---  
  
Referenced by
[draftguitools.gui_beziers.BezCurve.action()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#ae90c7f6298d0843cb57ac2f622639277),
[draftguitools.gui_beziers.CubicBezCurve.action()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#acd8ada0e97a9f8e643473d35198fcb2d),
[ifc4.ifcbsplinecurvewithknots.consistentbspline()](../../d9/ddd/classifc4_1_1ifcbsplinecurvewithknots.html#a553ce6d5c93ac3e63ae4bc1e6e867f77),
[draftguitools.gui_beziers.CubicBezCurve.drawUpdate()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#a07bb52edac47d574d81021580bed29fa),
[draftguitools.gui_beziers.BezCurve.finish()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a6b4598d09cb7c1f0b06fe1b96cc9096f),
[draftguitools.gui_beziers.CubicBezCurve.finish()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#abadcbdae43b1e54d516d249c71fc0991),
[draftguitools.gui_trackers.bezcurveTracker.recompute()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#abb21c673d4078ec0eafdaa2ce727520d),
[draftguitools.gui_beziers.BezCurve.undolast()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#ad854156c386141afae3f075e17ca8353),
[draftguitools.gui_beziers.CubicBezCurve.undolast()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#af9cfc192da6c19230fa4477a2e3d1915),
[draftguitools.gui_trackers.bezcurveTracker.update()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#a768d7d59cf62a7cfe8fbdc4486a17a63),
[draftguitools.gui_beziers.BezCurve.updateShape()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a17001d6d2b71e61a07739e823b6395ea),
[draftguitools.gui_beziers.CubicBezCurve.updateShape()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#a95913c90c546e4fe4d147e1b52c23ebf),
[automotive_design.b_spline_curve_with_knots.wr1()](../../d3/d16/classautomotive__design_1_1b__spline__curve__with__knots.html#a6eb502dab95aeaba15aa7808ecb10e06),
and
[config_control_design.b_spline_curve_with_knots.wr1()](../../d2/dc3/classconfig__control__design_1_1b__spline__curve__with__knots.html#a670e34aa43e8c3d276bf8a7df99f1d94).

## ◆ self_intersect

automotive_design.b_spline_curve.self_intersect  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

