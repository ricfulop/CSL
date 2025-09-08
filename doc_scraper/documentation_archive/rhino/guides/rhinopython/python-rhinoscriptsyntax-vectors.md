---
url: https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-vectors/
scraped_at: 2025-09-08T15:37:30.949894
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

[Vectors in Python](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-vectors/)

  * Vectors
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Vectors in Python

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Thursday, March 9, 2023)

## Vectors

Similar to 3D points, 3D vectors are stored as
[Vector3d](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Vector3d.htm)
structures. They can be thought as a zero-based, one-dimensional list that
contain three numbers. These three number represent to the X, Y and Z
coordinate direction of the vector.

    
    
    vector3d contains (1.0, 2.0, 3.0)  
    

Here is an easy way to construct a vector:

    
    
    import rhinoscriptsyntax as rs
    
    vec = rs.CreateVector(1.0, 2.0, 3.0)
    

A Vector3d’s coordinates can be accessed as a list, one element at a time:

    
    
    import rhinoscriptsyntax as rs
    
    vec = rs.CreateVector(1.0, 2.0, 3.0)
    
    print(vec[0]) #Prints the X coordinate of the Vector3d
    print(vec[1]) #Print the Y coordinate of the Vector3d
    print(vec[2]) #Print the Z coordinate of the Vector3d
    

The coordinates of a Vector3d may also be accessed through its `.X`, `.Y` and
`.Z` properties:

    
    
    import rhinoscriptsyntax as rs
    
    vec = rs.CreateVector(1.0, 2.0, 3.0)
    
    print(vec.X) # Prints the X coordinate of the Vector3d
    print(vec.Y) # Print the Y coordinate of the Vector3d
    print(vec.Z) # Print the Z coordinate of the Vector3d
    

To change the individual coordinate of a Vector3d, simply assign a new value
to the coordinate through the index location or coordinate property:

    
    
    import rhinoscriptsyntax as rs
    
    point1 = (1,2,3)
    point2 = (4,6,7)
    vec = rs.CreateVector(1.0, 2.0, 3.0)
    
    vec[0] = 5.0 # Sets the X coordinate to 5.0
    vec.Y = 45.0 # Sets the Y coordinate to 45.0
    
    print(vec) #Print the new coordinates
    

To find the vector between two points, use vector subtraction:

![https://developer.rhino3d.com/images/image180.png](https://developer.rhino3d.com/images/math-
image180.png)

    
    
    point1 = rs.CreatePoint(1,2,3)
    point2 = rs.CreatePoint(4,5,6)
    
    vector = point1 - point2
    
    print(vector) #prints the new coordinates.
    

In the above example, the vector goes from point1 to point2. Reversing this
direction is a common mistake. It is important to be sure that the starting
point is subtracted from the ending point.

Vectors can also be added to points to create new point locations. Here is an
example of moving a point location by a vector:

![https://developer.rhino3d.com/images/image172.png](https://developer.rhino3d.com/images/math-
image172.png)

    
    
    #  A base point
    point1 = rs.CreatePoint(1,1,1)
    
    # A vector with a direction of 2 units in the X direction
    vector1 = rs.CreateVector(2.0, 0.0, 0.0)
    
    # Setting the coordinate of point1 to to units more in the X direction.
    vector = point1 + vector1
    # point1 + vector1 = [1+2, 1+0, 1+0] = [3,1,1]
    
    print(vector)
    

RhinoScriptSyntax contains a number of methods to manipulate vectors. See
[RhinoScript Points and Vectors
Methods](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-point-vector-methods/) for details.

## Related Topics

  * [Python Points](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-points/)
  * [Python Vectors](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-vectors/)
  * [Python Lines](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-line/)
  * [Python Planes](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-plane/)
  * [Python Objects](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-objects/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-vectors/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-vectors/index.md) [
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

