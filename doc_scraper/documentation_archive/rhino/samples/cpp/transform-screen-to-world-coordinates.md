---
url: https://developer.rhino3d.com/samples/cpp/transform-screen-to-world-coordinates/
scraped_at: 2025-09-08T15:48:19.766752
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

Transform Screen to World Coordinates

__

Windows only

Demonstrates how to transform screen coordinates to world coordinates.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoCommand::result rc = failure;
    
      // Get the active view
      CRhinoView* view = RhinoApp().ActiveView();
      if( view )
      {
        // Get the current cursor position
        POINT point;
        if( GetCursorPos(&point ) )
        {
          // Convert the screen coordinates to client coordinates
          view->ScreenToClient( &point );
    
          // Obtain the view's screen-to-world transformation
          ON_Xform screen_to_world;
          view->ActiveViewport().VP().GetXform( ON::screen_cs, ON::world_cs, screen_to_world );
    
          // Create a 3-D point
          ON_3dPoint pt( point.x, point.y, 0 );
          // Transform it
          pt.Transform( screen_to_world );
    
          // Add it to the document
          context.m_doc.AddPointObject( pt );
          context.m_doc.Redraw();
    
          rc = success;
        }
      }
    
      return rc;
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

