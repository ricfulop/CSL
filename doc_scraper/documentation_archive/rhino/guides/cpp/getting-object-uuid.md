---
url: https://developer.rhino3d.com/guides/cpp/getting-object-uuid/
scraped_at: 2025-09-08T15:39:01.327263
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

[Getting Object UUIDs](https://developer.rhino3d.com/guides/cpp/getting-
object-uuid/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Getting Object UUIDs

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
October 7, 2024)

## Overview

Rhino can create and manipulate many geometric objects, including points,
point clouds, curves, surfaces, Breps, extrusions, subds, meshes, lights,
annotations and more.

A universally unique identifier, or
[UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier), is
assigned to each object in the Rhino document when the objects are created.
The object’s UUID uniquely identifies the object.

Because UUIDs are saved in the 3DM file, an object’s unique identifier will
persist between editing sessions.

## Sample

The following code sample demonstrates how to obtain an object’s unique
identifier, or UUID, using C/C++:

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoGetObject go;
      go.SetCommandPrompt(L"Select object");
      go.GetObjects(1, 1);
      if (go.CommandResult() != CRhinoCommand::success)
        return go.CommandResult();
    
      const CRhinoObjRef& ref = go.Object(0);
      const CRhinoObject* obj = ref.Object();
      if (nullptr == obj)
        return CRhinoCommand::failure;
    
      ON_UUID uuid = obj->ModelObjectId();
      ON_wString str;
      ON_UuidToString(uuid, str);
      RhinoApp().Print(L"The object's unique identifier is \"%s\".\n", str);
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/getting-
object-uuid/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/getting-
object-uuid/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

