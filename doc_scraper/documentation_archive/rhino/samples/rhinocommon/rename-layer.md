---
url: https://developer.rhino3d.com/samples/rhinocommon/rename-layer/
scraped_at: 2025-09-08T15:45:30.642143
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

Rename Layer

Demonstrates how to rename a layer.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result RenameLayer(RhinoDoc doc)
      {
        string layer_name = "";
        var rc = RhinoGet.GetString("Name of layer to rename", true, ref layer_name);
        if (rc != Result.Success)
          return rc;
        if (String.IsNullOrWhiteSpace(layer_name))
          return Result.Nothing;
    
        // because of sublayers it's possible that more than one layer has the same name
        // so simply calling doc.Layers.Find(layerName) isn't good enough.  If "layerName" returns
        // more than one layer then present them to the user and let him decide.
        var matching_layers = (from layer in doc.Layers
                               where layer.Name == layer_name
                               select layer).ToList<Layer>();
    
        Layer layer_to_rename = null;
        if (matching_layers.Count == 0)
        {
          RhinoApp.WriteLine("Layer \"{0}\" does not exist.", layer_name);
          return Result.Nothing;
        }
        else if (matching_layers.Count == 1)
        {
          layer_to_rename = matching_layers[0];
        }
        else if (matching_layers.Count > 1)
        {
          for (int i = 0; i < matching_layers.Count; i++)
          {
            RhinoApp.WriteLine("({0}) {1}", i+1, matching_layers[i].FullPath.Replace("::", "->"));
          }
          int selected_layer = -1;
          rc = RhinoGet.GetInteger("which layer?", true, ref selected_layer);
          if (rc != Result.Success)
            return rc;
          if (selected_layer > 0 && selected_layer <= matching_layers.Count)
            layer_to_rename = matching_layers[selected_layer - 1];
          else return Result.Nothing;
        }
    
        if (layer_to_rename == null)
          return Result.Nothing;
    
        layer_name = "";
        rc = RhinoGet.GetString("New layer name", true, ref layer_name);
        if (rc != Result.Success)
          return rc;
        if (String.IsNullOrWhiteSpace(layer_name))
          return Result.Nothing;
    
        layer_to_rename.Name = layer_name;
        if (!layer_to_rename.CommitChanges())
          return Result.Failure;
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function RenameLayer(ByVal doc As RhinoDoc) As Result
    	Dim layer_name As String = ""
    	Dim rc = RhinoGet.GetString("Name of layer to rename", True, layer_name)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	If String.IsNullOrWhiteSpace(layer_name) Then
    	  Return Result.Nothing
    	End If
    
    	' because of sublayers it's possible that more than one layer has the same name
    	' so simply calling doc.Layers.Find(layerName) isn't good enough.  If "layerName" returns
    	' more than one layer then present them to the user and let him decide.
    	Dim matching_layers = (
    	    From layer In doc.Layers
    	    Where layer.Name = layer_name
    	    Select layer).ToList()
    
    	Dim layer_to_rename As Layer = Nothing
    	If matching_layers.Count = 0 Then
    	  RhinoApp.WriteLine("Layer ""{0}"" does not exist.", layer_name)
    	  Return Result.Nothing
    	ElseIf matching_layers.Count = 1 Then
    	  layer_to_rename = matching_layers(0)
    	ElseIf matching_layers.Count > 1 Then
    	  For i As Integer = 0 To matching_layers.Count - 1
    		RhinoApp.WriteLine("({0}) {1}", i+1, matching_layers(i).FullPath.Replace("::", "->"))
    	  Next i
    	  Dim selected_layer As Integer = -1
    	  rc = RhinoGet.GetInteger("which layer?", True, selected_layer)
    	  If rc IsNot Result.Success Then
    		Return rc
    	  End If
    	  If selected_layer > 0 AndAlso selected_layer <= matching_layers.Count Then
    		layer_to_rename = matching_layers(selected_layer - 1)
    	  Else
    		  Return Result.Nothing
    	  End If
    	End If
    
    	If layer_to_rename Is Nothing Then
    	  Return Result.Nothing
    	End If
    
    	layer_name = ""
    	rc = RhinoGet.GetString("New layer name", True, layer_name)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	If String.IsNullOrWhiteSpace(layer_name) Then
    	  Return Result.Nothing
    	End If
    
    	layer_to_rename.Name = layer_name
    	If Not layer_to_rename.CommitChanges() Then
    	  Return Result.Failure
    	End If
    	Return Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    from scriptcontext import doc
    
    def rename():
        layerName = rs.GetString("Name of layer to rename")
    
        matchingLayers = [layer for layer in doc.Layers if layer.Name == layerName]
    
        layerToRename = None
        if len(matchingLayers) == 0:
            print "Layer \"{0}\" does not exist.".format(layerName)
            return
        if len(matchingLayers) == 1:
            layerToRename = matchingLayers[0]
        elif len(matchingLayers) > 1:
            i = 0;
            for layer in matchingLayers:
                print "({0}) {1}".format(
                    i+1, matchingLayers[i].FullPath.replace("::", "->"))
                i += 1
    
            selectedLayer = rs.GetInteger(
                "which layer?", -1, 1, len(matchingLayers))
            if selectedLayer == None:
                return
            layerToRename = matchingLayers[selectedLayer - 1]
    
        layerName = rs.GetString("New layer name")
        layerToRename.Name = layerName
        layerToRename.CommitChanges()
        return
    
    if __name__ == "__main__":
        rename()
    

  

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

