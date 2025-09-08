---
url: https://developer.rhino3d.com/guides/opennurbs/what-is-rhino3dmio/
scraped_at: 2025-09-08T15:38:05.257617
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

[What is Rhino3dm?](https://developer.rhino3d.com/guides/opennurbs/what-is-
rhino3dmio/)

  * Overview
  * Rhino3dm.py
  * Rhino3dm.js
  * Rhino3dm.NET

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

What is Rhino3dm?

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) (Last updated:
Monday, October 7, 2024)

## Overview

Rhino3dm is a set of libraries based on the
[OpenNURBS](https://developer.rhino3d.com/guides/opennurbs/what-is-opennurbs/)
geometry library. They provide the ability to access and manipulate geometry
through .NET, Python or JavaScript applications independent of Rhino.

Functionality includes:

  * Create, interrogate, and store all geometry types supported in Rhino. This includes points, point clouds, NURBS curves and surfaces, polysurfaces (BReps), meshes, annotations, extrusions, and SubDs.
  * Work with non-geometry classes supported in Rhino like layers, object attributes, transforms and viewports.
  * Read and write all of the above information to and from the .3dm file format.
  * Use as a client to make calls into the [Rhino.Compute](https://developer.rhino3d.com/guides/compute/) cloud server for advanced manipulation of geometry objects.
  * Available on most platforms (Windows, macOS, Linux).

Rhino3dm is [open source](https://github.com/mcneel/rhino3dm).

Explore all of the rhino3dm samples: [rhino3dm
samples](https://github.com/mcneel/rhino-developer-samples/tree/8/rhino3dm)

#### WARNING

Rhino3dm is NOT meant for any Rhino plug-in development. You should only be
using Rhino3dm if you are attempting to read/write 3dm files from an
application other than Rhino!

Rhino3dm comes in three flavors.

## Rhino3dm.py

[Rhino3dm.py](https://pypi.org/project/rhino3dm/) is a Python package that can
be used on all current versions of CPython (3.7 - 3.11) and is available on
all platforms (Windows, macOS, Linux).

Rhino3dm.pys packages are available on the [Python Package Index
(PyPI)](https://pypi.org/project/rhino3dm/).

See our [Python
documentation](https://github.com/mcneel/rhino3dm/blob/main/docs/python/RHINO3DM.PY.md)
for details.

## Rhino3dm.js

[Rhino3dm.js](https://www.npmjs.com/package/rhino3dm) is a JavaScript library
with an associated web assembly (rhino3dm.wasm). Rhino3dm.js should run on all
major browsers as well as [node.js](https://nodejs.org).

Rhino3dm.js packages are available on
[npm](https://www.npmjs.com/package/rhino3dm).

See our [JavaScript
documentation](https://github.com/mcneel/rhino3dm/blob/main/docs/javascript/RHINO3DM.JS.md)
for details.

## Rhino3dm.NET

[Rhino3dm.NET](https://www.nuget.org/packages/Rhino3dm/), formerly known as
Rhino3dmIO, allows you to write standalone .NET applications.

Rhino3dm.NET packages are available on
[NuGet](https://www.nuget.org/packages/Rhino3dm/).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/what-
is-rhino3dmio/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/what-
is-rhino3dmio/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

