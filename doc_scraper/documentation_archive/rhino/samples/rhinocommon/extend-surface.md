---
url: https://developer.rhino3d.com/samples/rhinocommon/extend-surface/
scraped_at: 2025-09-08T15:46:08.779619
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

Extend Surface

Demonstrates how to extend a user-specified edge of a surface.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ExtendSurface(RhinoDoc doc)
      {
        var go = new Rhino.Input.Custom.GetObject();
        go.SetCommandPrompt("Select edge of surface to extend");
        go.GeometryFilter = ObjectType.EdgeFilter;
        go.GeometryAttributeFilter = GeometryAttributeFilter.EdgeCurve;
        go.Get();
        if (go.CommandResult() != Result.Success)
          return go.CommandResult();
        var obj_ref = go.Object(0);
    
        var surface = obj_ref.Surface();
        if (surface == null)
        {
          RhinoApp.WriteLine("Unable to extend polysurfaces.");
          return Result.Failure;
        }
    
        var brep = obj_ref.Brep();
        var face = obj_ref.Face();
        if (brep == null || face == null)
          return Result.Failure;
        if (face.FaceIndex < 0)
          return Result.Failure;
    
        if( !brep.IsSurface)
        {
          RhinoApp.WriteLine("Unable to extend trimmed surfaces.");
          return Result.Nothing;
        }
    
        var curve = obj_ref.Curve();
    
        var trim = obj_ref.Trim();
        if (trim == null)
          return Result.Failure;
    
        if (trim.TrimType == BrepTrimType.Seam)
        {
          RhinoApp.WriteLine("Unable to extend surface at seam.");
          return Result.Nothing;
        }
    
        var extended_surface = surface.Extend(trim.IsoStatus, 5.0, true);
        if (extended_surface != null)
        {
          var mybrep = Brep.CreateFromSurface(extended_surface);
          doc.Objects.Replace(obj_ref.ObjectId, mybrep);
          doc.Views.Redraw();
        }
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ExtendSurface(ByVal doc As RhinoDoc) As Result
    	Dim go = New Rhino.Input.Custom.GetObject()
    	go.SetCommandPrompt("Select edge of surface to extend")
    	go.GeometryFilter = ObjectType.EdgeFilter
    	go.GeometryAttributeFilter = GeometryAttributeFilter.EdgeCurve
    	go.Get()
    	If go.CommandResult() <> Result.Success Then
    	  Return go.CommandResult()
    	End If
    	Dim obj_ref = go.Object(0)
    
    	Dim surface = obj_ref.Surface()
    	If surface Is Nothing Then
    	  RhinoApp.WriteLine("Unable to extend polysurfaces.")
    	  Return Result.Failure
    	End If
    
    	Dim brep = obj_ref.Brep()
    	Dim face = obj_ref.Face()
    	If brep Is Nothing OrElse face Is Nothing Then
    	  Return Result.Failure
    	End If
    	If face.FaceIndex < 0 Then
    	  Return Result.Failure
    	End If
    
    	If Not brep.IsSurface Then
    	  RhinoApp.WriteLine("Unable to extend trimmed surfaces.")
    	  Return Result.Nothing
    	End If
    
    	Dim curve = obj_ref.Curve()
    
    	Dim trim = obj_ref.Trim()
    	If trim Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	If trim.TrimType = BrepTrimType.Seam Then
    	  RhinoApp.WriteLine("Unable to extend surface at seam.")
    	  Return Result.Nothing
    	End If
    
    	Dim extended_surface = surface.Extend(trim.IsoStatus, 5.0, True)
    	If extended_surface IsNot Nothing Then
    	  Dim mybrep = Brep.CreateFromSurface(extended_surface)
    	  doc.Objects.Replace(obj_ref.ObjectId, mybrep)
    	  doc.Views.Redraw()
    	End If
    	Return Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    from Rhino.Input.Custom import *
    from Rhino.DocObjects import *
    from Rhino.Commands import *
    from Rhino.Geometry import *
    from scriptcontext import doc
    
    def RunCommand():
        go = Rhino.Input.Custom.GetObject()
        go.SetCommandPrompt("Select edge of surface to extend")
        go.GeometryFilter = ObjectType.EdgeFilter
        go.GeometryAttributeFilter = GeometryAttributeFilter.EdgeCurve
        go.Get()
        if go.CommandResult() != Result.Success:
            return go.CommandResult()
        obj_ref = go.Object(0)
    
        surface = obj_ref.Surface()
        if surface == None:
            print "Unable to extend polysurfaces."
            return Result.Failure
    
        brep = obj_ref.Brep()
        face = obj_ref.Face()
        if brep == None or face == None:
            return Result.Failure
        if face.FaceIndex < 0:
            return Result.Failure
    
        if not brep.IsSurface:
            print "Unable to extend trimmed surfaces."
            return Result.Nothing
    
        curve = obj_ref.Curve()
    
        trim = obj_ref.Trim()
        if trim == None:
            return Result.Failure
    
        if trim.TrimType == BrepTrimType.Seam:
            print "Unable to extend surface at seam."
            return Result.Nothing
    
        extended_surface = surface.Extend(trim.IsoStatus, 5.0, True)
        if extended_surface != None:
            mybrep = Brep.CreateFromSurface(extended_surface)
            doc.Objects.Replace(obj_ref.ObjectId, mybrep)
            doc.Views.Redraw()
        return Result.Success
    
    if __name__ == "__main__":
        RunCommand()
    

  

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

