---
url: https://freecad.github.io/SourceDoc/d3/d48/classAddonManager_1_1CommandAddonManager.html
scraped_at: 2025-09-08T14:52:55.169460
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [AddonManager](../../da/d1f/namespaceAddonManager.html)
  * [CommandAddonManager](../../d3/d48/classAddonManager_1_1CommandAddonManager.html)

[List of all members](../../d6/d67/classAddonManager_1_1CommandAddonManager-members.html) | Classes | Public Member Functions | Public Attributes | Static Public Attributes

AddonManager.CommandAddonManager Class Reference

##  Classes  
  
---  
class | [MissingDependencies](../../d8/dca/classAddonManager_1_1CommandAddonManager_1_1MissingDependencies.html)  
  
##  Public Member Functions  
  
---  
None | [activate_table_widgets](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aeb8df4878a5a24da5fe675be652c4778) (self)  
None | [Activated](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad7c611053497eaa621def6c5d923a159) (self)  
None | [add_addon_repo](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a0128d399282eb71e55417bf8ef4ec946) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) addon_repo)  
None | [append_to_repos_list](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a34106546e723a43de9e286223474904e) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
def | [cache_macro](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#acb3085995e350d60c43165c96d8783f0) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
def | [cache_package](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa0dce945020f3abc615a5b77bf44803e) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [cancel_dependency_installation](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5dc57756d95f8932602cd2745d15ff1) (self)  
def | [cancel_network_check](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af078842263c7b1297a3355d504d15aa1) (self, button)  
None | [check_updates](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6fcf66f208db8991362e236fe9c2e4b5) (self)  
None | [cleanup_workers](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d86001908bd07941d546db0e6463065) (self, wait=False)  
None | [dependency_dialog_ignore_clicked](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a4ed7647e25da6eceedb37636d1008264) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [dependency_dialog_yes_clicked](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a24130c49cbb70c64796e0327923b9396) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [dependency_installation_failure](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa52493ff30557ea04b4000c33243abac) (self, [str](../../d9/d36/classstr.html) short_message, [str](../../d9/d36/classstr.html) details)  
None | [determine_cache_update_status](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a654998e0b8406348918e12bb0d7ebabf) (self)  
None | [display_dep_resolution_dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1d877a2b1be0ca6fe9f7d03529d62e81) (self, missing, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [do_next_startup_phase](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b) (self)  
None | [enable_updates](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afbe900e4d7a33a684336a1e4ba2910f9) (self, [int](../../d1/da0/classint.html) number_of_updates)  
None | [executemacro](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa9a71a1815f63568b938dd0ec14dc2be) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [force_check_updates](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a59ef1319a65cb46f3dab02bb23a7158d) (self, standalone=False)  
[str](../../d9/d36/classstr.html) | [get_cache_file_name](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac3080230c1760668c7bb2f73f20c8b02) (self, [str](../../d9/d36/classstr.html) file)  
QtGui.QIcon | [get_icon](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af26c090829a2aed899ae8280e559ec20) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo, [bool](../../d9/db9/classbool.html) [update](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a9fb1423755e16ebc88ece93f8c1a3a9a)=False)  
Dict[[str](../../d9/d36/classstr.html), [str](../../d9/d36/classstr.html)] | [GetResources](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a12df7e1fc23eb4a786a7887f32932fb5) (self)  
[bool](../../d9/db9/classbool.html) | [handle_disallowed_python](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a98d4404b8f0a7b16cff129ea4e65c8f4) (self, List[[str](../../d9/d36/classstr.html)] python_required)  
None | [hide_progress_widgets](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5aa671118056f1c4e1b25468c63a02e) (self)  
None | [install](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7844bcb2c34932d39cf0f18ebc9cedfc) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [launch](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af470a4ccce430d6fad97169583b688db) (self)  
None | [load_macro_metadata](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2507d2bb48755c69af59d525493adf1a) (self)  
None | [mark_repo_update_available](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a670656464d505dcab469a2f1bd7de259) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo, [bool](../../d9/db9/classbool.html) available)  
None | [network_connection_failed](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a188cb85c67487f14a33a9835660d25fa) (self, [str](../../d9/d36/classstr.html) message)  
None | [no_pip](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abe9fbe57e535559f53434676040a0f80) (self, [str](../../d9/d36/classstr.html) command, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [no_python_exe](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a02ecc07f773ae69b309435ae5df313f7) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [on_buttonBack_clicked](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afb6e3f578cb11b910660d85fadebf680) (self)  
None | [on_buttonUpdateCache_clicked](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa49366f509bb5b61e1d518f286f05adf) (self)  
None | [on_installation_failed](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac8cf465e055e3880d958923bcf98f094) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) _, [str](../../d9/d36/classstr.html) message)  
None | [on_package_installed](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo, [str](../../d9/d36/classstr.html) message)  
None | [on_package_updated](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae31bf139686923b617a182aeb1588425) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [on_update_all_completed](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982) (self)  
None | [populate_macros](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a94671ecd8a490dd469f52823a2abe9ba) (self)  
None | [populate_packages_table](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#adcc9afd53c106b8a724792bf17943fe3) (self)  
None | [reject](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca) (self)  
None | [remove](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [remove_readonly](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7fa7eb4d9cf67befc603bb70735c4329) (self, func, path, _)  
[bool](../../d9/db9/classbool.html) | [report_missing_workbenches](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a90d0c6b99bc0b3a71e3f98d69c6dc3b2) (self, [str](../../d9/d36/classstr.html) addon_name, wbs)  
None | [resolve_dependencies](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a61c2eb1ed8627176ccd7b098754dbb18) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [select_addon](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa632e875b2d90517423d4e47fa60a263) (self, [str](../../d9/d36/classstr.html) name)  
def | [show_connection_check_message](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a45ab69ddffce3263be237d5bd32c087e) (self)  
None | [show_information](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa2f17e60211c4a2e322e8801da6ff052) (self, [str](../../d9/d36/classstr.html) message)  
None | [show_progress_widgets](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af9df8398a3a7418385e7368fe10f6fe0) (self)  
None | [show_workbench](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a29da4a500ceeef891d623aeb0d1dbd2d) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [startup](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e) (self)  
None | [status_updated](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a34e713179c4b82c43c5228dcc3a5edab) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [stop_update](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a625e178c0cc51da55bfb3c7b93595000) (self)  
None | [table_row_activated](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad3f15ade8b0e8128d0807d6bd3800422) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) selected_repo)  
None | [update](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a9fb1423755e16ebc88ece93f8c1a3a9a) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) repo)  
None | [update_all](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8aefdf5b187b70350fbba8cf16f05c67) (self)  
None | [update_allowed_packages_list](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8ecd6c71a00d65219a51c1e348da1c48) (self)  
None | [update_check_complete](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad6f86c6ddb56f3acd0d7b6985c49e936) (self)  
None | [update_metadata_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aadd646ff8e8567949cd480b3b372c2e2) (self)  
None | [update_progress_bar](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a552bbbcaaddfd7c7a3b3c15b1c3235b3) (self, [int](../../d1/da0/classint.html) current_value, [int](../../d1/da0/classint.html) max_value)  
def | [validate](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3b5bdb4d937ff0f22e82fa180bb5ed2e) (self)  
def | [validate_package_xml](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a86159438c92359a47c0532b554c7a8fc) (self, [Addon](../../d8/d91/classAddon_1_1Addon.html) addon)  
List[[str](../../d9/d36/classstr.html)] | [validate_preference_pack_metadata](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab9f81005fc4fc5b5d053223ca14871be) (self, pack)  
List[[str](../../d9/d36/classstr.html)] | [validate_workbench_metadata](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a44675a97a3097fead4243eb01c13c2be) (self, workbench)  
None | [write_cache_stopfile](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a410f21935724a5523f58f7251665452e) (self)  
def | [write_macro_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a5f956f75f80aa2563d2c8bd114387e90) (self)  
def | [write_package_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#add9dfb8ffaeab53db5705aced8b74650) (self)  
  
##  Public Attributes  
  
---  
|
[allowed_packages](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad2a1d62812ae163770f31755e88cdc3b)  
|
[check_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a621838b8ffa429829b3d11dcb7149184)  
|
[connection_check_message](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad821e69a9b47a037c91d78c23ded47d1)  
|
[connection_checker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae09263d357722d8a1446e5641a9b70dd)  
|
[connection_message_timer](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a70410ac8f20b7f4118fc20fd5168aba4)  
|
[current_progress_region](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aefdfbb84ab79c69c64b9304c1175c9a6)  
|
[dependency_dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa4ee8a66041afb43e09a60343546e229)  
|
[dependency_installation_dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a27aaa595bb20682d14e670ac21dfd243)  
|
[dependency_installation_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a18d31847caef0ea220c1ac9548c726c1)  
|
[dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071)  
|
[install_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#acdd1fe66e2d3ea3689894520a2c40b3e)  
|
[item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71)  
|
[load_macro_metadata_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae0e666a1f038aa9b3eecaf351e866e6f)  
|
[macro_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a157471c3fb9935d0f067e3141a328cc3)  
|
[macro_repo_dir](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2d7a3b0cb550143d424032b3dc50844f)  
|
[macro_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7571fe89c418f658bf959d3993133598)  
|
[number_of_progress_regions](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a57dd7b86672718dbe0efeaeec5cee2e8)  
|
[package_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#adca5d3afe751aea3551e876f1e252bb4)  
|
[packageDetails](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a679d03e5007b7af469f33747cdf775b1)  
|
[packageList](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad8169fc92c91c669b9d8ab582dc7acfb)  
|
[packages_with_updates](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d88c6553e005f63afc1a273124f84f5)  
|
[restart_required](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a57d044ba187262004cf918372b305144)  
|
[startup_sequence](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a168ce09c7258aa2886497388ddd52b42)  
|
[subupdates_failed](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae2f0fce91d3f9cd8f53096884ba1d05e)  
|
[subupdates_succeeded](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a0b4437389a5959910c21ad57170ad54e)  
|
[trigger_recache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a698ebaa80979342fd3244c76fe20b5c6)  
|
[update_all_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a767f2572a102ecf48666ba4a4672bcf9)  
|
[update_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab9b23f9a93121e99fe07a1b33e555144)  
|
[update_metadata_cache_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2d89b57e2888643813485ecf9199b0e0)  
|
[update_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a94abb7e67b3be6eda938add023afa064)  
  
##  Static Public Attributes  
  
---  
|
[lock](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad17bd5b7265a48f723442507a0ab640f)
= threading.Lock()  
[bool](../../d9/db9/classbool.html) | [restart_required](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2a4426eba4e6ecd1b6baf3e61403e99b) = False  
list | [workers](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3414e0cc98f96ec31b3a7073b3be08e1)  
  
## Detailed Description

    
    
    The main Addon Manager class and FreeCAD command

## Member Function Documentation

## ◆ activate_table_widgets()

None AddonManager.CommandAddonManager.activate_table_widgets  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
and
[AddonManager.CommandAddonManager.packageList](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad8169fc92c91c669b9d8ab582dc7acfb).

Referenced by
[AddonManager.CommandAddonManager.startup()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e).

## ◆ Activated()

None AddonManager.CommandAddonManager.Activated  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftguitools.gui_arcs.Arc.finish()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a2262d966a879bfa9b71d9c699e6929b2),
[draftguitools.gui_beziers.BezCurve.finish()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a6b4598d09cb7c1f0b06fe1b96cc9096f),
[draftguitools.gui_beziers.CubicBezCurve.finish()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#abadcbdae43b1e54d516d249c71fc0991),
[draftguitools.gui_ellipses.Ellipse.finish()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#aa534628f13f8ad6effacb1fcbd76bb2a),
[draftguitools.gui_lines.Line.finish()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#a622af4e1166f892f860b86d3d1e3f053),
[draftguitools.gui_mirror.Mirror.finish()](../../d8/dbd/classdraftguitools_1_1gui__mirror_1_1Mirror.html#a73d8f0dba4d186590485bf972fa8e25d),
[draftguitools.gui_move.Move.finish()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#aa2c8c371106351f316c238f67bf7accf),
[draftguitools.gui_polygons.Polygon.finish()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a06317245940b6d99d62b0823d657dcb2),
[draftguitools.gui_rectangles.Rectangle.finish()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a7ba174f4093affb5af55e58c804a527d),
[draftguitools.gui_rotate.Rotate.finish()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#ad60faae5b86f1d2c74f045c2291ae6dd),
[draftguitools.gui_splines.BSpline.finish()](../../d1/d3f/classdraftguitools_1_1gui__splines_1_1BSpline.html#ab00ba1111a2b9d2afcee43a0396a4cd5),
[draftguitools.gui_texts.Text.finish()](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a3fe64be64c77319af1f265609dd8e985),
[draftguitools.gui_points.Point.finish()](../../d7/dc7/classdraftguitools_1_1gui__points_1_1Point.html#ac55499c15db7b01680f41b3f3dd32477),
[draftguitools.gui_shapestrings.ShapeString.finish()](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#af7a14bf7135177bc521cfa7a9123b2bf),
[draftguitools.gui_arcs.Arc_3Points.getPoint()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#addd65326b504c7bf765526ef2db14321),
and
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb).

## ◆ add_addon_repo()

None AddonManager.CommandAddonManager.add_addon_repo  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _addon_repo_  
| ) | |   
      
    
    adds a workbench to the list

References
[AddonManager.CommandAddonManager.get_icon()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af26c090829a2aed899ae8280e559ec20),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
and
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4).

## ◆ append_to_repos_list()

None AddonManager.CommandAddonManager.append_to_repos_list  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
      
    
    this function allows threads to update the main list of workbenches

References
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
and
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4).

## ◆ cache_macro()

def AddonManager.CommandAddonManager.cache_macro  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
Referenced by
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca).

## ◆ cache_package()

def AddonManager.CommandAddonManager.cache_package  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
Referenced by
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca).

## ◆ cancel_dependency_installation()

None AddonManager.CommandAddonManager.cancel_dependency_installation  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.dependency_installation_dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a27aaa595bb20682d14e670ac21dfd243),
and
[AddonManager.CommandAddonManager.dependency_installation_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a18d31847caef0ea220c1ac9548c726c1).

## ◆ cancel_network_check()

def AddonManager.CommandAddonManager.cancel_network_check  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _button_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.connection_check_message](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad821e69a9b47a037c91d78c23ded47d1),
[AddonManager.CommandAddonManager.connection_checker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae09263d357722d8a1446e5641a9b70dd),
[AddonManager.CommandAddonManager.launch()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af470a4ccce430d6fad97169583b688db),
and
[AddonManager.CommandAddonManager.network_connection_failed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a188cb85c67487f14a33a9835660d25fa).

## ◆ check_updates()

None AddonManager.CommandAddonManager.check_updates  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
[AddonManager.CommandAddonManager.force_check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a59ef1319a65cb46f3dab02bb23a7158d),
and
[AddonManager.CommandAddonManager.packages_with_updates](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d88c6553e005f63afc1a273124f84f5).

Referenced by
[AddonManager.CommandAddonManager.on_buttonUpdateCache_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa49366f509bb5b61e1d518f286f05adf),
and
[AddonManager.CommandAddonManager.startup()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e).

## ◆ cleanup_workers()

None AddonManager.CommandAddonManager.cleanup_workers  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _wait_ = `False`  
| ) | |   
      
    
    Ensure that no workers are running by explicitly asking them to stop and waiting for them until they do

References
[AddonManager.CommandAddonManager.workers](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3414e0cc98f96ec31b3a7073b3be08e1),
and
[addonmanager_workers.CacheMacroCode.workers](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a817e3c52e14b2cee3da87afdd37e718b).

Referenced by
[AddonManager.CommandAddonManager.stop_update()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a625e178c0cc51da55bfb3c7b93595000).

## ◆ dependency_dialog_ignore_clicked()

None AddonManager.CommandAddonManager.dependency_dialog_ignore_clicked  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.install()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7844bcb2c34932d39cf0f18ebc9cedfc),
[addonmanager_macro.Macro.install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
and
[package_details.PackageDetails.install](../../d1/df5/classpackage__details_1_1PackageDetails.html#a1cce00da958c9512788747c7ed968b87).

## ◆ dependency_dialog_yes_clicked()

None AddonManager.CommandAddonManager.dependency_dialog_yes_clicked  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.dependency_dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa4ee8a66041afb43e09a60343546e229),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
and
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4).

## ◆ dependency_installation_failure()

None AddonManager.CommandAddonManager.dependency_installation_failure  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _short_message_ ,   
|  | [str](../../d9/d36/classstr.html) | _details_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.dependency_installation_dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a27aaa595bb20682d14e670ac21dfd243),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
and
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3).

