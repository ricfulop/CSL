---
url: https://developer.rhino3d.com/guides/rhinocommon/using-nuget/
scraped_at: 2025-09-08T15:36:43.868770
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

[Using NuGet](https://developer.rhino3d.com/guides/rhinocommon/using-nuget/)

  * Why NuGet?
    * Advantages
    * Potential Pitfalls
  * Getting Started
    * Step-by-Step (Windows)
    * Step-by-Step (Mac)
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Using NuGet

by [Luis Fraguada](https://discourse.mcneel.com/u/fraguada/), [Will
Pearson](https://discourse.mcneel.com/u/will/), and [Callum
Sykes](https://discourse.mcneel.com/u/Callumsykes/) (Last updated: Saturday,
May 18, 2019)

## Why NuGet?

In [previous](https://developer.rhino3d.com/guides/rhinocommon/your-first-
plugin-windows/)
[guides](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-
mac/) you’ve seen how to set up a project to develop a RhinoCommon Plugin or
Grasshopper component. These guides relied on the Visual Studio Project
Wizards that we publish to quickly get you going on plugin development. The
wizards automatically reference the necessary assemblies to make RhinoCommon
and Grasshopper SDKs available in your Visual Studio project. While this
project setup should be fine for a number of cases, there might be some
reasons to switch the RhinoCommon and Grasshopper assembly references to those
which are published by [McNeel on
NuGet](https://www.nuget.org/profiles/McNeel)…

### Advantages

There are several potential advantages to using NuGet packages for RhinoCommon
SDKs:

  * It’s great for projects with multiple developers (or developers with multiple computers). No more references to `Grasshopper.dll` that include `C:\Users\<username>\AppData\...`.
  * NuGet runs on Windows and Mac and is baked into Visual Studio (for Windows).
  * Are you using Continuous Integration (CI)? Your build servers can automatically download the correct version of the SDK before compiling and publishing your shiny new release.
  * You’re probably already using it to install packages like [Json.NET](https://www.nuget.org/packages/newtonsoft.json).
  * You can target a lower version of RhinoCommon than you have installed to ensure full compatibility across all Rhino versions

### Potential Pitfalls

NuGet makes it easy to compile plug-ins against versions of Rhino other than
those installed on your computer. This is handy for backwards-compatible
and/or cross-platform development. However, the fact that your Rhino
installation and your RhinoCommon/Grasshopper references are “out of sync” can
cause problems.

  * NuGet packages will need to be updated separately to Rhino
  * You _may_ have trouble debugging your plug-in if it was built against a version of RhinoCommon that is newer than the one included with Rhino1

## Getting Started

**Note** : You may wish to read Microsoft’s guide to [installing NuGet
packages in Visual Studio](https://docs.microsoft.com/en-
gb/nuget/quickstart/use-a-package) in addition to this one. And how to
[install a Nuget Package in Visual Studio
Code.](https://code.visualstudio.com/docs/csharp/package-management)

We have a few NuGet packages available and you can install them like you would
any other.

The [RhinoCommon](https://www.nuget.org/packages/rhinocommon) package includes

  * _RhinoCommon.dll_
  * _Eto.dll_
  * _Rhino.UI.dll_

The [Grasshopper](https://www.nuget.org/packages/grasshopper) package depends2
on the RhinoCommon package _with the same version_ and includes

  * _Grasshopper.dll_
  * _GH_IO.dll_

We also have a [RhinoWindows](https://www.nuget.org/packages/RhinoWindows)
package.

We’re currently publishing new package versions for every public release of
Rhino for Windows, including preleases (WIP, release candidate and beta). If
you’re developing for Rhino WIP for Mac, choose the latest 6.* package –
RhinoCommon and Grasshopper are cross-platform!

If you’re searching for a version of one of our packages that corresponds to a
prerelease version of Rhino then make sure you check “include prerelease”.
These packages are marked with a prerelease suffix in the version number, such
as `-wip` or `-rc`.

### Step-by-Step (Windows)

To switch to NuGet packages, follow these steps:

  1. In Visual Studio, find the _Solution Explorer_ and right-click on the _References_ section of your project. Select _Manage NuGet Packages…_ Alternatively, the same can be done through the Visual Studio _Project_ menu, and choosing _Manage NuGet Packages…_

![Manage NuGet Packages - Windows](https://developer.rhino3d.com/images/using-
nuget-01.png)

  2. In the NuGet tab which appears, click on _Browse_. In the search box, type in _RhinoCommon_. You should see an entry for RhinoCommon and one for Grasshopper. If you are writing a Rhino Plugin or Grasshopper Add-on for Rhino WIP, ensure you check _Include prerelease_.

If your project is a **RhinoCommon Plug-in** , select the
[RhinoCommon](https://www.nuget.org/packages/rhinocommon) package. For Rhino
WIP choose the _Latest prerelease_ and click _Install_. NuGet will install3
_RhinoCommon.dll_ , _Rhino.UI_ and _Eto.dll_.

If your project is a **Grasshopper Add-on** , select the
[Grasshopper](https://www.nuget.org/packages/grasshopper) package. For
Grasshopper Add-ons in Rhino WIP choose the _Latest prerelease_ and click
_Install_. NuGet will install3 _Grasshopper.dll_ and _GH_IO.dll_ as well as
the corresponding version of the RhinoCommon assemblies.

![Choose NuGet Packages - Windows](https://developer.rhino3d.com/images/using-
nuget-02.png)

  3. _(Optional)_ The references created by these packages have `CopyLocal` set to `true`. Normally, it is a best practice to make sure that the references are not copied to the output directory, since they are included with Rhino. You can do this by selecting any of the following references if they exist in your project - _RhinoCommon_ , _Eto_ , _Rhino.UI_ , _Grasshopper_ , _GH_IO_ \- and, in the _Properties_ window, set `CopyLocal` to `false`. The reason this step is _optional_ is that we’ve included some MSBuild witchcraft that will ensure that `CopyLocal` is set to `false` when compiling your project, regardless of what it says in the _Properties_ window.

![Copy Local](https://developer.rhino3d.com/images/using-nuget-03.png)

### Step-by-Step (Mac)

Further Reading [NuGet in Visual Studio
Code](https://code.visualstudio.com/docs/csharp/package-management)

  1. In Visual Studio Code, open the Command Palette _(⌘ ⇧ P)_ and search nuget, choose _Add NuGet Package_. Alternatively, the same can be done through the Solution Explorer by right clicking the Project you wish to add the package to, and choosing _Add NuGet Package…_

__Required Plugin __

[C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-
dotnettools.csdevkit))

![Manage NuGet Packages - Mac](https://developer.rhino3d.com/images/using-
nuget-04.png)

  2. The command palette will appear at the top of Visual Studio Code. In the search box, type in _RhinoCommon_ and press enter. You should see an entry for RhinoCommon and one for Grasshopper.

![Manage NuGet Packages - Mac](https://developer.rhino3d.com/images/using-
nuget-05.png)

  3. Now you can choose the version of the NuGet package you wish to target

![Choose NuGet Packages - Mac](https://developer.rhino3d.com/images/using-
nuget-06.png)

__Pre-release Versions __

If you are writing a Rhino Plugin or Grasshopper Add-on for Rhino WIP, you
will need to install a pre-release NuGet Package. At the time of writing time
the C# Dev Kit does not include a way to show pre-release versions. You must
use _dotnet add package RhinoCommon_ in the terminal, _([The RhinoCommon NuGet
Page](https://www.nuget.org/packages/rhinocommon) has a handy copy paste to
make this easier)_. Or you can use the [NuGet Gallery
Plugin](https://marketplace.visualstudio.com/items?itemName=patcx.vscode-
nuget-gallery) which offers this functionality.

If your project is a **RhinoCommon Plug-in** , select the
[RhinoCommon](https://www.nuget.org/packages/rhinocommon) package. NuGet will
install _RhinoCommon.dll_ , _Rhino.UI_ and _Eto.dll_ once you have selected a
version.

If your project is a **Grasshopper Add-on** , select the
[Grasshopper](https://www.nuget.org/packages/grasshopper) package. NuGet will
install2 _Grasshopper.dll_ and _GH_IO.dll_ as well as the corresponding
version of the RhinoCommon assemblies once you have selected a version.

  4. Confirm your NuGet Packages installed correctly Check your Project in the Solution Explorer, you should see a new entry under dependencies > Packages

![Choose NuGet Packages - Mac](https://developer.rhino3d.com/images/using-
nuget-07.png)

## Related topics

  * [Your First Plugin (Windows)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-windows/)
  * [Your First Plugin (Mac)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-mac/)

**Footnotes**

* * *

  1. Your plug-in will not load if it uses parts of the API which don’t exist in the running version of Rhino. ↩︎

  2. This means that if you install the Grasshopper NuGet package, the matching RhinoCommon package will be installed automatically. ↩︎ ↩︎

  3. If your project already references one of the above assemblies, don’t worry! NuGet will handle it. ↩︎ ↩︎

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/using-
nuget/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/using-
nuget/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

