---
url: https://freecad.github.io/SourceDoc/d5/db4/classBase_1_1Matrix4D.html
scraped_at: 2025-09-08T15:16:38.060826
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html)

[List of all members](../../d3/d48/classBase_1_1Matrix4D-members.html) | Public Member Functions

Base::Matrix4D Class Reference

The [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html "The Matrix4D class.")
class. [More...](../../d5/db4/classBase_1_1Matrix4D.html#details)

`#include <Matrix.h>`

##  Public Member Functions  
  
---  
|
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html#a7cecf058dd181984d8ca7fee1423c6e2)
()  
| Default constructor.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a7cecf058dd181984d8ca7fee1423c6e2)  
  
|
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html#a5472578ad460fac8f609f3c233cf981a)
(const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx)  
| Construction.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a5472578ad460fac8f609f3c233cf981a)  
  
|
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html#a44f0ee01702a449aea9f97a988304048)
(const
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e)
&rclBase, const
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e)
&rclDir, double fAngle)  
|
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html#aff848b9c1b3ec8ce602679471ced18de)
(const
[Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea)
&rclBase, const
[Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea)
&rclDir, float fAngle)  
| Construction with an [Axis](../../d5/d61/classBase_1_1Axis.html "The Axis
class.").
[More...](../../d5/db4/classBase_1_1Matrix4D.html#aff848b9c1b3ec8ce602679471ced18de)  
  
|
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html#a35f9e91ede6099f9802724db5aed0eca)
(double a11, double a12, double a13, double a14, double a21, double a22,
double a23, double a24, double a31, double a32, double a33, double a34, double
a41, double a42, double a43, double a44)  
| Construction.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a35f9e91ede6099f9802724db5aed0eca)  
  
|
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html#ad11e5cb5c95303a13420beaf88519f8b)
(float a11, float a12, float a13, float a14, float a21, float a22, float a23,
float a24, float a31, float a32, float a33, float a34, float a41, float a42,
float a43, float a44)  
| Construction.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#ad11e5cb5c95303a13420beaf88519f8b)  
  
|
[~Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html#a7657b54d19ec5fbb21ea8a4cee9abc81)
()  
| Destruction.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a7657b54d19ec5fbb21ea8a4cee9abc81)  
  
Operators  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [operator+](../../d5/db4/classBase_1_1Matrix4D.html#a0ffb754075ba01571ca57ae128b6c4d0) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx) const  
| Matrix addition.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a0ffb754075ba01571ca57ae128b6c4d0)  
  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | [operator+=](../../d5/db4/classBase_1_1Matrix4D.html#a286e99537dc2e4ece7902f0485e13df1) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx)  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [operator-](../../d5/db4/classBase_1_1Matrix4D.html#aca2b8eee736d55afecb7102492de3170) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx) const  
| Matrix subtraction.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#aca2b8eee736d55afecb7102492de3170)  
  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | [operator-=](../../d5/db4/classBase_1_1Matrix4D.html#a44356b4b7c89610746e300d707c04cdb) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx)  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | [operator*=](../../d5/db4/classBase_1_1Matrix4D.html#af76cf6a87a851c4fa05158aa3b9c698e) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx)  
| Matrix multiplication.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#af76cf6a87a851c4fa05158aa3b9c698e)  
  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | [operator=](../../d5/db4/classBase_1_1Matrix4D.html#a10c2021fd7bd23c64d5a1ab2f835f3fe) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx)  
| Assignment.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a10c2021fd7bd23c64d5a1ab2f835f3fe)  
  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [operator*](../../d5/db4/classBase_1_1Matrix4D.html#a18dd0ab04a687ee6e7ce16e956de8507) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx) const  
| Matrix multiplication.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a18dd0ab04a687ee6e7ce16e956de8507)  
  
[Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) | [operator*](../../d5/db4/classBase_1_1Matrix4D.html#ab8a45ff4ced15d460ae0b11239629d52) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclVct) const  
| Multiplication matrix with vector.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#ab8a45ff4ced15d460ae0b11239629d52)  
  
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [operator*](../../d5/db4/classBase_1_1Matrix4D.html#a7824f654d72efbc4b3e6ae9c2523998c) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclVct) const  
void | [multVec](../../d5/db4/classBase_1_1Matrix4D.html#a79baa069033c73b44bfe38be08497010) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &src, [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &dst) const  
void | [multVec](../../d5/db4/classBase_1_1Matrix4D.html#a2e982037837f0005bd3cf78bffe5131e) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &src, [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &dst) const  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [operator*](../../d5/db4/classBase_1_1Matrix4D.html#a588f3aeb957cc81b9b9f90f8d5ded21a) (double) const  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | [operator*=](../../d5/db4/classBase_1_1Matrix4D.html#ac31e2c14a25fa6c688e0b7dd26672817) (double)  
[bool](../../d9/db9/classbool.html) | [operator!=](../../d5/db4/classBase_1_1Matrix4D.html#a492e0e12adc0fc7948330a6564901e82) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx) const  
| Comparison.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a492e0e12adc0fc7948330a6564901e82)  
  
[bool](../../d9/db9/classbool.html) | [operator==](../../d5/db4/classBase_1_1Matrix4D.html#a87d83e47a883eeb6578a98ed9876973c) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx) const  
| Comparison.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a87d83e47a883eeb6578a98ed9876973c)  
  
double * | [operator[]](../../d5/db4/classBase_1_1Matrix4D.html#ae4a2b30be432e9b7afa328107f26abd3) (unsigned short usNdx)  
| Index operator.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#ae4a2b30be432e9b7afa328107f26abd3)  
  
const double * | [operator[]](../../d5/db4/classBase_1_1Matrix4D.html#a153292e98a407fef0744f91f012b1163) (unsigned short usNdx) const  
| Index operator.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a153292e98a407fef0744f91f012b1163)  
  
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [getRow](../../d5/db4/classBase_1_1Matrix4D.html#a59942c0e00de3f27545d839f8065e927) (unsigned short usNdx) const  
| Get vector of row.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a59942c0e00de3f27545d839f8065e927)  
  
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [getCol](../../d5/db4/classBase_1_1Matrix4D.html#a7c55f098c7d3a8b13886a11d24eeeee7) (unsigned short usNdx) const  
| Get vector of column.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a7c55f098c7d3a8b13886a11d24eeeee7)  
  
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [trace](../../d5/db4/classBase_1_1Matrix4D.html#a280fe4b79e071408a1ffdd5f8da3f8ef) () const  
| Get vector of trace.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a280fe4b79e071408a1ffdd5f8da3f8ef)  
  
void | [setRow](../../d5/db4/classBase_1_1Matrix4D.html#a610073e4f45e8627135c6d07446c543b) (unsigned short usNdx, const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &)  
| Set row to vector.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a610073e4f45e8627135c6d07446c543b)  
  
void | [setCol](../../d5/db4/classBase_1_1Matrix4D.html#a05ebc3e1f67001c32bbe6acf3a9d7c17) (unsigned short usNdx, const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &)  
| Set column to vector.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a05ebc3e1f67001c32bbe6acf3a9d7c17)  
  
void | [setTrace](../../d5/db4/classBase_1_1Matrix4D.html#a79bb856451a35304e7fbed253c0c0fe0) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &)  
| Set trace to vector.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a79bb856451a35304e7fbed253c0c0fe0)  
  
double | [determinant](../../d5/db4/classBase_1_1Matrix4D.html#a0c32e42a28c6e542105e02725216f1bd) () const  
| Compute the determinant of the matrix.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a0c32e42a28c6e542105e02725216f1bd)  
  
double | [determinant3](../../d5/db4/classBase_1_1Matrix4D.html#ad02d34778d600ed973f9538e64cec5a1) () const  
| Compute the determinant of the 3x3 sub-matrix.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#ad02d34778d600ed973f9538e64cec5a1)  
  
std::string | [analyse](../../d5/db4/classBase_1_1Matrix4D.html#a9303ce9048d7f949a108b12e928a08e0) () const  
| Analyse the transformation.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a9303ce9048d7f949a108b12e928a08e0)  
  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | [Outer](../../d5/db4/classBase_1_1Matrix4D.html#a6da1790aab096b22aafe2aa485db7b37) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rV1, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rV2)  
| Outer product (Dyadic product)
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a6da1790aab096b22aafe2aa485db7b37)  
  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | [Outer](../../d5/db4/classBase_1_1Matrix4D.html#a8e19dc5e655bc920f9527c62c1ecf7aa) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rV1, const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rV2)  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | [Hat](../../d5/db4/classBase_1_1Matrix4D.html#aba4ac5381849e58b53387154016fad47) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rV)  
| Hat operator (skew symmetric)
[More...](../../d5/db4/classBase_1_1Matrix4D.html#aba4ac5381849e58b53387154016fad47)  
  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | [Hat](../../d5/db4/classBase_1_1Matrix4D.html#ae5b666346437729d9c62741a35497aa7) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rV)  
void | [getMatrix](../../d5/db4/classBase_1_1Matrix4D.html#a4bc6007ba913b385566b00515cf3a951) (double dMtrx[16]) const  
void | [setMatrix](../../d5/db4/classBase_1_1Matrix4D.html#aea280b3150df9d34f1b5f44ed6481687) (const double dMtrx[16])  
void | [getGLMatrix](../../d5/db4/classBase_1_1Matrix4D.html#a8bb6545451679312a37458ea2760d18e) (double dMtrx[16]) const  
| get the matrix in OpenGL style
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a8bb6545451679312a37458ea2760d18e)  
  
void | [setGLMatrix](../../d5/db4/classBase_1_1Matrix4D.html#a5d5e095f8b68b6a726b0f0bf0ba9866f) (const double dMtrx[16])  
| set the matrix in OpenGL style
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a5d5e095f8b68b6a726b0f0bf0ba9866f)  
  
unsigned long | [getMemSpace](../../d5/db4/classBase_1_1Matrix4D.html#aa5b26cad294ef7ed43a10b3cda6ea3bd) ()  
  
## Manipulation  
  
---  
void | [setToUnity](../../d5/db4/classBase_1_1Matrix4D.html#ac860beb3fa5c0c0fe9d1e305bd2b68b8) ()  
| Makes unity matrix.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#ac860beb3fa5c0c0fe9d1e305bd2b68b8)  
  
[bool](../../d9/db9/classbool.html) | [isUnity](../../d5/db4/classBase_1_1Matrix4D.html#abbc86a8d5a8b98ac613a2df92b0575ba) () const  
| Checks if this is the unit matrix.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#abbc86a8d5a8b98ac613a2df92b0575ba)  
  
void | [nullify](../../d5/db4/classBase_1_1Matrix4D.html#a1c524fe37aea3c5ee050e8a56f565fbd) ()  
| Makes a null matrix.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a1c524fe37aea3c5ee050e8a56f565fbd)  
  
[bool](../../d9/db9/classbool.html) | [isNull](../../d5/db4/classBase_1_1Matrix4D.html#a059fb23607e58181fe7c1d5766c0f502) () const  
| Checks if this is the null matrix.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a059fb23607e58181fe7c1d5766c0f502)  
  
void | [move](../../d5/db4/classBase_1_1Matrix4D.html#ac26497380187a175bcd5e43a0c81740f) (float x, float y, float z)  
| moves the coordinatesystem for the x,y,z value
[More...](../../d5/db4/classBase_1_1Matrix4D.html#ac26497380187a175bcd5e43a0c81740f)  
  
void | [move](../../d5/db4/classBase_1_1Matrix4D.html#a59a2433fd9abc6e1d10b09fe327540f5) (double x, double y, double z)  
void | [move](../../d5/db4/classBase_1_1Matrix4D.html#acba412fbe0fe2b035de62770898c9cda) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclVct)  
| moves the coordinatesystem for the vector
[More...](../../d5/db4/classBase_1_1Matrix4D.html#acba412fbe0fe2b035de62770898c9cda)  
  
void | [move](../../d5/db4/classBase_1_1Matrix4D.html#ac833395bac6936432368efa5595387bd) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclVct)  
void | [scale](../../d5/db4/classBase_1_1Matrix4D.html#aa0838e1c628e3f405a83904679acec56) (float x, float y, float z)  
| scale for the vector
[More...](../../d5/db4/classBase_1_1Matrix4D.html#aa0838e1c628e3f405a83904679acec56)  
  
void | [scale](../../d5/db4/classBase_1_1Matrix4D.html#a51538c6417017c84b430f7409d99ba3b) (double x, double y, double z)  
void | [scale](../../d5/db4/classBase_1_1Matrix4D.html#ad9ce1a6cb945b73f95200100ec41d9f9) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclVct)  
| scale for the x,y,z value
[More...](../../d5/db4/classBase_1_1Matrix4D.html#ad9ce1a6cb945b73f95200100ec41d9f9)  
  
void | [scale](../../d5/db4/classBase_1_1Matrix4D.html#a3121f149e2b6034c29235b776f44989b) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclVct)  
void | [scale](../../d5/db4/classBase_1_1Matrix4D.html#a86eb8902833104000a7fafa682f003c9) (float scalexyz)  
| uniform scale
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a86eb8902833104000a7fafa682f003c9)  
  
void | [scale](../../d5/db4/classBase_1_1Matrix4D.html#a7fcca096764991222b08313f6089d19a) (double scalexyz)  
[ScaleType](../../db/d07/namespaceBase.html#a3489a4d5c3a17f301fb9d2ee4a089d19) | [hasScale](../../d5/db4/classBase_1_1Matrix4D.html#a88d80af7379be993bf083974310879a6) (double tol=0.0) const  
| Check for scaling factor.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a88d80af7379be993bf083974310879a6)  
  
void | [rotX](../../d5/db4/classBase_1_1Matrix4D.html#a00cf847ceba2e2c051ff2b5bb9946c87) (double fAngle)  
| Rotate around the X axis (in transformed space) for the given value in
radians.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a00cf847ceba2e2c051ff2b5bb9946c87)  
  
void | [rotY](../../d5/db4/classBase_1_1Matrix4D.html#a1b05478654c4a76f6b7c85243802682b) (double fAngle)  
| Rotate around the Y axis (in transformed space) for the given value in
radians.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a1b05478654c4a76f6b7c85243802682b)  
  
void | [rotZ](../../d5/db4/classBase_1_1Matrix4D.html#a612598e13e27ff95d6bf93bb516cf72d) (double fAngle)  
| Rotate around the Z axis (in transformed space) for the given value in
radians.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a612598e13e27ff95d6bf93bb516cf72d)  
  
void | [rotLine](../../d5/db4/classBase_1_1Matrix4D.html#aefb253d9d003400aa224a52d7171ad6f) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclVct, float fAngle)  
| Rotate around an arbitrary axis passing the origin in radians.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#aefb253d9d003400aa224a52d7171ad6f)  
  
void | [rotLine](../../d5/db4/classBase_1_1Matrix4D.html#aff3583443a5de61928925fa6b8af6f21) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclVct, double fAngle)  
| Rotate around an arbitrary axis passing the origin in radians.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#aff3583443a5de61928925fa6b8af6f21)  
  
void | [rotLine](../../d5/db4/classBase_1_1Matrix4D.html#ac181a77ffe6861908725c5d22030afa2) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclBase, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclDir, float fAngle)  
| Rotate around an arbitrary axis that needn't necessarily pass the origin in
radians.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#ac181a77ffe6861908725c5d22030afa2)  
  
void | [rotLine](../../d5/db4/classBase_1_1Matrix4D.html#aec5a2013fb02d974a514e5d735b87bcd) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclBase, const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclDir, double fAngle)  
| Rotate around an arbitrary axis that needn't necessarily pass the origin in
radians.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#aec5a2013fb02d974a514e5d735b87bcd)  
  
[bool](../../d9/db9/classbool.html) | [toAxisAngle](../../d5/db4/classBase_1_1Matrix4D.html#a3c28ec45a2f21383dcdb5c3d1b70ee82) ([Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclBase, [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclDir, float &fAngle, float &fTranslation) const  
| Extract the rotation axis and angle. Therefore the 3x3 submatrix must be
orthogonal.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a3c28ec45a2f21383dcdb5c3d1b70ee82)  
  
[bool](../../d9/db9/classbool.html) | [toAxisAngle](../../d5/db4/classBase_1_1Matrix4D.html#aebaf3536031474ff723f0a4abd621e55) ([Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclBase, [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclDir, double &fAngle, double &fTranslation) const  
void | [transform](../../d5/db4/classBase_1_1Matrix4D.html#af81d4febac264b2a48dca8b5c4649df9) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclVct, const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx)  
| transform (move,scale,rotate) around a point
[More...](../../d5/db4/classBase_1_1Matrix4D.html#af81d4febac264b2a48dca8b5c4649df9)  
  
void | [transform](../../d5/db4/classBase_1_1Matrix4D.html#a1155ec8976ecc3b381ba8bacee5ab171) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclVct, const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtrx)  
void | [inverse](../../d5/db4/classBase_1_1Matrix4D.html#a900463c57b2a13203064efde770795c4) ()  
| Matrix is expected to have a 3x3 rotation submatrix.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a900463c57b2a13203064efde770795c4)  
  
void | [inverseOrthogonal](../../d5/db4/classBase_1_1Matrix4D.html#a59fc9807b582d580c0e91ef3d0b0a5b0) ()  
| Matrix is expected to have a 3x3 rotation submatrix.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a59fc9807b582d580c0e91ef3d0b0a5b0)  
  
void | [inverseGauss](../../d5/db4/classBase_1_1Matrix4D.html#ab10ef93ba66ebfb66dfa31d923d100c5) ()  
| Arbitrary, non-singular matrix.
[More...](../../d5/db4/classBase_1_1Matrix4D.html#ab10ef93ba66ebfb66dfa31d923d100c5)  
  
void | [transpose](../../d5/db4/classBase_1_1Matrix4D.html#abf80f30b7c17ed0f200c60b37c929f16) ()  
void | [Print](../../d5/db4/classBase_1_1Matrix4D.html#aba8fe581d301c049f77b5644999a0ad1) () const  
std::string | [toString](../../d5/db4/classBase_1_1Matrix4D.html#a5879834fc2b997759929ea7192244814) () const  
| write the 16 double of the matrix into a string
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a5879834fc2b997759929ea7192244814)  
  
void | [fromString](../../d5/db4/classBase_1_1Matrix4D.html#a30c5ba1c5624d7955fa495f3baf25fad) (const std::string &[str](../../d9/d36/classstr.html))  
| read the 16 double of the matrix from a string
[More...](../../d5/db4/classBase_1_1Matrix4D.html#a30c5ba1c5624d7955fa495f3baf25fad)  
  
  
## Detailed Description

The [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html "The Matrix4D class.")
class.

## Constructor & Destructor Documentation

## ◆ Matrix4D() [1/6]

Matrix4D::Matrix4D  | ( | | ) |   
---|---|---|---|---  
  
Default constructor.

Initialises to an identity matrix

Referenced by
[getMemSpace()](../../d5/db4/classBase_1_1Matrix4D.html#aa5b26cad294ef7ed43a10b3cda6ea3bd).

## ◆ Matrix4D() [2/6]

Matrix4D::Matrix4D  | ( | float  | _a11_ ,   
---|---|---|---  
|  | float  | _a12_ ,   
|  | float  | _a13_ ,   
|  | float  | _a14_ ,   
|  | float  | _a21_ ,   
|  | float  | _a22_ ,   
|  | float  | _a23_ ,   
|  | float  | _a24_ ,   
|  | float  | _a31_ ,   
|  | float  | _a32_ ,   
|  | float  | _a33_ ,   
|  | float  | _a34_ ,   
|  | float  | _a41_ ,   
|  | float  | _a42_ ,   
|  | float  | _a43_ ,   
|  | float  | _a44_  
| ) | |   
  
Construction.

## ◆ Matrix4D() [3/6]

Matrix4D::Matrix4D  | ( | double  | _a11_ ,   
---|---|---|---  
|  | double  | _a12_ ,   
|  | double  | _a13_ ,   
|  | double  | _a14_ ,   
|  | double  | _a21_ ,   
|  | double  | _a22_ ,   
|  | double  | _a23_ ,   
|  | double  | _a24_ ,   
|  | double  | _a31_ ,   
|  | double  | _a32_ ,   
|  | double  | _a33_ ,   
|  | double  | _a34_ ,   
|  | double  | _a41_ ,   
|  | double  | _a42_ ,   
|  | double  | _a43_ ,   
|  | double  | _a44_  
| ) | |   
  
Construction.

## ◆ Matrix4D() [4/6]

Matrix4D::Matrix4D  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_| ) |   
---|---|---|---|---|---  
  
Construction.

## ◆ Matrix4D() [5/6]

Matrix4D::Matrix4D  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclDir_ ,   
|  | float  | _fAngle_  
| ) | |   
  
Construction with an [Axis](../../d5/d61/classBase_1_1Axis.html "The Axis
class.").

References
[rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aefb253d9d003400aa224a52d7171ad6f).

## ◆ Matrix4D() [6/6]

Matrix4D::Matrix4D  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclDir_ ,   
|  | double  | _fAngle_  
| ) | |   
  
References
[rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aefb253d9d003400aa224a52d7171ad6f).

## ◆ ~Matrix4D()

Base::Matrix4D::~Matrix4D  | ( | | ) |   
---|---|---|---|---  
  
Destruction.

## Member Function Documentation

## ◆ analyse()

std::string Matrix4D::analyse  | ( | | ) |  const  
---|---|---|---|---  
  
Analyse the transformation.

References
[determinant()](../../d5/db4/classBase_1_1Matrix4D.html#a0c32e42a28c6e542105e02725216f1bd),
and
[transpose()](../../d5/db4/classBase_1_1Matrix4D.html#abf80f30b7c17ed0f200c60b37c929f16).

## ◆ determinant()

double Matrix4D::determinant  | ( | | ) |  const  
---|---|---|---|---  
  
Compute the determinant of the matrix.

Referenced by
[analyse()](../../d5/db4/classBase_1_1Matrix4D.html#a9303ce9048d7f949a108b12e928a08e0).

## ◆ determinant3()

double Matrix4D::determinant3  | ( | | ) |  const  
---|---|---|---|---  
  
Compute the determinant of the 3x3 sub-matrix.

Referenced by
[hasScale()](../../d5/db4/classBase_1_1Matrix4D.html#a88d80af7379be993bf083974310879a6).

## ◆ fromString()

void Matrix4D::fromString  | ( | const std::string & | _str_| ) |   
---|---|---|---|---|---  
  
read the 16 double of the matrix from a string

Referenced by
[Points::PropertyPointKernel::Restore()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a4e72a35a1ea913ffee981734df7e500f).

## ◆ getCol()

[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) Base::Matrix4D::getCol  | ( | unsigned short  | _usNdx_| ) |  const  
---|---|---|---|---|---  
  
Get vector of column.

## ◆ getGLMatrix()

void Matrix4D::getGLMatrix  | ( | double  | _dMtrx_[16]| ) |  const  
---|---|---|---|---|---  
  
get the matrix in OpenGL style

Referenced by
[Gui::ViewProvider::convert()](../../d3/db3/classGui_1_1ViewProvider.html#a5818a11a94776a34ad509c27d824c90d),
[inverseGauss()](../../d5/db4/classBase_1_1Matrix4D.html#ab10ef93ba66ebfb66dfa31d923d100c5),
[Gui::View3DInventorViewer::setEditingTransform()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a4b4070aa8381b49fafb07a2b74ac02f6),
[Gui::LinkView::setTransform()](../../da/d11/classGui_1_1LinkView.html#a19c90dc21b9657ff2b378cd1588c7f64),
and
[Gui::ViewProvider::setTransformation()](../../d3/db3/classGui_1_1ViewProvider.html#a8d06af6b975e2907f1971bd712f95cf0).

## ◆ getMatrix()

void Matrix4D::getMatrix  | ( | double  | _dMtrx_[16]| ) |  const  
---|---|---|---|---|---  
  
## ◆ getMemSpace()

unsigned long Matrix4D::getMemSpace  | ( | | ) |   
---|---|---|---|---  
  
References
[Matrix4D()](../../d5/db4/classBase_1_1Matrix4D.html#a7cecf058dd181984d8ca7fee1423c6e2).

## ◆ getRow()

[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) Base::Matrix4D::getRow  | ( | unsigned short  | _usNdx_| ) |  const  
---|---|---|---|---|---  
  
Get vector of row.

## ◆ hasScale()

[ScaleType](../../db/d07/namespaceBase.html#a3489a4d5c3a17f301fb9d2ee4a089d19) Matrix4D::hasScale  | ( | double  | _tol_ = `0.0`| ) |  const  
---|---|---|---|---|---  
  
Check for scaling factor.

References
[determinant3()](../../d5/db4/classBase_1_1Matrix4D.html#ad02d34778d600ed973f9538e64cec5a1),
[Base::NonUniformLeft](../../db/d07/namespaceBase.html#a3489a4d5c3a17f301fb9d2ee4a089d19a5b0bc428554747977e1aa652963ac971),
[Base::NonUniformRight](../../db/d07/namespaceBase.html#a3489a4d5c3a17f301fb9d2ee4a089d19a5a4b4bf949a118bdc1e436d33bf19aba),
[Base::NoScaling](../../db/d07/namespaceBase.html#a3489a4d5c3a17f301fb9d2ee4a089d19a0f4d90af8697a25b7a0f6258fdfeac5c),
[Base::Other](../../db/d07/namespaceBase.html#a3489a4d5c3a17f301fb9d2ee4a089d19a6311ae17c1ee52b36e68aaf4ad066387),
[Base::Vector3< _Precision
>::Sqr()](../../d1/d13/classBase_1_1Vector3.html#a80a17d5af270b4bbb5b85c9ca9caa1e8),
and
[Base::Uniform](../../db/d07/namespaceBase.html#a3489a4d5c3a17f301fb9d2ee4a089d19af19516d11f2946f894070e92fcb56b6d).

## ◆ Hat() [1/2]

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & Matrix4D::Hat  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rV_| ) |   
---|---|---|---|---|---  
  
References
[setToUnity()](../../d5/db4/classBase_1_1Matrix4D.html#ac860beb3fa5c0c0fe9d1e305bd2b68b8),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ Hat() [2/2]

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & Matrix4D::Hat  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rV_| ) |   
---|---|---|---|---|---  
  
Hat operator (skew symmetric)

References
[Hat()](../../d5/db4/classBase_1_1Matrix4D.html#aba4ac5381849e58b53387154016fad47),
and
[setToUnity()](../../d5/db4/classBase_1_1Matrix4D.html#ac860beb3fa5c0c0fe9d1e305bd2b68b8).

Referenced by
[Hat()](../../d5/db4/classBase_1_1Matrix4D.html#aba4ac5381849e58b53387154016fad47).

## ◆ inverse()

void Matrix4D::inverse  | ( | | ) |   
---|---|---|---|---  
  
Matrix is expected to have a 3x3 rotation submatrix.

Referenced by
[PartGui::evaluateAngularPreSelection()](../../d5/d49/namespacePartGui.html#af0dc1ad1549a7fac118db816447cb551),
[PartGui::TaskMeasureAngular::onSelectionChanged()](../../d7/dea/classPartGui_1_1TaskMeasureAngular.html#a611207e21f64ba3dcde78e56d224786c),
[PathGui::PathSelectionObserver::onSelectionChanged()](../../db/d77/classPathGui_1_1PathSelectionObserver.html#a647466bb806e71c512362f4dafc43e7b),
[Gui::ViewProviderDragger::setEditViewer()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5746c8658c714b1910627ea804ca2353),
and
[Data::ComplexGeoData::transformToInside()](../../d8/daf/classData_1_1ComplexGeoData.html#a8b0cc05d2cf2ab2a1bb36e7f2a70949e).

## ◆ inverseGauss()

void Matrix4D::inverseGauss  | ( | | ) |   
---|---|---|---|---  
  
Arbitrary, non-singular matrix.

References
[getGLMatrix()](../../d5/db4/classBase_1_1Matrix4D.html#a8bb6545451679312a37458ea2760d18e),
and
[setGLMatrix()](../../d5/db4/classBase_1_1Matrix4D.html#a5d5e095f8b68b6a726b0f0bf0ba9866f).

Referenced by
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
and
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83).

## ◆ inverseOrthogonal()

void Matrix4D::inverseOrthogonal  | ( | | ) |   
---|---|---|---|---  
  
Matrix is expected to have a 3x3 rotation submatrix.

References
[operator*()](../../d5/db4/classBase_1_1Matrix4D.html#a18dd0ab04a687ee6e7ce16e956de8507),
and
[transpose()](../../d5/db4/classBase_1_1Matrix4D.html#abf80f30b7c17ed0f200c60b37c929f16).

## ◆ isNull()

[bool](../../d9/db9/classbool.html) Matrix4D::isNull  | ( | | ) |  const  
---|---|---|---|---  
  
Checks if this is the null matrix.

## ◆ isUnity()

[bool](../../d9/db9/classbool.html) Matrix4D::isUnity  | ( | | ) |  const  
---|---|---|---|---  
  
Checks if this is the unit matrix.

## ◆ move() [1/4]

void Matrix4D::move  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclVct_| ) |   
---|---|---|---|---|---  
  
References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[draftguitools.gui_circulararray.CircularArray::Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
and
[draftguitools.gui_polararray.PolarArray::Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6).

## ◆ move() [2/4]

void Matrix4D::move  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclVct_| ) |   
---|---|---|---|---|---  
  
moves the coordinatesystem for the vector

References
[move()](../../d5/db4/classBase_1_1Matrix4D.html#ac26497380187a175bcd5e43a0c81740f).

Referenced by
[draftguitools.gui_circulararray.CircularArray::Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
and
[draftguitools.gui_polararray.PolarArray::Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6).

## ◆ move() [3/4]

void Base::Matrix4D::move  | ( | double  | _x_ ,   
---|---|---|---  
|  | double  | _y_ ,   
|  | double  | _z_  
| ) | |   
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

Referenced by
[draftguitools.gui_circulararray.CircularArray::Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
and
[draftguitools.gui_polararray.PolarArray::Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6).

## ◆ move() [4/4]

void Base::Matrix4D::move  | ( | float  | _x_ ,   
---|---|---|---  
|  | float  | _y_ ,   
|  | float  | _z_  
| ) | |   
  
moves the coordinatesystem for the x,y,z value

References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

Referenced by
[draftguitools.gui_circulararray.CircularArray::Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
[draftguitools.gui_polararray.PolarArray::Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6),
[Data::ComplexGeoData::applyTranslation()](../../d8/daf/classData_1_1ComplexGeoData.html#a8dd74bf0b7000e68c6223498b01f066b),
[Base::ViewProjMatrix::getProjectionMatrix()](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a9c88e958a0eabeaa0942715bec0606bb),
[move()](../../d5/db4/classBase_1_1Matrix4D.html#acba412fbe0fe2b035de62770898c9cda),
[DraftUtils::DraftDxfRead::OnReadInsert()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#ac8f621a910fd6c038b68223ae2721519),
[Import::ImpExpDxfRead::OnReadInsert()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#aa0077bf26b3b3ccb2f92c59b71651ba1),
and
[transform()](../../d5/db4/classBase_1_1Matrix4D.html#af81d4febac264b2a48dca8b5c4649df9).

## ◆ multVec() [1/2]

void Base::Matrix4D::multVec  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _src_ ,   
---|---|---|---  
|  | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _dst_  
| ) | |  const  
  
Referenced by
[MeshCore::MeshGeomFacet::Transform()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a4f58a72ef69d6ed83d5b3525da62cf9b),
[MeshCore::MeshPointArray::Transform()](../../db/d5c/classMeshCore_1_1MeshPointArray.html#a9de448d67cc3887dac8a0b03260bbe18),
[Points::PointKernel::transformGeometry()](../../dc/de1/classPoints_1_1PointKernel.html#a9d2e317d17208cc8fde8c0976303cc0c),
and
[Points::PropertyNormalList::transformGeometry()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a064a298f4261410fe6727a3bbd903ca9).

## ◆ multVec() [2/2]

void Base::Matrix4D::multVec  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _src_ ,   
---|---|---|---  
|  | [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _dst_  
| ) | |  const  
  
## ◆ nullify()

void Matrix4D::nullify  | ( | | ) |   
---|---|---|---|---  
  
Makes a null matrix.

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) Base::Matrix4D::operator!=  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_| ) |  const  
---|---|---|---|---|---  
  
Comparison.

## ◆ operator*() [1/4]

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) Base::Matrix4D::operator*  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_| ) |  const  
---|---|---|---|---|---  
  
Matrix multiplication.

Referenced by
[inverseOrthogonal()](../../d5/db4/classBase_1_1Matrix4D.html#a59fc9807b582d580c0e91ef3d0b0a5b0).

## ◆ operator*() [2/4]

[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) Base::Matrix4D::operator*  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclVct_| ) |  const  
---|---|---|---|---|---  
  
References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ operator*() [3/4]

[Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) Base::Matrix4D::operator*  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclVct_| ) |  const  
---|---|---|---|---|---  
  
Multiplication matrix with vector.

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ operator*() [4/4]

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) Base::Matrix4D::operator*  | ( | double  | _scalar_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator*=() [1/2]

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & Base::Matrix4D::operator*=  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_| ) |   
---|---|---|---|---|---  
  
Matrix multiplication.

## ◆ operator*=() [2/2]

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & Base::Matrix4D::operator*=  | ( | double  | _scalar_| ) |   
---|---|---|---|---|---  
  
## ◆ operator+()

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) Base::Matrix4D::operator+  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_| ) |  const  
---|---|---|---|---|---  
  
Matrix addition.

## ◆ operator+=()

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & Base::Matrix4D::operator+=  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_| ) |   
---|---|---|---|---|---  
  
## ◆ operator-()

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) Base::Matrix4D::operator-  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_| ) |  const  
---|---|---|---|---|---  
  
Matrix subtraction.

## ◆ operator-=()

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & Base::Matrix4D::operator-=  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_| ) |   
---|---|---|---|---|---  
  
## ◆ operator=()

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & Base::Matrix4D::operator=  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_| ) |   
---|---|---|---|---|---  
  
Assignment.

## ◆ operator==()

[bool](../../d9/db9/classbool.html) Base::Matrix4D::operator==  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_| ) |  const  
---|---|---|---|---|---  
  
Comparison.

References [Base::float_traits< double
>::epsilon()](../../da/df3/structBase_1_1float__traits_3_01double_01_4.html#af8e8706ed747786f7edf1ddb4177cb21).

## ◆ operator[]() [1/2]

double * Base::Matrix4D::operator[]  | ( | unsigned short  | _usNdx_| ) |   
---|---|---|---|---|---  
  
Index operator.

## ◆ operator[]() [2/2]

const double * Base::Matrix4D::operator[]  | ( | unsigned short  | _usNdx_| ) |  const  
---|---|---|---|---|---  
  
Index operator.

## ◆ Outer() [1/2]

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & Matrix4D::Outer  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rV1_ ,   
---|---|---|---  
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rV2_  
| ) | |   
  
References
[setToUnity()](../../d5/db4/classBase_1_1Matrix4D.html#ac860beb3fa5c0c0fe9d1e305bd2b68b8),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ Outer() [2/2]

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & Matrix4D::Outer  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rV1_ ,   
---|---|---|---  
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rV2_  
| ) | |   
  
Outer product (Dyadic product)

References
[Outer()](../../d5/db4/classBase_1_1Matrix4D.html#a6da1790aab096b22aafe2aa485db7b37),
and
[setToUnity()](../../d5/db4/classBase_1_1Matrix4D.html#ac860beb3fa5c0c0fe9d1e305bd2b68b8).

Referenced by
[Outer()](../../d5/db4/classBase_1_1Matrix4D.html#a6da1790aab096b22aafe2aa485db7b37).

## ◆ Print()

void Matrix4D::Print  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ rotLine() [1/4]

void Matrix4D::rotLine  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclDir_ ,   
|  | double  | _fAngle_  
| ) | |   
  
Rotate around an arbitrary axis that needn't necessarily pass the origin in
radians.

References
[rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aefb253d9d003400aa224a52d7171ad6f),
and
[transform()](../../d5/db4/classBase_1_1Matrix4D.html#af81d4febac264b2a48dca8b5c4649df9).

## ◆ rotLine() [2/4]

void Matrix4D::rotLine  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclVct_ ,   
---|---|---|---  
|  | double  | _fAngle_  
| ) | |   
  
Rotate around an arbitrary axis passing the origin in radians.

References [Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ rotLine() [3/4]

void Matrix4D::rotLine  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclDir_ ,   
|  | float  | _fAngle_  
| ) | |   
  
Rotate around an arbitrary axis that needn't necessarily pass the origin in
radians.

References
[rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aefb253d9d003400aa224a52d7171ad6f).

## ◆ rotLine() [4/4]

void Matrix4D::rotLine  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclVct_ ,   
---|---|---|---  
|  | float  | _fAngle_  
| ) | |   
  
Rotate around an arbitrary axis passing the origin in radians.

References
[rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aefb253d9d003400aa224a52d7171ad6f).

Referenced by
[Matrix4D()](../../d5/db4/classBase_1_1Matrix4D.html#aff848b9c1b3ec8ce602679471ced18de),
[rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aefb253d9d003400aa224a52d7171ad6f),
and
[TechDraw::DrawUtil::vecRotate()](../../da/d23/classTechDraw_1_1DrawUtil.html#aac1da77931bff55f92121b1c93c19919).

## ◆ rotX()

void Matrix4D::rotX  | ( | double  | _fAngle_| ) |   
---|---|---|---|---|---  
  
Rotate around the X axis (in transformed space) for the given value in
radians.

## ◆ rotY()

void Matrix4D::rotY  | ( | double  | _fAngle_| ) |   
---|---|---|---|---|---  
  
Rotate around the Y axis (in transformed space) for the given value in
radians.

## ◆ rotZ()

void Matrix4D::rotZ  | ( | double  | _fAngle_| ) |   
---|---|---|---|---|---  
  
Rotate around the Z axis (in transformed space) for the given value in
radians.

Referenced by
[Part::Prism::execute()](../../dc/d69/classPart_1_1Prism.html#aee3abdd806303810dee9bcb407871e8e),
[Part::RegularPolygon::execute()](../../d2/d69/classPart_1_1RegularPolygon.html#ab826050ea7815c765e6f0615554e01f0),
[PartDesign::Prism::execute()](../../d9/daf/classPartDesign_1_1Prism.html#afbe0d9e86e58c4781f3f58aed9371937),
[DraftUtils::DraftDxfRead::OnReadInsert()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#ac8f621a910fd6c038b68223ae2721519),
and
[Import::ImpExpDxfRead::OnReadInsert()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#aa0077bf26b3b3ccb2f92c59b71651ba1).

## ◆ scale() [1/6]

void Matrix4D::scale  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclVct_| ) |   
---|---|---|---|---|---  
  
References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[automotive_design.cartesian_transformation_operator::scl()](../../d7/d5c/classautomotive__design_1_1cartesian__transformation__operator.html#a607065ae6d7bb5dacfd7c75bd6711dc5),
[config_control_design.cartesian_transformation_operator::scl()](../../d5/de5/classconfig__control__design_1_1cartesian__transformation__operator.html#a0f720927aeb8f85e823ae00966334520),
[ifc2x3.ifccartesiantransformationoperator::scl()](../../d8/d5d/classifc2x3_1_1ifccartesiantransformationoperator.html#a1230d04a4e6e505a3ea5cbb23a36f383),
and
[ifc4.ifccartesiantransformationoperator::scl()](../../d4/d39/classifc4_1_1ifccartesiantransformationoperator.html#a7a36aec732fadc2ec945b4ad3bc1570d).

## ◆ scale() [2/6]

void Matrix4D::scale  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclVct_| ) |   
---|---|---|---|---|---  
  
scale for the x,y,z value

References
[scale()](../../d5/db4/classBase_1_1Matrix4D.html#aa0838e1c628e3f405a83904679acec56).

Referenced by
[automotive_design.cartesian_transformation_operator::scl()](../../d7/d5c/classautomotive__design_1_1cartesian__transformation__operator.html#a607065ae6d7bb5dacfd7c75bd6711dc5),
[config_control_design.cartesian_transformation_operator::scl()](../../d5/de5/classconfig__control__design_1_1cartesian__transformation__operator.html#a0f720927aeb8f85e823ae00966334520),
[ifc2x3.ifccartesiantransformationoperator::scl()](../../d8/d5d/classifc2x3_1_1ifccartesiantransformationoperator.html#a1230d04a4e6e505a3ea5cbb23a36f383),
and
[ifc4.ifccartesiantransformationoperator::scl()](../../d4/d39/classifc4_1_1ifccartesiantransformationoperator.html#a7a36aec732fadc2ec945b4ad3bc1570d).

## ◆ scale() [3/6]

void Base::Matrix4D::scale  | ( | double  | _scalexyz_| ) |   
---|---|---|---|---|---  
  
References
[draftfunctions.scale::scale()](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10).

Referenced by
[automotive_design.cartesian_transformation_operator::scl()](../../d7/d5c/classautomotive__design_1_1cartesian__transformation__operator.html#a607065ae6d7bb5dacfd7c75bd6711dc5),
[config_control_design.cartesian_transformation_operator::scl()](../../d5/de5/classconfig__control__design_1_1cartesian__transformation__operator.html#a0f720927aeb8f85e823ae00966334520),
[ifc2x3.ifccartesiantransformationoperator::scl()](../../d8/d5d/classifc2x3_1_1ifccartesiantransformationoperator.html#a1230d04a4e6e505a3ea5cbb23a36f383),
and
[ifc4.ifccartesiantransformationoperator::scl()](../../d4/d39/classifc4_1_1ifccartesiantransformationoperator.html#a7a36aec732fadc2ec945b4ad3bc1570d).

## ◆ scale() [4/6]

void Base::Matrix4D::scale  | ( | double  | _x_ ,   
---|---|---|---  
|  | double  | _y_ ,   
|  | double  | _z_  
| ) | |   
  
References
[draftfunctions.scale::scale()](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10).

Referenced by
[automotive_design.cartesian_transformation_operator::scl()](../../d7/d5c/classautomotive__design_1_1cartesian__transformation__operator.html#a607065ae6d7bb5dacfd7c75bd6711dc5),
[config_control_design.cartesian_transformation_operator::scl()](../../d5/de5/classconfig__control__design_1_1cartesian__transformation__operator.html#a0f720927aeb8f85e823ae00966334520),
[ifc2x3.ifccartesiantransformationoperator::scl()](../../d8/d5d/classifc2x3_1_1ifccartesiantransformationoperator.html#a1230d04a4e6e505a3ea5cbb23a36f383),
and
[ifc4.ifccartesiantransformationoperator::scl()](../../d4/d39/classifc4_1_1ifccartesiantransformationoperator.html#a7a36aec732fadc2ec945b4ad3bc1570d).

## ◆ scale() [5/6]

void Base::Matrix4D::scale  | ( | float  | _scalexyz_| ) |   
---|---|---|---|---|---  
  
uniform scale

References
[draftfunctions.scale::scale()](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10).

Referenced by
[automotive_design.cartesian_transformation_operator::scl()](../../d7/d5c/classautomotive__design_1_1cartesian__transformation__operator.html#a607065ae6d7bb5dacfd7c75bd6711dc5),
[config_control_design.cartesian_transformation_operator::scl()](../../d5/de5/classconfig__control__design_1_1cartesian__transformation__operator.html#a0f720927aeb8f85e823ae00966334520),
[ifc2x3.ifccartesiantransformationoperator::scl()](../../d8/d5d/classifc2x3_1_1ifccartesiantransformationoperator.html#a1230d04a4e6e505a3ea5cbb23a36f383),
and
[ifc4.ifccartesiantransformationoperator::scl()](../../d4/d39/classifc4_1_1ifccartesiantransformationoperator.html#a7a36aec732fadc2ec945b4ad3bc1570d).

## ◆ scale() [6/6]

void Base::Matrix4D::scale  | ( | float  | _x_ ,   
---|---|---|---  
|  | float  | _y_ ,   
|  | float  | _z_  
| ) | |   
  
scale for the vector

References
[draftfunctions.scale::scale()](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10).

Referenced by
[App::LinkBaseExtension::extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a),
[Base::ViewProjMatrix::getProjectionMatrix()](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a9c88e958a0eabeaa0942715bec0606bb),
[App::LinkBaseExtension::getTransform()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa78286a7bc1a3dfdb80c98f58726d827),
[TechDraw::ShapeExtractor::getXShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4e820635335afa9ce7506faaf4274cbd),
[DraftUtils::DraftDxfRead::OnReadInsert()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#ac8f621a910fd6c038b68223ae2721519),
[Import::ImpExpDxfRead::OnReadInsert()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#aa0077bf26b3b3ccb2f92c59b71651ba1),
[scale()](../../d5/db4/classBase_1_1Matrix4D.html#ad9ce1a6cb945b73f95200100ec41d9f9),
[automotive_design.cartesian_transformation_operator::scl()](../../d7/d5c/classautomotive__design_1_1cartesian__transformation__operator.html#a607065ae6d7bb5dacfd7c75bd6711dc5),
[config_control_design.cartesian_transformation_operator::scl()](../../d5/de5/classconfig__control__design_1_1cartesian__transformation__operator.html#a0f720927aeb8f85e823ae00966334520),
[ifc2x3.ifccartesiantransformationoperator::scl()](../../d8/d5d/classifc2x3_1_1ifccartesiantransformationoperator.html#a1230d04a4e6e505a3ea5cbb23a36f383),
[ifc4.ifccartesiantransformationoperator::scl()](../../d4/d39/classifc4_1_1ifccartesiantransformationoperator.html#a7a36aec732fadc2ec945b4ad3bc1570d),
and
[Gui::ViewProviderLink::updateDataPrivate()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2f2113e0017af3819a9064380ed30d0d).

## ◆ setCol()

void Base::Matrix4D::setCol  | ( | unsigned short  | _usNdx_ ,   
---|---|---|---  
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _v_  
| ) | |   
  
Set column to vector.

## ◆ setGLMatrix()

void Matrix4D::setGLMatrix  | ( | const double  | _dMtrx_[16]| ) |   
---|---|---|---|---|---  
  
set the matrix in OpenGL style

Referenced by
[inverseGauss()](../../d5/db4/classBase_1_1Matrix4D.html#ab10ef93ba66ebfb66dfa31d923d100c5).

## ◆ setMatrix()

void Matrix4D::setMatrix  | ( | const double  | _dMtrx_[16]| ) |   
---|---|---|---|---|---  
  
## ◆ setRow()

void Base::Matrix4D::setRow  | ( | unsigned short  | _usNdx_ ,   
---|---|---|---  
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _v_  
| ) | |   
  
Set row to vector.

## ◆ setToUnity()

void Matrix4D::setToUnity  | ( | | ) |   
---|---|---|---|---  
  
Makes unity matrix.

Referenced by
[MeshCore::FunctionContainer::GetHessian()](../../dc/dd3/classMeshCore_1_1FunctionContainer.html#a81f096e1a4705eb02c0bba8757135763),
[MeshCore::AbstractPolygonTriangulator::GetTransformToFitPlane()](../../d9/d6e/classMeshCore_1_1AbstractPolygonTriangulator.html#aaaa240d0f1a906bdc7cc01c81dea9250),
[Hat()](../../d5/db4/classBase_1_1Matrix4D.html#aba4ac5381849e58b53387154016fad47),
[Base::Rotation::makeRotationByAxes()](../../d4/d18/classBase_1_1Rotation.html#a0b7c436d3243f3703959c7f6be8ecad2),
[Outer()](../../d5/db4/classBase_1_1Matrix4D.html#a6da1790aab096b22aafe2aa485db7b37),
[Mesh::PropertyNormalList::transformGeometry()](../../df/dcd/classMesh_1_1PropertyNormalList.html#a064a298f4261410fe6727a3bbd903ca9),
[Mesh::PropertyCurvatureList::transformGeometry()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a698d1e0cfd7a47a876f28ae6239bcfda),
[Points::PropertyNormalList::transformGeometry()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a064a298f4261410fe6727a3bbd903ca9),
and
[Points::PropertyCurvatureList::transformGeometry()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a698d1e0cfd7a47a876f28ae6239bcfda).

## ◆ setTrace()

void Base::Matrix4D::setTrace  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _v_| ) |   
---|---|---|---|---|---  
  
Set trace to vector.

## ◆ toAxisAngle() [1/2]

[bool](../../d9/db9/classbool.html) Matrix4D::toAxisAngle  | ( | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclBase_ ,   
---|---|---|---  
|  | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclDir_ ,   
|  | double & | _fAngle_ ,   
|  | double & | _fTranslation_  
| ) | |  const  
  
References [Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ toAxisAngle() [2/2]

[bool](../../d9/db9/classbool.html) Matrix4D::toAxisAngle  | ( | [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclBase_ ,   
---|---|---|---  
|  | [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclDir_ ,   
|  | float & | _rfAngle_ ,   
|  | float & | _fTranslation_  
| ) | |  const  
  
Extract the rotation axis and angle. Therefore the 3x3 submatrix must be
orthogonal.

If this matrix describes a rotation around an arbitrary axis with a
translation (in axis direction) then the base point of the axis, its
direction, the rotation angle and the translation part get calculated.

In this case the return value is set to true, if this matrix doesn't describe
a rotation false is returned.

The translation vector can be calculated with _fTranslation_ * _rclDir_ ,
whereas the length of _rclDir_ is normalized to 1.

Note: In case the _fTranslation_ part is zero then passing _rclBase_ ,
_rclDir_ and _rfAngle_ to a new matrix object creates an identical matrix.

References
[toAxisAngle()](../../d5/db4/classBase_1_1Matrix4D.html#a3c28ec45a2f21383dcdb5c3d1b70ee82).

Referenced by
[toAxisAngle()](../../d5/db4/classBase_1_1Matrix4D.html#a3c28ec45a2f21383dcdb5c3d1b70ee82).

## ◆ toString()

std::string Matrix4D::toString  | ( | | ) |  const  
---|---|---|---|---  
  
write the 16 double of the matrix into a string

## ◆ trace()

[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) Base::Matrix4D::trace  | ( | | ) |  const  
---|---|---|---|---  
  
Get vector of trace.

## ◆ transform() [1/2]

void Matrix4D::transform  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclVct_ ,   
---|---|---|---  
|  | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_  
| ) | |   
  
References
[move()](../../d5/db4/classBase_1_1Matrix4D.html#ac26497380187a175bcd5e43a0c81740f).

Referenced by
[importSVG.svgHandler::applyTrans()](../../dc/d45/classimportSVG_1_1svgHandler.html#a38ca516f06b0765c43bc94623af7b74c),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[importSVG.svgHandler::endElement()](../../dc/d45/classimportSVG_1_1svgHandler.html#a1bd77a0a99233ef4a9075eefc2da04f3),
[ArchSite.Compass::locate()](../../d9/d61/classArchSite_1_1Compass.html#ab97b56e1db99fff1ca2d03d1819a0da5),
[ArchSite.Compass::rotate()](../../d9/d61/classArchSite_1_1Compass.html#a265d59029ed54f579ec07d75beadffc0),
and
[ArchSite.Compass::scale()](../../d9/d61/classArchSite_1_1Compass.html#a6bd34d985770e9ec9970bee17031d98b).

## ◆ transform() [2/2]

void Matrix4D::transform  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclVct_ ,   
---|---|---|---  
|  | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtrx_  
| ) | |   
  
transform (move,scale,rotate) around a point

References
[move()](../../d5/db4/classBase_1_1Matrix4D.html#ac26497380187a175bcd5e43a0c81740f).

Referenced by
[importSVG.svgHandler::applyTrans()](../../dc/d45/classimportSVG_1_1svgHandler.html#a38ca516f06b0765c43bc94623af7b74c),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[importSVG.svgHandler::endElement()](../../dc/d45/classimportSVG_1_1svgHandler.html#a1bd77a0a99233ef4a9075eefc2da04f3),
[ArchSite.Compass::locate()](../../d9/d61/classArchSite_1_1Compass.html#ab97b56e1db99fff1ca2d03d1819a0da5),
[ArchSite.Compass::rotate()](../../d9/d61/classArchSite_1_1Compass.html#a265d59029ed54f579ec07d75beadffc0),
[rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aec5a2013fb02d974a514e5d735b87bcd),
and
[ArchSite.Compass::scale()](../../d9/d61/classArchSite_1_1Compass.html#a6bd34d985770e9ec9970bee17031d98b).

## ◆ transpose()

void Matrix4D::transpose  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[analyse()](../../d5/db4/classBase_1_1Matrix4D.html#a9303ce9048d7f949a108b12e928a08e0),
and
[inverseOrthogonal()](../../d5/db4/classBase_1_1Matrix4D.html#a59fc9807b582d580c0e91ef3d0b0a5b0).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Matrix.h
  * FreeCAD/src/Base/Matrix.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

