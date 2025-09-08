---
url: https://freecad.github.io/SourceDoc/d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html
scraped_at: 2025-09-08T14:53:13.131329
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [addonmanager_workers](../../d7/da4/namespaceaddonmanager__workers.html)
  * [UpdateMetadataCacheWorker](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html)

[List of all members](../../d5/d8f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker-members.html) | Classes | Public Member Functions | Public Attributes | Static Public Attributes

addonmanager_workers.UpdateMetadataCacheWorker Class Reference

##  Classes  
  
---  
class | [RequestType](../../d8/dbe/classaddonmanager__workers_1_1UpdateMetadataCacheWorker_1_1RequestType.html)  
  
##  Public Member Functions  
  
---  
None | [download_completed](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad08f2e5d64217721f3eca79acb8675da) (self, [int](../../d1/da0/classint.html) index, [int](../../d1/da0/classint.html) code, QtCore.QByteArray data)  
def | [process_icon](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a5cf0fd0e4fa73b73a2c13988752593f0) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo, QtCore.QByteArray data)  
def | [process_metadata_txt](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a921a85ca0055b090e171a8a9d2b0d7a9) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo, QtCore.QByteArray data)  
def | [process_package_xml](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad05f76bd86f0e2ad319c5b65ec4ce242) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo, QtCore.QByteArray data)  
def | [process_requirements_txt](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a1f5b401874bff312cf4979ab5031ec74) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo, QtCore.QByteArray data)  
def | [run](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a2ee7c2d005efedad23a0a5e4a6c202cb) (self)  
  
##  Public Attributes  
  
---  
|
[repos](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aff0ed6b0b1ef66eb803ae66e02ae5b52)  
|
[requests_completed](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ac81d7d54324df088551f8d91ad5c4687)  
|
[store](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a085afc14523d65f4caccfab89a6c38d1)  
|
[total_requests](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a5f79bad94ba483f073d41d4f2f4cb36e)  
|
[updated_repos](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aea6697fd4c535c12b0cb25bcfcc9a9a6)  
  
##  Static Public Attributes  
  
---  
|
[package_updated](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a9d7d4fb0041734afa4912aa71073d064)
= QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html))  
|
[progress_made](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ae662a656eac3bde23e8556a47ce15a97)
= QtCore.Signal([int](../../d1/da0/classint.html),
[int](../../d1/da0/classint.html))  
|
[status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2)
= QtCore.Signal([str](../../d9/d36/classstr.html))  
  
## Member Function Documentation

## ◆ download_completed()

None addonmanager_workers.UpdateMetadataCacheWorker.download_completed  | ( |  | _self_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _index_ ,   
|  | [int](../../d1/da0/classint.html) | _code_ ,   
|  | QtCore.QByteArray  | _data_  
| ) | |   
  
