---
url: https://freecad.github.io/SourceDoc/d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html
scraped_at: 2025-09-08T14:53:08.118027
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [InstallWorkbenchWorker](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html)

[List of all members](../../d5/d9b/classaddonmanager__workers_1_1InstallWorkbenchWorker-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

addonmanager_workers.InstallWorkbenchWorker Class Reference

##  Public Member Functions  
  
---  
def | [finish_zip](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aafea671f9554ba9e2f58208d011e1823) (self, [int](../../d1/da0/classint.html) index, [int](../../d1/da0/classint.html) response_code, os.PathLike filename)  
None | [launch_zip](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adfe4a53563dc3d0679c1c4b55c105e23) (self, [str](../../d9/d36/classstr.html) [zipdir](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb9dbff621a815bd2b51c28a7f8eb617))  
def | [run](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab4f35eb3b8558bfde6c9bed37b61bb98) (self)  
None | [run_git](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aa24af9e6f90bccf4cbde30f007225a08) (self, [str](../../d9/d36/classstr.html) clonedir)  
None | [run_git_clone](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a6a2d19b2a80037740caebe6a694ec544) (self, [str](../../d9/d36/classstr.html) clonedir)  
None | [run_git_update](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a2476b9e40d1e3c156e73fa57751343e8) (self, [str](../../d9/d36/classstr.html) clonedir)  
def | [update_metadata](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab38237a511d4457126dfcccd44914d2c) (self)  
None | [update_status](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a1c775af73dfc50bd38f5d20b8f30fc60) (self)  
def | [update_zip_status](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab359ae038ce28b1712013e7d2800e7dc) (self, [int](../../d1/da0/classint.html) index, [int](../../d1/da0/classint.html) bytes_read, [int](../../d1/da0/classint.html) data_size)  
  
##  Public Attributes  
  
---  
|
[bakdir](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aa864bc12615b21374f597a61c5ce2fa2)  
|
[git_progress](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ad15f40e56c329bcce5e74baf0f83d7e2)  
|
[repo](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb740b7501c2d9833372b11aa4338608)  
|
[update_timer](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#af6fc6a8d60210403463c2fb057be75e0)  
|
[zip_complete](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a3a4aeb51bec58c031f1c0c85f88d1c32)  
|
[zip_download_index](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ae0f5c6f789c5b623deaff6065323a7eb)  
|
[zipdir](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb9dbff621a815bd2b51c28a7f8eb617)  
  
##  Static Public Attributes  
  
---  
|
[failure](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aebef215dec1817e92522a99df709ac87)
= QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html),
[str](../../d9/d36/classstr.html))  
|
[progress_made](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a3eff4b2ef9e78c42b0b775d28346f569)
= QtCore.Signal([int](../../d1/da0/classint.html),
[int](../../d1/da0/classint.html))  
|
[status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
|
[success](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a65247f58b9c0d2bb122759dc36c9ce14)
= QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html),
[str](../../d9/d36/classstr.html))  
  
## Member Function Documentation

## ◆ finish_zip()

def addonmanager_workers.InstallWorkbenchWorker.finish_zip  | ( |  | _self_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _index_ ,   
|  | [int](../../d1/da0/classint.html) | _response_code_ ,   
|  | os.PathLike  | _filename_  
| ) | |   
  
References
[addonmanager_workers.InstallWorkbenchWorker.bakdir](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aa864bc12615b21374f597a61c5ce2fa2),
[addonmanager_workers.ConnectionChecker.failure](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a3e0c50e69224c95190023c513848c624),
[addonmanager_workers.InstallWorkbenchWorker.failure](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aebef215dec1817e92522a99df709ac87),
[addonmanager_workers.DependencyInstallationWorker.failure](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a7bfb1ce653996a5c031a43b8f7cd8bab),
[addonmanager_workers.UpdateAllWorker.failure](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a2ebc0aac3ef88b4614fdbedc4e718214),
[addonmanager_workers.UpdateSingleWorker.failure](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a4eaf21e72f40cac969a348224d5a6a2c),
[addonmanager_workers.CheckSingleUpdateWorker.repo](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ae50f5edf0ada57f45653579ce2f728d1),
[addonmanager_workers.InstallWorkbenchWorker.repo](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb740b7501c2d9833372b11aa4338608),
[change_branch.ChangeBranchDialogModel.repo](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a9a5e684f9b7257f172747a8e1821e4d4),
[package_details.PackageDetails.repo](../../d1/df5/classpackage__details_1_1PackageDetails.html#af636079625de5fa04f2543585b07181a),
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2),
[addonmanager_workers.ConnectionChecker.success](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a14cf02183ee0ebb0c9b4f2b53d2313fe),
[addonmanager_workers.InstallWorkbenchWorker.success](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a65247f58b9c0d2bb122759dc36c9ce14),
[addonmanager_workers.DependencyInstallationWorker.success](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a8c699c9f999374f975896557ed333ca7),
[addonmanager_workers.UpdateAllWorker.success](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#aaa4d285f7e85eca8099f9d62f6dbbd68),
[addonmanager_workers.UpdateSingleWorker.success](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a9c2bdb48945f6866bb4072e0f06257a9),
[addonmanager_workers.InstallWorkbenchWorker.update_metadata()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab38237a511d4457126dfcccd44914d2c),
[addonmanager_workers.InstallWorkbenchWorker.zip_complete](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a3a4aeb51bec58c031f1c0c85f88d1c32),
and
[addonmanager_workers.InstallWorkbenchWorker.zipdir](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb9dbff621a815bd2b51c28a7f8eb617).

## ◆ launch_zip()

None addonmanager_workers.InstallWorkbenchWorker.launch_zip  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _zipdir_  
| ) | |   
  
