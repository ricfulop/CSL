---
url: https://developer.rhino3d.com/samples/rhinocommon/duplicate-surface-border/
scraped_at: 2025-09-08T15:46:03.825543
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

Duplicate Surface Border

Demonstrates how to duplicate the borders of a user-specified surface or
polysurface.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result DupBorder(Rhino.RhinoDoc doc)
      {
        const ObjectType filter = Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter;
        Rhino.DocObjects.ObjRef objref;
        Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", false, filter, out objref);
        if (rc != Rhino.Commands.Result.Success || objref == null)
          return rc;
    
        Rhino.DocObjects.RhinoObject rhobj = objref.Object();
        Rhino.Geometry.Brep brep = objref.Brep();
        if (rhobj == null || brep == null)
          return Rhino.Commands.Result.Failure;
    
        rhobj.Select(false);
        Rhino.Geometry.Curve[] curves = brep.DuplicateEdgeCurves(true);
        double tol = doc.ModelAbsoluteTolerance * 2.1;
        curves = Rhino.Geometry.Curve.JoinCurves(curves, tol);
        for (int i = 0; i < curves.Length; i++)
        {
          Guid id = doc.Objects.AddCurve(curves[i]);
          doc.Objects.Select(id);
        }
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function DupBorder(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Surface Or Rhino.DocObjects.ObjectType.PolysrfFilter
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", False, filter, objref)
    	If rc IsNot Rhino.Commands.Result.Success OrElse objref Is Nothing Then
    	  Return rc
    	End If
    
    	Dim rhobj As Rhino.DocObjects.RhinoObject = objref.Object()
    	Dim brep As Rhino.Geometry.Brep = objref.Brep()
    	If rhobj Is Nothing OrElse brep Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	rhobj.Select(False)
    	Dim curves() As Rhino.Geometry.Curve = brep.DuplicateEdgeCurves(True)
    	Dim tol As Double = doc.ModelAbsoluteTolerance * 2.1
    	curves = Rhino.Geometry.Curve.JoinCurves(curves, tol)
    	For i As Integer = 0 To curves.Length - 1
    	  Dim id As Guid = doc.Objects.AddCurve(curves(i))
    	  doc.Objects.Select(id)
    	Next i
    	doc.Views.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def DupBorder():
        filter = Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", False, filter)
        if rc != Rhino.Commands.Result.Success: return rc
    
        rhobj = objref.Object()
        brep = objref.Brep()
        if not rhobj or not brep: return Rhino.Commands.Result.Failure
        rhobj.Select(False)
        curves = brep.DuplicateEdgeCurves(True)
        tol = scriptcontext.doc.ModelAbsoluteTolerance * 2.1
        curves = Rhino.Geometry.Curve.JoinCurves(curves, tol)
        for curve in curves:
            id = scriptcontext.doc.Objects.AddCurve(curve)
            scriptcontext.doc.Objects.Select(id)
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        DupBorder()
    

  

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

