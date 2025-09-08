---
url: https://freecad.github.io/SourceDoc/de/d46/classconfig__control__design_1_1b__spline__surface.html
scraped_at: 2025-09-08T15:20:22.876459
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [b_spline_surface](../../de/d46/classconfig__control__design_1_1b__spline__surface.html)

[List of all members](../../d1/db9/classconfig__control__design_1_1b__spline__surface-members.html) | Public Member Functions | Public Attributes

config_control_design.b_spline_surface Class Reference

##  Public Member Functions  
  
---  
def | [control_points](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a7f30f922cfccbabe89073ee253a944c8) ()  
def | [control_points_list](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#aa1b366e31d899cc417b08134279a8459) ()  
def | [self_intersect](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a77049c5d51fcf17d3c88bc98e1416784) ()  
def | [surface_form](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a39242e3b85687eae585e8db328338564) ()  
def | [u_closed](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a83e156fa2166dc68779e732b6250f870) ()  
def | [u_degree](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a5aa6d146290b53d4041fc98ffe107e8a) ()  
def | [u_upper](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#ab949a61fc35271f21ccf0ff96cf04d34) ()  
def | [v_closed](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a7ef022464052dcf1c043bdd9be33c6f5) ()  
def | [v_degree](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#ac17b44aa0c54c80f63537307536a1234) ()  
def | [v_upper](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a07480bbc0bba2230d560575ab0a41c2b) ()  
def | [wr1](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a7b8fa4169157c5e5b779fdc1bfbbeb97) (self)  
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
[control_points_list](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a32ded8f4c1082d4f1e122440c1d43309)  
|
[self_intersect](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a8c314c22fe865c70960358efc204dd8a)  
|
[surface_form](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#aac08b23dcd3fc7c89b8db036c4e85e50)  
|
[u_closed](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#af4f570ce050b156bf8d6cdf62d99475b)  
|
[u_degree](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#ac4b5224a5272b1179f5f98a83a607644)  
|
[v_closed](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#ac1c1214a355a6bb1b3c622f5a3ee69c0)  
|
[v_degree](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a1a43a8618be50249b039ace0803392e7)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
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

def config_control_design.b_spline_surface.control_points  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface.control_points_list,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve.control_points_list,
[automotive_design.b_spline_surface.control_points_list](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a79feb58cf5e62987a2bbc4dd64715672),
[automotive_design.b_spline_curve.control_points_list](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac4a7bc236467fb08ef8a1f49f94a437f),
[config_control_design.b_spline_surface.control_points_list](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a32ded8f4c1082d4f1e122440c1d43309),
[config_control_design.b_spline_curve.control_points_list](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a11d6438f4c597f87addccd7bad9abc47),
[config_control_design.make_array_of_array()](../../d4/d07/namespaceconfig__control__design.html#abb5a571265ebf1395690efb52f72fe9c),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface.u_upper(),
[automotive_design.b_spline_surface.u_upper()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#af78bd95b1f90d7f7b2b8fce1fc4056a5),
[config_control_design.b_spline_surface.u_upper()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#ab949a61fc35271f21ccf0ff96cf04d34),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface.v_upper(),
[automotive_design.b_spline_surface.v_upper()](../../d8/dc4/classautomotive__design_1_1b__spline__surface.html#a3849c73666331d9d738eb5da58282f7e),
and
[config_control_design.b_spline_surface.v_upper()](../../de/d46/classconfig__control__design_1_1b__spline__surface.html#a07480bbc0bba2230d560575ab0a41c2b).

## ◆ control_points_list()

def config_control_design.b_spline_surface.control_points_list  | ( | | ) |   
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

def config_control_design.b_spline_surface.self_intersect  | ( | | ) |   
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

def config_control_design.b_spline_surface.surface_form  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._surface_form,
automotive_design.b_spline_surface._surface_form, and
config_control_design.b_spline_surface._surface_form.

## ◆ u_closed()

def config_control_design.b_spline_surface.u_closed  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._u_closed,
automotive_design.b_spline_surface._u_closed, and
config_control_design.b_spline_surface._u_closed.

## ◆ u_degree()

def config_control_design.b_spline_surface.u_degree  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._u_degree,
automotive_design.b_spline_surface._u_degree, and
config_control_design.b_spline_surface._u_degree.

## ◆ u_upper()

def config_control_design.b_spline_surface.u_upper  | ( | | ) |   
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

def config_control_design.b_spline_surface.v_closed  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._v_closed,
automotive_design.b_spline_surface._v_closed, and
config_control_design.b_spline_surface._v_closed.

## ◆ v_degree()

def config_control_design.b_spline_surface.v_degree  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_surface._v_degree,
automotive_design.b_spline_surface._v_degree, and
config_control_design.b_spline_surface._v_degree.

## ◆ v_upper()

def config_control_design.b_spline_surface.v_upper  | ( | | ) |   
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

def config_control_design.b_spline_surface.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13).

Reimplemented in
[config_control_design.rational_b_spline_surface](../../df/da0/classconfig__control__design_1_1rational__b__spline__surface.html#a21c1bb1a384a79e5ef50126d0c2cb71c),
and
[config_control_design.b_spline_surface_with_knots](../../d9/d81/classconfig__control__design_1_1b__spline__surface__with__knots.html#abe07d58f15c35095876483703b505fa9).

## Member Data Documentation

## ◆ control_points_list

config_control_design.b_spline_surface.control_points_list  
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

config_control_design.b_spline_surface.self_intersect  
---  
  
## ◆ surface_form

config_control_design.b_spline_surface.surface_form  
---  
  
## ◆ u_closed

config_control_design.b_spline_surface.u_closed  
---  
  
## ◆ u_degree

config_control_design.b_spline_surface.u_degree  
---  
  
## ◆ v_closed

config_control_design.b_spline_surface.v_closed  
---  
  
## ◆ v_degree

config_control_design.b_spline_surface.v_degree  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

