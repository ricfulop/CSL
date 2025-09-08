---
url: https://developer.rhino3d.com/guides/opennurbs/brep-loop-edge-directions/
scraped_at: 2025-09-08T15:38:10.207513
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

[Brep Loop & Edge
Directions](https://developer.rhino3d.com/guides/opennurbs/brep-loop-edge-
directions/)

  * Question
  * Answer

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Brep Loop & Edge Directions

by [Dale Lear](https://discourse.mcneel.com/u/dalelear/) (Last updated:
Wednesday, December 5, 2018)

## Question

Is there a function to query if a loop `ON_BrepLoop` is reversed on the face
`ON_BrepFace`? In other words, whether the boundary of the face agrees with or
opposes that of the corresponding loop?

Also, is there a way to query if the edge `ON_BrepEdge` direction is reversed?
Or, whether an edge curve agrees with the start and end vertices?

## Answer

Loops are always oriented so that the active region of the face is to the left
of the 2D curve. Thus, outer loops are oriented counter-clockwise and inner
loops are oriented clockwise.

Also, to determine whether or not an edge is reversed, use
`ON_BrepEdge::ProxyCurveIsReversed()`. See _opennurbs_curveproxy.h_ for
details.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/brep-
loop-edge-directions/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/brep-
loop-edge-directions/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

