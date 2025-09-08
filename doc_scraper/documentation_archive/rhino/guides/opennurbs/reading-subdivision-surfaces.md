---
url: https://developer.rhino3d.com/guides/opennurbs/reading-subdivision-surfaces/
scraped_at: 2025-09-08T15:38:15.239892
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

[Reading Subdivision
Surfaces](https://developer.rhino3d.com/guides/opennurbs/reading-subdivision-
surfaces/)

  * Overview
  * openNURBS and ON_SubD
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Reading Subdivision Surfaces

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Thursday, June 24, 2021)

## Overview

Rhino SubD objects are high-precision Catmull-Clark subdivision surfaces. They
can have creases, sharp or smooth corners, and holes. The Rhino SubD object is
designed to quickly model and edit complex organic shapes.

Unlike traditional mesh-based SubD implementations, Rhino SubD objects are NOT
a subdivided mesh object.

The Rhino SubD user experience will be the same as Rhino NURBS and mesh object
experience. There will also be new SubD modeling and editing tools based on
traditional techniques.

Rhino SubD surfaces are predictable, measurable, and manufacturable. They can
be converted to either high-quality NURBS or mesh (quads or triangles) objects
when needed.

Rhino SubD objects will be supported in all Rhino export formats that support
either meshes or NURBS including IGES, STEP, OBJ, and STL.

## openNURBS and ON_SubD

Rhino SubD object are defined on openNURBS in the `ON_SubD` class. See
`opennurbs_subd.h`, in the openNURBS source code, for details.

Like other Rhino objects, the `ON_SubD` class inherits from `ON_Geometry`.
Thus when you are reading 3DM files, you can use `ONX_ModelComponentIterator`
object to look for SubD object just like you would if you were looking for
other types of geometry, such as curves, Breps, and meshes.

The following code sample demonstrates how to iterate an `ONX_Model` object
and look for `ON_SubD` objects. When found, the control net mesh (or input
mesh used to calculate a subdivision surface) is obtained.

    
    
    ONX_Model model = ...
    
    ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
    const ON_ModelComponent* model_component = nullptr;
    for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
    {
      const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
      if (nullptr != model_geometry)
      {
        // Test for subd object
        const ON_SubD* subd = ON_SubD::Cast(model_geometry->Geometry(nullptr));
        if (nullptr != subd)
        {
          // Get control net mesh
          ON_Mesh* mesh = subd->GetControlNetMesh(nullptr, ON_SubDGetControlNetMeshPriority::Geometry);
          if (nullptr != mesh)
          {
            // TODO: do something with mesh
            delete mesh; // don't leak memory
          }
        }
      }
    }
    

The control net is mesh generally coarse and not acceptable for use for
rendering, rapid prototyping, and other. So the version of openNURBS, included
with Rhino, contains two powerful functions that are useful for converting
SubD objects to Breps or smooth meshes:

    
    
    // Gets a ON_Brep representation the subdivision limit surface
    ON_SubD::GetSurfaceBrep()
    
    // Get a ON_Mesh representation of the subdivision limit surface
    ON_SubD::GetSurfaceMesh()
    

These two function are used internally by Rhino when exporting to file formats
that do not support SubD objects. However, these two functions **are not
available** in the free, publicly available openNURBS toolkit.

Rhino SubD objects are 100% “industry standard” and Rhino evaluation results
comply 100% with public domain algorithms widely described in published
technical literature. Please see the [Rhino SubD
Rules](https://docs.google.com/document/d/13QkEGz9SedvauQQegiZ2HXSKOiwn0INVO4FxGlfvRps)
document for complete details about the subdivision algorithm. If you already
have actually have code that correctly meshes and performs the “to NURBS”
conversion on Catmull-Clark subdivision surfaces, then you should use it.

If you don’t have this capability, then you might try subdividing the SubD
object before acquiring the control net mesh. Here is an example:

    
    
    const ON_SubD* subd = ON_SubD::Cast(model_geometry->Geometry(nullptr));
    if (nullptr != subd)
    {
      ON_SubD* new_subd = subd->Duplicate();
      if (nullptr != new_subd)
      {
        // The number of subdivisions you require
        const int count = 3;
        
        // Apply the Catmull-Clark subdivision algorithm and save the results in this ON_SubD
        new_subd->GlobalSubdivide(count);
        
        // Get control net mesh
        ON_Mesh* mesh = new_subd->GetControlNetMesh(nullptr, ON_SubDGetControlNetMeshPriority::Geometry);
        if (nullptr != mesh)
        {
          // TODO: do something with mesh
          delete mesh; // don't leak memory
        }
        delete new_subd; // don't leak memory
      }
    }
    

## Related Topics

  * [What is openNURBS?](https://developer.rhino3d.com/guides/opennurbs/what-is-opennurbs/)
  * [Rhino SubD Rules](https://docs.google.com/document/d/13QkEGz9SedvauQQegiZ2HXSKOiwn0INVO4FxGlfvRps)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/reading-
subdivision-surfaces/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/reading-
subdivision-surfaces/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

