---
url: https://openjscad.xyz/docs/module-modeling_geometries_poly3.html#.validate
scraped_at: 2025-09-08T16:31:00.541869
title: Untitled
---

Represents a convex 3D polygon consisting of a list of ordered vertices.

Source:

    

  * [modeling/src/geometries/poly3/index.js](modeling_src_geometries_poly3_index.js.html), [line 1](modeling_src_geometries_poly3_index.js.html#line1)

See:

    

  * [poly3](global.html#poly3) for data structure information.

##### Examples

    
    
    poly3.create([[0,0,0], [4,0,0], [4,3,12]])
    
    
    {"vertices": [[0,0,0], [4,0,0], [4,3,12]]}

### Methods

#### (static) clone(outopt, polygon) → {[poly3](global.html#poly3)}

Source:

    

  * [modeling/src/geometries/poly3/clone.js](modeling_src_geometries_poly3_clone.js.html), [line 13](modeling_src_geometries_poly3_clone.js.html#line13)

Create a deep clone of the given polygon

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`out` |  [poly3](global.html#poly3) |  <optional>  
| receiving polygon  
`polygon` |  [poly3](global.html#poly3) |  | polygon to clone  
  
##### Returns:

a new polygon

Type

     [poly3](global.html#poly3)

#### (static) create(verticesopt) → {[poly3](global.html#poly3)}

Source:

    

  * [modeling/src/geometries/poly3/create.js](modeling_src_geometries_poly3_create.js.html), [line 17](modeling_src_geometries_poly3_create.js.html#line17)

Creates a new 3D polygon with initial values.

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`vertices` |  Array |  <optional>  
| a list of vertices (3D)  
  
##### Returns:

a new polygon

Type

     [poly3](global.html#poly3)

#### (static) fromPoints(points) → {[poly3](global.html#poly3)}

Source:

    

  * [modeling/src/geometries/poly3/fromPoints.js](modeling_src_geometries_poly3_fromPoints.js.html), [line 20](modeling_src_geometries_poly3_fromPoints.js.html#line20)

Create a polygon from the given points.

##### Example

    
    
    const points = [
      [0,  0, 0],
      [0, 10, 0],
      [0, 10, 10]
    ]
    const polygon = fromPoints(points)

##### Parameters:

Name | Type | Description  
---|---|---  
`points` |  Array | list of points (3D)  
  
##### Returns:

a new polygon

Type

     [poly3](global.html#poly3)

#### (static) fromPointsAndPlane(vertices, plane) →
{[poly3](global.html#poly3)}

Source:

    

  * [modeling/src/geometries/poly3/fromPointsAndPlane.js](modeling_src_geometries_poly3_fromPointsAndPlane.js.html), [line 11](modeling_src_geometries_poly3_fromPointsAndPlane.js.html#line11)

Create a polygon from the given vertices and plane. NOTE: No checks are
performed on the parameters.

##### Parameters:

Name | Type | Description  
---|---|---  
`vertices` |  Array | list of vertices (3D)  
`plane` |  [plane](global.html#plane) | plane of the polygon  
  
##### Returns:

a new polygon

Type

     [poly3](global.html#poly3)

#### (static) invert(polygon) → {[poly3](global.html#poly3)}

Source:

    

  * [modeling/src/geometries/poly3/invert.js](modeling_src_geometries_poly3_invert.js.html), [line 11](modeling_src_geometries_poly3_invert.js.html#line11)

Invert the give polygon to face the opposite direction.

##### Parameters:

Name | Type | Description  
---|---|---  
`polygon` |  [poly3](global.html#poly3) | the polygon to invert  
  
##### Returns:

a new poly3

Type

     [poly3](global.html#poly3)

#### (static) isA(object) → {Boolean}

Source:

    

  * [modeling/src/geometries/poly3/isA.js](modeling_src_geometries_poly3_isA.js.html), [line 7](modeling_src_geometries_poly3_isA.js.html#line7)

Determine if the given object is a polygon.

##### Parameters:

Name | Type | Description  
---|---|---  
`object` |  Object | the object to interrogate  
  
##### Returns:

true if the object matches a poly3

Type

     Boolean

#### (static) isConvex(polygon) → {Boolean}

Source:

    

  * [modeling/src/geometries/poly3/isConvex.js](modeling_src_geometries_poly3_isConvex.js.html), [line 10](modeling_src_geometries_poly3_isConvex.js.html#line10)

Check whether the given polygon is convex.

##### Parameters:

Name | Type | Description  
---|---|---  
`polygon` |  [poly3](global.html#poly3) | the polygon to interrogate  
  
##### Returns:

true if convex

Type

     Boolean

#### (static) measureArea(polygon) → {Number}

Source:

    

  * [modeling/src/geometries/poly3/measureArea.js](modeling_src_geometries_poly3_measureArea.js.html), [line 10](modeling_src_geometries_poly3_measureArea.js.html#line10)

See:

    

  * 2000 softSurfer http://geomalgorithms.com

Measure the area of the given polygon.

##### Parameters:

Name | Type | Description  
---|---|---  
`polygon` |  [poly3](global.html#poly3) | the polygon to measure  
  
##### Returns:

area of the polygon

Type

     Number

#### (static) measureBoundingBox(polygon) → {Array}

Source:

    

  * [modeling/src/geometries/poly3/measureBoundingBox.js](modeling_src_geometries_poly3_measureBoundingBox.js.html), [line 8](modeling_src_geometries_poly3_measureBoundingBox.js.html#line8)

##### Parameters:

Name | Type | Description  
---|---|---  
`polygon` |  [poly3](global.html#poly3) | the polygon to measure  
  
##### Returns:

an array of two vectors (3D); minimum and maximum coordinates

Type

     Array

#### (static) measureBoundingSphere(polygon) → {[vec4](global.html#vec4)}

Source:

    

  * [modeling/src/geometries/poly3/measureBoundingSphere.js](modeling_src_geometries_poly3_measureBoundingSphere.js.html), [line 11](modeling_src_geometries_poly3_measureBoundingSphere.js.html#line11)

Measure the bounding sphere of the given polygon.

##### Parameters:

Name | Type | Description  
---|---|---  
`polygon` |  [poly3](global.html#poly3) | the polygon to measure  
  
##### Returns:

the computed bounding sphere; center point (3D) and radius

Type

     [vec4](global.html#vec4)

#### (static) measureSignedVolume(polygon) → {Number}

Source:

    

  * [modeling/src/geometries/poly3/measureSignedVolume.js](modeling_src_geometries_poly3_measureSignedVolume.js.html), [line 12](modeling_src_geometries_poly3_measureSignedVolume.js.html#line12)

See:

    

  * <http://chenlab.ece.cornell.edu/Publication/Cha/icip01_Cha.pdf>

Measure the signed volume of the given polygon, which must be convex. The
volume is that formed by the tetrahedron connected to the axis [0,0,0], and
will be positive or negative based on the rotation of the vertices.

##### Parameters:

Name | Type | Description  
---|---|---  
`polygon` |  [poly3](global.html#poly3) | the polygon to measure  
  
##### Returns:

volume of the polygon

Type

     Number

#### (static) toPoints(polygon) → {Array}

Source:

    

  * [modeling/src/geometries/poly3/toPoints.js](modeling_src_geometries_poly3_toPoints.js.html), [line 8](modeling_src_geometries_poly3_toPoints.js.html#line8)

Return the given polygon as a list of points. NOTE: The returned array should
not be modified as the points are shared with the geometry.

##### Parameters:

Name | Type | Description  
---|---|---  
`polygon` |  [poly3](global.html#poly3) | the polygon  
  
##### Returns:

list of points (3D)

Type

     Array

#### (static) toString(polygon) → {String}

Source:

    

  * [modeling/src/geometries/poly3/toString.js](modeling_src_geometries_poly3_toString.js.html), [line 8](modeling_src_geometries_poly3_toString.js.html#line8)

##### Parameters:

Name | Type | Description  
---|---|---  
`polygon` |  [poly3](global.html#poly3) | the polygon to measure  
  
##### Returns:

the string representation

Type

     String

#### (static) transform(matrix, polygon) → {[poly3](global.html#poly3)}

Source:

    

  * [modeling/src/geometries/poly3/transform.js](modeling_src_geometries_poly3_transform.js.html), [line 13](modeling_src_geometries_poly3_transform.js.html#line13)

Transform the given polygon using the given matrix.

##### Parameters:

Name | Type | Description  
---|---|---  
`matrix` |  [mat4](global.html#mat4) | the matrix to transform with  
`polygon` |  [poly3](global.html#poly3) | the polygon to transform  
  
##### Returns:

a new polygon

Type

     [poly3](global.html#poly3)

#### (static) validate(object)

Source:

    

  * [modeling/src/geometries/poly3/validate.js](modeling_src_geometries_poly3_validate.js.html), [line 19](modeling_src_geometries_poly3_validate.js.html#line19)

Determine if the given object is a valid polygon. Checks for valid data
structure, convex polygons, and duplicate points.

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
    

