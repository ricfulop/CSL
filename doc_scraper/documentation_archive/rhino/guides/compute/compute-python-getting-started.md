---
url: https://developer.rhino3d.com/guides/compute/compute-python-getting-started/
scraped_at: 2025-09-08T15:43:15.517548
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

[Calling Compute with
Python](https://developer.rhino3d.com/guides/compute/compute-python-getting-
started/)

  * Setting up a Compute Project in Python
  * The first use of Compute

[Guides](https://developer.rhino3d.com/en/guides/) / [Compute
Guides](https://developer.rhino3d.com/en/guides/compute/) /

Calling Compute with Python

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Thursday, November 12, 2020)

By the end of this guide, you should have all the tools installed necessary
for using the [Rhino Compute](https://www.rhino3d.com/compute) through Python.

For an [getting started video tutorial from Junichiro Horikawa with
Python](https://youtu.be/XCkRXAEJMhg)

This guide presumes you have Python installed on the platform:

  * Python 2.7 - Windows (32 and 64 bit)
  * Python 3.7 - Windows (32 and 64 bit)
  * Python 2.7 - OSX (installed through homebrew)
  * Python 3.7 - OSX (installed through homebrew)
  * Linux and other python versions are supported through source distributions on PyPi

## Setting up a Compute Project in Python

There are a few client side tools which need to be installed in Python that
are essential to communicate with the Compute server. These include:

  * **rhino3dm.py** \- This is the part of the [Rhino3dm libraries](https://github.com/mcneel/rhino3dm). It is a Python wrapper for [OpenNurbs](https://developer.rhino3d.com/guides/opennurbs/) which contains the functions to read and write Rhino Geometry Objects. This is available as a Pip package.

`pip install rhino3dm`

  * **compute-rhino3d.py** \- This is a work in progress package which is meant to add classes available in [RhinoCommon](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/), but not available through rhino3dm.py. Compute-rhino3d makes calls into the McNeel Cloud Compute server for these functions. It handles all the transaction authorizations and JSON data conversion.

`pip install compute-rhino3d`

## The first use of Compute

An example of using Python to access compute can be found in the [makemesh.py
example](https://github.com/mcneel/rhino-developer-
samples/tree/8/compute/py/SampleTkinter).

Please note that the compute Python calls are made through the
`compute_rhino3d.py` package using a `_` (underbar) and not a `-` (dash).

# Next Steps

_Congratulations!_ You have the tools to use [Rhino Compute
server](https://www.rhino3d.com/compute). _Now what?_

  1. To see the transactional nature of Compute, read through **compute.rhino3d.py**
  2. See a list of the [2400+ API calls](https://compute.rhino3d.com/sdk) available for compute.rhino3d.com.
  3. Download the [Compute Samples repo from GitHub](https://github.com/mcneel/compute.rhino3d.samples).
  4. The libraries are still very new and changing rapidly. Give them a try or get involved. Ask any questions or share what you are working on the [Compute Discussion Forum](https://discourse.mcneel.com/c/serengeti/compute-rhino3d)

* * *

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/compute/compute-
python-getting-started/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/compute/compute-
python-getting-started/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

