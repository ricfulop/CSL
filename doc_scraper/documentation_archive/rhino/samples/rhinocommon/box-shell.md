---
url: https://developer.rhino3d.com/samples/rhinocommon/box-shell/
scraped_at: 2025-09-08T15:45:43.667365
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

Box Shell

Demonstrates how to give thickness to (or shell) a Brep box.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result BoxShell(Rhino.RhinoDoc doc)
      {
        Rhino.Geometry.Box box;
        Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetBox(out box);
        if (rc == Rhino.Commands.Result.Success)
        {
          Rhino.Geometry.Brep brep = Rhino.Geometry.Brep.CreateFromBox(box);
          if (null != brep)
          {
            System.Collections.Generic.List<int> facesToRemove = new System.Collections.Generic.List<int>(1);
            facesToRemove.Add(0);
            Rhino.Geometry.Brep[] shells = Rhino.Geometry.Brep.CreateShell(brep, facesToRemove, 1.0, doc.ModelAbsoluteTolerance);
            if (null != shells)
            {
              for (int i = 0; i < shells.Length; i++)
                doc.Objects.AddBrep(shells[i]);
              doc.Views.Redraw();
            }
          }
        }
        return rc;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function BoxShell(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim box As Rhino.Geometry.Box = Nothing
    	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetBox(box)
    	If rc Is Rhino.Commands.Result.Success Then
    	  Dim brep As Rhino.Geometry.Brep = Rhino.Geometry.Brep.CreateFromBox(box)
    	  If Nothing IsNot brep Then
    		Dim facesToRemove As New System.Collections.Generic.List(Of Integer)(1)
    		facesToRemove.Add(0)
    		Dim shells() As Rhino.Geometry.Brep = Rhino.Geometry.Brep.CreateShell(brep, facesToRemove, 1.0, doc.ModelAbsoluteTolerance)
    		If Nothing IsNot shells Then
    		  For i As Integer = 0 To shells.Length - 1
    			doc.Objects.AddBrep(shells(i))
    		  Next i
    		  doc.Views.Redraw()
    		End If
    	  End If
    	End If
    	Return rc
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

