---
url: https://developer.rhino3d.com/samples/rhinoscript/select-multiple-files/
scraped_at: 2025-09-08T15:50:34.320035
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

Select Multiple Files

__

Windows only

Demonstrates how to use RhinoScript's MultiListBox function to select multiple
files.

VBScript

    
    
    Sub Test
      Dim sFolder
      sFolder = Rhino.BrowseForFolder( , "Select folder with 3DM files" )
      If VarType( sFolder ) <> vbString Then Exit Sub
    
      Dim oFSO
      Set oFSO = CreateObject( "Scripting.FileSystemObject" )
    
      Dim oFolder
      Set oFolder = oFSO.GetFolder( sFolder )
    
      Dim oFile, aFiles(), nCount
      nCount = 0
      For Each oFile In oFolder.Files
        ReDim Preserve aFiles(nCount)
        aFiles(nCount) = oFile.Name
        nCount = nCount + 1
      Next
    
      If nCount = 0 Then
        Rhino.Print "Selected folder contained no 3DM files."
        Exit Sub
      End If
    
      Dim aSelected, sSelected
      aSelected = Rhino.MultiListBox(aFiles, oFolder.Path)
      If IsArray(aSelected) Then
        For Each sSelected In aSelected
          Rhino.Print sSelected
        Next
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

