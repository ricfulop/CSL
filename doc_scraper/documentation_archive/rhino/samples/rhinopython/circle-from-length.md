---
url: https://developer.rhino3d.com/samples/rhinopython/circle-from-length/
scraped_at: 2025-09-08T15:46:52.947929
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

Circle From Length

Demonstrates how to add a circle based on its circumference using Python.

Python

    
    
    # Create a circle from a center point and a circumference.
    import rhinoscriptsyntax as rs
    import math
    
    def CreateCircle(circumference=None):
        center = rs.GetPoint("Center point of circle")
        if center:
            plane = rs.MovePlane(rs.ViewCPlane(), center)
            length = circumference
            if length is None: length = rs.GetReal("Circle circumference")
            if length and length>0:
                radius = length/(2*math.pi)
                objectId = rs.AddCircle(plane, radius)
                rs.SelectObject(objectId)
                return length
        return None
    
    # Check to see if this file is being executed as the "Main" python
    # script instead of being used as a module by some other python script
    # This allows us to use the module which ever way we want.
    if __name__ == '__main__':
        CreateCircle()
    
    # NOTE: see UseModule.py sample for using this script as a module
    

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

