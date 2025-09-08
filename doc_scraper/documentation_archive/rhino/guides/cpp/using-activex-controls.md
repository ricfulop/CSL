---
url: https://developer.rhino3d.com/guides/cpp/using-activex-controls/
scraped_at: 2025-09-08T15:40:20.774665
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

[Using ActiveX Controls](https://developer.rhino3d.com/guides/cpp/using-
activex-controls/)

  * Problem
  * Solution
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Using ActiveX Controls

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

ActiveX controls placed in a simple dialog box will crash Rhino.

## Solution

ActiveX, or OLE, controls work in Rhino plugins, as C/C++ plugin are simply
regular MFC DLLs. For more information on MFC DLLs, read [MFC Technical Note
33](http://msdn.microsoft.com/en-us/library/hw85e4bb%28v=VS.80%29.aspx) and
[MFC Technical Note 58](http://msdn.microsoft.com/en-
us/library/ft1t4bbc%28v=VS.80%29.aspx) for more information.

Also, you will need to call this function:

    
    
    void AfxEnableControlContainer();
    

in your `CWinApp`-derived object’s `InitInstance()` member to enable support
for containment of OLE controls.

## Related Topics

  * [MFC ActiveX Controls (on MSDN)](https://msdn.microsoft.com/en-us/library/k194shk8%28v=VS.80%29.aspx)
  * [MFC Technical Note 33 (on MSDN)](http://msdn.microsoft.com/en-us/library/hw85e4bb%28v=VS.80%29.aspx)
  * [MFC Technical Note 58](http://msdn.microsoft.com/en-us/library/ft1t4bbc%28v=VS.80%29.aspx)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/using-
activex-controls/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/using-
activex-controls/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

