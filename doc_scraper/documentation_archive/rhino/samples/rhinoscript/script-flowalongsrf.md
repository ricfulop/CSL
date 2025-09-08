---
url: https://developer.rhino3d.com/samples/rhinoscript/script-flowalongsrf/
scraped_at: 2025-09-08T15:49:45.124462
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

Script FlowAlongSrf

__

Windows only

Demonstrates how to script the FlowAlongSrf command using RhinoScript.

VBScript

    
    
    Function DoFlowAlongSrf(arrObjects, strBase, strTarget)
    
      ' Declare local variables
      Dim saved, cmd
    
      ' For speed, turn of screen redrawing
      Rhino.EnableRedraw False
    
      ' Save any selected objects
      saved = Rhino.SelectedObjects
    
      ' Unselect all objects
      Rhino.UnSelectAllObjects
    
      ' Select the brep
      Rhino.SelectObjects arrObjects
    
      ' Script the split command
      cmd = "_FlowAlongSrf _SelID " & strBase & " _SelID " & strTarget
      Rhino.Command cmd, 0
    
      ' By preselecting the brep, the results of
      ' Split will be selected. So, get the selected
      ' objects and return them to the caller.
      DoFlowAlongSrf = Rhino.SelectedObjects
    
      ' Unselect all objects
      Rhino.UnSelectAllObjects
    
      ' If any objects were selected before calling
      ' this function, re-select them
      If IsArray(saved) Then Rhino.SelectObjects(saved)
    
      ' Don't forget to turn redrawing back on
      Rhino.EnableRedraw True
    
    End Function
    

  

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

