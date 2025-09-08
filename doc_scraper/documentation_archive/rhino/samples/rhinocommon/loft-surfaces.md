---
url: https://developer.rhino3d.com/samples/rhinocommon/loft-surfaces/
scraped_at: 2025-09-08T15:46:22.828142
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

Loft Surfaces

Demonstrates how to create a lofted surface from a set of user-specified
curves.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result Loft(RhinoDoc doc)
      {
        // select curves to loft
        var gs = new GetObject();
        gs.SetCommandPrompt("select curves to loft");
        gs.GeometryFilter = ObjectType.Curve;
        gs.DisablePreSelect();
        gs.SubObjectSelect = false;
        gs.GetMultiple(2, 0);
        if (gs.CommandResult() != Result.Success)
          return gs.CommandResult();
    
        var curves = gs.Objects().Select(obj => obj.Curve()).ToList();
    
        var breps = Brep.CreateFromLoft(curves, Point3d.Unset, Point3d.Unset, LoftType.Tight, false);
        foreach (var brep in breps)
          doc.Objects.AddBrep(brep);
    
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function Loft(ByVal doc As RhinoDoc) As Result
    	' select curves to loft
    	Dim gs = New GetObject()
    	gs.SetCommandPrompt("select curves to loft")
    	gs.GeometryFilter = ObjectType.Curve
    	gs.DisablePreSelect()
    	gs.SubObjectSelect = False
    	gs.GetMultiple(2, 0)
    	If gs.CommandResult() <> Result.Success Then
    	  Return gs.CommandResult()
    	End If
    
    	Dim curves = gs.Objects().Select(Function(obj) obj.Curve()).ToList()
    
    	Dim breps = Brep.CreateFromLoft(curves, Point3d.Unset, Point3d.Unset, LoftType.Tight, False)
    	For Each brep In breps
    	  doc.Objects.AddBrep(brep)
    	Next brep
    
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    
    def RunCommand():
        crvids = rs.GetObjects(message="select curves to loft", filter=rs.filter.curve, minimum_count=2)
        if not crvids: return
    
        rs.AddLoftSrf(object_ids=crvids, loft_type = 3) #3 = tight
    
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

