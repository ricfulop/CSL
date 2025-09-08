---
url: https://developer.rhino3d.com/guides/grasshopper/multi-treaded-components/
scraped_at: 2025-09-08T15:41:33.098305
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

[Multi-threaded
components](https://developer.rhino3d.com/guides/grasshopper/multi-treaded-
components/)

  * Overview
  * Creating you own multi-threaded components in Grasshopper

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) /

Multi-threaded components

by [Steve Baer](https://discourse.mcneel.com/u/stevebaer/) and [Scott
Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated: Wednesday,
December 5, 2018)

## Overview

Grasshopper for Rhino 6 provides multi-threaded solving in specific
components. Benchmarks have shown that Grasshopper can be up to 20% faster
when using multi-threaded components. Results may vary as there are only
specific components that can compute in parallel.

The following components have been modified to perform calculations using
multiple threads.

  * Curve Plane Intersection
  * Project Curve
  * Pull Curve
  * Split with Brep
  * Shatter
  * Split with Breps
  * Trim with Brep
  * Trim with Breps
  * Area
  * Area Moments
  * Volume
  * Volume Moments
  * Brep Closest Point
  * Mesh Plane Intersection
  * Brep Line Intersection
  * Brep Brep Intersection
  * Brep Plane Intersection
  * Curve Curve Intersection
  * Curve Curves Intersection
  * Point in Brep
  * Point in Breps
  * Curve Self-Intersection
  * Contour
  * Dash Pattern
  * Divide Curve
  * Boundary Surface

Multi-threaded components are decorated with small dots in the upper left
corner to help you understand the component’s capabilities and current ‘mode’
of operation.

![https://developer.rhino3d.com/images/gh-multi-
threaded.png](https://developer.rhino3d.com/images/gh-multi-threaded.png)

  * No dots : the component does not currently support multi-threaded calculations
  * One dot: the component does support multi-threaded calculations, but is currently calculating with a single thread (i.e. legacy mode)
  * Two dots: the component does support multi-threaded calculations and is solving using multiple threads.

For components that support multi-threaded calculations, the feature can be
enabled/disabled using the right click context menu on the component itself.

We continue to look for components that would be useful to have multi-
threaded. Join the [Multi-threaded Grasshopper component
discussion](https://discourse.mcneel.com/t/v6-feature-multi-threaded-gh-
components/47049) to participate.

## Creating you own multi-threaded components in Grasshopper

Custom multi-threaded components are also possible by programmer your own
components in C# or Python. for details on this read the [Making Task Capable
Components in
Grasshopper](https://developer.rhino3d.com/guides/grasshopper/programming-
task-capable-component/) guide

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/multi-
treaded-components/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/multi-
treaded-components/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

