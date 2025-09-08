---
url: https://developer.rhino3d.com/samples/rhinoscript/opening-3dm-files/
scraped_at: 2025-09-08T15:50:26.281448
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

Opening 3DM Files

__

Windows only

Demonstrates how to open 3DM files using RhinoScript.

VBScript

    
    
    Sub TestFileOpen()
    
      ' Local variable declarations
      Dim strFile
    
      ' Let the user pick a 3dm file. If the return value is null,
      ' then the user picked the "Cancel" button...
      strFile = Rhino.OpenFileName("Open", "Rhino 3D Models (*.3dm)|*.3dm|")
      If IsNull(strFile) Then Exit Sub
    
      ' To keep Rhino from displaying the dreaded
      ' "Save changes to <filename>" dialog, we can fool it
      ' into thinking that the document was never modified
      ' by doing the following.
      Call Rhino.DocumentModified(False)
    
      ' If the picked a file that has a space character in its name,
      ' or resides in a folder that has a space character, then we
      ' need to surround the file string in double-quotes so Rhino's
      ' command line parser will interpret the string correctly.
      strFile = Chr(34) & strFile & Chr(34)
    
      ' Now we can simply script Rhino's Open command to open the file.
       Call Rhino.Command("_-Open " & strFile, 0)
    
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

