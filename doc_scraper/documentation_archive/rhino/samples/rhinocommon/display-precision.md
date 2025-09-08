---
url: https://developer.rhino3d.com/samples/rhinocommon/display-precision/
scraped_at: 2025-09-08T15:46:00.777530
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

Display Precision

Demonstrates how to change the display precision in a Rhino model.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result DisplayPrecision(RhinoDoc doc)
      {
        var gi = new GetInteger();
        gi.SetCommandPrompt("New display precision");
        gi.SetDefaultInteger(doc.ModelDistanceDisplayPrecision);
        gi.SetLowerLimit(0, false);
        gi.SetUpperLimit(7, false);
        gi.Get();
        if (gi.CommandResult() != Result.Success)
          return gi.CommandResult();
        var distance_display-precision = gi.Number();
    
        if (distance_display-precision != doc.ModelDistanceDisplayPrecision)
          doc.ModelDistanceDisplayPrecision = distance_display-precision;
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function DisplayPrecision(ByVal doc As RhinoDoc) As Result
    	Dim gi = New GetInteger()
    	gi.SetCommandPrompt("New display precision")
    	gi.SetDefaultInteger(doc.ModelDistanceDisplayPrecision)
    	gi.SetLowerLimit(0, False)
    	gi.SetUpperLimit(7, False)
    	gi.Get()
    	If gi.CommandResult() <> Result.Success Then
    	  Return gi.CommandResult()
    	End If
    	Dim distance_display-precision = gi.Number()
    
    	If distance_display-precision IsNot doc.ModelDistanceDisplayPrecision Then
    	  doc.ModelDistanceDisplayPrecision = distance_display-precision
    	End If
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.Input.Custom import *
    from Rhino.Commands import *
    from scriptcontext import doc
    import rhinoscriptsyntax as rs
    
    def RunCommand():
        distance_display-precision = rs.GetInteger("Display precision",
            doc.ModelDistanceDisplayPrecision, 0, 7)
        if distance_display-precision == None: return Result.Nothing
    
        if distance_display-precision != doc.ModelDistanceDisplayPrecision:
            doc.ModelDistanceDisplayPrecision = distance_display-precision
    
        return Result.Success
    
    if __name__ ==  "__main__":
        RunCommand()
    

  

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

