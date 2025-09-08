---
url: https://developer.rhino3d.com/samples/rhinocommon/orthogonal-mode/
scraped_at: 2025-09-08T15:46:30.870403
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

Orthogonal Mode

Demonstrates how to enable or disable orthogonal mode and its effects.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result Ortho(RhinoDoc doc)
      {
        var gp = new GetPoint();
        gp.SetCommandPrompt("Start of line");
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var start_point = gp.Point();
    
        var original_ortho = ModelAidSettings.Ortho;
        if (!original_ortho)
          ModelAidSettings.Ortho = true;
    
        gp.SetCommandPrompt("End of line");
        gp.SetBasePoint(start_point, false);
        gp.DrawLineFromPoint(start_point, true);
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var end_point = gp.Point();
    
        if (ModelAidSettings.Ortho != original_ortho)
          ModelAidSettings.Ortho = original_ortho;
    
        doc.Objects.AddLine(start_point, end_point);
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function Ortho(ByVal doc As RhinoDoc) As Result
    	Dim gp = New GetPoint()
    	gp.SetCommandPrompt("Start of line")
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim start_point = gp.Point()
    
    	Dim original_ortho = ModelAidSettings.Ortho
    	If Not original_ortho Then
    	  ModelAidSettings.Ortho = True
    	End If
    
    	gp.SetCommandPrompt("End of line")
    	gp.SetBasePoint(start_point, False)
    	gp.DrawLineFromPoint(start_point, True)
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim end_point = gp.Point()
    
    	If ModelAidSettings.Ortho IsNot original_ortho Then
    	  ModelAidSettings.Ortho = original_ortho
    	End If
    
    	doc.Objects.AddLine(start_point, end_point)
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.ApplicationSettings import *
    from Rhino.Commands import *
    from Rhino.Input.Custom import *
    from scriptcontext import doc
    
    def RunCommand():
        gp = GetPoint()
        gp.SetCommandPrompt("Start of line")
        gp.Get()
        if gp.CommandResult() != Result.Success:
            return gp.CommandResult()
        start_point = gp.Point()
    
        original_ortho = ModelAidSettings.Ortho
        if not original_ortho:
            ModelAidSettings.Ortho = True
    
        gp.SetCommandPrompt("End of line")
        gp.SetBasePoint(start_point, False)
        gp.DrawLineFromPoint(start_point, True)
        gp.Get()
        if gp.CommandResult() != Result.Success:
            return gp.CommandResult()
        end_point = gp.Point()
    
        if ModelAidSettings.Ortho != original_ortho:
            ModelAidSettings.Ortho = original_ortho
    
        doc.Objects.AddLine(start_point, end_point)
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

