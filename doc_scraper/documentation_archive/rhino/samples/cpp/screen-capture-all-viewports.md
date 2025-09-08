---
url: https://developer.rhino3d.com/samples/cpp/screen-capture-all-viewports/
scraped_at: 2025-09-08T15:48:14.742342
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

Screen Capture All Viewports

__

Windows only

Demonstrates how to screen capture all the visible viewports to a file.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      AFX_MANAGE_STATE( ::RhinoApp().RhinoModuleState() );
    
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
    
      // Wait for the dialog to disappear. Otherwise,
      // we might see dialog artifacts in our image.
      RhinoApp().Wait( 500 );
    
      CMDIFrameWnd* pFrameWnd = (CMDIFrameWnd*)pMainWnd;
      if( pFrameWnd )
      {
        CWnd* pClientWnd = CWnd::FromHandle( pFrameWnd->m_hWndMDIClient );
        if( pClientWnd )
        {
          CClientDC srcDC( pClientWnd );
    
          CRect rect;
          pClientWnd->GetClientRect( rect );
    
          CRhinoDib dib;
          if( dib.CreateDib(rect.Width(), rect.Height(), 24, true) )
          {
            CDC* dstDC = dib;
            if( dstDC )
            {
              dstDC->BitBlt( 0, 0, rect.Width(), rect.Height(), &srcDC, 0, 0, SRCCOPY );
              dib.CopyToClipboard( 0 );
              dib.WriteToFile( filename );
            }
          }
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

