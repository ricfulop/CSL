---
url: https://developer.rhino3d.com/samples/rhinocommon/extract-render-mesh/
scraped_at: 2025-09-08T15:46:09.782992
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

Extract Render Mesh

Demonstrates how to extract the render mesh from a surface or polysurface.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result ExtractRenderMesh(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef objRef = null;
        Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", false, Rhino.DocObjects.ObjectType.Brep, out objRef);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
    
        Rhino.DocObjects.RhinoObject obj = objRef.Object();
        if (null == obj)
          return Rhino.Commands.Result.Failure;
    
        System.Collections.Generic.List<Rhino.DocObjects.RhinoObject> objList = new System.Collections.Generic.List<Rhino.DocObjects.RhinoObject>(1);
        objList.Add(obj);
    
        Rhino.DocObjects.ObjRef[] meshObjRefs = Rhino.DocObjects.RhinoObject.GetRenderMeshes(objList, true, false);
        if (null != meshObjRefs)
        {
          for (int i = 0; i < meshObjRefs.Length; i++)
          {
            Rhino.DocObjects.ObjRef meshObjRef = meshObjRefs[i];
            if (null != meshObjRef)
            {
              Rhino.Geometry.Mesh mesh = meshObjRef.Mesh();
              if (null != mesh)
                doc.Objects.AddMesh(mesh);
            }
          }
          doc.Views.Redraw();
        }
    
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ExtractRenderMesh(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim objRef As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", False, Rhino.DocObjects.ObjectType.Brep, objRef)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	Dim obj As Rhino.DocObjects.RhinoObject = objRef.Object()
    	If Nothing Is obj Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim objList As New System.Collections.Generic.List(Of Rhino.DocObjects.RhinoObject)(1)
    	objList.Add(obj)
    
    	Dim meshObjRefs() As Rhino.DocObjects.ObjRef = Rhino.DocObjects.RhinoObject.GetRenderMeshes(objList, True, False)
    	If Nothing IsNot meshObjRefs Then
    	  For i As Integer = 0 To meshObjRefs.Length - 1
    		Dim meshObjRef As Rhino.DocObjects.ObjRef = meshObjRefs(i)
    		If Nothing IsNot meshObjRef Then
    		  Dim mesh As Rhino.Geometry.Mesh = meshObjRef.Mesh()
    		  If Nothing IsNot mesh Then
    			doc.Objects.AddMesh(mesh)
    		  End If
    		End If
    	  Next i
    	  doc.Views.Redraw()
    	End If
    
    	Return Rhino.Commands.Result.Success
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

