---
url: https://developer.rhino3d.com/samples/cpp/select-objects-by-layer/
scraped_at: 2025-09-08T15:48:00.669321
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

Select Objects by Layer

__

Windows only

Demonstrates how to select all of the objects on a specified layer.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Get a reference to the layer table
      CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;
      // Get the current layer
      const CRhinoLayer& current_layer = layer_table.CurrentLayer();
    
      // Prompt for a layer name
      CRhinoGetString gs;
      gs.SetCommandPrompt( L"Name of layer to select object" );
      gs.SetDefaultString( current_layer.LayerName() );
      gs.AcceptNothing( TRUE );
      gs.GetString();
      if( gs.CommandResult() != CRhinoCommand::success )
        return gs.CommandResult();
    
      // Validate the string
      ON_wString layer_name = gs.String();
      layer_name.TrimLeftAndRight();
      if( layer_name.IsEmpty() )
        return CRhinoCommand::cancel;
    
      // Find the layer
      int layer_index = layer_table.FindLayer( layer_name );
      if( layer_index < 0 )
      {
        RhinoApp().Print( L"\"%s\" does not exists.\n", layer_name );
        return CRhinoCommand::cancel;
      }
    
      // Get the layer
      const CRhinoLayer& layer = layer_table[layer_index];
    
      // Get all of the objects on the layer
      ON_SimpleArray<CRhinoObject*> obj_list;
      int i, obj_count = context.m_doc.LookupObject( layer, obj_list );
    
      // Select all of the layer objects
      for( i = 0; i < obj_count; i++ )
      {
        CRhinoObject* obj = obj_list[i];
        if( obj && obj->IsSelectable() )
          obj->Select();
      }
    
      if( obj_count )
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

