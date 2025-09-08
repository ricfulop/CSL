---
url: https://developer.rhino3d.com/guides/cpp/modifying-advanced-display-settings/
scraped_at: 2025-09-08T15:40:00.575229
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

[Modifying Advanced Display
Settings](https://developer.rhino3d.com/guides/cpp/modifying-advanced-display-
settings/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Modifying Advanced Display Settings

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The advanced display features in Rhino give the user almost unlimited control
over how objects appear on the screen. All of these features are also exposed
to the C/C++ developer.

Rhino maintains advanced display settings using the
`CDisplayPipelineAttributes` class. Rhino will maintain a number of these
objects, one for each advanced display setting created by the user (i.e.
Wireframe, Shaded, Rendered, Ghosted, X-Ray, etc.) or by 3rd party plugins.

The C/C++ developer can gain access to these objects using the Display
Attributes Manager, which is implemented as a number of static functions found
on the `CRhinoDisplayAttrsMgr` class.

The process for updating advanced display settings is similar to updating or
modifying other objects in Rhino.

  1. Make a copy of the original.
  2. Modify one or more setting or parameters.
  3. Replace the original object with the modified copy.

## Sample

    
    
    // The following example code demonstrates how to modify advanced display settings using
    // the Rhino SDK. In this example, a display mode's mesh wireframe thickness (in pixels)
    // will be modified.
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Use the display attributes manager to build a list of display modes.
      // Note, these are copies of the originals...
      DisplayAttrsMgrList attrs_list;
      int attrs_count = CRhinoDisplayAttrsMgr::GetDisplayAttrsList( attrs_list );
      if( attrs_count == 0 )
        return failure;
    
      // Construct an options picker so the user can pick which
      // display mode they want modified
      CRhinoGetOption go;
      go.SetCommandPrompt( L"Display mode to modify mesh thickness" );
    
      ON_SimpleArray<int> opt_list( attrs_count );
      opt_list.SetCount( attrs_count );
    
      for( int i = 0; i < attrs_count; i++ )
      {
        // Verify the display mode had a valid
        // CDisplayPipelineAttributes pointer
        if( 0 == attrs_list[i].m_pAttrs )
        {
          opt_list[i] = 0;
          continue;
        }
    
        // Get the display attributes English name
        ON_wString english_name = attrs_list[i].m_pAttrs->EnglishName();
        english_name.Remove( L'_' );
        english_name.Remove( L' ' );
        english_name.Remove( L'-' );
        english_name.Remove( L',' );
        english_name.Remove( L'.' );
    
        // Get the display attributes localized name
        ON_wString local_name = attrs_list[i].m_pAttrs->LocalName();
        local_name.Remove( L'_' );
        local_name.Remove( L' ' );
        local_name.Remove( L'-' );
        local_name.Remove( L',' );
        local_name.Remove( L'.' );
    
        // Add the command option
        opt_list[i] = go.AddCommandOption( CRhinoCommandOptionName(english_name, local_name) );
      }
    
      // Get the command option
      go.GetOption();
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const CRhinoCommandOption* opt = go.Option();
      if( 0 == opt )
        return failure;
    
      // Figure out which command option was picked
      int attrs_index = -1;
      for( int i = 0; i < opt_list.Count(); i++ )
      {
        if( opt_list[i] == opt->m_option_index )
        {
          attrs_index = i;
          break;
        }
      }
    
      // Validate...
      if( attrs_index < 0 | attrs_index >= attrs_count )
        return failure;
    
      // Get the display mode requested by the user
      DisplayAttrsMgrListDesc desc = attrs_list[attrs_index];
      if( 0 == desc.m_pAttrs )
        return failure;
    
      // Modify the desired display mode. In this case, we
      // will just set the mesh wireframe thickness to zero.
      desc.m_pAttrs->m_nMeshWireThickness = 0;
    
      // Use the display attributes manager to update the display mode.
      CRhinoDisplayAttrsMgr::UpdateAttributes( desc );
    
      // Force the document to regenerate.
      context.m_doc.Regen();
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/modifying-
advanced-display-settings/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/modifying-
advanced-display-settings/index.md) [
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