## ◆ determine_cache_update_status()

None AddonManager.CommandAddonManager.determine_cache_update_status  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Determine whether we need to update the cache, based on user preference, and previous
    cache update status. Sets self.update_cache to either True or False.

References
[AddonManager.CommandAddonManager.update_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab9b23f9a93121e99fe07a1b33e555144).

## ◆ display_dep_resolution_dialog()

None AddonManager.CommandAddonManager.display_dep_resolution_dialog  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _missing_ ,   
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
Referenced by
[AddonManager.CommandAddonManager.resolve_dependencies()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a61c2eb1ed8627176ccd7b098754dbb18).

## ◆ do_next_startup_phase()

None AddonManager.CommandAddonManager.do_next_startup_phase  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Pop the top item in self.startup_sequence off the list and run it

References
[AddonManager.CommandAddonManager.current_progress_region](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aefdfbb84ab79c69c64b9304c1175c9a6),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.hide_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5aa671118056f1c4e1b25468c63a02e),
[AddonManager.CommandAddonManager.packageList](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad8169fc92c91c669b9d8ab582dc7acfb),
[AddonManager.CommandAddonManager.startup_sequence](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a168ce09c7258aa2886497388ddd52b42),
and
[AddonManager.CommandAddonManager.update_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab9b23f9a93121e99fe07a1b33e555144).

