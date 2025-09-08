---
url: https://developer.rhino3d.com/samples/rhinocommon/get-angle/
scraped_at: 2025-09-08T15:45:31.630297
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

Get Angle

Demonstrates how to interactively pick an angle given a base point and two
reference points.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result GetAngle(RhinoDoc doc)
      {
        var gp = new GetPoint();
        gp.SetCommandPrompt("Base point");
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var base_point = gp.Point();
    
        gp.SetCommandPrompt("First reference point");
        gp.DrawLineFromPoint(base_point, true);
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var first_point = gp.Point();
    
        double angle_radians;
        var rc = RhinoGet.GetAngle("Second reference point", base_point, first_point, 0, out angle_radians);
        if (rc == Result.Success)
          RhinoApp.WriteLine("Angle = {0} degrees", RhinoMath.ToDegrees(angle_radians));
    
        return rc;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function GetAngle(ByVal doc As RhinoDoc) As Result
    	Dim gp = New GetPoint()
    	gp.SetCommandPrompt("Base point")
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim base_point = gp.Point()
    
    	gp.SetCommandPrompt("First reference point")
    	gp.DrawLineFromPoint(base_point, True)
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim first_point = gp.Point()
    
    	Dim angle_radians As Double = Nothing
    	Dim rc = RhinoGet.GetAngle("Second reference point", base_point, first_point, 0, angle_radians)
    	If rc Is Result.Success Then
    	  RhinoApp.WriteLine("Angle = {0} degrees", RhinoMath.ToDegrees(angle_radians))
    	End If
    
    	Return rc
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.Commands import *
    from Rhino.Input import *
    from Rhino.Input.Custom import *
    
    def RunCommand():
        gp = GetPoint()
        gp.SetCommandPrompt("Base point")
        gp.Get()
        if gp.CommandResult() != Result.Success:
            return gp.CommandResult()
        base_point = gp.Point()
    
        gp.SetCommandPrompt("First reference point")
        gp.DrawLineFromPoint(base_point, True)
        gp.Get()
        if gp.CommandResult() != Result.Success:
            return gp.CommandResult()
        first_point = gp.Point()
    
    
        rc, angle_radians = RhinoGet.GetAngle("Second reference point", base_point, first_point, 0)
        if rc == Result.Success:
            print "Angle = {0} degrees".format(RhinoMath.ToDegrees(angle_radians))
        return rc
    
    if __name__ == "__main__":
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

