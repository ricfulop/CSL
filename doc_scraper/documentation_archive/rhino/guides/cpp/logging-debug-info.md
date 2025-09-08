---
url: https://developer.rhino3d.com/guides/cpp/logging-debug-info/
scraped_at: 2025-09-08T15:39:04.451055
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

[Logging Debug Info](https://developer.rhino3d.com/guides/cpp/logging-debug-
info/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Logging Debug Info

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The openNURBS C/C++ SDK, which is also included with the Rhino C/C++ SDK,
contains a `ON_TextLog` class that makes it very simple to write, or dump,
information to a text file. The class can be very handy when trying to debug
geometric objects, for most objects have the ability to dump their contents to
a log file.

## Sample

The following is an example of using the `ON_TextLog` class to dump the
contents of a brep object to a text file. For more information on
`ON_TextLog`, see _opennurbs_textlog.h_

    
    
    CRhinoCommand::result CCommandTest::RunCommand(
        const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select brep" );
      go.SetGeometryFilter(
           CRhinoGetObject::surface_object |
           CRhinoGetObject::polysrf_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() == CRhinoCommand::success )
      {
        const ON_Brep* brep = go.Object(0).Brep();
        if( brep )
        {
          FILE* fp = ON::OpenFile( L"c:\\bug_report.txt", L"w" );
          if( fp )
          {
            ON_TextLog text_log( fp );
            text_log.Print( L"Dumping Brep...\n" );
            brep->Dump( text_log );
            ON::CloseFile( fp );
          }
        }
      }
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/logging-
debug-info/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/logging-
debug-info/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

