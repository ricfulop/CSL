---
url: https://developer.rhino3d.com/samples/rhinoscript/export-layer-objects/
scraped_at: 2025-09-08T15:49:29.043985
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

Export Layer Objects

__

Windows only

Demonstrates how to export all objects by layer, with each layer exported to a
new file using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub ExportLayerObjects
    
      ' Declare local variables
      Dim strPath, strFile
      Dim arrLayers, strLayer
      Dim arrSelected
    
      ' Get the path to and name of the current document.
      ' Surround with double-quotes in case path includes spaces.
      strPath = Chr(34) & Rhino.DocumentPath & Rhino.DocumentName & Chr(34)
    
      ' Get names of all layers
      arrLayers = Rhino.LayerNames
    
      ' Disable redrawing
      Rhino.EnableRedraw False
    
      ' Process each layer
      For Each strLayer In arrLayers
    
        ' Unselect all   
        Rhino.Command "_-SelNone", 0
    
        ' Select all objects on layer. Surround layer name
        ' with double-quotes in case it includes spaces.
        Rhino.Command "_-SelLayer " & Chr(34) & strLayer & Chr(34), 0
    
        ' Make sure some objects were selected
        arrSelected = Rhino.SelectedObjects
        If IsArray(arrSelected) Then
    
          ' Generate a modified path string
          ' that includes the layer name
          strFile = strPath
          strFile = Replace(strFile, ".3dm", "_" & strLayer & ".3dm")
    
          ' Export the selected objects
          Rhino.Command "_-Export " & strFile, 0
    
        End If
      Next
    
      ' Unselect all
      Rhino.Command "_-SelNone", 0
    
      ' Enable redrawing
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

