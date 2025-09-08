---
url: https://developer.rhino3d.com/samples/cpp/extend-surface/
scraped_at: 2025-09-08T15:48:07.747982
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

Extend Surface

__

Windows only

Demonstrates how to use RhinoExtendSurface() to extend a surface object.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select edge of surface to extend" );
      go.SetGeometryFilter(CRhinoGetObject::edge_object);
      go.SetGeometryAttributeFilter( CRhinoGetObject::edge_curve );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const CRhinoObjRef& objref = go.Object(0);
      const ON_Surface* srf = objref.Surface();
      if( !srf )
      {
        RhinoApp().Print( L"Unable to extend polysurfaces.\n" );
        return CRhinoCommand::nothing;    
      }
    
      const ON_Brep* brep = objref.Brep();
      const ON_BrepFace* face = objref.Face();
      if( !brep | !face | face->m_face_index < 0 )
        return CRhinoCommand::failure;
    
      if( !brep->IsSurface() )
      {
        RhinoApp().Print( L"Unable to extend trimmed surfaces.\n" );
        return CRhinoCommand::nothing;    
      }
    
      const ON_BrepTrim* trim = objref.Trim();
      if( !trim )
        return CRhinoCommand::failure;
    
      ON_Surface::ISO edge_index( trim->m_iso );
      int dir = edge_index % 2;
      if( srf->IsClosed(1-dir) )
      {
        RhinoApp().Print(L"Unable to extend surface at seam.\n" );
        return CRhinoCommand::nothing;  
      }
      if( edge_index < ON_Surface::W_iso | edge_index > ON_Surface::N_iso )
      {
        RhinoApp().Print( L"Selected edge must be an underlying surface edge.\n" );
        return CRhinoCommand::nothing;  
      }
    
      ON_Surface* myface = srf->DuplicateSurface();
      if( !myface )
        return CRhinoCommand::failure;
    
      bool rc = RhinoExtendSurface( myface, edge_index, 5.0, true);  
      if( rc )
      {
        ON_Brep* mybrep = new ON_Brep();
        mybrep->Create( myface );
        CRhinoBrepObject* obj = new CRhinoBrepObject();
        obj->SetBrep( mybrep );
        context.m_doc.ReplaceObject( CRhinoObjRef(objref.Object()), obj );
        context.m_doc.Redraw();
      }
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

