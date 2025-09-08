---
url: https://developer.rhino3d.com/guides/cpp/rdk-render-content-editors/
scraped_at: 2025-09-08T15:40:43.738507
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

[RDK Render Content Editors](https://developer.rhino3d.com/guides/cpp/rdk-
render-content-editors/)

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

RDK Render Content Editors

__

Windows only

by [John Croudy](https://discourse.mcneel.com/u/johnc/) (Last updated:
Tuesday, January 22, 2019)

The _RDK Render Content Editors_ display objects called _Render Contents_ and
allow the user to edit them. These editors are all based on a similar
interface with only small functional differences between them. Render Contents
are the foundation of the RDK core and one of the most important objects it
provides. Please see [Render
Content](https://developer.rhino3d.com/guides/cpp/rdk-render-content/) for
more information. The Texture Editor is known to users as the Texture
_Palette_ but programmatically it is an editor just like the other two.

![Material Environment and Texture
Editors](https://developer.rhino3d.com/images/rdk-met-editors.png)

  1. Navigation controls similar to those found on a web browser.
  2. Resizeable Floating Previews.
  3. Configurable thumbnails with multiple sizes and styles.
  4. Resizeable preview pane.
  5. User interface for editing render content parameters (AKA _fields_).
  6. Breadcrumb navigation control similar to those found on file explorers.
  7. [Task](https://developer.rhino3d.com/guides/cpp/rdk-task-classes/) menu for performing actions on render contents and setting editor options.

These editors are integrated with Rhino’s tabbed pane system. You can access
them through the Rhino Render menu, the Rendering tool bar, or the editor
commands.

Lists of materials, environments, and textures are stored in the Rhino
document. Each editor displays the relevant render content type as preview
thumbnails.

Contents display an interface below the preview thumbnails in an area reserved
for collapsible UI panels. An addition to the basic UI panels, several
additional collapsible panels are provided by Rhino within the same area as
the content UI. These include the Name, Notes, Texture Summary, Local Mapping,
Graph and Adjustment panels.

Each material, environment or texture can have child nodes (AKA _child slots_
or _sub-nodes_). The children can be of any content type, but specific child
slots will only support specific types. The most common child type is a
texture. For example, the _Color_ child slot for a Custom Material will only
support textures, as will the _Background image_ child slot on a Basic
Environment.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/rdk-
render-content-editors/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/rdk-
render-content-editors/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

