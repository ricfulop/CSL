---
url: https://developer.rhino3d.com/samples/rhinoscript/tag-object-as-flamingo-plant/
scraped_at: 2025-09-08T15:50:01.204559
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

Tag Object As Flamingo Plant

__

Windows only

Demonstrates how to tag an object as a Flamingo nXt plant in RhinoScript.

VBScript

    
    
    Option Explicit
    
    Call Main()
    
    Sub Main()
    	Dim objPlugIn, plantFile, strObject, topiary, location, plant
    	On Error Resume Next
    	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
    	If Err Then
    		MsgBox Err.Description
    		Exit Sub
    	End If
      plantFile = objPlugIn.GetPlantFileName("")
      If Not IsNull(plantFile) Then
    	  strObject = Rhino.GetObject("Select object to tag as plant")
        If Not IsNull(strObject) And Not strObject = "" Then
          topiary = False
          location = Array(0.0, 0.0, 0.0)
          If objPlugIn.PlantFileNameIsGroundcover(plantFile) Then
            topiary = Rhino.GetBoolean("Plant topiary", Array( "Topiary", "Off", "On"), Array(topiary))
          Else
            location = Rhino.GetPoint("Plant location")
          End If
          If Not IsNull(location) And Not IsNull(topiary) Then
            Set plant = objPlugIn.NewPlant()
            plant.FileName = plantFile
            plant.Location = location
            plant.Topiary = topiary
            If objPlugIn.TagObjectAsPlant(strObject, Plant) Then
                Rhino.Print("Plant " & plantName & " assigned to selected object")
            End If
            Set plant = Nothing
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