Referenced by
[AddonManager.CommandAddonManager.activate_table_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aeb8df4878a5a24da5fe675be652c4778),
[AddonManager.CommandAddonManager.check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6fcf66f208db8991362e236fe9c2e4b5),
[AddonManager.CommandAddonManager.force_check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a59ef1319a65cb46f3dab02bb23a7158d),
[AddonManager.CommandAddonManager.select_addon()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa632e875b2d90517423d4e47fa60a263),
and
[AddonManager.CommandAddonManager.validate()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3b5bdb4d937ff0f22e82fa180bb5ed2e).

## ◆ enable_updates()

None AddonManager.CommandAddonManager.enable_updates  | ( |  | _self_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _number_of_updates_  
| ) | |   
      
    
    enables the update button

References
[AddonManager.CommandAddonManager.check_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a621838b8ffa429829b3d11dcb7149184),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
and
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3).

Referenced by
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982),
[AddonManager.CommandAddonManager.status_updated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a34e713179c4b82c43c5228dcc3a5edab),
and
[AddonManager.CommandAddonManager.update_check_complete()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad6f86c6ddb56f3acd0d7b6985c49e936).

## ◆ executemacro()

None AddonManager.CommandAddonManager.executemacro  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
      
    
    executes a selected macro

References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.macro_repo_dir](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2d7a3b0cb550143d424032b3dc50844f),
and
[AddonManager.CommandAddonManager.on_installation_failed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac8cf465e055e3880d958923bcf98f094).

## ◆ force_check_updates()

None AddonManager.CommandAddonManager.force_check_updates  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _standalone_ = `False`  
| ) | |   
  
References
[AddonManager.CommandAddonManager.check_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a621838b8ffa429829b3d11dcb7149184),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
and
[AddonManager.CommandAddonManager.packages_with_updates](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d88c6553e005f63afc1a273124f84f5).

Referenced by
[AddonManager.CommandAddonManager.check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6fcf66f208db8991362e236fe9c2e4b5),
and
[AddonManager.CommandAddonManager.on_buttonUpdateCache_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa49366f509bb5b61e1d518f286f05adf).

## ◆ get_cache_file_name()

[str](../../d9/d36/classstr.html) AddonManager.CommandAddonManager.get_cache_file_name  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _file_  
| ) | |   
  
Referenced by
[AddonManager.CommandAddonManager.populate_macros()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a94671ecd8a490dd469f52823a2abe9ba),
[AddonManager.CommandAddonManager.populate_packages_table()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#adcc9afd53c106b8a724792bf17943fe3),
[AddonManager.CommandAddonManager.write_cache_stopfile()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a410f21935724a5523f58f7251665452e),
[AddonManager.CommandAddonManager.write_macro_cache()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a5f956f75f80aa2563d2c8bd114387e90),
and
[AddonManager.CommandAddonManager.write_package_cache()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#add9dfb8ffaeab53db5705aced8b74650).

## ◆ get_icon()

QtGui.QIcon AddonManager.CommandAddonManager.get_icon  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_ ,   
|  | [bool](../../d9/db9/classbool.html) | _update_ = `False`  
| ) | |   
      
    
    Returns an icon for an Addon. Uses a cached icon if possible, unless update is True,
    in which case the icon is regenerated.

Referenced by
[AddonManager.CommandAddonManager.add_addon_repo()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a0128d399282eb71e55417bf8ef4ec946),
and
[AddonManager.CommandAddonManager.on_package_updated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae31bf139686923b617a182aeb1588425).

## ◆ GetResources()

Dict[[str](../../d9/d36/classstr.html), [str](../../d9/d36/classstr.html)] AddonManager.CommandAddonManager.GetResources  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.QT_TRANSLATE_NOOP()](../../da/d1f/namespaceAddonManager.html#a8e5e2346c4a1edb4f9eb075c63d92eb4).

## ◆ handle_disallowed_python()

[bool](../../d9/db9/classbool.html) AddonManager.CommandAddonManager.handle_disallowed_python  | ( |  | _self_ ,   
---|---|---|---  
|  | List[[str](../../d9/d36/classstr.html)]  | _python_required_  
| ) | |   
      
    
    Determine if we are missing any required Python packages that are not in the allowed
    packages list. If so, display a message to the user, and return True. Otherwise return
    False.

References
[AddonManager.CommandAddonManager.allowed_packages](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad2a1d62812ae163770f31755e88cdc3b),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
and
[AddonManager.CommandAddonManager.update_allowed_packages_list()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8ecd6c71a00d65219a51c1e348da1c48).

Referenced by
[AddonManager.CommandAddonManager.resolve_dependencies()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a61c2eb1ed8627176ccd7b098754dbb18).

## ◆ hide_progress_widgets()

None AddonManager.CommandAddonManager.hide_progress_widgets  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    hides the progress bar and related widgets

References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
and
[AddonManager.CommandAddonManager.packageList](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad8169fc92c91c669b9d8ab582dc7acfb).

Referenced by
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
[AddonManager.CommandAddonManager.on_installation_failed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac8cf465e055e3880d958923bcf98f094),
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982),
and
[AddonManager.CommandAddonManager.stop_update()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a625e178c0cc51da55bfb3c7b93595000).

## ◆ install()

None AddonManager.CommandAddonManager.install  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
      
    
    installs or updates a workbench, macro, or package

References
[AddonManager.CommandAddonManager.dependency_installation_dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a27aaa595bb20682d14e670ac21dfd243),
[AddonManager.CommandAddonManager.install_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#acdd1fe66e2d3ea3689894520a2c40b3e),
and
[AddonManager.CommandAddonManager.show_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af9df8398a3a7418385e7368fe10f6fe0).

Referenced by
[AddonManager.CommandAddonManager.dependency_dialog_ignore_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a4ed7647e25da6eceedb37636d1008264),
[AddonManager.CommandAddonManager.no_pip()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abe9fbe57e535559f53434676040a0f80),
[AddonManager.CommandAddonManager.no_python_exe()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a02ecc07f773ae69b309435ae5df313f7),
[AddonManager.CommandAddonManager.resolve_dependencies()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a61c2eb1ed8627176ccd7b098754dbb18),
and
[AddonManager.CommandAddonManager.update()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a9fb1423755e16ebc88ece93f8c1a3a9a).

## ◆ launch()

None AddonManager.CommandAddonManager.launch  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Shows the Addon Manager UI

Referenced by
[AddonManager.CommandAddonManager.cancel_network_check()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af078842263c7b1297a3355d504d15aa1).

## ◆ load_macro_metadata()

None AddonManager.CommandAddonManager.load_macro_metadata  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.update_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab9b23f9a93121e99fe07a1b33e555144).

Referenced by
[AddonManager.CommandAddonManager.startup()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e).

## ◆ mark_repo_update_available()

None AddonManager.CommandAddonManager.mark_repo_update_available  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_ ,   
|  | [bool](../../d9/db9/classbool.html) | _available_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
and
[AddonManager.CommandAddonManager.packageDetails](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a679d03e5007b7af469f33747cdf775b1).

## ◆ network_connection_failed()

None AddonManager.CommandAddonManager.network_connection_failed  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _message_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.connection_check_message](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad821e69a9b47a037c91d78c23ded47d1).

Referenced by
[AddonManager.CommandAddonManager.cancel_network_check()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af078842263c7b1297a3355d504d15aa1).

## ◆ no_pip()

