---
url: https://openjscad.xyz/docs/module-modeling_geometries_geom2.html#.validate
scraped_at: 2025-09-08T16:30:08.318337
title: Untitled
---

Represents a 2D geometry consisting of a list of sides.

Source:

    

  * [modeling/src/geometries/geom2/index.js](modeling_src_geometries_geom2_index.js.html), [line 1](modeling_src_geometries_geom2_index.js.html#line1)

See:

    

  * [geom2](global.html#geom2) for data structure information.

##### Examples

    
    
    colorize([0.5,0,1,1], square()) // purple square
    
    
    {
      "sides": [[[-1,1],[-1,-1]],[[-1,-1],[1,-1]],[[1,-1],[1,1]],[[1,1],[-1,1]]],
      "transforms": [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
      "color": [0.5,0,1,1]
    }

### Methods

#### (static) clone(geometry) → {[geom2](global.html#geom2)}

Source:

    

  * [modeling/src/geometries/geom2/clone.js](modeling_src_geometries_geom2_clone.js.html), [line 7](modeling_src_geometries_geom2_clone.js.html#line7)

Performs a shallow clone of the given geometry.

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom2](global.html#geom2) | the geometry to clone  
  
##### Returns:

new geometry

Type

     [geom2](global.html#geom2)

#### (static) create(sidesopt) → {[geom2](global.html#geom2)}

Source:

    

  * [modeling/src/geometries/geom2/create.js](modeling_src_geometries_geom2_create.js.html), [line 16](modeling_src_geometries_geom2_create.js.html#line16)

Create a new 2D geometry composed of unordered sides (two connected points).

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`sides` |  Array |  <optional>  
| list of sides where each side is an array of two points  
  
##### Returns:

a new geometry

Type

     [geom2](global.html#geom2)

#### (static) fromCompactBinary(data) → {[geom2](global.html#geom2)}

Source:

    

  * [modeling/src/geometries/geom2/fromCompactBinary.js](modeling_src_geometries_geom2_fromCompactBinary.js.html), [line 12](modeling_src_geometries_geom2_fromCompactBinary.js.html#line12)

Create a new 2D geometry from the given compact binary data.

##### Parameters:

Name | Type | Description  
---|---|---  
`data` |  Array | compact binary data  
  
##### Returns:

a new geometry

Type

     [geom2](global.html#geom2)

#### (static) fromPoints(points) → {[geom2](global.html#geom2)}

Source:

    

  * [modeling/src/geometries/geom2/fromPoints.js](modeling_src_geometries_geom2_fromPoints.js.html), [line 14](modeling_src_geometries_geom2_fromPoints.js.html#line14)

Create a new 2D geometry from the given points. The direction (rotation) of
the points is not relevant, as the points can define a convex or a concave
polygon. The geometry must not self intersect, i.e. the sides cannot cross.

##### Parameters:

Name | Type | Description  
---|---|---  
`points` |  Array | list of points in 2D space  
  
##### Returns:

a new geometry

Type

     [geom2](global.html#geom2)

#### (static) isA(object) → {Boolean}

Source:

    

  * [modeling/src/geometries/geom2/isA.js](modeling_src_geometries_geom2_isA.js.html), [line 7](modeling_src_geometries_geom2_isA.js.html#line7)

Determine if the given object is a 2D geometry.

##### Parameters:

Name | Type | Description  
---|---|---  
`object` |  Object | the object to interrogate  
  
##### Returns:

true, if the object matches a geom2 based object

Type

     Boolean

#### (static) reverse(geometry) → {[geom2](global.html#geom2)}

Source:

    

  * [modeling/src/geometries/geom2/reverse.js](modeling_src_geometries_geom2_reverse.js.html), [line 14](modeling_src_geometries_geom2_reverse.js.html#line14)

Reverses the given geometry so that the sides are flipped in the opposite
order. This swaps the left (interior) and right (exterior) edges.

##### Example

    
    
    let newgeometry = reverse(geometry)

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom2](global.html#geom2) | the geometry to reverse  
  
##### Returns:

the new reversed geometry

Type

     [geom2](global.html#geom2)

#### (static) toCompactBinary(geometry) → {TypedArray}

Source:

    

  * [modeling/src/geometries/geom2/toCompactBinary.js](modeling_src_geometries_geom2_toCompactBinary.js.html), [line 7](modeling_src_geometries_geom2_toCompactBinary.js.html#line7)

Produces a compact binary representation from the given geometry.

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom2](global.html#geom2) | the geometry  
  
##### Returns:

compact binary representation

Type

     TypedArray

#### (static) toOutlines(geometry) → {Array}

Source:

    

  * [modeling/src/geometries/geom2/toOutlines.js](modeling_src_geometries_geom2_toOutlines.js.html), [line 52](modeling_src_geometries_geom2_toOutlines.js.html#line52)

Create the outline(s) of the given geometry.

##### Example

    
    
    let geometry = subtract(rectangle({size: [5, 5]}), rectangle({size: [3, 3]}))
    let outlines = toOutlines(geometry) // returns two outlines

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom2](global.html#geom2) | geometry to create outlines from  
  
##### Returns:

an array of outlines, where each outline is an array of ordered points

Type

     Array

#### (static) toPoints(geometry) → {Array}

Source:

    

  * [modeling/src/geometries/geom2/toPoints.js](modeling_src_geometries_geom2_toPoints.js.html), [line 14](modeling_src_geometries_geom2_toPoints.js.html#line14)

Produces an array of points from the given geometry. The returned array should
not be modified as the points are shared with the geometry. NOTE: The points
returned do NOT define an order. Use toOutlines() for ordered points.

##### Example

    
    
    let sharedpoints = toPoints(geometry)

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom2](global.html#geom2) | the geometry  
  
##### Returns:

an array of points

Type

     Array

#### (static) toSides(geometry) → {Array}

Source:

    

  * [modeling/src/geometries/geom2/toSides.js](modeling_src_geometries_geom2_toSides.js.html), [line 14](modeling_src_geometries_geom2_toSides.js.html#line14)

Produces an array of sides from the given geometry. The returned array should
not be modified as the data is shared with the geometry. NOTE: The sides
returned do NOT define an order. Use toOutlines() for ordered points.

##### Example

    
    
    let sharedsides = toSides(geometry)

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom2](global.html#geom2) | the geometry  
  
##### Returns:

an array of sides

Type

     Array

#### (static) toString(geometry) → {String}

Source:

    

  * [modeling/src/geometries/geom2/toString.js](modeling_src_geometries_geom2_toString.js.html), [line 14](modeling_src_geometries_geom2_toString.js.html#line14)

Create a string representing the contents of the given geometry.

##### Example

    
    
    console.out(toString(geometry))

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom2](global.html#geom2) | the geometry  
  
##### Returns:

a representative string

Type

     String

#### (static) transform(matrix, geometry) → {[geom2](global.html#geom2)}

Source:

    

  * [modeling/src/geometries/geom2/transform.js](modeling_src_geometries_geom2_transform.js.html), [line 17](modeling_src_geometries_geom2_transform.js.html#line17)

Transform the given geometry using the given matrix. This is a lazy transform
of the sides, as this function only adjusts the transforms. The transforms are
applied when accessing the sides via toSides().

##### Example

    
    
    let newgeometry = transform(fromZRotation(degToRad(90)), geometry)

##### Parameters:

Name | Type | Description  
---|---|---  
`matrix` |  [mat4](global.html#mat4) | the matrix to transform with  
`geometry` |  [geom2](global.html#geom2) | the geometry to transform  
  
##### Returns:

a new geometry

Type

     [geom2](global.html#geom2)

#### (static) validate(object)

Source:

    

  * [modeling/src/geometries/geom2/validate.js](modeling_src_geometries_geom2_validate.js.html), [line 15](modeling_src_geometries_geom2_validate.js.html#line15)

Determine if the given object is a valid geom2. Checks for closedness, self-
edges, and valid data points.

**If the geometry is not valid, an exception will be thrown with details of
the geometry error.**

##### Parameters:

Name | Type | Description  
---|---|---  
`object` |  Object | the object to interrogate  
  
##### Throws:

error if the geometry is not valid

    

Type

     Error
    

