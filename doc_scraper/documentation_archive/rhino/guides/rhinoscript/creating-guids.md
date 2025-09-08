---
url: https://developer.rhino3d.com/guides/rhinoscript/creating-guids/
scraped_at: 2025-09-08T15:42:15.127988
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

[Creating GUIDs](https://developer.rhino3d.com/guides/rhinoscript/creating-
guids/)

  * Overview
  * GUID Generation
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Creating GUIDs

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

[Globally Unique
Identifiers](https://en.wikipedia.org/wiki/Globally_unique_identifier) \- or
GUIDs - are unique identification numbers that are used to track items. Rhino
uses GUIDs just for this purpose. GUIDs come in different formats, but are
usually stored as 128-bit values, and are commonly displayed as 32 hexadecimal
digits with groups separated by hyphens:

`{3AEC4721-34KP-3152-B2BB-17442C41208P}`

Let’s write a script that creates GUIDs…

## GUID Generation

There is actually a very easy way to generate GUIDs. The `Scriptlet.TypeLib`
object includes a method that generates GUIDs. If you need a GUID, here is a
short script that will supply you with one:

    
    
    ' Creates a Registry-formatted GUID string
    ' Ex: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
    Function CreateGuidRegistryFormat
      Dim objTypeLib
      Set objTypeLib = CreateObject("Scriptlet.TypeLib")
      CreateGuidRegistryFormat = Left(objTypeLib.Guid, 38)
    End Function
    

If you want to create a plain GUID - one without the surrounding curly
brackets, then you can do something like this:

    
    
    ' Creates a plain-formatted GUID string
    ' Ex: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    Function CreateGuidPlainFormat
      Dim objTypeLib
      Set objTypeLib = CreateObject("Scriptlet.TypeLib")
      CreateGuidPlainFormat = Mid(objTypeLib.Guid, 2, 36)
    End Function
    

## Related Topics

  * [Globally Unique Identifier (Wikipedia)](https://en.wikipedia.org/wiki/Globally_unique_identifier)
  * [Converting GUIDs to Strings](https://developer.rhino3d.com/guides/rhinoscript/converting-guids-to-strings/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/creating-
guids/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/creating-
guids/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

