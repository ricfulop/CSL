---
url: https://developer.rhino3d.com/samples/cpp/convert-arc-to-nurbs-curve/
scraped_at: 2025-09-08T15:47:45.612746
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

Convert an Arc to a NURBS Curve

__

Windows only

Demonstrates how to convert an ON_ArcCurve object to an ON_NurbsCurve object.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select arc to convert" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.SetGeometryAttributeFilter( CRhinoGetObject::open_curve );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const CRhinoObjRef& obj_ref = go.Object(0);
      const CRhinoObject* obj = obj_ref.Object();
      if( !obj )
        return failure;
    
      const ON_ArcCurve* arc_crv = ON_ArcCurve::Cast( obj_ref.Geometry() );
      if( !arc_crv )
      {
        RhinoApp().Print( L"Curve is not an arc.\n" );
        return nothing;
      }
    
      ON_NurbsCurve nurbs_crv;
      if( arc_crv->GetNurbForm(nurbs_crv) && nurbs_crv.IsValid() )
      {
        ON_3dmObjectAttributes attribs = obj->Attributes();
        context.m_doc.AddCurveObject( nurbs_crv, &attribs );
        context.m_doc.DeleteObject( obj_ref );
        context.m_doc.Redraw();
        return success;
      }
    
      return failure;
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

