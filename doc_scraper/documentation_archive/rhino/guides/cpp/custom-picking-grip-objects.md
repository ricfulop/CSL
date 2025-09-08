---
url: https://developer.rhino3d.com/guides/cpp/custom-picking-grip-objects/
scraped_at: 2025-09-08T15:39:41.588447
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

[Custom Picking Grip Objects](https://developer.rhino3d.com/guides/cpp/custom-
picking-grip-objects/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Custom Picking Grip Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Imagine you are trying to wrote code to pick grip objects, and you want that
only grips at the boundary of a mesh to be selectable. You might have just
spent a considerable amount of time trying to get the following to work:

  1. Derive a class from `CRhinoGetObject`.
  2. Override `CRhinoGetObject::CustomGeometryFilter`.

What is missing is a pointer to a grip object inside
`CRhinoGetObject::CustomGeometryFilter`. One might think this code would work…

    
    
    CMyGetObject go;
    go.SetGeometryFilter( CRhinoGetObject::grip_object );
    

but now `CRhinoGetObject::CustomGeometryFilter` override is not even called
anymore. On the other hand, if you do not specify a
`CRhinoGetObject::SetGeometryFilter` up front, the function is called but you
don’t get any grip object from the geometry parameter of
`CRhinoGetObject::CustomGeometryFilter`.

Is there a way around this problem?

## Solution

Yes. In order to pick grip objects, using `CRhinoGetObject`, you must set the
`CRhinoGetObject::grip_object` geometry filter. If not, then Rhino will ignore
grips in an effort to improve picking performance.

Also, if you want your `CRhinoGetObject::CustomGeometryFilter` override to be
called, make sure to call `CRhinoGetObject::EnableSubObjectSelect` to disable
subobject picking. For example:

    
    
    CMyGetObject go;
    go.SetGeometryFilter( CRhinoObject::grip_object );
    go.EnableSubObjectSelect( false );
    go.GetObjects( 1, 0 );
    if( go.CommandResult() == CRhinoCommand::success )
    {
      // TODO...
    }
    

Regarding the picking of grips at the boundary of a mesh, here is a sample
class that you can use…

    
    
    class CRhGetMeshBoundaryGrip : public CRhinoGetObject
    {
    public:
      bool CustomGeometryFilter(
        const CRhinoObject* obj,
        const ON_Geometry* geo,
        ON_COMPONENT_INDEX ci
        ) const;
    };
    
    bool CRhGetMeshBoundaryGrip::CustomGeometryFilter(
      const CRhinoObject* obj,
      const ON_Geometry* geo,
      ON_COMPONENT_INDEX ci
      ) const
    {
      if( 0 == obj )
        return false;
    
      // Is grip object?
      const CRhinoGripObject* grip_obj = CRhinoGripObject::Cast( obj );
      if( 0 == grip_obj )
        return false;
    
      // Is mesh grip object?
      const CRhinoMeshObject* mesh_obj = CRhinoMeshObject::Cast( grip_obj->Owner() );
      if( 0 == mesh_obj )
        return false;
    
      // Is the grip on the border?
      const ON_Mesh* mesh = mesh_obj->Mesh();
      if( mesh && !mesh->IsClosed() )
      {
        const ON_MeshTopology& meshtop = mesh->Topology();
        int topvi = meshtop.m_topv_map[grip_obj->m_grip_index];
        const ON_MeshTopologyVertex& topv = meshtop.m_topv[topvi];
        for( int i = 0; i < topv.m_tope_count; i++ )
        {
          const ON_MeshTopologyEdge& tope = meshtop.m_tope[topv.m_topei[i]];
          if( 1 == tope.m_topf_count )
            return true;
        }
      }
    
      return false;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/custom-
picking-grip-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/custom-
picking-grip-objects/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

