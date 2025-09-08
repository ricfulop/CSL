---
url: https://developer.rhino3d.com/samples/cpp/block-definition-geometry/
scraped_at: 2025-09-08T15:47:35.133314
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

Block Definition Geometry

__

Windows only

Demonstrates how to obtain a block instance's definition geometry.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt(L"Select instance");
      go.SetGeometryFilter(CRhinoGetObject::instance_reference);
      go.GetObjects(1, 1);
      if (go.CommandResult() != CRhinoCommand::success)
        return go.CommandResult();
    
      const CRhinoInstanceObject* iref = CRhinoInstanceObject::Cast(go.Object(0).Object());
      if (iref == 0)
        return CRhinoCommand::failure;
    
      const CRhinoInstanceDefinition* idef = iref->InstanceDefinition();
      if (idef == 0)
        return CRhinoCommand::failure;
    
      ON_SimpleArray<const CRhinoObject*> objects;
      int count = idef->GetObjects(objects);
      for (int i = 0; i < count; i++ )
      {
        const CRhinoObject* obj = objects[i];
        if (obj != 0)
        {
          ON_wString str;
          ON_UuidToString( obj->Attributes().m_uuid, str );
          RhinoApp().Print(L"Object %d = %s\n", i, str);
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

