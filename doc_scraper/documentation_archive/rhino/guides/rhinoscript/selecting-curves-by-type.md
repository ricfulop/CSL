---
url: https://developer.rhino3d.com/guides/rhinoscript/selecting-curves-by-type/
scraped_at: 2025-09-08T15:42:29.321319
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

[Selecting Curves by
Type](https://developer.rhino3d.com/guides/rhinoscript/selecting-curves-by-
type/)

  * Non-Linear Curves
  * Linear Curves

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Selecting Curves by Type

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Non-Linear Curves

The following RhinoScript subroutine will select all non-linear curves in the
document:

    
    
    Sub SelNonLinearCrv()
      Dim arrCurves, strCurve
      arrCurves = Rhino.ObjectsByType(4)
      If IsArray(arrCurves) Then
        Rhino.EnableRedraw False
        For Each strCurve In arrCurves
          If Not Rhino.IsCurveLinear(strCurve) Then
            Rhino.SelectObject strCurve
          End If
        Next
        Rhino.EnableRedraw True
      End If
    End Sub
    

## Linear Curves

The following RhinoScript subroutine will select all linear curves in the
document:

    
    
    Sub SelLinearCrv()
      Dim arrCurves, strCurve
      arrCurves = Rhino.ObjectsByType(4)
      If IsArray(arrCurves) Then
        Rhino.EnableRedraw False
        For Each strCurve In arrCurves
          If Rhino.IsCurveL
          inear(strCurve) Then
            Rhino.SelectObject strCurve
          End If
        Next
        Rhino.EnableRedraw True
      End If
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/selecting-
curves-by-type/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/selecting-
curves-by-type/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

