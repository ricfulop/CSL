---
url: https://developer.rhino3d.com/guides/cpp/using-sizeof-with-tchar-wchar-t/
scraped_at: 2025-09-08T15:39:25.541765
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

[Using the sizeof operator with TCHAR and
wchar_t](https://developer.rhino3d.com/guides/cpp/using-sizeof-with-tchar-
wchar-t/)

  * Discussion

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Using the sizeof operator with TCHAR and wchar_t

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Discussion

The `sizeof` keyword gives the amount of storage, in bytes, associated with a
variable or a type. It does not return number of elements in an array, such as
an array of characters.

Mistakes using the `sizeof` operator when dealing with UNICODE strings is very
common. For example:

    
    
    char szBuffer[24];
    GetWindowText( hWnd, szBuffer, sizeof(szBuffer) ); // OK
    
    wchar_t wszBuffer[24];
    GetWindowText( hWnd, wszBuffer, sizeof(wszBuffer) ); // WRONG
    

In the above examples, the first block of code works because the char data
type just happens to take up only one byte of storage. Thus, the `sizeof`
operator, when used on an array of chars just happens to work. The other
example is incorrect for a `wchar_t` requires two bytes of storage. Thus, you
have just told the `GetWindowText` that the buffer you have passed in is
bigger than it really is. This can crash your plugin.

The following is the proper method for using the sizeof operator when using
UNICODE text strings…

    
    
    wchar_t wszBuffer[24];
    GetWindowText( hWnd, wszBuffer, sizeof(wszBuffer)/sizeof(wchar_t) );
    

If you find yourself writing the above statement frequently, you might
consider adding the following macro to your project:

    
    
    #define _countof(array) (sizeof(array)/sizeof(array[0]))
    
    wchar_t wszBuffer[24];
    GetWindowText( hWnd, wszBuffer, _countof(wszBuffer) );
    

The `TCHAR` data type definition is based on whether or not your plugins
compile as MBCS or as UNICODE. Rhino 6 plugins are compiled as UNICODE. Thus,
a TCHAR in Rhino 6 will be a `wchar_t`.

To be safe in all cases, you should use the following convention when dealing
with TCHARs:

    
    
    TCHAR tchBuffer[24];
    GetWindowText( hWnd, tchBuffer, sizeof(tchBuffer)/sizeof(TCHAR) );
    

In doing this, your code will be safe when compiled as either MBCS or UNICODE.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/using-
sizeof-with-tchar-wchar-t/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/using-
sizeof-with-tchar-wchar-t/index.md) [
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

