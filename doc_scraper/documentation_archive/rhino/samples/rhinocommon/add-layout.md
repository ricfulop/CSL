---
url: https://developer.rhino3d.com/samples/rhinocommon/add-layout/
scraped_at: 2025-09-08T15:44:23.364930
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

Add Layout

Demonstrates how to generate a layout with a single detail view that zooms to
a list of objects.

C# VB.NET Python

    
    
    partial class Examples
    {
      /// <summary>
      /// Generate a layout with a single detail view that zooms to a list of objects
      /// </summary>
      /// <param name="doc"></param>
      /// <returns></returns>
      public static Rhino.Commands.Result AddLayout(Rhino.RhinoDoc doc)
      {
        doc.PageUnitSystem = Rhino.UnitSystem.Millimeters;
        var page_views = doc.Views.GetPageViews();
        int page_number = (page_views==null) ? 1 : page_views.Length + 1;
        var pageview = doc.Views.AddPageView(string.Format("A0_{0}",page_number), 1189, 841);
        if( pageview!=null )
        {
          Rhino.Geometry.Point2d top_left = new Rhino.Geometry.Point2d(20,821);
          Rhino.Geometry.Point2d bottom_right = new Rhino.Geometry.Point2d(1169, 20);
          var detail = pageview.AddDetailView("ModelView", top_left, bottom_right, Rhino.Display.DefinedViewportProjection.Top);
          if (detail != null)
          {
            pageview.SetActiveDetail(detail.Id);
            detail.Viewport.ZoomExtents();
            detail.DetailGeometry.IsProjectionLocked = true;
            detail.DetailGeometry.SetScale(1, doc.ModelUnitSystem, 10, doc.PageUnitSystem);
            // Commit changes tells the document to replace the document's detail object
            // with the modified one that we just adjusted
            detail.CommitChanges();
          }
          pageview.SetPageAsActive();
          doc.Views.ActiveView = pageview;
          doc.Views.Redraw();
          return Rhino.Commands.Result.Success;
        }
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      ''' <summary>
      ''' Generate a layout with a single detail view that zooms to a list of objects
      ''' </summary>
      ''' <param name="doc"></param>
      ''' <returns></returns>
      Public Shared Function AddLayout(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	doc.PageUnitSystem = Rhino.UnitSystem.Millimeters
    	Dim page_views = doc.Views.GetPageViews()
    	Dim page_number As Integer = If(page_views Is Nothing, 1, page_views.Length + 1)
    	Dim pageview = doc.Views.AddPageView(String.Format("A0_{0}",page_number), 1189, 841)
    	If pageview IsNot Nothing Then
    	  Dim top_left As New Rhino.Geometry.Point2d(20,821)
    	  Dim bottom_right As New Rhino.Geometry.Point2d(1169, 20)
    	  Dim detail = pageview.AddDetailView("ModelView", top_left, bottom_right, Rhino.Display.DefinedViewportProjection.Top)
    	  If detail IsNot Nothing Then
    		pageview.SetActiveDetail(detail.Id)
    		detail.Viewport.ZoomExtents()
    		detail.DetailGeometry.IsProjectionLocked = True
    		detail.DetailGeometry.SetScale(1, doc.ModelUnitSystem, 10, doc.PageUnitSystem)
    		' Commit changes tells the document to replace the document's detail object
    		' with the modified one that we just adjusted
    		detail.CommitChanges()
    	  End If
    	  pageview.SetPageAsActive()
    	  doc.Views.ActiveView = pageview
    	  doc.Views.Redraw()
    	  Return Rhino.Commands.Result.Success
    	End If
    	Return Rhino.Commands.Result.Failure
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

