---
url: https://developer.rhino3d.com/samples/rhinoscript/import-interpolated-curve/
scraped_at: 2025-09-08T15:49:19.002898
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

Import Interpolated Curve

__

Windows only

Demonstrates how to read a point file and create an interpolated curve using
RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub ImportInterpCrv()
    
      Dim strFilter, strFileName
      strFilter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*|"
      strFileName = Rhino.OpenFileName("Open Point File", strFilter)
      If IsNull(strFileName) Then Exit Sub
    
      Dim objFSO, objFile
      Set objFSO = CreateObject("Scripting.FileSystemObject")
    
      On Error Resume Next
      Set objFile = objFSO.OpenTextFile(strFileName, 1)
      If Err Then
        MsgBox Err.Description
        Exit Sub
      End If
    
      Dim strLine, arrPt, arrPoints(), nCount
      nCount = 0  
      Do While objFile.AtEndOfStream <> True
        strLine = objFile.ReadLine
        If Not IsNull(strLine) Then
          strLine = Replace(strLine, Chr(34), , 1)
          arrPt = Rhino.Str2Pt(strLine)
          If IsArray(arrPoint) Then
            ReDim Preserve arrPoints(nCount)
            arrPoints(nCount) = arrPt
            nCount = nCount + 1
          End If
        End If
      Loop
    
      If IsArray(arrPoints) Then
        Rhino.AddInterpCurveEx arrPoints
      End If
    
      objFile.Close
    
      Set objFile = Nothing
      Set objFSO = Nothing
    
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

