---
url: https://developer.rhino3d.com/samples/rhinocommon/determine-object-layer/
scraped_at: 2025-09-08T15:44:42.412439
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

Determine Object Layer

Demonstrates how to determine which layer a user-specified object is on and
print the name.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result DetermineObjectLayer(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef obref;
        Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select object", true, Rhino.DocObjects.ObjectType.AnyObject, out obref);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
        Rhino.DocObjects.RhinoObject rhobj = obref.Object();
        if (rhobj == null)
          return Rhino.Commands.Result.Failure;
        int index = rhobj.Attributes.LayerIndex;
        string name = doc.Layers[index].Name;
        Rhino.RhinoApp.WriteLine("The selected object's layer is '{0}'", name);
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function DetermineObjectLayer(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim obref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select object", True, Rhino.DocObjects.ObjectType.AnyObject, obref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    	Dim rhobj As Rhino.DocObjects.RhinoObject = obref.Object()
    	If rhobj Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    	Dim index As Integer = rhobj.Attributes.LayerIndex
    	Dim name As String = doc.Layers(index).Name
    	Rhino.RhinoApp.WriteLine("The selected object's layer is '{0}'", name)
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def DetermineObjectLayer():
        rc, obref = Rhino.Input.RhinoGet.GetOneObject("Select object", True, Rhino.DocObjects.ObjectType.AnyObject)
        if rc!=Rhino.Commands.Result.Success: return rc
        rhobj = obref.Object()
        if rhobj is None: return Rhino.Commands.Result.Failure
        index = rhobj.Attributes.LayerIndex
        name = scriptcontext.doc.Layers[index].Name
        print "The selected object's layer is '", name, "'"
        return Rhino.Commands.Result.Success
    
    if __name__ == "__main__":
        DetermineObjectLayer()
    

  

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

