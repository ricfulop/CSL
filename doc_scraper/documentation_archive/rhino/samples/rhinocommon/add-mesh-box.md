---
url: https://developer.rhino3d.com/samples/rhinocommon/add-mesh-box/
scraped_at: 2025-09-08T15:44:29.350275
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

Add Mesh Box

Demonstrates how to construct a mesh box from a Brep box.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddMeshBox(Rhino.RhinoDoc doc)
      {
        Rhino.Geometry.Box box;
        Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetBox(out box);
        if (rc == Rhino.Commands.Result.Success)
        {
          Rhino.Geometry.Mesh mesh = Rhino.Geometry.Mesh.CreateFromBox(box, 2, 2, 2);
          if (null != mesh)
          {
            doc.Objects.AddMesh(mesh);
            doc.Views.Redraw();
            return Rhino.Commands.Result.Success;
          }
        }
    
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddMeshBox(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim box As Rhino.Geometry.Box = Nothing
    	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetBox(box)
    	If rc Is Rhino.Commands.Result.Success Then
    	  Dim mesh As Rhino.Geometry.Mesh = Rhino.Geometry.Mesh.CreateFromBox(box, 2, 2, 2)
    	  If Nothing IsNot mesh Then
    		doc.Objects.AddMesh(mesh)
    		doc.Views.Redraw()
    		Return Rhino.Commands.Result.Success
    	  End If
    	End If
    
    	Return Rhino.Commands.Result.Failure
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

