---
url: https://freecad.github.io/SourceDoc/db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html
scraped_at: 2025-09-08T14:53:11.091381
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [UpdateAllWorker](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html)

[List of all members](../../df/dfc/classaddonmanager__workers_1_1UpdateAllWorker-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

addonmanager_workers.UpdateAllWorker Class Reference

##  Public Member Functions  
  
---  
None | [on_failure](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#abc670e23e0e537749e6290fd93788700) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [on_success](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a1e4ac86d73584f134a64abdbbca782b5) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
def | [run](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a04587fd788c227b0731b334b2fdd1151) (self)  
  
##  Public Attributes  
  
---  
|
[repo_queue](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a625b14bc0531aef739c6f2449d7e1316)  
|
[repos](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#aee71f307e0b0a8115e94ad3ad0078054)  
  
##  Static Public Attributes  
  
---  
|
[failure](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a2ebc0aac3ef88b4614fdbedc4e718214)
= QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html))  
|
[progress_made](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a76399853f70e57e05c11e12ea5ab474e)
= QtCore.Signal([int](../../d1/da0/classint.html),
[int](../../d1/da0/classint.html))  
|
[status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
|
[success](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#aaa4d285f7e85eca8099f9d62f6dbbd68)
= QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html))  
  
## Detailed Description

    
    
    Update all listed packages, of any kind

## Member Function Documentation

## ◆ on_failure()

None addonmanager_workers.UpdateAllWorker.on_failure  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
[addonmanager_workers.ConnectionChecker.failure](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a3e0c50e69224c95190023c513848c624),
[addonmanager_workers.InstallWorkbenchWorker.failure](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#aebef215dec1817e92522a99df709ac87),
[addonmanager_workers.DependencyInstallationWorker.failure](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a7bfb1ce653996a5c031a43b8f7cd8bab),
[addonmanager_workers.UpdateAllWorker.failure](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a2ebc0aac3ef88b4614fdbedc4e718214),
[addonmanager_workers.UpdateSingleWorker.failure](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a4eaf21e72f40cac969a348224d5a6a2c),
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
and
[package_list.PackageListItemModel.repos](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#af6a54ed385b515cda7e8a0ec23de9148).

## ◆ on_success()

None addonmanager_workers.UpdateAllWorker.on_success  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
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
[addonmanager_workers.ConnectionChecker.success](../../df/d37/classaddonmanager__workers_1_1ConnectionChecker.html#a14cf02183ee0ebb0c9b4f2b53d2313fe),
[addonmanager_workers.InstallWorkbenchWorker.success](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a65247f58b9c0d2bb122759dc36c9ce14),
[addonmanager_workers.DependencyInstallationWorker.success](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a8c699c9f999374f975896557ed333ca7),
[addonmanager_workers.UpdateAllWorker.success](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#aaa4d285f7e85eca8099f9d62f6dbbd68),
and
[addonmanager_workers.UpdateSingleWorker.success](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#a9c2bdb48945f6866bb4072e0f06257a9).

## ◆ run()

def addonmanager_workers.UpdateAllWorker.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.progress_made](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#aec3c2db73953f95de347889b8c3092cf),
[addonmanager_workers.FillMacroListWorker.progress_made](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#accd0dfdc2e30e5c92c6b604d7e7e439b),
[addonmanager_workers.CacheMacroCode.progress_made](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ac2ea5cd107221a9b413ffc96e2f3509f),
[addonmanager_workers.InstallWorkbenchWorker.progress_made](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a3eff4b2ef9e78c42b0b775d28346f569),
[addonmanager_workers.UpdateMetadataCacheWorker.progress_made](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ae662a656eac3bde23e8556a47ce15a97),
[addonmanager_workers.UpdateAllWorker.progress_made](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a76399853f70e57e05c11e12ea5ab474e),
[NetworkManager.NetworkManager.progress_made](../../d6/d8c/classNetworkManager_1_1NetworkManager.html#ac48cb7d6c22c7c510ef9eaf2e6918aea),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.repos](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#abc6aace302f1831aff61160bdc0a1598),
[addonmanager_workers.CacheMacroCode.repos](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a81ad4bd417378a765cbcccfbb97414d5),
[addonmanager_workers.UpdateMetadataCacheWorker.repos](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aff0ed6b0b1ef66eb803ae66e02ae5b52),
[addonmanager_workers.UpdateAllWorker.repos](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#aee71f307e0b0a8115e94ad3ad0078054),
and
[package_list.PackageListItemModel.repos](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#af6a54ed385b515cda7e8a0ec23de9148).

Referenced by
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[femsolver.task.Task.protector()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a913c60a87594a8bfe76580d27effcb51).

## Member Data Documentation

## ◆ failure

| addonmanager_workers.UpdateAllWorker.failure =
QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html))  
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

## ◆ progress_made

| addonmanager_workers.UpdateAllWorker.progress_made =
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

addonmanager_workers.UpdateAllWorker.repo_queue  
---  
  
Referenced by
[addonmanager_workers.UpdateAllWorker.on_failure()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#abc670e23e0e537749e6290fd93788700),
[addonmanager_workers.UpdateAllWorker.on_success()](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a1e4ac86d73584f134a64abdbbca782b5),
[addonmanager_workers.UpdateSingleWorker.run()](../../d5/dfc/classaddonmanager__workers_1_1UpdateSingleWorker.html#ab5933d27952d887b4ebeb075ea1a30fd),
and
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

## ◆ repos

addonmanager_workers.UpdateAllWorker.repos  
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

| addonmanager_workers.UpdateAllWorker.status_message =
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

| addonmanager_workers.UpdateAllWorker.success =
QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html))  
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

