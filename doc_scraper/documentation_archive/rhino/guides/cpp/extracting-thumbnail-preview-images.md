---
url: https://developer.rhino3d.com/guides/cpp/extracting-thumbnail-preview-images/
scraped_at: 2025-09-08T15:39:53.532375
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

[Extracting Thumbnail Preview
Images](https://developer.rhino3d.com/guides/cpp/extracting-thumbnail-preview-
images/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Extracting Thumbnail Preview Images

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to be able to display a 3dm file’s thumbnail preview image in a
dialog box.

## Solution

When Rhino reads a 3dm file, it ignores the thumbnail preview image stored in
the file (since it is never used). Thus, if you want to obtain the thumbnail
preview image for the current document, or any 3dm file, you will have to read
the 3dm file yourself. Fortunately, you only need to read a very small portion
of the 3dm file to get the thumbnail preview image.

Rhino stores a document’s thumbnail preview image as an `ON_WindowsBitmap`,
which is just an uncompressed Windows device independent bitmap, or DIB. At
the heart of `ON_WindowsBitmap` is simply a Windows `BITMAPINFO` structure.

## Sample

The following sample code demonstrates how to read the thumbnail preview image
from a 3dm file.

    
    
    bool Read3dmThumbnailPreviewImage( const wchar_t* filename, ON_WindowsBitmap& bitmap )
    {
      if( 0 == filename | 0 == filename[0] )
        return false;
    
      try
      {
        FILE* archive_fp = ON::OpenFile( filename, L"rb" );
        if( 0 == archive_fp )
          return false;
    
        ON_BinaryFile archive( ON::read3dm, archive_fp );
    
        // STEP 1: REQUIRED - Read start section
        int file_version = 0;
        ON_String strComments;
        if( !archive.Read3dmStartSection(&file_version, strComments) )
        {
          ON::CloseFile( archive_fp );
          return false;
        }
    
        // STEP 2: REQUIRED - Read properties section
        ON_3dmProperties properties;
        if( !archive.Read3dmProperties(properties) )
        {
          ON::CloseFile( archive_fp );
          return false;
        }
    
        ON::CloseFile( archive_fp );
    
        if( !properties.m_PreviewImage.IsValid() )
          return false;
    
        bitmap = properties.m_PreviewImage;
      }
    
      catch(...) // Handle all exceptions
      {
        return false;
      }
    
      return true;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/extracting-
thumbnail-preview-images/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/extracting-
thumbnail-preview-images/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

