---
url: https://developer.rhino3d.com/samples/rhinopython/array-points-on-surface/
scraped_at: 2025-09-08T15:46:51.839052
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

Array Points on Surface

Demonstrates how to array points on a surface using Python.

Python

    
    
    # Creates an array of points on a surface
    import rhinoscriptsyntax as rs
    
    def ArrayPointsOnSurface():
        # Get the surface object
        surface_id = rs.GetObject("Select surface", rs.filter.surface)
        if surface_id is None: return
    
        # Get the number of rows
        rows = rs.GetInteger("Number of rows", 2, 2)
        if rows is None: return
    
        # Get the number of columns
        columns = rs.GetInteger("Number of columns", 2, 2)
        if columns is None: return
    
        # Get the domain of the surface
        U = rs.SurfaceDomain(surface_id, 0)
        V = rs.SurfaceDomain(surface_id, 1)
        if U is None or V is None: return
    
        # Add the points
        for i in range(0,rows):
            param0 = U[0] + (((U[1] - U[0]) / (rows-1)) * i)
            for j in range(0,columns):
                param1 = V[0] + (((V[1] - V[0]) / (columns-1)) * j)
                point = rs.EvaluateSurface(surface_id, param0, param1)
                rs.AddPoint(point)
    
    
    # Check to see if this file is being executed as the "main" python
    # script instead of being used as a module by some other python script
    # This allows us to use the module which ever way we want.
    if __name__ == "__main__":
        # call the function defined above
        ArrayPointsOnSurface()
    

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

