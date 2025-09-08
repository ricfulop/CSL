---
url: https://developer.rhino3d.com/samples/rhinoscript/create-box-frames/
scraped_at: 2025-09-08T15:48:54.932293
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

Create Box Frames

__

Windows only

Demonstrates how to create a box frame with RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' BoxFrame.rvb -- November 2009
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Option Explicit
    
    Sub BoxFrame()
    
      ' Local constants
      Const X = 0
      Const Y = 1
      Const Z = 2
      Const TOL = 0.01
    
      ' Local variables
      Dim box_points, box_object, box_center, box_plane
      Dim offset(2), dist(2), pfact(2), nfact(2)
      Dim xform(2), boxes(2)
    
      ' Prompt the user to define a box    
      box_points = Rhino.GetBox()
      If IsNull(box_points) Then Exit Sub
    
      ' Calculate half distances between corners    
      dist(X) = Rhino.Distance(box_points(0), box_points(1)) * 0.5
      dist(Y) = Rhino.Distance(box_points(0), box_points(3)) * 0.5
      dist(Z) = Rhino.Distance(box_points(0), box_points(4)) * 0.5
    
      ' Define axes offsets
      offset(X) = Rhino.GetReal("Thickness in X direction", 1.0, TOL, dist(X) - TOL)
      If IsNull(offset(X)) Then Exit Sub
    
      offset(Y) = Rhino.GetReal("Thickness in Y direction", 1.0, TOL, dist(Y) - TOL)
      If IsNull(offset(Y)) Then Exit Sub
    
      offset(Z) = Rhino.GetReal("Thickness in Z direction", 1.0, TOL, dist(Z) - TOL)
      If IsNull(offset(Z)) Then Exit Sub
    
      ' Do this for performance
      Call Rhino.EnableRedraw(False)    
    
      ' Calculate increasing scale factors
      pfact(X) = (dist(X) + offset(X)) / dist(X)
      pfact(Y) = (dist(Y) + offset(Y)) / dist(Y)
      pfact(Z) = (dist(Z) + offset(Z)) / dist(Z)
    
      ' Calculate decreasing scale factors
      nfact(X) = (dist(X) - offset(X)) / dist(X)
      nfact(Y) = (dist(Y) - offset(Y)) / dist(Y)
      nfact(Z) = (dist(Z) - offset(Z)) / dist(Z)
    
      ' Some stuff need for the scale transformation
      box_center = Rhino.PointDivide(Rhino.PointAdd(box_points(0), box_points(6)), 2.0)
      box_plane = Rhino.PlaneFromPoints(box_points(0), box_points(1), box_points(3))
      box_plane = Rhino.MovePlane(box_plane, box_center)
    
      ' Define scale transformations
      xform(0) = Rhino.XformScale(box_plane, pfact(0), nfact(1), nfact(2))
      xform(1) = Rhino.XformScale(box_plane, nfact(0), pfact(1), nfact(2))
      xform(2) = Rhino.XformScale(box_plane, nfact(0), nfact(1), pfact(2))
    
      ' Create the box
      box_object = Rhino.AddBox(box_points)
    
      ' Create the boxes to difference
      boxes(0) = Rhino.TransformObject(box_object, xform(0), True)
      boxes(1) = Rhino.TransformObject(box_object, xform(1), True)
      boxes(2) = Rhino.TransformObject(box_object, xform(2), True)
    
      ' Do the difference
      Call Rhino.BooleanDifference(Array(box_object), boxes, True)
    
      ' Enable redraw
      Call Rhino.EnableRedraw(True)    
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "BoxFrame", "_NoEcho _-RunScript (BoxFrame)"
    

  

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

