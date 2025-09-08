---
url: https://developer.rhino3d.com/samples/rhinocommon/add-nested-block/
scraped_at: 2025-09-08T15:44:31.369021
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

Add Nested Block

Demonstrates how to add a nested block to an instance definition.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddNestedBlock(RhinoDoc doc)
      {
        var circle = new Circle(Point3d.Origin, 5);
        Curve[] curveList = { new ArcCurve(circle) };
        var circleIndex = doc.InstanceDefinitions.Add("Circle", "Circle with radius of 5", Point3d.Origin, curveList);
        var transform = Transform.Identity;
        var irefId = doc.InstanceDefinitions[circleIndex].Id;
        var iref = new InstanceReferenceGeometry(irefId, transform);
        circle.Radius = circle.Radius * 2.0;
        GeometryBase[] blockList = { iref, new ArcCurve(circle) };
        var circle2Index = doc.InstanceDefinitions.Add("TwoCircles", "Nested block test", Point3d.Origin, blockList);
        doc.Objects.AddInstanceObject(circle2Index, transform);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddNestedBlock(ByVal doc As RhinoDoc) As Rhino.Commands.Result
    	Dim circle = New Circle(Point3d.Origin, 5)
    	Dim curveList() As Curve = { New ArcCurve(circle) }
    	Dim circleIndex = doc.InstanceDefinitions.Add("Circle", "Circle with radius of 5", Point3d.Origin, curveList)
    	Dim transform = Transform.Identity
    	Dim irefId = doc.InstanceDefinitions(circleIndex).Id
    	Dim iref = New InstanceReferenceGeometry(irefId, transform)
    	circle.Radius = circle.Radius * 2.0
    	Dim blockList() As GeometryBase = { iref, New ArcCurve(circle) }
    	Dim circle2Index = doc.InstanceDefinitions.Add("TwoCircles", "Nested block test", Point3d.Origin, blockList)
    	doc.Objects.AddInstanceObject(circle2Index, transform)
    	doc.Views.Redraw()
    	Return Rhino.Commands.Result.Success
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

