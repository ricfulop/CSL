---
url: https://developer.rhino3d.com/samples/rhinoscript/exploding-meshes/
scraped_at: 2025-09-08T15:50:13.333402
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

Exploding Meshes

__

Windows only

Demonstrates how to explode a mesh into individual faces using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub ExplodeMesh
      Dim mesh
      mesh = Rhino.GetObject("Select mesh to explode", 32)
      If IsNull(mesh) Then Exit Sub
    
      Dim faces
      faces = Rhino.MeshFaces(mesh, True)
      If Not IsArray(faces) Then Exit Sub
    
      Rhino.EnableRedraw False
      Dim i, a, b, c, d, bQuad
      i = 0
    
      While i <= UBound(faces)
        a = faces(i)
        b = faces(i+1)
        c = faces(i+2)
        d = faces(i+3)
        If c(0)=d(0) And c(1)=d(1) And c(2)=d(2) Then
          Rhino.AddMesh Array(a,b,c,d), Array(Array(0,1,2,2))
        Else
          Rhino.AddMesh Array(a,b,c,d), Array(Array(0,1,2,3))
        End If
        i = i + 4
      Wend
    
      Rhino.DeleteObject mesh
      Rhino.EnableRedraw True
    
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

