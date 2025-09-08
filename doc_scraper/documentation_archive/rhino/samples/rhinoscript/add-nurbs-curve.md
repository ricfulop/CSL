---
url: https://developer.rhino3d.com/samples/rhinoscript/add-nurbs-curve/
scraped_at: 2025-09-08T15:48:47.860092
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

Add NURBS Curve

__

Windows only

Demonstrates how to add a NURBS curve to Rhino using RhinoScript.

VBScript

    
    
    Sub TestNurbsCurve
    
      Dim degree : degree = 3
      Dim cv_count : cv_count = 6
      Dim knot_count : knot_count = cv_count + degree - 1
    
      Dim cvs() : ReDim cvs(cv_count - 1)
      cvs(0) = Array(0.0, 0.0, 0.0)
      cvs(1) = Array(5.0, 10.0, 0.0)
      cvs(2) = Array(10.0, 0.0, 0.0)
      cvs(3) = Array(15.0, 10.0, 0.0)
      cvs(4) = Array(20.0, 0.0, 0.0)
      cvs(5) = Array(25.0, 10.0, 0.0)
    
      Dim knots() : ReDim knots(knot_count - 1)
      knots(0) = 0.0
      knots(1) = 0.0
      knots(2) = 0.0
      knots(3) = 1.0
      knots(4) = 2.0
      knots(5) = 3.0
      knots(6) = 3.0
      knots(7) = 3.0
    
      Call Rhino.AddNurbsCurve(cvs, knots, degree)
    
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

