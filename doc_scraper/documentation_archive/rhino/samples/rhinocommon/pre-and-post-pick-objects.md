---
url: https://developer.rhino3d.com/samples/rhinocommon/pre-and-post-pick-objects/
scraped_at: 2025-09-08T15:44:53.346992
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

Pre and Post-Pick Objects

Demonstrates how to customize Rhino's pre and post picking of objects
behavior.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result PrePostPick(RhinoDoc doc)
      {
        var go = new Rhino.Input.Custom.GetObject();
        go.SetCommandPrompt("Select objects");
        go.EnablePreSelect(true, true);
        go.EnablePostSelect(true);
        go.GetMultiple(0, 0);
        if (go.CommandResult() != Result.Success)
          return go.CommandResult();
    
        var selected_objects = go.Objects().ToList();
    
        if (go.ObjectsWerePreselected)
        {
          go.EnablePreSelect(false, true);
          go.DeselectAllBeforePostSelect = false;
          go.EnableUnselectObjectsOnExit(false);
          go.GetMultiple(0, 0);
          if (go.CommandResult() == Result.Success)
          {
            foreach (var obj in go.Objects())
            {
              selected_objects.Add(obj);
              // The normal behavior of commands is that when they finish,
              // objects that were pre-selected remain selected and objects
              // that were post-selected will not be selected. Because we
              // potentially could have both, we'll try to do something
              // consistent and make sure post-selected objects also stay selected
              obj.Object().Select(true);
            }
          }
        }
        return selected_objects.Count > 0 ? Result.Success : Result.Nothing;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function PrePostPick(ByVal doc As RhinoDoc) As Result
    	Dim go = New Rhino.Input.Custom.GetObject()
    	go.SetCommandPrompt("Select objects")
    	go.EnablePreSelect(True, True)
    	go.EnablePostSelect(True)
    	go.GetMultiple(0, 0)
    	If go.CommandResult() <> Result.Success Then
    	  Return go.CommandResult()
    	End If
    
    	Dim selected_objects = go.Objects().ToList()
    
    	If go.ObjectsWerePreselected Then
    	  go.EnablePreSelect(False, True)
    	  go.DeselectAllBeforePostSelect = False
    	  go.EnableUnselectObjectsOnExit(False)
    	  go.GetMultiple(0, 0)
    	  If go.CommandResult() = Result.Success Then
    		For Each obj In go.Objects()
    		  selected_objects.Add(obj)
    		  ' The normal behavior of commands is that when they finish,
    		  ' objects that were pre-selected remain selected and objects
    		  ' that were post-selected will not be selected. Because we
    		  ' potentially could have both, we'll try to do something
    		  ' consistent and make sure post-selected objects also stay selected
    		  obj.Object().Select(True)
    		Next obj
    	  End If
    	End If
    	Return If(selected_objects.Count > 0, Result.Success, Result.Nothing)
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.Commands import *
    from Rhino.Input.Custom import *
    
    def RunCommand():
        go = GetObject()
        go.SetCommandPrompt("Select objects")
        go.EnablePreSelect(True, True)
        go.EnablePostSelect(True)
        go.GetMultiple(0, 0)
        if go.CommandResult() != Result.Success:
            return go.CommandResult()
    
        selected_objects = []
        for obj in go.Objects():
            selected_objects.Add(obj)
    
        if go.ObjectsWerePreselected:
            go.EnablePreSelect(False, True)
            go.DeselectAllBeforePostSelect = False
            go.EnableUnselectObjectsOnExit(False)
            go.GetMultiple(0, 0)
            if go.CommandResult() == Result.Success:
                for obj in go.Objects():
                    selected_objects.Add(obj)
                    # The normal behavior of commands is that when they finish,
                    # objects that were pre-selected remain selected and objects
                    # that were post-selected will not be selected. Because we
                    # potentially could have both, we'll try to do something
                    # consistent and make sure post-selected objects also stay selected
                    obj.Object().Select(True)
        return Result.Success if selected_objects.Count > 0 else Result.Nothing
    
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

