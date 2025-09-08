---
url: https://developer.rhino3d.com/samples/rhinoscript/multiple-pipe/
scraped_at: 2025-09-08T15:49:00.923560
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

Multiple Pipe

__

Windows only

Demonstrates how to Pipe on multiple curves at a time using RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' PipeAll.rvb -- September 2008
    ' If this code works, it was written by Rajaa Issa.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    
    Option Explicit
    
    Sub PipeOne(strRail, strRadius)
      Dim strCmd
      strCmd = "! _-Pipe _SelID " & strRail & " " & strRadius & " _Cap=_Round _Enter _Enter"
      Call Rhino.Command(strCmd, 0)
    End Sub
    
    Sub PipeAll
     Dim arrCurves, name, pipeRadius
     arrCurves = Rhino.GetObjects("Select curves to pipe", 4)
     pipeRadius = Rhino.GetReal("Pipe radius")
    
     'PIPE
     If IsArray(arrCurves) Then
      For Each name In arrCurves
       Call PipeOne(name, pipeRadius)
      Next
     End If
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "PipeAll", "_NoEcho _-RunScript (PipeAll)"
    

  

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

