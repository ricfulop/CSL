---
url: https://wiki.freecad.org/Python_console
title: Python console
scraped_at: 2025-09-08 16:46:07
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Scripting
  * 3 Context menu
  * 4 Notes

# Python Console

  * [Page](/Python_Console "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Python_Console&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Python_Console)
  * [Edit](/index.php?title=Python_Console&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Python_Console&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Python_Console.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Python_Console&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Python_Console)
  * [Edit](/index.php?title=Python_Console&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Python_Console&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Python_Console&action=history)

General

  * [What links here](/Special:WhatLinksHere/Python_Console "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Python_Console "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Python_Console&oldid=1634054 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Python_Console&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Python_Console&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Python+Console&action=page&filter=&language=en)(Redirected from [Python
console](/index.php?title=Python_console&redirect=no "Python console"))  
  
This is the approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Python+Console&language=&task=view "Start translation for this language")
  * [Deutsch](/Python_Console/de "Python-Konsole \(100% translated\)")
  * English
  * [español](/Python_Console/es "Consola de Python \(74% translated\)")
  * [français](/Python_Console/fr "Console Python \(95% translated\)")
  * [italiano](/Python_Console/it "Console Python \(84% translated\)")
  * [polski](/Python_Console/pl "Konsola Pythona \(100% translated\)")
  * [português do Brasil](/Python_Console/pt-br "Console Python \(11% translated\)")
  * [русский](/Python_Console/ru "Консоль Python \(11% translated\)")
  * [한국어](/Python_Console/ko "파이썬 콘솔\(Python console\) \(0% translated\)")

## Introduction

The Python Console is a panel that is part of the FreeCAD [user
interface](/Interface "Interface"). It runs an instance of the
[Python](/Python "Python") interpreter which can be used to control FreeCAD
processes, and create and modify objects and their properties.

It can be made visible/hidden through the **View → Panels → Python Console**
drop-down menu.

The Python Console in FreeCAD has basic syntax highlighting, to differentiate,
with various styles and colors, comments, strings, numeric values, built in
functions, printed text output, and delimiters like parentheses and commas.
These properties of the console can be configured in the [Preferences
Editor](/Preferences_Editor "Preferences Editor").

[![](/images/thumb/0/0b/FreeCAD_Python_console.png/600px-
FreeCAD_Python_console.png)](/index.php?title=File:FreeCAD_Python_console.png&filetimestamp=20190921064541&)

The Python Console showing messages when FreeCAD has just started.

## Scripting

_For absolute beginners, see:_ [Introduction to
Python](/Introduction_to_Python "Introduction to Python"), and [Python
scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial").

_See also:_ [FreeCAD scripting basics](/FreeCAD_Scripting_Basics "FreeCAD
Scripting Basics"), and [Scripted objects](/Scripted_objects "Scripted
objects").

The Python Console can perform basic code completion when a dot is written
after an object; it will show public methods and attributes (variables) of the
current object (class), for example, `obj.`

The console is also able to show the documentation string of a particular
function when the opening parenthesis is written, for example, `function(`

[![](/images/thumb/2/29/FreeCAD_Python_console_example.png/600px-
FreeCAD_Python_console_example.png)](/index.php?title=File:FreeCAD_Python_console_example.png&filetimestamp=20190921072538&)

Example Python code that produces objects in the 3D view.

The FreeCAD initialization scripts automatically load some modules, and define
some aliases. Therefore, in the Python Console these are available:

    
    
    App = FreeCAD
    Gui = FreeCADGui
    

Therefore these are equal:

    
    
    App.newDocument()
    FreeCAD.newDocument()
    

_Note:_ these pre-loaded modules and aliases are only available from the
Python Console embedded inside the FreeCAD program. If you use FreeCAD as a
library in an external program, you must remember to load the `FreeCAD` and
`FreeCADGui` modules and define the necessary aliases if you wish.

## Context menu

Right-clicking the Python Console opens a context menu with the following
commands:

  * **Copy** : stores the selected text in the clipboard for later pasting; it is disabled if nothing is selected.
  * **Copy Command** : stores the selected command in the clipboard for later pasting; it is disabled if nothing is selected.
  * **Copy History** : copy the entire history of Python commands entered in this session.
  * **Save History As…** : save the entire history of Python commands entered in this session to a text file.
  * **Save History** : TBD.
  * **Paste** : paste previously copied text in the clipboard to the Python Console.
  * **Select All** : selects all text in the Python Console.
  * **Clear Console** : erases all commands entered into the Python Console. This is useful if the Python Console is full of messages and previously entered commands that may be distracting when testing a new function. This is merely aesthetic, as this command doesn't delete existing variables nor clears the imported modules in the session.
  * **Insert File Name…** : opens a dialog to search for a file in the system, then it inserts the full path of the file. This is useful to test functions that process an input file, without having to write the entire name in the console, which is error prone. This command does not run the file, and does not import it as a Python module, it just returns the full path of that file.
  * **Word Wrap** : wrap very long lines that exceed the horizontal dimension of the Python Console.

## Notes

  * One has the ability to scroll the API in the Python Console. Example: 
    1. In the console type: `FreeCAD.`
    2. A dialog box will display with optional classes/functions to choose from
    3. Scroll through the list to read the description of each class/function
    4. By choosing a function and following it with a `.` one can repeat steps 2 and 3 to traverse deeper in to the API
  * Tab/Word completion is supported using the Ctrl+Space shortcut

  

Expand[![](/images/0/06/Freecad.svg)](/index.php?title=File:Freecad.svg&filetimestamp=20240704193018&)
[Interface](/Interface "Interface")

  * [Preferences Editor](/Preferences_Editor "Preferences Editor"), [Interface Customization](/Interface_Customization "Interface Customization")
  * Main window: [Standard menu](/Standard_Menu "Standard Menu"), [Main view area](/Main_view_area "Main view area"), [3D view](/3D_view "3D view"), [Combo view](/Combo_view "Combo view") ([Tree view](/Tree_view "Tree view"), [Task panel](/Task_panel "Task panel"), [Property editor](/Property_editor "Property editor")), [Selection view](/Selection_view "Selection view"), [Report view](/Report_view "Report view"), [Python console](/Python_console "Python console"), [Status bar](/Status_bar "Status bar"), [DAG view](/DAG_view "DAG view"), [Workbench Selector](/Std_Workbench "Std Workbench")
  * Auxiliary windows: [Scene inspector](/Std_SceneInspector "Std SceneInspector"), [Dependency graph](/Std_DependencyGraph "Std DependencyGraph")

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

  * **[Tools](/Std_Tools_Menu "Std Tools Menu"):** [Edit parameters](/Std_DlgParameter "Std DlgParameter"), [Save image](/Std_ViewScreenShot "Std ViewScreenShot"), [Load image](/Std_ViewLoadImage "Std ViewLoadImage"), [Scene inspector](/Std_SceneInspector "Std SceneInspector"), [Dependency graph](/Std_DependencyGraph "Std DependencyGraph"), [Export dependency graph](/Std_ExportDependencyGraph "Std ExportDependencyGraph"), [Document utility](/Std_ProjectUtil "Std ProjectUtil"), [Add text document](/Std_TextDocument "Std TextDocument"), [View turntable](/Std_DemoMode "Std DemoMode"), [Units converter](/Std_UnitsCalculator "Std UnitsCalculator"), [Customize](/Std_DlgCustomize "Std DlgCustomize"), [Addon manager](/Std_AddonMgr "Std AddonMgr"), [Measure](/Std_Measure "Std Measure")

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

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

