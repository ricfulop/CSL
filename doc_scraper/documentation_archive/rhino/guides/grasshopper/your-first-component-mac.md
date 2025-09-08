---
url: https://developer.rhino3d.com/guides/grasshopper/your-first-component-mac/
scraped_at: 2025-09-08T15:41:23.047835
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

[Your First Component
(Mac)](https://developer.rhino3d.com/guides/grasshopper/your-first-component-
mac/)

  * Prerequisites
  * HelloGrasshopper
    * Download the required template
    * Starting the Project
    * Boilerplate Build
    * Component Anatomy
    * Debugging
  * Next Steps
    * Adding components
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) /

Your First Component (Mac)

__

macOS only

by [Steve Baer](https://discourse.mcneel.com/u/stevebaer/) and [Callum
Sykes](https://discourse.mcneel.com/u/Callumsykes/) (Last updated: Monday,
October 7, 2024)

## Prerequisites

It is presumed you already have the necessary tools installed and are ready to
go. If you are not there yet, see [Installing Tools
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-
mac/).

## HelloGrasshopper

We will use Visual Studio Code and the dotnet Rhino Grasshopper template to
create a new, basic, Grasshopper component called _HelloGrasshopper_.

If you are familiar with Visual Studio Code, these step-by-step instructions
may be overly detailed for you. The executive summary: create a new Solution
using the Grasshopper Component dotnet template, build and run, and then make
a change.

We are presuming you have never used Visual Studio Code before, so we’ll go
through this one step at a time.

### Download the required template

  1. Launch Visual Studio Code.
  2. Open _Visual Studio Code’s Terminal_ via _Terminal (menu entry)_ > _New Terminal_ , or using the command palette _(⌘ ⇧ P)_ and search for “Terminal”.
  3. Inside Terminal, run: 
         
         dotnet new install Rhino.Templates
         

### Starting the Project

  1. Create a folder on your mac where you would like your project to live. Name the folder `HelloGrasshopper`.
  2. If you have not done so already, _launch Visual Studio Code_.
  3. Now we can open our new folder, navigate to _File_ > _Open Folder_ and choose the folder we just created.
  4. Open Terminal via _Terminal_ > _New Terminal_ , or using the command palette _(⌘ ⇧ P)_ and search for “Terminal”.
  5. Enter the following command into the Terminal: 
         
         dotnet new grasshopper --version 8 -sample
         

  6. In our Folder explorer, we should see the project appear as Visual Studio Code discovers the files.
  7. Expand the Solution Explorer, this is the best way to interact with C# projects on Mac in Visual Studio Code.

### Boilerplate Build

__Build Issue?__

Older Rhino Templates do not have System.Drawing.Common referenced. To add
them to your project run the command **dotnet add package
System.Drawing.Common -v 7.0.0** in the terminal.

  1. Before we do anything, let’s _Run and Debug_ HelloGrasshopper to make sure everything is working as expected. We’ll just build the boilerplate Plugin template. Click the _Run and Debug_ button on the left hand side of Visual Studio Code and then the green play button in the newly opened panel.

![New Project](https://developer.rhino3d.com/images/your-first-component-
mac-01.png)

  2. _Rhinoceros and Grasshopper_ launch.

  3. We will find the HelloGrasshopper Component under **Category / SubCategory**

![Solution Anatomy](https://developer.rhino3d.com/images/your-first-component-
mac-02.png)

  4. Adding the component to the canvas will run the component and output some interesting geometry in the Rhino Viewport

![Solution Anatomy](https://developer.rhino3d.com/images/your-first-component-
mac-03.png)

  5. Press Stop Debugging _(⇧ F5)_ , in Visual Studio Code, signified by the Red Square in the debug toolbar. This stops the debugging session. Now let’s n take a look at the Plugin Anatomy.

### Component Anatomy

Use the **Solution Explorer** to expand the **Solution** (_.sln_) so that it
looks like this…

