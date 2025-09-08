---
url: https://developer.rhino3d.com/samples/rhinoscript/airfoil-shapes/
scraped_at: 2025-09-08T15:50:03.205464
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

Airfoil Shapes

__

Windows only

How to read point files that describe airfoils and create interpolated curves
using RhinoScript.

VBScript

    
    
    Option Explicit
    
    ' Subroutine to import "Selig" formatted airfoil shapes
    Sub ImportAirfoil
    
      ' Local constants
      Const ForReading = 1
    
      ' Local variables
      Dim objFSO, objFile
      Dim strFileName, strAirfoil, strLine, strCurve
      Dim arrPt, arrPoints(), nCount
    
      ' Prompt for an airfoil data file
      strFileName = Rhino.OpenFileName("Open", "Airfoil Data File (*.dat)|*.dat|")
      If IsNull(strFileName) Then Exit Sub
    
      ' Create a file system object
      Set objFSO = CreateObject("Scripting.FileSystemObject")
    
      ' Open the data file for reading
      On Error Resume Next
      Set objFile = objFSO.OpenTextFile(strFileName, ForReading)
      If Err Then
        MsgBox Err.Description
        Exit Sub
      End If  
    
      ' Read the name of the airfoil
      strAirfoil = objFile.ReadLine
    
      ' Read through the file looking for point coordinates
      nCount = 0
      Do While objFile.AtEndOfStream <> True
        strLine = objFile.ReadLine
        ' Convert the string to a point
        arrPt = PointFromString(strLine)
        If IsArray(arrPt) Then
          ReDim Preserve arrPoints(nCount)
          arrPoints(nCount) = arrPt
          nCount = nCount + 1
        End If
      Loop
    
      ' Close the curve
      ReDim Preserve arrPoints(nCount)
      arrPoints(nCount) = arrPoints(0)
    
      ' Add the named interpolated curve
      If IsArray(arrPoints) Then
        strCurve = Rhino.AddInterpCurveEx(arrPoints)
        Rhino.ObjectName strCurve, strAirfoil
      End If
    
      ' Close the file and release objects
      objFile.Close
      Set objFile = Nothing
      Set objFSO = Nothing
    
    End Sub
    
    ' Function to generate a point from a string
    Function PointFromString( strLine )
      Dim arrTokens, arrPoint, x, y
      PointFromString = Null
      If VarType(strLine) = vbString Then
        strLine = Trim(strLine)
        arrTokens = Rhino.StrTok(strLine, " ")
        If IsArray(arrTokens) And UBound(arrTokens) = 1 Then
          x = CDbl(arrTokens(0))
          y = CDbl(arrTokens(1))
          arrPoint = Array(x, y, 0.0)
          PointFromString = arrPoint
        End If
      End If
    End Function
    

  

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

