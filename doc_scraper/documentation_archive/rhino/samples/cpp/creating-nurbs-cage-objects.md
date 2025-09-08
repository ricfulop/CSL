---
url: https://developer.rhino3d.com/samples/cpp/creating-nurbs-cage-objects/
scraped_at: 2025-09-08T15:47:29.099153
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

Creating NURBS Cage Objects

__

Windows only

Demonstrates how to create a NURBS Cage objects.

C/C++

    
    
    CRhinoCommand::result CCommandFooBar::RunCommand( const CRhinoCommandContext& context )
    {
      ON_3dPoint box_corners[8];
      CArgsRhinoGetBox args;
    
      CRhinoCommand::result rc = RhinoGetBox( args, box_corners, 0 );
      if( rc == CRhinoCommand::success )
      {
        int degree[3] = {3,3,3};   // defaults
        int cv_count[3] = {4,4,4}; // defaults
    
        ON_NurbsCage nurbs_cage;
        if( nurbs_cage.Create( box_corners,
            degree[0]+1, degree[1]+1, degree[2]+1,
            cv_count[0], cv_count[1], cv_count[2])
            )
        {
          CRhinoCageObject* cage_object = new CRhinoCageObject();
          if( cage_object )
          {
            cage_object->SetCage( nurbs_cage );
            context.m_doc.AddObject( cage_object );
            context.m_doc.Redraw();
          }
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

