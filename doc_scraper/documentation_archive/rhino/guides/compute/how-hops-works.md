---
url: https://developer.rhino3d.com/guides/compute/how-hops-works/
scraped_at: 2025-09-08T15:43:25.560193
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

[How Hops Works](https://developer.rhino3d.com/guides/compute/how-hops-works/)

  * Quick Links

[Guides](https://developer.rhino3d.com/en/guides/) / [Compute
Guides](https://developer.rhino3d.com/en/guides/compute/) /

How Hops Works

by [Andy Payne](https://discourse.mcneel.com/u/andypayne/) (Last updated:
Friday, February 18, 2022)

The communication process between Hops and a Hops compliant server is a little
more nuanced than simply sending and receiving a single http request and
response. The first step in the process occurs when Hops bundles up the
referenced Grasshopper definition and sends a http request to an endpoint on
the server.

An endpoint is a URL address where the server can be reached to perform a
certain function. In this request, the server opens the Grasshopper definition
sent from Hops and determines what information will be needed to populate the
inputs and outputs for the Hops component. So, the endpoint will be called
`/io` (short for Input Output).

![https://developer.rhino3d.com/images/hops_io_request.png](https://developer.rhino3d.com/images/hops_io_request.png)

The Hops component should now have enough information to create the necessary
inputs and output nodes for itself.

![https://developer.rhino3d.com/images/hops_get_inputs.png](https://developer.rhino3d.com/images/hops_get_inputs.png)

When all of the Hops inputs have been connected to source parameters, it will
then send another http request to the server - only this time it will it will
send the request to the `/solve` endpoint. The Grasshopper definition does not
need to be resent since it was stored on the server during the `/io` process.
Instead, the data sent in the `/solve` request only contains a pointer ID
which tells the server where to find the correct file and all of the input
data.

The http response from the server contains all data which would be returned
from running the Grasshopper file in the traditional manner.

![https://developer.rhino3d.com/images/hops_return_results.png](https://developer.rhino3d.com/images/hops_return_results.png)

To have a better understanding of how each step above works, you can export
the last http request and response for both the `/io` and `/solve` endpoints
directly from the Hops component.

![https://developer.rhino3d.com/images/hops_export_requests.png](https://developer.rhino3d.com/images/hops_export_requests.png)

* * *

## Quick Links

  * [What is Hops](../what-is-hops)
  * [The Hops Component](../hops-component)
  * [Setting up a Production Environment](../deploy-to-iis)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/compute/how-
hops-works/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/compute/how-
hops-works/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

