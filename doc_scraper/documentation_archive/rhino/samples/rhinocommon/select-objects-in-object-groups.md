---
url: https://developer.rhino3d.com/samples/rhinocommon/select-objects-in-object-groups/
scraped_at: 2025-09-08T15:44:56.471785
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

Select Objects in Object Groups

Demonstrates how to select objects that are an object group.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result SelectObjectsInObjectGroups(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rs = RhinoGet.GetOneObject(
          "Select object", false, ObjectType.AnyObject, out obj_ref);
        if (rs != Result.Success)
          return rs;
        var rhino_object = obj_ref.Object();
        if (rhino_object == null)
          return Result.Failure;
    
        var rhino_object_groups = rhino_object.Attributes.GetGroupList().DefaultIfEmpty(-1);
    
        var selectable_objects= from obj in doc.Objects.GetObjectList(ObjectType.AnyObject)
                                where obj.IsSelectable(true, false, false, false)
                                select obj;
    
        foreach (var selectable_object in selectable_objects)
        {
          foreach (var group in selectable_object.Attributes.GetGroupList())
          {
            if (rhino_object_groups.Contains(group))
            {
                selectable_object.Select(true);
                continue;
            }
          }
        }
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function SelectObjectsInObjectGroups(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rs = RhinoGet.GetOneObject("Select object", False, ObjectType.AnyObject, obj_ref)
    	If rs IsNot Result.Success Then
    	  Return rs
    	End If
    	Dim rhino_object = obj_ref.Object()
    	If rhino_object Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	Dim rhino_object_groups = rhino_object.Attributes.GetGroupList().DefaultIfEmpty(-1)
    
    	Dim selectable_objects = From obj In doc.Objects.GetObjectList(ObjectType.AnyObject)
    	                         Where obj.IsSelectable(True, False, False, False)
    	                         Select obj
    
    	For Each selectable_object In selectable_objects
    	  For Each group In selectable_object.Attributes.GetGroupList()
    		If rhino_object_groups.Contains(group) Then
    			selectable_object.Select(True)
    			Continue For
    		End If
    	  Next group
    	Next selectable_object
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.Commands import *
    from Rhino.DocObjects import *
    from Rhino.Input import *
    from scriptcontext import doc
    
    def RunCommand():
        rs, obj_ref = RhinoGet.GetOneObject("Select object", False, ObjectType.AnyObject)
        if rs != Result.Success:
            return rs
        rhino_object = obj_ref.Object()
        if rhino_object == None:
            return Result.Failure
    
        rhino_object_groups = [group for group in rhino_object.Attributes.GetGroupList()]
    
        selectable_objects= [
            obj for obj in doc.Objects.GetObjectList(ObjectType.AnyObject)
            if obj.IsSelectable(True, False, False, False)]
    
        for selectable_object in selectable_objects:
            for group in selectable_object.Attributes.GetGroupList():
                if rhino_object_groups.Contains(group):
                    selectable_object.Select(True)
                    continue
    
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

