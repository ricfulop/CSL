---
url: https://developer.rhino3d.com/samples/cpp/test-if-object-is-circle/
scraped_at: 2025-09-08T15:48:46.855823
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

Test if an Object is a Circle

__

Windows only

Demonstrates how to test if an object looks like a circle.

C/C++

    
    
    bool IsCircle( const CRhinoObject* obj )
    {
      bool rc = false;
      if( obj )
      {
        // Is the object a circle?
        if( const ON_ArcCurve* arc = ON_ArcCurve::Cast(obj->Geometry()) )
        {
          if( arc->IsCircle() )
            rc = true;
        }
        // Is the object an curve that just looks like a circle?
        else if( const ON_Curve* crv = ON_Curve::Cast(obj->Geometry()) )
        {
          ON_NurbsCurve nurb;
          if( crv->GetNurbForm(nurb) )
          {
            ON_Arc arc;
            double tol = ::RhinoApp().ActiveDoc()->AbsoluteTolerance();
            if( nurb.IsArc(0, &arc, tol) && arc.IsCircle()  )
              rc = true;
          }
        }
      }
      return rc;
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

