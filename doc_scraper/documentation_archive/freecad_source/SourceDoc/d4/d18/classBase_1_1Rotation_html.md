---
url: https://freecad.github.io/SourceDoc/d4/d18/classBase_1_1Rotation.html
scraped_at: 2025-09-08T15:17:11.145278
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Rotation](../../d4/d18/classBase_1_1Rotation.html)

[List of all members](../../d7/d41/classBase_1_1Rotation-members.html) | Public Types | Public Member Functions | Static Public Member Functions

Base::Rotation Class Reference

`#include <Rotation.h>`

##  Public Types  
  
---  
enum | [EulerSequence](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678e) {   
[Invalid](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ead7113376f16c44e537617a61a852aa14)
,
[EulerAngles](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea5ee836a0e6906fe49cd1f90e6fbe37d4)
,
[YawPitchRoll](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678eafab385fbf1927d35a3adffa382a9e2a2)
,
[Extrinsic_XYZ](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678eaf65854933f8ece6413031fe649bdd8f5)
,  
[Extrinsic_XZY](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea8056fd4581448df64151aade62a64eac)
,
[Extrinsic_YZX](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea1b4af56092922032ef4b411c6cf00846)
,
[Extrinsic_YXZ](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea1a3952673afea2a8c95e6c8422298ca8)
,
[Extrinsic_ZXY](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea5a40e886ac1f3d9c190b6a3ff2a03926)
,  
[Extrinsic_ZYX](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea18c9ac496158676107db8a6cebe3d03f)
,
[Intrinsic_XYZ](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea741f339b22227a547d80d89d98d06006)
,
[Intrinsic_XZY](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea7d32f603f75fc5238dfc43863b796c23)
,
[Intrinsic_YZX](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea6f1e192ed7c08e4e46115a36751b3cde)
,  
[Intrinsic_YXZ](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678eadaee2904d268d9e7b808971e314cd158)
,
[Intrinsic_ZXY](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea0cf0380b3f2fb6e92c9039135e4f46cd)
,
[Intrinsic_ZYX](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea81cc1d7e731e398fcc66de674d977766)
,
[Extrinsic_XYX](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea411b5085829d94bd4cc8682989e6b497)
,  
[Extrinsic_XZX](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea2af109d7eb50749705c2dea1cc2b8ea5)
,
[Extrinsic_YZY](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678eac75f0ba5eca42998a1dcd40159feb9f4)
,
[Extrinsic_YXY](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea366f6e0347adb21662bee2eba27d1db4)
,
[Extrinsic_ZYZ](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea962523d39a63dd419d8c559c7949ad31)
,  
[Extrinsic_ZXZ](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea78bbe2fab9a9cc1c2e037a82beecf77b)
,
[Intrinsic_XYX](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678eaeba05b6994da4c6634eddb2e05c923bf)
,
[Intrinsic_XZX](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678eae4c3a4f2d01be86002d9eb235bb35101)
,
[Intrinsic_YZY](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea4451cff7847e4a7bb8aba45de54377e0)
,  
[Intrinsic_YXY](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678eac730d8f9e4fd17060690fbfb939476ff)
,
[Intrinsic_ZXZ](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea0a547f002aaa69031f40d3f8e9525556)
,
[Intrinsic_ZYZ](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea5f1e7a1208a5ef36565df7ae1bbc3779)
,
[EulerSequenceLast](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea731cd34425700647c06b5aa25d343888)  
}  
  
##  Public Member Functions  
  
