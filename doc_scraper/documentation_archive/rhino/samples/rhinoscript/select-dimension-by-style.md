---
url: https://developer.rhino3d.com/samples/rhinoscript/select-dimension-by-style/
scraped_at: 2025-09-08T15:49:34.961900
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

Select Dimensions by Style

__

Windows only

Demonstrates how to select an objects (dimensions) by their dimension style
using RhinoScript.

VBScript

    
    
    Sub SelDimStyle
    
      ' Declare local constants and variables
      Const rhAnnotation = 512
      Dim strStyle, arrObjects, strObject
    
      ' Prompt the user to enter the name of the dimension style
      strStyle = Rhino.GetString("Dimension style to select", Rhino.CurrentDimStyle)
      If IsNull(strStyle) Then Exit Sub
      If Not Rhino.IsDimStyle(strStyle) Then Exit Sub
    
      ' Create an array of all annotation objects
      arrObjects = Rhino.ObjectsByType(rhAnnotation)
      If Not IsArray(arrObjects) Then Exit Sub
    
      Rhino.EnableRedraw False
    
      ' Process each annotation object
      For Each strObject In arrObjects
        If Rhino.IsDimension(strObject) Then
          If StrComp(Rhino.DimensionStyle(strObject), strStyle, 1) = 0 Then
            Rhino.SelectObject strObject
          End If
        End If
      Next
    
      Rhino.EnableRedraw True
    
    End Sub
    

This one allows selection of a dimension style from a list…

    
    
    Sub SelDimStyleList
    
    ' Declare local constants and variables
    Const rhAnnotation = 512
    Dim strStyle, arrObjects, strObject, arrStyles
    
    'get the existing styles
    arrStyles = Rhino.DimStyleNames ()
    
    ' Prompt the user to select the name of the dimension style
    strStyle = Rhino.ListBox(arrStyles, "Dimension style to select", "Dimension styles")
    If IsNull(strStyle) Then Exit Sub
    If Not Rhino.IsDimStyle(strStyle) Then Exit Sub
    
    ' Create an array of all annotation objects
    arrObjects = Rhino.ObjectsByType(rhAnnotation)
    If Not IsArray(arrObjects) Then Exit Sub
    
    Rhino.EnableRedraw False
    
    ' Process each annotation object
    For Each strObject In arrObjects
      If Rhino.IsDimension(strObject) Then
        If StrComp(Rhino.DimensionStyle(strObject), strStyle, 1) = 0 Then
          Rhino.SelectObject strObject
        End If
    End If
    Next
    
    Rhino.EnableRedraw True
    
    End Sub
    

This one selects dimensions matching the styles of selected dimensions…

    
    
    Sub SelDimStyleMatch
    
    ' Declare local constants and variables
    Const rhAnnotation = 512
    Dim sStyle, aDims, sDim, strObject, aStyles(),aStyles1, aSel, sSel, i
    
    ' Create an array of all annotation objects
    aDims = Rhino.ObjectsByType(rhAnnotation)
    If Not IsArray(aDims) Then Exit Sub
    
    'Get the selected dimensions to match
    aSel = Rhino.GetObjects("Select dimensions",rhAnnotation,True,True,True,aDims)
    
    'create an array of the selcted dimension styles
    If isarray(aSel) Then
     For Each sSel In  aSel
       ReDim Preserve aStyles(i)
       aStyles(i) =  Rhino.DimensionStyle(sSel)    
       i = i + 1
     Next
    Else Exit Sub
    End If
    
    'cull duplicate styles from the array
    aStyles1 = Rhino.CullDuplicateStrings(aStyles)
    
    Rhino.EnableRedraw False
    
    ' Process each annotation object with each selected dim stlye
    
    For Each sDim In aDims
     For Each sStyle In aStyles1
       If StrComp(Rhino.DimensionStyle(sDim), sStyle, 1) = 0 Then
         Rhino.SelectObject sDim
       End If
     Next
    Next
    
    Rhino.EnableRedraw True
    
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

