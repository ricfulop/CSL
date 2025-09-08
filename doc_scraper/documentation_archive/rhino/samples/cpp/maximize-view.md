---
url: https://developer.rhino3d.com/samples/cpp/maximize-view/
scraped_at: 2025-09-08T15:48:13.721031
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

Maximize View

__

Windows only

Demonstrates how to maximize a view.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoGetString gs;
      gs.SetCommandPrompt( L"Name of viewport to maximize" );
      gs.GetString();
      if( gs.CommandResult() != CRhinoCommand::success )
        return gs.CommandResult();
    
      ON_wString view_name( gs.String() );
      view_name.TrimLeftAndRight();
      if( view_name.IsEmpty() )
        return CRhinoCommand::cancel;
    
      ON_SimpleArray<CRhinoView*> view_list;
      int view_count = context.m_doc.GetViewList( view_list );
    
      CRhinoView* active_view = NULL;
      int i;
    
      for( i = 0; i < view_count; i++ )
      {
        CRhinoView* view = view_list[i];
        if( view && view_name.CompareNoCase(view->Viewport().Name()) == 0 )
        {
          active_view = view;
          break;
        }
      }
    
      if( !active_view )
      {
        RhinoApp().Print( L"Unable to find viewport named %s\n", view_name );
        return CRhinoCommand::nothing;
      }
    
      ::RhinoApp().SetActiveView( active_view );
      CWnd* frame_wnd = active_view->GetParent();
      if( frame_wnd )
      {
        frame_wnd->ShowWindow( SW_SHOWMAXIMIZED );
        frame_wnd->BringWindowToTop();
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

