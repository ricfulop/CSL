---
url: https://developer.rhino3d.com/samples/rhinoscript/revolve-profile-curves/
scraped_at: 2025-09-08T15:49:05.012038
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

Revolve Profile Curves

__

Windows only

Demonstrates how to create a surface by revolving one or more profile curves
using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub MyRevolve
    
      ' Declare local variables
      Dim obj_list, crv_list, crv, axis0, axis1
    
      ' Select one or more curves to revolve
      obj_list = Rhino.GetObjects("Select curves to revolve", 4, True, True)
      If IsNull(obj_list) Then Exit Sub
    
      ' Pick start of revolve axis    
      axis0 = Rhino.GetPoint("Start of revolve axis")
      If IsNull(axis0) Then Exit Sub
    
      ' Pick end of revolve axis    
      axis1 = Rhino.GetPoint("End of revolve axis", axis0)
      If IsNull(axis1) Then Exit Sub
    
      ' If more than one curve as picked, try to join them
      If (UBound(obj_list) > 0) Then
        crv_list = Rhino.JoinCurves(obj_list, False)
      Else
        crv_list = Array(obj_list(0))
      End If
    
      ' Create the surfaces of revolution  
      For Each crv In crv_list
        Call Rhino.AddRevSrf(crv, Array(axis0, axis1))
      Next
    
      ' Delete the temporary joined curves
      Call Rhino.DeleteObjects(crv_list)
    
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

