---
url: https://openjscad.xyz/docs/module-modeling_hulls.html#.hullPoints3
scraped_at: 2025-09-08T16:31:05.539886
title: Untitled
---

All shapes (primitives or the results of operations) can be passed to hull
functions to determine the convex hull of all points. In all cases, the
function returns the results, and never changes the original shapes.

Source:

    

  * [modeling/src/operations/hulls/index.js](modeling_src_operations_hulls_index.js.html), [line 1](modeling_src_operations_hulls_index.js.html#line1)

##### Example

    
    
    const { hull, hullChain, hullPoints2, hullPoints3 } = require('@jscad/modeling').hulls

### Methods

#### (static) hull(…geometries) →
{[geom2](global.html#geom2)|[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/operations/hulls/hull.js](modeling_src_operations_hulls_hull.js.html), [line 35](modeling_src_operations_hulls_hull.js.html#line35)

Create a convex hull of the given geometries. The given geometries should be
of the same type, either geom2 or geom3 or path2.

##### Examples

    
    
    let myshape = hull(rectangle({center: [-5,-5]}), ellipse({center: [5,5]}))
    
    
    +-------+           +-------+
    |       |           |        \
    |   A   |           |         \
    |       |           |          \
    +-------+           +           \
                     =   \           \
          +-------+       \           +
          |       |        \          |
          |   B   |         \         |
          |       |          \        |
          +-------+           +-------+

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`geometries` |  Objects |  <repeatable>  
| list of geometries from which to create a hull  
  
##### Returns:

new geometry

Type

     [geom2](global.html#geom2) | [geom3](global.html#geom3)

#### (static) hullChain(…geometries) →
{[geom2](global.html#geom2)|[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/operations/hulls/hullChain.js](modeling_src_operations_hulls_hullChain.js.html), [line 32](modeling_src_operations_hulls_hullChain.js.html#line32)

Create a chain of hulled geometries from the given geometries. Essentially
hull A+B, B+C, C+D, etc., then union the results. The given geometries should
be of the same type, either geom2 or geom3 or path2.

##### Examples

    
    
    let newshape = hullChain(rectangle({center: [-5,-5]}), circle({center: [0,0]}), rectangle({center: [5,5]}))
    
    
    +-------+   +-------+     +-------+   +------+
    |       |   |       |     |        \ /       |
    |   A   |   |   C   |     |         |        |
    |       |   |       |     |                  |
    +-------+   +-------+     +                  +
                          =   \                 /
          +-------+            \               /
          |       |             \             /
          |   B   |              \           /
          |       |               \         /
          +-------+                +-------+

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`geometries` |  Objects |  <repeatable>  
| list of geometries from which to create a hull  
  
##### Returns:

new geometry

Type

     [geom2](global.html#geom2) | [geom3](global.html#geom3)

#### (static) hullPoints2(uniquePoints) → {Array}

Source:

    

  * [modeling/src/operations/hulls/hullPoints2.js](modeling_src_operations_hulls_hullPoints2.js.html), [line 11](modeling_src_operations_hulls_hullPoints2.js.html#line11)

See:

    

  * <https://en.wikipedia.org/wiki/Graham_scan>

Create a convex hull of the given set of points, where each point is an array
of [x,y].

##### Parameters:

Name | Type | Description  
---|---|---  
`uniquePoints` |  Array | list of UNIQUE points from which to create a hull  
  
##### Returns:

a list of points that form the hull

Type

     Array

#### (static) hullPoints3(uniquePoints) → {Array}

Source:

    

  * [modeling/src/operations/hulls/hullPoints3.js](modeling_src_operations_hulls_hullPoints3.js.html), [line 12](modeling_src_operations_hulls_hullPoints3.js.html#line12)

Create a convex hull of the given set of points, where each point is an array
of [x,y,z].

##### Parameters:

Name | Type | Description  
---|---|---  
`uniquePoints` |  Array | list of UNIQUE points from which to create a hull  
  
##### Returns:

a list of polygons (poly3)

Type

     Array

