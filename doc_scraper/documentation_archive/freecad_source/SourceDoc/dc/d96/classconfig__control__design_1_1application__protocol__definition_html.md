---
url: https://freecad.github.io/SourceDoc/dc/d96/classconfig__control__design_1_1application__protocol__definition.html
scraped_at: 2025-09-08T15:20:03.765150
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [application_protocol_definition](../../dc/d96/classconfig__control__design_1_1application__protocol__definition.html)

[List of all members](../../df/d59/classconfig__control__design_1_1application__protocol__definition-members.html) | Public Member Functions | Public Attributes

config_control_design.application_protocol_definition Class Reference

##  Public Member Functions  
  
---  
def | [application](../../dc/d96/classconfig__control__design_1_1application__protocol__definition.html#a6cca0837d089ff37d4f21c29424dc720) ()  
def | [application_interpreted_model_schema_name](../../dc/d96/classconfig__control__design_1_1application__protocol__definition.html#a50f9527d84f7e625d0bd2ff8c37c7e63) ()  
def | [application_protocol_year](../../dc/d96/classconfig__control__design_1_1application__protocol__definition.html#adcaffecaaf67c1eebac7174eeb1e5539) ()  
def | [status](../../dc/d96/classconfig__control__design_1_1application__protocol__definition.html#a9bcecac47cdebf87a2e7501506921f49) ()  
  
##  Public Attributes  
  
---  
|
[application](../../dc/d96/classconfig__control__design_1_1application__protocol__definition.html#a09aba98fcbcaef580bb30b564483020d)  
|
[application_interpreted_model_schema_name](../../dc/d96/classconfig__control__design_1_1application__protocol__definition.html#a734a8670f73511c6242ffeaaf59cc530)  
|
[application_protocol_year](../../dc/d96/classconfig__control__design_1_1application__protocol__definition.html#a6261937683743baeb6ec06660cb5a4b2)  
|
[status](../../dc/d96/classconfig__control__design_1_1application__protocol__definition.html#a067479ffa6b368621a280ba9936f98fe)  
  
## Detailed Description

    
    
    Entity application_protocol_definition definition.
    
        :param status
        :type status:label
    
        :param application_interpreted_model_schema_name
        :type application_interpreted_model_schema_name:label
    
        :param application_protocol_year
        :type application_protocol_year:year_number
    
        :param application
        :type application:application_context

## Member Function Documentation

## ◆ application()

def config_control_design.application_protocol_definition.application  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.application_context._application,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.application_protocol_definition._application,
automotive_design.application_context._application,
automotive_design.application_protocol_definition._application,
config_control_design.application_context._application, and
config_control_design.application_protocol_definition._application.

## ◆ application_interpreted_model_schema_name()

def config_control_design.application_protocol_definition.application_interpreted_model_schema_name  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.application_protocol_definition._application_interpreted_model_schema_name,
automotive_design.application_protocol_definition._application_interpreted_model_schema_name,
and
config_control_design.application_protocol_definition._application_interpreted_model_schema_name.

## ◆ application_protocol_year()

def config_control_design.application_protocol_definition.application_protocol_year  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.application_protocol_definition._application_protocol_year,
automotive_design.application_protocol_definition._application_protocol_year,
and
config_control_design.application_protocol_definition._application_protocol_year.

## ◆ status()

def config_control_design.application_protocol_definition.status  | ( | | ) |   
---|---|---|---|---  
  
References femsolver.task.Task._status,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.approval._status,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.action_status._status,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.application_protocol_definition._status,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.action_request_status._status,
automotive_design.approval._status, automotive_design.action_status._status,
automotive_design.application_protocol_definition._status,
automotive_design.action_request_status._status,
config_control_design.approval._status,
config_control_design.action_status._status,
config_control_design.application_protocol_definition._status,
config_control_design.action_request_status._status,
ifc2x3.ifcdocumentinformation._status, ifc2x3.ifctask._status,
ifc2x3.ifccostschedule._status, ifc2x3.ifcprojectorder._status,
ifc4.ifcdocumentinformation._status, ifc4.ifctask._status,
ifc4.ifcpermit._status, ifc4.ifcapproval._status,
ifc4.ifccostschedule._status, ifc4.ifcactionrequest._status, and
ifc4.ifcprojectorder._status.

Referenced by
[package_list.PackageListFilter.filterAcceptsRow()](../../d3/d7c/classpackage__list_1_1PackageListFilter.html#ac6c224ec61dac5c46121a0fc4cf1cb17),
and
[package_list.PackageListFilter.setStatusFilter()](../../d3/d7c/classpackage__list_1_1PackageListFilter.html#a22cd720e4853ae43b7d7f39758f2ff99).

## Member Data Documentation

## ◆ application

config_control_design.application_protocol_definition.application  
---  
  
## ◆ application_interpreted_model_schema_name

config_control_design.application_protocol_definition.application_interpreted_model_schema_name  
---  
  
## ◆ application_protocol_year

config_control_design.application_protocol_definition.application_protocol_year  
---  
  
## ◆ status

config_control_design.application_protocol_definition.status  
---  
  
Referenced by
[package_list.PackageListFilter.filterAcceptsRow()](../../d3/d7c/classpackage__list_1_1PackageListFilter.html#ac6c224ec61dac5c46121a0fc4cf1cb17),
and
[package_list.PackageListFilter.setStatusFilter()](../../d3/d7c/classpackage__list_1_1PackageListFilter.html#a22cd720e4853ae43b7d7f39758f2ff99).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

