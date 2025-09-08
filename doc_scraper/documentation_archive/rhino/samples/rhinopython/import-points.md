---
url: https://developer.rhino3d.com/samples/rhinopython/import-points/
scraped_at: 2025-09-08T15:47:02.019606
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

Import Points

Demonstrates importing points from a file into Rhino using Python.

Python

    
    
    # Import points from a text file
    import rhinoscriptsyntax as rs
    
    def ImportPoints():
        #prompt the user for a file to import
        filter = "Text file (*.txt)|*.txt|All Files (*.*)|*.*||"
        filename = rs.OpenFileName("Open Point File", filter)
        if not filename: return
        
        #read each line from the file
        file = open(filename, "r")
        contents = file.readlines()
        file.close()
    
        # local helper function    
        def __point_from_string(text):
            items = text.strip("()\n").split(",")
            x = float(items[0])
            y = float(items[1])
            z = float(items[2])
            return x, y, z
    
        contents = [__point_from_string(line) for line in contents]
        rs.AddPoints(contents)
    
    
    
    ##########################################################################
    # Check to see if this file is being executed as the "main" python
    # script instead of being used as a module by some other python script
    # This allows us to use the module which ever way we want.
    if( __name__ == "__main__" ):
        ImportPoints()
    

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

