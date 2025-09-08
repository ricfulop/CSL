---
url: https://developer.rhino3d.com/guides/cpp/finding-points-on-curves-at-arc-length-distances/
scraped_at: 2025-09-08T15:38:57.421347
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

[Finding Points on Curves at Arc Length
Distances](https://developer.rhino3d.com/guides/cpp/finding-points-on-curves-
at-arc-length-distances/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Finding Points on Curves at Arc Length Distances

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

For a given length from the beginning of a curve, you would like to get the
curve’s parameter at this point.

## Solution

The two functions on `ON_Curve` that are useful for determining the parameter
of the point on a curve that is a prescribed arc length distance from the
start of a curve are:

  * `ON_Curve::GetNormalizedArcLengthPoint`
  * `ON_Curve::GetNormalizedArcLengthPoints`

To use these functions, calculate a normalized arc length parameter. That is,
a parameter on the curve where 0.0 = the start of the curve, 0.5 = the
midpoint of the curve, and 1.0 = the end of the curve.

**NOTE** : To determine the parameter of the point on a curve that is a
prescribed arc length distance from the end of a curve, just reverse the curve
before calling one of the above curve members.

## Sample

The following code sample demonstrates how to use these functions:

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const CRhinoObjRef& obj_ref = go.Object(0);
      const ON_Curve* crv = obj_ref.Curve();
      if( 0 == crv )
        return failure;
    
      double crv_length = 0.0;
      if( !crv->GetLength(&crv_length) )
        return failure;
    
      CRhinoGetNumber gn;
      gn.SetCommandPrompt( L"Length from start" );
      gn.SetLowerLimit( 0.0, TRUE );
      gn.SetUpperLimit( crv_length, TRUE );
      gn.GetNumber();
      if( gn.CommandResult() != success )
        return gn.CommandResult();
    
      // Cook up a normalized arc length parameter,
      // where 0.0 <= s <= 1.0.
      double length = fabs( gn.Number() );
      double s = 0.0;
      if( length == 0.0 )
        s = 0.0;
      else if( length == crv_length )
        s = 1.0;
      else
        s = length / crv_length;
    
      // Get the parameter of the point on the curve that is a
      // prescribed arc length from the start of the curve.
      double t = 0.0;
      if( crv->GetNormalizedArcLengthPoint(s, &t) )
      {
        ON_3dPoint pt = crv->PointAt( t );
        context.m_doc.AddPointObject( pt );
        context.m_doc.Redraw();
      }
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/finding-
points-on-curves-at-arc-length-distances/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/finding-
points-on-curves-at-arc-length-distances/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

