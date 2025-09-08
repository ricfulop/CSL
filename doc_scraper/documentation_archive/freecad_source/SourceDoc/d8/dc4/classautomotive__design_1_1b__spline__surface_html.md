---
url: https://freecad.github.io/SourceDoc/d8/dc4/classautomotive__design_1_1b__spline__surface.html
scraped_at: 2025-09-08T15:00:43.945993
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [b_spline_surface](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html)

[List of all members](../../dc/dbb/classautomotive__design_1_1b__spline__surface-members.html) | Public Member Functions | Public Attributes

automotive_design.b_spline_surface Class Reference

##  Public Member Functions  
  
---  
def | [control_points](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a4b5e27a8ac216b8362c4ff04e69219cf) ()  
def | [control_points_list](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a6eb2e52651bd9f6d3e3055dbd9a493a1) ()  
def | [self_intersect](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a79dd3b3e983b129fab7ec3e175af31a3) ()  
def | [surface_form](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a8587d6eda9b3f00d0d80cdee8b4bac85) ()  
def | [u_closed](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#ab2141e3337648452533051098e34255f) ()  
def | [u_degree](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a88ac97de4e681e4a2df7fa23a3db589b) ()  
def | [u_upper](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#af78bd95b1f90d7f7b2b8fce1fc4056a5) ()  
def | [v_closed](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a2eef247be648a4dd9ffed39d35a5b531) ()  
def | [v_degree](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a6657aa9c8e6205040731dee5f9842c44) ()  
def | [v_upper](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a3849c73666331d9d738eb5da58282f7e) ()  
def | [wr1](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a1ab1c681c70a774d87f229eb39a2c898) (self)  
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
[control_points_list](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a79feb58cf5e62987a2bbc4dd64715672)  
|
[self_intersect](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#acd4c89719c34b249cac5c50a993a740a)  
|
[surface_form](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a2c2b519eefc124f1f9b6f1cba84954d7)  
|
[u_closed](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#ae72c1d8f20936f32120b88768f0d43d6)  
|
[u_degree](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#ad185926bf842cae7f76a30fd6b9ee36d)  
|
[v_closed](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a1eb8a07d63c3b049a08903200b37b9e8)  
|
[v_degree](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a15be083e646d4fb4d967547b4e213527)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity b_spline_surface definition.
    
        :param u_degree
        :type u_degree:INTEGER
    
        :param v_degree
        :type v_degree:INTEGER
    
        :param control_points_list
        :type control_points_list:LIST(2,None,LIST(2,None,'cartesian_point', scope = schema_scope))
    
        :param surface_form
        :type surface_form:b_spline_surface_form
    
        :param u_closed
        :type u_closed:LOGICAL
    
        :param v_closed
        :type v_closed:LOGICAL
    
        :param self_intersect
        :type self_intersect:LOGICAL
    
        :param u_upper
        :type u_upper:INTEGER
    
        :param v_upper
        :type v_upper:INTEGER
    
        :param control_points
        :type control_points:ARRAY(0,u_upper,ARRAY(0,v_upper,'cartesian_point', scope = schema_scope))

## Member Function Documentation

## ◆ control_points()

def automotive_design.b_spline_surface.control_points  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface.control_points_list,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve.control_points_list,
[automotive_design.b_spline_surface.control_points_list](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a79feb58cf5e62987a2bbc4dd64715672),
[automotive_design.b_spline_curve.control_points_list](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac4a7bc236467fb08ef8a1f49f94a437f),
[config_control_design.b_spline_surface.control_points_list](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a32ded8f4c1082d4f1e122440c1d43309),
[config_control_design.b_spline_curve.control_points_list](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a11d6438f4c597f87addccd7bad9abc47),
[automotive_design.make_array_of_array()](../../d4/ddf/namespaceautomotive__design.html#affdf970c1fe5ccf0ec11d43724026e7e),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface.u_upper(),
[automotive_design.b_spline_surface.u_upper()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#af78bd95b1f90d7f7b2b8fce1fc4056a5),
[config_control_design.b_spline_surface.u_upper()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#ab949a61fc35271f21ccf0ff96cf04d34),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface.v_upper(),
[automotive_design.b_spline_surface.v_upper()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a3849c73666331d9d738eb5da58282f7e),
and
[config_control_design.b_spline_surface.v_upper()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a07480bbc0bba2230d560575ab0a41c2b).

## ◆ control_points_list()

def automotive_design.b_spline_surface.control_points_list  | ( | | ) |   
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

## ◆ self_intersect()

def automotive_design.b_spline_surface.self_intersect  | ( | | ) |   
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

## ◆ surface_form()

def automotive_design.b_spline_surface.surface_form  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._surface_form,
automotive_design.b_spline_surface._surface_form, and
config_control_design.b_spline_surface._surface_form.

## ◆ u_closed()

def automotive_design.b_spline_surface.u_closed  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._u_closed,
automotive_design.b_spline_surface._u_closed, and
config_control_design.b_spline_surface._u_closed.

## ◆ u_degree()

def automotive_design.b_spline_surface.u_degree  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._u_degree,
automotive_design.b_spline_surface._u_degree, and
config_control_design.b_spline_surface._u_degree.

## ◆ u_upper()

def automotive_design.b_spline_surface.u_upper  | ( | | ) |   
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
[automotive_design.b_spline_surface.control_points()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a4b5e27a8ac216b8362c4ff04e69219cf),
[config_control_design.b_spline_surface.control_points()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a7f30f922cfccbabe89073ee253a944c8),
[automotive_design.rational_b_spline_surface.weights()](../../db/de5/classautomotive__design_1_1rational__b__spline__surface.html#af9dce70be29578712867ae951c1be191),
and
[config_control_design.rational_b_spline_surface.weights()](../../df/da0/classconfig__control__design_1_1rational__b__spline__surface.html#a9e7f71b84fad72fa4dceb4cc12bad9a3).

## ◆ v_closed()

def automotive_design.b_spline_surface.v_closed  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._v_closed,
automotive_design.b_spline_surface._v_closed, and
config_control_design.b_spline_surface._v_closed.

## ◆ v_degree()

def automotive_design.b_spline_surface.v_degree  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._v_degree,
automotive_design.b_spline_surface._v_degree, and
config_control_design.b_spline_surface._v_degree.

## ◆ v_upper()

def automotive_design.b_spline_surface.v_upper  | ( | | ) |   
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
[automotive_design.b_spline_surface.control_points()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a4b5e27a8ac216b8362c4ff04e69219cf),
[config_control_design.b_spline_surface.control_points()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a7f30f922cfccbabe89073ee253a944c8),
[automotive_design.rational_b_spline_surface.weights()](../../db/de5/classautomotive__design_1_1rational__b__spline__surface.html#af9dce70be29578712867ae951c1be191),
and
[config_control_design.rational_b_spline_surface.weights()](../../df/da0/classconfig__control__design_1_1rational__b__spline__surface.html#a9e7f71b84fad72fa4dceb4cc12bad9a3).

## ◆ wr1()

def automotive_design.b_spline_surface.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

Reimplemented in
[automotive_design.rational_b_spline_surface](../../db/de5/classautomotive__design_1_1rational__b__spline__surface.html#a525eb257f8323ae17121c16170f69616),
and
[automotive_design.b_spline_surface_with_knots](../../d1/da5/classautomotive__design_1_1b__spline__surface__with__knots.html#a15d86ece1d5b9bfa36c043d34aa02bc3).

## Member Data Documentation

## ◆ control_points_list

automotive_design.b_spline_surface.control_points_list  
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

## ◆ self_intersect

automotive_design.b_spline_surface.self_intersect  
---  
  
## ◆ surface_form

automotive_design.b_spline_surface.surface_form  
---  
  
## ◆ u_closed

automotive_design.b_spline_surface.u_closed  
---  
  
## ◆ u_degree

automotive_design.b_spline_surface.u_degree  
---  
  
## ◆ v_closed

automotive_design.b_spline_surface.v_closed  
---  
  
## ◆ v_degree

automotive_design.b_spline_surface.v_degree  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

