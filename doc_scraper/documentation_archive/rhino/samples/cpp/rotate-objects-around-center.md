---
url: https://developer.rhino3d.com/samples/cpp/rotate-objects-around-center/
scraped_at: 2025-09-08T15:48:40.829035
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

Rotate Objects Around Center

__

Windows only

Demonstrates how rotate objects around the center point of their bounding box.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Select objects to rotate
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select objects to rotate" );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      // Rotation angle (in degrees)
      CRhinoGetNumber gn;
      gn.SetCommandPrompt( L"Rotation angle" );
      gn.SetDefaultNumber( m_angle );
      gn.GetNumber();
      if( gn.CommandResult() != success )
        return gn.CommandResult();
    
      // Validate input
      double angle = gn.Number();
      if( angle == 0 )
        return nothing;
    
      m_angle = angle;
    
      // Get the active view's construction plane
      ON_Plane plane = RhinoActiveCPlane();
    
      // Do not split objects that get kinky
      // when they are transformed.
      CRhinoKeepKinkySurfaces keep_kinky_srfs;
    
      int i;
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        // Get an object reference
        const CRhinoObjRef& ref = go.Object(i);
    
        // Get the real object
        const CRhinoObject* obj = ref.Object();
        if( !obj )
          continue;
    
        // Get the object's tight bounding box
        ON_BoundingBox bbox;
        if( !obj->GetTightBoundingBox(bbox, false, 0) )
          continue;
    
        // Create transformation matrix
        ON_Xform xform;
        xform.Rotation( m_angle * ON_PI / 180.0, plane.zaxis, bbox.Center() );
    
        // Transform the object
        context.m_doc.TransformObject( obj, xform, true, true, true );
      }
    
      context.m_doc.Redraw();
    
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

