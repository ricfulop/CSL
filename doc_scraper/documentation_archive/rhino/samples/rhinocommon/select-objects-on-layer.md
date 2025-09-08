---
url: https://developer.rhino3d.com/samples/rhinocommon/select-objects-on-layer/
scraped_at: 2025-09-08T15:44:57.502406
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

Select Objects on Layer

Demonstrates how to select all the objects on a user-specified layer.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result SelLayer(Rhino.RhinoDoc doc)
      {
        // Prompt for a layer name
        string layername = doc.Layers.CurrentLayer.Name;
        Result rc = Rhino.Input.RhinoGet.GetString("Name of layer to select objects", true, ref layername);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
    
        // Get all of the objects on the layer. If layername is bogus, you will
        // just get an empty list back
        Rhino.DocObjects.RhinoObject[] rhobjs = doc.Objects.FindByLayer(layername);
        if (rhobjs == null || rhobjs.Length < 1)
          return Rhino.Commands.Result.Cancel;
    
        for (int i = 0; i < rhobjs.Length; i++)
          rhobjs[i].Select(true);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function SelLayer(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	' Prompt for a layer name
    	Dim layername As String = doc.Layers.CurrentLayer.Name
    	Dim rc As Result = Rhino.Input.RhinoGet.GetString("Name of layer to select objects", True, layername)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	' Get all of the objects on the layer. If layername is bogus, you will
    	' just get an empty list back
    	Dim rhobjs() As Rhino.DocObjects.RhinoObject = doc.Objects.FindByLayer(layername)
    	If rhobjs Is Nothing OrElse rhobjs.Length < 1 Then
    	  Return Rhino.Commands.Result.Cancel
    	End If
    
    	For i As Integer = 0 To rhobjs.Length - 1
    	  rhobjs(i).Select(True)
    	Next i
    	doc.Views.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid, System.Drawing.Color
    
    def SelLayer():
        # Prompt for a layer name
        layername = scriptcontext.doc.Layers.CurrentLayer.Name
        rc, layername = Rhino.Input.RhinoGet.GetString("Name of layer to select objects", True, layername)
        if rc!=Rhino.Commands.Result.Success: return rc
    
        # Get all of the objects on the layer. If layername is bogus, you will
        # just get an empty list back
        rhobjs = scriptcontext.doc.Objects.FindByLayer(layername)
        if not rhobjs: Rhino.Commands.Result.Cancel
    
        for obj in rhobjs: obj.Select(True)
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        SelLayer()
    

  

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

