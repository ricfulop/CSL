---
url: https://developer.rhino3d.com/samples/rhinopython/export-control-points/
scraped_at: 2025-09-08T15:46:57.976568
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

Export Control Points

Demonstrates how to export control points with Python.

Python

    
    
    import rhinoscriptsyntax as rs
    
    def ExportControlPoints():
        "Export curve's control points to a text file"
        #pick a curve object
        object_id = rs.GetObject("Select curve", rs.filter.curve)
        
        #get the curve's control points
        points = rs.CurvePoints(object_id)
        if not points: return
        
        #prompt the user to specify a file name
        filter = "Text File (*.txt)|*.txt|All files (*.*)|*.*||"
        filename = rs.SaveFileName("Save Control Points As", filter)
        if not filename: return
    
        file = open( filename, "w" )
        for pt in points:
            file.write( str(pt.X) )
            file.write( ", " )
            file.write( str(pt.Y) )
            file.write( ", " )
            file.write( str(pt.Z) )
            file.write( "\n" )
        file.close()
    
    
    ##########################################################################
    # Check to see if this file is being executed as the "main" python
    # script instead of being used as a module by some other python script
    # This allows us to use the module which ever way we want.
    if( __name__ == "__main__" ):
        ExportControlPoints()
    

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

