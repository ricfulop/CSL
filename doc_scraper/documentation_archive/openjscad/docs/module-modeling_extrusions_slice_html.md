---
url: https://openjscad.xyz/docs/module-modeling_extrusions_slice.html#.transform
scraped_at: 2025-09-08T16:29:53.305622
title: Untitled
---

Represents a 3D geometry consisting of a list of edges.

Source:

    

  * [modeling/src/operations/extrusions/slice/index.js](modeling_src_operations_extrusions_slice_index.js.html), [line 1](modeling_src_operations_extrusions_slice_index.js.html#line1)

See:

    

  * [slice](global.html#slice) for data structure information.

### Methods

#### (static) calculatePlane(slice) → {[plane](global.html#plane)}

Source:

    

  * [modeling/src/operations/extrusions/slice/calculatePlane.js](modeling_src_operations_extrusions_slice_calculatePlane.js.html), [line 14](modeling_src_operations_extrusions_slice_calculatePlane.js.html#line14)

Calculate the plane of the given slice. NOTE: The slice (and all points) are
assumed to be planar from the beginning.

##### Example

    
    
    let myplane = calculatePlane(slice)

##### Parameters:

Name | Type | Description  
---|---|---  
`slice` |  [slice](global.html#slice) | the slice  
  
##### Returns:

the plane of the slice

Type

     [plane](global.html#plane)

#### (static) clone(outopt, slice) → {[slice](global.html#slice)}

Source:

    

  * [modeling/src/operations/extrusions/slice/clone.js](modeling_src_operations_extrusions_slice_clone.js.html), [line 13](modeling_src_operations_extrusions_slice_clone.js.html#line13)

Create a deep clone of the given slice.

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`out` |  [slice](global.html#slice) |  <optional>  
| receiving slice  
`slice` |  [slice](global.html#slice) |  | slice to clone  
  
##### Returns:

a new slice

Type

     [slice](global.html#slice)

#### (static) create() → {[slice](global.html#slice)}

Source:

    

  * [modeling/src/operations/extrusions/slice/create.js](modeling_src_operations_extrusions_slice_create.js.html), [line 13](modeling_src_operations_extrusions_slice_create.js.html#line13)

Creates a new empty slice.

##### Returns:

a new slice

Type

     [slice](global.html#slice)

#### (static) equals(a, b) → {Boolean}

Source:

    

  * [modeling/src/operations/extrusions/slice/equals.js](modeling_src_operations_extrusions_slice_equals.js.html), [line 10](modeling_src_operations_extrusions_slice_equals.js.html#line10)

Determine if the given slices have the same edges.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [slice](global.html#slice) | the first slice to compare  
`b` |  [slice](global.html#slice) | the second slice to compare  
  
##### Returns:

true if the slices are equal

Type

     Boolean

#### (static) fromPoints(points) → {[slice](global.html#slice)}

Source:

    

  * [modeling/src/operations/extrusions/slice/fromPoints.js](modeling_src_operations_extrusions_slice_fromPoints.js.html), [line 20](modeling_src_operations_extrusions_slice_fromPoints.js.html#line20)

Create a slice from the given points.

##### Example

    
    
    const points = [
      [0,  0],
      [0, 10],
      [0, 10]
    ]
    const slice = fromPoints(points)

##### Parameters:

Name | Type | Description  
---|---|---  
`points` |  Array | list of points, where each point is either 2D or 3D  
  
##### Returns:

a new slice

Type

     [slice](global.html#slice)

#### (static) fromSides(sides) → {[slice](global.html#slice)}

Source:

    

  * [modeling/src/operations/extrusions/slice/fromSides.js](modeling_src_operations_extrusions_slice_fromSides.js.html), [line 16](modeling_src_operations_extrusions_slice_fromSides.js.html#line16)

Create a slice from the given sides (see geom2).

##### Example

    
    
    const myshape = circle({radius: 10})
    const slice = fromSides(geom2.toSides(myshape))

##### Parameters:

Name | Type | Description  
---|---|---  
`sides` |  Array | list of sides from geom2  
  
##### Returns:

a new slice

Type

     [slice](global.html#slice)

#### (static) isA(object) → {Boolean}

Source:

    

  * [modeling/src/operations/extrusions/slice/isA.js](modeling_src_operations_extrusions_slice_isA.js.html), [line 7](modeling_src_operations_extrusions_slice_isA.js.html#line7)

Determine if the given object is a slice.

##### Parameters:

Name | Type | Description  
---|---|---  
`object` |  [slice](global.html#slice) | the object to interrogate  
  
##### Returns:

true if the object matches a slice

Type

     Boolean

#### (static) reverse(outopt, slice) → {[slice](global.html#slice)}

Source:

    

  * [modeling/src/operations/extrusions/slice/reverse.js](modeling_src_operations_extrusions_slice_reverse.js.html), [line 11](modeling_src_operations_extrusions_slice_reverse.js.html#line11)

Reverse the edges of the given slice.

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`out` |  [slice](global.html#slice) |  <optional>  
| receiving slice  
`slice` |  [slice](global.html#slice) |  | slice to reverse  
  
##### Returns:

reverse of the slice

Type

     [slice](global.html#slice)

#### (static) toEdges(slice) → {Array}

Source:

    

  * [modeling/src/operations/extrusions/slice/toEdges.js](modeling_src_operations_extrusions_slice_toEdges.js.html), [line 11](modeling_src_operations_extrusions_slice_toEdges.js.html#line11)

Produces an array of edges from the given slice. The returned array should not
be modified as the data is shared with the slice.

##### Example

    
    
    let sharededges = toEdges(slice)

##### Parameters:

Name | Type | Description  
---|---|---  
`slice` |  [slice](global.html#slice) | the slice  
  
##### Returns:

an array of edges, each edge contains an array of two points (3D)

Type

     Array

#### (static) toPolygons(slice) → {Array}

Source:

    

  * [modeling/src/operations/extrusions/slice/toPolygons.js](modeling_src_operations_extrusions_slice_toPolygons.js.html), [line 11](modeling_src_operations_extrusions_slice_toPolygons.js.html#line11)

Return a list of polygons which are enclosed by the slice.

##### Parameters:

Name | Type | Description  
---|---|---  
`slice` |  [slice](global.html#slice) | the slice  
  
##### Returns:

a list of polygons (3D)

Type

     Array

#### (static) toString(slice) → {String}

Source:

    

  * [modeling/src/operations/extrusions/slice/toString.js](modeling_src_operations_extrusions_slice_toString.js.html), [line 13](modeling_src_operations_extrusions_slice_toString.js.html#line13)

##### Parameters:

Name | Type | Description  
---|---|---  
`slice` |  [slice](global.html#slice) | the slice  
  
##### Returns:

the string representation

Type

     String

#### (static) transform(matrix, slice) → {[slice](global.html#slice)}

Source:

    

  * [modeling/src/operations/extrusions/slice/transform.js](modeling_src_operations_extrusions_slice_transform.js.html), [line 16](modeling_src_operations_extrusions_slice_transform.js.html#line16)

Transform the given slice using the given matrix.

##### Example

    
    
    let matrix = mat4.fromTranslation([1, 2, 3])
    let newslice = transform(matrix, oldslice)

##### Parameters:

Name | Type | Description  
---|---|---  
`matrix` |  [mat4](global.html#mat4) | transform matrix  
`slice` |  [slice](global.html#slice) | slice to transform  
  
##### Returns:

the transformed slice

Type

     [slice](global.html#slice)

