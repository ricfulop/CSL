---
url: https://developer.rhino3d.com/samples/cpp/add-new-layer/
scraped_at: 2025-09-08T15:47:12.031390
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

Add a New Layer

__

Windows only

Demonstrates how to add a new layer to Rhino.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Get reference to the document's layer table
      CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;
      // Cook up an unused layer name
      ON_wString unused_name;
      layer_table.GetUnusedLayerName( unused_name );
    
      // Prompt the user to enter a layer name
      CRhinoGetString gs;
      gs.SetCommandPrompt( L"Name of layer to add" );
      gs.SetDefaultString( unused_name );
      gs.AcceptNothing( TRUE );
      gs.GetString();
      if( gs.CommandResult() != CRhinoCommand::success )
        return gs.CommandResult();
    
      // Was a layer named entered?
      ON_wString layer_name = gs.String();
      layer_name.TrimLeftAndRight();
      if( layer_name.IsEmpty() )
      {
        RhinoApp().Print( L"Layer name cannot be blank.\n" );
        return CRhinoCommand::cancel;
      }
    
      // Is the layer name valid?
      if( !RhinoIsValidName(layer_name) )
      {
        RhinoApp().Print( L"\"%s\" is not a valid layer name.\n", layer_name );
        return CRhinoCommand::cancel;
      }
    
      // Does a layer with the same name already exist?
      int layer_index = layer_table.FindLayer( layer_name );
      if( layer_index >= 0 )
      {
        RhinoApp().Print( L"A layer with the name \"%s\" already exists.\n", layer_name );
        return CRhinoCommand::cancel;
      }
    
      // Create a new layer
      ON_Layer layer;
      layer.SetLayerName( layer_name );
      // Add the layer to the layer table
      layer_index = layer_table.AddLayer( layer );
      if( layer_index < 0 )
      {
        RhinoApp().Print( L"Unable to add \"%s\" layer.\n", layer_name );
        return CRhinoCommand::failure;
      }
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

