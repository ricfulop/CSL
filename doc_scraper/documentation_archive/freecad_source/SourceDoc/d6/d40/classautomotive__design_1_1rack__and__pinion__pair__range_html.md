---
url: https://freecad.github.io/SourceDoc/d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html
scraped_at: 2025-09-08T15:11:24.572644
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [rack_and_pinion_pair_range](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html)

[List of all members](../../de/d68/classautomotive__design_1_1rack__and__pinion__pair__range-members.html) | Public Member Functions | Public Attributes

automotive_design.rack_and_pinion_pair_range Class Reference

##  Public Member Functions  
  
---  
def | [lower_limit_rack_displacement](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#a53cf2cc4ff88c513a52396efb73c3d53) ()  
def | [simple_pair_range_applies_to_pair](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#a14b603630aeea935323ea0eabb552718) ()  
def | [upper_limit_rack_displacement](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#a4df0e31a58133136b85b4c2fe179c869) ()  
def | [wr1](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#ae74770e5b75011a141f1094a29e1dd04) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
def | [applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a34d466ba4abfc972eddb7542a66e3865) ()  
  
##  Public Attributes  
  
---  
|
[lower_limit_rack_displacement](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#a0b726a6fe85fa0803b88314e6f3be820)  
|
[simple_pair_range_applies_to_pair](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#abe75f91b7cfeb147c800021786808c8d)  
|
[upper_limit_rack_displacement](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#adc0794c4c61351243a9915f3072d5ecb)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
|
[applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a482e1ee88d0745baefe27406e3b45d03)  
  
## Detailed Description

    
    
    Entity rack_and_pinion_pair_range definition.
    
        :param simple_pair_range_applies_to_pair
        :type simple_pair_range_applies_to_pair:rack_and_pinion_pair
    
        :param lower_limit_rack_displacement
        :type lower_limit_rack_displacement:translational_range_measure
    
        :param upper_limit_rack_displacement
        :type upper_limit_rack_displacement:translational_range_measure

## Member Function Documentation

## ◆ lower_limit_rack_displacement()

def automotive_design.rack_and_pinion_pair_range.lower_limit_rack_displacement  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.rack_and_pinion_pair_range._lower_limit_rack_displacement,
and
[automotive_design.translational_range_measure](../../d4/ddf/namespaceautomotive__design.html#a8c20f8bd88dcd73e869e38b254a3f173).

Referenced by
[automotive_design.rack_and_pinion_pair_range.wr1()](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#ae74770e5b75011a141f1094a29e1dd04).

## ◆ simple_pair_range_applies_to_pair()

def automotive_design.rack_and_pinion_pair_range.simple_pair_range_applies_to_pair  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.planar_curve_pair_range._simple_pair_range_applies_to_pair,
automotive_design.point_on_planar_curve_pair_range._simple_pair_range_applies_to_pair,
automotive_design.planar_pair_range._simple_pair_range_applies_to_pair,
automotive_design.cylindrical_pair_range._simple_pair_range_applies_to_pair,
automotive_design.universal_pair_range._simple_pair_range_applies_to_pair,
automotive_design.spherical_pair_range._simple_pair_range_applies_to_pair,
automotive_design.gear_pair_range._simple_pair_range_applies_to_pair,
automotive_design.screw_pair_range._simple_pair_range_applies_to_pair,
automotive_design.surface_pair_range._simple_pair_range_applies_to_pair,
automotive_design.rack_and_pinion_pair_range._simple_pair_range_applies_to_pair,
automotive_design.point_on_surface_pair_range._simple_pair_range_applies_to_pair,
automotive_design.prismatic_pair_range._simple_pair_range_applies_to_pair, and
automotive_design.revolute_pair_range._simple_pair_range_applies_to_pair.

## ◆ upper_limit_rack_displacement()

def automotive_design.rack_and_pinion_pair_range.upper_limit_rack_displacement  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.rack_and_pinion_pair_range._upper_limit_rack_displacement,
and
[automotive_design.translational_range_measure](../../d4/ddf/namespaceautomotive__design.html#a8c20f8bd88dcd73e869e38b254a3f173).

Referenced by
[automotive_design.rack_and_pinion_pair_range.wr1()](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#ae74770e5b75011a141f1094a29e1dd04).

## ◆ wr1()

def automotive_design.rack_and_pinion_pair_range.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.rack_and_pinion_pair_range.lower_limit_rack_displacement](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#a0b726a6fe85fa0803b88314e6f3be820),
and
[automotive_design.rack_and_pinion_pair_range.upper_limit_rack_displacement](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#adc0794c4c61351243a9915f3072d5ecb).

## Member Data Documentation

## ◆ lower_limit_rack_displacement

automotive_design.rack_and_pinion_pair_range.lower_limit_rack_displacement  
---  
  
Referenced by
[automotive_design.rack_and_pinion_pair_range.wr1()](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#ae74770e5b75011a141f1094a29e1dd04).

## ◆ simple_pair_range_applies_to_pair

automotive_design.rack_and_pinion_pair_range.simple_pair_range_applies_to_pair  
---  
  
## ◆ upper_limit_rack_displacement

automotive_design.rack_and_pinion_pair_range.upper_limit_rack_displacement  
---  
  
Referenced by
[automotive_design.rack_and_pinion_pair_range.wr1()](../../d6/d40/classautomotive__design_1_1rack__and__pinion__pair__range.html#ae74770e5b75011a141f1094a29e1dd04).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

