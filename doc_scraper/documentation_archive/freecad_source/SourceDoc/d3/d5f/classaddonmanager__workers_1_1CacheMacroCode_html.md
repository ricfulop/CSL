---
url: https://freecad.github.io/SourceDoc/d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html
scraped_at: 2025-09-08T14:53:00.053551
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [CacheMacroCode](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html)

[List of all members](../../d8/d67/classaddonmanager__workers_1_1CacheMacroCode-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

addonmanager_workers.CacheMacroCode Class Reference

##  Public Member Functions  
  
---  
def | [run](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a337d9ec4228904f76fd1ed0b5e28944f) (self)  
None | [terminate](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad7e2fd17788450db3eedb1cfa1195aa9) (self, worker)  
None | [update_and_advance](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
  
##  Public Attributes  
  
---  
|
[counter](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a15dec1a148fd960db1ca8f08e4b96caf)  
|
[failed](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad9318003074a8623c1b26126dce5ec2f)  
|
[lock](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a34409bcd85d153bfccf525439ff48e9a)  
|
[repo_queue](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#affcb64c59e53fbfe5a70b1aef5289b16)  
|
[repos](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a81ad4bd417378a765cbcccfbb97414d5)  
|
[terminators](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a09036d3d098e4ba457735cd70c68f606)  
|
[workers](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a817e3c52e14b2cee3da87afdd37e718b)  
  
##  Static Public Attributes  
  
---  
|
[progress_made](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ac2ea5cd107221a9b413ffc96e2f3509f)
= QtCore.Signal([int](../../d1/da0/classint.html),
[int](../../d1/da0/classint.html))  
|
[status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
|
[update_macro](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a1887980ea42b0fcfb19f3c96dd8276d2)
= QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html))  
  
## Detailed Description

    
    
    Download and cache the macro code, and parse its internal metadata

## Member Function Documentation

## ◆ run()

def addonmanager_workers.CacheMacroCode.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
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

## ◆ terminate()

None addonmanager_workers.CacheMacroCode.terminate  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _worker_  
| ) | |   
  
References
[addonmanager_workers.CacheMacroCode.failed](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad9318003074a8623c1b26126dce5ec2f),
[femsolver.task.Task.failed()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a576a857af0c80cebc298e7dba90d136a),
[SALOMEDS::Locker.lock](../../d6/df4/classSALOMEDS_1_1Locker.html#aa81aed607133209dade63a226818224d),
[Utils_Mutex.lock()](../../dd/dca/classUtils__Mutex.html#afb576429956b8b38fa6823ce009e2f5f),
[e57::PacketReadCache.lock()](../../d5/dd4/classe57_1_1PacketReadCache.html#ae7c5d06657c0f485dddc0cb46d2ee7f8),
Base::StateLocker.lock,
[Gui::EditorViewP.lock](../../d8/d13/classGui_1_1EditorViewP.html#aef8cdeb8caad916edacc1e4290e8cae5),
[AddonManager.CommandAddonManager.lock](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad17bd5b7265a48f723442507a0ab640f),
[addonmanager_workers.CacheMacroCode.lock](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a34409bcd85d153bfccf525439ff48e9a),
[drafttaskpanels.task_scale.ScaleTaskPanel.lock](../../df/d70/classdrafttaskpanels_1_1task__scale_1_1ScaleTaskPanel.html#ad83c52110d9f64357206b0d5d23669e3),
and
[PathScripts.PathCamoticsGui.CAMoticsUI.lock](../../d2/df4/classPathScripts_1_1PathCamoticsGui_1_1CAMoticsUI.html#aa6f16f7304d9de48b95e87e0345da8e8).

Referenced by
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

## ◆ update_and_advance()

None addonmanager_workers.CacheMacroCode.update_and_advance  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
[FaceQuadStruct::SideIterator.counter](../../d2/d4b/structFaceQuadStruct_1_1SideIterator.html#ae421c327cbddd482b6f6dd2f42afb31a),
[Gui::SoFCSelectionContext.counter](../../d7/dbb/structGui_1_1SoFCSelectionContext.html#ae9474063c1d12cb677ba44f47bfb3eb1),
[Gui::SoFCSelectionCounter.counter](../../de/ded/classGui_1_1SoFCSelectionCounter.html#a415205483f5eaf2d82fa352738134fa6),
[addonmanager_workers.CacheMacroCode.counter](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a15dec1a148fd960db1ca8f08e4b96caf),
[addonmanager_workers.CacheMacroCode.failed](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad9318003074a8623c1b26126dce5ec2f),
[femsolver.task.Task.failed()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a576a857af0c80cebc298e7dba90d136a),
[SALOMEDS::Locker.lock](../../d6/df4/classSALOMEDS_1_1Locker.html#aa81aed607133209dade63a226818224d),
[Utils_Mutex.lock()](../../dd/dca/classUtils__Mutex.html#afb576429956b8b38fa6823ce009e2f5f),
[e57::PacketReadCache.lock()](../../d5/dd4/classe57_1_1PacketReadCache.html#ae7c5d06657c0f485dddc0cb46d2ee7f8),
Base::StateLocker.lock,
[Gui::EditorViewP.lock](../../d8/d13/classGui_1_1EditorViewP.html#aef8cdeb8caad916edacc1e4290e8cae5),
[AddonManager.CommandAddonManager.lock](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad17bd5b7265a48f723442507a0ab640f),
[addonmanager_workers.CacheMacroCode.lock](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a34409bcd85d153bfccf525439ff48e9a),
[drafttaskpanels.task_scale.ScaleTaskPanel.lock](../../df/d70/classdrafttaskpanels_1_1task__scale_1_1ScaleTaskPanel.html#ad83c52110d9f64357206b0d5d23669e3),
[PathScripts.PathCamoticsGui.CAMoticsUI.lock](../../d2/df4/classPathScripts_1_1PathCamoticsGui_1_1CAMoticsUI.html#aa6f16f7304d9de48b95e87e0345da8e8),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.progress_made](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#aec3c2db73953f95de347889b8c3092cf),
[addonmanager_workers.FillMacroListWorker.progress_made](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#accd0dfdc2e30e5c92c6b604d7e7e439b),
[addonmanager_workers.CacheMacroCode.progress_made](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ac2ea5cd107221a9b413ffc96e2f3509f),
[addonmanager_workers.InstallWorkbenchWorker.progress_made](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a3eff4b2ef9e78c42b0b775d28346f569),
[addonmanager_workers.UpdateMetadataCacheWorker.progress_made](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ae662a656eac3bde23e8556a47ce15a97),
[addonmanager_workers.UpdateAllWorker.progress_made](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a76399853f70e57e05c11e12ea5ab474e),
[NetworkManager.NetworkManager.progress_made](../../d6/d8c/classNetworkManager_1_1NetworkManager.html#ac48cb7d6c22c7c510ef9eaf2e6918aea),
[addonmanager_workers.CacheMacroCode.repo_queue](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#affcb64c59e53fbfe5a70b1aef5289b16),
[addonmanager_workers.UpdateAllWorker.repo_queue](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a625b14bc0531aef739c6f2449d7e1316),
[addonmanager_workers.UpdateSingleWorker.repo_queue](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#ad38e8e67b490c04cabb1ddcc40a0ae33),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.repos](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#abc6aace302f1831aff61160bdc0a1598),
[addonmanager_workers.CacheMacroCode.repos](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a81ad4bd417378a765cbcccfbb97414d5),
[addonmanager_workers.UpdateMetadataCacheWorker.repos](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aff0ed6b0b1ef66eb803ae66e02ae5b52),
[addonmanager_workers.UpdateAllWorker.repos](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#aee71f307e0b0a8115e94ad3ad0078054),
[package_list.PackageListItemModel.repos](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#af6a54ed385b515cda7e8a0ec23de9148),
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2),
[XMLTools.terminate()](../../dc/d06/classXMLTools.html#ac39ed2fbccc2e2536739388151108e07),
[SandboxGui::DrawingPlane.terminate()](../../da/d3b/classSandboxGui_1_1DrawingPlane.html#a53c80645eaaffdd1e627df72d1b4396e),
[Gui::PolyPickerSelection.terminate()](../../d2/d39/classGui_1_1PolyPickerSelection.html#ace863a7d0a2f51192bf4b5de0fde7a23),
[Gui::RubberbandSelection.terminate()](../../d3/d4e/classGui_1_1RubberbandSelection.html#a6c332a9124b943fa38b765d28c859b1a),
[Gui::BoxZoomSelection.terminate()](../../d3/d8e/classGui_1_1BoxZoomSelection.html#a630a3eacf089b37d264ad67b40dc7507),
[Gui::AbstractMouseSelection.terminate()](../../da/d82/classGui_1_1AbstractMouseSelection.html#a62f38141116b5ca59113b45aa6f94777),
[addonmanager_workers.CacheMacroCode.terminate()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad7e2fd17788450db3eedb1cfa1195aa9),
[addonmanager_workers.CacheMacroCode.terminators](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a09036d3d098e4ba457735cd70c68f606),
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631),
[addonmanager_workers.CacheMacroCode.update_macro](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a1887980ea42b0fcfb19f3c96dd8276d2),
[addonmanager_workers.UpdateSingleWorker.update_macro()](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#aa7730aefc0c4a0a491d31f718241c1bd),
[AddonManager.CommandAddonManager.workers](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3414e0cc98f96ec31b3a7073b3be08e1),
and
[addonmanager_workers.CacheMacroCode.workers](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a817e3c52e14b2cee3da87afdd37e718b).

Referenced by
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

## Member Data Documentation

## ◆ counter

addonmanager_workers.CacheMacroCode.counter  
---  
  
Referenced by
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

## ◆ failed

addonmanager_workers.CacheMacroCode.failed  
---  
  
Referenced by
[femsolver.run.Machine.run()](../../d2/d54/classfemsolver_1_1run_1_1Machine.html#a863785c4039b699f146fefbea26bfd02),
[addonmanager_workers.CacheMacroCode.terminate()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad7e2fd17788450db3eedb1cfa1195aa9),
and
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

## ◆ lock

addonmanager_workers.CacheMacroCode.lock  
---  
  
Referenced by
[AddonManager.CommandAddonManager.on_package_updated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae31bf139686923b617a182aeb1588425),
[drafttaskpanels.task_scale.ScaleTaskPanel.retranslateUi()](../../df/d70/classdrafttaskpanels_1_1task__scale_1_1ScaleTaskPanel.html#ab5cdf6b149fea39e027f877ea7b5a12c),
[drafttaskpanels.task_scale.ScaleTaskPanel.setValue()](../../df/d70/classdrafttaskpanels_1_1task__scale_1_1ScaleTaskPanel.html#a1782575b8f05ad2356a3dc6d60cd6f2d),
[addonmanager_workers.CacheMacroCode.terminate()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad7e2fd17788450db3eedb1cfa1195aa9),
and
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

## ◆ progress_made

| addonmanager_workers.CacheMacroCode.progress_made =
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

## ◆ repo_queue

addonmanager_workers.CacheMacroCode.repo_queue  
---  
  
Referenced by
[addonmanager_workers.UpdateAllWorker.on_failure()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#abc670e23e0e537749e6290fd93788700),
[addonmanager_workers.UpdateAllWorker.on_success()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a1e4ac86d73584f134a64abdbbca782b5),
[addonmanager_workers.UpdateSingleWorker.run()](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#ab5933d27952d887b4ebeb075ea1a30fd),
and
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

## ◆ repos

addonmanager_workers.CacheMacroCode.repos  
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

## ◆ status_message

| addonmanager_workers.CacheMacroCode.status_message =
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

## ◆ terminators

addonmanager_workers.CacheMacroCode.terminators  
---  
  
Referenced by
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

## ◆ update_macro

| addonmanager_workers.CacheMacroCode.update_macro =
QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html))  
---  
static  
  
Referenced by
[addonmanager_workers.UpdateSingleWorker.run()](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#ab5933d27952d887b4ebeb075ea1a30fd),
and
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

## ◆ workers

addonmanager_workers.CacheMacroCode.workers  
---  
  
Referenced by
[AddonManager.CommandAddonManager.cleanup_workers()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d86001908bd07941d546db0e6463065),
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca),
and
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/addonmanager_workers.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

