---
url: https://freecad.github.io/SourceDoc/d8/d8c/classautomotive__design_1_1placement.html
scraped_at: 2025-09-08T15:09:29.088240
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [placement](../../d8/d8c/classautomotive__design_1_1placement.html)

[List of all members](../../d2/d28/classautomotive__design_1_1placement-members.html) | Public Member Functions | Public Attributes

automotive_design.placement Class Reference

##  Public Member Functions  
  
---  
def | [location](../../d8/d8c/classautomotive__design_1_1placement.html#ae557180edc9d5dd0ae9def8d6e23eb6d) ()  
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
[location](../../d8/d8c/classautomotive__design_1_1placement.html#aade15ec8d9163d4f50f6ebd55bf9e306)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity placement definition.
    
        :param location
        :type location:cartesian_point

## Member Function Documentation

## ◆ location()

def automotive_design.placement.location  | ( | | ) |   
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

automotive_design.placement.location  
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

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

