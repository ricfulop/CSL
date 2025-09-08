---
url: https://developer.rhino3d.com/samples/rhinoscript/set-hierarchical-layer-names/
scraped_at: 2025-09-08T15:49:32.047334
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

Set Hierarchical Layer Names

__

Windows only

Demonstrates how to rename layers in a hierarchical manner using RhinoScript.

VBScript

    
    
    Option Explicit
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' SetHierarchicalLayerNames
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub SetHierarchicalLayerNames()
    
      ' String that separates layer names
      Const separator = "-"
    
      ' Get all of the layer names.
      Dim all_layer
      all_layer = Rhino.LayerNames
    
      ' If only one layer, just bail.
      If UBound(all_layer) = 0 Then Exit Sub
    
      ' Build an array of layers who have no parent
      ' and that are from a reference file.
      Dim root_layers(), layer_count
      layer_count = 0  
      Dim layer_name, parent_layer
      For Each layer_name In all_layer
        parent_layer = Rhino.ParentLayer(layer_name)
        If IsNull(parent_layer) And Rhino.IsLayerReference(layer_name) = vbFalse Then
          ReDim Preserve root_layers(layer_count)
          root_layers(layer_count) = layer_name
          layer_count = layer_count + 1
        End If
      Next
    
      ' If the lists are the same size, then there are not
      ' child layers. So, just bail.
      If UBound(all_layer) = UBound(root_layers) Then Exit Sub
    
      ' Process the list of parentless layers    
      ProcessLayerList root_layers, separator
    
    End Sub
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' ProcessLayerList
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub ProcessLayerList(layer_list, separator)
      ' Process each layer in the array. Note,
      ' this is a recursive function.
      Dim layer_name, layer_children
      For Each layer_name In layer_list
        ProcessLayer layer_name, separator
      Next
    End Sub
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' ProcessLayer
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub ProcessLayer(layer_name, separator)
    
      ' Get the layer's parent
      Dim parent_layer, renamed_layer, layer_children
      parent_layer = Rhino.ParentLayer(layer_name)
    
      ' If the layer has a parent, then modify its name
      ' to include its parent name.
      If IsNull(parent_layer) Then
        renamed_layer = layer_name
      Else
        renamed_layer = parent_layer & separator & layer_name
        Rhino.RenameLayer layer_name, renamed_layer
      End If
    
      ' Get the layer's immediate children
      layer_children = Rhino.LayerChildren(renamed_layer)
      If IsArray(layer_children) Then
        ' Process these layers too    
        ProcessLayerList layer_children, separator
      End If  
    
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

