---
url: https://developer.rhino3d.com/samples/cpp/on-simplearray-utils/
scraped_at: 2025-09-08T15:48:38.817817
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

ON_SimpleArray Utilities

__

Windows only

Demonstrates how to sort and cull simple arrays.

C/C++

    
    
    void SortDoubles( ON_SimpleArray<double>& arr, bool bIncreasing = true )
    {
      if( arr.Count() > 1 )
      {
        if( bIncreasing )
          arr.QuickSort( &ON_CompareIncreasing<double> );
        else
          arr.QuickSort( &ON_CompareDecreasing<double> );
      }
    }
    
    void CullDoubles( ON_SimpleArray<double>& arr, double tolerance = ON_ZERO_TOLERANCE )
    {
      const int count = arr.Count();
      if( count > 1 )
      {
        arr.QuickSort( &ON_CompareIncreasing<double> );
    
        if( tolerance < ON_ZERO_TOLERANCE )
          tolerance = ON_ZERO_TOLERANCE;
    
        double d = *arr.Last();
        int i;
        for( i = count - 2; i >= 0; i-- )
        {
          if( fabs(d - arr[i]) <= tolerance )
            arr.Remove(i);
          else
            d = arr[i];
        }
    
        arr.Shrink();
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

