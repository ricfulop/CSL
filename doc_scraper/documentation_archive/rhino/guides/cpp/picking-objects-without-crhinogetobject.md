---
url: https://developer.rhino3d.com/guides/cpp/picking-objects-without-crhinogetobject/
scraped_at: 2025-09-08T15:40:04.685288
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

[Picking Objects without
CRhinoGetObject](https://developer.rhino3d.com/guides/cpp/picking-objects-
without-crhinogetobject/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Picking Objects without CRhinoGetObject

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Imagine you have a 3D point, now you want to pick all the objects that are
underneath it.

## Solution

You can use `CRhinoPickContext` to build your own object picker. For more
details on `CRhinoPickContext`, see _rhinoSdkPick.h_. With the
`CRhinoPickContext` class, you can define the rules for picking. For example,
you can specify a picking style (point, window, crossing). You can also
specify a filter so you only pick the types of objects you want. The most
important part is to define a pick chord, which starts on near clipping plane
and ends on far clipping plane.

After you have created the `CRhinoPickContext` object and filled out its
parameters, call `CRhinoDoc::PickObjects`. This function goes through the list
of eligible objects and intersects them with the pick frustum. If they hit the
frustum in an acceptable manner, the object is added to a pick list passed in
by the caller.

Here is a simple example of a function that might work for you:

    
    
    static int MyObjectPicker( CRhinoDoc& doc, CRhinoView* view, POINT point, CRhinoObjRefArray& pick_list )
    {
      if( 0 == view )
        return 0;
    
      CRhinoPickContext pick_context;
      pick_context.m_view = view;
      pick_context.m_pick_style = CRhinoPickContext::point_pick;
    
      CRhinoViewport& active_vp = view->ActiveViewport();
      switch( active_vp.DisplayMode() )
      {
        case ON::shaded_display:
        case ON::renderpreview_display:
          pick_context.m_pick_mode = CRhinoPickContext::shaded_pick;
          break;
      }
    
      int pick_count = 0;
      if( active_vp.GetPickXform(point.x, point.y, pick_context.m_pick_region.m_xform) )
      {
        // adds objects to pick_list - does not change any status
        active_vp.VP().GetFrustumLine( point.x, point.y, pick_context.m_pick_line );
        pick_context.UpdateClippingPlanes();
        pick_count = doc.PickObjects( pick_context, pick_list );
      }
    
      return pick_count;
    }
    

And, here is a sample of its use:

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetPoint gp;
      gp.GetPoint();
      if( gp.CommandResult() != CRhinoCommand::success )
        return gp.CommandResult();
    
      CRhinoView* view = gp.View();
      if( 0 == view )
        return failure;
    
      ON_Xform w2s;
      view->ActiveViewport().VP().GetXform( ON::world_cs, ON::screen_cs, w2s );
    
      ON_3dPoint pt3d = gp.Point();
      pt3d.Transform( w2s );
    
      POINT pt2d;
      pt2d.x = (int)pt3d.x;
      pt2d.y = (int)pt3d.y;
    
      CRhinoObjRefArray pick_list;
      int pick_count = MyObjectPicker( context.m_doc, view, pt2d, pick_list );
      for( int i = 0; i < pick_count; i++ )
      {
        const CRhinoObject* obj = pick_list[i].Object();
        if( obj )
          obj->Select( true, true, true );
      }
      context.m_doc.Redraw();
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/picking-
objects-without-crhinogetobject/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/picking-
objects-without-crhinogetobject/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

