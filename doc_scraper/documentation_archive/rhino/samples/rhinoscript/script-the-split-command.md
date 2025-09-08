---
url: https://developer.rhino3d.com/samples/rhinoscript/script-the-split-command/
scraped_at: 2025-09-08T15:49:46.116124
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

Script the Split Command

__

Windows only

Demonstrates how to script the Split command using RhinoScript.

VBScript

    
    
    Function DoBrepSplit(brep, cutter)
    
       ' Declare local variables
       Dim saved, cmd
    
       ' Set default return value  
       DoBrepSplit = Null
    
       ' For speed, turn of screen redrawing
       Rhino.EnableRedraw False
    
       ' Save any selected objects
       saved = Rhino.SelectedObjects
    
       ' Unselect all objects
       Rhino.UnSelectAllObjects
    
       ' Select the brep
       Rhino.SelectObject brep
    
       ' Script the split command
       cmd = "_Split _SelID " & cutter & " _Enter"
       Rhino.Command cmd, 0
    
       ' By preselecting the brep, the results of
       ' Split will be selected. So, get the selected
       ' objects and return them to the caller.
       DoBrepSplit = Rhino.SelectedObjects
    
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