References
[addonmanager_workers.ConnectionChecker.failure](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a3e0c50e69224c95190023c513848c624),
[addonmanager_workers.InstallWorkbenchWorker.failure](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aebef215dec1817e92522a99df709ac87),
[addonmanager_workers.DependencyInstallationWorker.failure](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a7bfb1ce653996a5c031a43b8f7cd8bab),
[addonmanager_workers.UpdateAllWorker.failure](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a2ebc0aac3ef88b4614fdbedc4e718214),
[addonmanager_workers.UpdateSingleWorker.failure](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a4eaf21e72f40cac969a348224d5a6a2c),
[addonmanager_workers.CheckSingleUpdateWorker.repo](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ae50f5edf0ada57f45653579ce2f728d1),
[addonmanager_workers.InstallWorkbenchWorker.repo](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb740b7501c2d9833372b11aa4338608),
[change_branch.ChangeBranchDialogModel.repo](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a9a5e684f9b7257f172747a8e1821e4d4),
and
[package_details.PackageDetails.repo](../../d1/df5/classpackage__details_1_1PackageDetails.html#af636079625de5fa04f2543585b07181a).

Referenced by
[addonmanager_workers.InstallWorkbenchWorker.run()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab4f35eb3b8558bfde6c9bed37b61bb98).

## ◆ run()

def addonmanager_workers.InstallWorkbenchWorker.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[addonmanager_workers.InstallWorkbenchWorker.launch_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adfe4a53563dc3d0679c1c4b55c105e23),
[addonmanager_workers.CheckSingleUpdateWorker.repo](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ae50f5edf0ada57f45653579ce2f728d1),
[addonmanager_workers.InstallWorkbenchWorker.repo](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb740b7501c2d9833372b11aa4338608),
[change_branch.ChangeBranchDialogModel.repo](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a9a5e684f9b7257f172747a8e1821e4d4),
[package_details.PackageDetails.repo](../../d1/df5/classpackage__details_1_1PackageDetails.html#af636079625de5fa04f2543585b07181a),
and
[addonmanager_workers.InstallWorkbenchWorker.run_git()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aa24af9e6f90bccf4cbde30f007225a08).

Referenced by
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[femsolver.task.Task.protector()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a913c60a87594a8bfe76580d27effcb51).

## ◆ run_git()

None addonmanager_workers.InstallWorkbenchWorker.run_git  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _clonedir_  
| ) | |   
  
Referenced by
[addonmanager_workers.InstallWorkbenchWorker.run()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab4f35eb3b8558bfde6c9bed37b61bb98).

## ◆ run_git_clone()

None addonmanager_workers.InstallWorkbenchWorker.run_git_clone  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _clonedir_  
| ) | |   
  
References
[addonmanager_workers.InstallWorkbenchWorker.git_progress](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ad15f40e56c329bcce5e74baf0f83d7e2),
[addonmanager_workers.CheckSingleUpdateWorker.repo](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ae50f5edf0ada57f45653579ce2f728d1),
[addonmanager_workers.InstallWorkbenchWorker.repo](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb740b7501c2d9833372b11aa4338608),
[change_branch.ChangeBranchDialogModel.repo](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a9a5e684f9b7257f172747a8e1821e4d4),
[package_details.PackageDetails.repo](../../d1/df5/classpackage__details_1_1PackageDetails.html#af636079625de5fa04f2543585b07181a),
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2),
[addonmanager_workers.ConnectionChecker.success](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a14cf02183ee0ebb0c9b4f2b53d2313fe),
[addonmanager_workers.InstallWorkbenchWorker.success](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a65247f58b9c0d2bb122759dc36c9ce14),
[addonmanager_workers.DependencyInstallationWorker.success](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a8c699c9f999374f975896557ed333ca7),
[addonmanager_workers.UpdateAllWorker.success](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#aaa4d285f7e85eca8099f9d62f6dbbd68),
[addonmanager_workers.UpdateSingleWorker.success](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a9c2bdb48945f6866bb4072e0f06257a9),
and
[addonmanager_workers.InstallWorkbenchWorker.update_metadata()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab38237a511d4457126dfcccd44914d2c).

## ◆ run_git_update()

None addonmanager_workers.InstallWorkbenchWorker.run_git_update  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _clonedir_  
| ) | |   
  
