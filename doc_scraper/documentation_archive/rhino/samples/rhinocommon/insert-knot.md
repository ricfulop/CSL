---
url: https://developer.rhino3d.com/samples/rhinocommon/insert-knot/
scraped_at: 2025-09-08T15:46:14.811189
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

Insert Knot

Demonstrates how to insert a knot into a user-selected NURBS curve.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result InsertKnot(Rhino.RhinoDoc doc)
      {
        const ObjectType filter = Rhino.DocObjects.ObjectType.Curve;
        Rhino.DocObjects.ObjRef objref;
        Result rc = Rhino.Input.RhinoGet.GetOneObject("Select curve for knot insertion", false, filter, out objref);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
        Rhino.Geometry.Curve curve = objref.Curve();
        if (null == curve)
          return Rhino.Commands.Result.Failure;
        Rhino.Geometry.NurbsCurve nurb = curve.ToNurbsCurve();
        if (null == nurb)
          return Rhino.Commands.Result.Failure;
    
        Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
        gp.SetCommandPrompt("Point on curve to add knot");
        gp.Constrain(nurb, false);
        gp.Get();
        if (gp.CommandResult() == Rhino.Commands.Result.Success)
        {
          double t;
          Rhino.Geometry.Curve crv = gp.PointOnCurve(out t);
          if( crv!=null && nurb.Knots.InsertKnot(t) )
          {
            doc.Objects.Replace(objref, nurb);
            doc.Views.Redraw();
          }
        }
        return Rhino.Commands.Result.Success;  
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function InsertKnot(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Curve
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc As Result = Rhino.Input.RhinoGet.GetOneObject("Select curve for knot insertion", False, filter, objref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    	Dim curve As Rhino.Geometry.Curve = objref.Curve()
    	If Nothing Is curve Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    	Dim nurb As Rhino.Geometry.NurbsCurve = curve.ToNurbsCurve()
    	If Nothing Is nurb Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim gp As New Rhino.Input.Custom.GetPoint()
    	gp.SetCommandPrompt("Point on curve to add knot")
    	gp.Constrain(nurb, False)
    	gp.Get()
    	If gp.CommandResult() = Rhino.Commands.Result.Success Then
    	  Dim t As Double = Nothing
    	  Dim crv As Rhino.Geometry.Curve = gp.PointOnCurve(t)
    	  If crv IsNot Nothing AndAlso nurb.Knots.InsertKnot(t) Then
    		doc.Objects.Replace(objref, nurb)
    		doc.Views.Redraw()
    	  End If
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def InsertKnot():
        filter = Rhino.DocObjects.ObjectType.Curve
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve for knot insertion", False, filter)
        if rc != Rhino.Commands.Result.Success: return rc
    
        curve = objref.Curve()
        if not curve: return Rhino.Commands.Result.Failure
        nurb = curve.ToNurbsCurve()
        if not nurb: return Rhino.Commands.Result.Failure
    
        gp = Rhino.Input.Custom.GetPoint()
        gp.SetCommandPrompt("Point on curve to add knot")
        gp.Constrain(nurb, False)
        gp.Get()
        if gp.CommandResult() == Rhino.Commands.Result.Success:
            crv, t = gp.PointOnCurve()
            if crv and nurb.Knots.InsertKnot(t):
                scriptcontext.doc.Objects.Replace(objref, nurb)
                scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        InsertKnot()
    

  

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

