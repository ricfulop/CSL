---
url: https://developer.rhino3d.com/guides/rhinocommon/loading-tool-palettes-mac/#related-topics
scraped_at: 2025-09-08T16:07:49.954564
title: Untitled
---

[RhinoDeveloper®](/)

[design, model, present, analyze, realize...](/)

[![Rhino Logo](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account
](https://www.rhino3d.com/my-account/ "Manage your account, licenses, and
teams")

[Loading Tool Palettes
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/loading-tool-palettes-
mac/)

  * Prerequisites
  * Overview
  * Create or Convert A Tool Palette Collection
    * Creating from Scratch
    * Convert RUI to plist
  * Add the Palette to your Project
  * Load the Tool Palette
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Loading Tool Palettes (Mac)

__

macOS only

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) (Last updated:
Monday, May 9, 2022)

__DEPRECATED __

This guide covers information relevant to Rhino 5-7 for Mac. Rhino 8 is the
current shipping version.

For updated guides see:

  * [The Rhino UI System](https://developer.rhino3d.com/guides/general/rhino-ui-system/)
  * [Creating and Deploying Plugin Toolbars](https://developer.rhino3d.com/guides/rhinocommon/create-deploy-plugin-toolbar/)

## Prerequisites

This guide presumes that you have a RhinoCommon plugin that has commands that
can be run from a tool palette. In Rhino for Windows, this UI is normally
stored in an _rui_ file that includes the buttons, the icons, and their
associated commands. If you do not yet have a plugin, please begin with the
[Your First Plugin
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-
mac/) guide.

## Overview

There are three steps in creating and loading a tool palette collection for
your plugin in Rhino for Mac:

  1. The first step is to [create (or convert) a tool palette collection](https://developer.rhino3d.com/guides/rhinocommon/loading-tool-palettes-mac/#create-or-convert-a-tool-palette-collection) that calls the appropriate commands - or to convert a Rhino for Windows _.rui_ file - to _ToolPaletteCollection.plist_ file.
  2. The second step is to [add this _.plist_ in your plugin project](https://developer.rhino3d.com/guides/rhinocommon/loading-tool-palettes-mac/#add-the-palette-to-your-project) as a resource.
  3. The third and final step is to tell Rhino for Mac to [load the tool palette from the appropriate file](https://developer.rhino3d.com/guides/rhinocommon/loading-tool-palettes-mac/#load-the-tool-palette) when your plugin is being loaded.

## Create or Convert A Tool Palette Collection

If you are familiar with the [Command
Editor](http://docs.mcneel.com/rhino/mac/help/en-
us/index.htm#macpreferencesandsettings/commands.htm) in Rhino for Mac, you are
already well on your way to understanding how to create a custom tool palette
collection for use in your plugin. If not, don’t worry: creating a tool
palette collection is relatively easy.

If you already have an existing _rui_ file from Rhino for Windows, this job is
even easier: you can [import that _rui_ and convert it to a
_plist_](https://developer.rhino3d.com/guides/rhinocommon/loading-tool-
palettes-mac/#convert-rui-to-plist).

### Creating from Scratch

  1. Open Rhino - if it is not already open - and start a new modeling window.
  2. Enter the `TestEditToolPaletteCollection` command. (You will need to type the entire command; it will not autocomplete). This launches a developer tool similar to the Command Editor where tool palette collections can be created, organized, and saved to _plist_ files…
  3. By default, the `TestEditToolPaletteCollection` editor presumes you have a Rhino for Windows _rui_ file you would like to convert. A finder window opens where you can navigate to the _rui_ file to import.
  4. If you do not have a Rhino for Windows _rui_ file that you would like to convert, you will need to create your Tool Palette Collection “from scratch.” On the finder window, press _Cancel_. An interface much like the [Command Editor](http://docs.mcneel.com/rhino/mac/help/en-us/index.htm#macpreferencesandsettings/commands.htm) window appears. This is where you can create, configure, organize, and save your tool palette collection.
  5. Press the _+_ (add) button in the _Palette Browser_ … ![TestEditToolPaletteCollection](https://developer.rhino3d.com/images/loading-tool-palettes-mac-01.png)
  6. An _Untitled_ tool palette appears in the _Palette Browser_ (upper left). Click on the name of the _Untitled_ palette and give your tool palette a name… ![Name Tool Palette](https://developer.rhino3d.com/images/loading-tool-palettes-mac-02.png)
  7. In the _Command Button Browser_ (the area in the lower-left corner), click the _+_ button to _add a new button_. An _Untitled_ button should appear. Select it. ![Add a button](https://developer.rhino3d.com/images/loading-tool-palettes-mac-03.png)
  8. In the _Button Editor_ (area at lower-right), you can configure your button. Add a Text title, some Menu text, some informative tooltip, and - most importantly - the macro or command (from your plugin) that you wish to run when this button is clicked. ![Button Editor](https://developer.rhino3d.com/images/loading-tool-palettes-mac-04.png)
  9. You can drag new images onto the button icon displayed in the _Button Editor_. Rhino for Mac prefers PDF icons as they will scale nicely between Retina and non-Retina displays. If you do not have PDF assets for your icons, use 64 x 64 png images. ![Add a PNG](https://developer.rhino3d.com/images/loading-tool-palettes-mac-05.png)
  10. You may add as many buttons as you need to the _Command Button Browser_. These are the buttons that can be added to Tool Palettes.
  11. With the tool palette you want to add buttons to, drag buttons from the _Command Button Browser_ into the _Palette Contents_ area (top, center)… ![Add to Palette](https://developer.rhino3d.com/images/loading-tool-palettes-mac-07.png)
  12. When you are satisfied with the contents of your tool palette(s), you can save your converted tool palette collection to a _plist_ by clicking on the _Save_ button in the lower-right corner of the _Command Editor_ window.
  13. _NOTE_ : Should you want to make changes to this tool palette collection, you can always reload the tool palette collection by re-running the `TestEditToolPaletteCollection` command and opening the _plist_ file you created. In order to add a menu to a tool palette button you must save and reload the tool palette in order for the menu to show up in the available menus.

### Convert RUI to plist

  1. Open Rhino - if it is not already open - and start a new modeling window.
  2. Enter the `TestEditToolPaletteCollection` command. (You will need to type the entire command; it will not autocomplete). This launches a developer tool similar to the Command Editor where tool palette collections can be created, organized, and saved to _plist_ files…
  3. By default, the `TestEditToolPaletteCollection` editor presumes you have a Rhino for Windows _rui_ file you would like to convert. A finder window opens where you can navigate to the _rui_ file to import. Navigate to the folder containing your _rui_ , select it, click _Open_. Rhino for Mac imports this _rui_ and uses it as a template.
  4. The contents of your _rui_ should appear. Notice that there is a _Modified Tool Palette_ with the name of your toolbar(s)… ![Imported RUI](https://developer.rhino3d.com/images/loading-tool-palettes-mac-06.png)
  5. The buttons with their associated icons should appear in the _Command Button Browser_ (the area in the lower-left corner). If you select buttons in this area, you will notice their editable details appear in the _Button Editor_ (area at lower-right).
  6. You can drag new images onto the button icon displayed in the _Button Editor_. Rhino for Mac prefers PDF icons as they will scale nicely between Retina and non-Retina displays. If you do not have PDF assets for your icons, use 64 x 64 png images.
  7. With the tool palette you want to add buttons to, drag buttons from the _Command Button Browser_ into the _Palette Contents_ area (top, center)… ![Add to Palette](https://developer.rhino3d.com/images/loading-tool-palettes-mac-07.png)
  8. When you are satisfied with the contents of your tool palette(s), you can save your converted tool palette collection to a _plist_ by clicking on the _Save_ button in the lower-right corner of the _Command Editor_ window.
  9. _NOTE_ : Should you want to make changes to this tool palette collection, you can always reload the tool palette collection by re-running the `TestEditToolPaletteCollection` command and opening the _plist_ file you created. In order to add a menu to a tool palette button you must save and reload the tool palette in order for the menu to show up in the available menus.

## Add the Palette to your Project

Now that you have Tool Palette Collection _plist_ , you need to add it to your
plugin as a resource. The best practice is to create a folder within your
project called _Resources_ (or similar) and move your Tool Palette Collection
_plist_ into to that folder. _NOTE_ : You are free to place your _plist_
anywhere you think appropriate.

  1. Open _Visual Studio for Mac_ if you have not done so already and open your plugin project.
  2. Right-click your plugin project in the _Solution Explorer_ and select _Add_ > _New Folder_ …
  3. Name this folder _Resources_ (or similar).
  4. Right-click the new _Resources_ folder in the _Solution Explorer_ and select _Add_ > _Add Files…_.
  5. Navigate to the _plist_ you saved and add it to the plugin project _Resources_ folder. When prompted, _Move_ the _plist_ to the plugin _Resources_ project folder.
  6. Select your _ToolPaletteCollection.plist_ in _Solution Explorer_ and open the _Properties_ panel.
  7. In the _Build_ section of _Properties_ , in the _Copy the output directory_ entry, select _Copy if newer_.

## Load the Tool Palette

  1. In order to load the tool palette, you must reference _RhinoMac.dll_ and _Rhino.UI.dll_. In _Visual Studio for Mac_ , right-click on the project entry in the _Solution Explorer_ and select _Tools_ > _Edit File_. This opens up the _csproj_ file for your project as xml text in the code editor.
  2. Find the area of the xml near where _RhinoCommon_ is being referenced and add the following entries:

    
    
    <Reference Include="Rhino.UI">
      <HintPath>\Applications\Rhinoceros.app\Contents\Frameworks\RhCore.framework\Versions\Current\Resources\Rhino.UI.dll</HintPath>
      <Private>False</Private>
    </Reference>
    <Reference Include="RhinoMac">
      <HintPath>\Applications\Rhinoceros.app\Contents\Frameworks\RhCore.framework\Versions\Current\Resources\RhinoMac.dll</HintPath>
      <Private>False</Private>
    </Reference>
    

  1. Close the _csproj_ that is open in the code editor. Visual Studio for Mac reloads the project. If you check in the _References_ section of your project in the _Solution Explorer_ , you should see references to _RhinoMac_ and _Rhino.UI_.
  2. In your `Plugin` class, if you have not done so already, override the `OnLoad` method.
  3. Load your tool palette plist from your desired location by calling the `RhinoMac.Runtime.MacPlatformService.LoadToolPaletteCollection` and passing in the full path to your _plist_. For example, if your _plist_ is in the _Resources_ folder of your _rhp_ , use the following example:

    
    
    protected override Rhino.PlugIns.LoadReturnCode OnLoad (ref string errorMessage)
    {
      var pluginPath = System.IO.Path.GetDirectoryName(Assembly.Location);
      var resourcesPath = System.IO.Path.Combine (pluginPath, "Resources");
      var plistPath = System.IO.Path.Combine (resourcesPath, "ToolPalette.plist");
      bool didLoad = RhinoMac.Runtime.MacPlatformService.LoadToolPaletteCollection (plistPath);
      if (!didLoad)
        System.Diagnostics.Debug.WriteLine("WARNING: Failed to load tool palette.");
    
      return base.OnLoad (ref errorMessage);
    }
    

Your tool palette collection will be loaded and displayed when Rhino loads
your plugin.

## Related Topics

  * [Your First Plugin (Mac)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-mac/)
  * [Command Editor (from Rhino Help)](http://docs.mcneel.com/rhino/mac/help/en-us/index.htm#macpreferencesandsettings/commands.htm)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/loading-
tool-palettes-mac/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/loading-
tool-palettes-mac/index.md) [ Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2025 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/user/RhinoGuide/videos) [](https://vimeo.com/rhino)
[![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

