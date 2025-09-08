---
url: https://developer.rhino3d.com/guides/rhinoscript/byref-vs-byval/
scraped_at: 2025-09-08T15:42:11.150169
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

[ByRef vs ByVal](https://developer.rhino3d.com/guides/rhinoscript/byref-vs-
byval/)

  * Overview
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

ByRef vs ByVal

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

There has always been confusion about what exactly `ByRef` and `ByVal` mean in
VBScript. The confusion arises because VBScript uses “by reference” to mean
two similar, but different things. VBScript supports:

  1. Reference types
  2. Variable references

The best way to illustrate the difference is with an example. Consider this
class:

    
    
    Class Foo
      Public Bar
    End Class
    

Now we can create an instance of this class:

    
    
    Dim Blah, Baz
    Set Blah = New Foo
    Set Baz = Blah
    Blah.Bar = 123
    

Both `Blah` and `Baz` are references to the same object. The fourth line
changes both `Blah.Bar` and `Baz.Bar` because these are different names for
the same thing.

That’s the “reference type” feature. We say that VBScript treats objects as
reference types.

Now consider this little program:

    
    
    Sub Change(ByRef XYZ)
      XYZ = 5
    End Sub
    Dim ABC
    ABC = 123
    Change ABC
    

This passes a reference to variable `ABC`. The local variable `XYZ` becomes an
alias for `ABC`, so the assignment `XYZ = 5` changes `ABC` as well.

## Related Topics

  * [Parentheses](https://developer.rhino3d.com/guides/rhinoscript/parentheses/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/byref-
vs-byval/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/byref-
vs-byval/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

