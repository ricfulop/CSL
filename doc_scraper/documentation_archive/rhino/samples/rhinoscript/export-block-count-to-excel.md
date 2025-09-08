---
url: https://developer.rhino3d.com/samples/rhinoscript/export-block-count-to-excel/
scraped_at: 2025-09-08T15:49:09.976574
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

Export Block Count to Excel

__

Windows only

Demonstrates how to count blocks and then export the results to Microsoft
Excel.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' ExportBlockCount.rvb -- May 2010
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    
    Option Explicit
    
    Sub ExportBlockCount()
    
      Dim arrBlocks, strBlock, strName
      Dim objCounts, objKey
      Dim objExcel, objBook, objSheet, nCell
    
      ' Get all of the block instances in the document
      arrBlocks = Rhino.ObjectsByType(4096)
      If IsNull(arrBlocks) Then
        Call Rhino.Print("No blocks to export.")
        Exit Sub
      End If
    
      ' Create a dictionary object for counting blocks
      Set objCounts = CreateObject("Scripting.Dictionary")
    
      ' Count the blocks
      For Each strBlock In arrBlocks
        strName = Rhino.BlockInstanceName(strBlock)
        If objCounts.Exists(strName) Then
          objCounts(strName) = objCounts(strName) + 1
        Else
          Call objCounts.Add(strName, 1)
        End If
      Next
    
      ' Create a Excel object
      Set objExcel = CreateObject("Excel.Application")
      objExcel.Visible = True
    
      ' Initialize Excel
      Set objBook = objExcel.Workbooks.Add
      Set objSheet = objBook.Worksheets(1)
    
      ' Place titles on sheet
      nCell = 1
      objExcel.Cells(nCell, 1).Value = "Block Name"
      objExcel.Cells(nCell, 2).Value = "Count"
      nCell = nCell + 1
    
      ' Write the blocks and counts to the sheet
      Call Rhino.Print("Block counts:")
      For Each objKey In objCounts
        objExcel.Cells(nCell, 1).Value = CStr(objKey)
        objExcel.Cells(nCell, 2).Value = CStr(objCounts(objKey))
        ' Print to command line too
        Call Rhino.Print("  " & CStr(objKey) & " = " & CStr(objCounts(objKey)))
       nCell = nCell + 1
      Next
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Drag & drop and alias creation stuff
    Rhino.AddStartUpScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "ExportBlockCount", "_-RunScript (ExportBlockCount)"
    

  

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

