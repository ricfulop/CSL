---
url: https://developer.rhino3d.com/samples/rhinocommon/add-cylinder/
scraped_at: 2025-09-08T15:44:21.368339
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

Add Cylinder

Demonstrates how to construct a cylinder using a center-point, height and
axis.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddCylinder(Rhino.RhinoDoc doc)
      {
        Rhino.Geometry.Point3d center_point = new Rhino.Geometry.Point3d(0, 0, 0);
        Rhino.Geometry.Point3d height_point = new Rhino.Geometry.Point3d(0, 0, 10);
        Rhino.Geometry.Vector3d zaxis = height_point - center_point;
        Rhino.Geometry.Plane plane = new Rhino.Geometry.Plane(center_point, zaxis);
        const double radius = 5;
        Rhino.Geometry.Circle circle = new Rhino.Geometry.Circle(plane, radius);
        Rhino.Geometry.Cylinder cylinder = new Rhino.Geometry.Cylinder(circle, zaxis.Length);
        Rhino.Geometry.Brep brep = cylinder.ToBrep(true, true);
        if (brep != null)
        {
          doc.Objects.AddBrep(brep);
          doc.Views.Redraw();
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddCylinder(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim center_point As New Rhino.Geometry.Point3d(0, 0, 0)
    	Dim height_point As New Rhino.Geometry.Point3d(0, 0, 10)
    	Dim zaxis As Rhino.Geometry.Vector3d = height_point - center_point
    	Dim plane As New Rhino.Geometry.Plane(center_point, zaxis)
    	Const radius As Double = 5
    	Dim circle As New Rhino.Geometry.Circle(plane, radius)
    	Dim cylinder As New Rhino.Geometry.Cylinder(circle, zaxis.Length)
    	Dim brep As Rhino.Geometry.Brep = cylinder.ToBrep(True, True)
    	If brep IsNot Nothing Then
    	  doc.Objects.AddBrep(brep)
    	  doc.Views.Redraw()
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddCylinder():
        center_point = Rhino.Geometry.Point3d(0, 0, 0)
        height_point = Rhino.Geometry.Point3d(0, 0, 10)
        zaxis = height_point-center_point
        plane = Rhino.Geometry.Plane(center_point, zaxis)
        radius = 5
        circle = Rhino.Geometry.Circle(plane, radius)
        cylinder = Rhino.Geometry.Cylinder(circle, zaxis.Length)
        brep = cylinder.ToBrep(True, True)
        if brep:
            if scriptcontext.doc.Objects.AddBrep(brep)!=System.Guid.Empty:
                scriptcontext.doc.Views.Redraw()
                return Rhino.Commands.Result.Success
        return Rhino.Commands.Result.Failure
    
    if __name__=="__main__":
        AddCylinder()
    

  

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

