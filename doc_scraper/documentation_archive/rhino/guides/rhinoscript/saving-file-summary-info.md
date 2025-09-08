---
url: https://developer.rhino3d.com/guides/rhinoscript/saving-file-summary-info/
scraped_at: 2025-09-08T15:43:00.423889
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

[Saving File Summary
Info](https://developer.rhino3d.com/guides/rhinoscript/saving-file-summary-
info/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Saving File Summary Info

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

When you right-click on a file, using Windows Explorer, and pick
“Properties…”, to bring up the File Properties dialog, you can add summary
information to a file by clicking on the Summary tab and entering the
appropriate information. Imagine you would like to do this when saving Rhino
files. Rhino does not have this capability, but RhinoScript can help.

## Solution

The following example script will save the Rhino file by scripting Rhino’s
Save command. If the command was successful in saving the file, script will
then display the File Properties dialog and display the summary information
for that file…

    
    
    Sub SuperSaver()
      Rhino.Command "_Save"
      If (0 = Rhino.LastCommandResult()) Then
        Dim objShell, objFolder, objFolderItem, objInfo
        Set objShell = CreateObject("Shell.Application")
        Set objFolder = objShell.NameSpace(Rhino.DocumentPath)
        If (Not objFolder Is Nothing) Then
          Set objFolderItem = objFolder.ParseName(Rhino.DocumentName)
          If (Not objFolderItem Is Nothing) Then
            Call objFolderItem.InvokeVerbEx("properties", "summary")
          End If
          Set objFolderItem = Nothing
        End If
        Set objFolder = Nothing
        Set objShell = Nothing
      End If
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/saving-
file-summary-info/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/saving-
file-summary-info/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

