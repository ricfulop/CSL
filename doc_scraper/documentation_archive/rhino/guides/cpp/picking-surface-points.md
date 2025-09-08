---
url: https://developer.rhino3d.com/guides/cpp/picking-surface-points/
scraped_at: 2025-09-08T15:39:13.363537
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

[Picking Surface Point](https://developer.rhino3d.com/guides/cpp/picking-
surface-points/)

  * Problem
  * Solution
  * Using CRhinoGetObject
  * Using CRhinoGetPoint

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Picking Surface Point

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You want to pick a point on the surface of an object.

## Solution

There are a couple of ways to do this:

  * Use a `CRhinoGetObject` class.
  * Use a `CRhinoGetPoint` class.

## Using CRhinoGetObject

When picking objects with a `CRhinoGetObject` object, the `CRhinoObjRef`
returned by the object contains picking information, such as the location of
the pick…

    
    
    CRhinoCommand::result CCommandTestPick1::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select a surface or a polysurface" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object | CRhinoGetObject::polysrf_object );
      go.EnablePreSelect( FALSE );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const CRhinoObjRef& ref = go.Object(0);
    
      // If the object was selected by picking a point on it, then
      // SelectionPoint() returns true and the point where the selection
      // occured.
      ON_3dPoint pt;
      if( ref.SelectionPoint(pt) )
      {
        context.m_doc.AddPointObject( pt );
        context.m_doc.Redraw();
      }
    
      return CRhinoCommand::success;
    }
    

## Using CRhinoGetPoint

When picking points with a `CRhinoGetPoint` object, you can constrain the
point picking to a surface…

    
    
    CRhinoCommand::result CCommandTestPick2::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select a surface" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object );
      go.EnablePreSelect( FALSE );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const CRhinoObjRef& ref = go.Object(0);
      const ON_BrepFace* face = ref.Face();
      if( 0 == face )
        return CRhinoCommand::failure;
    
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Select point on surface" );
      gp.Constrain( *face );
      gp.GetPoint();
      if( gp.CommandResult() != CRhinoCommand::success )
        return gp.CommandResult();
    
      ON_3dPoint pt = gp.Point();
      context.m_doc.AddPointObject( pt );
      context.m_doc.Redraw();
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/picking-
surface-points/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/picking-
surface-points/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

