---
url: https://developer.rhino3d.com/guides/rhinocommon/rhinoaccounts/ra-overview/
scraped_at: 2025-09-08T15:36:51.870698
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

[Interacting with Rhino
Accounts](https://developer.rhino3d.com/guides/rhinocommon/rhinoaccounts/ra-
overview/)

  * Overview
  * Required Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Interacting with Rhino Accounts

by [Andrés Jacobo (AJ) González](https://discourse.mcneel.com/u/aj1/) (Last
updated: Thursday, May 13, 2021)

## Overview

Rhino Accounts is an authentication and authorization system built and
supported by Robert McNeel & Associates. It is built on top of the [OpenID
Connect protocol](https://openid.net/connect/).

As a brief summary, the authentication services of Rhino Accounts enables you,
the developer, to verify an individual’s identity and access (with the user’s
permission) account information such as their name, email addresses, profile
picture, and more. This allows you to tailor your experience for the user or
learn more about who is using your product.

The authorization services are based on OAuth 2 Tokens. A token allows you to
access any services that use Rhino Accounts for authorization, including your
own. For example, your web server might accept certain files to be uploaded
and downloaded from your plugin that sync accross different machines. An
authorization token can be obtained by your plugin and can be presented to
your web server when uploading or downloading files. The web server can check
with Rhino Accounts that the token is valid and the individual it belongs to.

For a more thourough overview of Rhino Accounts, please see the [Rhino
Accounts
Reference](https://docs.google.com/document/d/1-U0FYt6iQAM3UA6Rio4z0sDVXBSdc0kQk5e4zumnKig).

OpenID Connect is built on top of HTTP. Since Rhino Accounts is an OpenID
Connect provider, you can interact with Rhino Accounts using any HTTP client
from .NET, JavaScript, Python, etc. However, making raw HTTP calls to Rhino
Accounts can be tedious. Handling all the possible outcomes can be time
consuming, and future-proofing your code in case the HTTP endpoints change can
be frustrating. More importantly, taking into account all the possible
security considerations to avoid leaking sensisive user data requires a
rigorous review of your code. For all these reasons, we _strongly_ recommend
that you use Rhino’s built in capabilities to interact with Rhino Accounts
described in this guide. It will also greatly simplify your development and
make things easier down the road.

Taking advantage of Rhino Accounts within Rhino is simple, and requires the
following steps to be implemented.

## Required Steps

To take Advantage of Rhino Accounts within Rhino:

  1. [Contact us](mailto:support@mcneel.com) to obtain a unique client id and secret for Rhino Accounts. This will represent your service within the system.
  2. [Call `GetTokensAsync` or `TryGetAuthTokens` to retrieve authentication and authorization tokens](https://developer.rhino3d.com/guides/rhinocommon/rhinoaccounts/ra-example/).
  3. (_Optional_) [Call `RevokeAuthTokenAsync` to invalidate an authorization token when you no longer need it.](https://developer.rhino3d.com/guides/rhinocommon/rhinoaccounts/ra-revoke/).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/rhinoaccounts/ra-
overview/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/rhinoaccounts/ra-
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

