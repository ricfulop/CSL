---
url: https://freecad.github.io/SourceDoc/d7/dfa/classconfig__control__design_1_1address.html
scraped_at: 2025-09-08T15:19:56.752044
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [address](../../d7/dfa/classconfig__control__design_1_1address.html)

[List of all members](../../d4/db2/classconfig__control__design_1_1address-members.html) | Public Member Functions | Public Attributes

config_control_design.address Class Reference

##  Public Member Functions  
  
---  
def | [country](../../d7/dfa/classconfig__control__design_1_1address.html#aac7cb7c9867d6b3f9cbec6c3900a06c2) ()  
def | [electronic_mail_address](../../d7/dfa/classconfig__control__design_1_1address.html#af07fb989832894305618d506564b1879) ()  
def | [facsimile_number](../../d7/dfa/classconfig__control__design_1_1address.html#a46b123c773fab5c6f21a97878b9daca3) ()  
def | [internal_location](../../d7/dfa/classconfig__control__design_1_1address.html#a6328dfbee9f426aa1df320997ae58972) ()  
def | [postal_box](../../d7/dfa/classconfig__control__design_1_1address.html#ab9d90d703cd51a9f040dce927bed0a72) ()  
def | [postal_code](../../d7/dfa/classconfig__control__design_1_1address.html#ad4d09de71b362702a6aaeb8eab82d915) ()  
def | [region](../../d7/dfa/classconfig__control__design_1_1address.html#af5510122b89ef76e3151c1928da8d36b) ()  
def | [street](../../d7/dfa/classconfig__control__design_1_1address.html#a71f29ab64ff1d3740bb768de02473ad0) ()  
def | [street_number](../../d7/dfa/classconfig__control__design_1_1address.html#a1140c8f4db7e033f5efc3d4d0b829076) ()  
def | [telephone_number](../../d7/dfa/classconfig__control__design_1_1address.html#aafa488ea7e8a092ad873abc6e2de77b4) ()  
def | [telex_number](../../d7/dfa/classconfig__control__design_1_1address.html#a0ccb6a982bc29254810a803ee4a02c14) ()  
def | [town](../../d7/dfa/classconfig__control__design_1_1address.html#ac91724aceff84c629f943552fc5a26e6) ()  
def | [wr1](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c) (self)  
  
##  Public Attributes  
  
---  
|
[country](../../d7/dfa/classconfig__control__design_1_1address.html#aa04fa8e75ca4631241c550d44a19f9cf)  
|
[electronic_mail_address](../../d7/dfa/classconfig__control__design_1_1address.html#ab3a8a996cad3a482ce40b22830390458)  
|
[facsimile_number](../../d7/dfa/classconfig__control__design_1_1address.html#a3b2377c5812cbb88463ad6d4a189c689)  
|
[internal_location](../../d7/dfa/classconfig__control__design_1_1address.html#afae63a182de9444d76bbc0af3252099a)  
|
[postal_box](../../d7/dfa/classconfig__control__design_1_1address.html#ada543d5f456f8a02a73be289a829f1ba)  
|
[postal_code](../../d7/dfa/classconfig__control__design_1_1address.html#a55613da735a32b947c044ff337c73540)  
|
[region](../../d7/dfa/classconfig__control__design_1_1address.html#afda5ab2fb21aa0f8598f5ec6a67f2999)  
|
[street](../../d7/dfa/classconfig__control__design_1_1address.html#ad8ba4a91c3d540a149374506347ddc88)  
|
[street_number](../../d7/dfa/classconfig__control__design_1_1address.html#a3269750bf56fc7577c76ff2e031179ae)  
|
[telephone_number](../../d7/dfa/classconfig__control__design_1_1address.html#a494e4574bfba75feb5796a795e918826)  
|
[telex_number](../../d7/dfa/classconfig__control__design_1_1address.html#a5a3983e39ac0d214bda27dbd670d37e6)  
|
[town](../../d7/dfa/classconfig__control__design_1_1address.html#aa8bd323b7158dd10ab4a03056be340ac)  
  
## Detailed Description

    
    
    Entity address definition.
    
        :param internal_location
        :type internal_location:label
    
        :param street_number
        :type street_number:label
    
        :param street
        :type street:label
    
        :param postal_box
        :type postal_box:label
    
        :param town
        :type town:label
    
        :param region
        :type region:label
    
        :param postal_code
        :type postal_code:label
    
        :param country
        :type country:label
    
        :param facsimile_number
        :type facsimile_number:label
    
        :param telephone_number
        :type telephone_number:label
    
        :param electronic_mail_address
        :type electronic_mail_address:label
    
        :param telex_number
        :type telex_number:label

## Member Function Documentation

## ◆ country()

def config_control_design.address.country  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._country,
automotive_design.address._country, config_control_design.address._country,
ifc2x3.ifcpostaladdress._country, and ifc4.ifcpostaladdress._country.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c),
[ifc2x3.ifcpostaladdress.wr1()](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#aa19dc28cf9a04c3746f8e9709a332b3b),
and
[ifc4.ifcpostaladdress.wr1()](../../de/df1/classifc4_1_1ifcpostaladdress.html#aad86cd00317181eff9997792161c796c).

## ◆ electronic_mail_address()

def config_control_design.address.electronic_mail_address  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._electronic_mail_address,
automotive_design.address._electronic_mail_address, and
config_control_design.address._electronic_mail_address.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ facsimile_number()

def config_control_design.address.facsimile_number  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._facsimile_number,
automotive_design.address._facsimile_number, and
config_control_design.address._facsimile_number.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ internal_location()

def config_control_design.address.internal_location  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._internal_location,
automotive_design.address._internal_location, and
config_control_design.address._internal_location.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ postal_box()

def config_control_design.address.postal_box  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._postal_box,
automotive_design.address._postal_box, and
config_control_design.address._postal_box.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ postal_code()

def config_control_design.address.postal_code  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._postal_code,
automotive_design.address._postal_code, and
config_control_design.address._postal_code.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ region()

def config_control_design.address.region  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._region,
automotive_design.address._region, config_control_design.address._region,
ifc2x3.ifcpostaladdress._region, and ifc4.ifcpostaladdress._region.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c),
[ifc2x3.ifcpostaladdress.wr1()](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#aa19dc28cf9a04c3746f8e9709a332b3b),
and
[ifc4.ifcpostaladdress.wr1()](../../de/df1/classifc4_1_1ifcpostaladdress.html#aad86cd00317181eff9997792161c796c).

## ◆ street()

def config_control_design.address.street  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._street,
automotive_design.address._street, and config_control_design.address._street.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ street_number()

def config_control_design.address.street_number  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._street_number,
automotive_design.address._street_number, and
config_control_design.address._street_number.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ telephone_number()

def config_control_design.address.telephone_number  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._telephone_number,
automotive_design.address._telephone_number, and
config_control_design.address._telephone_number.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ telex_number()

def config_control_design.address.telex_number  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._telex_number,
automotive_design.address._telex_number, and
config_control_design.address._telex_number.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ town()

def config_control_design.address.town  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._town,
automotive_design.address._town, config_control_design.address._town,
ifc2x3.ifcpostaladdress._town, and ifc4.ifcpostaladdress._town.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c),
[ifc2x3.ifcpostaladdress.wr1()](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#aa19dc28cf9a04c3746f8e9709a332b3b),
and
[ifc4.ifcpostaladdress.wr1()](../../de/df1/classifc4_1_1ifcpostaladdress.html#aad86cd00317181eff9997792161c796c).

## ◆ wr1()

def config_control_design.address.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.country,
[automotive_design.address.country](../../db/d9d/classautomotive__design_1_1address.html#ae7e3f48c7145e79339941f20ffab27fc),
[config_control_design.address.country](../../d7/dfa/classconfig__control__design_1_1address.html#aa04fa8e75ca4631241c550d44a19f9cf),
[ifc2x3.ifcpostaladdress.country](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#a1d004e0536ce0d6fee426f3e7373b453),
[ifc4.ifcpostaladdress.country](../../de/df1/classifc4_1_1ifcpostaladdress.html#aaaaeaa5f789d5afbc72937bf00b20e16),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.electronic_mail_address,
[automotive_design.address.electronic_mail_address](../../db/d9d/classautomotive__design_1_1address.html#a7af73287318b76292c652e3191c7e22b),
[config_control_design.address.electronic_mail_address](../../d7/dfa/classconfig__control__design_1_1address.html#ab3a8a996cad3a482ce40b22830390458),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.facsimile_number,
[automotive_design.address.facsimile_number](../../db/d9d/classautomotive__design_1_1address.html#aea7215bd7ca542b597ac2d2ead518860),
[config_control_design.address.facsimile_number](../../d7/dfa/classconfig__control__design_1_1address.html#a3b2377c5812cbb88463ad6d4a189c689),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.internal_location,
[automotive_design.address.internal_location](../../db/d9d/classautomotive__design_1_1address.html#a94536106ae5a55da0e83c37d38303963),
[config_control_design.address.internal_location](../../d7/dfa/classconfig__control__design_1_1address.html#afae63a182de9444d76bbc0af3252099a),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.postal_box,
[automotive_design.address.postal_box](../../db/d9d/classautomotive__design_1_1address.html#a134464f4d57b94c7967c09480165b862),
[config_control_design.address.postal_box](../../d7/dfa/classconfig__control__design_1_1address.html#ada543d5f456f8a02a73be289a829f1ba),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.postal_code,
[automotive_design.address.postal_code](../../db/d9d/classautomotive__design_1_1address.html#ad577393839cb3550c4137bd6c39297a4),
[config_control_design.address.postal_code](../../d7/dfa/classconfig__control__design_1_1address.html#a55613da735a32b947c044ff337c73540),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.region,
[automotive_design.address.region](../../db/d9d/classautomotive__design_1_1address.html#a045e31c25a805720ab7be29c6ffce34f),
[config_control_design.address.region](../../d7/dfa/classconfig__control__design_1_1address.html#afda5ab2fb21aa0f8598f5ec6a67f2999),
[ifc2x3.ifcpostaladdress.region](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#a2600eb54ed6218a66346f6ccfa391bcf),
[ifc4.ifcpostaladdress.region](../../de/df1/classifc4_1_1ifcpostaladdress.html#a9d64f483e1d914eeb29a57b5a78e6140),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.street,
[automotive_design.address.street](../../db/d9d/classautomotive__design_1_1address.html#aa934ad257f9faac9904a514ee0e4753f),
[config_control_design.address.street](../../d7/dfa/classconfig__control__design_1_1address.html#ad8ba4a91c3d540a149374506347ddc88),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.street_number,
[automotive_design.address.street_number](../../db/d9d/classautomotive__design_1_1address.html#a1aee6cde9c81ea21cdf1f439a7762f8f),
[config_control_design.address.street_number](../../d7/dfa/classconfig__control__design_1_1address.html#a3269750bf56fc7577c76ff2e031179ae),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.telephone_number,
[automotive_design.address.telephone_number](../../db/d9d/classautomotive__design_1_1address.html#a2e1b2dd8dd176dd74e78b79fa7b74757),
[config_control_design.address.telephone_number](../../d7/dfa/classconfig__control__design_1_1address.html#a494e4574bfba75feb5796a795e918826),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.telex_number,
[automotive_design.address.telex_number](../../db/d9d/classautomotive__design_1_1address.html#acbfcdaa1b5e5a0c8f918115a937f8809),
[config_control_design.address.telex_number](../../d7/dfa/classconfig__control__design_1_1address.html#a5a3983e39ac0d214bda27dbd670d37e6),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address.town,
[automotive_design.address.town](../../db/d9d/classautomotive__design_1_1address.html#adf52cf66e29d5acc4e232c3451063c8a),
[config_control_design.address.town](../../d7/dfa/classconfig__control__design_1_1address.html#aa8bd323b7158dd10ab4a03056be340ac),
[ifc2x3.ifcpostaladdress.town](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#aa0e0253c01d08f954229dca61fe7e1ad),
and
[ifc4.ifcpostaladdress.town](../../de/df1/classifc4_1_1ifcpostaladdress.html#a80331f9373d4de3b934b2deeaa930ee0).

## Member Data Documentation

## ◆ country

config_control_design.address.country  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c),
[ifc2x3.ifcpostaladdress.wr1()](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#aa19dc28cf9a04c3746f8e9709a332b3b),
and
[ifc4.ifcpostaladdress.wr1()](../../de/df1/classifc4_1_1ifcpostaladdress.html#aad86cd00317181eff9997792161c796c).

## ◆ electronic_mail_address

config_control_design.address.electronic_mail_address  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ facsimile_number

config_control_design.address.facsimile_number  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ internal_location

config_control_design.address.internal_location  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ postal_box

config_control_design.address.postal_box  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ postal_code

config_control_design.address.postal_code  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ region

config_control_design.address.region  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c),
[ifc2x3.ifcpostaladdress.wr1()](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#aa19dc28cf9a04c3746f8e9709a332b3b),
and
[ifc4.ifcpostaladdress.wr1()](../../de/df1/classifc4_1_1ifcpostaladdress.html#aad86cd00317181eff9997792161c796c).

## ◆ street

config_control_design.address.street  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ street_number

config_control_design.address.street_number  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ telephone_number

config_control_design.address.telephone_number  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ telex_number

config_control_design.address.telex_number  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ town

config_control_design.address.town  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c),
[ifc2x3.ifcpostaladdress.wr1()](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#aa19dc28cf9a04c3746f8e9709a332b3b),
and
[ifc4.ifcpostaladdress.wr1()](../../de/df1/classifc4_1_1ifcpostaladdress.html#aad86cd00317181eff9997792161c796c).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

