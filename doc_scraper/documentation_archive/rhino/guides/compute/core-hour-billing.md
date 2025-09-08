---
url: https://developer.rhino3d.com/guides/compute/core-hour-billing/
scraped_at: 2025-09-08T15:43:19.524595
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

[Licensing & Billing](https://developer.rhino3d.com/guides/compute/core-hour-
billing/)

  * About Core-Hour Billing
  * Setting Up Core-Hour Billing
  * Using Core-Hour Billing
  * Single-Computer licensing Not Supported

[Guides](https://developer.rhino3d.com/en/guides/) / [Compute
Guides](https://developer.rhino3d.com/en/guides/compute/) /

Licensing & Billing

__

Windows only

by [Brian Gillespie](https://discourse.mcneel.com/u/brian/) (Last updated:
Monday, October 7, 2024)

## About Core-Hour Billing

When Rhino is logged in to a service account and is running on a Windows
Server-based operating system, you will be billed **$0.10 per core per hour**
that Rhino is running (pro-rated per minute).

_**Example 1:** Rhino running on a 32-core server for one hour:_

  * 1 computer * 32-cores * 1 hour * $0.10/core-hour = $3.20

_**Example 2:** Rhino running on 200 4-core servers for 6 minutes:_

  * 200 computers * 4 cores * 0.1 hour * $0.10/core-hour = $8.00

_**Example 3:** 1 Rhino instance running on a 2-core server 8 hours a day for
30 days:_

  * 1 computer * 2 cores * 8 hours/day * 30 days/month * $0.10/core-hour = $48/month

_**Example 4:** 10 Rhino instances running on a 2-core server 8 hours a day
for 30 days:_

  * 1 computer * 2 cores * 8 hours/day * 30 days/month * $0.10/core-hour = $48/month
  * (Notice that the number of instances of Rhino does not affect your bill)

**Billing is based on uptime** , not on usage - we don’t track the activity of
each core, just that you have one running with Rhino. You can scale your
workloads up and down to optimize performance and cost to you.

**Multiple instances are allowed** \- you may run as many instances of Rhino
on the same machine as you want, and the cost will be the same as running one
instance.

## Setting Up Core-Hour Billing

Core-hour billing is required when running Rhino on a Windows Server-based
operating system.

  1. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) (login to your Rhino account if prompted).

  2. Click _Create New Team_ and create a team to use for your compute project. 

__Note __

Creating a new team is not strictly required, but core-hour billing is _not
compatible_ with existing licenses in the team. So if your team has licenses
in it, core-hour billing will not be allowed.

  3. Click _Manage Team_ -> _Manage Core-Hour Billing_.

  4. Check the checkbox next to the products you want to enable.   
**Note, if you’ve had a team running for years, you may need to enable newer
versions of Rhino.**

  5. Click _Save_ , and enter payment information when prompted for your new team.

## Using Core-Hour Billing

  1. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) and select the team that you just set up with Core-hour billing.

  2. Click _Manage Team_ -> _Manage Core-Hour Billing_.

  3. Click _Action_ -> _Get Auth Token_ to get a token.

  4. Create a new environment variable with the name `RHINO_TOKEN` and use the token as the value. Since the token is too long for Windows’ Environment Variables dialog, it’s easiest to do this via a PowerShell command.
         
         [System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'your token here', 'Machine')
         

From now on, when you start Rhino on this machine it will use your core-hour
billing team.

__Warning __

**Warning!** This token allows anyone with it to charge your team at will. Do
**NOT** share this token with anyone.

## Single-Computer licensing Not Supported

When running on Windows Server, it is not possible to enter a license key to
run as a single-computer license, as Rhino requires a license per core.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/compute/core-
hour-billing/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/compute/core-
hour-billing/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

