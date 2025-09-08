---
url: https://developer.rhino3d.com/samples/rhinocommon/add-texture/
scraped_at: 2025-09-08T15:44:36.414748
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

Add Texture

Demonstrates how to add a texture to an object from a user-specified bitmap
file.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddTexture(Rhino.RhinoDoc doc)
      {
        // Select object to add texture to.
        const ObjectType filter = Rhino.DocObjects.ObjectType.Surface |
                                  Rhino.DocObjects.ObjectType.PolysrfFilter |
                                  Rhino.DocObjects.ObjectType.Mesh;
        var rc = Rhino.Input.RhinoGet.GetOneObject("Select object to add texture", false, filter, out ObjRef objref);
        if (rc != Rhino.Commands.Result.Success)
        return rc;
    
        var rhino_object = objref.Object();
        if (rhino_object == null)
          return Rhino.Commands.Result.Failure;
    
        // Choose a texture file.
        var fd = new Rhino.UI.OpenFileDialog
        {
          Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"
        };
        if (!fd.ShowOpenDialog())
          return Rhino.Commands.Result.Cancel;
    
        // Verify that the file exists.
        string bitmap_filename = fd.FileName;
        if (string.IsNullOrEmpty(bitmap_filename) || !System.IO.File.Exists(bitmap_filename))
          return Rhino.Commands.Result.Nothing;
    
        // Make sure the object has a render material assigned.
        if (rhino_object.RenderMaterial == null)
        {
          // Create a Rhino material.
          var rhino_material = new Rhino.DocObjects.Material()
          {
            DiffuseColor = System.Drawing.Color.White
          };
    
          // Create a basic Render material from the Rhino material.
          var render_material = Rhino.Render.RenderMaterial.CreateBasicMaterial(rhino_material, doc);
    
          // Create a Rhino texture for the filename.
          var tex = new Rhino.DocObjects.Texture
          {
            FileName = bitmap_filename
          };
    
          // Create a bitmap texture from the Rhino texture.
          var sim = new Rhino.Render.SimulatedTexture(doc, tex);
          var render_texture = Rhino.Render.RenderTexture.NewBitmapTexture(sim, doc);
    
          // Set the texture as a child of the material in the bump slot.
          var child_slot_name = "bump-texture";
          render_material.SetChild(render_texture, child_slot_name);
          render_material.SetChildSlotOn(child_slot_name, true, Rhino.Render.RenderContent.ChangeContexts.Program);
          render_material.SetChildSlotAmount(child_slot_name, 100.0, Rhino.Render.RenderContent.ChangeContexts.Program);
    
          // Add the basic Render material to the document.
          doc.RenderMaterials.Add(render_material);
    
          // Assign the render material to the object.
          rhino_object.RenderMaterial = render_material;
    
          // Don't forget to update the object, if necessary.
          rhino_object.CommitChanges();
        }
    
        doc.Views.Redraw();
    
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddTexture(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
      
      	' TODO: This needs to be converted to be the same as the C# method.
      
    	' Select object to add texture to.
    	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Surface Or Rhino.DocObjects.ObjectType.PolysrfFilter Or Rhino.DocObjects.ObjectType.Mesh
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select object to add texture", False, filter, objref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	Dim rhino_object As Rhino.DocObjects.RhinoObject = objref.Object()
    	If rhino_object Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	' Choose a texture file.
    	Dim fd As New Rhino.UI.OpenFileDialog()
    	fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"
    	If Not fd.ShowDialog() Then
    	  Return Rhino.Commands.Result.Cancel
    	End If
    
    	' Verify that the file exists.
    	Dim bitmap_filename As String = fd.FileName
    	If String.IsNullOrEmpty(bitmap_filename) OrElse Not System.IO.File.Exists(bitmap_filename) Then
    	  Return Rhino.Commands.Result.Nothing
    	End If
    
    	' Make sure the object has it's material source set to "material_from_object"
    	rhino_object.Attributes.MaterialSource = Rhino.DocObjects.ObjectMaterialSource.MaterialFromObject
    
    	' Make sure the object has a material assigned.
    	Dim material_index As Integer = rhino_object.Attributes.MaterialIndex
    	If material_index < 0 Then
    	  ' Create a new material based on Rhino's default material
    	  material_index = doc.Materials.Add()
    	  ' Assign the new material (index) to the object.
    	  rhino_object.Attributes.MaterialIndex = material_index
    	End If
    
    	If material_index >= 0 Then
    	  Dim mat As Rhino.DocObjects.Material = doc.Materials(material_index)
    	  mat.SetBumpTexture(bitmap_filename)
    	  mat.CommitChanges()
    
    	  ' Don't forget to update the object, if necessary.
    	  rhino_object.CommitChanges()
    
    	  doc.Views.Redraw()
    	  Return Rhino.Commands.Result.Success
    	End If
    
    	Return Rhino.Commands.Result.Failure
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    import System.Windows.Forms.DialogResult
    import System.IO.File
    
    def AddTexture():
        # Select object to add texture to.
        filter = Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter | Rhino.DocObjects.ObjectType.Mesh
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select object to add texture", False, filter)
        if rc != Rhino.Commands.Result.Success:
            return rc
    
        rhino_object = objref.Object()
        if rhino_object is None:
            return Rhino.Commands.Result.Failure
    
        # Choose a texture file.
        fd = Rhino.UI.OpenFileDialog()
        fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"
        if not fd.ShowDialog():
            return Rhino.Commands.Result.Cancel
    
        # Verify that the file exists.
        bitmap_filename = fd.FileName
        if not System.IO.File.Exists(bitmap_filename):
            return Rhino.Commands.Result.Nothing
    
        # Make sure the object has a render material assigned.
        if rhino_object.RenderMaterial is None:
          
          # Create a Rhino material.
          rhino_material = Rhino.DocObjects.Material()
          rhino_material.DiffuseColor = System.Drawing.Color.White
    
          # Create a basic Render material from the Rhino material.
          render_material = Rhino.Render.RenderMaterial.CreateBasicMaterial(rhino_material, scriptcontext.doc);
    
          # Create a Rhino texture for the filename.
          tex = Rhino.DocObjects.Texture()
          tex.FileName = bitmap_filename
    
          # Create a bitmap texture from the Rhino texture.
          sim = Rhino.Render.SimulatedTexture(scriptcontext.doc, tex);
          render_texture = Rhino.Render.RenderTexture.NewBitmapTexture(sim, scriptcontext.doc);
    
          # Set the texture as a child of the material in the bump slot.
          child_slot_name = "bump-texture";
          render_material.SetChild(render_texture, child_slot_name);
          render_material.SetChildSlotOn(child_slot_name, True, Rhino.Render.RenderContent.ChangeContexts.Program);
          render_material.SetChildSlotAmount(child_slot_name, 100.0, Rhino.Render.RenderContent.ChangeContexts.Program);
    
          # Add the basic Render material to the document.
          scriptcontext.doc.RenderMaterials.Add(render_material);
    
          # Assign the render material to the object.
          rhino_object.RenderMaterial = render_material;
    
          # Don't forget to update the object, if necessary.
          rhino_object.CommitChanges();
    
        scriptcontext.doc.Views.Redraw();
    
        return Rhino.Commands.Result.Success;
    
    if __name__=="__main__":
        AddTexture()
    

  

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

