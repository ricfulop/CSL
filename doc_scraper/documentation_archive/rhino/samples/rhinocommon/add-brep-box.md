---
url: https://developer.rhino3d.com/samples/rhinocommon/add-brep-box/
scraped_at: 2025-09-08T15:44:15.292350
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

Add Brep Box

Demonstrates how to add a Brep Box to a Rhino model by specifying two points.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddBrepBox(Rhino.RhinoDoc doc)
      {
        Rhino.Geometry.Point3d pt0 = new Rhino.Geometry.Point3d(0, 0, 0);
        Rhino.Geometry.Point3d pt1 = new Rhino.Geometry.Point3d(10, 10, 10);
        Rhino.Geometry.BoundingBox box = new Rhino.Geometry.BoundingBox(pt0, pt1);
        Rhino.Geometry.Brep brep = box.ToBrep();
        Rhino.Commands.Result rc = Rhino.Commands.Result.Failure;
        if( doc.Objects.AddBrep(brep) != System.Guid.Empty )
        {
          rc = Rhino.Commands.Result.Success;
          doc.Views.Redraw();
        }
        return rc;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddBrepBox(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim pt0 As New Rhino.Geometry.Point3d(0, 0, 0)
    	Dim pt1 As New Rhino.Geometry.Point3d(10, 10, 10)
    	Dim box As New Rhino.Geometry.BoundingBox(pt0, pt1)
    	Dim brep As Rhino.Geometry.Brep = box.ToBrep()
    	Dim rc As Rhino.Commands.Result = Rhino.Commands.Result.Failure
    	If doc.Objects.AddBrep(brep) <> System.Guid.Empty Then
    	  rc = Rhino.Commands.Result.Success
    	  doc.Views.Redraw()
    	End If
    	Return rc
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddBrepBox():
        pt0 = Rhino.Geometry.Point3d(0, 0, 0)
        pt1 = Rhino.Geometry.Point3d(10, 10, 10)
        box = Rhino.Geometry.BoundingBox(pt0, pt1)
        brep = box.ToBrep()
        rc = Rhino.Commands.Result.Failure
        if( scriptcontext.doc.Objects.AddBrep(brep) != System.Guid.Empty ):
            rc = Rhino.Commands.Result.Success
            scriptcontext.doc.Views.Redraw()
        return rc
    
    if( __name__ == "__main__" ):
        AddBrepBox()
    

  

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

