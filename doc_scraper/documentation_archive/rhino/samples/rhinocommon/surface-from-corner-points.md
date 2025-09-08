---
url: https://developer.rhino3d.com/samples/rhinocommon/surface-from-corner-points/
scraped_at: 2025-09-08T15:46:41.902703
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

Surface from Corner Points

Demonstrates how to create a surface from a set of corner points.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result SurfaceFromCorners(RhinoDoc doc)
      {
        var surface = NurbsSurface.CreateFromCorners(
          new Point3d(5, 0, 0),
          new Point3d(5, 5, 5),
          new Point3d(0, 5, 0),
          new Point3d(0, 0, 0));
    
        doc.Objects.AddSurface(surface);
        doc.Views.Redraw();
    
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function SurfaceFromCorners(ByVal doc As RhinoDoc) As Result
    	Dim surface = NurbsSurface.CreateFromCorners(New Point3d(5, 0, 0), New Point3d(5, 5, 5), New Point3d(0, 5, 0), New Point3d(0, 0, 0))
    
    	doc.Objects.AddSurface(surface)
    	doc.Views.Redraw()
    
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    from Rhino.Geometry import NurbsSurface, Point3d
    from scriptcontext import doc
    
    surface = NurbsSurface.CreateFromCorners(
        Point3d(5, 0, 0),
        Point3d(5, 5, 5),
        Point3d(0, 5, 0),
        Point3d(0, 0, 0));
    
    doc.Objects.AddSurface(surface);
    doc.Views.Redraw();
    

  

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

