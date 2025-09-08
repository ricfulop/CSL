---
url: https://developer.rhino3d.com/samples/rhinocommon/block-insertion-point/
scraped_at: 2025-09-08T15:45:00.493905
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

Block Insertion Point

Demonstrates how to set (or reset) the block insertion point of a block
instance.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result BlockInsertionPoint(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef objref;
        Result rc = Rhino.Input.RhinoGet.GetOneObject("Select instance", true, Rhino.DocObjects.ObjectType.InstanceReference, out objref);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
        Rhino.DocObjects.InstanceObject instance = objref.Object() as Rhino.DocObjects.InstanceObject;
        if (instance != null)
        {
          Rhino.Geometry.Point3d pt = instance.InsertionPoint;
          doc.Objects.AddPoint(pt);
          doc.Views.Redraw();
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function BlockInsertionPoint(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc As Result = Rhino.Input.RhinoGet.GetOneObject("Select instance", True, Rhino.DocObjects.ObjectType.InstanceReference, objref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    	Dim instance As Rhino.DocObjects.InstanceObject = TryCast(objref.Object(), Rhino.DocObjects.InstanceObject)
    	If instance IsNot Nothing Then
    	  Dim pt As Rhino.Geometry.Point3d = instance.InsertionPoint
    	  doc.Objects.AddPoint(pt)
    	  doc.Views.Redraw()
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def BlockInsertionPoint():
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select instance", True, Rhino.DocObjects.ObjectType.InstanceReference)
        if rc!=Rhino.Commands.Result.Success: return rc;
        instance = objref.Object()
        if instance:
            pt = instance.InsertionPoint
            scriptcontext.doc.Objects.AddPoint(pt)
            scriptcontext.doc.Views.Redraw()
            return Rhino.Commands.Result.Success
        return Rhino.Commands.Result.Failure
    
    if __name__=="__main__":
        BlockInsertionPoint()
    

  

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