References
[addonmanager_workers.UpdateMetadataCacheWorker.process_icon()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a5cf0fd0e4fa73b73a2c13988752593f0),
[addonmanager_workers.UpdateMetadataCacheWorker.process_metadata_txt()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a921a85ca0055b090e171a8a9d2b0d7a9),
[addonmanager_workers.UpdateMetadataCacheWorker.process_package_xml()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad05f76bd86f0e2ad319c5b65ec4ce242),
[addonmanager_workers.UpdateMetadataCacheWorker.process_requirements_txt()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a1f5b401874bff312cf4979ab5031ec74),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.progress_made](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#aec3c2db73953f95de347889b8c3092cf),
[addonmanager_workers.FillMacroListWorker.progress_made](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#accd0dfdc2e30e5c92c6b604d7e7e439b),
[addonmanager_workers.CacheMacroCode.progress_made](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ac2ea5cd107221a9b413ffc96e2f3509f),
[addonmanager_workers.InstallWorkbenchWorker.progress_made](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a3eff4b2ef9e78c42b0b775d28346f569),
[addonmanager_workers.UpdateMetadataCacheWorker.progress_made](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ae662a656eac3bde23e8556a47ce15a97),
[addonmanager_workers.UpdateAllWorker.progress_made](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a76399853f70e57e05c11e12ea5ab474e),
[NetworkManager.NetworkManager.progress_made](../../d6/d8c/classNetworkManager_1_1NetworkManager.html#ac48cb7d6c22c7c510ef9eaf2e6918aea),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.action_directive.requests,
[automotive_design.action_directive.requests](../../d1/d2d/classautomotive__design_1_1action__directive.html#a58b56b3d26b35f5241f2a0913d5f6e10),
[config_control_design.action_directive.requests](../../d8/d09/classconfig__control__design_1_1action__directive.html#a5f77e6c29cbc8ab6d129f848e70b7dcc),
[addonmanager_workers.UpdateMetadataCacheWorker.requests_completed](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ac81d7d54324df088551f8d91ad5c4687),
[addonmanager_workers.UpdateMetadataCacheWorker.total_requests](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a5f79bad94ba483f073d41d4f2f4cb36e),
and
[addonmanager_workers.UpdateMetadataCacheWorker.updated_repos](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aea6697fd4c535c12b0cb25bcfcc9a9a6).

Referenced by
[addonmanager_workers.UpdateMetadataCacheWorker.run()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a2ee7c2d005efedad23a0a5e4a6c202cb).

## ◆ process_icon()

def addonmanager_workers.UpdateMetadataCacheWorker.process_icon  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_ ,   
|  | QtCore.QByteArray  | _data_  
| ) | |   
  
References
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
and
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2).

Referenced by
[addonmanager_workers.UpdateMetadataCacheWorker.download_completed()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad08f2e5d64217721f3eca79acb8675da).

## ◆ process_metadata_txt()

def addonmanager_workers.UpdateMetadataCacheWorker.process_metadata_txt  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_ ,   
|  | QtCore.QByteArray  | _data_  
| ) | |   
  
References
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2),
and
[addonmanager_workers.UpdateMetadataCacheWorker.store](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a085afc14523d65f4caccfab89a6c38d1).

Referenced by
[addonmanager_workers.UpdateMetadataCacheWorker.download_completed()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad08f2e5d64217721f3eca79acb8675da).

## ◆ process_package_xml()

def addonmanager_workers.UpdateMetadataCacheWorker.process_package_xml  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_ ,   
|  | QtCore.QByteArray  | _data_  
| ) | |   
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.action_directive.requests,
[automotive_design.action_directive.requests](../../d1/d2d/classautomotive__design_1_1action__directive.html#a58b56b3d26b35f5241f2a0913d5f6e10),
[config_control_design.action_directive.requests](../../d8/d09/classconfig__control__design_1_1action__directive.html#a5f77e6c29cbc8ab6d129f848e70b7dcc),
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2),
[addonmanager_workers.UpdateMetadataCacheWorker.store](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a085afc14523d65f4caccfab89a6c38d1),
and
[addonmanager_workers.UpdateMetadataCacheWorker.total_requests](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a5f79bad94ba483f073d41d4f2f4cb36e).

Referenced by
[addonmanager_workers.UpdateMetadataCacheWorker.download_completed()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad08f2e5d64217721f3eca79acb8675da).

## ◆ process_requirements_txt()

def addonmanager_workers.UpdateMetadataCacheWorker.process_requirements_txt  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_ ,   
|  | QtCore.QByteArray  | _data_  
| ) | |   
  
