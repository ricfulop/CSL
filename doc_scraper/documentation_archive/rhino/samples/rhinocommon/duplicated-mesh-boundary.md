---
url: https://developer.rhino3d.com/samples/rhinocommon/duplicated-mesh-boundary/
scraped_at: 2025-09-08T15:46:02.735256
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

Duplicate Mesh Boundary

Demonstrates how to create a bounding polyline from naked edges of an open
mesh.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result DupMeshBoundary(RhinoDoc doc)
      {
        var gm = new GetObject();
        gm.SetCommandPrompt("Select open mesh");
        gm.GeometryFilter = ObjectType.Mesh;
        gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh;
        gm.Get();
        if (gm.CommandResult() != Result.Success)
          return gm.CommandResult();
        var mesh = gm.Object(0).Mesh();
        if (mesh == null)
          return Result.Failure;
    
        var polylines = mesh.GetNakedEdges();
        foreach (var polyline in polylines)
        {
          doc.Objects.AddPolyline(polyline);
        }
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function DupMeshBoundary(ByVal doc As RhinoDoc) As Result
    	Dim gm = New GetObject()
    	gm.SetCommandPrompt("Select open mesh")
    	gm.GeometryFilter = ObjectType.Mesh
    	gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh
    	gm.Get()
    	If gm.CommandResult() <> Result.Success Then
    	  Return gm.CommandResult()
    	End If
    	Dim mesh = gm.Object(0).Mesh()
    	If mesh Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	Dim polylines = mesh.GetNakedEdges()
    	For Each polyline In polylines
    	  doc.Objects.AddPolyline(polyline)
    	Next polyline
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino.Commands import *
    from Rhino.Input.Custom import *
    from Rhino.DocObjects import *
    from scriptcontext import doc
    
    def RunCommand():
        gm = GetObject()
        gm.SetCommandPrompt("Select open mesh")
        gm.GeometryFilter = ObjectType.Mesh
        gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh
        gm.Get()
        if gm.CommandResult() != Result.Success:
            return gm.CommandResult()
        mesh = gm.Object(0).Mesh()
        if mesh == None:
            return Result.Failure
    
        polylines = mesh.GetNakedEdges()
        for polyline in polylines:
            doc.Objects.AddPolyline(polyline)
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

