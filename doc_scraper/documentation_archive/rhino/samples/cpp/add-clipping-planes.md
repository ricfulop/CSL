---
url: https://developer.rhino3d.com/samples/cpp/add-clipping-planes/
scraped_at: 2025-09-08T15:47:16.046412
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

Add Clipping Planes

__

Windows only

Demonstrates how to add a viewport clipping plane object.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Define the corners of the clipping plane
      CArgsRhinoGetPlane args;
      ON_3dPoint corners[4];
      CRhinoHistory history( *this );
      CRhinoCommand::result rc = RhinoGetRectangle( args, corners, &history );
      if( rc != CRhinoCommand::success )
        return rc;
    
      // Get the active view
      CRhinoView* view = RhinoApp().ActiveView();
      if( 0 == view  )
        return CRhinoCommand::failure;
    
      const ON_3dPoint& p0 = corners[0];
      const ON_3dPoint& p1 = corners[1];
      const ON_3dPoint& p2 = corners[2];
      const ON_3dPoint& p3 = corners[3];
    
      ON_Interval domain0, domain1;
      domain0.Set( 0.0, p0.DistanceTo(p1) );
      domain1.Set( 0.0, p0.DistanceTo(p3) );
    
      // Create a plane from the corner points
      ON_Plane plane( p0, p1, p3);
    
      // Create a plane surface
      ON_PlaneSurface plane_srf( plane );
      plane_srf.SetExtents( 0, domain0, true );
      plane_srf.SetExtents( 1, domain1, true );
      plane_srf.SetDomain( 0, domain0.Min(), domain0.Max() );
      plane_srf.SetDomain( 1, domain1.Min(), domain1.Max() );
    
      // Create a clipping plane object
      rc = CRhinoCommand::failure;
      CRhinoClippingPlaneObject* plane_obj = new CRhinoClippingPlaneObject();
      if( plane_obj )
      {
        plane_obj->SetPlaneSurface( plane_srf );
    
        // Add the clipping plane
        if( plane_obj->AddClipViewport(view->ActiveViewport().ViewportId()) )
        {
          context.m_doc.AddObject( plane_obj );
          context.m_doc.Regen();
          rc = CRhinoCommand::success;
        }
        else
        {
          delete plane_obj;
          plane_obj = 0;
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

