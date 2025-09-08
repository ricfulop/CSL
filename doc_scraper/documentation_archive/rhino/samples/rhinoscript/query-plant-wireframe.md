---
url: https://developer.rhino3d.com/samples/rhinoscript/query-plant-wireframe/
scraped_at: 2025-09-08T15:50:00.154911
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

Query Plant Wireframe

__

Windows only

Demonstrates how to generate a wire-frame representation of a Flamingo 2.0
plant using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Call Main()
    
    Sub Main()
    	Dim objPlugIn, plant, lines, line, i, count
    	On Error Resume Next
    	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
    	If Err Then
    		MsgBox Err.Description
    		Exit Sub
    	End If
      plant = objPlugIn.ModalFlamingo2PlantBrowser("", "", "")
      If Not IsNull(plant) Then
        lines = objPlugIn.GetFlamingo2PlantWireframe(plant(0), plant(1), plant(2))
        If Not IsNull(lines) Then
          count = UBound(lines)
          If count > 0 Then
            For i = 0 to count
              Rhino.Print("Line " & (i + 1) & " of " & (count + 1))
              Rhino.AddLine Array(lines(i,0), lines(i,1), lines(i,2)), Array(lines(i,3), lines(i,4), lines(i,5))
            Next
          	Rhino.Redraw()
          End If
        End If
    	End If
    	Set objPlugIn = Nothing
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

