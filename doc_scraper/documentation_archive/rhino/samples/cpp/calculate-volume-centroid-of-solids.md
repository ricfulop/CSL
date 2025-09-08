---
url: https://developer.rhino3d.com/samples/cpp/calculate-volume-centroid-of-solids/
scraped_at: 2025-09-08T15:48:27.786321
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

Calculate Volume Centroid of Solids

__

Windows only

http://wiki.mcneel.com/developer/sdksamples/volumecentroid

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select solids for volume centroid calculation" );
      go.SetGeometryFilter(
            CRhinoGetObject::surface_object |
            CRhinoGetObject::polysrf_object
            );
      go.SetGeometryAttributeFilter(
            CRhinoGetObject::closed_surface |
            CRhinoGetObject::closed_polysrf
            );
      go.EnableSubObjectSelect( false );
      go.EnableGroupSelect( true );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      ON_SimpleArray<const ON_Geometry*> geom( go.ObjectCount() );
      int i;
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const ON_Geometry* geo = go.Object(i).Geometry();
        if( 0 == geo )
          return failure;
        geom.Append( geo );
      }
    
      // Get bounding box of all objects
      ON_BoundingBox bbox;
      for( i = 0; i < geom.Count(); i++ )
        geom[i]->GetBoundingBox( bbox, bbox.IsValid() );
    
      ON_3dPoint base_point = bbox.Center();
      ON_SimpleArray<ON_MassProperties> MassProp;
      MassProp.Reserve( geom.Count() );
    
      for( i = 0; i < geom.Count(); i++ )
      {
        ON_MassProperties* mp = &MassProp.AppendNew();
    
        if( const ON_Surface* srf = ON_Surface::Cast(geom[i]) )
          srf->VolumeMassProperties( *mp, true, true, false, false, base_point );       
    
        else if( const ON_Brep* brep = ON_Brep::Cast(geom[i]) )
          brep->VolumeMassProperties( *mp, true, true, false, false, base_point );
      }
    
      ON_MassProperties results;
      results.Sum( MassProp.Count(), MassProp.Array() );
    
      ON_3dPoint pt( results.m_x0, results.m_y0, results.m_z0 );
      context.m_doc.AddPointObject( pt );
      context.m_doc.Redraw();
    
      RhinoApp().Print( L"Volume centroid = %g,%g,%g\n", pt.x, pt.y, pt.z );
    
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

