---
url: https://developer.rhino3d.com/samples/rhinoscript/create-square-pipes/
scraped_at: 2025-09-08T15:48:56.887054
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

Create Square Pipes

__

Windows only

Demonstrates how to create square pipes using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub SquarePipe
    
    	' Declare local variables
    	Dim arrCrvs, strCrv, dblLength
    	Dim arrStart, dblParam, arrPlane
    	Dim x0, x1, y0, y1, arrX, arrY
    	Dim arrPoints(4), strSqr
    
    	' Pick the input, or path, curves
    	arrCrvs = Rhino.GetObjects("Select curves", 4)
    	If IsNull(strCrv) Then Exit Sub
    
    	' Specify the lengths of the sides of the square    
    	dblLength = Rhino.GetReal("Length of sides", 1.0, 0.0)
    	If Not IsNumeric(dblLength) Or dblLength <= 0 Then Exit Sub
    
    	Call Rhino.EnableRedraw(False)
    
    	For Each strCrv In arrCrvs
    
    		' Determine the curve's starting point    
    		arrStart = Rhino.CurveStartPoint(strCrv)
    
    		' Determine the parameter at the starting point  
    		dblParam = Rhino.CurveClosestPoint(strCrv, arrStart)
    
    		' Detemine the curve's perpendicular plane at its starting point.
    		' We can use this plane to cook up the coordinates of the square.
    		arrPlane = Rhino.CurvePerpFrame(strCrv, dblParam)
    
    		' Scale the vectors based on the user input
    		arrX = Rhino.VectorScale(arrPlane(1), dblLength * 0.5)
    		arrY = Rhino.VectorScale(arrPlane(2), dblLength * 0.5)
    
    		' Cook up some temporary points
    		x0 = Rhino.PointAdd(arrStart, arrX)
    		x1 = Rhino.PointAdd(arrStart, Rhino.VectorReverse(arrX))
    		y0 = Rhino.PointAdd(arrStart, arrY)
    		y1 = Rhino.PointAdd(arrStart, Rhino.VectorReverse(arrY))
    
    		' Define the points of the square  
    		arrPoints(0) = Rhino.PointAdd(x0, Rhino.VectorReverse(arrY))
    		arrPoints(1) = Rhino.PointAdd(y1, Rhino.VectorReverse(arrX))
    		arrPoints(2) = Rhino.PointAdd(x1, arrY)
    		arrPoints(3) = Rhino.PointAdd(y0, arrX)
    		arrPoints(4) = arrPoints(0)
    
    		' Create the square
    		strSqr = Rhino.AddPolyline(arrPoints)
    
    		' Extrude the polyline along the input curve
    		Call Rhino.ExtrudeCurve(strSqr, strCrv)
    
    		' Delete polyline
    		Call Rhino.DeleteObject(strSqr)
    
    	Next
    
    	Call Rhino.EnableRedraw(True)
    
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

