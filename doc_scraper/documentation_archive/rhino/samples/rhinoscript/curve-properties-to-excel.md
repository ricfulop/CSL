---
url: https://developer.rhino3d.com/samples/rhinoscript/curve-properties-to-excel/
scraped_at: 2025-09-08T15:49:10.956079
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

Curve Properties to Excel

__

Windows only

Illustrates RhinoScript code that extracts curve properties into Excel.

VBScript

    
    
    Option Explicit
    
    Sub ExtractProperties
    
      ' Declare variables
      Dim xlApp, xlBook, xlSheet  ' Declare variable to hold the reference.
      Dim strObject
      Dim arrObjects
      Dim intCount
      Dim arrStart, arrEnd
    
      'Set Default Values
      intCount = 0
    
      ' Select some objects      
      arrObjects = Rhino.GetObjects("Select objects for extraction",4)
      If Not IsArray(arrObjects) Then Exit Sub
    
      ' Open Excel object
      Set xlApp = CreateObject("excel.application")
       ' You may have to set Visible property to True
       ' if you want to see the application.
      xlApp.Visible = True
       ' Use xlApp to access Microsoft Excel's
       ' other objects.
       Set xlBook = xlApp.Workbooks.Add
       Set xlSheet = xlBook.Worksheets(1)
    
      'Place titles on sheet
          xlApp.Cells(1, 1).Value = "Name"
          xlApp.Cells(1, 2).Value = "Length"
          xlApp.Cells(1,3).Value = "StartX"
          xlApp.Cells(1,4).Value = "StartY"
          xlApp.Cells(1,5).Value = "StartZ"
          xlApp.Cells(1,6).Value = "EndX"
          xlApp.Cells(1,7).Value = "EndY"
          xlApp.Cells(1,8).Value = "EndZ"
    
      'Extract Properties of Curves
      For Each strObject In arrObjects
          'Curves Processed
        If Rhino.IsCurve(strObject) Then
         xlApp.Cells(intCount + 2, 1).Value = Rhino.ObjectName(strObject)
         xlApp.Cells(intCount + 2, 2).Value = Rhino.CurveLength(strObject)
         'Extract StartPoint
         arrStart = Rhino.CurveStartPoint(strObject)
         xlApp.Cells(intCount + 2, 3).Value = arrStart(0)
         xlApp.Cells(intCount + 2, 4).Value = arrStart(1)
         xlApp.Cells(intCount + 2, 5).Value = arrStart(2)
         'Extract EndPoint
         arrEnd = Rhino.CurveEndPoint(strObject)
         xlApp.Cells(intCount + 2, 6).Value = arrEnd(0)
         xlApp.Cells(intCount + 2, 7).Value = arrEnd(1)
         xlApp.Cells(intCount + 2, 8).Value = arrEnd(2)
        End If
        intCount = intCount + 1
      Next
    
    'xlApp.Quit   ' When you finish, use the Quit method to close
    
     Set xlApp = Nothing   ' the application, then release the reference.
    
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

