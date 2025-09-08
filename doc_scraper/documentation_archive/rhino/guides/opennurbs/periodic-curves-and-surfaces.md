---
url: https://developer.rhino3d.com/guides/opennurbs/periodic-curves-and-surfaces/
scraped_at: 2025-09-08T15:38:13.233657
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

[Periodic Curves &
Surfaces](https://developer.rhino3d.com/guides/opennurbs/periodic-curves-and-
surfaces/)

  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Periodic Curves & Surfaces

by [Dale Lear](https://discourse.mcneel.com/u/dalelear/) (Last updated:
Wednesday, December 5, 2018)

A periodic knot vector can be either uniform or non-uniform.

A periodic degree d NURBS curve has (d-1) continuous derivatives at the
start/end point.

The differences between successive knot values are equal near the start and
end of the spline; that is, the differences repeat themselves and hence the
term “periodic”.

Specifically, when -degree < i < degree, a periodic knot vector satisfies:

    
    
    k[(degree-1)+i+1] - k[(degree-1)+i] = k[(cv_count-1)+i+1] - k[(cv_count)+i]
    

For example a cubic periodic knot vector looks like:

    
    
    {a,b,c,d,e, ...,  p+a,p+b,p+c,p+d,p+e}
    

with a < b < c < d < e and e < p+a.

Chapter 12 of The NURBS Book has a few pages discussing periodic
[NURBS](https://developer.rhino3d.com/guides/opennurbs/nurbs-geometry-
overview/) (look in the index), but the discussion is limited. Chapter 14 of
DeBoor’s Practical Guide to Splines provides a few more details.

## Related topics

  * [NURBS Geometry Overview](https://developer.rhino3d.com/guides/opennurbs/nurbs-geometry-overview/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/periodic-
curves-and-surfaces/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/periodic-
curves-and-surfaces/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

