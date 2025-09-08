---
url: https://openjscad.xyz/docs/module-modeling_maths_plane.html#~toString
scraped_at: 2025-09-08T16:32:25.912835
title: Untitled
---

Represents a plane in 3D coordinate space as determined by a normal
(perpendicular to the plane) and distance from 0,0,0.

Source:

    

  * [modeling/src/maths/plane/index.js](modeling_src_maths_plane_index.js.html), [line 1](modeling_src_maths_plane_index.js.html#line1)

See:

    

  * [plane](global.html#plane) for data structure information.

### Methods

#### (static) flip(out, plane) → {[plane](global.html#plane)}

Source:

    

  * [modeling/src/maths/plane/flip.js](modeling_src_maths_plane_flip.js.html), [line 9](modeling_src_maths_plane_flip.js.html#line9)

Flip the given plane.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [plane](global.html#plane) | receiving plane  
`plane` |  [plane](global.html#plane) | plane to flip  
  
##### Returns:

out

Type

     [plane](global.html#plane)

#### (static) fromNoisyPoints(out, …vertices) → {Plane}

Source:

    

  * [modeling/src/maths/plane/fromNoisyPoints.js](modeling_src_maths_plane_fromNoisyPoints.js.html), [line 17](modeling_src_maths_plane_fromNoisyPoints.js.html#line17)

Create a best-fit plane from the given noisy vertices.

NOTE: There are two possible orientations for every plane. This function
always produces positive orientations.

See http://www.ilikebigbits.com for the original discussion

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`out` |  Plane |  | receiving plane  
`vertices` |  Array |  <repeatable>  
| list of vertices in any order or position  
  
##### Returns:

out

Type

     Plane

#### (static) fromNormalAndPoint(out, normal, point) →
{[plane](global.html#plane)}

Source:

    

  * [modeling/src/maths/plane/fromNormalAndPoint.js](modeling_src_maths_plane_fromNormalAndPoint.js.html), [line 21](modeling_src_maths_plane_fromNormalAndPoint.js.html#line21)

Create a new plane from the given normal and point values.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [plane](global.html#plane) | receiving plane  
`normal` |  [vec3](global.html#vec3) | directional vector  
`point` |  [vec3](global.html#vec3) | origin of plane  
  
##### Returns:

out

Type

     [plane](global.html#plane)

#### (static) fromPoints(out, …vertices) → {[plane](global.html#plane)}

Source:

    

  * [modeling/src/maths/plane/fromPoints.js](modeling_src_maths_plane_fromPoints.js.html), [line 11](modeling_src_maths_plane_fromPoints.js.html#line11)

Create a plane from the given points.

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`out` |  [plane](global.html#plane) |  | receiving plane  
`vertices` |  Array |  <repeatable>  
| points on the plane  
  
##### Returns:

out

Type

     [plane](global.html#plane)

#### (static) fromPointsRandom(out, a, b, c) → {[plane](global.html#plane)}

Source:

    

  * [modeling/src/maths/plane/fromPointsRandom.js](modeling_src_maths_plane_fromPointsRandom.js.html), [line 17](modeling_src_maths_plane_fromPointsRandom.js.html#line17)

Create a new plane from the given points like fromPoints, but allow the
vectors to be on one point or one line. In such a case, a random plane through
the given points is constructed.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [plane](global.html#plane) | receiving plane  
`a` |  [vec3](global.html#vec3) | 3D point  
`b` |  [vec3](global.html#vec3) | 3D point  
`c` |  [vec3](global.html#vec3) | 3D point  
  
##### Returns:

out

Type

     [plane](global.html#plane)

#### (static) projectionOfPoint(plane, point) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/plane/projectionOfPoint.js](modeling_src_maths_plane_projectionOfPoint.js.html), [line 11](modeling_src_maths_plane_projectionOfPoint.js.html#line11)

Project the given point on to the given plane.

##### Parameters:

Name | Type | Description  
---|---|---  
`plane` |  [plane](global.html#plane) | plane of reference  
`point` |  [vec3](global.html#vec3) | point of reference  
  
##### Returns:

projected point on plane

Type

     [vec3](global.html#vec3)

#### (static) signedDistanceToPoint(plane, point) → {Number}

Source:

    

  * [modeling/src/maths/plane/signedDistanceToPoint.js](modeling_src_maths_plane_signedDistanceToPoint.js.html), [line 11](modeling_src_maths_plane_signedDistanceToPoint.js.html#line11)

Calculate the distance to the given point.

##### Parameters:

Name | Type | Description  
---|---|---  
`plane` |  [plane](global.html#plane) | plane of reference  
`point` |  [vec3](global.html#vec3) | point of reference  
  
##### Returns:

signed distance to point

Type

     Number

#### (static) transform(out, plane, matrix) → {[plane](global.html#plane)}

Source:

    

  * [modeling/src/maths/plane/transform.js](modeling_src_maths_plane_transform.js.html), [line 16](modeling_src_maths_plane_transform.js.html#line16)

Transform the given plane using the given matrix

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [plane](global.html#plane) | receiving plane  
`plane` |  [plane](global.html#plane) | plane to transform  
`matrix` |  [mat4](global.html#mat4) | matrix to transform with  
  
##### Returns:

out

Type

     [plane](global.html#plane)

#### (inner) clone()

Source:

    

  * [modeling/src/maths/plane/index.js](modeling_src_maths_plane_index.js.html), [line 8](modeling_src_maths_plane_index.js.html#line8)

See:

    

  * [vec4.clone()](module-modeling_maths_vec4.html#.clone)

#### (inner) copy()

Source:

    

  * [modeling/src/maths/plane/index.js](modeling_src_maths_plane_index.js.html), [line 13](modeling_src_maths_plane_index.js.html#line13)

See:

    

  * [vec4.copy()](module-modeling_maths_vec4.html#.copy)

#### (inner) create()

Source:

    

  * [modeling/src/maths/plane/index.js](modeling_src_maths_plane_index.js.html), [line 18](modeling_src_maths_plane_index.js.html#line18)

See:

    

  * [vec4.create()](module-modeling_maths_vec4.html#.create)

#### (inner) equals()

Source:

    

  * [modeling/src/maths/plane/index.js](modeling_src_maths_plane_index.js.html), [line 23](modeling_src_maths_plane_index.js.html#line23)

See:

    

  * [vec4.equals()](module-modeling_maths_vec4.html#.equals)

#### (inner) fromValues()

Source:

    

  * [modeling/src/maths/plane/index.js](modeling_src_maths_plane_index.js.html), [line 30](modeling_src_maths_plane_index.js.html#line30)

See:

    

  * [vec4.fromValues()](module-modeling_maths_vec4.html#.fromValues)

#### (inner) toString()

Source:

    

  * [modeling/src/maths/plane/index.js](modeling_src_maths_plane_index.js.html), [line 40](modeling_src_maths_plane_index.js.html#line40)

See:

    

  * [vec4.toString()](module-modeling_maths_vec4.html#.toString)

