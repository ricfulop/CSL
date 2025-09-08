---
url: https://developer.rhino3d.com/samples/rhinocommon/conduit-draw-shaded-mesh/
scraped_at: 2025-09-08T15:45:26.481959
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

Conduit Draw Shaded Mesh

Demonstrates how to draw a shaded mesh using a display conduit.

C# VB.NET Python

    
    
    public class DrawShadedMeshConduit : Rhino.Display.DisplayConduit
    {
      public Rhino.Geometry.Mesh Mesh { get; set; }
    
      protected override void CalculateBoundingBox(Rhino.Display.CalculateBoundingBoxEventArgs e)
      {
        if (null != Mesh)
        {
          Rhino.Geometry.BoundingBox bbox = Mesh.GetBoundingBox(false);
          // Unites a bounding box with the current display bounding box in
          // order to ensure dynamic objects in "box" are drawn.
          e.IncludeBoundingBox(bbox);
        }
      }
    
      protected override void PostDrawObjects(Rhino.Display.DrawEventArgs e)
      {
        if (null != Mesh)
        {
          Rhino.Display.DisplayMaterial material = new Rhino.Display.DisplayMaterial();
          material.Diffuse = System.Drawing.Color.Blue;
          e.Display.DrawMeshShaded(Mesh, material);
        }
      }
    }
    
    partial class Examples
    {
      public static Rhino.Commands.Result ConduitDrawShadedMesh(Rhino.RhinoDoc doc)
      {
        Rhino.Geometry.Mesh mesh = MeshBox(100, 500, 10);
        if (null == mesh)
          return Rhino.Commands.Result.Failure;
    
        DrawShadedMeshConduit conduit = new DrawShadedMeshConduit();
        conduit.Mesh = mesh;
        conduit.Enabled = true;
        doc.Views.Redraw();
    
        string outputString = string.Empty;
        Rhino.Input.RhinoGet.GetString("Press <Enter> to continue", true, ref outputString);
    
        conduit.Enabled = false;
        doc.Views.Redraw();
    
        return Rhino.Commands.Result.Success;
      }
    
      public static Rhino.Geometry.Mesh MeshBox(double x, double y, double z)
      {
        Rhino.Geometry.Mesh mesh = new Rhino.Geometry.Mesh();
        mesh.Vertices.Add(0, 0, 0);
        mesh.Vertices.Add(x, 0, 0);
        mesh.Vertices.Add(x, y, 0);
        mesh.Vertices.Add(0, y, 0);
        mesh.Vertices.Add(0, 0, z);
        mesh.Vertices.Add(x, 0, z);
        mesh.Vertices.Add(x, y, z);
        mesh.Vertices.Add(0, y, z);
        mesh.Faces.AddFace(3, 2, 1, 0);
        mesh.Faces.AddFace(4, 5, 6, 7);
        mesh.Faces.AddFace(0, 1, 5, 4);
        mesh.Faces.AddFace(1, 2, 6, 5);
        mesh.Faces.AddFace(2, 3, 7, 6);
        mesh.Faces.AddFace(3, 0, 4, 7);
        mesh.Normals.ComputeNormals();
        mesh.Compact();
        if (mesh.IsValid)
          return mesh;
        return null;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ConduitDrawShadedMesh(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim mesh As Rhino.Geometry.Mesh = MeshBox(100, 500, 10)
    	If Nothing Is mesh Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim conduit As New DrawShadedMeshConduit()
    	conduit.Mesh = mesh
    	conduit.Enabled = True
    	doc.Views.Redraw()
    
    	Dim outputString As String = String.Empty
    	Rhino.Input.RhinoGet.GetString("Press <Enter> to continue", True, outputString)
    
    	conduit.Enabled = False
    	doc.Views.Redraw()
    
    	Return Rhino.Commands.Result.Success
      End Function
    
      Public Shared Function MeshBox(ByVal x As Double, ByVal y As Double, ByVal z As Double) As Rhino.Geometry.Mesh
    	Dim mesh As New Rhino.Geometry.Mesh()
    	mesh.Vertices.Add(0, 0, 0)
    	mesh.Vertices.Add(x, 0, 0)
    	mesh.Vertices.Add(x, y, 0)
    	mesh.Vertices.Add(0, y, 0)
    	mesh.Vertices.Add(0, 0, z)
    	mesh.Vertices.Add(x, 0, z)
    	mesh.Vertices.Add(x, y, z)
    	mesh.Vertices.Add(0, y, z)
    	mesh.Faces.AddFace(3, 2, 1, 0)
    	mesh.Faces.AddFace(4, 5, 6, 7)
    	mesh.Faces.AddFace(0, 1, 5, 4)
    	mesh.Faces.AddFace(1, 2, 6, 5)
    	mesh.Faces.AddFace(2, 3, 7, 6)
    	mesh.Faces.AddFace(3, 0, 4, 7)
    	mesh.Normals.ComputeNormals()
    	mesh.Compact()
    	If mesh.IsValid Then
    	  Return mesh
    	End If
    	Return Nothing
      End Function
    End Class
    
    
    
    # No Python sample available
    

  

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

