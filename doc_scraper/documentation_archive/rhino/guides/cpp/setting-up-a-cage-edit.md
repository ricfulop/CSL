---
url: https://developer.rhino3d.com/guides/cpp/setting-up-a-cage-edit/
scraped_at: 2025-09-08T15:40:11.708409
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

[Setting Up a Cage Edit](https://developer.rhino3d.com/guides/cpp/setting-up-
a-cage-edit/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Setting Up a Cage Edit

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Imagine you have two objects: a surface and a line curve and you would like to
setup cage editing, with the surface as the captive object and the line curve
as the control object.

## Solution

To allow the line curve to control the surface, you will need to create a
`CRhinoMorphControl` object. A `CRhinoMorphControl` object has a
`ON_MorphControl` object, as its data member, which contains the definition of
the controlling object (in this case, line).

Once you have properly defined the `ON_MorphControl` object and created the
runtime `CRhinoMorphControl` object, you can use the RhinoCaptureObject API
function to setup the “capture.”

The following example code demonstrates how you might write a command that
allows a surface to be controlled by a line…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      ON_Workspace ws;
      CRhinoCommand::result rc = CRhinoCommand::success;
    
      // Get the captive object
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select captive surface or polysurface" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object | CRhinoGetObject::polysrf_object );
      go.GetObjects( 1, 1 );
      rc = go.CommandResult();
      if( CRhinoCommand::success != rc )
        return rc;
    
      const CRhinoObject* captive = go.Object(0).Object();
      if( 0 == captive )
        return CRhinoCommand::failure;
    
      // Define the control line
      ON_Line line;
      rc = RhinoGetLine( CArgsRhinoGetLine(), line );
      if( CRhinoCommand::success != rc )
        return rc;
    
      // Get the curve parameters
      int degree = 3;
      int cv_count = 4;
      for(;;)
      {
        CRhinoGetOption gl;
        gl.SetCommandPrompt( L"NURBS Parameters" );
        gl.AcceptNothing();
        int d_opt = gl.AddCommandOptionInteger( RHCMDOPTNAME(L"Degree"), &degree, L"Curve degree", 1.0, 100.0 );
        int p_opt = gl.AddCommandOptionInteger( RHCMDOPTNAME(L"PointCount"), &cv_count, L"Number of control points", 2.0, 100.0 );
        gl.GetOption();
        rc = gl.CommandResult();
        if( CRhinoCommand::success != rc )
          return rc;
    
        if( CRhinoGet::nothing == gl.Result() )
          break;
    
        if( cv_count <= degree )
        {
          if( CRhinoGet::option != gl.Result() )
            continue;
          const CRhinoCommandOption* opt = go.Option();
          if( 0 == opt )
            continue;
          if( d_opt == opt->m_option_index )
            cv_count = degree + 1;
          else
            degree = cv_count - 1;
        }
      }
    
      // Set up morph control
      ON_MorphControl* control = new ON_MorphControl();
      control->m_varient = 1; // 1= curve
    
      // Specify the source line curve
      control->m_nurbs_curve0.Create( 3, false, 2, 2 );
      control->m_nurbs_curve0.MakeClampedUniformKnotVector();
      control->m_nurbs_curve0.SetCV( 0, line.from );
      control->m_nurbs_curve0.SetCV( 1, line.to );
    
      // Specify the destination NURBS curve
      control->m_nurbs_curve.Create( 3, false, degree + 1, cv_count );
      control->m_nurbs_curve.MakeClampedUniformKnotVector();
      double* g = ws.GetDoubleMemory( control->m_nurbs_curve.m_cv_count );
      control->m_nurbs_curve.GetGrevilleAbcissae( g );
      ON_Interval d = control->m_nurbs_curve.Domain();
      double s = 0.0;
      int i;
      for( i = 0; i < control->m_nurbs_curve.m_cv_count; i++ )
      {
        s = d.NormalizedParameterAt( g[i] );
        control->m_nurbs_curve.SetCV( i, line.PointAt(s) );
      }
    
      // Make sure domains match
      s = line.Length();
      if( s > ON_SQRT_EPSILON )
        control->m_nurbs_curve0.SetDomain( 0.0, s );
      d = control->m_nurbs_curve0.Domain();
      control->m_nurbs_curve.SetDomain( d[0], d[1] );
    
      // Create the morph control object
      CRhinoMorphControl* control_object = new CRhinoMorphControl();
      control_object->SetControl( control );
      context.m_doc.AddObject( control_object );
    
      // Set up the capture
      RhinoCaptureObject( control_object, const_cast<CRhinoObject*>(captive) );
    
      // Clean up display
      context.m_doc.UnselectAll();
    
      // Turn on the control grips
      control_object->EnableGrips( true );
      context.m_doc.Redraw( CRhinoView::mark_display_hint );
    
      return rc;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/setting-
up-a-cage-edit/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/setting-
up-a-cage-edit/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

