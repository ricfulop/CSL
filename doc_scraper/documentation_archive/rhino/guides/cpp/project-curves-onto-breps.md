---
url: https://developer.rhino3d.com/guides/cpp/project-curves-onto-breps/
scraped_at: 2025-09-08T15:40:07.707312
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

[Project Curves onto Breps](https://developer.rhino3d.com/guides/cpp/project-
curves-onto-breps/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Project Curves onto Breps

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You want to project curves onto a brep, but you do not function any C/C++
function to do this. Is there a solution for this?

## Solution

It is true that the Rhino C/C++ SDK does not currently have a function that
will project a curve onto a brep. But, using some of the existing functions,
you can write your own function without too much effort.

To project a curve onto a brep, you need to do the following:

  1. Extrude the curve through the brep using the `RhinoExtrudeCurveStraight()` function.
  2. Intersect the two breps using `RhinoIntersectBreps()` function.
  3. The results of the brep intersection will be the projected curves.

## Sample

The following sample code demonstrates how one might write such a function…

    
    
    /*
    Description:
      Projects a curve onto a surface or polysurface
    Parameters:
      brep  - [in] The brep to project the curve onto.
      curve - [in] The curve to project.
      dir   - [in] The direction of the projection.
      tol   - [in] The intersection tolerance.
      output_curves - [out] The output curves.
                            NOTE, the caller is responsible
                            for destroying these curves.
    Returns:
      true if successful.
      false if unsuccessful.
    */
    bool ProjectCurveToBrep(
            const ON_Brep& brep,
            const ON_Curve& curve,
            const ON_3dVector& dir,
            double tolerance,
            ON_SimpleArray<ON_Curve*>& output_curves
            )
    {
      ON_3dVector n = dir;
      if( !n.Unitize() )
        return false;
    
      ON_BoundingBox bbox = brep.BoundingBox();
      bbox.Union( curve.BoundingBox() );
    
      ON_Surface* pExtrusion = RhinoExtrudeCurveStraight( &curve, dir, bbox.Diagonal().Length() );
      if( 0 == pExtrusion )
        return false;
    
      ON_Brep* pBrep = ON_Brep::New();
      pBrep->Create( pExtrusion );
    
      BOOL rc = RhinoIntersectBreps( *pBrep, brep, tolerance, output_curves );
      delete pBrep; // Don't leak...
    
      return ( rc ) ? true : false;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/project-
curves-onto-breps/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/project-
curves-onto-breps/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

