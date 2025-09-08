---
url: https://developer.rhino3d.com/guides/cpp/fpu-issues/
scraped_at: 2025-09-08T15:40:46.869024
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

[FPU Issues](https://developer.rhino3d.com/guides/cpp/fpu-issues/)

  * Problem
  * Workaround

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

FPU Issues

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

When your plugin tries to perform a certain calculation, you get the following
text in Visual Studio’s output window:

    
    
    [[developer:opennurbs:home|opennurbs]] ERROR # 2 .\rhino3MathErrorHandling.cpp:154 Serious math library or floating point errors occurred.
    
    [[developer:opennurbs:home|opennurbs]] ERROR # 3 .\opennurbs_plus_fpu.cpp:289 ON_FPU_BeforeSloppyCall - fpu STAT is already dirty. See source comment for next steps.
    

## Workaround

These two opennurbs errors are most likely related.

Sometimes it is impossible to avoid calling code that performs invalid
floating point operations or rudely changes the FPU control settings. We have
found dozens of cases in Windows core DLLs, 3rd party DLLs, OpenGL drivers,
VBScript, and the .NET JIT compiler where the FPU CTRL setting is changed or
floating point exceptions are generated. When these cases are discovered, we
bracket the code that is abusing the FPU with:

    
    
    ON_FPU_BeforeSloppyCall();
    // call that abuses the FPU
    ON_FPU_AfterSloppyCall();
    

In doing this, we don’t lose any information about exceptions in our own code
and we don’t get pestered about exceptions we can’t do anything about. (Note,
if you are calling something that may run the .NET JIT, then use
`ON_FPU_AfterDotNetJITUse` instead of `ON_FPU_AfterSloppyCall`).

Also, the following error occurs when a serious divide by zero, overflow, or
invalid operation happened sometime before the call to
`ON_FPU_BeforeSloppyCall`:

    
    
    [[developer:opennurbs:home|opennurbs]] ERROR # 3 .\opennurbs_plus_fpu.cpp:289 ON_FPU_BeforeSloppyCall - fpu STAT is already dirty. See source comment for next steps.
    

These are easy to find. Start Rhino, run `TestErrorCheck` and set
`CrashOnFPUException=Yes`. Then do whatever it is that made the FPU dirty. You
will crash on the line that is dividing by zero, overflowing, or performing
the invalid operation.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/fpu-
issues/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/fpu-
issues/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

