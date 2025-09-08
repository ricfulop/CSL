---
url: https://developer.rhino3d.com/samples/rhinoscript/batch-render/
scraped_at: 2025-09-08T15:50:06.223697
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

Batch Render

__

Windows only

Demonstrates how to recurse through a folder and render every Rhino file using
RhinoScript.

VBScript

    
    
    Option Explicit
    
    ' Run the subroutine
    Call BatchRender
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' BatchRender
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub BatchRender()
    
      ' Allow the user to interactively pick a folder
      Dim sFolder
      sFolder = Rhino.BrowseForFolder(, "Select folder to process", "Batch Render" )
      If VarType( sFolder ) <> vbString Then Exit Sub
    
      ' Create a file system object
      Dim oFSO
      Set oFSO = CreateObject( "Scripting.FileSystemObject" )
    
      ' Get a folder object based on the selected folder
      Dim oFolder
      Set oFolder = oFSO.GetFolder( sFolder )
    
      ' Process the folder
      RecurseFolder oFolder
    
      ' Open an empty model
      Rhino.Command "_-New _None", 0
    
      ' Release the objects
      Set oFolder = Nothing
      Set oFSO = Nothing
    
    End Sub
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' RecurseFolder
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub RecurseFolder( oFolder )
    
      ' Process each file in the folder
      Dim oFile
      For Each oFile In oFolder.Files
        ProcessFile oFile.Path
      Next
    
      ' Remark out the following lines if you do not want
      ' to recursively process the folder
    
      ' Process each subfolder in this folder
      Dim oSubFolder
      For Each oSubFolder In oFolder.SubFolders
        RecurseFolder( oSubFolder )
      Next
    
    End Sub
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' ProcessFile
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub ProcessFile( sFile )
    
      ' Once we have gotten here, we have a valid file name.
      ' In this case, we are interested in just 3DM files.
    
      Dim sBitmap
      If (InStr(LCase(sFile), ".3dm") > 0) Then
        sBitmap = Replace(sFile, ".3dm", ".jpg", 1, -1, 1)
        Rhino.DocumentModified False
        Rhino.Command "_-Open " & Chr(34) & sFile & Chr(34), 0
        Rhino.Command "_-Render", 0
        Rhino.Command "_-SaveRenderWindowAs " & Chr(34) & sBitmap & Chr(34), 0
        Rhino.Command "_-CloseRenderWindow", 0
        Rhino.DocumentModified False
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

