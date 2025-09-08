---
url: https://freecad.github.io/SourceDoc/d9/d7c/classconfig__control__design_1_1composite__curve__segment.html
scraped_at: 2025-09-08T15:20:53.990994
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [composite_curve_segment](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html)

[List of all members](../../d4/d60/classconfig__control__design_1_1composite__curve__segment-members.html) | Public Member Functions | Public Attributes

config_control_design.composite_curve_segment Class Reference

##  Public Member Functions  
  
---  
def | [parent_curve](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#a9daf902a59c1d549ef629bf0d2bd7028) ()  
def | [same_sense](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#a89b88dd8e7be6ee2c367e16155a5edf8) ()  
def | [transition](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#a1c52bb765f7aaadeaa0189b0fab7dcdb) ()  
def | [using_curves](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#acd2e49d510e7d4b91dc6712e13ae72cd) ()  
def | [wr1](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#aa41973aa607ba41964959dcedb011dd7) (self)  
  
##  Public Attributes  
  
---  
|
[parent_curve](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#aca7f94a973184eb4c5f6a1bbfb78be15)  
|
[same_sense](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#a2378fe4779f884d4d878dbcc2486e799)  
|
[transition](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#a5d12b1a8ffee9975776721e3d43bcc12)  
  
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

def config_control_design.composite_curve_segment.parent_curve  | ( | | ) |   
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

def config_control_design.composite_curve_segment.same_sense  | ( | | ) |   
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

def config_control_design.composite_curve_segment.transition  | ( | | ) |   
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

def config_control_design.composite_curve_segment.using_curves  | ( | | ) |   
---|---|---|---|---  
  
## ◆ wr1()

def config_control_design.composite_curve_segment.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented in
[config_control_design.reparametrised_composite_curve_segment](../../df/d3a/classconfig__control__design_1_1reparametrised__composite__curve__segment.html#a3e9d3809f5ac7f706b664d8a957ad043).

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

config_control_design.composite_curve_segment.parent_curve  
---  
  
Referenced by
[automotive_design.composite_curve_segment.wr1()](../../d2/df7/classautomotive__design_1_1composite__curve__segment.html#a5631b696b5b2510fe9352894238be183),
[config_control_design.composite_curve_segment.wr1()](../../d9/d7c/classconfig__control__design_1_1composite__curve__segment.html#aa41973aa607ba41964959dcedb011dd7),
[automotive_design.curve_replica.wr2()](../../db/dc0/classautomotive__design_1_1curve__replica.html#a99c0a575edee4c403d2ca89bb0f0318f),
and
[config_control_design.curve_replica.wr2()](../../db/d4a/classconfig__control__design_1_1curve__replica.html#a3aed04b938581b9bb578d15e9c0d2b61).

## ◆ same_sense

config_control_design.composite_curve_segment.same_sense  
---  
  
## ◆ transition

config_control_design.composite_curve_segment.transition  
---  
  
Referenced by
[automotive_design.composite_curve.closed_curve()](../../de/d2c/classautomotive__design_1_1composite__curve.html#a6b988086709b2d29b533fa3145010e1d),
[config_control_design.composite_curve.closed_curve()](../../d9/d22/classconfig__control__design_1_1composite__curve.html#a606f93c957672f4e687eeb1e9b043943),
[ifc2x3.ifccompositecurve.closedcurve()](../../d5/d63/classifc2x3_1_1ifccompositecurve.html#abe11170956a9bdb9fb2f6b79755654f6),
and
[ifc4.ifccompositecurve.closedcurve()](../../d2/d3c/classifc4_1_1ifccompositecurve.html#aacdc4b96c7973938b35ac746950227bf).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

