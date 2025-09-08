---
url: https://developer.rhino3d.com/samples/rhinoscript/fibonacci-spirals/
scraped_at: 2025-09-08T15:48:58.934849
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

Fibonacci Spirals

__

Windows only

Demonstrates how to create a Fibonacci Spiral with RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' FibonacciSpiral.rvb -- June 2009
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Option Explicit
    
    Call FibonacciSpiral()
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Computes Fibonacci Spiral
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub FibonacciSpiral()
    
      ' Local variables
      Dim steps, scale, plane, xform
      Dim origin, pt0, pt1, pt2, pt3
      Dim n, cmd
    
      ' Get number of Fibonacci numbers to calculate
      steps = Rhino.GetInteger("Number of steps", 10, 1, 50)
      If IsNull(steps) Then Exit Sub
    
      ' Original origin point
      origin = Array(0,0,0)
    
      ' Process every step...
      For n = 1 To steps
    
        ' Compute Fibonacci number using Binet's formula      
        scale = Round(((Sqr(5) + 1) / 2) ^ n / Sqr(5))
    
        ' Determine x and y axes based on where we are
        plane = Rhino.WorldXYPlane()
        xform = Rhino.XformRotation(90.0 * (n Mod 4), plane(3), plane(0))
        plane = Rhino.PlaneTransform(plane, xform)
    
        ' Calculate arc points
        pt0 = origin
        ' Offset pt0 in the xaxis direction by scale
        pt1 = Rhino.PointAdd(pt0, Rhino.VectorScale(plane(1), scale))
        ' Offset pt1 in the yaxis direction by scale
        pt2 = Rhino.PointAdd(pt1, Rhino.VectorScale(plane(2), scale))
        ' Offset origin in the yaxis direction by scale
        pt3 = Rhino.PointAdd(pt0, Rhino.VectorScale(plane(2), scale))
    
        ' Add a closed polyline
        Call Rhino.AddPolyline(Array(pt0, pt1, pt2, pt3, pt0))
    
        ' Build a command script that will create an arc from
        ' start, end, and direction
        cmd = "_-Arc _StartPoint " & _
              Rhino.Pt2Str(pt0)    & _
              " "                  & _
              Rhino.Pt2Str(pt2)    & _
              " _Direction "       & _
              Rhino.Pt2Str(pt1)
    
        ' Run the command script to create the arc          
        Call Rhino.Command(cmd, 0)
    
        ' Update the origin point
        origin = pt2
    
      Next
    
    End Sub
    

  

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

