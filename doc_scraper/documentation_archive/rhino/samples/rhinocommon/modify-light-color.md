---
url: https://developer.rhino3d.com/samples/rhinocommon/modify-light-color/
scraped_at: 2025-09-08T15:46:24.846959
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

Modify Light Color

Demonstrates how to change the color of a user-specified light.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ModifyLightColor(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select light to change color", true,
          ObjectType.Light, out obj_ref);
        if (rc != Result.Success)
          return rc;
        var light = obj_ref.Light();
        if (light == null)
          return Result.Failure;
    
        var diffuse_color = light.Diffuse;
        if (Dialogs.ShowColorDialog(ref diffuse_color))
        {
          light.Diffuse = diffuse_color;
        }
    
        doc.Lights.Modify(obj_ref.ObjectId, light);
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ModifyLightColor(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select light to change color", True, ObjectType.Light, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim light = obj_ref.Light()
    	If light Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	Dim diffuse_color = light.Diffuse
    	If Dialogs.ShowColorDialog(diffuse_color) Then
    	  light.Diffuse = diffuse_color
    	End If
    
    	doc.Lights.Modify(obj_ref.ObjectId, light)
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Input import *
    from Rhino.UI import *
    from Rhino.Commands import Result
    from scriptcontext import doc
    
    def RunCommand():
        rc, obj_ref = RhinoGet.GetOneObject("Select light to change color", True, ObjectType.Light)
        if rc != Result.Success:
            return rc
        light = obj_ref.Light()
        if light == None:
            return Result.Failure
    
        b, color = Dialogs.ShowColorDialog(light.Diffuse)
        if b:
            light.Diffuse = color
    
        doc.Lights.Modify(obj_ref.ObjectId, light)
        return Result.Success
    
    if __name__ == "__main__":
        RunCommand()
    

  

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

