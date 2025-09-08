---
url: https://wiki.freecad.org/Std_AddonMgr
title: Std AddonMgr
scraped_at: 2025-09-08 16:46:02
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Description
  * 2 Usage
  * 3 Options
  * 4 Preferences
  * 5 Sorting by score
  * 6 Notes
  * 7 Information for addon developers
  * 8 Scripting Toggle Scripting subsection
    * 8.1 Commandline (non-GUI) use
    * 8.2 GUI use

# Std AddonMgr

  * [Page](/Std_AddonMgr "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Std_AddonMgr&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Std_AddonMgr)
  * [Edit](/index.php?title=Std_AddonMgr&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Std_AddonMgr&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Std_AddonMgr.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Std_AddonMgr&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Std_AddonMgr)
  * [Edit](/index.php?title=Std_AddonMgr&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Std_AddonMgr&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Std_AddonMgr&action=history)

General

  * [What links here](/Special:WhatLinksHere/Std_AddonMgr "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Std_AddonMgr "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Std_AddonMgr&oldid=1626018 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Std_AddonMgr&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Std_AddonMgr&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Std+AddonMgr&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Std+AddonMgr&language=&task=view "Start translation for this language")
  * [Deutsch](/Std_AddonMgr/de "Std AddonManager \(100% translated\)")
  * English
  * [Türkçe](/Std_AddonMgr/tr "Eklenti Yöneticisi \(3% translated\)")
  * [español](/Std_AddonMgr/es "Std GestorComplementos \(35% translated\)")
  * [français](/Std_AddonMgr/fr "Std Gestionnaire des extensions \(100% translated\)")
  * [hrvatski](/Std_AddonMgr/hr "Std AddonMgr/hr \(0% translated\)")
  * [italiano](/Std_AddonMgr/it "Strumenti: Addon manager \(100% translated\)")
  * [polski](/Std_AddonMgr/pl "Std: Menadżer dodatków \(100% translated\)")
  * [português](/Std_AddonMgr/pt "Std AddonMgr/pt \(0% translated\)")
  * [português do Brasil](/Std_AddonMgr/pt-br "Gerenciador de Extensões \(3% translated\)")
  * [română](/Std_AddonMgr/ro "Std: Mangerul de Addon \(3% translated\)")
  * [русский](/Std_AddonMgr/ru "Команда "Менеджер дополнений" \(38% translated\)")
  * [日本語](/Std_AddonMgr/ja "共通・アドオンマネージャー \(3% translated\)")
  * [한국어](/Std_AddonMgr/ko "애드온 관리자 \(3% translated\)")

![](/images/0/06/Freecad.svg)

![](/images/4/4e/Std_Measure.svg) [Measure](/Std_Measure "Std Measure")
![](/images/a/af/Arrow-right.svg)

[Std Tools Menu](/Std_Tools_Menu "Std Tools Menu")
![](/images/0/06/Freecad.svg)

![](/images/e/ee/Std_AddonMgr.svg) Std AddonMgr  
---  
Menu location  
Tools → Addon manager  
Workbenches  
All  
Default shortcut  
_None_  
Introduced in version  
0.17  
See also  
[External workbenches](/External_workbenches "External workbenches"),
[Macros](/Macros "Macros")  
  
  
  
## Description

The **Std AddonMgr** command opens the Addon manager. With the Addon manager
you can install and manage [external workbenches](/External_workbenches
"External workbenches"), [macros](/Macros "Macros"), and [preference
packs](/Preference_Packs "Preference Packs") provided by the FreeCAD
community. By default the available addons are taken from two repositories,
[FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) and from the
[Macros recipes](/Macros_recipes "Macros recipes") page of this wiki. If git
is installed on your system, additional macros will be loaded from [FreeCAD-
macros](https://github.com/FreeCAD/FreeCAD-macros/). Custom repositories can
be added in the [Addon manager preferences](/Preferences_Editor#Addon_Manager
"Preferences Editor").

As of May 2025, the Addon manager can now be used to install and update a
self-updating version of itself by installing the "Addon Manager" addon. It is
compatible with FreeCAD 0.21 and later.

## Usage

  1. Select the **Tools →[![](/images/e/ee/Std_AddonMgr.svg)](/index.php?title=File:Std_AddonMgr.svg&filetimestamp=20240704212012&) Addon manager** option from the menu.
  2. If you are using the Addon manager for the first time, a dialog box will open warning you that the addons in the Addon manager are not officially part of FreeCAD. It also presents several options related to the Addon manager's data usage. Adjust those options to your liking and press the OK button to confirm and continue.
  3. The Addon manager dialog box opens. For more information see Options.
  4. If you have installed or updated a workbench a new dialog box will open informing you that you have to restart FreeCAD for the changes to take effect.

## Options

[![](/images/thumb/7/78/AddonManager_Main.png/600px-
AddonManager_Main.png)](/index.php?title=File:AddonManager_Main.png&filetimestamp=20220909083927&)

  1. The Addon manager provides two view layouts: "Condensed" and "Expanded". In "Condensed" view, each addon takes a single line, and its description is truncated to fit the available space. "Expanded" shows additional details, including more of the description text as well as maintainer information, more installation details, etc.
  2. Five types of addons are supported: [workbenches](/External_workbenches "External workbenches"), [macros](/Macros "Macros"), [preference packs](/Preference_Packs "Preference Packs"), bundles, and "other". You can choose to show just one type, or all of them in a single list.
  3. The list can be limited to show just installed packages, just packages with available updates, or just packages that are not yet installed.
  4. The list can be filtered, searching for a keyword in the title, description, and tags (description and tags must be specified by the addon developer in their addon's metadata). The filter can even be a regular expression, for fine-grained control of the exact search term.
  5. The expanded view shows available version information, description, maintainer information, and installation version information, for packages that provide a [package metadata](/Package_Metadata "Package Metadata") file (or for macros with embedded metadata).
  6. Addon data is cached locally, with a variable cache update frequency set in the user preferences.
  7. At any time you can choose to manually update your local cache to see the latest updates available for each addon.
  8. Update checks may be set up to be automatic, or done manually via a button click (configured in user preferences). If GitPython and git are installed on your system then update information is fetched using git. If not, then update information is obtained from any present metadata file.

Clicking on an addon in this view brings up the addon's Details page:

[![](/images/thumb/5/54/AddonManager_Details.png/600px-
AddonManager_Details.png)](/index.php?title=File:AddonManager_Details.png&filetimestamp=20220909084027&)

The details page shows buttons allowing installing, uninstalling, updating,
and temporarily disabling an addon. For installed addons it lists the
currently installed version and the installation date, and whether that is the
most recent version available. Below is an embedded web browser window showing
the addon's README page (for workbenches and preference packs), or Wiki page
(for macros).

## Preferences

The preferences for the Addon manager can be found in the [Preferences
Editor](/Preferences_Editor#Addon_Manager "Preferences Editor"). [introduced
in 0.20](/Release_notes_0.20 "Release notes 0.20")

## Sorting by score

[introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

The Addon manager supports sorting by a number of different criteria. Most of
these are downloaded directly from FreeCAD's servers (which caches them from
GitHub and the FreeCAD Wiki) but one, "Score," is not provided by FreeCAD at
all, and only appears as an option if the Score Source URL setting is provided
in the Preferences.

The Score Source URL is a path to a remote JSON-formatted document listing
addons and a "score" of some kind. Score can be calculated in any way the data
provider likes, but should be an integer value, with higher scores being
"better" in some sense. Any addon not listed is assigned a score of zero
internally. The format of the file is a single JSON dictionary where the key
is the addon URL (for workbenches and preference packs) or the name of the
macro (for macros). See [this data
source](https://gist.githubusercontent.com/chennes/e8f60e80f16e6ffbd057dd47ca36ad2a/raw/7b118cca8e84444c3379919bbd744b99e6ef6711/addon_score_for_testing.json)
for an example (note the score there is simply the length of the addon's
description, and is intended only for testing and demonstration purposes).

## Notes

  * The use of addons is not restricted to the FreeCAD version they were installed from. You will also be able to use them in any other FreeCAD version, supported by the addon, that you may have on your system.
  * The addons available in the Addon manager are not part of the official FreeCAD program and are not supported by the core FreeCAD development team. You should read the provided information carefully to make sure you know what you are installing.
  * Bug reports and feature requests should be made directly to the creator of the addon by visiting the indicated website. Many addon developers are regular users of the [FreeCAD forum](https://forum.freecad.org), and can also be contacted there.
  * If the the source-code management software `git` is installed on your computer the Addon manager will use it, making updates faster.
  * You can also install addons manually. See [How to install additional workbenches](/How_to_install_additional_workbenches "How to install additional workbenches") and [How to install macros](/How_to_install_macros "How to install macros").

## Information for addon developers

See [Addon](/Addon#Information_for_developers "Addon").

## Scripting

[introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")

Some features of the Addon manager are designed for access via FreeCAD's
Python API. In particular an addon can be installed, updated, and removed via
the Python interface. Most uses of this API require you to create an object
with at least three attributes: `name`, `branch` and `url`. For example:

    
    
    class MyAddonClass:
        def __init__(self):
            self.name = "TestAddon"
            self.url = "https://github.com/Me/MyTestAddon"
            self.branch = "main"
    my_addon = MyAddonClass()
    

Your object `my_addon` is now ready for use with the Addon manager API.

### Commandline (non-GUI) use

If your code needs to install or update an addon synchronously (e.g. without a
GUI) the code can be very simple:

    
    
    from addonmanager_installer import AddonInstaller
    installer = AddonInstaller(my_addon)
    installer.run()
    

Note that this code blocks until complete, so you shouldn't run it on the main
GUI thread. To the Addon manager, "install" and "update" are the same call: if
this addon is already installed, and git is available, it will be updated via
"git pull". If it is not installed, or was installed via a non-git
installation method, it is downloaded from scratch (using git if available).

To uninstall, use:

    
    
    from addonmanager_uninstaller import AddonUninstaller
    uninstaller = AddonUninstaller(my_addon)
    uninstaller.run()
    

### GUI use

If you plan on your code running in a GUI, or supporting running in the full
version of FreeCAD, it's best to run your installation in a separate non-GUI
thread, so the GUI remains responsive. To do this, first check to see if the
GUI is running, and if it is, spawn a `QThread` (don't try to spawn a
`QThread` if the GUI is not up: they require an active event loop to
function).

    
    
    from PySide import QtCore
    from addonmanager_installer import AddonInstaller
    
    worker_thread = QtCore.QThread()
    installer = AddonInstaller(my_addon)
    installer.moveToThread(worker_thread)
    installer.success.connect(installation_succeeded)
    installer.failure.connect(installation_failed)
    installer.finished.connect(worker_thread.quit)
    worker_thread.started.connect(installer.run)
    worker_thread.start() # Returns immediately
    

Then define the functions `installation_succeeded` and `installation_failed`
to be run in each case. For uninstallation you can use the same technique,
though it is usually much faster and will not block the GUI for very long, so
in general it's safe to use the uninstaller directly, as shown above.

  

![](/images/0/06/Freecad.svg)

![](/images/4/4e/Std_Measure.svg) [Measure](/Std_Measure "Std Measure")
![](/images/a/af/Arrow-right.svg)

[Std Tools Menu](/Std_Tools_Menu "Std Tools Menu")
![](/images/0/06/Freecad.svg)

Expand[![](/images/0/06/Freecad.svg)](/index.php?title=File:Freecad.svg&filetimestamp=20240704193018&)
[Std Base](/Std_Base "Std Base")

  * **[File](/Std_File_Menu "Std File Menu"):** [New](/Std_New "Std New"), [Open](/Std_Open "Std Open"), [Open Recent](/Std_RecentFiles "Std RecentFiles"), [Close](/Std_CloseActiveWindow "Std CloseActiveWindow"), [Close All](/Std_CloseAllWindows "Std CloseAllWindows"), [Save](/Std_Save "Std Save"), [Save As](/Std_SaveAs "Std SaveAs"), [Save a Copy](/Std_SaveCopy "Std SaveCopy"), [Save All](/Std_SaveAll "Std SaveAll"), [Revert](/Std_Revert "Std Revert"), [Import](/Std_Import "Std Import"), [Export](/Std_Export "Std Export"),[Merge project](/Std_MergeProjects "Std MergeProjects"), [Document information](/Std_ProjectInfo "Std ProjectInfo"), [Print](/Std_Print "Std Print"), [Print preview](/Std_PrintPreview "Std PrintPreview"), [Export PDF](/Std_PrintPdf "Std PrintPdf"), [Exit](/Std_Quit "Std Quit")

* * *

  * **[Edit](/Std_Edit_Menu "Std Edit Menu"):** [Undo](/Std_Undo "Std Undo"), [Redo](/Std_Redo "Std Redo"), [Cut](/Std_Cut "Std Cut"), [Copy](/Std_Copy "Std Copy"), [Paste](/Std_Paste "Std Paste"), [Duplicate selection](/Std_DuplicateSelection "Std DuplicateSelection"), [Refresh](/Std_Refresh "Std Refresh"), [Box selection](/Std_BoxSelection "Std BoxSelection"), [Box element selection](/Std_BoxElementSelection "Std BoxElementSelection"), [Select All](/Std_SelectAll "Std SelectAll"), [Delete](/Std_Delete "Std Delete"), [Send to Python Console](/Std_SendToPythonConsole "Std SendToPythonConsole"), [Placement](/Std_Placement "Std Placement"), [Transform](/Std_TransformManip "Std TransformManip"), [Alignment](/Std_Alignment "Std Alignment"), [Toggle Edit mode](/Std_Edit "Std Edit"), [Properties](/index.php?title=Std_Propertiest&action=edit&redlink=1 "Std Propertiest \(page does not exist\)"), [Edit mode](/Std_UserEditMode "Std UserEditMode"), [Preferences](/Std_DlgPreferences "Std DlgPreferences")

* * *

  * **[View](/Std_View_Menu "Std View Menu"):**
    * **Miscellaneous:** [Create new view](/Std_ViewCreate "Std ViewCreate"), [Orthographic view](/Std_OrthographicCamera "Std OrthographicCamera"), [Perspective view](/Std_PerspectiveCamera "Std PerspectiveCamera"), [Fullscreen](/Std_MainFullscreen "Std MainFullscreen"), [Bounding box](/Std_SelBoundingBox "Std SelBoundingBox"), [Toggle axis cross](/Std_AxisCross "Std AxisCross"), [Clipping plane](/Std_ToggleClipPlane "Std ToggleClipPlane"), [Persistent section cut](/Part_SectionCut "Part SectionCut"), [Texture mapping](/Std_TextureMapping "Std TextureMapping"), [Toggle navigation/Edit mode](/Std_ToggleNavigation "Std ToggleNavigation"), [Material](/Std_SetMaterial "Std SetMaterial"), [Appearance](/Std_SetAppearance "Std SetAppearance"), [Random color](/Std_RandomColor "Std RandomColor"), [Color per face](/Part_ColorPerFace "Part ColorPerFace"), [Toggle transparency](/Std_ToggleTransparency "Std ToggleTransparency"), [Workbench](/Std_Workbench "Std Workbench"), [Status bar](/Std_ViewStatusBar "Std ViewStatusBar")
    * **Standard views:** [Fit all](/Std_ViewFitAll "Std ViewFitAll"), [Fit selection](/Std_ViewFitSelection "Std ViewFitSelection"), [Align to selection](/Std_AlignToSelection "Std AlignToSelection"), [Isometric](/Std_ViewIsometric "Std ViewIsometric"), [Dimetric](/Std_ViewDimetric "Std ViewDimetric"), [Trimetric](/Std_ViewTrimetric "Std ViewTrimetric"), [Home](/Std_ViewHome "Std ViewHome"), [Front](/Std_ViewFront "Std ViewFront"), [Top](/Std_ViewTop "Std ViewTop"), [Right](/Std_ViewRight "Std ViewRight"), [Rear](/Std_ViewRear "Std ViewRear"), [Bottom](/Std_ViewBottom "Std ViewBottom"), [Left](/Std_ViewLeft "Std ViewLeft"), [Rotate Left](/Std_ViewRotateLeft "Std ViewRotateLeft"), [Rotate Right](/Std_ViewRotateRight "Std ViewRotateRight"), [Store working view](/Std_StoreWorkingView "Std StoreWorkingView"), [Recall working view](/Std_RecallWorkingView "Std RecallWorkingView")
    * **[Freeze display](/Std_FreezeViews "Std FreezeViews"):** [Save views](/Std_FreezeViews#Save_views "Std FreezeViews"), [Load views](/Std_FreezeViews#Load_views "Std FreezeViews"), [Freeze view](/Std_FreezeViews#Freeze_view "Std FreezeViews"), [Clear views](/Std_FreezeViews#Clear_views "Std FreezeViews")
    * **[Draw style](/Std_DrawStyle "Std DrawStyle"):** [As is](/Std_DrawStyle#As_is "Std DrawStyle"), [Points](/Std_DrawStyle#Points "Std DrawStyle"), [Wireframe](/Std_DrawStyle#Wireframe "Std DrawStyle"), [Hidden line](/Std_DrawStyle#Hidden_line "Std DrawStyle"), [No shading](/Std_DrawStyle#No_shading "Std DrawStyle"), [Shaded](/Std_DrawStyle#Shaded "Std DrawStyle"), [Flat lines](/Std_DrawStyle#Flat_lines "Std DrawStyle")
    * **Stereo:** [Stereo red/cyan](/Std_ViewIvStereoRedGreen "Std ViewIvStereoRedGreen"), [Stereo quad buffer](/Std_ViewIvStereoQuadBuff "Std ViewIvStereoQuadBuff"), [Stereo Interleaved Rows](/Std_ViewIvStereoInterleavedRows "Std ViewIvStereoInterleavedRows"), [Stereo Interleaved Columns](/Std_ViewIvStereoInterleavedColumns "Std ViewIvStereoInterleavedColumns"), [Stereo Off](/Std_ViewIvStereoOff "Std ViewIvStereoOff"), [Issue camera position](/Std_ViewIvIssueCamPos "Std ViewIvIssueCamPos")
    * **Zoom:** [Zoom In](/Std_ViewZoomIn "Std ViewZoomIn"), [Zoom Out](/Std_ViewZoomOut "Std ViewZoomOut"), [Box zoom](/Std_ViewBoxZoom "Std ViewBoxZoom")
    * **Document window:** [Docked](/Std_ViewDockUndockFullscreen#Docked "Std ViewDockUndockFullscreen"), [Undocked](/Std_ViewDockUndockFullscreen#Undocked "Std ViewDockUndockFullscreen"), [Fullscreen](/Std_ViewFullscreen "Std ViewFullscreen")
    * **Visibility:** [Toggle visibility](/Std_ToggleVisibility "Std ToggleVisibility"), [Show selection](/Std_ShowSelection "Std ShowSelection"), [Hide selection](/Std_HideSelection "Std HideSelection"), [Select visible objects](/Std_SelectVisibleObjects "Std SelectVisibleObjects"), [Toggle all objects](/Std_ToggleObjects "Std ToggleObjects"), [Show all objects](/Std_ShowObjects "Std ShowObjects"), [Hide all objects](/Std_HideObjects "Std HideObjects"), [Toggle selectability](/Std_ToggleSelectability "Std ToggleSelectability")
    * **Toolbars:** File, Edit, Clipboard, Workbench, Macro, View, Individual views, Structure, Help, [Lock toolbars](/index.php?title=Std_ToggleToolBarLock&action=edit&redlink=1 "Std ToggleToolBarLock \(page does not exist\)")
    * **Panels:** [Tree view](/Tree_view "Tree view"), [Property view](/Property_editor "Property editor"), [Model](/Combo_view "Combo view"), [Selection view](/Selection_view "Selection view"), [Python console](/Python_console "Python console"), [Report view](/Report_view "Report view"), [Tasks](/Task_panel "Task panel"), [DAG view](/DAG_view "DAG view")
    * **Dock window overlay:** [Toggle overlay for all](/Std_DockOverlayAll "Std DockOverlayAll"), [Toggle transparent for all](/Std_DockOverlayTransparentAll "Std DockOverlayTransparentAll"), [Toggle overlay](/Std_DockOverlayToggle "Std DockOverlayToggle"), [Toggle transparent](/Std_DockOverlayToggleTransparent "Std DockOverlayToggleTransparent"), [Bypass mouse events in docked overlay windows](/Std_DockOverlayMouseTransparent "Std DockOverlayMouseTransparent"), [Toggle left](/Std_DockOverlayToggleLeft "Std DockOverlayToggleLeft"), [Toggle right](/Std_DockOverlayToggleRight "Std DockOverlayToggleRight"), [Toggle top](/Std_DockOverlayToggleTop "Std DockOverlayToggleTop"), [Toggle bottom](/Std_DockOverlayToggleBottom "Std DockOverlayToggleBottom")
    * **Link navigation:** [Go to linked object](/Std_LinkSelectLinked "Std LinkSelectLinked"), [Go to the deepest linked object](/Std_LinkSelectLinkedFinal "Std LinkSelectLinkedFinal"), [Select all links](/Std_LinkSelectAllLinks "Std LinkSelectAllLinks")
    * **Tree view actions:** [Sync view](/Std_TreeSyncView "Std TreeSyncView"), [Sync selection](/Std_TreeSyncSelection "Std TreeSyncSelection"), [Sync placement](/Std_TreeSyncPlacement "Std TreeSyncPlacement"), [Pre-selection](/Std_TreePreSelection "Std TreePreSelection"), [Record selection](/Std_TreeRecordSelection "Std TreeRecordSelection"), [Single document](/Std_TreeSingleDocument "Std TreeSingleDocument"), [Multi document](/Std_TreeMultiDocument "Std TreeMultiDocument"), [Collapse/Expand](/Std_TreeCollapseDocument "Std TreeCollapseDocument"), [Initiate dragging](/Std_TreeDrag "Std TreeDrag"), [Go to selection](/Std_TreeSelection "Std TreeSelection"), [Selection back](/Std_SelBack "Std SelBack"), [Selection forward](/Std_SelForward "Std SelForward")

* * *

  * **[Tools](/Std_Tools_Menu "Std Tools Menu"):** [Edit parameters](/Std_DlgParameter "Std DlgParameter"), [Save image](/Std_ViewScreenShot "Std ViewScreenShot"), [Load image](/Std_ViewLoadImage "Std ViewLoadImage"), [Scene inspector](/Std_SceneInspector "Std SceneInspector"), [Dependency graph](/Std_DependencyGraph "Std DependencyGraph"), [Export dependency graph](/Std_ExportDependencyGraph "Std ExportDependencyGraph"), [Document utility](/Std_ProjectUtil "Std ProjectUtil"), [Add text document](/Std_TextDocument "Std TextDocument"), [View turntable](/Std_DemoMode "Std DemoMode"), [Units converter](/Std_UnitsCalculator "Std UnitsCalculator"), [Customize](/Std_DlgCustomize "Std DlgCustomize"), Addon manager, [Measure](/Std_Measure "Std Measure")

* * *

  * **[Macro](/Std_Macro_Menu "Std Macro Menu"):** [Macro recording](/Std_DlgMacroRecord "Std DlgMacroRecord"), [Macros](/Std_DlgMacroExecute "Std DlgMacroExecute"), Recent macros, [Execute macro](/Std_DlgMacroExecuteDirect "Std DlgMacroExecuteDirect"), [Attach to remote debugger](/Std_MacroAttachDebugger "Std MacroAttachDebugger"), [Debug macro](/Std_MacroStartDebug "Std MacroStartDebug"), [Stop debugging](/Std_MacroStopDebug "Std MacroStopDebug"), [Step over](/Std_MacroStepOver "Std MacroStepOver"), [Step into](/Std_MacroStepInto "Std MacroStepInto"), [Toggle breakpoint](/Std_ToggleBreakpoint "Std ToggleBreakpoint")

* * *

  * **[Windows](/Std_Windows_Menu "Std Windows Menu"):** [Next](/Std_ActivateNextWindow "Std ActivateNextWindow"), [Previous](/Std_ActivatePrevWindow "Std ActivatePrevWindow"), [Tile](/Std_TileWindows "Std TileWindows"), [Cascade](/Std_CascadeWindows "Std CascadeWindows"), [Windows](/Std_Windows "Std Windows")

* * *

  * **[Help](/Std_Help_Menu "Std Help Menu"):** [Help](/Std_OnlineHelp "Std OnlineHelp"), [FreeCAD Website](/Std_FreeCADWebsite "Std FreeCADWebsite"), [Donate](/Std_FreeCADDonation "Std FreeCADDonation"), [Users documentation](/Std_FreeCADUserHub "Std FreeCADUserHub"), [Python scripting documentation](/Std_FreeCADPowerUserHub "Std FreeCADPowerUserHub"), [Automatic Python modules documentation](/Std_PythonHelp "Std PythonHelp"), [FreeCAD Forum](/Std_FreeCADForum "Std FreeCADForum"), [FreeCAD FAQ](/Std_FreeCADFAQ "Std FreeCADFAQ"), [Report a bug](/Std_ReportBug "Std ReportBug"), [About FreeCAD](/Std_About "Std About"), [What's This](/Std_WhatsThis "Std WhatsThis"), [Start](/index.php?title=Start_Start&action=edit&redlink=1 "Start Start \(page does not exist\)")

* * *

  * **[Additional](/Std_Base "Std Base"):**
    * **Miscellaneous:** [Create part](/Std_Part "Std Part"), [Create group](/Std_Group "Std Group"), [Create a variable set](/Std_VarSet "Std VarSet"), [Make link group](/index.php?title=Std_LinkMakeGroup&action=edit&redlink=1 "Std LinkMakeGroup \(page does not exist\)"), [Select all instances](/Std_TreeSelectAllInstances "Std TreeSelectAllInstances"), [Toggle freeze](/Std_ToggleFreeze "Std ToggleFreeze")
    * **Create datums:** [Create coordinate system](/Part_CoordinateSystem "Part CoordinateSystem"), [Create datum plane](/Part_DatumPlane "Part DatumPlane"), [Create datum line](/Part_DatumLine "Part DatumLine"), [Create datum point](/Part_DatumPoint "Part DatumPoint")
    * **Link tools:** [Make link](/Std_LinkMake "Std LinkMake"), [Make sub-link](/Std_LinkMakeRelative "Std LinkMakeRelative"), [Replace with link](/Std_LinkReplace "Std LinkReplace"), [Unlink](/Std_LinkUnlink "Std LinkUnlink"), [Import links](/Std_LinkImport "Std LinkImport"), [Import all links](/Std_LinkImportAll "Std LinkImportAll")
    * **[Expression actions](/Std_Expressions "Std Expressions"):** [Copy selected](/Std_Expressions#Copy_selected "Std Expressions"), [Copy active document](/Std_Expressions#Copy_active_document "Std Expressions"), [Copy all documents](/Std_Expressions#Copy_all_documents "Std Expressions"), [Paste](/Std_Expressions#Paste "Std Expressions")
    * **[Selection filter](/Part_SelectFilter "Part SelectFilter"):** [Vertex selection](/Part_SelectFilter#Vertex_selection "Part SelectFilter"), [Edge selection](/Part_SelectFilter#Edge_selection "Part SelectFilter"), [Face selection](/Part_SelectFilter#Face_selection "Part SelectFilter"), [All selection filters cleared](/Part_SelectFilter#All_selection_filters_cleared "Part SelectFilter")

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** Addon Manager, [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

