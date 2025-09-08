---
url: https://freecad.github.io/SourceDoc/df/d23/classconfig__control__design_1_1rectangular__composite__surface.html
scraped_at: 2025-09-08T15:23:33.682185
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [rectangular_composite_surface](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html)

[List of all members](../../d9/d4b/classconfig__control__design_1_1rectangular__composite__surface-members.html) | Public Member Functions | Public Attributes

config_control_design.rectangular_composite_surface Class Reference

##  Public Member Functions  
  
---  
def | [n_u](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#a46c4af2f490bd2d65613e06ea3bf530e) ()  
def | [n_v](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#abc79a02565c5628da0423b8af53f5a1a) ()  
def | [segments](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#a08aa8c1e1af0edf4b3c2a58bd3650b61) ()  
def | [wr1](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#ac31aeab4af00b3f915b8d9d8efa69acb) (self)  
def | [wr2](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#ac1625e84845e3415b3d07af275d27f4e) (self)  
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
[segments](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#a793546bdb7074e54a4781a12b91defc9)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity rectangular_composite_surface definition.
    
        :param segments
        :type segments:LIST(1,None,LIST(1,None,'surface_patch', scope = schema_scope))
    
        :param n_u
        :type n_u:INTEGER
    
        :param n_v
        :type n_v:INTEGER

## Member Function Documentation

## ◆ n_u()

def config_control_design.rectangular_composite_surface.n_u  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.solid_with_stepped_round_hole.segments,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve.segments,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_composite_surface.segments,
[automotive_design.composite_curve.segments](../../de/d2c/classautomotive__design_1_1composite__curve.html#a568c2816d1f69a0584b0e631b61b6384),
[automotive_design.rectangular_composite_surface.segments](../../d0/d43/classautomotive__design_1_1rectangular__composite__surface.html#a9d54216c528b18fdb2062ac14feac57e),
[config_control_design.composite_curve.segments](../../d9/d22/classconfig__control__design_1_1composite__curve.html#ae8a5053338a65c76f329af7bfa3350fe),
[config_control_design.rectangular_composite_surface.segments](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#a793546bdb7074e54a4781a12b91defc9),
[ifc2x3.ifccompositecurve.segments](../../d5/d63/classifc2x3_1_1ifccompositecurve.html#a10d41f61d9a1af3e987bbfb7c93a90a5),
[ifc4.ifccompositecurve.segments](../../d2/d3c/classifc4_1_1ifccompositecurve.html#ae3fe98d5766b1a76603b35bcc7a9a16a),
[MeshCore::MeshSurfaceSegment.segments](../../d8/dcb/classMeshCore_1_1MeshSurfaceSegment.html#a1052c424817f18435e774f445e6cc5c2),
MeshPart::BrepMesh.segments, MeshPart::Mesher.segments,
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.segments](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a251d9ef635d56c2399d0840df469fa8d),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.segments](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a38bcf4c122952fa801be7142491a2a1e),
[Mod.PartDesign.WizardShaft.ShaftFeature.ShaftFeature.segments](../../d4/d7b/classMod_1_1PartDesign_1_1WizardShaft_1_1ShaftFeature_1_1ShaftFeature.html#a0d10d549bf4e0383fc36f94efb19dbfc),
[Path::Voronoi::diagram_type.segments](../../d8/d4a/classPath_1_1Voronoi_1_1diagram__type.html#a65b03e05a41b8bdd7e0061fb89e0924d),
KDL::Chain.segments, KDL::Tree.segments, and
[TechDraw::BSpline.segments](../../d6/d09/classTechDraw_1_1BSpline.html#ac406ffc8ad00a1c32e074716d81a5d93).

## ◆ n_v()

def config_control_design.rectangular_composite_surface.n_v  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.solid_with_stepped_round_hole.segments,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve.segments,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_composite_surface.segments,
[automotive_design.composite_curve.segments](../../de/d2c/classautomotive__design_1_1composite__curve.html#a568c2816d1f69a0584b0e631b61b6384),
[automotive_design.rectangular_composite_surface.segments](../../d0/d43/classautomotive__design_1_1rectangular__composite__surface.html#a9d54216c528b18fdb2062ac14feac57e),
[config_control_design.composite_curve.segments](../../d9/d22/classconfig__control__design_1_1composite__curve.html#ae8a5053338a65c76f329af7bfa3350fe),
[config_control_design.rectangular_composite_surface.segments](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#a793546bdb7074e54a4781a12b91defc9),
[ifc2x3.ifccompositecurve.segments](../../d5/d63/classifc2x3_1_1ifccompositecurve.html#a10d41f61d9a1af3e987bbfb7c93a90a5),
[ifc4.ifccompositecurve.segments](../../d2/d3c/classifc4_1_1ifccompositecurve.html#ae3fe98d5766b1a76603b35bcc7a9a16a),
[MeshCore::MeshSurfaceSegment.segments](../../d8/dcb/classMeshCore_1_1MeshSurfaceSegment.html#a1052c424817f18435e774f445e6cc5c2),
MeshPart::BrepMesh.segments, MeshPart::Mesher.segments,
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.segments](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a251d9ef635d56c2399d0840df469fa8d),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.segments](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a38bcf4c122952fa801be7142491a2a1e),
[Mod.PartDesign.WizardShaft.ShaftFeature.ShaftFeature.segments](../../d4/d7b/classMod_1_1PartDesign_1_1WizardShaft_1_1ShaftFeature_1_1ShaftFeature.html#a0d10d549bf4e0383fc36f94efb19dbfc),
[Path::Voronoi::diagram_type.segments](../../d8/d4a/classPath_1_1Voronoi_1_1diagram__type.html#a65b03e05a41b8bdd7e0061fb89e0924d),
KDL::Chain.segments, KDL::Tree.segments, and
[TechDraw::BSpline.segments](../../d6/d09/classTechDraw_1_1BSpline.html#ac406ffc8ad00a1c32e074716d81a5d93).

## ◆ segments()

def config_control_design.rectangular_composite_surface.segments  | ( | | ) |   
---|---|---|---|---  
  
References VISCOUS_2D::_SegmentTree._segments,
VISCOUS_2D::_PolyLine._segments,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.solid_with_stepped_round_hole._segments,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve._segments,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rectangular_composite_surface._segments,
automotive_design.composite_curve._segments,
automotive_design.rectangular_composite_surface._segments,
config_control_design.composite_curve._segments,
config_control_design.rectangular_composite_surface._segments,
ifc2x3.ifccompositecurve._segments, ifc4.ifccompositecurve._segments, and
Mesh::MeshObject._segments.

Referenced by
[Mod.PartDesign.WizardShaft.Shaft.Shaft.addSegment()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#af319eb97781c3009a5aa91127a1d3db4),
[Mod.PartDesign.WizardShaft.ShaftFeature.ShaftFeature.addSegment()](../../d4/d7b/classMod_1_1PartDesign_1_1WizardShaft_1_1ShaftFeature_1_1ShaftFeature.html#a414dc2d25efbb1bab5aeafe8c4a68d01),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.addSegment()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a73f34ba120a3641c2169927f34d29564),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.buildFromDict()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a2c57f83e52f39c635284f45cc053dda1),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.clone()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#ad92aa172c3deeaae22d2c9a323401581),
[automotive_design.composite_curve.closed_curve()](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6b988086709b2d29b533fa3145010e1d),
[config_control_design.composite_curve.closed_curve()](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a606f93c957672f4e687eeb1e9b043943),
[ifc2x3.ifccompositecurve.closedcurve()](../../d5/d63/classifc2x3_1_1ifccompositecurve.html#abe11170956a9bdb9fb2f6b79755654f6),
[ifc4.ifccompositecurve.closedcurve()](../../d2/d3c/classifc4_1_1ifccompositecurve.html#aacdc4b96c7973938b35ac746950227bf),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.editConstraint()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a2a556795c1c955fda7894cbcf86821ca),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.equilibrium()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#abf673f8921374b011ced4c4a770d44e6),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.evaluate()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a53b2bca87ec4a37fbc548844bc74212d),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.findSegment()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#ad3edcede1160ed861fd173c6603b177d),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.getConstraint()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a73a9a809bcb19b3656b4741f3f25d187),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.getLengthTo()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a18723abe21145e0827ff9715ec27a806),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.index()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#acdbb4a0cb4437b86f5f1a57d9b9759d0),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.integrate()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a970224c8c0203e03fce6e48929c3ca0d),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.isZero()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#af6041af2936203051b7f862cb6f75954),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.lowervalue()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a6195357a490bbc09983af0098f46ec9f),
[automotive_design.composite_curve.n_segments()](../../de/d2c/classautomotive__design_1_1composite__curve.html#ad537919a3fcbf060a73068a13add3be9),
[config_control_design.composite_curve.n_segments()](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a7c1b752f8fd4e84d36657c2481563d37),
[automotive_design.rectangular_composite_surface.n_u()](../../d0/d43/classautomotive__design_1_1rectangular__composite__surface.html#a3d12a335b5ce7054dbd70d99324ec71f),
[config_control_design.rectangular_composite_surface.n_u()](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#a46c4af2f490bd2d65613e06ea3bf530e),
[automotive_design.rectangular_composite_surface.n_v()](../../d0/d43/classautomotive__design_1_1rectangular__composite__surface.html#ae6762f8b09e0e9aef037568cd1f22a43),
[config_control_design.rectangular_composite_surface.n_v()](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#abc79a02565c5628da0423b8af53f5a1a),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.negate()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aabae4b0090390577c0a0c965916ed1ee),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.negated()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a5795b736757b320867de23b236ab1a53),
[ifc2x3.ifccompositecurve.nsegments()](../../d5/d63/classifc2x3_1_1ifccompositecurve.html#a9296c39341a8df10ce8f6efb8a9128a7),
[ifc4.ifccompositecurve.nsegments()](../../d2/d3c/classifc4_1_1ifccompositecurve.html#a3214b9535637708eb75ca0d718836526),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.output()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aeedd5f59969cc27432880d1916f3d7f9),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.showDiagram()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#ac648180672c3434f2214d26ff3bd2cde),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.updateConstraint()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#ab68630f3abfd4af53b7a2ad324b48fc4),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.updateSegment()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a85eed6d628ef239013e65c073c7e96e5),
and
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.value()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#ad7d5b047ccc55b6711c2f47004b18c0e).

## ◆ wr1()

def config_control_design.rectangular_composite_surface.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13).

## ◆ wr2()

def config_control_design.rectangular_composite_surface.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[config_control_design.constraints_rectangular_composite_surface()](../../d4/d07/namespaceconfig__control__design.html#a016b25ed29f2dd3424c067bcb48dc1e8).

## Member Data Documentation

## ◆ segments

config_control_design.rectangular_composite_surface.segments  
---  
  
Referenced by
[Mod.PartDesign.WizardShaft.Shaft.Shaft.addSegment()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#af319eb97781c3009a5aa91127a1d3db4),
[Mod.PartDesign.WizardShaft.ShaftFeature.ShaftFeature.addSegment()](../../d4/d7b/classMod_1_1PartDesign_1_1WizardShaft_1_1ShaftFeature_1_1ShaftFeature.html#a414dc2d25efbb1bab5aeafe8c4a68d01),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.addSegment()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a73f34ba120a3641c2169927f34d29564),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.buildFromDict()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a2c57f83e52f39c635284f45cc053dda1),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.clone()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#ad92aa172c3deeaae22d2c9a323401581),
[automotive_design.composite_curve.closed_curve()](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6b988086709b2d29b533fa3145010e1d),
[config_control_design.composite_curve.closed_curve()](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a606f93c957672f4e687eeb1e9b043943),
[ifc2x3.ifccompositecurve.closedcurve()](../../d5/d63/classifc2x3_1_1ifccompositecurve.html#abe11170956a9bdb9fb2f6b79755654f6),
[ifc4.ifccompositecurve.closedcurve()](../../d2/d3c/classifc4_1_1ifccompositecurve.html#aacdc4b96c7973938b35ac746950227bf),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.editConstraint()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a2a556795c1c955fda7894cbcf86821ca),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.equilibrium()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#abf673f8921374b011ced4c4a770d44e6),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.evaluate()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a53b2bca87ec4a37fbc548844bc74212d),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.findSegment()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#ad3edcede1160ed861fd173c6603b177d),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.getConstraint()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a73a9a809bcb19b3656b4741f3f25d187),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.getLengthTo()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a18723abe21145e0827ff9715ec27a806),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.index()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#acdbb4a0cb4437b86f5f1a57d9b9759d0),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.integrate()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a970224c8c0203e03fce6e48929c3ca0d),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.isZero()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#af6041af2936203051b7f862cb6f75954),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.lowervalue()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a6195357a490bbc09983af0098f46ec9f),
[automotive_design.composite_curve.n_segments()](../../de/d2c/classautomotive__design_1_1composite__curve.html#ad537919a3fcbf060a73068a13add3be9),
[config_control_design.composite_curve.n_segments()](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a7c1b752f8fd4e84d36657c2481563d37),
[automotive_design.rectangular_composite_surface.n_u()](../../d0/d43/classautomotive__design_1_1rectangular__composite__surface.html#a3d12a335b5ce7054dbd70d99324ec71f),
[config_control_design.rectangular_composite_surface.n_u()](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#a46c4af2f490bd2d65613e06ea3bf530e),
[automotive_design.rectangular_composite_surface.n_v()](../../d0/d43/classautomotive__design_1_1rectangular__composite__surface.html#ae6762f8b09e0e9aef037568cd1f22a43),
[config_control_design.rectangular_composite_surface.n_v()](../../df/d23/classconfig__control__design_1_1rectangular__composite__surface.html#abc79a02565c5628da0423b8af53f5a1a),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.negate()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aabae4b0090390577c0a0c965916ed1ee),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.negated()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a5795b736757b320867de23b236ab1a53),
[ifc2x3.ifccompositecurve.nsegments()](../../d5/d63/classifc2x3_1_1ifccompositecurve.html#a9296c39341a8df10ce8f6efb8a9128a7),
[ifc4.ifccompositecurve.nsegments()](../../d2/d3c/classifc4_1_1ifccompositecurve.html#a3214b9535637708eb75ca0d718836526),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.output()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aeedd5f59969cc27432880d1916f3d7f9),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.showDiagram()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#ac648180672c3434f2214d26ff3bd2cde),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.updateConstraint()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#ab68630f3abfd4af53b7a2ad324b48fc4),
[Mod.PartDesign.WizardShaft.Shaft.Shaft.updateSegment()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a85eed6d628ef239013e65c073c7e96e5),
and
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.value()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#ad7d5b047ccc55b6711c2f47004b18c0e).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

