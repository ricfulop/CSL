---
url: https://freecad.github.io/SourceDoc/db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html
scraped_at: 2025-09-08T15:21:09.051499
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [coordinated_universal_time_offset](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html)

[List of all members](../../d6/d83/classconfig__control__design_1_1coordinated__universal__time__offset-members.html) | Public Member Functions | Public Attributes

config_control_design.coordinated_universal_time_offset Class Reference

##  Public Member Functions  
  
---  
def | [hour_offset](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html#ac332f77da6d0f1bfc005967dbcf4c559) ()  
def | [minute_offset](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html#a9f702caf589ddfd7c2dfbd593725e654) ()  
def | [sense](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html#a9c1425f06d68b4b349f7e043a684cc9d) ()  
  
##  Public Attributes  
  
---  
|
[hour_offset](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html#ad85eca1ab6d9be63c3bbefd27df8bda5)  
|
[minute_offset](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html#aafcf4dc90d5d109173bad0bcb4d88cc6)  
|
[sense](../../db/d99/classconfig__control__design_1_1coordinated__universal__time__offset.html#a5a5086c477e689886e95e97dc957302a)  
  
## Detailed Description

    
    
    Entity coordinated_universal_time_offset definition.
    
        :param hour_offset
        :type hour_offset:hour_in_day
    
        :param minute_offset
        :type minute_offset:minute_in_hour
    
        :param sense
        :type sense:ahead_or_behind

## Member Function Documentation

## ◆ hour_offset()

def config_control_design.coordinated_universal_time_offset.hour_offset  | ( | | ) |   
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

def config_control_design.coordinated_universal_time_offset.minute_offset  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset._minute_offset,
automotive_design.coordinated_universal_time_offset._minute_offset, and
config_control_design.coordinated_universal_time_offset._minute_offset.

Referenced by
[automotive_design.coordinated_universal_time_offset.actual_minute_offset()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#abd77f511b1793d973ecbd6f88f0500f5).

## ◆ sense()

def config_control_design.coordinated_universal_time_offset.sense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.coordinated_universal_time_offset._sense,
automotive_design.coordinated_universal_time_offset._sense,
config_control_design.coordinated_universal_time_offset._sense, and
ifc2x3.ifccoordinateduniversaltimeoffset._sense.

Referenced by
[automotive_design.coordinated_universal_time_offset.wr3()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a28e045951b1fdbd124a5c1a9cb5c99bc).

## Member Data Documentation

## ◆ hour_offset

config_control_design.coordinated_universal_time_offset.hour_offset  
---  
  
Referenced by
[automotive_design.coordinated_universal_time_offset.wr1()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#acb2b7950072fbe14dbde6c47a3eb493a),
and
[automotive_design.coordinated_universal_time_offset.wr3()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a28e045951b1fdbd124a5c1a9cb5c99bc).

## ◆ minute_offset

config_control_design.coordinated_universal_time_offset.minute_offset  
---  
  
Referenced by
[automotive_design.coordinated_universal_time_offset.actual_minute_offset()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#abd77f511b1793d973ecbd6f88f0500f5).

## ◆ sense

config_control_design.coordinated_universal_time_offset.sense  
---  
  
Referenced by
[automotive_design.coordinated_universal_time_offset.wr3()](../../d3/d93/classautomotive__design_1_1coordinated__universal__time__offset.html#a28e045951b1fdbd124a5c1a9cb5c99bc).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

