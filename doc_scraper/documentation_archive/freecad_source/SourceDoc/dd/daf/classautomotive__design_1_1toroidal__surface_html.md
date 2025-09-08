---
url: https://freecad.github.io/SourceDoc/dd/daf/classautomotive__design_1_1toroidal__surface.html
scraped_at: 2025-09-08T15:14:44.415321
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [toroidal_surface](../../dd/daf/classautomotive__design_1_1toroidal__surface.html)

[List of all members](../../dd/df7/classautomotive__design_1_1toroidal__surface-members.html) | Public Member Functions | Public Attributes

automotive_design.toroidal_surface Class Reference

##  Public Member Functions  
  
---  
def | [major_radius](../../dd/daf/classautomotive__design_1_1toroidal__surface.html#a303bf5a44cf9d1c800324ee4b38065df) ()  
def | [minor_radius](../../dd/daf/classautomotive__design_1_1toroidal__surface.html#a609b055d5908d1ed8f2fb9ecf8f70935) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.elementary_surface](../../d9/d29/classautomotive__design_1_1elementary__surface.html)  
def | [position](../../d9/d29/classautomotive__design_1_1elementary__surface.html#a9423f2741b736eb18ce2de676b1d9f56) ()  
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
[major_radius](../../dd/daf/classautomotive__design_1_1toroidal__surface.html#a49c468b596d4042fc69d35d3da9a26e0)  
|
[minor_radius](../../dd/daf/classautomotive__design_1_1toroidal__surface.html#a867d306837362228ad9f822d18fb448d)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.elementary_surface](../../d9/d29/classautomotive__design_1_1elementary__surface.html)  
|
[position](../../d9/d29/classautomotive__design_1_1elementary__surface.html#a4068702c5244832f2abdbcc15226412e)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity toroidal_surface definition.
    
        :param major_radius
        :type major_radius:positive_length_measure
    
        :param minor_radius
        :type minor_radius:positive_length_measure

## Member Function Documentation

## ◆ major_radius()

def automotive_design.toroidal_surface.major_radius  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.toroidal_surface._major_radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus._major_radius,
automotive_design.toroidal_surface._major_radius,
automotive_design.torus._major_radius, and
config_control_design.toroidal_surface._major_radius.

Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

## ◆ minor_radius()

def automotive_design.toroidal_surface.minor_radius  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.toroidal_surface._minor_radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus._minor_radius,
automotive_design.toroidal_surface._minor_radius,
automotive_design.torus._minor_radius, and
config_control_design.toroidal_surface._minor_radius.

Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

## Member Data Documentation

## ◆ major_radius

automotive_design.toroidal_surface.major_radius  
---  
  
Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

## ◆ minor_radius

automotive_design.toroidal_surface.minor_radius  
---  
  
Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

