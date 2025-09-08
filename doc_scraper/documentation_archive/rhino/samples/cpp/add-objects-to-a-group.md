---
url: https://developer.rhino3d.com/samples/cpp/add-objects-to-a-group/
scraped_at: 2025-09-08T15:47:18.119391
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

Add Objects to a Group

__

Windows only

Demonstrates how to add selected objects to an object group.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select objects to group" );
      go.EnableGroupSelect();
      go.GetObjects(1,0);
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      int i = 0, count = go.ObjectCount();
      ON_SimpleArray<const CRhinoObject*> members( count );
    
      for( i = 0; i < count; i++ )
        members.Append( go.Object(i).Object() );
    
      int index = context.m_doc.m_group_table.AddGroup( ON_Group(), members );
      context.m_doc.Redraw();
      return (index >= 0) ? CRhinoCommand::success : CRhinoCommand::failure;
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

