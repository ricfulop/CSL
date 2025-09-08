---
url: https://developer.rhino3d.com/guides/cpp/picking-brep-components/
scraped_at: 2025-09-08T15:39:11.496825
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

[Picking Brep Components](https://developer.rhino3d.com/guides/cpp/picking-
brep-components/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Picking Brep Components

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to pick a brep component (e.g. face or edge) and then take
action depending on what was picked. If you write an object picker as such:

    
    
    CRhinoGetObject go;
    go.SetCommandPrompt( L"Select face or edge" );
    go.SetGeometryFilter( CRhinoGetObject::surface_object |
    CRhinoGetObject::edge_object );
    go.EnableSubObjectSelect( true );
    go.GetObjects( 1, 1 );
    

and then use it to try to pick the edge of a box, for example, only the faces
show up on the “choose one object” menu.

## Solution

You need to enable “choose one question” to get multiple subobject types on
one brep to work. So, this should work:

    
    
    CRhinoGetObject go;
    go.SetCommandPrompt( L"Select face or edge" );
    go.SetGeometryFilter( CRhinoGetObject::surface_object |
    CRhinoGetObject::edge_object );
    go.EnableSubObjectSelect( true );
    go.EnableChooseOneQuestion( true ); // ADD THIS...
    go.GetObjects( 1, 1 );
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/picking-
brep-components/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/picking-
brep-components/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

