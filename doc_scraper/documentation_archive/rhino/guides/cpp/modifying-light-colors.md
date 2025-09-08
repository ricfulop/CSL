---
url: https://developer.rhino3d.com/guides/cpp/modifying-light-colors/
scraped_at: 2025-09-08T15:39:07.503941
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

[Modifying a Light's
Color](https://developer.rhino3d.com/guides/cpp/modifying-light-colors/)

  * Overview
  * How To
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Modifying a Light's Color

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The process for modifying a light object is slightly different than the
process for modifying other geometric objects, such as points, curves, and
surfaces. This is because light objects are stored in a different location in
the Rhino document.

## How To

Light objects are stored in a `CRhinoLightTable` object that is held by the
active document object. Thus, instead of using one of the `ModifyObject()`
members found on `CRhinoDoc`, you need to use the `ModifyLight()` member found
on `CRhinoLightTable` in order to modify an existing light object.

For more details on `CRhinoLight` and `CRhinoLightTable`, see
_rhinoSdkLight.h_ included with the C/C++ SDK.

## Sample

The following example demonstrates how to modify the diffuse color of a light
object…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Pick an existing light object
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select light to change color" );
      go.SetGeometryFilter( CRhinoGetObject::light_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      // The the light object
      CRhinoObjRef& ref = go.Object(0);
      const CRhinoLight* light_obj = CRhinoLight::Cast( ref.Object() );
      if( !light_obj )
        return CRhinoCommand::failure;
    
      // Prompt the user to pick a new color
      ON_Color color = light_obj->Light().Diffuse();
      if( !RhinoColorDialog(RhinoApp().MainWnd(), color) )
        CRhinoCommand::cancel;
    
      // Copy the light object's underlying ON_Light
      ON_Light light( light_obj->Light() );
      // Modify the diffuse color
      light.SetDiffuse( color );
    
      // Modify the light
      CRhinoLightTable& light_table = context.m_doc.m_light_table;
      light_table.ModifyLight( light, light_obj->LightIndex() );
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/modifying-
light-colors/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/modifying-
light-colors/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

