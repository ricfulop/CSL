---
url: https://freecad.github.io/SourceDoc/d9/d47/classautomotive__design_1_1box__domain.html
scraped_at: 2025-09-08T15:01:11.049657
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [box_domain](../../d9/d47/classautomotive__design_1_1box__domain.html)

[List of all members](../../d1/dc8/classautomotive__design_1_1box__domain-members.html) | Public Member Functions | Public Attributes

automotive_design.box_domain Class Reference

##  Public Member Functions  
  
---  
def | [corner](../../d9/d47/classautomotive__design_1_1box__domain.html#a4cbc33fc67dc9762c4995c225ff3aa52) ()  
def | [wr1](../../d9/d47/classautomotive__design_1_1box__domain.html#a8054d03e651707ab91c682852c2a57f3) (self)  
def | [xlength](../../d9/d47/classautomotive__design_1_1box__domain.html#af43ef09439543e68a96405ba858114b6) ()  
def | [ylength](../../d9/d47/classautomotive__design_1_1box__domain.html#ad7f468abe0a4dace6279b3ad6d89b882) ()  
def | [zlength](../../d9/d47/classautomotive__design_1_1box__domain.html#a8e20798de8fea69ca1d3952272a9164f) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.founded_item](../../d4/d12/classautomotive__design_1_1founded__item.html)  
def | [users](../../d4/d12/classautomotive__design_1_1founded__item.html#a0299c3fccdb8223cc8c9f590f7cee9a5) ()  
def | [wr1](../../d4/d12/classautomotive__design_1_1founded__item.html#a0668b2127d1c208daa93b2d435855a7f) (self)  
def | [wr2](../../d4/d12/classautomotive__design_1_1founded__item.html#a1ef4a4f4c94d46b616c25ec02609838f) (self)  
  
##  Public Attributes  
  
---  
|
[corner](../../d9/d47/classautomotive__design_1_1box__domain.html#a488aacdad818460c3a23b494bc26f71d)  
|
[xlength](../../d9/d47/classautomotive__design_1_1box__domain.html#a6a5c300220127b3c8fbbe178a616370d)  
|
[ylength](../../d9/d47/classautomotive__design_1_1box__domain.html#a86de94c210406740b6e5c41029fbff54)  
|
[zlength](../../d9/d47/classautomotive__design_1_1box__domain.html#a411b51b3a7e428d58e349fcee74385a4)  
  
## Detailed Description

    
    
    Entity box_domain definition.
    
        :param corner
        :type corner:cartesian_point
    
        :param xlength
        :type xlength:positive_length_measure
    
        :param ylength
        :type ylength:positive_length_measure
    
        :param zlength
        :type zlength:positive_length_measure

## Member Function Documentation

## ◆ corner()

def automotive_design.box_domain.corner  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.box_domain._corner,
automotive_design.box_domain._corner, ifc2x3.ifcboundingbox._corner, and
ifc4.ifcboundingbox._corner.

## ◆ wr1()

def automotive_design.box_domain.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.founded_item](../../d4/d12/classautomotive__design_1_1founded__item.html#a0668b2127d1c208daa93b2d435855a7f).

## ◆ xlength()

def automotive_design.box_domain.xlength  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.box_domain._xlength,
automotive_design.box_domain._xlength, ifc2x3.ifcrectangularpyramid._xlength,
ifc2x3.ifcblock._xlength, ifc4.ifcrectangularpyramid._xlength, and
ifc4.ifcblock._xlength.

Referenced by
[Mod.PartDesign.WizardShaft.ShaftDiagram.Diagram.update()](../../d9/d97/classMod_1_1PartDesign_1_1WizardShaft_1_1ShaftDiagram_1_1Diagram.html#a7dbcfc52379def311707bc63d73d8edc).

## ◆ ylength()

def automotive_design.box_domain.ylength  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.box_domain._ylength,
automotive_design.box_domain._ylength, ifc2x3.ifcrectangularpyramid._ylength,
ifc2x3.ifcblock._ylength, ifc4.ifcrectangularpyramid._ylength, and
ifc4.ifcblock._ylength.

## ◆ zlength()

def automotive_design.box_domain.zlength  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.box_domain._zlength,
automotive_design.box_domain._zlength, ifc2x3.ifcblock._zlength, and
ifc4.ifcblock._zlength.

## Member Data Documentation

## ◆ corner

automotive_design.box_domain.corner  
---  
  
## ◆ xlength

automotive_design.box_domain.xlength  
---  
  
Referenced by
[Mod.PartDesign.WizardShaft.ShaftDiagram.Diagram.update()](../../d9/d97/classMod_1_1PartDesign_1_1WizardShaft_1_1ShaftDiagram_1_1Diagram.html#a7dbcfc52379def311707bc63d73d8edc).

## ◆ ylength

automotive_design.box_domain.ylength  
---  
  
## ◆ zlength

automotive_design.box_domain.zlength  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

