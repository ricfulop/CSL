---
url: https://developer.rhino3d.com/guides/cpp/what-is-the-rdk/
scraped_at: 2025-09-08T15:40:38.732569
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

[What is the RDK?](https://developer.rhino3d.com/guides/cpp/what-is-the-rdk/)

  * Overview
  * Features
  * Material, Environment and Texture Editors
  * Render Window
  * HDR and EXR Support
  * Decals
  * Sun
  * Summary

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

What is the RDK?

__

Windows only

by [Andrew Le Bihan](https://discourse.mcneel.com/u/andy/) and [John
Croudy](https://discourse.mcneel.com/u/johnc/) (Last updated: Wednesday,
January 23, 2019)

![RDK Logo](https://developer.rhino3d.com/images/rdk-what-is-the-rdk-01.png)

### Overview

The RDK is a collection of tools that extend the Rhino application platform
with visualization-specific capabilities. Third-party developers can use the
RDK SDK to integrate their renderers into Rhino.

### Features

![RDK Features Banner](https://developer.rhino3d.com/images/rdk-what-is-the-
rdk-02.png)

  * Extensible Material, Environment and Texture editors which display and edit Materials, Environments and Textures (AKA _Render Content_) and allow [operations](https://developer.rhino3d.com/guides/cpp/rdk-task-classes/) to be performed on them.
  * Render content can have tags assigned.
  * [Frame buffer](https://developer.rhino3d.com/guides/cpp/rdk-rendering-classes/) implementation with multiple channels and post-processing.
  * Pre-process custom mesh provision interface for third party developers.
  * Built-in material types, including gem, glass, plastic, plaster, metal, paint, picture and custom.
  * Built-in procedural textures, including wood, marble, granite, noise generators, perturbs, and so on.
  * Built-in HDR and OpenEXR support.
  * Improved [render pipeline](https://developer.rhino3d.com/guides/cpp/rdk-rendering-classes/) that makes it much easier for developers to implement a renderer engine in Rhino.
  * [Sun light](https://developer.rhino3d.com/guides/cpp/rdk-sun-classes/) and sun angle calculation tools.
  * [Skylight](https://developer.rhino3d.com/guides/cpp/rdk-skylight-classes/) support.
  * [Safe Frame](https://developer.rhino3d.com/guides/cpp/rdk-safe-frame-classes/) support.
  * Gamma, [Linear Workflow](https://developer.rhino3d.com/guides/cpp/rdk-linear-workflow-classes/) and [Dithering](https://developer.rhino3d.com/guides/cpp/rdk-dithering-classes/) support.
  * Automatic shader UI support for third party Material/Environment/Texture providers.
  * Several utility classes to aid in the development of renderers and visualization related tools.
  * Decal support with planar, UV, cylindrical or spherical mapping.
  * [Ground Plane](https://developer.rhino3d.com/guides/cpp/rdk-ground-plane-classes/) support with automatic height, material and texture mapping options.
  * 360 degree [environment](https://developer.rhino3d.com/guides/cpp/rdk-current-environment-classes/) preview in the viewport.
  * Extensive library of ready-to-use materials, environments and textures with Library browser.

### Material, Environment and Texture Editors

![MET editors](https://developer.rhino3d.com/images/rdk-what-is-the-
rdk-03.png) The Material, Environment, and Texture Editors display objects
called _Render Contents_ and allow the user to edit them. These editors are
all based on a similar interface with only small functional differences
between them. Render Contents are the foundation of the RDK and one of the
most important objects it provides. The RDK SDK provides an extensive system
that allows render engine developers to create their own custom render
contents. The editors then allow users to create, edit and manage these
specialized contents as well as the ones bundled with the RDK and apply them
to objects in the scene.

Main articles:

  * [Render Content](https://developer.rhino3d.com/guides/cpp/rdk-render-content/)
  * [Render Content Editors](https://developer.rhino3d.com/guides/cpp/rdk-render-content-editors/)

### Render Window

![Render Window](https://developer.rhino3d.com/images/rdk-what-is-the-
rdk-04.png)

A user thinks of the [Render
Window](https://developer.rhino3d.com/guides/cpp/rdk-rendering-classes/) as
the window that appears on the screen when one renders a model (see the
picture above). However, the render window object used by developers
corresponds more to the actual _frame buffer_. It contains information about
the channels and pixels that make up the rendered image. The standard render
window provides a number of features to renderers, including built-in support
for scripting, cloning, saving to high dynamic-range formats, post effects,
zooming and channel display.

### HDR and EXR Support

![HDR and EXR Support](https://developer.rhino3d.com/images/rdk-what-is-the-
rdk-05.png)

An HDR image which provides automatic conversion to a bitmap for non-HDR
capable renderers. This allows the Rhino renderer and viewport display to show
HDR environments while providing HDR tools to third-party renderer engines.

The HDR texture also provides projection conversion features. Most HDRi files
come as Light Probe projection. The Basic Environment requires Spherical
(Equirectangular) projection for spherical environments, so the HDR texture
defaults to this conversion. However, several other types are supported.

The LDR exposure determines the brightness of the image when converted to a
bitmap image. This will not affect the rendering when used by a HDR capable
renderer.

HDR multiplier is a simple linear multiplier on all values in the image. This
can be used to brighten or dim the image in an HDR capable renderer.

The Save As button can be used to convert the image to a bitmap file. The LDR
exposure value is used convert the image during this process.

Azimuth and Altitude values modify the way the image is rotated in space
during the projection conversion.

### Decals

![Decals](https://developer.rhino3d.com/images/rdk-what-is-the-rdk-07.png)

Decals are non-repeating textures that are applied to the surface of an object
with a given projection. They are an easy-to-use way of attaching single
images or similar textures to objects without going through the complexity of
the texture mapping process.

Decals are textures that are placed directly on a specified area of one or
more objects. They consist of a single instance of a texture, rather than
being tiled as they are when used in a material. Users use decals to modify a
limited part of an object’s color.

![Decals2](https://developer.rhino3d.com/images/rdk-what-is-the-rdk-08.jpg)

The following classes can be used to access decal features:

  * [IRhRdkDecal](https://developer.rhino3d.com/guides/cpp/rdk-decal-classes/#IRhRdkDecal)
  * [CRhRdkObjectDataAccess](https://developer.rhino3d.com/guides/cpp/rdk-decal-classes/#CRhRdkObjectDataAccess)

### Sun

![Sun](https://developer.rhino3d.com/images/rdk-what-is-the-rdk-06.png)

The RDK provides easy-to-use sun tools, including a docking panel to control
the [document sun](https://developer.rhino3d.com/guides/cpp/rdk-sun-
classes/#DocumentSun), a sunlight preview within the Rendered viewport, a
Sunlight command and a number of other scripting and developer tools to make
sun-angle calculations easy.

The following classes can be used to access sun features:

  * [IRhRdkSun](https://developer.rhino3d.com/guides/cpp/rdk-sun-classes/#IRhRdkSun)
  * [CRhRdkSun](https://developer.rhino3d.com/guides/cpp/rdk-sun-classes/#CRhRdkSun)
  * [CRhRdkSunDialog](https://developer.rhino3d.com/guides/cpp/rdk-sun-classes/#CRhRdkSunDialog)

### Summary

This article introduced the RDK and described some of its main features. Each
feature is explained in more detail in a different article.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/what-
is-the-rdk/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/what-
is-the-rdk/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

