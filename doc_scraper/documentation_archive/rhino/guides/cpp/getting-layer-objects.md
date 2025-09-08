---
url: https://developer.rhino3d.com/guides/cpp/getting-layer-objects/
scraped_at: 2025-09-08T15:39:00.450710
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

[Getting Layer Objects](https://developer.rhino3d.com/guides/cpp/getting-
layer-objects/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Getting Layer Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Friday,
August 28, 2020)

## Problem

You would like to get all the objects on a specific layer.

## Solution

You can get all of the objects on a specified layer in two ways:

  1. Use `CRhinoDoc::LookupObject`.
  2. Use a `CRhinoObjectIterator`.

The `CRhinoDoc::LookupObject` is somewhat easier. So, we will demonstrate this
in the following sample…

## Sample

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      const wchar_t* psz_layer_name = L"Default"; ;
      int layer_index = context.m_doc.m_layer_table.FindLayerFromFullPathName(psz_layer_name, ON_UNSET_INT_INDEX);
      if (layer_index >= 0 && layer_index < context.m_doc.m_layer_table.LayerCount())
      {
        const CRhinoLayer& layer = context.m_doc.m_layer_table[layer_index];
        ON_SimpleArray<CRhinoObject*> objects;
        int object_count = context.m_doc.LookupObject(layer, objects);
        if (object_count > 0)
        {
          RhinoApp().Print(L"%s layer object(s)s:\n", psz_layer_name);
          for (int i = 0; i < object_count; i++)
          {
            const CRhinoObject* object = objects[i];
            if (object)
              RhinoApp().Print(L"  %s\n", object->ShortDescription(false));
          }
        }
      }
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/getting-
layer-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/getting-
layer-objects/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

