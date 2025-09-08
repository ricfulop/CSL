---
url: https://developer.rhino3d.com/samples/cpp/pick-angle-interactively/
scraped_at: 2025-09-08T15:48:03.686173
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

Pick Angle Interactively

__

Windows only

Demonstrates how to use the CRhinoGetAngle class to pick an angle.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      // Prompt for base point
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Base point" );
      gp.ConstrainToConstructionPlane( FALSE );
      gp.GetPoint();
      if( gp.CommandResult() != CRhinoCommand::success )
        return gp.CommandResult();
    
      // Get first picked point
      ON_3dPoint origin = gp.Point();
    
      // Get view used during GetPoint
      CRhinoView* view = gp.View();
      if( !view )
      {
        // If scripted, get active view
        view = ::RhinoApp().ActiveView();
        if( !view )
          return CRhinoCommand::failure;
      }
    
      // Get view's construction plane and move it to the picked point
      ON_Plane plane = view->Viewport().ConstructionPlane().m_plane;
      plane.SetOrigin( origin );
    
      // Prompt for first reference point
      gp.SetCommandPrompt( L"First reference point" );
      gp.SetBasePoint( origin );
      gp.DrawLineFromPoint( origin, TRUE );
      gp.Constrain( plane );  // Constrain picking to plane
      gp.GetPoint();
      if( gp.CommandResult() != CRhinoCommand::success )
        return gp.CommandResult();
    
      // Get second picked point
      ON_3dPoint refpt = gp.Point();
    
      // Prompt for angle
      CRhinoGetAngle ga;
      ga.SetCommandPrompt( L"Second reference point" );
      ga.SetBasePoint( origin );
      ga.SetBase( origin );
      ga.SetReferencePoint( refpt );
      ga.Constrain( plane );  // Constrain picking to plane
      ga.GetAngle();
      if( ga.CommandResult() != CRhinoCommand::success )
        return ga.CommandResult();
    
      // Results
      double radians = ga.Angle();
      double degrees = radians * (180.0/ON_PI);
      RhinoApp().Print( L"Angle = %f.\n", degrees );
    
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

