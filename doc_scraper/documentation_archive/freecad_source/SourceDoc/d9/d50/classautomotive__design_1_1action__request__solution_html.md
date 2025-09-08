---
url: https://freecad.github.io/SourceDoc/d9/d50/classautomotive__design_1_1action__request__solution.html
scraped_at: 2025-09-08T14:59:12.554659
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [action_request_solution](../../d9/d50/classautomotive__design_1_1action__request__solution.html)

[List of all members](../../d3/d78/classautomotive__design_1_1action__request__solution-members.html) | Public Member Functions | Public Attributes

automotive_design.action_request_solution Class Reference

##  Public Member Functions  
  
---  
def | [description](../../d9/d50/classautomotive__design_1_1action__request__solution.html#a01d260284831f7aa9d9746e8e236f6ea) ()  
def | [method](../../d9/d50/classautomotive__design_1_1action__request__solution.html#afc2048af3cfd11b8b85212f6019bed10) ()  
def | [name](../../d9/d50/classautomotive__design_1_1action__request__solution.html#a9ca7bad2efe9f66f6b1649d2086ae230) ()  
def | [request](../../d9/d50/classautomotive__design_1_1action__request__solution.html#a73152db0ba9f354e8352034ef81f5119) ()  
def | [wr1](../../d9/d50/classautomotive__design_1_1action__request__solution.html#a46faf033ce231f87a914230a9d2de9a2) (self)  
def | [wr2](../../d9/d50/classautomotive__design_1_1action__request__solution.html#ab6e24dc8a33b5462cec002e5d06bfdb2) (self)  
  
##  Public Attributes  
  
---  
|
[method](../../d9/d50/classautomotive__design_1_1action__request__solution.html#a565686559a4b2864d5232b3980a9780b)  
|
[request](../../d9/d50/classautomotive__design_1_1action__request__solution.html#a33334a3e2df21b0c9aa89d1e58a388e5)  
  
## Detailed Description

    
    
    Entity action_request_solution definition.
    
        :param method
        :type method:action_method
    
        :param request
        :type request:versioned_action_request
    
        :param description
        :type description:text
    
        :param name
        :type name:label

## Member Function Documentation

## ◆ description()

def automotive_design.action_request_solution.description  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.get_description_value()](../../d4/ddf/namespaceautomotive__design.html#a7894d555e3f25a436366bbbf328b1bf2).

Referenced by
[Addon.Addon.set_metadata()](../../d8/d91/classAddon_1_1Addon.html#a799523f4861c30f1516a59602d5b77cd),
and
[Addon.Addon.to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5).

## ◆ method()

def automotive_design.action_request_solution.method  | ( | | ) |   
---|---|---|---|---  
  
References StdMeshers_ViscousLayers._method, VISCOUS_3D::AverageHyp._method,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.action_request_solution._method,
automotive_design.action_request_solution._method,
config_control_design.action_request_solution._method, and
zipios::ZipOutputStreambuf._method.

Referenced by
[PathScripts.PathDressupRampEntry.ObjectDressup.execute()](../../d4/d77/classPathScripts_1_1PathDressupRampEntry_1_1ObjectDressup.html#a6e5b12e06a02c6d2a2ec8116d7d751bd),
and
[PathScripts.PathDressupRampEntry.ObjectDressup.generateRamps()](../../d4/d77/classPathScripts_1_1PathDressupRampEntry_1_1ObjectDressup.html#a0f648732d60ede47ef6ed09e4ec10c42).

## ◆ name()

def automotive_design.action_request_solution.name  | ( | | ) |   
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

## ◆ request()

def automotive_design.action_request_solution.request  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.action_request_solution._request,
automotive_design.action_request_solution._request, and
config_control_design.action_request_solution._request.

## ◆ wr1()

def automotive_design.action_request_solution.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ wr2()

def automotive_design.action_request_solution.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ method

automotive_design.action_request_solution.method  
---  
  
Referenced by
[PathScripts.PathDressupRampEntry.ObjectDressup.execute()](../../d4/d77/classPathScripts_1_1PathDressupRampEntry_1_1ObjectDressup.html#a6e5b12e06a02c6d2a2ec8116d7d751bd),
and
[PathScripts.PathDressupRampEntry.ObjectDressup.generateRamps()](../../d4/d77/classPathScripts_1_1PathDressupRampEntry_1_1ObjectDressup.html#a0f648732d60ede47ef6ed09e4ec10c42).

## ◆ request

automotive_design.action_request_solution.request  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

