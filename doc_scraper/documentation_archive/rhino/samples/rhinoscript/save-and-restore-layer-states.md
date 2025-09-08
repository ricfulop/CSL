---
url: https://developer.rhino3d.com/samples/rhinoscript/save-and-restore-layer-states/
scraped_at: 2025-09-08T15:49:31.078147
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

Save and Restore Layer States

__

Windows only

Demonstrates how to save and restore the states of layers using RhinoScript.

VBScript

    
    
    Option Explicit
    
    '--------------------------------------------------------------------
    ' Subroutine: SaveLayerStates
    ' Purpose:    Saves a "named" layer state to an INI-style file.
    '--------------------------------------------------------------------
    Sub SaveLayerStates
    
      If StrComp(Rhino.DocumentName, "untitled", 1) = 0 Then
        Rhino.MessageBox "You must save your model before using _
                                 this script.", 48, "LayerStates"
        Exit Sub
      End If
    
      Dim arrLayers
      arrLayers = Rhino.LayerNames
      If Not IsArray(arrLayers) Then Exit Sub
    
      Dim strName
      strName = Rhino.StringBox("Save Layer State As", , "LayerStates")
      If IsNull(strName) Then Exit Sub
    
      Dim strFile
      strFile = Rhino.DocumentPath & Rhino.DocumentName
      strFile = Replace(strFile, ".3dm", ".layer", 1, -1, 1)
    
      Dim strLayer, strValue
      For Each strLayer In arrLayers
        strValue = CStr(CInt(Rhino.IsLayerCurrent(strLayer)))
        strValue = strValue & ";" & CStr(Rhino.LayerMode(strLayer))
        strValue = strValue & ";" & CStr(Rhino.LayerColor(strLayer))
        Rhino.SaveSettings strFile, strName, strLayer, strValue
      Next
    
    End Sub
    
    '--------------------------------------------------------------------
    ' Subroutine: RestoreLayerStates
    ' Purpose:    Restores a "named" layer state from an INI-style file.
    '--------------------------------------------------------------------
    Sub RestoreLayerStates
    
      If StrComp(Rhino.DocumentName, "untitled", 1) = 0 Then
        Rhino.MessageBox "This script only works on saved models.", _
                                 48, "LayerStates"
        Exit Sub
      End If
    
      Dim strFile
      strFile = Rhino.DocumentPath & Rhino.DocumentName
      strFile = Replace(strFile, ".3dm", ".layer", 1, -1, 1)
    
      Dim arrNames
      arrNames = Rhino.GetSettings(strFile)
      If Not IsArray(arrNames) Then
        Rhino.MessageBox "No layer states to restore.", 64, "LayerStates"
        Exit Sub
      End If
    
      Dim strName
      strName = Rhino.ListBox(arrNames, "Layer state to restore", _
                                     "LayerStates")
      If IsNull(strName) Then Exit Sub  
    
      Dim arrLayers
      arrLayers = Rhino.GetSettings(strFile, strName)
      If Not IsArray(arrLayers) Then
        Rhino.MessageBox "No layers to restore.", 64, "LayerStates"
        Exit Sub
      End If
    
      Dim strLayer, strValue, arrValues
      For Each strLayer In arrLayers
        strValue = Rhino.GetSettings(strFile, strName, strLayer)
        arrValues = Split(strValue, ";")
        If CBool(arrValues(0)) = True Then Rhino.CurrentLayer strLayer
        Rhino.LayerMode strLayer, CInt(arrValues(1))
        Rhino.LayerColor strLayer, CLng(arrValues(2))
      Next
    
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

