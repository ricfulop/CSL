---
url: https://developer.rhino3d.com/samples/rhinocommon/modify-object-color/
scraped_at: 2025-09-08T15:44:47.444773
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

Modify Object Color

Demonstrates how to modify the color of a user-specified object.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ModifyObjectColor(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select object", false, ObjectType.AnyObject, out obj_ref);
        if (rc != Result.Success)
          return rc;
        var rhino_object = obj_ref.Object();
        var color = rhino_object.Attributes.ObjectColor;
        bool b = Rhino.UI.Dialogs.ShowColorDialog(ref color);
        if (!b) return Result.Cancel;
    
        rhino_object.Attributes.ObjectColor = color;
        rhino_object.Attributes.ColorSource = ObjectColorSource.ColorFromObject;
        rhino_object.CommitChanges();
    
        // an object's color attributes can also be specified
        // when the object is added to Rhino
        var sphere = new Sphere(Point3d.Origin, 5.0);
        var attributes = new ObjectAttributes();
        attributes.ObjectColor = Color.CadetBlue;
        attributes.ColorSource = ObjectColorSource.ColorFromObject;
        doc.Objects.AddSphere(sphere, attributes);
    
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ModifyObjectColor(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select object", False, ObjectType.AnyObject, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim rhino_object = obj_ref.Object()
    	Dim color = rhino_object.Attributes.ObjectColor
    	Dim b As Boolean = Rhino.UI.Dialogs.ShowColorDialog(color)
    	If Not b Then
    		Return Result.Cancel
    	End If
    
    	rhino_object.Attributes.ObjectColor = color
    	rhino_object.Attributes.ColorSource = ObjectColorSource.ColorFromObject
    	rhino_object.CommitChanges()
    
    	' an object's color attributes can also be specified
    	' when the object is added to Rhino
    	Dim sphere = New Sphere(Point3d.Origin, 5.0)
    	Dim attributes = New ObjectAttributes()
    	attributes.ObjectColor = System.Drawing.Color.CadetBlue
    	attributes.ColorSource = ObjectColorSource.ColorFromObject
    	doc.Objects.AddSphere(sphere, attributes)
    
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from System.Drawing import *
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Geometry import *
    from Rhino.Input import *
    from Rhino.Commands import *
    from Rhino.UI.Dialogs import ShowColorDialog
    from scriptcontext import doc
    
    def RunCommand():
        rc, obj_ref = RhinoGet.GetOneObject("Select object", False, ObjectType.AnyObject)
        if rc != Result.Success:
            return rc
        rhino_object = obj_ref.Object()
        color = rhino_object.Attributes.ObjectColor
        b, color = ShowColorDialog(color)
        if not b: return Result.Cancel
    
        rhino_object.Attributes.ObjectColor = color
        rhino_object.Attributes.ColorSource = ObjectColorSource.ColorFromObject
        rhino_object.CommitChanges()
    
        # an object's color attributes can also be specified
        # when the object is added to Rhino
        sphere = Sphere(Point3d.Origin, 5.0)
        attributes = ObjectAttributes()
        attributes.ObjectColor = Color.CadetBlue
        attributes.ColorSource = ObjectColorSource.ColorFromObject
        doc.Objects.AddSphere(sphere, attributes)
    
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

