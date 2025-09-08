---
url: https://developer.rhino3d.com/guides/rhinopython/python-reading-writing/
scraped_at: 2025-09-08T15:37:47.029023
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

[How to read and write a simple
file](https://developer.rhino3d.com/guides/rhinopython/python-reading-
writing/)

  * Reading a file
  * Writing a file

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

How to read and write a simple file

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Wednesday, December 5, 2018)

We’ll use a couple of simple scripts from the Python Samples folder as
examples - we’ll dissect these to see how they work.

## Reading a file

Here is the import-points.py script

    
    
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
    

We’ve put the action inside a function in this script, the

    
    
    def ImportPoints()
    

section. This allows the code to be re-used and simplifies error checking. The
first part uses the rs function

    
    
    rs.OpenFileName()
    

to allow the user to specify a file to open, and sets a variable ‘filename’ to
hold this information:

    
    
    filename = rs.OpenFileName("Open Point File", filter)
    

with a filter for text files.

If for some reason the user does not specify a file, say with a Cancel, then
the line

    
    
    if not filename: return
    

ensures that the rest of the code inside this particular function will not be
run, since there is nothing that can be done without a file name, and
executing the next lines in the script will result in error messages without
it. Since there is only the one function in this script, a cancel means the
script will stop.

Next a variable is set to the open file for reading:

    
    
    file = open(filename, "r")
    

and a variable is set to the contents of the file which is then held in memory
as a list with one item per line:

    
    
    contents = file.readlines()
    

The file is then closed:

    
    
    python file.close()
    

See python documentation for other ways to read files
(<https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-
files>).

At this point in the script, a new function is added, called
___point_from_string(text)_ , inside the main function, that parses text in
the expected format and converts the text into three numbers and returns those
as the xy,z coordinates of a point.

The list of lines from the orignal text file is fed into this function, line
by line to create a list of points, by calling that function:

    
    
    contents = [__point_from_string(line) for line in contents]
    

Lastly, the points in the list are added to the Rhino document as point
objects:

    
    
    rs.AddPoints(contents)
    

Note all if this code will not actually run unless the function is called -
this is done from the very last line of the script:

    
    
    if( __name__ == "__main__" ):
        ImportPoints()
    

## Writing a file

Writing a file is similar to reading, but the order in which things are done
is different. This time we’ll look at the ExportPoints.py sample file.

    
    
    import rhinoscriptsyntax as rs
    
    #Get the points to export
    objectIds = rs.GetObjects("Select Points",1+2, True, True)
    if( objectIds==None ): return
    
    #Get the filename to create
    filter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*||"
    filename = rs.SaveFileName("Save point coordinates as", filter)
    if( filename==None ): return
    
    
    with open(filename, "w") as file:
         # treat the objects differently depending on whether they are points or point clouds
        for id in objectIds:
            #process point clouds
            if( rs.IsPointCloud(id) ):
            points = rs.PointCloudPoints(id)
            for pt in points:
                file.write(str(pt)+"\n")
            elif( rs.IsPoint(id) ):
            point = rs.PointCoordinates(id)
            file.write(str(point) + "\n")
    

There are a couple of things to notice, compared to the previous example. We
need some points to export, so we’ll let the user select some point objects
and point clouds. There is a filter applied to the selection, the _1+2_. 1
filters for point objects and 2 filters for point clouds - we can add the
filters together to make combinations such as we have here - 1+2 or, we could
have written just 3, that would work as well, it is just harder to parse when
reviewing or modifying the code:

    
    
    objectIds = rs.GetObjects("Select Points", 1+2, True, True)
    

As before we check to make sure that the user has in fact selected the things
we’re looking for.

    
    
    if( objectIds==None ): return
    

Next we’ll get a file name as in the first example:

    
    
    #Get the filename to create
    filter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*||"
    filename = rs.SaveFileName("Save point coordinates as", filter)
    if( filename==None ): return
    

When writing to a file it must first be _opened_. While it is open, the
information can be written to the file. After writing all the information, the
file must be closed. In the first example we explicitly opened, read and then
closed the file. This time we’ve used the _with_ statement to open the file -
_with_ is convenient because it takes care of closing the file and cleaning up
when the script leaves the indented _with_ section.

    
    
    with open(filename, "w") as file:
         # treat the objects differently depending on whether they are points or point clouds
        for id in objectIds:
            #process point clouds
            if( rs.IsPointCloud(id) ):
            points = rs.PointCloudPoints(id)
            for pt in points:
                file.write(str(pt)+"\n")
            #process point objects
            elif( rs.IsPoint(id) ):
            point = rs.PointCoordinates(id)
            file.write(str(point) + "\n")
    ​```
    
    Keep in mind that 'points' in the script are not the same as 'point objects' in the Rhino file. Points are a list of x,y,z coordinates and point objects are objects in the Rhino file that have, among other properties like display color or layer, a location - the point coordinates.  As you can see in the above, the script iterates a list of IDs -those of the selected point objects or point clouds, and extracts the x,y,z coordinates to write to the file. The exported points are only the x,y,z coordinates of the point objects.
    
    For more information on reading and writing from Python, see the [Python Methods in File Objects documentation](https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects)
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
reading-writing/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
reading-writing/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

