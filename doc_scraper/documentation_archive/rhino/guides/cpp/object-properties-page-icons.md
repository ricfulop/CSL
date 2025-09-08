---
url: https://developer.rhino3d.com/guides/cpp/object-properties-page-icons/
scraped_at: 2025-09-08T15:40:03.744569
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

[Object Properties Page
Icons](https://developer.rhino3d.com/guides/cpp/object-properties-page-icons/)

  * Problem
  * Solution
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Object Properties Page Icons

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

In Rhino, the object properties dialog shows a list of icons that allows you
to select between the available properties pages. You would like to add a
custom icon to the object properties dialog when your plugin adds a custom
page.

## Solution

Derive your custom object properties page from
`CRhinoObjectPropertiesDialogPageEx`, which has a virtual `Icon()` member that
you must override and implement. You will want to implement this virtual
function as follows:

    
    
    HICON CTestObjectPropertiesPageExDlg::Icon() const
    {
      AFX_MANAGE_STATE( AfxGetStaticModuleState() );
      return (HICON)::LoadImage(AfxGetInstanceHandle(), MAKEINTRESOURCE(IDI_OBJPROPPAGE_DIALOG), IMAGE_ICON, 24, 24, LR_SHARED);
    }
    

**NOTE** : Make carefully the `AFX_MANAGE_STATE` macro. See [MFC Technical
Notes 33](https://msdn.microsoft.com/en-us/library/hw85e4bb.aspx) and
[58](https://msdn.microsoft.com/en-us/library/ft1t4bbc.aspx) for additional
details.

## Related Topics

  * [TN033: DLL Version of MFC (on MSDN)](https://msdn.microsoft.com/en-us/library/hw85e4bb.aspx)
  * [TN058: MFC Module State Implementation (on MSDN)](https://msdn.microsoft.com/en-us/library/ft1t4bbc.aspx)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/object-
properties-page-icons/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/object-
properties-page-icons/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

