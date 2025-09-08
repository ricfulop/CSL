---
url: https://freecad.github.io/SourceDoc/d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html
scraped_at: 2025-09-08T15:11:38.663937
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [rectangular_trimmed_surface](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html)

[List of all members](../../d9/da5/classautomotive__design_1_1rectangular__trimmed__surface-members.html) | Public Member Functions | Public Attributes

automotive_design.rectangular_trimmed_surface Class Reference

##  Public Member Functions  
  
---  
def | [basis_surface](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#af66917c9257691b24edf825bfbd80e3e) ()  
def | [u1](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a7fa03a8a623373ac8f68da03aeb0eef8) ()  
def | [u2](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#ac4137d14e87117f488f60a625930b8be) ()  
def | [usense](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#ae5e74fca2e85da76b8c103e4062f02a0) ()  
def | [v1](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a1d822c44b6436e4ddeae95c9be08c068) ()  
def | [v2](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a40337bca48c6839bdb418abb545ad6f7) ()  
def | [vsense](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a92d633e67689d370539d8a425d26dd73) ()  
def | [wr1](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#ab6342084bde80740f75f1b7f8b41f2ac) (self)  
def | [wr2](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a08af6d5de821e783c54cc675d0ae4997) (self)  
def | [wr3](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801) (self)  
def | [wr4](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939) (self)  
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
[basis_surface](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#aed9764c3a03e2191bba3317e28371b00)  
|
[u1](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a838bc1b559aa8286f25e14d0b12cb3f2)  
|
[u2](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a2501a5fed9fca354a7ba0f1c8b6d49a9)  
|
[usense](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a8f1cd80094a1c52dbeea04c696b9ed58)  
|
[v1](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#aa0a543cf98a11f4f50f8815ceec2b038)  
|
[v2](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a2a2873579d00270cb90e7aa0b4af5146)  
|
[vsense](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#aa48d24ed601f52ab224cec854c02ad4e)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity rectangular_trimmed_surface definition.
    
        :param basis_surface
        :type basis_surface:surface
    
        :param u1
        :type u1:parameter_value
    
        :param u2
        :type u2:parameter_value
    
        :param v1
        :type v1:parameter_value
    
        :param v2
        :type v2:parameter_value
    
        :param usense
        :type usense:BOOLEAN
    
        :param vsense
        :type vsense:BOOLEAN

## Member Function Documentation

## ◆ basis_surface()

def automotive_design.rectangular_trimmed_surface.basis_surface  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_surface._basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.point_on_surface._basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.pcurve._basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface._basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.degenerate_pcurve._basis_surface,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_bounded_surface._basis_surface,
automotive_design.offset_surface._basis_surface,
automotive_design.point_on_surface._basis_surface,
automotive_design.pcurve._basis_surface,
automotive_design.rectangular_trimmed_surface._basis_surface,
automotive_design.degenerate_pcurve._basis_surface,
automotive_design.curve_bounded_surface._basis_surface,
config_control_design.offset_surface._basis_surface,
config_control_design.point_on_surface._basis_surface,
config_control_design.pcurve._basis_surface,
config_control_design.rectangular_trimmed_surface._basis_surface,
config_control_design.degenerate_pcurve._basis_surface, and
config_control_design.curve_bounded_surface._basis_surface.

Referenced by
[automotive_design.swept_area_solid.wr1()](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#af06ba2d89fb93f3538bd0cfb3899ca7d),
[automotive_design.surface_curve_swept_area_solid.wr1()](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773),
[automotive_design.composite_curve_on_surface.wr1()](../../d9/d62/classautomotive__design_1_1composite__curve__on__surface.html#aa4c4c80418d0ac5f7c0d8c14865f4126),
[config_control_design.composite_curve_on_surface.wr1()](../../da/d0c/classconfig__control__design_1_1composite__curve__on__surface.html#af1248e63f087994050d924b1f03ce2a7),
[automotive_design.curve_bounded_surface.wr2()](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#aee9bebad9973fccb90b85a3418fe6259),
[config_control_design.curve_bounded_surface.wr2()](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a6c40b7a7eaace49a3aabfe3fa47d2a35),
[automotive_design.rectangular_trimmed_surface.wr3()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801),
[config_control_design.rectangular_trimmed_surface.wr3()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#af917d1182a7d07aa13d556e19e3be76a),
[automotive_design.rectangular_trimmed_surface.wr4()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939),
and
[config_control_design.rectangular_trimmed_surface.wr4()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a58eb9b75ab01c968f17742257c5de3e2).

## ◆ u1()

def automotive_design.rectangular_trimmed_surface.u1  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface._u1,
automotive_design.rectangular_trimmed_surface._u1,
config_control_design.rectangular_trimmed_surface._u1,
ifc2x3.ifcrectangulartrimmedsurface._u1, and
ifc4.ifcrectangulartrimmedsurface._u1.

Referenced by
[ifc4.ifcrectangulartrimmedsurface.u1andu2different()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#aa5b4a7fef83f4bf838b1cf14976ca87a),
[ifc4.ifcrectangulartrimmedsurface.usensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a8ea572c839b78784e147b1c5aa4100fe),
[automotive_design.rectangular_trimmed_surface.wr1()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#ab6342084bde80740f75f1b7f8b41f2ac),
[config_control_design.rectangular_trimmed_surface.wr1()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a44a102b137d46fed49015ee7810a342b),
[ifc2x3.ifcrectangulartrimmedsurface.wr1()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#aaff0b4df1f021e5c54aa51f8a1715f24),
[automotive_design.rectangular_trimmed_surface.wr3()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801),
[config_control_design.rectangular_trimmed_surface.wr3()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#af917d1182a7d07aa13d556e19e3be76a),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr3()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a9497a0e529fbd8cadb95d8572030d934).

## ◆ u2()

def automotive_design.rectangular_trimmed_surface.u2  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface._u2,
automotive_design.rectangular_trimmed_surface._u2,
config_control_design.rectangular_trimmed_surface._u2,
ifc2x3.ifcrectangulartrimmedsurface._u2, and
ifc4.ifcrectangulartrimmedsurface._u2.

Referenced by
[ifc4.ifcrectangulartrimmedsurface.u1andu2different()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#aa5b4a7fef83f4bf838b1cf14976ca87a),
[ifc4.ifcrectangulartrimmedsurface.usensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a8ea572c839b78784e147b1c5aa4100fe),
[automotive_design.rectangular_trimmed_surface.wr1()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#ab6342084bde80740f75f1b7f8b41f2ac),
[config_control_design.rectangular_trimmed_surface.wr1()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a44a102b137d46fed49015ee7810a342b),
[ifc2x3.ifcrectangulartrimmedsurface.wr1()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#aaff0b4df1f021e5c54aa51f8a1715f24),
[automotive_design.rectangular_trimmed_surface.wr3()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801),
[config_control_design.rectangular_trimmed_surface.wr3()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#af917d1182a7d07aa13d556e19e3be76a),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr3()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a9497a0e529fbd8cadb95d8572030d934).

## ◆ usense()

def automotive_design.rectangular_trimmed_surface.usense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface._usense,
automotive_design.rectangular_trimmed_surface._usense,
config_control_design.rectangular_trimmed_surface._usense,
ifc2x3.ifcrectangulartrimmedsurface._usense, and
ifc4.ifcrectangulartrimmedsurface._usense.

Referenced by
[ifc4.ifcrectangulartrimmedsurface.usensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a8ea572c839b78784e147b1c5aa4100fe),
[automotive_design.rectangular_trimmed_surface.wr3()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801),
[config_control_design.rectangular_trimmed_surface.wr3()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#af917d1182a7d07aa13d556e19e3be76a),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr3()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a9497a0e529fbd8cadb95d8572030d934).

## ◆ v1()

def automotive_design.rectangular_trimmed_surface.v1  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface._v1,
automotive_design.rectangular_trimmed_surface._v1,
config_control_design.rectangular_trimmed_surface._v1,
ifc2x3.ifcrectangulartrimmedsurface._v1, and
ifc4.ifcrectangulartrimmedsurface._v1.

Referenced by
[ifc4.ifcrectangulartrimmedsurface.v1andv2different()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a66398a7e0b8ada8fb0aff78bb5e47177),
[ifc4.ifcrectangulartrimmedsurface.vsensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a50985c501c44ee45facb0c1ef9edc280),
[automotive_design.rectangular_trimmed_surface.wr2()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a08af6d5de821e783c54cc675d0ae4997),
[config_control_design.rectangular_trimmed_surface.wr2()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a3596a94c33e8507d7d2601984c8eec68),
[ifc2x3.ifcrectangulartrimmedsurface.wr2()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#afaeded3bb2633818accd0d3994944f15),
[automotive_design.rectangular_trimmed_surface.wr4()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939),
[config_control_design.rectangular_trimmed_surface.wr4()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a58eb9b75ab01c968f17742257c5de3e2),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr4()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#ad434b58ab56136cf8dee0b98291a3b7a).

## ◆ v2()

def automotive_design.rectangular_trimmed_surface.v2  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface._v2,
automotive_design.rectangular_trimmed_surface._v2,
config_control_design.rectangular_trimmed_surface._v2,
ifc2x3.ifcrectangulartrimmedsurface._v2, and
ifc4.ifcrectangulartrimmedsurface._v2.

Referenced by
[ifc4.ifcrectangulartrimmedsurface.v1andv2different()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a66398a7e0b8ada8fb0aff78bb5e47177),
[ifc4.ifcrectangulartrimmedsurface.vsensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a50985c501c44ee45facb0c1ef9edc280),
[automotive_design.rectangular_trimmed_surface.wr2()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a08af6d5de821e783c54cc675d0ae4997),
[config_control_design.rectangular_trimmed_surface.wr2()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a3596a94c33e8507d7d2601984c8eec68),
[ifc2x3.ifcrectangulartrimmedsurface.wr2()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#afaeded3bb2633818accd0d3994944f15),
[automotive_design.rectangular_trimmed_surface.wr4()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939),
[config_control_design.rectangular_trimmed_surface.wr4()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a58eb9b75ab01c968f17742257c5de3e2),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr4()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#ad434b58ab56136cf8dee0b98291a3b7a).

## ◆ vsense()

def automotive_design.rectangular_trimmed_surface.vsense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface._vsense,
automotive_design.rectangular_trimmed_surface._vsense,
config_control_design.rectangular_trimmed_surface._vsense,
ifc2x3.ifcrectangulartrimmedsurface._vsense, and
ifc4.ifcrectangulartrimmedsurface._vsense.

Referenced by
[ifc4.ifcrectangulartrimmedsurface.vsensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a50985c501c44ee45facb0c1ef9edc280),
[automotive_design.rectangular_trimmed_surface.wr4()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939),
[config_control_design.rectangular_trimmed_surface.wr4()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a58eb9b75ab01c968f17742257c5de3e2),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr4()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#ad434b58ab56136cf8dee0b98291a3b7a).

## ◆ wr1()

def automotive_design.rectangular_trimmed_surface.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.u1,
[automotive_design.rectangular_trimmed_surface.u1](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a838bc1b559aa8286f25e14d0b12cb3f2),
[config_control_design.rectangular_trimmed_surface.u1](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a7d8ddf37bd734edbe1386248ab65c930),
[ifc2x3.ifcrectangulartrimmedsurface.u1](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a3d076d6a64246bce84c81e8680ef4cf2),
[ifc4.ifcrectangulartrimmedsurface.u1](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#ad762b4ceb43583642ecae10526be037f),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.u2,
[automotive_design.rectangular_trimmed_surface.u2](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a2501a5fed9fca354a7ba0f1c8b6d49a9),
[config_control_design.rectangular_trimmed_surface.u2](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a7f1785df7abda681b6ac1e8d1ca8f1e0),
[ifc2x3.ifcrectangulartrimmedsurface.u2](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#aebfbd5bb4bba2c6136e47b1568e03e8a),
and
[ifc4.ifcrectangulartrimmedsurface.u2](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#af164f6ea764b18145550d550ef910233).

## ◆ wr2()

def automotive_design.rectangular_trimmed_surface.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[StringGuard.v1](../../d2/d45/classStringGuard.html#a9875eb97f905c102c2bd75c5f3f861ed),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.v1,
[automotive_design.rectangular_trimmed_surface.v1](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#aa0a543cf98a11f4f50f8815ceec2b038),
[config_control_design.rectangular_trimmed_surface.v1](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a606cf9de296e547f2885ad27a6c13fed),
[ifc2x3.ifcrectangulartrimmedsurface.v1](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a63a15ac64e07d09d9509fc0e61b5627d),
[ifc4.ifcrectangulartrimmedsurface.v1](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#ab7acd54013a6f2f7a31c205d39eca082),
[Part::EdgePoints.v1](../../db/dda/structPart_1_1EdgePoints.html#aebfdd41a8f4ca6b3d31264c4c86d71b2),
geoff_geometry::Triangle3d.v1,
[TechDraw::WalkerEdge.v1](../../d1/d56/classTechDraw_1_1WalkerEdge.html#a45c5e3f5898399f352e071c165e3c2ed),
[EdgePoints.v1](../../d3/d11/structEdgePoints.html#a91125ede8871f3767615b1f6286f6013),
[StringGuard.v2](../../d2/d45/classStringGuard.html#a7b8888ba31239e2172fba9b56c82aacb),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.v2,
[automotive_design.rectangular_trimmed_surface.v2](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a2a2873579d00270cb90e7aa0b4af5146),
[config_control_design.rectangular_trimmed_surface.v2](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a5d34eef55d8bec8c55c398af29e8fb32),
[ifc2x3.ifcrectangulartrimmedsurface.v2](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#acac5aa3580414757776155b4469961b9),
[ifc4.ifcrectangulartrimmedsurface.v2](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#af6a61cca6757c0573cedcf81bf086895),
[Part::EdgePoints.v2](../../db/dda/structPart_1_1EdgePoints.html#a4d62ea88a24625865e0730d383f9dff9),
[TechDraw::WalkerEdge.v2](../../d1/d56/classTechDraw_1_1WalkerEdge.html#af1d1164b0760f7090c558d54cfb3d024),
and
[EdgePoints.v2](../../d3/d11/structEdgePoints.html#af70f9e9674732c7ce136669c9d1d2edb).

## ◆ wr3()

def automotive_design.rectangular_trimmed_surface.wr3  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
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
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.u1,
[automotive_design.rectangular_trimmed_surface.u1](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a838bc1b559aa8286f25e14d0b12cb3f2),
[config_control_design.rectangular_trimmed_surface.u1](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a7d8ddf37bd734edbe1386248ab65c930),
[ifc2x3.ifcrectangulartrimmedsurface.u1](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a3d076d6a64246bce84c81e8680ef4cf2),
[ifc4.ifcrectangulartrimmedsurface.u1](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#ad762b4ceb43583642ecae10526be037f),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.u2,
[automotive_design.rectangular_trimmed_surface.u2](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a2501a5fed9fca354a7ba0f1c8b6d49a9),
[config_control_design.rectangular_trimmed_surface.u2](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a7f1785df7abda681b6ac1e8d1ca8f1e0),
[ifc2x3.ifcrectangulartrimmedsurface.u2](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#aebfbd5bb4bba2c6136e47b1568e03e8a),
[ifc4.ifcrectangulartrimmedsurface.u2](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#af164f6ea764b18145550d550ef910233),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.usense,
[automotive_design.rectangular_trimmed_surface.usense](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a8f1cd80094a1c52dbeea04c696b9ed58),
[config_control_design.rectangular_trimmed_surface.usense](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a0c6777b3887fcd51a080bc1959e9f55e),
[ifc2x3.ifcrectangulartrimmedsurface.usense](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#ab8677ca020a12bb7d6d1335d29feee29),
and
[ifc4.ifcrectangulartrimmedsurface.usense](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a4585fc33752ece0df888b0563591b294).

## ◆ wr4()

def automotive_design.rectangular_trimmed_surface.wr4  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
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
[StringGuard.v1](../../d2/d45/classStringGuard.html#a9875eb97f905c102c2bd75c5f3f861ed),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.v1,
[automotive_design.rectangular_trimmed_surface.v1](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#aa0a543cf98a11f4f50f8815ceec2b038),
[config_control_design.rectangular_trimmed_surface.v1](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a606cf9de296e547f2885ad27a6c13fed),
[ifc2x3.ifcrectangulartrimmedsurface.v1](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a63a15ac64e07d09d9509fc0e61b5627d),
[ifc4.ifcrectangulartrimmedsurface.v1](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#ab7acd54013a6f2f7a31c205d39eca082),
[Part::EdgePoints.v1](../../db/dda/structPart_1_1EdgePoints.html#aebfdd41a8f4ca6b3d31264c4c86d71b2),
geoff_geometry::Triangle3d.v1,
[TechDraw::WalkerEdge.v1](../../d1/d56/classTechDraw_1_1WalkerEdge.html#a45c5e3f5898399f352e071c165e3c2ed),
[EdgePoints.v1](../../d3/d11/structEdgePoints.html#a91125ede8871f3767615b1f6286f6013),
[StringGuard.v2](../../d2/d45/classStringGuard.html#a7b8888ba31239e2172fba9b56c82aacb),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.v2,
[automotive_design.rectangular_trimmed_surface.v2](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a2a2873579d00270cb90e7aa0b4af5146),
[config_control_design.rectangular_trimmed_surface.v2](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a5d34eef55d8bec8c55c398af29e8fb32),
[ifc2x3.ifcrectangulartrimmedsurface.v2](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#acac5aa3580414757776155b4469961b9),
[ifc4.ifcrectangulartrimmedsurface.v2](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#af6a61cca6757c0573cedcf81bf086895),
[Part::EdgePoints.v2](../../db/dda/structPart_1_1EdgePoints.html#a4d62ea88a24625865e0730d383f9dff9),
[TechDraw::WalkerEdge.v2](../../d1/d56/classTechDraw_1_1WalkerEdge.html#af1d1164b0760f7090c558d54cfb3d024),
[EdgePoints.v2](../../d3/d11/structEdgePoints.html#af70f9e9674732c7ce136669c9d1d2edb),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_trimmed_surface.vsense,
[automotive_design.rectangular_trimmed_surface.vsense](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#aa48d24ed601f52ab224cec854c02ad4e),
[config_control_design.rectangular_trimmed_surface.vsense](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a05ad8d0c9c28c58953d29003e677130b),
[ifc2x3.ifcrectangulartrimmedsurface.vsense](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a0bff684909a753295f64c7de1cebe336),
and
[ifc4.ifcrectangulartrimmedsurface.vsense](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a798b0668cfa777b5bac2276845aa2cda).

## Member Data Documentation

## ◆ basis_surface

automotive_design.rectangular_trimmed_surface.basis_surface  
---  
  
Referenced by
[automotive_design.swept_area_solid.wr1()](../../d9/d56/classautomotive__design_1_1swept__area__solid.html#af06ba2d89fb93f3538bd0cfb3899ca7d),
[automotive_design.surface_curve_swept_area_solid.wr1()](../../dc/db7/classautomotive__design_1_1surface__curve__swept__area__solid.html#a9c3872eaf0dbc9d98d40429cc3dbf773),
[automotive_design.composite_curve_on_surface.wr1()](../../d9/d62/classautomotive__design_1_1composite__curve__on__surface.html#aa4c4c80418d0ac5f7c0d8c14865f4126),
[config_control_design.composite_curve_on_surface.wr1()](../../da/d0c/classconfig__control__design_1_1composite__curve__on__surface.html#af1248e63f087994050d924b1f03ce2a7),
[automotive_design.curve_bounded_surface.wr2()](../../de/dfd/classautomotive__design_1_1curve__bounded__surface.html#aee9bebad9973fccb90b85a3418fe6259),
[config_control_design.curve_bounded_surface.wr2()](../../dc/d61/classconfig__control__design_1_1curve__bounded__surface.html#a6c40b7a7eaace49a3aabfe3fa47d2a35),
[automotive_design.rectangular_trimmed_surface.wr3()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801),
[config_control_design.rectangular_trimmed_surface.wr3()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#af917d1182a7d07aa13d556e19e3be76a),
[automotive_design.rectangular_trimmed_surface.wr4()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939),
and
[config_control_design.rectangular_trimmed_surface.wr4()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a58eb9b75ab01c968f17742257c5de3e2).

## ◆ u1

automotive_design.rectangular_trimmed_surface.u1  
---  
  
Referenced by
[ifc4.ifcrectangulartrimmedsurface.u1andu2different()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#aa5b4a7fef83f4bf838b1cf14976ca87a),
[ifc4.ifcrectangulartrimmedsurface.usensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a8ea572c839b78784e147b1c5aa4100fe),
[automotive_design.rectangular_trimmed_surface.wr1()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#ab6342084bde80740f75f1b7f8b41f2ac),
[config_control_design.rectangular_trimmed_surface.wr1()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a44a102b137d46fed49015ee7810a342b),
[ifc2x3.ifcrectangulartrimmedsurface.wr1()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#aaff0b4df1f021e5c54aa51f8a1715f24),
[automotive_design.rectangular_trimmed_surface.wr3()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801),
[config_control_design.rectangular_trimmed_surface.wr3()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#af917d1182a7d07aa13d556e19e3be76a),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr3()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a9497a0e529fbd8cadb95d8572030d934).

## ◆ u2

automotive_design.rectangular_trimmed_surface.u2  
---  
  
Referenced by
[ifc4.ifcrectangulartrimmedsurface.u1andu2different()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#aa5b4a7fef83f4bf838b1cf14976ca87a),
[ifc4.ifcrectangulartrimmedsurface.usensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a8ea572c839b78784e147b1c5aa4100fe),
[automotive_design.rectangular_trimmed_surface.wr1()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#ab6342084bde80740f75f1b7f8b41f2ac),
[config_control_design.rectangular_trimmed_surface.wr1()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a44a102b137d46fed49015ee7810a342b),
[ifc2x3.ifcrectangulartrimmedsurface.wr1()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#aaff0b4df1f021e5c54aa51f8a1715f24),
[automotive_design.rectangular_trimmed_surface.wr3()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801),
[config_control_design.rectangular_trimmed_surface.wr3()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#af917d1182a7d07aa13d556e19e3be76a),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr3()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a9497a0e529fbd8cadb95d8572030d934).

## ◆ usense

automotive_design.rectangular_trimmed_surface.usense  
---  
  
Referenced by
[ifc4.ifcrectangulartrimmedsurface.usensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a8ea572c839b78784e147b1c5aa4100fe),
[automotive_design.rectangular_trimmed_surface.wr3()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a4c4fa09bc28e0979821dcb919bc70801),
[config_control_design.rectangular_trimmed_surface.wr3()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#af917d1182a7d07aa13d556e19e3be76a),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr3()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a9497a0e529fbd8cadb95d8572030d934).

## ◆ v1

automotive_design.rectangular_trimmed_surface.v1  
---  
  
Referenced by
[ifc4.ifcrectangulartrimmedsurface.v1andv2different()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a66398a7e0b8ada8fb0aff78bb5e47177),
[ifc4.ifcrectangulartrimmedsurface.vsensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a50985c501c44ee45facb0c1ef9edc280),
[automotive_design.rectangular_trimmed_surface.wr2()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a08af6d5de821e783c54cc675d0ae4997),
[config_control_design.rectangular_trimmed_surface.wr2()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a3596a94c33e8507d7d2601984c8eec68),
[ifc2x3.ifcrectangulartrimmedsurface.wr2()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#afaeded3bb2633818accd0d3994944f15),
[automotive_design.rectangular_trimmed_surface.wr4()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939),
[config_control_design.rectangular_trimmed_surface.wr4()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a58eb9b75ab01c968f17742257c5de3e2),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr4()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#ad434b58ab56136cf8dee0b98291a3b7a).

## ◆ v2

automotive_design.rectangular_trimmed_surface.v2  
---  
  
Referenced by
[ifc4.ifcrectangulartrimmedsurface.v1andv2different()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a66398a7e0b8ada8fb0aff78bb5e47177),
[ifc4.ifcrectangulartrimmedsurface.vsensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a50985c501c44ee45facb0c1ef9edc280),
[automotive_design.rectangular_trimmed_surface.wr2()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#a08af6d5de821e783c54cc675d0ae4997),
[config_control_design.rectangular_trimmed_surface.wr2()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a3596a94c33e8507d7d2601984c8eec68),
[ifc2x3.ifcrectangulartrimmedsurface.wr2()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#afaeded3bb2633818accd0d3994944f15),
[automotive_design.rectangular_trimmed_surface.wr4()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939),
[config_control_design.rectangular_trimmed_surface.wr4()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a58eb9b75ab01c968f17742257c5de3e2),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr4()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#ad434b58ab56136cf8dee0b98291a3b7a).

## ◆ vsense

automotive_design.rectangular_trimmed_surface.vsense  
---  
  
Referenced by
[ifc4.ifcrectangulartrimmedsurface.vsensecompatible()](../../d2/d88/classifc4_1_1ifcrectangulartrimmedsurface.html#a50985c501c44ee45facb0c1ef9edc280),
[automotive_design.rectangular_trimmed_surface.wr4()](../../d3/d74/classautomotive__design_1_1rectangular__trimmed__surface.html#afc4757205d91cd02edfd30794d089939),
[config_control_design.rectangular_trimmed_surface.wr4()](../../d3/df2/classconfig__control__design_1_1rectangular__trimmed__surface.html#a58eb9b75ab01c968f17742257c5de3e2),
and
[ifc2x3.ifcrectangulartrimmedsurface.wr4()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#ad434b58ab56136cf8dee0b98291a3b7a).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

