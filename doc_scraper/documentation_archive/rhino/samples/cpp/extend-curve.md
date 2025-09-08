---
url: https://developer.rhino3d.com/samples/cpp/extend-curve/
scraped_at: 2025-09-08T15:47:51.644186
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

Extend Curve

__

Windows only

Demonstrates how to extend a curve by a line, arc or smooth extension until it
intersects a collection of objects.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
            const CRhinoCommandContext& context )
    {
      CRhinoGetObject gc;
      gc.SetCommandPrompt( L"Select line to extend" );
      gc.SetGeometryFilter( CRhinoGetObject::curve_object );
      gc.GetObjects( 1, 1 );
      if( gc.CommandResult() != CRhinoCommand::success )
        return gc.CommandResult();
    
      const CRhinoObjRef& objref = gc.Object(0);
      const ON_Curve* pC = ON_Curve::Cast( objref.Geometry() );
      if( !pC )
        return CRhinoCommand::failure;
    
      int side = 0; // start of curve
      ON_3dPoint pt;
      if( objref.SelectionPoint(pt) )
      {
        ON_3dPoint p0 = pC->PointAtStart();
        ON_3dPoint p1 = pC->PointAtEnd();
        if( (p0-pt).Length() > (p1-pt).Length() )
          side = 1; // end of curve
      }
    
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select boundary surfaces" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object |
                            CRhinoGetObject::polysrf_object );
      go.EnablePreSelect( false );
      go.EnableDeselectAllBeforePostSelect( false );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      int object_count = go.ObjectCount();
      ON_SimpleArray<const ON_Geometry*> geom( object_count );
    
      for( int i = 0; i < object_count; i++ )
      {
        const CRhinoObject* obj = go.Object(i).Object();
        if( obj )
          geom.Append( obj->Geometry() );
      }
    
      if( geom.Count() <= 0 )
        return CRhinoCommand::cancel;
    
      ON_Curve* crv = pC->DuplicateCurve();
      if( !crv )
        return CRhinoCommand::failure;
    
      // Do the curve extension
      bool rc = RhinoExtendCurve(crv, CRhinoExtend::Line, side, geom);
    
      if( rc )
      {
        // CRhinoDoc::ReplaceObject() will copy our curve
        // so, we will need to clean up when finshed.
        context.m_doc.ReplaceObject( objref, *crv );
        context.m_doc.Redraw();
      }
    
      // Clean up or leak...
      delete crv;
      crv = 0;
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

