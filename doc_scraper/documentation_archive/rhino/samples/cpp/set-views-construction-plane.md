---
url: https://developer.rhino3d.com/samples/cpp/set-views-construction-plane/
scraped_at: 2025-09-08T15:48:17.766918
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

Set a View's Construction Plane

__

Windows only

Demonstrates how to set a view's construction plane.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
              const CRhinoCommandContext& context )
    {
      CRhinoView* view = ::RhinoApp().ActiveView();
      if( !view )
        return CRhinoCommand::failure;
    
      CRhinoGetOption go;
      go.SetCommandPrompt( L"Select a construction plane" );
      int back_option   = go.AddCommandOption( RHCMDOPTNAME(L"Back") );
      int bottom_option = go.AddCommandOption( RHCMDOPTNAME(L"Bottom") );
      int front_option  = go.AddCommandOption( RHCMDOPTNAME(L"Front") );
      int left_option   = go.AddCommandOption( RHCMDOPTNAME(L"Left") );
      int right_option  = go.AddCommandOption( RHCMDOPTNAME(L"Right") );
      int top_option    = go.AddCommandOption( RHCMDOPTNAME(L"Top") );
    
      go.GetOption();
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const CRhinoCommandOption* opt = go.Option();
      if( !opt )
        return CRhinoCommand::failure;
    
      int option_index = opt->m_option_index;
      ON_3dmConstructionPlane cplane = view->Viewport().ConstructionPlane();
      if( option_index == back_option )
        cplane.m_plane.CreateFromPoints( ON_origin, -ON_xaxis ,ON_zaxis );
      else if( option_index == bottom_option )
        cplane.m_plane.CreateFromPoints( ON_origin, -ON_xaxis, ON_yaxis );
      else if( option_index == front_option )
        cplane.m_plane.CreateFromPoints( ON_origin, ON_xaxis, ON_zaxis );
      else if( option_index == left_option )
        cplane.m_plane.CreateFromPoints( ON_origin, -ON_yaxis, ON_zaxis );
      else if( option_index == right_option )
        cplane.m_plane.CreateFromPoints( ON_origin, ON_yaxis, ON_zaxis );
      else if( option_index == top_option )
        cplane.m_plane.CreateFromPoints( ON_origin, ON_xaxis, ON_yaxis );
      else
        return CRhinoCommand::failure;
    
      view->Viewport().PushConstructionPlane( cplane );
      view->Redraw();
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

