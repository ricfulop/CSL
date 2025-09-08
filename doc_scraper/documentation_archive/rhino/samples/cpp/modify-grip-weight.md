---
url: https://developer.rhino3d.com/samples/cpp/modify-grip-weight/
scraped_at: 2025-09-08T15:48:36.809084
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

Modify Grip Weight

__

Windows only

Demonstrates how to modify the weight of a grip object.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Pick a grip object
      CRhinoGetObject go;
      go.SetCommandPrompt( RHSTR(L"Select control point for weight editing") );
      go.SetGeometryFilter( CRhinoGetObject::grip_object );
      go.EnableReferenceObjectSelect( false );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != CRhinoCommand::success )
        return go.CommandResult();
    
      // Add the object to an xform object list
      CRhinoXformObjectList objlist;
      if( objlist.AddObjects(go, true) < 1 )
        return CRhinoCommand::failure;
    
      // Get the grip's weight
      double weight = objlist.m_grips[0]->Weight();
    
      // Prompt for a new value
      CRhinoGetNumber gn;
      gn.SetCommandPrompt( RHSTR(L"New control point weight") );
      gn.SetDefaultNumber( weight );
      gn.AcceptNothing();
    
      // Validate the results
      CRhinoGet::result res = gn.GetNumber();
      if( res == CRhinoGet::number )
        weight = gn.Number();
      else if( res == CRhinoGet::nothing )
        return CRhinoCommand::nothing;
      else
        return CRhinoCommand::cancel;
    
      // Do nothing if weights are the same
      if( weight == objlist.m_grips[0]->Weight() )
        return CRhinoCommand::nothing;
    
      // Modify the grip's weight
      objlist.m_grips[0]->SetWeight( weight );
    
      // Get the grip object's owning object
      CRhinoObject* old_object = objlist.m_grip_owners[0];
      if( old_object && old_object->m_grips )
      {
        // Create a new object based on the updated grip information
        CRhinoObject* new_object = old_object->m_grips->NewObject();
        if( new_object )
        {
          // Replace the old object with the new object
          context.m_doc.ReplaceObject( CRhinoObjRef(old_object), new_object );
          context.m_doc.Redraw();
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

