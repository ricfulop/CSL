---
url: https://developer.rhino3d.com/samples/rhinocommon/object-color/
scraped_at: 2025-09-08T15:44:50.454169
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

Object Color

Demonstrates how to set the color of user-specified objects.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result ObjectColor(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef[] objRefs;
        Rhino.Commands.Result cmdResult = Rhino.Input.RhinoGet.GetMultipleObjects("Select objects to change color", false, Rhino.DocObjects.ObjectType.AnyObject, out objRefs);
        if (cmdResult != Rhino.Commands.Result.Success)
          return cmdResult;
    
        System.Drawing.Color color = System.Drawing.Color.Black;
        bool rc = Rhino.UI.Dialogs.ShowColorDialog(ref color);
        if (!rc)
          return Rhino.Commands.Result.Cancel;
    
        for (int i = 0; i < objRefs.Length; i++)
        {
          Rhino.DocObjects.RhinoObject obj = objRefs[i].Object();
          if (null == obj || obj.IsReference)
            continue;
    
          if (color != obj.Attributes.ObjectColor)
          {
            obj.Attributes.ObjectColor = color;
            obj.Attributes.ColorSource = Rhino.DocObjects.ObjectColorSource.ColorFromObject;
            obj.CommitChanges();
          }
        }
    
        doc.Views.Redraw();
    
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ObjectColor(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim objRefs() As Rhino.DocObjects.ObjRef = Nothing
    	Dim cmdResult As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetMultipleObjects("Select objects to change color", False, Rhino.DocObjects.ObjectType.AnyObject, objRefs)
    	If cmdResult IsNot Rhino.Commands.Result.Success Then
    	  Return cmdResult
    	End If
    
    	Dim color As System.Drawing.Color = System.Drawing.Color.Black
    	Dim rc As Boolean = Rhino.UI.Dialogs.ShowColorDialog(color)
    	If Not rc Then
    	  Return Rhino.Commands.Result.Cancel
    	End If
    
    	For i As Integer = 0 To objRefs.Length - 1
    	  Dim obj As Rhino.DocObjects.RhinoObject = objRefs(i).Object()
    	  If Nothing Is obj OrElse obj.IsReference Then
    		Continue For
    	  End If
    
    	  If color <> obj.Attributes.ObjectColor Then
    		obj.Attributes.ObjectColor = color
    		obj.Attributes.ColorSource = Rhino.DocObjects.ObjectColorSource.ColorFromObject
    		obj.CommitChanges()
    	  End If
    	Next i
    
    	doc.Views.Redraw()
    
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

