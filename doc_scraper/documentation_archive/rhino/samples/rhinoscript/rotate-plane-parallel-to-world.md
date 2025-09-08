---
url: https://developer.rhino3d.com/samples/rhinoscript/rotate-plane-parallel-to-world/
scraped_at: 2025-09-08T15:50:29.266650
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

Rotate Plane Parallel to World

__

Windows only

Demonstrates how to rotate a plane so its x-axis is parallel to the world
using RhinoScript.

VBScript

    
    
    Option Explicit
    
    '------------------------------------------------------------------------------
    ' Subroutine: XParallelPlane
    ' Purpose:    Rotate a plane about it's z-axis so that it's x-axis
                  is parallel with the world xy-plane.
    ' Parameters:
    '             plane - A valid plane to rotate
    '             dir   - Direction (True = positive, False = negative)
    ' Returns:
    '             A valid plane if successful, Null otherwise.
    '------------------------------------------------------------------------------
    Function XParallelPlane(plane, dir)
    
      Dim xaxis, yaxis, zaxis
      XParallelPlane = Null 'default return value
    
      zaxis = Rhino.VectorUnitize(plane(3))
      If (dir = True) Then
        xaxis = Rhino.VectorUnitize(Array(zaxis(1), -zaxis(0), 0.0))
      Else
        xaxis = Rhino.VectorUnitize(Array(-zaxis(0), zaxis(1), 0.0))
      End If
    
      yaxis = Rhino.VectorCrossProduct(zaxis, xaxis)
      If IsArray(yaxis) Then
        yaxis = Rhino.VectorUnitize(yaxis)
        XParallelPlane = Rhino.PlaneFromFrame(plane(0), xaxis, yaxis)
      End If
    
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

