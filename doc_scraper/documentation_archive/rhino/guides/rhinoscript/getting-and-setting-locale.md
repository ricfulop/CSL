---
url: https://developer.rhino3d.com/guides/rhinoscript/getting-and-setting-locale/
scraped_at: 2025-09-08T15:42:46.404086
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

[Getting & Setting
Locale](https://developer.rhino3d.com/guides/rhinoscript/getting-and-setting-
locale/)

  * Overview
  * Details
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Getting & Setting Locale

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Formatted numbers are locale-sensitive. That is, the way numbers are formatted
differs depending on which region of the world you are in.

Here are a few examples:

Culture | Format  
---|---  
United States | 1,234,567.89  
France | 1 234 567,89  
German | 1.234.567,89  
Switzerland | 1’234’567.89  
  
## Details

VBScript supports the functionality of retrieving and changing the current
locale settings of your computer. The two functions that support this feature
are `GetLocale()` and `SetLocale()`. `GetLocale()` returns the current locale
on the client machine. `SetLocale()` sets the locale to the new specified
locale. These functions can be used accordingly to localize numeric values.

The `SetLocale()` function requires one argument, the LCID, which is a short
string, decimal value, or hex value that uniquely identifies a geographic
locale. The various geographic locales are based upon the user’s language,
country, and culture. For example, the locale “English - United States” can be
designated as either “en-us”, or “1033”, or “0x0409”.

This locale information is used to establish user preferences and formats for
such things as alphabets, currency, dates, keyboard layout, and numbers. A
list of these locales, and their return values, can be found on the [MSDN
Locale ID (LCID) Chart](https://msdn.microsoft.com/en-
us/library/0h88fahh%28v=vs.85%29.aspx).

**NOTE** : If the LCID argument is set to zero, the locale will be set by the
system.

The following examples demonstrates the use of the `SetLocale()` function:

    
    
    Sub TestLocale()
    
      Dim dblValue : dblValue = 1234567.89
    
      Call SetLocale(1033) 'English - United States
      Rhino.Print "English - United States = " & FormatNumber(dblValue)
    
      Call SetLocale(1036) 'French - France
      Rhino.Print "French - France = " & FormatNumber(dblValue)
    
      Call SetLocale(1031) 'German - Germany
      Rhino.Print "German - Germany = " & FormatNumber(dblValue)
    
      Call SetLocale(2055) 'German - Switzerland
      Rhino.Print "German - Switzerland = " & FormatNumber(dblValue)
    
      Call SetLocale(0)
    
    End Sub
    

which outputs:

    
    
    English - United States = 1,234,567.89
    French - France = 1 234 567,89
    German - Germany = 1.234.567,89
    German - Switzerland = 1'234'567.89
    

## Related Topics

  * [Locale ID (LCID) Chart on MSDN](https://msdn.microsoft.com/en-us/library/0h88fahh%28v=vs.85%29.aspx)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/getting-
and-setting-locale/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/getting-
and-setting-locale/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

