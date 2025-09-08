---
url: https://developer.rhino3d.com/guides/cpp/modifying-an-objects-color/
scraped_at: 2025-09-08T15:39:06.476200
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

[Modify an Object's Color](https://developer.rhino3d.com/guides/cpp/modifying-
an-objects-color/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Modify an Object's Color

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The color used to display an object is specified in one of four ways…

  1. `ON::color_from_layer` \- the object’s layer color, `ON_Layer::Color()`, determines the object’s color. This is the default method used when adding new objects to Rhino
  2. `ON::color_from_object` \- the value of an object’s `m_color` attribute determines the object’s color.
  3. `ON::color_from_material` \- the diffuse color of the object’s render material determines the object’s color.
  4. `ON::color_from_parent` \- if the object is part of an instance reference, the color is taken from the instance

## Sample

The following code sample demonstrates how to override the default “color by
layer” behavior and set an object to use “color by object.”

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select object" );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      const CRhinoObjRef& obj_ref = go.Object( 0 );
      const CRhinoObject* obj = obj_ref.Object();
      if( !obj )
        return CRhinoCommand::failure;
    
      ON_Color old_color = obj->Attributes().DrawColor();
      ON::object_color_source color_source = obj->Attributes().ColorSource();
      ON_Color new_color( old_color );
    
      if( !RhinoColorDialog( ::RhinoApp().MainWnd(), new_color) )
        return CRhinoCommand::cancel;
    
      if( new_color == old_color )
        return CRhinoCommand::nothing;
    
      CRhinoObjectAttributes att( obj->Attributes() );
      att.m_color = new_color;
      att.SetColorSource( ON::color_from_object );
      context.m_doc.ModifyObjectAttributes( obj_ref, att );
      context.m_doc.Redraw();
      return CRhinoCommand::success;
    }
    

When adding new objects using the C/C++ SDK, you can specify the attributes of
the object when adding it to Rhino. Thus, if you want to override the default
color behavior for new objects, just get a copy of the active document’s
default new object attributes, modify it in whatever way you want, and pass it
(along with the geometry) to the appropriate object creation function…

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      ON_Circle circle;
      circle.Create( RhinoActiveCPlane(), 5.0 );
      ON_3dmObjectAttributes att;
      context.m_doc.GetDefaultObjectAttributes( att );
    
      att.m_color = RGB(255,191,191);
      att.SetColorSource( ON::color_from_object );
      context.m_doc.AddCurveObject( circle, &att );
      context.m_doc.Redraw();
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/modifying-
an-objects-color/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/modifying-
an-objects-color/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

