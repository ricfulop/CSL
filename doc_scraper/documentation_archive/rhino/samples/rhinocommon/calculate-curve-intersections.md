---
url: https://developer.rhino3d.com/samples/rhinocommon/calculate-curve-intersections/
scraped_at: 2025-09-08T15:45:06.533823
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

Calculate Curve Intersections

Demonstrates how to calculate the intersection points between two user-
specified curves.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result IntersectCurves(Rhino.RhinoDoc doc)
      {
        // Select two curves to intersect
        var go = new Rhino.Input.Custom.GetObject();
        go.SetCommandPrompt("Select two curves");
        go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
        go.GetMultiple(2, 2);
        if (go.CommandResult() != Rhino.Commands.Result.Success)
          return go.CommandResult();
    
        // Validate input
        var curveA = go.Object(0).Curve();
        var curveB = go.Object(1).Curve();
        if (curveA == null || curveB == null)
          return Rhino.Commands.Result.Failure;
    
        // Calculate the intersection
        const double intersection_tolerance = 0.001;
        const double overlap_tolerance = 0.0;
        var events = Rhino.Geometry.Intersect.Intersection.CurveCurve(curveA, curveB, intersection_tolerance, overlap_tolerance);
    
        // Process the results
        if (events != null)
        {
          for (int i = 0; i < events.Count; i++)
          {
            var ccx_event = events[i];
            doc.Objects.AddPoint(ccx_event.PointA);
            if (ccx_event.PointA.DistanceTo(ccx_event.PointB) > double.Epsilon)
            {
              doc.Objects.AddPoint(ccx_event.PointB);
              doc.Objects.AddLine(ccx_event.PointA, ccx_event.PointB);
            }
          }
          doc.Views.Redraw();
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function IntersectCurves(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	' Select two curves to intersect
    	Dim go = New Rhino.Input.Custom.GetObject()
    	go.SetCommandPrompt("Select two curves")
    	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    	go.GetMultiple(2, 2)
    	If go.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return go.CommandResult()
    	End If
    
    	' Validate input
    	Dim curveA = go.Object(0).Curve()
    	Dim curveB = go.Object(1).Curve()
    	If curveA Is Nothing OrElse curveB Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	' Calculate the intersection
    	Const intersection_tolerance As Double = 0.001
    	Const overlap_tolerance As Double = 0.0
    	Dim events = Rhino.Geometry.Intersect.Intersection.CurveCurve(curveA, curveB, intersection_tolerance, overlap_tolerance)
    
    	' Process the results
    	If events IsNot Nothing Then
    	  For i As Integer = 0 To events.Count - 1
    		Dim ccx_event = events(i)
    		doc.Objects.AddPoint(ccx_event.PointA)
    		If ccx_event.PointA.DistanceTo(ccx_event.PointB) > Double.Epsilon Then
    		  doc.Objects.AddPoint(ccx_event.PointB)
    		  doc.Objects.AddLine(ccx_event.PointA, ccx_event.PointB)
    		End If
    	  Next i
    	  doc.Views.Redraw()
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def IntersectCurves():
        # Select two curves to intersect
        go = Rhino.Input.Custom.GetObject()
        go.SetCommandPrompt("Select two curves")
        go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
        go.GetMultiple(2, 2)
        if go.CommandResult()!=Rhino.Commands.Result.Success: return
    
        # Validate input
        curveA = go.Object(0).Curve()
        curveB = go.Object(1).Curve()
        if not curveA or not curveB: return
    
        # Calculate the intersection
        intersection_tolerance = 0.001
        overlap_tolerance = 0.0
        events = Rhino.Geometry.Intersect.Intersection.CurveCurve(curveA, curveB, intersection_tolerance, overlap_tolerance)
    
        # Process the results
        if not events: return
        for ccx_event in events:
            scriptcontext.doc.Objects.AddPoint(ccx_event.PointA)
            if ccx_event.PointA.DistanceTo(ccx_event.PointB) > float.Epsilon:
                scriptcontext.doc.Objects.AddPoint(ccx_event.PointB)
                scriptcontext.doc.Objects.AddLine(ccx_event.PointA, ccx_event.PointB)
        scriptcontext.doc.Views.Redraw()
    
    if __name__=="__main__":
        IntersectCurves()
    

  

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

