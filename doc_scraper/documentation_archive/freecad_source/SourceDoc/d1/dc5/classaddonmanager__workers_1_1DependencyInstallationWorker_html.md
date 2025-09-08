---
url: https://freecad.github.io/SourceDoc/d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html
scraped_at: 2025-09-08T14:53:04.053099
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [DependencyInstallationWorker](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html)

[List of all members](../../dc/d2f/classaddonmanager__workers_1_1DependencyInstallationWorker-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

addonmanager_workers.DependencyInstallationWorker Class Reference

##  Public Member Functions  
  
---  
def | [run](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a1a9736210fa3ae7feb0c78df6452e181) (self)  
  
##  Public Attributes  
  
---  
|
[addons](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a3c24ea545d20f56218c3119038b1771e)  
|
[python_optional](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#aee4943c0634b574fcc9a5fdcc0eaabe4)  
|
[python_required](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a351c4935c34b14ca2a2c6486c8003230)  
  
##  Static Public Attributes  
  
---  
|
[failure](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a7bfb1ce653996a5c031a43b8f7cd8bab)
= QtCore.Signal([str](../../d9/d36/classstr.html),
[str](../../d9/d36/classstr.html))  
|
[no_pip](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a856f72ae6da54853fdd98818a8ca8f0c)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
|
[no_python_exe](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#ab6741f0505e5e9e78c92cbae73b46365)
= QtCore.Signal()  
|
[success](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a8c699c9f999374f975896557ed333ca7)
= QtCore.Signal()  
  
## Detailed Description

    
    
    Install dependencies using Addonmanager for FreeCAD, and pip for python

## Member Function Documentation

## ◆ run()

def addonmanager_workers.DependencyInstallationWorker.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[addonmanager_workers.DependencyInstallationWorker.addons](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a3c24ea545d20f56218c3119038b1771e),
[addonmanager_workers.ConnectionChecker.failure](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a3e0c50e69224c95190023c513848c624),
[addonmanager_workers.InstallWorkbenchWorker.failure](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aebef215dec1817e92522a99df709ac87),
[addonmanager_workers.DependencyInstallationWorker.failure](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a7bfb1ce653996a5c031a43b8f7cd8bab),
[addonmanager_workers.UpdateAllWorker.failure](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a2ebc0aac3ef88b4614fdbedc4e718214),
[addonmanager_workers.UpdateSingleWorker.failure](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a4eaf21e72f40cac969a348224d5a6a2c),
[AddonManager.CommandAddonManager.no_pip()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abe9fbe57e535559f53434676040a0f80),
[addonmanager_workers.DependencyInstallationWorker.no_pip](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a856f72ae6da54853fdd98818a8ca8f0c),
[AddonManager.CommandAddonManager.no_python_exe()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a02ecc07f773ae69b309435ae5df313f7),
[addonmanager_workers.DependencyInstallationWorker.no_python_exe](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#ab6741f0505e5e9e78c92cbae73b46365),
[AddonManager.CommandAddonManager.MissingDependencies.python_optional](../../d8/dca/classAddonManager_1_1CommandAddonManager_1_1MissingDependencies.html#a52f9cb9122c2aa0d09d652812ad01760),
[addonmanager_workers.DependencyInstallationWorker.python_optional](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#aee4943c0634b574fcc9a5fdcc0eaabe4),
[AddonManager.CommandAddonManager.MissingDependencies.python_required](../../d8/dca/classAddonManager_1_1CommandAddonManager_1_1MissingDependencies.html#a70ab57966406441198c4531b5efc625e),
[addonmanager_workers.DependencyInstallationWorker.python_required](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a351c4935c34b14ca2a2c6486c8003230),
[addonmanager_workers.ConnectionChecker.success](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a14cf02183ee0ebb0c9b4f2b53d2313fe),
[addonmanager_workers.InstallWorkbenchWorker.success](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a65247f58b9c0d2bb122759dc36c9ce14),
[addonmanager_workers.DependencyInstallationWorker.success](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a8c699c9f999374f975896557ed333ca7),
[addonmanager_workers.UpdateAllWorker.success](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#aaa4d285f7e85eca8099f9d62f6dbbd68),
and
[addonmanager_workers.UpdateSingleWorker.success](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a9c2bdb48945f6866bb4072e0f06257a9).

Referenced by
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[femsolver.task.Task.protector()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a913c60a87594a8bfe76580d27effcb51).

## Member Data Documentation

## ◆ addons

addonmanager_workers.DependencyInstallationWorker.addons  
---  
  
Referenced by
[addonmanager_workers.DependencyInstallationWorker.run()](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a1a9736210fa3ae7feb0c78df6452e181).

## ◆ failure

| addonmanager_workers.DependencyInstallationWorker.failure =
QtCore.Signal([str](../../d9/d36/classstr.html),
[str](../../d9/d36/classstr.html))  
---  
static  
  
Referenced by
[addonmanager_workers.InstallWorkbenchWorker.finish_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aafea671f9554ba9e2f58208d011e1823),
[addonmanager_workers.InstallWorkbenchWorker.launch_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adfe4a53563dc3d0679c1c4b55c105e23),
[addonmanager_workers.UpdateAllWorker.on_failure()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#abc670e23e0e537749e6290fd93788700),
[addonmanager_workers.ConnectionChecker.run()](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a42bb05d34618cdb7f2547f1dd59f7821),
[addonmanager_workers.DependencyInstallationWorker.run()](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a1a9736210fa3ae7feb0c78df6452e181),
[addonmanager_workers.InstallWorkbenchWorker.run_git_update()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a2476b9e40d1e3c156e73fa57751343e8),
[addonmanager_workers.UpdateSingleWorker.update_macro()](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#aa7730aefc0c4a0a491d31f718241c1bd),
and
[addonmanager_workers.UpdateSingleWorker.update_package()](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a8c07b6634edc88372cfa0eba82de3a15).

## ◆ no_pip

| addonmanager_workers.DependencyInstallationWorker.no_pip =
QtCore.Signal([str](../../d9/d36/classstr.html))  
---  
static  
  
Referenced by
[addonmanager_workers.DependencyInstallationWorker.run()](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a1a9736210fa3ae7feb0c78df6452e181).

## ◆ no_python_exe

| addonmanager_workers.DependencyInstallationWorker.no_python_exe =
QtCore.Signal()  
---  
static  
  
Referenced by
[addonmanager_workers.DependencyInstallationWorker.run()](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a1a9736210fa3ae7feb0c78df6452e181).

## ◆ python_optional

addonmanager_workers.DependencyInstallationWorker.python_optional  
---  
  
Referenced by
[addonmanager_workers.DependencyInstallationWorker.run()](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a1a9736210fa3ae7feb0c78df6452e181),
[Addon.Addon.to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
and
[Addon.Addon.walk_dependency_tree()](../../d8/d91/classAddon_1_1Addon.html#ae50a0aa2397e9da1e2ab6e3372dd48be).

## ◆ python_required

addonmanager_workers.DependencyInstallationWorker.python_required  
---  
  
Referenced by
[addonmanager_workers.DependencyInstallationWorker.run()](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a1a9736210fa3ae7feb0c78df6452e181).

## ◆ success

| addonmanager_workers.DependencyInstallationWorker.success = QtCore.Signal()  
---  
static  
  
Referenced by
[addonmanager_workers.InstallWorkbenchWorker.finish_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aafea671f9554ba9e2f58208d011e1823),
[addonmanager_workers.UpdateAllWorker.on_success()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a1e4ac86d73584f134a64abdbbca782b5),
[addonmanager_workers.ConnectionChecker.run()](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a42bb05d34618cdb7f2547f1dd59f7821),
[addonmanager_workers.DependencyInstallationWorker.run()](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a1a9736210fa3ae7feb0c78df6452e181),
[addonmanager_workers.InstallWorkbenchWorker.run_git_clone()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a6a2d19b2a80037740caebe6a694ec544),
[addonmanager_workers.InstallWorkbenchWorker.run_git_update()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a2476b9e40d1e3c156e73fa57751343e8),
[addonmanager_workers.UpdateSingleWorker.update_macro()](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#aa7730aefc0c4a0a491d31f718241c1bd),
and
[addonmanager_workers.UpdateSingleWorker.update_package()](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a8c07b6634edc88372cfa0eba82de3a15).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/addonmanager_workers.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

