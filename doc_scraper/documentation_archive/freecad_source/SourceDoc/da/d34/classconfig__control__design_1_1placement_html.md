---
url: https://freecad.github.io/SourceDoc/da/d34/classconfig__control__design_1_1placement.html
scraped_at: 2025-09-08T15:22:55.523506
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [placement](../../da/d34/classconfig__control__design_1_1placement.html)

[List of all members](../../dd/d82/classconfig__control__design_1_1placement-members.html) | Public Member Functions | Public Attributes

config_control_design.placement Class Reference

##  Public Member Functions  
  
---  
def | [location](../../da/d34/classconfig__control__design_1_1placement.html#adf77ece548901b24af889e0b83726763) ()  
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
[location](../../da/d34/classconfig__control__design_1_1placement.html#a82d8e902f6a2bbfa6de928032d40bd1d)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity placement definition.
    
        :param location
        :type location:cartesian_point

## Member Function Documentation

## ◆ location()

def config_control_design.placement.location  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.placement._location,
automotive_design.placement._location,
config_control_design.placement._location,
ifc2x3.ifcexternalreference._location, ifc2x3.ifcplacement._location,
ifc4.ifcexternalreference._location, ifc4.ifcplacement._location,
ifc4.ifcdocumentinformation._location, ifc4.ifcclassification._location, and
ifc4.ifclibraryinformation._location.

Referenced by
[draftguitools.gui_circulararray.CircularArray.Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
[draftguitools.gui_polararray.PolarArray.Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6),
[automotive_design.revolved_area_solid.axis_line()](../../d4/ded/classautomotive__design_1_1revolved__area__solid.html#ae7714359aef57b10dc9d110c4c95109c),
[automotive_design.surface_of_revolution.axis_line()](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#ac11430bfca20d807bd7fbb1de4555324),
[automotive_design.revolved_face_solid.axis_line()](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a88ba8cae1c9e693beda33bf96a0423ca),
[ifc2x3.ifcsurfaceofrevolution.axisline()](../../db/d1b/classifc2x3_1_1ifcsurfaceofrevolution.html#a0689126db6a08f9f1183f65515b53370),
[ifc2x3.ifcrevolvedareasolid.axisline()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#ad7a180e86495ea93d5acb25ffcc33ffa),
[ifc4.ifcsurfaceofrevolution.axisline()](../../d4/de7/classifc4_1_1ifcsurfaceofrevolution.html#adf527bd278ddce78734fc2b01bec7b37),
[ifc4.ifcrevolvedareasolid.axisline()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a45efcb80c8963331649e13f991ec7534),
[ifc4.ifcrevolvedareasolid.axisstartinxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a76b11dffac1f3f7f53c5dfeef5227626),
[draftguitools.gui_circulararray.CircularArray.completed()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#abc4dc219237d7614302cefbc9599ac50),
[draftguitools.gui_polararray.PolarArray.completed()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#adf72543f71963c7a5a4dee8db0ab1b00),
[ifc2x3.ifcplacement.dim()](../../dd/dfd/classifc2x3_1_1ifcplacement.html#ac4dbcef9f43207432d3fa6d838dbdfb7),
[ifc4.ifcplacement.dim()](../../d4/da3/classifc4_1_1ifcplacement.html#a4ff119d99b8ac53bebec7145128d0452),
[ifc2x3.ifcexternalreference.wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc4.ifcexternalreference.wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
and
[ifc2x3.ifcrevolvedareasolid.wr31()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a16ccd5dc8889fd10923e40182318836b).

## Member Data Documentation

## ◆ location

config_control_design.placement.location  
---  
  
Referenced by
[draftguitools.gui_circulararray.CircularArray.Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
[draftguitools.gui_polararray.PolarArray.Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6),
[automotive_design.revolved_area_solid.axis_line()](../../d4/ded/classautomotive__design_1_1revolved__area__solid.html#ae7714359aef57b10dc9d110c4c95109c),
[automotive_design.surface_of_revolution.axis_line()](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#ac11430bfca20d807bd7fbb1de4555324),
[automotive_design.revolved_face_solid.axis_line()](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a88ba8cae1c9e693beda33bf96a0423ca),
[ifc2x3.ifcsurfaceofrevolution.axisline()](../../db/d1b/classifc2x3_1_1ifcsurfaceofrevolution.html#a0689126db6a08f9f1183f65515b53370),
[ifc2x3.ifcrevolvedareasolid.axisline()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#ad7a180e86495ea93d5acb25ffcc33ffa),
[ifc4.ifcsurfaceofrevolution.axisline()](../../d4/de7/classifc4_1_1ifcsurfaceofrevolution.html#adf527bd278ddce78734fc2b01bec7b37),
[ifc4.ifcrevolvedareasolid.axisline()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a45efcb80c8963331649e13f991ec7534),
[ifc4.ifcrevolvedareasolid.axisstartinxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a76b11dffac1f3f7f53c5dfeef5227626),
[draftguitools.gui_circulararray.CircularArray.completed()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#abc4dc219237d7614302cefbc9599ac50),
[draftguitools.gui_polararray.PolarArray.completed()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#adf72543f71963c7a5a4dee8db0ab1b00),
[ifc2x3.ifcplacement.dim()](../../dd/dfd/classifc2x3_1_1ifcplacement.html#ac4dbcef9f43207432d3fa6d838dbdfb7),
[ifc4.ifcplacement.dim()](../../d4/da3/classifc4_1_1ifcplacement.html#a4ff119d99b8ac53bebec7145128d0452),
[ifc2x3.ifcexternalreference.wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc4.ifcexternalreference.wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
and
[ifc2x3.ifcrevolvedareasolid.wr31()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a16ccd5dc8889fd10923e40182318836b).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

