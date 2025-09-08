---
url: https://developer.rhino3d.com/samples/rhinocommon/set-viewport-name/
scraped_at: 2025-09-08T15:45:36.653941
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

Set Viewport Name

Demonstrates how to set a viewport's name or title.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result SetViewName(RhinoDoc doc)
      {
        var view = doc.Views.ActiveView;
        if (view == null)
          return Result.Failure;
    
        view.MainViewport.Name = "Facade";
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function SetViewName(ByVal doc As RhinoDoc) As Result
    	Dim view = doc.Views.ActiveView
    	If view Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	view.MainViewport.Name = "Facade"
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino.Commands import *
    import rhinoscriptsyntax as rs
    from scriptcontext import doc
    
    def RunCommand():
        view = doc.Views.ActiveView
        if view == None:
            return Result.Failure
    
        view.MainViewport.Name = "Facade"
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

