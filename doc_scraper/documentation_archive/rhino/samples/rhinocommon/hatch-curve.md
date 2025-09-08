---
url: https://developer.rhino3d.com/samples/rhinocommon/hatch-curve/
scraped_at: 2025-09-08T15:45:17.723745
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

Hatch Curve

Demonstrates how to create a hatch from a curve.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result HatchCurve(Rhino.RhinoDoc doc)
      {
        var go = new Rhino.Input.Custom.GetObject();
        go.SetCommandPrompt("Select closed planar curve");
        go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
        go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve;
        go.SubObjectSelect = false;
        go.Get();
        if( go.CommandResult() != Rhino.Commands.Result.Success )
          return go.CommandResult();
    
        var curve = go.Object(0).Curve();
        if( curve==null || !curve.IsClosed || !curve.IsPlanar() )
          return Rhino.Commands.Result.Failure;
    
        string hatch_name = doc.HatchPatterns[doc.HatchPatterns.CurrentHatchPatternIndex].Name;
        var rc = Rhino.Input.RhinoGet.GetString("Hatch pattern", true, ref hatch_name);
        if( rc!= Rhino.Commands.Result.Success )
          return rc;
        hatch_name = hatch_name.Trim();
        if( string.IsNullOrWhiteSpace(hatch_name) )
          return Rhino.Commands.Result.Nothing;
        int index = doc.HatchPatterns.Find(hatch_name, true);
        if( index < 0 )
        {
          Rhino.RhinoApp.WriteLine("Hatch pattern does not exist.");
          return Rhino.Commands.Result.Nothing;
        }
    
        var hatches = Rhino.Geometry.Hatch.Create( curve, index, 0, 1);
        for( int i=0; i<hatches.Length; i++ )
          doc.Objects.AddHatch(hatches[i]);
        if( hatches.Length>0 )
          doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function HatchCurve(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim go = New Rhino.Input.Custom.GetObject()
    	go.SetCommandPrompt("Select closed planar curve")
    	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    	go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve
    	go.SubObjectSelect = False
    	go.Get()
    	If go.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return go.CommandResult()
    	End If
    
    	Dim curve = go.Object(0).Curve()
    	If curve Is Nothing OrElse Not curve.IsClosed OrElse Not curve.IsPlanar() Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim hatch_name As String = doc.HatchPatterns(doc.HatchPatterns.CurrentHatchPatternIndex).Name
    	Dim rc = Rhino.Input.RhinoGet.GetString("Hatch pattern", True, hatch_name)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    	hatch_name = hatch_name.Trim()
    	If String.IsNullOrWhiteSpace(hatch_name) Then
    	  Return Rhino.Commands.Result.Nothing
    	End If
    	Dim index As Integer = doc.HatchPatterns.Find(hatch_name, True)
    	If index < 0 Then
    	  Rhino.RhinoApp.WriteLine("Hatch pattern does not exist.")
    	  Return Rhino.Commands.Result.Nothing
    	End If
    
    	Dim hatches = Rhino.Geometry.Hatch.Create(curve, index, 0, 1)
    	For i As Integer = 0 To hatches.Length - 1
    	  doc.Objects.AddHatch(hatches(i))
    	Next i
    	If hatches.Length>0 Then
    	  doc.Views.Redraw()
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def HatchCurve():
        go = Rhino.Input.Custom.GetObject()
        go.SetCommandPrompt("Select closed planar curve")
        go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
        go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve
        go.SubObjectSelect = False
        go.Get()
        if go.CommandResult()!=Rhino.Commands.Result.Success: return
    
        curve = go.Object(0).Curve()
        if (not curve or not curve.IsClosed or not curve.IsPlanar()): return
    
        hatch_name = scriptcontext.doc.HatchPatterns[scriptcontext.doc.HatchPatterns.CurrentHatchPatternIndex].Name
        rc, hatch_name = Rhino.Input.RhinoGet.GetString("Hatch pattern", True, hatch_name)
        if rc!=Rhino.Commands.Result.Success or not hatch_name: return
    
        index = scriptcontext.doc.HatchPatterns.Find(hatch_name, True)
        if index<0:
            print "Hatch pattern does not exist."
            return
    
        hatches = Rhino.Geometry.Hatch.Create(curve, index, 0, 1)
        for hatch in hatches:
            scriptcontext.doc.Objects.AddHatch(hatch)
        if hatches: scriptcontext.doc.Views.Redraw()
    
    if __name__=="__main__":
        HatchCurve()
    

  

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

