---
url: https://developer.rhino3d.com/samples/rhinocommon/unroll-surface/
scraped_at: 2025-09-08T15:46:47.979980
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

Unroll Surface

Unrolling a developable surface

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result UnrollSurface(Rhino.RhinoDoc doc)
      {
        const ObjectType filter = Rhino.DocObjects.ObjectType.Brep | Rhino.DocObjects.ObjectType.Surface;
        Rhino.DocObjects.ObjRef objref;
        Result rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", false, filter, out objref);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
        Rhino.Geometry.Unroller unroll=null;
        Rhino.Geometry.Brep brep = objref.Brep();
        if (brep != null)
          unroll = new Rhino.Geometry.Unroller(brep);
        else
        {
          Rhino.Geometry.Surface srf = objref.Surface();
          if (srf != null)
            unroll = new Rhino.Geometry.Unroller(srf);
        }
        if (unroll == null)
          return Rhino.Commands.Result.Cancel;
    
        unroll.AbsoluteTolerance = 0.01;
        unroll.RelativeTolerance = 0.01;
    
        Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
        go.SetCommandPrompt("Select points, curves, and dots to unroll with surface");
        go.GeometryFilter = Rhino.DocObjects.ObjectType.Point | Rhino.DocObjects.ObjectType.Curve | Rhino.DocObjects.ObjectType.TextDot;
        go.AcceptNothing(true);
        go.GetMultiple(0, 0);
        if (go.CommandResult() != Rhino.Commands.Result.Success)
          return go.CommandResult();
        for (int i = 0; i < go.ObjectCount; i++)
        {
          objref = go.Object(i);
          Rhino.Geometry.GeometryBase g = objref.Geometry();
          Rhino.Geometry.Point pt = g as Rhino.Geometry.Point;
          Rhino.Geometry.Curve crv = g as Rhino.Geometry.Curve;
          Rhino.Geometry.TextDot dot = g as Rhino.Geometry.TextDot;
          if (pt != null)
            unroll.AddFollowingGeometry(pt.Location);
          else if (crv != null)
            unroll.AddFollowingGeometry(crv);
          else if (dot != null)
            unroll.AddFollowingGeometry(dot);
        }
    
        unroll.ExplodeOutput = false;
        Rhino.Geometry.Curve[] curves;
        Rhino.Geometry.Point3d[] points;
        Rhino.Geometry.TextDot[] dots;
        Rhino.Geometry.Brep[] breps = unroll.PerformUnroll(out curves, out points, out dots);
        if (breps == null || breps.Length < 1)
          return Rhino.Commands.Result.Failure;
    
        for (int i = 0; i < breps.Length; i++)
          doc.Objects.AddBrep(breps[i]);
        for (int i = 0; i < curves.Length; i++)
          doc.Objects.AddCurve(curves[i]);
        doc.Objects.AddPoints(points);
        for (int i = 0; i < dots.Length; i++)
          doc.Objects.AddTextDot(dots[i]);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function UnrollSurface(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Brep Or Rhino.DocObjects.ObjectType.Surface
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc As Result = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", False, filter, objref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    	Dim unroll As Rhino.Geometry.Unroller=Nothing
    	Dim brep As Rhino.Geometry.Brep = objref.Brep()
    	If brep IsNot Nothing Then
    	  unroll = New Rhino.Geometry.Unroller(brep)
    	Else
    	  Dim srf As Rhino.Geometry.Surface = objref.Surface()
    	  If srf IsNot Nothing Then
    		unroll = New Rhino.Geometry.Unroller(srf)
    	  End If
    	End If
    	If unroll Is Nothing Then
    	  Return Rhino.Commands.Result.Cancel
    	End If
    
    	unroll.AbsoluteTolerance = 0.01
    	unroll.RelativeTolerance = 0.01
    
    	Dim go As New Rhino.Input.Custom.GetObject()
    	go.SetCommandPrompt("Select points, curves, and dots to unroll with surface")
    	go.GeometryFilter = Rhino.DocObjects.ObjectType.Point Or Rhino.DocObjects.ObjectType.Curve Or Rhino.DocObjects.ObjectType.TextDot
    	go.AcceptNothing(True)
    	go.GetMultiple(0, 0)
    	If go.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return go.CommandResult()
    	End If
    	For i As Integer = 0 To go.ObjectCount - 1
    	  objref = go.Object(i)
    	  Dim g As Rhino.Geometry.GeometryBase = objref.Geometry()
    	  Dim pt As Rhino.Geometry.Point = TryCast(g, Rhino.Geometry.Point)
    	  Dim crv As Rhino.Geometry.Curve = TryCast(g, Rhino.Geometry.Curve)
    	  Dim dot As Rhino.Geometry.TextDot = TryCast(g, Rhino.Geometry.TextDot)
    	  If pt IsNot Nothing Then
    		unroll.AddFollowingGeometry(pt.Location)
    	  ElseIf crv IsNot Nothing Then
    		unroll.AddFollowingGeometry(crv)
    	  ElseIf dot IsNot Nothing Then
    		unroll.AddFollowingGeometry(dot)
    	  End If
    	Next i
    
    	unroll.ExplodeOutput = False
    	Dim curves() As Rhino.Geometry.Curve = Nothing
    	Dim points() As Rhino.Geometry.Point3d = Nothing
    	Dim dots() As Rhino.Geometry.TextDot = Nothing
    	Dim breps() As Rhino.Geometry.Brep = unroll.PerformUnroll(curves, points, dots)
    	If breps Is Nothing OrElse breps.Length < 1 Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	For i As Integer = 0 To breps.Length - 1
    	  doc.Objects.AddBrep(breps(i))
    	Next i
    	For i As Integer = 0 To curves.Length - 1
    	  doc.Objects.AddCurve(curves(i))
    	Next i
    	doc.Objects.AddPoints(points)
    	For i As Integer = 0 To dots.Length - 1
    	  doc.Objects.AddTextDot(dots(i))
    	Next i
    	doc.Views.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def UnrollSurface():
        filter = Rhino.DocObjects.ObjectType.Brep | Rhino.DocObjects.ObjectType.Surface
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", False, filter)
        if rc!=Rhino.Commands.Result.Success: return rc;
    
        unroll = Rhino.Geometry.Unroller(objref.Geometry())
        go = Rhino.Input.Custom.GetObject()
        go.SetCommandPrompt("Select points, curves, and dots to unroll with surface")
        go.GeometryFilter = Rhino.DocObjects.ObjectType.Point | Rhino.DocObjects.ObjectType.Curve | Rhino.DocObjects.ObjectType.TextDot
        go.AcceptNothing(True)
        go.GetMultiple(0, 0)
        if go.CommandResult()!=Rhino.Commands.Result.Success:
            return go.CommandResult()
    
        for i in range(go.ObjectCount):
            objref = go.Object(i);
            g = objref.Geometry();
            unroll.AddFollowingGeometry(g)
    
        unroll.ExplodeOutput = False
        breps, curves, points, dots = unroll.PerformUnroll()
        if not breps: return Rhino.Commands.Result.Failure
        for brep in breps: scriptcontext.doc.Objects.AddBrep(brep)
        for curve in curves: scriptcontext.doc.Objects.AddCurve(curve)
        for point in points: scriptcontext.doc.Objects.AddPoint(point)
        for dot in dots: scriptcontext.doc.Objects.AddTextDot(dot)
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        UnrollSurface()
    

  

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

