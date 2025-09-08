---
url: https://developer.rhino3d.com/guides/cpp/determining-normal-direction-of-brep-face/
scraped_at: 2025-09-08T15:38:56.433095
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

[Determining the Normal Direction of a Brep
Face](https://developer.rhino3d.com/guides/cpp/determining-normal-direction-
of-brep-face/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Determining the Normal Direction of a Brep Face

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

To determine the normal direction of a surface, you can use one of the
following functions:

    
    
    ON_Surface::NormalAt()
    ON_Surface::EvNormal()
    

To determine the normal direction of a face which is part of a Brep, you can
also use the above functions, as an `ON_BrepFace` object is derived from
`ON_Surface`. But, you will also need to take into account the orientation of
the Brep face. If the orientation of the Brep face is opposite of the
underlying, natural surface orientation, then you will need to reverse the
direction of the calculated normal vector.

It should also be noted that most surfaces in Rhino are really Breps with a
single face.

## Sample

The following sample code demonstrates how to interactively determine the
normal direction of a selected surface or Brep face.

    
    
    CRhinoCommand::result CCommandNormal::RunCommand( const CRhinoCommandContext& context )
    {
      // Select a surface
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select surface" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      // Get the selected face
      const CRhinoObjRef& ref = go.Object(0);
      const ON_BrepFace* face = ref.Face();
      if( 0 == face )
        return failure;
    
      // Pick a point on the surface. Constrain
      // picking to the face.
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Select point on surface" );
      gp.Constrain( *face );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      ON_3dPoint pt = gp.Point();
    
      // Get the parameters of the point on the
      // surface that is closest to pt
      double u, v;
      if( face->GetClosestPoint(pt, &u, &v) )
      {
        ON_3dPoint pt;
        ON_3dVector du, dv, dir;
        if( face->EvNormal(u, v, pt, du, dv, dir) )
        {
          // if the face orientation is opposite of
          // the natural surface orientation, then
          // reverse the direction of the vector.
          if( face->m_bRev )
            dir.Reverse();
    
          RhinoApp().Print(
            L"Surface normal at uv(%.2f,%.2f) = (%.2f,%.2f,%.2f)\n",
            u,
            v,
            dir.x,
            dir.y,
            dir.z
            );
        }
      }
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/determining-
normal-direction-of-brep-face/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/determining-
normal-direction-of-brep-face/index.md) [
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

