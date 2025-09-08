---
url: https://developer.rhino3d.com/samples/rhinocommon/transform-breps/
scraped_at: 2025-09-08T15:46:46.080878
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

Transform Breps

Demonstrates how to move (or transform) a user-specified Brep object.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result TransformBrep(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef rhobj;
        var rc = RhinoGet.GetOneObject("Select brep", true, Rhino.DocObjects.ObjectType.Brep, out rhobj);
        if(rc!= Rhino.Commands.Result.Success)
          return rc;
    
        // Simple translation transformation
        var xform = Rhino.Geometry.Transform.Translation(18,-18,25);
        doc.Objects.Transform(rhobj, xform, true);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function TransformBrep(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim rhobj As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select brep", True, Rhino.DocObjects.ObjectType.Brep, rhobj)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	' Simple translation transformation
    	Dim xform = Rhino.Geometry.Transform.Translation(18,-18,25)
    	doc.Objects.Transform(rhobj, xform, True)
    	doc.Views.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def TransformBrep():
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select brep", True, Rhino.DocObjects.ObjectType.Brep)
        if rc!=Rhino.Commands.Result.Success: return
    
        # Simple translation transformation
        xform = Rhino.Geometry.Transform.Translation(18,-18,25)
        scriptcontext.doc.Objects.Transform(objref, xform, True)
        scriptcontext.doc.Views.Redraw()
    
    if __name__=="__main__":
        TransformBrep()
    

  

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

