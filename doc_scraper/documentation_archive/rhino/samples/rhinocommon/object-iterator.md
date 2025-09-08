---
url: https://developer.rhino3d.com/samples/rhinocommon/object-iterator/
scraped_at: 2025-09-08T15:46:28.855011
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

Object Iterator

Demonstrates how to iterate (or enumerate) through Rhino's geometry table.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ObjectIterator(RhinoDoc doc)
      {
        var object_enumerator_settings = new ObjectEnumeratorSettings();
        object_enumerator_settings.IncludeLights = true;
        object_enumerator_settings.IncludeGrips = false;
        var rhino_objects = doc.Objects.GetObjectList(object_enumerator_settings);
    
        int count = 0;
        foreach (var rhino_object in rhino_objects)
        {
          if (rhino_object.IsSelectable() && rhino_object.IsSelected(false) == 0)
          {
            rhino_object.Select(true);
            count++;
          }
        }
        if (count > 0)
        {
          doc.Views.Redraw();
          RhinoApp.WriteLine("{0} object{1} selected", count,
            count == 1 ? "" : "s");
        }
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ObjectIterator(ByVal doc As RhinoDoc) As Result
    	Dim object_enumerator_settings = New ObjectEnumeratorSettings()
    	object_enumerator_settings.IncludeLights = True
    	object_enumerator_settings.IncludeGrips = False
    	Dim rhino_objects = doc.Objects.GetObjectList(object_enumerator_settings)
    
    	Dim count As Integer = 0
    	For Each rhino_object In rhino_objects
    	  If rhino_object.IsSelectable() AndAlso rhino_object.IsSelected(False) = 0 Then
    		rhino_object.Select(True)
    		count += 1
    	  End If
    	Next rhino_object
    	If count > 0 Then
    	  doc.Views.Redraw()
    	  RhinoApp.WriteLine("{0} object{1} selected", count,If(count = 1, "", "s"))
    	End If
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Commands import *
    from scriptcontext import doc
    
    def RunCommand():
        object_enumerator_settings = ObjectEnumeratorSettings()
        object_enumerator_settings.IncludeLights = True
        object_enumerator_settings.IncludeGrips = False
        rhino_objects = doc.Objects.GetObjectList(object_enumerator_settings)
    
        count = 0
        for rhino_object in rhino_objects:
            if rhino_object.IsSelectable() and rhino_object.IsSelected(False) == 0:
                rhino_object.Select(True)
                count += 1;
    
        if count > 0:
            doc.Views.Redraw()
            RhinoApp.WriteLine("{0} object{1} selected", count, "" if count == 1 else "s")
    
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

