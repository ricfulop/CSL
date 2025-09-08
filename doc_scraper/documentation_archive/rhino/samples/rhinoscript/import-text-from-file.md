---
url: https://developer.rhino3d.com/samples/rhinoscript/import-text-from-file/
scraped_at: 2025-09-08T15:50:18.207144
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

Import Text from File

__

Windows only

Demonstrates how to import text from a file using RhinoScript.

VBScript

    
    
    Sub ImportText
    
      Const ForReading = 1
      Dim strFile, strText
      Dim objFSO, objFile
      Dim arrOrigin
    
      strFile = Rhino.OpenFileName("Open", "Text Files (*.txt)|*.txt|")
      If IsNull(strFile) Then Exit Sub
    
      arrOrigin = Rhino.GetPoint("Start point")
      If Not IsArray(arrOrigin) Then Exit Sub
    
      Set objFSO = CreateObject("Scripting.FileSystemObject")
    
      On Error Resume Next
      Set objFile = objFSO.OpenTextFile(strFile, ForReading)
      If Err Then
        MsgBox Err.Description
        Exit Sub
      End If
    
      While Not objFile.AtEndOfStream
        strText = strText & objFile.ReadLine
        If Not objFile.AtEndOfStream Then
          strText = strText & VbCrLf
        End If
      Wend
    
      objFile.Close
    
      Set objFile = Nothing
      Set objFSO = Nothing
    
      If Len(strText) > 0 Then
        Rhino.AddText strText, arrOrigin
      End If
    
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

