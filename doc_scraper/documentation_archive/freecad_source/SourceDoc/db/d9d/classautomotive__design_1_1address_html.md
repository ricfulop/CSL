---
url: https://freecad.github.io/SourceDoc/db/d9d/classautomotive__design_1_1address.html
scraped_at: 2025-09-08T14:59:18.617081
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [address](../../db/d9d/classautomotive__design_1_1address.html)

[List of all members](../../dd/d50/classautomotive__design_1_1address-members.html) | Public Member Functions | Public Attributes

automotive_design.address Class Reference

##  Public Member Functions  
  
---  
def | [country](../../db/d9d/classautomotive__design_1_1address.html#a51dfd232d518b481e4a1b3ea5d1202b2) ()  
def | [electronic_mail_address](../../db/d9d/classautomotive__design_1_1address.html#a36020c8ace96b051169eb354a09a865e) ()  
def | [facsimile_number](../../db/d9d/classautomotive__design_1_1address.html#a81daaffb6e6e91a3e723d14c1be2b868) ()  
def | [internal_location](../../db/d9d/classautomotive__design_1_1address.html#a436a5adb27358cbd214afd2322aabce0) ()  
def | [name](../../db/d9d/classautomotive__design_1_1address.html#a6d7b0ac5ccb98813fd50b4ffd4a669c2) ()  
def | [postal_box](../../db/d9d/classautomotive__design_1_1address.html#a87b6c3b511266377e0cee949e9b71e42) ()  
def | [postal_code](../../db/d9d/classautomotive__design_1_1address.html#a33db567a8fc6dbf2f807156df317d1af) ()  
def | [region](../../db/d9d/classautomotive__design_1_1address.html#a59d4c8a8289c1436bc5c12ea213e1939) ()  
def | [street](../../db/d9d/classautomotive__design_1_1address.html#a883337bdd44fa5504db93d378455fc37) ()  
def | [street_number](../../db/d9d/classautomotive__design_1_1address.html#a15a58637c77296c4f20e472ab66ca37a) ()  
def | [telephone_number](../../db/d9d/classautomotive__design_1_1address.html#ac35b610f676d3874073ba98a03207637) ()  
def | [telex_number](../../db/d9d/classautomotive__design_1_1address.html#a4336c55393514e8527457d7bb2a4f325) ()  
def | [town](../../db/d9d/classautomotive__design_1_1address.html#a53efa45bef6e758c7e79304b77638380) ()  
def | [url](../../db/d9d/classautomotive__design_1_1address.html#ac356597ac2c81b2f431a6dcb28d7bea0) ()  
def | [wr1](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f) (self)  
  
##  Public Attributes  
  
---  
|
[country](../../db/d9d/classautomotive__design_1_1address.html#ae7e3f48c7145e79339941f20ffab27fc)  
|
[electronic_mail_address](../../db/d9d/classautomotive__design_1_1address.html#a7af73287318b76292c652e3191c7e22b)  
|
[facsimile_number](../../db/d9d/classautomotive__design_1_1address.html#aea7215bd7ca542b597ac2d2ead518860)  
|
[internal_location](../../db/d9d/classautomotive__design_1_1address.html#a94536106ae5a55da0e83c37d38303963)  
|
[postal_box](../../db/d9d/classautomotive__design_1_1address.html#a134464f4d57b94c7967c09480165b862)  
|
[postal_code](../../db/d9d/classautomotive__design_1_1address.html#ad577393839cb3550c4137bd6c39297a4)  
|
[region](../../db/d9d/classautomotive__design_1_1address.html#a045e31c25a805720ab7be29c6ffce34f)  
|
[street](../../db/d9d/classautomotive__design_1_1address.html#aa934ad257f9faac9904a514ee0e4753f)  
|
[street_number](../../db/d9d/classautomotive__design_1_1address.html#a1aee6cde9c81ea21cdf1f439a7762f8f)  
|
[telephone_number](../../db/d9d/classautomotive__design_1_1address.html#a2e1b2dd8dd176dd74e78b79fa7b74757)  
|
[telex_number](../../db/d9d/classautomotive__design_1_1address.html#acbfcdaa1b5e5a0c8f918115a937f8809)  
|
[town](../../db/d9d/classautomotive__design_1_1address.html#adf52cf66e29d5acc4e232c3451063c8a)  
  
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
    
        :param name
        :type name:label
    
        :param url
        :type url:identifier

## Member Function Documentation

## ◆ country()

def automotive_design.address.country  | ( | | ) |   
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

def automotive_design.address.electronic_mail_address  | ( | | ) |   
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

def automotive_design.address.facsimile_number  | ( | | ) |   
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

def automotive_design.address.internal_location  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._internal_location,
automotive_design.address._internal_location, and
config_control_design.address._internal_location.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ name()

def automotive_design.address.name  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.get_name_value()](../../d4/ddf/namespaceautomotive__design.html#ae730b907f9032c797025ed6d3d4fb54e).

Referenced by
[draftguitools.gui_groups.Ui_AddNamedGroup.accept()](../../d3/df7/classdraftguitools_1_1gui__groups_1_1Ui__AddNamedGroup.html#a9ea5973817eab7d74792f5b109a01466),
[prototype.Node.addtofreecad()](../../d2/d62/classprototype_1_1Node.html#adc095cc5636da029d1e0d9cef8859701),
[Addon.Addon.disable()](../../d8/d91/classAddon_1_1Addon.html#ae714705a38afe9f13cd2b17580178b31),
[Addon.Addon.enable()](../../d8/d91/classAddon_1_1Addon.html#a79d327ec9a0b4e85e9e96cfad4003ed6),
[addonmanager_macro.Macro.filename()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a5de4e6a1f3c41dce24066111955cd706),
[gzip_utf8.GzipFile.filename()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ab56fe84a4eb08c44e7a0026280c01229),
[addonmanager_macro.Macro.fill_details_from_code()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a49b8d021a9b8255f8a490e880eb15489),
[addonmanager_macro.Macro.fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[Addon.Addon.get_cached_icon_filename()](../../d8/d91/classAddon_1_1Addon.html#a7b026027a2904028032edbe3e99e2cbd),
[ifc4.ifcapproval.hasidentifierorname()](../../df/d91/classifc4_1_1ifcapproval.html#a54f558ba3b17fad5fc6579e9d5f50947),
[addonmanager_macro.Macro.install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
[Addon.Addon.is_disabled()](../../d8/d91/classAddon_1_1Addon.html#a5752a95fcf0c51ed06f9841b381d3e50),
[femsolver.elmer.sifio.Section.keys()](../../db/dab/classfemsolver_1_1elmer_1_1sifio_1_1Section.html#ab5b099447f66f33743850697f0e20de4),
[automotive_design.si_unit.named_unit_dimensions()](../../d5/d77/classautomotive__design_1_1si__unit.html#a68eb7954eb09daa334bc8f2c2abbe5f9),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.output()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aeedd5f59969cc27432880d1916f3d7f9),
[prototype.Node.pprint()](../../d2/d62/classprototype_1_1Node.html#a5ae181c34e48238d2364b0ba4960c252),
[prototype.Node.pprint2()](../../d2/d62/classprototype_1_1Node.html#aaedcc4ba1fb305c7ddcc025235043cd5),
[PathScripts.PathSetupSheetGui.OpTaskPanel.propertyGroup()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a69cbbaadcb9cff7b526af2c743041d7b),
[PathScripts.PathSetupSheetGui.OpTaskPanel.propertyName()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#ad9bd0e0149d1bc42fc8e89a290de4910),
[PathScripts.PathJobGui.TaskPanel.reject()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a54fd97ba9b0060fa8fed8a43c360da0c),
[addonmanager_macro.Macro.remove()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ad13245288f8beb62d92cb458a2d2ce05),
[Addon.Addon.to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
[ifc2x3.ifcexternalreference.wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc2x3.ifcdocumentreference.wr1()](../../df/dd6/classifc2x3_1_1ifcdocumentreference.html#a7d5fdb1cb0dee567c44834b868c5cdad),
[ifc4.ifcexternalreference.wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
[ifc4.ifcdocumentreference.wr1()](../../d7/d2b/classifc4_1_1ifcdocumentreference.html#a8779d74c67e647441d1fb20c76f44f97),
and
[automotive_design.general_property_association.wr2()](../../d2/df3/classautomotive__design_1_1general__property__association.html#ae7f46462c59bc4e541a5d2511631eb65).

## ◆ postal_box()

def automotive_design.address.postal_box  | ( | | ) |   
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

def automotive_design.address.postal_code  | ( | | ) |   
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

def automotive_design.address.region  | ( | | ) |   
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

def automotive_design.address.street  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.address._street,
automotive_design.address._street, and config_control_design.address._street.

Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ street_number()

def automotive_design.address.street_number  | ( | | ) |   
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

def automotive_design.address.telephone_number  | ( | | ) |   
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

def automotive_design.address.telex_number  | ( | | ) |   
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

def automotive_design.address.town  | ( | | ) |   
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

## ◆ url()

def automotive_design.address.url  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.get_id_value()](../../d4/ddf/namespaceautomotive__design.html#aee48db7b5bbe921b6733fd6ae7daa212).

Referenced by
[addonmanager_macro.Macro.fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[Addon.Addon.set_metadata()](../../d8/d91/classAddon_1_1Addon.html#a799523f4861c30f1516a59602d5b77cd),
[Addon.Addon.to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
and
[Addon.Addon.verify_url_and_branch()](../../d8/d91/classAddon_1_1Addon.html#a920e70c1e01170868b69690eff7913e3).

## ◆ wr1()

def automotive_design.address.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented in
[automotive_design.person_and_organization_address](../../de/ddb/classautomotive__design_1_1person__and__organization__address.html#a3be65905034c6ba667650095d74bdb87).

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

automotive_design.address.country  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c),
[ifc2x3.ifcpostaladdress.wr1()](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#aa19dc28cf9a04c3746f8e9709a332b3b),
and
[ifc4.ifcpostaladdress.wr1()](../../de/df1/classifc4_1_1ifcpostaladdress.html#aad86cd00317181eff9997792161c796c).

## ◆ electronic_mail_address

automotive_design.address.electronic_mail_address  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ facsimile_number

automotive_design.address.facsimile_number  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ internal_location

automotive_design.address.internal_location  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ postal_box

automotive_design.address.postal_box  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ postal_code

automotive_design.address.postal_code  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ region

automotive_design.address.region  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c),
[ifc2x3.ifcpostaladdress.wr1()](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#aa19dc28cf9a04c3746f8e9709a332b3b),
and
[ifc4.ifcpostaladdress.wr1()](../../de/df1/classifc4_1_1ifcpostaladdress.html#aad86cd00317181eff9997792161c796c).

## ◆ street

automotive_design.address.street  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ street_number

automotive_design.address.street_number  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ telephone_number

automotive_design.address.telephone_number  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ telex_number

automotive_design.address.telex_number  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
and
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c).

## ◆ town

automotive_design.address.town  
---  
  
Referenced by
[automotive_design.address.wr1()](../../db/d9d/classautomotive__design_1_1address.html#af597aa69fcc605c7c3fc6a8a6af3d78f),
[config_control_design.address.wr1()](../../d7/dfa/classconfig__control__design_1_1address.html#ad9d8ec693479345ced584ada7f5ac05c),
[ifc2x3.ifcpostaladdress.wr1()](../../d6/d43/classifc2x3_1_1ifcpostaladdress.html#aa19dc28cf9a04c3746f8e9709a332b3b),
and
[ifc4.ifcpostaladdress.wr1()](../../de/df1/classifc4_1_1ifcpostaladdress.html#aad86cd00317181eff9997792161c796c).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

