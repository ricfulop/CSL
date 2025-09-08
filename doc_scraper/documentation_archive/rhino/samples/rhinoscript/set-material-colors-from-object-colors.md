---
url: https://developer.rhino3d.com/samples/rhinoscript/set-material-colors-from-object-colors/
scraped_at: 2025-09-08T15:50:35.294541
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

Set Material Colors from Object Colors

__

Windows only

Demonstrates how to modify an object's material color to match its display
color using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub SetMaterialColorsFromObjectColors
    
     ' Constants
     Const rhColorByLayer = 0
     Const rhColorByObject = 1
    
     ' Variables
     Dim aObjects, sObject
     Dim nColor, nSource
     Dim sLayer, nMaterial
    
     ' Get all objects in the document
     aObjects = Rhino.AllObjects
     If Not IsArray(aObjects) Then Exit Sub
    
     ' Process each object    
     For Each sObject In aObjects
    
       ' Get the object's color and color source
       nColor = Rhino.ObjectColor(sObject)
       nSource = Rhino.ObjectColorSource(sObject)
       nMaterial = -1
    
       ' If the object's color source is "by layer"
       ' then get the layer's material index. If the
       ' layer does not have a material, add one.    
       If (nSource = rhColorByLayer) Then
         sLayer = Rhino.ObjectLayer(sObject)
         nMaterial = Rhino.LayerMaterialIndex(sLayer)
         If( nMaterial < 0 ) Then
           nMaterial = Rhino.AddMaterialToLayer(sLayer)
         End If
    
       ' If the object's color source is "by object"
       ' then get the object's material index. If the
       ' object does not have a material, add one.    
       ElseIf (nSource = rhColorByObject) Then
         nMaterial = Rhino.ObjectMaterialIndex(sObject)
         If( nMaterial < 0 ) Then
           nMaterial = Rhino.AddMaterialToObject(sObject)
         End If
    
       End If
    
       ' Set the material color
       If (nMaterial >= 0) Then
         If (nColor <> Rhino.MaterialColor(nMaterial)) Then
           Rhino.MaterialColor nMaterial, nColor
         End If
       End If
    
     Next
    
     ' Redraw the document
     Rhino.Redraw
    
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

