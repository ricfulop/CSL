---
url: https://developer.rhino3d.com/samples/cpp/add-truncated-cone/
scraped_at: 2025-09-08T15:47:22.086778
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

Add Truncated Cone

__

Windows only

Demonstrates how to create a truncated cone ON_BrepRevSurface and add it to
Rhino.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      ON_3dPoint bottom_pt( 0.0, 0.0, 0.0 );
      double bottom_radius = 2;
      ON_Circle bottom_circle( bottom_pt, bottom_radius );
    
      ON_3dPoint top_pt( 0.0, 0.0, 10.0 );
      double top_radius = 6;
      ON_Circle top_circle( top_pt, top_radius );
    
      ON_RevSurface* revsrf = new ON_RevSurface;
      ON_LineCurve* pShapeCurve = new ON_LineCurve;
      revsrf->m_curve = pShapeCurve;
      pShapeCurve->m_dim = 3;
      pShapeCurve->m_line.from = bottom_circle.PointAt(0);
      pShapeCurve->m_line.to = top_circle.PointAt(0);
      pShapeCurve->m_t.Set(0, pShapeCurve->m_line.from.DistanceTo(pShapeCurve->m_line.to));
      revsrf->m_axis.from = bottom_circle.Center();
      revsrf->m_axis.to = top_circle.Center();
      revsrf->m_angle[0] = revsrf->m_t[0] = 0.0;
      revsrf->m_angle[1] = revsrf->m_t[1] = 2.0*ON_PI;
    
      ON_Brep* tcone_brep = ON_BrepRevSurface(revsrf, TRUE, TRUE );
      if( tcone_brep )
      {
        CRhinoBrepObject* tcone_object = new CRhinoBrepObject();
        tcone_object->SetBrep( tcone_brep );
        if( context.m_doc.AddObject(tcone_object) )
          context.m_doc.Redraw();
        else
          delete tcone_object;
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

