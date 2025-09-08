---
url: https://freecad.github.io/SourceDoc/d4/d4f/classautomotive__design_1_1kinematic__pair.html
scraped_at: 2025-09-08T15:07:03.485169
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [kinematic_pair](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html)

[List of all members](../../d4/db1/classautomotive__design_1_1kinematic__pair-members.html) | Public Member Functions | Public Attributes

automotive_design.kinematic_pair Class Reference

##  Public Member Functions  
  
---  
def | [joint](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a3cc1a3fa91c668bc412ae98a6bb71801) ()  
def | [pair_placement_in_first_link_context](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a4c2d01c20c5af49ab32473d657a4c064) ()  
def | [pair_placement_in_second_link_context](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a95c998e19e5ff9bcc07073444b9a551a) ()  
def | [wr1](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a5bf15e517acfe323d781527c74eb5100) (self)  
def | [wr2](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a3974063d988bfa776fba5cd5dac1c369) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.item_defined_transformation](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html)  
def | [description](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#aea7020e577c8aaa199bb53f3c4f76a19) ()  
def | [name](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a677249d4b240467fd9f1f5cc5279b24d) ()  
def | [transform_item_1](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#aeb7769f338ddfe3f332b6f71eeff0231) ()  
def | [transform_item_2](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a9cfdcfa5ee62b8db6be37ae3c542158d) ()  
  
##  Public Attributes  
  
---  
|
[joint](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a129569b8355d19cee7527672b69b6258)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.item_defined_transformation](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html)  
|
[description](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a9639e4a7f29564c744654086b0613457)  
|
[name](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a71cd4ea422a14c796ae2be07eef15da8)  
|
[transform_item_1](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a35a6126264cb2506a21004dbfc053ac0)  
|
[transform_item_2](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#ae1905883f0ed10110e83ec393fbda4a4)  
  
## Detailed Description

    
    
    Entity kinematic_pair definition.
    
        :param joint
        :type joint:kinematic_joint
    
        :param pair_placement_in_first_link_context
        :type pair_placement_in_first_link_context:rigid_placement
    
        :param pair_placement_in_second_link_context
        :type pair_placement_in_second_link_context:rigid_placement

## Member Function Documentation

## ◆ joint()

def automotive_design.kinematic_pair.joint  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.kinematic_pair._joint.

Referenced by
[automotive_design.kinematic_pair.wr1()](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a5bf15e517acfe323d781527c74eb5100),
and
[automotive_design.kinematic_pair.wr2()](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a3974063d988bfa776fba5cd5dac1c369).

## ◆ pair_placement_in_first_link_context()

def automotive_design.kinematic_pair.pair_placement_in_first_link_context  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.kinematic_pair.wr1()](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a5bf15e517acfe323d781527c74eb5100).

## ◆ pair_placement_in_second_link_context()

def automotive_design.kinematic_pair.pair_placement_in_second_link_context  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.kinematic_pair.wr2()](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a3974063d988bfa776fba5cd5dac1c369).

## ◆ wr1()

def automotive_design.kinematic_pair.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented in
[automotive_design.surface_pair](../../d3/d78/classautomotive__design_1_1surface__pair.html#a4e29aa1ef1ee68a84f0448f2535103e1),
[automotive_design.universal_pair](../../dc/d49/classautomotive__design_1_1universal__pair.html#a2c3a62561ec65a695390bc8967cd88c4),
[automotive_design.planar_curve_pair](../../d6/d44/classautomotive__design_1_1planar__curve__pair.html#a30b475400022bf9cd71a7a9f6e4ff452),
[automotive_design.point_on_planar_curve_pair](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html#acaf537b23b8ca4d04b0a3b8df4656a07),
[automotive_design.point_on_surface_pair](../../de/df2/classautomotive__design_1_1point__on__surface__pair.html#a7d512562d6ed849a3c08ebfb80437cab),
and
[automotive_design.homokinetic_pair](../../d1/d83/classautomotive__design_1_1homokinetic__pair.html#a65c538babd5c117d36ca2271cb411b3b).

References
[automotive_design.coordinated_pair_link_representation()](../../d4/ddf/namespaceautomotive__design.html#a83dd21787bf3ffa29a0b95fee9264690),
[automotive_design.kinematic_joint.first_link](../../d4/df3/classautomotive__design_1_1kinematic__joint.html#afce9a49b1b3605faa23c40914bec9131),
[automotive_design.kinematic_pair.joint](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a129569b8355d19cee7527672b69b6258),
KDL::Segment.joint, and
[automotive_design.kinematic_pair.pair_placement_in_first_link_context()](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a4c2d01c20c5af49ab32473d657a4c064).

## ◆ wr2()

def automotive_design.kinematic_pair.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented in
[automotive_design.surface_pair](../../d3/d78/classautomotive__design_1_1surface__pair.html#ac70a19c48959c1ce8a4b2423f45373fc),
and
[automotive_design.planar_curve_pair](../../d6/d44/classautomotive__design_1_1planar__curve__pair.html#afbefb73b873a6a7cd9ec72d3811a84f0).

References
[automotive_design.coordinated_pair_link_representation()](../../d4/ddf/namespaceautomotive__design.html#a83dd21787bf3ffa29a0b95fee9264690),
[automotive_design.kinematic_pair.joint](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a129569b8355d19cee7527672b69b6258),
KDL::Segment.joint,
[automotive_design.kinematic_pair.pair_placement_in_second_link_context()](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a95c998e19e5ff9bcc07073444b9a551a),
and
[automotive_design.kinematic_joint.second_link](../../d4/df3/classautomotive__design_1_1kinematic__joint.html#a9d34ff4effa83996e2031bc652c12d99).

## Member Data Documentation

## ◆ joint

automotive_design.kinematic_pair.joint  
---  
  
Referenced by
[automotive_design.kinematic_pair.wr1()](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a5bf15e517acfe323d781527c74eb5100),
and
[automotive_design.kinematic_pair.wr2()](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a3974063d988bfa776fba5cd5dac1c369).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

