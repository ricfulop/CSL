---
url: https://developer.rhino3d.com/samples/cpp/reparameterize-curve/
scraped_at: 2025-09-08T15:47:56.665408
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

Reparameterize Curve

__

Windows only

Demonstrates how to Reparameterize a curve object.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoCommand::result rc = CRhinoCommand::success;
    
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve to reparameterize" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
      rc = go.CommandResult();
      if( rc != CRhinoCommand::success )
        return rc;
    
      CRhinoObjRef& objref = go.Object(0);
      const ON_Curve* pC = objref.Curve();
      if( !pC )
        return CRhinoCommand::failure;
    
      double s0, s1;
      pC->GetDomain( &s0, &s1 );
    
      CRhinoGetNumber gn;
      gn.SetCommandPrompt( L"Domain start" );
      gn.SetDefaultNumber( s0 ) ;
      gn.AcceptNothing();
      gn.GetNumber();
      rc = gn.CommandResult();
      if( rc != CRhinoCommand::success )
        return rc;
    
      double t0 = gn.Number();
    
      gn.SetCommandPrompt( L"Domain end" );
      gn.SetDefaultNumber( s1 );
      gn.SetLowerLimit( t0, TRUE );
      gn.AcceptNothing();
      gn.GetNumber();
      rc = gn.CommandResult();
      if( rc != CRhinoCommand::success )
        return rc;
    
      double t1 = gn.Number();
    
      if( s0 == t0 && s1 == t1 )
        return CRhinoCommand::nothing;
    
      ON_Curve *pNC = pC->DuplicateCurve();
      if( pNC )
      {
        pNC->SetDomain( t0, t1 );
        CRhinoCurveObject* obj = new CRhinoCurveObject();
        if( obj )
        {
          obj->SetCurve( pNC );
          context.m_doc.ReplaceObject( objref, obj );
          context.m_doc.Redraw();
       }
       else
         rc = CRhinoCommand::failure;
      }
      else
        rc = CRhinoCommand::failure;
    
      return rc;
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

