---
url: https://developer.rhino3d.com/guides/cpp/extracting-curve-edit-points/
scraped_at: 2025-09-08T15:39:52.533901
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

[Extracting Curve Edit
Points](https://developer.rhino3d.com/guides/cpp/extracting-curve-edit-
points/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Extracting Curve Edit Points

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to extract a curve’s edit points - the points you see when you
run the _EditPtOn_ command, but you do not see any methods on `ON_Curve` or
`ON_NurbsCurve` to do this.

## Solution

Unlike control points, edit points are not part of a NURBS curve’s data
structure. Rather, they are calculated when needed.

The following code demonstrates to get obtain the edit points for a NURBS
curve and then create point objects at those locations.

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const ON_Curve* crv = go.Object(0).Curve();
      if( 0 == crv )
        return failure;
    
      ON_NurbsCurve nc;
      if( crv->GetNurbForm(nc) )
      {
        // For every control point, we can calculate
        // a cooresponding edit point.
        ON_SimpleArray<double> t( nc.CVCount() );
        t.SetCount( nc.CVCount() );
    
        if( nc.GetGrevilleAbcissae(t.Array()) )
        {
          int i;
          for( i = 0; i < t.Count(); i++ )
            context.m_doc.AddPointObject( nc.PointAt(t[i]) );
          context.m_doc.Redraw();
        }
      }
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/extracting-
curve-edit-points/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/extracting-
curve-edit-points/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

