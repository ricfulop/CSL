---
url: https://developer.rhino3d.com/samples/rhinoscript/flamingo-legacy-plant-browser/
scraped_at: 2025-09-08T15:49:51.134561
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

Flamingo Legacy Plant Browser

__

Windows only

Demonstrates how to display the Flamingo nXt legacy plant browser using
RhinoScript.

VBScript

    
    
    Option Explicit
    
    Call Main()
    
    Sub Main()
    	Dim objPlugIn, plant
    	On Error Resume Next
    	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
    	If Err Then
    		MsgBox Err.Description
    		Exit Sub
    	End If
      plant = objPlugIn.ModalFlamingo2PlantBrowser("", "", "")
      If Not IsNull(plant) Then
        Rhino.Print("Library(" & plant(0) & ") Folder(" & plant(1) & ") Plant(" & plant(2) & ")")
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

