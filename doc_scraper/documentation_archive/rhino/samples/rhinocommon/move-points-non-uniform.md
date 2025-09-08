---
url: https://developer.rhino3d.com/samples/rhinocommon/move-points-non-uniform/
scraped_at: 2025-09-08T15:46:27.758832
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

Move Points Non Uniform

Demonstrates how to move points in a non-uniform manner.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result MovePointObjectsNonUniform(RhinoDoc doc)
      {
        ObjRef[] obj_refs;
        var rc = RhinoGet.GetMultipleObjects("Select points to move", false, ObjectType.Point, out obj_refs);
        if (rc != Result.Success || obj_refs == null)
          return rc;
    
        foreach (var obj_ref in obj_refs)
        {
          var point3d = obj_ref.Point().Location;
          // modify the point coordinates in some way ...
          point3d.X++;
          point3d.Y++;
          point3d.Z++;
    
          doc.Objects.Replace(obj_ref, point3d);
        }
    
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function MovePointObjectsNonUniform(ByVal doc As RhinoDoc) As Result
    	Dim obj_refs() As ObjRef = Nothing
    	Dim rc = RhinoGet.GetMultipleObjects("Select points to move", False, ObjectType.Point, obj_refs)
    	If rc IsNot Result.Success OrElse obj_refs Is Nothing Then
    	  Return rc
    	End If
    
    	For Each obj_ref In obj_refs
    	  Dim point3d = obj_ref.Point().Location
    	  ' modify the point coordinates in some way ...
    	  point3d.X += 1
    	  point3d.Y += 1
    	  point3d.Z += 1
    
    	  doc.Objects.Replace(obj_ref, point3d)
    	Next obj_ref
    
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Commands import *
    from Rhino.Input import *
    from scriptcontext import doc
    
    def RunCommand():
        rc, obj_refs = RhinoGet.GetMultipleObjects("Select points to move", False, ObjectType.Point)
        if rc != Result.Success or obj_refs == None:
            return rc
    
        for obj_ref in obj_refs:
            point3d = obj_ref.Point().Location
            point3d.X += 1
            point3d.Y += 1
            point3d.Z += 1
            doc.Objects.Replace(obj_ref, point3d)
    
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

