---
url: https://developer.rhino3d.com/samples/rhinocommon/add-mesh/
scraped_at: 2025-09-08T15:44:28.236597
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

Add Mesh

Demonstrates how to construct a mesh from a list of vertices and faces.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddMesh(Rhino.RhinoDoc doc)
      {
        Rhino.Geometry.Mesh mesh = new Rhino.Geometry.Mesh();
        mesh.Vertices.Add(0.0, 0.0, 1.0); //0
        mesh.Vertices.Add(1.0, 0.0, 1.0); //1
        mesh.Vertices.Add(2.0, 0.0, 1.0); //2
        mesh.Vertices.Add(3.0, 0.0, 0.0); //3
        mesh.Vertices.Add(0.0, 1.0, 1.0); //4
        mesh.Vertices.Add(1.0, 1.0, 2.0); //5
        mesh.Vertices.Add(2.0, 1.0, 1.0); //6
        mesh.Vertices.Add(3.0, 1.0, 0.0); //7
        mesh.Vertices.Add(0.0, 2.0, 1.0); //8
        mesh.Vertices.Add(1.0, 2.0, 1.0); //9
        mesh.Vertices.Add(2.0, 2.0, 1.0); //10
        mesh.Vertices.Add(3.0, 2.0, 1.0); //11
    
        mesh.Faces.AddFace(0, 1, 5, 4);
        mesh.Faces.AddFace(1, 2, 6, 5);
        mesh.Faces.AddFace(2, 3, 7, 6);
        mesh.Faces.AddFace(4, 5, 9, 8);
        mesh.Faces.AddFace(5, 6, 10, 9);
        mesh.Faces.AddFace(6, 7, 11, 10);
        mesh.Normals.ComputeNormals();
        mesh.Compact();
        if (doc.Objects.AddMesh(mesh) != Guid.Empty)
        {
          doc.Views.Redraw();
          return Rhino.Commands.Result.Success;
        }
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddMesh(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim mesh As New Rhino.Geometry.Mesh()
    	mesh.Vertices.Add(0.0, 0.0, 1.0) '0
    	mesh.Vertices.Add(1.0, 0.0, 1.0) '1
    	mesh.Vertices.Add(2.0, 0.0, 1.0) '2
    	mesh.Vertices.Add(3.0, 0.0, 0.0) '3
    	mesh.Vertices.Add(0.0, 1.0, 1.0) '4
    	mesh.Vertices.Add(1.0, 1.0, 2.0) '5
    	mesh.Vertices.Add(2.0, 1.0, 1.0) '6
    	mesh.Vertices.Add(3.0, 1.0, 0.0) '7
    	mesh.Vertices.Add(0.0, 2.0, 1.0) '8
    	mesh.Vertices.Add(1.0, 2.0, 1.0) '9
    	mesh.Vertices.Add(2.0, 2.0, 1.0) '10
    	mesh.Vertices.Add(3.0, 2.0, 1.0) '11
    
    	mesh.Faces.AddFace(0, 1, 5, 4)
    	mesh.Faces.AddFace(1, 2, 6, 5)
    	mesh.Faces.AddFace(2, 3, 7, 6)
    	mesh.Faces.AddFace(4, 5, 9, 8)
    	mesh.Faces.AddFace(5, 6, 10, 9)
    	mesh.Faces.AddFace(6, 7, 11, 10)
    	mesh.Normals.ComputeNormals()
    	mesh.Compact()
    	If doc.Objects.AddMesh(mesh) <> Guid.Empty Then
    	  doc.Views.Redraw()
    	  Return Rhino.Commands.Result.Success
    	End If
    	Return Rhino.Commands.Result.Failure
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddMesh():
        mesh = Rhino.Geometry.Mesh()
        mesh.Vertices.Add(0.0, 0.0, 1.0) #0
        mesh.Vertices.Add(1.0, 0.0, 1.0) #1
        mesh.Vertices.Add(2.0, 0.0, 1.0) #2
        mesh.Vertices.Add(3.0, 0.0, 0.0) #3
        mesh.Vertices.Add(0.0, 1.0, 1.0) #4
        mesh.Vertices.Add(1.0, 1.0, 2.0) #5
        mesh.Vertices.Add(2.0, 1.0, 1.0) #6
        mesh.Vertices.Add(3.0, 1.0, 0.0) #7
        mesh.Vertices.Add(0.0, 2.0, 1.0) #8
        mesh.Vertices.Add(1.0, 2.0, 1.0) #9
        mesh.Vertices.Add(2.0, 2.0, 1.0) #10
        mesh.Vertices.Add(3.0, 2.0, 1.0) #11
    
        mesh.Faces.AddFace(0, 1, 5, 4)
        mesh.Faces.AddFace(1, 2, 6, 5)
        mesh.Faces.AddFace(2, 3, 7, 6)
        mesh.Faces.AddFace(4, 5, 9, 8)
        mesh.Faces.AddFace(5, 6, 10, 9)
        mesh.Faces.AddFace(6, 7, 11, 10)
        mesh.Normals.ComputeNormals()
        mesh.Compact()
        if scriptcontext.doc.Objects.AddMesh(mesh)!=System.Guid.Empty:
            scriptcontext.doc.Views.Redraw()
            return Rhino.Commands.Result.Success
        return Rhino.Commands.Result.Failure
    
    
    if __name__=="__main__":
        AddMesh()
    

  

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

