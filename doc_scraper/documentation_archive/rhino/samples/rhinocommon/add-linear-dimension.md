---
url: https://developer.rhino3d.com/samples/rhinocommon/add-linear-dimension/
scraped_at: 2025-09-08T15:44:25.366643
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

Add Linear Dimension

Demonstrates how to add a linear dimension to a Rhino model.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddLinearDimension(Rhino.RhinoDoc doc)
      {
        Rhino.Geometry.LinearDimension dimension;
        Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetLinearDimension(out dimension);
        if (rc == Rhino.Commands.Result.Success && dimension != null)
        {
          if (doc.Objects.AddLinearDimension(dimension) == Guid.Empty)
            rc = Rhino.Commands.Result.Failure;
          else
            doc.Views.Redraw();
        }
        return rc;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddLinearDimension(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim dimension As Rhino.Geometry.LinearDimension = Nothing
    	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetLinearDimension(dimension)
    	If rc Is Rhino.Commands.Result.Success AndAlso dimension IsNot Nothing Then
    	  If doc.Objects.AddLinearDimension(dimension) = Guid.Empty Then
    		rc = Rhino.Commands.Result.Failure
    	  Else
    		doc.Views.Redraw()
    	  End If
    	End If
    	Return rc
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddLinearDimension():
        rc, dimension = Rhino.Input.RhinoGet.GetLinearDimension()
        if rc==Rhino.Commands.Result.Success:
            if scriptcontext.doc.Objects.AddLinearDimension(dimension)==System.Guid.Empty:
                rc = Rhino.Commands.Result.Failure
            else:
                scriptcontext.doc.Views.Redraw()
        return rc
    
    
    if __name__=="__main__":
        AddLinearDimension()
    

  

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

