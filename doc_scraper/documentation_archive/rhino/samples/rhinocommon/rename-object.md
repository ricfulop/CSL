---
url: https://developer.rhino3d.com/samples/rhinocommon/rename-object/
scraped_at: 2025-09-08T15:44:54.459479
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

Rename Object

Demonstrates how to rename a user-specified object.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result RenameObject(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select object to change name", true, ObjectType.AnyObject, out obj_ref);
        if (rc != Result.Success)
          return rc;
        var rhino_object = obj_ref.Object();
    
        var new_object_name = "";
        rc = RhinoGet.GetString("New object name", true, ref new_object_name);
        if (rc != Result.Success)
          return rc;
        if (string.IsNullOrWhiteSpace(new_object_name))
          return Result.Nothing;
    
        if (rhino_object.Name != new_object_name)
        {
          rhino_object.Attributes.Name = new_object_name;
          rhino_object.CommitChanges();
        }
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function RenameObject(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select object to change name", True, ObjectType.AnyObject, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim rhino_object = obj_ref.Object()
    
    	Dim new_object_name = ""
    	rc = RhinoGet.GetString("New object name", True, new_object_name)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	If String.IsNullOrWhiteSpace(new_object_name) Then
    	  Return Result.Nothing
    	End If
    
    	If rhino_object.Name <> new_object_name Then
    	  rhino_object.Attributes.Name = new_object_name
    	  rhino_object.CommitChanges()
    	End If
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    
    obj_id = rs.GetObject("Select object to change name")
    object_new_name = rs.GetString("New object name")
    
    rs.ObjectName(obj_id, object_new_name)
    

  

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

