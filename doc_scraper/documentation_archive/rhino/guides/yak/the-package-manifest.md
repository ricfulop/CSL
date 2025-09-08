---
url: https://developer.rhino3d.com/guides/yak/the-package-manifest
scraped_at: 2025-09-08T16:07:18.008373
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

[The Package Manifest](https://developer.rhino3d.com/guides/yak/the-package-
manifest/)

  * Overview
  * Example
  * Required Attributes
    * Name
    * Version
    * Authors
    * Description
  * Recommended Attributes
    * URL
    * Keywords
    * Icon
  * Obsolete Attributes
    * Icon URL
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Package Manager
Guides](https://developer.rhino3d.com/en/guides/yak/) /

The Package Manifest

by [Will Pearson](https://discourse.mcneel.com/u/will/) (Last updated:
Wednesday, July 21, 2021)

## Overview

Each package should have a manifest file containing a spec that can be
distilled into the database when the package is pushed to the server. The
manifest should be written in [YAML](http://www.yaml.org), following the
structure of the example below.

The manifest file should be named `manifest.yml` and should live in the root
of the package. (Don’t worry, the Yak CLI tool’s [`build`
command](https://developer.rhino3d.com/guides/yak/yak-cli-reference/#build)
takes care of this for you!)

The manifest’s purpose is to help with streamlining (and potentially
automating) the process of releasing packages, removing the need for any web
forms when publishing packages.

**Required Attributes**

  * [Name](https://developer.rhino3d.com/guides/yak/the-package-manifest/#name)
  * [Version](https://developer.rhino3d.com/guides/yak/the-package-manifest/#version)
  * [Authors](https://developer.rhino3d.com/guides/yak/the-package-manifest/#authors)
  * [Description](https://developer.rhino3d.com/guides/yak/the-package-manifest/#description)

**Recommended Attributes**

  * [URL](https://developer.rhino3d.com/guides/yak/the-package-manifest/#url)
  * [Keywords](https://developer.rhino3d.com/guides/yak/the-package-manifest/#keywords)
  * [Icon](https://developer.rhino3d.com/guides/yak/the-package-manifest/#icon)

## Example

Here’s an example for a Grasshopper plug-in.

    
    
    name: plankton
    version: 0.3.4
    authors:
      - Daniel Piker
      - Will Pearson
    description: >
      Plankton is a flexible and efficient library for handling n-gonal meshes.
      Plankton is written in C# and implements the halfedge data structure. The
      structure of the library is loosely based on Rhinocommon's mesh classes and
      was originally created for use within C#/VB scripting components in
      Grasshopper.  
    url: "https://github.com/meshmash/Plankton"
    

## Required Attributes

### Name

The short name describing the package. Preferably one world although multiple
words can be separated by underscores or hyphens.

_**Note:** Package name can only include letters, numbers, dashes, and
underscores_

_**Note 2:** Package names adopt the case used in the very first version that
was uploaded. Future uploads ignore the case of the package name and all
queries are case-insensitive._

    
    
    name: plankton
    

### Version

_Since 0.8: four-digit version numbers allowed_ _Since 0.9:`$version`
placeholder_

The version number given to the package.

Package version numbers **must** either follow [Semantic Versioning
2.0.0](http://semver.org/spec/v2.0.0.html) (e.g. `1.1.0-beta`) or
`System.Version` a.k.a. Microsoft’s four-digit standard (e.g. `1.2.3.4`). It’s
recommended to use Semantic Versioning because it allows package authors to
specify prerelease versions. These are handy for limited testing, since by
default the latest _stable_ version is installed.

To make the authoring process easier, it’s possible to replace the version
number with `$version` – the version number will be inferred from the contents
of the package and substituted during `yak build`.

    
    
    version: 0.3.4
    

### Authors

A list of author(s) of the package.

    
    
    authors:
      - Daniel Piker
      # list additional package authors below
      - Will Pearson
    

### Description

Describe the package. Be as in-depth or as brief as you feel is appropriate.

    
    
    description: This is an awesome package.
    

If you want to write more, you can use use YAML’s [folded
style](http://www.yaml.org/spec/1.2/spec.html#id2796251).

    
    
    description: >
      This is such an awesome package
      that I'm going to write a whole
      bunch of text describing it!
    
      This sentence will be on a new line.  
    

## Recommended Attributes

### URL

A webpage for the package. This can be any URL i.e. author contact info,
forums, tutorials or any other information about the plugin.

    
    
    url: "https://github.com/meshmash/Plankton"
    

### Keywords

A list of keywords that will help users to find the package.

    
    
    keywords:
    - one
    - two
    

### Icon

An icon file in the package. It should be small (e.g. 64x64) and it must be
either a PNG or a JPEG.

    
    
    icon: icon.png
    

## Obsolete Attributes

### Icon URL

__Warning __

⚠️ Replaced by the icon attribute.

Specify a **direct** link to an icon that will be used by the Package Manager
in Rhino. It should be small (32x32 is ideal) and it must be either a PNG or a
JPEG.

    
    
    icon_url: "https://example.com/path/to/icon.png"
    

## Related Topics

  * [Yak Guides and Tutorials](https://developer.rhino3d.com/guides/yak/)
  * [Anatomy of a Package](https://developer.rhino3d.com/guides/yak/the-anatomy-of-a-package/)
  * [Yak CLI Reference](https://developer.rhino3d.com/guides/yak/yak-cli-reference/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/yak/the-
package-manifest/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/yak/the-
package-manifest/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

