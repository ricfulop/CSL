---
url: https://developer.rhino3d.com/samples/cpp/move-objects-to-current-layer/
scraped_at: 2025-09-08T15:47:59.732436
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

Move Objects to the Current Layer

__

Windows only

Demonstrates how to iterate through the Rhino geometry table and modify the
layer of selected objects.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Get the current layer index
      const CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;
      int layer_index = layer_table.CurrentLayerIndex();
    
      // Create an object iterator that filters on selected,
      // non-light objects in the current document only
      CRhinoObjectIterator it( CRhinoObjectIterator::normal_objects,
                               CRhinoObjectIterator::active_objects  );
      it.EnableSelectedFilter( TRUE );
      it.IncludeLights( FALSE );
      CRhinoObject* obj = NULL;
      int count = 0;
    
      // Walk the geometry table
      for( obj = it.First(); obj; obj = it.Next() )
      {
        // Ignore select objects that are already on the current layer
        if( obj->Attributes().m_layer_index == layer_index )
          continue;
        // Copy the object's attributes and set the new layer index
        CRhinoObjectAttributes atts( obj->Attributes() );
        atts.m_layer_index = layer_index;
        // Modify the object's attributes
        CRhinoObjRef ref(obj);
        if( context.m_doc.ModifyObjectAttributes(ref, atts) )
          count++;
      }
      if( count > 0 )
        context.m_doc.Redraw();
     return CRhinoCommand::success;
    }
    

  

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

