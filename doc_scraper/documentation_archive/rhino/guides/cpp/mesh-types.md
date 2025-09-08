---
url: https://developer.rhino3d.com/guides/cpp/mesh-types/
scraped_at: 2025-09-08T15:39:05.454646
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

[Mesh Types](https://developer.rhino3d.com/guides/cpp/mesh-types/)

  * Which Mesh?
  * Discussion

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Mesh Types

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Which Mesh?

There is an `ON_Brep::GetMeshes()` routine of the C/C++ SDK. You might find
that very adequate meshes can be pulled from this routine when specifying
`ON::render_mesh`. You may have also noticed that you can also run this
routine with an enumeration for an “analysis mesh,” a “default mesh,” a
“preview mesh,” or “any mesh.”

What are the differences between all of these options?

## Discussion

Here is an overview of the mesh types:

  1. `ON::render_mesh` is a mesh for, obviously, rendering. This rendering can be for shaded or rendered display. It can also be used by rendering plugins. The quality of these meshes is controlled by the Meshes page in the Document Properties dialog, but can also be overridden on a per-object basis.
  2. `ON::analysis_mesh` is used by analysis modes, such as curvature, draft angle, environment map, and zebra.
  3. `ON::preview_mesh` is used when you use the Mesh command and poke the preview button - the pipeline needs a way to display preview meshes and this is it.
  4. `ON::default` mesh returns `ON::render_mesh` if it exists. Otherwise it returns `ON::analysis_mesh` if it exists.
  5. `ON::any_mesh` is only used when we want delete all meshes at one time.

**NOTE** : render and analysis meshes do not appear automatically. Some
command must trigger their creation, whether its just setting viewport for
rendered display or running an analysis command. The can also be generated
from plugins that call SDK functions.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/mesh-
types/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/mesh-
types/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

