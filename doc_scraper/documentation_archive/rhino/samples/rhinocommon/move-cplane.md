---
url: https://developer.rhino3d.com/samples/rhinocommon/move-cplane/
scraped_at: 2025-09-08T15:46:25.868614
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

Move CPlane

Demonstrates how to move a CPlane in the active viewport.

C# VB.NET Python

    
    
    class MoveCPlanePoint : Rhino.Input.Custom.GetPoint
    {
      readonly Rhino.DocObjects.ConstructionPlane m_cplane;
      public MoveCPlanePoint(Rhino.DocObjects.ConstructionPlane cplane)
      {
        m_cplane = cplane;
      }
    
      protected override void OnMouseMove(Rhino.Input.Custom.GetPointMouseEventArgs e)
      {
        Plane pl = m_cplane.Plane;
        pl.Origin = e.Point;
        m_cplane.Plane = pl;
      }
    
      protected override void OnDynamicDraw(Rhino.Input.Custom.GetPointDrawEventArgs e)
      {
        e.Display.DrawConstructionPlane(m_cplane);
      }
    }
    
    partial class Examples
    {
      public static Rhino.Commands.Result MoveCPlane(Rhino.RhinoDoc doc)
      {
        Rhino.Display.RhinoView view = doc.Views.ActiveView;
        if (view == null)
          return Rhino.Commands.Result.Failure;
    
        Rhino.DocObjects.ConstructionPlane cplane = view.ActiveViewport.GetConstructionPlane();
        Point3d origin = cplane.Plane.Origin;
    
        MoveCPlanePoint gp = new MoveCPlanePoint(cplane);
        gp.SetCommandPrompt("CPlane origin");
        gp.SetBasePoint(origin, true);
        gp.DrawLineFromPoint(origin, true);
        gp.Get();
    
        if (gp.CommandResult() != Rhino.Commands.Result.Success)
          return gp.CommandResult();
    
        Point3d point = gp.Point();
        Vector3d v = origin - point;
        if (v.IsTiny())
          return Rhino.Commands.Result.Nothing;
    
        Plane pl = cplane.Plane;
        pl.Origin = point;
        cplane.Plane = pl;
        view.ActiveViewport.SetConstructionPlane(cplane);
        view.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function MoveCPlane(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim view As Rhino.Display.RhinoView = doc.Views.ActiveView
    	If view Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim cplane As Rhino.DocObjects.ConstructionPlane = view.ActiveViewport.GetConstructionPlane()
    	Dim origin As Point3d = cplane.Plane.Origin
    
    	Dim gp As New MoveCPlanePoint(cplane)
    	gp.SetCommandPrompt("CPlane origin")
    	gp.SetBasePoint(origin, True)
    	gp.DrawLineFromPoint(origin, True)
    	gp.Get()
    
    	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return gp.CommandResult()
    	End If
    
    	Dim point As Point3d = gp.Point()
    	Dim v As Vector3d = origin - point
    	If v.IsTiny() Then
    	  Return Rhino.Commands.Result.Nothing
    	End If
    
    	Dim pl As Plane = cplane.Plane
    	pl.Origin = point
    	cplane.Plane = pl
    	view.ActiveViewport.SetConstructionPlane(cplane)
    	view.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    class MoveCPlanePoint(Rhino.Input.Custom.GetPoint):
        def __init__(self, cplane):
            self.m_cplane = cplane
        def OnMouseMove(self, e):
            pl = self.m_cplane.Plane
            pl.Origin = e.Point
            self.m_cplane.Plane = pl
        def OnDynamicDraw(self, e):
            e.Display.DrawConstructionPlane(self.m_cplane);
    
    def MoveCPlane():
        view = scriptcontext.doc.Views.ActiveView
        if not view: return Rhino.Commands.Result.Failure
    
        cplane = view.ActiveViewport.GetConstructionPlane()
        origin = cplane.Plane.Origin
        gp = MoveCPlanePoint(cplane)
        gp.SetCommandPrompt("CPlane origin")
        gp.SetBasePoint(origin, True)
        gp.DrawLineFromPoint(origin, True)
        gp.Get()
        if gp.CommandResult()!=Rhino.Commands.Result.Success:
            return gp.CommandResult()
    
        point = gp.Point()
        v = origin - point
        if v.IsTiny(): return Rhino.Commands.Result.Nothing
        pl = cplane.Plane
        pl.Origin = point
        cplane.Plane = pl
        view.ActiveViewport.SetConstructionPlane(cplane)
        view.Redraw()
        return Rhino.Commands.Result.Success
    
    
    if __name__=="__main__":
        MoveCPlane()
    

  

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

