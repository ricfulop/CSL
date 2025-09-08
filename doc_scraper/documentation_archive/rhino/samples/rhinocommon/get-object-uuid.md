---
url: https://developer.rhino3d.com/samples/rhinocommon/get-object-uuid/
scraped_at: 2025-09-08T15:44:46.457954
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

Get Object UUID

Demonstrates how to get the UUID (sometimes called GUID) of a Rhino object.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result GetUUID(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select object", false, ObjectType.AnyObject, out obj_ref);
        if (rc != Result.Success)
          return rc;
        if (obj_ref == null)
          return Result.Nothing;
    
        var uuid = obj_ref.ObjectId;
        RhinoApp.WriteLine("The object's unique id is {0}", uuid.ToString());
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function GetUUID(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select object", False, ObjectType.AnyObject, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	If obj_ref Is Nothing Then
    	  Return Result.Nothing
    	End If
    
    	Dim uuid = obj_ref.ObjectId
    	RhinoApp.WriteLine("The object's unique id is {0}", uuid.ToString())
    	Return Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    
    obj_id = rs.GetObject("Select object")
    if obj_id != None:
        print "The object's unique id is {0}".format(obj_id)
    

  

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

