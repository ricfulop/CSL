---
url: https://developer.rhino3d.com/samples/rhinoscript/extract-isocurve-intersection-points/
scraped_at: 2025-09-08T15:49:17.000040
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

Extract Isocurve Intersection Points

__

Windows only

Demonstrates how to get the intersection points of a surface's isocurves using
RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' ExtractUVIntersectPts.rvb -- November 2008
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Option Explicit
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    'Extracts surface wireframe curves
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function RhExtractWireframe(sSurface)
    
      Dim aResults
      RhExtractWireframe = Null
    
      Call Rhino.SelectObject(sSurface)
    
      Call Rhino.Command("_-ExtractWireframe", 0)
      aResults = Rhino.LastCreatedObjects
      If IsArray(aResults) Then
        RhExtractWireframe = aResults
        Rhino.UnselectObjects(aResults)
      End If
    
      Call Rhino.UnselectObject(sSurface)
    
    End Function
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    'Intersects curves
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function RhIntersect(aCurves)  
    
      Dim aResults, aPoints(), i
      RhIntersect = Null
    
      Call Rhino.SelectObjects(aCurves)  
    
      Call Rhino.Command("_-Intersect", 0)
      aResults = Rhino.LastCreatedObjects
      If IsArray(aResults) Then
        ReDim aPoints(UBound(aResults))
        For i = 0 To UBound(aResults)
          aPoints(i) = Rhino.PointCoordinates(aResults(i))
        Next
        Call Rhino.DeleteObjects(aResults)
        RhIntersect = aPoints
      End If
    
      Call Rhino.UnselectObjects(aCurves)
    
    End Function  
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' The one and only ExtractUVIntersectPts subroutine    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub ExtractUVIntersectPts
    
      Dim sSurface, aCurves, aPoints, aObjects
    
      sSurface = Rhino.GetObject("Select surface", 24, True)
      If IsNull(sSurface) Then Exit Sub
    
      Call Rhino.EnableRedraw(False)
      aCurves = RhExtractWireframe(sSurface)
      If IsArray(aCurves) Then
        aPoints = RhIntersect(aCurves)
        Call Rhino.DeleteObjects(aCurves)
        If IsArray(aPoints) Then
          aObjects = Rhino.AddPoints(Rhino.CullDuplicatePoints(aPoints))
          Call Rhino.SelectObjects(aObjects)
        End If
      End If
      Call Rhino.EnableRedraw(True)
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "ExtractUVIntersectPts", "_NoEcho _-RunScript (ExtractUVIntersectPts)"
    

  

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

