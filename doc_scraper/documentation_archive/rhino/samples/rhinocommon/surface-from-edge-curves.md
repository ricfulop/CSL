---
url: https://developer.rhino3d.com/samples/rhinocommon/surface-from-edge-curves/
scraped_at: 2025-09-08T15:45:24.596619
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

Surface from Edge Curves

Create a Surface from Edge Curves

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result EdgeSrf(RhinoDoc doc)
      {
        var go = new GetObject();
        go.SetCommandPrompt("Select 2, 3, or 4 open curves");
        go.GeometryFilter = ObjectType.Curve;
        go.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve;
        go.GetMultiple(2, 4);
        if (go.CommandResult() != Result.Success)
          return go.CommandResult();
    
        var curves = go.Objects().Select(o => o.Curve());
    
        var brep = Brep.CreateEdgeSurface(curves);
    
        if (brep != null)
        {
          doc.Objects.AddBrep(brep);
          doc.Views.Redraw();
        }
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function EdgeSrf(ByVal doc As RhinoDoc) As Result
    	Dim go = New GetObject()
    	go.SetCommandPrompt("Select 2, 3, or 4 open curves")
    	go.GeometryFilter = ObjectType.Curve
    	go.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
    	go.GetMultiple(2, 4)
    	If go.CommandResult() <> Result.Success Then
    	  Return go.CommandResult()
    	End If
    
    	Dim curves = go.Objects().Select(Function(o) o.Curve())
    
    	Dim brep = Brep.CreateEdgeSurface(curves)
    
    	If brep IsNot Nothing Then
    	  doc.Objects.AddBrep(brep)
    	  doc.Views.Redraw()
    	End If
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.Commands import *
    from Rhino.DocObjects import *
    from Rhino.Geometry import *
    from Rhino.Input.Custom import *
    from scriptcontext import doc
    
    def RunCommand():
        go = GetObject()
        go.SetCommandPrompt("Select 2, 3, or 4 open curves")
        go.GeometryFilter = ObjectType.Curve
        go.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
        go.GetMultiple(2, 4)
        if go.CommandResult() != Result.Success:
            return go.CommandResult()
    
        curves = [o.Curve() for o in go.Objects()]
    
        brep = Brep.CreateEdgeSurface(curves)
    
        if brep != None:
            doc.Objects.AddBrep(brep)
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

