---
url: https://developer.rhino3d.com/guides/cpp/finding-parameter-of-curve-at-point/
scraped_at: 2025-09-08T15:38:59.415689
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

[Finding the Parameter of a Curve at a
Point](https://developer.rhino3d.com/guides/cpp/finding-parameter-of-curve-at-
point/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Finding the Parameter of a Curve at a Point

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

In general, to find the parameter of a point on a curve that is closest to a
test point, use `ON_Curve::GetClosestPoint()`. See _opennurbs_curve.h_ for
more information.

## Sample

The following sample code demonstrates how to find the parameter of a curve at
a point. The code demonstrates how to select a curve object, and how to pick a
point on a curve.

For more information on the `CRhinoObjRef` class, see _rhinoSdkObject.h_.

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
        const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const CRhinoObjRef& objref = go.Object( 0 );
      const ON_Curve* crv = objref.Curve();
      if( !crv )
        return CRhinoCommand::failure;
    
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Pick a location on the curve" );
      gp.Constrain( *crv ); // constrain to curve
      gp.GetPoint();
      if( gp.CommandResult() != CRhinoCommand::success )
        return gp.CommandResult();
    
      ON_3dPoint pt = gp.Point();
      double t = 0.0;
      if( crv->GetClosestPoint(pt, &t) )
        RhinoApp().Print(
          L"Curve parameter at (%f,%f,%f) is %g.\n",
          pt.x, pt.y, pt.z, t );
    
      return CRhinoCommand::success;
    }
    

It is possible to save a step by examining the `CRhinoObjRef` class. The class
return information on the picking operation that just occurred, including the
object that was picked, the point that the user picked, and in this case, the
parameter of the curve that was closest to the picked point.

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
          const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const CRhinoObjRef& objref = go.Object( 0 );
    
      ON_3dPoint pt;
      objref.SelectionPoint( pt )
      double t = 0.0;
      const ON_Curve* crv = objref.CurveParameter( &t );
      if( crv )
        RhinoApp().Print(
            L"Curve parameter at (%f,%f,%f) is %g.\n",
            pt.x, pt.y, pt.z, t );
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/finding-
parameter-of-curve-at-point/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/finding-
parameter-of-curve-at-point/index.md) [
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

