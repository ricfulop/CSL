---
url: https://developer.rhino3d.com/guides/cpp/renaming-layers/
scraped_at: 2025-09-08T15:39:17.499669
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

[Renaming Layers](https://developer.rhino3d.com/guides/cpp/renaming-layers/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Renaming Layers

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Rhino layers (`CRhinoLayer`) are stored on a layer table (`CRhinoLayerTable`)
which is located on the active document. The process for modifying an existing
layer, such as changing its name, is:

  1. Get the existing layer.
  2. Make a copy of it.
  3. Modify the copy.
  4. Call `CRhinoLayerTable::ModifyLayer()`.

## Sample

The following code sample demonstrates how to rename an existing layer…

    
    
    CRhinoCommand::result CCommandTestSdk::RunCommand(const CRhinoCommandContext& context)
    {
      // Get the layer name
      CRhinoGetString gs;
      gs.SetCommandPrompt( L"Name of layer to rename" );
      gs.GetString();
      if( gs.CommandResult() != CRhinoCommand::success )
        return gs.CommandResult();
    
      // Validate the string
      ON_wString layer_name = gs.String();
      layer_name.TrimLeftAndRight();
      if( layer_name.IsEmpty() )
        return CRhinoCommand::nothing;
    
      // Get a reference to the layer table  
      CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;
    
      // Find the layer
      int layer_index = layer_table.FindLayer( layer_name );
      if( layer_index < 0 )
      {
        RhinoApp().Print( L"Layer \"%s\" does not exist.\n", layer_name );
        return CRhinoCommand::cancel;
      }
    
      // Get the new layer name  
      gs.SetCommandPrompt( L"New layer name" );
      gs.GetString();
      if( gs.CommandResult() != CRhinoCommand::success )
        return gs.CommandResult();
    
      // Validate the string
      ON_wString new_name = gs.String();
      layer_name.TrimLeftAndRight();
      if( layer_name.IsEmpty() )
        return CRhinoCommand::nothing;
    
      // Compare both names  
      if( layer_name.CompareNoCase(new_name) == 0 )
        return CRhinoCommand::nothing;
    
      // Get the layer
      const CRhinoLayer& layer = layer_table[layer_index];
    
      // Make a copy of it, and modify the name
      ON_Layer onlayer( layer );
      onlayer.SetLayerName( new_name );
    
      // Modify the exising layer with the new definition  
      CRhinoCommand::result rc = CRhinoCommand::cancel;
      if( layer_table.ModifyLayer(onlayer, layer_index) )
        rc = CRhinoCommand::success;
    
      return rc;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/renaming-
layers/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/renaming-
layers/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

