---
url: https://developer.rhino3d.com/guides/rhinoscript/importing-points-from-txt-files/
scraped_at: 2025-09-08T15:42:48.404059
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

[Importing Points from Text
Files](https://developer.rhino3d.com/guides/rhinoscript/importing-points-from-
txt-files/)

  * Overview
  * Example
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Importing Points from Text Files

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

One common task performed by Rhino users is the importing of point coordinates
from some kind of delimited file. This task is easy if you use the Points File
file type when opening or importing files. But what if the file you are
importing does not conform to the traditional delimited file notation. Or,
what if the file contains other information?

The key to understanding how to import data from a text is understanding the
File System Object included as part of the Microsoft Scripting Runtime. The
File System Object simplifies the task of dealing with any type of file input
or output and for dealing with the system file structure itself.

To access the File System Object model you must first create an instance of
the `FileSystemObject` object, the only externally creatable object in the
model. For more information on the `FileSystemObject`, see [Microsoft’s
VBScript documentation on MSDN](https://msdn.microsoft.com/en-
us/library/2z9ffy99%28v=vs.84%29.aspx).

## Example

The following code example demonstrates how to import point coordinates from a
text file. This can be easily modified to accommodate other information…

    
    
    Option Explicit
    '---------------------------------------------------------------
    ' Subroutine: ImportPoints
    ' Purpose:    Import points from a text file.
    '---------------------------------------------------------------
    Sub ImportPoints
      ' Prompt the user for a file to import
      Dim strFilter, strFileName
      strFilter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*|"
      strFileName = Rhino.OpenFileName("Open Point File", strFilter)
      If IsNull(strFileName) Then Exit Sub
    
      ' The the file system object
      Dim objFSO, objFile
      Set objFSO = CreateObject("Scripting.FileSystemObject")
      ' Try opening the text file
      On Error Resume Next
      Set objFile = objFSO.OpenTextFile(strFileName, 1)
      If Err Then
        MsgBox Err.Description
        Exit Sub
      End If
    
      Rhino.EnableRedraw False
    
      ' Read each line from the file
      Dim strLine, arrPoint
      Do While objFile.AtEndOfStream <> True
        strLine = objFile.ReadLine
        If Not IsNull(strLine) Then
          ' Remove any double-quote characters
          strLine = Replace(strLine, Chr(34), , 1)
          ' Convert the string to a 3D point
          arrPoint = Rhino.Str2Pt(strLine)
          ' Add the point to Rhino
          If IsArray(arrPoint) Then
            ' AddPoint will add a point object to Rhino
            Rhino.AddPoint arrPoint
          End If
        End If
      Loop
    
      Rhino.EnableRedraw True
      objFile.Close
      Set objFile = Nothing
      Set objFSO = Nothing
    End Sub
    

## Related Topics

  * [Microsoft’s VBScript documentation on MSDN](https://msdn.microsoft.com/en-us/library/2z9ffy99%28v=vs.84%29.aspx)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/importing-
points-from-txt-files/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/importing-
points-from-txt-files/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

