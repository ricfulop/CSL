---
url: https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-overview/
scraped_at: 2025-09-08T15:36:56.918563
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

[Creating Plugins that use Cloud
Zoo](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-
overview/)

  * Overview
  * Required Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Creating Plugins that use Cloud Zoo

by [Andrés Jacobo (AJ) González](https://discourse.mcneel.com/u/aj1/) (Last
updated: Thursday, June 20, 2019)

## Overview

Add Cloud Zoo support to your Plug-In by following the steps below. Cloud Zoo
allows Rhino users to add their license keys to their personal Rhino account
or to a team composed of multiple Rhino accounts. The users may then login
from any computer that has Rhino installed and run Rhino. Cloud Zoo enforces
license restrictions by making sure that users can only run concurrently in as
many computers as there are licenses for a specific product. This allows
individual users to run Rhino and other Plug-Ins on any machine. In a team
scenario, members can be anywhere in the world and have access to a license.

Cloud Zoo does not require users to have a constant internet connection—only
an occasional one every couple of weeks. This is possible because Cloud Zoo
employs license lease mechanism wherein a lease–not a license itself–is issued
by Cloud Zoo to a client running Rhino. A lease usually expires within a few
weeks, but a new lease is frequently issued between Rhino and Cloud Zoo while
a client is online. This allows for a buffer of a few weeks in case the
computer is offline for extended periods of time. This design allows Rhino and
other Plug-Ins to run reliably even in environments with poor internet
connections. Cloud Zoo can also void a lease at any point in time. For
example, when a license is removed by a user or by the developer (Such as when
a customer returns a license for a refund), Cloud Zoo immediately voids all
related leases, effectively ending the user’s ability to use the software the
license is intended for.

Under certain scenarios, such as when adding or removing a license, Cloud Zoo
will contact your server to make sure you allow such operations to succeed.
Your server is not required to interact with the license lease process.

![Cloud Zoo Overview](https://developer.rhino3d.com/images/cz-overview.png)

## Required Steps

To have your Plug-In support Cloud Zoo, you must:

  1. [Register as an Issuer in Cloud Zoo.](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-issuer/)
  2. [Add products to Cloud Zoo.](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-add-products/)
  3. [Implement the required HTTPS callbacks.](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-implement-http-callbacks/)
  4. [Modify Plug-In licensing code to support Cloud Zoo.](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-modify-plugin-licensing-code/)
  5. (_Optional_) [Take advantage of Cloud Zoo endpoints for querying and modifying licenses in Cloud Zoo.](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-optional-endpoints/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/cloudzoo/cloudzoo-
overview/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/cloudzoo/cloudzoo-
overview/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

