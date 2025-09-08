---
url: https://developer.rhino3d.com/samples/cpp/hatch-boundary/
scraped_at: 2025-09-08T15:48:31.828062
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

Hatch Boundary

__

Windows only

Demonstrates how to hatch a closed planar boundary.

C/C++

    
    
    CRhinoCommand::result CCommandBrenton::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select closed planar curve" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.SetGeometryAttributeFilter( CRhinoGetObject::closed_curve );
      go.EnableSubObjectSelect( false );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const ON_Curve* crv = go.Object(0).Curve();
      if( 0 == crv | !crv->IsClosed() | !crv->IsPlanar() )
        return failure;
    
      CRhinoHatchPatternTable& table = context.m_doc.m_hatchpattern_table;
    
      CRhinoGetString gs;
      gs.SetCommandPrompt( L"Hatch pattern" );
      gs.SetDefaultString( table.CurrentHatchPattern().Name() );
      gs.GetString();
      if( gs.CommandResult() != success )
        return gs.CommandResult();
    
      ON_wString name = gs.String();
      name.TrimLeftAndRight();
      if( name.IsEmpty() )
        return nothing;
    
      int index = table.FindHatchPattern( name );
      if( index < 0 )
      {
        RhinoApp().Print( L"Hatch pattern does not exist.\n" );
        return nothing;
      }
    
      CArgsRhinoHatch args;
      args.m_loops.Append( crv );
      args.SetPatternIndex( index );
      args.SetPatternScale( 1.0 ); // default
      args.SetPatternRotation( 0.0 ); // default
    
      ON_SimpleArray<ON_Hatch*> hatches;
      bool rc = RhinoCreateHatches( args, hatches );
      if( rc && hatches.Count() )
      {
        int i, num_added = 0;
        for( i = 0; i < hatches.Count(); i++ )
        {
          ON_Hatch* hatch = hatches[0];
          if( hatch )
          {
            CRhinoHatch* hatch_obj = new CRhinoHatch();
            if( hatch_obj )
            {
              hatch_obj->SetHatch( hatch );
              if( context.m_doc.AddObject(hatch_obj) )
                num_added++;
              else
                delete hatch_obj;
            }
            else
              delete hatch;
          }
        }
    
        if( num_added )
          context.m_doc.Redraw();
      }
    
      return rc ? success : failure;
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

