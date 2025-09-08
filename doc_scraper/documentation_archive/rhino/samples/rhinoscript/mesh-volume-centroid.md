---
url: https://developer.rhino3d.com/samples/rhinoscript/mesh-volume-centroid/
scraped_at: 2025-09-08T15:50:25.226917
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

Mesh Volume Centroid

__

Windows only

Demonstrates how to calculate the volume centroid of a mesh.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' MeshVolumeCentroid.rvb -- July 2009
    ' Mary Fugier, Robert McNeel & Associates
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Option Explicit
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Calculates the volume centroid of a mesh object.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub MeshVolumeCentroid()
    
      Const RHINO_MESH = 32
      Dim strObject, arrCentroid
    
      strObject = Rhino.GetObject("Select mesh for volume centroid calculation", RHINO_MESH)
      If Not IsNull(strObject) Then
        arrCentroid = Rhino.MeshVolumeCentroid(strObject)
        If IsArray(arrCentroid) Then
          Call Rhino.AddPoint(arrCentroid)
          Call Rhino.Print("Volume Centroid = " & Rhino.Pt2Str(arrCentroid))
        End If
      End If
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' If dragged and dropped on Rhino, a "MeshVolumeCentroid" alias
    ' will be created.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "MeshVolumeCentroid", "_NoEcho _-RunScript (MeshVolumeCentroid)"
    

  

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

