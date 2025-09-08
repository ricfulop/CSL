---
url: https://freecad.github.io/SourceDoc/d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html
scraped_at: 2025-09-08T15:23:31.670671
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [rational_b_spline_curve](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html)

[List of all members](../../d2/dbe/classconfig__control__design_1_1rational__b__spline__curve-members.html) | Public Member Functions | Public Attributes

config_control_design.rational_b_spline_curve Class Reference

##  Public Member Functions  
  
---  
def | [weights](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#a4efaf8a6ec31baf9094c93b5a1712542) ()  
def | [weights_data](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#a5d1fc0bf436a4f15a78648c8582b0c79) ()  
def | [wr1](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#ad450bf462f3eef07955850c3c609d71e) (self)  
def | [wr2](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#a34617959ddd42c863b815a20ee2aee36) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.b_spline_curve](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html)  
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
[weights_data](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#a5b03d4289a030aa408ada00b71712f29)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.b_spline_curve](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html)  
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

    
    
    Entity rational_b_spline_curve definition.
    
        :param weights_data
        :type weights_data:LIST(2,None,'REAL', scope = schema_scope)
    
        :param weights
        :type weights:ARRAY(0,upper_index_on_control_points,'REAL', scope = schema_scope)

## Member Function Documentation

## ◆ weights()

def config_control_design.rational_b_spline_curve.weights  | ( | | ) |   
---|---|---|---|---  
  
References
[config_control_design.list_to_array()](../../d4/d07/namespaceconfig__control__design.html#aa8a158ecb834f7e39e55fdd2e1b52ecf),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.b_spline_curve.upper_index_on_control_points(),
[automotive_design.b_spline_curve.upper_index_on_control_points()](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#ac9ccc74fa6ffcfcf3ed810f6f700abe1),
[config_control_design.b_spline_curve.upper_index_on_control_points()](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a13bfc700bf2396e0a4181b01ffe784d7),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rational_b_spline_curve.weights_data,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rational_b_spline_surface.weights_data,
[automotive_design.rational_b_spline_curve.weights_data](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#a4b3ac09e0532e7ff7608e220bcec00a5),
[automotive_design.rational_b_spline_surface.weights_data](../../db/de5/classautomotive__design_1_1rational__b__spline__surface.html#a6414521fd168c48bb227e6076c14369e),
[config_control_design.rational_b_spline_curve.weights_data](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#a5b03d4289a030aa408ada00b71712f29),
and
[config_control_design.rational_b_spline_surface.weights_data](../../df/da0/classconfig__control__design_1_1rational__b__spline__surface.html#aba810f149e0bb822c29cd99c249d17f7).

## ◆ weights_data()

def config_control_design.rational_b_spline_curve.weights_data  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rational_b_spline_curve._weights_data,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rational_b_spline_surface._weights_data,
automotive_design.rational_b_spline_curve._weights_data,
automotive_design.rational_b_spline_surface._weights_data,
config_control_design.rational_b_spline_curve._weights_data, and
config_control_design.rational_b_spline_surface._weights_data.

Referenced by
[automotive_design.rational_b_spline_curve.weights()](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#ab91315101d34e8a211b983234fbeec25),
[automotive_design.rational_b_spline_surface.weights()](../../db/de5/classautomotive__design_1_1rational__b__spline__surface.html#af9dce70be29578712867ae951c1be191),
[config_control_design.rational_b_spline_curve.weights()](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#a4efaf8a6ec31baf9094c93b5a1712542),
[config_control_design.rational_b_spline_surface.weights()](../../df/da0/classconfig__control__design_1_1rational__b__spline__surface.html#a9e7f71b84fad72fa4dceb4cc12bad9a3),
[automotive_design.rational_b_spline_curve.wr1()](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#a5e3d80b5dcfe98ab3c9d3354fbe52d62),
[automotive_design.rational_b_spline_surface.wr1()](../../db/de5/classautomotive__design_1_1rational__b__spline__surface.html#a525eb257f8323ae17121c16170f69616),
[config_control_design.rational_b_spline_curve.wr1()](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#ad450bf462f3eef07955850c3c609d71e),
and
[config_control_design.rational_b_spline_surface.wr1()](../../df/da0/classconfig__control__design_1_1rational__b__spline__surface.html#a21c1bb1a384a79e5ef50126d0c2cb71c).

## ◆ wr1()

def config_control_design.rational_b_spline_curve.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.b_spline_curve](../../d9/d93/classconfig__control__design_1_1b__spline__curve.html#a398f92dc8b064539c2a505afbeb470de).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, Gui::Dialog::DownloadManager.self,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rational_b_spline_curve.weights_data,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rational_b_spline_surface.weights_data,
[automotive_design.rational_b_spline_curve.weights_data](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#a4b3ac09e0532e7ff7608e220bcec00a5),
[automotive_design.rational_b_spline_surface.weights_data](../../db/de5/classautomotive__design_1_1rational__b__spline__surface.html#a6414521fd168c48bb227e6076c14369e),
[config_control_design.rational_b_spline_curve.weights_data](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#a5b03d4289a030aa408ada00b71712f29),
and
[config_control_design.rational_b_spline_surface.weights_data](../../df/da0/classconfig__control__design_1_1rational__b__spline__surface.html#aba810f149e0bb822c29cd99c249d17f7).

## ◆ wr2()

def config_control_design.rational_b_spline_curve.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[config_control_design.curve_weights_positive()](../../d4/d07/namespaceconfig__control__design.html#a51b7f37883153dcc97625044bb5a7004).

## Member Data Documentation

## ◆ weights_data

config_control_design.rational_b_spline_curve.weights_data  
---  
  
Referenced by
[automotive_design.rational_b_spline_curve.weights()](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#ab91315101d34e8a211b983234fbeec25),
[automotive_design.rational_b_spline_surface.weights()](../../db/de5/classautomotive__design_1_1rational__b__spline__surface.html#af9dce70be29578712867ae951c1be191),
[config_control_design.rational_b_spline_curve.weights()](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#a4efaf8a6ec31baf9094c93b5a1712542),
[config_control_design.rational_b_spline_surface.weights()](../../df/da0/classconfig__control__design_1_1rational__b__spline__surface.html#a9e7f71b84fad72fa4dceb4cc12bad9a3),
[automotive_design.rational_b_spline_curve.wr1()](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#a5e3d80b5dcfe98ab3c9d3354fbe52d62),
[automotive_design.rational_b_spline_surface.wr1()](../../db/de5/classautomotive__design_1_1rational__b__spline__surface.html#a525eb257f8323ae17121c16170f69616),
[config_control_design.rational_b_spline_curve.wr1()](../../d2/d28/classconfig__control__design_1_1rational__b__spline__curve.html#ad450bf462f3eef07955850c3c609d71e),
and
[config_control_design.rational_b_spline_surface.wr1()](../../df/da0/classconfig__control__design_1_1rational__b__spline__surface.html#a21c1bb1a384a79e5ef50126d0c2cb71c).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

