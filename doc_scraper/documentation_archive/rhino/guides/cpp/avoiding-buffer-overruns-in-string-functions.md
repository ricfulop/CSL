---
url: https://developer.rhino3d.com/guides/cpp/avoiding-buffer-overruns-in-string-functions/
scraped_at: 2025-09-08T15:38:46.400136
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

[Avoiding Buffer Overruns in String
Functions](https://developer.rhino3d.com/guides/cpp/avoiding-buffer-overruns-
in-string-functions/)

  * Overview
  * A Safer Method

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Avoiding Buffer Overruns in String Functions

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Buffer overruns can be caused by passing buffers to functions without also
passing the buffer’s size.

Consider the following function:

    
    
    int GetName( wchar_t* pInput )
    {
      wchar_t* pBuffer = (wchar_t*)malloc(100);
      wcscpy( pBuffer, pInput ); // might overrun buffer!
      wcscat( pBuffer, L".txt"); // also might overrun buffer!
      <...>
    }
    

## A Safer Method

Use the following techniques to write safer functions…

Add a `size_t` argument for buffer size…

    
    
    // Pass pointer to buffer and buffer size
    int GetName( wchar_t* buffer, size_t buffer_size );
    
    // Ex:
    wchar_t buffer[100];
    int rc = GetName( buffer, _countof(buffer) );
    
    // Ex:
    const size_t kBufLen = 100;
    wchar_t* pBuffer = new wchar_t[kBufLen];
    GetName( pBuffer, kBufLen );
    <...>
    delete pBuffer;
    
    // Ex:
    const size_t kBufLen = 100;
    ON_wString strBuffer;
    strBuffer.ReserveArray( kBufLen );
    GetName( strBuffer.Array(), kBufLen );
    
    // Ex:
    const size_t kBufLen = 100;
    CString strBuffer;
    GetName( strBuffer.GetBuffer(kBufLen), kBufLen );
    strBuffer.ReleaseBuffer();
    

Change buffer argument to use a string object reference…

    
    
    // Pass a reference to a ON_wString object
    int GetName( ON_wString& str );
    // Pass a reference to a CString object
    int GetName( CString& str );
    
    // Ex:
    ON_wString str;
    int rc = GetName( str );
    
    // Ex:
    CString str;
    int rc = GetName( str );
    

…change buffer argument to a fixed size array reference…

    
    
    // Pass a reference to a fixed size array
    int GetName( wchar_t(&buffer)[100] );
    
    // Ex:
    wchar_t buffer[100];
    int rc = GetName( buffer );
    

Change buffer point argument to reference to a pointer…

    
    
    // Pass a reference to a pointer
    // API allocates buffer, caller required to free it
    int GetName( wchar_t*& pBuffer );
    
    // Ex:
    wchar_t* pBuffer = 0;
    int rc = GetName( pBuffer );
    <...>
    delete pBuffer;
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/avoiding-
buffer-overruns-in-string-functions/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/avoiding-
buffer-overruns-in-string-functions/index.md) [
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

