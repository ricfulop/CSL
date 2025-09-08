---
url: https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods/
scraped_at: 2025-09-08T15:37:34.104623
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

[Point and Vector
Methods](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-point-vector-methods/)

  * Point & Vector Methods
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Point and Vector Methods

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Point & Vector Methods

The following methods are available for creating and manipulating 3-D points
and 3-D vectors. 3-D points and 3-D vectors are represented as zero-based,
one-dimensional arrays that contain three numbers. For more information, see
the [Points](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-points/) and
[Vectors](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-vectors/) discussion in [RhinoScript
Fundamentals](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-introduction/).

Method |  |  | Description  
---|---|---|---  
IsVectorParallelTo |  |  | Compares two vectors to see if they are parallel.  
IsVectorPerpendicularTo |  |  | Compares two vectors to see if they are perpendicular.  
IsVectorTiny |  |  | Verifies a vector is tiny.  
IsVectorZero |  |  | Verifies a vector is zero.  
PointAdd |  |  | Adds a point or a vector to a point.  
PointArrayBoundingBox |  |  | Returns the bounding box of an array of 3-D points.  
PointArrayClosestPoint |  |  | Finds the point in an array of 3-D points that is closest to a test point  
PointArrayTransform |  |  | Transforms an array of 3-D points.  
PointClosestObject |  |  | Finds the object that is closest to a test point.  
PointCompare |  |  | Compares two points.  
PointDivide |  |  | Divides a point by a value.  
PointsAreCoplanar |  |  | Verifies that a list of 3-D points are coplanar.  
PointScale |  |  | Scales a point by a value.  
PointSubtract |  |  | Subtracts a point or a vector from a point.  
PointTransform |  |  | Transforms a point.  
ProjectPointToMesh |  |  | Projects one or more points onto one or more meshes.  
ProjectPointToSurface |  |  | Projects one or more points onto one or more surfaces  
PullPoints |  |  | Pulls points to a surface or a mesh object.  
VectorAdd |  |  | Adds two vectors.  
VectorAngle |  |  | Returns the angle between two 3-D vectors.  
VectorCompare |  |  | Compares two vectors.  
VectorCreate |  |  | Create a vector from two 3-D points.  
VectorCrossProduct |  |  | Returns the cross product of two vectors.  
VectorDivide |  |  | Divides a vector.  
VectorDotProduct |  |  | Returns the dot product of two vectors.  
VectorLength |  |  | Returns the length of a vector.  
VectorMultiply |  |  | Multiplies two vectors.  
VectorReverse |  |  | Reverses a vector.  
VectorRotate |  |  | Rotates a vector.  
VectorScale |  |  | Scales a vector.  
VectorSubtract |  |  | Subtracts two vectors.  
VectorTransform |  |  | Transforms a vector.  
VectorUnitaze |  |  | Unitizes, or normalizes, a vector.  
  
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
rhinoscriptsyntax-point-vector-methods/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-point-vector-methods/index.md) [
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

