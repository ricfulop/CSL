---
url: https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-plane/
scraped_at: 2025-09-08T15:37:31.955286
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

[Planes in Python](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-plane/)

  * Planes
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Planes in Python

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, May 6, 2020)

## Planes

Planes are represented by a
[Plane](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Plane.htm)
structure. Planes can be thought of as a zero-based, one-dimensional list
containing four elements: the plane’s origin
([point3D](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-points/)), the plane’s X axis direction
([vector3d](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-vectors/)), the plane’s Y axis direction
([vector3d](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-vectors/)), and the plane’s Z axis direction
([vector3d](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-vectors/)).

![https://developer.rhino3d.com/images/primer-
planedefinition.svg](https://developer.rhino3d.com/images/primer-
planedefinition.svg)

    
    
    plane contains (pointOrigin, vectorX, vectorY, vectorZ)
    

It is easy to forget that there is a specific geometric relationship between
the axes. With Planes, the Y axis is automatically oriented 90-degrees to the
X axis. The X axis is the only axis that can be easily defined. The Y axis is
made orthogonal to the X vector, and the direction of the Z axis is computed
from the cross-product of the other two vectors.

Planes can be constructed in a number of ways. One common function is
`PlaneFromPoints`:

    
    
    import rhinoscriptsyntax as rs
    
    plane = rs.PlaneFromPoints((-2,-5,0),(1,2,0),(-3,3,0))
    
    print(plane.Origin) # origin point
    print(plane.XAxis) # x-axis vector
    print(plane.YAxis) # y-axis vector
    

Plane also have a number of properties that can be used to get or set the
individual values in the Point object. In the example below the `.Origin`,
`.XAxis`, `.Yaxis`, `.Zaxis` are used.

Planes can also be created using the `CreatePlane()`,
[PlaneFromFrame](https://developer.rhino3d.com/api/RhinoScriptSyntax/win/#collapse-
PlaneFromFrame),
[PlaneFromNormal](https://developer.rhino3d.com/api/RhinoScriptSyntax/win/#collapse-
PlaneFromNormal), and
[PlaneFromPoints](https://developer.rhino3d.com/api/RhinoScriptSyntax/win/#collapse-
PlaneFromPoints) functions.

To change origin of a Plane, simply assign a new value to the `.Origin`
property.

    
    
    import rhinoscriptsyntax as rs
    
    plane = rs.PlaneFromPoints((-2,-5,0),(1,2,0),(-3,3,0))
    
    print(plane.Origin) # origin point
    print(plane.XAxis) # x-axis vector
    print(plane.YAxis) # y-axis vector
    
    plane.Origin = rs.CreatePoint(3,4,5) # Changes the origin of the plane.
    
    print(plane.Origin)
    print(plane.XAxis) # x-axis vector
    print(plane.YAxis) # y-axis vector
    

RhinoScriptSyntax contains a number of functions to manipulate planes. See
[Lines and Planes](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-line-plane-methods/) for details.

Also, please see the Python primer [Section 8.5
Planes](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#85-planes).

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
rhinoscriptsyntax-plane/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-plane/index.md) [
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

