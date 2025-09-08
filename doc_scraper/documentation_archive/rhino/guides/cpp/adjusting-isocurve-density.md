---
url: https://developer.rhino3d.com/guides/cpp/adjusting-isocurve-density/
scraped_at: 2025-09-08T15:38:42.360242
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

[Adjusting Isocurve
Density](https://developer.rhino3d.com/guides/cpp/adjusting-isocurve-density/)

  * Problem
  * Solution
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Adjusting Isocurve Density

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

When creating a new surface from a selected curve, it is always a single
isocurve crossing the surface. One has to adjust isocurve density after the
fact from Rhino’s Properties window. It is possible to do this automatically
from a plugin?

## Solution

The isocurve density for surface object is stored on the object’s attributes.
For C/C++ plugins, this would be the `CRhinoObjectAttributes` and
`ON_3dmObjectAttributes` classes. Just set the `m_wire_density` property.
Note: setting this property to zero (0) will disable the display of isocurves
for that object.

## Example

    
    
    CRhinoCommand::result CCommandFooBar::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetGeometryFilter( CRhinoGetObject::surface_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() == CRhinoCommand::success )
      {
        const CRhinoObjRef& objref = go.Object(0);
        const CRhinoBrepObject* brep_obj = CRhinoBrepObject::Cast( objref.Object() );
        if( brep_obj )
        {
          CRhinoObjectAttributes atts = brep_obj->Attributes();
          atts.m_wire_density = 3; // for example
          context.m_doc.ModifyObjectAttributes( objref, atts );
          context.m_doc.Redraw();
        }
      }
    
      return go.CommandResult();
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/adjusting-
isocurve-density/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/adjusting-
isocurve-density/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

