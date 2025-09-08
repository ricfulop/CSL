---
url: https://developer.rhino3d.com/samples/rhinoscript/exploding-block-instances/
scraped_at: 2025-09-08T15:49:08.963461
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

Exploding Block Instances

__

Windows only

Demonstrates how to explode an instance of a block using RhinoScript.

VBScript

    
    
    Sub SuperExplodeBlock
      Const rhInstanceObject = 4096
      Dim arrBlocks, strBlock
      arrBlocks = Rhino.ObjectsByType(rhInstanceObject)
      If IsArray(arrBlocks) Then
        For Each strBlock In arrBlocks
          If Rhino.IsObjectSelectable(strBlock) Then
            DoInstanceExplosion strBlock
          End If
        Next
      End If
    End Sub
    
    Sub DoBlockExplosion(strBlock)
      Dim arrObjects, strObject
      If Rhino.IsBlockInstance(strBlock) Then
        arrObjects = Rhino.ExplodeBlockInstance(strBlock)
        If IsArray(arrObjects) Then
          For Each strObject In arrObjects
            DoBlockExplosion strObject '*RECURSE*
          Next
        End If
      End If
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

