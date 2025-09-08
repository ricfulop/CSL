---
url: https://developer.rhino3d.com/guides/grasshopper/your-first-component-windows/
scraped_at: 2025-09-08T15:41:22.095948
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
(Windows)](https://developer.rhino3d.com/guides/grasshopper/your-first-
component-windows/)

  * HelloGrasshopper
    * File New
    * Boilerplate Build
    * Component Anatomy
    * Make Changes
    * Debugging
  * Next Steps
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) /

Your First Component (Windows)

__

Windows only

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) and [Callum
Sykes](https://discourse.mcneel.com/u/Callumsykes/) (Last updated: Monday,
October 7, 2024)

It is presumed you already have the necessary tools installed and are ready to
go. If you are not there yet, see [Installing Tools
(Windows)](https://developer.rhino3d.com/guides/grasshopper/installing-tools-
windows/).

## HelloGrasshopper

We will use the Grasshopper Assembly templates to create a new, basic,
component library called HelloGrasshopper.

If you are familiar with Visual Studio, these step-by-step instructions may be
overly detailed for you. The executive summary: create a new project using the
Grasshopper Assembly template, build and run, and then make a change.

We are presuming you have never used Visual Studio before, so we’ll go through
this one step at a time.

### File New

  1. If you have not done so already, **launch Visual Studio** (for the purposes of this guide, we are using Visual Studio Community Edition and C#).
  2. Navigate to **File** > **New** > **Project** … ![File New Project](https://developer.rhino3d.com/images/your-first-plugin-windows-01.png)
  3. A **Create a new project** wizard should appear. In the **Search for templates** area, search for `Grasshopper` to filter the results. Find and select the **Grasshopper Assembly for Rhino (C#)** entry and click **Next**.
  4. For the purposes of this Guide, we will name our demo plugin _HelloGrasshopper_. In the **Configure your new project** dialog, fill in the **Project name** field. **Browse** and select a location for this project on your disk, then click **Next**
  5. The _New Grasshopper Add-On dialog_ appears. Check the _Provide sample code_ checkbox. ![New Grasshopper Assembly](https://developer.rhino3d.com/images/your-first-component-windows-03.png)
  6. This is where you fill out information about your first component: 
     1. Add-on display name: the name of component library itself.
     2. Name: the name of the component as displayed in the ribbon bar and search menus.
     3. Nickname: the default name of the component when inserted into the canvas.
     4. Category: name of tab where component icon will be shown.
     5. Subcategory: name of group inside tab where icon will be shown.
     6. Description: description shown in tooltip when mouse is over the component icon in the menu.
  7. For the purposes of this guide, let’s chek the “Provide Sample Code”, and then click **Finish** …
  8. A **new solution** called **HelloGrasshopper** should open… ![HelloGrasshopper Solution](https://developer.rhino3d.com/images/your-first-component-windows-04.png)

### Boilerplate Build

  1. Before we do anything, let’s **build** and **run** HelloGrasshopper to make sure everything is working as expected. We’ll just build the boilerplate Plugin template. Click **Start** (play) button in toolbar corner of Visual Studio (or press **F5**) to **Start Debugging** … ![Start Button](https://developer.rhino3d.com/images/your-first-compo-windows-06.png)
  2. **Rhinoceros** launches and a moment later, so will **Grasshopper**.

__First Debug __

_The first debug may take a while depending on your settings, as Visual Studio
downloads debugging files, this is normal._

  1. Navigate to **Curve** > **Primitive** in the components menus. You should see HelloGrasshopper in the list with a blank icon. Drag this onto the canvas. The component will run and some interesting Geometry will appear in the Rhino Viewport.
  2. **Exit** Rhinoceros. This stops the session. Go back to **Visual Studio**. Let’s take a look at the…

### Component Anatomy

  1. Use the **Solution Explorer** to expand the **Solution** (_.sln_) so that it looks like this… ![Grasshopper Component Anatomy](https://developer.rhino3d.com/images/your-first-component-windows-06.png)

_NOTE_ : Depending on your edition of Visual Studio, it may look slightly
different.

  2. The **HelloGrasshopper** project (_.csproj_) has the same name as its parent solution…this is the project that was created for us by the **Grasshopper Assembly** template wizard earlier.

  3. **Dependencies** : Just as with most projects, you will be referencing other libraries. The **Grasshopper Assembly** template added the necessary dependencies to create a custom Grasshopper component.

  4. **Framework Targets** \- The **Grasshopper Assembly** template is multi-targeted so that the correct assemblies are loaded for the correct platforms.

  5. **Grasshopper** \- The referenced Grasshopper Nuget.

  6. **Properties** contains the **launchSettings.json** file. This file contains all of the debug.

  7. **HelloGrasshopperInfo.cs** contains the component library information, such as the name, icon, etc.

  8. **HelloGrasshopperComponent.cs** is where the action is. Let’s take a look at this file…

### Make Changes

  1. Open **HelloGrasshopperComponent.cs** in Visual Studio’s Source Editor (if it isn’t already).

  2. Notice that `HelloGrasshopperComponent` inherits from `GH_Component` …
         
         public class HelloGrasshopperComponent : GH_Component
         

  3. If you hover over `GH_Component` you will notice this is actually `Grasshopper.Kernel.GH_Component`.

  4. `HelloGrasshopperComponent` also overrides two methods for determining the input and output parameters …

    
    
    protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
    ...
    protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
    

  5. The actual work done by the component is to be found in the `SolveInstance` method…

    
    
    protected override void SolveInstance(IGH_DataAccess DA)
    

  6. As you can see, this is where the action happens. This boilerplate component creates a spiral on a plane. Just to make sure everything is working, let’s change the default plane on which the spiral is constructed. On line1 67, in `SolveInstance`, notice that an XY plane is constructed…

    
    
    Plane plane = Plane.WorldXY;
    

  7. Further down in the `SolveInstance` method, you will notice that the input data is being fed into this plane…

    
    
    if (!DA.GetData(0, ref plane)) return;
    

  8. Go back to the `RegisterInputParams`, and find the line where the _Plane_ input is registered. The last argument being fed to the method - `Plane.WorldXY` \- is the default value of the input…

    
    
    pManager.AddPlaneParameter("Plane", "P", "Base plane for spiral", GH_ParamAccess.item, Plane.WorldXY);
    

  9. Change the default value of the _Plane_ input to be `Plane.WorldYZ` …

    
    
    pManager.AddPlaneParameter("Plane", "P", "Base plane for spiral", GH_ParamAccess.item, Plane.WorldYZ);
    

  10. Now let’s examine what happens when inputs are given to this component…

### Debugging

  1. Set a breakpoint on line1 99 of _HelloGrasshopperComponent.cs_. You set breakpoints in Visual Studio by clicking in the gutter… ![Set a breakpoint](https://developer.rhino3d.com/images/your-first-component-windows-07.png)
  2. **Build** and **Run**.
  3. In Grasshopper, place a _HelloGrasshopper_ component on the canvas…as soon as you do, you should hit your breakpoint and pause… ![Hit a breakpoint](https://developer.rhino3d.com/images/your-first-component-windows-08.png)
  4. The reason you hit the breakpoint is because the `SolveInstance` method was called once initially when the component was placed on the canvas. With Rhino and Grasshopper paused, in **Visual Studio** switch to the **Autos** tab (if it not already there). In the list, find the `plane` object. Our `plane` is a `Rhino.Geometry.Plane` with a value of `{Origin=0,0,0 XAxis=0,1,0, YAxis=0,0,1, ZAxis=1,0,0}` …an YZ plane, the default, as expected.
  5. **Continue** in Grasshopper by pressing the **Continue** button in the upper menu of **Visual Studio** (or press **F5**)… ![Continue Executing](https://developer.rhino3d.com/images/your-first-plugin-windows-11.png)
  6. Control is passed back to **Grasshopper** and the spiral draws in the Rhino viewport. Now, place an _XY Plane_ component on the canvas and feed it as an input into _HelloGrasshopper_ ’s _Plane_ input. Notice you hit your breakpoint again, because the `SolveInstance` is being called now that the input values have changed.
  7. **Exit** Grasshopper and Rhino or **Stop** the debugging session.
  8. **Remove** the breakpoint you created above by clicking on it in the gutter.

**DONE!**

**Congratulations!** You have just built your first Grasshopper component for
Rhino for Windows. **Now what?**

## Next Steps

You’ve built a component library from boilerplate code, but what about putting
together a new simple component “from scratch” and adding it to your project?
(Component libraries are made up of multiple components after all). Next,
check out the [Simple
Component](https://developer.rhino3d.com/guides/grasshopper/simple-component/)
guide.

Try debugging your new grasshopper plugin on
[Mac](https://developer.rhino3d.com/guides/grasshopper/your-first-component-
mac/), all plugins using the new templates are now cross-platform by default.

## Related topics

  * [Installing Tools (Windows)](https://developer.rhino3d.com/guides/grasshopper/installing-tools-windows/)
  * [Simple Component](https://developer.rhino3d.com/guides/grasshopper/simple-component/)

**Footnotes**

* * *

  1. **Line numbers** in Visual Studio can be enabled and disabled in **Tools** > **Options…** > **Text Editor** section > **All Languages** entry > **General** sub-entry > **Settings** subsection > check **Line numbers**. Click **OK** to close the **Options** dialog. ↩︎ ↩︎

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/your-
first-component-windows/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/your-
first-component-windows/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

