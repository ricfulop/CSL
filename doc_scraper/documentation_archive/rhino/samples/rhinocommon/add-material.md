---
url: https://developer.rhino3d.com/samples/rhinocommon/add-material/
scraped_at: 2025-09-08T15:44:27.352616
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

Add Material

Demonstrates how to add a material to the document and apply it to a sphere
object.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddMaterial(Rhino.RhinoDoc doc)
      {
        // Create a Rhino material with a texture.
        var rhino_material = new Material
        {
          Name = "Chocolate",
          DiffuseColor = System.Drawing.Color.Chocolate,
          SpecularColor = System.Drawing.Color.CadetBlue
        };
    
        var texture = new Texture
        {
          FileName = "my_image.jpg"
        };
        rhino_material.SetTexture(texture, TextureType.Bitmap);
    
        // Use the Rhino material to create a Render material.
        var render_material = RenderMaterial.CreateBasicMaterial(rhino_material, doc);
        doc.RenderMaterials.Add(render_material);
    
        // Create a sphere.
        var sphere = new Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 5);
    
        // Add the sphere to the document.
        var id = doc.Objects.AddSphere(sphere);
        var obj = doc.Objects.FindId(id);
        if (obj != null)
        {
          // Assign the render material to the sphere object.
          obj.RenderMaterial = render_material;
          obj.CommitChanges();
        }
    
        doc.Views.Redraw();
    
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddMaterial(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    
        Dim index As Integer = doc.Materials.Add()
        Dim mat As Rhino.DocObjects.Material = New Rhino.DocObjects.Material
        mat.DiffuseColor = System.Drawing.Color.Chocolate
        mat.SpecularColor = System.Drawing.Color.CadetBlue
    
        Dim texture As Rhino.DocObjects.Texture = New Rhino.DocObjects.Texture()
        texture.FileName = "my_image.jpg"
        mat.SetTexture(texture, TextureType.Bitmap)
    
        Dim rm As Rhino.Render.RenderMaterial = Rhino.Render.RenderMaterial.CreateBasicMaterial(mat, doc)
        doc.RenderMaterials.Add(rm)
    
        Dim sp As New Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 5)
        Dim id As Guid = doc.Objects.AddSphere(sp)
        Dim rhinoObject As RhinoObject = doc.Objects.Find(id)
        rhinoObject.RenderMaterial = rm
        rhinoObject.CommitChanges()
    
        doc.Views.Redraw()
    
        Return Rhino.Commands.Result.Success
    
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Drawing
    
    def AddMaterial():
    
        # Create a Rhino material.
        rhino_material = Rhino.DocObjects.Material();
        rhino_material.Name = "Chocolate";
        rhino_material.DiffuseColor = System.Drawing.Color.Chocolate;
        rhino_material.SpecularColor = System.Drawing.Color.CadetBlue;
        
        texture = Rhino.DocObjects.Texture()
        texture.FileName = "my_image.jpg"
        rhino_material.SetTexture(texture, Rhino.DocObjects.TextureType.Bitmap)
    
        # Use the Rhino material to create a Render material.
        render_material = Rhino.Render.RenderMaterial.CreateBasicMaterial(rhino_material, scriptcontext.doc)
        scriptcontext.doc.RenderMaterials.Add(render_material);
    
        # Create a sphere.
        sphere = Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 5);
    
        # Add the sphere to the document with a material.
        id = scriptcontext.doc.Objects.AddSphere(sphere);
        obj = scriptcontext.doc.Objects.FindId(id);
        if obj is not None:
          # Assign the render material to the sphere object.
          obj.RenderMaterial = render_material;
          obj.CommitChanges();
    
        scriptcontext.doc.Views.Redraw();
    
        return Rhino.Commands.Result.Success;
    
    if __name__=="__main__":
        AddMaterial()
    

  

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

