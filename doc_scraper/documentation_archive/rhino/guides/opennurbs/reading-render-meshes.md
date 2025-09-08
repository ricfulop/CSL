---
url: https://developer.rhino3d.com/guides/opennurbs/reading-render-meshes/
scraped_at: 2025-09-08T15:38:14.237687
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

[Reading Render
Meshes](https://developer.rhino3d.com/guides/opennurbs/reading-render-meshes/)

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Reading Render Meshes

by [Dale Lear](https://discourse.mcneel.com/u/dalelear/) (Last updated:
Wednesday, December 5, 2018)

If you are developing software to read .3dm files, you might find that the
software only _seems_ to read NURBS data; but render meshes are ignored. We do
provide methods for third-party developers to read render meshes from .3dm
files.

An object’s render meshes are stored on that object. For example, the render
meshes for `ON_Brep` and `ON_Extrusion` objects are stored on that object. The
developer can obtain an object’s render meshes from a Brep by calling
`ON_Brep::GetMesh` and from an Extrusion by calling `ON_MeshCache::Mesh`.

If you are referencing the `Example_read` sample included with the openNURBS
toolkit, then after the 3DM file has been read, you can obtain the render
meshes from the `ONX_Model` object as follows:

    
    
    ONX_Model model = ...
    
    ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
    const ON_ModelComponent* model_component = nullptr;
    for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
    {
      const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
      if (nullptr != model_geometry)
      {
        // Test for mesh object
        const ON_Mesh* mesh = ON_Mesh::Cast(model_geometry->Geometry(nullptr));
        if (nullptr != mesh)
        {
          // TODO: do something with ON_Mesh object...
          continue;
        }
    
        // Test for Brep object
        const ON_Brep* brep = ON_Brep::Cast(model_geometry->Geometry(nullptr));
        if (nullptr != brep)
        {
          ON_SimpleArray<const ON_Mesh*> meshes(brep->m_F.Count());
          const int mesh_count = brep->GetMesh(ON::render_mesh, meshes);
          if (mesh_count > 0)
          {
            // TODO: do something with array of ON_Mesh objects...
          }
          continue;
        }
    
        // Test for extrusion object
        const ON_Extrusion* extrusion = ON_Extrusion::Cast(model_geometry->Geometry(nullptr));
        if (nullptr != extrusion)
        {
          const ON_Mesh* mesh = extrusion->m_mesh_cache.Mesh(ON::render_mesh);
          if (nullptr != mesh)
          {
            // TODO: do something with ON_Mesh object...
          }
          continue;
        }
      }
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/reading-
render-meshes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/reading-
render-meshes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

