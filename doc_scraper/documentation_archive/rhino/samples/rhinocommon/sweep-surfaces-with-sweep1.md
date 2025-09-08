---
url: https://developer.rhino3d.com/samples/rhinocommon/sweep-surfaces-with-sweep1/
scraped_at: 2025-09-08T15:46:42.934179
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

Sweep Surfaces with Sweep1

Demonstrates how to sweep along a single rail curve.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result Sweep1(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef rail_ref;
        var rc = RhinoGet.GetOneObject("Select rail curve", false, Rhino.DocObjects.ObjectType.Curve, out rail_ref);
        if(rc!=Rhino.Commands.Result.Success)
          return rc;
    
        var rail_crv = rail_ref.Curve();
        if( rail_crv==null )
          return Rhino.Commands.Result.Failure;
    
        var gx = new Rhino.Input.Custom.GetObject();
        gx.SetCommandPrompt("Select cross section curves");
        gx.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
        gx.EnablePreSelect(false, true);
        gx.GetMultiple(1,0);
        if( gx.CommandResult() != Rhino.Commands.Result.Success )
          return gx.CommandResult();
    
        var cross_sections = new List<Rhino.Geometry.Curve>();
        for( int i=0; i<gx.ObjectCount; i++ )
        {
          var crv = gx.Object(i).Curve();
          if( crv!= null)
            cross_sections.Add(crv);
        }
        if( cross_sections.Count<1 )
          return Rhino.Commands.Result.Failure;
    
        var sweep = new Rhino.Geometry.SweepOneRail();
        sweep.AngleToleranceRadians = doc.ModelAngleToleranceRadians;
        sweep.ClosedSweep = false;
        sweep.SweepTolerance = doc.ModelAbsoluteTolerance;
        sweep.SetToRoadlikeTop();
        var breps = sweep.PerformSweep(rail_crv, cross_sections);
        for( int i=0; i<breps.Length; i++ )
          doc.Objects.AddBrep(breps[i]);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function Sweep1(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim rail_ref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select rail curve", False, Rhino.DocObjects.ObjectType.Curve, rail_ref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	Dim rail_crv = rail_ref.Curve()
    	If rail_crv Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim gx = New Rhino.Input.Custom.GetObject()
    	gx.SetCommandPrompt("Select cross section curves")
    	gx.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    	gx.EnablePreSelect(False, True)
    	gx.GetMultiple(1,0)
    	If gx.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return gx.CommandResult()
    	End If
    
    	Dim cross_sections = New List(Of Rhino.Geometry.Curve)()
    	For i As Integer = 0 To gx.ObjectCount - 1
    	  Dim crv = gx.Object(i).Curve()
    	  If crv IsNot Nothing Then
    		cross_sections.Add(crv)
    	  End If
    	Next i
    	If cross_sections.Count<1 Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim sweep = New Rhino.Geometry.SweepOneRail()
    	sweep.AngleToleranceRadians = doc.ModelAngleToleranceRadians
    	sweep.ClosedSweep = False
    	sweep.SweepTolerance = doc.ModelAbsoluteTolerance
    	sweep.SetToRoadlikeTop()
    	Dim breps = sweep.PerformSweep(rail_crv, cross_sections)
    	For i As Integer = 0 To breps.Length - 1
    	  doc.Objects.AddBrep(breps(i))
    	Next i
    	doc.Views.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    import Rhino
    import scriptcontext
    
    def Sweep1():
        rail = rs.GetObject("Select rail curve", rs.filter.curve)
        rail_crv = rs.coercecurve(rail)
        if not rail_crv: return
    
        cross_sections = rs.GetObjects("Select cross section curves", rs.filter.curve)
        if not cross_sections: return
        cross_sections = [rs.coercecurve(crv) for crv in cross_sections]
    
        sweep = Rhino.Geometry.SweepOneRail()
        sweep.AngleToleranceRadians = scriptcontext.doc.ModelAngleToleranceRadians
        sweep.ClosedSweep = False
        sweep.SweepTolerance = scriptcontext.doc.ModelAbsoluteTolerance
        sweep.SetToRoadlikeTop()
        breps = sweep.PerformSweep(rail_crv, cross_sections)
        for brep in breps: scriptcontext.doc.Objects.AddBrep(brep)
        scriptcontext.doc.Views.Redraw()
    
    if __name__ == "__main__":
        Sweep1()
    

  

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

