---
url: https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-mac/#related-topics
scraped_at: 2025-09-08T16:06:49.490161
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

[Your First Plugin
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-
mac/)

  * HelloRhinoCommon
    * Download the required template
    * Starting the Project
    * Boilerplate Build
    * Plugin Anatomy
    * Make Changes
    * Debugging
  * Next Steps
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Your First Plugin (Mac)

__

macOS only

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) and [Callum
Sykes](https://discourse.mcneel.com/u/Callumsykes/) (Last updated: Friday,
February 21, 2025)

It is presumed you already have the necessary tools installed and are ready to
go. If you are not there yet, see [Installing Tools
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-
mac/).

## HelloRhinoCommon

We will use Visual Studio Code to create a new, basic, command plugin called
HelloRhinoCommon.

We are presuming you are new to Visual Studio Code, so we’ll go through this
one step at a time.

### Download the required template

  1. Launch Visual Studio Code.
  2. Open _Visual Studio Code’s Terminal_ via _Terminal (menu entry)_ > _New Terminal_ , or using the command palette _(⌘ ⇧ P)_ and search for “Terminal”.
  3. Inside Terminal, run: 
         
         dotnet new install Rhino.Templates
         

### Starting the Project

  1. Create a folder on your mac where you would like your project to live. Name the folder `HelloRhinoCommon`.
  2. If you have not done so already, _launch Visual Studio Code_.
  3. Now we can open our new folder, navigate to _File_ > _Open Folder_ and choose the folder we just created.
  4. Open Terminal via _Terminal_ > _New Terminal_ , or using the command palette _(⌘ ⇧ P)_ and search for “Terminal”.
  5. Enter the following command into the Terminal: 
         
         dotnet new rhino --version 8 -sample
         

  6. In our Folder explorer, we should see the project appear as Visual Studio Code discovers the files.
  7. Expand the Solution Explorer, this is the best way to interact with C# projects on Mac in Visual Studio Code.

### Boilerplate Build

  1. Before we do anything, let’s _Run and Debug_ HelloRhinoCommon to make sure everything is working as expected. We’ll just build the boilerplate Plugin template. Click the _Run and Debug_ button on the left hand side of Visual Studio Code and then the green play button in the newly opened panel.

![New Project](https://developer.rhino3d.com/images/your-first-plugin-
mac-03.png)

  2. _Rhinoceros_ launches. Click _New Model_.

  3. Type `Hello` into the Rhino Commandline. Notice that the command autocompletes.

![Command Autocompletes](https://developer.rhino3d.com/images/your-first-
plugin-mac-04.png)

  4. The _HelloRhinoCommonCommand_ command lets us draw a line, and then prints out a message
  5. Press Stop Debugging _(⇧ F5)_ , in Visual Studio Code, signified by the Red Square in the debug toolbar. This stops the debugging session. Go back to _Visual Studio Code_. Let’s take a look at the Plugin Anatomy.

### Plugin Anatomy

  1. Use the _Solution Explorer_ to expand the project so that it looks like below.

![Solution Anatomy](https://developer.rhino3d.com/images/your-first-plugin-
mac-06.png)

  1. The _HelloRhinoCommon_ solution (_.sln_) contians all of our projects. This was created for us by the `dotnet` command we ran earlier.
  2. The _HelloRhinoCommon_ project (_.csproj_) has the same name as its parent solution. This is the project that was created for us by `dotnet` command we ran earlier.
  3. _Dependencies_ : Just as with most projects, you will be referencing other libraries. The _RhinoCommon Plugin_ template added the necessary references to create a basic RhinoCommon plugin.
  4. _EmbeddedResources_ : This is where you would place any image assets you want to ship with your plugin. The _RhinoCommon Plugin_ template added an icon file with a default boilerplate icon.
  5. _Properties_ contains the _AssemblyInfo.cs_ source file. This file contains the meta-data (author, version, etc), including the very-important `Guid`, which identifies the plugin.
  6. _HelloRhinoCommonCommand.cs_ is where the action is. Let’s take a look at this file in the next section below…
  7. _HelloRhinoCommonPlugin.cs_ is where this template plugin derives from _Rhino.Plugins.Plugin_ and returns a static Instance of itself.

