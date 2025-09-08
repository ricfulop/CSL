---
url: https://developer.rhino3d.com/samples/rhinocommon/line-between-curves/
scraped_at: 2025-09-08T15:45:20.559485
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

Line Between Curves

Demonstrates how to draw a line between two user-specified curves.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result LineBetweenCurves(Rhino.RhinoDoc doc)
      {
        Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
        go.SetCommandPrompt("Select two curves");
        go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
        go.GetMultiple(2, 2);
        if (go.CommandResult() != Rhino.Commands.Result.Success)
          return go.CommandResult();
    
        Rhino.DocObjects.ObjRef objRef0 = go.Object(0);
        Rhino.DocObjects.ObjRef objRef1 = go.Object(1);
    
        double t0 = Rhino.RhinoMath.UnsetValue;
        double t1 = Rhino.RhinoMath.UnsetValue;
        Rhino.Geometry.Curve curve0 = objRef0.CurveParameter(out t0);
        Rhino.Geometry.Curve curve1 = objRef1.CurveParameter(out t1);
        if (null == curve0 || !Rhino.RhinoMath.IsValidDouble(t0) ||
            null == curve1 || !Rhino.RhinoMath.IsValidDouble(t1) )
          return Rhino.Commands.Result.Failure;
    
        Rhino.Geometry.Line line = Rhino.Geometry.Line.Unset;
        bool rc = Rhino.Geometry.Line.TryCreateBetweenCurves(curve0, curve1, ref t0, ref t1, false, false, out line);
        if (rc)
        {
          if (Guid.Empty != doc.Objects.AddLine(line))
          {
            doc.Views.Redraw();
            return Rhino.Commands.Result.Success;
          }
        }
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function LineBetweenCurves(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim go As New Rhino.Input.Custom.GetObject()
    	go.SetCommandPrompt("Select two curves")
    	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    	go.GetMultiple(2, 2)
    	If go.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return go.CommandResult()
    	End If
    
    	Dim objRef0 As Rhino.DocObjects.ObjRef = go.Object(0)
    	Dim objRef1 As Rhino.DocObjects.ObjRef = go.Object(1)
    
    	Dim t0 As Double = Rhino.RhinoMath.UnsetValue
    	Dim t1 As Double = Rhino.RhinoMath.UnsetValue
    	Dim curve0 As Rhino.Geometry.Curve = objRef0.CurveParameter(t0)
    	Dim curve1 As Rhino.Geometry.Curve = objRef1.CurveParameter(t1)
    	If Nothing Is curve0 OrElse Not Rhino.RhinoMath.IsValidDouble(t0) OrElse Nothing Is curve1 OrElse Not Rhino.RhinoMath.IsValidDouble(t1) Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim line As Rhino.Geometry.Line = Rhino.Geometry.Line.Unset
    	Dim rc As Boolean = Rhino.Geometry.Line.TryCreateBetweenCurves(curve0, curve1, t0, t1, False, False, line)
    	If rc Then
    	  If Guid.Empty <> doc.Objects.AddLine(line) Then
    		doc.Views.Redraw()
    		Return Rhino.Commands.Result.Success
    	  End If
    	End If
    	Return Rhino.Commands.Result.Failure
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

