---
url: https://freecad.github.io/SourceDoc/d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html
scraped_at: 2025-09-08T14:53:06.058444
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [GetMacroDetailsWorker](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html)

[List of all members](../../de/d4d/classaddonmanager__workers_1_1GetMacroDetailsWorker-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

addonmanager_workers.GetMacroDetailsWorker Class Reference

##  Public Member Functions  
  
---  
def | [run](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#ab8de4d0260c284fe15f46e977d4a85d8) (self)  
  
##  Public Attributes  
  
---  
|
[macro](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a5d39fe4e8febb3bf117f55964a9441c1)  
  
##  Static Public Attributes  
  
---  
|
[readme_updated](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a30aa4978c209057ce065f287ce00d6e5)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
|
[status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
  
## Detailed Description

    
    
    Retrieve the macro details for a macro

## Member Function Documentation

## ◆ run()

def addonmanager_workers.GetMacroDetailsWorker.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[Addon.Addon.macro](../../d8/d91/classAddon_1_1Addon.html#a1dedba275b5318b25c175b7f3294fb50),
[addonmanager_workers.GetMacroDetailsWorker.macro](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a5d39fe4e8febb3bf117f55964a9441c1),
[PathTests.TestPathPost.TestOutputNameSubstitution.macro](../../d0/d6e/classPathTests_1_1TestPathPost_1_1TestOutputNameSubstitution.html#a2e5493600afdbf28ffbe552e837fdbd5),
[addonmanager_workers.GetMacroDetailsWorker.readme_updated](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a30aa4978c209057ce065f287ce00d6e5),
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
and
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2).

Referenced by
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[femsolver.task.Task.protector()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a913c60a87594a8bfe76580d27effcb51).

## Member Data Documentation

## ◆ macro

addonmanager_workers.GetMacroDetailsWorker.macro  
---  
  
Referenced by
[addonmanager_workers.GetMacroDetailsWorker.run()](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#ab8de4d0260c284fe15f46e977d4a85d8).

## ◆ readme_updated

| addonmanager_workers.GetMacroDetailsWorker.readme_updated =
QtCore.Signal([str](../../d9/d36/classstr.html))  
---  
static  
  
Referenced by
[addonmanager_workers.GetMacroDetailsWorker.run()](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#ab8de4d0260c284fe15f46e977d4a85d8).

## ◆ status_message

| addonmanager_workers.GetMacroDetailsWorker.status_message =
QtCore.Signal([str](../../d9/d36/classstr.html))  
---  
static  
  
Referenced by
[addonmanager_workers.InstallWorkbenchWorker.finish_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aafea671f9554ba9e2f58208d011e1823),
[addonmanager_workers.UpdateMetadataCacheWorker.process_icon()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a5cf0fd0e4fa73b73a2c13988752593f0),
[addonmanager_workers.UpdateMetadataCacheWorker.process_metadata_txt()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a921a85ca0055b090e171a8a9d2b0d7a9),
[addonmanager_workers.UpdateMetadataCacheWorker.process_package_xml()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad05f76bd86f0e2ad319c5b65ec4ce242),
[addonmanager_workers.UpdateMetadataCacheWorker.process_requirements_txt()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a1f5b401874bff312cf4979ab5031ec74),
[addonmanager_workers.CacheMacroCode.run()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a337d9ec4228904f76fd1ed0b5e28944f),
[addonmanager_workers.GetMacroDetailsWorker.run()](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#ab8de4d0260c284fe15f46e977d4a85d8),
[addonmanager_workers.InstallWorkbenchWorker.run_git_clone()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a6a2d19b2a80037740caebe6a694ec544),
[addonmanager_workers.InstallWorkbenchWorker.run_git_update()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a2476b9e40d1e3c156e73fa57751343e8),
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631),
[addonmanager_workers.InstallWorkbenchWorker.update_status()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a1c775af73dfc50bd38f5d20b8f30fc60),
and
[addonmanager_workers.InstallWorkbenchWorker.update_zip_status()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab359ae038ce28b1712013e7d2800e7dc).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/addonmanager_workers.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

