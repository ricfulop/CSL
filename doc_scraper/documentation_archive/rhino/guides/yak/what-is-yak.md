---
url: https://developer.rhino3d.com/guides/yak/what-is-yak/
scraped_at: 2025-09-08T15:57:58.914246
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

[What is the Package Manager?](https://developer.rhino3d.com/guides/yak/what-
is-yak/)

  * Overview
  * Server
  * Integrations
    * Package restore for Grasshopper
    * Package Manager UI
  * Command Line Tool
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Package Manager
Guides](https://developer.rhino3d.com/en/guides/yak/) /

What is the Package Manager?

by [Will Pearson](https://discourse.mcneel.com/u/will/) (Last updated:
Thursday, November 12, 2020)

## Overview

The Rhino Package Manager assists in the discovery, installation, and
management resources in the Rhino ecosystem (Grasshopper included!). Currently
it supports Rhino and Grasshopper plug-ins, but the goal is to include things
like scripts, materials, viewports, etc. in the future!

__Note __

The Rhino Package Manager was initially referred to by the codename “Yak”. The
name Yak is still used for the command line tool that creates and publishes
packages.

The package manager has several goals.

  * Make it easier for users to discover and manage plug-ins and more
  * Help developers and reusable content authors to share their work
  * Provide simple system administration tools

Not wanting to reinvent the wheel, we’ve taken inspiration from Linux and the
software development world. The package management system can be broken down
into three main areas.

  1. [Server](https://developer.rhino3d.com/guides/yak/what-is-yak/#server)
  2. [Integrations](https://developer.rhino3d.com/guides/yak/what-is-yak/#integrations)
  3. [Command line tool](https://developer.rhino3d.com/guides/yak/what-is-yak/#command-line-tool)

## Server

The package server is the heart of the system. Once created, packages are
pushed to the server to share them with others. It keeps the packages
organised for its clients – the command line tool and Rhino (via
integrations).

__Note __

In addition to the public package server (<https://yak.rhino3d.com>), the
package manager also supports file-/folder-based [custom package
repositories](../package-sources).

## Integrations

Integrations provide direct access to the package ecosystem from inside of
Rhino. Currently this has been done in two ways; “package restore” for
Grasshopper and the package manager UI.

### Package restore for Grasshopper

The Rhino Package Manager has been integrated into Grasshopper’s “Unrecognized
Objects” dialog, providing [package restore](../package-restore-in-
grasshopper) functionality. When opening a new file which contains components
from a plug-in not installed on the machine, the user is given the option to
check the package server for the missing plug-ins and install them directly.

![Package restore for Grasshopper](https://developer.rhino3d.com/images/yak-
gh-restore-guid.gif)

### Package Manager UI

The package manager UI is avilable via the `_PackageManager` command. It
provides a NuGet-style interface that allows users to search for packages,
install them and see if any updates are avilable to currently installed
packages.

![The package manager
UI](https://developer.rhino3d.com/images/testpackagemanager-wip.jpg)

## Command Line Tool

The command line tool provides a basic interface but with full functionality.
It is modelled on well known domain-specific package managers such as Ruby’s
`gem` and Python’s `pip`. It communicates with the server as well as hooking
into Rhino Accounts for authentication.

On Windows, the tool can be found at `"C:\Program Files\Rhino
8\System\yak.exe"`. On Mac there is a script, `"/Applications/Rhino
8.app/Contents/Resources/bin/yak"`.

Type `<path_to_yak> help` to get started.

## Related Topics

  * [Anatomy of a Package](https://developer.rhino3d.com/guides/yak/the-anatomy-of-a-package/)
  * [The Package Manifest](https://developer.rhino3d.com/guides/yak/the-package-manifest/)
  * [Yak CLI Reference](https://developer.rhino3d.com/guides/yak/yak-cli-reference/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/yak/what-
is-yak/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/yak/what-
is-yak/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

