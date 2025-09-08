---
url: https://developer.rhino3d.com/samples/cpp/create-new-view/
scraped_at: 2025-09-08T15:47:25.102025
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

Create New View

__

Windows only

Demonstrates how to create a new view that has the properties of an existing
view.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      AFX_MANAGE_STATE( ::RhinoApp().RhinoModuleState() );
    
      ON_SimpleArray<ON_UUID> viewport_ids;
      ON_SimpleArray<CRhinoView*> view_list;
      CRhinoView* view = 0;
      int i = 0;
    
      // Build a list of (current) viewport ids
      context.m_doc.GetViewList( view_list, true, false );
      for( i = 0; i < view_list.Count(); i++ )
      {
        CRhinoView* view = view_list[i];
        if( view )
          viewport_ids.Append( view->ActiveViewportID() );
      }
      view_list.Empty();
    
      // Create a new view
      context.m_doc.NewView( ON_3dmView() );
    
      // Find the viewport (id) that was just created
      context.m_doc.GetViewList( view_list, true, false );
      for( i = 0; i < view_list.Count(); i++ )
      {
        view = view_list[i];
        if( view )
        {
          int rc = viewport_ids.Search( view->ActiveViewportID() );
          if( rc < 0 )
            break;
          else
            view = 0;
        }
      }
    
      // Make the necessary updates.
      if( view )
      {
        ON_3dmView v = view->ActiveViewport().View();
        v.m_name = L"New View";
        view->ActiveViewport().SetView( v );
        view->Redraw();
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

