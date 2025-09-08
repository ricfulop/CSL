---
url: https://developer.rhino3d.com/samples/cpp/boolean-difference/
scraped_at: 2025-09-08T15:48:24.798568
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

Boolean Difference

__

Windows only

Demonstrates how to perform a Boolean Difference operation on two sets of
polysurfaces.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select first set of polysurfaces" );
      go.SetGeometryFilter( CRhinoGetObject::polysrf_object );
      go.EnablePreSelect( TRUE );
      go.GetObjects( 1, 0 );
      if( success != go.CommandResult() )
        return go.CommandResult();
    
      ON_SimpleArray<const ON_Brep*> InBreps0( go.ObjectCount() );
      int i;
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const ON_Brep* brep = go.Object(i).Brep();
        if( brep )
          InBreps0.Append( brep );
      }
    
      go.SetCommandPrompt( L"Select second set of polysurfaces" );
      go.EnablePreSelect( FALSE );
      go.EnableDeselectAllBeforePostSelect( false );
      go.GetObjects( 1, 0 );
      if( success != go.CommandResult() )
        return go.CommandResult();
    
      ON_SimpleArray<const ON_Brep*> InBreps1( go.ObjectCount() );
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const ON_Brep* brep = go.Object(i).Brep();
        if( brep )
          InBreps1.Append( brep );
      }
    
      ON_SimpleArray<ON_Brep*> OutBreps;
      ON_SimpleArray<int> InputIndexForOutput;
      bool something_happened = false;
      double tolerance = context.m_doc.AbsoluteTolerance();
    
      bool rc = RhinoBooleanDifference(
            InBreps0,
            InBreps1,
            tolerance,
            &something_happened,
            OutBreps,
            InputIndexForOutput
            );
    
      if( !rc | !something_happened )
      {
        for( i = 0; i < OutBreps.Count(); i++ )
        {
          delete OutBreps[i];
          OutBreps[i] = 0;
        }
        return nothing;
      }
    
      for( i = 0; i < OutBreps.Count(); i++ )
      {
        ON_Brep* brep = OutBreps[i];
        if( brep )
        {
          context.m_doc.AddBrepObject( *brep );
          brep = 0;
          delete OutBreps[i];
          OutBreps[i] = 0;
        }
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

