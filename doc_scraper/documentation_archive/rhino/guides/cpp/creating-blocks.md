---
url: https://developer.rhino3d.com/guides/cpp/creating-blocks/
scraped_at: 2025-09-08T15:38:50.400476
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

[Creating Blocks](https://developer.rhino3d.com/guides/cpp/creating-blocks/)

  * Overview
  * How To
  * Sample
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Creating Blocks

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Rhino blocks, known in the SDK as instances, are single objects that combine
one or more objects. Using blocks lets you:

  * Create parts libraries.
  * Update all instances by modifying the block definition.
  * Keep a smaller model size by using block instances instead of copying identical geometry.
  * Use the _BlockManager_ command to view information about the blocks defined in the model.
  * Use the _Insert_ command to place block instances into your model, which scales and rotates the instance.

## How To

Creating instance definitions using C/C++ requires two steps:

  1. Define the instance definition objects. Instance definition objects are similar to regular Rhino objects - the ones that you see on the screen. The difference is that instance definition objects reside in a different location in the document. To add instance definition objects to the document, use `CRhinoDoc::AddObject` and make sure you set the bInstanceDefinition parameter to true.
  2. Add a new instance definition object to Rhino’s instance definition table, which is located on the Rhino document. An instance definition defines the name of the instance and the instance definition objects used by it.

**NOTE** : An instance definition’s base point is always the world origin
(0,0,0). Knowing this, you need to orient your instance definition geometry
around the world origin. The _Block_ command does this by prompting the user
for a base point and then transforming the selected objects from the user’s
picked point to the world origin. If you are adding your own geometry on the
fly, and not picking it, just create your objects knowing that the base point
for your instance definition will be the world origin.

## Sample

The following example code demonstrates how to select one or more objects and
create a block definition with them.

**NOTE** : Unlike Rhino’s _Block_ command, this example code does not delete
the selected objects, nor does it automatically insert a block instance at the
location defined by the user.

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Select objects to define block
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select objects to define block" );
      go.EnableReferenceObjectSelect( false );
      go.EnableSubObjectSelect( false );
      go.EnableGroupSelect( true );
    
      // Phantoms, grips, lights, etc., cannot be in blocks.
      const unsigned int forbidden_geometry_filter
                    = CRhinoGetObject::light_object
                    | CRhinoGetObject::grip_object
                    | CRhinoGetObject::phantom_object;
      const unsigned int geometry_filter = forbidden_geometry_filter
                                   ^ CRhinoGetObject::any_object;
      go.SetGeometryFilter( geometry_filter );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      // Block base point
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Block base point" );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      ON_3dPoint base_point = gp.Point();
    
      // Block definition name
      CRhinoGetString gs;
      gs.SetCommandPrompt( L"Block definition name" );
      gs.GetString();
      if( gs.CommandResult() != success )
        return gs.CommandResult();
    
      // Validate block name
      ON_wString idef_name = gs.String();
      idef_name.TrimLeftAndRight();
      if( idef_name.IsEmpty() )
        return nothing;
    
      // See if block name already exists
      CRhinoInstanceDefinitionTable& idef_table = context.m_doc.m_instance_definition_table;
      int idef_index = idef_table.FindInstanceDefinition( idef_name );
      if( idef_index >= 0 )
      {
        RhinoApp().Print( L"Block definition \"%s\" already exists.\n", idef_name );
        return nothing;
      }
    
      // Create new block definition
      ON_InstanceDefinition idef;
      idef.SetName( idef_name );
    
      // Gather all of the selected objects
      ON_SimpleArray<const CRhinoObject*> objects( go.ObjectCount() );
      int i;
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const CRhinoObject* obj = go.Object(i).Object();
        if( obj )
          objects.Append( obj);
      }
    
      ON_Xform xform;
      xform.Translation( ON_origin - base_point );
    
      // Duplicate all of the selected objects and add them
      // to the document as instance definition objects
      ON_SimpleArray<const CRhinoObject*> idef_objects( objects.Count() );
      for( i = 0; i < objects.Count(); i++ )
      {
        const CRhinoObject* obj = objects[i];
        if( obj )
        {
          CRhinoObject* dupe = context.m_doc.TransformObject( obj, xform, false, false, false );
          if( dupe)
          {
            context.m_doc.AddObject( dupe, false, true );
            idef_objects.Append( dupe );
          }
        }
      }
    
      if( idef_objects.Count() < 1 )
      {
        RhinoApp().Print( L"Unable to duplicate block definition geometry.\n" );
        return failure;
      }
    
      idef_index = idef_table.AddInstanceDefinition( idef, idef_objects );
      if( idef_index < 0 )
      {
        RhinoApp().Print( L"Unable to create block definition \"%s\".\n", idef_name );
        return failure;
      }
    
      return success;
    }
    

## Related Topics

  * [Dynamically Inserting Blocks](https://developer.rhino3d.com/guides/cpp/dynamically-inserting-blocks/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/creating-
blocks/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/creating-
blocks/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

