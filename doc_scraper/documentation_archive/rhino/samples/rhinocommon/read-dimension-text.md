---
url: https://developer.rhino3d.com/samples/rhinocommon/read-dimension-text/
scraped_at: 2025-09-08T15:46:34.922767
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

Read Dimension Text

Demonstrates how to read dimension text from an annotation object.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ReadDimensionText(RhinoDoc doc)
      {
        var go = new GetObject();
        go.SetCommandPrompt("Select annotation");
        go.GeometryFilter = ObjectType.Annotation;
        go.Get();
        if (go.CommandResult() != Result.Success)
          return Result.Failure;
        var annotation = go.Object(0).Object() as AnnotationObjectBase;
        if (annotation == null)
          return Result.Failure;
    
        RhinoApp.WriteLine("Annotation text = {0}", annotation.DisplayText);
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ReadDimensionText(ByVal doc As RhinoDoc) As Result
    	Dim go = New GetObject()
    	go.SetCommandPrompt("Select annotation")
    	go.GeometryFilter = ObjectType.Annotation
    	go.Get()
    	If go.CommandResult() <> Result.Success Then
    	  Return Result.Failure
    	End If
    	Dim annotation = TryCast(go.Object(0).Object(), AnnotationObjectBase)
    	If annotation Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	RhinoApp.WriteLine("Annotation text = {0}", annotation.DisplayText)
    
    	Return Result.Success
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

