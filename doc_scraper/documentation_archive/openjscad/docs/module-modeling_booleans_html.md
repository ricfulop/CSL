---
url: https://openjscad.xyz/docs/module-modeling_booleans.html#.union
scraped_at: 2025-09-08T16:29:13.100304
title: Untitled
---

All shapes (primitives or the results of operations) can be passed to boolean
functions to perform logical operations, e.g. remove a hole from a board. In
all cases, the function returns the results, and never changes the original
shapes.

Source:

    

  * [modeling/src/operations/booleans/index.js](modeling_src_operations_booleans_index.js.html), [line 1](modeling_src_operations_booleans_index.js.html#line1)

##### Example

    
    
    const { intersect, subtract, union } = require('@jscad/modeling').booleans

### Methods

#### (static) intersect(…geometries) →
{[geom2](global.html#geom2)|[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/operations/booleans/intersect.js](modeling_src_operations_booleans_intersect.js.html), [line 32](modeling_src_operations_booleans_intersect.js.html#line32)

Return a new geometry representing space in both the first geometry and all
subsequent geometries. The given geometries should be of the same type, either
geom2 or geom3.

##### Examples

    
    
    let myshape = intersect(cube({size: 5}), cube({size: 5, center: [3,3,3]}))
    
    
    +-------+
    |       |
    |   A   |
    |    +--+----+   =   +--+
    +----+--+    |       +--+
         |   B   |
         |       |
         +-------+

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`geometries` |  Object |  <repeatable>  
| list of geometries  
  
##### Returns:

a new geometry

Type

     [geom2](global.html#geom2) | [geom3](global.html#geom3)

#### (static) scission(…objects) → {Array}

Source:

    

  * [modeling/src/operations/booleans/scission.js](modeling_src_operations_booleans_scission.js.html), [line 32](modeling_src_operations_booleans_scission.js.html#line32)

Scission (divide) the given geometry into the component pieces.

NOTE: Currently only 3D geometries are supported.

##### Examples

    
    
    let figure = require('./my.stl')
    let pieces = scission(figure)
    
    
    +-------+            +-------+
    |       |            |       |
    |   +---+            | A +---+
    |   |    +---+   =   |   |    +---+
    +---+    |   |       +---+    |   |
         +---+   |            +---+   |
         |       |            |    B  |
         +-------+            +-------+

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`objects` |  Object |  <repeatable>  
| list of geometries  
  
##### Returns:

list of pieces from each geometry

Type

     Array

#### (static) subtract(…geometries) →
{[geom2](global.html#geom2)|[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/operations/booleans/subtract.js](modeling_src_operations_booleans_subtract.js.html), [line 32](modeling_src_operations_booleans_subtract.js.html#line32)

Return a new geometry representing space in the first geometry but not in all
subsequent geometries. The given geometries should be of the same type, either
geom2 or geom3.

##### Examples

    
    
    let myshape = subtract(cuboid({size: 5}), cuboid({size: 5, center: [3,3,3]}))
    
    
    +-------+            +-------+
    |       |            |       |
    |   A   |            |       |
    |    +--+----+   =   |    +--+
    +----+--+    |       +----+
         |   B   |
         |       |
         +-------+

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`geometries` |  Object |  <repeatable>  
| list of geometries  
  
##### Returns:

a new geometry

Type

     [geom2](global.html#geom2) | [geom3](global.html#geom3)

#### (static) union(…geometries) →
{[geom2](global.html#geom2)|[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/operations/booleans/union.js](modeling_src_operations_booleans_union.js.html), [line 31](modeling_src_operations_booleans_union.js.html#line31)

Return a new geometry representing the total space in the given geometries.
The given geometries should be of the same type, either geom2 or geom3.

##### Examples

    
    
    let myshape = union(cube({size: 5}), cube({size: 5, center: [3,3,3]}))
    
    
    +-------+            +-------+
    |       |            |       |
    |   A   |            |       |
    |    +--+----+   =   |       +----+
    +----+--+    |       +----+       |
         |   B   |            |       |
         |       |            |       |
         +-------+            +-------+

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`geometries` |  Object |  <repeatable>  
| list of geometries  
  
##### Returns:

a new geometry

Type

     [geom2](global.html#geom2) | [geom3](global.html#geom3)

