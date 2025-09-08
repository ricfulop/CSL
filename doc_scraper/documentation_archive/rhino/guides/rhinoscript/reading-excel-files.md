---
url: https://developer.rhino3d.com/guides/rhinoscript/reading-excel-files/
scraped_at: 2025-09-08T15:42:57.317282
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

[Reading Excel
Files](https://developer.rhino3d.com/guides/rhinoscript/reading-excel-files/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Reading Excel Files

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to read a Microsoft Excel file from RhinoScript into an array
that can be accessed in Rhino.

## Solution

The following general purpose function will read an Excel worksheet into a
two-dimensional array…

    
    
    ' Description:
    '   Reads a Microsoft Excel file.
    ' Parameters:
    '   strFile - [in] The name of the Excel file to read.
    ' Returns:
    '   A two-dimension array of cell values, if successful.
    '   Null on error
    Option Explicit
    
    Function ReadExcelFile(ByVal strFile)
    
      ' Local variable declarations
      Dim objExcel, objSheet, objCells
      Dim nUsedRows, nUsedCols, nTop, nLeft, nRow, nCol
      Dim arrSheet()
    
      ' Default return value
      ReadExcelFile = Null
    
      ' Create the Excel object
      On Error Resume Next
      Set objExcel = CreateObject("Excel.Application")
      If (Err.Number <> 0) Then
        Exit Function
      End If
    
      ' Don't display any alert messages
      objExcel.DisplayAlerts = 0  
    
      ' Open the document as read-only
      On Error Resume Next
      Call objExcel.Workbooks.Open(strFile, False, True)
      If (Err.Number <> 0) Then
        Exit Function
      End If
    
      ' If you wanted to read all sheets, you could call
      ' objExcel.Worksheets.Count to get the number of sheets
      ' and the loop through each one. But in this example, we
      ' will just read the first sheet.
      Set objSheet = objExcel.ActiveWorkbook.Worksheets(1)
    
      ' Get the number of used rows
      nUsedRows = objSheet.UsedRange.Rows.Count
    
      ' Get the number of used columns
      nUsedCols = objSheet.UsedRange.Columns.Count
    
      ' Get the topmost row that has data
      nTop = objSheet.UsedRange.Row
    
      ' Get leftmost column that has data
      nLeft = objSheet.UsedRange.Column
    
      ' Get the used cells
      Set objCells = objSheet.Cells
    
      ' Dimension the sheet array
      ReDim arrSheet(nUsedRows - 1, nUsedCols - 1)
    
      ' Loop through each row
      For nRow = 0 To (nUsedRows - 1)
        ' Loop through each column
        For nCol = 0 To (nUsedCols - 1)
      ' Add the cell value to the sheet array
      arrSheet(nRow, nCol) = objCells(nRow + nTop, nCol + nLeft).Value
        Next
      Next
    
      ' Close the workbook without saving
      Call objExcel.ActiveWorkbook.Close(False)
    
      ' Quit Excel
      objExcel.Application.Quit
    
      ' Return the sheet data to the caller
      ReadExcelFile = arrSheet
    
    End Function
    

You can use this function to dump the contents of a spreadsheet to Rhino’s
command line:

    
    
    Sub ExcelDumper()
    
      ' Local variable declarations
      Dim strFile, arrSheet, i, j, varCell, strFormat
    
      ' Prompt for the Excel file to read  
      strFile = Rhino.OpenFileName("Open", "Excel Files (*.xls)|*.xls|")
      If IsNull(strFile) Then Exit Sub
    
      ' Read the Excel file
      arrSheet = ReadExcelFile(strFile)
      If IsNull(arrSheet) Then Exit Sub
    
      ' Dump the worksheet to the command line
      For i = 0 To UBound(arrSheet, 1)
        For j = 0 To UBound(arrSheet, 2)
          strFormat = "Sheet(" & CStr(i) & "," & CStr(j) & ") = "      
          varCell = arrSheet(i, j)
          If IsEmpty(varCell) Then
            Rhino.Print strFormat & "<empty>"
          Else
            Rhino.Print strFormat & CStr(varCell)
          End If      
        Next
      Next
    
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/reading-
excel-files/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/reading-
excel-files/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

