---
url: https://developer.rhino3d.com/samples/cpp/create-surface-from-edge-curves/
scraped_at: 2025-09-08T15:47:27.986611
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

Create Surface from Edge Curves

__

Windows only

Demonstrates how to create a surface object from four edge curves.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      // Pick four curve objects
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select 4 curves" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object);
      go.GetObjects( 4, 4 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      // Validate results
      int i, count = go.ObjectCount();
      if( count != 4 )
        return CRhinoCommand::failure;
    
      ON_NurbsCurve nc[4];
      // Get nurb form of each curve
      for( i = 0; i < count; i++)
      {
        const ON_Curve* crv = go.Object(i).Curve();
        if( !crv )
          return CRhinoCommand::failure;
        if( !crv->GetNurbForm(nc[i]) )
          return CRhinoCommand::failure;
      }
    
      // Create the surface
      ON_Brep* brep = RhinoCreateEdgeSrf( 4, nc );
      if( !brep )
      {
        RhinoApp().Print( L"Unable to create surface.\n" );
        return CRhinoCommand::failure;
      }
    
      // Ready new brep object
      CRhinoBrepObject* obj = new CRhinoBrepObject;
      obj->SetBrep( brep );
    
      // Add new objet to document
      if( !context.m_doc.AddObject( obj ) )
      {
        delete obj;
        RhinoApp().Print( L"Unable to create surface.\n" );
        return CRhinoCommand::failure;
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

