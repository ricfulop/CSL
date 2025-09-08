---
url: https://developer.rhino3d.com/samples/cpp/crhinogetfiledialog-to-preview-images/
scraped_at: 2025-09-08T15:48:29.787588
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

CRhinoGetFileDialog to Preview Bitmaps

__

Windows only

Demonstrates how to use the CRhinoGetFileDialog class to preview bitmap
images.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      ON_wString filename;
    
      // Prompt for a bitmap filename
      CRhinoGetFileDialog gf;
      gf.SetScriptMode( context.IsInteractive() ? FALSE : TRUE );
      BOOL rc = gf.DisplayFileDialog(
            CRhinoGetFileDialog::open_bitmap_dialog,
            filename,
            CWnd::FromHandle( RhinoApp().MainWnd() )
            );
      if( !rc )
        return cancel;
    
      // Verify filename
      filename = gf.FileName();
      filename.TrimLeftAndRight();
      if( filename.IsEmpty() )
        return cancel;
    
      // Verify the file
      if( !CRhinoFileUtilities::FileExists(filename) )
      {
        ON_wString error = L"The specified file was not found.\n";
        if( context.IsInteractive() )
          ::RhinoMessageBox( error, L"Test", MB_OK | MB_ICONEXCLAMATION );
        else
          RhinoApp().Print( error );
        return CRhinoCommand::failure;
      }
    
      // Verify the bitmap
      CRhinoDib dib;
      if( !dib.ReadFromFile(filename) )
      {
        ON_wString error = L"The specified file cannot be identifed as a supported type.\n";
        if( context.IsInteractive() )
          ::RhinoMessageBox( error, L"Test", MB_OK | MB_ICONEXCLAMATION );
        else
          RhinoApp().Print( error );
        return CRhinoCommand::failure;
      }
    
      // To do...
    
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

