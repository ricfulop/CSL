---
url: https://developer.rhino3d.com/samples/cpp/add-arrowheads-to-curves/
scraped_at: 2025-09-08T15:47:14.046555
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

Add Arrowheads to Curves

__

Windows only

Demonstrates how arrowheads can be added to any curve object my modifying
attributes.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Define a line
      ON_Line line;
      line.from = ON_3dPoint(0, 0, 0);
      line.to = ON_3dPoint(10, 0, 0);
    
      // Make a copy of Rhino's default object attributes
      ON_3dmObjectAttributes attribs;
      context.m_doc.GetDefaultObjectAttributes( attribs );
    
      // Modify the object decoration style
      //attribs.m_object_decoration = ON::no_object_decoration;
      //attribs.m_object_decoration = ON::start_arrowhead;
      //attribs.m_object_decoration = ON::end_arrowhead;
      attribs.m_object_decoration = ON::both_arrowhead;
    
      // Create a new curve object with our attributes
      context.m_doc.AddCurveObject( line, &attribs );
      context.m_doc.Redraw();
    
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

