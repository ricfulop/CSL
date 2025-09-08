---
url: https://developer.rhino3d.com/samples/rhinocommon/move-points/
scraped_at: 2025-09-08T15:46:26.869798
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

Move Points

Demonstrates how to move user-specified points to a new location.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result MovePointObjects(RhinoDoc doc)
      {
        ObjRef[] obj_refs;
        var rc = RhinoGet.GetMultipleObjects("Select points to move", false, ObjectType.Point, out obj_refs);
        if (rc != Result.Success || obj_refs == null)
          return rc;
    
        var gp = new GetPoint();
        gp.SetCommandPrompt("Point to move from");
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var start_point = gp.Point();
    
        gp.SetCommandPrompt("Point to move to");
        gp.SetBasePoint(start_point, false);
        gp.DrawLineFromPoint(start_point, true);
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var end_point = gp.Point();
    
        var xform = Transform.Translation(end_point - start_point);
    
        foreach (var obj_ref in obj_refs)
        {
          doc.Objects.Transform(obj_ref, xform, true);
        }
    
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function MovePointObjects(ByVal doc As RhinoDoc) As Result
    	Dim obj_refs() As ObjRef = Nothing
    	Dim rc = RhinoGet.GetMultipleObjects("Select points to move", False, ObjectType.Point, obj_refs)
    	If rc IsNot Result.Success OrElse obj_refs Is Nothing Then
    	  Return rc
    	End If
    
    	Dim gp = New GetPoint()
    	gp.SetCommandPrompt("Point to move from")
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim start_point = gp.Point()
    
    	gp.SetCommandPrompt("Point to move to")
    	gp.SetBasePoint(start_point, False)
    	gp.DrawLineFromPoint(start_point, True)
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim end_point = gp.Point()
    
    	Dim xform = Transform.Translation(end_point - start_point)
    
    	For Each obj_ref In obj_refs
    	  doc.Objects.Transform(obj_ref, xform, True)
    	Next obj_ref
    
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Commands import *
    from Rhino.Input import *
    from Rhino.Input.Custom import *
    from Rhino.Geometry import *
    from scriptcontext import doc
    
    def RunCommand():
        rc, obj_refs = RhinoGet.GetMultipleObjects("Select points to move", False, ObjectType.Point)
        if rc != Result.Success or obj_refs == None:
            return rc
    
        gp = GetPoint()
        gp.SetCommandPrompt("Point to move from")
        gp.Get()
        if gp.CommandResult() != Result.Success:
            return gp.CommandResult()
        start_point = gp.Point()
    
        gp.SetCommandPrompt("Point to move to")
        gp.SetBasePoint(start_point, False)
        gp.DrawLineFromPoint(start_point, True)
        gp.Get()
        if gp.CommandResult() != Result.Success:
            return gp.CommandResult()
        end_point = gp.Point()
    
        xform = Transform.Translation(end_point - start_point)
    
        for obj_ref in obj_refs:
            doc.Objects.Transform(obj_ref, xform, True)
    
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

