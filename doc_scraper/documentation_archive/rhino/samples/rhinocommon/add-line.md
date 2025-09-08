---
url: https://developer.rhino3d.com/samples/rhinocommon/add-line/
scraped_at: 2025-09-08T15:44:24.338340
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

Add Line

Demonstrates how to construct a line from two points.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddLine(Rhino.RhinoDoc doc)
      {
        Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
        gp.SetCommandPrompt("Start of line");
        gp.Get();
        if (gp.CommandResult() != Rhino.Commands.Result.Success)
          return gp.CommandResult();
    
        Rhino.Geometry.Point3d pt_start = gp.Point();
    
        gp.SetCommandPrompt("End of line");
        gp.SetBasePoint(pt_start, false);
        gp.DrawLineFromPoint(pt_start, true);
        gp.Get();
        if (gp.CommandResult() != Rhino.Commands.Result.Success)
          return gp.CommandResult();
    
        Rhino.Geometry.Point3d pt_end = gp.Point();
        Rhino.Geometry.Vector3d v = pt_end - pt_start;
        if (v.IsTiny(Rhino.RhinoMath.ZeroTolerance))
          return Rhino.Commands.Result.Nothing;
    
        if (doc.Objects.AddLine(pt_start, pt_end) != Guid.Empty)
        {
          doc.Views.Redraw();
          return Rhino.Commands.Result.Success;
        }
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddLine(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim gp As New Rhino.Input.Custom.GetPoint()
    	gp.SetCommandPrompt("Start of line")
    	gp.Get()
    	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return gp.CommandResult()
    	End If
    
    	Dim pt_start As Rhino.Geometry.Point3d = gp.Point()
    
    	gp.SetCommandPrompt("End of line")
    	gp.SetBasePoint(pt_start, False)
    	gp.DrawLineFromPoint(pt_start, True)
    	gp.Get()
    	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return gp.CommandResult()
    	End If
    
    	Dim pt_end As Rhino.Geometry.Point3d = gp.Point()
    	Dim v As Rhino.Geometry.Vector3d = pt_end - pt_start
    	If v.IsTiny(Rhino.RhinoMath.ZeroTolerance) Then
    	  Return Rhino.Commands.Result.Nothing
    	End If
    
    	If doc.Objects.AddLine(pt_start, pt_end) <> Guid.Empty Then
    	  doc.Views.Redraw()
    	  Return Rhino.Commands.Result.Success
    	End If
    	Return Rhino.Commands.Result.Failure
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddLine():
        gp = Rhino.Input.Custom.GetPoint()
        gp.SetCommandPrompt("Start of line")
        gp.Get()
        if gp.CommandResult()!=Rhino.Commands.Result.Success:
            return gp.CommandResult()
        pt_start = gp.Point()
    
        gp.SetCommandPrompt("End of line")
        gp.SetBasePoint(pt_start, False)
        gp.DrawLineFromPoint(pt_start, True)
        gp.Get()
        if gp.CommandResult() != Rhino.Commands.Result.Success:
            return gp.CommandResult()
        pt_end = gp.Point()
        v = pt_end - pt_start
        if v.IsTiny(Rhino.RhinoMath.ZeroTolerance):
            return Rhino.Commands.Result.Nothing
    
        id = scriptcontext.doc.Objects.AddLine(pt_start, pt_end)
        if id!=System.Guid.Empty:
            scriptcontext.doc.Views.Redraw()
            return Rhino.Commands.Result.Success
        return Rhino.Commands.Result.Failure
    
    if __name__=="__main__":
        AddLine()
    

  

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

