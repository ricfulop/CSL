---
url: https://developer.rhino3d.com/guides/cpp/plugin-loading/
scraped_at: 2025-09-08T15:40:05.739196
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

[Plugin Loading](https://developer.rhino3d.com/guides/cpp/plugin-loading/)

  * Loading

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Plugin Loading

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Loading

Rhino plugins are loaded twice. The first time as follows:

    
    
    hModule = ::LoadLibraryEx(
        lpFileName,
        0,
        DONT_RESOLVE_DLL_REFERENCES | LOAD_WITH_ALTERED_SEARCH_PATH
        );
    

By using the `DONT_RESOLVE_DLL_REFERENCES` flag, the system does not call the
plugin’s `DllMain` for process and thread initialization and termination.
Also, the system does not load additional executable modules that are
referenced by the specified module. This allows Rhino to quickly verify the
Rhino SDK version and that the proper plugin exports are available.

The `LOAD_WITH_ALTERED_SEARCH_PATH` flag is used so `LoadLibraryEx` looks for
dependent DLLs in the directory specified by `lpFileName`, not by _Rhino.exe_.

The plugin module is freed as follows:

    
    
    ::FreeLibrary( hModule );
    

If the above was successful, the plugin is loaded for a final time as follows:

    
    
    hModule = ::LoadLibraryEx(
        lpFileName,
        0,
        LOAD_WITH_ALTERED_SEARCH_PATH
        );
    

Again, the altered search path flag is used.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/plugin-
loading/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/plugin-
loading/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

