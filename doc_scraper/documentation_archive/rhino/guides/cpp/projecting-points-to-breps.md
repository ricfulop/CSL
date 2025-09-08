---
url: https://developer.rhino3d.com/guides/cpp/projecting-points-to-breps/
scraped_at: 2025-09-08T15:40:08.703632
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

[Projecting Points to
Breps](https://developer.rhino3d.com/guides/cpp/projecting-points-to-breps/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Projecting Points to Breps

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to project a 2D point (x,y) onto a brep object in order to
acquire the z-coordinate.

## Solution

Use the `RhinoProjectPointsToBreps` function. In order to use this function
you will need to provide the following:

  1. An array of one or more Brep objects.
  2. An array of one or more points to project.
  3. A projection direction (vector).

## Sample

The following sample code demonstrates how you can use this function…

    
    
    CRhinoCommand::result CCommandFoobarCpp::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt(L"Select surface or polysurface");
      go.SetGeometryFilter(
        CRhinoGetObject::surface_object |
        CRhinoGetObject::polysrf_object
        );
      go.GetObjects(1, 1);
      if (go.CommandResult() != CRhinoCommand::success)
        return go.CommandResult();
    
      const ON_Brep* brep = go.Object(0).Brep();
      if (0 == brep)
        return CRhinoCommand::failure;
    
      ON_3dPoint point(0.0, 0.0, 0.0); // some point on the world x-y plane
    
      // Prepare input to RhinoProjectPointsToBreps
    
      ON_SimpleArray<const ON_Brep*> Breps;
      Breps.Append(brep);
    
      ON_3dPointArray Points;
      Points.Append(point);
    
      ON_3dVector ProjDir(0.0, 0.0, 1.0); // world z-axis
    
      ON_3dPointArray OutPoints;
      ON_SimpleArray<int> Indices;
    
      bool rc = RhinoProjectPointsToBreps(
        Breps,
        Points,
        ProjDir,
        OutPoints,
        Indices,
        context.m_doc.AbsoluteTolerance()
        );
    
      if (rc == true)
      {
        for (int i = 0; i < OutPoints.Count(); i++)
        {
          ON_3dPoint pt = OutPoints[i];
          context.m_doc.AddPointObject(pt);
        }
        context.m_doc.Redraw();
      }
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/projecting-
points-to-breps/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/projecting-
points-to-breps/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

