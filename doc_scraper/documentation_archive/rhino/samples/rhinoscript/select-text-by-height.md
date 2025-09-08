---
url: https://developer.rhino3d.com/samples/rhinoscript/select-text-by-height/
scraped_at: 2025-09-08T15:49:39.091963
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

Select Text by Height

__

Windows only

Demonstrates how to select text objects by their text height using
RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' SelTextHeight.rvb -- July 2009
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0 and 5.0
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Option Explicit
    
    ' Global variables
    Public g_min_height
    Public g_max_height
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Selects text objects based on their text height
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub SelTextHeight()
    
      ' Local variables
      Dim min_height, max_height
      Dim objects, obj, height, sel_count
    
      ' Initialize global variables, if necessary
      If IsEmpty(g_min_height) Or IsNull(g_min_height) Then g_min_height = 1.0
      If IsEmpty(g_max_height) Or IsNull(g_max_height) Then g_max_height = 1.0
    
      ' Prompt for minimum height
      min_height = Rhino.GetReal("Minimum text height", g_min_height, 0.0)
      If IsNull(min_height) Then Exit Sub
    
      ' Prompt for maximum height
      max_height = Rhino.GetReal("Maximum text height", g_max_height, min_height)
      If IsNull(min_height) Then Exit Sub
      If (min_height > max_height) Then Exit Sub
    
      ' More initialization
      g_min_height = min_height
      g_max_height = max_height
      sel_count = 0
    
      Rhino.EnableRedraw False
    
      ' Find text objects that meet our criteria      
      objects = Rhino.ObjectsByType(512) 'annotations
      For Each obj In objects
        If Rhino.IsText(obj) Then
          height = Rhino.TextObjectHeight(obj)
          If (g_min_height <= height) And (height <= g_max_height) Then
            If Rhino.SelectObject(obj) Then sel_count = sel_count + 1
          End If    
        End If
      Next
    
      Rhino.EnableRedraw True
    
      Rhino.Print CStr(sel_count) & " text added to selection."
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "SelTextHeight", "_NoEcho _-RunScript (SelTextHeight)"
    

  

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

