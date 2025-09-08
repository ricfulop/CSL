---
url: https://freecad.github.io/SourceDoc/d9/d93/classconfig__control__design_1_1b__spline__curve.html
scraped_at: 2025-09-08T15:20:19.860968
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [b_spline_curve](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html)

[List of all members](../../d4/d90/classconfig__control__design_1_1b__spline__curve-members.html) | Public Member Functions | Public Attributes

config_control_design.b_spline_curve Class Reference

##  Public Member Functions  
  
---  
def | [closed_curve](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#aa084ec588facff488a05c2f9ad709264) ()  
def | [control_points](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#ab3065fdf6d422ab74c91e79564ce1f38) ()  
def | [control_points_list](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#afc86aecda757412f7583132b5a9034cc) ()  
def | [curve_form](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#aa18c9410b2adc3e470a1b53a2be10688) ()  
def | [degree](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a99eaf886f43baba6122ca73372c648cb) ()  
def | [self_intersect](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a4c33a2f834b9d713ddc288450292abdd) ()  
def | [upper_index_on_control_points](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a13bfc700bf2396e0a4181b01ffe784d7) ()  
def | [wr1](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a398f92dc8b064539c2a505afbeb470de) (self)  
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
[closed_curve](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a2947367918704f9270e1d0b156d8dd50)  
|
[control_points_list](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a11d6438f4c597f87addccd7bad9abc47)  
|
[curve_form](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a3217b7bdd9ffb7eea3e930da359ba3a6)  
|
[degree](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a2d955e657f7a17ad526177ac10dd148f)  
|
[self_intersect](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#ab5d964aee69e50cf3b937a02fe0f8512)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
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

def config_control_design.b_spline_curve.closed_curve  | ( | | ) |   
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

def config_control_design.b_spline_curve.control_points  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface.control_points_list,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve.control_points_list,
[automotive_design.b_spline_surface.control_points_list](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a79feb58cf5e62987a2bbc4dd64715672),
[automotive_design.b_spline_curve.control_points_list](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac4a7bc236467fb08ef8a1f49f94a437f),
[config_control_design.b_spline_surface.control_points_list](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a32ded8f4c1082d4f1e122440c1d43309),
[config_control_design.b_spline_curve.control_points_list](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a11d6438f4c597f87addccd7bad9abc47),
[config_control_design.list_to_array()](../../d4/d07/namespaceconfig__control__design.html#aa8a158ecb834f7e39e55fdd2e1b52ecf),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve.upper_index_on_control_points(),
[automotive_design.b_spline_curve.upper_index_on_control_points()](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac9ccc74fa6ffcfcf3ed810f6f700abe1),
and
[config_control_design.b_spline_curve.upper_index_on_control_points()](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a13bfc700bf2396e0a4181b01ffe784d7).

## ◆ control_points_list()

def config_control_design.b_spline_curve.control_points_list  | ( | | ) |   
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

def config_control_design.b_spline_curve.curve_form  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve._curve_form,
automotive_design.b_spline_curve._curve_form, and
config_control_design.b_spline_curve._curve_form.

## ◆ degree()

def config_control_design.b_spline_curve.degree  | ( | | ) |   
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

def config_control_design.b_spline_curve.self_intersect  | ( | | ) |   
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

def config_control_design.b_spline_curve.upper_index_on_control_points  | ( | | ) |   
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

def config_control_design.b_spline_curve.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13).

Reimplemented in
[config_control_design.rational_b_spline_curve](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#ad450bf462f3eef07955850c3c609d71e),
and
[config_control_design.b_spline_curve_with_knots](../../d2/dc3/classconfig__control__design_1_1b__spline__curve__with__knots.html#a670e34aa43e8c3d276bf8a7df99f1d94).

## Member Data Documentation

## ◆ closed_curve

config_control_design.b_spline_curve.closed_curve  
---  
  
Referenced by
[automotive_design.composite_curve.wr1()](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6c06ad45cd7346e7624b280655556968),
and
[config_control_design.composite_curve.wr1()](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a7adb0598ad5498f569df00d0632714ec).

## ◆ control_points_list

config_control_design.b_spline_curve.control_points_list  
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

config_control_design.b_spline_curve.curve_form  
---  
  
## ◆ degree

config_control_design.b_spline_curve.degree  
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

config_control_design.b_spline_curve.self_intersect  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

