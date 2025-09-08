---
url: https://developer.rhino3d.com/samples/rhinoscript/list-iges-export-schemes/
scraped_at: 2025-09-08T15:50:22.255720
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

List IGES Export Schemes

__

Windows only

Demonstrates how to build a list of IGES export schemes using RhinoScript.

VBScript

    
    
    Option Explicit
    
    Function GetIgesExportSchemes()
      Const HKEY_CURRENT_USER = &H80000001
    
      Dim objReg, strComputer, strKey, arrSubKeys
      strComputer = "."
      strKey = "Software\McNeel\Rhinoceros\4.0\Scheme: Default\Plug-ins\7f0ca561-0c7c-4cea-b822-b95ebe71c409\Settings"
    
      On Error Resume Next   
      Set objReg = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\default:StdRegProv")
      If Err.Number = 0 Then
        Call objReg.EnumKey(HKEY_CURRENT_USER, strKey, arrSubKeys)
      End If
    
      If IsArray(arrSubKeys) Then
        GetIgesExportSchemes = Rhino.SortStrings(arrSubKeys)
      Else
        GetIgesExportSchemes = Null
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

