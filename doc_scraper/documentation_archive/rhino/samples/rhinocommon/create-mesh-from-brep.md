---
url: https://developer.rhino3d.com/samples/rhinocommon/create-mesh-from-brep/
scraped_at: 2025-09-08T15:45:48.688847
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

Create Mesh from Brep

Demonstrates how to create a mesh from a selected surface or polysurface.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result CreateMeshFromBrep(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select surface or polysurface to mesh", true, ObjectType.Surface | ObjectType.PolysrfFilter, out obj_ref);
        if (rc != Result.Success)
          return rc;
        var brep = obj_ref.Brep();
        if (null == brep)
          return Result.Failure;
    
        // you could choose anyone of these for example
        var jagged_and_faster = MeshingParameters.Coarse;
        var smooth_and_slower = MeshingParameters.Smooth;
        var default_mesh_params = MeshingParameters.Default;
        var minimal = MeshingParameters.Minimal;
    
        var meshes = Mesh.CreateFromBrep(brep, smooth_and_slower);
        if (meshes == null || meshes.Length == 0)
          return Result.Failure;
    
        var brep_mesh = new Mesh();
        foreach (var mesh in meshes)
          brep_mesh.Append(mesh);
        doc.Objects.AddMesh(brep_mesh);
        doc.Views.Redraw();
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function CreateMeshFromBrep(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select surface or polysurface to mesh", True, ObjectType.Surface Or ObjectType.PolysrfFilter, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim brep = obj_ref.Brep()
    	If Nothing Is brep Then
    	  Return Result.Failure
    	End If
    
    	' you could choose anyone of these for example
    	Dim jagged_and_faster = MeshingParameters.Coarse
    	Dim smooth_and_slower = MeshingParameters.Smooth
    	Dim default_mesh_params = MeshingParameters.Default
    	Dim minimal = MeshingParameters.Minimal
    
    	Dim meshes = Mesh.CreateFromBrep(brep, smooth_and_slower)
    	If meshes Is Nothing OrElse meshes.Length = 0 Then
    	  Return Result.Failure
    	End If
    
    	Dim brep_mesh = New Mesh()
    	For Each mesh In meshes
    	  brep_mesh.Append(mesh)
    	Next mesh
    	doc.Objects.AddMesh(brep_mesh)
    	doc.Views.Redraw()
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    from Rhino.Geometry import *
    from Rhino.Input import RhinoGet
    from Rhino.Commands import Result
    from Rhino.DocObjects import ObjectType
    import rhinoscriptsyntax as rs
    from scriptcontext import doc
    
    def RunCommand():
        rc, objRef = RhinoGet.GetOneObject("Select surface or polysurface to mesh", True, ObjectType.Surface | ObjectType.PolysrfFilter)
        if rc != Result.Success:
            return rc
        brep = objRef.Brep()
        if None == brep:
            return Result.Failure
    
        jaggedAndFaster = MeshingParameters.Coarse
        smoothAndSlower = MeshingParameters.Smooth
        defaultMeshParams = MeshingParameters.Default
        minimal = MeshingParameters.Minimal
    
        meshes = Mesh.CreateFromBrep(brep, smoothAndSlower)
        if meshes == None or meshes.Length == 0:
            return Result.Failure
    
        brepMesh = Mesh()
        for mesh in meshes:
            brepMesh.Append(mesh)
        doc.Objects.AddMesh(brepMesh)
        doc.Views.Redraw()
    
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

