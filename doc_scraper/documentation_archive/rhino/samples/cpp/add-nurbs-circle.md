---
url: https://developer.rhino3d.com/samples/cpp/add-nurbs-circle/
scraped_at: 2025-09-08T15:47:13.038524
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

Add a NURBS Circle

__

Windows only

Demonstrates how to use ON_NurbsCurve to create a circle.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context )
    {
      int dimension = 3;
      BOOL bIsRational = TRUE;
      int order = 3;
      int cv_count = 9;
    
      ON_NurbsCurve nc( dimension, bIsRational, order, cv_count );
      nc.SetCV( 0, ON_4dPoint(1.0, 0.0, 0.0, 1.0) );
      nc.SetCV( 1, ON_4dPoint(0.707107, 0.707107, 0.0, 0.707107) );
      nc.SetCV( 2, ON_4dPoint(0.0, 1.0, 0.0, 1.0) );
      nc.SetCV( 3, ON_4dPoint(-0.707107, 0.707107, 0.0, 0.707107) );
      nc.SetCV( 4, ON_4dPoint(-1.0, 0.0, 0.0, 1.0) );
      nc.SetCV( 5, ON_4dPoint(-0.707107, -0.707107, 0.0, 0.707107) );
      nc.SetCV( 6, ON_4dPoint(0.0, -1.0, 0.0, 1.0) );
      nc.SetCV( 7, ON_4dPoint(0.707107, -0.707107, 0.0, 0.707107) );
      nc.SetCV( 8, ON_4dPoint(1.0, 0.0, 0.0, 1.0) );
      nc.SetKnot( 0, 0.0 );
      nc.SetKnot( 1, 0.0 );
      nc.SetKnot( 2, 0.5*ON_PI );
      nc.SetKnot( 3, 0.5*ON_PI );
      nc.SetKnot( 4, ON_PI );
      nc.SetKnot( 5, ON_PI );
      nc.SetKnot( 6, 1.5*ON_PI );
      nc.SetKnot( 7, 1.5*ON_PI );
      nc.SetKnot( 8, 2.0*ON_PI );
      nc.SetKnot( 9, 2.0*ON_PI );
    
      if( nc.IsValid() )
      {
        context.m_doc.AddCurveObject( nc );
        context.m_doc.Redraw();
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

