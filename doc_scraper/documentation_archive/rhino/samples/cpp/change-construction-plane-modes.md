---
url: https://developer.rhino3d.com/samples/cpp/change-construction-plane-modes/
scraped_at: 2025-09-08T15:48:28.782052
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

Change Construction Plane Modes

__

Windows only

Demonstrates how to switch between standard and universal construction plane
modes.

C/C++

    
    
    CRhinoCommand::result CCommandCPlaneMode::RunCommand( const CRhinoCommandContext& context )
    {
      BOOL bUPlane = RhinoApp().AppSettings().ModelAidSettings().m_uplane_mode;
    
      ON_wString str;
      if( bUPlane )
        str = L"Universal construction planes enabled. New value";
      else
        str = L"Standard construction planes enabled. New value";
    
      CRhinoGetOption go;
      go.SetCommandPrompt( str );
      int c_option = go.AddCommandOption( RHCMDOPTNAME(L"CPlane") );
      int u_option = go.AddCommandOption( RHCMDOPTNAME(L"UPlane") );
      int t_option = go.AddCommandOption( RHCMDOPTNAME(L"Toggle") );
      go.GetOption();
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const CRhinoCommandOption* option = go.Option();
      if( 0 == option )
        return CRhinoCommand::failure;
    
      CRhinoAppModelAidSettings settings = RhinoApp().AppSettings().ModelAidSettings();
    
      int option_index = option->m_option_index;
      if( c_option == option_index )
      {
        if( bUPlane )
        {
          settings.m_uplane_mode = FALSE;
          RhinoApp().AppSettings().SetModelAidSettings( settings );
        }
      }
      else if( u_option == option_index )
      {
        if( !bUPlane )
        {
          settings.m_uplane_mode = TRUE;
          RhinoApp().AppSettings().SetModelAidSettings( settings );
        }
      }
      else if( t_option == option_index )
      {
        settings.m_uplane_mode = !bUPlane;
        RhinoApp().AppSettings().SetModelAidSettings( settings );
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

