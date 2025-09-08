---
url: https://developer.rhino3d.com/guides/general/rhino-technology-overview/#related-topics
scraped_at: 2025-09-08T15:57:40.759017
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

[Rhino Technology
Overview](https://developer.rhino3d.com/guides/general/rhino-technology-
overview/)

  * Overview
  * Foundation
    * C++ Rhino Core
    * openNURBS
    * C++ SDK
  * C++ Stack
    * C++ Plugins
    * RhinoScript
  * .NET Stack
    * C API
    * .NET Framework
    * RhinoCommon
    * Eto
    * .NET Plugins
    * Grasshopper Components
    * Python Scripts
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [General
Guides](https://developer.rhino3d.com/en/guides/general/) /

Rhino Technology Overview

by [Brian Gillespie](https://discourse.mcneel.com/u/brian/) (Last updated:
Friday, April 25, 2025)

## Overview

Rhinoceros is composed of many layers - written in many languages - all
stacked on top of each other. The most foundational are on the bottom, but the
top layers should by no means be considered superficial…

![The Rhino Stack](https://developer.rhino3d.com/images/rhino-technology-
overview-01.png)

Let’s discuss each of the layers in turn, starting on the bottom with the…

## Foundation

### C++ Rhino Core

The C++ Core of Rhino is the oldest and broadest set of code. We use
Microsoft’s MFC in places, including the SDK. This is where the runtime
document is managed, where all the OpenGL viewport drawing code exists, and
it’s where the computational geometry code written by our mathematicians
lives. Many of Rhino’s commands are here.

Lots of user interface - the command line, the application mainframe, status
bar, and the dialog boxes for many commands in the Rhino core.

### openNURBS

openNURBS is free C++ source code that lets you read and write Rhino _3dm_
files - all the way back to version 1. openNURBS was our first open-source
project.

The code compiles on Windows, macOS, Linux, iOS, and Android. It’s used in
various third-party applications like ArchiCAD, SolidWorks, Inventor, SketchUp
and many other products to read or write _3dm_ files directly.

openNURBS is what Rhino uses natively to read/write _3dm_ files. This toolkit
is released before Rhino, so any product, including our competitors, can be
compatible with the latest _3dm_ files. There is no difference between the
_3dm_ files Rhino writes and those of other applications using openNURBS to
read and write _3dm_.

For more information about openNURBS, please see the [openNURBS
guides](https://developer.rhino3d.com/guides/opennurbs/).

### C++ SDK

On top of all of this is our C++ SDK, available only on Windows.

Compiling against the C++ SDK requires a specific version of Microsoft Visual
Studio and the Microsoft C-Runtime. You have to recompile for every major
version of Rhino.

Virtually everything Rhino can do is exposed through the C++ SDK. Some
commands and features haven’t been exposed yet, but this SDK is very broad and
rich.

Unfortunately, because it’s so tightly coupled to the Rhino Core, plugin
developers need to recompile their plugins for every Rhino release.

For more information about the C++ SDK, check out the [C/C++
guides](https://developer.rhino3d.com/guides/cpp/).

## C++ Stack

On the right column of the stack diagram above is the C++ portion of Rhino.
The C++ stack allows us - as well as third-party plugin developers - to write
Rhino plugins using the same C++ SDK that we use to develop Rhino itself. Note
that you cannot author Grasshopper components using C++.

### C++ Plugins

On top of the C++ SDK are C++ plugins. Many features that ship with Rhino,
including some Commands, File I/O, Renderers are actually C++ plugins. There
are also dozens of third-party C++ plugins, like [VisualARQ by
Asuni](http://www.visualarq.com/), [RhinoCAM by
MecSoft](https://mecsoft.com/rhinocam-software/), and [V-Ray by Chaos
Software](https://www.chaosgroup.com/vray/rhino).

For more information about the C++ SDK, check out the [C/C++
guides](https://developer.rhino3d.com/guides/cpp/).

### RhinoScript

One of the C++ plugins we ship with Rhino is
[RhinoScript](https://developer.rhino3d.com/guides/rhinoscript/what-are-
vbscript-rhinoscript/). RhinoScript exposes a useful subset of Rhino’s SDK via
VBScript - a widely used and popular scripting language. RhinoScript gives you
access not only to Rhino, but to any other COM object on Windows.

For more information, see the [RhinoScript
guides](https://developer.rhino3d.com/guides/rhinoscript/), and more
specifically the [What are VBScript and
RhinoScript?](https://developer.rhino3d.com/guides/rhinoscript/what-are-
vbscript-rhinoscript/) guide.

## .NET Stack

The .NET SDK is represented here in three layers:

  * C API
  * .NET Framework
  * RhinoCommon
  * Eto

### C API

A straight C API wraps the C++ SDK, allowing us to Platform Invoke (P/Invoke)
into the C++ SDK, forming a bridge between the native C++ code and the managed
.NET layers.

### .NET Framework

Microsoft develops the [.NET
Framework](https://www.microsoft.com/net/framework). .NET makes it possible to
write plugins in C#, F#, VB.NET, and any other language that compiles down to
Microsoft’s IL.

The Microsoft .NET framework ships with Windows.

In Rhino for Mac, we embed [.NET
Core](https://developer.rhino3d.com/guides/rhinocommon/moving-to-dotnet-core/)
within the app itself.

### RhinoCommon

RhinoCommon is our .NET SDK for Rhino, built atop the portions of the .NET
framework that are _common_ on both Windows and macOS (via Mono). RhinoCommon
allows developers to run .NET code on both Rhino for Windows and Rhino for
Mac.

For more information about RhinoCommon, see the [RhinoCommon
guides](https://developer.rhino3d.com/guides/rhinocommon/), or more
specifically, the [What is
RhinoCommon?](https://developer.rhino3d.com/guides/rhinocommon/what-is-
rhinocommon/) guide.

### Eto

Using RhinoCommon, you can write .NET plugins that work on Windows and
Mac…except for the User Interface. The Mono team did not clone WinForms or
WPF, so neither of those technologies work on the Mac. To address this
problem, Rhino now ships with Eto.Forms. Eto lets you write user interface
once in C#, XAML, or JSON and use it on Windows and macOS. Actually, your UI
written in Eto, can run on iOS, Android, and Linux, too.

For more information about Eto, check out [Eto.Forms on
GitHub](https://github.com/picoe/Eto).

### .NET Plugins

Built on top of RhinoCommon are numerous plugins, both internal and third-
party developed plugins. [Grasshopper](http://www.grasshopper3d.com/), for
example, is a RhinoCommon plugin. Some commands, renderers, and file IO
plugins in Rhino are actually written as RhinoCommon plugins. As time goes on,
we are moving more and more convenient functionality into RhinoCommon/.NET
plugins so as to share more code between platforms. Many successful third-
party plugins are also written using RhinoCommon and .NET, such as
[RhinoGold](http://www.tdmsolutions.com/) and [Matrix by
GEMVision](http://www.stuller.com/matrix), and [Orca3D](http://orca3d.com/).

For more information about RhinoCommon, see the [RhinoCommon
guides](https://developer.rhino3d.com/guides/rhinocommon/).

### Grasshopper Components

Rhino now ships with Grasshopper, our visual programming language for
algorithmic and parametric design. Grasshopper is a development platform unto
itself, with [hundreds of third-party authored Grasshopper
components](http://www.food4rhino.com/grasshopper-addons), for doing all sorts
of things from [physics
simulation](http://www.food4rhino.com/project/kangaroo), to [creating custom
user-interfaces](http://www.food4rhino.com/project/human-ui), to [industrial
robotic programming and control](http://www.food4rhino.com/project/hal).

For more information about Grasshopper, more specifically developing
Grasshopper components, check out the [Grasshopper
guides](https://developer.rhino3d.com/guides/grasshopper/).

### Python Scripts

One of the .NET plugins that ships with Rhino is RhinoPython. Written using
[IronPython](http://ironpython.net/), a .NET implementation of the
[python](https://www.python.org/) runtime, RhinoPython exposes the entire
RhinoCommon SDK to the python scripting language. That means any time we add a
feature to RhinoCommon, it shows up automatically in RhinoPython.

For more information about RhinoPython, see the [RhinoPython
guides](https://developer.rhino3d.com/guides/rhinopython/).

## Related Topics

  * [C/C++ guides](https://developer.rhino3d.com/guides/cpp/)
  * [openNURBS guides](https://developer.rhino3d.com/guides/opennurbs/)
  * [RhinoScript guides](https://developer.rhino3d.com/guides/rhinoscript/)
  * [Microsoft .NET Framework (on microsoft.com)](https://www.microsoft.com/net/framework)
  * [What is RhinoCommon?](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/)
  * [RhinoCommon guides](https://developer.rhino3d.com/guides/rhinocommon/)
  * [Mono Project](https://www.mono-project.com)
  * [Eto.Forms on GitHub](https://github.com/picoe/Eto)
  * [Grasshopper guides](https://developer.rhino3d.com/guides/grasshopper/)
  * [RhinoPython guides](https://developer.rhino3d.com/guides/rhinopython/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/general/rhino-
technology-overview/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/general/rhino-
technology-overview/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

