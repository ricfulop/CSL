---
url: https://developer.rhino3d.com/guides/rhinoscript/quadratic-solver/
scraped_at: 2025-09-08T15:42:54.298629
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

[Quadratic Solver](https://developer.rhino3d.com/guides/rhinoscript/quadratic-
solver/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Quadratic Solver

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

If you are trying to solve quadratic equations like:

$${-b \pm \sqrt{b^2 - 4ac} \over 2a }$$

the results may seem incorrect at times.

## Solution

Most likely, the problem that is that there are floating point rounding
errors. Being that you only get 15 decimal places of accuracy, you can use
them all up if you are dealing with small numbers.

The following algorithm should produce more accurate results:

    
    
    Function QuadraticSolver(a, b, c)
      Dim d, s0, s1
      d = b * b - 4 * a * c
      If d < 0 Then
        ' No real solution
        QuadraticSolver = Null
      Else
        s0 = (-b - Sqr(d)) / (2 * a)
        s1 = (-b + Sqr(d)) / (2 * a)
        If Abs(s0) < Abs(s1) Then s0 = s1
        s1 = c / (a * s0)
        QuadraticSolver = Array(s0,s1)
      End If
    End Function
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/quadratic-
solver/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/quadratic-
solver/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

