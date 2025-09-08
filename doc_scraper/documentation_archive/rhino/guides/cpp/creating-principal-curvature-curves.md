---
url: https://developer.rhino3d.com/guides/cpp/creating-principal-curvature-curves/
scraped_at: 2025-09-08T15:38:49.420647
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

[Create Principal Curvature
Curves](https://developer.rhino3d.com/guides/cpp/creating-principal-curvature-
curves/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Create Principal Curvature Curves

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You are looking for a way to create Principal Curvature lines starting with
points on a surface. There is an `ON_EvPrincipalCurvatures` function, it’s not
clear how it should be used.

## Solution

Before using `ON_EvPrincipalCurvatures`, you will need to calculate the second
derivative of the surface that the test location. Then, it is just a matter of
creating up some curves based on the results.

## Sample

The following is an example of how you might write such a command.

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoGetObject go;
      go.SetCommandPrompt(L"Select surface");
      go.SetGeometryFilter(CRhinoGetObject::surface_object);
      go.GetObjects(1, 1);
      if (go.CommandResult() != CRhinoCommand::success)
        return go.CommandResult();
    
      const CRhinoObject* obj = go.Object(0).Object();
      const ON_BrepFace* face = go.Object(0).Face();
      if (nullptr == obj || nullptr == face)
        return CRhinoCommand::failure;
    
      CRhinoGetPoint gp;
      gp.SetCommandPrompt(L"Select point on surface");
      gp.Constrain(*face, obj->Attributes().m_wire_density);
      gp.GetPoint();
      if (gp.CommandResult() != CRhinoCommand::success)
        return gp.CommandResult();
    
      double s = 0.0, t = 0.0;
      const ON_Surface* srf = gp.PointOnSurface(&s, &t);
      if (nullptr == srf)
        return CRhinoCommand::failure;
    
      ON_3dPoint P;
      ON_3dVector Ds, Dt, Dss, Dst, Dtt;
      if (!srf->Ev2Der(s, t, P, Ds, Dt, Dss, Dst, Dtt))
        return CRhinoCommand::failure; // failed to evaluate derivatives
    
      ON_3dVector N;
      if (!srf->EvNormal(s, t, N))
        return CRhinoCommand::failure; // failed to evaluate normal
    
      double gauss = 0.0, mean = 0.0, k[2] = { 0.0, 0.0 };
      ON_3dVector K[2];
      if (!ON_EvPrincipalCurvatures(Ds, Dt, Dss, Dst, Dtt, N, &gauss, &mean, &k[0], &k[1], K[0], K[1]))
        return CRhinoCommand::failure; // failed to evaluate principal curvatures
    
      for (int i = 0; i < 2; i++)
      {
        if (fabs(k[i]) <= 1.0e-4 || fabs(k[i]) >= 1.0e4)
        {
          // just draw a line as curvature is huge/tiny
          ON_Line line(P - K[i] * 5.0, P + K[i] * 5.0);
          context.m_doc.AddCurveObject(line);
        }
        else
        {
          double r = 1.0 / k[i];
          ON_3dPoint center = P + r * N;
          ON_3dPoint start = center - r * K[i];
          ON_3dPoint end = center + r * K[i];
          ON_Arc arc(start, P, end);
          context.m_doc.AddCurveObject(arc);
        }
      }
      context.m_doc.Redraw();
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/creating-
principal-curvature-curves/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/creating-
principal-curvature-curves/index.md) [
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

