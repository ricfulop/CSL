---
url: https://developer.rhino3d.com/samples/rhinocommon/add-nurbs-curve/
scraped_at: 2025-09-08T15:44:33.398378
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

Add NURBS Curve

Demonstrates how to create a NURBS curve from a list of points.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddNurbsCurve(Rhino.RhinoDoc doc)
      {
        Rhino.Collections.Point3dList points = new Rhino.Collections.Point3dList(5);
        points.Add(0, 0, 0);
        points.Add(0, 2, 0);
        points.Add(2, 3, 0);
        points.Add(4, 2, 0);
        points.Add(4, 0, 0);
        Rhino.Geometry.NurbsCurve nc = Rhino.Geometry.NurbsCurve.Create(false, 3, points);
        Rhino.Commands.Result rc = Rhino.Commands.Result.Failure;
        if (nc != null && nc.IsValid)
        {
          if (doc.Objects.AddCurve(nc) != Guid.Empty)
          {
            doc.Views.Redraw();
            rc = Rhino.Commands.Result.Success;
          }
        }
        return rc;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddNurbsCurve(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim points As New Rhino.Collections.Point3dList(5)
    	points.Add(0, 0, 0)
    	points.Add(0, 2, 0)
    	points.Add(2, 3, 0)
    	points.Add(4, 2, 0)
    	points.Add(4, 0, 0)
    	Dim nc As Rhino.Geometry.NurbsCurve = Rhino.Geometry.NurbsCurve.Create(False, 3, points)
    	Dim rc As Rhino.Commands.Result = Rhino.Commands.Result.Failure
    	If nc IsNot Nothing AndAlso nc.IsValid Then
    	  If doc.Objects.AddCurve(nc) <> Guid.Empty Then
    		doc.Views.Redraw()
    		rc = Rhino.Commands.Result.Success
    	  End If
    	End If
    	Return rc
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddNurbsCurve():
        points = Rhino.Collections.Point3dList(5)
        points.Add(0, 0, 0)
        points.Add(0, 2, 0)
        points.Add(2, 3, 0)
        points.Add(4, 2, 0)
        points.Add(4, 0, 0)
    
        nc = Rhino.Geometry.NurbsCurve.Create(False, 3, points)
        rc = Rhino.Commands.Result.Failure
        if nc and nc.IsValid:
            if scriptcontext.doc.Objects.AddCurve(nc)!=System.Guid.Empty:
                scriptcontext.doc.Views.Redraw()
                rc = Rhino.Commands.Result.Success
        return rc
    
    if __name__=="__main__":
        AddNurbsCurve()
    

  

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

