---
url: https://freecad.github.io/SourceDoc/db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html
scraped_at: 2025-09-08T14:53:05.063207
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [FillMacroListWorker](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html)

[List of all members](../../d3/d02/classaddonmanager__workers_1_1FillMacroListWorker-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

addonmanager_workers.FillMacroListWorker Class Reference

##  Public Member Functions  
  
---  
None | [remove_readonly](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#ae1c5e6e2ef2b52fa687320b20e1c240e) (self, func, path, _)  
def | [retrieve_macros_from_git](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a10ee78b1d84f50a0ca27e2887239ad32) (self)  
def | [retrieve_macros_from_wiki](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a3f024a71e79c2e9c92e240913af1b8b6) (self)  
def | [run](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a37584e9c645d33c8a5ccb38b253c8248) (self)  
  
##  Public Attributes  
  
---  
|
[current_thread](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a3c03c4fdebe15ddbc06bac93985d3e21)  
|
[repo_dir](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#ad2af3c0ecb704006f390067ff0e3920b)  
|
[repo_names](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#af4088ecbdaba24f8b41cb8b72cba43a3)  
  
##  Static Public Attributes  
  
---  
|
[add_macro_signal](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a524b70aca5a71a7a659d1d95ef3433f9)
= QtCore.Signal([object](../../dc/dd8/classobject.html))  
|
[progress_made](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#accd0dfdc2e30e5c92c6b604d7e7e439b)
= QtCore.Signal([int](../../d1/da0/classint.html),
[int](../../d1/da0/classint.html))  
|
[status_message_signal](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#aec6ae447a694fff4dd4fb1f4ee53aa35)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
  
## Detailed Description

    
    
    This worker populates the list of macros

## Member Function Documentation

## ◆ remove_readonly()

None addonmanager_workers.FillMacroListWorker.remove_readonly  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _func_ ,   
|  |  | _path_ ,   
|  |  | ___  
| ) | |   
      
    
    Remove a read-only file.

Referenced by
[AddonManager.CommandAddonManager.on_buttonUpdateCache_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa49366f509bb5b61e1d518f286f05adf),
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00),
and
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_git()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a10ee78b1d84f50a0ca27e2887239ad32).

## ◆ retrieve_macros_from_git()

def addonmanager_workers.FillMacroListWorker.retrieve_macros_from_git  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Retrieve macros from FreeCAD-macros.git
    
    Emits a signal for each macro in
    https://github.com/FreeCAD/FreeCAD-macros.git
    

References
[addonmanager_workers.LoadMacrosFromCacheWorker.add_macro_signal](../../d8/d75/classaddonmanager__workers_1_1LoadMacrosFromCacheWorker.html#a3767bf8f9a478915ca228bdb0460fb55),
[addonmanager_workers.FillMacroListWorker.add_macro_signal](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a524b70aca5a71a7a659d1d95ef3433f9),
[addonmanager_workers.UpdateWorker.current_thread](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a0c48da9f79a18d97f6d0deb9321fee11),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.current_thread](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#a28c730493adffabdbb3665082a7abfde),
[addonmanager_workers.FillMacroListWorker.current_thread](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a3c03c4fdebe15ddbc06bac93985d3e21),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.progress_made](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#aec3c2db73953f95de347889b8c3092cf),
[addonmanager_workers.FillMacroListWorker.progress_made](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#accd0dfdc2e30e5c92c6b604d7e7e439b),
[addonmanager_workers.CacheMacroCode.progress_made](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ac2ea5cd107221a9b413ffc96e2f3509f),
[addonmanager_workers.InstallWorkbenchWorker.progress_made](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a3eff4b2ef9e78c42b0b775d28346f569),
[addonmanager_workers.UpdateMetadataCacheWorker.progress_made](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ae662a656eac3bde23e8556a47ce15a97),
[addonmanager_workers.UpdateAllWorker.progress_made](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a76399853f70e57e05c11e12ea5ab474e),
[NetworkManager.NetworkManager.progress_made](../../d6/d8c/classNetworkManager_1_1NetworkManager.html#ac48cb7d6c22c7c510ef9eaf2e6918aea),
[AddonManager.CommandAddonManager.remove_readonly()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7fa7eb4d9cf67befc603bb70735c4329),
[addonmanager_workers.FillMacroListWorker.remove_readonly()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#ae1c5e6e2ef2b52fa687320b20e1c240e),
[addonmanager_workers.FillMacroListWorker.repo_dir](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#ad2af3c0ecb704006f390067ff0e3920b),
and
[addonmanager_workers.FillMacroListWorker.status_message_signal](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#aec6ae447a694fff4dd4fb1f4ee53aa35).

## ◆ retrieve_macros_from_wiki()

def addonmanager_workers.FillMacroListWorker.retrieve_macros_from_wiki  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Retrieve macros from the wiki
    
    Read the wiki and emit a signal for each found macro.
    Reads only the page https://wiki.freecad.org/Macros_recipes
    

References
[addonmanager_workers.LoadMacrosFromCacheWorker.add_macro_signal](../../d8/d75/classaddonmanager__workers_1_1LoadMacrosFromCacheWorker.html#a3767bf8f9a478915ca228bdb0460fb55),
[addonmanager_workers.FillMacroListWorker.add_macro_signal](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a524b70aca5a71a7a659d1d95ef3433f9),
[addonmanager_workers.UpdateWorker.current_thread](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a0c48da9f79a18d97f6d0deb9321fee11),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.current_thread](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#a28c730493adffabdbb3665082a7abfde),
[addonmanager_workers.FillMacroListWorker.current_thread](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a3c03c4fdebe15ddbc06bac93985d3e21),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.progress_made](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#aec3c2db73953f95de347889b8c3092cf),
[addonmanager_workers.FillMacroListWorker.progress_made](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#accd0dfdc2e30e5c92c6b604d7e7e439b),
[addonmanager_workers.CacheMacroCode.progress_made](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ac2ea5cd107221a9b413ffc96e2f3509f),
[addonmanager_workers.InstallWorkbenchWorker.progress_made](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a3eff4b2ef9e78c42b0b775d28346f569),
[addonmanager_workers.UpdateMetadataCacheWorker.progress_made](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ae662a656eac3bde23e8556a47ce15a97),
[addonmanager_workers.UpdateAllWorker.progress_made](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a76399853f70e57e05c11e12ea5ab474e),
and
[NetworkManager.NetworkManager.progress_made](../../d6/d8c/classNetworkManager_1_1NetworkManager.html#ac48cb7d6c22c7c510ef9eaf2e6918aea).

## ◆ run()

def addonmanager_workers.FillMacroListWorker.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Populates the list of macros

Referenced by
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[femsolver.task.Task.protector()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a913c60a87594a8bfe76580d27effcb51).

## Member Data Documentation

## ◆ add_macro_signal

| addonmanager_workers.FillMacroListWorker.add_macro_signal =
QtCore.Signal([object](../../dc/dd8/classobject.html))  
---  
static  
  
Referenced by
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_git()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a10ee78b1d84f50a0ca27e2887239ad32),
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_wiki()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a3f024a71e79c2e9c92e240913af1b8b6),
and
[addonmanager_workers.LoadMacrosFromCacheWorker.run()](../../d8/d75/classaddonmanager__workers_1_1LoadMacrosFromCacheWorker.html#a0a44e06ac71aa472cc7f3024fe634c6e).

## ◆ current_thread

addonmanager_workers.FillMacroListWorker.current_thread  
---  
  
Referenced by
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_git()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a10ee78b1d84f50a0ca27e2887239ad32),
and
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_wiki()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a3f024a71e79c2e9c92e240913af1b8b6).

## ◆ progress_made

| addonmanager_workers.FillMacroListWorker.progress_made =
QtCore.Signal([int](../../d1/da0/classint.html),
[int](../../d1/da0/classint.html))  
---  
static  
  
Referenced by
[NetworkManager.NetworkManager.abort()](../../d6/d8c/classNetworkManager_1_1NetworkManager.html#ab50a39b6dcc08d9cadc732fc3ca89431),
[addonmanager_workers.UpdateMetadataCacheWorker.download_completed()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad08f2e5d64217721f3eca79acb8675da),
[addonmanager_workers.UpdateAllWorker.on_failure()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#abc670e23e0e537749e6290fd93788700),
[addonmanager_workers.UpdateAllWorker.on_success()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a1e4ac86d73584f134a64abdbbca782b5),
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_git()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a10ee78b1d84f50a0ca27e2887239ad32),
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_wiki()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a3f024a71e79c2e9c92e240913af1b8b6),
[addonmanager_workers.UpdateAllWorker.run()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a04587fd788c227b0731b334b2fdd1151),
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631),
[addonmanager_workers.InstallWorkbenchWorker.update_status()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a1c775af73dfc50bd38f5d20b8f30fc60),
and
[addonmanager_workers.InstallWorkbenchWorker.update_zip_status()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab359ae038ce28b1712013e7d2800e7dc).

## ◆ repo_dir

addonmanager_workers.FillMacroListWorker.repo_dir  
---  
  
Referenced by
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_git()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a10ee78b1d84f50a0ca27e2887239ad32).

## ◆ repo_names

addonmanager_workers.FillMacroListWorker.repo_names  
---  
  
## ◆ status_message_signal

| addonmanager_workers.FillMacroListWorker.status_message_signal =
QtCore.Signal([str](../../d9/d36/classstr.html))  
---  
static  
  
Referenced by
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_git()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a10ee78b1d84f50a0ca27e2887239ad32).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/addonmanager_workers.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

