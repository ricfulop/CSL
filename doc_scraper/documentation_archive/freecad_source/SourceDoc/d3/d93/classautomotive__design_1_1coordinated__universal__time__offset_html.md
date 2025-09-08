---
url: https://freecad.github.io/SourceDoc/d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html
scraped_at: 2025-09-08T15:02:49.464740
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [coordinated_universal_time_offset](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html)

[List of all members](../../d5/db8/classautomotive__design_1_1coordinated__universal__time__offset-members.html) | Public Member Functions | Public Attributes

automotive_design.coordinated_universal_time_offset Class Reference

##  Public Member Functions  
  
---  
def | [actual_minute_offset](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#abd77f511b1793d973ecbd6f88f0500f5) ()  
def | [hour_offset](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a67c38463e8ffef9a76cbdc1e8a265e53) ()  
def | [minute_offset](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a87a4cd5789eddb88ae57fb56f658981c) ()  
def | [sense](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a97e9be3461042e4ab85c3337c837c609) ()  
def | [wr1](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#acb2b7950072fbe14dbde6c47a3eb493a) (self)  
def | [wr2](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a42bea66eeec8da312b94e14cd02de10b) (self)  
def | [wr3](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a28e045951b1fdbd124a5c1a9cb5c99bc) (self)  
  
##  Public Attributes  
  
---  
|
[hour_offset](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#aa90665b11eae293aebcc59aa70649b44)  
|
[minute_offset](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a210904167345b8ba3df37f925fb2f2df)  
|
[sense](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#adc38817a341d93053c4bcaf04d33943a)  
  
## Detailed Description

    
    
    Entity coordinated_universal_time_offset definition.
    
        :param hour_offset
        :type hour_offset:INTEGER
    
        :param minute_offset
        :type minute_offset:INTEGER
    
        :param sense
        :type sense:ahead_or_behind
    
        :param actual_minute_offset
        :type actual_minute_offset:INTEGER

## Member Function Documentation

## ◆ actual_minute_offset()

def automotive_design.coordinated_universal_time_offset.actual_minute_offset  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset.minute_offset,
[automotive_design.coordinated_universal_time_offset.minute_offset](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a210904167345b8ba3df37f925fb2f2df),
and
[config_control_design.coordinated_universal_time_offset.minute_offset](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html#aafcf4dc90d5d109173bad0bcb4d88cc6).

Referenced by
[automotive_design.coordinated_universal_time_offset.wr2()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a42bea66eeec8da312b94e14cd02de10b),
and
[automotive_design.coordinated_universal_time_offset.wr3()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a28e045951b1fdbd124a5c1a9cb5c99bc).

## ◆ hour_offset()

def automotive_design.coordinated_universal_time_offset.hour_offset  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset._hour_offset,
automotive_design.coordinated_universal_time_offset._hour_offset, and
config_control_design.coordinated_universal_time_offset._hour_offset.

Referenced by
[automotive_design.coordinated_universal_time_offset.wr1()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#acb2b7950072fbe14dbde6c47a3eb493a),
and
[automotive_design.coordinated_universal_time_offset.wr3()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a28e045951b1fdbd124a5c1a9cb5c99bc).

## ◆ minute_offset()

def automotive_design.coordinated_universal_time_offset.minute_offset  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset._minute_offset,
automotive_design.coordinated_universal_time_offset._minute_offset, and
config_control_design.coordinated_universal_time_offset._minute_offset.

Referenced by
[automotive_design.coordinated_universal_time_offset.actual_minute_offset()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#abd77f511b1793d973ecbd6f88f0500f5).

## ◆ sense()

def automotive_design.coordinated_universal_time_offset.sense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset._sense,
automotive_design.coordinated_universal_time_offset._sense,
config_control_design.coordinated_universal_time_offset._sense, and
ifc2x3.ifccoordinateduniversaltimeoffset._sense.

Referenced by
[automotive_design.coordinated_universal_time_offset.wr3()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a28e045951b1fdbd124a5c1a9cb5c99bc).

## ◆ wr1()

def automotive_design.coordinated_universal_time_offset.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset.hour_offset,
[automotive_design.coordinated_universal_time_offset.hour_offset](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#aa90665b11eae293aebcc59aa70649b44),
and
[config_control_design.coordinated_universal_time_offset.hour_offset](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html#ad85eca1ab6d9be63c3bbefd27df8bda5).

## ◆ wr2()

def automotive_design.coordinated_universal_time_offset.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset.actual_minute_offset(),
and
[automotive_design.coordinated_universal_time_offset.actual_minute_offset()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#abd77f511b1793d973ecbd6f88f0500f5).

## ◆ wr3()

def automotive_design.coordinated_universal_time_offset.wr3  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset.actual_minute_offset(),
[automotive_design.coordinated_universal_time_offset.actual_minute_offset()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#abd77f511b1793d973ecbd6f88f0500f5),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset.hour_offset,
[automotive_design.coordinated_universal_time_offset.hour_offset](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#aa90665b11eae293aebcc59aa70649b44),
[config_control_design.coordinated_universal_time_offset.hour_offset](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html#ad85eca1ab6d9be63c3bbefd27df8bda5),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset.sense,
[automotive_design.coordinated_universal_time_offset.sense](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#adc38817a341d93053c4bcaf04d33943a),
[config_control_design.coordinated_universal_time_offset.sense](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html#a5a5086c477e689886e95e97dc957302a),
and
[ifc2x3.ifccoordinateduniversaltimeoffset.sense](../../d4/dc4/classifc2x3_1_1ifccoordinateduniversaltimeoffset.html#a2e3b7f3492a95009b3a376ac6bb6315f).

## Member Data Documentation

## ◆ hour_offset

automotive_design.coordinated_universal_time_offset.hour_offset  
---  
  
Referenced by
[automotive_design.coordinated_universal_time_offset.wr1()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#acb2b7950072fbe14dbde6c47a3eb493a),
and
[automotive_design.coordinated_universal_time_offset.wr3()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a28e045951b1fdbd124a5c1a9cb5c99bc).

## ◆ minute_offset

automotive_design.coordinated_universal_time_offset.minute_offset  
---  
  
Referenced by
[automotive_design.coordinated_universal_time_offset.actual_minute_offset()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#abd77f511b1793d973ecbd6f88f0500f5).

## ◆ sense

automotive_design.coordinated_universal_time_offset.sense  
---  
  
Referenced by
[automotive_design.coordinated_universal_time_offset.wr3()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a28e045951b1fdbd124a5c1a9cb5c99bc).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

