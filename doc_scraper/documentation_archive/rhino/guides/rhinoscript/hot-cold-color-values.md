---
url: https://developer.rhino3d.com/guides/rhinoscript/hot-cold-color-values/
scraped_at: 2025-09-08T15:42:47.279340
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

[Hot & Cold Colors](https://developer.rhino3d.com/guides/rhinoscript/hot-cold-
color-values/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Hot & Cold Colors

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

It is often useful to show curvature with a color index. For example, if you
divide a curve into 500 points and measure the curvature at each point, you
can assign a “curvature radius” color to each of the points using RhinoScript.
Let’s take a look at how this is done.

## Solution

One solution you might consider is to determine the minimum and maximum
curvature values for your samples. Then, you can use this function to
calculate a color value for each point.

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Return a RGB color given a scalar v in the range [vmin, vmax].
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function GetHotColdColor(v, vmin, vmax)
    
      Dim r, g, b, dv
      r = 1.0 : g = 1.0 : b = 1.0 'white
    
      If (v < vmin) Then v = vmin
      If (v > vmax) Then v = vmax
      dv = vmax - vmin
    
      If (v < (vmin + 0.25 * dv)) Then
        r = 0
        g = 4 * (v - vmin) / dv
      ElseIf (v < (vmin + 0.5 * dv)) Then
        r = 0
        b = 1 + 4 * (vmin + 0.25 * dv - v) / dv
      ElseIf (v < (vmin + 0.75 * dv)) Then
        r = 4 * (v - vmin - 0.5 * dv) / dv
        b = 0
      Else
        g = 1 + 4 * (vmin + 0.75 * dv - v) / dv
        b = 0
      End If
    
      GetHotColdColor = RGB(Int(r*255), Int(g*255), Int(b*255))
    
    End Function
    

Here is a sample script that you can use to test the above function…

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Test procedure creates a "hot-to-cold" color ramp mesh.
    ' To see the results, set a viewport to "rendered" display.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub TestGetHotColdColor()
    
      ' Mesh with 200 vertices and 100 faces
      Dim v(199), f(99), c(199), ub, i
    
      ' Fill in arrays
      ub = UBound(v)
      For i = 0 To UBound(v) Step 2
        v(i) = Array(i/2,0,0)
        v(i+1) = Array(i/2,10,0)
        c(i) = GetHotColdColor(i,0,ub)
        c(i+1) = c(i)
        f(i/2) = Array(i,i+2,i+3,i+1)
      Next
    
      ' Create the mesh object
      Call Rhino.AddMesh(v,f,,,c)
    
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/hot-
cold-color-values/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/hot-
cold-color-values/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

