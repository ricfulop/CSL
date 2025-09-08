---
url: https://developer.rhino3d.com/guides/cpp/duplicating-objects-with-group/
scraped_at: 2025-09-08T15:39:46.601909
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

[Duplicating Objects with
Group](https://developer.rhino3d.com/guides/cpp/duplicating-objects-with-
group/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Duplicating Objects with Group

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

When you duplicate a Rhino object which happens to be a member of a group, the
duplicate object is (also) a member of that same group. Is there a quick way
to duplicate a Rhino object and have the duplicated object be a member of a
new group?

## Solution

You can use the `RhinoUpdateObjectGroups` function. See _rhinoSdkGrips.h_ for
details.

Here is a sample of its usage:

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select objects to copy in-place" );
      go.EnableGroupSelect( TRUE );
      go.EnableSubObjectSelect( FALSE );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      ON_Xform xform;
      xform.Identity();
    
      ON_2dexMap group_map;
    
      for( int i = 0; i < go.ObjectCount(); i++ )
      {
        const CRhinoObject* object = go.Object(i).Object();
        if( object )
        {
          CRhinoObject* duplicate = context.m_doc.TransformObject( object, xform, true, false, true );
          if( duplicate )
            RhinoUpdateObjectGroups( duplicate, group_map );
        }
      }
    
      context.m_doc.Redraw();
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/duplicating-
objects-with-group/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/duplicating-
objects-with-group/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

