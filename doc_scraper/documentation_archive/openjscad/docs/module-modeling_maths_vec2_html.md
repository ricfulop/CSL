---
url: https://openjscad.xyz/docs/module-modeling_maths_vec2.html#.transform
scraped_at: 2025-09-08T16:33:04.134994
title: Untitled
---

Represents a two dimensional vector.

Source:

    

  * [modeling/src/maths/vec2/index.js](modeling_src_maths_vec2_index.js.html), [line 1](modeling_src_maths_vec2_index.js.html#line1)

### Methods

#### (static) abs(out, vector) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/abs.js](modeling_src_maths_vec2_abs.js.html), [line 9](modeling_src_maths_vec2_abs.js.html#line9)

Calculates the absolute coordinates of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`vector` |  [vec2](global.html#vec2) | vector of reference  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) add(out, a, b) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/add.js](modeling_src_maths_vec2_add.js.html), [line 10](modeling_src_maths_vec2_add.js.html#line10)

Adds the coordinates of two vectors (A+B).

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) angleDegrees(vector) → {Number}

Source:

    

  * [modeling/src/maths/vec2/angleDegrees.js](modeling_src_maths_vec2_angleDegrees.js.html), [line 10](modeling_src_maths_vec2_angleDegrees.js.html#line10)

Calculate the angle of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec2](global.html#vec2) | vector of reference  
  
##### Returns:

angle in degrees

Type

     Number

#### (static) angleRadians(vector) → {Number}

Source:

    

  * [modeling/src/maths/vec2/angleRadians.js](modeling_src_maths_vec2_angleRadians.js.html), [line 8](modeling_src_maths_vec2_angleRadians.js.html#line8)

Calculate the angle of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec2](global.html#vec2) | vector of reference  
  
##### Returns:

angle in radians

Type

     Number

#### (static) clone(vector) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/clone.js](modeling_src_maths_vec2_clone.js.html), [line 10](modeling_src_maths_vec2_clone.js.html#line10)

Create a clone of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec2](global.html#vec2) | vector to clone  
  
##### Returns:

a new vector

Type

     [vec2](global.html#vec2)

#### (static) copy(out, vector) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/copy.js](modeling_src_maths_vec2_copy.js.html), [line 9](modeling_src_maths_vec2_copy.js.html#line9)

Create a copy of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`vector` |  [vec2](global.html#vec2) | source vector  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) create() → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/create.js](modeling_src_maths_vec2_create.js.html), [line 13](modeling_src_maths_vec2_create.js.html#line13)

Creates a new vector, initialized to [0,0].

##### Returns:

a new vector

Type

     [vec2](global.html#vec2)

#### (static) cross(out, a, b) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/vec2/cross.js](modeling_src_maths_vec2_cross.js.html), [line 10](modeling_src_maths_vec2_cross.js.html#line10)

Computes the cross product (3D) of two vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec3](global.html#vec3) | receiving vector (3D)  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

out

Type

     [vec3](global.html#vec3)

#### (static) distance(a, b) → {Number}

Source:

    

  * [modeling/src/maths/vec2/distance.js](modeling_src_maths_vec2_distance.js.html), [line 9](modeling_src_maths_vec2_distance.js.html#line9)

Calculates the distance between two vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

distance

Type

     Number

#### (static) divide(out, a, b) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/divide.js](modeling_src_maths_vec2_divide.js.html), [line 10](modeling_src_maths_vec2_divide.js.html#line10)

Divides the coordinates of two vectors (A/B).

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) dot(a, b) → {Number}

Source:

    

  * [modeling/src/maths/vec2/dot.js](modeling_src_maths_vec2_dot.js.html), [line 9](modeling_src_maths_vec2_dot.js.html#line9)

Calculates the dot product of two vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

dot product

Type

     Number

#### (static) equals(a, b) → {Boolean}

Source:

    

  * [modeling/src/maths/vec2/equals.js](modeling_src_maths_vec2_equals.js.html), [line 9](modeling_src_maths_vec2_equals.js.html#line9)

Compare the given vectors for equality.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

true if a and b are equal

Type

     Boolean

#### (static) fromAngleDegrees(out, degrees) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/fromAngleDegrees.js](modeling_src_maths_vec2_fromAngleDegrees.js.html), [line 11](modeling_src_maths_vec2_fromAngleDegrees.js.html#line11)

Create a new vector in the direction of the given angle.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`degrees` |  Number | angle in degrees  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) fromAngleRadians(out, radians) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/fromAngleRadians.js](modeling_src_maths_vec2_fromAngleRadians.js.html), [line 11](modeling_src_maths_vec2_fromAngleRadians.js.html#line11)

Create a new vector in the direction of the given angle.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`radians` |  Number | angle in radians  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) fromScalar(out, scalar) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/fromScalar.js](modeling_src_maths_vec2_fromScalar.js.html), [line 9](modeling_src_maths_vec2_fromScalar.js.html#line9)

Create a vector from a single scalar value.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`scalar` |  Number | the scalar value  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) fromValues(x, y) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/fromValues.js](modeling_src_maths_vec2_fromValues.js.html), [line 11](modeling_src_maths_vec2_fromValues.js.html#line11)

Creates a new vector initialized with the given values.

##### Parameters:

Name | Type | Description  
---|---|---  
`x` |  Number | X coordinate  
`y` |  Number | Y coordinate  
  
##### Returns:

a new vector

Type

     [vec2](global.html#vec2)

#### (static) length(vector) → {Number}

Source:

    

  * [modeling/src/maths/vec2/length.js](modeling_src_maths_vec2_length.js.html), [line 8](modeling_src_maths_vec2_length.js.html#line8)

Calculates the length of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec2](global.html#vec2) | vector of reference  
  
##### Returns:

length

Type

     Number

#### (static) lerp(out, a, b, t) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/lerp.js](modeling_src_maths_vec2_lerp.js.html), [line 11](modeling_src_maths_vec2_lerp.js.html#line11)

Performs a linear interpolation between two vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
`t` |  Number | interpolation amount between the two vectors  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) max(out, a, b) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/max.js](modeling_src_maths_vec2_max.js.html), [line 10](modeling_src_maths_vec2_max.js.html#line10)

Returns the maximum coordinates of two vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) min(out, a, b) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/min.js](modeling_src_maths_vec2_min.js.html), [line 10](modeling_src_maths_vec2_min.js.html#line10)

Returns the minimum coordinates of two vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) multiply(out, a, b) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/multiply.js](modeling_src_maths_vec2_multiply.js.html), [line 10](modeling_src_maths_vec2_multiply.js.html#line10)

Multiplies the coordinates of two vectors (A*B).

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) negate(out, vector) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/negate.js](modeling_src_maths_vec2_negate.js.html), [line 9](modeling_src_maths_vec2_negate.js.html#line9)

Negates the coordinates of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`vector` |  [vec2](global.html#vec2) | vector to negate  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) normal(out, vector) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/normal.js](modeling_src_maths_vec2_normal.js.html), [line 15](modeling_src_maths_vec2_normal.js.html#line15)

Calculates the normal of the given vector. The normal value is the given
vector rotated 90 degrees.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`vector` |  [vec2](global.html#vec2) | given value  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) normalize(out, vector) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/normalize.js](modeling_src_maths_vec2_normalize.js.html), [line 9](modeling_src_maths_vec2_normalize.js.html#line9)

Normalize the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`vector` |  [vec2](global.html#vec2) | vector to normalize  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) rotate(out, vector, origin, radians) →
{[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/rotate.js](modeling_src_maths_vec2_rotate.js.html), [line 11](modeling_src_maths_vec2_rotate.js.html#line11)

Rotates the given vector by the given angle.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`vector` |  [vec2](global.html#vec2) | vector to rotate  
`origin` |  [vec2](global.html#vec2) | origin of the rotation  
`radians` |  Number | angle of rotation (radians)  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) scale(out, vector, amount) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/scale.js](modeling_src_maths_vec2_scale.js.html), [line 10](modeling_src_maths_vec2_scale.js.html#line10)

Scales the coordinates of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`vector` |  [vec2](global.html#vec2) | vector to scale  
`amount` |  Number | amount to scale  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) snap(out, vector, epsilon) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/snap.js](modeling_src_maths_vec2_snap.js.html), [line 10](modeling_src_maths_vec2_snap.js.html#line10)

Snaps the coordinates of the given vector to the given epsilon.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`vector` |  [vec2](global.html#vec2) | vector to snap  
`epsilon` |  Number | epsilon of precision, less than 0  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) squaredDistance(a, b) → {Number}

Source:

    

  * [modeling/src/maths/vec2/squaredDistance.js](modeling_src_maths_vec2_squaredDistance.js.html), [line 9](modeling_src_maths_vec2_squaredDistance.js.html#line9)

Calculates the squared distance between the given vectors.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

squared distance

Type

     Number

#### (static) squaredLength(vector) → {Number}

Source:

    

  * [modeling/src/maths/vec2/squaredLength.js](modeling_src_maths_vec2_squaredLength.js.html), [line 8](modeling_src_maths_vec2_squaredLength.js.html#line8)

Calculates the squared length of the given vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec2](global.html#vec2) | vector of reference  
  
##### Returns:

squared length

Type

     Number

#### (static) subtract(out, a, b) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/subtract.js](modeling_src_maths_vec2_subtract.js.html), [line 10](modeling_src_maths_vec2_subtract.js.html#line10)

Subtracts the coordinates of two vectors (A-B).

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`a` |  [vec2](global.html#vec2) | first operand  
`b` |  [vec2](global.html#vec2) | second operand  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

#### (static) toString(vector) → {String}

Source:

    

  * [modeling/src/maths/vec2/toString.js](modeling_src_maths_vec2_toString.js.html), [line 8](modeling_src_maths_vec2_toString.js.html#line8)

Convert the given vector to a representative string.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec2](global.html#vec2) | vector of reference  
  
##### Returns:

string representation

Type

     String

#### (static) transform(out, vector, matrix) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/vec2/transform.js](modeling_src_maths_vec2_transform.js.html), [line 10](modeling_src_maths_vec2_transform.js.html#line10)

Transforms the given vector using the given matrix.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [vec2](global.html#vec2) | receiving vector  
`vector` |  [vec2](global.html#vec2) | vector to transform  
`matrix` |  [mat4](global.html#mat4) | matrix to transform with  
  
##### Returns:

out

Type

     [vec2](global.html#vec2)

