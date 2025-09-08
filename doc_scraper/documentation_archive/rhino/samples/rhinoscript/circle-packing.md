---
url: https://developer.rhino3d.com/samples/rhinoscript/circle-packing/
scraped_at: 2025-09-08T15:50:09.196991
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

Circle Packing

__

Windows only

Multi-radius circle packing algorithm in RhinoScript.

VBScript

    
    
    Option Explicit
    'Script written by Steven Janssen
    'Script copyrighted by Steven Janssen
    'Script version Sunday, 18 May 2008 11:34:18 AM
    
    Call Main()
    Sub Main()
    	Dim arrPoint(), arrRadius(), intCircleNumber, arrInputR, arrSide(2)
    	Dim strCurrentCircleID, R, intCurrentCentre, k
    	Dim dblCosA, dblRotA
    	Dim checkdistanceA, checkdistanceB, checkloop, marker, intHole
    
    	'Get Input Circles
    	arrInputR = Rhino.GetObjects("Select Circles", 4)
    	If Not IsArray(arrInputR) Then
    		Exit Sub
    	End If
    
    	'Get Radii from Input Circles
    	For R = 0 To Ubound(arrInputR)
    		If Rhino.IsCircle(arrInputR(R)) Then
    			arrInputR(R) = Rhino.CircleRadius(arrInputR(R))
    		End If
    	Next
    
    	intCircleNumber = Rhino.GetInteger("Number of Circles",1000)
    	intCircleNumber = intCircleNumber - 1
    
    	ReDim arrPoint(intCircleNumber)
    	ReDim arrRadius(intCircleNumber)
    
    	'Draw 1st Circle
    	arrRadius(0) = arrInputR(Int(RND*(Ubound(arrInputR)+1)))
    	arrPoint(0) = Rhino.GetPoint("Centre of Circle")
    	If Not IsArray(arrPoint(0)) Then
    		Exit Sub
    	End If
    	strCurrentCircleID = Rhino.AddCircle(Array(arrPoint(0),Array(1,0,0),Array(0,1,0),Array(0,0,1)),arrRadius(0))
    
    	Rhino.EnableRedraw vbFalse
    
    	'Draw 2nd Circle
    	arrRadius(1) = arrInputR(Int(RND*(Ubound(arrInputR)+1)))
    	arrPoint(1) = arrPoint(0)
    	arrPoint(1)(0) = arrPoint(1)(0) + arrRadius(0) + arrRadius(1)
    	strCurrentCircleID = Rhino.AddCircle(Array(arrPoint(1),Array(1,0,0),Array(0,1,0),Array(0,0,1)),arrRadius(1))
    
    	intCurrentCentre = 0
    	intHole = 1
    
    	'Draw other Circles
    	For k = 2 To intCircleNumber
    
    		Rhino.StatusBarMessage k+1 & "/" & intCircleNumber+1
    		arrRadius(k) = arrInputR(Int(RND*(Ubound(arrInputR)+1)))
    
    		Do
    			marker = 0
    
    			'Calculate the lengths of the sides
    			arrSide(0) = Rhino.distance(arrPoint(intCurrentCentre), arrPoint(k-intHole))
    			arrSide(1) = arrRadius(k) + arrRadius(intCurrentCentre)
    			arrSide(2) = arrRadius(k) + arrRadius(k-intHole)
    
    			'Calculate Angle
    			dblCosA = (arrSide(0)^2 + arrSide(1)^2 - arrSide(2)^2) / (2 * arrSide(0) * arrSide(1))
    
    			If dblCosA > 1 Then
    				marker = 1
    			Else
    				dblRotA = Atn(-dblCosA / Sqr((-dblCosA * dblCosA) + 1)) + (2 * Atn(1))
    				dblRotA = Rhino.ToDegrees(dblRotA)
    
    				'Create, rotate and scale Vector
    				arrPoint(k) = Rhino.VectorCreate(arrPoint(k-intHole),arrPoint(intCurrentCentre))
    				arrPoint(k) = Rhino.VectorRotate(arrPoint(k),dblRotA,Array(0,0,1))
    				arrPoint(k) = Rhino.VectorScale(arrPoint(k),(arrSide(1)/arrSide(0)))
    				arrPoint(k) = Rhino.VectorAdd(arrPoint(k),arrPoint(intCurrentCentre))
    
    				'Check if Circle will Intersect with Existing Circles
    				For checkloop = (k-1) To 0 Step -1
    					checkdistanceA = Rhino.distance(arrPoint(k), arrPoint(checkloop)) + 0.001
    					checkdistanceB = (arrRadius(k) + arrRadius(checkloop))
    					If checkdistanceA < checkdistanceB Then
    						marker = 1
    						Exit For
    					End If
    				Next
    				If marker = 0 Then
    					'rhino.AddLine arrPoint(k-intHole), arrPoint(k)
    					strCurrentCircleID = Rhino.AddCircle(Array(arrPoint(k),Array(1,0,0),Array(0,1,0),Array(0,0,1)),arrRadius(k))
    				End If
    			End If
    
    			'Exit the Do Loop if the Circle is Good
    			If marker = 0 Then
    				intHole = 1
    				Exit Do
    			End If
    
    			intCurrentCentre = intCurrentCentre + 1
    
    			If intCurrentCentre = k-intHole Then
    				intHole = intHole + 1
    				intCurrentCentre = 0
    				'If intHole > 2 Then
    				'	rhino.addpoint arrPoint(k-intHole)
    				'End If
    				'rhino.messagebox intHole
    			End If
    
    		Loop
    	Next
    
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

