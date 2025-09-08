---
url: https://developer.rhino3d.com/samples/rhinocommon/replace-hatch-pattern/
scraped_at: 2025-09-08T15:44:55.492903
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

Replace Hatch Pattern

Demonstrates how to replace an object's hatch pattern.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ReplaceHatchPattern(RhinoDoc doc)
      {
        ObjRef[] obj_refs;
        var rc = RhinoGet.GetMultipleObjects("Select hatches to replace", false, ObjectType.Hatch, out obj_refs);
        if (rc != Result.Success || obj_refs == null)
          return rc;
    
        var gs = new GetString();
        gs.SetCommandPrompt("Name of replacement hatch pattern");
        gs.AcceptNothing(false);
        gs.Get();
        if (gs.CommandResult() != Result.Success)
          return gs.CommandResult();
        var hatch_name = gs.StringResult();
    
        var pattern_index = doc.HatchPatterns.Find(hatch_name, true);
    
        if (pattern_index < 0)
        {
          RhinoApp.WriteLine("The hatch pattern \"{0}\" not found  in the document.", hatch_name);
          return Result.Nothing;
        }
    
        foreach (var obj_ref in obj_refs)
        {
          var hatch_object = obj_ref.Object() as HatchObject;
          if (hatch_object.HatchGeometry.PatternIndex != pattern_index)
          {
            hatch_object.HatchGeometry.PatternIndex = pattern_index;
            hatch_object.CommitChanges();
          }
        }
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ReplaceHatchPattern(ByVal doc As RhinoDoc) As Result
    	Dim obj_refs() As ObjRef = Nothing
    	Dim rc = RhinoGet.GetMultipleObjects("Select hatches to replace", False, ObjectType.Hatch, obj_refs)
    	If rc IsNot Result.Success OrElse obj_refs Is Nothing Then
    	  Return rc
    	End If
    
    	Dim gs = New GetString()
    	gs.SetCommandPrompt("Name of replacement hatch pattern")
    	gs.AcceptNothing(False)
    	gs.Get()
    	If gs.CommandResult() <> Result.Success Then
    	  Return gs.CommandResult()
    	End If
    	Dim hatch_name = gs.StringResult()
    
    	Dim pattern_index = doc.HatchPatterns.Find(hatch_name, True)
    
    	If pattern_index < 0 Then
    	  RhinoApp.WriteLine("The hatch pattern ""{0}"" not found  in the document.", hatch_name)
    	  Return Result.Nothing
    	End If
    
    	For Each obj_ref In obj_refs
    	  Dim hatch_object = TryCast(obj_ref.Object(), HatchObject)
    	  If hatch_object.HatchGeometry.PatternIndex IsNot pattern_index Then
    		hatch_object.HatchGeometry.PatternIndex = pattern_index
    		hatch_object.CommitChanges()
    	  End If
    	Next obj_ref
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Commands import *
    from Rhino.Input import *
    from Rhino.Input.Custom import *
    from scriptcontext import doc
    
    def RunCommand():
        rc, obj_refs = RhinoGet.GetMultipleObjects("Select hatches to replace", False, ObjectType.Hatch)
        if rc != Result.Success or obj_refs == None:
            return rc
    
        gs = GetString()
        gs.SetCommandPrompt("Name of replacement hatch pattern")
        gs.AcceptNothing(False)
        gs.Get()
        if gs.CommandResult() != Result.Success:
            return gs.CommandResult()
        hatch_name = gs.StringResult()
    
        pattern_index = doc.HatchPatterns.Find(hatch_name, True)
    
        if pattern_index < 0:
            RhinoApp.WriteLine("The hatch pattern \"{0}\" not found  in the document.", hatch_name)
            return Result.Nothing
    
        for obj_ref in obj_refs:
            hatch_object = obj_ref.Object()
            if hatch_object.HatchGeometry.PatternIndex != pattern_index:
                hatch_object.HatchGeometry.PatternIndex = pattern_index
                hatch_object.CommitChanges()
    
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

