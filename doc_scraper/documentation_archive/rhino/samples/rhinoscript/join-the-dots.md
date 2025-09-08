---
url: https://developer.rhino3d.com/samples/rhinoscript/join-the-dots/
scraped_at: 2025-09-08T15:50:20.227400
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

Join the Dots

__

Windows only

Demonstrates joining points into polylines in RhinoScript.

VBScript

    
    
    Option Explicit
    'Script written by Steven Janssen
    'Script version Monday, 9 July 2007 5:23:12 PM
    
    Call Main()
    Sub Main()
    	Dim arrPoints, arrPoint1, arrPoint2, arrVirtual, arrClosestPt, arrExtractedCoords
    	Dim arrVecBetweenPts, arrJoin
    	Dim intTolerance, intCurrentDist, intMinDist
    	Dim k, i
    	i = 0
    
    	arrPoint1 = Rhino.GetPoint("Choose starting point")
    	arrPoint2 = Rhino.GetPoint("Choose second point")
    	intTolerance = 2 * rhino.Distance(arrPoint1, arrPoint2)
    	'intTolerance = Rhino.GetReal("Maximum Distance?",intTolerance)
    	arrPoints = Rhino.GetObjects("Select other Points", 1)
    
    	Rhino.EnableRedraw vbFalse
    	Do
    		'add line between Point1 and Point2
    		i = i + 1
    		rhino.Print i
    		rhino.addline arrPoint1, arrPoint2
    
    		'create the virtual point
    		arrVecBetweenPts = rhino.VectorCreate(arrPoint2,arrPoint1)
    		arrVecBetweenPts = rhino.VectorScale(arrVecBetweenPts,2)
    		arrVirtual = rhino.VectorAdd(arrVecBetweenPts,arrPoint1)
    
    		'find closest point to the virtual point by sifting through all the other points
    		intMinDist = 10 * intTolerance 'starting distance
    		For k = 0 To Ubound(arrPoints)
    			arrExtractedCoords = rhino.PointCoordinates(arrPoints(k))
    			If rhino.Pointcompare(arrExtractedCoords,arrPoint2) = vbFalse Then
    
    				intCurrentDist = rhino.Distance(arrExtractedCoords,arrVirtual)
    
    				If intCurrentDist < intMinDist Then
    					intMinDist = intCurrentDist
    					arrClosestPt = arrExtractedCoords
    				End If
    			End If
    		Next
    
    		'adaptive Tolerance
    		'If (2 * intMinDist) > intTolerance Then
    		'	intTolerance = (2 * intMinDist)
    		'End If
    
    		'check if distance is greater than tolerance and exit if it is
    		'rhino.print intMinDist & ", "
    		If intMinDist > intTolerance Then
    			Exit Do
    		End If
    
    		'move the points so that Point2 is Point1 and the newly found point is Point2
    		arrPoint1 = arrPoint2
    		arrPoint2 = arrClosestPt
    
    		'the following prevents endless loops when there are two points close together at the end
    		If rhino.distance(arrPoint1, arrPoint2) < (intTolerance/50) Then
    			Exit Do
    		End If
    
    	Loop
    	Rhino.EnableRedraw vbTrue
    
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

