---
url: https://developer.rhino3d.com/samples/rhinocommon/export-control-points/
scraped_at: 2025-09-08T15:46:07.711993
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

Export Control Points

Demonstrates how to export the control points of a user-selected curve and
write them to a file.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result ExportControlPoints(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef objref;
        var get_rc = Rhino.Input.RhinoGet.GetOneObject("Select curve", false, Rhino.DocObjects.ObjectType.Curve, out objref);
        if (get_rc != Rhino.Commands.Result.Success)
          return get_rc;
        var curve = objref.Curve();
        if (curve == null)
          return Rhino.Commands.Result.Failure;
        var nc = curve.ToNurbsCurve();
    
        var fd = new SaveFileDialog();
        //fd.Filters = "Text Files | *.txt";
        //fd.Filter = "Text Files | *.txt";
        //fd.DefaultExt = "txt";
        //if( fd.ShowDialog(Rhino.RhinoApp.MainWindow())!= System.Windows.Forms.DialogResult.OK)
        if (fd.ShowDialog(null) != DialogResult.Ok)
          return Rhino.Commands.Result.Cancel;
        string path = fd.FileName;
        using( System.IO.StreamWriter sw = new System.IO.StreamWriter(path) )
        {
          foreach( var pt in nc.Points )
          {
            var loc = pt.Location;
            sw.WriteLine("{0} {1} {2}", loc.X, loc.Y, loc.Z);
          }
          sw.Close();
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ExportControlPoints(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim get_rc = Rhino.Input.RhinoGet.GetOneObject("Select curve", False, Rhino.DocObjects.ObjectType.Curve, objref)
    	If get_rc IsNot Rhino.Commands.Result.Success Then
    	  Return get_rc
    	End If
    	Dim curve = objref.Curve()
    	If curve Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    	Dim nc = curve.ToNurbsCurve()
    
    	Dim fd = New SaveFileDialog()
    	'fd.Filters = "Text Files | *.txt";
    	'fd.Filter = "Text Files | *.txt";
    	'fd.DefaultExt = "txt";
    	'if( fd.ShowDialog(Rhino.RhinoApp.MainWindow())!= System.Windows.Forms.DialogResult.OK)
    	If fd.ShowDialog(Nothing) <> DialogResult.Ok Then
    	  Return Rhino.Commands.Result.Cancel
    	End If
    	Dim path As String = fd.FileName
    	Using sw As New System.IO.StreamWriter(path)
    	  For Each pt In nc.Points
    		Dim loc = pt.Location
    		sw.WriteLine("{0} {1} {2}", loc.X, loc.Y, loc.Z)
    	  Next pt
    	  sw.Close()
    	End Using
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

