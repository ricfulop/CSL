---
url: https://developer.rhino3d.com/guides/rhinoscript/archimedian-spirals/
scraped_at: 2025-09-08T15:42:33.383980
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

[Archimedean
Spirals](https://developer.rhino3d.com/guides/rhinoscript/archimedian-
spirals/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Archimedean Spirals

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

It is possible to define an Archimedean Spiral with polar coordinates. In
polar coordinates $$(r, θ)$$, an Archimedean Spiral can be described by the
following equation:

$$r = a+bθ$$

with real numbers $$a$$ and $$b$$. Changing the parameter a will turn the
spiral, while $$b$$ controls the distance between successive turnings…

![Archimedean Spiral](https://developer.rhino3d.com/images/archimedean-
spirals-01.png)

## Sample

Once the polar coordinates have been calculated, we can use RhinoScript’s
`Polar` method to convert them to Cartesian coordinates, which will allow us
to plot the curve using RhinoScript’s `AddInterpCurve` method.

The following sample script code demonstrates how to create an interpolated
curve through the points that were calculated using the above equation…

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
     ' ArchimedeanSpiral.rvb -- June 2008
     ' If this code works, it was written by Dale Fugier.
     ' If not, I don't know who wrote it.
     ' Works with Rhino 4.0.
    
     Option Explicit
    
     Sub ArchimedeanSpiral()
    
       Dim a_const, b_const, step_angle, num_points
       Dim curr_angle, base_point, radius, points(), i
    
       Rhino.Print "Archimedean Spiral (r = a + bθ)"
    
       a_const = Rhino.GetReal("Value of 'A' constant", 1.0, 0.01)
       If IsNull(a_const) Then Exit Sub
    
       b_const = Rhino.GetReal("Value of 'B' constant", 1.0, 0.01)
       If IsNull(a_const) Then Exit Sub
    
       num_points = Rhino.GetInteger("Number of points to calculate", 10, 2)
       If IsNull(num_points) Then Exit Sub
    
       step_angle = Rhino.GetReal("Angle between points", 30.0, 1.0, 45.0)
       If IsNull(step_angle) Then Exit Sub
    
       curr_angle = 0.0
       base_point = Array(0.0, 0.0, 0.0)
       ReDim points(num_points - 1)
    
       For i = 0 To UBound(points)
         radius = a_const + (b_const * curr_angle)
         points(i) = Rhino.Polar(base_point, radius, curr_angle)
         curr_angle = curr_angle + step_angle
       Next
    
       Rhino.AddInterpCurve points
       'Rhino.AddPoints points
    
     End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/archimedian-
spirals/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/archimedian-
spirals/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

