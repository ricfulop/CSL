---
url: https://developer.rhino3d.com/samples/rhinocommon/dynamically-draw-geometry-when-picking-points/
scraped_at: 2025-09-08T15:45:28.600526
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

Dynamically Draw Geometry when Picking Points

Demonstrates how to dynamically draw geometry during point picking.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result GetPointDynamicDraw(RhinoDoc doc)
      {
        var gp = new GetPoint();
        gp.SetCommandPrompt("Center point");
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var center_point = gp.Point();
        if (center_point == Point3d.Unset)
          return Result.Failure;
    
        var gcp = new GetCircleRadiusPoint(center_point);
        gcp.SetCommandPrompt("Radius");
        gcp.ConstrainToConstructionPlane(false);
        gcp.SetBasePoint(center_point, true);
        gcp.DrawLineFromPoint(center_point, true);
        gcp.Get();
        if (gcp.CommandResult() != Result.Success)
          return gcp.CommandResult();
    
        var radius = center_point.DistanceTo(gcp.Point());
        var cplane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane();
        doc.Objects.AddCircle(new Circle(cplane, center_point, radius));
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    public class GetCircleRadiusPoint : GetPoint
    {
      private Point3d m_center_point;
    
      public GetCircleRadiusPoint(Point3d centerPoint)
      {
        m_center_point = centerPoint;
      }
    
      protected override void OnDynamicDraw(GetPointDrawEventArgs e)
      {
        base.OnDynamicDraw(e);
        var cplane = e.RhinoDoc.Views.ActiveView.ActiveViewport.ConstructionPlane();
        var radius = m_center_point.DistanceTo(e.CurrentPoint);
        var circle = new Circle(cplane, m_center_point, radius);
        e.Display.DrawCircle(circle, System.Drawing.Color.Black);
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function GetPointDynamicDraw(ByVal doc As RhinoDoc) As Result
    	Dim gp = New GetPoint()
    	gp.SetCommandPrompt("Center point")
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim center_point = gp.Point()
    	If center_point Is Point3d.Unset Then
    	  Return Result.Failure
    	End If
    
    	Dim gcp = New GetCircleRadiusPoint(center_point)
    	gcp.SetCommandPrompt("Radius")
    	gcp.ConstrainToConstructionPlane(False)
    	gcp.SetBasePoint(center_point, True)
    	gcp.DrawLineFromPoint(center_point, True)
    	gcp.Get()
    	If gcp.CommandResult() <> Result.Success Then
    	  Return gcp.CommandResult()
    	End If
    
    	Dim radius = center_point.DistanceTo(gcp.Point())
    	Dim cplane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane()
    	doc.Objects.AddCircle(New Circle(cplane, center_point, radius))
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    Public Class GetCircleRadiusPoint
    	Inherits GetPoint
    
      Private m_center_point As Point3d
    
      Public Sub New(ByVal centerPoint As Point3d)
    	m_center_point = centerPoint
      End Sub
    
      Protected Overrides Sub OnDynamicDraw(ByVal e As GetPointDrawEventArgs)
    	MyBase.OnDynamicDraw(e)
    	Dim cplane = e.RhinoDoc.Views.ActiveView.ActiveViewport.ConstructionPlane()
    	Dim radius = m_center_point.DistanceTo(e.CurrentPoint)
    	Dim circle = New Circle(cplane, m_center_point, radius)
    	e.Display.DrawCircle(circle, System.Drawing.Color.Black)
      End Sub
    End Class
    
    
    
    from Rhino import *
    from Rhino.Geometry import *
    from Rhino.Commands import *
    from Rhino.Input.Custom import *
    from scriptcontext import doc
    from System.Drawing import *
    
    def RunCommand():
        gp = GetPoint()
        gp.SetCommandPrompt("Center point")
        gp.Get()
        if gp.CommandResult() != Result.Success:
            return gp.CommandResult()
        center_point = gp.Point()
        if center_point == Point3d.Unset:
            return Result.Failure
    
        gcp = GetCircleRadiusPoint(center_point)
        gcp.SetCommandPrompt("Radius")
        gcp.ConstrainToConstructionPlane(False)
        gcp.SetBasePoint(center_point, True)
        gcp.DrawLineFromPoint(center_point, True)
        gcp.Get()
        if gcp.CommandResult() != Result.Success:
            return gcp.CommandResult()
    
        radius = center_point.DistanceTo(gcp.Point())
        cplane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane()
        doc.Objects.AddCircle(Circle(cplane, center_point, radius))
        doc.Views.Redraw()
        return Result.Success
    
    class GetCircleRadiusPoint (GetPoint):
        def __init__(self, centerPoint):
            self.m_center_point = centerPoint
    
        def OnDynamicDraw(self, e):
            cplane = e.RhinoDoc.Views.ActiveView.ActiveViewport.ConstructionPlane()
            radius = self.m_center_point.DistanceTo(e.CurrentPoint)
            circle = Circle(cplane, self.m_center_point, radius)
            e.Display.DrawCircle(circle, Color.Black)
    
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

