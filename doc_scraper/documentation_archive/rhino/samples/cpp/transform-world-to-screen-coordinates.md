---
url: https://developer.rhino3d.com/samples/cpp/transform-world-to-screen-coordinates/
scraped_at: 2025-09-08T15:48:20.759557
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

Transform World to Screen Coordinates

__

Windows only

Demonstrates how to transform world coordinates to screen coordinates.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Pick a point
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Pick point" );
      gp.GetPoint();
      if( gp.CommandResult() != CRhinoCommand::success )
        return gp.CommandResult();
    
      // Get the view the point was picked in
      CRhinoView* view = gp.View();
      if( 0 == view )
        return CRhinoCommand::failure;
    
      // Obtain the view's world-to-screen transformation
      ON_Xform world_to_screen;
      view->ActiveViewport().VP().GetXform( ON::world_cs, ON::screen_cs, world_to_screen );
    
      // Get the picked point
      ON_3dPoint picked_pt = gp.Point();
    
      // Create a 3-D point
      ON_3dPoint screen_pt = picked_pt;
      // Transform it
      screen_pt.Transform( world_to_screen );
    
      // Create a Windows 2-D point from the transformed point
      POINT pt2d;
      pt2d.x = (int)screen_pt.x;
      pt2d.y = (int)screen_pt.y;
    
      // TODO...
    
      RhinoApp().Print( L"Screen point = %d, %d\n", pt2d.x, pt2d.y );
    
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

