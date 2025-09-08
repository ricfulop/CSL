---
url: https://developer.rhino3d.com/samples/rhinocommon/isocurve-density/
scraped_at: 2025-09-08T15:46:21.704513
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

Isocurve Density

Demonstrates how to adjust the the isocurve density of a user-specified
surface.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result IsocurveDensity(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef objref;
        var rc = Rhino.Input.RhinoGet.GetOneObject("Select surface", false, Rhino.DocObjects.ObjectType.Surface, out objref);
        if( rc!= Rhino.Commands.Result.Success )
          return rc;
    
        var brep_obj = objref.Object() as Rhino.DocObjects.BrepObject;
        if( brep_obj!=null )
        {
          brep_obj.Attributes.WireDensity = 3;
          brep_obj.CommitChanges();
          doc.Views.Redraw();
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function IsocurveDensity(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select surface", False, Rhino.DocObjects.ObjectType.Surface, objref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	Dim brep_obj = TryCast(objref.Object(), Rhino.DocObjects.BrepObject)
    	If brep_obj IsNot Nothing Then
    	  brep_obj.Attributes.WireDensity = 3
    	  brep_obj.CommitChanges()
    	  doc.Views.Redraw()
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def IsocurveDensity():
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select surface", False, Rhino.DocObjects.ObjectType.Surface)
        if rc!= Rhino.Commands.Result.Success: return
    
        brep_obj = objref.Object()
        if brep_obj:
            brep_obj.Attributes.WireDensity = 3
            brep_obj.CommitChanges()
            scriptcontext.doc.Views.Redraw()
    
    if __name__=="__main__":
        IsocurveDensity()
    

  

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

