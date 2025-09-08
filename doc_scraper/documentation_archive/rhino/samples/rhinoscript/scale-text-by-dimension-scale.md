---
url: https://developer.rhino3d.com/samples/rhinoscript/scale-text-by-dimension-scale/
scraped_at: 2025-09-08T15:50:33.290382
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

Scale Text by Dimension Scale

__

Windows only

Demonstrates how to properly scale text objects by the document's dimension
scale in RhinoScript.

VBScript

    
    
    Option Explicit
    
    ' Scales all text objects by the document's dimension scale
    Sub DimScaleText
    
      ' Dim local variables
      Dim arrObjects, strObject, arrPlane, dblScale
    
      ' Get document's dimension scale  
      dblScale = Rhino.DimScale
      If dblScale = 1.0 Then
        Rhino.Print "Dimension scale set to 1.0."
        Exit Sub
      End If
    
      ' Get ids of all annotation objects    
      arrObjects = Rhino.ObjectsByType(512)
      If Not IsArray(arrObjects) Then
        Rhino.Print "No text objects to scale."
        Exit Sub
      End If
    
      ' Turn off viewport redrawing (faster)    
      Rhino.EnableRedraw False
    
      ' Save current view's construction plane
      arrPlane = Rhino.ViewCPlane(Rhino.CurrentView)
    
      ' Process each object
      For Each strObject In arrObjects
    
        ' Verify object is a text object
        If Rhino.IsText(strObject) And Rhino.IsObjectSelectable(strObject) Then
    
          ' Set the current view's construction plane to plane
          ' that defines the position and orientatio of the text
          Rhino.ViewCPlane Rhino.CurrentView, Rhino.TextObjectPlane(strObject)
    
          ' Select the object
          Rhino.SelectObject strObject
    
          ' Scale the object by the dimension scale
          Rhino.Command "_-Scale 0,0,0 " & CStr(dblScale), False
    
          ' Unselect the object
          Rhino.UnselectObject strObject
    
        End If
      Next
    
      ' Restore current view's construction plane
      Rhino.ViewCPlane Rhino.CurrentView, arrPlane
    
      ' Turn on viewport drawing
      Rhino.EnableRedraw True
    
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

