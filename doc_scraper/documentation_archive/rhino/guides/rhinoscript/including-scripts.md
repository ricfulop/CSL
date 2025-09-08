---
url: https://developer.rhino3d.com/guides/rhinoscript/including-scripts/
scraped_at: 2025-09-08T15:42:20.299591
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

[Including
Scripts](https://developer.rhino3d.com/guides/rhinoscript/including-scripts/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Including Scripts

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

In programming languages like C/C++ and C#, there are statements like
`#include` and `using` where you can reference functions from other source
files. This is often used when you want to build a library of common functions
that can be used from within other scripts,

VBScript does not have an equivalent to the C/C++ `#include` statement. But,
its possible to write your own include-type function.

## Solution

The following subroutine can be used to include scripts…

    
    
    ' ---------------------------------------------------------------------------
    ' Subroutine:  Include
    ' Purpose:     Includes, or loads, other RhinoScript files
    ' Argument:    A script file name to include
    ' Example:     Call Include("C:\Scripts\MyScriptFile.rvb")
    ' ---------------------------------------------------------------------------
    Sub Include(strScriptName)
      Dim objFSO, objFile
      Set objFSO = CreateObject("Scripting.FileSystemObject")
      Set objFile = objFSO.OpenTextFile(strScriptName)
      ExecuteGlobal objFile.ReadAll()
      objFile.Close
    End Sub
    

Also, if you have a number of script files that define utility functions and
procedures that you would like to call from any source file, then consider
adding these script files to the list of startup script file (_Tools_ >
_Options_ > _RhinoScript_).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/including-
scripts/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/including-
scripts/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

