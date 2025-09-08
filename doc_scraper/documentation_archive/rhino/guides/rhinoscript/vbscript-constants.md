---
url: https://developer.rhino3d.com/guides/rhinoscript/vbscript-constants/
scraped_at: 2025-09-08T15:42:03.384117
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

[VBScript
Constants](https://developer.rhino3d.com/guides/rhinoscript/vbscript-
constants/)

  * Overview
  * Creating Constants
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

VBScript Constants

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

A constant is a meaningful name that takes the place of a number or string and
never changes. VBScript defines a number of intrinsic constants. You can get
information about these intrinsic constants from the VBScript language
reference.

## Creating Constants

You create user-defined constants in VBScript using the `Const` statement.
Using the `Const` statement, you can create string or numeric constants with
meaningful names and assign them literal values. For example:

    
    
    Const MyString = "This is my string."
    Const MyAge = 49
    

Note that the string literal is enclosed in quotation marks (`" "`). Quotation
marks are the most obvious way to differentiate string values from numeric
values. You represent Date literals and time literals by enclosing them in
number signs (`#`). For example:

    
    
    Const CutoffDate = #11-17-2008#
    

You may want to adopt a naming scheme to differentiate constants from
variables. This will prevent you from trying to reassign constant values while
your script is running. For example, you might want to use a “vb” or “con”
prefix on your constant names, or you might name your constants in all capital
letters. Differentiating constants from variables eliminates confusion as you
develop more complex scripts.

## Related Topics

  * [What are VBScript and RhinoScript?](https://developer.rhino3d.com/guides/rhinoscript/what-are-vbscript-rhinoscript/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/vbscript-
constants/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/vbscript-
constants/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

