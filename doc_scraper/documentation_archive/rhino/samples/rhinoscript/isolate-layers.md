---
url: https://developer.rhino3d.com/samples/rhinoscript/isolate-layers/
scraped_at: 2025-09-08T15:49:30.046507
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

Isolate Layers

__

Windows only

Demonstrates how to isolate the layers of selected objects using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub IsolateLayers()
    
      ' Select objects
      Dim objects
      objects = Rhino.GetObjects("Select objects on layers to isolate", , True, True)
      If Not IsArray(objects) Then Exit Sub
    
      ' Determine the number of selected objects
      Dim bound
      bound = UBound(objects)
    
      ' Create an array to the object layer names
      Dim object_layers()
      ReDim object_layers( bound + 1 )
    
      ' Fill the array
      Dim i
      For i = 0 To bound
        object_layers(i) = Rhino.ObjectLayer(objects(i))
      Next
    
      ' Don't forget to include current layer      
      object_layers(bound + 1) = Rhino.CurrentLayer
    
      ' Cull any duplicate layer names
      Dim culled_layers
      culled_layers = Rhino.CullDuplicateStrings(object_layers)
    
      ' Create an array containing all of the layer names
      Dim all_layers
      all_layers = Rhino.LayerNames
    
      ' For each layer name, search the list of culled layer names.
      ' If the layer name is not found, then turn it off.
      Dim layer
      For Each layer In all_layers
        If UBound(Filter(culled_layers, layer)) < 0 Then
          Rhino.LayerMode layer, 1
        End If
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

