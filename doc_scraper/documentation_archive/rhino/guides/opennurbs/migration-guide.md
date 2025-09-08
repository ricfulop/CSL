---
url: https://developer.rhino3d.com/guides/opennurbs/migration-guide/
scraped_at: 2025-09-08T15:38:09.236046
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

[What's New and Update
Guide](https://developer.rhino3d.com/guides/opennurbs/migration-guide/)

  * Overview
  * Updating
  * openNURBS 8
  * openNURBS 7
  * openNURBS 6

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

What's New and Update Guide

by [Dale Lear](https://discourse.mcneel.com/u/dalelear/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The openNURBS toolkit reads and writes Rhino 3DM files.

To get the current openNURBS toolkit or technical support, visit
[openNURBS](https://www.rhino3d.com/opennurbs).

## Updating

For most developers, updating from the previous verson of openNURBS will
involve recompiling and minor changes. As before, the easiest way to read a
3DM file is to use one of the `ONX_Model::Read()` functions. The easiest way
to write a 3DM file is to use one of the `ONX_Model::Write()` functions.

## openNURBS 8

OpenNURBS and Rhino3dm now provide direct access to rendering information in
the absence of Rhino. Prior to this, the only way to access this information
outside of Rhino was by getting the data as XML and parsing it.

The following new objects are provided:

**openNURBS** | **Rhino3dm** | **Description**  
---|---|---  
`ON_RenderContent` | `File3dmRenderContent` | Provides access to generic render content settings.  
`ON_RenderMaterial` | `File3dmRenderMaterial` | Provides access to settings specific to render materials.  
`ON_RenderEnvironment` | `File3dmRenderEnvironment` | Provides access to settings specific to render environments.  
`ON_RenderTexture` | `File3dmRenderTexture` | Provides access to settings specific to render textures.  
`ON_Decals` | `Render.Decals` | Provides access to a collection of decals stored on object attributes.  
`ON_Decal` | `Render.Decal` | Provides access to settings for an individual decal in the collection.  
`ON_Dithering` | `Render.Dithering` | Provides access to dithering settings.  
`ON_EmbeddedFile` | `File3dmEmbeddedFile` | Provides access to embedded texture files.  
`ON_GroundPlane` | `Render.GroundPlane` | Provides access to ground plane settings.  
`ON_LinearWorkflow` | `Render.LinearWorkflow` | Provides access to gamma and linear workflow settings.  
`ON_RenderChannels` | `Render.RenderChannels` | Provides access to render channels settings.  
`ON_SafeFrame` | `Render.SafeFrame` | Provides access to safe frame settings.  
`ON_Skylight` | `Render.Skylight` | Provides access to skylighting settings.  
`ON_Sun` | `Render.Sun` | Provides access to sun settings and sun position calculations.  
`ON_PostEffects` | `Render.PostEffects.PostEffectCollection` | Provides access to the list of post effects.  
`ON_PostEffect` | `Render.PostEffects.PostEffectData` | Provides access to settings for an individual post effect in the list.  
  
## openNURBS 7

A new subdivision surface object has been added to Rhino 7. The core geometry
component is `ON_SubD` class, which is also part of openNURBS. All subdivision
code will be available in the Rhino plug-in SDK.

The `ON_SubD` class has full support for Catmull-Clark quad subdivision
surfaces and for Loop-Warren triangle subdivision surfaces. The Rhino
subdivision surface control polygons have no limits on vertex valences (edge
and face counts) or facet edge counts.

Rhino subdivision objects are automatically converted to cubic NURBS
polysurfaces or meshes when a subdivision object is selected as input to a
command that is expecting a polysurface or mesh. This is how Rhino’s
lightweight extrusion object behaves.

## openNURBS 6

To build openNURBS 6, use a C++ compiler that supports C++11. Both Microsoft’s
Visual Studio 2017 and Apple’s XCode 9 support C++11.

Use iterators to go through the contents of an `ONX_Model`. For an example,
look at the source code for `ONX_Model::DumpComponentList()` in
_opennurbs_extensions.cpp_.

`ON_ComponentManifest` is a manifest of every component in a model or 3DM
file. It provides simple ways fo find components by id or name. The function
`ONX_Model.Manifest()` returns the manifest of the `ONX_Model`. When merging
models, `ON_ManifestMap` can be used to efficiently manage name and id
collisions.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/migration-
guide/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/migration-
guide/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

