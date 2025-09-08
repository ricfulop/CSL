---
url: https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-list-points/
scraped_at: 2025-09-08T15:37:28.033738
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

[List of Points in
Python](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-list-points/)

  * Lists of Points
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

List of Points in Python

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Lists of Points

Many rhinoscriptsyntax functions require a list of points as an argument or
return a list of
[Point3d](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-points/) structures. For example the ‘DivideCurve()’
function will return a list of points:

    
    
    import rhinoscriptsyntax as rs
    
    obj = rs.GetObject("Select a curve")
    
    if obj:
        points = rs.DivideCurve(obj, 4)
        
    print(points[0])
    

There are a number of ways to access the information in these lists.

Use an index to access any one of the points as in the line:

    
    
    print(points[0]) # Returns a Point3d structure
    

With Python, it is easy to use the `for` loop to walk through the list and
print out the coordinates for each point,

    
    
    for i in points:
        print(i)
    

It is also possible to use nested indexes to access a specific coordinate of a
point in the list. This example will access the Y coordinate of the second
point in the list:

    
    
    print(points[1][1])
    

Using the .Y property on the
[Point3d](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-points/) also would work:

    
    
    print(points[1].Y)
    

To add a point to this list, first create the point3d with `CreatePoint()`,
then [append](https://docs.python.org/2/tutorial/datastructures.html) it:

    
    
    points.append(rs.CreatePoint(1.0, 2.0, 3.0))
    
    for i in points:
        print(i)
    

## Related Topics

  * [What is Python and RhinoScript?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Python Points](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-points/)
  * [Python Vectors](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-vectors/)
  * [Python Lines](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-lines)
  * [Python Planes](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-planes)
  * [Python Objects](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-objects/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-list-points/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-list-points/index.md) [
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

