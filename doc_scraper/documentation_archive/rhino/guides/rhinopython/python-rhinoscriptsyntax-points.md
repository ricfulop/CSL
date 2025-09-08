---
url: https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-points/
scraped_at: 2025-09-08T15:37:27.054139
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

[Points in Python](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-points/)

  * Points
    * Creating Points
    * Accessing Point Coordinates
    * Editing Points
    * Adding a point to display in Rhino
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Points in Python

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, May 6, 2020)

## Points

In Python, a Rhino 3D point is represented as a
[Point3d](http://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Point3d.htm)
structure. Conceptually, Point3d exist in memory as a zero-based list
containing three numbers. These three numbers represent the X, Y and Z
coordinate values of the point.

    
    
    point3D contains (1.0, 2.0, 3.0)  
    

### Creating Points

A Point3D structure can be constructed in a number of different ways. Two
common ways are:

    
    
    import rhinoscriptsyntax as rs
    
    pnt = rs.CreatePoint(1.0, 2.0, 3.0)
    pnt = rs.CreatePoint(1.0, 2.0) # This creates a point with the Z coordinate set to 0
    

The ‘CreatePoint()’ function is very flexible. It can take a tuple of two or 3
numbers and return a Point3d. The function can also extract the coordinates of
a Rhino GUID to return a Point3D.

It is not always necessary to construct a point before passing it to a
function that requires a point. It is possible to construct points directly as
an argument to a function. A Point is a list like structure. Wrap coordinates
in parenthesis`()` when passing them directly to a function. For instance the
`rs.addline(point, point)` function requires two points. Use the following
syntax to construct the points on the fly:

    
    
    rs.AddLine((45,56,32),(56,47,89))
    

Like 3-D points, Python represents a single 2-D point as a zero-based list of
numbers. The difference being that 2-D points contain only X and Y coordinate
values.

Passing coordinates in `()` to a function is common with RhinoScriptSyntax.

### Accessing Point Coordinates

A Point3D list can be accessed like a simple python tupple, one element at a
time:

    
    
    import rhinoscriptsyntax as rs
    
    pnt = rs.CreatePoint(1.0, 2.0, 3.0)
    
    print(pnt[0]) #Print the X coordinate of the Point3D
    print(pnt[1]) #Print the Y coordinate of the Point3D
    print(pnt[2]) #Print the Z coordinate of the Point3D
    

The coordinates of a Point3d may also be accessed through its .X, .Y and .Z
properties.

    
    
    import rhinoscriptsyntax as rs
    
    pnt = rs.CreatePoint(1.0, 2.0, 3.0)
    
    print(pnt.X) # Print the X coordinate of the Point3D
    print(pnt.Y) # Print the Y coordinate of the Point3D
    print(pnt.Z) # Print the Z coordinate of the Point3D
    

### Editing Points

To change an individual coordinate of a Point3d simply assign a new value to
the correct coordinate through the index location or coordinate property:

    
    
    import rhinoscriptsyntax as rs
    
    pnt = rs.CreatePoint(1.0, 2.0, 3.0)
    
    pnt[0] = 5.0 # Sets the X coordinate to 5.0
    pnt.Y = 45.0 # Sets the Y coordinate to 45.0
    
    print(pnt) #Print the new coordinates
    

Rhinoscriptsyntax contains a number of methods to manipulate points. See
[RhinoScript Points and Vectors
Methods](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-point-vector-methods/) for details.

### Adding a point to display in Rhino

It is important to understand the difference between a Point3d and a point
object added to Rhino’s document. Any geometry object that exists in Rhino’s
database is assigned an object identifier. This is represented as a
[Guid](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-objects/). The [Guid’s
object](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-objects/) is geometry and the associated attributes that can
be drawn, belongs to a layer, is saved to a Rhino file and is counted as a
Rhino object. A Point3d is simply a data structure of 3 numbers that exists in
memory. It can be manipulated in memory, but will not be seen in Rhino or
saved. A Point3d is added to the Rhino document through the `rs.AddPoint()`
command. To create a Point3d from a Guid, use the `rs.PointCoordinates(guid)`
or the `rs.CreatePoint(Guid)` function.

## Related Topics

  * [What is RhinoScriptSyntax and RhinoScript?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Python List of Points](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-list-points/)
  * [Python Vectors](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-vectors/)
  * [Python Lines](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-lines)
  * [Python Planes](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-plane/)
  * [Python Objects](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-objects/)
  * [RhinoScript Points and Vectors Methods](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods/)
  * [Point3d RhinoCommon Documentation](http://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Point3d.htm)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-points/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-points/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

