---
url: https://developer.rhino3d.com/guides/opennurbs/linking-with-opennurbs/
scraped_at: 2025-09-08T15:38:08.229697
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

[Linking with
openNURBS](https://developer.rhino3d.com/guides/opennurbs/linking-with-
opennurbs/)

  * Problem
  * Solution
  * Sample
    * opennurbs_static_linking.h
    * opennurbs_dynamic_linking.h

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Linking with openNURBS

by [Dale Lear](https://discourse.mcneel.com/u/dalelear/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You are trying to write a simple console application like the _example_write_
sample included with the openNURBS toolkit. However, you are having problems
linking. You are using the _opennurbs_staticlib_linking_pragmas.h_ header
included with openNURBS, but it does not seem to work.

## Solution

The _opennurbs_staticlib_linking_pragmas.h_ header, included with openNURBS,
is only designed to help build the example projects included with the toolkit.
That is, it only works if your project is inside the openNURBS folder.

Unlike the `#include` statement, `#pragma` statements, used in this header,
are not very path smart. The library paths used by `#pragma` statement must be
relative to the project, not the `#include` file in which it is used.

You certainly don’t have to use _opennurbs_staticlib_linking_pragmas.h_ in
your project. You can always add the required openNURBS libraries to your
project’s _Additional Dependencies_ link settings. You can also just include
the required libraries in your project, like you would a _.cpp_ or _.h_ file.

But, if you like the flexibility that providing linking instructions via
`#pragma` statements provide, then you can always change
_opennurbs_staticlib_linking_pragmas.h_ to reflect the path to your project.
That said, if you use openNURBS in more than one project and the projects are
not all stored in the same relative location, this will not work.

## Sample

Below is sample that contains two header files that you can include in any
project that needs to link with openNURBS. One of the headers provides
instruction for statically linking openNURBS, and the other one for
dynamically linking. Once these files are included in your project, you can
edit them to reflect your project’s relative path to the openNURBS toolkit.

### opennurbs_static_linking.h

    
    
    /////////////////////////////////////////////////////////////////////////////
    // linking_pragmas_static.h
    
    // This file is specific to Micrsoft's compiler.
    
    #pragma once
    
    #if defined(ON_DLL_IMPORTS) || defined(ON_DLL_EXPORTS)
    #error This file contains STATIC LIBRARY linking pragmas.
    #endif
    
    #if defined(WIN64)
    
    // x64 (64 bit) static libraries
    
    #if defined(NDEBUG)
    
    // Release x64 (64 bit) libs
    #pragma message( " --- openNURBS Release x64 (64 bit) build." )
    #pragma comment(lib, "../opennurbs/zlib/x64/Release/zlibx64.lib")
    #pragma comment(lib, "../opennurbs/x64/ReleaseStaticLib/opennurbsx64_static.lib")
    
    #else // _DEBUG
    
    // Debug x64 (64 bit) libs
    #pragma message( " --- openNURBS Debug x64 (64 bit) build." )
    #pragma comment(lib, "../opennurbs/zlib/x64/Debug/zlibx64_d.lib")
    #pragma comment(lib, "../opennurbs/x64/DebugStaticLib/opennurbsx64_staticd.lib")
    
    #endif // NDEBUG else _DEBUG
    
    #else // WIN32
    
    // x86 (32 bit) static libraries
    
    #if defined(NDEBUG)
    
    // Release x86 (32 bit) libs
    #pragma message( " --- openNURBS Release x86 (32 bit) build." )
    #pragma comment(lib, "../opennurbs/zlib/Release/zlib.lib")
    #pragma comment(lib, "../opennurbs/ReleaseStaticLib/opennurbs_static.lib")
    
    #else // _DEBUG
    
    // Debug x86 (32 bit) libs
    #pragma message( " --- openNURBS Debug x86 (32 bit) build." )
    #pragma comment(lib, "../opennurbs/zlib/Debug/zlib_d.lib")
    #pragma comment(lib, "../opennurbs/DebugStaticLib/opennurbs_staticd.lib")
    
    #endif // NDEBUG else _DEBUG
    
    #endif // WIN64 else WIN32
    

### opennurbs_dynamic_linking.h

    
    
    /////////////////////////////////////////////////////////////////////////////
    // linking_pragmas_static.h
    
    // This file is specific to Micrsoft's compiler.
    
    #pragma once
    
    #if !defined(ON_DLL_IMPORTS)
    #error This file contains DYNAMIC LIBRARY linking pragmas.
    #endif
    
    #if defined(WIN64)
    
    // x64 (64 bit) dynamic libraries
    
    #if defined(NDEBUG)
    
    // Release x64 (64 bit) libs
    #pragma message( " --- openNURBS Release x64 (64 bit) build." )
    #pragma comment(lib, "../opennurbs/zlib/x64/Release/zlibx64.lib")
    #pragma comment(lib, "../opennurbs/x64/Release/opennurbsx64.lib")
    
    #else // _DEBUG
    
    // Debug x64 (64 bit) libs
    #pragma message( " --- openNURBS Debug x64 (64 bit) build." )
    #pragma comment(lib, "../opennurbs/zlib/x64/Debug/zlibx64_d.lib")
    #pragma comment(lib, "../opennurbs/x64/Debug/opennurbsx64_d.lib")
    
    #endif // NDEBUG else _DEBUG
    
    #else // WIN32
    
    // x86 (32 bit) dynamic libraries
    
    #if defined(NDEBUG)
    
    // Release x86 (32 bit) libs
    #pragma message( " --- openNURBS Release x86 (32 bit) build." )
    #pragma comment(lib, "../opennurbs/zlib/Release/zlib.lib")
    #pragma comment(lib, "../opennurbs/Release/opennurbs.lib")
    
    #else // _DEBUG
    
    // Debug x86 (32 bit) libs
    #pragma message( " --- openNURBS Debug x86 (32 bit) build." )
    #pragma comment(lib, "../opennurbs/zlib/Debug/zlib_d.lib")
    #pragma comment(lib, "../opennurbs/Debug/opennurbs_d.lib")
    
    #endif // NDEBUG else _DEBUG
    
    #endif // WIN64 else WIN32
    

To use these headers, just include them to your project’s _stdafx.h_ file like
this:

    
    
    // stdafx.h
    
    #pragma once
    
    #include "targetver.h"
    
    #include <stdio.h>
    #include <tchar.h>
    
    // TODO: reference additional headers your program requires here
    
    // Uncomment the following if you want to use the openNURBS dynamic link library
    //#define ON_DLL_IMPORTS
    
    #include "../opennurbs/opennurbs.h"
    
    #if defined(ON_DLL_IMPORTS)
    #include "opennurbs_dynamic_linking.h"
    #else
    #include "opennurbs_static_linking.h"
    #endif
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/linking-
with-opennurbs/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/linking-
with-opennurbs/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

