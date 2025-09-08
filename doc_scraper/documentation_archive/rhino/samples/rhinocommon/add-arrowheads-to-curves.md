---
url: https://developer.rhino3d.com/samples/rhinocommon/add-arrowheads-to-curves/
scraped_at: 2025-09-08T15:44:13.341025
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

Add Arrowheads to Curves

Demonstrates how to decorate curves in a Rhino model with arrowheads.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result ObjectDecoration(Rhino.RhinoDoc doc)
      {
        // Define a line
        var line = new Rhino.Geometry.Line(new Rhino.Geometry.Point3d(0, 0, 0), new Rhino.Geometry.Point3d(10, 0, 0));
    
        // Make a copy of Rhino's default object attributes
        var attribs = doc.CreateDefaultAttributes();
    
        // Modify the object decoration style
        attribs.ObjectDecoration = Rhino.DocObjects.ObjectDecoration.BothArrowhead;
    
        // Create a new curve object with our attributes
        doc.Objects.AddLine(line, attribs);
        doc.Views.Redraw();
    
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ObjectDecoration(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	' Define a line
    	Dim line = New Rhino.Geometry.Line(New Rhino.Geometry.Point3d(0, 0, 0), New Rhino.Geometry.Point3d(10, 0, 0))
    
    	' Make a copy of Rhino's default object attributes
    	Dim attribs = doc.CreateDefaultAttributes()
    
    	' Modify the object decoration style
    	attribs.ObjectDecoration = Rhino.DocObjects.ObjectDecoration.BothArrowhead
    
    	' Create a new curve object with our attributes
    	doc.Objects.AddLine(line, attribs)
    	doc.Views.Redraw()
    
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def ObjectDecoration():
        # Define a line
        line = Rhino.Geometry.Line(Rhino.Geometry.Point3d(0, 0, 0), Rhino.Geometry.Point3d(10, 0, 0))
    
        # Make a copy of Rhino's default object attributes
        attribs = scriptcontext.doc.CreateDefaultAttributes()
    
        # Modify the object decoration style
        attribs.ObjectDecoration = Rhino.DocObjects.ObjectDecoration.BothArrowhead
    
        # Create a new curve object with our attributes
        scriptcontext.doc.Objects.AddLine(line, attribs)
        scriptcontext.doc.Views.Redraw()
    
    if __name__ == "__main__":
        ObjectDecoration()
    

  

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

