---
url: https://developer.rhino3d.com/guides/cpp/pre-and-post-picking-objects/
scraped_at: 2025-09-08T15:39:15.479084
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

[Pre- and Post-Picking Objects](https://developer.rhino3d.com/guides/cpp/pre-
and-post-picking-objects/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Pre- and Post-Picking Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The normal operation for commands that manipulate geometric objects is to
allow the user to either pre-pick or post-pick the objects. Occasionally,
though, it might be necessary for commands to want to allow for both pre-
picked and post-picked objects. That is, after it has been determined that
objects were pre-picked, allow the user to continue to pos-pick more objects.

## Sample

The following code sample demonstrates this capability…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      bool bObjectsWerePreSelected = false;
      bool bObjectsWerePostSelected = false;
      ON_SimpleArray<const CRhinoObject*> obj_list;
    
      // Select some objects. Allow for pre-selected objects
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select objects" );
      go.EnablePreSelect( TRUE );
      go.GetObjects( 0, 0 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      // Add the selected objects to our list
      int i;
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const CRhinoObjRef& objref = go.Object(i);
        const CRhinoObject* obj = objref.Object();
        if( obj )
          obj_list.Append( obj );
      }
    
      // Determine of the bjects were pre-selected
      // or post-selected.
      if( go.ObjectsWerePreSelected() )
        bObjectsWerePreSelected = true;
      else
        bObjectsWerePostSelected = true;
    
      // If objects were pre-selected, then select
      // more objects. But, ignore pre-selected ones.
      if( bObjectsWerePreSelected )
      {
        go.EnablePreSelect( FALSE );
        go.EnableDeselectAllBeforePostSelect( FALSE );
        go.GetObjects( 0, 0 );
        if( go.CommandResult() != CRhinoCommand::success )
          return go.CommandResult();
    
        for( i = 0; i < go.ObjectCount(); i++ )
        {
          const CRhinoObjRef& objref = go.Object(i);
          const CRhinoObject* obj = objref.Object();
          if( obj )
            obj_list.Append( obj );
        }
    
        bObjectsWerePostSelected = true;
      }
    
      if( obj_list.Count() == 0 )
        return CRhinoCommand::nothing;
      //
      // TODO: do something with the object list here
      //
      // The normal behavior of commands is that when they finish,
      // objects that were pre-selected remain selected and objects
      // that were post-selected will not be selected. Because we
      // potentially could have both, we'll try to do something
      // consistent.
      if( bObjectsWerePreSelected && bObjectsWerePreSelected )
      {
        for( i = 0; i < obj_list.Count(); i++ )
        {
          const CRhinoObject* obj = obj_list[i];
          if( obj && obj->IsSelected() )
            obj->Select( false );
        }
        context.m_doc.Redraw();
      }
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/pre-
and-post-picking-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/pre-
and-post-picking-objects/index.md) [
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

