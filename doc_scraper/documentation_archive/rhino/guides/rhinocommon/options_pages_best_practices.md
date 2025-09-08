---
url: https://developer.rhino3d.com/guides/rhinocommon/options_pages_best_practices/#applying-changes
scraped_at: 2025-09-08T16:09:24.395175
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

[Options Pages Best
Practices](https://developer.rhino3d.com/guides/rhinocommon/options_pages_best_practices/)

  * Overview
  * Details

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Options Pages Best Practices

by [John Morse](https://discourse.mcneel.com/u/johnm/) (Last updated:
Wednesday, December 5, 2018)

## Overview

One of the things your plug-in may want to do is add options or document
property settings pages to Rhino. You can add pages by overriding the
[PlugIn.OptionsDialogPages](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_PlugIns_PlugIn_OptionsDialogPages.htm)
and/or
[PlugIn.DocumentPropertiesDialogPages](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_PlugIns_PlugIn_DocumentPropertiesDialogPages.htm)
methods and adding a custom
[OptionsDialogPage](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_UI_OptionsDialogPage.htm)
to the provided page list.

You can create options pages in a plug-in using WinForms(Windows), WPF
(Windows) or Eto (Windows and Mac).

You can find samples that demonstrate how to create options pages in the
[Developer Samples repository](https://github.com/mcneel/rhino-developer-
samples) on GitHub.

## Details

When writing options pages, it is important to remember that the page should
initialize its content when activated, apply its changes when notified and
optionally provide cancel support.

#### Content Initialization

The
[OnActivate](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnActivate.htm)
method is called with `active == true` when becoming the current, visible page
which is the appropriate time to update the page contents.

#### Applying Changes

It is up to the page author to decide when to apply user changes to the
document or runtime environment. If you wish to see the document or Rhino
update while making changes, you may apply the changes in real time. It is
important to save the original settings prior to making changes if your
options page is going to support the cancel mechanism. Typically changes
should be queued up and made in the
[OnApply](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnApply.htm)
override, canceling should be performed in the
[OnCancel](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnCancel.htm)
override.

#### Rhino for Windows Behavior

Rhino for Windows contains a single Options/Document Properties dialog box
which can be displayed using the Options or DocumentProperties Rhino commands.
This dialog box is modal in nature and will call the
[PlugIn.OptionsDialogPages](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_PlugIns_PlugIn_OptionsDialogPages.htm)
and
[PlugIn.DocumentPropertiesDialogPages](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_PlugIns_PlugIn_DocumentPropertiesDialogPages.htm)
methods each time it is displayed. It creates the
[PageControl](https://developer.rhino3d.com/api/RhinoCommon/html/P_Rhino_UI_StackedDialogPage_PageControl.htm)
the first time the page is made current. If your page is never made current,
the page control is never created. Rhino will call
[OnActivate](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnActivate.htm)
with `active == true` when a page becomes the active page. When a page is no
longer active, the
[OnActivate](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnActivate.htm)
method is called with `active == false` followed by a call to
[OnApply](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnApply.htm).
If the Rhino Options/Document Properties dialog is closed by cancelling, then
[OnCancel](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnCancel.htm)
is called for any page displayed while the modal dialog was visible.

#### Rhino for Mac Behavior

Rhino for Mac contains File/Settings (Document Properties) and
Rhinoceros/Preferences (Options) modeless windows. The main things to consider
here are the host windows are modeless and cancel is never called. Since the
host winows are independent you will get slightly different behavior for
Preferences (Options) panels than you will with File/Settings (Document
Properties) panels.

##### Preferences Window (Options)

The Preferences window will call
[PlugIn.OptionsDialogPages](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_PlugIns_PlugIn_OptionsDialogPages.htm)
the first time the window is displayed and will never call it again. The
Preferences window is never really closed; it is only hidden or shown. The
following is a description of the methods called and when they are called:

  * [PageControl](https://developer.rhino3d.com/api/RhinoCommon/html/P_Rhino_UI_StackedDialogPage_PageControl.htm) is referenced the first time the page is displayed and should return the one and only options page control.
  * [OnActivate](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnActivate.htm) with `active == true` is called when: 
    * A page becomes the active page.
    * The Options window becomes the active window and a page is active.
  * [OnActivate](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnActivate.htm) with `active == false` is called when: 
    * The active page changes and a page is no longer the active page.
    * The Options window is deactivated or hidden and a page is the active page.
  * [OnApply](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnApply.htm) is called on the active page when: 
    * The active page changes and a page is no longer the active page.
    * The Options window is deactivated or hidden and a page is the active page.

##### File Settings Window (Document Properties)

The File Settings window will call
[PlugIn.DocumentPropertiesDialogPages](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_PlugIns_PlugIn_DocumentPropertiesDialogPages.htm)
the first time the window is displayed and each time a new document is
created. The Settings window keeps a list of pages associated with each open
document and displays the active page assocated with the current document. The
Settings window is never really closed; it is only hidden or shown. The
following is a description of the methods called and when they are called:

  * [PageControl](https://developer.rhino3d.com/api/RhinoCommon/html/P_Rhino_UI_StackedDialogPage_PageControl.htm) is referenced the first time the page is displayed for a given document instance and should return the settings page control. It will also get called when a new document is opened or created and a page is the active page.
  * [OnActivate](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnActivate.htm) with `active == true` is called when: 
    * A page becomes the active page.
    * The Settings window becomes the active window and a page is active.
  * [OnActivate](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnActivate.htm) with `active == false` is called when: 
    * The active page changes and a page is no longer the active page.
    * The Settings window is deactivated or hidden and a page is the active page.
  * [OnApply](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_UI_StackedDialogPage_OnApply.htm) is called on the active page when: 
    * The active page changes and a page is no longer the active page.
    * The Settings window is deactivated or hidden and a page is the active page.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/options_pages_best_practices/index.md)
[
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/options_pages_best_practices/index.md)
[ Admin](https://developer.rhino3d.com/admin)

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

