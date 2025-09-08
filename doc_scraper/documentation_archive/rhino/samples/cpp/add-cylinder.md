---
url: https://developer.rhino3d.com/samples/cpp/add-cylinder/
scraped_at: 2025-09-08T15:47:09.059655
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

Add a Cylinder

__

Windows only

Demonstrates how to create a cylinder using ON_BrepCylinder and add it to
Rhino.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      ON_3dPoint center_point( 0.0, 0.0, 0.0 );
      double radius = 5.0;
      ON_3dPoint height_point( 0.0, 0.0, 10.0 );
      ON_3dVector zaxis = height_point - center_point;
      ON_Plane plane( center_point, zaxis );
      ON_Circle circle( plane, radius );
      ON_Cylinder cylinder( circle, zaxis.Length() );
      ON_Brep* brep = ON_BrepCylinder( cylinder, TRUE, TRUE );
      if( brep )
      {
        CRhinoBrepObject* cylinder_object = new CRhinoBrepObject();
        cylinder_object->SetBrep( brep );
        if( context.m_doc.AddObject(cylinder_object) )
          context.m_doc.Redraw();
        else
          delete cylinder_object;
      }
    
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

