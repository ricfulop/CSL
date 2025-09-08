---
url: https://developer.rhino3d.com/samples/rhinoscript/modify-flamingo-plant/
scraped_at: 2025-09-08T15:49:58.192282
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

Modify Flamingo Plant

__

Windows only

Demonstrates how to modify an existing Flamingo nXt plant using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Call Main()
    
    Sub Main()
    	Dim objPlugIn, strObject, plant, xml, xmlDoc, node
    	On Error Resume Next
    	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
    	If Err Then
    		MsgBox Err.Description
    		Exit Sub
    	End If
    	strObject = Rhino.GetObject("Select object")
      If Not IsNull(strObject) And Not strObject = "" Then
    		Set plant = objPlugIn.PlantFromObject(strObject)
        If IsNull(plant) Then
          Rhino.Print("Object is not a plant")
        Else
          xml = plant.XmlWithoutHeader
          If IsNull(xml) Then
            Rhino.Print("Error extracting plant XML")
          Else
            Set xmlDoc = CreateObject("Microsoft.XMLDOM")
            If IsNull(xmlDoc) Then
              Rhino.Print("Error creating XML document")
            Else
              xmlDoc.LoadXml(xml)
              Set node = xmlDoc.SelectSingleNode("ArPlantDef/PlantDef/nTrunks")
              If IsNull(node) Or IsEmpty(node) Then
                Rhino.Print("Error getting plant XML")
              Else
                'Mofiy the trunk value changing it to 3 trunks
                node.Text = "3"
                If objPlugIn.ModifyPlantObject(strObject, xmlDoc.xml) Then
                  Rhino.Print("Plant now has three trunks...")
                Else
                  Rhino.Print("Error modifing plant...")
                End If
              End If
            End If
          End If
        End If
    	End If
      Set plant = Nothing
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

