---
url: https://freecad.github.io/SourceDoc/da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html
scraped_at: 2025-09-08T14:53:02.041960
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [CheckWorkbenchesForUpdatesWorker](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html)

[List of all members](../../d9/dde/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

addonmanager_workers.CheckWorkbenchesForUpdatesWorker Class Reference

##  Public Member Functions  
  
---  
def | [run](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#af4877b6e7ad507fcf13e9b34260247bb) (self)  
  
##  Public Attributes  
  
---  
|
[basedir](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#a7e4db656a6793d560fcfd99fb79f5464)  
|
[current_thread](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#a28c730493adffabdbb3665082a7abfde)  
|
[moddir](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#a2c9a1c473a49c2a9c4fb32ce3d596381)  
|
[repos](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#abc6aace302f1831aff61160bdc0a1598)  
  
##  Static Public Attributes  
  
---  
|
[progress_made](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#aec3c2db73953f95de347889b8c3092cf)
= QtCore.Signal([int](../../d1/da0/classint.html),
[int](../../d1/da0/classint.html))  
|
[update_status](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#a0dbe65a310779daaa8d48aa7881d8935)
= QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html))  
  
## Detailed Description

    
    
    This worker checks for available updates for all workbenches

## Member Function Documentation

## ◆ run()

def addonmanager_workers.CheckWorkbenchesForUpdatesWorker.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[femsolver.task.Task.protector()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a913c60a87594a8bfe76580d27effcb51).

## Member Data Documentation

## ◆ basedir

addonmanager_workers.CheckWorkbenchesForUpdatesWorker.basedir  
---  
  
## ◆ current_thread

addonmanager_workers.CheckWorkbenchesForUpdatesWorker.current_thread  
---  
  
Referenced by
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_git()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a10ee78b1d84f50a0ca27e2887239ad32),
and
[addonmanager_workers.FillMacroListWorker.retrieve_macros_from_wiki()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#a3f024a71e79c2e9c92e240913af1b8b6).

## ◆ moddir

addonmanager_workers.CheckWorkbenchesForUpdatesWorker.moddir  
---  
  
Referenced by
[addonmanager_workers.UpdateChecker.check_package()](../../d1/d26/classaddonmanager__workers_1_1UpdateChecker.html#a95dc947d2a142817e21485e9920ae9e0),
and
[addonmanager_workers.UpdateChecker.check_workbench()](../../d1/d26/classaddonmanager__workers_1_1UpdateChecker.html#a1da32314d6885a6cee4a88e511c9fcbd).

## ◆ progress_made

| addonmanager_workers.CheckWorkbenchesForUpdatesWorker.progress_made =
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

## ◆ repos

addonmanager_workers.CheckWorkbenchesForUpdatesWorker.repos  
---  
  
Referenced by
[package_list.PackageListItemModel.append_item()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#ae6ca870990288c91a44d79f370a6b00a),
[package_list.PackageListItemModel.data()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#ab221470d0aa251920997ea7be8198b54),
[addonmanager_workers.UpdateAllWorker.on_failure()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#abc670e23e0e537749e6290fd93788700),
[addonmanager_workers.UpdateAllWorker.on_success()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a1e4ac86d73584f134a64abdbbca782b5),
[package_list.PackageListItemModel.reload_item()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#a88d4c0d16fd407f84abe03d8bd1d55c9),
[package_list.PackageListItemModel.rowCount()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#aef443ac131f248ff19ad493357fb907f),
[addonmanager_workers.UpdateMetadataCacheWorker.run()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a2ee7c2d005efedad23a0a5e4a6c202cb),
[addonmanager_workers.UpdateAllWorker.run()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a04587fd788c227b0731b334b2fdd1151),
[package_list.PackageListItemModel.setData()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#ae93144aca21b886d805bd1517cbc68f9),
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631),
[package_list.PackageListItemModel.update_item_icon()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#ac42a6bdc52fbbd4b036906f263ec2007),
and
[package_list.PackageListItemModel.update_item_status()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#a4d22be53f021c227b368ac920544263c).

## ◆ update_status

| addonmanager_workers.CheckWorkbenchesForUpdatesWorker.update_status =
QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html))  
---  
static  
  
Referenced by
[package_details.PackageDetails.branch_changed()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a15328dbccbc762df726cf1fe9264cb5c),
[package_details.PackageDetails.disable_clicked()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a0b127e8433a9db40523d10257c612dd3),
[addonmanager_workers.CheckSingleUpdateWorker.do_work()](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#a6e2315825d6edc51c358bbd4e6974ff3),
[package_details.PackageDetails.enable_clicked()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a9633078163d737ff02767885299c4b13),
and
[Addon.Addon.status()](../../d8/d91/classAddon_1_1Addon.html#a90e6cb0915b389fd7c401152070733f9).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/addonmanager_workers.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

