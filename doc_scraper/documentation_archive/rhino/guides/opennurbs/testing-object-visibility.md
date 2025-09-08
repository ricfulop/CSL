---
url: https://developer.rhino3d.com/guides/opennurbs/testing-object-visibility/
scraped_at: 2025-09-08T15:38:24.292539
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

[Testing for Object
Visibility](https://developer.rhino3d.com/guides/opennurbs/testing-object-
visibility/)

  * Question
  * Answer
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Testing for Object Visibility

by [Dale Lear](https://discourse.mcneel.com/u/dalelear/) (Last updated:
Wednesday, December 5, 2018)

## Question

I have created a sample model this has a parent layer and a sublayer. If I add
objects to each of these two layer and then turn off the parent layer in
Rhino, the objects on both layers do not appear. But, when I read the .3dm
file using openNURBS, the objects on the sublayer report as being visible. How
can I correctly detect the visibility of an object?

## Answer

A Rhino object is considered visible if:

  1. The object’s mode is not set to hidden.
  2. If the object’s layer is not hidden.
  3. If the object’s layer does not have a parent layer that is hidden.

## Example

The following example code can be used to detect an object’s true visibility
when using the openNURBS toolkit:

    
    
    static bool IsLayerVisible(const ONX_Model& model, ON_UUID layer_id)
    {
      bool rc = false;
      const ON_ModelComponentReference& model_component_ref = model.ComponentFromId(ON_ModelComponent::Type::Layer, layer_id);
      if (!model_component_ref.IsEmpty())
      {
        const ON_Layer* layer = ON_Layer::Cast(model_component_ref.ModelComponent());
        if (nullptr != layer)
        {
          rc = layer->IsVisible();
          if (rc && layer->ParentIdIsNotNil())
            return IsLayerVisible(model, layer->ParentId());
        }
      }
      return rc;
    }
    
    static bool IsLayerVisible(const ONX_Model& model, int layer_index)
    {
      bool rc = false;
      const ON_ModelComponentReference& model_component_ref = model.ComponentFromIndex(ON_ModelComponent::Type::Layer, layer_index);
      if (!model_component_ref.IsEmpty())
      {
        const ON_Layer* layer = ON_Layer::Cast(model_component_ref.ModelComponent());
        if (nullptr != layer)
        {
          rc = layer->IsVisible();
          if (rc && layer->ParentIdIsNotNil())
            return IsLayerVisible(model, layer->ParentId());
        }
      }
      return rc;
    }
    
    static bool IsModelGeometryVisible(const ONX_Model& model, const ON_ModelGeometryComponent* model_geometry)
    {
      bool rc = false;
      if (nullptr != model_geometry)
      {
        const ON_3dmObjectAttributes* attributes = model_geometry->Attributes(nullptr);
        if (nullptr != attributes)
        {
          switch (attributes->Mode())
          {
          case ON::normal_object:
          case ON::idef_object:
          case ON::locked_object:
            rc = IsLayerVisible(model, attributes->m_layer_index);
            break;
          }
        }
      }
      return rc;
    }
    

You can test the above static functions by adding the following sample code to
the _Example_Read_ project included with the openNURBS toolkit:

    
    
    ONX_Model model = ...;
    
    ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
    const ON_ModelComponent* model_component = nullptr;
    for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
    {
      const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
      if (nullptr != model_geometry)
      {
        bool bVisible = IsModelGeometryVisible(model, model_geometry);
        if (bVisible)
        {
          // TODO...
        }
      }
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/testing-
object-visibility/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/testing-
object-visibility/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

