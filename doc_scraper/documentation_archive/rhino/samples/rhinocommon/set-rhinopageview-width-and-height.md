---
url: https://developer.rhino3d.com/samples/rhinocommon/set-rhinopageview-width-and-height/
scraped_at: 2025-09-08T15:46:35.895891
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

Set RhinoPageView Width and Height

Demonstrates how to set the RhinoPageView width and height dimensions.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result SetRhinoPageViewWidthAndHeight(RhinoDoc doc)
      {
        var width = 1189;
        var height = 841;
        var page_views = doc.Views.GetPageViews();
        int page_number = (page_views==null) ? 1 : page_views.Length + 1;
        var pageview = doc.Views.AddPageView(string.Format("A0_{0}",page_number), width, height);
    
        int new_width = width;
        var rc = RhinoGet.GetInteger("new width", false, ref new_width);
        if (rc != Result.Success || new_width <= 0) return rc;
    
        int new_height = height;
        rc = RhinoGet.GetInteger("new height", false, ref new_height);
        if (rc != Result.Success || new_height <= 0) return rc;
    
        pageview.PageWidth = new_width;
        pageview.PageHeight = new_height;
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function SetRhinoPageViewWidthAndHeight(ByVal doc As RhinoDoc) As Result
    	Dim width = 1189
    	Dim height = 841
    	Dim page_views = doc.Views.GetPageViews()
    	Dim page_number As Integer = If(page_views Is Nothing, 1, page_views.Length + 1)
    	Dim pageview = doc.Views.AddPageView(String.Format("A0_{0}",page_number), width, height)
    
    	Dim new_width As Integer = width
    	Dim rc = RhinoGet.GetInteger("new width", False, new_width)
    	If rc IsNot Result.Success OrElse new_width <= 0 Then
    		Return rc
    	End If
    
    	Dim new_height As Integer = height
    	rc = RhinoGet.GetInteger("new height", False, new_height)
    	If rc IsNot Result.Success OrElse new_height <= 0 Then
    		Return rc
    	End If
    
    	pageview.PageWidth = new_width
    	pageview.PageHeight = new_height
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    # No Python sample available
    

  

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

