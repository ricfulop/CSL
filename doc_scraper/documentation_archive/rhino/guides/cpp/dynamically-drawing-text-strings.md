---
url: https://developer.rhino3d.com/guides/cpp/dynamically-drawing-text-strings/
scraped_at: 2025-09-08T15:39:49.623802
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

[Dynamically Drawing Text
Strings](https://developer.rhino3d.com/guides/cpp/dynamically-drawing-text-
strings/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Dynamically Drawing Text Strings

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

On occasion, it is useful to dynamically display some text while in the middle
of a point picking operation. Rhino’s `VariableFilletSrf` command is a good
example of a command that does this.

To add this capability to an plugin command, you need to:

  1. Derive a new class from `CRhinoGetPoint`.
  2. Override the `CRhinoGetPoint::DynamicDraw` virtual function.
  3. From within the `DynamicDraw` override, call `CRhinoViewport::DrawString`.

## Sample

The following example code demonstrates how to derive a new class from
`CRhinoGetPoint`, override the `CRhinoGetPoint::DynamicDraw` member, and draw
text dynamically.

    
    
    class CDrawStringGetPoint : public CRhinoGetPoint
    {
    public:
      CDrawStringGetPoint() {}
      void DynamicDraw( HDC hdc, CRhinoViewport& vp, const ON_3dPoint& pt );
    };
    
    void CDrawStringGetPoint::DynamicDraw( HDC hdc, CRhinoViewport& vp, const ON_3dPoint& pt )
    {
      // Format active point as a string
      ON_wString str;
      RhinoFormatPoint( pt, str );
    
      // Build world-to-screen coordinate transformation
      ON_Xform w2s;
      vp.VP().GetXform( ON::world_cs, ON::screen_cs, w2s );
    
      // Transform point from world to screen coordinates
      ON_3dPoint screenpoint = w2s * pt;
    
      // Offset point so text does not overlap cursor
      screenpoint.x += 5.0;
      screenpoint.y += -5.0;
    
      // Draw string using the system font
      vp.DrawString( str, str.Length(), screenpoint, false, 0, 12, L"System" );
    
      // Allow base class to draw
      CRhinoGetPoint::DynamicDraw( hdc, vp, pt );
    }
    

You can use the above class as you would a `CRhinoGetPoint` object. Just
create a new `CDrawStringGetPoint` object, initialize the class by calling
base class members, and call it’s `GetPoint` member. For example:

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CDrawStringGetPoint gp;
      gp.SetCommandPrompt( L"Pick test point" );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      // TODO...
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/dynamically-
drawing-text-strings/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/dynamically-
drawing-text-strings/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

