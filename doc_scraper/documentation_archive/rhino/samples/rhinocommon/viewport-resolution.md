---
url: https://developer.rhino3d.com/samples/rhinocommon/viewport-resolution/
scraped_at: 2025-09-08T15:45:37.696986
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

Viewport Resolution

Print Active Viewport Resolution

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ViewportResolution(RhinoDoc doc)
      {
        var active_viewport = doc.Views.ActiveView.ActiveViewport;
        RhinoApp.WriteLine("Name = {0}: Width = {1}, Height = {2}",
          active_viewport.Name, active_viewport.Size.Width, active_viewport.Size.Height);
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ViewportResolution(ByVal doc As RhinoDoc) As Result
    	Dim active_viewport = doc.Views.ActiveView.ActiveViewport
    	RhinoApp.WriteLine("Name = {0}: Width = {1}, Height = {2}", active_viewport.Name, active_viewport.Size.Width, active_viewport.Size.Height)
    	Return Result.Success
      End Function
    End Class
    
    
    
    from scriptcontext import doc
    
    activeViewport = doc.Views.ActiveView.ActiveViewport
    print "Name = {0}: Width = {1}, Height = {2}".format(
        activeViewport.Name, activeViewport.Size.Width, activeViewport.Size.Height)
    

  

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

