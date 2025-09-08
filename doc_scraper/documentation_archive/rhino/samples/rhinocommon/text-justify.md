---
url: https://developer.rhino3d.com/samples/rhinocommon/text-justify/
scraped_at: 2025-09-08T15:46:43.936989
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

Text Justify

Demonstrates how to set text justification with a specific font.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result TextJustify(RhinoDoc doc)
      {
        var text_entity = new TextEntity
        {
          Plane = Plane.WorldXY,
          Text = "Hello Rhino!",
          Justification = TextJustification.MiddleCenter,
          FontIndex = doc.Fonts.FindOrCreate("Arial", false, false)
        };
    
        doc.Objects.AddText(text_entity);
        doc.Views.Redraw();
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function TextJustify(ByVal doc As RhinoDoc) As Result
    	Dim text_entity = New TextEntity With {.Plane = Plane.WorldXY, .Text = "Hello Rhino!", .Justification = TextJustification.MiddleCenter, .FontIndex = doc.Fonts.FindOrCreate("Arial", False, False)}
    
    	doc.Objects.AddText(text_entity)
    	doc.Views.Redraw()
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    from scriptcontext import doc
    from Rhino.Geometry import *
    
    text_entity = TextEntity()
    text_entity.Plane = Plane.WorldXY
    text_entity.Text = "Hello Rhino!"
    text_entity.Justification = TextJustification.MiddleCenter
    text_entity.FontIndex = doc.Fonts.FindOrCreate("Arial", False, False)
    
    doc.Objects.AddText(text_entity)
    doc.Views.Redraw()
    

  

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

