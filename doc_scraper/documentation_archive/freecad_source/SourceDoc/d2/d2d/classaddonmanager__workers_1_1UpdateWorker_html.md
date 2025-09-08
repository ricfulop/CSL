---
url: https://freecad.github.io/SourceDoc/d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html
scraped_at: 2025-09-08T14:53:16.113889
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [UpdateWorker](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html)

[List of all members](../../d7/df3/classaddonmanager__workers_1_1UpdateWorker-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

addonmanager_workers.UpdateWorker Class Reference

##  Public Member Functions  
  
---  
def | [run](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a846779872d87246408c0197a12d6e5c9) (self)  
  
##  Public Attributes  
  
---  
|
[current_thread](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a0c48da9f79a18d97f6d0deb9321fee11)  
  
##  Static Public Attributes  
  
---  
|
[addon_repo](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#aae70d6db7bb370536c65dbe841ef2f7d)
= QtCore.Signal([object](../../dc/dd8/classobject.html))  
|
[status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
  
## Detailed Description

    
    
    This worker updates the list of available workbenches

## Member Function Documentation

## ◆ run()

def addonmanager_workers.UpdateWorker.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[femsolver.task.Task.protector()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a913c60a87594a8bfe76580d27effcb51).

## Member Data Documentation

## ◆ addon_repo

| addonmanager_workers.UpdateWorker.addon_repo =
QtCore.Signal([object](../../dc/dd8/classobject.html))  
---  
static  
  
Referenced by
[addonmanager_workers.LoadPackagesFromCacheWorker.run()](../../d2/d8e/classaddonmanager__workers_1_1LoadPackagesFromCacheWorker.html#aa6200a9f877fc435439aa5d9c18e63e6).

## ◆ current_thread

addonmanager_workers.UpdateWorker.current_thread  
---  
  
Referenced by
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_git()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a10ee78b1d84f50a0ca27e2887239ad32),
and
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_wiki()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a3f024a71e79c2e9c92e240913af1b8b6).

## ◆ status_message

| addonmanager_workers.UpdateWorker.status_message =
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

