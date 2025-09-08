---
url: https://developer.rhino3d.com/guides/cpp/enabling-orthogonal-mode/
scraped_at: 2025-09-08T15:39:51.627114
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

[Enabling Orthogonal Mode](https://developer.rhino3d.com/guides/cpp/enabling-
orthogonal-mode/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Enabling Orthogonal Mode

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You are trying to draw a line and you need ortho enabled.

## Solution

The state of Rhino’s orthogonal drawing mode is stored in Rhino’s application
settings, or it’s `CRhinoAppSettings` object. To check the current state of
ortho, call `CRhinoAppSettings::Ortho`. To enable or disable ortho, call
`CRhinoAppSettings::EnableOrtho` and pass in the boolean value that is
appropriate. For more information on this and Rhino’s application settings
class, see _rhinoSdkAppSettings.h_.

## Sample

The following sample code illustrates how to use this feature:

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoGetPoint gp;
      gp.SetCommandPrompt(L"Starting point");
      gp.GetPoint();
      if (gp.CommandResult() != success)
        return gp.CommandResult();
    
      ON_3dPoint start_point = gp.Point();
    
      CRhinoAppSettings& settings = RhinoApp().AppSettings();
      bool bOldValue = settings.Ortho();
      if (bOldValue == false)
        settings.EnableOrtho(true);
    
      gp.SetCommandPrompt(L"Ending point");
      gp.SetBasePoint(start_point);
      gp.DrawLineFromPoint(start_point, true);
      gp.GetPoint();
    
      if (bOldValue != settings.Ortho())
        settings.EnableOrtho(bOldValue);
    
      if (gp.CommandResult() != success)
        return gp.CommandResult();
    
      ON_3dPoint end_point = gp.Point();
    
      ON_Line line(start_point, end_point);
      context.m_doc.AddCurveObject(line);
      context.m_doc.Redraw();
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/enabling-
orthogonal-mode/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/enabling-
orthogonal-mode/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

