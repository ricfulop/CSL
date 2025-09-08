---
url: https://developer.rhino3d.com/guides/cpp/writing-to-text-files/
scraped_at: 2025-09-08T15:39:27.523748
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

[Writing to Text Files](https://developer.rhino3d.com/guides/cpp/writing-to-
text-files/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Writing to Text Files

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You need to write to a text file from my general utility plugin.

## Solution

Rhino C/C++ SDK does not have any special functions or classes to help you
read or write text files.

With that said, there are a number of ways to read and write text files in
C/C++.

  1. Use the C-runtime library’s `fopen`, `fputs`, `fwrite` and `fclose` functions.
  2. You can use the `iostream` library’s `ofstream` class.
  3. You can use Win32’s `CreateFile`, `WriteFile`, and `CloseHandle` functions.
  4. You can use MFC’s `CFile` and `CStdioFile` classes.

## Sample

Here is a simple example that uses the C-runtime library.

    
    
    /*
    Description:
      Writes a string to a text file
    Parameters:
      text     - [in] The string to write
      filename - [in] The name of the file to write. If the file does not
                      exist, it will be created. If the file does exist,
                      it will be overwritten.
    Returns:
      true if successful, false otherwise.
    */
    bool WriteStringToFile( const wchar_t* text, const wchar_t* filename )
    {
      bool rc = false;
      if( (text && text[0]) && (filename && filename[0]) )
      {
        FILE* fp = _wfopen( filename, L"w" );
        if( fp )
        {
          size_t num_write = wcslen( text );
          size_t num_written = fwrite( text, sizeof(wchar_t), num_write, fp );
          fclose( fp );
          rc = ( num_written == num_write );
        }
      }
      return rc;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/writing-
to-text-files/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/writing-
to-text-files/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

