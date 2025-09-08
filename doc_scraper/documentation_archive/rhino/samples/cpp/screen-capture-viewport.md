---
url: https://developer.rhino3d.com/samples/cpp/screen-capture-viewport/
scraped_at: 2025-09-08T15:48:15.752086
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

Screen Capture Viewport

__

Windows only

Demonstrates how to screen capture a viewport to a file.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CWnd* pMainWnd = CWnd::FromHandle( RhinoApp().MainWnd() );
      if( 0 == pMainWnd )
        return failure;
    
      CRhinoGetFileDialog gf;
      gf.SetScriptMode( context.IsInteractive() ? FALSE : TRUE );
      BOOL rc = gf.DisplayFileDialog( CRhinoGetFileDialog::save_bitmap_dialog, 0, pMainWnd );
      if( !rc )
        return cancel;
    
      ON_wString filename = gf.FileName();
      filename.TrimLeftAndRight();
      if( filename.IsEmpty() )
        return nothing;
    
      CRhinoView* view = RhinoApp().ActiveView();
      if( view )
      {
        CRect rect;
        view->GetClientRect( rect );
    
        CRhinoDib dib;
        if( dib.CreateDib(rect.Width(), rect.Height(), 24, true) )
        {
          // Set these flags as you wish.
          BOOL bIgnoreHighlights = TRUE;
          BOOL bDrawTitle = FALSE;
          BOOL bDrawConstructionPlane = FALSE;
          BOOL bDrawWorldAxes = FALSE;
    
          CRhinoObjectIterator it( CRhinoObjectIterator::normal_or_locked_objects,
                                   CRhinoObjectIterator::active_and_reference_objects
                                   );
    
          if( view->ActiveViewport().DisplayMode() == ON::wireframe_display )
          {
            context.m_doc.DrawToDC( it, dib, dib.Width(), dib.Height(),
              view->ActiveViewport().View(),
              bIgnoreHighlights,
              bDrawTitle,
              bDrawConstructionPlane,
              bDrawWorldAxes
              );
          }
          else
          {
            context.m_doc.RenderToDC( it, dib, dib.Width(), dib.Height(),
              view->ActiveViewport().View(),
              bIgnoreHighlights,
              bDrawTitle,
              bDrawConstructionPlane,
              bDrawWorldAxes,
              view->ActiveViewport().GhostedShade()
              );
          }
    
          dib.WriteToFile( filename );
        }
      }
    
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

