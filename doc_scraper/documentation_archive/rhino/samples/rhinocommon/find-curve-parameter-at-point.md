---
url: https://developer.rhino3d.com/samples/rhinocommon/find-curve-parameter-at-point/
scraped_at: 2025-09-08T15:45:15.557437
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

Find Curve Parameter At Point

Demonstrates how to find the curve parameter given a specific point on the
curve.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result FindCurveParameterAtPoint(RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef objref;
        var rc = RhinoGet.GetOneObject("Select curve", true, ObjectType.Curve,out objref);
        if(rc!= Result.Success)
          return rc;
        var curve = objref.Curve();
        if( curve==null )
          return Result.Failure;
    
        var gp = new GetPoint();
        gp.SetCommandPrompt("Pick a location on the curve");
        gp.Constrain(curve, false);
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
    
        var point = gp.Point();
        double closest_point_param;
        if (curve.ClosestPoint(point, out closest_point_param))
        {
          RhinoApp.WriteLine("point: ({0}), parameter: {1}", point, closest_point_param);
          doc.Objects.AddPoint(point);
          doc.Views.Redraw();
        }
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function FindCurveParameterAtPoint(ByVal doc As RhinoDoc) As Result
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select curve", True, ObjectType.Curve,objref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim curve = objref.Curve()
    	If curve Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	Dim gp = New GetPoint()
    	gp.SetCommandPrompt("Pick a location on the curve")
    	gp.Constrain(curve, False)
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    
    	Dim point = gp.Point()
    	Dim closest_point_param As Double = Nothing
    	If curve.ClosestPoint(point, closest_point_param) Then
    	  RhinoApp.WriteLine("point: ({0}), parameter: {1}", point, closest_point_param)
    	  doc.Objects.AddPoint(point)
    	  doc.Views.Redraw()
    	End If
    	Return Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import rhinoscriptsyntax as rs
    
    def RunCommand():
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve", True, Rhino.DocObjects.ObjectType.Curve)
        if(rc!= Rhino.Commands.Result.Success):
            return rc
        crv = objref.Curve()
        if( crv == None ):
            return Rhino.Commands.Result.Failure
    
        gp = Rhino.Input.Custom.GetPoint()
        gp.SetCommandPrompt("Pick a location on the curve")
        gp.Constrain(crv, False)
        gp.Get()
        if (gp.CommandResult() != Rhino.Commands.Result.Success):
            return gp.CommandResult();
    
        p = gp.Point()
        b, cp = crv.ClosestPoint(p)
        if (b):
            print "point: ({0},{1},{2}), parameter: {3}".format(p.X, p.Y, p.Z, cp)
            scriptcontext.doc.Objects.AddPoint(p)
            scriptcontext.doc.Views.Redraw()
    
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
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

