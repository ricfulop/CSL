---
url: https://developer.rhino3d.com/samples/rhinopython/garden-path/
scraped_at: 2025-09-08T15:46:59.004092
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

Garden Path Sample

Demonstrates basic syntax for writing python scripts.

Python

    
    
    import rhinoscriptsyntax as rs
    import math #Use this to get sine, cosine and radians.
    import scriptcontext as sc
    
    def test():
    
            #Assign variables to the sin and cos functions for use later.
        Sin = math.sin
        Cos = math.cos
    
    
        	# Acquire information for the garden path
    
        	# set default values for the distances
        default_hwidth = 1
        default_trad = 1
        default_tspace = 1
    
    
        	# look for any previously used values stored in sticky and use those if available.
        if sc.sticky.has_key("GP_WIDTH"):
            default_hwidth = sc.sticky["GP_WIDTH"]
    
        if sc.sticky.has_key("GP_RAD"):
            default_trad = sc.sticky["GP_RAD"]
    
        if sc.sticky.has_key("GP_Space"):
            default_tspace = sc.sticky["GP_SPACE"]
    
            #get the path direction, length and location from two points entered by the user
        sp = rs.GetPoint("Start point of path centerline")
        if sp is None: return
    
        ep = rs.GetPoint("End point of path centerline", sp)
        if ep is None: return
    
            #now ask the user what the distances should be, offering the defaults arrived at above
    
        hwidth = rs.GetDistance(sp, default_hwidth,  second_pt_msg = "Half width of path")
        if hwidth is None: return
    
            #Store the new value in sticky for use next time
        sc.sticky["GP_WIDTH"] = hwidth
    
        trad = rs.GetDistance(sp, default_trad, second_pt_msg = "Radius of tiles")
        if trad is None: return
    
            #Store  the new value in sticky for use next time
        sc.sticky["GP_RAD"] = trad
    
        tspace = rs .GetDistance(sp, default_tspace, second_pt_msg = "Distance between tiles")
        if tspace is None: return
    
            #Store  the new value in sticky for use next time
        sc.sticky["GP_SPACE"] = tspace
    
        	# Calculate angles
    
        temp = rs.Angle(sp, ep)
    
        pangle = temp[0]
    
        plength = rs.Distance(sp, ep)
    
        width = hwidth * 2
    
        angp90 = pangle + 90.0
    
        angm90 = pangle - 90.0
    
    
    	# To increase speed, disable redrawing
    
        rs.EnableRedraw (False)
    
    	# Draw the outline of the path
        #make an empty list
        pline = []
    
        #add points to the list
        pline.append(rs.Polar(sp, angm90, hwidth))
    
        pline.append(rs.Polar(pline[0], pangle, plength))
    
        pline.append(rs.Polar(pline[1], angp90, width))
    
        pline.append(rs.Polar(pline[2], pangle + 180.0, plength))
    
        #add the first point back on to the end of the list to close the pline
        pline.append (pline[0])
    
        #create the polyline from the lst of points.
        rs.AddPolyline (pline)
    
    
    
        # Draw the rows of tiles
    
        #define a plane -
        #using the WorldXY plane the reults will always be added parallel to that plane,
        #regardless of the active plane where the points are picked.
    
        plane = rs.WorldXYPlane()
    
        pdist = trad + tspace
    
        off = 0.0
    
        while (pdist <= plength - trad):
    
            #Place one row of tiles given distance along path
    
            # and possibly offset it
    
            pfirst = rs.Polar(sp, pangle, pdist)
    
            pctile = rs.Polar(pfirst, angp90, off)
    
            pltile = pctile
    
            while (rs.Distance(pfirst, pltile) < hwidth - trad):
    
                plane = rs.MovePlane(plane, pltile)
    
                rs.AddCircle (plane, trad)
    
                pltile = rs.Polar(pltile, angp90, tspace + trad + trad)
    
    
            pltile = rs.Polar(pctile, angm90, tspace + trad + trad)
    
            while (rs.Distance(pfirst, pltile) < hwidth - trad):
    
                plane = rs.MovePlane(plane, pltile)
    
                rs.AddCircle (plane, trad)
    
                pltile = rs.Polar(pltile, angm90, tspace + trad + trad)
    
            pdist = pdist + ((tspace + trad + trad) * Sin(math.radians(60)))
    
            if off == 0.0:
    
                off = (tspace + trad + trad) * Cos(math.radians(60))
    
            else:
    
                off = 0.0
    
    
    
    
    
    
    if __name__ == "__main__":
    
        test()
    

The goal of the garden path sample is to develop a script that draws a garden
path and fills it with circular concrete tiles. For those familiar with
AutoLISP®, the programming language of Autodesk’s AutoCAD®, you are probably
also familiar with the garden path tutorial.

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

