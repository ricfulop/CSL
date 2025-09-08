---
url: https://developer.rhino3d.com/samples/rhinocommon/find-point-on-curve-at-distance/
scraped_at: 2025-09-08T15:45:16.561459
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

Find point on curve at distance

Demonstrates how find a point on a curve given a specified length from the
start of the curve.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result ArcLengthPoint(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef objref;
        Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select curve",
          true, Rhino.DocObjects.ObjectType.Curve,out objref);
        if(rc!= Rhino.Commands.Result.Success)
          return rc;
        Rhino.Geometry.Curve crv = objref.Curve();
        if( crv==null )
          return Rhino.Commands.Result.Failure;
    
        double crv_length = crv.GetLength();
        double length = 0;
        rc = Rhino.Input.RhinoGet.GetNumber("Length from start", true, ref length, 0, crv_length);
        if(rc!= Rhino.Commands.Result.Success)
          return rc;
    
        Rhino.Geometry.Point3d pt = crv.PointAtLength(length);
        if (pt.IsValid)
        {
          doc.Objects.AddPoint(pt);
          doc.Views.Redraw();
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ArcLengthPoint(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select curve", True, Rhino.DocObjects.ObjectType.Curve,objref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    	Dim crv As Rhino.Geometry.Curve = objref.Curve()
    	If crv Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim crv_length As Double = crv.GetLength()
    	Dim length As Double = 0
    	rc = Rhino.Input.RhinoGet.GetNumber("Length from start", True, length, 0, crv_length)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	Dim pt As Rhino.Geometry.Point3d = crv.PointAtLength(length)
    	If pt.IsValid Then
    	  doc.Objects.AddPoint(pt)
    	  doc.Views.Redraw()
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def ArcLengthPoint():
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve", True, Rhino.DocObjects.ObjectType.Curve)
        if rc!=Rhino.Commands.Result.Success: return rc
        crv = objref.Curve()
        if not crv: return Rhino.Commands.Result.Failure
        crv_length = crv.GetLength()
        length = 0
        rc, length = Rhino.Input.RhinoGet.GetNumber("Length from start", True, length, 0, crv_length)
        if rc!=Rhino.Commands.Result.Success: return rc
        pt = crv.PointAtLength(length)
        if pt.IsValid:
            scriptcontext.doc.Objects.AddPoint(pt)
            scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        ArcLengthPoint()
    

  

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