References
[addonmanager_workers.UpdateWorker.status_message](../../d2/d2d/classaddonmanager__workers_1_1UpdateWorker.html#a3204eada4090de9f92bd6508f9ecbc54),
[addonmanager_workers.CacheMacroCode.status_message](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad50a7c415eb611c669697b2520acade4),
[addonmanager_workers.GetMacroDetailsWorker.status_message](../../d9/ded/classaddonmanager__workers_1_1GetMacroDetailsWorker.html#a2e9d754e70c0afa81531f3e6d7de2ff2),
[addonmanager_workers.InstallWorkbenchWorker.status_message](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a970867912bcfda86a5f796ee7552e640),
[addonmanager_workers.UpdateMetadataCacheWorker.status_message](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aa1b456bda1ceda9c600ca684c02981b2),
[addonmanager_workers.UpdateAllWorker.status_message](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#a811622bfda2631ce55a0c13c47266ab2),
and
[addonmanager_workers.UpdateMetadataCacheWorker.store](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a085afc14523d65f4caccfab89a6c38d1).

Referenced by
[addonmanager_workers.UpdateMetadataCacheWorker.download_completed()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad08f2e5d64217721f3eca79acb8675da).

## ◆ run()

def addonmanager_workers.UpdateMetadataCacheWorker.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[addonmanager_workers.UpdateMetadataCacheWorker.download_completed()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad08f2e5d64217721f3eca79acb8675da),
[addonmanager_workers.UpdateMetadataCacheWorker.package_updated](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a9d7d4fb0041734afa4912aa71073d064),
[addonmanager_workers.CheckWorkbenchesForUpdatesWorker.repos](../../da/d66/classaddonmanager__workers_1_1CheckWorkbenchesForUpdatesWorker.html#abc6aace302f1831aff61160bdc0a1598),
[addonmanager_workers.CacheMacroCode.repos](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a81ad4bd417378a765cbcccfbb97414d5),
[addonmanager_workers.UpdateMetadataCacheWorker.repos](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aff0ed6b0b1ef66eb803ae66e02ae5b52),
[addonmanager_workers.UpdateAllWorker.repos](../../db/d3a/classaddonmanager__workers_1_1UpdateAllWorker.html#aee71f307e0b0a8115e94ad3ad0078054),
[package_list.PackageListItemModel.repos](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#af6a54ed385b515cda7e8a0ec23de9148),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.action_directive.requests,
[automotive_design.action_directive.requests](../../d1/d2d/classautomotive__design_1_1action__directive.html#a58b56b3d26b35f5241f2a0913d5f6e10),
[config_control_design.action_directive.requests](../../d8/d09/classconfig__control__design_1_1action__directive.html#a5f77e6c29cbc8ab6d129f848e70b7dcc),
[addonmanager_workers.UpdateMetadataCacheWorker.total_requests](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a5f79bad94ba483f073d41d4f2f4cb36e),
and
[addonmanager_workers.UpdateMetadataCacheWorker.updated_repos](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#aea6697fd4c535c12b0cb25bcfcc9a9a6).

Referenced by
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[femsolver.task.Task.protector()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a913c60a87594a8bfe76580d27effcb51).

## Member Data Documentation

## ◆ package_updated

| addonmanager_workers.UpdateMetadataCacheWorker.package_updated =
QtCore.Signal([Addon](../../d8/d91/classAddon_1_1Addon.html))  
---  
static  
  
Referenced by
[addonmanager_workers.UpdateMetadataCacheWorker.run()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a2ee7c2d005efedad23a0a5e4a6c202cb).

## ◆ progress_made

| addonmanager_workers.UpdateMetadataCacheWorker.progress_made =
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

addonmanager_workers.UpdateMetadataCacheWorker.repos  
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

## ◆ requests_completed

addonmanager_workers.UpdateMetadataCacheWorker.requests_completed  
---  
  
Referenced by
[addonmanager_workers.UpdateMetadataCacheWorker.download_completed()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad08f2e5d64217721f3eca79acb8675da).

## ◆ status_message

| addonmanager_workers.UpdateMetadataCacheWorker.status_message =
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

## ◆ store

addonmanager_workers.UpdateMetadataCacheWorker.store  
---  
  
Referenced by
[addonmanager_workers.UpdateMetadataCacheWorker.process_metadata_txt()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a921a85ca0055b090e171a8a9d2b0d7a9),
[addonmanager_workers.UpdateMetadataCacheWorker.process_package_xml()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad05f76bd86f0e2ad319c5b65ec4ce242),
and
[addonmanager_workers.UpdateMetadataCacheWorker.process_requirements_txt()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a1f5b401874bff312cf4979ab5031ec74).

## ◆ total_requests

addonmanager_workers.UpdateMetadataCacheWorker.total_requests  
---  
  
Referenced by
[addonmanager_workers.UpdateMetadataCacheWorker.download_completed()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad08f2e5d64217721f3eca79acb8675da),
[addonmanager_workers.UpdateMetadataCacheWorker.process_package_xml()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad05f76bd86f0e2ad319c5b65ec4ce242),
and
[addonmanager_workers.UpdateMetadataCacheWorker.run()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a2ee7c2d005efedad23a0a5e4a6c202cb).

## ◆ updated_repos

addonmanager_workers.UpdateMetadataCacheWorker.updated_repos  
---  
  
Referenced by
[addonmanager_workers.UpdateMetadataCacheWorker.download_completed()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#ad08f2e5d64217721f3eca79acb8675da),
and
[addonmanager_workers.UpdateMetadataCacheWorker.run()](../../d5/d0f/classaddonmanager__workers_1_1UpdateMetadataCacheWorker.html#a2ee7c2d005efedad23a0a5e4a6c202cb).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/addonmanager_workers.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

