---
url: https://developer.rhino3d.com/guides/cpp/printing-layer-full-path/
scraped_at: 2025-09-08T15:39:16.505244
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

[Printing a Layer's Full
Path](https://developer.rhino3d.com/guides/cpp/printing-layer-full-path/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Printing a Layer's Full Path

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You could like to print a layer’s full path. That is, if a layer “MyLayer””"
is nested, I would like to print out the nesting like this:

`"GreatGrandParent / GrandParent / Parent / MyLayer"`

## Solution

The following sample function ought to do the trick:

    
    
    static ON_wString RhinoFullLayerPath( CRhinoDoc& doc, const CRhinoLayer& layer )
    {
      ON_wString layer_path;
    
      CRhinoLayerNode layer_node;
      layer_node.Create(layer.m_layer_index, 2, 0, true );
      if( layer_node.m_parent_count > 0 )
      {
        int i, layer_index = -1;
        for( i = layer_node.m_parent_count - 1; i >= 0; i-- )
        {
          layer_index = layer_node.m_parent_list[i];
          layer_path += doc.m_layer_table[layer_index].LayerName();
          layer_path += L" / ";
        }
      }
      layer_path += layer.LayerName();
    
      return layer_path;
    }
    

You can use the function like this…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      ON_wString s = RhinoFullLayerPath( context.m_doc, context.m_doc.m_layer_table.CurrentLayer() );
      RhinoApp().Print( L"%s\n", s.Array() );
      return CRhinoCommand::success;
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/printing-
layer-full-path/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/printing-
layer-full-path/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

