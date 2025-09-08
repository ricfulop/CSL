---
url: https://developer.rhino3d.com/samples/rhinocommon/offset-curve/
scraped_at: 2025-09-08T15:45:21.578352
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

Offset Curve

Demonstrates how to offset curves to one side or another by a distance.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result OffsetCurve(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rs = RhinoGet.GetOneObject(
          "Select Curve", false, ObjectType.Curve, out obj_ref);
        if (rs != Result.Success)
          return rs;
        var curve = obj_ref.Curve();
        if (curve == null)
          return Result.Nothing;
    
        Point3d point;
        rs = RhinoGet.GetPoint("Select Side", false, out point);
        if (rs != Result.Success)
          return rs;
        if (point == Point3d.Unset)
          return Result.Nothing;
    
        var curves = curve.Offset(point, Vector3d.ZAxis, 1.0,
          doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.None);
    
        foreach (var offset-curve in curves)
          doc.Objects.AddCurve(offset-curve);
    
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function OffsetCurve(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rs = RhinoGet.GetOneObject("Select Curve", False, ObjectType.Curve, obj_ref)
    	If rs IsNot Result.Success Then
    	  Return rs
    	End If
    	Dim curve = obj_ref.Curve()
    	If curve Is Nothing Then
    	  Return Result.Nothing
    	End If
    
    	Dim point As Point3d = Nothing
    	rs = RhinoGet.GetPoint("Select Side", False, point)
    	If rs IsNot Result.Success Then
    	  Return rs
    	End If
    	If point Is Point3d.Unset Then
    	  Return Result.Nothing
    	End If
    
    	Dim curves = curve.Offset(point, Vector3d.ZAxis, 1.0, doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.None)
    
    	For Each offset-curve In curves
    	  doc.Objects.AddCurve(offset-curve)
    	Next offset-curve
    
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Geometry import *
    from Rhino.Input import *
    from Rhino.Commands import *
    from scriptcontext import doc
    import rhinoscriptsyntax as rs
    
    def RunCommand():
        rc, obj_ref = RhinoGet.GetOneObject("Select Curve", False, ObjectType.Curve)
        if rc != Result.Success:
            return rc
        curve = obj_ref.Curve()
        if curve == None:
            return Result.Nothing
    
        rc, point = RhinoGet.GetPoint("Select Side", False)
        if rc != Result.Success:
            return rc
        if point == Point3d.Unset:
            return Result.Nothing
    
        curves = curve.Offset(point, Vector3d.ZAxis, 1.0, doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.None)
    
        for offset_curve in curves:
            doc.Objects.AddCurve(offset_curve)
    
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

