---
url: https://developer.rhino3d.com/samples/rhinoscript/get-rgb-color-intensities/
scraped_at: 2025-09-08T15:50:17.230215
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

Get RGB Color Intensities

__

Windows only

Demonstrates retrieve red, green, and blue color intensities using VBScript.

VBScript

    
    
    ''' ---------------------------------------------------------------------------
    ''' Function:   GetRValue
    ''' Purpose:    Returns the Red value from an RGB color value
    ''' Arguments:  vbLong - An RGB color value
    ''' Returns:    vbLong - A Red color value, -1 on error
    ''' ---------------------------------------------------------------------------
    Function GetRValue(val)
      If val > -1 And val < 16777216 Then
        GetRValue = val \ 256 ^ 0 And 255
      Else
        GetRValue = -1
      End If
    End Function
    
    ''' ---------------------------------------------------------------------------
    ''' Function:   GetGValue
    ''' Purpose:    Returns the Green value from an RGB color value
    ''' Arguments:  vbLong - an RGB color value
    ''' Returns:    vbLong - a Green color value, -1 on error
    ''' ---------------------------------------------------------------------------
    Function GetGValue(val)
      If val > -1 And val < 16777216 Then
        GetGValue = val \ 256 ^ 1 And 255
      Else
        GetGValue = -1
      End If
    End Function
    
    ''' ---------------------------------------------------------------------------
    ''' Function:   GetBValue
    ''' Purpose:    Returns the Blue value from an RGB color value
    ''' Arguments:  vbLong - an RGB color value
    ''' Returns:    vbLong - a Blue color value, -1 on error
    ''' ---------------------------------------------------------------------------
    Function GetBValue(val)
      If val > -1 And val < 16777216 Then
        GetBValue = val \ 256 ^ 2 And 255
      Else
        GetBValue = -1
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

