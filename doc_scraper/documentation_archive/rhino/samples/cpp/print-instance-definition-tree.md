---
url: https://developer.rhino3d.com/samples/cpp/print-instance-definition-tree/
scraped_at: 2025-09-08T15:47:41.439422
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

Print Instance Definition Tree

__

Windows only

Demonstrates how to print the names of all instance definitions, including
objects and sub-instances, in a tree-style format.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      const CRhinoInstanceDefinitionTable& idef_table = context.m_doc.m_instance_definition_table;
      int idef_count = idef_table.InstanceDefinitionCount();
      if (idef_count == 0)
      {
        RhinoApp().Print("No instance definitions found.\n");
        return CRhinoCommand::nothing;
      }
    
      ON_wString writer;
      ON_TextLog dump( writer );
      dump.SetIndentSize( 4 );
    
      for (int i = 0; i < idef_count; i++)
        DumpInstanceDefinition( idef_table[i], dump, true );
    
      RhinoApp().Print( L"%s\n", writer );
    
      return CRhinoCommand::success;
    }
    
    void CCommandTest::DumpInstanceDefinition( const CRhinoInstanceDefinition* idef, ON_TextLog& dump, bool bRoot )
    {
      if( idef && ! idef->IsDeleted() )
      {
        ON_wString node;
        if( bRoot )
          node = L"\u2500";
        else
          node = L"\u2514";
        dump.Print(L"%s Instance definition %d = %s\n", node, idef->Index(), idef->Name() );
    
        const int idef_object_count = idef->ObjectCount();
        if( idef_object_count )
        {
          dump.PushIndent();
          for( int i = 0; i < idef->ObjectCount(); i++ )
          {
            const CRhinoObject* obj = idef->Object( i );
            if( obj )
            {
              const CRhinoInstanceObject* iref = CRhinoInstanceObject::Cast( obj );
              if( iref )
                DumpInstanceDefinition( iref->InstanceDefinition(), dump, false ); // Recursive...
              else
                dump.Print(L"\u2514 Object %d = %s\n", i, obj->ShortDescription(false) );
            }
          }
          dump.PopIndent();
        }
      }
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

