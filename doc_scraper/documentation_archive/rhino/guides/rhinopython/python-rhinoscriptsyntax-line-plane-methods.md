---
url: https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-line-plane-methods/
scraped_at: 2025-09-08T15:37:35.098004
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

[Line and Plane
Methods](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-line-plane-methods/)

  * Line and Plane Methods
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Line and Plane Methods

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Line and Plane Methods

The following methods are available for creating and manipulating lines and
planes.

Lines are represented as zero-based, one-dimensional arrays containing two
elements: the start point (3-D point) and the end point (3-D point).

Planes are represented as zero-based, one-dimensional arrays containing four
elements: the plane’s origin (3-D point), the plane’s x-axis direction (3-D
vector), the plane’s y-axis direction (3-D vector), and the plane’s z-axis
direction (3-D vector).

For more information in [RhinoScript
Fundamentals](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-introduction/).

Method |  |  | Description  
---|---|---|---  
DistanceToPlane |  |  | Returns the distance from a plane to a point.  
EvaluatePlane |  |  | Evaluates a point on a plane.  
IntersectPlanes |  |  | Returns the point calculated by intersecting three planes.  
LineArcIntersection |  |  | Intersects an infinite line and an arc.  
LineBetweenCurves |  |  | Create a line perpendicular or tangent between two curves.  
LineBoxIntersection |  |  | Intersects an infinite line and an axis aligned bounding box.  
LineCircleIntersection |  |  | Intersects an infinite line and a circle.  
LineClosestPoint |  |  | Finds the point on an infinite line that is closest to a test point.  
LineCurveIntersection |  |  | Intersect an infinite line and a curve object.  
LineCylinderIntersection |  |  | Calculates the intersection of a line and a cylinder.  
LineIsFartherThan |  |  | Determines if the shortest distance from a line to a point or another line is greater than a specified distance.  
LineLineIntersection |  |  | Returns the point calculated by intersecting two lines.  
LineMaxDistanceTo |  |  | Finds the longest distance between the line, as a finite chord, and a point or another line.  
LineMeshIntersection |  |  | Intersects an infinite line with a mesh object.  
LineMinDistanceTo |  |  | Finds the shortest distance between the line, as a finite chord, and a point or another line.  
LinePlane |  |  | Returns a plane that contains the line.  
LinePlaneIntersection |  |  | Returns the point calculated by intersecting a line with a plane.  
LineSphereIntersection |  |  | Calculates the intersection of a line and a sphere.  
LineTransform |  |  | Transforms a line.  
MovePlane |  |  | Moves the origin of a plane.  
PlaneAngle |  |  | Calculates the angle between two points on a plane.  
PlaneArcIntersection |  |  | Intersects a plane and an arc.  
PlaneCircleIntersection |  |  | Intersects a plane and a circle.  
PlaneClosestPoint |  |  | Returns the closest point on a plane from a point.  
PlaneCurveIntersection |  |  | Intersects an infinite plane and a curve object.  
PlaneEquation |  |  | Returns the equation of a plane.  
PlaneFitFromPoints |  |  | Returns a plane through an array of points.  
PlaneFromFrame |  |  | Creates a plane from an origin point, X axis direction, and Y axis direction.  
PlaneFromNormal |  |  | Creates a plane from an origin point, and a normal direction.  
PlaneFromPoints |  |  | Creates a plane from three non-colinear points.  
PlanePlaneIntersection |  |  | Returns the line calculated by intersecting two planes.  
PlaneSphereIntersection |  |  | Calculates the intersection of a plane and a sphere.  
PlaneTransform |  |  | Transforms a plane.  
RotatePlane |  |  | Rotates a plane.  
WorldXYPlane |  |  | Returns Rhino’s world XY plane.  
WorldYZPlane |  |  | Returns Rhino’s world YZ plane.  
WorldZXPlane |  |  | Returns Rhino’s world ZX plane.  
  
## Related Topics

  * [What is RhinoScriptSyntax and RhinoScript?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Python List of Points](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-list-points/)
  * [Python Vectors](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-vectors/)
  * [Python Lines](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-lines)
  * [Python Planes](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-planes)
  * [Python Objects](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-objects/)
  * [RhinoScript Points and Vectors Methods](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-line-plane-methods/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-line-plane-methods/index.md) [
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

