---
url: https://freecad.github.io/SourceDoc/d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html
scraped_at: 2025-09-08T15:19:03.536743
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [change_branch](../../dc/d9f/namespacechange__branch.html)
  * [ChangeBranchDialogModel](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html)

[List of all members](../../da/d15/classchange__branch_1_1ChangeBranchDialogModel-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

change_branch.ChangeBranchDialogModel Class Reference

##  Public Member Functions  
  
---  
[int](../../d1/da0/classint.html) | [columnCount](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#ab78fc27e11ca1ecb6010729eaf6fe1e0) (self, QtCore.QModelIndex parent=QtCore.QModelIndex())  
def | [data](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#aeb42e63ba760cbcdaa58d35d89299e0c) (self, QtCore.QModelIndex index, [int](../../d1/da0/classint.html) role=QtCore.Qt.DisplayRole)  
def | [headerData](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a074faaf1f410c617a325d41e9daab535) (self, [int](../../d1/da0/classint.html) section, QtCore.Qt.Orientation orientation, [int](../../d1/da0/classint.html) role=QtCore.Qt.DisplayRole)  
[int](../../d1/da0/classint.html) | [rowCount](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a7aec0b6fe78cd161c1d2835dd8a122cc) (self, QtCore.QModelIndex parent=QtCore.QModelIndex())  
  
##  Public Attributes  
  
---  
|
[refs](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a201ccf5e8a8e0e1f2be5ae46f347b3d3)  
|
[repo](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a9a5e684f9b7257f172747a8e1821e4d4)  
  
##  Static Public Attributes  
  
---  
|
[DataSortRole](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a722ac26d3370c5fbfdcdca630e1d6bcf)
= QtCore.Qt.UserRole  
list | [display_data](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#af8be1fe10ce4785a1d8836a3f362035f) = []  
[int](../../d1/da0/classint.html) | [RefAccessRole](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#af621549f79942f52461484a8e99a67ab) = QtCore.Qt.UserRole + 1  
list | [refs](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a54d87cdb87d22184e0acec7834f62c10) = []  
  
## Member Function Documentation

## ◆ columnCount()

[int](../../d1/da0/classint.html) change_branch.ChangeBranchDialogModel.columnCount  | ( |  | _self_ ,   
---|---|---|---  
|  | QtCore.QModelIndex  | _parent_ = `QtCore.QModelIndex()`  
| ) | |   
  
## ◆ data()

def change_branch.ChangeBranchDialogModel.data  | ( |  | _self_ ,   
---|---|---|---  
|  | QtCore.QModelIndex  | _index_ ,   
|  | [int](../../d1/da0/classint.html) | _role_ = `QtCore.Qt.DisplayRole`  
| ) | |   
  
References
[change_branch.ChangeBranchDialogModel.display_data](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#af8be1fe10ce4785a1d8836a3f362035f),
[change_branch.ChangeBranchDialogModel.refs](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a54d87cdb87d22184e0acec7834f62c10),
importIFClegacy._tempEntityHolder.refs,
[draftguitools.gui_scale.Scale.refs](../../d5/d4f/classdraftguitools_1_1gui__scale_1_1Scale.html#a17936d756efbfbf0665ba1854bcfe94b),
[Simplify.refs](../../de/df0/classSimplify.html#a923b3fc89b61175cbf8b29e227379687),
[addonmanager_workers.CheckSingleUpdateWorker.repo](../../dd/dc7/classaddonmanager__workers_1_1CheckSingleUpdateWorker.html#ae50f5edf0ada57f45653579ce2f728d1),
[addonmanager_workers.InstallWorkbenchWorker.repo](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#adb740b7501c2d9833372b11aa4338608),
[change_branch.ChangeBranchDialogModel.repo](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a9a5e684f9b7257f172747a8e1821e4d4),
[package_details.PackageDetails.repo](../../d1/df5/classpackage__details_1_1PackageDetails.html#af636079625de5fa04f2543585b07181a),
and
[DraftVecUtils.toString()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf4889ceb585ea38ecf58d3f2af95b39a).

Referenced by
[Mod.Show.mTempoVis.TempoVis.activateWorkbench()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#aa6458989a197d280b7ac79b953caf670),
[Mod.Show.SceneDetail.SceneDetail.apply_data()](../../d6/d7f/classMod_1_1Show_1_1SceneDetail_1_1SceneDetail.html#a425bb9029228f555ead1f14a93504189),
[importIFClegacy.IfcSchema.capitalize()](../../df/d35/classimportIFClegacy_1_1IfcSchema.html#aeb13a8b2744f056b1605a77dce2baf28),
[Mod.Show.mTempoVis.TempoVis.forget()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a389e177f56526fc11a2369f3a8abcca6),
[Mod.Show.mTempoVis.TempoVis.forgetDetail()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#adaf62ce827a9e878daf496f2d52f4c6d),
[Mod.Show.mTempoVis.TempoVis.has()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a322395e1dec7c78badbb7c66ed4a5ab0),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[importIFClegacy.IfcSchema.readEntities()](../../df/d35/classimportIFClegacy_1_1IfcSchema.html#a94b733b95fdc448d0497e175ed0218ba),
[importIFClegacy.IfcSchema.readTypes()](../../df/d35/classimportIFClegacy_1_1IfcSchema.html#af47d35a40d9db8da941bcf1b08b4d2fb),
[Mod.Show.mTempoVis.TempoVis.restore()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a5f7f273cfe6cf3c62f94bdc51d4004d4),
[Mod.Show.mTempoVis.TempoVis.save()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#ac8d2e5cafacbdcfcdea24c6ba6ac747a),
[Mod.Show.mTempoVis.TempoVis.stored_val()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#acdf29a5e17807170cfbe87ef55bed82a),
[FeaturePython.ViewProviderOctahedron.updateData()](../../dc/d32/classFeaturePython_1_1ViewProviderOctahedron.html#a8fa8c308e725ac02c99adc604bc6c1f3),
and
[Dice3DS.dom3ds.UndefinedChunk.write()](../../d2/d34/classDice3DS_1_1dom3ds_1_1UndefinedChunk.html#acbb6e48136459a4387788be62b8ab5d7).

## ◆ headerData()

def change_branch.ChangeBranchDialogModel.headerData  | ( |  | _self_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _section_ ,   
|  | QtCore.Qt.Orientation  | _orientation_ ,   
|  | [int](../../d1/da0/classint.html) | _role_ = `QtCore.Qt.DisplayRole`  
| ) | |   
  
## ◆ rowCount()

[int](../../d1/da0/classint.html) change_branch.ChangeBranchDialogModel.rowCount  | ( |  | _self_ ,   
---|---|---|---  
|  | QtCore.QModelIndex  | _parent_ = `QtCore.QModelIndex()`  
| ) | |   
  
References
[change_branch.ChangeBranchDialogModel.refs](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a54d87cdb87d22184e0acec7834f62c10),
importIFClegacy._tempEntityHolder.refs,
[draftguitools.gui_scale.Scale.refs](../../d5/d4f/classdraftguitools_1_1gui__scale_1_1Scale.html#a17936d756efbfbf0665ba1854bcfe94b),
and
[Simplify.refs](../../de/df0/classSimplify.html#a923b3fc89b61175cbf8b29e227379687).

Referenced by
[package_list.PackageListItemModel.append_item()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#ae6ca870990288c91a44d79f370a6b00a),
and
[package_list.PackageListItemModel.clear()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#a1cb97185b8c8640a9bf5377338ef811f).

## Member Data Documentation

## ◆ DataSortRole

| change_branch.ChangeBranchDialogModel.DataSortRole = QtCore.Qt.UserRole  
---  
static  
  
## ◆ display_data

| list change_branch.ChangeBranchDialogModel.display_data = []  
---  
static  
  
Referenced by
[change_branch.ChangeBranchDialogModel.data()](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#aeb42e63ba760cbcdaa58d35d89299e0c).

## ◆ RefAccessRole

| [int](../../d1/da0/classint.html)
change_branch.ChangeBranchDialogModel.RefAccessRole = QtCore.Qt.UserRole + 1  
---  
static  
  
## ◆ refs [1/2]

| list change_branch.ChangeBranchDialogModel.refs = []  
---  
static  
  
Referenced by
[change_branch.ChangeBranchDialogModel.data()](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#aeb42e63ba760cbcdaa58d35d89299e0c),
and
[change_branch.ChangeBranchDialogModel.rowCount()](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a7aec0b6fe78cd161c1d2835dd8a122cc).

## ◆ refs [2/2]

change_branch.ChangeBranchDialogModel.refs  
---  
  
Referenced by
[change_branch.ChangeBranchDialogModel.data()](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#aeb42e63ba760cbcdaa58d35d89299e0c),
and
[change_branch.ChangeBranchDialogModel.rowCount()](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#a7aec0b6fe78cd161c1d2835dd8a122cc).

## ◆ repo

change_branch.ChangeBranchDialogModel.repo  
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

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/change_branch.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