None AddonManager.CommandAddonManager.no_pip  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _command_ ,   
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.dependency_installation_dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a27aaa595bb20682d14e670ac21dfd243),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.install()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7844bcb2c34932d39cf0f18ebc9cedfc),
[addonmanager_macro.Macro.install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
and
[package_details.PackageDetails.install](../../d1/df5/classpackage__details_1_1PackageDetails.html#a1cce00da958c9512788747c7ed968b87).

Referenced by
[addonmanager_workers.DependencyInstallationWorker.run()](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a1a9736210fa3ae7feb0c78df6452e181).

## ◆ no_python_exe()

None AddonManager.CommandAddonManager.no_python_exe  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.dependency_installation_dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a27aaa595bb20682d14e670ac21dfd243),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.install()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7844bcb2c34932d39cf0f18ebc9cedfc),
[addonmanager_macro.Macro.install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
and
[package_details.PackageDetails.install](../../d1/df5/classpackage__details_1_1PackageDetails.html#a1cce00da958c9512788747c7ed968b87).

Referenced by
[addonmanager_workers.DependencyInstallationWorker.run()](../../d1/dc5/classaddonmanager__workers_1_1DependencyInstallationWorker.html#a1a9736210fa3ae7feb0c78df6452e181).

## ◆ on_buttonBack_clicked()

None AddonManager.CommandAddonManager.on_buttonBack_clicked  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.packageDetails](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a679d03e5007b7af469f33747cdf775b1),
and
[AddonManager.CommandAddonManager.packageList](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad8169fc92c91c669b9d8ab582dc7acfb).

## ◆ on_buttonUpdateCache_clicked()

None AddonManager.CommandAddonManager.on_buttonUpdateCache_clicked  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6fcf66f208db8991362e236fe9c2e4b5),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.force_check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a59ef1319a65cb46f3dab02bb23a7158d),
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00),
[AddonManager.CommandAddonManager.remove_readonly()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7fa7eb4d9cf67befc603bb70735c4329),
[addonmanager_workers.FillMacroListWorker.remove_readonly()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#ae1c5e6e2ef2b52fa687320b20e1c240e),
[AddonManager.CommandAddonManager.startup()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e),
[AddonManager.CommandAddonManager.startup_sequence](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a168ce09c7258aa2886497388ddd52b42),
and
[AddonManager.CommandAddonManager.update_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab9b23f9a93121e99fe07a1b33e555144).

## ◆ on_installation_failed()

None AddonManager.CommandAddonManager.on_installation_failed  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | ___ ,   
|  | [str](../../d9/d36/classstr.html) | _message_  
| ) | |   
  
References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
and
[AddonManager.CommandAddonManager.hide_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5aa671118056f1c4e1b25468c63a02e).

Referenced by
[AddonManager.CommandAddonManager.executemacro()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa9a71a1815f63568b938dd0ec14dc2be).

## ◆ on_package_installed()

None AddonManager.CommandAddonManager.on_package_installed  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_ ,   
|  | [str](../../d9/d36/classstr.html) | _message_  
| ) | |   
  
References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.enable_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afbe900e4d7a33a684336a1e4ba2910f9),
[AddonManager.CommandAddonManager.hide_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5aa671118056f1c4e1b25468c63a02e),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
[AddonManager.CommandAddonManager.packageDetails](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a679d03e5007b7af469f33747cdf775b1),
[AddonManager.CommandAddonManager.packages_with_updates](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d88c6553e005f63afc1a273124f84f5),
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00),
and
[AddonManager.CommandAddonManager.restart_required](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2a4426eba4e6ecd1b6baf3e61403e99b).

## ◆ on_package_updated()

None AddonManager.CommandAddonManager.on_package_updated  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
      
    
    Called when the named package has either new metadata or a new icon (or both)

References
[AddonManager.CommandAddonManager.get_icon()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af26c090829a2aed899ae8280e559ec20),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
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

## ◆ on_update_all_completed()

None AddonManager.CommandAddonManager.on_update_all_completed  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.enable_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afbe900e4d7a33a684336a1e4ba2910f9),
[AddonManager.CommandAddonManager.hide_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5aa671118056f1c4e1b25468c63a02e),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
[AddonManager.CommandAddonManager.packages_with_updates](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d88c6553e005f63afc1a273124f84f5),
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00),
[AddonManager.CommandAddonManager.restart_required](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2a4426eba4e6ecd1b6baf3e61403e99b),
[AddonManager.CommandAddonManager.subupdates_failed](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae2f0fce91d3f9cd8f53096884ba1d05e),
and
[AddonManager.CommandAddonManager.subupdates_succeeded](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a0b4437389a5959910c21ad57170ad54e).

## ◆ populate_macros()

None AddonManager.CommandAddonManager.populate_macros  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.get_cache_file_name()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac3080230c1760668c7bb2f73f20c8b02),
and
[AddonManager.CommandAddonManager.update_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab9b23f9a93121e99fe07a1b33e555144).

Referenced by
[AddonManager.CommandAddonManager.startup()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e).

## ◆ populate_packages_table()

None AddonManager.CommandAddonManager.populate_packages_table  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.get_cache_file_name()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac3080230c1760668c7bb2f73f20c8b02),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
and
[AddonManager.CommandAddonManager.update_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab9b23f9a93121e99fe07a1b33e555144).

Referenced by
[AddonManager.CommandAddonManager.startup()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e).

## ◆ reject()

None AddonManager.CommandAddonManager.reject  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    called when the window has been closed

References
[AddonManager.CommandAddonManager.cache_macro()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#acb3085995e350d60c43165c96d8783f0),
[AddonManager.CommandAddonManager.cache_package()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa0dce945020f3abc615a5b77bf44803e),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
[AddonManager.CommandAddonManager.restart_required](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2a4426eba4e6ecd1b6baf3e61403e99b),
[AddonManager.CommandAddonManager.startup_sequence](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a168ce09c7258aa2886497388ddd52b42),
[AddonManager.CommandAddonManager.workers](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3414e0cc98f96ec31b3a7073b3be08e1),
[addonmanager_workers.CacheMacroCode.workers](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a817e3c52e14b2cee3da87afdd37e718b),
[AddonManager.CommandAddonManager.write_cache_stopfile()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a410f21935724a5523f58f7251665452e),
[AddonManager.CommandAddonManager.write_macro_cache()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a5f956f75f80aa2563d2c8bd114387e90),
and
[AddonManager.CommandAddonManager.write_package_cache()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#add9dfb8ffaeab53db5705aced8b74650).

Referenced by
[draftguitools.gui_hatch.Draft_Hatch_TaskPanel.accept()](../../d1/d6e/classdraftguitools_1_1gui__hatch_1_1Draft__Hatch__TaskPanel.html#a233bb1c01579f1e00acc06984efec11a),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel.accept()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#ae0e2ec6f40370c732beb919549a0111d),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanelCmd.accept()](../../df/d8e/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanelCmd.html#ac1562e837c0659251e16a2a5b7796cf2),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanelEdit.accept()](../../d7/da9/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanelEdit.html#a9201c29e738ab0b73095e222421cdfc3),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanel.action()](../../d9/d1e/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanel.html#aff179367fdb60160feb642c72ea17465),
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.toolEdit()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#ac20855be381c22621c17d3df63458595).

## ◆ remove()

None AddonManager.CommandAddonManager.remove  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
      
    
    uninstalls a macro or workbench

References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
[AddonManager.CommandAddonManager.packageDetails](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a679d03e5007b7af469f33747cdf775b1),
[AddonManager.CommandAddonManager.remove_readonly()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7fa7eb4d9cf67befc603bb70735c4329),
[addonmanager_workers.FillMacroListWorker.remove_readonly()](../../db/dd0/classaddonmanager__workers_1_1FillMacroListWorker.html#ae1c5e6e2ef2b52fa687320b20e1c240e),
and
[AddonManager.CommandAddonManager.restart_required](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2a4426eba4e6ecd1b6baf3e61403e99b).

Referenced by
[AddonManager.CommandAddonManager.on_buttonUpdateCache_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa49366f509bb5b61e1d518f286f05adf),
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
and
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982).

## ◆ remove_readonly()

None AddonManager.CommandAddonManager.remove_readonly  | ( |  | _self_ ,   
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

## ◆ report_missing_workbenches()

[bool](../../d9/db9/classbool.html) AddonManager.CommandAddonManager.report_missing_workbenches  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _addon_name_ ,   
|  |  | _wbs_  
| ) | |   
  
References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
and
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3).

Referenced by
[AddonManager.CommandAddonManager.resolve_dependencies()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a61c2eb1ed8627176ccd7b098754dbb18).

## ◆ resolve_dependencies()

None AddonManager.CommandAddonManager.resolve_dependencies  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.allowed_packages](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad2a1d62812ae163770f31755e88cdc3b),
[AddonManager.CommandAddonManager.display_dep_resolution_dialog()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1d877a2b1be0ca6fe9f7d03529d62e81),
[AddonManager.CommandAddonManager.handle_disallowed_python()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a98d4404b8f0a7b16cff129ea4e65c8f4),
[AddonManager.CommandAddonManager.install()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7844bcb2c34932d39cf0f18ebc9cedfc),
[addonmanager_macro.Macro.install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
[package_details.PackageDetails.install](../../d1/df5/classpackage__details_1_1PackageDetails.html#a1cce00da958c9512788747c7ed968b87),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
and
[AddonManager.CommandAddonManager.report_missing_workbenches()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a90d0c6b99bc0b3a71e3f98d69c6dc3b2).

## ◆ select_addon()

None AddonManager.CommandAddonManager.select_addon  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _name_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
and
[AddonManager.CommandAddonManager.table_row_activated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad3f15ade8b0e8128d0807d6bd3800422).

Referenced by
[AddonManager.CommandAddonManager.startup()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e).

## ◆ show_connection_check_message()

def AddonManager.CommandAddonManager.show_connection_check_message  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.connection_checker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae09263d357722d8a1446e5641a9b70dd).

## ◆ show_information()

None AddonManager.CommandAddonManager.show_information  | ( |  | _self_ ,   
---|---|---|---  
|  | [str](../../d9/d36/classstr.html) | _message_  
| ) | |   
      
    
    shows generic text in the information pane

References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
and
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3).

## ◆ show_progress_widgets()

None AddonManager.CommandAddonManager.show_progress_widgets  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
and
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3).

