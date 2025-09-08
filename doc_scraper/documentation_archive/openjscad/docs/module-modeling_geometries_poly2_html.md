---
url: https://openjscad.xyz/docs/module-modeling_geometries_poly2.html#.flip
scraped_at: 2025-09-08T16:30:44.454075
title: Untitled
---

Represents a 2D polygon consisting of a list of ordered vertices.

Source:

    

  * [modeling/src/geometries/poly2/index.js](modeling_src_geometries_poly2_index.js.html), [line 1](modeling_src_geometries_poly2_index.js.html#line1)

See:

    

  * [poly2](global.html#poly2) for data structure information.

##### Examples

    
    
    poly2.create([[0,0], [4,0], [4,3]])
    
    
    {"vertices": [[0,0], [4,0], [4,3]]}

### Members

#### (static, constant) measureArea

Source:

    

  * [modeling/src/geometries/poly2/measureArea.js](modeling_src_geometries_poly2_measureArea.js.html), [line 8](modeling_src_geometries_poly2_measureArea.js.html#line8)

Measure the area under the given polygon.

### Methods

#### (static) arePointsInside(points, polygon) → {Integer}

Source:

    

  * [modeling/src/geometries/poly2/arePointsInside.js](modeling_src_geometries_poly2_arePointsInside.js.html), [line 12](modeling_src_geometries_poly2_arePointsInside.js.html#line12)

Determine if the given points are inside the given polygon.

##### Parameters:

Name | Type | Description  
---|---|---  
`points` |  Array | a list of points, where each point is an array with X and Y values  
`polygon` |  [poly2](global.html#poly2) | a 2D polygon  
  
##### Returns:

1 if all points are inside, 0 if some or none are inside

Type

     Integer

#### (static) create(verticesopt) → {[poly2](global.html#poly2)}

Source:

    

  * [modeling/src/geometries/poly2/create.js](modeling_src_geometries_poly2_create.js.html), [line 17](modeling_src_geometries_poly2_create.js.html#line17)

Creates a new polygon with initial values.

##### Example

    
    
    let polygon = create()

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`vertices` |  Array |  <optional>  
| list of vertices (2D)  
  
##### Returns:

a new polygon

Type

     [poly2](global.html#poly2)

#### (static) flip(polygon) → {[poly2](global.html#poly2)}

Source:

    

  * [modeling/src/geometries/poly2/flip.js](modeling_src_geometries_poly2_flip.js.html), [line 10](modeling_src_geometries_poly2_flip.js.html#line10)

Flip the give polygon, rotating the opposite direction.

##### Parameters:

Name | Type | Description  
---|---|---  
`polygon` |  [poly2](global.html#poly2) | the polygon to flip  
  
##### Returns:

a new polygon

Type

     [poly2](global.html#poly2)

