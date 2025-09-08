---
url: https://developer.rhino3d.com/samples/rhinocommon/add-layer/
scraped_at: 2025-09-08T15:44:22.355742
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

Add Layer

Demonstrates how to add a layer to a Rhino model and validate that it does not
already exist.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddLayer(Rhino.RhinoDoc doc)
      {
        // Cook up an unused layer name
        string unused_name = doc.Layers.GetUnusedLayerName(false);
    
        // Prompt the user to enter a layer name
        Rhino.Input.Custom.GetString gs = new Rhino.Input.Custom.GetString();
        gs.SetCommandPrompt("Name of layer to add");
        gs.SetDefaultString(unused_name);
        gs.AcceptNothing(true);
        gs.Get();
        if (gs.CommandResult() != Rhino.Commands.Result.Success)
          return gs.CommandResult();
    
        // Was a layer named entered?
        string layer_name = gs.StringResult().Trim();
        if (string.IsNullOrEmpty(layer_name))
        {
          Rhino.RhinoApp.WriteLine("Layer name cannot be blank.");
          return Rhino.Commands.Result.Cancel;
        }
    
        // Is the layer name valid?
        if (!Rhino.DocObjects.Layer.IsValidName(layer_name))
        {
          Rhino.RhinoApp.WriteLine(layer_name + " is not a valid layer name.");
          return Rhino.Commands.Result.Cancel;
        }
    
        // Does a layer with the same name already exist?
        int layer_index = doc.Layers.Find(layer_name, true);
        if (layer_index >= 0)
        {
          Rhino.RhinoApp.WriteLine("A layer with the name {0} already exists.", layer_name);
          return Rhino.Commands.Result.Cancel;
        }
    
        // Add a new layer to the document
        layer_index = doc.Layers.Add(layer_name, System.Drawing.Color.Black);
        if (layer_index < 0)
        {
          Rhino.RhinoApp.WriteLine("Unable to add {0} layer.", layer_name);
          return Rhino.Commands.Result.Failure;
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddLayer(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	' Cook up an unused layer name
    	Dim unused_name As String = doc.Layers.GetUnusedLayerName(False)
    
    	' Prompt the user to enter a layer name
    	Dim gs As New Rhino.Input.Custom.GetString()
    	gs.SetCommandPrompt("Name of layer to add")
    	gs.SetDefaultString(unused_name)
    	gs.AcceptNothing(True)
    	gs.Get()
    	If gs.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return gs.CommandResult()
    	End If
    
    	' Was a layer named entered?
    	Dim layer_name As String = gs.StringResult().Trim()
    	If String.IsNullOrEmpty(layer_name) Then
    	  Rhino.RhinoApp.WriteLine("Layer name cannot be blank.")
    	  Return Rhino.Commands.Result.Cancel
    	End If
    
    	' Is the layer name valid?
    	If Not Rhino.DocObjects.Layer.IsValidName(layer_name) Then
    	  Rhino.RhinoApp.WriteLine(layer_name & " is not a valid layer name.")
    	  Return Rhino.Commands.Result.Cancel
    	End If
    
    	' Does a layer with the same name already exist?
    	Dim layer_index As Integer = doc.Layers.Find(layer_name, True)
    	If layer_index >= 0 Then
    	  Rhino.RhinoApp.WriteLine("A layer with the name {0} already exists.", layer_name)
    	  Return Rhino.Commands.Result.Cancel
    	End If
    
    	' Add a new layer to the document
    	layer_index = doc.Layers.Add(layer_name, System.Drawing.Color.Black)
    	If layer_index < 0 Then
    	  Rhino.RhinoApp.WriteLine("Unable to add {0} layer.", layer_name)
    	  Return Rhino.Commands.Result.Failure
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid, System.Drawing.Color
    
    def AddLayer():
        # Cook up an unused layer name
        unused_name = scriptcontext.doc.Layers.GetUnusedLayerName(False)
    
        # Prompt the user to enter a layer name
        gs = Rhino.Input.Custom.GetString()
        gs.SetCommandPrompt("Name of layer to add")
        gs.SetDefaultString(unused_name)
        gs.AcceptNothing(True)
        gs.Get()
        if gs.CommandResult()!=Rhino.Commands.Result.Success:
            return gs.CommandResult()
    
        # Was a layer named entered?
        layer_name = gs.StringResult().Trim()
        if not layer_name:
            print "Layer name cannot be blank."
            return Rhino.Commands.Result.Cancel
    
        # Is the layer name valid?
        if not Rhino.DocObjects.Layer.IsValidName(layer_name):
            print layer_name, "is not a valid layer name."
            return Rhino.Commands.Result.Cancel
    
        # Does a layer with the same name already exist?
        layer_index = scriptcontext.doc.Layers.Find(layer_name, True)
        if layer_index>=0:
            print "A layer with the name", layer_name, "already exists."
            return Rhino.Commands.Result.Cancel
    
        # Add a new layer to the document
        layer_index = scriptcontext.doc.Layers.Add(layer_name, System.Drawing.Color.Black)
        if layer_index<0:
            print "Unable to add", layer_name, "layer."
            return Rhino.Commands.Result.Failure
    
        return Rhino.Commands.Result.Success
    
    
    if __name__=="__main__":
        AddLayer()
    

  

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

