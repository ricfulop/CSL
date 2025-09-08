---
url: https://developer.rhino3d.com/samples/cpp/print-instance-definition-names/
scraped_at: 2025-09-08T15:47:36.164904
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

Print Instance Definition Names

__

Windows only

Demonstrates how to print the names of all instance definitions in the
document.

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
    
      int num_printed = 0;
      for (int i = 0; i < idef_count; i++)
      {
        const CRhinoInstanceDefinition* idef = idef_table[i];
        if (idef != 0 && idef->IsDeleted() == false)
        {
          ON_wString idef_name = idef->Name();
          RhinoApp().Print(L"Instance definition %d = %s\n", num_printed, idef_name);
          num_printed += 1;
        }
      }
    
      return CRhinoCommand::success;
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

