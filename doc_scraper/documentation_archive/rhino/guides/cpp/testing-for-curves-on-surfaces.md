---
url: https://developer.rhino3d.com/guides/cpp/testing-for-curves-on-surfaces/
scraped_at: 2025-09-08T15:40:15.742835
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

[Testing for Curves on
Surfaces](https://developer.rhino3d.com/guides/cpp/testing-for-curves-on-
surfaces/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Testing for Curves on Surfaces

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

In your plugin, you are using a surface and an interpolated curve on that
surface. You know the curve is interpolated on the surface because that is how
you created it (using the _InterpCrfOnSrf_ command). Now, what if you import
some other 3dm file with curve and surface already in it? How can one check
that curve lies completely on surface using C/C++?

## Solution

The Rhino C/C++ SDK does not have a function that tests whether or not a curve
lies on a surface. But, you can write your own test that should give you the
correct answer for most cases.

The best approach for writing a function to do this would be to sample many
curve points and perform closest point tests against the surface with each
curve point. If the distance between the curve points and the surface points
are within some tolerance, then chances are the curve is on the surface - at
least the sampled points are on the surface.

## Sample

The following sample function does just this:

    
    
    // Description:
    //   Test to see if a curve lies on a surface.
    // Parameters:
    //   srf - [in] The surface
    //   crv - [in] The curve
    //   tol - [in] The tolerance
    // Returns:
    //   True if the curve (probably) lies on the surface.
    //   False otherwise.
    
    static bool RhinoIsCurveOnSurface(
            const ON_Surface& srf,
            const ON_Curve& crv,
            double tol
            )
    {
      if( !srf.IsValid() | !crv.IsValid() )
        return false;
    
      ON_NurbsCurve nc;
      if( !crv.GetNurbForm(nc) )
        return false;
    
      const int span_count = nc.SpanCount();
      ON_SimpleArray<double> span_vector( span_count + 1 );
      span_vector.SetCount( span_count + 1 );
      nc.GetSpanVector( span_vector.Array() );
    
      bool rc = true;
      double num_samples = nc.Degree() * 2;
      int i, j;
      for( i = 0; i < span_count && rc; i++ )
      {
        ON_Interval span( span_vector[i], span_vector[i+1] );
        rc = span.IsIncreasing();
        if( rc )
        {
          for( j = 0; j <= num_samples && rc; j++ )
          {
            double crv_t = span.ParameterAt( j / num_samples );
            ON_3dPoint crv_pt = nc.PointAt( crv_t );
            double s = 0.0, t = 0.0;
            rc = srf.GetClosestPoint( crv_pt, &s, &t );
            if( rc )
            {
              ON_3dPoint srf_pt = srf.PointAt( s, t );
              rc = ( fabs(crv_pt.DistanceTo(srf_pt)) <= tol );
            }
          }
        }
      }
    
      return rc;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/testing-
for-curves-on-surfaces/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/testing-
for-curves-on-surfaces/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

