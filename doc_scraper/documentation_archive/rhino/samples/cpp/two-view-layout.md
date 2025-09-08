---
url: https://developer.rhino3d.com/samples/cpp/two-view-layout/
scraped_at: 2025-09-08T15:48:21.747394
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

Two View Layout

__

Windows only

Demonstrates how to create a two-view viewport layout.

C/C++

    
    
    CRhinoCommand::result CCommand2View::RunCommand( const CRhinoCommandContext& context )
    {
      ON_3dmView views[2];
      double def_size = 15.0;
      ON_BoundingBox bbox;
      bbox.m_min.Set( -def_size, -def_size, -def_size );
      bbox.m_max.Set(  def_size, def_size, def_size );
      ON_3dPoint target = ON_origin;
      const CRhinoAppViewSettings& view_settings = RhinoApp().AppSettings().ViewSettings();
    
      // top view
      {
        views[0].m_name = L"Top";
        views[0].m_target = target;
        ON_3dVector dir( 0.0, 0.0, -100.0 );
        views[0].m_vp.SetCameraLocation( views[0].m_target - dir );
        views[0].m_vp.SetCameraDirection( dir );
        views[0].m_vp.SetCameraUp( ON_yaxis );
        views[0].m_vp.SetProjection( ON::parallel_view );
        views[0].m_vp.SetScreenPort( 0, 100, 100, 0, 0, 1 );
        views[0].m_vp.Extents( atan(12.0 / view_settings.m_camera_lense_length), bbox );
        views[0].m_cplane.m_plane = ON_xy_plane;
        views[0].m_position.m_wnd_left = 0.0;
        views[0].m_position.m_wnd_right = 0.5;
        views[0].m_position.m_wnd_top = 0.0;
        views[0].m_position.m_wnd_bottom = 1.0;
      }
    
      // perspective view
      {
        views[1].m_name = L"Perspective";
        views[1].m_target = target;
        ON_3dVector dir( -43.30, 75.00, -50.00 );
        views[1].m_vp.SetCameraLocation( views[1].m_target - dir );
        views[1].m_vp.SetCameraDirection( dir );
        views[1].m_vp.SetCameraUp( ON_zaxis );
        views[1].m_vp.SetProjection( ON::perspective_view );
        views[1].m_vp.SetScreenPort( 0, 100, 100, 0, 0, 1 );
        views[1].m_vp.Extents( atan(12.0 / view_settings.m_camera_lense_length), bbox );
        views[0].m_cplane.m_plane = ON_xy_plane;
        views[1].m_position.m_wnd_left = 0.5;
        views[1].m_position.m_wnd_right = 1.0;
        views[1].m_position.m_wnd_top = 0.0;
        views[1].m_position.m_wnd_bottom = 1.0;
      }
    
      context.m_doc.ReplaceModelViews( 2, views );
      context.m_doc.Redraw();
    
      return CRhinoCommand::success;
    }
    

  

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

