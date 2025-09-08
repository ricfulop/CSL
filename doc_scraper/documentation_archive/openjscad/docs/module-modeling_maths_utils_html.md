---
url: https://openjscad.xyz/docs/module-modeling_maths_utils.html#.intersect
scraped_at: 2025-09-08T16:32:30.924146
title: Untitled
---

Utility functions for maths.

Source:

    

  * [modeling/src/maths/utils/index.js](modeling_src_maths_utils_index.js.html), [line 1](modeling_src_maths_utils_index.js.html#line1)

##### Example

    
    
    const { area, solve2Linear } = require('@jscad/maths').utils

### Methods

#### (static) aboutEqualNormals(a, b) → {Boolean}

Source:

    

  * [modeling/src/maths/utils/aboutEqualNormals.js](modeling_src_maths_utils_aboutEqualNormals.js.html), [line 10](modeling_src_maths_utils_aboutEqualNormals.js.html#line10)

Compare two normals (unit vectors) for near equality.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [vec3](global.html#vec3) | normal a  
`b` |  [vec3](global.html#vec3) | normal b  
  
##### Returns:

true if a and b are nearly equal

Type

     Boolean

#### (static) area(points) → {Number}

Source:

    

  * [modeling/src/maths/utils/area.js](modeling_src_maths_utils_area.js.html), [line 7](modeling_src_maths_utils_area.js.html#line7)

Calculate the area under the given points.

##### Parameters:

Name | Type | Description  
---|---|---  
`points` |  Array | list of 2D points  
  
##### Returns:

area under the given points

Type

     Number

#### (static) interpolateBetween2DPointsForY(point1, point2, y) → {Array}

Source:

    

  * [modeling/src/maths/utils/interpolateBetween2DPointsForY.js](modeling_src_maths_utils_interpolateBetween2DPointsForY.js.html), [line 10](modeling_src_maths_utils_interpolateBetween2DPointsForY.js.html#line10)

Get the X coordinate of a point with a certain Y coordinate, interpolated
between two points. Interpolation is robust even if the points have the same Y
coordinate

##### Parameters:

Name | Type | Description  
---|---|---  
`point1` |  [vec2](global.html#vec2) |   
`point2` |  [vec2](global.html#vec2) |   
`y` |  Number |   
  
##### Returns:

X and Y of interpolated point

Type

     Array

#### (static) intersect(p1, p2, p3, p4) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/utils/intersect.js](modeling_src_maths_utils_intersect.js.html), [line 12](modeling_src_maths_utils_intersect.js.html#line12)

See:

    

  * <http://paulbourke.net/geometry/pointlineplane/>

Calculate the intersect point of the two line segments (p1-p2 and p3-p4), end
points included. Note: If the line segments do NOT intersect then undefined is
returned.

##### Parameters:

Name | Type | Description  
---|---|---  
`p1` |  [vec2](global.html#vec2) | first point of first line segment  
`p2` |  [vec2](global.html#vec2) | second point of first line segment  
`p3` |  [vec2](global.html#vec2) | first point of second line segment  
`p4` |  [vec2](global.html#vec2) | second point of second line segment  
  
##### Returns:

intersection point of the two line segments, or undefined

Type

     [vec2](global.html#vec2)

