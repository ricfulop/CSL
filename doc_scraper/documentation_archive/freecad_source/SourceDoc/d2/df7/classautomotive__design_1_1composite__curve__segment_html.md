---
url: https://freecad.github.io/SourceDoc/d2/df7/classautomotive__design_1_1composite__curve__segment.html
scraped_at: 2025-09-08T15:02:08.298996
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [composite_curve_segment](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html)

[List of all members](../../d9/dd1/classautomotive__design_1_1composite__curve__segment-members.html) | Public Member Functions | Public Attributes

automotive_design.composite_curve_segment Class Reference

##  Public Member Functions  
  
---  
def | [parent_curve](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#a10d3a5b97183c85a907ab563e593c122) ()  
def | [same_sense](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#a1e0c27985f547779a15ee7a0d1977238) ()  
def | [transition](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#a2d7e94b426dafe978a3a2eff9e4658bb) ()  
def | [using_curves](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#ad6ca047500db0d951d83a46208ff4b8a) ()  
def | [wr1](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#a5631b696b5b2510fe9352894238be183) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.founded_item](../../d4/d12/classautomotive__design_1_1founded__item.html)  
def | [users](../../d4/d12/classautomotive__design_1_1founded__item.html#a0299c3fccdb8223cc8c9f590f7cee9a5) ()  
def | [wr1](../../d4/d12/classautomotive__design_1_1founded__item.html#a0668b2127d1c208daa93b2d435855a7f) (self)  
def | [wr2](../../d4/d12/classautomotive__design_1_1founded__item.html#a1ef4a4f4c94d46b616c25ec02609838f) (self)  
  
##  Public Attributes  
  
---  
|
[parent_curve](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#abebec68ca761166042d03848fd2a46cf)  
|
[same_sense](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#a3def3c3280e190d5ad7074cc06270e0d)  
|
[transition](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#abe359149c361f201ed16679b727e2a05)  
  
## Detailed Description

    
    
    Entity composite_curve_segment definition.
    
        :param transition
        :type transition:transition_code
    
        :param same_sense
        :type same_sense:BOOLEAN
    
        :param parent_curve
        :type parent_curve:curve
    
        :param using_curves
        :type using_curves:BAG(1,None,'composite_curve', scope = schema_scope)

## Member Function Documentation

## ◆ parent_curve()

def automotive_design.composite_curve_segment.parent_curve  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_replica._parent_curve,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve_segment._parent_curve,
automotive_design.curve_replica._parent_curve,
automotive_design.composite_curve_segment._parent_curve,
config_control_design.curve_replica._parent_curve, and
config_control_design.composite_curve_segment._parent_curve.

Referenced by
[automotive_design.composite_curve_segment.wr1()](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#a5631b696b5b2510fe9352894238be183),
[config_control_design.composite_curve_segment.wr1()](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#aa41973aa607ba41964959dcedb011dd7),
[automotive_design.curve_replica.wr2()](../../db/dc0/classautomotive__design_1_1curve__replica.html#a99c0a575edee4c403d2ca89bb0f0318f),
and
[config_control_design.curve_replica.wr2()](../../db/d4a/classconfig__control__design_1_1curve__replica.html#a3aed04b938581b9bb578d15e9c0d2b61).

## ◆ same_sense()

def automotive_design.composite_curve_segment.same_sense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve_segment._same_sense,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.face_surface._same_sense,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.edge_curve._same_sense,
automotive_design.composite_curve_segment._same_sense,
automotive_design.face_surface._same_sense,
automotive_design.edge_curve._same_sense,
config_control_design.composite_curve_segment._same_sense,
config_control_design.face_surface._same_sense, and
config_control_design.edge_curve._same_sense.

## ◆ transition()

def automotive_design.composite_curve_segment.transition  | ( | | ) |   
---|---|---|---|---  
  
References F_IntersectPoint._transition, FaceLineIntersector._transition,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve_segment._transition,
automotive_design.composite_curve_segment._transition,
config_control_design.composite_curve_segment._transition,
ifc2x3.ifccompositecurvesegment._transition, and
ifc4.ifccompositecurvesegment._transition.

Referenced by
[automotive_design.composite_curve.closed_curve()](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6b988086709b2d29b533fa3145010e1d),
[config_control_design.composite_curve.closed_curve()](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a606f93c957672f4e687eeb1e9b043943),
[ifc2x3.ifccompositecurve.closedcurve()](../../d5/d63/classifc2x3_1_1ifccompositecurve.html#abe11170956a9bdb9fb2f6b79755654f6),
and
[ifc4.ifccompositecurve.closedcurve()](../../d2/d3c/classifc4_1_1ifccompositecurve.html#aacdc4b96c7973938b35ac746950227bf).

## ◆ using_curves()

def automotive_design.composite_curve_segment.using_curves  | ( | | ) |   
---|---|---|---|---  
  
## ◆ wr1()

def automotive_design.composite_curve_segment.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.founded_item](../../d4/d12/classautomotive__design_1_1founded__item.html#a0668b2127d1c208daa93b2d435855a7f).

Reimplemented in
[automotive_design.reparametrised_composite_curve_segment](../../da/dcf/classautomotive__design_1_1reparametrised__composite__curve__segment.html#adcfb57154b0c2d04f5d91d6a6b659a25).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.curve_replica.parent_curve,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve_segment.parent_curve,
[automotive_design.curve_replica.parent_curve](../../db/dc0/classautomotive__design_1_1curve__replica.html#ad31f053094f57066f2ba82633323e1a2),
[automotive_design.composite_curve_segment.parent_curve](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#abebec68ca761166042d03848fd2a46cf),
[config_control_design.curve_replica.parent_curve](../../db/d4a/classconfig__control__design_1_1curve__replica.html#ac9b926bffa0a6f9128f06cf22ac161f7),
and
[config_control_design.composite_curve_segment.parent_curve](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#aca7f94a973184eb4c5f6a1bbfb78be15).

## Member Data Documentation

## ◆ parent_curve

automotive_design.composite_curve_segment.parent_curve  
---  
  
Referenced by
[automotive_design.composite_curve_segment.wr1()](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#a5631b696b5b2510fe9352894238be183),
[config_control_design.composite_curve_segment.wr1()](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#aa41973aa607ba41964959dcedb011dd7),
[automotive_design.curve_replica.wr2()](../../db/dc0/classautomotive__design_1_1curve__replica.html#a99c0a575edee4c403d2ca89bb0f0318f),
and
[config_control_design.curve_replica.wr2()](../../db/d4a/classconfig__control__design_1_1curve__replica.html#a3aed04b938581b9bb578d15e9c0d2b61).

## ◆ same_sense

automotive_design.composite_curve_segment.same_sense  
---  
  
## ◆ transition

automotive_design.composite_curve_segment.transition  
---  
  
Referenced by
[automotive_design.composite_curve.closed_curve()](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6b988086709b2d29b533fa3145010e1d),
[config_control_design.composite_curve.closed_curve()](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a606f93c957672f4e687eeb1e9b043943),
[ifc2x3.ifccompositecurve.closedcurve()](../../d5/d63/classifc2x3_1_1ifccompositecurve.html#abe11170956a9bdb9fb2f6b79755654f6),
and
[ifc4.ifccompositecurve.closedcurve()](../../d2/d3c/classifc4_1_1ifccompositecurve.html#aacdc4b96c7973938b35ac746950227bf).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

