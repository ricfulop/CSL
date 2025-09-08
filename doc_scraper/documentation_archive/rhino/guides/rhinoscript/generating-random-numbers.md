---
url: https://developer.rhino3d.com/guides/rhinoscript/generating-random-numbers/
scraped_at: 2025-09-08T15:42:19.288835
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

[Generating Random
Numbers](https://developer.rhino3d.com/guides/rhinoscript/generating-random-
numbers/)

  * Standard VBScript
  * Using .NET
  * Floating Point

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Generating Random Numbers

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Standard VBScript

The following code sample demonstrates how to generate random integers that
fall within a specified range.

First, the standard VBScript method:

    
    
    Sub Test1()
      nLow = 1
      nHigh = 100
      Randomize
      Rhino.Print Int((nHigh - nLow + 1) * Rnd + nLow)
    End Sub
    

**NOTE** : since the `Int` function always rounds down, we add one to the
difference between the limits.

## Using .NET

Now, a little help from the .NET Framework:

    
    
    Sub Test2()
      nLow = 1
      nHigh = 100
      Set objRandom = CreateObject("System.Random")
      Rhino.Print objRandom.Next_2(nLow, nHigh)
    End Sub
    

## Floating Point

If you want a random floating point number that falls within a specified
range, you can use the technique below…

    
    
    Sub Test3()
      dblLow = 10.0
      dblHigh = 50.0
      Randomize
      Rhino.Print Rnd * (dblHigh - dblLow) + dblLow
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/generating-
random-numbers/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/generating-
random-numbers/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

