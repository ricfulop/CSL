---
url: https://developer.rhino3d.com/samples/rhinoscript/move-curve-grips/
scraped_at: 2025-09-08T15:49:22.000949
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

Move Curve Grips

__

Windows only

Demonstrates how to move a curve's grips using RhinoScript.

VBScript

    
    
    Sub MoveCurveGrip
      Const rhCurve = 4
    
      Dim sCurve : sCurve = Rhino.GetObject("Select a curve", rhCurve)
      If IsNull(sCurve) Then Exit Sub
    
      Dim bGripsOn : bGripsOn = Rhino.ObjectGripsOn(sCurve)
      If (bGripsOn = False) Then
        bGripsOn = Rhino.EnableObjectGrips(sCurve, True)
      End If
    
      Dim aGrip : aGrip = Rhino.GetObjectGrip("Select a curve grip")
      If IsArray(aGrip) Then
        Dim aPt : aPt = aGrip(2)
        aPt(2) = aPt(2) + 1.0
        Rhino.ObjectGripLocation sCurve, aGrip(1), aPt
      End If
    
      If (bGripsOn = True) Then
        Rhino.EnableObjectGrips sCurve, False
      End If
    
    End Sub
    

  

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

