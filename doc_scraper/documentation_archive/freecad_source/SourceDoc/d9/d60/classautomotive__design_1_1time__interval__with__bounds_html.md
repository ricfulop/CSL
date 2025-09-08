---
url: https://freecad.github.io/SourceDoc/d9/d60/classautomotive__design_1_1time__interval__with__bounds.html
scraped_at: 2025-09-08T15:14:35.384385
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [time_interval_with_bounds](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html)

[List of all members](../../d0/d69/classautomotive__design_1_1time__interval__with__bounds-members.html) | Public Member Functions | Public Attributes

automotive_design.time_interval_with_bounds Class Reference

##  Public Member Functions  
  
---  
def | [duration](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#ace4480b74d9dd540aed3337b36d751eb) ()  
def | [primary_bound](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a2a7e57cc406d66c1c980384b535d8959) ()  
def | [secondary_bound](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a1c627a41958bc611971dfcb96f83452d) ()  
def | [wr1](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a89932cc8870641129565a39b3c2de758) (self)  
def | [wr2](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a238586b0a0535fccfe5ed634ebfcd7ae) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.time_interval](../../d7/d5e/classautomotive__design_1_1time__interval.html)  
def | [description](../../d7/d5e/classautomotive__design_1_1time__interval.html#ad5bf780f2ad4ba0982834246de16ff5c) ()  
def | [id](../../d7/d5e/classautomotive__design_1_1time__interval.html#a616d553d1407a48cbc110ec428a95d84) ()  
def | [name](../../d7/d5e/classautomotive__design_1_1time__interval.html#a5d9f49c291b1e5cf2769c25b13be6d35) ()  
  
##  Public Attributes  
  
---  
|
[duration](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a35ac75d546de9015a11b97478728276d)  
|
[primary_bound](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a255492068df5abeb41d9cbf98aa4984c)  
|
[secondary_bound](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#aeff6b3c1fd2e43ce98bae287701b616b)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.time_interval](../../d7/d5e/classautomotive__design_1_1time__interval.html)  
|
[description](../../d7/d5e/classautomotive__design_1_1time__interval.html#a565b249f771a0a7dedaf624cdc055523)  
|
[id](../../d7/d5e/classautomotive__design_1_1time__interval.html#accafd9fb40c6f00c4a23371ae6d7c97e)  
|
[name](../../d7/d5e/classautomotive__design_1_1time__interval.html#a4953135eb1e188953e58990edc0a8d49)  
  
## Detailed Description

    
    
    Entity time_interval_with_bounds definition.
    
        :param primary_bound
        :type primary_bound:date_time_or_event_occurrence
    
        :param secondary_bound
        :type secondary_bound:date_time_or_event_occurrence
    
        :param duration
        :type duration:time_measure_with_unit

## Member Function Documentation

## ◆ duration()

def automotive_design.time_interval_with_bounds.duration  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.time_interval_with_bounds._duration,
automotive_design.time_interval_with_bounds._duration,
ifc2x3.ifcworkcontrol._duration, and ifc4.ifcworkcontrol._duration.

Referenced by
[automotive_design.time_interval_with_bounds.wr1()](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a89932cc8870641129565a39b3c2de758).

## ◆ primary_bound()

def automotive_design.time_interval_with_bounds.primary_bound  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.time_interval_with_bounds._primary_bound,
automotive_design.time_interval_with_bounds._primary_bound, and
[automotive_design.date_time_or_event_occurrence](../../d4/ddf/namespaceautomotive__design.html#ac6a3972ffef2a826aea2e97795c1ab97).

Referenced by
[automotive_design.time_interval_with_bounds.wr2()](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a238586b0a0535fccfe5ed634ebfcd7ae).

## ◆ secondary_bound()

def automotive_design.time_interval_with_bounds.secondary_bound  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.time_interval_with_bounds._secondary_bound,
automotive_design.time_interval_with_bounds._secondary_bound, and
[automotive_design.date_time_or_event_occurrence](../../d4/ddf/namespaceautomotive__design.html#ac6a3972ffef2a826aea2e97795c1ab97).

Referenced by
[automotive_design.time_interval_with_bounds.wr1()](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a89932cc8870641129565a39b3c2de758),
and
[automotive_design.time_interval_with_bounds.wr2()](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a238586b0a0535fccfe5ed634ebfcd7ae).

## ◆ wr1()

def automotive_design.time_interval_with_bounds.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.time_interval_with_bounds.duration,
[automotive_design.time_interval_with_bounds.duration](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a35ac75d546de9015a11b97478728276d),
[ifc2x3.ifcworkcontrol.duration](../../d0/de3/classifc2x3_1_1ifcworkcontrol.html#a6ab9f91812e928cf518e3573bfeb788b),
[ifc4.ifcworkcontrol.duration](../../d8/df6/classifc4_1_1ifcworkcontrol.html#ad545e523c2273e95a9ebf5f8146d9d99),
KDL::Trajectory_Composite.duration, KDL::Trajectory_Stationary.duration,
KDL::VelocityProfile_Trap.duration, KDL::VelocityProfile_TrapHalf.duration,
[RobotGui::TaskTrajectory.duration](../../d1/da4/classRobotGui_1_1TaskTrajectory.html#a3ed90051a09df7ddf44a2c7a1072fc72),
[RobotGui::TrajectorySimulate.duration](../../d6/d2d/classRobotGui_1_1TrajectorySimulate.html#a624a2f534fd28948e949936f6e09ca77),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.time_interval_with_bounds.secondary_bound,
and
[automotive_design.time_interval_with_bounds.secondary_bound](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#aeff6b3c1fd2e43ce98bae287701b616b).

## ◆ wr2()

def automotive_design.time_interval_with_bounds.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.time_interval_with_bounds.primary_bound,
[automotive_design.time_interval_with_bounds.primary_bound](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a255492068df5abeb41d9cbf98aa4984c),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.time_interval_with_bounds.secondary_bound,
and
[automotive_design.time_interval_with_bounds.secondary_bound](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#aeff6b3c1fd2e43ce98bae287701b616b).

## Member Data Documentation

## ◆ duration

automotive_design.time_interval_with_bounds.duration  
---  
  
Referenced by
[automotive_design.time_interval_with_bounds.wr1()](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a89932cc8870641129565a39b3c2de758).

## ◆ primary_bound

automotive_design.time_interval_with_bounds.primary_bound  
---  
  
Referenced by
[automotive_design.time_interval_with_bounds.wr2()](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a238586b0a0535fccfe5ed634ebfcd7ae).

## ◆ secondary_bound

automotive_design.time_interval_with_bounds.secondary_bound  
---  
  
Referenced by
[automotive_design.time_interval_with_bounds.wr1()](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a89932cc8870641129565a39b3c2de758),
and
[automotive_design.time_interval_with_bounds.wr2()](../../d9/d60/classautomotive__design_1_1time__interval__with__bounds.html#a238586b0a0535fccfe5ed634ebfcd7ae).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

