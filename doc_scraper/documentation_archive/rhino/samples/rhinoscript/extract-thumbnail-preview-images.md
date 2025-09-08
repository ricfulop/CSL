---
url: https://developer.rhino3d.com/samples/rhinoscript/extract-thumbnail-preview-images/
scraped_at: 2025-09-08T15:50:16.112047
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

Extract Thumbnail Preview Images

__

Windows only

Demonstrates how to extract the thumbnail preview image from .3DM files using
RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' BatchExtractThumbnails.rvb -- October 2008
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Option Explicit
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' BatchExtractThumbnails
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub BatchExtractThumbnails()
    
      ' Allow the user to interactively pick a folder
      Dim sFolder : sFolder = Rhino.WorkingFolder
      sFolder = Rhino.BrowseForFolder(sFolder, "Select folder to process", "Batch Extract Thumbnails" )
      If IsNull(sFolder) Then Exit Sub
    
      ' Create a file system object
      Dim oFSO : Set oFSO = CreateObject("Scripting.FileSystemObject")
    
      ' Get a folder object based on the selected folder
      Dim oFolder : Set oFolder = oFSO.GetFolder(sFolder)
    
      ' Process the entire folder
      Call DoThumbnailExtraction(oFSO, oFolder)
    
      ' Done
      Call Rhino.Print("Done!")  
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' DoThumbnailExtraction
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub DoThumbnailExtraction(oFSO, oFolder)
    
      ' Process all 3dm files in the folder
      Dim oFile, strOpen, strSave
      For Each oFile In oFolder.Files
        If LCase(oFSO.GetExtensionName(oFile.Path)) = "3dm" Then
          strOpen = LCase(oFile.Path)
          strSave = LCase(Replace(strOpen, ".3dm", ".jpg", 1, -1, 1))
          Call Rhino.Print("Processing " & strOpen & "...")
          Call Rhino.ExtractPreviewImage(strSave, strOpen)
        End If
      Next
    
      ' Un-comment the following if you want to recurse this folder
      'Dim oSubFolder
      'For Each oSubFolder In oFolder.SubFolders
      '  Call DoThumbnailExtraction(oFSO, oSubFolder)
      'Next
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "BatchExtractThumbnails", "_NoEcho _-RunScript (BatchExtractThumbnails)"
    

  

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

