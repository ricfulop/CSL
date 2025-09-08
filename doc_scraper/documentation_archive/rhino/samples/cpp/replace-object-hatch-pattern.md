---
url: https://developer.rhino3d.com/samples/cpp/replace-object-hatch-pattern/
scraped_at: 2025-09-08T15:48:39.870519
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

Replace Object Hatch Pattern

__

Windows only

Demonstrates how to replace a Hatch Object's pattern.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select hatches to replace pattern" );
      go.SetGeometryFilter( CRhinoGetObject::hatch_object );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      CRhinoGetString gs;
      gs.SetCommandPrompt( L"Name of replacement hatch pattern" );
      gs.GetString();
      if( gs.CommandResult() != success )
        return gs.CommandResult();
    
      ON_wString pattern_name = gs.String();
      pattern_name.TrimLeftAndRight();
      if( pattern_name.IsEmpty() )
        return nothing;
    
      int hatch_index = context.m_doc.m_hatchpattern_table.FindHatchPattern( pattern_name );
      if( hatch_index < 0 )
      {
        RhinoApp().Print( L"Specified hatch pattern not found in the document.\n" );
        return nothing;
      }
    
      int i, replaced = 0;
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const CRhinoHatch* hatch_obj = CRhinoHatch::Cast( go.Object(i).Object() );
        if( 0 == hatch_obj )
          continue;
    
        if( hatch_index == hatch_obj->PatternIndex() )
          continue;
    
        const ON_Hatch* hatch = hatch_obj->Hatch();
        if( 0 == hatch )
          continue;
    
        ON_Hatch* dup_hatch = hatch->DuplicateHatch();
        if( 0 == dup_hatch )
          continue;
    
        dup_hatch->SetPatternIndex( hatch_index );
    
        CRhinoHatch* dup_obj = hatch_obj->Duplicate();
        if( 0 == dup_obj )
        {
          delete dup_hatch;
          continue;
        }
    
        dup_obj->SetHatch( dup_hatch );
        if( !context.m_doc.ReplaceObject(CRhinoObjRef(hatch_obj), dup_obj) )
        {
          delete dup_obj;
          continue;
        }
    
        replaced++;
      }
    
      if( replaced > 0 )
      {
        context.m_doc.Redraw();
        if( 1 == replaced )
          RhinoApp().Print( L"1 hatch pattern replaced.\n" );
        else
          RhinoApp().Print( L"%d hatch patterns replaced.\n", replaced );
      }
      else
        RhinoApp().Print( L"0 hatch patterns replaced.\n" );
    
      return success;
    }
    

  

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

