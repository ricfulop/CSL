---
url: https://developer.rhino3d.com/guides/rhinoscript/vbscript-string-literals/
scraped_at: 2025-09-08T15:42:09.227698
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

[VBScript String
Literals](https://developer.rhino3d.com/guides/rhinoscript/vbscript-string-
literals/)

  * Overview

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

VBScript String Literals

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

In VBScript, you enclose strings with double quote characters, and you use the
ampersand (`&`) operator to concatenate strings. For example:

    
    
    Dim s
    s = "Hello"
    s = "Hello" & " Rhino!"
    

What if you want to assign `"Hello Rhino!"` (including the quotes) to the
variables? In VBScript, you can use two double quote characters to include a
double quote character in the string. For example:

    
    
    Dim s
    s = "Hello Rhino!"
    

Alternatively you can use the `Chr(34)` construct:

    
    
    Dim s
    s = Chr(34) & "Hello Rhino" & Chr(34)
    

Or, to make your code more readable, you can write a function…

    
    
    Function Quote(ByVal s)
    	Quote = Null
    	If (VarType(s) = vbString) Then
    		Quote = Chr(34) & CStr(s) & Chr(34)
    End If
    End Function
    
    '...
    
    Dim s
    s = Quote("Hello Rhino!")
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/vbscript-
string-literals/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/vbscript-
string-literals/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

