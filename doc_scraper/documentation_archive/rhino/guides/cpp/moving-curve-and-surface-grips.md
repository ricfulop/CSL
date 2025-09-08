---
url: https://developer.rhino3d.com/guides/cpp/moving-curve-and-surface-grips/
scraped_at: 2025-09-08T15:40:01.710552
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

[Moving Curve and Surface
Grips](https://developer.rhino3d.com/guides/cpp/moving-curve-and-surface-
grips/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Moving Curve and Surface Grips

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to move the control points of a curve or surface object using
the Rhino C/C++ SDK.

## Solution

The curve and surface grips you see on the screen, after running Rhino’s
_PointsOn_ command, are represented by `CRhinoGripObject`-derived objects. To
move a grip object, you have to do a few things:

  1. Get a `CRhinoGripObject`. You can use a `CRhinoGetObject` object to do this.
  2. Call `CRhinoGripObject::MoveGrip` to transform the grip’s location.
  3. Call `CRhinoGripObject::Owner` to get the grips owning `CRhinoObject` object.
  4. Call `CRhinoObject::NewObject` to create a new `CRhinoObject` object based on the new grip location.
  5. Call `CRhinoDoc::ReplaceObject` to replace the original owning object with the new one.

## Sample

The following sample code demonstrates this.

**NOTE** : This sample uses a `CRhinoXformObjectList` object to maintain the
list of grips and grip owners.

    
    
    CRhinoCommand::result CCommandMoveGrips::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select grips to move" );
      go.SetGeometryFilter( CRhinoGetObject::grip_object );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      CRhinoXformObjectList xform_list;
      if( xform_list.AddObjects(go, true) < 1 )
        return failure;
    
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Point to move from" );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      ON_3dPoint from = gp.Point();
    
      gp.SetCommandPrompt( L"Point to move to" );
      gp.SetBasePoint( from );
      gp.DrawLineFromPoint( from, TRUE );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      ON_3dPoint to = gp.Point();
    
      ON_Xform xform;
      xform.Translation( to - from );
      if( xform.IsValid() )
      {
        // Transform the grip objects
        int i;
        for( i = 0; i < xform_list.m_grips.Count(); i++ )
          xform_list.m_grips[i]->MoveGrip( xform );
    
        // Replace the old owner with a new one
        for( i = 0; i < xform_list.m_grip_owners.Count(); i++ )
        {
          CRhinoObject* old_object = xform_list.m_grip_owners[i];
          if( old_object )
          {
            CRhinoObject* new_object = old_object->m_grips->NewObject();
            if( new_object )
              context.m_doc.ReplaceObject( CRhinoObjRef(old_object), new_object, true );
          }
        }
    
        context.m_doc.Redraw();
      }
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/moving-
curve-and-surface-grips/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/moving-
curve-and-surface-grips/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

