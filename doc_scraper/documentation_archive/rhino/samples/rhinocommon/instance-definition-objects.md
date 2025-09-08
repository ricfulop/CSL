---
url: https://developer.rhino3d.com/samples/rhinocommon/instance-definition-objects/
scraped_at: 2025-09-08T15:45:02.546745
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

Instance Definition Objects

Demonstrates how to print (or list) the objects that make up a block
definition.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result InstanceDefinitionObjects(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef objref;
        var rc = Rhino.Input.RhinoGet.GetOneObject("Select instance", false, Rhino.DocObjects.ObjectType.InstanceReference, out objref);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
    
        var iref = objref.Object() as Rhino.DocObjects.InstanceObject;
        if (iref != null)
        {
          var idef = iref.InstanceDefinition;
          if (idef != null)
          {
            var rhino_objects = idef.GetObjects();
            for (int i = 0; i < rhino_objects.Length; i++)
              Rhino.RhinoApp.WriteLine("Object {0} = {1}", i, rhino_objects[i].Id);
          }
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function InstanceDefinitionObjects(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select instance", False, Rhino.DocObjects.ObjectType.InstanceReference, objref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	Dim iref = TryCast(objref.Object(), Rhino.DocObjects.InstanceObject)
    	If iref IsNot Nothing Then
    	  Dim idef = iref.InstanceDefinition
    	  If idef IsNot Nothing Then
    		Dim rhino_objects = idef.GetObjects()
    		For i As Integer = 0 To rhino_objects.Length - 1
    		  Rhino.RhinoApp.WriteLine("Object {0} = {1}", i, rhino_objects(i).Id)
    		Next i
    	  End If
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def InstanceDefinitionObjects():
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select instance", False, Rhino.DocObjects.ObjectType.InstanceReference)
        if rc != Rhino.Commands.Result.Success: return
    
        iref = objref.Object()
        if iref:
            idef = iref.InstanceDefinition
            if idef:
                rhino_objects = idef.GetObjects()
                for i, rhobj in enumerate(rhino_objects):
                    print "Object", i, "=", rhobj.Id
    
    if __name__=="__main__":
        InstanceDefinitionObjects()
    

  

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

