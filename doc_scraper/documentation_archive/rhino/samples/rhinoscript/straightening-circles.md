---
url: https://developer.rhino3d.com/samples/rhinoscript/straightening-circles/
scraped_at: 2025-09-08T15:49:27.018235
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

Straightening Circles

__

Windows only

Demonstrates how to create lines based on circle geometry using RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' StraightenCircles.rvb -- September 2008
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    
    Option Explicit
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' StraightenCircles
    ' Creates lines based on the circumferences of circles.
    ' Lines will be oriented based on the plane of the circle.
    
    Sub StraightenCircles
    
      Dim obj_list, obj
      Dim length, plane, origin, xaxis
      Dim endpt, line
    
      obj_list = Rhino.GetObjects("Select circles to straighten", 4, True, True)
      If IsArray(obj_list) Then
    
        Call Rhino.EnableRedraw(False)
    
        For Each obj In obj_list
          If Rhino.IsCircle(obj) Then
            ' Gather data
            length = Rhino.CurveLength(obj)
            plane = Rhino.CurvePlane(obj)
            origin = plane(0)
            xaxis = plane(1)
            ' Calculate
            xaxis = Rhino.VectorUnitize(xaxis)
            xaxis = Rhino.VectorScale(xaxis, length)
            endpt = Rhino.PointAdd(origin, xaxis)
            line = Rhino.AddLine(origin, endpt)
            Call Rhino.SelectObject(line)
          End If
    
        Next
    
        Call Rhino.EnableRedraw(True)
    
      End If
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "StraightenCircles", "_NoEcho _-RunScript (StraightenCircles)"
    

  

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

