---
url: https://developer.rhino3d.com/guides/rhinocommon/moving-to-dotnet-core/#discussions
scraped_at: 2025-09-08T15:51:01.795410
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

[Moving to .NET Core](https://developer.rhino3d.com/guides/rhinocommon/moving-
to-dotnet-core/)

  * Advantages of .NET Core for Rhino
  * Choosing the .NET Runtime on Windows
  * Rhino.Inside
  * Checking if your plugin is compatible
  * Migrating your plugin
  * Debugging .NET Core on Windows
    * How to add a .NET Core launcher project in Visual Studio
  * Debugging on Mac
  * Discussions

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Moving to .NET Core

[New in 8](https://developer.rhino3d.com/8/new)

by [Curtis Wensley](https://discourse.mcneel.com/u/curtisw/) and [Callum
Sykes](https://discourse.mcneel.com/u/Callumsykes/) (Last updated: Friday,
April 25, 2025)

Rhino 8 now uses the open source [.NET Core
Runtime](https://github.com/dotnet/runtime) for running .NET code on both
Windows and Mac. This brings some performance improvements and aligns the .NET
runtimes used across platforms. Previously, Rhino 7 and earlier used the [mono
runtime](https://www.mono-project.com) on Mac, and .NET Framework exclusively
on Windows.

On Windows, you can still optionally run using the .NET Framework runtime in
the case of compatibility issues or running inside other software that
requires it (e.g. Rhino.Inside Revit).

Most plugins are already compatible when running in .NET Core without any
recompilation, but in the case of any incompatibilities you may need to update
your plugin.

## Advantages of .NET Core for Rhino

Using .NET Core allows Rhino and plugins to take advantage of many
[performance
improvements](https://devblogs.microsoft.com/dotnet/performance_improvements_in_net_7/)
which will make just about all .NET code execute much faster. This can
potentially provide huge productivity gains with computational libraries or
large data sets.

Additionally, using .NET Core on Mac eliminates a lot of compatibility issues
between the Mac and Windows versions of Rhino making it easier to make plugins
work on both platforms.

## Choosing the .NET Runtime on Windows

There may be reasons to continue to use .NET Framework on Windows, in
particular if you need to use 3rd party plugins that aren’t compatible with
.NET Core yet. The disadvantage to using .NET Framework is that Rhino may run
a little slower in certain use cases.

Rhino 8 initially shipped with the .NET 7.0.0 runtime. Rhino 8.12 or later has
the option to use a manually installed .NET 8 runtime, and Rhino 8.20 installs
and defaults to using .NET 8.0.14 or later.

There are a few ways to select the runtime and version that Rhino uses:

  1. Use the `SetDotNetRuntime` command, then restart Rhino.
  2. Pass either `/netcore` or `/netfx` as an argument when launching `Rhino.exe`. This overrides the `SetDotNetRuntime` setting.
  3. Pass either `/netcore-8` or `/netcore-7` to specify a particular .NET Core version. This requires that the chosen version is manually installed if it’s different from Rhino’s default.

## Rhino.Inside

When using Rhino.Inside, the runtime Rhino uses is the same as the host
application. For example, since Revit currently uses .NET Framework,
Rhino.Inside.Revit will also run using .NET Framework. Custom Rhino.Inside
applications should still work, however migrating to .NET 7+ would allow you
to take advantage of the performance improvements offered with .NET Core.

## Checking if your plugin is compatible

Rhino 8 will automatically scan plugins for any known API breakages when
running in .NET Core, and will provide a report of the specific assemblies and
APIs that are not comatible.

To check manually, you can use the `compat.exe` tool on each of your plugin
assemblies:

    
    
    "C:\Program Files\Rhino 8\System\netcore\compat.exe" -q --check-system-assemblies MyPlugin.rhp
    

You can also use Microsoft’s [upgrade
assistant](https://learn.microsoft.com/en-us/dotnet/core/porting/upgrade-
assistant-overview) to analyze your project for compatibility issues.

## Migrating your plugin

Many plugins won’t need any changes to run in Rhino 8 with .NET Core, but if
they do it is recommended to multi-target your plugin(s) for .NET 4.8 and .NET
7.0 so that it can run in either runtime on Windows.

For Mac-specific plugins you can target .NET 7.0 as .NET Core is the only
runtime available in Rhino 8. If you want the plugin to be compatible with
Rhino 7, target .NET 4.8 instead or use multi-targeting.

__AnyCPU __

Since Rhino 8 can run natively on Apple Silicon or on Intel, you must compile
your .NET assemblies for AnyCPU, and any native binaries need to be compiled
as a [Universal Binary](https://developer.apple.com/documentation/apple-
silicon/building-a-universal-macos-binary).

If your plugin uses any unavailable or non-working APIs when running in .NET
Core, some code changes may be necessary. This is especially true with many
3rd party libraries that have different versions of their library for .NET 4.8
and .NET Core. The compat report will show you which APIs and libraries you
need to avoid or update.

If you [multi-target your project](https://learn.microsoft.com/en-
us/nuget/create-packages/multiple-target-frameworks-project-file) to both .NET
4.8 and .NET 7.0, you can easily find and resolve compatibility issues during
compilation.

## Debugging .NET Core on Windows

To debug in .NET Core on Windows you will need to use Visual Studio 2022 or
Visual Studio Code.

Visual Studio determines the debugging runtime by the project’s target
framework, so either you need to [multi-target your
project](https://learn.microsoft.com/en-us/nuget/create-packages/multiple-
target-frameworks-project-file), or create a separate launcher project used
for debugging purposes only.

With Visual Studio Code, use the `coreclr` debugger type from the C#
extension. You do not need to multi-target or create a launcher project when
using Visual Studio Code.

Our [project
templates](https://github.com/mcneel/RhinoVisualStudioExtensions?tab=readme-
ov-file#rhinocommon-visual-studio-extensions) automatically create a multi-
targeted plugin, creates launch configurations for both VS and VS Code, and
has options to include a yak packaging step for multiple Rhino versions.

### How to add a .NET Core launcher project in Visual Studio

This is only required when you want to debug in .NET Core using Visual Studio
2022 on Windows, and if you’re not ready to multi-target your project(s).

  1. Right-click on your solution node and select _Add > New Project…_
  2. Select the C# **Console App** then click _Next_.
  3. Enter a name e.g. `Rhino8Launcher` then click _Next_.
  4. Select **.NET 7.0** for the Framework then click _Create_.
  5. Right-click the launcher project and select _Properties_.
  6. Go to the **Application > General** panel and change the **Output Type** drop down to _Windows Application_.
  7. Go to the **Debug > General** panel and click _Open debug launch profiles UI_.
  8. Delete the default profile by clicking the _Delete selected profile_ button.
  9. Create a new **Executable** profile, and enter the path to Rhino.exe. E.g. `C:\Program Files\Rhino 8\System\Rhino.exe`

You may also want to add your plugin project as a dependency of the launcher
project so it compiles before launching.

## Debugging on Mac

On Mac, you will need to use [Visual Studio
Code](https://code.visualstudio.com/). Follow the [Your First Plugin
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-
mac/#setting-up-debug)

## Discussions

Jump over to our [developer discourse
channel](https://discourse.mcneel.com/c/rhino-developer/3) to ask questions
regarding the move to .NET Core.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/moving-
to-dotnet-core/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/moving-
to-dotnet-core/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

