---
url: https://openjscad.xyz/docs/module-modeling_geometries_path2.html#.validate
scraped_at: 2025-09-08T16:30:40.462244
title: Untitled
---

Represents a 2D geometry consisting of a list of ordered points.

Source:

    

  * [modeling/src/geometries/path2/index.js](modeling_src_geometries_path2_index.js.html), [line 1](modeling_src_geometries_path2_index.js.html#line1)

See:

    

  * [path2](global.html#path2) for data structure information.

##### Examples

    
    
    colorize([0,0,0,1], path2.fromPoints({ closed: true }, [[0,0], [4,0], [4,3]]))
    
    
    {
      "points": [[0,0], [4,0], [4,3]],
      "isClosed": true,
      "transforms": [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
      "color": [0,0,0,1]
    }

### Methods

#### (static) appendArc(options, geometry) → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/appendArc.js](modeling_src_geometries_path2_appendArc.js.html), [line 27](modeling_src_geometries_path2_appendArc.js.html#line27)

See:

    

  * <http://www.w3.org/TR/SVG/paths.html#PathDataEllipticalArcCommands>

Append a series of points to the given geometry that represent an arc. This
implementation follows the SVG specifications.

##### Example

    
    
    let p1 = path2.fromPoints({}, [[27.5,-22.96875]]);
    p1 = path2.appendPoints([[27.5,-3.28125]], p1);
    p1 = path2.appendArc({endpoint: [12.5, -22.96875], radius: [15, -19.6875]}, p1);

##### Parameters:

Name | Type | Description  
---|---|---  
`options` |  Object | options for construction

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`endpoint` |  [vec2](global.html#vec2) |  |  | end point of arc (REQUIRED)  
`radius` |  [vec2](global.html#vec2) |  <optional>  
|  `[0,0]` | radius of arc (X and Y)  
`xaxisrotation` |  Number |  <optional>  
|  `0` | rotation (RADIANS) of the X axis of the arc with respect to the X axis of the coordinate system  
`clockwise` |  Boolean |  <optional>  
|  `false` | draw an arc clockwise with respect to the center point  
`large` |  Boolean |  <optional>  
|  `false` | draw an arc longer than TAU / 2 radians  
`segments` |  Number |  <optional>  
|  `16` | number of segments per full rotation  
`geometry` |  [path2](global.html#path2) | the path of which to append the arc  
  
##### Returns:

a new path with the appended points

Type

     [path2](global.html#path2)

#### (static) appendBezier(options, geometry) → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/appendBezier.js](modeling_src_geometries_path2_appendBezier.js.html), [line 27](modeling_src_geometries_path2_appendBezier.js.html#line27)

Append a series of points to the given geometry that represent a Bezier curve.
The Bézier curve starts at the last point in the given geometry, and ends at
the last control point. The other control points are intermediate control
points to transition the curve from start to end points. The first control
point may be null to ensure a smooth transition occurs. In this case, the
second to last point of the given geometry is mirrored into the control points
of the Bezier curve. In other words, the trailing gradient of the geometry
matches the new gradient of the curve.

##### Example

    
    
    let p5 = path2.create({}, [[10,-20]])
    p5 = path2.appendBezier({controlPoints: [[10,-10],[25,-10],[25,-20]]}, p5);
    p5 = path2.appendBezier({controlPoints: [null, [25,-30],[40,-30],[40,-20]]}, p5)

##### Parameters:

Name | Type | Description  
---|---|---  
`options` |  Object | options for construction

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`controlPoints` |  Array |  |  | list of control points (2D) for the bezier curve  
`segment` |  Number |  <optional>  
|  `16` | number of segments per 360 rotation  
`geometry` |  [path2](global.html#path2) | the path of which to appended points  
  
##### Returns:

a new path with the appended points

Type

     [path2](global.html#path2)

#### (static) appendPoints(points, geometry) → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/appendPoints.js](modeling_src_geometries_path2_appendPoints.js.html), [line 13](modeling_src_geometries_path2_appendPoints.js.html#line13)

Append the given list of points to the end of the given geometry.

##### Example

    
    
    let newpath = appendPoints([[3, 4], [4, 5]], oldpath)

##### Parameters:

Name | Type | Description  
---|---|---  
`points` |  Array | the points (2D) to append to the given path  
`geometry` |  [path2](global.html#path2) | the given path  
  
##### Returns:

a new path with the appended points

Type

     [path2](global.html#path2)

#### (static) clone(geometry) → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/clone.js](modeling_src_geometries_path2_clone.js.html), [line 7](modeling_src_geometries_path2_clone.js.html#line7)

Performs a shallow clone of the give geometry.

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [path2](global.html#path2) | the geometry to clone  
  
##### Returns:

a new path

Type

     [path2](global.html#path2)

#### (static) close(geometry) → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/close.js](modeling_src_geometries_path2_close.js.html), [line 13](modeling_src_geometries_path2_close.js.html#line13)

Close the given geometry.

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [path2](global.html#path2) | the path to close  
  
##### Returns:

a new path

Type

     [path2](global.html#path2)

#### (static) concat(…paths) → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/concat.js](modeling_src_geometries_path2_concat.js.html), [line 20](modeling_src_geometries_path2_concat.js.html#line20)

Concatenate the given paths.

If both contain the same point at the junction, merge it into one. A
concatenation of zero paths is an empty, open path. A concatenation of one
closed path to a series of open paths produces a closed path. A concatenation
of a path to a closed path is an error.

##### Example

    
    
    let newpath = concat(fromPoints({}, [[1, 2]]), fromPoints({}, [[3, 4]]))

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`paths` |  [path2](global.html#path2) |  <repeatable>  
| the paths to concatenate  
  
##### Returns:

a new path

Type

     [path2](global.html#path2)

#### (static) create() → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/create.js](modeling_src_geometries_path2_create.js.html), [line 19](modeling_src_geometries_path2_create.js.html#line19)

Create an empty, open path.

##### Example

    
    
    let newpath = create()

##### Returns:

a new path

Type

     [path2](global.html#path2)

#### (static) equals(a, b) → {Boolean}

Source:

    

  * [modeling/src/geometries/path2/equals.js](modeling_src_geometries_path2_equals.js.html), [line 13](modeling_src_geometries_path2_equals.js.html#line13)

Determine if the given paths are equal. For closed paths, this includes
equality under point order rotation.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [path2](global.html#path2) | the first path to compare  
`b` |  [path2](global.html#path2) | the second path to compare  
  
##### Returns:

Type

     Boolean

#### (static) fromCompactBinary(data) → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/fromCompactBinary.js](modeling_src_geometries_path2_fromCompactBinary.js.html), [line 12](modeling_src_geometries_path2_fromCompactBinary.js.html#line12)

Create a new path from the given compact binary data.

##### Parameters:

Name | Type | Description  
---|---|---  
`data` |  TypedArray | compact binary data  
  
##### Returns:

a new path

Type

     [path2](global.html#path2)

#### (static) fromPoints(options, points) → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/fromPoints.js](modeling_src_geometries_path2_fromPoints.js.html), [line 21](modeling_src_geometries_path2_fromPoints.js.html#line21)

Create a new path from the given points. The points must be provided an array
of points, where each point is an array of two numbers.

##### Parameters:

Name | Type | Description  
---|---|---  
`options` |  Object | options for construction

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`closed` |  Boolean |  <optional>  
|  `false` | if the path should be open or closed  
`points` |  Array | array of points (2D) from which to create the path  
  
##### Returns:

a new path

Type

     [path2](global.html#path2)

#### (static) isA(object) → {Boolean}

Source:

    

  * [modeling/src/geometries/path2/isA.js](modeling_src_geometries_path2_isA.js.html), [line 7](modeling_src_geometries_path2_isA.js.html#line7)

Determine if the given object is a path2 geometry.

##### Parameters:

Name | Type | Description  
---|---|---  
`object` |  Object | the object to interrogate  
  
##### Returns:

true if the object matches a path2

Type

     Boolean

#### (static) reverse(geometry) → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/reverse.js](modeling_src_geometries_path2_reverse.js.html), [line 13](modeling_src_geometries_path2_reverse.js.html#line13)

Reverses the path so that the points are in the opposite order. This swaps the
left (interior) and right (exterior) edges.

##### Example

    
    
    let newpath = reverse(mypath)

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [path2](global.html#path2) | the path to reverse  
  
##### Returns:

a new path

Type

     [path2](global.html#path2)

#### (static) toCompactBinary(geometry) → {TypedArray}

Source:

    

  * [modeling/src/geometries/path2/toCompactBinary.js](modeling_src_geometries_path2_toCompactBinary.js.html), [line 7](modeling_src_geometries_path2_toCompactBinary.js.html#line7)

Produce a compact binary representation from the given path.

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [path2](global.html#path2) | the path geometry  
  
##### Returns:

compact binary representation

Type

     TypedArray

#### (static) toPoints(geometry) → {Array}

Source:

    

  * [modeling/src/geometries/path2/toPoints.js](modeling_src_geometries_path2_toPoints.js.html), [line 13](modeling_src_geometries_path2_toPoints.js.html#line13)

Produces an array of points from the given geometry. The returned array should
not be modified as the data is shared with the geometry.

##### Example

    
    
    let sharedpoints = toPoints(geometry)

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [path2](global.html#path2) | the geometry  
  
##### Returns:

an array of points

Type

     Array

#### (static) toString(geometry) → {String}

Source:

    

  * [modeling/src/geometries/path2/toString.js](modeling_src_geometries_path2_toString.js.html), [line 14](modeling_src_geometries_path2_toString.js.html#line14)

Create a string representing the contents of the given path.

##### Example

    
    
    console.out(toString(path))

##### Parameters:

Name | Type | Description  
---|---|---  
`geometry` |  [path2](global.html#path2) | the path  
  
##### Returns:

a representative string

Type

     String

#### (static) transform(matrix, geometry) → {[path2](global.html#path2)}

Source:

    

  * [modeling/src/geometries/path2/transform.js](modeling_src_geometries_path2_transform.js.html), [line 15](modeling_src_geometries_path2_transform.js.html#line15)

Transform the given geometry using the given matrix. This is a lazy transform
of the points, as this function only adjusts the transforms. The transforms
are applied when accessing the points via toPoints().

##### Example

    
    
    let newpath = transform(fromZRotation(TAU / 8), path)

##### Parameters:

Name | Type | Description  
---|---|---  
`matrix` |  [mat4](global.html#mat4) | the matrix to transform with  
`geometry` |  [path2](global.html#path2) | the geometry to transform  
  
##### Returns:

a new path

Type

     [path2](global.html#path2)

#### (static) validate(object)

Source:

    

  * [modeling/src/geometries/path2/validate.js](modeling_src_geometries_path2_validate.js.html), [line 14](modeling_src_geometries_path2_validate.js.html#line14)

Determine if the given object is a valid path2. Checks for valid data points,
and duplicate points.

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
    

