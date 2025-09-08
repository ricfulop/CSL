---
url: https://developer.rhino3d.com/samples/rhinocommon/increase-nurbs-curve-degree/
scraped_at: 2025-09-08T15:45:18.576405
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

Increase NURBS Curve Degree

Demonstrates how to increase the degree of a NURBS curve.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result NurbsCurveIncreaseDegree(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject(
          "Select curve", false, ObjectType.Curve, out obj_ref);
        if (rc != Result.Success) return rc;
        if (obj_ref == null) return Result.Failure;
        var curve = obj_ref.Curve();
        if (curve == null) return Result.Failure;
        var nurbs_curve = curve.ToNurbsCurve();
    
        int new_degree = -1;
        rc = RhinoGet.GetInteger(string.Format("New degree <{0}...11>", nurbs_curve.Degree), true, ref new_degree,
          nurbs_curve.Degree, 11);
        if (rc != Result.Success) return rc;
    
        rc = Result.Failure;
        if (nurbs_curve.IncreaseDegree(new_degree))
          if (doc.Objects.Replace(obj_ref.ObjectId, nurbs_curve))
            rc = Result.Success;
    
        RhinoApp.WriteLine("Result: {0}", rc.ToString());
        doc.Views.Redraw();
        return rc;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function NurbsCurveIncreaseDegree(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select curve", False, ObjectType.Curve, obj_ref)
    	If rc IsNot Result.Success Then
    		Return rc
    	End If
    	If obj_ref Is Nothing Then
    		Return Result.Failure
    	End If
    	Dim curve = obj_ref.Curve()
    	If curve Is Nothing Then
    		Return Result.Failure
    	End If
    	Dim nurbs_curve = curve.ToNurbsCurve()
    
    	Dim new_degree As Integer = -1
    	rc = RhinoGet.GetInteger(String.Format("New degree <{0}...11>", nurbs_curve.Degree), True, new_degree, nurbs_curve.Degree, 11)
    	If rc IsNot Result.Success Then
    		Return rc
    	End If
    
    	rc = Result.Failure
    	If nurbs_curve.IncreaseDegree(new_degree) Then
    	  If doc.Objects.Replace(obj_ref.ObjectId, nurbs_curve) Then
    		rc = Result.Success
    	  End If
    	End If
    
    	RhinoApp.WriteLine("Result: {0}", rc.ToString())
    	doc.Views.Redraw()
    	Return rc
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.Commands import *
    from Rhino.Input import *
    from Rhino.DocObjects import *
    from scriptcontext import doc
    
    def RunCommand():
        rc, obj_ref = RhinoGet.GetOneObject("Select curve", False, ObjectType.Curve)
        if rc != Result.Success: return rc
        if obj_ref == None: return Result.Failure
        curve = obj_ref.Curve()
        if curve == None: return Result.Failure
        nurbs_curve = curve.ToNurbsCurve()
    
        new_degree = -1
        rc, new_degree = RhinoGet.GetInteger("New degree <{0}...11>".format(nurbs_curve.Degree), True, new_degree, nurbs_curve.Degree, 11)
        if rc != Result.Success: return rc
    
        rc = Result.Failure
        if nurbs_curve.IncreaseDegree(new_degree):
            if doc.Objects.Replace(obj_ref.ObjectId, nurbs_curve):
                rc = Result.Success
    
        print "Result: {0}".format(rc)
        doc.Views.Redraw()
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

