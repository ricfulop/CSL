---
url: https://developer.rhino3d.com/guides/cpp/adding-nurbs-curve-from-control-points/
scraped_at: 2025-09-08T15:38:37.340721
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

[Adding a NURBS Curve from Control
Points](https://developer.rhino3d.com/guides/cpp/adding-nurbs-curve-from-
control-points/)

  * Overview
  * Method 1
  * Method 2

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Adding a NURBS Curve from Control Points

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Imagine you would like to create a NURBS curve from a set of control points,
such that it looks like this:

![NURBS Curve Control Points](https://developer.rhino3d.com/images/adding-a-
nurbs-curve-from-control-points-01.png)

There are two methods to achieve this…

## Method 1

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
            const CRhinoCommandContext& context )
    {
      ON_3dPointArray points;
      points.Append( ON_3dPoint(0, 0, 0) );
      points.Append( ON_3dPoint(0, 2, 0) );
      points.Append( ON_3dPoint(2, 4, 0) );
      points.Append( ON_3dPoint(4, 2, 0) );
      points.Append( ON_3dPoint(4, 0, 0) );
     
      CRhinoCommand::result res;
      ON_NurbsCurve nc;
      if ( nc.CreateClampedUniformNurbs( 3, 4, points.Count(), points)
        && nc.IsValid())
      {
        context.m_doc.AddCurveObject( nc );
        res = CRhinoCommand::success;
      }
      else
        res = CRhinoCommand::failure;
    
      context.m_doc.Redraw();
      return res;
    }
    

## Method 2

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
            const CRhinoCommandContext& context )
    {
      ON_3dPointArray points;
      points.Append( ON_3dPoint(0, 0, 0) );
      points.Append( ON_3dPoint(0, 2, 0) );
      points.Append( ON_3dPoint(2, 4, 0) );
      points.Append( ON_3dPoint(4, 2, 0) );
      points.Append( ON_3dPoint(4, 0, 0) );
    
      int dimension = 3;
      bool bIsRat = false;
      int order = 4;
      int cv_count = points.Count();
    
      ON_NurbsCurve nc(dimension, bIsRat, order, cv_count);
      if( !nc.IsValid() )
      {
        return CRhinoCommand::failure;
      }
    
      //Set CV points
      nc.ReserveCVCapacity( cv_count );
      for( int i = 0; i < cv_count; i++ )
      {
        nc.SetCV(i, points[i] );
      }
    
      //Set Knots
      nc.ReserveKnotCapacity( order+cv_count-2 );
      ON_MakeClampedUniformKnotVector( order, cv_count, nc.m_knot );
    
      CRhinoCommand::result res;
    
      if( nc.IsValid() )
      {
        context.m_doc.AddCurveObject( nc );
        res = CRhinoCommand::success;
      }
      else
        res = CRhinoCommand::failure;
    
      context.m_doc.Redraw();
      return res;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/adding-
nurbs-curve-from-control-points/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/adding-
nurbs-curve-from-control-points/index.md) [
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

