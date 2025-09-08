---
url: https://developer.rhino3d.com/guides/yak/creating-a-multi-targeted-rhino-plugin-package/
scraped_at: 2025-09-08T15:58:07.080306
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

[Creating a Multi-targeted Rhino Plug-In
Package](https://developer.rhino3d.com/guides/yak/creating-a-multi-targeted-
rhino-plugin-package/)

  * Next Steps
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Package Manager
Guides](https://developer.rhino3d.com/en/guides/yak/) /

Creating a Multi-targeted Rhino Plug-In Package

by [Callum Sykes](https://discourse.mcneel.com/u/Callumsykes/) (Last updated:
Tuesday, July 29, 2025)

The [Package Manager](https://developer.rhino3d.com/guides/yak/) was
introduced in Rhino 7. It makes it easier to discover, install and manage
Rhino plug-ins from within Rhino. This guide will describe how to create a
package from a Rhino plug-in that can be published to the package server.

__Note __

The package manager is cross-platform. The examples below are for Windows. For
Mac, replace the path to the Yak CLI tool with `"/Applications/Rhino
8.app/Contents/Resources/bin/yak"`.

First, let’s assume you have a build directory on your computer which contains
all the files that you would like to distribute in your multi-targeted
package. Something like below.

    
    
    C:\Users\Bozo\dist\
    ├───net48                            
    │   │   icon.png                     
    │   │   Tamarin.rhp                  
    │   └───misc                         
    │           License.txt              
    │           README.md                
    └───net7.0                           
        │   icon.png                     
        │   Tamarin.rhp                  
        └───misc                         
                License.txt              
                README.md                
    

__Note __

This is just an example. The only files that matter are Tamarin.rhp and
icon.png (we’ll reference the icon in the manifest.yml file later).

We’re going to use the Yak CLI tool to create the package, so open up a
Command Prompt and navigate to the directory above.

    
    
    cd C:\Users\Bozo\dist\
    

Now, we need a `manifest.yml` file! You can easily create your own by studying
the [Manifest Reference Guide](../the-package-manifest). Alternatively, you
can use the `spec` command to generate a skeleton file. We’ll do the latter
here.

    
    
    > "C:\Program Files\Rhino 8\System\Yak.exe" spec
    
    Inspecting content: Tamarin.rhp
    
    ---
    name: tamarin
    version: 1.0.0
    authors:
    - Park Ranger
    description: An example RhinoCommon plug-in
    url: https://example.com
    
    
    Saved to C:\Users\Bozo\dist\manifest.yml
    

The `spec` command takes a look at the current directory and, if present, will
glean useful information from the `.rhp` assembly and use it generate a
`manifest.yml` with name, version, description etc. pre-populated. If you
haven’t added this information, then placeholders will be used.

The RhinoCommon plug-in inspector extracts the assembly attributes that you
set when creating your plug-in. The `AssemblyInformationalVersion` attribute
is used to populate the version field, since this attribute isn’t bound to the
Microsoft four-digit version spec and can contain a SemVer-compatible version
string. The `AssemblyVersion` attribute is used as a fallback.

__Note __

The `spec` command is useful for generating the manifest.yml file initially.
Once you have one, keep it with your project and update it for each release.

Next, open the manifest file with your [favourite
editor](https://code.visualstudio.com) and fill in the gaps.

Afterwards, you should have something that looks a little like this…

    
    
    ---
    name: tamarin
    version: 1.0.0
    authors:
    - Park Ranger
    description: >
      This plug-in does something. I'm not really sure exactly what it's supposed to
      do, but it does it better than any other plug-in.  
    url: https://example.com
    icon: icon.png
    keywords:
    - something
    

Now that we have a manifest file, we can build the package!

    
    
    > "C:\Program Files\Rhino 8\System\Yak.exe" build
    
    Building package from contents of C:\Users\Bozo\dist
    
    Found manifest.yml for package: tamarin (1.0.0)
    Inspecting content: Tamarin.rhp
    Creating tamarin-1.0.0-rh8_0-any.yak
    
    ---
    name: tamarin
    version: 1.0.0
    authors:
    - Will Pearson
    description: >
      This plug-in does something. I'm not really sure exactly what it's supposed to
      do, but it does it better than any other plug-in.
    url: https://example.com
    keywords:
    - something
    - guid:c9beedb9-07ec-4974-a0a2-44670ddb17e4
    
    C:\Users\Bozo\dist\tamarin-1.0.0-rh8_0-any.yak
    ├── manifest.yml
    ├── net48/
    │   ├── Tamarin.dll
    │   ├── Tamarin.rhp
    │   ├── icon.png
    │   └── misc/
    │       ├── License.txt
    │       └── README.md
    └── net7.0/
        ├── Tamarin.dll
        ├── Tamarin.rhp
        ├── icon.png
        └── misc/
            ├── License.txt
            └── README.md
    

__Note __

The filename includes a [“distribution tag”](../the-anatomy-of-a-
package#distributions) (in this case `rh8_0-any`). The first part, `rh8_0`, is
inferred from the version of Rhinocommon.dll or Rhino C++ SDK that is
referenced in the plug-in project. The second part, `any`, refers to the
platform that the plug-in is intended for. To build a platform-specfic
package, run the `build` command again with the `--platform <platform>`
argument, where `<platform>` can be either `win` or `mac`.

__Note __

You might notice your plug-in’s GUID lurking in the keywords. More information
on how this is used can be found in the [“Package Restore in
Grasshopper”](../package-restore-in-grasshopper) guide.

Congratulations! 🙌 You’ve just created a multi-targeted package for your Rhino
plug-in.

## Next Steps

Now that you’ve created a package, [push it to the package server](../pushing-
a-package-to-the-server) to make it available in the package manager!

## Related Topics

  * [Creating a Grasshopper Plug-in Package](https://developer.rhino3d.com/guides/yak/creating-a-grasshopper-plugin-package/)
  * [RhinoCommon: Your First Plugin (Windows)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-windows/)
  * [RhinoCommon: Your First Plugin (Mac)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-mac/)
  * [Creating your first C/C++ plugin for Rhino](https://developer.rhino3d.com/guides/cpp/your-first-plugin-windows/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/yak/creating-
a-multi-targeted-rhino-plugin-package/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/yak/creating-
a-multi-targeted-rhino-plugin-package/index.md) [
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