---  
void | [getEulerAngles](../../d4/d18/classBase_1_1Rotation.html#a45744af0651d0b716ff5a279a82efe94) ([EulerSequence](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678e) seq, double &alpha, double &beta, double &gamma) const  
void | [getRawValue](../../d4/d18/classBase_1_1Rotation.html#afe860f0bcfaec728e99861e4c65904aa) ([Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &axis, double &rfAngle) const  
| Does the same as the method above unless normalizing the axis.
[More...](../../d4/d18/classBase_1_1Rotation.html#afe860f0bcfaec728e99861e4c65904aa)  
  
const double * | [getValue](../../d4/d18/classBase_1_1Rotation.html#a995899d98b886215e24758cb6da029dd) () const  
| Methods to get or set rotations.
[More...](../../d4/d18/classBase_1_1Rotation.html#a995899d98b886215e24758cb6da029dd)  
  
void | [getValue](../../d4/d18/classBase_1_1Rotation.html#a8c7de33b95060dff50be1912476aa0d1) (double &q0, double &q1, double &q2, double &q3) const  
void | [getValue](../../d4/d18/classBase_1_1Rotation.html#ad98999c960a074e637a9d8a56bcef7f5) ([Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &matrix) const  
| Returns this rotation in form of a matrix.
[More...](../../d4/d18/classBase_1_1Rotation.html#ad98999c960a074e637a9d8a56bcef7f5)  
  
void | [getValue](../../d4/d18/classBase_1_1Rotation.html#af95c57a06636f68b2a6cc779dc042edd) ([Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &axis, double &rfAngle) const  
| If not a null quaternion then _axis_ will be normalized.
[More...](../../d4/d18/classBase_1_1Rotation.html#af95c57a06636f68b2a6cc779dc042edd)  
  
void | [getYawPitchRoll](../../d4/d18/classBase_1_1Rotation.html#a6f698aefd52eae38d85f751db969e34b) (double &y, double &p, double &r) const  
| Euler angles in yaw,pitch,roll notation.
[More...](../../d4/d18/classBase_1_1Rotation.html#a6f698aefd52eae38d85f751db969e34b)  
  
[Rotation](../../d4/d18/classBase_1_1Rotation.html) | [inverse](../../d4/d18/classBase_1_1Rotation.html#a6a9f25fb1ab2ab0f607a9caf0e54b96a) () const  
[Rotation](../../d4/d18/classBase_1_1Rotation.html) & | [invert](../../d4/d18/classBase_1_1Rotation.html#a876705414e92f79fcba83e9d6f0e4b42) ()  
| Invert rotations.
[More...](../../d4/d18/classBase_1_1Rotation.html#a876705414e92f79fcba83e9d6f0e4b42)  
  
[bool](../../d9/db9/classbool.html) | [isIdentity](../../d4/d18/classBase_1_1Rotation.html#a969256cb1d71bfa521429992f930a5ea) () const  
[bool](../../d9/db9/classbool.html) | [isNull](../../d4/d18/classBase_1_1Rotation.html#a90b3756767a8a3625a536f0bde531c5f) () const  
[bool](../../d9/db9/classbool.html) | [isSame](../../d4/d18/classBase_1_1Rotation.html#a6d176928529120d0697e288cec4a8e7b) (const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &) const  
[bool](../../d9/db9/classbool.html) | [isSame](../../d4/d18/classBase_1_1Rotation.html#aeca2576faed35a27694c1ad995867d1a) (const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &, double tol) const  
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [multVec](../../d4/d18/classBase_1_1Rotation.html#a821f2724bbe295e18be79684e61094a6) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &src) const  
void | [multVec](../../d4/d18/classBase_1_1Rotation.html#a3cdb5a5eb357dd8a1c974f7374fe4a87) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &src, [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &dst) const  
[bool](../../d9/db9/classbool.html) | [operator!=](../../d4/d18/classBase_1_1Rotation.html#a0725d326f9813eae2abbdd407012d99e) (const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &q) const  
[Rotation](../../d4/d18/classBase_1_1Rotation.html) | [operator*](../../d4/d18/classBase_1_1Rotation.html#ab648b8088b9d49c05f00eea98cd8eeeb) (const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &q) const  
[Rotation](../../d4/d18/classBase_1_1Rotation.html) & | [operator*=](../../d4/d18/classBase_1_1Rotation.html#a6a65332d4581fb8be3a84aa152790a0e) (const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &q)  
| Operators.
[More...](../../d4/d18/classBase_1_1Rotation.html#a6a65332d4581fb8be3a84aa152790a0e)  
  
void | [operator=](../../d4/d18/classBase_1_1Rotation.html#a01b5c5891fcc142bc88f41ff4203dc9b) (const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &)  
[bool](../../d9/db9/classbool.html) | [operator==](../../d4/d18/classBase_1_1Rotation.html#aee08ae5bec82fb1c54a48d6ee710d737) (const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &q) const  
double & | [operator[]](../../d4/d18/classBase_1_1Rotation.html#abd829d4f8db961e97d6720ae751501c4) (unsigned short usIndex)  
const double & | [operator[]](../../d4/d18/classBase_1_1Rotation.html#ade4cf31d5a96cb7473e4a617d2453408) (unsigned short usIndex) const  
|
[Rotation](../../d4/d18/classBase_1_1Rotation.html#a13ea1d345ca0a92c0f09b4de544ca460)
()  
| Construction.
[More...](../../d4/d18/classBase_1_1Rotation.html#a13ea1d345ca0a92c0f09b4de544ca460)  
  
|
[Rotation](../../d4/d18/classBase_1_1Rotation.html#a0b44b787886cb5c6ee83a5b852241e36)
(const double q0, const double q1, const double q2, const double q3)  
| Construct a rotation initialized with the given quaternion components: q0 =
x, q1 = y, q2 = z and q3 = w, where the quaternion is specified by
q=w+xi+yj+zk.
[More...](../../d4/d18/classBase_1_1Rotation.html#a0b44b787886cb5c6ee83a5b852241e36)  
  
|
[Rotation](../../d4/d18/classBase_1_1Rotation.html#a4de6e781008526df7c4f1ffca423c306)
(const double q[4])  
| Construct a rotation initialized with the given quaternion components: q[0]
= x, q[1] = y, q[2] = z and q[3] = w, where the quaternion is specified by
q=w+xi+yj+zk.
[More...](../../d4/d18/classBase_1_1Rotation.html#a4de6e781008526df7c4f1ffca423c306)  
  
|
[Rotation](../../d4/d18/classBase_1_1Rotation.html#a4845a2f9fd716d19345b73be39b3d21f)
(const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &matrix)  
|
[Rotation](../../d4/d18/classBase_1_1Rotation.html#ab8d61ec28cfb5a1a50727bad569a6901)
(const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &rot)  
|
[Rotation](../../d4/d18/classBase_1_1Rotation.html#a6ded479672faa2dea5197741d8233e70)
(const
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e)
&axis, const double fAngle)  
| Construct a rotation by rotation axis and angle.
[More...](../../d4/d18/classBase_1_1Rotation.html#a6ded479672faa2dea5197741d8233e70)  
  
|
[Rotation](../../d4/d18/classBase_1_1Rotation.html#adbe4e0c63bcd46a1a1f9041ac9472516)
(const
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e)
&rotateFrom, const
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e)
&rotateTo)  
void | [scaleAngle](../../d4/d18/classBase_1_1Rotation.html#acd28bd5bf84be383248a4deaa5be8387) (const double scaleFactor)  
void | [setEulerAngles](../../d4/d18/classBase_1_1Rotation.html#a52a56e06607a716bb38c8dd815ea67c1) ([EulerSequence](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678e) seq, double alpha, double beta, double gamma)  
void | [setValue](../../d4/d18/classBase_1_1Rotation.html#a1219586eb3bf57070cc0ae34392d114f) (const double q0, const double q1, const double q2, const double q3)  
void | [setValue](../../d4/d18/classBase_1_1Rotation.html#a6ecd31ec082c19071772be21c1eb0b16) (const double q[4])  
void | [setValue](../../d4/d18/classBase_1_1Rotation.html#aad214cd54652ce3ac0070dc828ea66ab) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &matrix)  
void | [setValue](../../d4/d18/classBase_1_1Rotation.html#a62c0b4012cb383de60d0e4a225c39550) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &axis, const double fAngle)  
void | [setValue](../../d4/d18/classBase_1_1Rotation.html#a30632b9d88a9a7ac0886568842791397) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rotateFrom, const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rotateTo)  
void | [setYawPitchRoll](../../d4/d18/classBase_1_1Rotation.html#a077074c2a926f0b51dd2a384d1a48b11) (double y, double p, double r)  
| Euler angles in yaw,pitch,roll notation.
[More...](../../d4/d18/classBase_1_1Rotation.html#a077074c2a926f0b51dd2a384d1a48b11)  
  
  
##  Static Public Member Functions  
  
---  
static [EulerSequence](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678e) | [eulerSequenceFromName](../../d4/d18/classBase_1_1Rotation.html#a516cf440c8328dde0c92347da673744b) (const char *name)  
static const char * | [eulerSequenceName](../../d4/d18/classBase_1_1Rotation.html#ab45c593e91b076575ed44bed2bcc1826) ([EulerSequence](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678e) seq)  
static [Rotation](../../d4/d18/classBase_1_1Rotation.html) | [identity](../../d4/d18/classBase_1_1Rotation.html#a3000e4c0ff0259294e5bf14ccd6fcaec) ()  
static [Rotation](../../d4/d18/classBase_1_1Rotation.html) | [makeRotationByAxes](../../d4/d18/classBase_1_1Rotation.html#a0b7c436d3243f3703959c7f6be8ecad2) ([Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) xdir, [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) ydir, [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) zdir, const char *priorityOrder="ZXY")  
| makeRotationByAxes(xdir, ydir, zdir, priorityOrder): creates a rotation that
converts a vector in local cs with axes given as arguments, into a vector in
global cs.
[More...](../../d4/d18/classBase_1_1Rotation.html#a0b7c436d3243f3703959c7f6be8ecad2)  
  
static [Rotation](../../d4/d18/classBase_1_1Rotation.html) | [slerp](../../d4/d18/classBase_1_1Rotation.html#ad8eeefc5709d927b052bf0199c49be3c) (const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &rot0, const [Rotation](../../d4/d18/classBase_1_1Rotation.html) &rot1, double t)  
| Specialty constructors.
[More...](../../d4/d18/classBase_1_1Rotation.html#ad8eeefc5709d927b052bf0199c49be3c)  
  
  
## Member Enumeration Documentation

## ◆ EulerSequence

enum
[Base::Rotation::EulerSequence](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678e)  
---  
  
Enumerator  
---  
Invalid |   
EulerAngles | Classic Euler angles, alias to Intrinsic_ZXZ.   
YawPitchRoll | Yaw Pitch Roll (or nautical) angles, alias to Intrinsic_ZYX.   
Extrinsic_XYZ |   
Extrinsic_XZY |   
Extrinsic_YZX |   
Extrinsic_YXZ |   
Extrinsic_ZXY |   
Extrinsic_ZYX |   
Intrinsic_XYZ |   
Intrinsic_XZY |   
Intrinsic_YZX |   
Intrinsic_YXZ |   
Intrinsic_ZXY |   
Intrinsic_ZYX |   
Extrinsic_XYX |   
Extrinsic_XZX |   
Extrinsic_YZY |   
Extrinsic_YXY |   
Extrinsic_ZYZ |   
Extrinsic_ZXZ |   
Intrinsic_XYX |   
Intrinsic_XZX |   
Intrinsic_YZY |   
Intrinsic_YXY |   
Intrinsic_ZXZ |   
Intrinsic_ZYZ |   
EulerSequenceLast |   
  
## Constructor & Destructor Documentation

## ◆ Rotation() [1/7]

Rotation::Rotation  | ( | | ) |   
---|---|---|---|---  
  
Construction.

Referenced by
[identity()](../../d4/d18/classBase_1_1Rotation.html#a3000e4c0ff0259294e5bf14ccd6fcaec),
[makeRotationByAxes()](../../d4/d18/classBase_1_1Rotation.html#a0b7c436d3243f3703959c7f6be8ecad2),
and
[slerp()](../../d4/d18/classBase_1_1Rotation.html#ad8eeefc5709d927b052bf0199c49be3c).

## ◆ Rotation() [2/7]

Rotation::Rotation  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _axis_ ,   
---|---|---|---  
|  | const double  | _fAngle_  
| ) | |   
  
Construct a rotation by rotation axis and angle.

References
[setValue()](../../d4/d18/classBase_1_1Rotation.html#a1219586eb3bf57070cc0ae34392d114f).

## ◆ Rotation() [3/7]

Rotation::Rotation  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _matrix_| ) |   
---|---|---|---|---|---  
  
References
[setValue()](../../d4/d18/classBase_1_1Rotation.html#a1219586eb3bf57070cc0ae34392d114f).

## ◆ Rotation() [4/7]

Rotation::Rotation  | ( | const double  | _q_[4]| ) |   
---|---|---|---|---|---  
  
Construct a rotation initialized with the given quaternion components: q[0] =
x, q[1] = y, q[2] = z and q[3] = w, where the quaternion is specified by
q=w+xi+yj+zk.

References
[setValue()](../../d4/d18/classBase_1_1Rotation.html#a1219586eb3bf57070cc0ae34392d114f).

## ◆ Rotation() [5/7]

Rotation::Rotation  | ( | const double  | _q0_ ,   
---|---|---|---  
|  | const double  | _q1_ ,   
|  | const double  | _q2_ ,   
|  | const double  | _q3_  
| ) | |   
  
Construct a rotation initialized with the given quaternion components: q0 = x,
q1 = y, q2 = z and q3 = w, where the quaternion is specified by q=w+xi+yj+zk.

References
[setValue()](../../d4/d18/classBase_1_1Rotation.html#a1219586eb3bf57070cc0ae34392d114f).

## ◆ Rotation() [6/7]

Rotation::Rotation  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rotateFrom_ ,   
---|---|---|---  
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rotateTo_  
| ) | |   
  
References
[setValue()](../../d4/d18/classBase_1_1Rotation.html#a1219586eb3bf57070cc0ae34392d114f).

## ◆ Rotation() [7/7]

Rotation::Rotation  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _rot_| ) |   
---|---|---|---|---|---  
  
## Member Function Documentation

## ◆ eulerSequenceFromName()

| [Rotation::EulerSequence](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678e) Rotation::eulerSequenceFromName  | ( | const char *  | _name_| ) |   
---|---|---|---|---|---  
static  
  
References
[Invalid](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ead7113376f16c44e537617a61a852aa14).

## ◆ eulerSequenceName()

| const char * Rotation::eulerSequenceName  | ( | [EulerSequence](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678e) | _seq_| ) |   
---|---|---|---|---|---  
static  
  
References
[EulerSequenceLast](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea731cd34425700647c06b5aa25d343888),
and
[Invalid](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ead7113376f16c44e537617a61a852aa14).

## ◆ getEulerAngles()

void Rotation::getEulerAngles  | ( | [EulerSequence](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678e) | _seq_ ,   
---|---|---|---  
|  | double & | _alpha_ ,   
|  | double & | _beta_ ,   
|  | double & | _gamma_  
| ) | |  const  
  
References
[getValue()](../../d4/d18/classBase_1_1Rotation.html#a995899d98b886215e24758cb6da029dd).

## ◆ getRawValue()

void Rotation::getRawValue  | ( | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _axis_ ,   
---|---|---|---  
|  | double & | _rfAngle_  
| ) | |  const  
  
Does the same as the method above unless normalizing the axis.

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ getValue() [1/4]

const double * Rotation::getValue  | ( | | ) |  const  
---|---|---|---|---  
  
Methods to get or set rotations.

Referenced by
[Data::ComplexGeoData::applyRotation()](../../d8/daf/classData_1_1ComplexGeoData.html#aef9dda5fc94a65d2b1578e70921ed329),
[Import::ExportOCAF::createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[Part::Tools::fromPlacement()](../../d9/d36/classPart_1_1Tools.html#a545eed1fde2f3eae32b94b5d24f6e960),
[getEulerAngles()](../../d4/d18/classBase_1_1Rotation.html#a45744af0651d0b716ff5a279a82efe94),
[Part::Feature::getLocation()](../../d7/d7e/classPart_1_1Feature.html#a84164b4adfe9b6ecef87da8d7aa1ac9d),
[Part::FeatureReference::getLocation()](../../d2/da1/classPart_1_1FeatureReference.html#aee6f4d426e17d5a0193108fd06f7309c),
[operator*=()](../../d4/d18/classBase_1_1Rotation.html#a6a65332d4581fb8be3a84aa152790a0e),
[Path::Toolpath::recalculate()](../../d6/d0c/classPath_1_1Toolpath.html#a6fcb5afb3f1023ef686cd87b4f69c0f9),
[Part::Geometry::rotate()](../../dc/df0/classPart_1_1Geometry.html#a3c7ebf21592da6737fccb28bf9508a75),
[Import::ExportOCAF::saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[scaleAngle()](../../d4/d18/classBase_1_1Rotation.html#acd28bd5bf84be383248a4deaa5be8387),
[Gui::PropertyEditor::RotationHelper::setAxis()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#a3b49948e5ac8d72ce290c36b98f94bc3),
[Gui::View3DInventorPy::setCameraOrientation()](../../d3/df7/classGui_1_1View3DInventorPy.html#adfb67b877d2c67ad696b64fdde062363),
[Part::TopoShape::setShapePlacement()](../../d8/ded/classPart_1_1TopoShape.html#a8ae38d04353d5ccc4c60beaad3a4a497),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[Gui::ViewProviderDragger::updateTransform()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5f8676364e82e30b6e558c8f25e06b88),
and
[Gui::View3DInventorPy::viewPosition()](../../d3/df7/classGui_1_1View3DInventorPy.html#aa0c6354d70103dbcf7f4fddc2c12265d).

## ◆ getValue() [2/4]

void Rotation::getValue  | ( | double & | _q0_ ,   
---|---|---|---  
|  | double & | _q1_ ,   
|  | double & | _q2_ ,   
|  | double & | _q3_  
| ) | |  const  
  
## ◆ getValue() [3/4]

void Rotation::getValue  | ( | [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _matrix_| ) |  const  
---|---|---|---|---|---  
  
Returns this rotation in form of a matrix.

## ◆ getValue() [4/4]

void Rotation::getValue  | ( | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _axis_ ,   
---|---|---|---  
|  | double & | _rfAngle_  
| ) | |  const  
  
If not a null quaternion then _axis_ will be normalized.

References [Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ getYawPitchRoll()

void Rotation::getYawPitchRoll  | ( | double & | _y_ ,   
---|---|---|---  
|  | double & | _p_ ,   
|  | double & | _r_  
| ) | |  const  
  
Euler angles in yaw,pitch,roll notation.

Referenced by
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[Path::Command::setFromPlacement()](../../d7/d2e/classPath_1_1Command.html#a62372d49bbf1003cc81fe7035c7b592e),
[Path::Command::transform()](../../d7/d2e/classPath_1_1Command.html#a86423c625f09285dd820b578462c199e),
and
[RobotGui::TaskTrajectoryDressUpParameter::viewPlacement()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#acf61f87e511a7480c2dfa829800e17cc).

## ◆ identity()

| [Rotation](../../d4/d18/classBase_1_1Rotation.html) Rotation::identity  | ( | | ) |   
---|---|---|---|---  
static  
  
References
[Rotation()](../../d4/d18/classBase_1_1Rotation.html#a13ea1d345ca0a92c0f09b4de544ca460).

## ◆ inverse()

[Rotation](../../d4/d18/classBase_1_1Rotation.html) Rotation::inverse  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ invert()

[Rotation](../../d4/d18/classBase_1_1Rotation.html) & Rotation::invert  | ( | | ) |   
---|---|---|---|---  
  
Invert rotations.

Referenced by
[PathScripts.PathDressupLeadInOut.ObjectDressup::getLeadEnd()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#ac4be8c95d4aa1440fb03c096c4e44e57),
and
[PathScripts.PathDressupLeadInOut.ObjectDressup::getLeadStart()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#a2d9de34620ee069b425e7f99f0efe9da).

## ◆ isIdentity()

[bool](../../d9/db9/classbool.html) Rotation::isIdentity  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[ArchComponent.Component::applyShape()](../../de/d87/classArchComponent_1_1Component.html#ac8174503690f56dcf8b6d8e324fadbc5),
[ArchComponent.Component::getExtrusionData()](../../de/d87/classArchComponent_1_1Component.html#abe6b1db0166c4b8edb14db2440ab4919),
[ArchComponent.Component::processSubShapes()](../../de/d87/classArchComponent_1_1Component.html#a34cd7509406ea5e01a1d72b41e900742),
[Points::PlyWriter::write()](../../d4/d57/classPoints_1_1PlyWriter.html#afcad40b7eec0e6e291d5bb1ffc6b0014),
and
[Points::PcdWriter::write()](../../df/dc2/classPoints_1_1PcdWriter.html#a29a665c849f6da4f82ba12eb6bf06095).

## ◆ isNull()

[bool](../../d9/db9/classbool.html) Rotation::isNull  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isSame() [1/2]

[bool](../../d9/db9/classbool.html) Rotation::isSame  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _q_| ) |  const  
---|---|---|---|---|---  
  
## ◆ isSame() [2/2]

[bool](../../d9/db9/classbool.html) Rotation::isSame  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _q_ ,   
---|---|---|---  
|  | double  | _tol_  
| ) | |  const  
  
## ◆ makeRotationByAxes()

| [Rotation](../../d4/d18/classBase_1_1Rotation.html) Rotation::makeRotationByAxes  | ( | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | _xdir_ ,   
---|---|---|---  
|  | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | _ydir_ ,   
|  | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | _zdir_ ,   
|  | const char *  | _priorityOrder_ = `"ZXY"`  
| ) | |   
static  
  
makeRotationByAxes(xdir, ydir, zdir, priorityOrder): creates a rotation that
converts a vector in local cs with axes given as arguments, into a vector in
global cs.

Parameters

     xdir| is wanted direction of local X axis   
---|---  
ydir| ...  
zdir|  
priorityOrder| sets which directions are followed. It is a string like "ZXY".
This means, Z direction is followed precisely; X direction is corrected to be
perpendicular to Z direction, and used; Y direction argument is ignored
altogether (Y direction is generated from Z and X).  
  
If only one vector provided is nonzero, the other two directions are picked
automatically.

References [Base::Vector3< _Precision
>::Cross()](../../d1/d13/classBase_1_1Vector3.html#aeff630b92f5a52f5aa52dc87ccf77bac),
[Base::Vector3< _Precision
>::Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[Rotation()](../../d4/d18/classBase_1_1Rotation.html#a13ea1d345ca0a92c0f09b4de544ca460),
[Base::Matrix4D::setToUnity()](../../d5/db4/classBase_1_1Matrix4D.html#ac860beb3fa5c0c0fe9d1e305bd2b68b8),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98).

## ◆ multVec() [1/2]

[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) Rotation::multVec  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _src_| ) |  const  
---|---|---|---|---|---  
  
References
[multVec()](../../d4/d18/classBase_1_1Rotation.html#a3cdb5a5eb357dd8a1c974f7374fe4a87).

## ◆ multVec() [2/2]

void Rotation::multVec  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _src_ ,   
---|---|---|---  
|  | [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _dst_  
| ) | |  const  
  
Referenced by
[ReenGui::FitBSplineSurfaceWidget::accept()](../../d9/d48/classReenGui_1_1FitBSplineSurfaceWidget.html#af94ddfaebc20a805f34a94face578ce6),
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Part::Extrusion::calculateShapeNormal()](../../db/d6c/classPart_1_1Extrusion.html#a9068fcaf96e864a90a04b860140de9c9),
[Path::compensateRotation()](../../d2/df0/namespacePath.html#aadca55cb07003f879ce82c8cb429d9a8),
[Base::CoordinateSystem::displacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[PartDesign::Line::getDirection()](../../d0/d2a/classPartDesign_1_1Line.html#af89a81d14e0ccb27353122f43844600c),
[PartDesign::Plane::getNormal()](../../df/df0/classPartDesign_1_1Plane.html#ad208270773ba2e063212171e36895e6e),
[PartDesign::ProfileBased::getProfileNormal()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#af389a14c1da76e8ce4aa4dd5dc874540),
[PartDesign::ProfileBased::getReversedAngle()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a3b3aa636b6181cd9edacd1f7b1412f0b),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[PartDesign::CoordinateSystem::getXAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a04498f548e650362eb2c094f89f5470b),
[PartDesign::CoordinateSystem::getYAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a38beb2d58454d7cb970b4dfb222fe8d3),
[PartDesign::CoordinateSystem::getZAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a4b9edd67bb7f8c895a9f5bd726fb92e2),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
[PartDesign::Feature::makePlnFromPlane()](../../d7/d51/classPartDesign_1_1Feature.html#a6ab00d23c99b505b5bf57dedac353631),
[multVec()](../../d4/d18/classBase_1_1Rotation.html#a821f2724bbe295e18be79684e61094a6),
[Attacher::AttachEngine::placementFactory()](../../d2/d85/classAttacher_1_1AttachEngine.html#a0eff77539401a8d4a04554a970bd85b4),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[TechDraw::DrawViewSection::sectionLineEnds()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a4f8580c4dea1570bca8520f11f871ebe),
[Gui::View3DInventorViewer::toggleClippingPlane()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ae41b2cfdc548e959d744937ff7a85317),
[Gui::ManualAlignment::Private::transformation2x2()](../../d9/d29/classManualAlignment_1_1Private.html#a0573960c1dd6d2a1686ceced75e1cdf7),
[Gui::ManualAlignment::Private::transformation3x3()](../../d9/d29/classManualAlignment_1_1Private.html#aa5fbe288a60e9ea2ed178adfc883fbeb),
[Path::PathSegmentWalker::walk()](../../d0/d7b/classPath_1_1PathSegmentWalker.html#a2d2253be4424a16caf28ec136b658dc6),
[Points::PlyWriter::write()](../../d4/d57/classPoints_1_1PlyWriter.html#afcad40b7eec0e6e291d5bb1ffc6b0014),
and
[Points::PcdWriter::write()](../../df/dc2/classPoints_1_1PcdWriter.html#a29a665c849f6da4f82ba12eb6bf06095).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) Rotation::operator!=  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _q_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator*()

[Rotation](../../d4/d18/classBase_1_1Rotation.html) Rotation::operator*  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _q_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator*=()

[Rotation](../../d4/d18/classBase_1_1Rotation.html) & Rotation::operator*=  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _q_| ) |   
---|---|---|---|---|---  
  
Operators.

References
[getValue()](../../d4/d18/classBase_1_1Rotation.html#a995899d98b886215e24758cb6da029dd),
and
[setValue()](../../d4/d18/classBase_1_1Rotation.html#a1219586eb3bf57070cc0ae34392d114f).

## ◆ operator=()

void Rotation::operator=  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _rot_| ) |   
---|---|---|---|---|---  
  
## ◆ operator==()

[bool](../../d9/db9/classbool.html) Rotation::operator==  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _q_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator[]() [1/2]

double & Base::Rotation::operator[]  | ( | unsigned short  | _usIndex_| ) |   
---|---|---|---|---|---  
  
## ◆ operator[]() [2/2]

const double & Base::Rotation::operator[]  | ( | unsigned short  | _usIndex_| ) |  const  
---|---|---|---|---|---  
  
## ◆ scaleAngle()

void Rotation::scaleAngle  | ( | const double  | _scaleFactor_| ) |   
---|---|---|---|---|---  
  
References
[getValue()](../../d4/d18/classBase_1_1Rotation.html#a995899d98b886215e24758cb6da029dd),
and
[setValue()](../../d4/d18/classBase_1_1Rotation.html#a1219586eb3bf57070cc0ae34392d114f).

## ◆ setEulerAngles()

void Rotation::setEulerAngles  | ( | [EulerSequence](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678e) | _seq_ ,   
---|---|---|---  
|  | double  | _alpha_ ,   
|  | double  | _beta_ ,   
|  | double  | _gamma_  
| ) | |   
  
References
[EulerSequenceLast](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ea731cd34425700647c06b5aa25d343888),
and
[Invalid](../../d4/d18/classBase_1_1Rotation.html#a66b2c1d786883f041d7cf6d82d8b678ead7113376f16c44e537617a61a852aa14).

## ◆ setValue() [1/5]

void Rotation::setValue  | ( | const double  | _q0_ ,   
---|---|---|---  
|  | const double  | _q1_ ,   
|  | const double  | _q2_ ,   
|  | const double  | _q3_  
| ) | |   
  
Referenced by
[operator*=()](../../d4/d18/classBase_1_1Rotation.html#a6a65332d4581fb8be3a84aa152790a0e),
[Rotation()](../../d4/d18/classBase_1_1Rotation.html#a6ded479672faa2dea5197741d8233e70),
[scaleAngle()](../../d4/d18/classBase_1_1Rotation.html#acd28bd5bf84be383248a4deaa5be8387),
[Gui::PropertyEditor::RotationHelper::setAngle()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#a513883344181063d90dbd754039d33d3),
[Gui::PropertyEditor::RotationHelper::setAxis()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#a3b49948e5ac8d72ce290c36b98f94bc3),
[App::PropertyRotation::setPyObject()](../../df/d76/classApp_1_1PropertyRotation.html#a636fa584705a1852eeab7e32e09f0846),
[setValue()](../../d4/d18/classBase_1_1Rotation.html#a30632b9d88a9a7ac0886568842791397),
and
[setYawPitchRoll()](../../d4/d18/classBase_1_1Rotation.html#a077074c2a926f0b51dd2a384d1a48b11).

## ◆ setValue() [2/5]

void Rotation::setValue  | ( | const double  | _q_[4]| ) |   
---|---|---|---|---|---  
  
## ◆ setValue() [3/5]

void Rotation::setValue  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _matrix_| ) |   
---|---|---|---|---|---  
  
## ◆ setValue() [4/5]

void Rotation::setValue  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _axis_ ,   
---|---|---|---  
|  | const double  | _fAngle_  
| ) | |   
  
References [Base::Vector3< _Precision
>::Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[draftfunctions.scale::scale()](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ setValue() [5/5]

void Rotation::setValue  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rotateFrom_ ,   
---|---|---|---  
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rotateTo_  
| ) | |   
  
References [Base::Vector3< double
>::epsilon()](../../d1/d13/classBase_1_1Vector3.html#afc0aba7a73e8528bb4a5ffa9d7c1429a),
[Base::Vector3< _Precision
>::Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[setValue()](../../d4/d18/classBase_1_1Rotation.html#a1219586eb3bf57070cc0ae34392d114f),
and [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c).

## ◆ setYawPitchRoll()

void Rotation::setYawPitchRoll  | ( | double  | _y_ ,   
---|---|---|---  
|  | double  | _p_ ,   
|  | double  | _r_  
| ) | |   
  
Euler angles in yaw,pitch,roll notation.

References
[setValue()](../../d4/d18/classBase_1_1Rotation.html#a1219586eb3bf57070cc0ae34392d114f).

Referenced by
[Path::Command::getPlacement()](../../d7/d2e/classPath_1_1Command.html#a24d8f7cbd0c7a627ae60673e6b8faddf),
and
[Path::yawPitchRoll()](../../d2/df0/namespacePath.html#a8dc2ca5333672d7abee2d90ac47d0a9c).

## ◆ slerp()

| [Rotation](../../d4/d18/classBase_1_1Rotation.html) Rotation::slerp  | ( | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _rot0_ ,   
---|---|---|---  
|  | const [Rotation](../../d4/d18/classBase_1_1Rotation.html) & | _rot1_ ,   
|  | double  | _t_  
| ) | |   
static  
  
Specialty constructors.

References [Base::Vector3< double
>::epsilon()](../../d1/d13/classBase_1_1Vector3.html#afc0aba7a73e8528bb4a5ffa9d7c1429a),
[DraftVecUtils::neg()](../../dc/dc3/group__DRAFTVECUTILS.html#gadc85e420d51ac389c376dadd8b68e558),
and
[Rotation()](../../d4/d18/classBase_1_1Rotation.html#a13ea1d345ca0a92c0f09b4de544ca460).

Referenced by
[Base::Placement::slerp()](../../d1/d10/classBase_1_1Placement.html#a62fed3e2fa2d1a68e5d57bc4b89103f9).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Rotation.h
  * FreeCAD/src/Base/Rotation.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

