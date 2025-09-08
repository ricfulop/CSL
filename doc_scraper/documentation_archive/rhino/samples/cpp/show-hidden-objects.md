---
url: https://developer.rhino3d.com/samples/cpp/show-hidden-objects/
scraped_at: 2025-09-08T15:48:42.851635
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

Show Hidden Objects

__

Windows only

Demonstrates how to iterate through the geometry table and unhide hidden
objects.

C/C++

    
    
    int ShowAllHiddenObjects( CRhinoDoc& doc, bool bRedraw )
    {
      CRhinoObjectIterator it(
            doc,
            CRhinoObjectIterator::undeleted_objects,
            CRhinoObjectIterator::active_and_reference_objects
            );
      it.IncludeLights();
    
      int count = 0;
      CRhinoObject* obj = 0;
      for( obj = it.First(); obj; obj = it.Next() )
      {
        // Ignore objects that are not hidden
        if( obj->Attributes().Mode() != ON::hidden_object )
          continue;
        // Ignore objects on hidden or locked layers
        if( ON::normal_layer != obj->ObjectLayer().Mode() )
          continue;
        if( doc.ShowObject(obj) )
          count++;
      }
    
      if( count > 0 && bRedraw )
        doc.Redraw();
      return count;
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

