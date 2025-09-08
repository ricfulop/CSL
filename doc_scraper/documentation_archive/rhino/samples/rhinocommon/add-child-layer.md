---
url: https://developer.rhino3d.com/samples/rhinocommon/add-child-layer/
scraped_at: 2025-09-08T15:44:16.187455
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

Add Child Layer

Demonstrates how to add a child (or sub) layer to a parent layer in a Rhino
model.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddChildLayer(Rhino.RhinoDoc doc)
      {
        // Get an existing layer
        string default_name = doc.Layers.CurrentLayer.Name;
    
        // Prompt the user to enter a layer name
        Rhino.Input.Custom.GetString gs = new Rhino.Input.Custom.GetString();
        gs.SetCommandPrompt("Name of existing layer");
        gs.SetDefaultString(default_name);
        gs.AcceptNothing(true);
        gs.Get();
        if (gs.CommandResult() != Rhino.Commands.Result.Success)
          return gs.CommandResult();
    
        // Was a layer named entered?
        string layer_name = gs.StringResult().Trim();
        int index = doc.Layers.Find(layer_name, true);
        if (index<0)
          return Rhino.Commands.Result.Cancel;
    
        Rhino.DocObjects.Layer parent_layer = doc.Layers[index];
    
        // Create a child layer
        string child_name = parent_layer.Name + "_child";
        Rhino.DocObjects.Layer childlayer = new Rhino.DocObjects.Layer();
        childlayer.ParentLayerId = parent_layer.Id;
        childlayer.Name = child_name;
        childlayer.Color = System.Drawing.Color.Red;
    
        index = doc.Layers.Add(childlayer);
        if (index < 0)
        {
          Rhino.RhinoApp.WriteLine("Unable to add {0} layer.", child_name);
          return Rhino.Commands.Result.Failure;
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddChildLayer(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	' Get an existing layer
    	Dim default_name As String = doc.Layers.CurrentLayer.Name
    
    	' Prompt the user to enter a layer name
    	Dim gs As New Rhino.Input.Custom.GetString()
    	gs.SetCommandPrompt("Name of existing layer")
    	gs.SetDefaultString(default_name)
    	gs.AcceptNothing(True)
    	gs.Get()
    	If gs.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return gs.CommandResult()
    	End If
    
    	' Was a layer named entered?
    	Dim layer_name As String = gs.StringResult().Trim()
    	Dim index As Integer = doc.Layers.Find(layer_name, True)
    	If index<0 Then
    	  Return Rhino.Commands.Result.Cancel
    	End If
    
    	Dim parent_layer As Rhino.DocObjects.Layer = doc.Layers(index)
    
    	' Create a child layer
    	Dim child_name As String = parent_layer.Name & "_child"
    	Dim childlayer As New Rhino.DocObjects.Layer()
    	childlayer.ParentLayerId = parent_layer.Id
    	childlayer.Name = child_name
    	childlayer.Color = System.Drawing.Color.Red
    
    	index = doc.Layers.Add(childlayer)
    	If index < 0 Then
    	  Rhino.RhinoApp.WriteLine("Unable to add {0} layer.", child_name)
    	  Return Rhino.Commands.Result.Failure
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Drawing.Color
    
    def AddChildLayer():
        # Get an existing layer
        default_name = scriptcontext.doc.Layers.CurrentLayer.Name
        # Prompt the user to enter a layer name
        gs = Rhino.Input.Custom.GetString()
        gs.SetCommandPrompt("Name of existing layer")
        gs.SetDefaultString(default_name)
        gs.AcceptNothing(True)
        gs.Get()
        if gs.CommandResult()!=Rhino.Commands.Result.Success:
            return gs.CommandResult()
    
        # Was a layer named entered?
        layer_name = gs.StringResult().Trim()
        index = scriptcontext.doc.Layers.Find(layer_name, True)
        if index<0: return Rhino.Commands.Result.Cancel
    
        parent_layer = scriptcontext.doc.Layers[index]
    
        # Create a child layer
        child_name = parent_layer.Name + "_child"
        childlayer = Rhino.DocObjects.Layer()
        childlayer.ParentLayerId = parent_layer.Id
        childlayer.Name = child_name
        childlayer.Color = System.Drawing.Color.Red
    
        index = scriptcontext.doc.Layers.Add(childlayer)
        if index<0:
            print "Unable to add", child_name, "layer."
            return Rhino.Commands.Result.Failure
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        AddChildLayer()
    

  

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

