---
url: https://freecad.github.io/SourceDoc/dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html
scraped_at: 2025-09-08T14:53:01.044655
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [CheckSingleUpdateWorker](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html)

[List of all members](../../d0/d8d/classaddonmanager__workers_1_1CheckSingleUpdateWorker-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

addonmanager_workers.CheckSingleUpdateWorker Class Reference

##  Public Member Functions  
  
---  
def | [do_work](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#a6e2315825d6edc51c358bbd4e6974ff3) (self)  
  
##  Public Attributes  
  
---  
|
[repo](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ae50f5edf0ada57f45653579ce2f728d1)  
  
##  Static Public Attributes  
  
---  
|
[update_status](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ad469196d2e39833474901564d96ecd64)
= QtCore.Signal([int](../../d1/da0/classint.html))  
  
## Detailed Description

    
    
    This worker is a little different from the others: the actual recommended way of
    running in a QThread is to make a worker object that gets moved into the thread.

## Member Function Documentation

## ◆ do_work()

def addonmanager_workers.CheckSingleUpdateWorker.do_work  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[addonmanager_workers.CheckSingleUpdateWorker.repo](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ae50f5edf0ada57f45653579ce2f728d1),
[addonmanager_workers.InstallWorkbenchWorker.repo](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb740b7501c2d9833372b11aa4338608),
[change_branch.ChangeBranchDialogModel.repo](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a9a5e684f9b7257f172747a8e1821e4d4),
[package_details.PackageDetails.repo](../../d1/df5/classpackage__details_1_1PackageDetails.html#af636079625de5fa04f2543585b07181a),
[Addon.Addon.update_status](../../d8/d91/classAddon_1_1Addon.html#aad61be4901c10955b3b4f78de986fc40),
[addonmanager_workers.CheckSingleUpdateWorker.update_status](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ad469196d2e39833474901564d96ecd64),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.update_status](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#a0dbe65a310779daaa8d48aa7881d8935),
[addonmanager_workers.InstallWorkbenchWorker.update_status()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a1c775af73dfc50bd38f5d20b8f30fc60),
and
[package_details.PackageDetails.update_status](../../d1/df5/classpackage__details_1_1PackageDetails.html#ad40d0044d11ee9629cf43a1f4819d72f).

## Member Data Documentation

## ◆ repo

addonmanager_workers.CheckSingleUpdateWorker.repo  
---  
  
Referenced by
[package_details.PackageDetails.branch_changed()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a15328dbccbc762df726cf1fe9264cb5c),
[package_details.PackageDetails.change_branch_clicked()](../../d1/df5/classpackage__details_1_1PackageDetails.html#afd7c8de0e903b89492fae61e6b22d418),
[change_branch.ChangeBranchDialogModel.data()](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#aeb42e63ba760cbcdaa58d35d89299e0c),
[package_details.PackageDetails.disable_clicked()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a0b127e8433a9db40523d10257c612dd3),
[package_details.PackageDetails.display_repo_status()](../../d1/df5/classpackage__details_1_1PackageDetails.html#abafff14948ac22d38fe00e5cf8110900),
[addonmanager_workers.CheckSingleUpdateWorker.do_work()](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#a6e2315825d6edc51c358bbd4e6974ff3),
[package_details.PackageDetails.enable_clicked()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a9633078163d737ff02767885299c4b13),
[addonmanager_workers.InstallWorkbenchWorker.finish_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aafea671f9554ba9e2f58208d011e1823),
[addonmanager_workers.InstallWorkbenchWorker.launch_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adfe4a53563dc3d0679c1c4b55c105e23),
[package_details.PackageDetails.macro_readme_updated()](../../d1/df5/classpackage__details_1_1PackageDetails.html#adaec13a0b56c829e2f4fd5018d49dc5e),
[package_details.PackageDetails.requires_newer_freecad()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a9928cf0e86ec8711412e7924876265f5),
[addonmanager_workers.InstallWorkbenchWorker.run()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab4f35eb3b8558bfde6c9bed37b61bb98),
[addonmanager_workers.InstallWorkbenchWorker.run_git_clone()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a6a2d19b2a80037740caebe6a694ec544),
[addonmanager_workers.InstallWorkbenchWorker.run_git_update()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a2476b9e40d1e3c156e73fa57751343e8),
[package_details.PackageDetails.set_change_branch_button_state()](../../d1/df5/classpackage__details_1_1PackageDetails.html#aef7177bce5cd10a353851f12a8eedb45),
[package_details.PackageDetails.set_disable_button_state()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a3bbe5faf55f51f98c78ce43e0501cf02),
[package_details.PackageDetails.show_repo()](../../d1/df5/classpackage__details_1_1PackageDetails.html#aae7b13ab2d26ff73d55732b868b71edf),
and
[addonmanager_workers.InstallWorkbenchWorker.update_metadata()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab38237a511d4457126dfcccd44914d2c).

## ◆ update_status

| addonmanager_workers.CheckSingleUpdateWorker.update_status =
QtCore.Signal([int](../../d1/da0/classint.html))  
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

