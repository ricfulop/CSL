---
url: https://developer.rhino3d.com/samples/rhinoscript/match-text-properties/
scraped_at: 2025-09-08T15:50:24.252613
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

Match Text Properties

__

Windows only

Demonstrates how to match text object properties in RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' MatchText.rvb -- July 2009
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0 and 5.0
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Option Explicit
    
    Sub MatchText()
    
      Dim objects, source, match, items, values, i
      Dim font, height, style
    
      objects = Rhino.GetObjects("Select text objects to modify", 512,, True)
      If IsNull(objects) Then Exit Sub
    
      source = Rhino.GetObject("Select source object", 512)
      If IsNull(source) Then Exit Sub
    
      items = Array("Font", "Height", "Style")
      values = Array(True, True, True)
      match = Rhino.CheckListBox(items, values, "Properties to match:", "Match Text")
      If IsNull(match) Then Exit Sub
    
      font = Rhino.TextObjectFont(source)
      height = Rhino.TextObjectHeight(source)
      style = Rhino.TextObjectStyle(source)
    
      Call Rhino.EnableRedraw(False)
    
      For i = 0 To UBound(objects)
        If match(0) = True Then Call Rhino.TextObjectFont(objects(i), font)
        If match(1) = True Then Call Rhino.TextObjectHeight(objects(i), height)
        If match(2) = True Then Call Rhino.TextObjectStyle(objects(i), style)
      Next
    
      Call Rhino.EnableRedraw(True)
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "MatchText", "_NoEcho _-RunScript (MatchText)"
    

  

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

