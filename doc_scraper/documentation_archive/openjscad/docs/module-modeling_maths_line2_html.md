---
url: https://openjscad.xyz/docs/module-modeling_maths_line2.html#.xAtY
scraped_at: 2025-09-08T16:31:22.662139
title: Untitled
---

Represents a unbounded line in 2D space, positioned at a point of origin.

Source:

    

  * [modeling/src/maths/line2/index.js](modeling_src_maths_line2_index.js.html), [line 1](modeling_src_maths_line2_index.js.html#line1)

See:

    

  * [line2](global.html#line2) for data structure information.

### Methods

#### (static) clone(line) → {[line2](global.html#line2)}

Source:

    

  * [modeling/src/maths/line2/clone.js](modeling_src_maths_line2_clone.js.html), [line 10](modeling_src_maths_line2_clone.js.html#line10)

Create a clone of the given line.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line2](global.html#line2) | line to clone  
  
##### Returns:

a new unbounded line

Type

     [line2](global.html#line2)

#### (static) closestPoint(line, point) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/line2/closestPoint.js](modeling_src_maths_line2_closestPoint.js.html), [line 14](modeling_src_maths_line2_closestPoint.js.html#line14)

Determine the closest point on the given line to the given point.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line2](global.html#line2) | line of reference  
`point` |  [vec2](global.html#vec2) | point of reference  
  
##### Returns:

closest point

Type

     [vec2](global.html#vec2)

#### (static) copy(out, line) → {[line2](global.html#line2)}

Source:

    

  * [modeling/src/maths/line2/copy.js](modeling_src_maths_line2_copy.js.html), [line 9](modeling_src_maths_line2_copy.js.html#line9)

Copy the given line to the receiving line.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [line2](global.html#line2) | receiving line  
`line` |  [line2](global.html#line2) | line to copy  
  
##### Returns:

out

Type

     [line2](global.html#line2)

#### (static) create() → {[line2](global.html#line2)}

Source:

    

  * [modeling/src/maths/line2/create.js](modeling_src_maths_line2_create.js.html), [line 18](modeling_src_maths_line2_create.js.html#line18)

Create a line, positioned at 0,0, and running along the X axis.

##### Returns:

a new unbounded line

Type

     [line2](global.html#line2)

#### (static) direction(line) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/line2/direction.js](modeling_src_maths_line2_direction.js.html), [line 10](modeling_src_maths_line2_direction.js.html#line10)

Return the direction of the given line.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line2](global.html#line2) | line of reference  
  
##### Returns:

a vector in the direction of the line

Type

     [vec2](global.html#vec2)

#### (static) distanceToPoint(line, point) → {Number}

Source:

    

  * [modeling/src/maths/line2/distanceToPoint.js](modeling_src_maths_line2_distanceToPoint.js.html), [line 11](modeling_src_maths_line2_distanceToPoint.js.html#line11)

Calculate the distance (positive) between the given point and line.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line2](global.html#line2) | line of reference  
`point` |  [vec2](global.html#vec2) | point of reference  
  
##### Returns:

distance between line and point

Type

     Number

#### (static) equals(line1, line2) → {Boolean}

Source:

    

  * [modeling/src/maths/line2/equals.js](modeling_src_maths_line2_equals.js.html), [line 9](modeling_src_maths_line2_equals.js.html#line9)

Compare the given lines for equality.

##### Parameters:

Name | Type | Description  
---|---|---  
`line1` |  [line2](global.html#line2) | first line to compare  
`line2` |  [line2](global.html#line2) | second line to compare  
  
##### Returns:

true if lines are equal

Type

     Boolean

#### (static) fromPoints(out, point1, point2) → {[line2](global.html#line2)}

Source:

    

  * [modeling/src/maths/line2/fromPoints.js](modeling_src_maths_line2_fromPoints.js.html), [line 12](modeling_src_maths_line2_fromPoints.js.html#line12)

Create a new line that passes through the given points.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [line2](global.html#line2) | receiving line  
`point1` |  [vec2](global.html#vec2) | start point of the line  
`point2` |  [vec2](global.html#vec2) | end point of the line  
  
##### Returns:

a new unbounded line

Type

     [line2](global.html#line2)

#### (static) fromValues(x, y, d) → {[line2](global.html#line2)}

Source:

    

  * [modeling/src/maths/line2/fromValues.js](modeling_src_maths_line2_fromValues.js.html), [line 12](modeling_src_maths_line2_fromValues.js.html#line12)

Creates a new line initialized with the given values.

##### Parameters:

Name | Type | Description  
---|---|---  
`x` |  Number | X coordinate of the unit normal  
`y` |  Number | Y coordinate of the unit normal  
`d` |  Number | distance of the line from [0,0]  
  
##### Returns:

a new unbounded line

Type

     [line2](global.html#line2)

#### (static) intersectPointOfLines(line1, line2) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/line2/intersectPointOfLines.js](modeling_src_maths_line2_intersectPointOfLines.js.html), [line 16](modeling_src_maths_line2_intersectPointOfLines.js.html#line16)

Return the point of intersection between the given lines.

NOTES: The point will have Infinity values if the lines are parallel. The
point will have NaN values if the lines are the same.

##### Parameters:

Name | Type | Description  
---|---|---  
`line1` |  [line2](global.html#line2) | line of reference  
`line2` |  [line2](global.html#line2) | line of reference  
  
##### Returns:

the point of intersection

Type

     [vec2](global.html#vec2)

#### (static) origin(line) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/line2/origin.js](modeling_src_maths_line2_origin.js.html), [line 11](modeling_src_maths_line2_origin.js.html#line11)

Return the origin of the given line. The origin is the point on the line which
is closest to the origin [0, 0].

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line2](global.html#line2) | line of reference  
  
##### Returns:

the origin of the line

Type

     [vec2](global.html#vec2)

#### (static) reverse(out, line) → {[line2](global.html#line2)}

Source:

    

  * [modeling/src/maths/line2/reverse.js](modeling_src_maths_line2_reverse.js.html), [line 14](modeling_src_maths_line2_reverse.js.html#line14)

Create a new line in the opposite direction as the given.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [line2](global.html#line2) | receiving line  
`line` |  [line2](global.html#line2) | line to reverse  
  
##### Returns:

out

Type

     [line2](global.html#line2)

#### (static) toString(line) → {String}

Source:

    

  * [modeling/src/maths/line2/toString.js](modeling_src_maths_line2_toString.js.html), [line 8](modeling_src_maths_line2_toString.js.html#line8)

Return a string representing the given line.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line2](global.html#line2) | line of reference  
  
##### Returns:

string representation

Type

     String

#### (static) transform(out, line, matrix) → {[line2](global.html#line2)}

Source:

    

  * [modeling/src/maths/line2/transform.js](modeling_src_maths_line2_transform.js.html), [line 16](modeling_src_maths_line2_transform.js.html#line16)

Transforms the given line using the given matrix.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [line2](global.html#line2) | receiving line  
`line` |  [line2](global.html#line2) | line to transform  
`matrix` |  [mat4](global.html#mat4) | matrix to transform with  
  
##### Returns:

out

Type

     [line2](global.html#line2)

#### (static) xAtY(line, y) → {Number}

Source:

    

  * [modeling/src/maths/line2/xAtY.js](modeling_src_maths_line2_xAtY.js.html), [line 13](modeling_src_maths_line2_xAtY.js.html#line13)

Determine the X coordinate of the given line at the Y coordinate.

The X coordinate will be Infinity if the line is parallel to the X axis.

##### Parameters:

Name | Type | Description  
---|---|---  
`line` |  [line2](global.html#line2) | line of reference  
`y` |  Number | Y coordinate on the line  
  
##### Returns:

the X coordinate on the line

Type

     Number

