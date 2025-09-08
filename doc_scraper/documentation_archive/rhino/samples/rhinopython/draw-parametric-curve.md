---
url: https://developer.rhino3d.com/samples/rhinopython/draw-parametric-curve/
scraped_at: 2025-09-08T15:46:56.854362
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

Draw a Parametric Curve

Demonstrates how to draw a parametric curve Python.

Python

    
    
    import rhinoscriptsyntax as rs
    import math
    
    # Something really interesting about this script is
    # that we are passing a function as a parameter
    def DrawParametricCurve(parametric_equation):
        "Create a interpolated curve based on a parametric equation."
        # Get the minimum parameter
        t0 = rs.GetReal("Minimum t value", 0.0)
        if( t0==None ): return
        
        # Get the maximum parameter
        t1 = rs.GetReal("Maximum t value", 1.0)
        if( t1==None ): return
    
        # Get the number of sampling points to interpolate through
        count = rs.GetInteger("Number of points", 50, 2)
        if count<1: return
    
        arrPoints = list()
        #Get the first point
        point = parametric_equation(t0)
        arrPoints.append(point)
    
        #Get the rest of the points
        for x in range(1,count-2):
            t = (1.0-(x/count))*t0 + (x/count)*t1
            point = parametric_equation(t)
            arrPoints.append(point)
      
        #Get the last point
        point = parametric_equation(t1)
        arrPoints.append(point)
        
        #Add the curve
        rs.AddInterpCurve(arrPoints)
    
    
    #Customizable function that solves a parametric equation
    def __CalculatePoint(t):
        x = (4*(1-t)+1*t ) * math.sin(3*6.2832*t)
        y = (4*(1-t)+1*t ) * math.cos(3*6.2832*t)
        z = 5*t
        return x,y,z
    
    ##########################################################################
    # Check to see if this file is being executed as the "main" python
    # script instead of being used as a module by some other python script
    # This allows us to use the module which ever way we want.
    if( __name__ == "__main__" ):
        #Call the function passing another function as a parameter
        DrawParametricCurve(__CalculatePoint)
    

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

