---
url: https://developer.rhino3d.com/samples/rhinoscript/export-points-to-excel/
scraped_at: 2025-09-08T15:50:14.256538
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

Export Points to Excel

__

Windows only

Illustrates RhinoScript code that exports Rhino point coordinates to Microsoft
Excel.

VBScript

    
    
    Sub ExportPointsToExcel()
    
      Const rhPoint = 1
    
      Dim arrPoints
      arrPoints = Rhino.GetObjects("Select points to export", rhPoint, True, True)
      If Not IsArray(arrPoints) Then Exit Sub
    
      Dim objXL
      Set objXL = CreateObject("Excel.Application")
    
      objXL.Visible = True
    
      objXL.WorkBooks.Add
    
      objXL.Columns(1).ColumnWidth = 20
      objXL.Columns(2).ColumnWidth = 20
      objXL.Columns(3).ColumnWidth = 20
    
      objXL.Cells(1, 1).Value = "X"
      objXL.Cells(1, 2).Value = "Y"
      objXL.Cells(1, 3).Value = "Z"
    
      objXL.Range("A1:C1").Select
      objXL.Selection.Font.Bold = True
      objXL.Selection.Interior.ColorIndex = 1
      objXL.Selection.Interior.Pattern = 1 'xlSolid
      objXL.Selection.Font.ColorIndex = 2
    
      objXL.Columns("B:B").Select
      objXL.Selection.HorizontalAlignment = &hFFFFEFDD ' xlLeft
    
      Dim intIndex
      intIndex = 2
    
      Dim strPoint, arrPt
      For Each strPoint In arrPoints
        arrPt = Rhino.PointCoordinates(strPoint)
        objXL.Cells(intIndex, 1).Value = arrPt(0)
        objXL.Cells(intIndex, 2).Value = arrPt(1)
        objXL.Cells(intIndex, 3).Value = arrPt(2)
        intIndex = intIndex + 1
      Next
    
      objXL.UserControl = True
    
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

