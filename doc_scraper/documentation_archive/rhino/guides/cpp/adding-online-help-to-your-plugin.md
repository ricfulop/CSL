---
url: https://developer.rhino3d.com/guides/cpp/adding-online-help-to-your-plugin/
scraped_at: 2025-09-08T15:39:30.541566
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

[Adding Online Help to Your
Plugin](https://developer.rhino3d.com/guides/cpp/adding-online-help-to-your-
plugin/)

  * Overview
  * Authoring Tools
  * Plugin Support
  * Command Support
  * Dialog Support
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Adding Online Help to Your Plugin

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Once you have your Rhino plugin completed, you may want to add online help
support to help your customers use your plugin efficiently and properly. Most
Windows applications provide online help in the form of an HTML help file.

## Authoring Tools

HTML help files are made with help authoring tools.

Microsoft provides a free utility called the [HTML Help
Workshop](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=00535334-c8a6-452f-9aa0-d597d16580cc)
that can compile existing HTML files into an HTML help file (.chm). This is a
fairly low-level utility in that it will only build HTML help files - it will
not create or edit content. Thus, most who are looking to produce online help
are looking for something a bit more full featured.

MadCap make a popular help authoring tool called [MadCap
Flare](http://www.madcapsoftware.com/products/flare/) that will help you
create, edit, and publish professional quality topic based technical content.
This is the tool used to create the help files for Rhino.

There are several other tools available on the market. Google “Create HTML
Help File” to see the list.

## Plugin Support

You can add your plugin to Rhino’s _Help_ > _Plug-ins_ menu by overriding the
following two virtual functions:

  1. `CRhinoPlugIn::AddToPlugInHelpMenu`: Called by Rhino to determine if the plugin name should be added to the Rhino _Help_ > _Plug-ins_ menu.
  2. `CRhinoPlugIn::OnDisplayPlugInHelp`: Called by Rhino if `CRhinoPlugIn::AddToPlugInHelpMenu` returns true and the menu item associated with this plugin is selected.

Details on both of these virtual function can be found in _rhinoSdkPlugIn.h_.

## Command Support

While running a Rhino command, you can press `F1` to bring up online help for
that command. Your plugin commands can do the same. Simply override the
`CRhinoCommand::DoHelp` virtual function. If your command is running when the
user presses `F1`, this member will be called.

Also, if your want your command’s help to appear in Rhino’s command help
dockable window (_Help_ > _Command Help_), then override the
`CRhinoCommand::ContextHelpURL` virtual function.

Details on both of these virtual function can be found in _rhinoSdkCommand.h_.

## Dialog Support

There are a couple of ways you can add help support to dialog boxes. The first
is to simply place a “Help” button somewhere on the form.

Also, if your dialog box has focus and the user presses `F1`, Windows will
send a WM_HELPINFO message to it. So, by adding a message handler to your
dialog box, you can capture these notifications and display the requested
information.

And, if you add the “Context Help” style to your dialog box resource, a ? icon
will appear in the upper right corner of the window. Now, if the user clicks
the ? icon and then clicks a control, your dialog’s `OnHelpInfo`
implementation will and passed information about the control that was clicked.

MSDN had lots of information on how to add context help to dialog boxes.

## Related Topics

  * [HTML Help Workshop (on Microsoft.com)](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=00535334-c8a6-452f-9aa0-d597d16580cc)
  * [MadCap Flare](http://www.madcapsoftware.com/products/flare/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/adding-
online-help-to-your-plugin/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/adding-
online-help-to-your-plugin/index.md) [
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

