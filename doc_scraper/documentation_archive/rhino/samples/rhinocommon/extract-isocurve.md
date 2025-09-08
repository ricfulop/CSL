---
url: https://developer.rhino3d.com/samples/rhinocommon/extract-isocurve/
scraped_at: 2025-09-08T15:45:13.529713
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

Extract Isocurve

Demonstrates how to extract the isoparametric curves from selected surfaces.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ExtractIsoCurve(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select surface", false, ObjectType.Surface, out obj_ref);
        if (rc != Result.Success || obj_ref == null)
          return rc;
        var surface = obj_ref.Surface();
    
        var gp = new GetPoint();
        gp.SetCommandPrompt("Point on surface");
        gp.Constrain(surface, false);
        var option_toggle = new OptionToggle(false, "U", "V");
        gp.AddOptionToggle("Direction", ref option_toggle);
        Point3d point = Point3d.Unset;
        while (true)
        {
          var grc = gp.Get();
          if (grc == GetResult.Option)
            continue;
          else if (grc == GetResult.Point)
          {
            point = gp.Point();
            break;
          }
          else
            return Result.Nothing;
        }
        if (point == Point3d.Unset)
          return Result.Nothing;
    
        int direction = option_toggle.CurrentValue ? 1 : 0; // V : U
        double u_parameter, v_parameter;
        if (!surface.ClosestPoint(point, out u_parameter, out v_parameter)) return Result.Failure;
    
        var iso_curve = surface.IsoCurve(direction, direction == 1 ? u_parameter : v_parameter);
        if (iso_curve == null) return Result.Failure;
    
        doc.Objects.AddCurve(iso_curve);
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ExtractIsoCurve(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select surface", False, ObjectType.Surface, obj_ref)
    	If rc IsNot Result.Success OrElse obj_ref Is Nothing Then
    	  Return rc
    	End If
    	Dim surface = obj_ref.Surface()
    
    	Dim gp = New GetPoint()
    	gp.SetCommandPrompt("Point on surface")
    	gp.Constrain(surface, False)
    	Dim option_toggle = New OptionToggle(False, "U", "V")
    	gp.AddOptionToggle("Direction", option_toggle)
    	Dim point As Point3d = Point3d.Unset
    	Do
    	  Dim grc = gp.Get()
    	  If grc Is GetResult.Option Then
    		Continue Do
    	  ElseIf grc Is GetResult.Point Then
    		point = gp.Point()
    		Exit Do
    	  Else
    		Return Result.Nothing
    	  End If
    	Loop
    	If point Is Point3d.Unset Then
    	  Return Result.Nothing
    	End If
    
    	Dim direction As Integer = If(option_toggle.CurrentValue, 1, 0) ' V : U
    	Dim u_parameter As Double = Nothing, v_parameter As Double = Nothing
    	If Not surface.ClosestPoint(point, u_parameter, v_parameter) Then
    		Return Result.Failure
    	End If
    
    	Dim iso_curve = surface.IsoCurve(direction,If(direction = 1, u_parameter, v_parameter))
    	If iso_curve Is Nothing Then
    		Return Result.Failure
    	End If
    
    	doc.Objects.AddCurve(iso_curve)
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Commands import *
    from Rhino.Input import *
    from Rhino.Input.Custom import *
    from Rhino.Geometry import *
    from scriptcontext import doc
    
    def RunCommand():
        rc, obj_ref = RhinoGet.GetOneObject("Select surface", False, ObjectType.Surface)
        if rc != Result.Success or obj_ref == None:
            return rc
        surface = obj_ref.Surface()
    
        gp = GetPoint()
        gp.SetCommandPrompt("Point on surface")
        gp.Constrain(surface, False)
        option_toggle = OptionToggle(False, "U", "V")
        gp.AddOptionToggle("Direction", option_toggle)
        point = Point3d.Unset
    
        while True:
            grc = gp.Get()
            if grc == GetResult.Option:
                continue
            elif grc == GetResult.Point:
                point = gp.Point()
                break
            else:
                return Result.Nothing
    
        if point == Point3d.Unset:
            return Result.Nothing
    
        direction = 1 if option_toggle.CurrentValue else 0
        b, u_parameter, v_parameter = surface.ClosestPoint(point)
        if not b: return Result.Failure
    
        iso_curve = surface.IsoCurve(direction, u_parameter if direction == 1 else v_parameter)
        if iso_curve == None:
            return Result.Failure
    
        doc.Objects.AddCurve(iso_curve)
        doc.Views.Redraw()
        return Result.Success
    
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

