---
url: https://openjscad.xyz/docs/module-modeling_maths_vec3.html#.transform
scraped_at: 2025-09-08T16:33:37.284803
title: Untitled
---

Represents a three dimensional vector.

Source:

    

  * [modeling/src/maths/vec3/index.js](modeling_src_maths_vec3_index.js.html), [line 1](modeling_src_maths_vec3_index.js.html#line1)

See:

    

  * [vec3](global.html#vec3) for data structure information.

### Methods

#### (static) abs(out, vector) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/abs.js](modeling_src_maths_vec3_abs.js.html), [line 9](modeling_src_maths_vec3_abs.js.html#line9)

Calculates the absolute coordinates of the give vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector of reference  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) add(out, a, b) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/add.js](modeling_src_maths_vec3_add.js.html), [line 10](modeling_src_maths_vec3_add.js.html#line10)

Adds the coordinates of two vectors (A+B).

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) angle(a, b) → {Number}

Source:

    

  * [modeling/src/maths/vec3/angle.js](modeling_src_maths_vec3_angle.js.html), [line 11](modeling_src_maths_vec3_angle.js.html#line11)

Calculate the angle between two vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
  
##### Returns:

angle (radians)

Type

     Number

#### (static) clone(vector) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/clone.js](modeling_src_maths_vec3_clone.js.html), [line 10](modeling_src_maths_vec3_clone.js.html#line10)

Create a clone of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec3](global.html#vec3) | vector to clone  
  
##### Returns:

a new vector

Type

     [vec3](global.html#vec3)

#### (static) copy(out, vector) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/copy.js](modeling_src_maths_vec3_copy.js.html), [line 9](modeling_src_maths_vec3_copy.js.html#line9)

Create a copy of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector to copy  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) create() → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/create.js](modeling_src_maths_vec3_create.js.html), [line 13](modeling_src_maths_vec3_create.js.html#line13)

Creates a new vector initialized to [0,0,0].

##### Returns:

a new vector

Type

     [vec3](global.html#vec3)

#### (static) cross(out, a, b) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/cross.js](modeling_src_maths_vec3_cross.js.html), [line 10](modeling_src_maths_vec3_cross.js.html#line10)

Computes the cross product of the given vectors (AxB).

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) distance(a, b) → {Number}

Source:

    

  * [modeling/src/maths/vec3/distance.js](modeling_src_maths_vec3_distance.js.html), [line 9](modeling_src_maths_vec3_distance.js.html#line9)

Calculates the Euclidian distance between the given vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
  
##### Returns:

distance

Type

     Number

#### (static) divide(out, a, b) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/divide.js](modeling_src_maths_vec3_divide.js.html), [line 10](modeling_src_maths_vec3_divide.js.html#line10)

Divides the coordinates of two vectors (A/B).

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`a` |  [vec3](global.html#vec3) | dividend vector  
`b` |  [vec3](global.html#vec3) | divisor vector  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) dot(a, b) → {Number}

Source:

    

  * [modeling/src/maths/vec3/dot.js](modeling_src_maths_vec3_dot.js.html), [line 9](modeling_src_maths_vec3_dot.js.html#line9)

Calculates the dot product of two vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
  
##### Returns:

dot product

Type

     Number

#### (static) equals(a, b) → {Boolean}

Source:

    

  * [modeling/src/maths/vec3/equals.js](modeling_src_maths_vec3_equals.js.html), [line 9](modeling_src_maths_vec3_equals.js.html#line9)

Compare the given vectors for equality.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
  
##### Returns:

true if a and b are equal

Type

     Boolean

#### (static) fromScalar(out, scalar) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/fromScalar.js](modeling_src_maths_vec3_fromScalar.js.html), [line 10](modeling_src_maths_vec3_fromScalar.js.html#line10)

Creates a vector from a single scalar value. All components of the resulting
vector have the given value.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`scalar` |  Number |   
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) fromValues(x, y, z) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/fromValues.js](modeling_src_maths_vec3_fromValues.js.html), [line 12](modeling_src_maths_vec3_fromValues.js.html#line12)

Creates a new vector initialized with the given values.

##### Parameters:

Name | Type | Description  
---|---|---  
`x` |  Number | X component  
`y` |  Number | Y component  
`z` |  Number | Z component  
  
##### Returns:

a new vector

Type

     [vec3](global.html#vec3)

#### (static) fromVec2(out, vector, zopt) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/fromVec2.js](modeling_src_maths_vec3_fromVec2.js.html), [line 10](modeling_src_maths_vec3_fromVec2.js.html#line10)

Create a new vector by extending a 2D vector with a Z value.

##### Parameters:

Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`out` |  [vec3](global.html#vec3) |  |  | receiving vector  
`vector` |  Array |  |  | 2D vector of values  
`z` |  Number |  <optional>  
|  `0` | Z value  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) length(vector) → {Number}

Source:

    

  * [modeling/src/maths/vec3/length.js](modeling_src_maths_vec3_length.js.html), [line 8](modeling_src_maths_vec3_length.js.html#line8)

Calculates the length of a vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec3](global.html#vec3) | vector to calculate length of  
  
##### Returns:

length

Type

     Number

#### (static) lerp(out, a, b, t) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/lerp.js](modeling_src_maths_vec3_lerp.js.html), [line 11](modeling_src_maths_vec3_lerp.js.html#line11)

Performs a linear interpolation between two vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
`t` |  Number | interpolant (0.0 to 1.0) applied between the two inputs  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) max(out, a, b) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/max.js](modeling_src_maths_vec3_max.js.html), [line 10](modeling_src_maths_vec3_max.js.html#line10)

Returns the maximum coordinates of the given vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) min(out, a, b) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/min.js](modeling_src_maths_vec3_min.js.html), [line 10](modeling_src_maths_vec3_min.js.html#line10)

Returns the minimum coordinates of the given vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) multiply(out, a, b) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/multiply.js](modeling_src_maths_vec3_multiply.js.html), [line 10](modeling_src_maths_vec3_multiply.js.html#line10)

Multiply the coordinates of the given vectors (A*B).

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) negate(out, vector) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/negate.js](modeling_src_maths_vec3_negate.js.html), [line 9](modeling_src_maths_vec3_negate.js.html#line9)

Negates the coordinates of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector to negate  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) normalize(out, vector) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/normalize.js](modeling_src_maths_vec3_normalize.js.html), [line 9](modeling_src_maths_vec3_normalize.js.html#line9)

Normalize the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector to normalize  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) orthogonal(out, vector) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/orthogonal.js](modeling_src_maths_vec3_orthogonal.js.html), [line 13](modeling_src_maths_vec3_orthogonal.js.html#line13)

Create a new vector that is orthogonal to the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector of reference  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) rotateX(out, vector, origin, radians) →
{[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/rotateX.js](modeling_src_maths_vec3_rotateX.js.html), [line 11](modeling_src_maths_vec3_rotateX.js.html#line11)

Rotate the given vector around the given origin, X axis only.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector to rotate  
`origin` |  [vec3](global.html#vec3) | origin of the rotation  
`radians` |  Number | angle of rotation  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) rotateY(out, vector, origin, radians) →
{[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/rotateY.js](modeling_src_maths_vec3_rotateY.js.html), [line 11](modeling_src_maths_vec3_rotateY.js.html#line11)

Rotate the given vector around the given origin, Y axis only.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector to rotate  
`origin` |  [vec3](global.html#vec3) | origin of the rotation  
`radians` |  Number | angle of rotation  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) rotateZ(out, vector, origin, radians) →
{[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/rotateZ.js](modeling_src_maths_vec3_rotateZ.js.html), [line 11](modeling_src_maths_vec3_rotateZ.js.html#line11)

Rotate the given vector around the given origin, Z axis only.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector to rotate  
`origin` |  [vec3](global.html#vec3) | origin of the rotation  
`radians` |  Number | angle of rotation in radians  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) scale(out, vector, amount) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/scale.js](modeling_src_maths_vec3_scale.js.html), [line 10](modeling_src_maths_vec3_scale.js.html#line10)

Scales the coordinates of the given vector by a scalar number.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector to scale  
`amount` |  Number | amount to scale the vector by  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) snap(out, vector, epsilon) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/snap.js](modeling_src_maths_vec3_snap.js.html), [line 10](modeling_src_maths_vec3_snap.js.html#line10)

Snaps the coordinates of the given vector to the given epsilon.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector to snap  
`epsilon` |  Number | epsilon of precision, less than 0  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) squaredDistance(a, b) → {Number}

Source:

    

  * [modeling/src/maths/vec3/squaredDistance.js](modeling_src_maths_vec3_squaredDistance.js.html), [line 9](modeling_src_maths_vec3_squaredDistance.js.html#line9)

Calculates the squared distance between two vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [vec3](global.html#vec3) | first operand  
`b` |  [vec3](global.html#vec3) | second operand  
  
##### Returns:

squared distance

Type

     Number

#### (static) squaredLength(vector) → {Number}

Source:

    

  * [modeling/src/maths/vec3/squaredLength.js](modeling_src_maths_vec3_squaredLength.js.html), [line 8](modeling_src_maths_vec3_squaredLength.js.html#line8)

Calculates the squared length of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec3](global.html#vec3) | vector to calculate squared length of  
  
##### Returns:

squared length

Type

     Number

#### (static) subtract(out, a, b) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/subtract.js](modeling_src_maths_vec3_subtract.js.html), [line 10](modeling_src_maths_vec3_subtract.js.html#line10)

Subtracts the coordinates of two vectors (A-B).

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`a` |  [vec3](global.html#vec3) | minuend vector  
`b` |  [vec3](global.html#vec3) | subtrahend vector  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) toString(vec) → {String}

Source:

    

  * [modeling/src/maths/vec3/toString.js](modeling_src_maths_vec3_toString.js.html), [line 7](modeling_src_maths_vec3_toString.js.html#line7)

Convert the given vector to a representative string.

##### Parameters:

Name | Type | Description  
---|---|---  
`vec` |  [vec3](global.html#vec3) | vector of reference  
  
##### Returns:

string representation

Type

     String

#### (static) transform(out, vector, matrix) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec3/transform.js](modeling_src_maths_vec3_transform.js.html), [line 10](modeling_src_maths_vec3_transform.js.html#line10)

Transforms the given vector using the given matrix.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector  
`vector` |  [vec3](global.html#vec3) | vector to transform  
`matrix` |  [mat4](global.html#mat4) | transform matrix  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

