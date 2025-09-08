---
url: https://developer.rhino3d.com/guides/cpp/creating-sublayers/
scraped_at: 2025-09-08T15:38:52.392184
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

[Creating Sublayers](https://developer.rhino3d.com/guides/cpp/creating-
sublayers/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Creating Sublayers

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to create a “sublayer” (or a “child layer”) of a parent layer.

## Solution

All layers have a layer id field, returned by `ON_Layer::Id()`, that uniquely
identifies that layer. Layers also maintain a parent id field, returned by
`ON_Layer::ParentLayerId()`, that identifies the layer’s parent. If a layer’s
parent id is a `null` UUID, then the layer does not have a parent and, thus,
is considered a root layer.

## Sample

The following sample demonstrates how to add a parent layer then then add a
child layer to that parent.

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;
    
      // Define parent layer
      ON_Layer parent_layer;
      parent_layer.SetName(L"Parent");
    
      // Add parent layer
      int parent_layer_index = layer_table.AddLayer(parent_layer);
      if (parent_layer_index >= 0) 
      {
        // Get the layer we just added
        const CRhinoLayer& layer = layer_table[parent_layer_index];
    
        // Define child layer
        ON_Layer child_layer;
        child_layer.SetName(L"Child");
    
        // Assign parent layer's id as child's parent id
        child_layer.SetParentLayerId(layer.Id());
    
        // Add child layer
        layer_table.AddLayer(child_layer);
      }
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/creating-
sublayers/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/creating-
sublayers/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

