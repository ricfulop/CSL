---
url: https://developer.rhino3d.com/samples/rhinoscript/split-file-path-string/
scraped_at: 2025-09-08T15:50:36.292028
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

Split File Path String

__

Windows only

Demonstrates how to break a file path string in to its components using
RhinoScript.

VBScript

    
    
    Sub SplitPath(ByVal sPath, ByRef sDrive, ByRef sDir, ByRef sFname, ByRef sExt)
      Dim fso
      Set fso = CreateObject("Scripting.FileSystemObject")
      sDrive = fso.GetDriveName(sPath)
      sDir = Mid(fso.GetParentFolderName(sPath), Len(sDrive)+1) & "\"
      sFname = fso.GetBaseName(sPath)
      sExt = "." & fso.GetExtensionName(sPath)
      Set fso = Nothing
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

