---
url: https://developer.rhino3d.com/samples/rhinocommon/move-objects-to-current-layer/
scraped_at: 2025-09-08T15:44:49.445084
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

Move Objects to Current Layer

Demonstrates how to move object to the currently active layer.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result MoveObjectsToCurrentLayer(RhinoDoc doc)
      {
        // all non-light objects that are selected
        var object_enumerator_settings = new ObjectEnumeratorSettings();
        object_enumerator_settings.IncludeLights = false;
        object_enumerator_settings.IncludeGrips = true;
        object_enumerator_settings.NormalObjects = true;
        object_enumerator_settings.LockedObjects = true;
        object_enumerator_settings.HiddenObjects = true;
        object_enumerator_settings.ReferenceObjects = true;
        object_enumerator_settings.SelectedObjectsFilter = true;
        var selected_objects = doc.Objects.GetObjectList(object_enumerator_settings);
    
        var current_layer_index = doc.Layers.CurrentLayerIndex;
        foreach (var selected_object in selected_objects)
        {
          selected_object.Attributes.LayerIndex = current_layer_index;
          selected_object.CommitChanges();
        }
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function MoveObjectsToCurrentLayer(ByVal doc As RhinoDoc) As Result
    	' all non-light objects that are selected
    	Dim object_enumerator_settings = New ObjectEnumeratorSettings()
    	object_enumerator_settings.IncludeLights = False
    	object_enumerator_settings.IncludeGrips = True
    	object_enumerator_settings.NormalObjects = True
    	object_enumerator_settings.LockedObjects = True
    	object_enumerator_settings.HiddenObjects = True
    	object_enumerator_settings.ReferenceObjects = True
    	object_enumerator_settings.SelectedObjectsFilter = True
    	Dim selected_objects = doc.Objects.GetObjectList(object_enumerator_settings)
    
    	Dim current_layer_index = doc.Layers.CurrentLayerIndex
    	For Each selected_object In selected_objects
    	  selected_object.Attributes.LayerIndex = current_layer_index
    	  selected_object.CommitChanges()
    	Next selected_object
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.Commands import *
    from Rhino.DocObjects import *
    from scriptcontext import doc
    
    def RunCommand():
        # all non-light objects that are selected
        object_enumerator_settings = ObjectEnumeratorSettings()
        object_enumerator_settings.IncludeLights = False
        object_enumerator_settings.IncludeGrips = True
        object_enumerator_settings.NormalObjects = True
        object_enumerator_settings.LockedObjects = True
        object_enumerator_settings.HiddenObjects = True
        object_enumerator_settings.ReferenceObjects = True
        object_enumerator_settings.SelectedObjectsFilter = True
        selected_objects = doc.Objects.GetObjectList(object_enumerator_settings)
    
        current_layer_index = doc.Layers.CurrentLayerIndex
        for selected_object in selected_objects:
            selected_object.Attributes.LayerIndex = current_layer_index
            selected_object.CommitChanges()
    
        doc.Views.Redraw()
        return Result.Success
    
    if __name__ == "__main__":
        RunCommand()
    

  

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

