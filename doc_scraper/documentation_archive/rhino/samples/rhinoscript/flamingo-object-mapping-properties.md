---
url: https://developer.rhino3d.com/samples/rhinoscript/flamingo-object-mapping-properties/
scraped_at: 2025-09-08T15:49:52.137796
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

Flamingo Object Mapping Properties

__

Windows only

Demonstrates how to set Flamingo nXt mapping properties for an object using
RhinoScript.

VBScript

    
    
    Option Explicit
    
    Call Main()
    
    Sub Main()
    	Dim objPlugIn, strObject, scale, xscale, yscale, zscale
    	On Error Resume Next
    	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
    	If Err Then
    		MsgBox Err.Description
    		Exit Sub
    	End If
    	strObject = Rhino.GetObject("Select object")
      If Not IsNull(strObject) And Not strObject = "" Then
      	scale = objPlugIn.GetMappingScale(strObject)
        xscale = 1.0
        yscale = 1.0
        zscale = 1.0
        If Not IsNull(scale) Then
          xscale = CDbl(scale(0))
          yscale = CDbl(scale(1))
          zScale = CDbl(scale(2))
        End If
      	xscale = Rhino.GetReal("X-Scale", xscale)
    	  If Not IsNull(xscale) Then
      	  yscale = Rhino.GetReal("Y-Scale", yscale)
    	    If Not IsNull(xscale) Then
      	    zscale = Rhino.GetReal("Z-Scale", zscale)
    	      If Not IsNull(xscale) Then
              If objPlugIn.SetMappingScale(strObject, xscale, yscale, zscale) Then
                Rhino.Print("Object mapping scale set to: x-scale:" & xscale & "  y-scale: " & yscale & "  z-scale: " & zscale)
              Else
                Rhino.Print("Error setting objects mapping scale")
              End If
            End If
          End If
        End If
    	End If
    	Set objPlugIn = Nothing
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

