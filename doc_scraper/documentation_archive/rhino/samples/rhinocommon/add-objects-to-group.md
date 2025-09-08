---
url: https://developer.rhino3d.com/samples/rhinocommon/add-objects-to-group/
scraped_at: 2025-09-08T15:44:34.366290
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

Add Objects to Group

Demonstrates how to group objects from a user-specified selection set of
objects.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddObjectsToGroup(Rhino.RhinoDoc doc)
      {
        Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
        go.SetCommandPrompt("Select objects to group");
        go.GroupSelect = true;
        go.GetMultiple(1, 0);
        if (go.CommandResult() != Rhino.Commands.Result.Success)
          return go.CommandResult();
    
        List<Guid> ids = new List<Guid>();
        for (int i = 0; i < go.ObjectCount; i++)
        {
          ids.Add(go.Object(i).ObjectId);
        }
        int index = doc.Groups.Add(ids);
        doc.Views.Redraw();
        if (index >= 0)
          return Rhino.Commands.Result.Success;
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddObjectsToGroup(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim go As New Rhino.Input.Custom.GetObject()
    	go.SetCommandPrompt("Select objects to group")
    	go.GroupSelect = True
    	go.GetMultiple(1, 0)
    	If go.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return go.CommandResult()
    	End If
    
    	Dim ids As New List(Of Guid)()
    	For i As Integer = 0 To go.ObjectCount - 1
    	  ids.Add(go.Object(i).ObjectId)
    	Next i
    	Dim index As Integer = doc.Groups.Add(ids)
    	doc.Views.Redraw()
    	If index >= 0 Then
    	  Return Rhino.Commands.Result.Success
    	End If
    	Return Rhino.Commands.Result.Failure
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def AddObjectsToGroup():
        go = Rhino.Input.Custom.GetObject()
        go.SetCommandPrompt("Select objects to group")
        go.GroupSelect = True
        go.GetMultiple(1, 0)
        if go.CommandResult()!=Rhino.Commands.Result.Success:
            return go.CommandResult()
    
        ids = [go.Object(i).ObjectId for i in range(go.ObjectCount)]
        index = scriptcontext.doc.Groups.Add(ids)
        scriptcontext.doc.Views.Redraw()
        if index>=0: return Rhino.Commands.Result.Success
        return Rhino.Commands.Result.Failure
    
    
    if __name__ == "__main__":
        AddObjectsToGroup()
    

  

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

