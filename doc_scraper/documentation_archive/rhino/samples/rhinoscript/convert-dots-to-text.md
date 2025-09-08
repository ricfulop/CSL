---
url: https://developer.rhino3d.com/samples/rhinoscript/convert-dots-to-text/
scraped_at: 2025-09-08T15:48:51.879110
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

Convert Dots to Text

__

Windows only

Illustrates RhinoScript code that converts annotation dots to text object.

VBScript

    
    
    Sub ConvertDotsToText
      Dim arrDots, strDot
      arrDots = Rhino.GetObjects("Select dots", 0, True, True )
      If Not IsArray(arrDots) Then Exit Sub
    
      Dim arrPt, strText
      For Each strDot In arrDots
        If Rhino.IsTextDot(strDot) Then
          strText = Rhino.TextDotText(strDot)
          arrPt = Rhino.TextDotPoint(strDot)
          Rhino.AddText strText, arrPt
          Rhino.DeleteObject strDot
        End If
      Next
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

