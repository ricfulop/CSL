---
url: https://openjscad.xyz/docs/module-modeling_maths_line3.html#.transform
scraped_at: 2025-09-08T16:31:38.720785
title: Untitled
---

Represents a unbounded line in 3D space, positioned at a point of origin.

Source:

    

  * [modeling/src/maths/line3/index.js](modeling_src_maths_line3_index.js.html), [line 1](modeling_src_maths_line3_index.js.html#line1)

See:

    

  * [line3](global.html#line3) for data structure information.

### Methods

#### (static) clone(line) → {[line3](global.html#line3)}

Source:

    

  * [modeling/src/maths/line3/clone.js](modeling_src_maths_line3_clone.js.html), [line 12](modeling_src_maths_line3_clone.js.html#line12)

Create a clone of the given line.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line3](global.html#line3) | line to clone  
  
##### Returns:

a new unbounded line

Type

     [line3](global.html#line3)

#### (static) closestPoint(line, point) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/line3/closestPoint.js](modeling_src_maths_line3_closestPoint.js.html), [line 11](modeling_src_maths_line3_closestPoint.js.html#line11)

Determine the closest point on the given line to the given point.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line3](global.html#line3) | line of reference  
`point` |  [vec3](global.html#vec3) | point of reference  
  
##### Returns:

a point

Type

     [vec3](global.html#vec3)

#### (static) copy(out, line) → {[line3](global.html#line3)}

Source:

    

  * [modeling/src/maths/line3/copy.js](modeling_src_maths_line3_copy.js.html), [line 11](modeling_src_maths_line3_copy.js.html#line11)

Copy the given line into the receiving line.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [line3](global.html#line3) | receiving line  
`line` |  [line3](global.html#line3) | line to copy  
  
##### Returns:

out

Type

     [line3](global.html#line3)

#### (static) create() → {[line3](global.html#line3)}

Source:

    

  * [modeling/src/maths/line3/create.js](modeling_src_maths_line3_create.js.html), [line 18](modeling_src_maths_line3_create.js.html#line18)

Create a line, positioned at 0,0,0 and lying on the X axis.

##### Returns:

a new unbounded line

Type

     [line3](global.html#line3)

#### (static) direction(line) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/line3/direction.js](modeling_src_maths_line3_direction.js.html), [line 8](modeling_src_maths_line3_direction.js.html#line8)

Return the direction of the given line.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line3](global.html#line3) | line for reference  
  
##### Returns:

the relative vector in the direction of the line

Type

     [vec3](global.html#vec3)

#### (static) distanceToPoint(line, point) → {Number}

Source:

    

  * [modeling/src/maths/line3/distanceToPoint.js](modeling_src_maths_line3_distanceToPoint.js.html), [line 13](modeling_src_maths_line3_distanceToPoint.js.html#line13)

Calculate the distance (positive) between the given point and line.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line3](global.html#line3) | line of reference  
`point` |  [vec3](global.html#vec3) | point of reference  
  
##### Returns:

distance between line and point

Type

     Number

#### (static) equals(line1, line2) → {Boolean}

Source:

    

  * [modeling/src/maths/line3/equals.js](modeling_src_maths_line3_equals.js.html), [line 11](modeling_src_maths_line3_equals.js.html#line11)

Compare the given lines for equality.

##### Parameters:

Name | Type | Description  
---|---|---  
`line1` |  [line3](global.html#line3) | first line to compare  
`line2` |  [line3](global.html#line3) | second line to compare  
  
##### Returns:

true if lines are equal

Type

     Boolean

#### (static) fromPlanes(out, plane1, plane2) → {[line3](global.html#line3)}

Source:

    

  * [modeling/src/maths/line3/fromPlanes.js](modeling_src_maths_line3_fromPlanes.js.html), [line 17](modeling_src_maths_line3_fromPlanes.js.html#line17)

Create a line the intersection of the given planes.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [line3](global.html#line3) | receiving line  
`plane1` |  [plane](global.html#plane) | first plane of reference  
`plane2` |  [plane](global.html#plane) | second plane of reference  
  
##### Returns:

out

Type

     [line3](global.html#line3)

#### (static) fromPointAndDirection(out, point, direction) →
{[line3](global.html#line3)}

Source:

    

  * [modeling/src/maths/line3/fromPointAndDirection.js](modeling_src_maths_line3_fromPointAndDirection.js.html), [line 17](modeling_src_maths_line3_fromPointAndDirection.js.html#line17)

Create a line from the given point (origin) and direction.

The point can be any random point on the line. The direction must be a vector
with positive or negative distance from the point.

See the logic of fromPoints() for appropriate values.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [line3](global.html#line3) | receiving line  
`point` |  [vec3](global.html#vec3) | start point of the line segment  
`direction` |  [vec3](global.html#vec3) | direction of the line segment  
  
##### Returns:

out

Type

     [line3](global.html#line3)

#### (static) fromPoints(out, point1, point2) → {[line3](global.html#line3)}

Source:

    

  * [modeling/src/maths/line3/fromPoints.js](modeling_src_maths_line3_fromPoints.js.html), [line 14](modeling_src_maths_line3_fromPoints.js.html#line14)

Create a line that passes through the given points.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [line3](global.html#line3) | receiving line  
`point1` |  [vec3](global.html#vec3) | start point of the line segment  
`point2` |  [vec3](global.html#vec3) | end point of the line segment  
  
##### Returns:

out

Type

     [line3](global.html#line3)

#### (static) intersectPointOfLineAndPlane(line, plane) →
{[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/line3/intersectPointOfLineAndPlane.js](modeling_src_maths_line3_intersectPointOfLineAndPlane.js.html), [line 14](modeling_src_maths_line3_intersectPointOfLineAndPlane.js.html#line14)

Determine the closest point on the given plane to the given line.

NOTES: The point of intersection will be invalid if the line is parallel to
the plane, e.g. NaN.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line3](global.html#line3) | line of reference  
`plane` |  [plane](global.html#plane) | plane of reference  
  
##### Returns:

a point on the line

Type

     [vec3](global.html#vec3)

#### (static) origin(line) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/line3/origin.js](modeling_src_maths_line3_origin.js.html), [line 8](modeling_src_maths_line3_origin.js.html#line8)

Return the origin of the given line.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line3](global.html#line3) | line of reference  
  
##### Returns:

the origin of the line

Type

     [vec3](global.html#vec3)

#### (static) reverse(out, line) → {[line3](global.html#line3)}

Source:

    

  * [modeling/src/maths/line3/reverse.js](modeling_src_maths_line3_reverse.js.html), [line 13](modeling_src_maths_line3_reverse.js.html#line13)

Create a line in the opposite direction as the given.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [line3](global.html#line3) | receiving line  
`line` |  [line3](global.html#line3) | line to reverse  
  
##### Returns:

out

Type

     [line3](global.html#line3)

#### (static) toString(line) → {String}

Source:

    

  * [modeling/src/maths/line3/toString.js](modeling_src_maths_line3_toString.js.html), [line 8](modeling_src_maths_line3_toString.js.html#line8)

Return a string representing the given line.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line3](global.html#line3) | line of reference  
  
##### Returns:

string representation

Type

     String

#### (static) transform(out, line, matrix) → {[line3](global.html#line3)}

Source:

    

  * [modeling/src/maths/line3/transform.js](modeling_src_maths_line3_transform.js.html), [line 14](modeling_src_maths_line3_transform.js.html#line14)

Transforms the given line using the given matrix.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [line3](global.html#line3) | line to update  
`line` |  [line3](global.html#line3) | line to transform  
`matrix` |  [mat4](global.html#mat4) | matrix to transform with  
  
##### Returns:

a new unbounded line

Type

     [line3](global.html#line3)

