---
url: https://developer.rhino3d.com/samples/cpp/extract-isoparametric-curves-from-surfaces/
scraped_at: 2025-09-08T15:47:52.656510
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

Extracting Isoparametric Curves from Surfaces

__

Windows only

Demonstrates how to extract isoparametric curves from surfaces.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Select the surface to extract isocurve
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select surface" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      // Validate selection
      const CRhinoObjRef& ref = go.Object(0);
      const ON_Surface* srf = ref.Surface();
      if( !srf )
        return failure;
    
      ON_3dPoint pt( ON_UNSET_POINT );
      BOOL dir = FALSE;
    
      // Pick a point on the surface
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Point on surface" );
      gp.AddCommandOptionToggle(
                RHCMDOPTNAME(L"Direction"),
                RHCMDOPTVALUE(L"U"),
                RHCMDOPTVALUE(L"V"),
                dir, &dir );
      gp.Constrain( *srf );
      for(;;)
      {
        CRhinoGet::result res = gp.GetPoint();
        if( res == CRhinoGet::point )
        {
          pt = gp.Point();
          break;
        }
        else if( res == CRhinoGet::option )
          continue;
        else
          return cancel;
      }
    
      // Get the parameters of the point on
      // the surface that is closest to pt.
      double u, v;
      if( srf->GetClosestPoint(pt, &u, &v) )
      {
        // Get the isoparametric curve. ON_Surface::IsoCurve
        // allocates memory for the resulting curve that we
        // will be responsible for.
        ON_Curve* crv = srf->IsoCurve( dir, dir ? u : v );
        if( crv )
        {
          context.m_doc.AddCurveObject( *crv );
    
          // CRhinoDoc::AddCurveObject make a copy of the input curve.
          // So, we need to delete crv otherwise we will leak memory.
          delete crv;
          crv = 0;
    
          context.m_doc.Redraw();
        }
      }
    
      return success;
    }
    

  

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

