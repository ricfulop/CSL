---
url: https://developer.rhino3d.com/samples/rhinocommon/unroll-surface-and-mesh/
scraped_at: 2025-09-08T15:46:48.939399
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

Unroll Surface and Mesh

Unroll developable surface and associated mesh

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result UnrollSurface2(Rhino.RhinoDoc doc)
      {
        const ObjectType filter = Rhino.DocObjects.ObjectType.Brep | Rhino.DocObjects.ObjectType.Surface;
        Rhino.DocObjects.ObjRef objref;
        Result rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", false, filter, out objref);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
        Rhino.Geometry.Unroller unroll=null;
        Rhino.Geometry.Brep brep = objref.Brep();
        Rhino.Geometry.Mesh mesh=null;
        if (brep != null)
        {
          unroll = new Rhino.Geometry.Unroller(brep);
          mesh = brep.Faces[0].GetMesh(Rhino.Geometry.MeshType.Render);
        }
        else
        {
          Rhino.Geometry.Surface srf = objref.Surface();
          if (srf != null)
          {
            unroll = new Rhino.Geometry.Unroller(srf);
          }
        }
        if (unroll == null || mesh==null)
          return Rhino.Commands.Result.Cancel;
    
        unroll.AddFollowingGeometry(mesh.Vertices.ToPoint3dArray());
    
        unroll.ExplodeOutput = false;
        Rhino.Geometry.Curve[] curves;
        Rhino.Geometry.Point3d[] points;
        Rhino.Geometry.TextDot[] dots;
        unroll.PerformUnroll(out curves, out points, out dots);
    
        // change the mesh vertices to the flattened form and add it to the document
        if( points.Length == mesh.Vertices.Count )
        {
          for( int i=0; i<points.Length; i++ )
            mesh.Vertices.SetVertex(i, points[i]);
          mesh.Normals.ComputeNormals();
        }
        doc.Objects.AddMesh(mesh, objref.Object().Attributes);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function UnrollSurface2(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Brep Or Rhino.DocObjects.ObjectType.Surface
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc As Result = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", False, filter, objref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    	Dim unroll As Rhino.Geometry.Unroller=Nothing
    	Dim brep As Rhino.Geometry.Brep = objref.Brep()
    	Dim mesh As Rhino.Geometry.Mesh=Nothing
    	If brep IsNot Nothing Then
    	  unroll = New Rhino.Geometry.Unroller(brep)
    	  mesh = brep.Faces(0).GetMesh(Rhino.Geometry.MeshType.Render)
    	Else
    	  Dim srf As Rhino.Geometry.Surface = objref.Surface()
    	  If srf IsNot Nothing Then
    		unroll = New Rhino.Geometry.Unroller(srf)
    	  End If
    	End If
    	If unroll Is Nothing OrElse mesh Is Nothing Then
    	  Return Rhino.Commands.Result.Cancel
    	End If
    
    	unroll.AddFollowingGeometry(mesh.Vertices.ToPoint3dArray())
    
    	unroll.ExplodeOutput = False
    	Dim curves() As Rhino.Geometry.Curve = Nothing
    	Dim points() As Rhino.Geometry.Point3d = Nothing
    	Dim dots() As Rhino.Geometry.TextDot = Nothing
    	unroll.PerformUnroll(curves, points, dots)
    
    	' change the mesh vertices to the flattened form and add it to the document
    	If points.Length = mesh.Vertices.Count Then
    	  For i As Integer = 0 To points.Length - 1
    		mesh.Vertices.SetVertex(i, points(i))
    	  Next i
    	  mesh.Normals.ComputeNormals()
    	End If
    	doc.Objects.AddMesh(mesh, objref.Object().Attributes)
    	doc.Views.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def UnrollSurface2():
        filter = Rhino.DocObjects.ObjectType.Brep | Rhino.DocObjects.ObjectType.Surface
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", False, filter)
        if rc!=Rhino.Commands.Result.Success: return rc;
    
        unroll = Rhino.Geometry.Unroller(objref.Geometry())
        mesh = objref.Brep().Faces[0].GetMesh(0)
        if not mesh: return Rhino.Commands.Result.Cancel
    
        unroll.AddFollowingGeometry(mesh.Vertices.ToPoint3dArray())
        unroll.ExplodeOutput = False
        breps, curves, points, dots = unroll.PerformUnroll()
        # change the mesh vertices to the flattened form and add it to the document
        if points.Length==mesh.Vertices.Count:
            for i, point in enumerate(points): mesh.Vertices.SetVertex(i, point)
            mesh.Normals.ComputeNormals()
        scriptcontext.doc.Objects.AddMesh(mesh, objref.Object().Attributes)
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        UnrollSurface2()
    

  

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

