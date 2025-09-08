---
url: https://developer.rhino3d.com/samples/rhinoscript/calculate-the-angle-between-two-vectors/
scraped_at: 2025-09-08T15:50:08.090518
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

Calculate the Angle Between Two Vectors

__

Windows only

Demonstrates how to calculate the angle between two vectors using RhinoScript.

VBScript

    
    
    ' Description:
    '  Calculates the angle between two 3-D vectors.
    ' Parameters:
    '   v0 - [in] - the first vector.
    '   v1 - [in] - the second vector.
    ' Returns:
    '   the angle in degrees.
    
    Function VectorAngle(v0, v1)
    
      Dim u0  : u0  = Rhino.VectorUnitize(v0)
      Dim u1  : u1  = Rhino.VectorUnitize(v1)  
      Dim dot : dot = Rhino.VectorDotProduct(u0, u1)
    
      ' Force the dot product of the two input vectors to
      ' fall within the domain for inverse cosine, which
      ' is -1 <= x <= 1. This will prevent runtime
      ' "domain error" math exceptions.
      If (dot < -1.0) Then
        dot = -1.0
      ElseIf (dot > 1.0) Then
        dot = 1.0
      End If
    
      VectorAngle = Rhino.ToDegrees(Rhino.ACos(dot))
    
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

