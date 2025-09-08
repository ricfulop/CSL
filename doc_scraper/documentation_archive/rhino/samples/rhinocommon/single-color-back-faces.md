---
url: https://developer.rhino3d.com/samples/rhinocommon/single-color-back-faces/
scraped_at: 2025-09-08T15:46:37.949032
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

Single Color Back Faces

Demonstrates how to determine the curve and object colors of back faces.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result SingleColorBackfaces(RhinoDoc doc)
      {
        var display_mode_descs = //DisplayModeDescription.GetDisplayModes();
          from dm in DisplayModeDescription.GetDisplayModes()
          where dm.EnglishName == "Shaded"
          select dm;
    
        foreach (var dmd in display_mode_descs)
        {
          RhinoApp.WriteLine("CurveColor {0}", dmd.DisplayAttributes.CurveColor.ToKnownColor());
          RhinoApp.WriteLine("ObjectColor {0}", dmd.DisplayAttributes.ObjectColor.ToKnownColor());
        }
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function SingleColorBackfaces(ByVal doc As RhinoDoc) As Result
    	Dim display_mode_descs = From dm In DisplayModeDescription.GetDisplayModes()
    	                         Where dm.EnglishName = "Shaded"
    	                         Select dm 'DisplayModeDescription.GetDisplayModes();
    
    	For Each dmd In display_mode_descs
    	  RhinoApp.WriteLine("CurveColor {0}", dmd.DisplayAttributes.CurveColor.ToKnownColor())
    	  RhinoApp.WriteLine("ObjectColor {0}", dmd.DisplayAttributes.ObjectColor.ToKnownColor())
    	Next dmd
    	Return Result.Success
      End Function
    End Class
    
    
    
    # No Python sample available
    

  

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

