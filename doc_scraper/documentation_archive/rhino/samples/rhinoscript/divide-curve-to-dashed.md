---
url: https://developer.rhino3d.com/samples/rhinoscript/divide-curve-to-dashed/
scraped_at: 2025-09-08T15:49:11.955624
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

Divide Curve to Dashed

__

Windows only

Demonstrates how to chop up a curve into segments and spaces.

VBScript

    
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' DivideCurveDashed.rvb -- October 2010
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0 and 5.0.
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Option Explicit
    
    ' Divides a curve into "dashed" segments
    Sub DivideCurveDashed
    
      Dim curve, slength, dlength
      Dim i, length, pt, t, dom, results
    
      curve = Rhino.GetObject("Select curve to divide", 4, True)
      If IsNull(curve) Then Exit Sub
    
      slength = Rhino.GetReal("Segment length", 1.0)
      If IsNull(slength) Then Exit Sub
      If (slength <= 0) Then Exit Sub  
    
      dlength = Rhino.GetReal("Dash length", 1.0)
      If IsNull(dlength) Then Exit Sub
      If (dlength <= 0) Then Exit Sub
    
      Call Rhino.EnableRedraw(False)
      i = 0
    
      Do
    
        If (i Mod 2 = 0) Then
          length = slength
        Else
          length = dlength
        End If
    
        pt = Rhino.CurveArcLengthPoint(curve, length)
        If IsNull(pt) Then Exit Do
    
        t = Rhino.CurveClosestPoint(curve, pt)
    
        If (i Mod 2 = 0) Then
          results = Rhino.SplitCurve(curve, t, True)
          curve = results(1)
        Else
          dom = Rhino.CurveDomain(curve)
          curve = Rhino.TrimCurve(curve, Array(t, dom(1)), True)
        End If
    
        i = i + 1
    
      Loop While True    
    
      Call Rhino.EnableRedraw(True)
    
    End Sub
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Drag & drop and alias creation stuff
    Rhino.AddStartUpScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "DivideCurveDashed", "_-RunScript (DivideCurveDashed)"
    

  

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

