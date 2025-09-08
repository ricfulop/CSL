---
url: https://developer.rhino3d.com/samples/rhinocommon/determine-active-viewport/
scraped_at: 2025-09-08T15:45:34.661333
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

Determine Active Viewport

Demonstrates how to determine the active viewport name, even in a layout or a
detail view.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result ActiveViewport(Rhino.RhinoDoc doc)
      {
        Rhino.Display.RhinoView view = doc.Views.ActiveView;
        if (view == null)
          return Rhino.Commands.Result.Failure;
    
        Rhino.Display.RhinoPageView pageview = view as Rhino.Display.RhinoPageView;
        if (pageview != null)
        {
          string layout_name = pageview.PageName;
          if (pageview.PageIsActive)
          {
            Rhino.RhinoApp.WriteLine("The layout {0} is active", layout_name);
          }
          else
          {
            string detail_name = pageview.ActiveViewport.Name;
            Rhino.RhinoApp.WriteLine("The detail {0} on layout {1} is active", detail_name, layout_name);
          }
        }
        else
        {
          string viewport_name = view.MainViewport.Name;
          Rhino.RhinoApp.WriteLine("The viewport {0} is active", viewport_name);
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ActiveViewport(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim view As Rhino.Display.RhinoView = doc.Views.ActiveView
    	If view Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim pageview As Rhino.Display.RhinoPageView = TryCast(view, Rhino.Display.RhinoPageView)
    	If pageview IsNot Nothing Then
    	  Dim layout_name As String = pageview.PageName
    	  If pageview.PageIsActive Then
    		Rhino.RhinoApp.WriteLine("The layout {0} is active", layout_name)
    	  Else
    		Dim detail_name As String = pageview.ActiveViewport.Name
    		Rhino.RhinoApp.WriteLine("The detail {0} on layout {1} is active", detail_name, layout_name)
    	  End If
    	Else
    	  Dim viewport_name As String = view.MainViewport.Name
    	  Rhino.RhinoApp.WriteLine("The viewport {0} is active", viewport_name)
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def ActiveViewport():
        view = scriptcontext.doc.Views.ActiveView
        if view is None: return
        if isinstance(view, Rhino.Display.RhinoPageView):
            if view.PageIsActive:
                print "The layout", view.PageName, "is active"
            else:
                detail_name = view.ActiveViewport.Name
                print "The detail", detail_name, "on layout", view.PageName, "is active"
        else:
            print "The viewport", view.MainViewport.Name, "is active"
    
    
    if __name__ == "__main__":
        ActiveViewport()
    

  

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