### Make Changes

  1. Open _HelloRhinoCommonCommand.cs_ in Visual Studio Code’s Source Editor (if it isn’t already).
  2. Notice that `HelloRhinoCommonCommand` inherits from `Rhino.Commands.Command`

    
    
            public class HelloRhinoCommonCommand : Rhino.Commands.Command
    

  3. And that it overrides one inherited property called `EnglishName`

    
    
            public override string EnglishName  => "HelloRhinoCommonCommand";
    

  4. All Rhino commands must have an `EnglishName` property. This command name will become inaccurate soon, as we’re going to spice up our quite pointless command. Let’s rename the command to _HelloDrawLine_ :

    
    
            public override string EnglishName  => "HelloDrawLine";
    

  5. Further down, notice that `HelloRhinoCommandCommand` overrides the `RunCommand` method:

    
    
            protected override Result RunCommand (Rhino.RhinoDoc doc, RunMode mode)
    

  6. And then type in the following by hand on line 62 to get a feel for the editor.

    
    
    RhinoApp.WriteLine("I'm writing my first Rhino Plugin!");
    

  7. Notice that - as you type - Visual Studio Code uses IntelliSense, just like Visual Studio for Windows (and many other editors).

### Debugging

  1. Set a breakpoint on line 59 of _HelloRhinoCommonCommand.cs_. You set breakpoints in Visual Studio Code by clicking in the gutter to the left of the line numbers. ![Set a breakpoint](https://developer.rhino3d.com/images/your-first-plugin-mac-07.png)
  2. _Run and Debug_. our project. The breakpoint will become an empty circle, this is because our code has not been loaded yet. Once we hit the breakpoint once and continue, the code will be loaded until we end our Debug session. ![Set a breakpoint](https://developer.rhino3d.com/images/your-first-plugin-mac-08.png)
  3. Click New Model. And then run our _HelloDrawLine_ command. Create the two points and as soon as you do, you should hit your breakpoint and rhino will pause ![Hit a breakpoint](https://developer.rhino3d.com/images/your-first-plugin-mac-09.png)
  4. With Rhino paused, in _Visual Studio Code_ we will see _Locals_ under _Variables_. In the list, find the `pt1` object we authored. Click the dropdown _arrow_ to expand the list of members on `pt1`.  
Our `pt1` is a `Rhino.Geometry.Point3d` this class has an `X`, `Y`, `Z`
property just as we’ll find documented in the [RhinoCommon
API](https://developer.rhino3d.com/api/rhinocommon/rhino.geometry.point3d).
![Locals panel](https://developer.rhino3d.com/images/your-first-plugin-
mac-10.png)

  5. Let’s Continue Execution in Rhino by pressing the Green _Play_ button in the Debug Bar
  6. Control is passed back to _Rhino_ and your command finishes. _Quit_ Rhino or _Stop_ the debugging session.

_Congratulations!_ You have just built your first RhinoCommon plugin for Rhino
for Mac. _Now what?_

## Next Steps

If you’d like to push your exciting new plugin to Yak so that everyone can use
it, check out the [Creating a Yak
Package](https://developer.rhino3d.com/guides/yak/creating-a-rhino-plugin-
package/) guide.

If you’d like to collaborate with colleagues and friends commit your plugin to
a git repo. [Getting started with GitHub](https://github.blog/developer-
skills/github/beginners-guide-to-github-repositories-how-to-create-your-first-
repo/).

`dotnet new gitignore` will add a gitignore file so unnecessary files will not
be committed.

Try debugging your new plugin on
[Windows](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-
windows/), all plugins using the new templates are now cross-platform by
default.

## Related topics

  * [Installing Tools (Mac)](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-mac/)
  * [Plugin Installers (Mac)](https://developer.rhino3d.com/guides/rhinocommon/plugin-installers-mac/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/your-
first-plugin-mac/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/your-
first-plugin-mac/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

