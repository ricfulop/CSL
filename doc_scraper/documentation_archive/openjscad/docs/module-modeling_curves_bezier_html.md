---
url: https://openjscad.xyz/docs/module-modeling_curves_bezier.html#.valueAt
scraped_at: 2025-09-08T16:29:30.150038
title: Untitled
---

Represents a bezier easing function.

Source:

    

  * [modeling/src/curves/bezier/index.js](modeling_src_curves_bezier_index.js.html), [line 1](modeling_src_curves_bezier_index.js.html#line1)

See:

    

  * [bezier](global.html#bezier) for data structure information.

### Methods

#### (static) arcLengthToT(optionsopt, bezier)

Source:

    

  * [modeling/src/curves/bezier/arcLengthToT.js](modeling_src_curves_bezier_arcLengthToT.js.html), [line 25](modeling_src_curves_bezier_arcLengthToT.js.html#line25)

Convert a given arc length along a bezier curve to a t value. Useful for
generating equally spaced points along a bezier curve.

##### Example

    
    
    const points = [];
    const segments = 9; // this will generate 10 equally spaced points
    const increment = bezier.length(100, bezierCurve) / segments;
    for(let i = 0; i <= segments; i++) {
      const t = bezier.arcLengthToT({distance: i * increment}, bezierCurve);
      const point = bezier.valueAt(t, bezierCurve);
      points.push(point);
    }
    return points;

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`options` |  Object |  <optional>  
| options for construction

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`distance` |  Number |  <optional>  
|  `0` | the distance along the bezier curve for which we want to find the corresponding t value.  
`segments` |  Number |  <optional>  
|  `100` | the number of segments to use when approximating the curve length.  
`bezier` |  Object |  | a bezier curve.  
  
##### Returns:

a number in the [0, 1] interval or NaN if the arcLength is negative or greater
than the total length of the curve.

#### (static) create(points) → {[bezier](global.html#bezier)}

Source:

    

  * [modeling/src/curves/bezier/create.js](modeling_src_curves_bezier_create.js.html), [line 28](modeling_src_curves_bezier_create.js.html#line28)

Creates an object representing a bezier easing curve. Curves can have both an
arbitrary number of control points, and an arbitrary number of dimensions.

##### Example

    
    
    const b = bezier.create([0,10]) // a linear progression from 0 to 10
    const b = bezier.create([0, 0, 10, 10]) // a symmetrical cubic easing curve that starts slowly and ends slowly from 0 to 10
    const b = bezier.create([0,0,0], [0,5,10], [10,0,-5], [10,10,10]]) // a cubic 3 dimensional easing curve that can generate position arrays for modelling
    // Usage
    let position = bezier.valueAt(t,b) // where 0 < t < 1
    let tangent = bezier.tangentAt(t,b) // where 0 < t < 1

##### Parameters:

Name | Type | Description  
---|---|---  
`points` |  Array | An array with at least 2 elements of either all numbers, or all arrays of numbers that are the same size.  
  
##### Returns:

a new bezier data object

Type

     [bezier](global.html#bezier)

#### (static) length(segments, bezier)

Source:

    

  * [modeling/src/curves/bezier/length.js](modeling_src_curves_bezier_length.js.html), [line 16](modeling_src_curves_bezier_length.js.html#line16)

Approximates the length of the bezier curve by sampling it at a sequence of
points, then adding up all the distances. This is equivalent to flattening the
curve into lines and adding up all the line lengths.

##### Example

    
    
    const b = bezier.create([[0, 0], [0, 10]]);
    console.log(length(100, b)) // output 10

##### Parameters:

Name | Type | Description  
---|---|---  
`segments` |  Number | the number of segments to use when approximating the curve length.  
`bezier` |  Object | a bezier curve.  
  
##### Returns:

an approximation of the curve's length.

#### (static) tangentAt(t, bezier) → {array|number}

Source:

    

  * [modeling/src/curves/bezier/tangentAt.js](modeling_src_curves_bezier_tangentAt.js.html), [line 15](modeling_src_curves_bezier_tangentAt.js.html#line15)

Calculates the tangent at a specific position along a bezier easing curve. For
multidimensional curves, the tangent is the slope of each dimension at that
point. See the example called extrudeAlongPath.js

##### Example

    
    
    const b = bezier.create([[0,0,0], [0,5,10], [10,0,-5], [10,10,10]]) // a cubic 3 dimensional easing curve that can generate position arrays for modelling
    let tangent = bezier.tangentAt(t, b)

##### Parameters:

Name | Type | Description  
---|---|---  
`t` |  number | : the position of which to calculate the bezier's tangent value; 0 < t < 1  
`bezier` |  Object | : an array with at least 2 elements of either all numbers, or all arrays of numbers that are the same size.  
  
##### Returns:

the tangent at the requested position.

Type

     array | number

#### (static) valueAt(t, bezier) → {array|number}

Source:

    

  * [modeling/src/curves/bezier/valueAt.js](modeling_src_curves_bezier_valueAt.js.html), [line 16](modeling_src_curves_bezier_valueAt.js.html#line16)

Calculates the value at a specific position along a bezier easing curve. For
multidimensional curves, the tangent is the slope of each dimension at that
point. See the example called extrudeAlongPath.js to see this in use. Math and
explanation comes from <https://www.freecodecamp.org/news/nerding-out-with-
bezier-curves-6e3c0bc48e2f/>

##### Example

    
    
    const b = bezier.create([0,0,0], [0,5,10], [10,0,-5], [10,10,10]]) // a cubic 3 dimensional easing curve that can generate position arrays for modelling
    let position = bezier.valueAt(t,b) // where 0 < t < 1

##### Parameters:

Name | Type | Description  
---|---|---  
`t` |  number | : the position of which to calculate the value; 0 < t < 1  
`bezier` |  Object | : a bezier curve created with bezier.create().  
  
##### Returns:

the value at the requested position.

Type

     array | number

