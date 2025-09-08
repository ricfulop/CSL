---
url: https://developer.rhino3d.com/guides/scripting/projects-publish/#project-solution
scraped_at: 2025-09-08T16:05:26.993463
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

[Publishing Rhino/Grasshopper Script
Plugins](https://developer.rhino3d.com/guides/scripting/projects-publish/)

  * Build Plugins from Script Editor
  * Build Plugins from Terminal
  * Build Artifacts
  * Project Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [Scripting
Guides](https://developer.rhino3d.com/en/guides/scripting/) /

Publishing Rhino/Grasshopper Script Plugins

[New in 8](https://developer.rhino3d.com/8/new)

by [Ehsan Iran-Nejad](https://discourse.mcneel.com/u/eirannejad/) (Last
updated: Wednesday, November 13, 2024)

__Note __

[Creating Rhino
Projects](https://developer.rhino3d.com/guides/scripting/projects-create/) for
information on creating projects in Script Editor.

## Build Plugins from Script Editor

You can build a project directly from Script Editor:

  * Open Script Editor

  * Open Project (`File > Open Project` menu)

  * Choose **Publish Project** (`File > Publish Project` or _Publish_ button in editor dashboard)

![](https://developer.rhino3d.com/guides/scripting/projects-publish/project-
build-editor.png)

Project information fields are discussed in detail in [Create
Project](https://developer.rhino3d.com/guides/scripting/projects-create/).
Here we focus on choosing a _Build Target_ and _Build Path_.

  * Choose a **Build Target** :

This is the minimum version of Rhino required to run your plugin. The
available versions are queried from [Rhino NuGet
packages](https://www.nuget.org/profiles/McNeel). You can see `macOS` and
`Windows` specific targets as well.

![](https://developer.rhino3d.com/guides/scripting/projects-publish/project-
build-editor-buildtarget.png)

  * Choose a **Build Path** :

This is where all generated assemblies and files are placed. Depending on the
_Build Target_ a subpath is added to this build path to avoid conflicts (e.g
`build/rh8/`)

![](https://developer.rhino3d.com/guides/scripting/projects-publish/project-
build-editor-buildpath.png)

  * Choose **Build Package** to build the project:

On a successful build, status tray will show success message in green:

![](https://developer.rhino3d.com/guides/scripting/projects-publish/project-
build-success.png)

## Build Plugins from Terminal

__Note __

To build a project in terminal, use the `rhinocode` command line utility
shipped with Rhino.

See [RhinoCode Command Line
Interface](https://developer.rhino3d.com/guides/scripting/advanced-cli/) for
more information on setting up the build environment.

  * Open Terminal

  * Use `rhinocode` command line utility to build the project:

![](https://developer.rhino3d.com/guides/scripting/projects-publish/project-
build-terminal.png)

    
    
    $ rhinocode project build ~/MyProject.rhproj
      0% - Preparing project
     10% - Preparing build path
     20% - Preparing plugin assembly
     50% - Preparing grasshopper plugin assembly
     60% - Adding shared resources
     90% - Creating yak package
    100% - Complete
    

See [RhinoCode: Build a
Project](https://developer.rhino3d.com/guides/scripting/advanced-cli/#build-a-
project) for more information.

## Build Artifacts

Once project is built, the target path will contain all the generated
artifacts:

![](https://developer.rhino3d.com/guides/scripting/projects-publish/project-
build-artifacts.png)

A Yak package is generated that contains both Rhino and Grasshopper plugins.

__Note __

See [Pushing a Package to the
Server](https://developer.rhino3d.com/guides/yak/pushing-a-package-to-the-
server/) on how to publish `.yak` files to package server

## Project Solution

On successful build, a Visual Studio solution is automatically generated that
contains the source code for both Rhino and Grasshopper plugins. This solution
is created to allow full customization of Rhino and Grasshopper plugins. You
can add extra commands and components and make any other modifications.

Use [Visual Studio](https://visualstudio.microsoft.com/) or [Visual Studio
Code](https://code.visualstudio.com/) to edit the project.

Use `dotnet` command line utility to build the project from command line:

![](https://developer.rhino3d.com/guides/scripting/projects-publish/project-
build-terminal-dotnet.png)

Once the project is built, compiled Rhino and Grasshopper plugins are under
`bin/` directory of their respective projects:

![](https://developer.rhino3d.com/guides/scripting/projects-publish/project-
build-artifacts-dotnet.png)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/scripting/projects-
publish/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/scripting/projects-
publish/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

