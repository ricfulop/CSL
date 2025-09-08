---
url: https://developer.rhino3d.com/guides/opennurbs/importing-lightweight-extrusions/
scraped_at: 2025-09-08T15:38:12.219946
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

[Importing Lightweight
Extrusions](https://developer.rhino3d.com/guides/opennurbs/importing-
lightweight-extrusions/)

  * Question
  * Answer

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Importing Lightweight Extrusions

by [Dale Lear](https://discourse.mcneel.com/u/dalelear/) (Last updated:
Wednesday, December 5, 2018)

## Question

I was try to add some code for handling the `ON::extrusion_object` type
object. But, I don’t now know which API I could use to get data from extrusion
object. I know there was a new class `ON_Extrusion` in _opennurbs_beam.cpp_.
But I did not know how to use it. Can you give me some suggestion or some
sample code? I would like know how should I import extrusion object?

## Answer

In most cases, you will want to convert the extrusion object to a Brep and
then just pass the Brep to the Brep handling code that you’ve already written,
for example:

    
    
    ONX_Model model = ...
    
    ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
    const ON_ModelComponent* model_component = nullptr;
    for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
    {
      const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
      if (nullptr != model_geometry)
      {
        // Test for extrusion object
        const ON_Extrusion* extrusion = ON_Extrusion::Cast(model_geometry->Geometry(nullptr));
        if (nullptr != extrusion)
        {
          ON_Brep* brep = ON_Brep::New();
          if (brep != extrusion->BrepForm(brep, true))
          {
            delete brep; // don't leak...
            continue;
          }
    
          // TODO: do something with Brep here...
    
          delete brep; // don't leak...
        }
      }
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/importing-
lightweight-extrusions/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/importing-
lightweight-extrusions/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

