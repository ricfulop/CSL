---
url: https://developer.rhino3d.com/samples/cpp/create-plane-surface/
scraped_at: 2025-09-08T15:47:27.120751
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

Create Plane Surface

__

Windows only

Demonstrates how to create a plane surface.

C/C++

    
    
    CArgsRhinoGetPlane args;
    args.SetFirstPointPromptCorners( L"First corner of plane" );
    args.SetSecondPointPromptCorners( L"Other corner or length" );
    args.SetFirstPointPrompt3Point( L"Start of edge" );
    args.SetSecondPointPrompt3Point( L"End of edge" );
    args.SetThirdPointPrompt3Point( L"Width. Press Enter to use length" );
    args.SetFirstPointPromptVertical( L"Start of edge" );
    args.SetSecondPointPromptVertical( L"End of edge" );
    args.SetThirdPointPromptVertical( L"Height. Press Enter to use width" );
    args.SetFirstPointPromptCenter( L"Center of plane" );
    args.SetSecondPointPromptCenter( L"Other corner or length" );
    args.SetAllow3Point();
    args.SetAllowCenter();
    args.SetAllowVertical();
    args.SetAllowRounded( false );
    args.SetAllowDeformable( false );
    
    ON_3dPoint corners[4];
    CRhinoCommand::result rc = RhinoGetRectangle( args, corners );
    
    if( rc == CRhinoCommand::success)
    {
      ON_3dPoint& p0 = corners[0];
      ON_3dPoint& p1 = corners[1];
      ON_3dPoint& p3 = corners[3];
    
      ON_Interval domain0, domain1;
      domain0.Set( 0.0, p0.DistanceTo(p1) );
      domain1.Set( 0.0, p0.DistanceTo(p3) );
    
      ON_Plane plane( p0, p1, p3 );
    
      ON_PlaneSurface ps( plane );
      ps.SetExtents( 0, domain0, true );
      ps.SetExtents( 1, domain1, true );
      ps.SetDomain( 0, domain0.Min(), domain0.Max() );
      ps.SetDomain( 1, domain1.Min(), domain1.Max() );
    
      context.m_doc.AddSurfaceObject( ps );
      context.m_doc.Redraw();
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

