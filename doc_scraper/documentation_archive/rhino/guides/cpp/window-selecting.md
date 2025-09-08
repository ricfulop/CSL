---
url: https://developer.rhino3d.com/guides/cpp/window-selecting/
scraped_at: 2025-09-08T15:39:26.523487
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

[Window Selecting](https://developer.rhino3d.com/guides/cpp/window-selecting/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Window Selecting

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The `CRhinoGetObject` class is used for selecting Rhino objects. When active,
`CRhinoGetObject` object will allow the user to select objects either by
picking them or by dragging a crossing window. But, using C/C++, it is
possible to write your own object picking class or function. The heart of such
a tool is the `CRhinoPickContext` which defines the rules for the picking.
Once the rules have been defined, you can use `CRhinoDoc::PickObjects` to do
the work.

## Sample

The following sample code demonstrates how to drag a window to select objects.

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Drag a window to select objects" );
      gp.SetGetPointCursor( RhinoApp().m_default_cursor );
      gp.ConstrainToTargetPlane();
      CRhinoGet::result res = gp.Get2dRectangle( 0, 0, FALSE, PS_DOT );
      if( res != CRhinoGet::rect2d )
        return failure;
    
      CRect pick_rect = gp.Rectangle2d();
      CRhinoView* view = gp.View();
    
      CRhinoPickContext pick_context;
      pick_context.m_go = 0;
      pick_context.m_view = view;
      pick_context.m_pick_style = CRhinoPickContext::window_pick;
      pick_context.m_bPickGroups = true;
      switch( view->Viewport().DisplayMode() )
      {
        case ON::shaded_display:
        case ON::renderpreview_display:
          pick_context.m_pick_mode = CRhinoPickContext::shaded_pick;
          break;
      }
    
      CRhinoObjRefArray pick_list;
      int pick_count = 0;
      if( view->Viewport().GetPickXform(pick_rect, pick_context.m_pick_region.m_xform) )
      {
        pick_context.UpdateClippingPlanes();
        POINT screen_point = pick_rect.BottomRight();
        view->ActiveViewport().VP().GetFrustumLine( screen_point.x, screen_point.y, pick_context.m_pick_line );
        int i, pick_count = context.m_doc.PickObjects( pick_context, pick_list );
        for( i = 0; i < pick_count; i++ )
        {
          const CRhinoObject* obj = pick_list[i].Object();
          if( obj && obj->IsSelectable() )
            obj->Select( true );
        }
        if( pick_count )
          context.m_doc.Redraw();
      }
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/window-
selecting/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/window-
selecting/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