![Solution Anatomy](https://developer.rhino3d.com/images/your-first-component-
mac-04.png)

  1. The **HelloGrasshopper** solution (_.sln_)
  2. The **HelloGrasshopper** project (_.csproj_) has the same name as its parent solution…this is the project that was created for us by the template earlier.
  3. **References** : Just as with most projects, you will be referencing other libraries. The template added the necessary references to create a basic Grasshopper component.
  4. **Grasshopper** is the Rhino for Mac main grasshopper DLL. Classes in this DLL are subclassed and used by your custom component.
  5. **HelloGrasshopperComponent.cs** is where a custom `Grasshopper.Kernal.GH_Component` subclass is defined. Your project may contain multiple subclasses of GH _Component if you want to ship multiple components in a single _gha_.
  6. **HelloGrasshopperInfo.cs** defines general information about this _gha_.

### Debugging

  1. Add a breakpoint to line 75 of _HelloGrasshopperComponent.cs_. You set breakpoints in Visual Studio Code by clicking in the gutter to the left of the line numbers. ![Set a breakpoint](https://developer.rhino3d.com/images/your-first-component-mac-05.png)
  2. _Run and Debug_. our project. The breakpoint will become an empty circle, this is because our code has not been loaded yet. Once we hit the breakpoint once and continue, the code will be loaded until we end our Debug session. ![Set a breakpoint](https://developer.rhino3d.com/images/your-first-component-mac-06.png)
  3. Rhino and Grasshopper should open, if Grasshopper does not open, click “New Model” and run the _Grasshopper_ command.
  4. Place our sample component _HelloGrasshopperComponent_ and as soon as you do, you should hit your breakpoint and rhino/Grasshopper will pause (You may need to drag the Grasshopper window out of the way to see Visual Studio Code) ![Hit a breakpoint](https://developer.rhino3d.com/images/your-first-component-mac-07.png)
  5. With Rhino/Grasshopper paused, in _Visual Studio Code_ we will see _Locals_ under _Variables_. You can inspect all of the values for the variables in your component. ![Locals panel](https://developer.rhino3d.com/images/your-first-component-mac-08.png)
  6. Let’s Continue Execution in Rhino and Grasshopper by pressing the Green _Play_ button in the Debug Bar
  7. Control is passed back to _Rhino / Grasshopper_ and your command finishes. Now _Stop_ _(⇧ F5)_ the debugging session as before.
  8. **Remove** the breakpoint you created above by clicking on it in the gutter.

**Congratulations!** You have just built your first Grasshopper component for
Rhino for Mac. **Now what?**

## Next Steps

You’ve built a component library from boilerplate code, but what about putting
together a new simple component “from scratch” and adding it to your project?
(Component libraries are made up of multiple components after all). Next,
check out the [Simple
Component](https://developer.rhino3d.com/guides/grasshopper/simple-component/)
guide.

Try debugging your new grasshopper plugin on
[Windows](https://developer.rhino3d.com/guides/grasshopper/your-first-
component-windows/), all plugins using the new templates are now cross-
platform by default.

### Adding components

A single gha can contain more than one
[GH_Component](https://mcneel.github.io/grasshopper-api-
docs/api/grasshopper/html/T_Grasshopper_Kernel_GH_Component.htm) derived class
(and commonly does). Dotnet has support for adding more custom components to
your project.

  1. Open _Visual Studio Code’s Terminal_ via _Terminal (menu entry)_ > _New Terminal_ , or using the command palette _(⌘ ⇧ P)_ and search for “Terminal”.
  2. Inside Terminal, run:

    
    
    dotnet new ghcomponent -n "NewComponent"
    

  1. A new component will appear called _NewComponent_

## Related topics

This article is focused on initial setup and debugging a Grasshopper component
in Rhino for Mac. For further reading on customizing your component please
see:

  * [Grasshopper](https://developer.rhino3d.com/guides/grasshopper/csharp-essentials/)
  * [Distributing your Plugin](https://developer.rhino3d.com/guides/yak/creating-a-rhino-plugin-package/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/your-
first-component-mac/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/your-
first-component-mac/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

