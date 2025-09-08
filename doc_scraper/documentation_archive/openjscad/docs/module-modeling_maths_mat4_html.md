---
url: https://openjscad.xyz/docs/module-modeling_maths_mat4.html#.translate
scraped_at: 2025-09-08T16:32:10.898103
title: Untitled
---

Represents a 4x4 matrix which is column-major (when typed out it looks row-
major).

Source:

    

  * [modeling/src/maths/mat4/index.js](modeling_src_maths_mat4_index.js.html), [line 1](modeling_src_maths_mat4_index.js.html#line1)

See:

    

  * [mat4](global.html#mat4) for data structure information.

### Methods

#### (static) add(out, a, b) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/add.js](modeling_src_maths_mat4_add.js.html), [line 10](modeling_src_maths_mat4_add.js.html#line10)

Adds the two matrices (A+B).

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`a` |  [mat4](global.html#mat4) | first operand  
`b` |  [mat4](global.html#mat4) | second operand  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) clone(matrix) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/clone.js](modeling_src_maths_mat4_clone.js.html), [line 10](modeling_src_maths_mat4_clone.js.html#line10)

Creates a clone of the given matrix.

##### Parameters:

Name | Type | Description  
---|---|---  
`matrix` |  [mat4](global.html#mat4) | matrix to clone  
  
##### Returns:

a new matrix

Type

     [mat4](global.html#mat4)

#### (static) copy(out, matrix) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/copy.js](modeling_src_maths_mat4_copy.js.html), [line 9](modeling_src_maths_mat4_copy.js.html#line9)

Creates a copy of the given matrix.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`matrix` |  [mat4](global.html#mat4) | matrix to copy  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) create() → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/create.js](modeling_src_maths_mat4_create.js.html), [line 13](modeling_src_maths_mat4_create.js.html#line13)

Creates a new identity matrix.

##### Returns:

a new matrix

Type

     [mat4](global.html#mat4)

#### (static) equals(a, b) → {Boolean}

Source:

    

  * [modeling/src/maths/mat4/equals.js](modeling_src_maths_mat4_equals.js.html), [line 9](modeling_src_maths_mat4_equals.js.html#line9)

Returns whether or not the matrices have exactly the same elements in the same
position.

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  [mat4](global.html#mat4) | first matrix  
`b` |  [mat4](global.html#mat4) | second matrix  
  
##### Returns:

true if the matrices are equal

Type

     Boolean

#### (static) fromRotation(out, rad, axis) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/fromRotation.js](modeling_src_maths_mat4_fromRotation.js.html), [line 22](modeling_src_maths_mat4_fromRotation.js.html#line22)

Creates a matrix from a given angle around a given axis This is equivalent to
(but much faster than):

    
    
    mat4.identity(dest)
    mat4.rotate(dest, dest, rad, axis)
    

##### Example

    
    
    let matrix = fromRotation(create(), TAU / 4, [0, 0, 3])

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`rad` |  Number | angle to rotate the matrix by  
`axis` |  [vec3](global.html#vec3) | axis of which to rotate around  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) fromScaling(out, vector) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/fromScaling.js](modeling_src_maths_mat4_fromScaling.js.html), [line 15](modeling_src_maths_mat4_fromScaling.js.html#line15)

Creates a matrix from a vector scaling. This is equivalent to (but much faster
than):

    
    
    mat4.identity(dest)
    mat4.scale(dest, dest, vec)
    

##### Example

    
    
    let matrix = fromScaling([1, 2, 0.5])

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`vector` |  [vec3](global.html#vec3) | X, Y, Z factors by which to scale  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) fromTaitBryanRotation(out, yaw, pitch, roll) →
{[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/fromTaitBryanRotation.js](modeling_src_maths_mat4_fromTaitBryanRotation.js.html), [line 18](modeling_src_maths_mat4_fromTaitBryanRotation.js.html#line18)

See:

    

  * <https://en.wikipedia.org/wiki/Euler_angles>

Creates a matrix from the given Tait–Bryan angles.

Tait-Bryan Euler angle convention using active, intrinsic rotations around the
axes in the order z-y-x.

##### Example

    
    
    let matrix = fromTaitBryanRotation(create(), TAU / 4, 0, TAU / 2)

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`yaw` |  Number | Z rotation in radians  
`pitch` |  Number | Y rotation in radians  
`roll` |  Number | X rotation in radians  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) fromTranslation(out, vector) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/fromTranslation.js](modeling_src_maths_mat4_fromTranslation.js.html), [line 15](modeling_src_maths_mat4_fromTranslation.js.html#line15)

Creates a matrix from a vector translation. This is equivalent to (but much
faster than):

    
    
    mat4.identity(dest)
    mat4.translate(dest, dest, vec)
    

##### Example

    
    
    let matrix = fromTranslation(create(), [1, 2, 3])

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`vector` |  [vec3](global.html#vec3) | offset (vector) of translation  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) fromValues(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21,
m22, m23, m30, m31, m32, m33) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/fromValues.js](modeling_src_maths_mat4_fromValues.js.html), [line 32](modeling_src_maths_mat4_fromValues.js.html#line32)

Create a matrix with the given values.

##### Example

    
    
    let matrix = fromValues(
      1, 0, 0, 1,
      0, 1, 0, 0,
      0, 0, 1, 0,
      0, 0, 0, 1
    )

##### Parameters:

Name | Type | Description  
---|---|---  
`m00` |  Number | Component in column 0, row 0 position (index 0)  
`m01` |  Number | Component in column 0, row 1 position (index 1)  
`m02` |  Number | Component in column 0, row 2 position (index 2)  
`m03` |  Number | Component in column 0, row 3 position (index 3)  
`m10` |  Number | Component in column 1, row 0 position (index 4)  
`m11` |  Number | Component in column 1, row 1 position (index 5)  
`m12` |  Number | Component in column 1, row 2 position (index 6)  
`m13` |  Number | Component in column 1, row 3 position (index 7)  
`m20` |  Number | Component in column 2, row 0 position (index 8)  
`m21` |  Number | Component in column 2, row 1 position (index 9)  
`m22` |  Number | Component in column 2, row 2 position (index 10)  
`m23` |  Number | Component in column 2, row 3 position (index 11)  
`m30` |  Number | Component in column 3, row 0 position (index 12)  
`m31` |  Number | Component in column 3, row 1 position (index 13)  
`m32` |  Number | Component in column 3, row 2 position (index 14)  
`m33` |  Number | Component in column 3, row 3 position (index 15)  
  
##### Returns:

a new matrix

Type

     [mat4](global.html#mat4)

#### (static) fromVectorRotation(out, source, target) →
{[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/fromVectorRotation.js](modeling_src_maths_mat4_fromVectorRotation.js.html), [line 18](modeling_src_maths_mat4_fromVectorRotation.js.html#line18)

See:

    

  * <https://gist.github.com/kevinmoran/b45980723e53edeb8a5a43c49f134724>

Create a matrix that rotates the given source to the given target vector.

Each vector must be a directional vector with a length greater than zero.

##### Example

    
    
    let matrix = fromVectorRotation(mat4.create(), [1, 2, 2], [-3, 3, 12])

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`source` |  [vec3](global.html#vec3) | source vector  
`target` |  [vec3](global.html#vec3) | target vector  
  
##### Returns:

a new matrix

Type

     [mat4](global.html#mat4)

#### (static) fromXRotation(out, radians) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/fromXRotation.js](modeling_src_maths_mat4_fromXRotation.js.html), [line 17](modeling_src_maths_mat4_fromXRotation.js.html#line17)

Creates a matrix from the given angle around the X axis. This is equivalent to
(but much faster than):

    
    
    mat4.identity(dest)
    mat4.rotateX(dest, dest, radians)
    

##### Example

    
    
    let matrix = fromXRotation(create(), TAU / 4)

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`radians` |  Number | angle to rotate the matrix by  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) fromYRotation(out, radians) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/fromYRotation.js](modeling_src_maths_mat4_fromYRotation.js.html), [line 17](modeling_src_maths_mat4_fromYRotation.js.html#line17)

Creates a matrix from the given angle around the Y axis. This is equivalent to
(but much faster than):

    
    
    mat4.identity(dest)
    mat4.rotateY(dest, dest, radians)
    

##### Example

    
    
    let matrix = fromYRotation(create(), TAU / 4)

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`radians` |  Number | angle to rotate the matrix by  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) fromZRotation(out, radians) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/fromZRotation.js](modeling_src_maths_mat4_fromZRotation.js.html), [line 17](modeling_src_maths_mat4_fromZRotation.js.html#line17)

Creates a matrix from the given angle around the Z axis. This is equivalent to
(but much faster than):

    
    
    mat4.identity(dest)
    mat4.rotateZ(dest, dest, radians)
    

##### Example

    
    
    let matrix = fromZRotation(create(), TAU / 4)

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`radians` |  Number | angle to rotate the matrix by  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) identity(out) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/identity.js](modeling_src_maths_mat4_identity.js.html), [line 8](modeling_src_maths_mat4_identity.js.html#line8)

Set a matrix to the identity transform.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) invert(out, matrix) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/invert.js](modeling_src_maths_mat4_invert.js.html), [line 11](modeling_src_maths_mat4_invert.js.html#line11)

Author:

    

  * Julian Lloyd code from https://github.com/jlmakes/rematrix/blob/master/src/index.js

Creates a invert copy of the given matrix.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`matrix` |  [mat4](global.html#mat4) | matrix to invert  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) isIdentity(matrix) → {Boolean}

Source:

    

  * [modeling/src/maths/mat4/isIdentity.js](modeling_src_maths_mat4_isIdentity.js.html), [line 13](modeling_src_maths_mat4_isIdentity.js.html#line13)

Determine whether the given matrix is the identity transform. This is
equivalent to (but much faster than):

    
    
    mat4.equals(mat4.create(), matrix)
    

##### Example

    
    
    if (mat4.isIdentity(mymatrix)) ...

##### Parameters:

Name | Type | Description  
---|---|---  
`matrix` |  [mat4](global.html#mat4) | the matrix  
  
##### Returns:

true if matrix is the identity transform

Type

     Boolean

#### (static) isMirroring(matrix) → {Boolean}

Source:

    

  * [modeling/src/maths/mat4/isMirroring.js](modeling_src_maths_mat4_isMirroring.js.html), [line 8](modeling_src_maths_mat4_isMirroring.js.html#line8)

Determine whether the given matrix is a mirroring transformation.

##### Parameters:

Name | Type | Description  
---|---|---  
`matrix` |  [mat4](global.html#mat4) | matrix of reference  
  
##### Returns:

true if matrix is a mirroring transformation

Type

     Boolean

#### (static) isOnlyTransformScale(matrix) → {Boolean}

Source:

    

  * [modeling/src/maths/mat4/isOnlyTransformScale.js](modeling_src_maths_mat4_isOnlyTransformScale.js.html), [line 10](modeling_src_maths_mat4_isOnlyTransformScale.js.html#line10)

Determine whether the given matrix is only translate and/or scale. This code
returns true for TAU / 2 rotation as it can be interpreted as scale.

##### Parameters:

Name | Type | Description  
---|---|---  
`matrix` |  [mat4](global.html#mat4) | the matrix  
  
##### Returns:

true if matrix is for translate and/or scale

Type

     Boolean

#### (static) mirrorByPlane(out, plane) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/mirrorByPlane.js](modeling_src_maths_mat4_mirrorByPlane.js.html), [line 9](modeling_src_maths_mat4_mirrorByPlane.js.html#line9)

Create a matrix for mirroring about the given plane.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`plane` |  [vec4](global.html#vec4) | plane of which to mirror the matrix  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) multiply(out, a, b) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/multiply.js](modeling_src_maths_mat4_multiply.js.html), [line 10](modeling_src_maths_mat4_multiply.js.html#line10)

Multiplies the two matrices.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`a` |  [mat4](global.html#mat4) | first operand  
`b` |  [mat4](global.html#mat4) | second operand  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) rightMultiplyVec2(vector, matrix) → {[vec2](global.html#vec2)}

Source:

    

  * [modeling/src/maths/mat4/rightMultiplyVec2.js](modeling_src_maths_mat4_rightMultiplyVec2.js.html), [line 12](modeling_src_maths_mat4_rightMultiplyVec2.js.html#line12)

Multiply a 2D vector by a matrix (interpreted as 2 row, 1 column).

Calculation: result = v*M, where the fourth element is set to 1.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec2](global.html#vec2) | input vector  
`matrix` |  [mat4](global.html#mat4) | input matrix  
  
##### Returns:

a new vector

Type

     [vec2](global.html#vec2)

#### (static) rightMultiplyVec3(vector, matrix) → {[vec3](global.html#vec3)}

Source:

    

  * [modeling/src/maths/mat4/rightMultiplyVec3.js](modeling_src_maths_mat4_rightMultiplyVec3.js.html), [line 12](modeling_src_maths_mat4_rightMultiplyVec3.js.html#line12)

Multiply a 3D vector by a matrix (interpreted as 3 row, 1 column)

Calculation: result = v*M, where the fourth element is set to 1.

##### Parameters:

Name | Type | Description  
---|---|---  
`vector` |  [vec3](global.html#vec3) | input vector  
`matrix` |  [mat4](global.html#mat4) | input matrix  
  
##### Returns:

a new vector

Type

     [vec3](global.html#vec3)

#### (static) rotate(out, matrix, radians, axis) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/rotate.js](modeling_src_maths_mat4_rotate.js.html), [line 17](modeling_src_maths_mat4_rotate.js.html#line17)

Rotates a matrix by the given angle about the given axis.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`matrix` |  [mat4](global.html#mat4) | matrix to rotate  
`radians` |  Number | angle to rotate the matrix by  
`axis` |  [vec3](global.html#vec3) | axis to rotate around  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) rotateX(out, matrix, radians) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/rotateX.js](modeling_src_maths_mat4_rotateX.js.html), [line 12](modeling_src_maths_mat4_rotateX.js.html#line12)

Rotates a matrix by the given angle around the X axis.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`matrix` |  [mat4](global.html#mat4) | matrix to rotate  
`radians` |  Number | angle to rotate the matrix by  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) rotateY(out, matrix, radians) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/rotateY.js](modeling_src_maths_mat4_rotateY.js.html), [line 12](modeling_src_maths_mat4_rotateY.js.html#line12)

Rotates a matrix by the given angle around the Y axis.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`matrix` |  [mat4](global.html#mat4) | matrix to rotate  
`radians` |  Number | angle to rotate the matrix by  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) rotateZ(out, matrix, radians) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/rotateZ.js](modeling_src_maths_mat4_rotateZ.js.html), [line 12](modeling_src_maths_mat4_rotateZ.js.html#line12)

Rotates a matrix by the given angle around the Z axis.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`matrix` |  [mat4](global.html#mat4) | matrix to rotate  
`radians` |  Number | angle to rotate the matrix by  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) scale(out, matrix, dimensions) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/scale.js](modeling_src_maths_mat4_scale.js.html), [line 10](modeling_src_maths_mat4_scale.js.html#line10)

Scales the matrix by the given dimensions.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`matrix` |  [mat4](global.html#mat4) | matrix to scale  
`dimensions` |  [vec3](global.html#vec3) | dimensions to scale the matrix by  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) subtract(out, a, b) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/subtract.js](modeling_src_maths_mat4_subtract.js.html), [line 10](modeling_src_maths_mat4_subtract.js.html#line10)

Subtracts matrix b from matrix a. (A-B)

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`a` |  [mat4](global.html#mat4) | first operand  
`b` |  [mat4](global.html#mat4) | second operand  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

#### (static) toString(mat) → {String}

Source:

    

  * [modeling/src/maths/mat4/toString.js](modeling_src_maths_mat4_toString.js.html), [line 8](modeling_src_maths_mat4_toString.js.html#line8)

Return a string representing the given matrix.

##### Parameters:

Name | Type | Description  
---|---|---  
`mat` |  [mat4](global.html#mat4) | matrix of reference  
  
##### Returns:

string representation

Type

     String

#### (static) translate(out, matrix, offsets) → {[mat4](global.html#mat4)}

Source:

    

  * [modeling/src/maths/mat4/translate.js](modeling_src_maths_mat4_translate.js.html), [line 10](modeling_src_maths_mat4_translate.js.html#line10)

Translate the matrix by the given offset vector.

##### Parameters:

Name | Type | Description  
---|---|---  
`out` |  [mat4](global.html#mat4) | receiving matrix  
`matrix` |  [mat4](global.html#mat4) | matrix to translate  
`offsets` |  [vec3](global.html#vec3) | offset vector to translate by  
  
##### Returns:

out

Type

     [mat4](global.html#mat4)

