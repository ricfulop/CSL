---
url: https://freecad.github.io/SourceDoc/df/d37/classaddonmanager__workers_1_1ConnectionChecker.html
scraped_at: 2025-09-08T14:53:03.045352
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [ConnectionChecker](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html)

[List of all members](../../d9/d1f/classaddonmanager__workers_1_1ConnectionChecker-members.html) | Public Member Functions | Static Public Attributes

addonmanager_workers.ConnectionChecker Class Reference

##  Public Member Functions  
  
---  
def | [run](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a42bb05d34618cdb7f2547f1dd59f7821) (self)  
  
##  Static Public Attributes  
  
---  
|
[failure](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a3e0c50e69224c95190023c513848c624)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
|
[success](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a14cf02183ee0ebb0c9b4f2b53d2313fe)
= QtCore.Signal()  
  
## Member Function Documentation

## ◆ run()

def addonmanager_workers.ConnectionChecker.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[addonmanager_workers.ConnectionChecker.failure](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a3e0c50e69224c95190023c513848c624),
[addonmanager_workers.InstallWorkbenchWorker.failure](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aebef215dec1817e92522a99df709ac87),
[addonmanager_workers.DependencyInstallationWorker.failure](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a7bfb1ce653996a5c031a43b8f7cd8bab),
[addonmanager_workers.UpdateAllWorker.failure](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a2ebc0aac3ef88b4614fdbedc4e718214),
[addonmanager_workers.UpdateSingleWorker.failure](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a4eaf21e72f40cac969a348224d5a6a2c),
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

## ◆ failure

| addonmanager_workers.ConnectionChecker.failure =
QtCore.Signal([str](../../d9/d36/classstr.html))  
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

## ◆ success

| addonmanager_workers.ConnectionChecker.success = QtCore.Signal()  
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

