---
url: https://wiki.freecad.org/Interface_Customization
title: Interface Customization
scraped_at: 2025-09-08 16:43:46
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Usage
  * 3 Options Toggle Options subsection
    * 3.1 Keyboard
      * 3.1.1 Search
      * 3.1.2 Add a shortcut
      * 3.1.3 Remove a shortcut
      * 3.1.4 Restore a default shortcut
      * 3.1.5 Restore all default shortcuts
      * 3.1.6 Notes
    * 3.2 Toolbars
      * 3.2.1 Search
      * 3.2.2 Select the workbench
      * 3.2.3 Create a toolbar
      * 3.2.4 Rename a toolbar
      * 3.2.5 Delete a toolbar
      * 3.2.6 Disable a toolbar
      * 3.2.7 Add a command
      * 3.2.8 Remove a command
      * 3.2.9 Change a command position
      * 3.2.10 Notes
    * 3.3 Macros
      * 3.3.1 Add a macro command
      * 3.3.2 Remove a macro command
      * 3.3.3 Change a macro command
    * 3.4 Spaceball Motion
    * 3.5 Spaceball Buttons
  * 4 Themes
  * 5 Addons

# Interface Customization

  * [Page](/Interface_Customization "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Interface_Customization&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Interface_Customization)
  * [Edit](/index.php?title=Interface_Customization&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Interface_Customization&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Interface_Customization.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Interface_Customization&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Interface_Customization)
  * [Edit](/index.php?title=Interface_Customization&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Interface_Customization&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Interface_Customization&action=history)

General

  * [What links here](/Special:WhatLinksHere/Interface_Customization "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Interface_Customization "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Interface_Customization&oldid=1609241 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Interface_Customization&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Interface_Customization&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Interface+Customization&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Interface+Customization&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Interface_Customization/id "Interface Customization \(1% translated\)")
  * [Deutsch](/Interface_Customization/de "Anpassung der Oberfläche \(100% translated\)")
  * English
  * [Türkçe](/Interface_Customization/tr "Arayüz Özelleştirme \(1% translated\)")
  * [español](/Interface_Customization/es "Personalización del interfaz \(47% translated\)")
  * [français](/Interface_Customization/fr "Personnalisation de l'interface \(100% translated\)")
  * [hrvatski](/Interface_Customization/hr "Prilagođavanje sučelja \(15% translated\)")
  * [italiano](/Interface_Customization/it "Personalizzare l'interfaccia \(100% translated\)")
  * [polski](/Interface_Customization/pl "Dostosowywanie interfejsu użytkownika do własnych potrzeb \(100% translated\)")
  * [português](/Interface_Customization/pt "Interface Customization \(1% translated\)")
  * [português do Brasil](/Interface_Customization/pt-br "Personalização da interface \(18% translated\)")
  * [română](/Interface_Customization/ro "Personalizarea interfeţei \(1% translated\)")
  * [svenska](/Interface_Customization/sv "Interface Customization \(1% translated\)")
  * [čeština](/Interface_Customization/cs "Uživatelské nastavení \(1% translated\)")
  * [български](/Interface_Customization/bg "Настройки на Интерфейса \(1% translated\)")
  * [русский](/Interface_Customization/ru "Настройка интерфейса \(40% translated\)")
  * [українська](/Interface_Customization/uk "Interface Customization \(1% translated\)")
  * [中文](/Interface_Customization/zh "Interface Customization \(1% translated\)")
  * [中文（中国大陆）](/Interface_Customization/zh-cn "界面定制 \(1% translated\)")
  * [日本語](/Interface_Customization/ja "Interface Customization/ja \(0% translated\)")
  * [한국어](/Interface_Customization/ko "인터페이스 맞춤화 \(6% translated\)")

![](/images/6/6f/Arrow-left.svg) [Tutorials](/Tutorials "Tutorials")

[Preferences Editor](/Preferences_Editor "Preferences Editor")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

The FreeCAD interface is based on the modern
[Qt](https://en.wikipedia.org/wiki/Qt_\(toolkit\)) toolkit and has a state-of-
the-art organization. Some aspects of the interface can be customized. You
can, for example, add custom toolbars, with tools from several workbenches or
tools defined in macros, and you can create you own keyboard shortcuts. But
the menus and default toolbars that come with FreeCAD and its workbenches
cannot be changed.

[![](/images/f/f7/Std_DlgCustomize_tab_Toolbars.png)](/index.php?title=File:Std_DlgCustomize_tab_Toolbars.png&filetimestamp=20230605194424&)

The Customize dialog box

## Usage

  1. The commands available in the Customize dialog box depend on the workbenches that have been loaded in the current FreeCAD session. So you should first load all workbenches whose commands you want to have access to.
  2. There are several ways to invoke the [![](/images/0/0c/Std_DlgCustomize.svg)](/index.php?title=File:Std_DlgCustomize.svg&filetimestamp=20240704211946&) [Std DlgCustomize](/Std_DlgCustomize "Std DlgCustomize") command: 
     * Select the **Tools →[![](/images/0/0c/Std_DlgCustomize.svg)](/index.php?title=File:Std_DlgCustomize.svg&filetimestamp=20240704211946&) Customize...** option from the menu.
     * Right-click a toolbar area and choose **[![](/images/0/0c/Std_DlgCustomize.svg)](/index.php?title=File:Std_DlgCustomize.svg&filetimestamp=20240704211946&)Customize...** from the context menu.
  3. The **Customize** dialog box opens. For more information see Options.
  4. The Help button does not work at this time.
  5. Press the Close button to close the dialog box.

## Options

In the Customize dialog box the following tabs are available:

### Keyboard

[![](/images/3/3f/Std_DlgCustomize_tab_Keyboard.png)](/index.php?title=File:Std_DlgCustomize_tab_Keyboard.png&filetimestamp=20230605194453&)

The Keyboard tab

On this tab custom keyboard shortcuts can be defined. Shortcuts for macro
commands can be defined on the Macros tab.

#### Search

You can search for commands by entering at least 3 characters of their menu
text or name in the search field. The search is case-insensitive.

It is also possible to search for shortcuts:

  * In the search field special keys in shortcuts must be entered as strings. For example to search for commands that use Ctrl in their shortcut enter `ctrl` (4 letters).
  * Add parenthesis to search for single character shortcuts, for example: `(c)`.
  * Add a comma and space between the characters of multi-character shortcuts, for example: `g, b, b`.

#### Add a shortcut

  1. Select a command category from the **Category** dropdown list.
  2. Select a command from the **Commands** panel. 
     * Optionally click the `Command`, `Shortcut` or `Default` column headings to reorder the list.
     * Optionally drag the splitter to the right of the panel to resize it.
  3. The **Current shortcut** box displays the current short cut, if available.
  4. Enter a new shortcut in the **New shortcut** input box. Shortcuts can be up to 4 inputs long. Each input is either a single character, a combination of one or more special keys or a combination of one or more special keys and a character. Use Backspace to correct mistakes.
  5. Other active commands (see Notes) that already use the shortcut will be listed in the **Shortcut priority list**.
  6. Press the Assign button to assign the new shortcut.
  7. If the **Shortcut priority list** contains more than one command: optionally change its order by selecting individual commands and pressing the Up button or the Down button. If active commands share the same shortcut, the shortcut will trigger the one that is highest in the list.

#### Remove a shortcut

  1. Select a command category from the **Category** dropdown list.
  2. Select a command from the **Commands** panel.
  3. Press the Clear button.

#### Restore a default shortcut

  1. Select a command category from the **Category** dropdown list.
  2. Select a command from the **Commands** panel.
  3. Press the Reset button.

#### Restore all default shortcuts

  1. Press the Reset All button.

#### Notes

  * Shortcuts only work for active commands. Active commands are commands that appear in the standard menu, or in the menu of the active workbench, or commands that appear in a _visible_ toolbar.

Top

### Toolbars

[![](/images/f/f7/Std_DlgCustomize_tab_Toolbars.png)](/index.php?title=File:Std_DlgCustomize_tab_Toolbars.png&filetimestamp=20230605194424&)

The Toolbars tab

On this tab custom toolbars can be created and modified.

#### Search

See Keyboard.

#### Select the workbench

  1. In the dropdown list on the right select the workbench whose custom toolbars you want to modify. The `Global` option is there for custom toolbars that should be available in all workbenches.

#### Create a toolbar

  1. Press the New... button.
  2. Enter a name in the dialog box that opens.
  3. Press the OK button.
  4. The new toolbar will appear in the panel on the right.

#### Rename a toolbar

  1. Select a toolbar in the panel on the right.
  2. Press the Rename... button.
  3. Enter a new name in the dialog box that opens.
  4. Press the OK button.

#### Delete a toolbar

  1. Select a toolbar in the panel on the right.
  2. Press the Delete button.

#### Disable a toolbar

  1. Uncheck the checkbox in front of the toolbar name in the panel on the right.
  2. A disabled toolbar will be invisible in the FreeCAD interface.

#### Add a command

  1. At least one custom toolbar is required. See Create a toolbar.
  2. Select the correct toolbar in the panel on the right. If no toolbar is selected, the command will be added to the first toolbar in the list.
  3. Select a command category from the **Category** dropdown list. Macro commands that have been set up on the Macros tab appear in the `Macros` category.
  4. Select a command from the **Commands** panel, or select `<Separator>` to add a separator (a line between two toolbar buttons). 
     * Optionally drag the splitter to the right of the panel to resize it.
  5. Press [![](/images/5/52/Button_right.svg)](/index.php?title=File:Button_right.svg&filetimestamp=20240704191313&) button.

#### Remove a command

  1. If required, expand the toolbar in the panel on the right.
  2. Select a command.
  3. Press [![](/images/f/f6/Button_left.svg)](/index.php?title=File:Button_left.svg&filetimestamp=20240704191300&) button.

#### Change a command position

  1. If required, expand the toolbar in the panel on the right.
  2. Select a command.
  3. Press the [![](/images/8/82/Button_up.svg)](/index.php?title=File:Button_up.svg&filetimestamp=20240704191340&) button or the [![](/images/3/37/Button_down.svg)](/index.php?title=File:Button_down.svg&filetimestamp=20240704191234&) button.
  4. Optionally repeat this until the command is in the correct position.

#### Notes

  * Toolbars belonging to the current workbench are updated immediately, but after disabling/re-enabling a toolbar a workbench change is required (switch to a different workbench and then switch back).
  * To update global toolbars a workbench change (if commands have been added or removed) or a restart (if the order of a toolbar has changed or a toolbar was renamed) is required.

Top

### Macros

[![](/images/9/9c/Std_DlgCustomize_tab_Macros.png)](/index.php?title=File:Std_DlgCustomize_tab_Macros.png&filetimestamp=20230605194508&)

The Macros tab

On this tab macro commands can be set up. Once set up, they can be added to
custom toolbars. Macros installed with the
[![](/images/e/ee/Std_AddonMgr.svg)](/index.php?title=File:Std_AddonMgr.svg&filetimestamp=20240704212012&)
[Addon Manager](/Std_AddonMgr "Std AddonMgr") are set up automatically, and
added to a `Global` toolbar (see Toolbars), if you confirm the **Add button**
popup during the installation process.

If you want to use a macro downloaded from a different source you will have to
install it manually. See [How to install macros](/How_to_install_macros "How
to install macros") for more information. Note that FreeCAD uses a dedicated
folder for macros and only macros in that folder can be set up. Use the
[![](/images/b/b2/Std_DlgMacroExecute.svg)](/index.php?title=File:Std_DlgMacroExecute.svg&filetimestamp=20240704212406&)
[Std DlgMacroExecute](/Std_DlgMacroExecute "Std DlgMacroExecute") command to
find this folder on your system.

#### Add a macro command

  1. In the **Macro** dropdown list select a macro.
  2. Enter a **Menu text**. This will be the name used to identify the macro command and will also appear in the toolbar if there is no icon.
  3. Optionally enter a **Tool tip**. This text will appear near the location of the mouse when you hover the toolbar icon.
  4. Optionally enter a **Status text**. This text will appear in the [status bar](/Status_bar "Status bar") when you hover the toolbar icon.
  5. Optionally enter the wiki page for the macro, if available, in the **What's this** input box. Enter the page name, not the full URL.
  6. Optionally enter a shortcut in the **Accelerator** input box. See Keyboard for more information.
  7. To add an icon: 
     1. Press the **Pixmap** ... button.
     2. The **Choose Icon** dialog box opens.
     3. If required press the Icon folders... button to add an icon folder.
     4. Select an icon from the panel. The **Choose Icon** dialog box closes automatically.
  8. Press the Add button.
  9. The macro command appears in the panel on the left.
  10. The macro command can now be selected on the Toolbars tab.

#### Remove a macro command

  1. Select the macro command in the panel on the left.
  2. Press the Remove button.

#### Change a macro command

  1. Double-click the macro command in the panel on the left.
  2. Make the required changes. Note that you cannot remove the icon, you can only replace it.
  3. Press the Replace button.

Top

### Spaceball Motion

This tab is blank if no Spaceball is detected. See: [3Dconnexion input
devices](/3Dconnexion_input_devices "3Dconnexion input devices").

Top

### Spaceball Buttons

This tab is blank if no Spaceball is detected. See: [3Dconnexion input
devices](/3Dconnexion_input_devices "3Dconnexion input devices").

Top

## Themes

FreeCAD supports complete theming of the interface, via .qss stylesheets. The
[qss format](https://doc.qt.io/qt-5/stylesheet-syntax.html) is very similar to
the [css format](https://en.wikipedia.org/wiki/CSS) used in web pages, it
basically adds methods to reference the different widgets and elements of the
Qt interface. You can change the default theme (which simply takes the style
defined by your desktop system) by selecting a **style sheet** in the [FreeCAD
preferences](/Preferences_Editor#General "Preferences Editor").

You can also create your own theme if you are not satisfied with the themes
that are bundled with FreeCAD, for example by editing an [existing style
sheet](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets).
Your new style must be placed in a specific folder for it to be found by
FreeCAD:

  * %APPDATA%/FreeCAD/Gui/Stylesheets (on Windows). The %APPDATA% folder can be retrieved by entering `App.getUserAppDataDir()` in the [Python console](/Python_console "Python console").
  * $HOME/.FreeCAD/Gui/Stylesheets (on Linux).
  * $HOME/Library/Application Support/FreeCAD/Gui/Stylesheets (on macOS).

Top

## Addons

Addons from the
[![](/images/e/ee/Std_AddonMgr.svg)](/index.php?title=File:Std_AddonMgr.svg&filetimestamp=20240704212012&)
[Addon Manager](/Std_AddonMgr "Std AddonMgr") offer yet another way to
customize the user interface. Several dedicated [external
workbenches](/External_workbenches "External workbenches") and [Preference
Packs](/Preference_Packs "Preference Packs") are available.

Top

![](/images/6/6f/Arrow-left.svg) [Tutorials](/Tutorials "Tutorials")

[Preferences Editor](/Preferences_Editor "Preferences Editor")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

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

Expand[![](/images/0/06/Freecad.svg)](/index.php?title=File:Freecad.svg&filetimestamp=20240704193018&)
[Interface](/Interface "Interface")

  * [Preferences Editor](/Preferences_Editor "Preferences Editor"), Interface Customization
  * Main window: [Standard menu](/Standard_Menu "Standard Menu"), [Main view area](/Main_view_area "Main view area"), [3D view](/3D_view "3D view"), [Combo view](/Combo_view "Combo view") ([Tree view](/Tree_view "Tree view"), [Task panel](/Task_panel "Task panel"), [Property editor](/Property_editor "Property editor")), [Selection view](/Selection_view "Selection view"), [Report view](/Report_view "Report view"), [Python console](/Python_console "Python console"), [Status bar](/Status_bar "Status bar"), [DAG view](/DAG_view "DAG view"), [Workbench Selector](/Std_Workbench "Std Workbench")
  * Auxiliary windows: [Scene inspector](/Std_SceneInspector "Std SceneInspector"), [Dependency graph](/Std_DependencyGraph "Std DependencyGraph")

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

