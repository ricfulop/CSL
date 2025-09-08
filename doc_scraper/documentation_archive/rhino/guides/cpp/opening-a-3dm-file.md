---
url: https://developer.rhino3d.com/guides/cpp/opening-a-3dm-file/
scraped_at: 2025-09-08T15:39:09.454485
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

[Open a 3DM file](https://developer.rhino3d.com/guides/cpp/opening-a-3dm-
file/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Open a 3DM file

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to open a 3DM file, or an STL file, or any other file type that
Rhino supports, from your C/C++ plugin.

## Solution

As each type of file, support by Rhino for opening or importing, has a
different set of options, it not possible to write a single, generic file open
function and hope to support all formats. Thus, if you want to open or import
a file from a plugin command, then simply script either Rhino’s _Open_ or
_Import_ command using `CRhinoApp::RunScript()`.

## Sample

The following example command demonstrates how to open a Rhino 3DM file from a
plugin command. You can use this same technique to open other support file
types, such as STL, IGES, DWG, and others.

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Prompt the user for the name of a 3dm file to open
      ON_wString filename;
      CWnd* pParentWnd = CWnd::FromHandle( RhinoApp().MainWnd() );
    
      CRhinoGetFileDialog gf;
      gf.SetScriptMode( context.IsInteractive() ? FALSE : TRUE );
      BOOL rc = gf.DisplayFileDialog( CRhinoGetFileDialog::open_rhino_only_dialog, filename, pParentWnd );
      if( !rc )
        return CRhinoCommand::cancel;
    
      // Verify the file name string
      filename = gf.FileName();
      filename.TrimLeftAndRight();
      if( filename.IsEmpty() )
        return CRhinoCommand::nothing;
    
      // Verify the file
      if( !CRhinoFileUtilities::FileExists(filename) )
      {
        RhinoApp().Print( L"File not found.\n" );
        return CRhinoCommand::failure;
      }
    
      // Script Rhino's open command. Note, in case the file name
      // string contains spaces, we will want to surround the string
      // with double-quote characters so the command line parser
      // will deal with the string property.
      ON_wString script;
      script.Format( L"_-Open \"%s\"", filename );
      RhinoApp().RunScript( script, 0 );
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/opening-a-3dm-
file/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/opening-a-3dm-
file/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

