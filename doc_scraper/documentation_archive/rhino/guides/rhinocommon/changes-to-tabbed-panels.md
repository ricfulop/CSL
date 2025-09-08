---
url: https://developer.rhino3d.com/guides/rhinocommon/changes-to-tabbed-panels/#rhino-6-for-mac-behavior
scraped_at: 2025-09-08T16:09:10.198803
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

[Changes to Tabbed
Panels](https://developer.rhino3d.com/guides/rhinocommon/changes-to-tabbed-
panels/)

  * Overview
  * Details
  * More Information

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Changes to Tabbed Panels

by [John Morse](https://discourse.mcneel.com/u/johnm/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Many Rhino controls are contained in tabbed, dockable panels.

You can create tabbed panels in a plug-in using WinForms(Windows), WPF
(Windows) or Eto (Windows and Mac).

You can find a sample that demonstrate how to create tabbed panels in the
[Developer Samples repository](https://github.com/mcneel/rhino-developer-
samples) on GitHub.

## Details

The tabbed panel systems work differently in Rhino 6 than it did in Rhino 5.

#### Rhino 5 for Windows Behavior

  * The [registered](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_Panels_RegisterPanel.htm) panel class must be a `public` class and contain a default constructor that takes no parameters.
  * A panel instance is created the first time it is referenced by a visible host container and will survive for the length of a Rhino session.
  * When a panel is moved to a different host container, the panels parent is changed to the new host and the same panel instance is used.

#### Rhino 6 for Windows Behavior (Per-Document Panels)

  * The [registered](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_Panels_RegisterPanel_1.htm) panel class must be a `public` class and registered as a `PanelType.PerDoc` panel (the default [PanelType](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_UI_PanelType.htm)).
  * Rhino looks for public constructors in the following order: 
    * Constructor taking a `RhinoDoc`.
    * Constructor taking a `uint` representing the documents runtime serial number.
    * Constructor with no arguments.
  * A panel instance is created each time a new document is created, if the panel is in a visible host container, and disposed of when the document closes.
  * When a panel is moved to a different host container, the panels parent is changed to the new host and the same panel instance is used.

#### Rhino 6 for Windows Behavior (System Panels)

  * The [registered](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_Panels_RegisterPanel_1.htm) panel class must be a `public` class and registered as a `PanelType.System` panel.
  * Rhino looks for public constructors in the following order: 
    * Constructor taking a `RhinoDoc`.
    * Constructor taking a `uint` representing the documents runtime serial number.
    * Constructor with no arguments.
  * A panel instance is created the first time it is referenced by a visible host container and will survive for the length of a Rhino session.
  * When a panel is moved to a different host container, the panels parent is changed to the new host and the same panel instance is used.

#### Rhino 6 for Mac Behavior

Rhino for Mac works the same as Rhino for Windows, with the exception that
there will be a panel instance per inspector panel that includes the plug-in
panel.

## More Information

Rhino 6 includes a
[IPanel](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_UI_IPanel.htm)
interface which can be implemented to determine when a panel is shown, hidden
or closed.

Static events on `RhinoDoc` should be hooked by your panel class when created
and unhooked when disposed of in both Rhino 5 and Rhino 6.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/changes-
to-tabbed-panels/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/changes-
to-tabbed-panels/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

