---
url: https://developer.rhino3d.com/samples/cpp/divide-curve-by-segments/
scraped_at: 2025-09-08T15:47:50.669164
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

Divide a Curve by Segments

__

Windows only

Demonstrates how to divide a selected curve object by a specified number of
segments.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select curve to divide" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.GetObjects( 1, 1 );
    
      if( go.Result() == CRhinoGet::cancel )
        return CRhinoCommand::cancel;
    
      if( go.Result() != CRhinoGet::object | go.ObjectCount() <= 0 )
        return CRhinoCommand::failure;
    
      CRhinoObjRef& objref = go.Object(0);
      const ON_Curve* crv = objref.Curve();
      if( !crv )
        return CRhinoCommand::failure;
    
      CRhinoGetInteger gi;
      gi.SetCommandPrompt( L"Number of segments" );
      gi.SetDefaultInteger( 2 );
      gi.SetLowerLimit( 2 );
      gi.SetUpperLimit( 100 );
      gi.GetInteger();
    
      if( gi.Result() == CRhinoGet::cancel )
        return CRhinoCommand::cancel;
    
      if( gi.Result() != CRhinoGet::number )
        return CRhinoCommand::failure;
    
      int count = gi.Number();
      count++;
      ON_SimpleArray<double> t( count );
      t.SetCount( count );
    
      int i;
      for( i = 0; i < count; i++ )
      {
        double param = (double)i / ((double)count-1);
        t[i] = param;
      }
      if( crv->GetNormalizedArcLengthPoints(count, (double*)&t[0], (double*)&t[0]) )
      {
        for( i = 0; i < count; i++ )
        {
          ON_3dPoint pt = crv->PointAt( t[i] );
          context.m_doc.AddPointObject( pt );
        }
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

