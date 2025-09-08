---
url: https://freecad.github.io/SourceDoc/d9/dde/classautomotive__design_1_1rational__b__spline__curve.html
scraped_at: 2025-09-08T15:11:30.597286
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [rational_b_spline_curve](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html)

[List of all members](../../d2/d7f/classautomotive__design_1_1rational__b__spline__curve-members.html) | Public Member Functions | Public Attributes

automotive_design.rational_b_spline_curve Class Reference

##  Public Member Functions  
  
---  
def | [weights](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#ab91315101d34e8a211b983234fbeec25) ()  
def | [weights_data](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#ac86dfb4e981b5aacc360a8f2270c68e7) ()  
def | [wr1](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#a5e3d80b5dcfe98ab3c9d3354fbe52d62) (self)  
def | [wr2](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#a5568c2125886378729d2e550ad9e61ed) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.b_spline_curve](../../db/d4c/classautomotive__design_1_1b__spline__curve.html)  
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
[weights_data](../../d9/dde/classautomotive__design_1_1rational__b__spline__curve.html#a4b3ac09e0532e7ff7608e220bcec00a5)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.b_spline_curve](../../db/d4c/classautomotive__design_1_1b__spline__curve.html)  
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

    
    
    Entity rational_b_spline_curve definition.
    
        :param weights_data
        :type weights_data:LIST(2,None,'REAL', scope = schema_scope)
    
        :param weights
        :type weights:ARRAY(0,upper_index_on_control_points,'REAL', scope = schema_scope)

## Member Function Documentation

## ◆ weights()

def automotive_design.rational_b_spline_curve.weights  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.list_to_array()](../../d4/ddf/namespaceautomotive__design.html#ab7dc76b598137ee186868173eef1e979),
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

def automotive_design.rational_b_spline_curve.weights_data  | ( | | ) |   
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

def automotive_design.rational_b_spline_curve.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.b_spline_curve](../../db/d4c/classautomotive__design_1_1b__spline__curve.html#a829091a18fd135e17b2b1ac639c5e510).

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

def automotive_design.rational_b_spline_curve.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.curve_weights_positive()](../../d4/ddf/namespaceautomotive__design.html#ad092d6cbe9549f1afc9b3000317ad243).

## Member Data Documentation

## ◆ weights_data

automotive_design.rational_b_spline_curve.weights_data  
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

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

