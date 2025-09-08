---
url: https://developer.rhino3d.com/guides/cpp/do-not-test-for-equality/
scraped_at: 2025-09-08T15:40:45.906185
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

[Do NOT Test for Equality](https://developer.rhino3d.com/guides/cpp/do-not-
test-for-equality/)

  * A Warning

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Do NOT Test for Equality

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## A Warning

You almost never want to write code like the following:

    
    
    double x;
    double y;
    ...
    if (x == y) {...}
    

Most floating point operations involve at least a tiny loss of precision and
so even if two numbers are equal for all practical purposes, they may not be
exactly equal down to the last bit, and so the equality test is likely to
fail. For example, the following code snippet prints `-1.778636e-015`.
Although in theory, squaring should undo a square root, the round-trip
operation is slightly inaccurate.

    
    
    double x = 10;
    double y = sqrt(x);
    y *= y;
    if (x == y)
      RhinoApp().Print(L"Square root is exact\n");
    else
      RhinoApp().Print(L"%f\n", x-y);
    

In most cases, the equality test above should be written as something like the
following:

    
    
    double tolerance = ...
    if (fabs(x - y) < tolerance) {...}
    

Here, `tolerance` is some threshold that defines what is “close enough” for
equality. This begs the question of: how close is close enough? This cannot be
answered in the abstract; you have to know something about your particular
problem to know how close is close enough in your context.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/do-
not-test-for-equality/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/do-
not-test-for-equality/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

