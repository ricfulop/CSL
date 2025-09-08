---
url: https://developer.rhino3d.com/samples/rhinocommon/add-nurbs-circle/
scraped_at: 2025-09-08T15:44:32.360357
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

Add NURBS Circle

Demonstrates how to create a NURBS circle from scratch using points and knots.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddNurbsCircle(Rhino.RhinoDoc doc)
      {
        // The easy way to get a NURBS curve from a circle is with
        // the following two lines of code.
        //
        // Rhino.Geometry.Circle c = new Rhino.Geometry.Circle(20);
        // Rhino.Geometry.NurbsCurve nc = c.ToNurbsCurve();
        //
        // This sample demonstrates creating a NURBS curve from scratch.
        const int dimension = 3;
        const bool isRational = true;
        const int order = 3;
        const int cv_count = 9;
        Rhino.Geometry.NurbsCurve nc = new Rhino.Geometry.NurbsCurve(dimension, isRational, order, cv_count);
        nc.Points.SetPoint(0, 1.0, 0.0, 0.0, 1.0);
        nc.Points.SetPoint(1, 0.707107, 0.707107, 0.0, 0.707107);
        nc.Points.SetPoint(2, 0.0, 1.0, 0.0, 1.0);
        nc.Points.SetPoint(3, -0.707107, 0.707107, 0.0, 0.707107);
        nc.Points.SetPoint(4, -1.0, 0.0, 0.0, 1.0);
        nc.Points.SetPoint(5, -0.707107, -0.707107, 0.0, 0.707107);
        nc.Points.SetPoint(6, 0.0, -1.0, 0.0, 1.0);
        nc.Points.SetPoint(7, 0.707107, -0.707107, 0.0, 0.707107);
        nc.Points.SetPoint(8, 1.0, 0.0, 0.0, 1.0);
        nc.Knots[0] = 0.0;
        nc.Knots[1] = 0.0;
        nc.Knots[2] = 0.5 * Math.PI;
        nc.Knots[3] = 0.5 * Math.PI;
        nc.Knots[4] = Math.PI;
        nc.Knots[5] = Math.PI;
        nc.Knots[6] = 1.5 * Math.PI;
        nc.Knots[7] = 1.5 * Math.PI;
        nc.Knots[8] = 2.0 * Math.PI;
        nc.Knots[9] = 2.0 * Math.PI;
        if (nc.IsValid)
        {
          doc.Objects.AddCurve(nc);
          doc.Views.Redraw();
          return Rhino.Commands.Result.Success;
        }
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddNurbsCircle(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	' The easy way to get a NURBS curve from a circle is with
    	' the following two lines of code.
    	'
    	' Rhino.Geometry.Circle c = new Rhino.Geometry.Circle(20);
    	' Rhino.Geometry.NurbsCurve nc = c.ToNurbsCurve();
    	'
    	' This sample demonstrates creating a NURBS curve from scratch.
    	Const dimension As Integer = 3
    	Const isRational As Boolean = True
    	Const order As Integer = 3
    	Const cv_count As Integer = 9
    	Dim nc As New Rhino.Geometry.NurbsCurve(dimension, isRational, order, cv_count)
    	nc.Points.SetPoint(0, 1.0, 0.0, 0.0, 1.0)
    	nc.Points.SetPoint(1, 0.707107, 0.707107, 0.0, 0.707107)
    	nc.Points.SetPoint(2, 0.0, 1.0, 0.0, 1.0)
    	nc.Points.SetPoint(3, -0.707107, 0.707107, 0.0, 0.707107)
    	nc.Points.SetPoint(4, -1.0, 0.0, 0.0, 1.0)
    	nc.Points.SetPoint(5, -0.707107, -0.707107, 0.0, 0.707107)
    	nc.Points.SetPoint(6, 0.0, -1.0, 0.0, 1.0)
    	nc.Points.SetPoint(7, 0.707107, -0.707107, 0.0, 0.707107)
    	nc.Points.SetPoint(8, 1.0, 0.0, 0.0, 1.0)
    	nc.Knots(0) = 0.0
    	nc.Knots(1) = 0.0
    	nc.Knots(2) = 0.5 * Math.PI
    	nc.Knots(3) = 0.5 * Math.PI
    	nc.Knots(4) = Math.PI
    	nc.Knots(5) = Math.PI
    	nc.Knots(6) = 1.5 * Math.PI
    	nc.Knots(7) = 1.5 * Math.PI
    	nc.Knots(8) = 2.0 * Math.PI
    	nc.Knots(9) = 2.0 * Math.PI
    	If nc.IsValid Then
    	  doc.Objects.AddCurve(nc)
    	  doc.Views.Redraw()
    	  Return Rhino.Commands.Result.Success
    	End If
    	Return Rhino.Commands.Result.Failure
      End Function
    End Class
    
    
    
    import System
    from Rhino.Geometry import NurbsCurve
    from Rhino.Commands import Result
    from scriptcontext import doc
    
    def AddNurbsCircle():
        # The easy way to get a NURBS curve from a circle is with
        # the following two lines of code.
        #
        # Circle c = new Circle(20)
        # NurbsCurve nc = c.ToNurbsCurve()
        #
        # This sample demonstrates creating a NURBS curve from scratch.
        dimension = 3
        isRational = True
        order = 3
        cv_count = 9
        nc = NurbsCurve(dimension, isRational, order, cv_count)
        nc.Points.SetPoint(0, 1.0, 0.0, 0.0, 1.0)
        nc.Points.SetPoint(1, 1.0, 1.0, 0.0, 0.707107)
        nc.Points.SetPoint(2, 0.0, 1.0, 0.0, 1.0)
        nc.Points.SetPoint(3, -1.0, 1.0, 0.0, 0.707107)
        nc.Points.SetPoint(4, -1.0, 0.0, 0.0, 1.0)
        nc.Points.SetPoint(5, -1.0, -1.0, 0.0, 0.707107)
        nc.Points.SetPoint(6, 0.0, -1.0, 0.0, 1.0)
        nc.Points.SetPoint(7, 1.0, -1.0, 0.0, 0.707107)
        nc.Points.SetPoint(8, 1.0, 0.0, 0.0, 1.0)
        nc.Knots[0] = 0.0
        nc.Knots[1] = 0.0
        nc.Knots[2] = 0.5 * System.Math.PI
        nc.Knots[3] = 0.5 * System.Math.PI
        nc.Knots[4] = System.Math.PI
        nc.Knots[5] = System.Math.PI
        nc.Knots[6] = 1.5 * System.Math.PI
        nc.Knots[7] = 1.5 * System.Math.PI
        nc.Knots[8] = 2.0 * System.Math.PI
        nc.Knots[9] = 2.0 * System.Math.PI
        if nc.IsValid:
            doc.Objects.AddCurve(nc)
            doc.Views.Redraw()
            return Result.Success
        return Result.Failure
    
    if __name__=="__main__":
        AddNurbsCircle()
    

  

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

