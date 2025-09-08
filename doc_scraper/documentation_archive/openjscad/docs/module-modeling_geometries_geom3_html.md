---
url: https://openjscad.xyz/docs/module-modeling_geometries_geom3.html#.validate
scraped_at: 2025-09-08T16:30:22.381257
title: Untitled
---

Represents a 3D geometry consisting of a list of polygons.

Source:

    

  * [modeling/src/geometries/geom3/index.js](modeling_src_geometries_geom3_index.js.html), [line 1](modeling_src_geometries_geom3_index.js.html#line1)

See:

    

  * [geom3](global.html#geom3) for data structure information.

##### Examples

    
    
    colorize([0,0.5,1,0.6], cube()) // transparent ice cube
    
    
    {
      "polygons": [
        {"vertices": [[-1,-1,-1], [-1,-1,1], [-1,1,1], [-1,1,-1]]},
        {"vertices": [[1,-1,-1], [1,1,-1], [1,1,1], [1,-1,1]]},
        {"vertices": [[-1,-1,-1], [1,-1,-1], [1,-1,1], [-1,-1,1]]},
        {"vertices": [[-1,1,-1], [-1,1,1], [1,1,1], [1,1,-1]]},
        {"vertices": [[-1,-1,-1], [-1,1,-1], [1,1,-1], [1,-1,-1]]},
        {"vertices": [[-1,-1,1], [1,-1,1], [1,1,1], [-1,1,1]]}
      ],
      "transforms": [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
      "color": [0,0.5,1,0.6]
    }

### Methods

#### (static) clone(geometry) → {[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/geometries/geom3/clone.js](modeling_src_geometries_geom3_clone.js.html), [line 7](modeling_src_geometries_geom3_clone.js.html#line7)

Performs a shallow clone of the given geometry.

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom3](global.html#geom3) | the geometry to clone  
  
##### Returns:

a new geometry

Type

     [geom3](global.html#geom3)

#### (static) create(polygonsopt) → {[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/geometries/geom3/create.js](modeling_src_geometries_geom3_create.js.html), [line 16](modeling_src_geometries_geom3_create.js.html#line16)

Create a new 3D geometry composed of the given polygons.

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`polygons` |  Array |  <optional>  
| list of polygons, or undefined  
  
##### Returns:

a new geometry

Type

     [geom3](global.html#geom3)

#### (static) fromCompactBinary(data) → {[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/geometries/geom3/fromCompactBinary.js](modeling_src_geometries_geom3_fromCompactBinary.js.html), [line 14](modeling_src_geometries_geom3_fromCompactBinary.js.html#line14)

Construct a new 3D geometry from the given compact binary data.

##### Parameters:

Name | Type | Description  
---|---|---  
`data` |  TypedArray | compact binary data  
  
##### Returns:

a new geometry

Type

     [geom3](global.html#geom3)

#### (static) fromPoints(listofpoints) → {[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/geometries/geom3/fromPoints.js](modeling_src_geometries_geom3_fromPoints.js.html), [line 14](modeling_src_geometries_geom3_fromPoints.js.html#line14)

Construct a new 3D geometry from a list of points. The list of points should
contain sub-arrays, each defining a single polygon of points. In addition, the
points should follow the right-hand rule for rotation in order to define an
external facing polygon.

##### Parameters:

Name | Type | Description  
---|---|---  
`listofpoints` |  Array | list of lists, where each list is a set of points to construct a polygon  
  
##### Returns:

a new geometry

Type

     [geom3](global.html#geom3)

#### (static) fromPointsConvex(uniquePoints) → {[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/geometries/geom3/fromPointsConvex.js](modeling_src_geometries_geom3_fromPointsConvex.js.html), [line 11](modeling_src_geometries_geom3_fromPointsConvex.js.html#line11)

Construct a new convex 3D geometry from a list of unique points.

##### Parameters:

Name | Type | Description  
---|---|---  
`uniquePoints` |  Array | list of points to construct convex 3D geometry  
  
##### Returns:

a new geometry

Type

     [geom3](global.html#geom3)

#### (static) invert(geometry) → {[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/geometries/geom3/invert.js](modeling_src_geometries_geom3_invert.js.html), [line 12](modeling_src_geometries_geom3_invert.js.html#line12)

Invert the given geometry, transposing solid and empty space.

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom3](global.html#geom3) | the geometry to invert  
  
##### Returns:

a new geometry

Type

     [geom3](global.html#geom3)

#### (static) isA(object) → {Boolean}

Source:

    

  * [modeling/src/geometries/geom3/isA.js](modeling_src_geometries_geom3_isA.js.html), [line 7](modeling_src_geometries_geom3_isA.js.html#line7)

Determine if the given object is a 3D geometry.

##### Parameters:

Name | Type | Description  
---|---|---  
`object` |  Object | the object to interrogate  
  
##### Returns:

true if the object matches a geom3

Type

     Boolean

#### (static) toCompactBinary(geometry) → {TypedArray}

Source:

    

  * [modeling/src/geometries/geom3/toCompactBinary.js](modeling_src_geometries_geom3_toCompactBinary.js.html), [line 9](modeling_src_geometries_geom3_toCompactBinary.js.html#line9)

Return the given geometry in compact binary representation.

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom3](global.html#geom3) | the geometry  
  
##### Returns:

compact binary representation

Type

     TypedArray

#### (static) toPoints(geometry) → {Array}

Source:

    

  * [modeling/src/geometries/geom3/toPoints.js](modeling_src_geometries_geom3_toPoints.js.html), [line 12](modeling_src_geometries_geom3_toPoints.js.html#line12)

Return the given geometry as a list of points, after applying transforms. The
returned array should not be modified as the points are shared with the
geometry.

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom3](global.html#geom3) | the geometry  
  
##### Returns:

list of points, where each sub-array represents a polygon

Type

     Array

#### (static) toPolygons(geometry) → {Array}

Source:

    

  * [modeling/src/geometries/geom3/toPolygons.js](modeling_src_geometries_geom3_toPolygons.js.html), [line 13](modeling_src_geometries_geom3_toPolygons.js.html#line13)

Produces an array of polygons from the given geometry, after applying
transforms. The returned array should not be modified as the polygons are
shared with the geometry.

##### Example

    
    
    let sharedpolygons = toPolygons(geometry)

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom3](global.html#geom3) | the geometry  
  
##### Returns:

an array of polygons

Type

     Array

#### (static) toString(geometry) → {String}

Source:

    

  * [modeling/src/geometries/geom3/toString.js](modeling_src_geometries_geom3_toString.js.html), [line 14](modeling_src_geometries_geom3_toString.js.html#line14)

Create a string representing the contents of the given geometry.

##### Example

    
    
    console.out(toString(geometry))

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [geom3](global.html#geom3) | the geometry  
  
##### Returns:

a representative string

Type

     String

#### (static) transform(matrix, geometry) → {[geom3](global.html#geom3)}

Source:

    

  * [modeling/src/geometries/geom3/transform.js](modeling_src_geometries_geom3_transform.js.html), [line 15](modeling_src_geometries_geom3_transform.js.html#line15)

Transform the given geometry using the given matrix. This is a lazy transform
of the polygons, as this function only adjusts the transforms. See
applyTransforms() for the actual application of the transforms to the
polygons.

##### Example

    
    
    let newgeometry = transform(fromXRotation(degToRad(90)), geometry)

##### Parameters:

Name | Type | Description  
---|---|---  
`matrix` |  [mat4](global.html#mat4) | the matrix to transform with  
`geometry` |  [geom3](global.html#geom3) | the geometry to transform  
  
##### Returns:

a new geometry

Type

     [geom3](global.html#geom3)

#### (static) validate(object)

Source:

    

  * [modeling/src/geometries/geom3/validate.js](modeling_src_geometries_geom3_validate.js.html), [line 14](modeling_src_geometries_geom3_validate.js.html#line14)

Determine if the given object is a valid 3D geometry. Checks for valid data
structure, convex polygon faces, and manifold edges.

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
    

