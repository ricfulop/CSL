---
url: https://developer.rhino3d.com/samples/cpp/set-cplane-to-view/
scraped_at: 2025-09-08T15:48:16.619794
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

Set a CPlane to a View

__

Windows only

Demonstrates how to set the construction plane in the active viewport parallel
to the view.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
            const CRhinoCommandContext& context )
    {
      CRhinoCommand::result rc = CRhinoCommand::cancel;
    
      // Get the active view object
      CRhinoView* view = ::RhinoApp().ActiveView();
      if( view )
      {
        // Get reference to the view's viewport object
        CRhinoViewport& vp = view->Viewport();
        // Create plane object based on viewport parameters
        ON_Plane plane( vp.Target(), vp.VP().CameraX(), vp.VP().CameraY() );
        // Copy viewport's cplane object
        ON_3dmConstructionPlane cplane = vp.ConstructionPlane();
        // Set the cplane's plane object
        cplane.m_plane = plane;
        // Push the new cplane onto the cplane stack
        view->Viewport().PushConstructionPlane( cplane );
        // Redraw the view
        view->Redraw();
        rc = CRhinoCommand::success;
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

