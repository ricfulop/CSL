---
url: https://developer.rhino3d.com/guides/yak/installing-and-managing-packages/
scraped_at: 2025-09-08T15:58:08.964272
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

[Installing and Managing
Packages](https://developer.rhino3d.com/guides/yak/installing-and-managing-
packages/)

  * Install
  * Uninstall
  * List
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Package Manager
Guides](https://developer.rhino3d.com/en/guides/yak/) /

Installing and Managing Packages

by [Will Pearson](https://discourse.mcneel.com/u/will/) (Last updated:
Thursday, November 12, 2020)

__Note __

Yak is cross-platform. The examples below are for Windows. For Mac, replace
the path to the Yak CLI tool with `"/Applications/Rhino
8.app/Contents/Resources/bin/yak"`.

## Install

Installing a yak package with the CLI tool is simple.

    
    
    > "C:\Program Files\Rhino 8\System\Yak.exe" install marmoset
    
    Downloading marmoset (1.0.0)...
    Downloaded marmoset (1.0.0)
    Installing marmoset (1.0.0)...
    Successfully installed marmoset (1.0.0)
    

__Note __

Rhino will load new packages the next time it starts.

You can also ask Yak to install a specific version.

    
    
    > "C:\Program Files\Rhino 8\System\Yak.exe" install marmoset 1.0.0
    
    ...
    

The package is installed to a special folder, similar to the Grasshopper
Libraries folder but with a folder/file structure that Yak controls.

## Uninstall

Packages can also be easily uninstalled using the Yak CLI tool.

    
    
    > "C:\Program Files\Rhino 8\System\Yak.exe" uninstall marmoset
    
    marmoset successfully uninstalled
    

__Note __

Rhino will register that the package has been uninstalled the next time it
starts.

## List

At any point you can check which packages are currently installed.

    
    
    > "C:\Program Files\Rhino 8\System\Yak.exe" list
    
    marmoset (1.0.0)
    

## Related Topics

  * [Yak Guides and Tutorials](https://developer.rhino3d.com/guides/yak/)
  * [Creating a Grasshopper Plug-in Package](https://developer.rhino3d.com/guides/yak/creating-a-grasshopper-plugin-package/)
  * [Creating a Rhino Plug-in Package](https://developer.rhino3d.com/guides/yak/creating-a-rhino-plugin-package/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/yak/installing-
and-managing-packages/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/yak/installing-
and-managing-packages/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

