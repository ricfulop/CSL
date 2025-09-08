---
url: https://developer.rhino3d.com/samples/cpp/calculate-the-angle-between-two-vectors/
scraped_at: 2025-09-08T15:48:26.935445
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

Calculate the Angle Between Two Vectors

__

Windows only

Demonstrates how to calculate the angle between two vectors.

C/C++

    
    
    // Description: Calculates the angle between two 3-D vectors.
    // Parameters:
    //  v0           - [in]  The first angle.
    //  v1           - [in]  The second angle.
    //  reflex_angle - [out] The reflex angle.
    // Returns: The angle in radians.
    double ON_3dVectorAngle( ON_3dVector v0, ON_3dVector v1, double* reflex_angle = 0 )
    {
      // Unitize the input vectors
      v0.Unitize();
      v1.Unitize();
    
      double dot = ON_DotProduct( v0, v1 );
    
      // Force the dot product of the two input vectors to
      // fall within the domain for inverse cosine, which
      // is -1 <= x <= 1. This will prevent runtime
      // "domain error" math exceptions.
      dot = ( dot < -1.0 ? -1.0 : ( dot > 1.0 ? 1.0 : dot ) );
    
      double angle = acos( dot );
    
      if( reflex_angle )
        *reflex_angle = (ON_PI * 2) - angle;
    
      return angle;
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

