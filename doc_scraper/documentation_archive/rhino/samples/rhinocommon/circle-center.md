---
url: https://developer.rhino3d.com/samples/rhinocommon/circle-center/
scraped_at: 2025-09-08T15:45:46.569863
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

Circle Center

Demonstrates how to find the center of a circle.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result CircleCenter(Rhino.RhinoDoc doc)
      {
        Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
        go.SetCommandPrompt("Select objects");
        go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
        go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve;
        go.GetMultiple(1, 0);
        if( go.CommandResult() != Rhino.Commands.Result.Success )
          return go.CommandResult();
    
        Rhino.DocObjects.ObjRef[] objrefs = go.Objects();
        if( objrefs==null )
          return Rhino.Commands.Result.Nothing;
    
        double tolerance = doc.ModelAbsoluteTolerance;
        for( int i=0; i<objrefs.Length; i++ )
        {
          // get the curve geometry
          Rhino.Geometry.Curve curve = objrefs[i].Curve();
          if( curve==null )
            continue;
          Rhino.Geometry.Circle circle;
          if( curve.TryGetCircle(out circle, tolerance) )
          {
            Rhino.RhinoApp.WriteLine("Circle{0}: center = {1}", i+1, circle.Center);
          }
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function CircleCenter(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim go As New Rhino.Input.Custom.GetObject()
    	go.SetCommandPrompt("Select objects")
    	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    	go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve
    	go.GetMultiple(1, 0)
    	If go.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return go.CommandResult()
    	End If
    
    	Dim objrefs() As Rhino.DocObjects.ObjRef = go.Objects()
    	If objrefs Is Nothing Then
    	  Return Rhino.Commands.Result.Nothing
    	End If
    
    	Dim tolerance As Double = doc.ModelAbsoluteTolerance
    	For i As Integer = 0 To objrefs.Length - 1
    	  ' get the curve geometry
    	  Dim curve As Rhino.Geometry.Curve = objrefs(i).Curve()
    	  If curve Is Nothing Then
    		Continue For
    	  End If
    	  Dim circle As Rhino.Geometry.Circle = Nothing
    	  If curve.TryGetCircle(circle, tolerance) Then
    		Rhino.RhinoApp.WriteLine("Circle{0}: center = {1}", i+1, circle.Center)
    	  End If
    	Next i
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def CircleCenter():
        go = Rhino.Input.Custom.GetObject()
        go.SetCommandPrompt("Select objects")
        go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
        go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve
        go.GetMultiple(1, 0)
        if go.CommandResult()!=Rhino.Commands.Result.Success:
            return go.CommandResult()
    
        objrefs = go.Objects()
        if not objrefs: return Rhino.Commands.Result.Nothing
    
        tolerance = scriptcontext.doc.ModelAbsoluteTolerance
        for i, objref in enumerate(objrefs):
            # get the curve geometry
            curve = objref.Curve()
            if not curve: continue
            rc, circle = curve.TryGetCircle( tolerance )
            if rc:
                print "Circle", i+1, ": center = ", circle.Center
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        CircleCenter()
    

  

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

