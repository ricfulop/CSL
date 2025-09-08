---
url: https://developer.rhino3d.com/guides/cpp/shading-individual-objects/
scraped_at: 2025-09-08T15:40:12.723324
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

[Shading Individual Objects](https://developer.rhino3d.com/guides/cpp/shading-
individual-objects/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Shading Individual Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The drawing display pipeline technology provides both users and developers
great flexibility and control over how objects are drawn on the screen. One of
the features available is the ability to have objects draw using different
display modes in the same viewport. For example, it is possible for a viewport
to display both wireframe and shaded objects at the same time.

To allow an object to draw in a display mode other than what the viewport is
currently set to, all you need to do is to add an `ON_DisplayMaterialRef`
object to an object’s attributes. A `ON_DisplayMaterialRef` defines what
viewport an object will draw using a different display attributes and what
display attributes it will use.

## Sample

The following sample code demonstrates how to shade individual objects using
the Rhino C/C++ SDK. This shading is independent of the viewport’s current
display mode, or display attribute. Is is accomplished by adding a
`ON_DisplayMaterialRef` object to an object’s attributes.

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Get a list of available display attributes
      DisplayAttrsMgrList attrs_list;
      const int attrs_count = CRhinoDisplayAttrsMgr::GetDisplayAttrsList( attrs_list );
      if( attrs_count <= 0 )
        return CRhinoCommand::nothing;
    
      ON_wString display_name( L"Shaded" );
      ON_UUID display_material_id = ON_nil_uuid;
    
      // Find the "Shaded" display attribute
      int i;
      for( i = 0; i < attrs_count; i++ )
      {
        CDisplayPipelineAttributes* pAttrs = attrs_list[i].m_pAttrs;
        if( !pAttrs )
          continue;
    
        ON_wString english_name = pAttrs->EnglishName();
        english_name.Remove( '_' );
        english_name.Remove( ' ' );
        english_name.Remove( '-' );
        english_name.Remove( ',' );
        english_name.Remove( '.' );
    
        if( english_name.CompareNoCase(display_name) == 0 )
        {
          display_material_id = pAttrs->Id();
          break;
        }
      }
    
      // Bail if not found
      if( display_material_id == ON_nil_uuid )
      {
        RhinoApp().Print( L" \"%s\" display mode not found.\n", display_name );
        return CRhinoCommand::nothing;
      }
    
      // Select the objects to shade
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select surfaces, polysurfaces, and meshes to shade" );
      go.SetGeometryFilter( ON::surface_object | ON::brep_object | ON::mesh_object );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      // Get the viewport to shade the objects in
      CRhinoView* view = RhinoApp().ActiveView();
      if( !view )
        return failure;
    
      // Create a display material reference and assign
      // the display attributes id and the viewport id
      // to it.
      ON_DisplayMaterialRef dmr;
      dmr.m_display_material_id = display_material_id;
      dmr.m_viewport_id = view->Viewport().VP().ViewportId();
    
      // Process each selected object
      const int object_count = go.ObjectCount();
      for( i = 0; i < object_count; i++ )
      {
        const CRhinoObjRef& ref = go.Object(i);
        const CRhinoObject* obj = ref.Object();
        if( !obj )
          continue;
    
        // Make a copy of the object's attributes
        ON_3dmObjectAttributes attributes = obj->Attributes();
        // Add a display material reference
        attributes.AddDisplayMaterialRef( dmr );
        // Modify the object's attributes
        context.m_doc.ModifyObjectAttributes( ref, attributes );
      }
    
      context.m_doc.Redraw();
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/shading-
individual-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/shading-
individual-objects/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

