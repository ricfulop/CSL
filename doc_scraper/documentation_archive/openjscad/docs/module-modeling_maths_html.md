---
url: https://openjscad.xyz/docs/module-modeling_maths.html
scraped_at: 2025-09-08T16:31:06.555841
title: Untitled
---

Maths are computational units for fundamental Euclidean geometry. All maths
operate upon array data structures. Note: Maths data structures are considered
immutable, so never change the contents directly.

Source:

    

  * [modeling/src/maths/index.js](modeling_src_maths_index.js.html), [line 1](modeling_src_maths_index.js.html#line1)

See:

    

  * Most computations are based upon the glMatrix library (glmatrix.net)

##### Example

    
    
    const { constants, line2, line3, mat4, plane, utils, vec2, vec3, vec4 } = require('@jscad/modeling').maths

### Members

#### (static, constant) EPS

Source:

    

  * [modeling/src/maths/constants.js](modeling_src_maths_constants.js.html), [line 15](modeling_src_maths_constants.js.html#line15)

Default Value:

    

  * 0.00001

Epsilon used during determination of near zero distances. This should be 1 /
spacialResolution.

#### (static, constant) NEPS

Source:

    

  * [modeling/src/maths/constants.js](modeling_src_maths_constants.js.html), [line 22](modeling_src_maths_constants.js.html#line22)

Default Value:

    

  * 1e-13

Smaller epsilon used for measuring near zero distances.

#### (static, constant) spatialResolution

Source:

    

  * [modeling/src/maths/constants.js](modeling_src_maths_constants.js.html), [line 7](modeling_src_maths_constants.js.html#line7)

Default Value:

    

  * 100000

The resolution of space, currently one hundred nanometers. This should be 1 /
EPS.

