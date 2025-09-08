---
url: https://developer.rhino3d.com/guides/cpp/determining-if-brep-is-box/
scraped_at: 2025-09-08T15:38:54.410152
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

[Determining if a Brep is a
Box](https://developer.rhino3d.com/guides/cpp/determining-if-brep-is-box/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Determining if a Brep is a Box

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to determine whether or not a polysurface is a (brep) box.

## Solution

For a polysurface to be a box, the following conditions must be true:

  1. The brep must be solid.
  2. The brep must have six faces.
  3. Each of the six faces must be planar.
  4. Each of the planar face must be either perpendicular or antiparallel to the other planar faces.

## Sample

The following sample functions demonstrate how to determine whether or not a
polysurface is a box.

    
    
    bool IsBrepBox( const ON_Brep& brep )
    {
      double zero_tolerance = 1.0e-6; // or whatever
      ON_3dVector N[6];
    
      bool rc = brep.IsSolid();
    
      if (rc)
        rc = (brep.m_F.Count() == 6);
    
      if (rc)
      {
        for (int i = 0; rc && i < 6; i++)
        {
          ON_Plane plane;
          if (brep.m_F[i].IsPlanar(&plane, zero_tolerance))
          {
            N[i] = plane.zaxis;
            N[i].Unitize();
          }
          else
            rc = false;
        }
      }
    
      if (rc)
      {
        for (int i = 0; rc && i < 6; i++)
        {
          int count = 0;
          for (int j = 0; rc && j < 6; j++)
          {
            double dot = fabs(N[i] * N[j]);
            if (fabs(dot) <= zero_tolerance)
              continue;
            if (fabs(dot - 1.0) <= zero_tolerance)
              count++;
            else
              rc = false;
          }
    
          if (rc)
          {
            if (2 != count)
              rc = false;
          }
        }
      }
    
      return rc;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/determining-
if-brep-is-box/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/determining-
if-brep-is-box/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

