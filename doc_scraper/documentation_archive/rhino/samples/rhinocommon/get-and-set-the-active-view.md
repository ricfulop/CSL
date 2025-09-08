---
url: https://developer.rhino3d.com/samples/rhinocommon/get-and-set-the-active-view/
scraped_at: 2025-09-08T15:45:35.643365
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

Get and Set the Active View

Demonstrates how to determine and set the active view in Rhino.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result SetActiveView(RhinoDoc doc)
      {
        // view and view names
        var active_view_name = doc.Views.ActiveView.ActiveViewport.Name;
    
        var non_active_views =
          doc.Views
          .Where(v => v.ActiveViewport.Name != active_view_name)
          .ToDictionary(v => v.ActiveViewport.Name, v => v);
    
        // get name of view to set active
        var gs = new GetString();
        gs.SetCommandPrompt("Name of view to set active");
        gs.AcceptNothing(true);
        gs.SetDefaultString(active_view_name);
        foreach (var view_name in non_active_views.Keys)
          gs.AddOption(view_name);
        var result = gs.Get();
        if (gs.CommandResult() != Result.Success)
          return gs.CommandResult();
    
        var selected_view_name =
          result == GetResult.Option ? gs.Option().EnglishName : gs.StringResult();
    
        if (selected_view_name != active_view_name)
          if (non_active_views.ContainsKey(selected_view_name))
            doc.Views.ActiveView = non_active_views[selected_view_name];
          else
            RhinoApp.WriteLine("\"{0}\" is not a view name", selected_view_name);
    
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function SetActiveView(ByVal doc As RhinoDoc) As Result
    	' view and view names
    	Dim active_view_name = doc.Views.ActiveView.ActiveViewport.Name
    
    	Dim non_active_views = doc.Views.Where(Function(v) v.ActiveViewport.Name <> active_view_name).ToDictionary(Function(v) v.ActiveViewport.Name, Function(v) v)
    
    	' get name of view to set active
    	Dim gs = New GetString()
    	gs.SetCommandPrompt("Name of view to set active")
    	gs.AcceptNothing(True)
    	gs.SetDefaultString(active_view_name)
    	For Each view_name In non_active_views.Keys
    	  gs.AddOption(view_name)
    	Next view_name
    	Dim result = gs.Get()
    	If gs.CommandResult() <> Result.Success Then
    	  Return gs.CommandResult()
    	End If
    
    	Dim selected_view_name = If(result Is GetResult.Option, gs.Option().EnglishName, gs.StringResult())
    
    	If selected_view_name IsNot active_view_name Then
    	  If non_active_views.ContainsKey(selected_view_name) Then
    		doc.Views.ActiveView = non_active_views(selected_view_name)
    	  Else
    		RhinoApp.WriteLine("""{0}"" is not a view name", selected_view_name)
    	  End If
    	End If
    
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.Commands import *
    from Rhino.Input import *
    from Rhino.Input.Custom import *
    from scriptcontext import doc
    
    def RunCommand():
        # view and view names
        active_view_name = doc.Views.ActiveView.ActiveViewport.Name
    
        non_active_views = [(view.ActiveViewport.Name, view) for view in doc.Views if view.ActiveViewport.Name != active_view_name]
    
        # get name of view to set active
        gs = GetString()
        gs.SetCommandPrompt("Name of view to set active")
        gs.AcceptNothing(True)
        gs.SetDefaultString(active_view_name)
        for view_name, _ in non_active_views:
            gs.AddOption(view_name)
        result = gs.Get()
        if gs.CommandResult() != Result.Success:
            return gs.CommandResult()
    
        selected_view_name = "{0}".format(gs.StringResult())
        if gs.Option() != None:
            selected_view_name = gs.Option().EnglishName
    
        if selected_view_name != active_view_name:
            if selected_view_name in [seq[0] for seq in non_active_views]:
                doc.Views.ActiveView = [seq[1] for seq in non_active_views if seq[0] == selected_view_name][0]
            else:
                print "\"{0}\" is not a view name".format(selected_view_name)
    
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