Referenced by
[AddonManager.CommandAddonManager.install()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7844bcb2c34932d39cf0f18ebc9cedfc),
and
[AddonManager.CommandAddonManager.update_progress_bar()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a552bbbcaaddfd7c7a3b3c15b1c3235b3).

## ◆ show_workbench()

None AddonManager.CommandAddonManager.show_workbench  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.packageDetails](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a679d03e5007b7af469f33747cdf775b1),
and
[AddonManager.CommandAddonManager.packageList](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad8169fc92c91c669b9d8ab582dc7acfb).

## ◆ startup()

None AddonManager.CommandAddonManager.startup  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Downloads the available packages listings and populates the table
    
    This proceeds in four stages: first, the main GitHub repository is queried for a list of possible
    addons. Each addon is specified as a git submodule with name and branch information. The actual specific
    commit ID of the submodule (as listed on Github) is ignored. Any extra repositories specified by the
    user are appended to this list.
    
    Second, the list of macros is downloaded from the FreeCAD/FreeCAD-macros repository and the wiki
    
    Third, each of these items is queried for a package.xml metadata file. If that file exists it is
    downloaded, cached, and any icons that it references are also downloaded and cached.
    
    Finally, for workbenches that are not contained within a package (e.g. they provide no metadata), an
    additional git query is made to see if an update is available. Macros are checked for file changes.
    
    Each of these stages is launched in a separate thread to ensure that the UI remains responsive, and
    the operation can be cancelled.
    
    Each stage is also subject to caching, so may return immediately, if no cache update has been requested.

