---
url: https://developer.rhino3d.com/samples/cpp/add-spherical-surface/
scraped_at: 2025-09-08T15:47:19.061764
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

Add Spherical Surface

__

Windows only

Demonstrates how to create a sphere using ON_RevSurface and add it to Rhino.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoCommand::result rc = CRhinoCommand::cancel;
    
      ON_3dPoint center( 0.0, 0.0, 0.0 );
      double radius = 5.0;
      ON_Sphere sphere( center, radius );
      ON_RevSurface* sphere_srf = sphere.RevSurfaceForm();
      if( !sphere_srf )
        return rc;
    
      CRhinoSurfaceObject* sphere_obj = new CRhinoSurfaceObject();
      sphere_obj->SetSurface( sphere_srf );
    
      if( context.m_doc.AddObject(sphere_obj) )
      {
        context.m_doc.Redraw();
        rc = CRhinoCommand::success;
      }
      else
      {
        delete sphere_obj;
        sphere_obj = NULL;
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

