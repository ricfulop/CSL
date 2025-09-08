---
url: https://developer.rhino3d.com/guides/rhinoscript/isometric-views/
scraped_at: 2025-09-08T15:42:49.413004
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

[Isometric Views](https://developer.rhino3d.com/guides/rhinoscript/isometric-
views/)

  * Overview
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Isometric Views

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

AutoCAD has a VPOINT command that allows you to create isometric views of the
model. The VPOINT command uses the point entered by the user to create a
vector that defines the direction from which the drawing is viewed. You can do
this in Rhino using the ViewportProperties command. In the ViewportProperties
dialog, first set the view to parallel projection. Then, set the target
location to 0,0,0 and the camera location to where you want to be viewing
from.

If this seems too cumbersome, then you can also use the following RhinoScript
subroutine…

## Example

The following example subroutine mimics the VPOINT command using RhinoScript…

    
    
    Sub VPoint
    
      Dim strView
      strView = Rhino.CurrentView
      If Rhino.ViewProjection(strView) = 2 Then
        Rhino.Print "Viewport must be set for parallel projection."
        Exit Sub
      End If
    
      Dim arrOptions
      arrOptions = Array("NE Isometric", "NW Isometric", "SE Isometric", "SW Isometric", "User Defined")
    
      Dim strOption
      strOption = Rhino.ListBox(arrOptions, "Select viewing direction", "VPoint")
      If IsNull(strOption) Then Exit Sub
    
      Dim arrCamera
      Select Case strOption
        Case "NE Isometric" arrCamera = Array( 1, 1,1)
        Case "NW Isometric" arrCamera = Array(-1, 1,1)
        Case "SE Isometric" arrCamera = Array( 1,-1,1)
        Case "SW Isometric" arrCamera = Array(-1,-1,1)
        Case Else arrCamera = Rhino.GetPoint("View point")
      End Select
    
      If Not IsArray(arrCamera) Then Exit Sub
    
      Dim arrTarget, v
      arrTarget = Array(0,0,0)
      v = Rhino.VectorCreate(arrCamera, arrTarget)
      If Rhino.IsVectorTiny(v) Then Exit Sub
    
      Rhino.EnableRedraw False    
      Rhino.ViewCameraTarget strView, arrCamera, arrTarget
      Rhino.ZoomExtents strView
      Rhino.EnableRedraw True
    
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/isometric-
views/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/isometric-
views/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

