---
url: https://developer.rhino3d.com/guides/cpp/plugin-search-order/
scraped_at: 2025-09-08T15:40:06.717665
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

[Plugin Search Order](https://developer.rhino3d.com/guides/cpp/plugin-search-
order/)

  * Overview
  * Alternate Search Order
  * Standard Search Order
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Plugin Search Order

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Rhino plugins are Windows Dynamic Link Libraries, or DLLs. As such, Rhino uses
Windows to load your plugin. Rhino attempts to load your plugin, and any
dependent DLLs, in the following manner:

  1. Alternate Search Order - uses `LoadLibraryEx` with the `LOAD_WITH_ALTERED_SEARCH_PATH` flag.
  2. Standard Search Order - uses `LoadLibrary`.

**NOTE** : starting with Windows XP and later, the dynamic-link library (DLL)
search order used by the system depends on the setting of the
`HKLM\System\CurrentControlSet\Control\Session Manager\SafeDllSearchMode`
value. For Windows Server 2003: The default value is 1. Windows XP: The
default value is 0.

## Alternate Search Order

The `LoadLibraryEx` function supports an alternate search order if the call
specifies `LOAD_WITH_ALTERED_SEARCH_PATH` and the `lpFileName` parameter
specifies a path. If `SafeDllSearchMode` is 1, the alternate search order is
as follows:

  1. The directory specified by `lpFileName`.
  2. The system directory. Use the `GetSystemDirectory` function to get the path of this directory.
  3. The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
  4. The Windows directory. Use the `GetWindowsDirectory` function to get the path of this directory.
  5. The current directory.
  6. The directories that are listed in the `PATH` environment variable.

If `SafeDllSearchMode` is 0, the alternate search order is as follows:

  1. The directory specified by `lpFileName`.
  2. The current directory.
  3. The system directory. Use the `GetSystemDirectory` function to get the path of this directory.
  4. The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
  5. The Windows directory. Use the `GetWindowsDirectory` function to get the path of this directory.
  6. The directories that are listed in the `PATH` environment variable.

## Standard Search Order

If `SafeDllSearchMode` is 1, the search order is as follows:

  1. The directory from which the application loaded.
  2. The system directory. Use the `GetSystemDirectory` function to get the path of this directory.
  3. The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
  4. The Windows directory. Use the `GetWindowsDirectory` function to get the path of this directory.
  5. The current directory.
  6. The directories that are listed in the `PATH` environment variable.

If `SafeDllSearchMode` is 0, the search order is as follows:

  1. The directory from which the application loaded.
  2. The current directory.
  3. The system directory. Use the `GetSystemDirectory` function to get the path of this directory.
  4. The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
  5. The Windows directory. Use the `GetWindowsDirectory` function to get the path of this directory.
  6. The directories that are listed in the `PATH` environment variable.

Note, Windows 2000 does not support the `SafeDllSearchMode` value. T he search
order for Windows 2000 is as follows:

  1. The directory from which the application loaded.
  2. The current directory.
  3. The system directory. Use the `GetSystemDirectory` function to get the path of this directory.
  4. The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
  5. The Windows directory. Use the `GetWindowsDirectory` function to get the path of this directory.
  6. The directories that are listed in the `PATH` environment variable.

## Related Topics

  * [Plugin Loading](https://developer.rhino3d.com/guides/cpp/plugin-loading/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/plugin-
search-order/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/plugin-
search-order/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

