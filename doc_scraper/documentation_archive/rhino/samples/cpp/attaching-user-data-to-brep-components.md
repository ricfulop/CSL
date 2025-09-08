---
url: https://developer.rhino3d.com/samples/cpp/attaching-user-data-to-brep-components/
scraped_at: 2025-09-08T15:48:23.808474
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

Attaching User Data to Brep Components

__

Windows only

Demonstrates how to attach object user data to components of a Brep.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
          const CRhinoCommandContext& context)
    {
      // Allow for picking of either a surface or a brep face.
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select surface to attach data" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object );
      go.EnableSubObjectSelect( TRUE );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      // Get first object reference. Note, this reference
      // reprsents the picked surface or face, not the
      // top level brep.
      const CRhinoObjRef& objref = go.Object(0);
    
      // Get face on brep that was picked
      const ON_BrepFace* face = objref.Face();
      if( !face )
        return failure;
    
      // Get the faces underlying surface
      const ON_Surface* srf = face->SurfaceOf();
      if( !srf )
        return failure;
    
      // Query surface for user data
      CTestUserData* ud = CTestUserData::Cast( srf->GetUserData(ud->m_uuid) );
      if( ud )
      {
        RhinoApp().Print( L"Data already attached.\n" );
        return nothing;
      }
    
      // Get the top level object
      const CRhinoBrepObject* obj = CRhinoBrepObject::Cast( objref.Object() );
      if( !obj )
        return failure;
    
      // Duplicate the top level object.
      CRhinoBrepObject* dupe_obj = CRhinoBrepObject::Cast( obj->DuplicateObject() );
      if( !dupe_obj )
        return failure;
    
      // Get the brep
      ON_Brep* dupe_brep = dupe_obj->Brep();
      if( !dupe_brep )
        return failure;
    
      // Get the surface
      ON_Surface* dupe_srf = dupe_brep->m_S[face->SurfaceIndexOf()];
      if( !dupe_srf )
        return failure;
    
      // New up the user data
      ud = new CTestUserData();
      if( !ud )
      {
        delete dupe_obj;
        return failure;
      }
    
      // TODO: Initialize user data object here
    
      // Attach user data to surface, not face. Note, ud
      // is now owned by dupe_srf, not by us. So, we are
      // not responsible for deleting it;
      if( !dupe_srf->AttachUserData(ud) )
      {
        delete ud;
        delete dupe_obj;
        return failure;
      }
    
      // Replace object. Note, we cannot reuse objref for it references
      // the picked face, not the top level brep.
      // Note, dupe_obj is now owned by Rhino, so we are not
      // responsible for deleting it.
      if( !context.m_doc.ReplaceObject(CRhinoObjRef(obj), dupe_obj) )
      {
        delete dupe_obj;
        return failure;
      }
    
      // Done deal
      RhinoApp().Print( L"Data attached successfully.\n" );
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

