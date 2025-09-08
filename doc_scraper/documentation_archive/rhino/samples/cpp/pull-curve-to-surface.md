---
url: https://developer.rhino3d.com/samples/cpp/pull-curve-to-surface/
scraped_at: 2025-09-08T15:47:55.645558
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

Pull Curve to Surface

__

Windows only

Demonstrates how to use ON_Surface::Pullback() to pull a curve object to a
surface object.

C/C++

    
    
    CRhinoCommand::result CCommandTestSdk::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject gc;
      gc.SetCommandPrompt( L"Select a curve on a surface" );
      gc.SetGeometryFilter( CRhinoGetObject::curve_object );
      gc.GetObjects( 1, 1 );
      if( gc.CommandResult() != CRhinoCommand::success )
        return gc.CommandResult();
    
      const ON_Curve* pC3d = gc.Object(0).Curve();
      if( !pC3d )
        return CRhinoCommand::failure;
    
      CRhinoGetObject gs;
      gs.SetCommandPrompt(L"Select the surface" );
      gs.EnableHighlight();
      gs.SetGeometryFilter( CRhinoGetObject::surface_object );
      gs.EnableDeselectAllBeforePostSelect( false );
      gs.EnablePreSelect( FALSE );
      gs.GetObjects( 1, 1 );
      if( gs.CommandResult() != CRhinoCommand::success )
        return gs.CommandResult();
    
      const ON_Surface* pS = gs.Object(0).Surface();
      if( !pS )
        return CRhinoCommand::failure;
    
      ON_Curve* pC2d = pS->Pullback( *pC3d, context.m_doc.AbsoluteTolerance() );
      if( !pC2d )
      {
        RhinoApp().Print( L"Unable to pull curve to surface.\n" );
        return CRhinoCommand::failure;
      }
    
      // At this point we now have a 2D curve to do with what we want.
      // In this case, we will just add it to the document.
      pC2d->ChangeDimension(3);
      if( pC2d->IsValid() )
      {
        CRhinoCurveObject* crv_obj = new CRhinoCurveObject();
        crv_obj->SetCurve( pC2d );
        if( !context.m_doc.AddObject(crv_obj) )
        {
          delete crv_obj;
          return CRhinoCommand::failure;
        }
      }
    
      context.m_doc.Redraw();
    
      return CRhinoCommand::success;
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

