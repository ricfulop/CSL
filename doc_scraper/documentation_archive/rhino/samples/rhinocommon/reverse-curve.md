---
url: https://developer.rhino3d.com/samples/rhinocommon/reverse-curve/
scraped_at: 2025-09-08T15:45:23.566444
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

Reverse Curve

Demonstrates how to reverse the direction of user-specified curves.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ReverseCurve(RhinoDoc doc)
      {
        ObjRef[] obj_refs;
        var rc = RhinoGet.GetMultipleObjects("Select curves to reverse", true, ObjectType.Curve, out obj_refs);
        if (rc != Result.Success)
          return rc;
    
        foreach (var obj_ref in obj_refs)
        {
          var curve_copy = obj_ref.Curve().DuplicateCurve();
          if (curve_copy != null)
          {
            curve_copy.Reverse();
            doc.Objects.Replace(obj_ref, curve_copy);
          }
        }
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ReverseCurve(ByVal doc As RhinoDoc) As Result
    	Dim obj_refs() As ObjRef = Nothing
    	Dim rc = RhinoGet.GetMultipleObjects("Select curves to reverse", True, ObjectType.Curve, obj_refs)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    
    	For Each obj_ref In obj_refs
    	  Dim curve_copy = obj_ref.Curve().DuplicateCurve()
    	  If curve_copy IsNot Nothing Then
    		curve_copy.Reverse()
    		doc.Objects.Replace(obj_ref, curve_copy)
    	  End If
    	Next obj_ref
    	Return Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    from scriptcontext import *
    import Rhino
    
    def ReverseCurves():
        crvs = rs.GetObjects("Select curves to reverse", rs.filter.curve)
        if not crvs: return
    
        for crvid in crvs:
            crv = rs.coercecurve(crvid)
            if not crv: continue
            dup = crv.DuplicateCurve()
            if dup:
                dup.Reverse()
            doc.Objects.Replace(crvid, dup)
    
    if __name__ == "__main__":
        ReverseCurves()
    

  

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

