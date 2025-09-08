---
url: https://developer.rhino3d.com/samples/cpp/add-brep-box/
scraped_at: 2025-09-08T15:47:07.004314
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

Add a Brep Box

__

Windows only

Demonstrates how to add a Brep Box from a Rhino C++ plugin.

C/C++

    
    
    CRhinoCommand::result CCommandTestSdk::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoCommand::result rc = CRhinoCommand::nothing;
    
      // define the corners of the box
      ON_3dPointArray corners;
      corners.Append( ON_3dPoint( 0.0,  0.0,  0.0) );
      corners.Append( ON_3dPoint(10.0,  0.0,  0.0) );
      corners.Append( ON_3dPoint(10.0, 10.0,  0.0) );
      corners.Append( ON_3dPoint( 0.0, 10.0,  0.0) );
      corners.Append( ON_3dPoint( 0.0,  0.0, 10.0) );
      corners.Append( ON_3dPoint(10.0,  0.0, 10.0) );
      corners.Append( ON_3dPoint(10.0, 10.0, 10.0) );
      corners.Append( ON_3dPoint( 0.0, 10.0, 10.0) );
    
      // Build the brep  
      ON_Brep* pBrep = ON_BrepBox( corners );
      if( pBrep )
      {
        CRhinoBrepObject* pObject = new CRhinoBrepObject();
        pObject->SetBrep( pBrep );
        if( context.m_doc.AddObject(pObject) )
        {
          context.m_doc.Redraw();
          rc = CRhinoCommand::success;
        }
        else
        {
          delete pObject;
          pObject = 0;
          rc = CRhinoCommand::failure;
        }
      }
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

