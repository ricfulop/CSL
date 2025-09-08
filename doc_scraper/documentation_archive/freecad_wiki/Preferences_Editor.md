---
url: https://wiki.freecad.org/Preferences_Editor
title: Preferences Editor
scraped_at: 2025-09-08 16:45:46
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 General Toggle General subsection
    * 2.1 General
    * 2.2 Document
    * 2.3 Selection
    * 2.4 Cache
    * 2.5 Notification Area
    * 2.6 Report View
    * 2.7 Help
  * 3 Display Toggle Display subsection
    * 3.1 3D View
    * 3.2 Light Sources
    * 3.3 UI
    * 3.4 Navigation
    * 3.5 Colors
    * 3.6 Advanced
    * 3.7 Mesh View
  * 4 Workbenches Toggle Workbenches subsection
    * 4.1 Available Workbenches
  * 5 Python Toggle Python subsection
    * 5.1 Macro
    * 5.2 General
    * 5.3 Editor
  * 6 Addon Manager Toggle Addon Manager subsection
    * 6.1 Addon Manager Options
  * 7 Import-Export
  * 8 Measure Toggle Measure subsection
    * 8.1 Appearance
  * 9 Workbench related preferences
  * 10 Scripting
  * 11 Related

# Preferences Editor

  * [Page](/Preferences_Editor "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Preferences_Editor&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Preferences_Editor)
  * [Edit](/index.php?title=Preferences_Editor&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Preferences_Editor&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Preferences_Editor.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Preferences_Editor&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Preferences_Editor)
  * [Edit](/index.php?title=Preferences_Editor&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Preferences_Editor&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Preferences_Editor&action=history)

General

  * [What links here](/Special:WhatLinksHere/Preferences_Editor "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Preferences_Editor "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Preferences_Editor&oldid=1633615 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Preferences_Editor&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Preferences_Editor&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Preferences+Editor&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Preferences+Editor&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Preferences_Editor/id "Preferences Editor \(8% translated\)")
  * [Deutsch](/Preferences_Editor/de "Voreinstellungseditor \(77% translated\)")
  * English
  * [Türkçe](/Preferences_Editor/tr "Seçenekler Penceresi \(5% translated\)")
  * [español](/Preferences_Editor/es "Editor de preferencias \(12% translated\)")
  * [français](/Preferences_Editor/fr "Réglage des préférences \(100% translated\)")
  * [hrvatski](/Preferences_Editor/hr "Uređivač postavki \(3% translated\)")
  * [italiano](/Preferences_Editor/it "Impostare le preferenze \(57% translated\)")
  * [polski](/Preferences_Editor/pl "Edytor ustawień \(100% translated\)")
  * [português](/Preferences_Editor/pt "Editor de preferências \(9% translated\)")
  * [português do Brasil](/Preferences_Editor/pt-br "Editor de Preferências \(28% translated\)")
  * [română](/Preferences_Editor/ro "Preferences Editor \(5% translated\)")
  * [svenska](/Preferences_Editor/sv "Preferences Editor \(8% translated\)")
  * [čeština](/Preferences_Editor/cs "Editor předvoleb \(8% translated\)")
  * [български](/Preferences_Editor/bg "Меню Настройки \(5% translated\)")
  * [русский](/Preferences_Editor/ru "Редактор настроек \(100% translated\)")
  * [українська](/Preferences_Editor/uk "Preferences Editor \(1% translated\)")
  * [中文](/Preferences_Editor/zh "设置用户首选项 \(5% translated\)")
  * [中文（中国大陆）](/Preferences_Editor/zh-cn "首选项编辑器 \(9% translated\)")
  * [中文（臺灣）](/Preferences_Editor/zh-tw "Preferences Editor/zh-tw \(7% translated\)")
  * [日本語](/Preferences_Editor/ja "Preferences Editor \(8% translated\)")
  * [한국어](/Preferences_Editor/ko "환경 설정 편집기\(Preferences Editor\) \(11% translated\)")

![](/images/6/6f/Arrow-left.svg) [Interface
Customization](/Interface_Customization "Interface Customization")

[Import Export Preferences](/Import_Export_Preferences "Import Export
Preferences") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

To start the **Preferences editor** select the **Edit → Preferences...**
option from the menu or ([introduced in 1.1](/Release_notes_1.1 "Release notes
1.1")) use the keyboard shortcut Ctrl+,. On macOS the **Preferences...**
option appears in the **FreeCAD** menu instead (this is the default place for
preferences on the Mac).

FreeCAD uses a workbench concept, where each workbench is responsible for
specific tasks and functions. A workbench can have its own preferences. These
will only appear in the Preferences editor, usually in a dedicated group, if
the workbench has been loaded in the current FreeCAD session. Some workbenches
add support for specific import and export formats. If there are any related
preferences they will appear on one or more additional pages in the Import-
Export group of the Preferences editor.

To preserve resources, FreeCAD does not automatically load all available
workbenches. See Workbenches for more information. For a list of workbench
related preferences see Workbench related preferences.

If no workbench is loaded, seven groups appear in the Preferences editor:
General, Display, Workbenches, Python, Addon Manager, Import-Export and
Measure. Any workbenches that have been loaded, and have their own
preferences, will appear below these.

Pressing the Reset button in the lower left corner of the Preferences dialog
opens a menu ([introduced in 1.0](/Release_notes_1.0 "Release notes 1.0"))
with options to reset preferences to their default values. You can reset the
current page, the current group, or all preferences. In 0.21 and below the
button will reset **all** preferences.

Some advanced preferences can only be changed in the [Parameter
editor](/Std_DlgParameter "Std DlgParameter"). The [Fine-tuning](/Fine-tuning
"Fine-tuning") page lists some of them.

This page has been updated for version 1.0.

## General

This preferences group has seven pages: General, Document, Selection, Cache,
Notification Area, Report view and Help.

In 0.21 and below the seventh page, Help, is only available if the [Help
Addon](https://github.com/FreeCAD/FreeCAD-Help) has been
[installed](/Std_AddonMgr "Std AddonMgr").

### General

[![](/images/thumb/2/27/Preferences_General_Page_General.png/400px-
Preferences_General_Page_General.png)](/index.php?title=File:Preferences_General_Page_General.png&filetimestamp=20240720115445&)

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Language** | Language of the application's user interface.   
**Default unit system** | Unit system for all parts of the application. [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0"): Used as the default for the [document unit system](/Std_ProjectInfo "Std ProjectInfo") of new documents. The active document's unit system overrides the default unit system unless the next option is checked.   
**Ignore project unit system and use default** [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0") | If checked, project unit systems are ignored and do not override the default unit system.   
**Number of decimals** | The number of decimals that should be shown for numbers and dimensions.   
**Minimum fractional inch** | The minimum fractional inch that should be shown for numbers and dimensions. Only available for unit systems with fractional inches.   
**Number format** | Specifies the number format. The options are: 

  * **Operating system** : The decimal separator defined by the operating system is used.
  * **Selected language** : The decimal separator of the selected FreeCAD interface language is used.
  * **C/POSIX** : A point is used as the decimal separator.

  
**Substitute decimal separator** | If checked, the numerical keypad decimal separator will be substituted with the separator defined by the **Number format** setting. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21"): Notice that if this preference is enabled, using the numerical keypad decimal separator will always print a dot/period in the [Python console](/Python_console "Python console") and the [Macro editor](/Std_DlgMacroExecute#Edit "Std DlgMacroExecute").   
**Theme** | Specifies a [theme](/Interface_Customization#Themes "Interface Customization") to customize the appearance of the user interface.   
**Size of toolbar icons** | Specifies the size of the toolbar icons. The options are: 

  * **Small (16px)**
  * **Medium (24px)**
  * **Large (32px)**
  * **Extra large (48px)**

  
**Tree view and Property view mode** | Defines how the Tree view is shown in the user interface (restart required). The options are: 

  * **Combined** : Combines the [Tree view](/Tree_view "Tree view") and the [Property view](/Property_editor "Property editor") into one [panel](/Combo_view "Combo view").
  * **Independent** : Splits the Tree view and the Property view into separate panels.

  
**Size of recent file list** | Specifies how many files should be listed in the recent files list. Optionally, imported files can be excluded from this list, and exported files can be included. See [Fine-tuning](/Fine-tuning "Fine-tuning").   
**Enable tiled background** | If checked, the background of FreeCAD's main window will by default consist of tiles of this image: [![](/images/thumb/2/26/Background.png/64px-Background.png)](/index.php?title=File:Background.png&filetimestamp=20131110000302&) This option only has an effect if no **Style sheet** is selected. The image can be changed by adding the folders Gui/Images in the folder: [%APPDATA%](https://www.howtogeek.com/318177/what-is-the-appdata-folder-in-windows/)/FreeCAD (on Windows), $HOME/.FreeCAD (on Linux) or $HOME/Library/Preferences/FreeCAD (on macOS). Place a file named background.png in the Images folder, and uncheck/check this option to see the changed file.   
**Enable splash screen at start up** | If checked, a splash screen is shown when starting FreeCAD. The splash screen image can be changed by placing a file named splash_image.png in the Images folder already mentioned under **Enable tiled background**.   
**Enable cursor blinking** | If checked the text cursor in the [Python console](/Python_console "Python console") and the [Macro editor](/Std_DlgMacroExecute#Edit "Std DlgMacroExecute") will blink.   
**Activate overlay handling** [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0") | If checked, docked windows can be handled as transparent overlays.   
**Preference packs** | Lists the available [preference packs](/Preference_Packs "Preference Packs") and also allows you to import, save, manage and revert them.   
  
### Document

[![](/images/thumb/f/ff/Preferences_General_Page_Document.png/400px-
Preferences_General_Page_Document.png)](/index.php?title=File:Preferences_General_Page_Document.png&filetimestamp=20240422195639&)

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Create new document at start up** | If checked, FreeCAD will create a new document when started.   
**Document save compression level** | Specifies the compression level for FCStd files. FCStd files are ZIP-compressed files. Therefore you can rename their suffix .FCStd to .zip and open them with a ZIP archive program.   
**Using Undo/Redo on documents** | If checked, all changes in documents are stored so that they can be undone/redone.   
**Maximum Undo/Redo steps** | Specifies how many Undo/Redo steps should be recorded.   
**Allow aborting recomputation** | If checked, recomputations can be aborted by pressing Esc. This may slightly increase the recomputation time.   
**Run AutoRecovery at startup** | If there is a recovery file available FreeCAD will automatically run a file recovery when it is started. This way files can be restored if a crash occurred.   
**Save AutoRecovery information every** | Specifies how often a recovery file is written.   
**Save thumbnail into project file when saving document** | If checked, a thumbnail will be stored when the document is saved. The thumbnail will for example be shown in the list of recent files on the Start page. It is possible to select a **Size** between 128×128 and 512×512 pixels for the thumbnail. Common sizes are powers of two: 128, 256, 512.   
**Add the program logo to the generated thumbnail** | If checked, the FreeCAD program logo [![](/images/0/06/Freecad.svg)](/index.php?title=File:Freecad.svg&filetimestamp=20240704193018&) will be added to the thumbnail.   
**Maximum number of backup files to keep when resaving document** | If checked, backup files will be kept when saving the document. You can specify the number of backup files to keep. Backup files are previously saved versions of the document.   
**Use date and FCBak extension** | If checked, backup files will get the extension .FCbak and their file names get a date suffix according to the specified **Date format**. For a description of the date format see [Date & time formats cheatsheet](https://devhints.io/datetime). With the default settings a backup file will for example get this name TD-Cube.20200315-215654.FCBak (original filename is TD-Cube.FCStd).   
**Allow duplicate object labels in one document** | If checked, objects can have the same label.   
**Disable partial loading of external linked objects** | If partial loading of external linked objects is enabled, only the referenced objects and their dependencies will be loaded when the linked document is auto opened together with the main document. Such a partially loaded document cannot be edited. Double click the document icon in the tree view to reload it in full. A more detailed explanation of this feature can be found on the [Assembly3 documentation page](https://github.com/realthunder/FreeCAD_assembly3/wiki/Core-Changes#partial-document-loading).   
**Author name** | All created documents will get the specified author name. Keep the author field blank if you do not want to include this information. If the option **Set on save** is checked, the field **Last modified by** will be set to the specified author when saving the file. This field can be viewed using the **File → Project information** menu option.   
**Company** | All created documents will get the specified company name.   
**Default license** | Specifies the license for new documents. For predefined licenses the **License URL** will automatically be set accordingly. Select **Other** for a custom license.   
**License URL** | Specifies an URL describing the license selected in **Default license**.   
  
### Selection

[![](/images/thumb/4/49/Preferences_General_Page_Selection.png/400px-
Preferences_General_Page_Selection.png)](/index.php?title=File:Preferences_General_Page_Selection.png&filetimestamp=20250610104409&)

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Enable preselection** | If checked, [3D view](/3D_view "3D view") preselection is turned on and the specified color will be used for it. Preselection means that for example edges of objects will be highlighted while hovering over them with the mouse to indicate they can be selected.   
**Enable selection** | If checked, 3D view selection is turned on and the specified color is used for it. If not checked, objects can only be selected in the [Tree view](/Tree_view "Tree view"). Note that objects created while this option is not checked will have their View**Selectable** property set to `false`. With that value they are not selectable in the 3D view, even if this option is checked again.   
**Radius** | Sets the area for picking elements in the [3D view](/3D_view "3D view"). A larger value (in px) makes it easier to pick things, but can make some small features impossible to select.   
**Preselect the object in 3D view when hovering the cursor over the tree item** | Enables the [Tree view PreSelection mode](/Std_TreePreSelection "Std TreePreSelection").   
**Auto switch to the 3D view containing the selected item** | Enables the [Tree view SyncView mode](/Std_TreeSyncView "Std TreeSyncView").   
**Auto expand tree item when the corresponding object is selected in 3D view** | Enables the [Tree view SyncSelection mode](/Std_TreeSyncSelection "Std TreeSyncSelection").   
**Record selection in tree view in order to go back/forward using navigation button** | Enables the [Tree view RecordSelection mode](/Std_TreeRecordSelection "Std TreeRecordSelection").   
**Add checkboxes for selection in document tree** | Each [Tree view](/Tree_view "Tree view") item will get a checkbox. This is for example useful for selecting multiple items on a touchscreen.   
  
### Cache

[![](/images/thumb/9/9f/Preferences_General_Page_Cache.png/400px-
Preferences_General_Page_Cache.png)](/index.php?title=File:Preferences_General_Page_Cache.png&filetimestamp=20240624131811&)

These preferences are related to the cache directory where FreeCAD stores
temporary files.

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Location (read-only)** | Shows the path of the cache directory. Use the [![](/images/4/4f/Document-open.svg)](/index.php?title=File:Document-open.svg&filetimestamp=20240704191852&) button to browse the directory.   
**Check periodically at program start** | Controls the frequency with which the directory size is checked. The options are: 

  * **Always**
  * **Daily**
  * **Weekly**
  * **Monthly**
  * **Yearly**
  * **Never**

  
**Cache size limit** | Specifies the maximum size of the directory. You will be notified if a check is performed and the size exceeds this value. The options are: 

  * **100 MB**
  * **300 MB**
  * **500 MB**
  * **1 GB**
  * **2 GB**
  * **3 GB**

  
**Current cache size** | Shows the current size of the directory, if available. Press the Check now... button to update the value.   
  
### Notification Area

[![](/images/thumb/7/72/Preferences_General_Page_Notification_Area.png/400px-
Preferences_General_Page_Notification_Area.png)](/index.php?title=File:Preferences_General_Page_Notification_Area.png&filetimestamp=20250610104744&)

These preferences control the Notification Area and its notifications.

On this page ([introduced in 0.21](/Release_notes_0.21 "Release notes 0.21"))
you can specify the following:

Name  | CollapseDescription   
---|---  
**Enable notification area** | If checked, the Notification Area will appear in the status bar.   
**Debug errors** | If checked, errors intended for developers will appear in the Notification Area.   
**Debug warnings** | If checked, warnings intended for developers will appear in the Notification Area.   
**Maximum notification count** | Limits the number of notifications that will be kept in the list. If 0, there is no limit.   
**Auto-remove user notifications** | If checked, notifications will be removed from the message list when the **Maximum Duration** has elapsed.   
**Enable pop-up notifications** | If checked, non-intrusive pop-up notifications will appear above the status bar.   
**Maximum duration** | Maximum duration during which notifications are shown (unless mouse buttons are clicked).   
**Minimum duration** | Minimum duration (idem).   
**Maximum concurrent notification count** | Maximum number of notifications that will be simultaneously present in the notification bubble.   
**Notification bubble width** | Width of the pop-up notification bubble in pixels.   
**Hide when other window is activated** | If checked, open notifications will disappear when another window is activated.   
**Do not show when window is inactive** | If checked, notifications will not appear if the FreeCAD window is not the active window.   
  
### Report View

[![](/images/thumb/6/67/Preferences_General_Page_Report_view.png/400px-
Preferences_General_Page_Report_view.png)](/index.php?title=File:Preferences_General_Page_Report_view.png&filetimestamp=20240422195728&)

These preferences control the behavior of the [Report view](/Report_view
"Report view"). This panel can be opened using the **View → Panels → Report
view** menu option.

The Report view uses the same font settings as the Macro editor.

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Record normal messages** | If checked, normal messages will be recorded. They will be displayed in the [Report view](/Report_view "Report view") with the color set in **Normal messages**.   
**Record log messages** | If checked, log messages will be recorded. They will be displayed in the [Report view](/Report_view "Report view") with the color set in **Log messages**.   
**Record warnings** | If checked, warnings will be recorded. They will be displayed in the [Report view](/Report_view "Report view") with the color set in **Warnings**.   
**Record error messages** | If checked, error messages will be recorded. They will be displayed in the [Report view](/Report_view "Report view") with the color set in **Errors**.   
**Show report view on error** | If checked, the [Report view](/Report_view "Report view") will be shown automatically when an error is recorded.   
**Show report view on warning** | If checked, the [Report view](/Report_view "Report view") will be shown automatically when a warning is recorded.   
**Show report view on normal message** | If checked, the [Report view](/Report_view "Report view") will be shown automatically when a normal message is recorded.   
**Show report view on log message** | If checked, the [Report view](/Report_view "Report view") will be shown automatically when a log message is recorded.   
**Include a timecode for each entry** | If checked, each message and warning will receive a timecode.   
**Normal messages** | Specifies the font color for normal messages.   
**Log messages** | Specifies the font color for log messages.   
**Warnings** | Specifies the font color for warning messages.   
**Errors** | Specifies the font color for error messages.   
**Redirect internal Python output to report view** | If checked, internal Python output will be redirected from the [Python console](/Python_console "Python console") to the [Report view](/Report_view "Report view").   
**Redirect internal Python errors to report view** | If checked, internal Python error messages will be redirected from the [Python console](/Python_console "Python console") to the [Report view](/Report_view "Report view").   
  
### Help

[![](/images/thumb/4/44/Preferences_General_Page_Help.png/400px-
Preferences_General_Page_Help.png)](/index.php?title=File:Preferences_General_Page_Help.png&filetimestamp=20240517105829&)

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Source** | Specifies the source of the Help files. The options are: 

  * **FreeCAD Wiki (online)** :
  * **Markdown version (online)** :
  * **GitHub (online)** : Cannot be selected.
  * **Custom location** : Enter the path where the downloaded FreeCAD documentation can be found. To download the documentation select the _offline-documentation_ addon from the Workbenches list in the [Addon Manager](/Std_AddonMgr "Std AddonMgr").

**Translation suffix** : For the Wiki option and the Markdown option a
[language suffix](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) can
be specified. Use for example `fr` for the French translation.  
**Display** | Specifies where the documentation should be displayed. The options are: 

  * **In your default web browser** : The documentation is displayed in the default web browser.
  * **In a FreeCAD tab** : The documentation is displayed on a new tab in the [Main view area](/Main_view_area "Main view area"). [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0"): Can no longer be used.
  * **In a separate, embeddable, dialog** : The documentation is displayed in a separate dialog. This dialog can be docked on top of the [Combo view](/Combo_view "Combo view") for example. [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0"): Can no longer be used.

  
**Custom stylesheet** | Specifies an optional custom stylesheet. Not used for the Wiki.   
  
## Display

This preferences group has six standard pages: 3D View, Light Sources, UI,
Navigation, Colors and Advanced. A seventh page, Mesh view, is added if the
[Mesh Workbench](/Mesh_Workbench "Mesh Workbench") has been loaded.

### 3D View

[![](/images/thumb/8/80/Preferences_Display_Page_3D_View.png/400px-
Preferences_Display_Page_3D_View.png)](/index.php?title=File:Preferences_Display_Page_3D_View.png&filetimestamp=20250610110413&)

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Show coordinate system in the corner** | If checked, the main coordinate system will be shown in the lower right corner of the [3D view](/3D_view "3D view"). The **Relative size** defines the size of the representation as a percentage of the view size (the minimum of its height and width). The **Letter color** defines the color of the axis letters. [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1"): The **X-axis color** , **Y-axis color** and **Z-axis color** define the colors of the axes.   
**Show axis cross by default** | If checked, the axis cross will be shown by default in the [3D view](/3D_view "3D view").   
**Show counter of frames per second** | If checked, the time needed for the last operation and the resulting [frame rate](https://en.wikipedia.org/wiki/Frame_rate) will be shown in the lower left corner of the [3D view](/3D_view "3D view").   
**Use software OpenGL** | If checked, [OpenGL](https://en.wikipedia.org/wiki/OpenGL) will use the CPU instead of the GPU. This option is useful for troubleshooting graphics card and driver problems. Changing this option requires a restart of the application.   
**Use OpenGL VBO (Vertex Buffer Object)** | If checked, [Vertex Buffer Objects](https://en.wikipedia.org/wiki/Vertex_Buffer_Object) (VBO) will be used. A VBO is an [OpenGL](https://en.wikipedia.org/wiki/OpenGL) feature that provides methods for uploading vertex data (position, normal vector, color, etc.) to the graphics card. VBOs offer substantial performance gains because the data resides in the graphics memory rather than the system memory and so it can be rendered directly by the GPU. For more background info see [Understanding OpenGL Objects](https://www.haroldserrano.com/blog/understanding-opengl-objects).   
**Render Cache** | "Render Cache" or "Render Acceleration" is explained in more detail in [FreeCAD assembly3 render-caching](https://github.com/realthunder/FreeCAD_assembly3/wiki/Link#render-caching). The options are: 

  * **Auto** : Let Coin3D decide where to cache (default).
  * **Distributed** : Manually turn on cache for all view provider root nodes.
  * **Centralized** : Manually turn off cache in all nodes of all view providers, and only cache at the scene graph root node. This offers the fastest rendering speed, but slower response to any scene changes.

  
**Anti-Aliasing** | Specifies if and what type of [multisample anti-aliasing](https://en.wikipedia.org/wiki/Multisample_anti-aliasing) is used   
**Transparent objects** | Specifies the render type of transparent objects. The options are: 

  * **One pass** : Rendering is done in one pass (default). This can lead to triangular artifacts. If these occur the type **Backface pass** can be used to avoid them.
  * **Backface pass** : Rendering is done in two passes. Back-facing polygons are rendered in the first pass and front-facing polygons in the second pass.

  
**Marker size** | Specifies the size of [vertices](/Glossary#Vertex "Glossary") (points) in the [Sketcher Workbench](/Sketcher_Workbench "Sketcher Workbench"). The clickable area of points can be additionally enlarged by increasing the **Pick radius**.   
**Eye to eye distance for stereo modes** | Specifies the eye-to-eye distance used for stereo projections. The specified value is a factor that will be multiplied with the [bounding box](/Property_editor#View "Property editor") size of the 3D object that is currently displayed.   
**Camera type** | Specifies the camera projection type. The options are: 

  * **Perspective rendering** : Objects will appear in a [perspective projection](/Std_PerspectiveCamera "Std PerspectiveCamera").
  * **Orthographic rendering** : Objects will be appear in an [orthographic projection](/Std_OrthographicCamera "Std OrthographicCamera").

  
  
### Light Sources

[introduced in 1.0](/Release_notes_1.0 "Release notes 1.0"), page updated for
1.1

[![](/images/thumb/c/c6/Preferences_Display_Page_Light_Sources.png/400px-
Preferences_Display_Page_Light_Sources.png)](/index.php?title=File:Preferences_Display_Page_Light_Sources.png&filetimestamp=20250610110533&)

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Main Light** | If checked, the objects in the [3D view](/3D_view "3D view") are lit by main light source of three-point lighting from given Horizontal Angle and Vertical Angle. The specified Color and Intensity will be used for it.   
**Back Light** | If checked, the objects in the [3D view](/3D_view "3D view") are lit by back light source of three-point lighting from given Horizontal Angle and Vertical Angle. The specified Color and Intensity will be used for it.   
**Fill Light** | If checked, the objects in the [3D view](/3D_view "3D view") are lit by fill light source of three-point lighting from given Horizontal Angle and Vertical Angle. The specified Color and Intensity will be used for it.   
**Ambient Light** | Color and Intensity settings for ambient light.   
**Preview** | The preview shows a sphere lit by the currently enabled lights. You can zoom the preview in and out with the buttons in the lower left corner.   
  
### UI

[introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

[![](/images/thumb/2/28/Preferences_Display_Page_UI.png/400px-
Preferences_Display_Page_UI.png)](/index.php?title=File:Preferences_Display_Page_UI.png&filetimestamp=20240907090659&)

### Navigation

[![](/images/thumb/9/9a/Preferences_Display_Page_Navigation.png/400px-
Preferences_Display_Page_Navigation.png)](/index.php?title=File:Preferences_Display_Page_Navigation.png&filetimestamp=20250610111528&)

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Navigation cube** | If checked, the [Navigation cube](/Navigation_Cube "Navigation Cube") is shown in the [3D view](/3D_view "3D view"). **Steps by turn** defines the number of steps required for a full rotation when using the Navigation cube rotation arrows. If **Rotate to nearest** is checked, the 3D view is rotated to the nearest most logical position, based on the current orientation of the cube, when a cube face is clicked. Else clicking a face will always result in the same rotation. **Cube size** defines the size of the cube. **Color** sets the base color for all elements. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21") **Corner** defines where the Navigation cube is displayed in the [3D view](/3D_view "3D view"). The options are: 

  * **Top left**
  * **Top right**
  * **Bottom left**
  * **Bottom right**

**Font name** specifies the font used for the cube's texts. [introduced in
0.21](/Release_notes_0.21 "Release notes 0.21") **Opacity when inactive**
Opacity of the Navigation cube when not hovered by the mouse. [introduced in
1.0](/Release_notes_1.0 "Release notes 1.0")  
**Rotation center indicator** [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0") | If checked, the rotation center of the view is shown when dragging. The **Sphere size** and the **Color and transparency** of the indicator can be specified.   
**3D Navigation** | Specifies a [mouse navigation style](/Mouse_navigation "Mouse navigation"). To see the details of each style, select it and then press the Mouse... button.   
**Orbit style** | Specifies the rotation orbit style used when in rotation mode. The options are: 

  * **Turntable** : Moving the mouse will divide the rotation in steps, rotations around the different axes are performed sequentially.
  * **Trackball** : Rotations around the different axes are performed simultaneously.
  * **Free Turntable** : Like **Trackball** , but if possible the rotation axis is kept collinear with the global 3D view axis. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")
  * **Trackball Classic** : [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")
  * **Rounded Arcball** : [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")

  
**Rotation mode** | Defines the rotation center. The options are: 

  * **Window center**
  * **Drag at cursor**
  * **Object center**

  
**Default camera orientation** | Specifies the camera orientation for new documents. This setting is also used by the [Std ViewHome](/Std_ViewHome "Std ViewHome") command.   
**Camera zoom** | Affects the initial camera zoom level for new documents. The value you set is the diameter of a sphere that fits in the [3D view](/3D_view "3D view"). The default is 100 mm. It also sets the initial size of origin features (base planes in new [PartDesign Bodies](/PartDesign_Body "PartDesign Body") and [Std Parts](/Std_Part "Std Part")).   
**Zoom at cursor** | If checked, zoom operations will be performed at the position of the mouse pointer. Otherwise zoom operations will be performed at the center of the current view. The **Zoom step** defines how much will be zoomed. A zoom step of **1** means a factor of 7.5 for every zoom step.   
**Invert zoom** | If checked, the direction of zoom operations will be inverted.   
**Disable touchscreen tilt gesture** | If checked, and **3D Navigation** is set to **Gesture** , the tilting gesture will be disabled for pinch-zooming (two-finger zooming).   
**Enable support of legacy space mouse devices** [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1") | If checked, legacy space mouse devices can be used.   
**Animations** | If checked, view rotations and zooms, except those invoked by mouse actions, are animated. The **Animation duration** can be specified. **Enable spinning animations** if checked, and if **3D Navigation** is set to **CAD** , rotations invoked by the mouse can be animated as well. If the mouse is moved while the scroll wheel and the right mouse button are pressed, the view is rotated. If one keeps the mouse moving while releasing the right mouse button, the rotation will continue. To end this animation left-click with the mouse.   
  
### Colors

[![](/images/thumb/0/01/Preferences_Display_Page_Colors.png/400px-
Preferences_Display_Page_Colors.png)](/index.php?title=File:Preferences_Display_Page_Colors.png&filetimestamp=20240422195401&)

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Simple color** | If selected, the background of the [3D view](/3D_view "3D view") will have the specified color.   
**Linear gradient** | If selected, the background of the [3D view](/3D_view "3D view") will have a vertical color gradient defined by the specified **Top** and **Bottom** colors. if enabled, a **Middle** color can also be specified. Press the [![](/images/c/cc/Button_sort.svg)](/index.php?title=File:Button_sort.svg&filetimestamp=20240704190908&) button ([introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")) to switch the top and bottom colors.   
**Radial gradient** [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21") | If selected, the background of the [3D view](/3D_view "3D view") will have a radial color gradient defined by the specified **Central** and **End** colors. if enabled, a **Midway** color can also be specified. Press the [![](/images/c/cc/Button_sort.svg)](/index.php?title=File:Button_sort.svg&filetimestamp=20240704190908&) button to switch the central and end colors.   
**Object being edited** | Specifies the background color for objects in the tree view that are currently edited.   
**Active container** | Specifies the background color for active containers in the tree view. For example an [active PartDesign Body](/PartDesign_Body#Active_Status "PartDesign Body") will get this color.   
**Label text color** | The color used for the labels of the color bar. The color bar is used in the [Mesh Workbench](/Mesh_Workbench "Mesh Workbench") and [FEM Workbench](/FEM_Workbench "FEM Workbench").   
**Label text size** | The size of those labels.   
  
### Advanced

[introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

[![](/images/thumb/2/27/Preferences_Display_Page_Advanced.png/400px-
Preferences_Display_Page_Advanced.png)](/index.php?title=File:Preferences_Display_Page_Advanced.png&filetimestamp=20240704145002&)

### Mesh View

[![](/images/thumb/e/e7/Preferences_Display_Page_Mesh_view.png/400px-
Preferences_Display_Page_Mesh_view.png)](/index.php?title=File:Preferences_Display_Page_Mesh_view.png&filetimestamp=20240422195416&)

This page is only available if the [Mesh Workbench](/Mesh_Workbench "Mesh
Workbench") has been loaded.

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Default mesh color** | Specifies the default face color.   
**Default line color** | Specifies the default line color.   
**Mesh transparency** | Specifies the default mesh transparency.   
**Line transparency** | Specifies the default line transparency.   
**Two-side rendering** | If checked, the default value for the View**Lighting** property is `Two side` instead of `One side`. `Two side` means the color of the interior side of faces is the same as the color of the exterior side. `One side` means their color is either the backlight color, if enabled, or black.   
**Show bounding-box for highlighted or selected meshes** | If checked, the default value for the View**Selection Style** property is `BoundBox` instead of `Shape`. `BoundBox` means a highlighted bounding box is displayed if meshes are highlighted or selected. `Shape` means the shape itself is then highlighted.   
**Define normal per vertex** | If checked, [Phong shading](https://en.wikipedia.org/wiki/Phong_shading) is used, otherwise flat shading. Shading defines the appearance of surfaces. With flat shading the surface normals are not defined per vertex. This leads to an unrealistic appearance for curved surfaces. While Phong shading leads to a more realistic, smoother appearance.   
**Crease angle** | The crease angle is a threshold angle between two faces. It can only be set if the option **Define normal per vertex** is used. 

    If face angle ≥ crease angle, facet shading is used.
    If face angle < crease angle, smooth shading is used.  
  
## Workbenches

This preferences group has a single page: Available Workbenches.

### Available Workbenches

[![](/images/thumb/7/79/Preferences_Workbenches_Page_Available_Workbenches.png/400px-
Preferences_Workbenches_Page_Available_Workbenches.png)](/index.php?title=File:Preferences_Workbenches_Page_Available_Workbenches.png&filetimestamp=20250610111719&)

These preferences control workbench loading.

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Workbench list** | The list displays all installed workbenches. The list can be reordered by drag and drop ([introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")) and sorted by right-clicking the list and selecting **Sort alphabetically** ([introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")). The order of the list also determines the order of the [Workbench selector](/Std_Workbench "Std Workbench"). 

  * [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21"): **First checkbox in each row** : If checked, the workbench will be available in the Workbench selector in the next FreeCAD session. The start up workbench cannot be unchecked. Unchecked workbenches are moved to the bottom of the list.
  * **Auto-load** : If checked, the workbench will auto-load when FreeCAD starts. Loading more workbenches will make the start up slower, but switching between workbenches that have already been loaded is faster.
  * Load: Press this button to load the workbench in the current FreeCAD session.

  
**Workbench selector items style** [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0") | The options are: 

  * **Icon & Text**
  * **Icon**
  * **Text**

  
**Workbench selector type** [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0") | The options are: 

  * **ComboBox** : Workbenches can be selected from a dropdown list.
  * **TabBar** : Workbenches can be selected from a tab bar. This takes fewer clicks than the previous option, but takes up more screen space.

  
**Start up workbench** | The workbench that is activated when FreeCAD starts.   
**Remember active workbench by tab** | If checked, FreeCAD will remember and restore the workbench that was active for each tab in the [Main view area](/Main_view_area "Main view area").   
  
## Python

This preferences group ([introduced in 0.21](/Release_notes_0.21 "Release
notes 0.21")) has three pages: Macro, General and Editor.

### Macro

[![](/images/thumb/8/88/Preferences_Python_Page_Macro.png/400px-
Preferences_Python_Page_Macro.png)](/index.php?title=File:Preferences_Python_Page_Macro.png&filetimestamp=20240422195811&)

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Run macros in local environment** | If checked, variables defined by macros are created as local variables, otherwise as global Python variables.   
**Macro path** | Specifies the path for macro files.   
**Record GUI commands** | If checked, [recorded macros](/Std_DlgMacroRecord "Std DlgMacroRecord") will also contain user interface commands.   
**Record as comment** | If checked, [recorded macros](/Std_DlgMacroRecord "Std DlgMacroRecord") will also contain user interface commands, but as comments. This is useful if you don't want to execute these commands when running the macro, but do want to see what has been done while recording.   
**Show script commands in python console** | If checked, the commands executed by macro scripts are shown in the Python console. This console can be opened using the **View → Panels → Python console** menu option.   
**Size of recent macro list** | Controls the number of recent macros to display in the menu.   
**Shortcut count** | Controls the number of recent macros that get dynamically assigned shortcuts.   
**Keyboard Modifiers** | Controls which keyboard modifiers are used for the shortcuts, example **Ctrl+Shift+** creates shortcuts in the form of **Ctrl+Shift+1** , **Ctrl+Shift+2** , etc.   
  
### General

[![](/images/thumb/e/e0/Preferences_Python_Page_General.png/400px-
Preferences_Python_Page_General.png)](/index.php?title=File:Preferences_Python_Page_General.png&filetimestamp=20240422195759&)

These preferences control the behavior of the [Python console](/Python_console
"Python console"). This console can be opened using the **View → Panels →
Python console** menu option.

Note that the color and font settings for the console are defined on the
Editor page.

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Enable word wrap** | If checked, words will be wrapped if they exceed the available horizontal space in the console.   
**Enable block cursor** | If checked, the cursor will have a block shape.   
**Save history** | If checked, Python history is saved across sessions.   
**Python profiler interval (milliseconds)** [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0") | The interval at which the profiler runs when there is Python code running (to keep the GUI responding). Set to 0 to disable.   
**Path to external Python executable (optional)** | Used for package installation with pip and debugging with debugpy. Autodetected if needed and not specified.   
  
### Editor

[![](/images/thumb/e/e1/Preferences_Python_Page_Editor.png/400px-
Preferences_Python_Page_Editor.png)](/index.php?title=File:Preferences_Python_Page_Editor.png&filetimestamp=20240422195749&)

These preferences control the behavior of the [Macro
editor](/Std_DlgMacroExecute#Edit "Std DlgMacroExecute"). This editor can be
opened using the **Macro → Macros... → Edit** or **Create** menu option.

The color and font settings are also used by the [Python
console](/Python_console "Python console"). The font settings are also used by
the [Report view](/Report_view "Report view").

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Enable line numbers** | If checked, the code lines will be numbered.   
**Enable block cursor** | If checked, the cursor will have a block shape.   
**Tab size** | Specifies the tabulator raster (how many spaces). If it is for example set to **6** , pressing Tab will jump to character 7 or 13 or 19 etc., depending on the current cursor position. This setting is only used if **Keep tabs** is selected.   
**Indent size** | Specifies how many spaces will be inserted when pressing Tab. This setting is only used if **Insert spaces** is selected.   
**Keep tabs** | If selected, pressing Tab will insert a tabulator with the raster defined by **Tab size**.   
**Insert spaces** | If selected, pressing Tab will insert the amount of spaces defined by **Indent size**.   
**Display Items** | Specifies the code type the color and font settings will be applied to. The result can be checked in the **Preview** field.   
**Family** | Specifies the font family that should be used for the selected code type.   
**Size** | Specifies the font size that should be used for the selected code type.   
**Color** | Specifies the color that should be used for the selected code type.   
  
## Addon Manager

This preferences group has a single page: Addon manager options.

### Addon Manager Options

[![](/images/thumb/a/a4/Preferences_Addon_Manager_Page_Addon_manager_options.png/400px-
Preferences_Addon_Manager_Page_Addon_manager_options.png)](/index.php?title=File:Preferences_Addon_Manager_Page_Addon_manager_options.png&filetimestamp=20240422195215&)

These preferences control the behavior of the [Addon manager](/Std_AddonMgr
"Std AddonMgr").

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Automatically check for updates at start (requires git)** | If checked, the Addon manager will check for updates when it is launched. Git must be installed for this to work.   
**Download Macro metadata (approximately 10MB)** | If checked, macro metadata is downloaded for display in the Addon manager's main addon listing. This data is cached locally.   
**Cache update frequency** | Controls the frequency with which the locally cached addon availability and metadata information is updated. The options are: 

  * **Manual (no automatic updates)**
  * **Daily**
  * **Weekly**

  
**Hide Addons without license** [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0") | If checked, addons without a license are not included in the listing.   
**Hide Addons with non-FSF Free/Libre license** [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0") | If checked, addons with a Free/Libre license not published by the [Free Software Foundation](https://www.fsf.org/licensing) are not included in the listing.   
**Hide Addons with non-OSI-approved license** [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0") | If checked, addons with a license not approved by the [Open Source Initiative](https://opensource.org/licenses) are not included in the listing.   
**Hide Addons marked Python 2 Only** | If checked, addons marked as "Python 2 Only" are not included in the listing. These addons are unlikely to work in the current FreeCAD version.   
**Hide Addons marked Obsolete** | If checked, addons marked as "Obsolete" are not included in the listing.   
**Hide Addons that require a newer version of FreeCAD** | If checked, addons that require a newer FreeCAD version are not included in the listing.   
**Custom repositories** | Custom repositories can be specified here. To add a repository press the [![](/images/8/8e/List-add.svg)](/index.php?title=File:List-add.svg&filetimestamp=20240522171753&) button. Both the **Repository URL** and the **Branch** , typically `master` or `main`, must be specifies in the dialog that opens. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21") To remove a repository select it in the list and press the [![](/images/1/17/List-remove.svg)](/index.php?title=File:List-remove.svg&filetimestamp=20240522171811&) button. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
**Proxy** | The Addon manager includes experimental support for proxies requiring authentication, set up as user-defined proxies.   
**Score source URL** [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0") | The URL for the Addon Score data. See [Std AddonMgr](/Std_AddonMgr#Sorting_by_score "Std AddonMgr") for formatting and hosting details.   
**Path to git executable (optional)** [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21") | The Addon manager attempts to determine the git executable. To override this selection, the path to the executable can be set here.   
**Show option to change branches (requires git)** | If checked, the Addon manager provides an interface on the addon's details screen that allows switching which git branch is currently checked out. This is intended for advanced users only, as it is possible that a non-primary-branch version of an addon may result in instability and compatibility issues. Git must be installed for this to work. Use with caution.   
**Disable git (fall back to ZIP downloads only)** [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21") | If checked, git downloads are disabled.   
**Addon developer mode** [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21") | If checked, Addon manager options intended for developers of addons are activated.   
  
## Import-Export

The Import-Export preferences affect how files are imported and exported. They
are described on the [Import Export Preferences](/Import_Export_Preferences
"Import Export Preferences") page.

## Measure

[introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

This preferences group has a single page: Appearance.

### Appearance

[![](/images/thumb/1/1c/Preferences_Measure_Page_Appearance.png/400px-
Preferences_Measure_Page_Appearance.png)](/index.php?title=File:Preferences_Measure_Page_Appearance.png&filetimestamp=20240624120738&)

On this page you can specify the following:

Name  | CollapseDescription   
---|---  
**Text size** | Specifies the size of the text in pixels.   
**Text color** | Specifies the color of the text.   
**Line color** | Specifies the color of the line connecting the text label with the measured element(s).   
**Background color** | Specifies the background color of the text label.   
  
## Workbench related preferences

Preferences for the built-in workbenches are linked below. These links are
also listed in [Category:Preferences](/Category:Preferences
"Category:Preferences"). Some workbenches have no preferences.

  * [Assembly Preferences](/Assembly_Preferences "Assembly Preferences")
  * [BIM Preferences](/BIM_Preferences "BIM Preferences")
  * [CAM Preferences](/CAM_Preferences "CAM Preferences")
  * [Draft Preferences](/Draft_Preferences "Draft Preferences")
  * [FEM Preferences](/FEM_Preferences "FEM Preferences")
  * Inspection Preferences (none)
  * [Material Preferences](/Material_Preferences "Material Preferences")
  * [Mesh Design Preferences](/Mesh_Workbench#Preferences "Mesh Workbench")
  * [OpenSCAD Preferences](/OpenSCAD_Preferences "OpenSCAD Preferences")
  * Part Preferences: the Part workbench also uses the [PartDesign Preferences](/PartDesign_Preferences "PartDesign Preferences")
  * [PartDesign Preferences](/PartDesign_Preferences "PartDesign Preferences")
  * Points Preferences (none)
  * Reverse Engineering Preferences (none)
  * Robot Preferences (none)
  * [Sketcher Preferences](/Sketcher_Preferences "Sketcher Preferences")
  * [Spreadsheet Preferences](/Spreadsheet_Preferences "Spreadsheet Preferences")
  * Surface Preferences (none)
  * [TechDraw Preferences](/TechDraw_Preferences "TechDraw Preferences")
  * Test Framework Preferences (none)

## Scripting

See [Std DlgParameter](/Std_DlgParameter#Scripting "Std DlgParameter").

## Related

  * [Parameter editor](/Std_DlgParameter "Std DlgParameter")
  * [Fine-tuning](/Fine-tuning "Fine-tuning")

  

![](/images/6/6f/Arrow-left.svg) [Interface
Customization](/Interface_Customization "Interface Customization")

[Import Export Preferences](/Import_Export_Preferences "Import Export
Preferences") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), Preferences, [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

