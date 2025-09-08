---
url: https://developer.rhino3d.com/samples/rhinocommon/change-dimension-style/
scraped_at: 2025-09-08T15:45:45.669295
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

Change Dimension Style

Demonstrates how to change the dimension style on all objects in a Rhino
document.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ChangeDimensionStyle(RhinoDoc doc)
      {
        foreach (var rhino_object in doc.Objects.GetObjectList(ObjectType.Annotation))
        {
          var annotation_object = rhino_object as AnnotationObjectBase;
          if (annotation_object == null) continue;
    
          var annotation = annotation_object.Geometry as AnnotationBase;
          if (annotation == null) continue;
    
          if (annotation.Index == doc.DimStyles.CurrentDimensionStyleIndex) continue;
    
          annotation.Index = doc.DimStyles.CurrentDimensionStyleIndex;
          annotation_object.CommitChanges();
        }
    
        doc.Views.Redraw();
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ChangeDimensionStyle(ByVal doc As RhinoDoc) As Result
    	For Each rhino_object In doc.Objects.GetObjectList(ObjectType.Annotation)
    	  Dim annotation_object = TryCast(rhino_object, AnnotationObjectBase)
    	  If annotation_object Is Nothing Then
    		  Continue For
    	  End If
    
    	  Dim annotation = TryCast(annotation_object.Geometry, AnnotationBase)
    	  If annotation Is Nothing Then
    		  Continue For
    	  End If
    
    	  If annotation.Index = doc.DimStyles.CurrentDimensionStyleIndex Then
    		  Continue For
    	  End If
    
    	  annotation.Index = doc.DimStyles.CurrentDimensionStyleIndex
    	  annotation_object.CommitChanges()
    	Next rhino_object
    
    	doc.Views.Redraw()
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Commands import *
    from Rhino.Geometry import *
    from scriptcontext import doc
    
    def RunCommand():
        for annotation_object in doc.Objects.GetObjectList(ObjectType.Annotation):
            if not isinstance (annotation_object, AnnotationObjectBase):
                continue
    
            annotation = annotation_object.Geometry
    
            if annotation.Index == doc.DimStyles.CurrentDimensionStyleIndex:
                continue
    
            annotation.Index = doc.DimStyles.CurrentDimensionStyleIndex
            annotation_object.CommitChanges()
    
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

