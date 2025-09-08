---
url: https://developer.rhino3d.com/guides/rhinocommon/commas-and-periods/#english-culture
scraped_at: 2025-09-08T16:07:33.173808
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

[Commas & Periods](https://developer.rhino3d.com/guides/rhinocommon/commas-
and-periods/)

  * English Culture

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Commas & Periods

by [Steve Baer](https://discourse.mcneel.com/u/stevebaer/) (Last updated:
Wednesday, December 5, 2018)

## English Culture

Depending on the user’s culture settings, their computer may be set up to use
commas instead of periods for decimal separators. This can cause problems when
writing numbers into xml files and reading these xml files on a different
culture setting.

An easy way around this problem is to temporarily adjust the application’s
culture settings when reading/writing files to always use a single culture…

C# VB.NET

    
    
    // save current culture
    System.Globalization.CultureInfo current_culture = System.Threading.Thread.CurrentThread.CurrentCulture;
    
    // create and set english-us culture
    System.Globalization.CultureInfo us_culture = new System.Globalization.CultureInfo("en-us");
    System.Threading.Thread.CurrentThread.CurrentCulture = us_culture;
    
    int rc = WriteMyFile( filename );
    
    // restore the saved culture
    System.Threading.Thread.CurrentThread.CurrentCulture = current_culture;
    
    
    
    ' save current culture
    Dim current_culture As System.Globalization.CultureInfo = System.Threading.Thread.CurrentThread.CurrentCulture
    
    ' create and set english-us culture
    Dim us_culture As new System.Globalization.CultureInfo("en-us")
    System.Threading.Thread.CurrentThread.CurrentCulture = us_culture
    
    Dim rc As Integer = WriteMyFile( filename )
    
    ' restore the saved culture
    System.Threading.Thread.CurrentThread.CurrentCulture = current_culture
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/commas-
and-periods/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/commas-
and-periods/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

