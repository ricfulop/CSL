---
url: https://developer.rhino3d.com/samples/rhinoscript/export-curve-control-points/
scraped_at: 2025-09-08T15:49:14.865998
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

Export Curve Control Points

__

Windows only

Demonstrates how to export the 3D coordinates of a curve's control points to a
text file using RhinoScript.

VBScript

    
    
    Sub ExportControlPoints()
    
      'Pick a curve object
      Dim strObject
      strObject = Rhino.GetObject("Select curve", 4)
      If IsNull(strObject) Then Exit Sub
    
      ' Get the curve's control points
      Dim arrPoints
      arrPoints = Rhino.CurvePoints(strObject)
      If Not IsArray(arrPoints) Then Exit Sub
    
      ' Prompt the user to specify a file name    
      Dim strFilter, strFileName
      strFilter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*|"
      strFileName = Rhino.SaveFileName("Save Control Points As", strFilter)
      If IsNull(strFileName) Then Exit Sub
    
      ' Get the file system object
      Dim objFSO, objStream
      Set objFSO = CreateObject("Scripting.FileSystemObject")
    
      ' Open a text file to write to
      On Error Resume Next
      Set objStream = objFSO.CreateTextFile(strFileName, True)
      If Err Then
        MsgBox Err.Description
        Exit Sub
      End If
    
      ' Write each point as text to the file
      Dim strPoint, strText
      For Each strPoint In arrPoints
        strText = Rhino.Pt2Str(strPoint)
        objStream.WriteLine(strText)
      Next
    
      ' Close the file
      objStream.Close
    
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

