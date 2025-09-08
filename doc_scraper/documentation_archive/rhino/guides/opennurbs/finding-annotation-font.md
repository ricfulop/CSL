---
url: https://developer.rhino3d.com/guides/opennurbs/finding-annotation-font/
scraped_at: 2025-09-08T15:38:21.274616
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

[Finding an Annotation object's
font](https://developer.rhino3d.com/guides/opennurbs/finding-annotation-font/)

  * Question
  * Answer
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Finding an Annotation object's font

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Question

There are many changes to `ONX_Model` in openNURBS. In prior versions, I was
getting the font and its id information for `ON_Leader2` with:

    
    
    ONX_Model model = ...
    const ON_Leader2* leader = ...
    const ON_Font& font = model.m_font_table[leader->Index()];
    

How can I do this with the current openNURBS?

## Answer

In openNURBS, the the dimension style, or `ON_DimStyle`, specifies all
appearance properties like the text font, size, and alignment, arrow head
shape, and so on. To obtain the font used by an Annotation object, such as an
`ON_Leader`, you just need to query the object’s effective dimension style.

## Example

The following example code can be used to get the `ON_Font` used by an
`ON_Leader` using the openNURBS toolkit:

    
    
    ONX_Model model = ...
    
    // Create a model geometry interator
    ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
    const ON_ModelComponent* model_component = nullptr;
    for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
    {
      // Get the model geometry
      const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
      if (nullptr == model_geometry)
        continue;
    
      // Try getting an annotation leader
      const ON_Leader* leader = ON_Leader::Cast(model_geometry->Geometry(nullptr));
      if (nullptr == leader)
        continue;
    
      // Get the parent dimension style
      const ON_ModelComponentReference& parent_dim_style_ref = model.DimensionStyleFromId(leader->DimensionStyleId());
      const ON_DimStyle* parent_dim_style = ON_DimStyle::Cast(parent_dim_style_ref.ModelComponent());
      if (nullptr == parent_dim_style)
        continue;
        
      // Get the effective dimension style
      const ON_DimStyle& dim_style = leader->DimensionStyle(*parent_dim_style);
    
      // Get the font
      const ON_Font& font = dim_style.Font();
    
      // TODO...
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/finding-
annotation-font/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/finding-
annotation-font/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

