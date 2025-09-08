---
url: https://developer.rhino3d.com/samples/cpp/create-nurbs-surface/
scraped_at: 2025-09-08T15:47:26.093377
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

Create NURBS Surface

__

Windows only

Demonstrates how to create a NURBS surface.

C/C++

    
    
    static bool CreateSurfacesExample( CRhinoDoc& doc )
    {
      const int bIsRational = false;
      const int dim = 3;
      const int u_degree = 2;
      const int v_degree = 3;
      const int u_cv_count = 3;
      const int v_cv_count = 5;
    
      // The knot vectors do NOT have the 2 superfluous knots
      // at the start and end of the knot vector.  If you are
      // coming from a system that has the 2 superfluous knots,
      // just ignore them when creating NURBS surfaces.
      double u_knot[ u_cv_count + u_degree - 1 ];
      double v_knot[ v_cv_count + v_degree - 1 ];
    
      // make up a quadratic knot vector with no interior knots
      u_knot[0] = u_knot[1] = 0.0;
      u_knot[2] = u_knot[3] = 1.0;
    
      // make up a cubic knot vector with one simple interior knot
      v_knot[0] = v_knot[1] = v_knot[2] = 0.0;
      v_knot[3] = 1.5;
      v_knot[4] = v_knot[5] = v_knot[6] = 2.0;
    
      // Rational control points can be in either homogeneous
      // or euclidean form. Non-rational control points do not
      // need to specify a weight.  
      ON_3dPoint CV[u_cv_count][v_cv_count];
    
      int i, j;
      for ( i = 0; i < u_cv_count; i++ ) {
        for ( j = 0; j < v_cv_count; j++ ) {
          CV[i][j].x = i;
          CV[i][j].y = j;
          CV[i][j].z = i-j;
        }
      }
    
      ON_NurbsSurface nurbs_surface( dim, bIsRational,
                            u_degree+1, v_degree+1,
                            u_cv_count, v_cv_count );
    
      for ( i = 0; i < nurbs_surface.KnotCount(0); i++ )
        nurbs_surface.SetKnot( 0, i, u_knot[i] );
    
      for ( j = 0; j < nurbs_surface.KnotCount(1); j++ )
        nurbs_surface.SetKnot( 1, j, v_knot[j] );
    
      for ( i = 0; i < nurbs_surface.CVCount(0); i++ ) {
        for ( j = 0; j < nurbs_surface.CVCount(1); j++ ) {
          nurbs_surface.SetCV( i, j, CV[i][j] );
        }
      }
    
      bool ok = false;
      if ( nurbs_surface.IsValid() )
      {
        doc.AddSurfaceObject( nurbs_surface );
        doc.Redraw();
        ok = true;
      }
    
      return ok;
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

