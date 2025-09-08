---
url: https://developer.rhino3d.com/guides/rhinoscript/converting-text-to-geometry/
scraped_at: 2025-09-08T15:42:37.373930
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

[Converting Text to
Geometry](https://developer.rhino3d.com/guides/rhinoscript/converting-text-to-
geometry/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Converting Text to Geometry

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You have many text elements that you would like to convert to text objects
(geometry) for engraving. You can explode a text element and get curves that
outline the text. The problem is, when you change a text element to a single
stroke font, it automatically closes each letter/number and is unreadable. The
only way you have been able to make a single stroke font work is by creating
geometry using Rhino’s TextObject command. However, because you have so many
text elements it would take forever to remake geometry for each of them. It is
possible to write a script to automate this.

## Solution

The following script demonstrates how to convert text elements to text objects
(geometry). In this sample, text objects (geometry) are created with the
identical properties, such as font, height, bold, and italics, as the text
element.

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' ConvertTextToGeometry.rvb -- September 2008
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    
    Option Explicit
    
    Sub ConvertTextToGeometry
    
      ' Declare local variables
      Dim obj_list, obj, saved_plane, cmd
      Dim font, height, plane, style, text, bold, italic
    
      ' Select annotation objects
      obj_list = Rhino.GetObjects("Select text to convert to geometry", 512, True, True)
      If Not IsArray(obj_list) Then Exit Sub
    
      ' For speed, turn of screen redrawing
      Call Rhino.EnableRedraw(False)
    
      ' Save the current construction plane
      saved_plane = Rhino.ViewCPlane()
    
      ' Process each selected object
      For Each obj In obj_list
    
        ' Weed out just the text objects
        If Rhino.IsText(obj) Then
    
          ' Acquire the text parameters
          font = Rhino.TextObjectFont(obj)
          height = Rhino.TextObjectHeight(obj)
          plane = Rhino.TextObjectPlane(obj)
          style = Rhino.TextObjectStyle(obj)
          text = Rhino.TextObjectText(obj)
    
          If (style And 1) Then
            bold = "_Yes"
          Else
            bold = "_No"
          End If
    
          If (style And 2) Then
            italic = "_Yes"
          Else
            italic = "_No"
          End If
    
          ' Set the current construction plane
          Call Rhino.ViewCPlane(, plane)
    
          ' Add a new text object (geometry)
          cmd = "_-TextObject "
          cmd = cmd & "_GroupOutput=_Yes "
          cmd = cmd & "_FontName=" & font & " "
          cmd = cmd & "_Italic=" & italic & " "
          cmd = cmd & "_Bold=" & bold & " "
          cmd = cmd & "_Height=" & CStr(height) & " "
          cmd = cmd & "_Output=_Curves "
          cmd = cmd & "_AllowOpenCurves=_Yes "
          cmd = cmd & Chr(34) & text & Chr(34) & " "
          cmd = cmd & "0"
          Call Rhino.Command(cmd, 0)
    
          ' Delete the original object
          Call Rhino.DeleteObject(obj)
    
        End If
      Next
    
      ' Restore the saved construction plane      
      Call Rhino.ViewCPlane(, saved_plane)
    
      ' Enable screen redrawing
      Call Rhino.EnableRedraw(True)
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "ConvertTextToGeometry", "_NoEcho _-RunScript (ConvertTextToGeometry)"
    

If you want to override the font to use a single stroke font, simply modify
this line:

    
    
     font = Rhino.TextObjectFont(obj)
    

and replace it with something more like this:

    
    
     font = "<single_stroke_font_name>"
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/converting-
text-to-geometry/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/converting-
text-to-geometry/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