References
[addonmanager_workers.ConnectionChecker.failure](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a3e0c50e69224c95190023c513848c624),
[addonmanager_workers.InstallWorkbenchWorker.failure](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aebef215dec1817e92522a99df709ac87),
[addonmanager_workers.DependencyInstallationWorker.failure](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a7bfb1ce653996a5c031a43b8f7cd8bab),
[addonmanager_workers.UpdateAllWorker.failure](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a2ebc0aac3ef88b4614fdbedc4e718214),
[addonmanager_workers.UpdateSingleWorker.failure](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a4eaf21e72f40cac969a348224d5a6a2c),
[addonmanager_workers.CheckSingleUpdateWorker.repo](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ae50f5edf0ada57f45653579ce2f728d1),
[addonmanager_workers.InstallWorkbenchWorker.repo](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb740b7501c2d9833372b11aa4338608),
[change_branch.ChangeBranchDialogModel.repo](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a9a5e684f9b7257f172747a8e1821e4d4),
[package_details.PackageDetails.repo](../../d1/df5/classpackage__details_1_1PackageDetails.html#af636079625de5fa04f2543585b07181a),
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2),
[addonmanager_workers.ConnectionChecker.success](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a14cf02183ee0ebb0c9b4f2b53d2313fe),
[addonmanager_workers.InstallWorkbenchWorker.success](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a65247f58b9c0d2bb122759dc36c9ce14),
[addonmanager_workers.DependencyInstallationWorker.success](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a8c699c9f999374f975896557ed333ca7),
[addonmanager_workers.UpdateAllWorker.success](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#aaa4d285f7e85eca8099f9d62f6dbbd68),
[addonmanager_workers.UpdateSingleWorker.success](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a9c2bdb48945f6866bb4072e0f06257a9),
and
[addonmanager_workers.InstallWorkbenchWorker.update_metadata()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab38237a511d4457126dfcccd44914d2c).

## ◆ update_metadata()

def addonmanager_workers.InstallWorkbenchWorker.update_metadata  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[addonmanager_workers.CheckSingleUpdateWorker.repo](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ae50f5edf0ada57f45653579ce2f728d1),
[addonmanager_workers.InstallWorkbenchWorker.repo](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb740b7501c2d9833372b11aa4338608),
[change_branch.ChangeBranchDialogModel.repo](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a9a5e684f9b7257f172747a8e1821e4d4),
and
[package_details.PackageDetails.repo](../../d1/df5/classpackage__details_1_1PackageDetails.html#af636079625de5fa04f2543585b07181a).

Referenced by
[addonmanager_workers.InstallWorkbenchWorker.finish_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aafea671f9554ba9e2f58208d011e1823),
[addonmanager_workers.InstallWorkbenchWorker.run_git_clone()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a6a2d19b2a80037740caebe6a694ec544),
and
[addonmanager_workers.InstallWorkbenchWorker.run_git_update()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a2476b9e40d1e3c156e73fa57751343e8).

## ◆ update_status()

None addonmanager_workers.InstallWorkbenchWorker.update_status  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[addonmanager_workers.InstallWorkbenchWorker.git_progress](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ad15f40e56c329bcce5e74baf0f83d7e2),
[Base::SequencerBase.isRunning()](../../d5/d0d/classBase_1_1SequencerBase.html#a06f770a5ba78c654f4d132b235bccd28),
[Gui::GUISingleApplication.isRunning()](../../df/d7d/classGui_1_1GUISingleApplication.html#ac37ba24deeba8a8af79c5f0383d985f4),
[Gui::PythonDebugger.isRunning()](../../d6/d11/classGui_1_1PythonDebugger.html#a8095fc9284418f7c5c34996629c0866e),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.progress_made](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#aec3c2db73953f95de347889b8c3092cf),
[addonmanager_workers.FillMacroListWorker.progress_made](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#accd0dfdc2e30e5c92c6b604d7e7e439b),
[addonmanager_workers.CacheMacroCode.progress_made](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ac2ea5cd107221a9b413ffc96e2f3509f),
[addonmanager_workers.InstallWorkbenchWorker.progress_made](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a3eff4b2ef9e78c42b0b775d28346f569),
[addonmanager_workers.UpdateMetadataCacheWorker.progress_made](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ae662a656eac3bde23e8556a47ce15a97),
[addonmanager_workers.UpdateAllWorker.progress_made](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a76399853f70e57e05c11e12ea5ab474e),
[NetworkManager.NetworkManager.progress_made](../../d6/d8c/classNetworkManager_1_1NetworkManager.html#ac48cb7d6c22c7c510ef9eaf2e6918aea),
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
and
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2).

Referenced by
[package_details.PackageDetails.branch_changed()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a15328dbccbc762df726cf1fe9264cb5c),
[package_details.PackageDetails.disable_clicked()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a0b127e8433a9db40523d10257c612dd3),
[addonmanager_workers.CheckSingleUpdateWorker.do_work()](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#a6e2315825d6edc51c358bbd4e6974ff3),
[package_details.PackageDetails.enable_clicked()](../../d1/df5/classpackage__details_1_1PackageDetails.html#a9633078163d737ff02767885299c4b13),
and
[Addon.Addon.status()](../../d8/d91/classAddon_1_1Addon.html#a90e6cb0915b389fd7c401152070733f9).

## ◆ update_zip_status()

def addonmanager_workers.InstallWorkbenchWorker.update_zip_status  | ( |  | _self_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _index_ ,   
|  | [int](../../d1/da0/classint.html) | _bytes_read_ ,   
|  | [int](../../d1/da0/classint.html) | _data_size_  
| ) | |   
  
References
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.progress_made](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#aec3c2db73953f95de347889b8c3092cf),
[addonmanager_workers.FillMacroListWorker.progress_made](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#accd0dfdc2e30e5c92c6b604d7e7e439b),
[addonmanager_workers.CacheMacroCode.progress_made](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ac2ea5cd107221a9b413ffc96e2f3509f),
[addonmanager_workers.InstallWorkbenchWorker.progress_made](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a3eff4b2ef9e78c42b0b775d28346f569),
[addonmanager_workers.UpdateMetadataCacheWorker.progress_made](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ae662a656eac3bde23e8556a47ce15a97),
[addonmanager_workers.UpdateAllWorker.progress_made](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a76399853f70e57e05c11e12ea5ab474e),
[NetworkManager.NetworkManager.progress_made](../../d6/d8c/classNetworkManager_1_1NetworkManager.html#ac48cb7d6c22c7c510ef9eaf2e6918aea),
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2),
and
[addonmanager_workers.InstallWorkbenchWorker.zip_download_index](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ae0f5c6f789c5b623deaff6065323a7eb).

## Member Data Documentation

## ◆ bakdir

addonmanager_workers.InstallWorkbenchWorker.bakdir  
---  
  
Referenced by
[addonmanager_workers.InstallWorkbenchWorker.finish_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aafea671f9554ba9e2f58208d011e1823).

## ◆ failure

| addonmanager_workers.InstallWorkbenchWorker.failure =
QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html),
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

## ◆ git_progress

addonmanager_workers.InstallWorkbenchWorker.git_progress  
---  
  
Referenced by
[addonmanager_workers.InstallWorkbenchWorker.run_git_clone()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a6a2d19b2a80037740caebe6a694ec544),
and
[addonmanager_workers.InstallWorkbenchWorker.update_status()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a1c775af73dfc50bd38f5d20b8f30fc60).

## ◆ progress_made

| addonmanager_workers.InstallWorkbenchWorker.progress_made =
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

## ◆ repo

addonmanager_workers.InstallWorkbenchWorker.repo  
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

## ◆ status_message

| addonmanager_workers.InstallWorkbenchWorker.status_message =
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

## ◆ success

| addonmanager_workers.InstallWorkbenchWorker.success =
QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html),
[str](../../d9/d36/classstr.html))  
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

## ◆ update_timer

addonmanager_workers.InstallWorkbenchWorker.update_timer  
---  
  
## ◆ zip_complete

addonmanager_workers.InstallWorkbenchWorker.zip_complete  
---  
  
Referenced by
[addonmanager_workers.InstallWorkbenchWorker.finish_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aafea671f9554ba9e2f58208d011e1823).

## ◆ zip_download_index

addonmanager_workers.InstallWorkbenchWorker.zip_download_index  
---  
  
Referenced by
[addonmanager_workers.InstallWorkbenchWorker.update_zip_status()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#ab359ae038ce28b1712013e7d2800e7dc).

## ◆ zipdir

addonmanager_workers.InstallWorkbenchWorker.zipdir  
---  
  
Referenced by
[addonmanager_workers.InstallWorkbenchWorker.finish_zip()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aafea671f9554ba9e2f58208d011e1823).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/addonmanager_workers.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

