---
url: https://developer.rhino3d.com/samples/rhinocommon/duplicate-object/
scraped_at: 2025-09-08T15:44:43.429547
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

Duplicate Object

Demonstrates how to clone (or copy, or duplicate) a Rhino object.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result DuplicateObject(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select object to duplicate", false, ObjectType.AnyObject, out obj_ref);
        if (rc != Result.Success)
          return rc;
        var rhino_object = obj_ref.Object();
    
        var geometry_base = rhino_object.DuplicateGeometry();
        if (geometry_base != null)
          if (doc.Objects.Add(geometry_base) != Guid.Empty)
            doc.Views.Redraw();
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function DuplicateObject(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select object to duplicate", False, ObjectType.AnyObject, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim rhino_object = obj_ref.Object()
    
    	Dim geometry_base = rhino_object.DuplicateGeometry()
    	If geometry_base IsNot Nothing Then
    	  If doc.Objects.Add(geometry_base) <> Guid.Empty Then
    		doc.Views.Redraw()
    	  End If
    	End If
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    from System import *
    from Rhino import *
    from Rhino.Commands import *
    from Rhino.DocObjects import *
    from Rhino.Input import *
    from scriptcontext import doc
    
    def RunCommand():
    
        rc, obj_ref = RhinoGet.GetOneObject("Select object to duplicate", False, ObjectType.AnyObject)
        if rc != Result.Success:
            return rc
        rhino_object = obj_ref.Object()
    
        geometry_base = rhino_object.DuplicateGeometry()
        if geometry_base != None:
            if doc.Objects.Add(geometry_base) != Guid.Empty:
                doc.Views.Redraw()
    
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

