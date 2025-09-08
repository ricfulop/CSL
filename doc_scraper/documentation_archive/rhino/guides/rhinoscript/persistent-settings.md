---
url: https://developer.rhino3d.com/guides/rhinoscript/persistent-settings/
scraped_at: 2025-09-08T15:42:53.401504
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

[Persistent
Settings](https://developer.rhino3d.com/guides/rhinoscript/persistent-
settings/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Persistent Settings

__

Windows only

by [Jess Maertterer](https://discourse.mcneel.com/u/Jess/) (Last updated:
Wednesday, December 5, 2018)

## Problem

It can be annoying to enter the same custom parameter each time you run a
script.

## Solution

The following script demonstrates how to use a private variable to store a
parameter during a Rhino session.

    
    
    ' How to script with persisting settings
    ' Jess Maertterer - 20.12.2004
    Option Explicit
    Private dblLength
    
    If IsEmpty(dblLength) Then
      dblLength = 2.00
    End If
    
    '/////////////////////////////////////////////////////////////
    Sub Extend_Curve_Length_Persist
      Dim arrCurves, strCurve, dblResult
      arrCurves = Rhino.GetObjects("Select curves to extend", 4)
      If Not IsNull(arrCurves) Then
        dblResult = Rhino.GetReal("Length to extend", dblLength,0.00)
        If Not IsNull(dblResult) Then
          dblLength = dblResult
          For Each strCurve in arrCurves
            Rhino.ExtendCurveLength strCurve, 2, 2, dblLength
          Next
        End If
      End If
    End Sub
    

If your script should remember the settings from the last session, then you
have to use the RhinoScript methods `SaveSettings` and `GetSettings` to access
a separate _.ini_ file.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/persistent-
settings/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/persistent-
settings/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

