---
url: https://developer.rhino3d.com/samples/rhinocommon/add-annotation-text/
scraped_at: 2025-09-08T15:44:12.290289
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

Add Annotation Text

Demonstrates how to add annotation text to a Rhino model at a specific
location.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddAnnotationText(Rhino.RhinoDoc doc)
      {
        Rhino.Geometry.Point3d pt = new Rhino.Geometry.Point3d(10, 0, 0);
        const string text = "Hello RhinoCommon";
        const double height = 2.0;
        const string font = "Arial";
        Rhino.Geometry.Plane plane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane();
        plane.Origin = pt;
        Guid id = doc.Objects.AddText(text, plane, height, font, false, false);
        if( id != Guid.Empty )
        {
          doc.Views.Redraw();
          return Rhino.Commands.Result.Success;
        }
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddAnnotationText(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim pt As New Rhino.Geometry.Point3d(10, 0, 0)
    	Const text As String = "Hello RhinoCommon"
    	Const height As Double = 2.0
    	Const font As String = "Arial"
    	Dim plane As Rhino.Geometry.Plane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane()
    	plane.Origin = pt
    	Dim id As Guid = doc.Objects.AddText(text, plane, height, font, False, False)
    	If id <> Guid.Empty Then
    	  doc.Views.Redraw()
    	  Return Rhino.Commands.Result.Success
    	End If
    	Return Rhino.Commands.Result.Failure
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddAnnotationText():
        pt = Rhino.Geometry.Point3d(10, 0, 0)
        text = "Hello RhinoCommon"
        height = 2.0
        font = "Arial"
        plane = scriptcontext.doc.Views.ActiveView.ActiveViewport.ConstructionPlane()
        plane.Origin = pt
        id = scriptcontext.doc.Objects.AddText(text, plane, height, font, False, False)
        if id!=System.Guid.Empty:
            scriptcontext.doc.Views.Redraw()
            return Rhino.Commands.Result.Success
        return Rhino.Commands.Result.Failure
    
    
    if __name__=="__main__":
        AddAnnotationText()
    

  

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

