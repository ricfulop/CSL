---
url: https://developer.rhino3d.com/samples/rhinocommon/add-truncated-cone/
scraped_at: 2025-09-08T15:44:38.373342
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

Add Truncated Cone

Demonstrates how to construct a truncated cone (TCone) from two circles.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddTruncatedCone(Rhino.RhinoDoc doc)
      {
        Point3d bottom_pt = new Point3d(0,0,0);
        const double bottom_radius = 2;
        Circle bottom_circle = new Circle(bottom_pt, bottom_radius);
    
        Point3d top_pt = new Point3d(0,0,10);
        const double top_radius = 6;
        Circle top_circle = new Circle(top_pt, top_radius);
    
        LineCurve shapeCurve = new LineCurve(bottom_circle.PointAt(0), top_circle.PointAt(0));
        Line axis = new Line(bottom_circle.Center, top_circle.Center);
        RevSurface revsrf = RevSurface.Create(shapeCurve, axis);
        Brep tcone_brep = Brep.CreateFromRevSurface(revsrf, true, true);
        if( doc.Objects.AddBrep(tcone_brep) != Guid.Empty )
        {
          doc.Views.Redraw();
          return Rhino.Commands.Result.Success;
        }
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddTruncatedCone(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim bottom_pt As New Point3d(0,0,0)
    	Const bottom_radius As Double = 2
    	Dim bottom_circle As New Circle(bottom_pt, bottom_radius)
    
    	Dim top_pt As New Point3d(0,0,10)
    	Const top_radius As Double = 6
    	Dim top_circle As New Circle(top_pt, top_radius)
    
    	Dim shapeCurve As New LineCurve(bottom_circle.PointAt(0), top_circle.PointAt(0))
    	Dim axis As New Line(bottom_circle.Center, top_circle.Center)
    	Dim revsrf As RevSurface = RevSurface.Create(shapeCurve, axis)
    	Dim tcone_brep As Brep = Brep.CreateFromRevSurface(revsrf, True, True)
    	If doc.Objects.AddBrep(tcone_brep) <> Guid.Empty Then
    	  doc.Views.Redraw()
    	  Return Rhino.Commands.Result.Success
    	End If
    	Return Rhino.Commands.Result.Failure
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddTruncatedCone():
        bottom_pt = Rhino.Geometry.Point3d(0,0,0)
        bottom_radius = 2
        bottom_circle = Rhino.Geometry.Circle(bottom_pt, bottom_radius)
    
        top_pt = Rhino.Geometry.Point3d(0,0,10)
        top_radius = 6
        top_circle = Rhino.Geometry.Circle(top_pt, top_radius)
    
        shapeCurve = Rhino.Geometry.LineCurve(bottom_circle.PointAt(0), top_circle.PointAt(0))
        axis = Rhino.Geometry.Line(bottom_circle.Center, top_circle.Center)
        revsrf = Rhino.Geometry.RevSurface.Create(shapeCurve, axis)
        tcone_brep = Rhino.Geometry.Brep.CreateFromRevSurface(revsrf, True, True)
    
        if scriptcontext.doc.Objects.AddBrep(tcone_brep)!=System.Guid.Empty:
            scriptcontext.doc.Views.Redraw()
            return Rhino.Commands.Result.Success
        return Rhino.Commands.Result.Failure
    
    
    if __name__=="__main__":
        AddTruncatedCone()
    

  

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

