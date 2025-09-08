---
url: https://developer.rhino3d.com/samples/rhinocommon/reparameterize-curves/
scraped_at: 2025-09-08T15:45:22.570939
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

Reparameterize Curves

Demonstrates how to reparameterize - or change the domain of - user-specified
curves.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ReparameterizeCurve(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select curve to reparameterize", false, ObjectType.Curve, out obj_ref);
        if (rc != Result.Success)
          return rc;
        var curve = obj_ref.Curve();
        if (curve == null)
          return Result.Failure;
    
        double domain_start = 0;
        rc = RhinoGet.GetNumber("Domain start", false, ref domain_start);
        if (rc != Result.Success)
          return rc;
    
        double domain_end = 0;
        rc = RhinoGet.GetNumber("Domain end", false, ref domain_end);
        if (rc != Result.Success)
          return rc;
    
        if (Math.Abs(curve.Domain.T0 - domain_start) < RhinoMath.ZeroTolerance &&
            Math.Abs(curve.Domain.T1 - domain_end) < RhinoMath.ZeroTolerance)
          return Result.Nothing;
    
        var curve_copy = curve.DuplicateCurve();
        curve_copy.Domain = new Interval(domain_start, domain_end);
        if (!doc.Objects.Replace(obj_ref, curve_copy))
          return Result.Failure;
        else
        {
          doc.Views.Redraw();
          return Result.Success;
        }
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ReparameterizeCurve(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select curve to reparameterize", False, ObjectType.Curve, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim curve = obj_ref.Curve()
    	If curve Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	Dim domain_start As Double = 0
    	rc = RhinoGet.GetNumber("Domain start", False, domain_start)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    
    	Dim domain_end As Double = 0
    	rc = RhinoGet.GetNumber("Domain end", False, domain_end)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    
    	If Math.Abs(curve.Domain.T0 - domain_start) < RhinoMath.ZeroTolerance AndAlso Math.Abs(curve.Domain.T1 - domain_end) < RhinoMath.ZeroTolerance Then
    	  Return Result.Nothing
    	End If
    
    	Dim curve_copy = curve.DuplicateCurve()
    	curve_copy.Domain = New Interval(domain_start, domain_end)
    	If Not doc.Objects.Replace(obj_ref, curve_copy) Then
    	  Return Result.Failure
    	Else
    	  doc.Views.Redraw()
    	  Return Result.Success
    	End If
      End Function
    End Class
    
    
    
    from System import *
    from  Rhino import *
    from  Rhino.Commands import *
    from  Rhino.DocObjects import *
    from  Rhino.Geometry import *
    from  Rhino.Input import *
    from scriptcontext import doc
    
    def RunCommand():
    
        rc, obj_ref = RhinoGet.GetOneObject("Select curve to reparameterize", False, ObjectType.Curve)
        if rc != Result.Success:
            return rc
        curve = obj_ref.Curve()
        if curve == None:
            return Result.Failure
    
        domain_start = 0
        rc, domain_start = RhinoGet.GetNumber("Domain start", False, domain_start)
        if rc != Result.Success:
            return rc
    
        domain_end = 100
        rc, domain_end = RhinoGet.GetNumber("Domain end", False, domain_end)
        if rc != Result.Success:
            return rc
    
        if Math.Abs(curve.Domain.T0 - domain_start) < RhinoMath.ZeroTolerance and \
            Math.Abs(curve.Domain.T1 - domain_end) < RhinoMath.ZeroTolerance:
            return Result.Nothing
    
        curve_copy = curve.DuplicateCurve()
        curve_copy.Domain = Interval(domain_start, domain_end)
        if not doc.Objects.Replace(obj_ref, curve_copy):
            return Result.Failure
        else:
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

