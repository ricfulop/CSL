---
url: https://developer.rhino3d.com/samples/rhinoscript/rotate-object-around-point/
scraped_at: 2025-09-08T15:50:28.302852
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

Rotate Object Around Point

__

Windows only

Demonstrates how to rotate an object around the centroid of its bounding box
using RhinoScript.

VBScript

    
    
    Sub Rotate1
      Dim sObj, aBox, aMin, aMax, aCen
      sObj = Rhino.GetObject("Select object to rotate 1 degree", 0, True)
      If Not IsNull(sObj) Then
        aBox = Rhino.BoundingBox(sObj)
        If IsArray(aBox) Then
          aMin = aBox(0)
          aMax = aBox(6)
          aCen = Array( _
              0.5*(aMax(0)+aMin(0)), _
              0.5*(aMax(1)+aMin(1)), _
              0.5*(aMax(2)+aMin(2)) _
              )
          Rhino.RotateObject sObj, aCen, 1.0
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

