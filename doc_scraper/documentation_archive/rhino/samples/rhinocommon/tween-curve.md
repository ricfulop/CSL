---
url: https://developer.rhino3d.com/samples/rhinocommon/tween-curve/
scraped_at: 2025-09-08T15:45:25.596646
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

Tween Curve

Demonstrates how to tween two curves.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result TweenCurve(Rhino.RhinoDoc doc)
      {
        Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
        go.SetCommandPrompt("Select two curves");
        go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
        go.GetMultiple(2, 2);
        if (go.CommandResult() != Rhino.Commands.Result.Success)
          return go.CommandResult();
    
        Rhino.Geometry.Curve curve0 = go.Object(0).Curve();
        Rhino.Geometry.Curve curve1 = go.Object(1).Curve();
        if (null != curve0 && null != curve1)
        {
          Rhino.Geometry.Curve[] curves = Rhino.Geometry.Curve.CreateTweenCurves(curve0, curve1, 1);
          if (null != curves)
          {
            for (int i = 0; i < curves.Length; i++)
              doc.Objects.AddCurve(curves[i]);
    
            doc.Views.Redraw();
            return Rhino.Commands.Result.Success;
          }
        }
    
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function TweenCurve(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim go As New Rhino.Input.Custom.GetObject()
    	go.SetCommandPrompt("Select two curves")
    	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    	go.GetMultiple(2, 2)
    	If go.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return go.CommandResult()
    	End If
    
    	Dim curve0 As Rhino.Geometry.Curve = go.Object(0).Curve()
    	Dim curve1 As Rhino.Geometry.Curve = go.Object(1).Curve()
    	If Nothing IsNot curve0 AndAlso Nothing IsNot curve1 Then
    	  Dim curves() As Rhino.Geometry.Curve = Rhino.Geometry.Curve.CreateTweenCurves(curve0, curve1, 1)
    	  If Nothing IsNot curves Then
    		For i As Integer = 0 To curves.Length - 1
    		  doc.Objects.AddCurve(curves(i))
    		Next i
    
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

