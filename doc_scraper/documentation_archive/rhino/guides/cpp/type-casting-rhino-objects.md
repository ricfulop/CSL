---
url: https://developer.rhino3d.com/guides/cpp/type-casting-rhino-objects/
scraped_at: 2025-09-08T15:39:23.553925
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

[Type Casting Rhino Objects](https://developer.rhino3d.com/guides/cpp/type-
casting-rhino-objects/)

  * Problem
  * Solution
  * Samples

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Type Casting Rhino Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Given a Rhino object, how can one convert it to another Rhino object? For
example, if you have a `CRhinoObject` pointer, how can I convert it to a
`CRhinoCurveObject` pointer? Or, how can one get the curve geometry?

## Solution

All Rhino C/C++ SDK classes derived from `ON_Object` provide conversions
between pointers to related classes using a static `ON_Object::Cast` function.

If you have a pointer to some base class that inherits from `ON_Object`, and
you want to convert it to a pointer of a derived class, than simply call the
derived class `Cast` function.

For example:

    
    
    const CBase* a = ...;
    const CDerived* b = CDerived::Cast( a );
    

## Samples

    
    
    CRhinoGetObject go;
    go.SetCommandPrompt( L"Select something" );
    go.GetObjects( 1, 1 );
    if( CRhinoCommand::success == go.CommandResult() )
    {
      // Get the one (and only) object reference
      CRhinoObjRef obj_ref = go.Object(0);
    
      // Get the Rhino object
      const CRhinoObject* obj = obj_ref.Object();
      if( obj )
      {
        // Try casting as a Rhino point object
        const CRhinoPointObject* point_obj = CRhinoPointObject::Cast( obj );
        if( point_obj )
        {
          // Get the point object's point geometry
          const ON_Point& point = point_obj->Point();
          // todo...
        }
    
        // Try casting as a Rhino curve object
        const CRhinoCurveObject* curve_obj = CRhinoCurveObject::Cast( obj );
        if( curve_obj )
        {
          // Get the curve object's curve geometry
          const ON_Curve* curve = curve_obj->Curve();
          // todo...
        }
    
        // Try casting as a Rhino brep object
        const CRhinoBrepObject* brep_obj = CRhinoBrepObject::Cast( obj );
        if( brep_obj )
        {
          // Get the brep object's brep geometry
          const ON_Brep* brep = brep_obj->Brep();
          // todo...
        }
    
        // Try casting as a Rhino mesh object
        const CRhinoMeshObject* mesh_obj = CRhinoMeshObject::Cast( obj );
        if( mesh_obj )
        {
          // Get the mesh object's mesh geometry
          const ON_Mesh* mesh = mesh_obj->Mesh();
          // todo...
        }
    
        // etc...
      }
    }
    

and…

    
    
    CRhinoGetObject go;
    go.SetCommandPrompt( L"Select something" );
    go.GetObjects( 1, 1 );
    if( CRhinoCommand::success == go.CommandResult() )
    {
      // Get the one (and only) object reference
      CRhinoObjRef obj_ref = go.Object(0);
    
      // Get the Rhino object's geometry
      const ON_Geometry* geo = obj_ref.Geometry();
      if( geo )
      {
        // Try casting as a point object
        const ON_Point* point = ON_Point::Cast( geo );
        if( point )
        {
          // todo...
        }
    
        // Try casting as a curve object
        const ON_Curve* curve = ON_Curve::Cast( geo );
        if( curve )
        {
          // todo...
        }
    
        // Try casting as a brep object
        const ON_Brep* brep = ON_Brep::Cast( geo );
        if( brep )
        {
          // todo...
        }
    
        // Try casting as a mesh object
        const ON_Mesh* mesh = ON_Mesh::Cast( geo );
        if( mesh )
        {
          // todo...
        }
    
        // etc...
      }
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/type-
casting-rhino-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/type-
casting-rhino-objects/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

