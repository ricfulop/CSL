---
url: https://developer.rhino3d.com/samples/rhinocommon/add-cone/
scraped_at: 2025-09-08T15:44:20.321016
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

Add Cone

Demonstrates how to construct a cone using a plane, height, and radius.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddCone(Rhino.RhinoDoc doc)
      {
        Rhino.Geometry.Plane plane = Rhino.Geometry.Plane.WorldXY;
        const double height = 10;
        const double radius = 5;
        Rhino.Geometry.Cone cone = new Rhino.Geometry.Cone(plane, height, radius);
        if (cone.IsValid)
        {
          const bool cap_bottom = true;
          Rhino.Geometry.Brep cone_brep = cone.ToBrep(cap_bottom);
          if (cone_brep!=null)
          {
            doc.Objects.AddBrep(cone_brep);
            doc.Views.Redraw();
          }
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddCone(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim plane As Rhino.Geometry.Plane = Rhino.Geometry.Plane.WorldXY
    	Const height As Double = 10
    	Const radius As Double = 5
    	Dim cone As New Rhino.Geometry.Cone(plane, height, radius)
    	If cone.IsValid Then
    	  Const cap_bottom As Boolean = True
    	  Dim cone_brep As Rhino.Geometry.Brep = cone.ToBrep(cap_bottom)
    	  If cone_brep IsNot Nothing Then
    		doc.Objects.AddBrep(cone_brep)
    		doc.Views.Redraw()
    	  End If
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def AddCone():
        plane = Rhino.Geometry.Plane.WorldXY
        height = 10
        radius = 5
        cone = Rhino.Geometry.Cone(plane, height, radius)
        if cone.IsValid:
            cap_bottom = True
            cone_brep = cone.ToBrep(cap_bottom)
            if cone_brep:
                scriptcontext.doc.Objects.AddBrep(cone_brep)
                scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        AddCone()
    

  

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