References
[AddonManager.CommandAddonManager.activate_table_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aeb8df4878a5a24da5fe675be652c4778),
[AddonManager.CommandAddonManager.check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6fcf66f208db8991362e236fe9c2e4b5),
[AddonManager.CommandAddonManager.load_macro_metadata()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2507d2bb48755c69af59d525493adf1a),
[AddonManager.CommandAddonManager.populate_macros()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a94671ecd8a490dd469f52823a2abe9ba),
[AddonManager.CommandAddonManager.populate_packages_table()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#adcc9afd53c106b8a724792bf17943fe3),
[AddonManager.CommandAddonManager.select_addon()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa632e875b2d90517423d4e47fa60a263),
[AddonManager.CommandAddonManager.startup_sequence](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a168ce09c7258aa2886497388ddd52b42),
[AddonManager.CommandAddonManager.update_metadata_cache()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aadd646ff8e8567949cd480b3b372c2e2),
Py::Object.validate(),
[PartGui::DlgExtrusion.validate()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a9434547a26c67894da218387403f1c86),
[PartGui::DlgRevolution.validate()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a46d010b2d22c69a04bb9ede6a9d71c77),
Sandbox::DocumentProtector.validate(),
Sandbox::DocumentObjectProtector.validate(),
[Gui::UnsignedValidator.validate()](../../d9/d9a/classGui_1_1UnsignedValidator.html#a05cc88796f0e8737c11ead2d113f6847),
[Gui::QuantitySpinBoxPrivate.validate()](../../dd/d08/classGui_1_1QuantitySpinBoxPrivate.html#a3a7b86da24888398add92a65193c9b62),
[Gui::InputValidator.validate()](../../d7/d79/classGui_1_1InputValidator.html#a6bc8836891ab9d28983f2b533f1917cf),
[Gui::InputField.validate()](../../da/dfa/classGui_1_1InputField.html#a3ec8d78730daa4e16e809bcb2f3f4086),
[Gui::QuantitySpinBox.validate()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#a8f73a1bf385ec5c6103b72a36d310513),
[Gui::UIntSpinBox.validate()](../../d3/ded/classGui_1_1UIntSpinBox.html#ab76d61c4f0f025d8e3449928e40cc482),
and
[AddonManager.CommandAddonManager.validate()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3b5bdb4d937ff0f22e82fa180bb5ed2e).

Referenced by
[AddonManager.CommandAddonManager.on_buttonUpdateCache_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa49366f509bb5b61e1d518f286f05adf).

## ◆ status_updated()

None AddonManager.CommandAddonManager.status_updated  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.enable_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afbe900e4d7a33a684336a1e4ba2910f9),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
and
[AddonManager.CommandAddonManager.packages_with_updates](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d88c6553e005f63afc1a273124f84f5).

## ◆ stop_update()

None AddonManager.CommandAddonManager.stop_update  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.cleanup_workers()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d86001908bd07941d546db0e6463065),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.hide_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5aa671118056f1c4e1b25468c63a02e),
and
[AddonManager.CommandAddonManager.write_cache_stopfile()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a410f21935724a5523f58f7251665452e).

## ◆ table_row_activated()

None AddonManager.CommandAddonManager.table_row_activated  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _selected_repo_  
| ) | |   
      
    
    a row was activated, show the relevant data

References
[AddonManager.CommandAddonManager.packageDetails](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a679d03e5007b7af469f33747cdf775b1),
and
[AddonManager.CommandAddonManager.packageList](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad8169fc92c91c669b9d8ab582dc7acfb).

Referenced by
[AddonManager.CommandAddonManager.select_addon()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa632e875b2d90517423d4e47fa60a263).

## ◆ update()

None AddonManager.CommandAddonManager.update  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _repo_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.install()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7844bcb2c34932d39cf0f18ebc9cedfc),
[addonmanager_macro.Macro.install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
and
[package_details.PackageDetails.install](../../d1/df5/classpackage__details_1_1PackageDetails.html#a1cce00da958c9512788747c7ed968b87).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchAxisSystem.AxisSystemTaskPanel.addElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a68544065aac91fa78a8bddb3e6ed5a99),
[ArchComponent.ComponentTaskPanel.addElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a21a385085defc9e8ccca8b2261a57314),
[ArchSectionPlane.SectionPlaneTaskPanel.addElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a6317c0ca7eb0c28e60b863f96ddeb81f),
[DraftGui.FacebinderTaskPanel.addElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a7642fdc6d6fa90afec25930af3b0a66e),
[femtaskpanels.task_result_mechanical._TaskPanel.calculate()](../../d1/d11/classfemtaskpanels_1_1task__result__mechanical_1_1__TaskPanel.html#aa2b98b5a9e12d62038ea9cc00366ecb6),
[Spreadsheet_legacy.SpreadsheetView.changeCell()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a897cda21a4a4f34431c371a31579706e),
[draftguitools.gui_edit.Edit.endEditing()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#ab9797631ba43c7855016e2552c21834f),
[draftguitools.gui_trackers.boxTracker.height()](../../d5/dca/classdraftguitools_1_1gui__trackers_1_1boxTracker.html#a25f7d7bbd56b5ff5ef5da124e515dd00),
[draftguitools.gui_trackers.rectangleTracker.p3()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a1bf47cdde1ea165a58946f1a5fdc6c8e),
[Plot.Plot.plot()](../../d3/d54/classPlot_1_1Plot.html#a8b670f38324a7fae1c7128e117cba688),
[Spreadsheet_legacy.SpreadsheetView.recompute()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a1d8b8256ad183347aedaf40a269c2d3a),
[ArchAxisSystem.AxisSystemTaskPanel.removeElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a27e3fe8ffbc52acfd92f2d333626a76d),
[ArchComponent.ComponentTaskPanel.removeElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#ad9d18ffd3ef7556affab6b62a6acceb5),
[ArchSectionPlane.SectionPlaneTaskPanel.removeElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a544dbf3def03e06b86e6f32c390fd46a),
[DraftGui.FacebinderTaskPanel.removeElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a8ce5c644e81d1fbb3907e351e2050a0a),
[draftguitools.gui_trackers.gridTracker.reset()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a2c6f7e1d0a817adacef8297962691a9c),
[ArchNesting.Nester.run()](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102),
[draftguitools.gui_trackers.gridTracker.setMainlines()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#ac1c96a4a6282724211bc61a37ffa5a05),
[draftguitools.gui_trackers.gridTracker.setSize()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a6bb2d86a97781159c083a23a30f9fb9a),
[draftguitools.gui_trackers.gridTracker.setSpacing()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a67fe5637d9f2b95d4c6c6a717f41e6e4),
and
[draftguitools.gui_edit_arch_objects.ArchWallGuiTools.update_object_from_edit_points()](../../d1/d46/classdraftguitools_1_1gui__edit__arch__objects_1_1ArchWallGuiTools.html#a1340bdc87e40eb0a04ba856255ae0f93).

## ◆ update_all()

None AddonManager.CommandAddonManager.update_all  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Asynchronously apply all available updates: individual failures are noted, but do not stop other updates

References
[AddonManager.CommandAddonManager.update_all_worker](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a767f2572a102ecf48666ba4a4672bcf9).

## ◆ update_allowed_packages_list()

None AddonManager.CommandAddonManager.update_allowed_packages_list  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.allowed_packages](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad2a1d62812ae163770f31755e88cdc3b).

Referenced by
[AddonManager.CommandAddonManager.handle_disallowed_python()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a98d4404b8f0a7b16cff129ea4e65c8f4).

## ◆ update_check_complete()

None AddonManager.CommandAddonManager.update_check_complete  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.enable_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afbe900e4d7a33a684336a1e4ba2910f9),
and
[AddonManager.CommandAddonManager.packages_with_updates](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d88c6553e005f63afc1a273124f84f5).

## ◆ update_metadata_cache()

None AddonManager.CommandAddonManager.update_metadata_cache  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.update_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab9b23f9a93121e99fe07a1b33e555144).

Referenced by
[AddonManager.CommandAddonManager.startup()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e).

## ◆ update_progress_bar()

None AddonManager.CommandAddonManager.update_progress_bar  | ( |  | _self_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _current_value_ ,   
|  | [int](../../d1/da0/classint.html) | _max_value_  
| ) | |   
      
    
    Update the progress bar, showing it if it's hidden

References
[AddonManager.CommandAddonManager.current_progress_region](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aefdfbb84ab79c69c64b9304c1175c9a6),
Gui::Dialog::DlgParameterFind.dialog,
[RemoteDebugger.RemoteDebugger.dialog](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a36d8e434a10fb9e7d1aae9e2bc635c71),
Gui::Dialog::TaskTextureMapping.dialog, Gui::Dialog::TaskTransform.dialog,
[AddonManager.CommandAddonManager.dialog](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab6a31ca97dab5476ffeccb0e8b5bd071),
[ArchComponent.IfcEditorDelegate.dialog](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#adbc52010133bf10d5364aa3876413d3b),
[draftguitools.gui_shapestrings.ShapeString.dialog](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4d72dff4351e71a8639459fbc9a1b353),
[draftguitools.gui_texts.Text.dialog](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a66c664551f3a6e28ada5fb99f8051ea0),
[PathScripts.PathJobDlg.JobCreate.dialog](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af69757ca6b013ee2b5ad64272f26d74f),
[PathScripts.PathJobDlg.JobTemplateExport.dialog](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abbe5f7d6383f5e8a5bc27619fd557cc8),
[PathScripts.PathPost.DlgSelectPostProcessor.dialog](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a35ed78937500551699c74f44a7ca92e3),
[AddonManager.CommandAddonManager.number_of_progress_regions](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a57dd7b86672718dbe0efeaeec5cee2e8),
and
[AddonManager.CommandAddonManager.show_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af9df8398a3a7418385e7368fe10f6fe0).

Referenced by
[AddonManager.CommandAddonManager.validate()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3b5bdb4d937ff0f22e82fa180bb5ed2e).

## ◆ validate()

def AddonManager.CommandAddonManager.validate  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Developer tool: check all repos for validity and print report

References
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
[AddonManager.CommandAddonManager.item_model](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a935f56116ff654bd2adcf2049021fd71),
[change_branch.ChangeBranchDialog.item_model](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a2973e58066cedd227e8e9dc4b2f7407e),
[package_list.PackageList.item_model](../../d8/d41/classpackage__list_1_1PackageList.html#a2ef980f40752a0fe3bf98a23880921c4),
[AddonManager.CommandAddonManager.update_progress_bar()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a552bbbcaaddfd7c7a3b3c15b1c3235b3),
and
[AddonManager.CommandAddonManager.validate_package_xml()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a86159438c92359a47c0532b554c7a8fc).

Referenced by
[AddonManager.CommandAddonManager.startup()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e).

## ◆ validate_package_xml()

def AddonManager.CommandAddonManager.validate_package_xml  | ( |  | _self_ ,   
---|---|---|---  
|  | [Addon](../../d8/d91/classAddon_1_1Addon.html) | _addon_  
| ) | |   
  
References
[AddonManager.CommandAddonManager.validate_preference_pack_metadata()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab9f81005fc4fc5b5d053223ca14871be),
and
[AddonManager.CommandAddonManager.validate_workbench_metadata()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a44675a97a3097fead4243eb01c13c2be).

Referenced by
[AddonManager.CommandAddonManager.validate()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3b5bdb4d937ff0f22e82fa180bb5ed2e).

## ◆ validate_preference_pack_metadata()

List[[str](../../d9/d36/classstr.html)] AddonManager.CommandAddonManager.validate_preference_pack_metadata  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _pack_  
| ) | |   
  
Referenced by
[AddonManager.CommandAddonManager.validate_package_xml()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a86159438c92359a47c0532b554c7a8fc).

## ◆ validate_workbench_metadata()

List[[str](../../d9/d36/classstr.html)] AddonManager.CommandAddonManager.validate_workbench_metadata  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _workbench_  
| ) | |   
  
Referenced by
[AddonManager.CommandAddonManager.validate_package_xml()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a86159438c92359a47c0532b554c7a8fc).

## ◆ write_cache_stopfile()

None AddonManager.CommandAddonManager.write_cache_stopfile  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.get_cache_file_name()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac3080230c1760668c7bb2f73f20c8b02).

Referenced by
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca),
and
[AddonManager.CommandAddonManager.stop_update()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a625e178c0cc51da55bfb3c7b93595000).

## ◆ write_macro_cache()

def AddonManager.CommandAddonManager.write_macro_cache  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.get_cache_file_name()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac3080230c1760668c7bb2f73f20c8b02),
and
[AddonManager.CommandAddonManager.macro_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a157471c3fb9935d0f067e3141a328cc3).

Referenced by
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca).

## ◆ write_package_cache()

def AddonManager.CommandAddonManager.write_package_cache  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManager.CommandAddonManager.get_cache_file_name()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac3080230c1760668c7bb2f73f20c8b02),
and
[AddonManager.CommandAddonManager.package_cache](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#adca5d3afe751aea3551e876f1e252bb4).

Referenced by
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca).

## Member Data Documentation

## ◆ allowed_packages

AddonManager.CommandAddonManager.allowed_packages  
---  
  
Referenced by
[AddonManager.CommandAddonManager.handle_disallowed_python()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a98d4404b8f0a7b16cff129ea4e65c8f4),
[AddonManager.CommandAddonManager.resolve_dependencies()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a61c2eb1ed8627176ccd7b098754dbb18),
and
[AddonManager.CommandAddonManager.update_allowed_packages_list()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8ecd6c71a00d65219a51c1e348da1c48).

## ◆ check_worker

AddonManager.CommandAddonManager.check_worker  
---  
  
Referenced by
[AddonManager.CommandAddonManager.enable_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afbe900e4d7a33a684336a1e4ba2910f9),
and
[AddonManager.CommandAddonManager.force_check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a59ef1319a65cb46f3dab02bb23a7158d).

## ◆ connection_check_message

AddonManager.CommandAddonManager.connection_check_message  
---  
  
Referenced by
[AddonManager.CommandAddonManager.cancel_network_check()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af078842263c7b1297a3355d504d15aa1),
and
[AddonManager.CommandAddonManager.network_connection_failed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a188cb85c67487f14a33a9835660d25fa).

## ◆ connection_checker

AddonManager.CommandAddonManager.connection_checker  
---  
  
Referenced by
[AddonManager.CommandAddonManager.cancel_network_check()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af078842263c7b1297a3355d504d15aa1),
and
[AddonManager.CommandAddonManager.show_connection_check_message()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a45ab69ddffce3263be237d5bd32c087e).

## ◆ connection_message_timer

AddonManager.CommandAddonManager.connection_message_timer  
---  
  
## ◆ current_progress_region

AddonManager.CommandAddonManager.current_progress_region  
---  
  
Referenced by
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
and
[AddonManager.CommandAddonManager.update_progress_bar()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a552bbbcaaddfd7c7a3b3c15b1c3235b3).

## ◆ dependency_dialog

AddonManager.CommandAddonManager.dependency_dialog  
---  
  
Referenced by
[AddonManager.CommandAddonManager.dependency_dialog_yes_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a24130c49cbb70c64796e0327923b9396).

## ◆ dependency_installation_dialog

AddonManager.CommandAddonManager.dependency_installation_dialog  
---  
  
Referenced by
[AddonManager.CommandAddonManager.cancel_dependency_installation()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5dc57756d95f8932602cd2745d15ff1),
[AddonManager.CommandAddonManager.dependency_installation_failure()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa52493ff30557ea04b4000c33243abac),
[AddonManager.CommandAddonManager.install()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7844bcb2c34932d39cf0f18ebc9cedfc),
[AddonManager.CommandAddonManager.no_pip()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abe9fbe57e535559f53434676040a0f80),
and
[AddonManager.CommandAddonManager.no_python_exe()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a02ecc07f773ae69b309435ae5df313f7).

## ◆ dependency_installation_worker

AddonManager.CommandAddonManager.dependency_installation_worker  
---  
  
Referenced by
[AddonManager.CommandAddonManager.cancel_dependency_installation()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5dc57756d95f8932602cd2745d15ff1).

## ◆ dialog

AddonManager.CommandAddonManager.dialog  
---  
  
Referenced by
[RemoteDebugger.RemoteDebugger.accept()](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#ae2ed6ffa5958b758f58b061ab5ab5aa7),
[PathScripts.PathJobDlg.JobTemplateExport.checkUncheckTools()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a11c5eb6fce8ecee3c9352aa50ed686ac),
[AddonManager.CommandAddonManager.dependency_installation_failure()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa52493ff30557ea04b4000c33243abac),
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
[AddonManager.CommandAddonManager.enable_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afbe900e4d7a33a684336a1e4ba2910f9),
[RemoteDebugger.RemoteDebugger.exec_()](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a97a015d8cfdfae14723535c0b848a9aa),
[PathScripts.PathJobDlg.JobCreate.exec_()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a3949bbe83170d8e065b74724bcde9e2a),
[PathScripts.PathJobDlg.JobTemplateExport.exec_()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a0e1d5958964dcb0592e9e1582a2b02ec),
[PathScripts.PathPost.DlgSelectPostProcessor.exec_()](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a08d96f772033302b5f80db42c9ba3ae7),
[AddonManager.CommandAddonManager.executemacro()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa9a71a1815f63568b938dd0ec14dc2be),
[PathScripts.PathJobDlg.JobTemplateExport.exportButton()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a3bea8dbb69e7ff35e1b282948568c1d3),
[draftguitools.gui_texts.Text.finish()](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a3fe64be64c77319af1f265609dd8e985),
[AddonManager.CommandAddonManager.force_check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a59ef1319a65cb46f3dab02bb23a7158d),
[PathScripts.PathJobDlg.JobCreate.getTemplate()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#aff1aa651e747f139e2857baa3ac098cd),
[AddonManager.CommandAddonManager.handle_disallowed_python()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a98d4404b8f0a7b16cff129ea4e65c8f4),
[AddonManager.CommandAddonManager.hide_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5aa671118056f1c4e1b25468c63a02e),
[PathScripts.PathJobDlg.JobTemplateExport.includePostProcessing()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a5c0ae3a25dd31d7852c33ba61a077463),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettingCoolant()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abd2430ce061573743a362f761e0edf43),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettingOperationDepths()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a13a21bb42ed7f99ad2b0adae828162af),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettingOperationHeights()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#ac27ee58071125bf488a3dec81cbcccfd),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettingOpsSettings()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a29e5c0c9eee24a216ba723ab92ad49ca),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettings()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a2d9abd88c9a00cf383c0c5f0521c22ee),
[PathScripts.PathJobDlg.JobTemplateExport.includeSettingToolRapid()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a533790f9f6f5d30189750c73c3bc5920),
[PathScripts.PathJobDlg.JobTemplateExport.includeStock()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a27be0d3af9b7a30e228c80e7841fbb78),
[PathScripts.PathJobDlg.JobTemplateExport.includeStockExtent()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#ae3e2784d39e0002d29ed7849e7644abc),
[PathScripts.PathJobDlg.JobTemplateExport.includeStockPlacement()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#abc0e5c85e8c1e1abdaf83b287b1f255d),
[PathScripts.PathJobDlg.JobTemplateExport.includeToolControllers()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#a95880615cff4e1fdf5a478d87ae0aa89),
[AddonManager.CommandAddonManager.no_pip()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abe9fbe57e535559f53434676040a0f80),
[AddonManager.CommandAddonManager.no_python_exe()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a02ecc07f773ae69b309435ae5df313f7),
[AddonManager.CommandAddonManager.on_buttonUpdateCache_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa49366f509bb5b61e1d518f286f05adf),
[AddonManager.CommandAddonManager.on_installation_failed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ac8cf465e055e3880d958923bcf98f094),
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982),
[RemoteDebugger.RemoteDebugger.reject()](../../dc/dc3/classRemoteDebugger_1_1RemoteDebugger.html#a04c50a1b4f01889e599a863e1cede497),
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca),
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00),
[AddonManager.CommandAddonManager.report_missing_workbenches()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a90d0c6b99bc0b3a71e3f98d69c6dc3b2),
[ArchComponent.IfcEditorDelegate.setModelData()](../../dd/df9/classArchComponent_1_1IfcEditorDelegate.html#a1650f566d64beed8bdab63018e9da05e),
[PathScripts.PathJobDlg.JobCreate.setupModel()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#af073d7eb130a89da63d46c0b5365ebd6),
[PathScripts.PathJobDlg.JobCreate.setupTemplate()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a80e4cb8c0244d4087827496e639a0047),
[PathScripts.PathJobDlg.JobCreate.setupTitle()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#afb9f2a2deb2c8b0d282c4381f178b314),
[AddonManager.CommandAddonManager.show_information()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa2f17e60211c4a2e322e8801da6ff052),
[AddonManager.CommandAddonManager.show_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#af9df8398a3a7418385e7368fe10f6fe0),
[AddonManager.CommandAddonManager.stop_update()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a625e178c0cc51da55bfb3c7b93595000),
[AddonManager.CommandAddonManager.update_check_complete()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad6f86c6ddb56f3acd0d7b6985c49e936),
[AddonManager.CommandAddonManager.update_progress_bar()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a552bbbcaaddfd7c7a3b3c15b1c3235b3),
[PathScripts.PathPost.DlgSelectPostProcessor.updateTooltip()](../../d2/dac/classPathScripts_1_1PathPost_1_1DlgSelectPostProcessor.html#a7d0bd03437af3799d01917c0f65a8586),
and
[PathScripts.PathJobDlg.JobTemplateExport.updateUI()](../../d1/d30/classPathScripts_1_1PathJobDlg_1_1JobTemplateExport.html#add858b24fbcff0183f70f02aacb541f0).

## ◆ install_worker

AddonManager.CommandAddonManager.install_worker  
---  
  
Referenced by
[AddonManager.CommandAddonManager.install()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a7844bcb2c34932d39cf0f18ebc9cedfc).

## ◆ item_model

AddonManager.CommandAddonManager.item_model  
---  
  
Referenced by
[AddonManager.CommandAddonManager.add_addon_repo()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a0128d399282eb71e55417bf8ef4ec946),
[AddonManager.CommandAddonManager.append_to_repos_list()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a34106546e723a43de9e286223474904e),
[AddonManager.CommandAddonManager.dependency_dialog_yes_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a24130c49cbb70c64796e0327923b9396),
[change_branch.ChangeBranchDialog.exec()](../../dd/d27/classchange__branch_1_1ChangeBranchDialog.html#a6c58ac15929c71fac630a9462df2004c),
[AddonManager.CommandAddonManager.mark_repo_update_available()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a670656464d505dcab469a2f1bd7de259),
[package_list.PackageList.on_listPackages_clicked()](../../d8/d41/classpackage__list_1_1PackageList.html#a54fa96e2d947c6aea2e6ec176cca7fc9),
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
[AddonManager.CommandAddonManager.on_package_updated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae31bf139686923b617a182aeb1588425),
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982),
[AddonManager.CommandAddonManager.populate_packages_table()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#adcc9afd53c106b8a724792bf17943fe3),
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca),
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00),
[AddonManager.CommandAddonManager.resolve_dependencies()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a61c2eb1ed8627176ccd7b098754dbb18),
[AddonManager.CommandAddonManager.select_addon()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa632e875b2d90517423d4e47fa60a263),
[package_list.PackageList.set_view_style()](../../d8/d41/classpackage__list_1_1PackageList.html#ac8e3ffc5c454dd0f8df710ed32866696),
[AddonManager.CommandAddonManager.status_updated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a34e713179c4b82c43c5228dcc3a5edab),
and
[AddonManager.CommandAddonManager.validate()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a3b5bdb4d937ff0f22e82fa180bb5ed2e).

## ◆ load_macro_metadata_worker

AddonManager.CommandAddonManager.load_macro_metadata_worker  
---  
  
## ◆ lock

| AddonManager.CommandAddonManager.lock = threading.Lock()  
---  
static  
  
Referenced by
[AddonManager.CommandAddonManager.on_package_updated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ae31bf139686923b617a182aeb1588425),
[drafttaskpanels.task_scale.ScaleTaskPanel.retranslateUi()](../../df/d70/classdrafttaskpanels_1_1task__scale_1_1ScaleTaskPanel.html#ab5cdf6b149fea39e027f877ea7b5a12c),
[drafttaskpanels.task_scale.ScaleTaskPanel.setValue()](../../df/d70/classdrafttaskpanels_1_1task__scale_1_1ScaleTaskPanel.html#a1782575b8f05ad2356a3dc6d60cd6f2d),
[addonmanager_workers.CacheMacroCode.terminate()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#ad7e2fd17788450db3eedb1cfa1195aa9),
and
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

## ◆ macro_cache

AddonManager.CommandAddonManager.macro_cache  
---  
  
Referenced by
[AddonManager.CommandAddonManager.write_macro_cache()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a5f956f75f80aa2563d2c8bd114387e90).

## ◆ macro_repo_dir

AddonManager.CommandAddonManager.macro_repo_dir  
---  
  
Referenced by
[AddonManager.CommandAddonManager.executemacro()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa9a71a1815f63568b938dd0ec14dc2be).

## ◆ macro_worker

AddonManager.CommandAddonManager.macro_worker  
---  
  
## ◆ number_of_progress_regions

AddonManager.CommandAddonManager.number_of_progress_regions  
---  
  
Referenced by
[AddonManager.CommandAddonManager.update_progress_bar()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a552bbbcaaddfd7c7a3b3c15b1c3235b3).

## ◆ package_cache

AddonManager.CommandAddonManager.package_cache  
---  
  
Referenced by
[AddonManager.CommandAddonManager.write_package_cache()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#add9dfb8ffaeab53db5705aced8b74650).

## ◆ packageDetails

AddonManager.CommandAddonManager.packageDetails  
---  
  
Referenced by
[AddonManager.CommandAddonManager.mark_repo_update_available()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a670656464d505dcab469a2f1bd7de259),
[AddonManager.CommandAddonManager.on_buttonBack_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afb6e3f578cb11b910660d85fadebf680),
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00),
[AddonManager.CommandAddonManager.show_workbench()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a29da4a500ceeef891d623aeb0d1dbd2d),
and
[AddonManager.CommandAddonManager.table_row_activated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad3f15ade8b0e8128d0807d6bd3800422).

## ◆ packageList

AddonManager.CommandAddonManager.packageList  
---  
  
Referenced by
[AddonManager.CommandAddonManager.activate_table_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aeb8df4878a5a24da5fe675be652c4778),
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
[AddonManager.CommandAddonManager.hide_progress_widgets()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ab5aa671118056f1c4e1b25468c63a02e),
[AddonManager.CommandAddonManager.on_buttonBack_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afb6e3f578cb11b910660d85fadebf680),
[AddonManager.CommandAddonManager.show_workbench()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a29da4a500ceeef891d623aeb0d1dbd2d),
and
[AddonManager.CommandAddonManager.table_row_activated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad3f15ade8b0e8128d0807d6bd3800422).

## ◆ packages_with_updates

AddonManager.CommandAddonManager.packages_with_updates  
---  
  
Referenced by
[AddonManager.CommandAddonManager.check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6fcf66f208db8991362e236fe9c2e4b5),
[AddonManager.CommandAddonManager.force_check_updates()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a59ef1319a65cb46f3dab02bb23a7158d),
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982),
[AddonManager.CommandAddonManager.status_updated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a34e713179c4b82c43c5228dcc3a5edab),
and
[AddonManager.CommandAddonManager.update_check_complete()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad6f86c6ddb56f3acd0d7b6985c49e936).

## ◆ restart_required [1/2]

| [bool](../../d9/db9/classbool.html)
AddonManager.CommandAddonManager.restart_required = False  
---  
static  
  
Referenced by
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982),
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca),
and
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00).

## ◆ restart_required [2/2]

AddonManager.CommandAddonManager.restart_required  
---  
  
Referenced by
[AddonManager.CommandAddonManager.on_package_installed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#abf1dbc5ed9bc3918e6f96dda28954770),
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982),
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca),
and
[AddonManager.CommandAddonManager.remove()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aae7cdf308d96b87d195e7be2de765a00).

## ◆ startup_sequence

AddonManager.CommandAddonManager.startup_sequence  
---  
  
Referenced by
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
[AddonManager.CommandAddonManager.on_buttonUpdateCache_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa49366f509bb5b61e1d518f286f05adf),
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca),
and
[AddonManager.CommandAddonManager.startup()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a6dfd103034d4ae8f83c23abe93c6317e).

## ◆ subupdates_failed

AddonManager.CommandAddonManager.subupdates_failed  
---  
  
Referenced by
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982).

## ◆ subupdates_succeeded

AddonManager.CommandAddonManager.subupdates_succeeded  
---  
  
Referenced by
[AddonManager.CommandAddonManager.on_update_all_completed()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a1fa2c3ccb5f70dcb1d20df00bbb40982).

## ◆ trigger_recache

AddonManager.CommandAddonManager.trigger_recache  
---  
  
## ◆ update_all_worker

AddonManager.CommandAddonManager.update_all_worker  
---  
  
Referenced by
[AddonManager.CommandAddonManager.update_all()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8aefdf5b187b70350fbba8cf16f05c67).

## ◆ update_cache

AddonManager.CommandAddonManager.update_cache  
---  
  
Referenced by
[AddonManager.CommandAddonManager.determine_cache_update_status()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a654998e0b8406348918e12bb0d7ebabf),
[AddonManager.CommandAddonManager.do_next_startup_phase()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#afc0b4e496960a62e610043b953ec028b),
[AddonManager.CommandAddonManager.load_macro_metadata()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a2507d2bb48755c69af59d525493adf1a),
[AddonManager.CommandAddonManager.on_buttonUpdateCache_clicked()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aa49366f509bb5b61e1d518f286f05adf),
[AddonManager.CommandAddonManager.populate_macros()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a94671ecd8a490dd469f52823a2abe9ba),
[AddonManager.CommandAddonManager.populate_packages_table()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#adcc9afd53c106b8a724792bf17943fe3),
and
[AddonManager.CommandAddonManager.update_metadata_cache()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aadd646ff8e8567949cd480b3b372c2e2).

## ◆ update_metadata_cache_worker

AddonManager.CommandAddonManager.update_metadata_cache_worker  
---  
  
## ◆ update_worker

AddonManager.CommandAddonManager.update_worker  
---  
  
## ◆ workers

| list AddonManager.CommandAddonManager.workers  
---  
static  
  
**Initial value:**

= [

"connection_checker",

"update_worker",

"check_worker",

"show_worker",

"showmacro_worker",

"macro_worker",

"install_worker",

"update_metadata_cache_worker",

"load_macro_metadata_worker",

"update_all_worker",

"dependency_installation_worker",

]

Referenced by
[AddonManager.CommandAddonManager.cleanup_workers()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a8d86001908bd07941d546db0e6463065),
[AddonManager.CommandAddonManager.reject()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#aef345e1dbcc980bf3d435f6c365905ca),
and
[addonmanager_workers.CacheMacroCode.update_and_advance()](../../d3/d5f/classaddonmanager__workers_1_1CacheMacroCode.html#a66013edd1a442f8da1e606cff5f9d631).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/AddonManager.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

