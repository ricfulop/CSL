---
url: https://developer.rhino3d.com/samples/rhinocommon/find-objects-by-name/
scraped_at: 2025-09-08T15:44:45.441018
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

Find Objects by Name

Demonstrates how to find objects by their name or label.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result FindObjectsByName(Rhino.RhinoDoc doc)
      {
        const string name = "abc";
        Rhino.DocObjects.ObjectEnumeratorSettings settings = new Rhino.DocObjects.ObjectEnumeratorSettings();
        settings.NameFilter = name;
        System.Collections.Generic.List<Guid> ids = new System.Collections.Generic.List<Guid>();
        foreach (Rhino.DocObjects.RhinoObject rhObj in doc.Objects.GetObjectList(settings))
          ids.Add(rhObj.Id);
    
        if (ids.Count == 0)
        {
          Rhino.RhinoApp.WriteLine("No objects with the name " + name);
          return Rhino.Commands.Result.Failure;
        }
    
        Rhino.RhinoApp.WriteLine("Found {0} objects", ids.Count);
        foreach (Guid id in ids)
          Rhino.RhinoApp.WriteLine("  {0}", id);
    
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function FindObjectsByName(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Const name As String = "abc"
    	Dim settings As New Rhino.DocObjects.ObjectEnumeratorSettings()
    	settings.NameFilter = name
    	Dim ids As New System.Collections.Generic.List(Of Guid)()
    	For Each rhObj As Rhino.DocObjects.RhinoObject In doc.Objects.GetObjectList(settings)
    	  ids.Add(rhObj.Id)
    	Next rhObj
    
    	If ids.Count = 0 Then
    	  Rhino.RhinoApp.WriteLine("No objects with the name " & name)
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Rhino.RhinoApp.WriteLine("Found {0} objects", ids.Count)
    	For Each id As Guid In ids
    	  Rhino.RhinoApp.WriteLine("  {0}", id)
    	Next id
    
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def FindObjectsByName():
        name = "abc"
        settings = Rhino.DocObjects.ObjectEnumeratorSettings()
        settings.NameFilter = name
        ids = [rhobj.Id for rhobj in scriptcontext.doc.Objects.GetObjectList(settings)]
        if not ids:
            print "No objects with the name", name
            return Rhino.Commands.Result.Failure
        else:
            print "Found", len(ids), "objects"
            for id in ids: print "  ", id
        return Rhino.Commands.Result.Success
    
    if __name__ == "__main__":
        FindObjectsByName()
    

  

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

