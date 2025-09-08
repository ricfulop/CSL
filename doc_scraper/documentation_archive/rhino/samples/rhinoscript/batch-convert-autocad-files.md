---
url: https://developer.rhino3d.com/samples/rhinoscript/batch-convert-autocad-files/
scraped_at: 2025-09-08T15:50:05.197695
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

Batch Convert AutoCAD Files

__

Windows only

Demonstrates how to convert a folder of AutoCAD files to Rhino 3dm files using
RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' BatchConvertAutoCAD script for Rhinoceros
    ' Robert McNeel & Associates
    ' www.rhino3d.com
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Option Explicit
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' BatchConvertAutoCAD
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub BatchConvertAutoCAD()
    
      ' Make sure RhinoScript does not reinitialize when opening models,
      ' otherwise this script will only process one file.
      Rhino.Command "_-Options _RhinoScript _Reinitialize=_No _Enter _Enter", 0
    
      ' Allow the user to interactively pick a folder
      Dim sFolder
      sFolder = Rhino.BrowseForFolder(, "Select folder to process", "Batch Convert AutoCAD")
      If VarType(sFolder) <> vbString Then Exit Sub
    
      ' Create a file system object
      Dim oFSO
      Set oFSO = CreateObject("Scripting.FileSystemObject")
    
      ' Get a folder object based on the selected folder
      Dim oFolder
      Set oFolder = oFSO.GetFolder(sFolder)
    
      ' Process the folder
      ProcessFolder oFSO, oFolder
    
      ' Release the objects
      Set oFolder = Nothing
      Set oFSO = Nothing
    
      ' Close the last file processed
      Rhino.DocumentModified False
      Rhino.Command "_-New _None", 0
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' ProcessFolder
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub ProcessFolder(oFSO, oFolder)
    
      ' Process all .dwg files in the selected folder
      Dim oFile, strOpen, strSave
      For Each oFile In oFolder.Files
        If LCase(oFSO.GetExtensionName(oFile.Path)) = "dwg" Then
          strOpen = LCase(oFile.Path)
          strSave = LCase(Replace(strOpen, ".dwg", ".3dm", 1, -1, 1))
          ProcessFile strOpen, strSave
        End If
      Next
    
      ' Comment out the following lines if you do not
      ' want to recursively process the selected folder.
      Dim oSubFolder
      For Each oSubFolder In oFolder.SubFolders
        ProcessFolder oFSO, oSubFolder
      Next
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' ProcessFile
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub ProcessFile(strOpen, strSave)
      Rhino.DocumentModified False
      Rhino.Command "_-Open " & Chr(34) & strOpen & Chr(34), 0
      Rhino.Command "_-Zoom _All _Extents", 0
      Rhino.Command "_-SetActiveView _Top", 0
      Rhino.Command "_-Save " & Chr(34) & strSave & Chr(34), 0
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

