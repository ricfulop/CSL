---
url: https://developer.rhino3d.com/samples/rhinopython/export-points/
scraped_at: 2025-09-08T15:46:59.979988
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

Export Points

Demonstrates how to export points with Python.

Python

    
    
    # Export the coordinates of point and point cloud objects to a text file.
    import rhinoscriptsyntax as rs
    
    def ExportPoints():
        #Get the points to export
        objectIds = rs.GetObjects("Select Points",rs.filter.point | rs.filter.pointcloud,True,True)
        if( objectIds==None ): return
    
        #Get the filename to create
        filter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*||"
        filename = rs.SaveFileName("Save point coordinates as", filter)
        if( filename==None ): return
        
        """
        Using a 'with' loop to open the file, we do not need to clean
        up or close the file when we are done, Python takes care of it.
        Here, we'll write the points with a line break, otherwise
        all the points will end up on one line.
        """
        with open(filename, "w")as file:
            
            for id in objectIds:
                #process point clouds
                if( rs.IsPointCloud(id) ):
                    points = rs.PointCloudPoints(id)
                    for pt in points:
                        # convert the point list to a string, 
                        # add a new line character, and write to the file
                        file.write(str(pt)+ "\n")
                elif( rs.IsPoint(id) ):
                    point = rs.PointCoordinates(id)
                    file.write(str(point)+ "\n")
        
    
    ##########################################################################
    # Here we check to see if this file is being executed as the "main" python
    # script instead of being used as a module by some other python script
    # This allows us to use the module which ever way we want.
    if( __name__ == '__main__' ):
        ExportPoints()
    

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

