---
url: https://freecad.github.io/SourceDoc/d1/d13/classBase_1_1Vector3.html
scraped_at: 2025-09-08T15:18:10.474558
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Vector3](../../d1/d13/classBase_1_1Vector3.html)

[List of all members](../../df/d9d/classBase_1_1Vector3-members.html) | Public Types | Static Public Member Functions

Base::Vector3< _Precision > Class Template Reference

The Vector [Base](../../db/d07/namespaceBase.html "Basic structures used by
other FreeCAD components \(C++ API\)") class.
[More...](../../d1/d13/classBase_1_1Vector3.html#details)

`#include <Vector3D.h>`

##  Public Types  
  
---  
typedef _Precision | [num_type](../../d1/d13/classBase_1_1Vector3.html#ab23069c2eb082ae67c52b3ab8ccd8984)  
typedef [float_traits](../../d5/d79/structBase_1_1float__traits.html)< [num_type](../../d1/d13/classBase_1_1Vector3.html#ab23069c2eb082ae67c52b3ab8ccd8984) > | [traits_type](../../d1/d13/classBase_1_1Vector3.html#af76001acd4faf29569385651ad8b6a27)  
  
##  Public Member Functions  
  
---  
Operator  
_Precision & | [operator[]](../../d1/d13/classBase_1_1Vector3.html#aa0273fe0e0b45e6b6a45eb607314d901) (unsigned short usIndex)  
| Returns a reference to a coordinate. _usIndex_ must be in the range [0,2].
[More...](../../d1/d13/classBase_1_1Vector3.html#aa0273fe0e0b45e6b6a45eb607314d901)  
  
const _Precision & | [operator[]](../../d1/d13/classBase_1_1Vector3.html#a679eb2892b7958003466c28dfb8c3087) (unsigned short usIndex) const  
| Returns a const reference to a coordinate. _usIndex_ must be in the range
[0,2].
[More...](../../d1/d13/classBase_1_1Vector3.html#a679eb2892b7958003466c28dfb8c3087)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) | [operator+](../../d1/d13/classBase_1_1Vector3.html#a217bd5ebf8797d0930fda829c3f1698f) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct) const  
| Vector addition.
[More...](../../d1/d13/classBase_1_1Vector3.html#a217bd5ebf8797d0930fda829c3f1698f)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) | [operator&](../../d1/d13/classBase_1_1Vector3.html#ab377fb85d034e0486a08805cdf56b629) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct) const  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) | [operator-](../../d1/d13/classBase_1_1Vector3.html#ab8cca8856cabb105f7e2d002078776e4) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct) const  
| Vector subtraction.
[More...](../../d1/d13/classBase_1_1Vector3.html#ab8cca8856cabb105f7e2d002078776e4)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) | [operator-](../../d1/d13/classBase_1_1Vector3.html#a0f9c3919c099fc287a9818483e526cad) () const  
| Negative vector.
[More...](../../d1/d13/classBase_1_1Vector3.html#a0f9c3919c099fc287a9818483e526cad)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) & | [operator+=](../../d1/d13/classBase_1_1Vector3.html#a6ec2c033e94d0b2931852fe91aac2866) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct)  
| Vector summation.
[More...](../../d1/d13/classBase_1_1Vector3.html#a6ec2c033e94d0b2931852fe91aac2866)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) & | [operator-=](../../d1/d13/classBase_1_1Vector3.html#ad249de898d12e4086f677d5d89e53d7a) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct)  
| Vector subtraction.
[More...](../../d1/d13/classBase_1_1Vector3.html#ad249de898d12e4086f677d5d89e53d7a)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) | [operator*](../../d1/d13/classBase_1_1Vector3.html#a3cda7283e294083bffd0c64bdb87620e) (_Precision fScale) const  
| Vector scaling.
[More...](../../d1/d13/classBase_1_1Vector3.html#a3cda7283e294083bffd0c64bdb87620e)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) | [operator/](../../d1/d13/classBase_1_1Vector3.html#adf78c3473a035b21b3a191dd6a166b18) (_Precision fDiv) const  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) & | [operator*=](../../d1/d13/classBase_1_1Vector3.html#a13985f6a2cdc19b933708b35b0d152dc) (_Precision fScale)  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) & | [operator/=](../../d1/d13/classBase_1_1Vector3.html#abfbba0642da2bd7983fc1eeb7af21166) (_Precision fDiv)  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) & | [operator=](../../d1/d13/classBase_1_1Vector3.html#ace409e56d2a9f72e3ca4ad5a3650b20d) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &v)=default  
| Assignment.
[More...](../../d1/d13/classBase_1_1Vector3.html#ace409e56d2a9f72e3ca4ad5a3650b20d)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) & | [operator=](../../d1/d13/classBase_1_1Vector3.html#ae4640b8c9581ee48075baac0a2b6ee1c) ([Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &&v)=default  
_Precision | [operator*](../../d1/d13/classBase_1_1Vector3.html#a79a632a54013efd82381c3e2ec241406) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct) const  
| Scalar product.
[More...](../../d1/d13/classBase_1_1Vector3.html#a79a632a54013efd82381c3e2ec241406)  
  
_Precision | [Dot](../../d1/d13/classBase_1_1Vector3.html#a876a8620ec4213d4bc580190328ad899) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct) const  
| Scalar product.
[More...](../../d1/d13/classBase_1_1Vector3.html#a876a8620ec4213d4bc580190328ad899)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) | [operator%](../../d1/d13/classBase_1_1Vector3.html#a8e928c81f14ca74503e6fd435606cbde) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct) const  
| Cross product.
[More...](../../d1/d13/classBase_1_1Vector3.html#a8e928c81f14ca74503e6fd435606cbde)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) | [Cross](../../d1/d13/classBase_1_1Vector3.html#aeff630b92f5a52f5aa52dc87ccf77bac) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct) const  
| Cross product.
[More...](../../d1/d13/classBase_1_1Vector3.html#aeff630b92f5a52f5aa52dc87ccf77bac)  
  
[bool](../../d9/db9/classbool.html) | [operator!=](../../d1/d13/classBase_1_1Vector3.html#ab153ec115d58bcc4469098b4d41a0530) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct) const  
| Comparing for inequality.
[More...](../../d1/d13/classBase_1_1Vector3.html#ab153ec115d58bcc4469098b4d41a0530)  
  
[bool](../../d9/db9/classbool.html) | [operator==](../../d1/d13/classBase_1_1Vector3.html#a16ecb193ac37cef509936e00abdbc8c7) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct) const  
| Comparing for equality.
[More...](../../d1/d13/classBase_1_1Vector3.html#a16ecb193ac37cef509936e00abdbc8c7)  
  
[bool](../../d9/db9/classbool.html) | [IsOnLineSegment](../../d1/d13/classBase_1_1Vector3.html#a8de4e0c1d2d4deb2f29d1990804b201c) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &startVct, const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &endVct) const  
| Check if Vector is on a line segment.
[More...](../../d1/d13/classBase_1_1Vector3.html#a8de4e0c1d2d4deb2f29d1990804b201c)  
  
Modification  
void | [ScaleX](../../d1/d13/classBase_1_1Vector3.html#afad58caaa323cc2861b528c3a849a281) (_Precision f)  
void | [ScaleY](../../d1/d13/classBase_1_1Vector3.html#a73cfd02ba9dd66328247027d8f229529) (_Precision f)  
void | [ScaleZ](../../d1/d13/classBase_1_1Vector3.html#a2e2101e54b78b755304932ce7d29a43c) (_Precision f)  
void | [Scale](../../d1/d13/classBase_1_1Vector3.html#aff9627b9ca6eb620fbfe189e83aab8d5) (_Precision fX, _Precision fY, _Precision fZ)  
void | [MoveX](../../d1/d13/classBase_1_1Vector3.html#a0743f21653140bae73d5a02f786ba497) (_Precision f)  
void | [MoveY](../../d1/d13/classBase_1_1Vector3.html#adbff6c2cbe71a02233d869f458ba1b2a) (_Precision f)  
void | [MoveZ](../../d1/d13/classBase_1_1Vector3.html#a925ea62fbf073a719e066a404ad619b6) (_Precision f)  
void | [Move](../../d1/d13/classBase_1_1Vector3.html#a3326387f7f7eed1d69691ef721f3285a) (_Precision fX, _Precision fY, _Precision fZ)  
void | [RotateX](../../d1/d13/classBase_1_1Vector3.html#ae4b74aa1b2b0b0b8a3919f337dd680f6) (_Precision f)  
void | [RotateY](../../d1/d13/classBase_1_1Vector3.html#a35cf612a380c8d5dddeaa0730f44023c) (_Precision f)  
void | [RotateZ](../../d1/d13/classBase_1_1Vector3.html#af09471673c2fde5a6ef612c1e7f8b9b1) (_Precision f)  
void | [Set](../../d1/d13/classBase_1_1Vector3.html#a961b4f52c806809737f1d6fe18c8f9f6) (_Precision fX, _Precision fY, _Precision fZ)  
Mathematics  
_Precision | [Length](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a) () const  
| Length of the vector.
[More...](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a)  
  
_Precision | [Sqr](../../d1/d13/classBase_1_1Vector3.html#a80a17d5af270b4bbb5b85c9ca9caa1e8) () const  
| Squared length of the vector.
[More...](../../d1/d13/classBase_1_1Vector3.html#a80a17d5af270b4bbb5b85c9ca9caa1e8)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) & | [Normalize](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983) ()  
| Set length to 1.
[More...](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983)  
  
[bool](../../d9/db9/classbool.html) | [IsNull](../../d1/d13/classBase_1_1Vector3.html#ad3a0b14de1044acaac09ef5ef3418c4d) () const  
| Checks whether this is the null vector.
[More...](../../d1/d13/classBase_1_1Vector3.html#ad3a0b14de1044acaac09ef5ef3418c4d)  
  
_Precision | [GetAngle](../../d1/d13/classBase_1_1Vector3.html#aa7649aaf126c62148c8ebc54ad38ce27) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rcVect) const  
| Get angle between both vectors. The returned value lies in the interval
[0,pi].
[More...](../../d1/d13/classBase_1_1Vector3.html#aa7649aaf126c62148c8ebc54ad38ce27)  
  
void | [TransformToCoordinateSystem](../../d1/d13/classBase_1_1Vector3.html#a5369dfa0fb3929e42263f871a865324b) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclBase, const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclDirX, const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclDirY)  
| Transforms this point to the coordinate system defined by origin _rclBase_ ,
vector _vector_ rclDirX and vector _vector_ rclDirY.
[More...](../../d1/d13/classBase_1_1Vector3.html#a5369dfa0fb3929e42263f871a865324b)  
  
[bool](../../d9/db9/classbool.html) | [IsEqual](../../d1/d13/classBase_1_1Vector3.html#a37b0a33f0f163d93ead38519e3435a2b) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclPnt, _Precision tol) const  
| IsEqual.
[More...](../../d1/d13/classBase_1_1Vector3.html#a37b0a33f0f163d93ead38519e3435a2b)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) & | [ProjectToPlane](../../d1/d13/classBase_1_1Vector3.html#a24f91e91499245ab4282c6d0d0b7630c) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclBase, const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclNorm)  
| Projects this point onto the plane given by the base _rclBase_ and the
normal _rclNorm_.
[More...](../../d1/d13/classBase_1_1Vector3.html#a24f91e91499245ab4282c6d0d0b7630c)  
  
void | [ProjectToPlane](../../d1/d13/classBase_1_1Vector3.html#abd979792bf08f7c21ec230e7c0ffedc6) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclBase, const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclNorm, [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclProj) const  
| Projects this point onto the plane given by the base _rclBase_ and the
normal _rclNorm_ and stores the result in rclProj.
[More...](../../d1/d13/classBase_1_1Vector3.html#abd979792bf08f7c21ec230e7c0ffedc6)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) & | [ProjectToLine](../../d1/d13/classBase_1_1Vector3.html#afa7f4034959748405a9a53ae6e70dece) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclPoint, const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclLine)  
| Projects this point onto the line given by the base _rclPoint_ and the
direction _rclLine_.
[More...](../../d1/d13/classBase_1_1Vector3.html#afa7f4034959748405a9a53ae6e70dece)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) | [Perpendicular](../../d1/d13/classBase_1_1Vector3.html#ae16459f989f0d697a653b15126ac8e27) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclBase, const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclDir) const  
| Get the perpendicular of this point to the line defined by rclBase and
rclDir.
[More...](../../d1/d13/classBase_1_1Vector3.html#ae16459f989f0d697a653b15126ac8e27)  
  
_Precision | [DistanceToPlane](../../d1/d13/classBase_1_1Vector3.html#a252248a347173c84aff1b0872599fc79) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclBase, const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclNorm) const  
| Computes the distance to the given plane.
[More...](../../d1/d13/classBase_1_1Vector3.html#a252248a347173c84aff1b0872599fc79)  
  
_Precision | [DistanceToLine](../../d1/d13/classBase_1_1Vector3.html#af38176c3192c969e1ae2255a84885b8a) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclBase, const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclDirect) const  
| Computes the distance from this point to the line given by _rclBase_ and
_rclDirect_.
[More...](../../d1/d13/classBase_1_1Vector3.html#af38176c3192c969e1ae2255a84885b8a)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html) | [DistanceToLineSegment](../../d1/d13/classBase_1_1Vector3.html#afded3c26fdac4b7b199bcb0cc61d464f) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclP1, const [Vector3](../../d1/d13/classBase_1_1Vector3.html) &rclP2) const  
| Computes the vector from this point to the point on the line segment with
the shortest distance.
[More...](../../d1/d13/classBase_1_1Vector3.html#afded3c26fdac4b7b199bcb0cc61d464f)  
  
  
##  Static Public Member Functions  
  
---  
static [num_type](../../d1/d13/classBase_1_1Vector3.html#ab23069c2eb082ae67c52b3ab8ccd8984) | [epsilon](../../d1/d13/classBase_1_1Vector3.html#afc0aba7a73e8528bb4a5ffa9d7c1429a) ()  
  
## Public data members  
  
---  
_Precision | [x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c)  
| x-coordinate
[More...](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c)  
  
_Precision | [y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6)  
| y-coordinate
[More...](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6)  
  
_Precision | [z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da)  
| z-coordinate
[More...](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da)  
  
|
[Vector3](../../d1/d13/classBase_1_1Vector3.html#a414939927415f07357f8ce4b1f53ab09)
(_Precision fx=0.0, _Precision fy=0.0, _Precision fz=0.0)  
| Construction.
[More...](../../d1/d13/classBase_1_1Vector3.html#a414939927415f07357f8ce4b1f53ab09)  
  
|
[Vector3](../../d1/d13/classBase_1_1Vector3.html#a49b048a558dbbe849c53d1672ae7e9e0)
(const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision >
&v)=default  
|
[Vector3](../../d1/d13/classBase_1_1Vector3.html#ae3a963c343f729d2552d136cfd5ef618)
([Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &&v)=default  
|
[~Vector3](../../d1/d13/classBase_1_1Vector3.html#a0317caa234d05ff3c41517673eb0c5a9)
()=default  
  
## Detailed Description

template<class _Precision>  
class Base::Vector3< _Precision >

The Vector [Base](../../db/d07/namespaceBase.html "Basic structures used by
other FreeCAD components \(C++ API\)") class.

## Member Typedef Documentation

## ◆ num_type

template<class _Precision >

typedef _Precision [Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)<
_Precision >::num_type  
---  
  
## ◆ traits_type

template<class _Precision >

typedef
[float_traits](../../d5/d79/structBase_1_1float__traits.html)<[num_type](../../d1/d13/classBase_1_1Vector3.html#ab23069c2eb082ae67c52b3ab8ccd8984)>
[Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision
>::traits_type  
---  
  
## Constructor & Destructor Documentation

## ◆ Vector3() [1/3]

template<class _Precision >

| Vector3::Vector3  | ( | _Precision  | _fx_ = `0.0`,   
---|---|---|---  
|  | _Precision  | _fy_ = `0.0`,   
|  | _Precision  | _fz_ = `0.0`  
| ) | |   
explicit  
  
Construction.

## ◆ Vector3() [2/3]

template<class _Precision >

| [Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision >::Vector3  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _v_| ) |   
---|---|---|---|---|---  
default  
  
## ◆ Vector3() [3/3]

template<class _Precision >

| [Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision >::Vector3  | ( | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > && | _v_| ) |   
---|---|---|---|---|---  
default  
  
## ◆ ~Vector3()

template<class _Precision >

| [Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision >::~[Vector3](../../d1/d13/classBase_1_1Vector3.html) | ( | | ) |   
---|---|---|---|---  
default  
  
## Member Function Documentation

## ◆ Cross()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > Vector3::Cross  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |  const  
---|---|---|---|---|---  
  
Cross product.

Referenced by
[Gui::PropertyEditor::RotationHelper::assignProperty()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#ac33aed562242424b692098b02ff8e956),
[MeshCore::MeshGeomEdge::ClosestPointsToLine()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a4379babae85cf28f2c826f2bafa2efb6),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[MeshPart::MeshProjection::findIntersection()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#af4823ea9dee9ce1891f3a480adc4b406),
[PartDesign::Helix::generateHelixPath()](../../d3/d78/classPartDesign_1_1Helix.html#a04dd9590e1c0afe9dd3f1066ab9f0395),
[TechDrawGui::DrawGuiUtil::get3DDirAndRot()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a6c011651124bc645ff71d71e7bd64f4d),
[TechDrawGui::DrawGuiUtil::getProjDirFromFace()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a1e16c708a7e2a33bd36999a5f02ae63b),
[TechDraw::DrawProjGroupItem::getRotateAngle()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a7089aa4623e73d602fe97394d22ac6de),
[TechDraw::getViewAxis()](../../d7/d31/namespaceTechDraw.html#ad612c2d90cb50e87312099ea9824c509),
[MeshCore::MeshGeomEdge::IntersectWithEdge()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a7717df3b7ef781e44ea6300d0acd53cd),
[MeshCore::MeshGeomEdge::IntersectWithLine()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a08f395e6ba3e8cacf8966ab51bba7076),
[MeshCore::MeshGeomEdge::IsCollinear()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a5b4b087a68a83d8cd8bd00e6d5466409),
[MeshCore::MeshGeomEdge::IsParallel()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#ade011f1447569c2bdb83b217ee961bd8),
[Part::Geom2dConic::isReversed()](../../d8/d0d/classPart_1_1Geom2dConic.html#aec5c8932c68cc202319386c05d360e0e),
[Part::Geom2dArcOfConic::isReversed()](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html#ac8038187938c29d508ec52019b36f556),
[TechDraw::legacyViewAxis1()](../../d7/d31/namespaceTechDraw.html#a6c5c5a402ebdc68e1048cb62d6ef595f),
[Base::Rotation::makeRotationByAxes()](../../d4/d18/classBase_1_1Rotation.html#a0b7c436d3243f3703959c7f6be8ecad2),
[PartDesign::Helix::safePitch()](../../d3/d78/classPartDesign_1_1Helix.html#a85474d1c32f51cf49c0be48c600993eb),
and
[TechDraw::DrawViewSection::sectionLineEnds()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a4f8580c4dea1570bca8520f11f871ebe).

## ◆ DistanceToLine()

template<class _Precision >

_Precision Vector3::DistanceToLine  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclDirect_  
| ) | |  const  
  
Computes the distance from this point to the line given by _rclBase_ and
_rclDirect_.

References [Base::Vector3< _Precision
>::Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a).

Referenced by
[MeshCoreFit::CylinderFit::ComputeApproximationsLine()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a7d87a1da7a9df75c24cdfc3620ce203f),
[MeshCore::CylinderFit::GetDistanceToCylinder()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a7e37395d2a64271694828d763d1582d4),
[MeshCoreFit::CylinderFit::GetDistanceToCylinder()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a7e37395d2a64271694828d763d1582d4),
[MeshCore::CylinderSurfaceFit::GetDistanceToSurface()](../../d1/d68/classMeshCore_1_1CylinderSurfaceFit.html#ab17cc09afa4390ea5b1fa631b6f33e30),
[MeshCore::MeshGeomFacet::IsPointOf()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0769f90328838e1a97e124a8df91c778),
[MeshCore::CylinderFit::ProjectToCylinder()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a71ab1ef852631efc2d6dc9541e071762),
[MeshCoreFit::CylinderFit::ProjectToCylinder()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a71ab1ef852631efc2d6dc9541e071762),
and
[MeshCoreFit::CylinderFit::SetApproximations()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a99a0bb1d84330b261b7199c1e4767ba9).

## ◆ DistanceToLineSegment()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > Vector3::DistanceToLineSegment  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclP1_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclP2_  
| ) | |  const  
  
Computes the vector from this point to the point on the line segment with the
shortest distance.

The line segment is defined by _rclP1_ and _rclP2_. Note: If the projection of
this point is outside the segment then the shortest distance to _rclP1_ or
_rclP2_ is computed.

References
[DraftVecUtils::dist()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2af953a65bfefb422584aa67c55dbc39),
and
[Base::DistanceP2()](../../db/d07/namespaceBase.html#a535d5c7d1718605bad594f3fc89605b9).

Referenced by
[CDxfWrite::writeLinearDimBlock()](../../d6/d47/classCDxfWrite.html#aa531fff948f77be09ef66f004bcc9e35).

## ◆ DistanceToPlane()

template<class _Precision >

_Precision Vector3::DistanceToPlane  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclNorm_  
| ) | |  const  
  
Computes the distance to the given plane.

Depending on the side this point is located the distance can also be negative.
The distance is positive if the point is at the same side the plane normal
points to, negative otherwise.

References [Base::Vector3< _Precision
>::Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a).

Referenced by
[MeshCore::MeshProjection::bboxInsideRectangle()](../../d8/d39/classMeshCore_1_1MeshProjection.html#a539d9b10cf1f5f07d00b366af8789f51),
[MeshCore::MeshGeomFacet::DistancePlaneToPoint()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a79551be230dbe3c5ff3b0c55899292ac),
[Mesh::SegmentByMesh::execute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#a0fd4604225620a5902f526c867f0a7ed),
[MeshCore::PlaneSurfaceFit::GetDistanceToSurface()](../../d9/df5/classMeshCore_1_1PlaneSurfaceFit.html#ab6d11998b5092b31be4b3894e0c294cd),
[MeshCore::MeshAlgorithm::GetFacetsFromPlane()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a1de62d26b8126163d7359d905c8186c5),
and
[MeshCore::MeshGeomEdge::IntersectWithLine()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a08f395e6ba3e8cacf8966ab51bba7076).

## ◆ Dot()

template<class _Precision >

_Precision Vector3::Dot  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |  const  
---|---|---|---|---|---  
  
Scalar product.

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[Gui::PropertyEditor::RotationHelper::assignProperty()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#ac33aed562242424b692098b02ff8e956),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[MeshPart::MeshProjection::findIntersection()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#af4823ea9dee9ce1891f3a480adc4b406),
[MeshCore::MeshFixCaps::Fixup()](../../dd/ddb/classMeshCore_1_1MeshFixCaps.html#ad50f1421a63196cbd099763be5ce1863),
[TechDraw::DrawProjGroupItem::getViewAxis()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a66cab4b4ebd52d41889c7fdb9c854821),
[MeshCore::MeshGeomEdge::IntersectWithEdge()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a7717df3b7ef781e44ea6300d0acd53cd),
[MeshCore::MeshGeomEdge::IntersectWithPlane()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a7a1f5982b3db3d2ce96f8ce80a476df8),
[MeshCore::TriangulationVerifier::MustFlip()](../../df/d1a/classMeshCore_1_1TriangulationVerifier.html#a09e8d80edd0e3956013d8a986a076751),
[MeshCore::TriangulationVerifierV2::MustFlip()](../../db/d03/classMeshCore_1_1TriangulationVerifierV2.html#a33700cb7e43c969de82c7d8c48e523a9),
and
[MeshCore::CylinderSurfaceFit::TestTriangle()](../../d1/d68/classMeshCore_1_1CylinderSurfaceFit.html#a0609b3fc11a2b0f290927d0c7c816a50).

## ◆ epsilon()

template<class _Precision >

| static [num_type](../../d1/d13/classBase_1_1Vector3.html#ab23069c2eb082ae67c52b3ab8ccd8984) [Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision >::epsilon  | ( | | ) |   
---|---|---|---|---  
static  
  
References
[draftutils.utils::epsilon()](../../de/d75/group__draftutils.html#ga7ca4044874669855d2291d7990debb22).

## ◆ GetAngle()

template<class _Precision >

_Precision Vector3::GetAngle  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVect_| ) |  const  
---|---|---|---|---|---  
  
Get angle between both vectors. The returned value lies in the interval
[0,pi].

References
[draftutils.utils::epsilon()](../../de/d75/group__draftutils.html#ga7ca4044874669855d2291d7990debb22),
and [Base::Vector3< _Precision
>::Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a).

Referenced by
[Base::Builder3D::addSingleArrow()](../../d6/d1b/classBase_1_1Builder3D.html#a000b4d9d1342d22dcb7c0ded96ad45b2),
[Base::InventorBuilder::addSingleArrow()](../../db/d7f/classBase_1_1InventorBuilder.html#a075ebfc1e2f098e0e0bcf104b3cbb916),
[TechDraw::DrawUtil::closestBasis()](../../da/d23/classTechDraw_1_1DrawUtil.html#a601e0012496ae9d9175f0131511d04da),
[MeshCore::MeshGeomEdge::ClosestPointsToLine()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a4379babae85cf28f2c826f2bafa2efb6),
[MeshCore::MeshGeomFacet::Enlarge()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a545696343f9e3a0250a7e98aa23f8e1f),
[TechDrawGui::QGIViewDimension::findIsoDir()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#adedbcfede3c86dacfd6f4574356eff2c),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[MeshCore::MeshGeomFacet::Foraminate()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#af88e493312dfae6ada18ff9ff839371d),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[TechDraw::DrawProjGroupItem::getRotateAngle()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a7089aa4623e73d602fe97394d22ac6de),
[MeshCore::MeshGeomEdge::IntersectWithLine()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a08f395e6ba3e8cacf8966ab51bba7076),
[MeshCore::MeshGeomFacet::MaximumAngle()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#ae41897c55bfafb48c5c10d49cd092f46),
[MeshCore::MeshGeomFacet::MinimumAngle()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0da2b4fe70fac25cbdc8958847f5d41f),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[MeshCore::MeshTopoAlgorithm::ShouldSwapEdge()](../../d6/d22/classMeshCore_1_1MeshTopoAlgorithm.html#a9d59e41e4d771b9907eab6f959256985),
[MeshCore::MeshGeomFacet::SubSample()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a240bb53b26cc8f8d48ccc0df32f886b8),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintForce::updateData()](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#ad691cf23756106d6b0ea043ddebd1b94),
and
[CDxfWrite::writeLinearDimBlock()](../../d6/d47/classCDxfWrite.html#aa531fff948f77be09ef66f004bcc9e35).

## ◆ IsEqual()

template<class _Precision >

[bool](../../d9/db9/classbool.html) Vector3::IsEqual  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclPnt_ ,   
---|---|---|---  
|  | _Precision  | _tol_  
| ) | |  const  
  
IsEqual.

Parameters

     rclPnt|   
---|---  
tol|  
  
Returns

    true or false If the distance to point _rclPnt_ is within the tolerance _tol_ both points are considered equal. 

References
[Base::Distance()](../../db/d07/namespaceBase.html#a04166a79d8f2c2f3cb0d5747ef0154f9).

Referenced by
[TechDraw::BSpline::asCircle()](../../d6/d09/classTechDraw_1_1BSpline.html#a2c628716c3a1e784abbe9f399786386f),
[TechDraw::DrawUtil::boxIntersect2d()](../../da/d23/classTechDraw_1_1DrawUtil.html#a394f9eed54ca909914560d4a3bfc09d3),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDrawGui::QGIViewDimension::findIsoExt()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a3888081268b10065d4854b4fee7b69c0),
[TechDraw::getViewAxis()](../../d7/d31/namespaceTechDraw.html#ad612c2d90cb50e87312099ea9824c509),
[TechDraw::legacyViewAxis1()](../../d7/d31/namespaceTechDraw.html#a6c5c5a402ebdc68e1048cb62d6ef595f),
[TechDrawGui::QGIFace::lineSetToFillItems()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#af53e0be46e34bf69b446f1f9bd03e259),
and
[TechDraw::CenterLine::scaledGeometry()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a104bfe6bf49d7b364f65000352e670ea).

## ◆ IsNull()

template<class _Precision >

[bool](../../d9/db9/classbool.html) Vector3::IsNull  
---  
  
Checks whether this is the null vector.

Referenced by
[MeshCore::MeshGeomEdge::IntersectWithEdge()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a7717df3b7ef781e44ea6300d0acd53cd),
[MeshCore::MeshGeomEdge::IsCollinear()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a5b4b087a68a83d8cd8bd00e6d5466409),
and
[MeshCore::MeshGeomEdge::IsParallel()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#ade011f1447569c2bdb83b217ee961bd8).

## ◆ IsOnLineSegment()

template<class _Precision >

[bool](../../d9/db9/classbool.html) Vector3::IsOnLineSegment  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _startVct_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _endVct_  
| ) | |  const  
  
Check if Vector is on a line segment.

## ◆ Length()

template<class _Precision >

_Precision Vector3::Length  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Length of the vector.

Referenced by
[CmdSketcherConstrainDistance::activated()](../../d4/de5/classCmdSketcherConstrainDistance.html#a24031613fd513a79165dfec1d75d6ecb),
[CmdSketcherConstrainAngle::activated()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a0d48a74c0960a5a240c1a39137f070a3),
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[Sketcher::SketchObject::addCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#a2ae92a618d60a264ed20d7a359b89f98),
[CmdSketcherConstrainDistance::applyConstraint()](../../d4/de5/classCmdSketcherConstrainDistance.html#a9c0f733b397d4f7e05af5f7c70f9debb),
[CmdSketcherConstrainAngle::applyConstraint()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a5602881a59f6c0a0a83a30641560aeb7),
[TechDraw::CenterLine::calcEndPoints2Points()](../../d5/dd5/classTechDraw_1_1CenterLine.html#aedb72634306a11f9eb49ffac16eb7e2b),
[TechDraw::DrawViewPart::checkXDirection()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a602f73fc08211bfc4edfa1382bc0ee64),
[Part::Extrusion::computeFinalParameters()](../../db/d6c/classPart_1_1Extrusion.html#a4b4ddc216eb6449e2b21480a430f5df8),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[Gui::LocationUi< Ui
>::directionActivated()](../../db/da1/classGui_1_1LocationUi.html#a2b6ad760230d84dfb3b22a565e1428cb),
[Gui::LocationImpUi< Ui
>::directionActivated()](../../df/d30/classGui_1_1LocationImpUi.html#aba736f8d2a7c54fde948d91c7bd87de2),
[Base::Vector3< _Precision
>::DistanceToLine()](../../d1/d13/classBase_1_1Vector3.html#af38176c3192c969e1ae2255a84885b8a),
[Base::Vector3< _Precision
>::DistanceToPlane()](../../d1/d13/classBase_1_1Vector3.html#a252248a347173c84aff1b0872599fc79),
[MeshCore::MeshEigensystem::Evaluate()](../../d1/dba/classMeshCore_1_1MeshEigensystem.html#a1ac0e9a86af25fa12c6e41d8780fd1bd),
[Mesh::SegmentByMesh::execute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#a0fd4604225620a5902f526c867f0a7ed),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[Sketcher::SketchObject::extend()](../../d9/dad/classSketcher_1_1SketchObject.html#a863df4c6af57263b15a8170b377ef466),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[Base::Vector3< _Precision
>::GetAngle()](../../d1/d13/classBase_1_1Vector3.html#aa7649aaf126c62148c8ebc54ad38ce27),
[MeshCore::QuadraticFit::GetCurvatureInfo()](../../d6/d9c/classMeshCore_1_1QuadraticFit.html#a41d6c4447ce530be7c38f0198ccc4798),
[MeshCore::SurfaceFit::GetCurvatureInfo()](../../d2/d9a/classMeshCore_1_1SurfaceFit.html#a728f78ff2b4ae3f86cdeeb1cfe4a228c),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[MeshCore::SphereFit::GetDistanceToSphere()](../../dc/dce/classMeshCore_1_1SphereFit.html#aca8b41099e947b212fee4dd15118fb69),
[MeshCoreFit::SphereFit::GetDistanceToSphere()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#aca8b41099e947b212fee4dd15118fb69),
[Reen::ParameterCorrection::GetGravityPoint()](../../dd/d71/classReen_1_1ParameterCorrection.html#aad7e692a566723170384956722dae228),
[ArchPanel.CommandPanel::getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[Robot::Trajectory::getVelocity()](../../d7/d14/classRobot_1_1Trajectory.html#a5f2eaa83ffa90506b54e685d8e3fd7b8),
[TechDraw::DrawViewPart::getXDirection()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a0e16d51e16c7c55b75f5cfa00c037fd0),
[TechDraw::DrawProjGroupItem::getXDirection()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a86b744ee5d2b7ff5de819b0f23488498),
[TechDraw::DrawViewSection::getXDirection()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a0cefd62711bac9ca360a2ffc37731820),
[Base::BoundBox3< _Precision
>::IsCutLine()](../../d8/d12/classBase_1_1BoundBox3.html#a55a718fe21f7a5240ac7b6651b4c5822),
[MeshCore::MeshAlgorithm::IsVertexVisible()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a28a3aedc6a3accf35a922860cf7be3b5),
[Base::Rotation::makeRotationByAxes()](../../d4/d18/classBase_1_1Rotation.html#a0b7c436d3243f3703959c7f6be8ecad2),
[Mesh::MeshObject::offsetSpecial2()](../../d8/dcc/classMesh_1_1MeshObject.html#a2be16c1ce13a5f5eecb318c442d64b20),
[MeshPart::MeshAlgos::offsetSpecial2()](../../db/d67/classMeshPart_1_1MeshAlgos.html#a9fd929c87723fd546563717fac248d11),
[Fem::ConstraintFluidBoundary::onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Fem::ConstraintForce::onChanged()](../../d6/d63/classFem_1_1ConstraintForce.html#aa19098735f62c480439948314f6532b3),
[Fem::ConstraintGear::onChanged()](../../d8/d55/classFem_1_1ConstraintGear.html#a971506b4ca246c3378e2755160ed4772),
[TechDraw::DrawViewPart::onChanged()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a6a340bbf67a96de757e412b21d7a5491),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[PartDesign::Helix::safePitch()](../../d3/d78/classPartDesign_1_1Helix.html#a85474d1c32f51cf49c0be48c600993eb),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
[Gui::LocationWidget::setDirection()](../../d9/d9a/classGui_1_1LocationWidget.html#a2af475de798c64df6995f659a2e7ab40),
[Gui::LocationUi< Ui
>::setDirection()](../../db/da1/classGui_1_1LocationUi.html#a13961053ead815e1adb59564608b8b8a),
[Gui::LocationImpUi< Ui
>::setDirection()](../../df/d30/classGui_1_1LocationImpUi.html#a95f67606fb3dbaab6d199980cb091c63),
[ArchPanel.CommandPanel::setLength()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a324c9bdbfec0dd8eacfb7d0cea302998),
[Base::Rotation::setValue()](../../d4/d18/classBase_1_1Rotation.html#a62c0b4012cb383de60d0e4a225c39550),
[MeshCore::MeshTopoAlgorithm::SnapVertex()](../../d6/d22/classMeshCore_1_1MeshTopoAlgorithm.html#a7079336d5bcaff71462d64d096f52395),
[MeshCore::MeshGeomFacet::SubSample()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a240bb53b26cc8f8d48ccc0df32f886b8),
[ArchPanel.CommandPanel::update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c),
[PartDesign::Groove::updateAxis()](../../d7/de3/classPartDesign_1_1Groove.html#a064b27171c35a5be3b681e2856208747),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintForce::updateData()](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#ad691cf23756106d6b0ea043ddebd1b94),
and
[FemGui::ViewProviderFemConstraintGear::updateData()](../../d1/d2f/classFemGui_1_1ViewProviderFemConstraintGear.html#a56f097a322b6fe5b2b4b7eead3374c49).

## ◆ Move()

template<class _Precision >

void Vector3::Move  | ( | _Precision  | _fX_ ,   
---|---|---|---  
|  | _Precision  | _fY_ ,   
|  | _Precision  | _fZ_  
| ) | |   
  
Referenced by
[MeshCore::CylinderFit::ProjectToCylinder()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a71ab1ef852631efc2d6dc9541e071762),
and
[MeshCoreFit::CylinderFit::ProjectToCylinder()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a71ab1ef852631efc2d6dc9541e071762).

## ◆ MoveX()

template<class _Precision >

void Vector3::MoveX  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
## ◆ MoveY()

template<class _Precision >

void Vector3::MoveY  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
## ◆ MoveZ()

template<class _Precision >

void Vector3::MoveZ  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
## ◆ Normalize()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &
Vector3::Normalize  
---  
  
Set length to 1.

Referenced by
[Base::Builder3D::addSingleArrow()](../../d6/d1b/classBase_1_1Builder3D.html#a000b4d9d1342d22dcb7c0ded96ad45b2),
[Base::InventorBuilder::addSingleArrow()](../../db/d7f/classBase_1_1InventorBuilder.html#a075ebfc1e2f098e0e0bcf104b3cbb916),
[MeshCore::MeshTopoAlgorithm::AdjustEdgesToCurvatureDirection()](../../d6/d22/classMeshCore_1_1MeshTopoAlgorithm.html#a9d434d84a9f0707b8c6ca3b4c35a0c26),
[Sketcher::SketchAnalysis::analyseMissingPointOnPointCoincident()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a353f09f64b5882c26cc62b5560299383),
[MeshCore::MeshProjection::bboxInsideRectangle()](../../d8/d39/classMeshCore_1_1MeshProjection.html#a539d9b10cf1f5f07d00b366af8789f51),
[TechDraw::DrawUtil::boxIntersect2d()](../../da/d23/classTechDraw_1_1DrawUtil.html#a394f9eed54ca909914560d4a3bfc09d3),
[TechDraw::CenterLine::calcEndPoints()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a34df15a8a959516ecc49512c3ec5a73c),
[TechDraw::CenterLine::calcEndPoints2Lines()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a54d1cc5e3f8aa8923c2c28bdbe25c262),
[TechDraw::CenterLine::calcEndPoints2Points()](../../d5/dd5/classTechDraw_1_1CenterLine.html#aedb72634306a11f9eb49ffac16eb7e2b),
[TechDraw::CenterLine::calcEndPointsNoRef()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ac096a3e174023e9aa7efaab88e4df343),
[Gui::ManualAlignment::computeAlignment()](../../d7/d97/classGui_1_1ManualAlignment.html#aff085ba77f9c444b8aada36102b3879b),
[Fem::ConstraintGear::ConstraintGear()](../../d8/d55/classFem_1_1ConstraintGear.html#a6220bd8552266b853c13e32b8b44bebc),
[TechDrawGui::QGIFace::dashedPPath()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#ac893b16b4130c990b40e45750d31b9a9),
[TechDrawGui::QGIViewPart::drawSectionLine()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a513e571f325b7c7cac09bdec0d1c512d),
[MeshCore::MeshGeomFacet::Enlarge()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a545696343f9e3a0250a7e98aa23f8e1f),
[Sketcher::SketchObject::extend()](../../d9/dad/classSketcher_1_1SketchObject.html#a863df4c6af57263b15a8170b377ef466),
[MeshCoreFit::CylinderFit::findBestSolDirection()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a6e0db1db743acde2daf19bc60f9d1e0c),
[Part::findFilletCenter()](../../d2/db9/namespacePart.html#ab01c47ee6de2dab1626ab457c264b394),
[MeshCore::MeshFixCaps::Fixup()](../../dd/ddb/classMeshCore_1_1MeshFixCaps.html#ad50f1421a63196cbd099763be5ce1863),
[MeshCore::MeshFixDeformedFacets::Fixup()](../../d3/d69/classMeshCore_1_1MeshFixDeformedFacets.html#a950efccb37b356170c865013bdad4eed),
[MeshCore::MeshKernel::GetFacetNormals()](../../dd/d95/classMeshCore_1_1MeshKernel.html#a0156c0edaac84b69f5ea7e124067acec),
[MeshCore::MeshAlgorithm::GetFacetsFromPlane()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a1de62d26b8126163d7359d905c8186c5),
[MeshCore::CylinderFit::GetInitialAxisFromNormals()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a94896bef3d7356707b274d1d34c101f4),
[MeshCore::MeshKernel::GetNormal()](../../dd/d95/classMeshCore_1_1MeshKernel.html#a899aefed5ca507614d6d0dbfabac5ed0),
[MeshCore::MeshRefPointToFacets::GetNormal()](../../d2/d4a/classMeshCore_1_1MeshRefPointToFacets.html#a31a7d85aba27324cefc2f0b8b44d923f),
[MeshCore::MeshRefPointToPoints::GetNormal()](../../db/d62/classMeshCore_1_1MeshRefPointToPoints.html#a2479fc314f617bff56eabb9f55ca61cf),
[Mesh::MeshObject::getPointNormal()](../../d8/dcc/classMesh_1_1MeshObject.html#ab3953ee00afa96512b922acb9ea5ec12),
[Mesh::MeshObject::getPointNormals()](../../d8/dcc/classMesh_1_1MeshObject.html#a16c59852a6633307010cc619c4d10143),
[TechDraw::DrawProjGroupItem::getRotateAngle()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a7089aa4623e73d602fe97394d22ac6de),
[Base::Rotation::getValue()](../../d4/d18/classBase_1_1Rotation.html#af95c57a06636f68b2a6cc779dc042edd),
[TechDraw::getViewAxis()](../../d7/d31/namespaceTechDraw.html#ad612c2d90cb50e87312099ea9824c509),
[MeshCore::MeshGeomFacet::IsDeformed()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a70db8543c02dd6d94fa586a18cf73732),
[TechDraw::legacyViewAxis1()](../../d7/d31/namespaceTechDraw.html#a6c5c5a402ebdc68e1048cb62d6ef595f),
[MeshPart::MeshAlgos::LoftOnCurve()](../../db/d67/classMeshPart_1_1MeshAlgos.html#af6d0bd2cf1dd2ca04dfb7a7f853f2aba),
[TechDrawGui::QGISectionLine::makeArrowsISO()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#a8f2cce08f6be3eb56a19c7de258ea884),
[TechDrawGui::QGISectionLine::makeArrowsTrad()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#aaa7b66291c65ca1fd3de5a83aa2cdf68),
[TechDrawGui::QGIArrow::makeFilledTriangle()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#a48ea2d959065f7dcddd8bf7f60135e62),
[TechDrawGui::QGIArrow::makeForkArrow()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#af362a5208def60772252b3e36d1d2c9a),
[TechDrawGui::QGIArrow::makeHashMark()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#ad350c362524675d0e695781e60dd6945),
[TechDrawGui::QGIArrow::makeOpenArrow()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#a5846b0a5797ddeebbb25e95297088489),
[TechDrawGui::QGIArrow::makePyramid()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#aedbc5bfceac71c55af61aa6981121425),
[Base::Rotation::makeRotationByAxes()](../../d4/d18/classBase_1_1Rotation.html#a0b7c436d3243f3703959c7f6be8ecad2),
[MeshPart::CurveProjectorWithToolMesh::makeToolMesh()](../../d8/dd2/classMeshPart_1_1CurveProjectorWithToolMesh.html#aa0428e1cea062658a882b2b5e3b9e05b),
[Mesh::MeshObject::offsetSpecial()](../../d8/dcc/classMesh_1_1MeshObject.html#a79fce33947d4de9f9de6f883f1897688),
[MeshPart::MeshAlgos::offsetSpecial()](../../db/d67/classMeshPart_1_1MeshAlgos.html#ade65ddc063ac090bae47a7a6ef797f93),
[Mesh::MeshObject::offsetSpecial2()](../../d8/dcc/classMesh_1_1MeshObject.html#a2be16c1ce13a5f5eecb318c442d64b20),
[MeshPart::MeshAlgos::offsetSpecial2()](../../db/d67/classMeshPart_1_1MeshAlgos.html#a9fd929c87723fd546563717fac248d11),
[SketcherGui::EditModeConstraintCoinManager::processConstraints()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a86abd481aa8756c9ea61b10d2e624804),
[MeshCore::MeshProjection::projectLineOnMesh()](../../d8/d39/classMeshCore_1_1MeshProjection.html#a1f99083cc7cb9f5d97e820659acbbe71),
[Base::Matrix4D::rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aff3583443a5de61928925fa6b8af6f21),
[TechDraw::DrawViewSection::sectionLineEnds()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a4f8580c4dea1570bca8520f11f871ebe),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
[MeshCoreFit::CylinderFit::SetApproximations()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#adcb5e011cf434f5d8642690ffb9fc6bb),
[Base::CoordinateSystem::setAxes()](../../d1/d66/classBase_1_1CoordinateSystem.html#aa739d8948fc7bc060cd5fdbc22f90d93),
[TechDrawGui::QGISectionLine::setDirection()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#a098a37e50ee68ae3d65cf23b952e10a8),
[MeshCore::MeshGeomFacet::SetNormal()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a284eb15810eef8ba429a00f3d4673c48),
[Base::Rotation::setValue()](../../d4/d18/classBase_1_1Rotation.html#a62c0b4012cb383de60d0e4a225c39550),
[Base::CoordinateSystem::setXDirection()](../../d1/d66/classBase_1_1CoordinateSystem.html#a7f2a242ff6094d1743686222ed37192d),
[Base::CoordinateSystem::setYDirection()](../../d1/d66/classBase_1_1CoordinateSystem.html#ad0bcb826af0de6e8e256cae84dccbd26),
[MeshCore::PlaneFitSmoothing::Smooth()](../../d4/d74/classMeshCore_1_1PlaneFitSmoothing.html#a8c02774a72bb114362c993f51dc0d7ec),
[MeshCore::PlaneFitSmoothing::SmoothPoints()](../../d4/d74/classMeshCore_1_1PlaneFitSmoothing.html#aa6fba7b76ab58215430b86da7dec700d),
[MeshCore::MeshGeomFacet::SubSample()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a240bb53b26cc8f8d48ccc0df32f886b8),
[Part::suggestFilletRadius()](../../d2/db9/namespacePart.html#a1903069f8259f815f24930b78481a785),
[Base::Matrix4D::toAxisAngle()](../../d5/db4/classBase_1_1Matrix4D.html#aebaf3536031474ff723f0a4abd621e55),
[Base::Vector3< _Precision
>::TransformToCoordinateSystem()](../../d1/d13/classBase_1_1Vector3.html#a5369dfa0fb3929e42263f871a865324b),
[FemGui::ViewProviderFemPostPlaneFunction::updateData()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#a6ec898b1ee3b9ae2983c1f424b2a55f4),
[SketcherGui::DrawSketchHandlerLineSet::updateTransitionData()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a87c661c6611a6c685accb1c089fdeba8),
[CDxfWrite::writeAngularDimBlock()](../../d6/d47/classCDxfWrite.html#a4a915e13347bfc87d7b55859523ab4cd),
[CDxfWrite::writeDiametricDimBlock()](../../d6/d47/classCDxfWrite.html#a1099141d6c71739945175a349d98129c),
[CDxfWrite::writeLinearDimBlock()](../../d6/d47/classCDxfWrite.html#aa531fff948f77be09ef66f004bcc9e35),
and
[CDxfWrite::writeRadialDimBlock()](../../d6/d47/classCDxfWrite.html#aa7f3fe99f84d1fd3ece63a019ba76dc5).

## ◆ operator!=()

template<class _Precision >

[bool](../../d9/db9/classbool.html) Vector3::operator!=  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |  const  
---|---|---|---|---|---  
  
Comparing for inequality.

## ◆ operator%()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > Vector3::operator%  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |  const  
---|---|---|---|---|---  
  
Cross product.

## ◆ operator&()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > Vector3::operator& | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |  const  
---|---|---|---|---|---  
  
References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ operator*() [1/2]

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > Vector3::operator*  | ( | _Precision  | _fScale_| ) |  const  
---|---|---|---|---|---  
  
Vector scaling.

## ◆ operator*() [2/2]

template<class _Precision >

_Precision Vector3::operator*  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |  const  
---|---|---|---|---|---  
  
Scalar product.

## ◆ operator*=()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & Vector3::operator*=  | ( | _Precision  | _fScale_| ) |   
---|---|---|---|---|---  
  
## ◆ operator+()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > Vector3::operator+  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |  const  
---|---|---|---|---|---  
  
Vector addition.

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ operator+=()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & Vector3::operator+=  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |   
---|---|---|---|---|---  
  
Vector summation.

## ◆ operator-() [1/2]

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > Vector3::operator-  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Negative vector.

## ◆ operator-() [2/2]

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > Vector3::operator-  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |  const  
---|---|---|---|---|---  
  
Vector subtraction.

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ operator-=()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & Vector3::operator-=  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |   
---|---|---|---|---|---  
  
Vector subtraction.

## ◆ operator/()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > Vector3::operator/  | ( | _Precision  | _fDiv_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator/=()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & Vector3::operator/=  | ( | _Precision  | _fDiv_| ) |   
---|---|---|---|---|---  
  
## ◆ operator=() [1/2]

template<class _Precision >

| [Vector3](../../d1/d13/classBase_1_1Vector3.html) & [Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision >::operator=  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _v_| ) |   
---|---|---|---|---|---  
default  
  
Assignment.

## ◆ operator=() [2/2]

template<class _Precision >

| [Vector3](../../d1/d13/classBase_1_1Vector3.html) & [Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision >::operator=  | ( | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > && | _v_| ) |   
---|---|---|---|---|---  
default  
  
## ◆ operator==()

template<class _Precision >

[bool](../../d9/db9/classbool.html) Vector3::operator==  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |  const  
---|---|---|---|---|---  
  
Comparing for equality.

## ◆ operator[]() [1/2]

template<class _Precision >

_Precision & Vector3::operator[]  | ( | unsigned short  | _usIndex_| ) |   
---|---|---|---|---|---  
  
Returns a reference to a coordinate. _usIndex_ must be in the range [0,2].

## ◆ operator[]() [2/2]

template<class _Precision >

const _Precision & Vector3::operator[]  | ( | unsigned short  | _usIndex_| ) |  const  
---|---|---|---|---|---  
  
Returns a const reference to a coordinate. _usIndex_ must be in the range
[0,2].

## ◆ Perpendicular()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > Vector3::Perpendicular  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclDir_  
| ) | |  const  
  
Get the perpendicular of this point to the line defined by rclBase and rclDir.

Note: Do not mix up this method with ProjectToLine.

Referenced by
[Sketcher::SketchObject::addSymmetric()](../../d9/dad/classSketcher_1_1SketchObject.html#afcbb1d6f5a99e52a70fdf6d9d3c9d361),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[MeshCore::MeshFixCaps::Fixup()](../../dd/ddb/classMeshCore_1_1MeshFixCaps.html#ad50f1421a63196cbd099763be5ce1863),
[PartDesign::ProfileBased::getReversedAngle()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a3b3aa636b6181cd9edacd1f7b1412f0b),
and
[Sketcher::SketchObject::split()](../../d9/dad/classSketcher_1_1SketchObject.html#ab73e7a53a704168c004b9aa6c9ad7a68).

## ◆ ProjectToLine()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & Vector3::ProjectToLine  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclPoint_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclLine_  
| ) | |   
  
Projects this point onto the line given by the base _rclPoint_ and the
direction _rclLine_.

Projects a point _rclPoint_ onto the line defined by the origin and the
direction _rclLine_. The result is a vector from _rclPoint_ to the point on
the line. The length of this vector is the distance from _rclPoint_ to the
line. Note: The resulting vector does not depend on the current vector.

References [Base::Vector3< _Precision
>::Sqr()](../../d1/d13/classBase_1_1Vector3.html#a80a17d5af270b4bbb5b85c9ca9caa1e8).

Referenced by
[Part::createFilletGeometry()](../../d2/db9/namespacePart.html#a4e47966fd6c762b34824b98614b76541),
[MeshCore::MeshEigensystem::Evaluate()](../../d1/dba/classMeshCore_1_1MeshEigensystem.html#a1ac0e9a86af25fa12c6e41d8780fd1bd),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[Part::findFilletCenter()](../../d2/db9/namespacePart.html#ab01c47ee6de2dab1626ab457c264b394),
[MeshCore::MeshProjection::isPointInsideDistance()](../../d8/d39/classMeshCore_1_1MeshProjection.html#a1bc07b7339c80de0c54cc14bf844a3d2),
[SketcherGui::EditModeConstraintCoinManager::processConstraints()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a86abd481aa8756c9ea61b10d2e624804),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
and
[Part::suggestFilletRadius()](../../d2/db9/namespacePart.html#a1903069f8259f815f24930b78481a785).

## ◆ ProjectToPlane() [1/2]

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & Vector3::ProjectToPlane  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclNorm_  
| ) | |   
  
Projects this point onto the plane given by the base _rclBase_ and the normal
_rclNorm_.

References [Base::Vector3< _Precision
>::Sqr()](../../d1/d13/classBase_1_1Vector3.html#a80a17d5af270b4bbb5b85c9ca9caa1e8).

Referenced by [Base::BoundBox3< _Precision
>::ClosestPoint()](../../d8/d12/classBase_1_1BoundBox3.html#a9f500110c95df8ca0b5e71e371d64149),
[Reen::ParameterCorrection::ProjectControlPointsOnPlane()](../../dd/d71/classReen_1_1ParameterCorrection.html#a54d70272eced8a72c72f8c11a11ac568),
[MeshCore::MeshGeomFacet::ProjectPointToPlane()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#aff341b81cdf623850a468d7021cadee7),
[MeshCore::CylinderFit::ProjectToCylinder()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a71ab1ef852631efc2d6dc9541e071762),
[MeshCoreFit::CylinderFit::ProjectToCylinder()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a71ab1ef852631efc2d6dc9541e071762),
and
[PartGui::ViewProviderMirror::setEdit()](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a1f2db7361989a26090e6071227f1562a).

## ◆ ProjectToPlane() [2/2]

template<class _Precision >

void Vector3::ProjectToPlane  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclNorm_ ,   
|  | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclProj_  
| ) | |  const  
  
Projects this point onto the plane given by the base _rclBase_ and the normal
_rclNorm_ and stores the result in rclProj.

References [Base::Vector3< _Precision
>::Sqr()](../../d1/d13/classBase_1_1Vector3.html#a80a17d5af270b4bbb5b85c9ca9caa1e8).

## ◆ RotateX()

template<class _Precision >

void Vector3::RotateX  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
References [Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ RotateY()

template<class _Precision >

void Vector3::RotateY  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ RotateZ()

template<class _Precision >

void Vector3::RotateZ  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
and [Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6).

Referenced by
[SketcherGui::EditModeConstraintCoinManager::processConstraints()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a86abd481aa8756c9ea61b10d2e624804).

## ◆ Scale()

template<class _Precision >

void Vector3::Scale  | ( | _Precision  | _fX_ ,   
---|---|---|---  
|  | _Precision  | _fY_ ,   
|  | _Precision  | _fZ_  
| ) | |   
  
Referenced by
[Base::Builder3D::addSingleArrow()](../../d6/d1b/classBase_1_1Builder3D.html#a000b4d9d1342d22dcb7c0ded96ad45b2),
[Base::InventorBuilder::addSingleArrow()](../../db/d7f/classBase_1_1InventorBuilder.html#a075ebfc1e2f098e0e0bcf104b3cbb916),
[MeshCore::MeshGeomFacet::Enlarge()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a545696343f9e3a0250a7e98aa23f8e1f),
[Sketcher::SketchObject::extend()](../../d9/dad/classSketcher_1_1SketchObject.html#a863df4c6af57263b15a8170b377ef466),
and [Base::BoundBox3< _Precision
>::IntersectPlaneWithLine()](../../d8/d12/classBase_1_1BoundBox3.html#a5754b8ae362cd53be98a930be6b0cd73).

## ◆ ScaleX()

template<class _Precision >

void Vector3::ScaleX  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
## ◆ ScaleY()

template<class _Precision >

void Vector3::ScaleY  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
## ◆ ScaleZ()

template<class _Precision >

void Vector3::ScaleZ  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
## ◆ Set()

template<class _Precision >

void Vector3::Set  | ( | _Precision  | _fX_ ,   
---|---|---|---  
|  | _Precision  | _fY_ ,   
|  | _Precision  | _fZ_  
| ) | |   
  
Referenced by
[StdCmdAlignment::activated()](../../df/d17/classStdCmdAlignment.html#a44409be4abd266d5d5e34dacb5484101),
[Base::InventorBuilder::addBoundingBox()](../../db/d7f/classBase_1_1InventorBuilder.html#a7fa4b2eb43c7d1a8df907bc949462fec),
[Base::BoundBox3< _Precision
>::CalcPlane()](../../d8/d12/classBase_1_1BoundBox3.html#ae34731e1d63a61b2d83e411a5043ebd6),
[MeshCore::MeshAlgorithm::CheckFacets()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#ac8032a5a0a06cee43035edcb9253b731),
[MeshCore::CylinderSurfaceFit::CylinderSurfaceFit()](../../d1/d68/classMeshCore_1_1CylinderSurfaceFit.html#a69dc3258327881edffb31edcadb637f0),
[MeshCore::MeshGeomFacet::DistanceToPoint()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a58f664bc14e352bdd067e05688d20910),
[Part::Extrusion::fetchAxisLink()](../../db/d6c/classPart_1_1Extrusion.html#aa781c2570b1b3d21e7879742e6e599ab),
[Part::Revolution::fetchAxisLink()](../../d3/d17/classPart_1_1Revolution.html#a53326aff3dc6f91064df528f1d706e18),
[MeshCoreFit::CylinderFit::findBestSolDirection()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a6e0db1db743acde2daf19bc60f9d1e0c),
[Mesh::MeshObject::getEigenSystem()](../../d8/dcc/classMesh_1_1MeshObject.html#a786294ab69d0aedecf59d3d3fb208d80),
[MeshCore::CylinderFit::GetInitialAxisFromNormals()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a94896bef3d7356707b274d1d34c101f4),
[MeshCore::MeshGeomFacet::IntersectWithPlane()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a1a60849171e88c8fcf54e341b36a56eb),
[Base::ViewProjMatrix::inverse()](../../dd/dc2/classBase_1_1ViewProjMatrix.html#ae9f20859b62da577c761b873751255eb),
[Part::GeomCurve::normalAt()](../../d4/dc1/classPart_1_1GeomCurve.html#a13a9604438c2f6887603ab4171dedfb6),
[MeshPart::MeshProjection::projectEdgeToEdge()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#a322496a26bba88d2ff370beef12fdc3b),
[MeshCore::MeshOutput::Save3MFModel()](../../db/d14/classMeshCore_1_1MeshOutput.html#a37bb55249af3cbca138ae4536bf71325),
[MeshCore::MeshOutput::SaveOBJ()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3d771358cea3ae77d666c54aba2692b5),
[MeshCore::MeshOutput::SaveOFF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8b4f5b020dd2b94b087ff831b7aee3c4),
[MeshCore::MeshOutput::SaveSMF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a7b44d31efb50a5d64b2b08fbcc91963f),
[MeshGui::ViewProviderMeshDegenerations::showDefects()](../../d2/da9/classMeshGui_1_1ViewProviderMeshDegenerations.html#a954810db894668aaea3d6a26f310f2ea),
[MeshCore::PlaneFitSmoothing::Smooth()](../../d4/d74/classMeshCore_1_1PlaneFitSmoothing.html#a8c02774a72bb114362c993f51dc0d7ec),
[MeshCore::PlaneFitSmoothing::SmoothPoints()](../../d4/d74/classMeshCore_1_1PlaneFitSmoothing.html#aa6fba7b76ab58215430b86da7dec700d),
[MeshCore::SphereSurfaceFit::SphereSurfaceFit()](../../d2/de9/classMeshCore_1_1SphereSurfaceFit.html#a034ac96465a9c7e760e464c5ee9b17d3),
[Fem::FemMesh::transformGeometry()](../../d3/d2e/classFem_1_1FemMesh.html#aab711c8f90f163cf31e4ef031c795f79),
[SketcherGui::DrawSketchHandlerLineSet::updateTransitionData()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a87c661c6611a6c685accb1c089fdeba8),
and
[Fem::FemMesh::writeABAQUS()](../../d3/d2e/classFem_1_1FemMesh.html#afa7074c6fdb3eaea8716c56a9c952785).

## ◆ Sqr()

template<class _Precision >

_Precision Vector3::Sqr  
---  
  
Squared length of the vector.

Referenced by
[MeshCore::MeshGeomFacet::AspectRatio()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#aa946c0e5fd5097d83ec19b89f8b25508),
[Gui::PropertyEditor::RotationHelper::assignProperty()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#ac33aed562242424b692098b02ff8e956),
[MeshCore::CylinderFit::GetInitialAxisFromNormals()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a94896bef3d7356707b274d1d34c101f4),
[Base::Matrix4D::hasScale()](../../d5/db4/classBase_1_1Matrix4D.html#a88d80af7379be993bf083974310879a6),
[Base::Vector3< _Precision
>::ProjectToLine()](../../d1/d13/classBase_1_1Vector3.html#afa7f4034959748405a9a53ae6e70dece),
[Base::Vector3< _Precision
>::ProjectToPlane()](../../d1/d13/classBase_1_1Vector3.html#a24f91e91499245ab4282c6d0d0b7630c),
[MeshCore::MeshGeomFacet::Roundness()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a521282713bec97c7a1327e31e15e2f04),
[Base::CoordinateSystem::setAxes()](../../d1/d66/classBase_1_1CoordinateSystem.html#aa739d8948fc7bc060cd5fdbc22f90d93),
[Part::GeomEllipse::setMajorAxisDir()](../../db/d52/classPart_1_1GeomEllipse.html#a05d29bbfe1e80f91559e12fb8b2cfc36),
[Part::GeomArcOfEllipse::setMajorAxisDir()](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#acb1e2d5a06a4a7b7e8d8ddee835e11b4),
[Part::GeomArcOfHyperbola::setMajorAxisDir()](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#a59725dadb45c4d7afd0562b646c36f79),
[MeshCore::MeshGeomFacet::SetNormal()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a284eb15810eef8ba429a00f3d4673c48),
[Gui::LinkView::setTransform()](../../da/d11/classGui_1_1LinkView.html#a19c90dc21b9657ff2b378cd1588c7f64),
[Part::GeomArcOfConic::setXAxisDir()](../../db/d48/classPart_1_1GeomArcOfConic.html#afdcf8bd89f0e40ba453289cbf098b364),
[Base::CoordinateSystem::setXDirection()](../../d1/d66/classBase_1_1CoordinateSystem.html#a7f2a242ff6094d1743686222ed37192d),
and
[Base::CoordinateSystem::setYDirection()](../../d1/d66/classBase_1_1CoordinateSystem.html#ad0bcb826af0de6e8e256cae84dccbd26).

## ◆ TransformToCoordinateSystem()

template<class _Precision >

void Vector3::TransformToCoordinateSystem  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclDirX_ ,   
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclDirY_  
| ) | |   
  
Transforms this point to the coordinate system defined by origin _rclBase_ ,
vector _vector_ rclDirX and vector _vector_ rclDirY.

Note

     _rclDirX_ must be perpendicular to _rclDirY_ , i.e. _rclDirX_ * _rclDirY_ = 0.. 

References [Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983).

Referenced by
[MeshCore::PlaneFit::Dimension()](../../db/dab/classMeshCore_1_1PlaneFit.html#a4044cefa963dbb89b1fea7e4044346b5),
[MeshCore::PlaneFit::GetLocalPoints()](../../db/dab/classMeshCore_1_1PlaneFit.html#afea00501e51e679c09dc7ca9064d4555),
[MeshCore::SurfaceFit::PolynomFit()](../../d2/d9a/classMeshCore_1_1SurfaceFit.html#a7dc8000c3b6f4bcae7320a4c8a48d489),
and
[MeshCore::AbstractPolygonTriangulator::PostProcessing()](../../d9/d6e/classMeshCore_1_1AbstractPolygonTriangulator.html#ae63972f8589101bef8696a9b4dccdd08).

## Member Data Documentation

## ◆ x

template<class _Precision >

_Precision [Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision
>::x  
---  
  
x-coordinate

Referenced by
[PartGui::DlgRevolution::accept()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a92a90c8ff44e8e2f6774d0713d47bbbd),
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[ReenGui::FitBSplineSurfaceWidget::accept()](../../d9/d48/classReenGui_1_1FitBSplineSurfaceWidget.html#af94ddfaebc20a805f34a94face578ce6),
[CmdSketcherConstrainLock::activated()](../../d9/dc2/classCmdSketcherConstrainLock.html#a337b578fd38e4359b3177138a91a9162),
[CmdSketcherConstrainDistance::activated()](../../d4/de5/classCmdSketcherConstrainDistance.html#a24031613fd513a79165dfec1d75d6ecb),
[CmdSketcherConstrainDistanceX::activated()](../../de/d7a/classCmdSketcherConstrainDistanceX.html#a175608d3c6099fc7504de3b5641a01c0),
[CmdSketcherConstrainPerpendicular::activated()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#ae4b39128a2a69168a71c214a6632f6fa),
[CmdSketcherConstrainAngle::activated()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a0d48a74c0960a5a240c1a39137f070a3),
[Base::BoundBox3< _Precision
>::Add()](../../d8/d12/classBase_1_1BoundBox3.html#ac9052e09ea4470fc68fb18b70ac608af),
[Mod.PartDesign.Scripts.FilletArc.Vector::add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[Sketcher::Sketch::addArc()](../../d9/d9b/classSketcher_1_1Sketch.html#adf324f188acc42de614642df2ea5bf66),
[Sketcher::Sketch::addArcOfEllipse()](../../d9/d9b/classSketcher_1_1Sketch.html#a61610930dafc4117e76e06c4e7f2e226),
[Sketcher::Sketch::addArcOfHyperbola()](../../d9/d9b/classSketcher_1_1Sketch.html#a9e105418a52e77f027b25e0568ba2e1f),
[Sketcher::Sketch::addArcOfParabola()](../../d9/d9b/classSketcher_1_1Sketch.html#a34fecada77c068415ee790ff28b3e2af),
[Base::InventorBuilder::addBoundingBox()](../../db/d7f/classBase_1_1InventorBuilder.html#a7fa4b2eb43c7d1a8df907bc949462fec),
[Sketcher::Sketch::addBSpline()](../../d9/d9b/classSketcher_1_1Sketch.html#a01262194178463ad90291725a52eb912),
[Sketcher::SketchObject::addCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#a2ae92a618d60a264ed20d7a359b89f98),
[Sketcher::Sketch::addEllipse()](../../d9/d9b/classSketcher_1_1Sketch.html#abed34ded55406512fb2dca3e58cfcde8),
[PartGui::FaceColors::Private::addFacesToSelection()](../../d4/d4b/classFaceColors_1_1Private.html#a9eb1efd1782f31dd3bad393299212f3b),
[MeshCore::MeshFastBuilder::AddFacet()](../../d3/d1d/classMeshCore_1_1MeshFastBuilder.html#a309ce02230a45347d21e2f8a861e9cc6),
[Points::PointsGrid::AddPoint()](../../d1/d4d/classPoints_1_1PointsGrid.html#a3c132db635cb686576c2b85a342891a7),
[MeshCore::MeshPointGrid::AddPoint()](../../dc/de4/classMeshCore_1_1MeshPointGrid.html#a58ee74fcf8e6719b3633d5329c06604a),
[Gui::SelectionSingleton::addSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a90a0ee6e4826630e0e35ba1deb5e98fa),
[Base::Builder3D::addSingleArrow()](../../d6/d1b/classBase_1_1Builder3D.html#a000b4d9d1342d22dcb7c0ded96ad45b2),
[Base::InventorBuilder::addSingleArrow()](../../db/d7f/classBase_1_1InventorBuilder.html#a075ebfc1e2f098e0e0bcf104b3cbb916),
[Base::Builder3D::addSingleLine()](../../d6/d1b/classBase_1_1Builder3D.html#accf2a8116bd1142069e93a4eac808d7b),
[Base::InventorBuilder::addSingleLine()](../../db/d7f/classBase_1_1InventorBuilder.html#a404c84909791311b5fe386216c074d65),
[Base::InventorBuilder::addSinglePlane()](../../db/d7f/classBase_1_1InventorBuilder.html#a7b3b6c4b92eb6b42f4ceab91ad24bc43),
[Base::Builder3D::addSingleTriangle()](../../d6/d1b/classBase_1_1Builder3D.html#a536ca5856ad41bf83a85d68af4ec5f68),
[Base::InventorBuilder::addSingleTriangle()](../../db/d7f/classBase_1_1InventorBuilder.html#aa559cd33d73da4c7f081923dd5c9ea51),
[Sketcher::SketchObject::addSymmetric()](../../d9/dad/classSketcher_1_1SketchObject.html#afcbb1d6f5a99e52a70fdf6d9d3c9d361),
[Base::Builder3D::addTransformation()](../../d6/d1b/classBase_1_1Builder3D.html#ac722adc9f5581af07ee4fb411e5bb7f5),
[Base::InventorBuilder::addTransformation()](../../db/d7f/classBase_1_1InventorBuilder.html#a6a994fa52660b07970bb2d9213f0257c),
[MeshCore::MeshTopoAlgorithm::AdjustEdgesToCurvatureDirection()](../../d6/d22/classMeshCore_1_1MeshTopoAlgorithm.html#a9d434d84a9f0707b8c6ca3b4c35a0c26),
[TechDraw::DrawUtil::angleWithX()](../../da/d23/classTechDraw_1_1DrawUtil.html#a5a709f9c1aa24f2f0de8ea18771b882b),
[TechDraw::Generic::apparentInter()](../../dd/d23/classTechDraw_1_1Generic.html#a324a686052aad81c15c53f46d663e40b),
[CmdSketcherConstrainLock::applyConstraint()](../../d9/dc2/classCmdSketcherConstrainLock.html#aa27c938f88973099b74d9474476d4254),
[CmdSketcherConstrainDistance::applyConstraint()](../../d4/de5/classCmdSketcherConstrainDistance.html#a9c0f733b397d4f7e05af5f7c70f9debb),
[CmdSketcherConstrainDistanceX::applyConstraint()](../../de/d7a/classCmdSketcherConstrainDistanceX.html#abf16c738ea7247db91721d5d14d279fc),
[CmdSketcherConstrainPerpendicular::applyConstraint()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#aa62bab542b8f016bd752fdef90110778),
[CmdSketcherConstrainAngle::applyConstraint()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a5602881a59f6c0a0a83a30641560aeb7),
[FemGui::ViewProviderFemMesh::applyDisplacementToNodes()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a2d65b42122fa5ff20cdd2cb783b7e8c5),
[TechDraw::DrawProjGroupItem::autoPosition()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#aed7c8d696a4a2b4f3a172ebc3789cbf7),
[TechDrawGui::QGIViewBalloon::balloonLabelDragFinished()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a287e2445be0351ce418e50714a807ea4),
[Base::BoundBox3< _Precision
>::BoundBox3()](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38),
[TechDraw::DrawUtil::boxIntersect2d()](../../da/d23/classTechDraw_1_1DrawUtil.html#a394f9eed54ca909914560d4a3bfc09d3),
[TechDraw::BSpline::BSpline()](../../d6/d09/classTechDraw_1_1BSpline.html#ab0d19db0c31b1dd84f5bdefcb2303443),
[TechDraw::CenterLine::calcEndPoints()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a34df15a8a959516ecc49512c3ec5a73c),
[TechDraw::CenterLine::calcEndPoints2Lines()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a54d1cc5e3f8aa8923c2c28bdbe25c262),
[TechDraw::CenterLine::calcEndPoints2Points()](../../d5/dd5/classTechDraw_1_1CenterLine.html#aedb72634306a11f9eb49ffac16eb7e2b),
[TechDraw::CenterLine::calcEndPointsNoRef()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ac096a3e174023e9aa7efaab88e4df343),
[MeshGui::ViewProviderMeshTransformDemolding::calcNormalVector()](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#ac95395413a936658e653faa60c9a3795),
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[TechDraw::CenterLine::CenterLine()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ae57d1c63055e3adaa4d445554084481e),
[MeshCore::MeshGeomFacet::CenterOfCircumCircle()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#afa4800556683c823c6e8a947b0f6b26d),
[MeshCore::MeshGeomFacet::CenterOfInscribedCircle()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#af8a76150bc765b0331bc42004f012cb9),
[DraftGui.DraftToolBar::changeXValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a2264e5b2058aeec75cb9044b36485378),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[MeshCore::MeshAlgorithm::CheckFacets()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#ac8032a5a0a06cee43035edcb9253b731),
[Sketcher::SketchAnalysis::checkHorizontal()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a81ee6f119f2454e26c9ec3df9cee9e5a),
[MeshCore::MeshGrid::CheckPosition()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a93306eb31fbf0f2fd27f197bf226ba83),
[Sketcher::SketchAnalysis::checkVertical()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a6f9e55182f9d529c50ea27bdacfe739f),
[PathScripts.PathInspect.GCodeEditorDialog::cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[TechDrawGui::TaskRichAnno::commonFeatureUpdate()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ab5a728afdf435f4c1631b56211559576),
[PartDesign::FeatureExtrude::computeDirection()](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a3af51bee887de0bc89953128cb0a4d1c),
[Part::Extrusion::computeFinalParameters()](../../db/d6c/classPart_1_1Extrusion.html#a4b4ddc216eb6449e2b21480a430f5df8),
[MeshCore::MeshCurvature::ComputePerVertex()](../../d3/d7e/classMeshCore_1_1MeshCurvature.html#a8b29abff540cab896736a08bbb74189f),
[TechDraw::CosmeticEdge::CosmeticEdge()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a6e49936bd5b7832d1024b04c2399095f),
[TechDrawGui::TaskRichAnno::createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[Part::createFilletGeometry()](../../d2/db9/namespacePart.html#a4e47966fd6c762b34824b98614b76541),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[Import::ExportOCAF::createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[Mod.PartDesign.Scripts.FilletArc.Vector::cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[cSimTool::cSimTool()](../../d3/d31/classcSimTool.html#a3b1d2577bcdde16048e83c1c5c75621c),
[TechDrawGui::QGIFace::dashedPPath()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#ac893b16b4130c990b40e45750d31b9a9),
[FemGui::TaskCreateNodeSet::DefineNodes()](../../da/d68/classFemGui_1_1TaskCreateNodeSet.html#a6bd7d00ad2d337fbb90c45d927e80c71),
[MeshCore::MeshInfo::DetailedEdgeInfo()](../../d3/d42/classMeshCore_1_1MeshInfo.html#aae041af175b0080900634a908c05a0c8),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[Base::CoordinateSystem::displacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970),
[TechDraw::DrawViewDimension::dist2Segs()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#abf50565454fb7688d30f946052010504),
[Base::Vector3< double
>::DistanceToLine()](../../d1/d13/classBase_1_1Vector3.html#af38176c3192c969e1ae2255a84885b8a),
[MeshCore::MeshGeomFacet::DistanceToLineSegment()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a275420989c96287043bc6b9ae1232111),
[MeshCore::MeshGeomFacet::DistanceToPoint()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a58f664bc14e352bdd067e05688d20910),
[PathScripts.PostUtils.GCodeEditorDialog::done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Base::Vector3< _Precision
>::Dot()](../../d1/d13/classBase_1_1Vector3.html#a876a8620ec4213d4bc580190328ad899),
[Mod.PartDesign.Scripts.FilletArc.Vector::dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[TechDrawGui::QGIViewBalloon::drawBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6d26eb06a692339e02c1b57545903f29),
[SketcherGui::EditModeConstraintCoinManager::drawConstraintIcons()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a20c4280c68dc704bd2652d6097b0383a),
[TechDrawGui::QGIViewPart::drawSectionLine()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a513e571f325b7c7cac09bdec0d1c512d),
[TechDraw::GeometryUtils::edgeFromGeneric()](../../d5/d83/classTechDraw_1_1GeometryUtils.html#a06fdb57b76577f20da4b79ab357aac24),
[PartDesign::Pad::execute()](../../d9/d14/classPartDesign_1_1Pad.html#a17b37a5aaa299709fbb066564ef25b3e),
[PartDesign::Pocket::execute()](../../d1/d89/classPartDesign_1_1Pocket.html#aac791837d2ea389e30768f0fb6d25935),
[Drawing::ProjectionAlgos::execute()](../../db/d32/classDrawing_1_1ProjectionAlgos.html#a014d5c556a4982a188e47e4e713ff883),
[Part::Mirroring::execute()](../../dc/dac/classPart_1_1Mirroring.html#aed38846265cf2381aae85d15dfb74be7),
[PartDesign::Hole::execute()](../../dd/dd0/classPartDesign_1_1Hole.html#ad3161d80bf31dc136534283281a5b3ad),
[TechDraw::ProjectionAlgos::execute()](../../dd/d7c/classTechDraw_1_1ProjectionAlgos.html#a014d5c556a4982a188e47e4e713ff883),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[Import::ImpExpDxfWrite::exportAngularDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a020d31516ae6342bc1160de1daabf79a),
[Import::ImpExpDxfWrite::exportDiametricDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#abb723df58a935f6b0590238bc09f7ad5),
[Import::ImpExpDxfWrite::exportLinearDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a469a35bb67d953bd7fc2193a70efa083),
[Import::ImpExpDxfWrite::exportRadialDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#aeccef9eee470f21a95169ed063af94e4),
[Import::ImpExpDxfWrite::exportText()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#aa372554ea19f3fd6ff21c048f8bef37c),
[Sketcher::SketchObject::exposeInternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a7d89f466b41e7479505e70c73d832428),
[TechDrawGui::QGISectionLine::extensionEndsISO()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#accfe95859edaa0110e334d22821ccd0b),
[TechDrawGui::QGISectionLine::extensionEndsTrad()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#a1f6e235dee697a90a21888b0eca7f520),
[Mesh::Facet::Facet()](../../d7/d79/classMesh_1_1Facet.html#aed4f45fccca652d2000ff55e1a06583c),
[Fem::FemPostDataAlongLineFilter::FemPostDataAlongLineFilter()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ac595ec7511d8d0a5111b5461ef0fa446),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[Part::find2DLinesIntersection()](../../d2/db9/namespacePart.html#a0dd46c09269433a805588c348a585bb0),
[TechDraw::LineSet::findAtomStart()](../../d7/d2f/classTechDraw_1_1LineSet.html#ad2bdafb64d48697d2072a07e8ad921e2),
[MeshCoreFit::CylinderFit::findBestSolDirection()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a6e0db1db743acde2daf19bc60f9d1e0c),
[Part::findFilletCenter()](../../d2/db9/namespacePart.html#ab01c47ee6de2dab1626ab457c264b394),
[MeshCore::CylinderFit::Fit()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a2b728f7c295c98d85f6159610ff36bc4),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[VisualPathSegmentVisitor::g38()](../../de/d18/classVisualPathSegmentVisitor.html#aefd30507eff704570080c7fe03b6d11d),
[PartDesign::Helix::generateHelixPath()](../../d3/d78/classPartDesign_1_1Helix.html#a04dd9590e1c0afe9dd3f1066ab9f0395),
[Part::GeomLine::GeomLine()](../../d5/d30/classPart_1_1GeomLine.html#a5a8457c1f4e91bf66c8070d86eb9887a),
[TechDrawGui::QGIViewPart::geomToPainterPath()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#aea20fa3e1100ec52240032c108712790),
[TechDrawGui::TaskDetail::getAnchorScene()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ac47e200bf1be3381e59b3c6c4610494d),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[Fem::Constraint::getBasePoint()](../../d0/d11/classFem_1_1Constraint.html#a53b58263b54f9ab82afbc002761ccd24),
[TechDraw::DrawViewSection::getCSFromBase()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a761c0e9c4fe742ad0f6250428875ecd4),
[TechDrawGui::QGEPath::getDeltasFromLeader()](../../d9/da7/classTechDrawGui_1_1QGEPath.html#a59c9f7dddcda624bf7724c39938353f2),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[MeshCoreFit::CylinderFit::GetDistanceToCylinder()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a7e37395d2a64271694828d763d1582d4),
[MeshCoreFit::SphereFit::GetDistanceToSphere()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#aca8b41099e947b212fee4dd15118fb69),
[Mesh::MeshObject::getEigenSystem()](../../d8/dcc/classMesh_1_1MeshObject.html#a786294ab69d0aedecf59d3d3fb208d80),
[MeshCore::MeshKernel::GetGravityPoint()](../../dd/d95/classMeshCore_1_1MeshKernel.html#a0cce71449b9303e9e2509487f487b290),
[MeshCore::CylinderFit::GetInitialAxisFromNormals()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a94896bef3d7356707b274d1d34c101f4),
[TechDrawGui::QGIWeldSymbol::getKinkPoint()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a369b5176e262931bc83085510cc7a0b9),
[MeshCore::PlaneFit::GetLocalPoints()](../../db/dab/classMeshCore_1_1PlaneFit.html#afea00501e51e679c09dc7ca9064d4555),
[Part::Feature::getLocation()](../../d7/d7e/classPart_1_1Feature.html#a84164b4adfe9b6ecef87da8d7aa1ac9d),
[Part::FeatureReference::getLocation()](../../d2/da1/classPart_1_1FeatureReference.html#aee6f4d426e17d5a0193108fd06f7309c),
[Base::BoundBox3< _Precision
>::GetOctantFromVector()](../../d8/d12/classBase_1_1BoundBox3.html#ae68b2abe794808185a01fd6cb01fad42),
[MeshGui::PlaneFitParameter::getParameter()](../../da/d31/classMeshGui_1_1PlaneFitParameter.html#acc96292a875e15e9e792e59994f02a71),
[MeshGui::CylinderFitParameter::getParameter()](../../d6/d6d/classMeshGui_1_1CylinderFitParameter.html#ab93a68400083131e275c6f9d3af94fab),
[TechDraw::LineSet::getPatternStartPoint()](../../d7/d2f/classTechDraw_1_1LineSet.html#aba20266c9fd3898beef7917120751246),
[Mesh::MeshObject::getPoint()](../../d8/dcc/classMesh_1_1MeshObject.html#a3b5cfb389c3be7ecad0809494f54418d),
[Mesh::MeshObject::getPointNormal()](../../d8/dcc/classMesh_1_1MeshObject.html#ab3953ee00afa96512b922acb9ea5ec12),
[Mesh::MeshObject::getPointNormals()](../../d8/dcc/classMesh_1_1MeshObject.html#a16c59852a6633307010cc619c4d10143),
[Mesh::MeshObject::getPoints()](../../d8/dcc/classMesh_1_1MeshObject.html#a4b7287613ca9dbab79d581af2a0632e6),
[TechDraw::DrawViewPart::getProjectionCS()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ae1dd72b98fa563bf72d6c39f49577632),
[Base::Rotation::getRawValue()](../../d4/d18/classBase_1_1Rotation.html#afe860f0bcfaec728e99861e4c65904aa),
[PartDesignGui::ViewProviderDatum::getRelevantBoundBox()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a8437c5be88154b9cb0bd2bae5ef94db3),
[TechDraw::DrawViewSection::getSectionCS()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aefc378d8464959b191ac4ff96f6bca12),
[Base::BoundBox3< _Precision
>::GetSideFromRay()](../../d8/d12/classBase_1_1BoundBox3.html#a900e54e09a7e5ba1909a10a0d83c40ea),
[TechDrawGui::QGIWeldSymbol::getTailPoint()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a2699319ad36e2b727f54a1a4e3268c7c),
[TechDrawGui::QGIWeldSymbol::getTileOrigin()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a1ac4c88fab7e971e0ab980b801c91f3e),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[MeshCore::AbstractPolygonTriangulator::GetTransformToFitPlane()](../../d9/d6e/classMeshCore_1_1AbstractPolygonTriangulator.html#aaaa240d0f1a906bdc7cc01c81dea9250),
[TechDraw::DrawGeomHatch::getTrimmedLinesSection()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a2fe5d2f18fe5801e37a1cfdb967fbce3),
[Gui::LocationWidget::getUserDirection()](../../d9/d9a/classGui_1_1LocationWidget.html#a928aeb60d1d1a95d4d336c6901fb950b),
[Gui::LocationDialog::getUserDirection()](../../dc/d22/classGui_1_1LocationDialog.html#aa52301a6aec2f1b750929d7444765c33),
[Base::Rotation::getValue()](../../d4/d18/classBase_1_1Rotation.html#af95c57a06636f68b2a6cc779dc042edd),
[TechDraw::DrawProjGroupItem::getViewAxis()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a66cab4b4ebd52d41889c7fdb9c854821),
[TechDraw::getViewAxis()](../../d7/d31/namespaceTechDraw.html#ad612c2d90cb50e87312099ea9824c509),
[MeshCore::MeshKernel::GetVolume()](../../dd/d95/classMeshCore_1_1MeshKernel.html#a919704318d645c2a0d30cd9fa2203439),
[Fem::FemMesh::getVolume()](../../d3/d2e/classFem_1_1FemMesh.html#a86dfe0bdac5ccbc115b39af5780ee2b1),
[Base::Matrix4D::Hat()](../../d5/db4/classBase_1_1Matrix4D.html#ae5b666346437729d9c62741a35497aa7),
[TechDraw::DrawUtil::Intersect2d()](../../da/d23/classTechDraw_1_1DrawUtil.html#afe855bd12c8cea41eb2af19ab79ba99d),
[MeshCore::MeshGeomEdge::IntersectBoundingBox()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#aa33bee65b66dc0904e254e42f20bf02d),
[MeshCore::MeshGeomFacet::IntersectBoundingBox()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0a6b404c351030f6727713ab4b9fa805),
[TechDraw::AOC::intersectsArc()](../../d0/d5c/classTechDraw_1_1AOC.html#a061b7f38a3cd0dca1c8c08a03c7a05fe),
[TechDraw::BSpline::intersectsArc()](../../d6/d09/classTechDraw_1_1BSpline.html#a5af43bc17061b8e8f6598dec030ea659),
[MeshCore::MeshGeomFacet::IntersectWithFacet()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a4324352edc96819d5ce83009cd1ed2df),
[Base::BoundBox3< _Precision
>::IntersectWithLine()](../../d8/d12/classBase_1_1BoundBox3.html#aa1b97e4eab9eecfd4711d01a3b9ed533),
[MeshCore::MeshGeomFacet::IntersectWithPlane()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a1a60849171e88c8fcf54e341b36a56eb),
[Gui::ViewVolumeProjection::inverse()](../../d8/d4d/classGui_1_1ViewVolumeProjection.html#a1d7fe268b671119971278bdf467133f2),
[Base::BoundBox3< _Precision
>::IsCutLine()](../../d8/d12/classBase_1_1BoundBox3.html#a55a718fe21f7a5240ac7b6651b4c5822),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#a755404902a0ec9b28e954657ba887307),
[cSimTool::isInside()](../../d3/d31/classcSimTool.html#ad2e9adbe06388f51b1ba05025d6021a3),
[TechDraw::DrawViewPart::isIso()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#af3b5d2ae674b8b2b423edc3b12833e29),
[Sketcher::SketchObject::isPointOnCurve()](../../d9/dad/classSketcher_1_1SketchObject.html#a56b81b36bf54912326dbd22750c19e8c),
[TechDraw::DrawWeldSymbol::isTailRightSide()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#a146cec4168e615dc4ddad1ea3eefbf2e),
[TechDraw::legacyViewAxis1()](../../d7/d31/namespaceTechDraw.html#a6c5c5a402ebdc68e1048cb62d6ef595f),
[Mod.PartDesign.Scripts.FilletArc.Vector::length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Points::PointsAlgos::LoadAscii()](../../d8/d62/classPoints_1_1PointsAlgos.html#a75d94f79566c5ebb47f14fbafa6be26e),
[MeshCore::MeshInput::LoadInventor()](../../d9/d08/classMeshCore_1_1MeshInput.html#acf19f4238be1fd7d9f3b260af125d599),
[MeshCore::MeshInput::LoadPLY()](../../d9/d08/classMeshCore_1_1MeshInput.html#a8f60cc2825d0ffd59075b0892d92417b),
[PartGui::Location::Location()](../../db/d6f/classPartGui_1_1Location.html#a2f77946d77e8f18590ccf3f7e73a18b4),
[MeshPart::MeshAlgos::LoftOnCurve()](../../db/d67/classMeshPart_1_1MeshAlgos.html#af6d0bd2cf1dd2ca04dfb7a7f853f2aba),
[TechDrawGui::QGISectionLine::makeArrowsISO()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#a8f2cce08f6be3eb56a19c7de258ea884),
[TechDrawGui::QGISectionLine::makeArrowsTrad()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#aaa7b66291c65ca1fd3de5a83aa2cdf68),
[TechDraw::DrawGeomHatch::makeEdgeOverlay()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#ad42d700267fb44056f1c72515659170c),
[TechDrawGui::QGIArrow::makeFilledTriangle()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#a48ea2d959065f7dcddd8bf7f60135e62),
[TechDrawGui::QGIArrow::makeForkArrow()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#af362a5208def60772252b3e36d1d2c9a),
[TechDrawGui::QGIArrow::makeHashMark()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#ad350c362524675d0e695781e60dd6945),
[TechDrawGui::QGIArrow::makeOpenArrow()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#a5846b0a5797ddeebbb25e95297088489),
[PartDesign::Feature::makePlnFromPlane()](../../d7/d51/classPartDesign_1_1Feature.html#a6ab00d23c99b505b5bf57dedac353631),
[TechDrawGui::QGIArrow::makePyramid()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#aedbc5bfceac71c55af61aa6981121425),
[Base::Rotation::makeRotationByAxes()](../../d4/d18/classBase_1_1Rotation.html#a0b7c436d3243f3703959c7f6be8ecad2),
[TechDrawGui::QGISectionLine::makeSymbolsISO()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#ac20091d52978917cd18aa37c17df9d6c),
[TechDrawGui::QGISectionLine::makeSymbolsTrad()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#ad784a67840ecc73314d932f8c3f523d9),
[SketcherGui::makeTangentToArcOfEllipseviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#ade2d18eb05327cda22e2eb86409e4642),
[SketcherGui::makeTangentToArcOfHyperbolaviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a2d88b81b020ee6003474b180fad75a3b),
[SketcherGui::makeTangentToArcOfParabolaviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a8153db87ad16afe18f0f5e0a01bf5251),
[SketcherGui::makeTangentToEllipseviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a0221a346db6666022488335587d92562),
[Part::Geometry::mirror()](../../dc/df0/classPart_1_1Geometry.html#af5e2f1761b12dcf915ffb3bc9f2e20fe),
[TechDraw::mirrorShapeVec()](../../d7/d31/namespaceTechDraw.html#a94c08edd68671f2042041c91350f1e36),
[DrawSketchHandlerBSplineInsertKnot::mouseMove()](../../d2/df2/classDrawSketchHandlerBSplineInsertKnot.html#a60d07ab6b604aef8674f849e380898ec),
[SketcherGui::DrawSketchHandlerExtend::mouseMove()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#aa7a93c3f3980309d65e4b1ecc9a559d0),
[SketcherGui::DrawSketchHandlerLineSet::mouseMove()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a113e395cf71488043942d51f78b7d167),
[SketcherGui::DrawSketchHandlerTrimming::mouseMove()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a206e252777274a73c12e2a6b51f0ecc9),
[Base::Matrix4D::move()](../../d5/db4/classBase_1_1Matrix4D.html#ac833395bac6936432368efa5595387bd),
[Sketcher::Sketch::movePoint()](../../d9/d9b/classSketcher_1_1Sketch.html#ad66e807fc32460d6686fb708fdb3a69c),
[TechDraw::moveShape()](../../d7/d31/namespaceTechDraw.html#a6984b4017e3ad0b59304844e743f064a),
[Mod.PartDesign.Scripts.FilletArc.Vector::mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector::norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[Gui::Dialog::Transform::on_applyButton_clicked()](../../d0/d8f/classGui_1_1Dialog_1_1Transform.html#aa736a36e69d76427b945f434e46f3a2a),
[Gui::ViewProviderOrigin::onChanged()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[Fem::FemPostDataAlongLineFilter::onChanged()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ae418afcb8e18abba84d16c2a645a434e),
[PathGui::ViewProviderPath::onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PathGui::PathSelectionObserver::onSelectionChanged()](../../db/d77/classPathGui_1_1PathSelectionObserver.html#a647466bb806e71c512362f4dafc43e7b),
[Base::Vector3< _Precision
>::operator&()](../../d1/d13/classBase_1_1Vector3.html#ab377fb85d034e0486a08805cdf56b629),
[Base::operator*()](../../db/d07/namespaceBase.html#ac7d409d67697b8ea931e0febfe6e26de),
[Base::Matrix4D::operator*()](../../d5/db4/classBase_1_1Matrix4D.html#ab8a45ff4ced15d460ae0b11239629d52),
[Base::Vector3< _Precision
>::operator+()](../../d1/d13/classBase_1_1Vector3.html#a217bd5ebf8797d0930fda829c3f1698f),
[Base::Vector3< _Precision
>::operator-()](../../d1/d13/classBase_1_1Vector3.html#ab8cca8856cabb105f7e2d002078776e4),
[MeshCore::MeshPoint::operator<()](../../dd/db5/classMeshCore_1_1MeshPoint.html#af48745635582de4c6c517382120f6440),
[PathScripts.PathDressupHoldingTags.Tag::originAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aa1cbd48305f117e5197555822fd45f3f),
[DrawingGui::orthoview::orthoview()](../../db/df8/classDrawingGui_1_1orthoview.html#afc8be37cc7e9325e722e05f2736af13d),
[Base::Matrix4D::Outer()](../../d5/db4/classBase_1_1Matrix4D.html#a8e19dc5e655bc920f9527c62c1ecf7aa),
[MeshCore::PlaneSurfaceFit::Parameters()](../../d9/df5/classMeshCore_1_1PlaneSurfaceFit.html#a2c0e5c7c7155ea8eb77c28af1589c1b4),
[MeshCore::CylinderSurfaceFit::Parameters()](../../d1/d68/classMeshCore_1_1CylinderSurfaceFit.html#a77a6a4645558df8448d8284ebe34417b),
[MeshGui::SoFCMeshPickNode::pick()](../../d1/d1b/classMeshGui_1_1SoFCMeshPickNode.html#ac140e23964b3171e35ff15585cd3ba14),
[Attacher::AttachEngine::placementFactory()](../../d2/d85/classAttacher_1_1AttachEngine.html#a0eff77539401a8d4a04554a970bd85b4),
[TechDraw::Vertex::point()](../../dd/db1/classTechDraw_1_1Vertex.html#a6556cf8e5cd0a2fbca8198ee0e06edc8),
[DraftGui.DraftToolBar::pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[MeshCore::SurfaceFit::PolynomFit()](../../d2/d9a/classMeshCore_1_1SurfaceFit.html#a7dc8000c3b6f4bcae7320a4c8a48d489),
[Points::PointsGrid::Pos()](../../d1/d4d/classPoints_1_1PointsGrid.html#aaa5c87982921d2673a7ac3227d2b6714),
[Inspection::MeshInspectGrid::Pos()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#ad94d0cf1a82a11f6b649619db7e1f5e3),
[MeshCore::MeshFacetGrid::Pos()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#ade0d241d31a50d7dd2be2defca3acc1e),
[MeshCore::MeshPointGrid::Pos()](../../dc/de4/classMeshCore_1_1MeshPointGrid.html#a5780dcbbe5bda437bf2b11407cf4c4bb),
[Points::PointsGrid::Position()](../../d1/d4d/classPoints_1_1PointsGrid.html#a5dc29f08827b2e5b849da258c39e0b49),
[MeshCore::MeshGrid::Position()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a8b0dcdb55de3e3c2f8bce7e3a618c0a9),
[MeshCore::MeshFacetGrid::PosWithCheck()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#a59cc6fc0efed46133e4b0580b5fe4ac8),
[SketcherGui::EditModeConstraintCoinManager::processConstraints()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a86abd481aa8756c9ea61b10d2e624804),
[Base::BoundBox3< _Precision
>::ProjectBox()](../../d8/d12/classBase_1_1BoundBox3.html#a4d8b86292716416ed2151d4190291ad1),
[Reen::ParameterCorrection::ProjectControlPointsOnPlane()](../../dd/d71/classReen_1_1ParameterCorrection.html#a54d70272eced8a72c72f8c11a11ac568),
[MeshPart::CurveProjectorSimple::projectCurve()](../../db/d5f/classMeshPart_1_1CurveProjectorSimple.html#a5932b3a0d0a1ee7119cc7f7b5f180ef8),
[MeshPart::CurveProjectorShape::projectCurve()](../../dc/d83/classMeshPart_1_1CurveProjectorShape.html#a78cb49a17db5b6adcb772e9589d32580),
[MeshPart::MeshProjection::projectEdgeToEdge()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#a322496a26bba88d2ff370beef12fdc3b),
[TechDraw::DrawViewPart::projectPoint()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#afbe98e95b0bd7b0cec45b29d29ce46b2),
[TechDraw::LandmarkDimension::projectPoint()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a55be6d3789c069c9509a7ae087324d99),
[MeshCoreFit::SphereFit::ProjectToSphere()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#ad019d88b25f67f7893cdf7179f1cd6c5),
[CDxfWrite::putArrow()](../../d6/d47/classCDxfWrite.html#af14654282595c1d9d2a47b4ac6427bbb),
[CDxfWrite::putText()](../../d6/d47/classCDxfWrite.html#a5af170abde99f5eebff5afac269622fd),
[Points::E57Reader::read()](../../d2/dfb/classPoints_1_1E57Reader.html#a7af6bb0bc50ff56c203f0cb0aa04d458),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[Path::Toolpath::recalculate()](../../d6/d0c/classPath_1_1Toolpath.html#a6fcb5afb3f1023ef686cd87b4f69c0f9),
[PathGui::ViewProviderPath::recomputeBoundingBox()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a4a681a533fc16dba93a80bc3fdfc21c3),
[SketcherGui::DrawSketchHandlerExtend::releaseButton()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#a3e947849d6dc89b7f93e87a1ebd9b160),
[DraftGui.DraftToolBar::reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[TechDraw::CosmeticVertex::Restore()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a11aa1f69e9211c240d61949a237056a1),
[TechDraw::CenterLine::Restore()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
[TechDraw::Vertex::Restore()](../../dd/db1/classTechDraw_1_1Vertex.html#a8db190000b0c2b933006ee8c4d94f511),
[TechDraw::Circle::Restore()](../../d3/d63/classTechDraw_1_1Circle.html#a0c95eda08d536f7de7c3a3abb3007e76),
[TechDraw::AOC::Restore()](../../d0/d5c/classTechDraw_1_1AOC.html#a6adb7fceabe6a5089727723cff4b2760),
[TechDraw::Generic::Restore()](../../dd/d23/classTechDraw_1_1Generic.html#a8850e5eb8a34c47b152b62fafe77905d),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::Geometry::rotate()](../../dc/df0/classPart_1_1Geometry.html#a3c7ebf21592da6737fccb28bf9508a75),
[TechDraw::DrawViewSection::rotateCSArbitrary()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a66a852d7e827780ebf6e1d46439d49e2),
[Base::Vector3< _Precision
>::RotateY()](../../d1/d13/classBase_1_1Vector3.html#a35cf612a380c8d5dddeaa0730f44023c),
[Base::Vector3< _Precision
>::RotateZ()](../../d1/d13/classBase_1_1Vector3.html#af09471673c2fde5a6ef612c1e7f8b9b1),
[Base::Matrix4D::rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aff3583443a5de61928925fa6b8af6f21),
[PartDesign::Helix::safePitch()](../../d3/d78/classPartDesign_1_1Helix.html#a85474d1c32f51cf49c0be48c600993eb),
[Part::GeomLine::Save()](../../d5/d30/classPart_1_1GeomLine.html#a88fd00890c6c4e7729b05c279a64656d),
[Part::GeomLineSegment::Save()](../../d9/d6f/classPart_1_1GeomLineSegment.html#acc377c70086de1bfbfd88e523b663529),
[Robot::Robot6Axis::Save()](../../dc/d5f/classRobot_1_1Robot6Axis.html#a7cf092c9dc75bf16fe3b6a01d9fa03d4),
[Robot::Waypoint::Save()](../../d1/dc7/classRobot_1_1Waypoint.html#a2d0f51a0e8e89f1148887af8e2eb0537),
[TechDraw::CosmeticVertex::Save()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#aee8e2101aa119ae2dc4750442745264c),
[TechDraw::CenterLine::Save()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[TechDraw::Vertex::Save()](../../dd/db1/classTechDraw_1_1Vertex.html#aed3011b8fc0de22659800304c3f1b0af),
[TechDraw::Circle::Save()](../../d3/d63/classTechDraw_1_1Circle.html#ab3a64b9c96ec1f8dc658f0432955bfa5),
[TechDraw::AOC::Save()](../../d0/d5c/classTechDraw_1_1AOC.html#a4627154c0a8d5886ee4ee54231107de2),
[App::PropertyPlacement::Save()](../../da/d51/classApp_1_1PropertyPlacement.html#ae1314101350bc9e76b9d692693c8e9e1),
[App::PropertyRotation::Save()](../../df/d76/classApp_1_1PropertyRotation.html#ad9e882ab49bd192e84f62de9a64c62ce),
[MeshCore::MeshOutput::Save3MFModel()](../../db/d14/classMeshCore_1_1MeshOutput.html#a37bb55249af3cbca138ae4536bf71325),
[MeshCore::MeshOutput::SaveAsciiPLY()](../../db/d14/classMeshCore_1_1MeshOutput.html#a4f5628a8d90a67d09484426b71f30a6a),
[MeshCore::MeshOutput::SaveAsciiSTL()](../../db/d14/classMeshCore_1_1MeshOutput.html#a978a9f0a89ca5ce4d828305f005de62b),
[MeshCore::MeshOutput::SaveAsymptote()](../../db/d14/classMeshCore_1_1MeshOutput.html#a31276c848ed13571a0e7f6f932e5a45e),
[MeshCore::MeshOutput::SaveBinaryPLY()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3f47cee51e773e3eb9310e1bf3ed8bf8),
[MeshCore::MeshOutput::SaveBinarySTL()](../../db/d14/classMeshCore_1_1MeshOutput.html#aa319df520ea268406d3a19a1c4a4f198),
[MeshCore::MeshOutput::SaveIDTF()](../../db/d14/classMeshCore_1_1MeshOutput.html#ad297d3f6095f421beb22932929190fbb),
[MeshCore::MeshOutput::SaveMeshNode()](../../db/d14/classMeshCore_1_1MeshOutput.html#a77cd49917f9394aadcd355c5247546f0),
[MeshCore::MeshOutput::SaveNastran()](../../db/d14/classMeshCore_1_1MeshOutput.html#a832d24717641893b591f5b4d99db9e3f),
[MeshCore::MeshOutput::SaveOBJ()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3d771358cea3ae77d666c54aba2692b5),
[MeshCore::MeshOutput::SaveOFF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8b4f5b020dd2b94b087ff831b7aee3c4),
[Import::ExportOCAF::saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[MeshCore::MeshOutput::SaveSMF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a7b44d31efb50a5d64b2b08fbcc91963f),
[MeshCore::MeshOutput::SaveVRML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8fc229d0641d58846478dbcaa077e8db),
[MeshCore::MeshOutput::SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
[MeshCore::MeshOutput::SaveXML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8a89241b7984ceab819293e9b7385c20),
[Base::Matrix4D::scale()](../../d5/db4/classBase_1_1Matrix4D.html#a3121f149e2b6034c29235b776f44989b),
[TechDraw::CenterLine::scaledGeometry()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a104bfe6bf49d7b364f65000352e670ea),
[MeshCore::MeshAlgorithm::SearchFacetsFromPolyline()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a72f7307406aa5146e43c481b5b3a25d7),
[MeshCore::MeshFacetGrid::SearchNearestFromPoint()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#afbb767d3a8804d125b5d7b80db72d471),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[TechDraw::DrawViewSection::sectionExec()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a79c8f60f63dd54684af4cad42f91ee4e),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
[Part::Part2DObject::seekTrimPoints()](../../d9/d57/classPart_1_1Part2DObject.html#a7f5beeba90cfa4cdf7a72f7827bae9f1),
[Part::GeomConic::setCenter()](../../d1/d86/classPart_1_1GeomConic.html#a0ef572424983321dada7f64d0aa1a3b9),
[Part::GeomArcOfConic::setCenter()](../../db/d48/classPart_1_1GeomArcOfConic.html#a8a2755a6bbbed714049540421198bb8a),
[MeshPartGui::ViewProviderCrossSections::setCoords()](../../dc/dfe/classMeshPartGui_1_1ViewProviderCrossSections.html#acdea9634b2faaa0d83425fd4ede721c7),
[PartGui::ViewProviderCrossSections::setCoords()](../../d8/df0/classPartGui_1_1ViewProviderCrossSections.html#a5e651bd86ec7aa11c84537275b1af31d),
[PartGui::DlgExtrusion::setDir()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a0519f8635962170f77bf009e2071a389),
[PartGui::DlgRevolution::setDirection()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a4df42abdf4af0ef46cb8cfcdca995c9c),
[Gui::LocationWidget::setDirection()](../../d9/d9a/classGui_1_1LocationWidget.html#a2af475de798c64df6995f659a2e7ab40),
[Gui::LocationUi< Ui
>::setDirection()](../../db/da1/classGui_1_1LocationUi.html#a13961053ead815e1adb59564608b8b8a),
[Gui::LocationImpUi< Ui
>::setDirection()](../../df/d30/classGui_1_1LocationImpUi.html#a95f67606fb3dbaab6d199980cb091c63),
[RobotGui::ViewProviderRobotObject::setDragger()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a7a94208ad67ec05ebc9013cac68d34f4),
[Path::Command::setFromPlacement()](../../d7/d2e/classPath_1_1Command.html#a62372d49bbf1003cc81fe7035c7b592e),
[Part::GeomLine::setLine()](../../d5/d30/classPart_1_1GeomLine.html#a602d118b05d480b3f1df2c16f9129bab),
[Part::GeomConic::setLocation()](../../d1/d86/classPart_1_1GeomConic.html#af9bbec6989f1ae76e3e6cff0fb02a05a),
[Part::GeomArcOfConic::setLocation()](../../db/d48/classPart_1_1GeomArcOfConic.html#a1f2b7ce2d1b354cda0ed3c33275d6ec6),
[Part::GeomEllipse::setMajorAxisDir()](../../db/d52/classPart_1_1GeomEllipse.html#a05d29bbfe1e80f91559e12fb8b2cfc36),
[Part::GeomArcOfEllipse::setMajorAxisDir()](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#acb1e2d5a06a4a7b7e8d8ddee835e11b4),
[Part::GeomArcOfHyperbola::setMajorAxisDir()](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#a59725dadb45c4d7afd0562b646c36f79),
[TechDraw::DrawViewBalloon::setOrigin()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a4976c3df5bccf5549523c6960c912624),
[App::PropertyVector::setPyObject()](../../d5/d2b/classApp_1_1PropertyVector.html#a4e4eae3cb50d20fece89b7aac9fa6324),
[Part::TopoShape::setShapePlacement()](../../d8/ded/classPart_1_1TopoShape.html#a8ae38d04353d5ccc4c60beaad3a4a497),
[Gui::Dialog::Transform::setTransformStrategy()](../../d0/d8f/classGui_1_1Dialog_1_1Transform.html#ae3b140a0d601a95674bcbda4e88aa6d4),
[TechDrawGui::TaskSectionView::setUiEdit()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a43dc3542cf896d0778a028ae2be230ce),
[TechDrawGui::TaskCosmeticLine::setUiEdit()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a99ac5dc7728cfedeee3aedf2b9559791),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[TechDrawGui::TaskSectionView::setUiPrimary()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a07485a3822d8c672d6e4580fe4bf858c),
[TechDrawGui::TaskCosmeticLine::setUiPrimary()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a4b1f902a521e9cd5fdf56889d51e52a3),
[PartDesign::Pipe::setupAlgorithm()](../../da/d61/classPartDesign_1_1Pipe.html#aee88e3fe184997d50ac86c9f99b113f2),
[MeshCoreFit::SphereFit::setupObservation()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#a56ac7d52481e7015dd415262b344b470),
[MeshCoreFit::CylinderFit::setupObservation()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a856fae3fea7c099c0972d1f07a89b8c9),
[Gui::PropertyEditor::PropertyRotationItem::setValue()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a65660d1593a8c2f7dabca98e9464c6cc),
[Gui::PropertyEditor::PropertyPlacementItem::setValue()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a7f8e70acbf194633b6b3422b87a07ab3),
[Base::Rotation::setValue()](../../d4/d18/classBase_1_1Rotation.html#a62c0b4012cb383de60d0e4a225c39550),
[Gui::ManualAlignment::setViewingDirections()](../../d7/d97/classGui_1_1ManualAlignment.html#ad3be3a6882c973db3ae9d21b40a85772),
[Part::GeomArcOfConic::setXAxisDir()](../../db/d48/classPart_1_1GeomArcOfConic.html#afdcf8bd89f0e40ba453289cbf098b364),
[MeshGui::ViewProviderMeshOrientation::showDefects()](../../d1/d8e/classMeshGui_1_1ViewProviderMeshOrientation.html#acad074355a307b6f0e8059ae22ba8d54),
[MeshGui::ViewProviderMeshNonManifolds::showDefects()](../../d5/d95/classMeshGui_1_1ViewProviderMeshNonManifolds.html#aa021d71ade5620d8dc36c94220862be8),
[MeshGui::ViewProviderMeshNonManifoldPoints::showDefects()](../../d6/d60/classMeshGui_1_1ViewProviderMeshNonManifoldPoints.html#ad648ec1aee86628d91e6aec48eafaa42),
[MeshGui::ViewProviderMeshDuplicatedFaces::showDefects()](../../d1/d9b/classMeshGui_1_1ViewProviderMeshDuplicatedFaces.html#a435c5361ffb8312295cc076da55d56a8),
[MeshGui::ViewProviderMeshDegenerations::showDefects()](../../d2/da9/classMeshGui_1_1ViewProviderMeshDegenerations.html#a954810db894668aaea3d6a26f310f2ea),
[MeshGui::ViewProviderMeshDuplicatedPoints::showDefects()](../../d5/d26/classMeshGui_1_1ViewProviderMeshDuplicatedPoints.html#af52e3e5a78f9c0ecceab7bb945b1c075),
[MeshGui::ViewProviderMeshIndices::showDefects()](../../dd/d71/classMeshGui_1_1ViewProviderMeshIndices.html#abcb21eec9d9285a3d13ee103e03beaaa),
[MeshGui::ViewProviderMeshFolds::showDefects()](../../d8/d06/classMeshGui_1_1ViewProviderMeshFolds.html#a1a9474aafd32ff0b730a7c795a8fc5e9),
[MeshGui::ViewProviderMeshNode::showOpenEdges()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a7db6427662808c81110a3efc5e523064),
[Part::TopoShape::slice()](../../d8/ded/classPart_1_1TopoShape.html#af54879971e721f27d014b938a1b57eb3),
[Part::TopoShape::slices()](../../d8/ded/classPart_1_1TopoShape.html#a808f0de39292b4e84445ed75b263852e),
[MeshCore::PlaneFitSmoothing::Smooth()](../../d4/d74/classMeshCore_1_1PlaneFitSmoothing.html#a8c02774a72bb114362c993f51dc0d7ec),
[MeshCore::PlaneFitSmoothing::SmoothPoints()](../../d4/d74/classMeshCore_1_1PlaneFitSmoothing.html#aa6fba7b76ab58215430b86da7dec700d),
[Sketcher::SketchObject::split()](../../d9/dad/classSketcher_1_1SketchObject.html#ab73e7a53a704168c004b9aa6c9ad7a68),
[Mod.PartDesign.Scripts.FilletArc.Vector::sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[Part::suggestFilletRadius()](../../d2/db9/namespacePart.html#a1903069f8259f815f24930b78481a785),
[FemGui::TaskPostDataAlongLine::TaskPostDataAlongLine()](../../db/dfe/classFemGui_1_1TaskPostDataAlongLine.html#a63d24585168c09609383c5025fc02c61),
[Base::Matrix4D::toAxisAngle()](../../d5/db4/classBase_1_1Matrix4D.html#aebaf3536031474ff723f0a4abd621e55),
[Gui::View3DInventorViewer::toggleClippingPlane()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ae41b2cfdc548e959d744937ff7a85317),
[Gui::PropertyEditor::PropertyRotationItem::toolTip()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#abbb3c671e82d0c8d54f1f6f2b95abe5d),
[Gui::PropertyEditor::PropertyPlacementItem::toolTip()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#add11217c79e909fa0d6a5fa97d739d2f),
[PartGui::Location::toPlacement()](../../db/d6f/classPartGui_1_1Location.html#a3a6283d802f45e675b6ddf9c714c8f47),
[TechDraw::DrawUtil::toR3()](../../da/d23/classTechDraw_1_1DrawUtil.html#adf8b4269fac80cfb6793e8b54873361e),
[Gui::PropertyEditor::PropertyRotationItem::toString()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a13b41010f83aeb8833bf251d9f1a652a),
[Gui::PropertyEditor::PropertyPlacementItem::toString()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a4866bdcbed09d39f47781b1b5aba4cec),
[TechDraw::CosmeticVertex::toString()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#acb9933bf213ddd298b48d573bfa63f2d),
[TechDraw::CenterLine::toString()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a0af372e8042e1f5e9b02fe8d176d38ca),
[TechDraw::Circle::toString()](../../d3/d63/classTechDraw_1_1Circle.html#a61924379310acb95418698663af100f0),
[TechDraw::AOC::toString()](../../d0/d5c/classTechDraw_1_1AOC.html#aad4400a1a3d31738afea85abe57d6917),
[Path::Command::transform()](../../d7/d2e/classPath_1_1Command.html#a86423c625f09285dd820b578462c199e),
[MeshCore::SurfaceFit::Transform()](../../d2/d9a/classMeshCore_1_1SurfaceFit.html#a4e5b025adea5142985b11b1042c8b256),
[Base::Vector3< double
>::TransformToCoordinateSystem()](../../d1/d13/classBase_1_1Vector3.html#a5369dfa0fb3929e42263f871a865324b),
[Data::ComplexGeoData::transformToInside()](../../d8/daf/classData_1_1ComplexGeoData.html#a8b0cc05d2cf2ab2a1bb36e7f2a70949e),
[MeshCore::MeshSearchNeighbours::TriangleCutsSphere()](../../d1/d7c/classMeshCore_1_1MeshSearchNeighbours.html#acb9381777434d3f7ca91c066aaee5124),
[DraftGui.DraftToolBar::update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar::update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[PartDesign::Groove::updateAxis()](../../d7/de3/classPartDesign_1_1Groove.html#a064b27171c35a5be3b681e2856208747),
[PartDesign::Helix::updateAxis()](../../d3/d78/classPartDesign_1_1Helix.html#aa8bfed8d9b7d87cdebf9e491a6193fd6),
[PartDesign::Revolution::updateAxis()](../../d2/de6/classPartDesign_1_1Revolution.html#a07ae95f9e32e5240284db567e6984b0d),
[TechDrawGui::TaskCosmeticLine::updateCosmeticLine()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a8f118f269d306e8675de346600f24e77),
[FemGui::ViewProviderFemConstraintBearing::updateData()](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#a3b3cf2fa05760751890d9e1cf51f178f),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintForce::updateData()](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#ad691cf23756106d6b0ea043ddebd1b94),
[FemGui::ViewProviderFemConstraintGear::updateData()](../../d1/d2f/classFemGui_1_1ViewProviderFemConstraintGear.html#a56f097a322b6fe5b2b4b7eead3374c49),
[FemGui::ViewProviderFemConstraintPulley::updateData()](../../d8/dfc/classFemGui_1_1ViewProviderFemConstraintPulley.html#a7ba40d63d4dff464026a808438d3630b),
[FemGui::ViewProviderFemConstraintTransform::updateData()](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#a2adf8aba7f15f7b95399068ab39c47b8),
[FemGui::ViewProviderFemPostPlaneFunction::updateData()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#a6ec898b1ee3b9ae2983c1f424b2a55f4),
[FemGui::ViewProviderFemPostSphereFunction::updateData()](../../d4/da4/classFemGui_1_1ViewProviderFemPostSphereFunction.html#a9fac4b851c890977a0c56223e6dcf40d),
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
[DraftGui.DraftToolBar::updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
[Gui::ViewProviderDragger::updateTransform()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5f8676364e82e30b6e558c8f25e06b88),
[SketcherGui::DrawSketchHandlerLineSet::updateTransitionData()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a87c661c6611a6c685accb1c089fdeba8),
[DraftGui.DraftToolBar::validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
[Gui::PropertyEditor::PropertyRotationItem::value()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a863981824fc5e2a970540f4e707913d1),
[Gui::PropertyEditor::PropertyPlacementItem::value()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a02b71a4429874d510e780c4a2375a1be),
[MeshGui::ViewProviderMeshTransformDemolding::valueChangedCallback()](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#a0866accd492d2de4c56bf1948fcf999c),
[Path::PathSegmentWalker::walk()](../../d0/d7b/classPath_1_1PathSegmentWalker.html#a2d2253be4424a16caf28ec136b658dc6),
[automotive_design.right_angular_wedge::wr1()](../../d4/df4/classautomotive__design_1_1right__angular__wedge.html#a08ba5a830562d7f45bb10fe924c7b534),
[Points::PlyWriter::write()](../../d4/d57/classPoints_1_1PlyWriter.html#afcad40b7eec0e6e291d5bb1ffc6b0014),
[Points::PcdWriter::write()](../../df/dc2/classPoints_1_1PcdWriter.html#a29a665c849f6da4f82ba12eb6bf06095),
[CDxfWrite::writeAngularDimBlock()](../../d6/d47/classCDxfWrite.html#a4a915e13347bfc87d7b55859523ab4cd),
[CDxfWrite::writeDiametricDimBlock()](../../d6/d47/classCDxfWrite.html#a1099141d6c71739945175a349d98129c),
[PartGui::DlgExtrusion::writeParametersToFeature()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8d059573a157c9f9128d55b3c9a9fcc1),
[CDxfWrite::writeRadialDimBlock()](../../d6/d47/classCDxfWrite.html#aa7f3fe99f84d1fd3ece63a019ba76dc5),
and
[TechDraw::Vertex::x()](../../dd/db1/classTechDraw_1_1Vertex.html#ae16837213db3b123c3b6988ff563ae04).

## ◆ y

template<class _Precision >

_Precision [Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision
>::y  
---  
  
y-coordinate

Referenced by
[PartGui::DlgRevolution::accept()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a92a90c8ff44e8e2f6774d0713d47bbbd),
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[ReenGui::FitBSplineSurfaceWidget::accept()](../../d9/d48/classReenGui_1_1FitBSplineSurfaceWidget.html#af94ddfaebc20a805f34a94face578ce6),
[CmdSketcherConstrainLock::activated()](../../d9/dc2/classCmdSketcherConstrainLock.html#a337b578fd38e4359b3177138a91a9162),
[CmdSketcherConstrainDistance::activated()](../../d4/de5/classCmdSketcherConstrainDistance.html#a24031613fd513a79165dfec1d75d6ecb),
[CmdSketcherConstrainDistanceY::activated()](../../da/d3d/classCmdSketcherConstrainDistanceY.html#a59b776e3be604ff1686d112c0f82334b),
[CmdSketcherConstrainPerpendicular::activated()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#ae4b39128a2a69168a71c214a6632f6fa),
[CmdSketcherConstrainAngle::activated()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a0d48a74c0960a5a240c1a39137f070a3),
[Base::BoundBox3< _Precision
>::Add()](../../d8/d12/classBase_1_1BoundBox3.html#ac9052e09ea4470fc68fb18b70ac608af),
[Mod.PartDesign.Scripts.FilletArc.Vector::add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[Sketcher::Sketch::addArc()](../../d9/d9b/classSketcher_1_1Sketch.html#adf324f188acc42de614642df2ea5bf66),
[Sketcher::Sketch::addArcOfEllipse()](../../d9/d9b/classSketcher_1_1Sketch.html#a61610930dafc4117e76e06c4e7f2e226),
[Sketcher::Sketch::addArcOfHyperbola()](../../d9/d9b/classSketcher_1_1Sketch.html#a9e105418a52e77f027b25e0568ba2e1f),
[Sketcher::Sketch::addArcOfParabola()](../../d9/d9b/classSketcher_1_1Sketch.html#a34fecada77c068415ee790ff28b3e2af),
[Base::InventorBuilder::addBoundingBox()](../../db/d7f/classBase_1_1InventorBuilder.html#a7fa4b2eb43c7d1a8df907bc949462fec),
[Sketcher::Sketch::addBSpline()](../../d9/d9b/classSketcher_1_1Sketch.html#a01262194178463ad90291725a52eb912),
[Sketcher::SketchObject::addCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#a2ae92a618d60a264ed20d7a359b89f98),
[Sketcher::Sketch::addEllipse()](../../d9/d9b/classSketcher_1_1Sketch.html#abed34ded55406512fb2dca3e58cfcde8),
[PartGui::FaceColors::Private::addFacesToSelection()](../../d4/d4b/classFaceColors_1_1Private.html#a9eb1efd1782f31dd3bad393299212f3b),
[MeshCore::MeshFastBuilder::AddFacet()](../../d3/d1d/classMeshCore_1_1MeshFastBuilder.html#a309ce02230a45347d21e2f8a861e9cc6),
[Points::PointsGrid::AddPoint()](../../d1/d4d/classPoints_1_1PointsGrid.html#a3c132db635cb686576c2b85a342891a7),
[MeshCore::MeshPointGrid::AddPoint()](../../dc/de4/classMeshCore_1_1MeshPointGrid.html#a58ee74fcf8e6719b3633d5329c06604a),
[Gui::SelectionSingleton::addSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a90a0ee6e4826630e0e35ba1deb5e98fa),
[Base::Builder3D::addSingleArrow()](../../d6/d1b/classBase_1_1Builder3D.html#a000b4d9d1342d22dcb7c0ded96ad45b2),
[Base::InventorBuilder::addSingleArrow()](../../db/d7f/classBase_1_1InventorBuilder.html#a075ebfc1e2f098e0e0bcf104b3cbb916),
[Base::Builder3D::addSingleLine()](../../d6/d1b/classBase_1_1Builder3D.html#accf2a8116bd1142069e93a4eac808d7b),
[Base::InventorBuilder::addSingleLine()](../../db/d7f/classBase_1_1InventorBuilder.html#a404c84909791311b5fe386216c074d65),
[Base::InventorBuilder::addSinglePlane()](../../db/d7f/classBase_1_1InventorBuilder.html#a7b3b6c4b92eb6b42f4ceab91ad24bc43),
[Base::Builder3D::addSingleTriangle()](../../d6/d1b/classBase_1_1Builder3D.html#a536ca5856ad41bf83a85d68af4ec5f68),
[Base::InventorBuilder::addSingleTriangle()](../../db/d7f/classBase_1_1InventorBuilder.html#aa559cd33d73da4c7f081923dd5c9ea51),
[Sketcher::SketchObject::addSymmetric()](../../d9/dad/classSketcher_1_1SketchObject.html#afcbb1d6f5a99e52a70fdf6d9d3c9d361),
[Base::Builder3D::addTransformation()](../../d6/d1b/classBase_1_1Builder3D.html#ac722adc9f5581af07ee4fb411e5bb7f5),
[Base::InventorBuilder::addTransformation()](../../db/d7f/classBase_1_1InventorBuilder.html#a6a994fa52660b07970bb2d9213f0257c),
[MeshCore::MeshTopoAlgorithm::AdjustEdgesToCurvatureDirection()](../../d6/d22/classMeshCore_1_1MeshTopoAlgorithm.html#a9d434d84a9f0707b8c6ca3b4c35a0c26),
[TechDraw::DrawLeaderLine::adjustLastSegment()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#af9979a970967304c97ce041e0bda2cfc),
[TechDraw::DrawUtil::angleWithX()](../../da/d23/classTechDraw_1_1DrawUtil.html#a5a709f9c1aa24f2f0de8ea18771b882b),
[TechDraw::Generic::apparentInter()](../../dd/d23/classTechDraw_1_1Generic.html#a324a686052aad81c15c53f46d663e40b),
[CmdSketcherConstrainLock::applyConstraint()](../../d9/dc2/classCmdSketcherConstrainLock.html#aa27c938f88973099b74d9474476d4254),
[CmdSketcherConstrainDistance::applyConstraint()](../../d4/de5/classCmdSketcherConstrainDistance.html#a9c0f733b397d4f7e05af5f7c70f9debb),
[CmdSketcherConstrainDistanceY::applyConstraint()](../../da/d3d/classCmdSketcherConstrainDistanceY.html#a2df22f90384fbde7d951992c9564d3ad),
[CmdSketcherConstrainPerpendicular::applyConstraint()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#aa62bab542b8f016bd752fdef90110778),
[CmdSketcherConstrainAngle::applyConstraint()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a5602881a59f6c0a0a83a30641560aeb7),
[FemGui::ViewProviderFemMesh::applyDisplacementToNodes()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a2d65b42122fa5ff20cdd2cb783b7e8c5),
[TechDraw::DrawProjGroupItem::autoPosition()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#aed7c8d696a4a2b4f3a172ebc3789cbf7),
[TechDrawGui::QGIViewBalloon::balloonLabelDragFinished()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a287e2445be0351ce418e50714a807ea4),
[Base::BoundBox3< _Precision
>::BoundBox3()](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38),
[TechDraw::DrawUtil::boxIntersect2d()](../../da/d23/classTechDraw_1_1DrawUtil.html#a394f9eed54ca909914560d4a3bfc09d3),
[TechDraw::BSpline::BSpline()](../../d6/d09/classTechDraw_1_1BSpline.html#ab0d19db0c31b1dd84f5bdefcb2303443),
[TechDraw::CenterLine::calcEndPoints()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a34df15a8a959516ecc49512c3ec5a73c),
[TechDraw::CenterLine::calcEndPoints2Lines()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a54d1cc5e3f8aa8923c2c28bdbe25c262),
[TechDraw::CenterLine::calcEndPoints2Points()](../../d5/dd5/classTechDraw_1_1CenterLine.html#aedb72634306a11f9eb49ffac16eb7e2b),
[TechDraw::CenterLine::calcEndPointsNoRef()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ac096a3e174023e9aa7efaab88e4df343),
[MeshGui::ViewProviderMeshTransformDemolding::calcNormalVector()](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#ac95395413a936658e653faa60c9a3795),
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[TechDraw::CenterLine::CenterLine()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ae57d1c63055e3adaa4d445554084481e),
[MeshCore::MeshGeomFacet::CenterOfCircumCircle()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#afa4800556683c823c6e8a947b0f6b26d),
[MeshCore::MeshGeomFacet::CenterOfInscribedCircle()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#af8a76150bc765b0331bc42004f012cb9),
[DraftGui.DraftToolBar::changeYValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a245f69442c47aa69844d30313e68b2b7),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[MeshCore::MeshAlgorithm::CheckFacets()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#ac8032a5a0a06cee43035edcb9253b731),
[Sketcher::SketchAnalysis::checkHorizontal()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a81ee6f119f2454e26c9ec3df9cee9e5a),
[MeshCore::MeshGrid::CheckPosition()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a93306eb31fbf0f2fd27f197bf226ba83),
[Sketcher::SketchAnalysis::checkVertical()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a6f9e55182f9d529c50ea27bdacfe739f),
[PathScripts.PathInspect.GCodeEditorDialog::cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[TechDrawGui::TaskRichAnno::commonFeatureUpdate()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ab5a728afdf435f4c1631b56211559576),
[PartDesign::FeatureExtrude::computeDirection()](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a3af51bee887de0bc89953128cb0a4d1c),
[Part::Extrusion::computeFinalParameters()](../../db/d6c/classPart_1_1Extrusion.html#a4b4ddc216eb6449e2b21480a430f5df8),
[MeshCore::MeshCurvature::ComputePerVertex()](../../d3/d7e/classMeshCore_1_1MeshCurvature.html#a8b29abff540cab896736a08bbb74189f),
[TechDraw::CosmeticEdge::CosmeticEdge()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a6e49936bd5b7832d1024b04c2399095f),
[TechDrawGui::TaskRichAnno::createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[Part::createFilletGeometry()](../../d2/db9/namespacePart.html#a4e47966fd6c762b34824b98614b76541),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[Import::ExportOCAF::createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[Mod.PartDesign.Scripts.FilletArc.Vector::cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[cSimTool::cSimTool()](../../d3/d31/classcSimTool.html#a3b1d2577bcdde16048e83c1c5c75621c),
[TechDrawGui::QGIFace::dashedPPath()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#ac893b16b4130c990b40e45750d31b9a9),
[FemGui::TaskCreateNodeSet::DefineNodes()](../../da/d68/classFemGui_1_1TaskCreateNodeSet.html#a6bd7d00ad2d337fbb90c45d927e80c71),
[MeshCore::MeshInfo::DetailedEdgeInfo()](../../d3/d42/classMeshCore_1_1MeshInfo.html#aae041af175b0080900634a908c05a0c8),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[Base::CoordinateSystem::displacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970),
[TechDraw::DrawViewDimension::dist2Segs()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#abf50565454fb7688d30f946052010504),
[Base::Vector3< double
>::DistanceToLine()](../../d1/d13/classBase_1_1Vector3.html#af38176c3192c969e1ae2255a84885b8a),
[MeshCore::MeshGeomFacet::DistanceToLineSegment()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a275420989c96287043bc6b9ae1232111),
[MeshCore::MeshGeomFacet::DistanceToPoint()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a58f664bc14e352bdd067e05688d20910),
[PathScripts.PostUtils.GCodeEditorDialog::done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Base::Vector3< _Precision
>::Dot()](../../d1/d13/classBase_1_1Vector3.html#a876a8620ec4213d4bc580190328ad899),
[Mod.PartDesign.Scripts.FilletArc.Vector::dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[TechDrawGui::QGIViewBalloon::drawBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6d26eb06a692339e02c1b57545903f29),
[SketcherGui::EditModeConstraintCoinManager::drawConstraintIcons()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a20c4280c68dc704bd2652d6097b0383a),
[TechDrawGui::QGIViewPart::drawSectionLine()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a513e571f325b7c7cac09bdec0d1c512d),
[TechDraw::GeometryUtils::edgeFromGeneric()](../../d5/d83/classTechDraw_1_1GeometryUtils.html#a06fdb57b76577f20da4b79ab357aac24),
[TechDrawGui::execHoleCircle()](../../dc/de6/namespaceTechDrawGui.html#a300c7a5c7d4f155d1349be760b7bb42c),
[PartDesign::Pad::execute()](../../d9/d14/classPartDesign_1_1Pad.html#a17b37a5aaa299709fbb066564ef25b3e),
[PartDesign::Pocket::execute()](../../d1/d89/classPartDesign_1_1Pocket.html#aac791837d2ea389e30768f0fb6d25935),
[Drawing::ProjectionAlgos::execute()](../../db/d32/classDrawing_1_1ProjectionAlgos.html#a014d5c556a4982a188e47e4e713ff883),
[Part::Mirroring::execute()](../../dc/dac/classPart_1_1Mirroring.html#aed38846265cf2381aae85d15dfb74be7),
[PartDesign::Hole::execute()](../../dd/dd0/classPartDesign_1_1Hole.html#ad3161d80bf31dc136534283281a5b3ad),
[TechDraw::ProjectionAlgos::execute()](../../dd/d7c/classTechDraw_1_1ProjectionAlgos.html#a014d5c556a4982a188e47e4e713ff883),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[Import::ImpExpDxfWrite::exportAngularDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a020d31516ae6342bc1160de1daabf79a),
[Import::ImpExpDxfWrite::exportDiametricDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#abb723df58a935f6b0590238bc09f7ad5),
[Import::ImpExpDxfWrite::exportLinearDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a469a35bb67d953bd7fc2193a70efa083),
[Import::ImpExpDxfWrite::exportRadialDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#aeccef9eee470f21a95169ed063af94e4),
[Import::ImpExpDxfWrite::exportText()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#aa372554ea19f3fd6ff21c048f8bef37c),
[Sketcher::SketchObject::exposeInternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a7d89f466b41e7479505e70c73d832428),
[TechDrawGui::QGISectionLine::extensionEndsISO()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#accfe95859edaa0110e334d22821ccd0b),
[TechDrawGui::QGISectionLine::extensionEndsTrad()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#a1f6e235dee697a90a21888b0eca7f520),
[Mesh::Facet::Facet()](../../d7/d79/classMesh_1_1Facet.html#aed4f45fccca652d2000ff55e1a06583c),
[Fem::FemPostDataAlongLineFilter::FemPostDataAlongLineFilter()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ac595ec7511d8d0a5111b5461ef0fa446),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[Part::find2DLinesIntersection()](../../d2/db9/namespacePart.html#a0dd46c09269433a805588c348a585bb0),
[TechDraw::LineSet::findAtomStart()](../../d7/d2f/classTechDraw_1_1LineSet.html#ad2bdafb64d48697d2072a07e8ad921e2),
[MeshCoreFit::CylinderFit::findBestSolDirection()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a6e0db1db743acde2daf19bc60f9d1e0c),
[Part::findFilletCenter()](../../d2/db9/namespacePart.html#ab01c47ee6de2dab1626ab457c264b394),
[MeshCore::CylinderFit::Fit()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a2b728f7c295c98d85f6159610ff36bc4),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[VisualPathSegmentVisitor::g38()](../../de/d18/classVisualPathSegmentVisitor.html#aefd30507eff704570080c7fe03b6d11d),
[PartDesign::Helix::generateHelixPath()](../../d3/d78/classPartDesign_1_1Helix.html#a04dd9590e1c0afe9dd3f1066ab9f0395),
[Part::GeomLine::GeomLine()](../../d5/d30/classPart_1_1GeomLine.html#a5a8457c1f4e91bf66c8070d86eb9887a),
[TechDrawGui::QGIViewPart::geomToPainterPath()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#aea20fa3e1100ec52240032c108712790),
[TechDrawGui::TaskDetail::getAnchorScene()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ac47e200bf1be3381e59b3c6c4610494d),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[Fem::Constraint::getBasePoint()](../../d0/d11/classFem_1_1Constraint.html#a53b58263b54f9ab82afbc002761ccd24),
[TechDraw::DrawViewSection::getCSFromBase()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a761c0e9c4fe742ad0f6250428875ecd4),
[TechDrawGui::QGEPath::getDeltasFromLeader()](../../d9/da7/classTechDrawGui_1_1QGEPath.html#a59c9f7dddcda624bf7724c39938353f2),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[MeshCoreFit::CylinderFit::GetDistanceToCylinder()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a7e37395d2a64271694828d763d1582d4),
[MeshCoreFit::SphereFit::GetDistanceToSphere()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#aca8b41099e947b212fee4dd15118fb69),
[Mesh::MeshObject::getEigenSystem()](../../d8/dcc/classMesh_1_1MeshObject.html#a786294ab69d0aedecf59d3d3fb208d80),
[MeshCore::MeshKernel::GetGravityPoint()](../../dd/d95/classMeshCore_1_1MeshKernel.html#a0cce71449b9303e9e2509487f487b290),
[MeshCore::CylinderFit::GetInitialAxisFromNormals()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a94896bef3d7356707b274d1d34c101f4),
[TechDrawGui::QGIWeldSymbol::getKinkPoint()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a369b5176e262931bc83085510cc7a0b9),
[MeshCore::PlaneFit::GetLocalPoints()](../../db/dab/classMeshCore_1_1PlaneFit.html#afea00501e51e679c09dc7ca9064d4555),
[Part::Feature::getLocation()](../../d7/d7e/classPart_1_1Feature.html#a84164b4adfe9b6ecef87da8d7aa1ac9d),
[Part::FeatureReference::getLocation()](../../d2/da1/classPart_1_1FeatureReference.html#aee6f4d426e17d5a0193108fd06f7309c),
[Base::BoundBox3< _Precision
>::GetOctantFromVector()](../../d8/d12/classBase_1_1BoundBox3.html#ae68b2abe794808185a01fd6cb01fad42),
[MeshGui::PlaneFitParameter::getParameter()](../../da/d31/classMeshGui_1_1PlaneFitParameter.html#acc96292a875e15e9e792e59994f02a71),
[MeshGui::CylinderFitParameter::getParameter()](../../d6/d6d/classMeshGui_1_1CylinderFitParameter.html#ab93a68400083131e275c6f9d3af94fab),
[TechDraw::LineSet::getPatternStartPoint()](../../d7/d2f/classTechDraw_1_1LineSet.html#aba20266c9fd3898beef7917120751246),
[Mesh::MeshObject::getPoint()](../../d8/dcc/classMesh_1_1MeshObject.html#a3b5cfb389c3be7ecad0809494f54418d),
[Mesh::MeshObject::getPointNormal()](../../d8/dcc/classMesh_1_1MeshObject.html#ab3953ee00afa96512b922acb9ea5ec12),
[Mesh::MeshObject::getPointNormals()](../../d8/dcc/classMesh_1_1MeshObject.html#a16c59852a6633307010cc619c4d10143),
[Mesh::MeshObject::getPoints()](../../d8/dcc/classMesh_1_1MeshObject.html#a4b7287613ca9dbab79d581af2a0632e6),
[TechDraw::DrawViewPart::getProjectionCS()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ae1dd72b98fa563bf72d6c39f49577632),
[Base::Rotation::getRawValue()](../../d4/d18/classBase_1_1Rotation.html#afe860f0bcfaec728e99861e4c65904aa),
[PartDesignGui::ViewProviderDatum::getRelevantBoundBox()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a8437c5be88154b9cb0bd2bae5ef94db3),
[TechDraw::DrawViewSection::getSectionCS()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aefc378d8464959b191ac4ff96f6bca12),
[Base::BoundBox3< _Precision
>::GetSideFromRay()](../../d8/d12/classBase_1_1BoundBox3.html#a900e54e09a7e5ba1909a10a0d83c40ea),
[TechDrawGui::QGIWeldSymbol::getTailPoint()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a2699319ad36e2b727f54a1a4e3268c7c),
[TechDrawGui::QGIWeldSymbol::getTileOrigin()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a1ac4c88fab7e971e0ab980b801c91f3e),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[MeshCore::AbstractPolygonTriangulator::GetTransformToFitPlane()](../../d9/d6e/classMeshCore_1_1AbstractPolygonTriangulator.html#aaaa240d0f1a906bdc7cc01c81dea9250),
[TechDraw::DrawGeomHatch::getTrimmedLinesSection()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a2fe5d2f18fe5801e37a1cfdb967fbce3),
[Gui::LocationWidget::getUserDirection()](../../d9/d9a/classGui_1_1LocationWidget.html#a928aeb60d1d1a95d4d336c6901fb950b),
[Gui::LocationDialog::getUserDirection()](../../dc/d22/classGui_1_1LocationDialog.html#aa52301a6aec2f1b750929d7444765c33),
[Base::Rotation::getValue()](../../d4/d18/classBase_1_1Rotation.html#af95c57a06636f68b2a6cc779dc042edd),
[TechDraw::DrawProjGroupItem::getViewAxis()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a66cab4b4ebd52d41889c7fdb9c854821),
[TechDraw::getViewAxis()](../../d7/d31/namespaceTechDraw.html#ad612c2d90cb50e87312099ea9824c509),
[MeshCore::MeshKernel::GetVolume()](../../dd/d95/classMeshCore_1_1MeshKernel.html#a919704318d645c2a0d30cd9fa2203439),
[Fem::FemMesh::getVolume()](../../d3/d2e/classFem_1_1FemMesh.html#a86dfe0bdac5ccbc115b39af5780ee2b1),
[Base::Matrix4D::Hat()](../../d5/db4/classBase_1_1Matrix4D.html#ae5b666346437729d9c62741a35497aa7),
[TechDraw::DrawUtil::Intersect2d()](../../da/d23/classTechDraw_1_1DrawUtil.html#afe855bd12c8cea41eb2af19ab79ba99d),
[MeshCore::MeshGeomEdge::IntersectBoundingBox()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#aa33bee65b66dc0904e254e42f20bf02d),
[MeshCore::MeshGeomFacet::IntersectBoundingBox()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0a6b404c351030f6727713ab4b9fa805),
[TechDraw::AOC::intersectsArc()](../../d0/d5c/classTechDraw_1_1AOC.html#a061b7f38a3cd0dca1c8c08a03c7a05fe),
[TechDraw::BSpline::intersectsArc()](../../d6/d09/classTechDraw_1_1BSpline.html#a5af43bc17061b8e8f6598dec030ea659),
[MeshCore::MeshGeomFacet::IntersectWithFacet()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a4324352edc96819d5ce83009cd1ed2df),
[Base::BoundBox3< _Precision
>::IntersectWithLine()](../../d8/d12/classBase_1_1BoundBox3.html#aa1b97e4eab9eecfd4711d01a3b9ed533),
[MeshCore::MeshGeomFacet::IntersectWithPlane()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a1a60849171e88c8fcf54e341b36a56eb),
[Gui::ViewVolumeProjection::inverse()](../../d8/d4d/classGui_1_1ViewVolumeProjection.html#a1d7fe268b671119971278bdf467133f2),
[Base::BoundBox3< _Precision
>::IsCutLine()](../../d8/d12/classBase_1_1BoundBox3.html#a55a718fe21f7a5240ac7b6651b4c5822),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#a755404902a0ec9b28e954657ba887307),
[cSimTool::isInside()](../../d3/d31/classcSimTool.html#ad2e9adbe06388f51b1ba05025d6021a3),
[TechDraw::DrawViewPart::isIso()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#af3b5d2ae674b8b2b423edc3b12833e29),
[Sketcher::SketchObject::isPointOnCurve()](../../d9/dad/classSketcher_1_1SketchObject.html#a56b81b36bf54912326dbd22750c19e8c),
[TechDraw::legacyViewAxis1()](../../d7/d31/namespaceTechDraw.html#a6c5c5a402ebdc68e1048cb62d6ef595f),
[Mod.PartDesign.Scripts.FilletArc.Vector::length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Points::PointsAlgos::LoadAscii()](../../d8/d62/classPoints_1_1PointsAlgos.html#a75d94f79566c5ebb47f14fbafa6be26e),
[MeshCore::MeshInput::LoadInventor()](../../d9/d08/classMeshCore_1_1MeshInput.html#acf19f4238be1fd7d9f3b260af125d599),
[MeshCore::MeshInput::LoadPLY()](../../d9/d08/classMeshCore_1_1MeshInput.html#a8f60cc2825d0ffd59075b0892d92417b),
[PartGui::Location::Location()](../../db/d6f/classPartGui_1_1Location.html#a2f77946d77e8f18590ccf3f7e73a18b4),
[MeshPart::MeshAlgos::LoftOnCurve()](../../db/d67/classMeshPart_1_1MeshAlgos.html#af6d0bd2cf1dd2ca04dfb7a7f853f2aba),
[TechDrawGui::QGISectionLine::makeArrowsISO()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#a8f2cce08f6be3eb56a19c7de258ea884),
[TechDrawGui::QGISectionLine::makeArrowsTrad()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#aaa7b66291c65ca1fd3de5a83aa2cdf68),
[TechDraw::DrawGeomHatch::makeEdgeOverlay()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#ad42d700267fb44056f1c72515659170c),
[TechDrawGui::QGIArrow::makeFilledTriangle()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#a48ea2d959065f7dcddd8bf7f60135e62),
[TechDrawGui::QGIArrow::makeForkArrow()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#af362a5208def60772252b3e36d1d2c9a),
[TechDrawGui::QGIArrow::makeHashMark()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#ad350c362524675d0e695781e60dd6945),
[TechDrawGui::QGIArrow::makeOpenArrow()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#a5846b0a5797ddeebbb25e95297088489),
[PartDesign::Feature::makePlnFromPlane()](../../d7/d51/classPartDesign_1_1Feature.html#a6ab00d23c99b505b5bf57dedac353631),
[TechDrawGui::QGIArrow::makePyramid()](../../d4/d60/classTechDrawGui_1_1QGIArrow.html#aedbc5bfceac71c55af61aa6981121425),
[Base::Rotation::makeRotationByAxes()](../../d4/d18/classBase_1_1Rotation.html#a0b7c436d3243f3703959c7f6be8ecad2),
[TechDrawGui::QGISectionLine::makeSymbolsISO()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#ac20091d52978917cd18aa37c17df9d6c),
[TechDrawGui::QGISectionLine::makeSymbolsTrad()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#ad784a67840ecc73314d932f8c3f523d9),
[SketcherGui::makeTangentToArcOfEllipseviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#ade2d18eb05327cda22e2eb86409e4642),
[SketcherGui::makeTangentToArcOfHyperbolaviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a2d88b81b020ee6003474b180fad75a3b),
[SketcherGui::makeTangentToArcOfParabolaviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a8153db87ad16afe18f0f5e0a01bf5251),
[SketcherGui::makeTangentToEllipseviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a0221a346db6666022488335587d92562),
[Part::Geometry::mirror()](../../dc/df0/classPart_1_1Geometry.html#af5e2f1761b12dcf915ffb3bc9f2e20fe),
[TechDraw::mirrorShapeVec()](../../d7/d31/namespaceTechDraw.html#a94c08edd68671f2042041c91350f1e36),
[DrawSketchHandlerBSplineInsertKnot::mouseMove()](../../d2/df2/classDrawSketchHandlerBSplineInsertKnot.html#a60d07ab6b604aef8674f849e380898ec),
[SketcherGui::DrawSketchHandlerExtend::mouseMove()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#aa7a93c3f3980309d65e4b1ecc9a559d0),
[SketcherGui::DrawSketchHandlerLineSet::mouseMove()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a113e395cf71488043942d51f78b7d167),
[SketcherGui::DrawSketchHandlerTrimming::mouseMove()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a206e252777274a73c12e2a6b51f0ecc9),
[Base::Matrix4D::move()](../../d5/db4/classBase_1_1Matrix4D.html#ac833395bac6936432368efa5595387bd),
[Sketcher::Sketch::movePoint()](../../d9/d9b/classSketcher_1_1Sketch.html#ad66e807fc32460d6686fb708fdb3a69c),
[TechDraw::moveShape()](../../d7/d31/namespaceTechDraw.html#a6984b4017e3ad0b59304844e743f064a),
[Mod.PartDesign.Scripts.FilletArc.Vector::mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector::norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[Gui::Dialog::Transform::on_applyButton_clicked()](../../d0/d8f/classGui_1_1Dialog_1_1Transform.html#aa736a36e69d76427b945f434e46f3a2a),
[Gui::ViewProviderOrigin::onChanged()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[Fem::FemPostDataAlongLineFilter::onChanged()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ae418afcb8e18abba84d16c2a645a434e),
[PathGui::ViewProviderPath::onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PathGui::PathSelectionObserver::onSelectionChanged()](../../db/d77/classPathGui_1_1PathSelectionObserver.html#a647466bb806e71c512362f4dafc43e7b),
[Base::Vector3< _Precision
>::operator&()](../../d1/d13/classBase_1_1Vector3.html#ab377fb85d034e0486a08805cdf56b629),
[Base::operator*()](../../db/d07/namespaceBase.html#ac7d409d67697b8ea931e0febfe6e26de),
[Base::Matrix4D::operator*()](../../d5/db4/classBase_1_1Matrix4D.html#ab8a45ff4ced15d460ae0b11239629d52),
[Base::Vector3< _Precision
>::operator+()](../../d1/d13/classBase_1_1Vector3.html#a217bd5ebf8797d0930fda829c3f1698f),
[Base::Vector3< _Precision
>::operator-()](../../d1/d13/classBase_1_1Vector3.html#ab8cca8856cabb105f7e2d002078776e4),
[MeshCore::MeshPoint::operator<()](../../dd/db5/classMeshCore_1_1MeshPoint.html#af48745635582de4c6c517382120f6440),
[PathScripts.PathDressupHoldingTags.Tag::originAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aa1cbd48305f117e5197555822fd45f3f),
[DrawingGui::orthoview::orthoview()](../../db/df8/classDrawingGui_1_1orthoview.html#afc8be37cc7e9325e722e05f2736af13d),
[Base::Matrix4D::Outer()](../../d5/db4/classBase_1_1Matrix4D.html#a8e19dc5e655bc920f9527c62c1ecf7aa),
[MeshCore::PlaneSurfaceFit::Parameters()](../../d9/df5/classMeshCore_1_1PlaneSurfaceFit.html#a2c0e5c7c7155ea8eb77c28af1589c1b4),
[MeshCore::CylinderSurfaceFit::Parameters()](../../d1/d68/classMeshCore_1_1CylinderSurfaceFit.html#a77a6a4645558df8448d8284ebe34417b),
[MeshGui::SoFCMeshPickNode::pick()](../../d1/d1b/classMeshGui_1_1SoFCMeshPickNode.html#ac140e23964b3171e35ff15585cd3ba14),
[Attacher::AttachEngine::placementFactory()](../../d2/d85/classAttacher_1_1AttachEngine.html#a0eff77539401a8d4a04554a970bd85b4),
[TechDraw::Vertex::point()](../../dd/db1/classTechDraw_1_1Vertex.html#a6556cf8e5cd0a2fbca8198ee0e06edc8),
[DraftGui.DraftToolBar::pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[MeshCore::SurfaceFit::PolynomFit()](../../d2/d9a/classMeshCore_1_1SurfaceFit.html#a7dc8000c3b6f4bcae7320a4c8a48d489),
[Points::PointsGrid::Pos()](../../d1/d4d/classPoints_1_1PointsGrid.html#aaa5c87982921d2673a7ac3227d2b6714),
[Inspection::MeshInspectGrid::Pos()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#ad94d0cf1a82a11f6b649619db7e1f5e3),
[MeshCore::MeshFacetGrid::Pos()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#ade0d241d31a50d7dd2be2defca3acc1e),
[MeshCore::MeshPointGrid::Pos()](../../dc/de4/classMeshCore_1_1MeshPointGrid.html#a5780dcbbe5bda437bf2b11407cf4c4bb),
[Points::PointsGrid::Position()](../../d1/d4d/classPoints_1_1PointsGrid.html#a5dc29f08827b2e5b849da258c39e0b49),
[MeshCore::MeshGrid::Position()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a8b0dcdb55de3e3c2f8bce7e3a618c0a9),
[MeshCore::MeshFacetGrid::PosWithCheck()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#a59cc6fc0efed46133e4b0580b5fe4ac8),
[SketcherGui::EditModeConstraintCoinManager::processConstraints()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a86abd481aa8756c9ea61b10d2e624804),
[Base::BoundBox3< _Precision
>::ProjectBox()](../../d8/d12/classBase_1_1BoundBox3.html#a4d8b86292716416ed2151d4190291ad1),
[Reen::ParameterCorrection::ProjectControlPointsOnPlane()](../../dd/d71/classReen_1_1ParameterCorrection.html#a54d70272eced8a72c72f8c11a11ac568),
[MeshPart::CurveProjectorSimple::projectCurve()](../../db/d5f/classMeshPart_1_1CurveProjectorSimple.html#a5932b3a0d0a1ee7119cc7f7b5f180ef8),
[MeshPart::CurveProjectorShape::projectCurve()](../../dc/d83/classMeshPart_1_1CurveProjectorShape.html#a78cb49a17db5b6adcb772e9589d32580),
[MeshPart::MeshProjection::projectEdgeToEdge()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#a322496a26bba88d2ff370beef12fdc3b),
[TechDraw::DrawViewPart::projectPoint()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#afbe98e95b0bd7b0cec45b29d29ce46b2),
[TechDraw::LandmarkDimension::projectPoint()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a55be6d3789c069c9509a7ae087324d99),
[MeshCoreFit::SphereFit::ProjectToSphere()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#ad019d88b25f67f7893cdf7179f1cd6c5),
[CDxfWrite::putArrow()](../../d6/d47/classCDxfWrite.html#af14654282595c1d9d2a47b4ac6427bbb),
[CDxfWrite::putText()](../../d6/d47/classCDxfWrite.html#a5af170abde99f5eebff5afac269622fd),
[Points::E57Reader::read()](../../d2/dfb/classPoints_1_1E57Reader.html#a7af6bb0bc50ff56c203f0cb0aa04d458),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[Path::Toolpath::recalculate()](../../d6/d0c/classPath_1_1Toolpath.html#a6fcb5afb3f1023ef686cd87b4f69c0f9),
[PathGui::ViewProviderPath::recomputeBoundingBox()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a4a681a533fc16dba93a80bc3fdfc21c3),
[SketcherGui::DrawSketchHandlerExtend::releaseButton()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#a3e947849d6dc89b7f93e87a1ebd9b160),
[DraftGui.DraftToolBar::reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[TechDraw::CosmeticVertex::Restore()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a11aa1f69e9211c240d61949a237056a1),
[TechDraw::CenterLine::Restore()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
[TechDraw::Vertex::Restore()](../../dd/db1/classTechDraw_1_1Vertex.html#a8db190000b0c2b933006ee8c4d94f511),
[TechDraw::Circle::Restore()](../../d3/d63/classTechDraw_1_1Circle.html#a0c95eda08d536f7de7c3a3abb3007e76),
[TechDraw::AOC::Restore()](../../d0/d5c/classTechDraw_1_1AOC.html#a6adb7fceabe6a5089727723cff4b2760),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::Geometry::rotate()](../../dc/df0/classPart_1_1Geometry.html#a3c7ebf21592da6737fccb28bf9508a75),
[TechDraw::DrawViewSection::rotateCSArbitrary()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a66a852d7e827780ebf6e1d46439d49e2),
[Base::Vector3< _Precision
>::RotateX()](../../d1/d13/classBase_1_1Vector3.html#ae4b74aa1b2b0b0b8a3919f337dd680f6),
[Base::Vector3< _Precision
>::RotateZ()](../../d1/d13/classBase_1_1Vector3.html#af09471673c2fde5a6ef612c1e7f8b9b1),
[Base::Matrix4D::rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aff3583443a5de61928925fa6b8af6f21),
[PartDesign::Helix::safePitch()](../../d3/d78/classPartDesign_1_1Helix.html#a85474d1c32f51cf49c0be48c600993eb),
[Part::GeomLine::Save()](../../d5/d30/classPart_1_1GeomLine.html#a88fd00890c6c4e7729b05c279a64656d),
[Part::GeomLineSegment::Save()](../../d9/d6f/classPart_1_1GeomLineSegment.html#acc377c70086de1bfbfd88e523b663529),
[Robot::Robot6Axis::Save()](../../dc/d5f/classRobot_1_1Robot6Axis.html#a7cf092c9dc75bf16fe3b6a01d9fa03d4),
[Robot::Waypoint::Save()](../../d1/dc7/classRobot_1_1Waypoint.html#a2d0f51a0e8e89f1148887af8e2eb0537),
[TechDraw::CosmeticVertex::Save()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#aee8e2101aa119ae2dc4750442745264c),
[TechDraw::CenterLine::Save()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[TechDraw::Vertex::Save()](../../dd/db1/classTechDraw_1_1Vertex.html#aed3011b8fc0de22659800304c3f1b0af),
[TechDraw::Circle::Save()](../../d3/d63/classTechDraw_1_1Circle.html#ab3a64b9c96ec1f8dc658f0432955bfa5),
[TechDraw::AOC::Save()](../../d0/d5c/classTechDraw_1_1AOC.html#a4627154c0a8d5886ee4ee54231107de2),
[App::PropertyPlacement::Save()](../../da/d51/classApp_1_1PropertyPlacement.html#ae1314101350bc9e76b9d692693c8e9e1),
[App::PropertyRotation::Save()](../../df/d76/classApp_1_1PropertyRotation.html#ad9e882ab49bd192e84f62de9a64c62ce),
[MeshCore::MeshOutput::Save3MFModel()](../../db/d14/classMeshCore_1_1MeshOutput.html#a37bb55249af3cbca138ae4536bf71325),
[MeshCore::MeshOutput::SaveAsciiPLY()](../../db/d14/classMeshCore_1_1MeshOutput.html#a4f5628a8d90a67d09484426b71f30a6a),
[MeshCore::MeshOutput::SaveAsciiSTL()](../../db/d14/classMeshCore_1_1MeshOutput.html#a978a9f0a89ca5ce4d828305f005de62b),
[MeshCore::MeshOutput::SaveAsymptote()](../../db/d14/classMeshCore_1_1MeshOutput.html#a31276c848ed13571a0e7f6f932e5a45e),
[MeshCore::MeshOutput::SaveBinaryPLY()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3f47cee51e773e3eb9310e1bf3ed8bf8),
[MeshCore::MeshOutput::SaveBinarySTL()](../../db/d14/classMeshCore_1_1MeshOutput.html#aa319df520ea268406d3a19a1c4a4f198),
[MeshCore::MeshOutput::SaveIDTF()](../../db/d14/classMeshCore_1_1MeshOutput.html#ad297d3f6095f421beb22932929190fbb),
[MeshCore::MeshOutput::SaveMeshNode()](../../db/d14/classMeshCore_1_1MeshOutput.html#a77cd49917f9394aadcd355c5247546f0),
[MeshCore::MeshOutput::SaveNastran()](../../db/d14/classMeshCore_1_1MeshOutput.html#a832d24717641893b591f5b4d99db9e3f),
[MeshCore::MeshOutput::SaveOBJ()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3d771358cea3ae77d666c54aba2692b5),
[MeshCore::MeshOutput::SaveOFF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8b4f5b020dd2b94b087ff831b7aee3c4),
[Import::ExportOCAF::saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[MeshCore::MeshOutput::SaveSMF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a7b44d31efb50a5d64b2b08fbcc91963f),
[MeshCore::MeshOutput::SaveVRML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8fc229d0641d58846478dbcaa077e8db),
[MeshCore::MeshOutput::SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
[MeshCore::MeshOutput::SaveXML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8a89241b7984ceab819293e9b7385c20),
[Base::Matrix4D::scale()](../../d5/db4/classBase_1_1Matrix4D.html#a3121f149e2b6034c29235b776f44989b),
[TechDraw::CenterLine::scaledGeometry()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a104bfe6bf49d7b364f65000352e670ea),
[MeshCore::MeshAlgorithm::SearchFacetsFromPolyline()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a72f7307406aa5146e43c481b5b3a25d7),
[MeshCore::MeshFacetGrid::SearchNearestFromPoint()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#afbb767d3a8804d125b5d7b80db72d471),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[TechDraw::DrawViewSection::sectionExec()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a79c8f60f63dd54684af4cad42f91ee4e),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
[Part::Part2DObject::seekTrimPoints()](../../d9/d57/classPart_1_1Part2DObject.html#a7f5beeba90cfa4cdf7a72f7827bae9f1),
[Part::GeomConic::setCenter()](../../d1/d86/classPart_1_1GeomConic.html#a0ef572424983321dada7f64d0aa1a3b9),
[Part::GeomArcOfConic::setCenter()](../../db/d48/classPart_1_1GeomArcOfConic.html#a8a2755a6bbbed714049540421198bb8a),
[MeshPartGui::ViewProviderCrossSections::setCoords()](../../dc/dfe/classMeshPartGui_1_1ViewProviderCrossSections.html#acdea9634b2faaa0d83425fd4ede721c7),
[PartGui::ViewProviderCrossSections::setCoords()](../../d8/df0/classPartGui_1_1ViewProviderCrossSections.html#a5e651bd86ec7aa11c84537275b1af31d),
[PartGui::DlgExtrusion::setDir()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a0519f8635962170f77bf009e2071a389),
[PartGui::DlgRevolution::setDirection()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a4df42abdf4af0ef46cb8cfcdca995c9c),
[Gui::LocationWidget::setDirection()](../../d9/d9a/classGui_1_1LocationWidget.html#a2af475de798c64df6995f659a2e7ab40),
[Gui::LocationUi< Ui
>::setDirection()](../../db/da1/classGui_1_1LocationUi.html#a13961053ead815e1adb59564608b8b8a),
[Gui::LocationImpUi< Ui
>::setDirection()](../../df/d30/classGui_1_1LocationImpUi.html#a95f67606fb3dbaab6d199980cb091c63),
[RobotGui::ViewProviderRobotObject::setDragger()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a7a94208ad67ec05ebc9013cac68d34f4),
[Path::Command::setFromPlacement()](../../d7/d2e/classPath_1_1Command.html#a62372d49bbf1003cc81fe7035c7b592e),
[Part::GeomLine::setLine()](../../d5/d30/classPart_1_1GeomLine.html#a602d118b05d480b3f1df2c16f9129bab),
[Part::GeomConic::setLocation()](../../d1/d86/classPart_1_1GeomConic.html#af9bbec6989f1ae76e3e6cff0fb02a05a),
[Part::GeomArcOfConic::setLocation()](../../db/d48/classPart_1_1GeomArcOfConic.html#a1f2b7ce2d1b354cda0ed3c33275d6ec6),
[Part::GeomEllipse::setMajorAxisDir()](../../db/d52/classPart_1_1GeomEllipse.html#a05d29bbfe1e80f91559e12fb8b2cfc36),
[Part::GeomArcOfEllipse::setMajorAxisDir()](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#acb1e2d5a06a4a7b7e8d8ddee835e11b4),
[Part::GeomArcOfHyperbola::setMajorAxisDir()](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#a59725dadb45c4d7afd0562b646c36f79),
[TechDraw::DrawViewBalloon::setOrigin()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a4976c3df5bccf5549523c6960c912624),
[App::PropertyVector::setPyObject()](../../d5/d2b/classApp_1_1PropertyVector.html#a4e4eae3cb50d20fece89b7aac9fa6324),
[Part::TopoShape::setShapePlacement()](../../d8/ded/classPart_1_1TopoShape.html#a8ae38d04353d5ccc4c60beaad3a4a497),
[Gui::Dialog::Transform::setTransformStrategy()](../../d0/d8f/classGui_1_1Dialog_1_1Transform.html#ae3b140a0d601a95674bcbda4e88aa6d4),
[TechDrawGui::TaskSectionView::setUiEdit()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a43dc3542cf896d0778a028ae2be230ce),
[TechDrawGui::TaskCosmeticLine::setUiEdit()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a99ac5dc7728cfedeee3aedf2b9559791),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[TechDrawGui::TaskSectionView::setUiPrimary()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a07485a3822d8c672d6e4580fe4bf858c),
[TechDrawGui::TaskCosmeticLine::setUiPrimary()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a4b1f902a521e9cd5fdf56889d51e52a3),
[PartDesign::Pipe::setupAlgorithm()](../../da/d61/classPartDesign_1_1Pipe.html#aee88e3fe184997d50ac86c9f99b113f2),
[MeshCoreFit::SphereFit::setupObservation()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#a56ac7d52481e7015dd415262b344b470),
[MeshCoreFit::CylinderFit::setupObservation()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a856fae3fea7c099c0972d1f07a89b8c9),
[Gui::PropertyEditor::PropertyRotationItem::setValue()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a65660d1593a8c2f7dabca98e9464c6cc),
[Gui::PropertyEditor::PropertyPlacementItem::setValue()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a7f8e70acbf194633b6b3422b87a07ab3),
[Base::Rotation::setValue()](../../d4/d18/classBase_1_1Rotation.html#a62c0b4012cb383de60d0e4a225c39550),
[Gui::ManualAlignment::setViewingDirections()](../../d7/d97/classGui_1_1ManualAlignment.html#ad3be3a6882c973db3ae9d21b40a85772),
[Part::GeomArcOfConic::setXAxisDir()](../../db/d48/classPart_1_1GeomArcOfConic.html#afdcf8bd89f0e40ba453289cbf098b364),
[MeshGui::ViewProviderMeshOrientation::showDefects()](../../d1/d8e/classMeshGui_1_1ViewProviderMeshOrientation.html#acad074355a307b6f0e8059ae22ba8d54),
[MeshGui::ViewProviderMeshNonManifolds::showDefects()](../../d5/d95/classMeshGui_1_1ViewProviderMeshNonManifolds.html#aa021d71ade5620d8dc36c94220862be8),
[MeshGui::ViewProviderMeshNonManifoldPoints::showDefects()](../../d6/d60/classMeshGui_1_1ViewProviderMeshNonManifoldPoints.html#ad648ec1aee86628d91e6aec48eafaa42),
[MeshGui::ViewProviderMeshDuplicatedFaces::showDefects()](../../d1/d9b/classMeshGui_1_1ViewProviderMeshDuplicatedFaces.html#a435c5361ffb8312295cc076da55d56a8),
[MeshGui::ViewProviderMeshDegenerations::showDefects()](../../d2/da9/classMeshGui_1_1ViewProviderMeshDegenerations.html#a954810db894668aaea3d6a26f310f2ea),
[MeshGui::ViewProviderMeshDuplicatedPoints::showDefects()](../../d5/d26/classMeshGui_1_1ViewProviderMeshDuplicatedPoints.html#af52e3e5a78f9c0ecceab7bb945b1c075),
[MeshGui::ViewProviderMeshIndices::showDefects()](../../dd/d71/classMeshGui_1_1ViewProviderMeshIndices.html#abcb21eec9d9285a3d13ee103e03beaaa),
[MeshGui::ViewProviderMeshFolds::showDefects()](../../d8/d06/classMeshGui_1_1ViewProviderMeshFolds.html#a1a9474aafd32ff0b730a7c795a8fc5e9),
[MeshGui::ViewProviderMeshNode::showOpenEdges()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a7db6427662808c81110a3efc5e523064),
[Part::TopoShape::slice()](../../d8/ded/classPart_1_1TopoShape.html#af54879971e721f27d014b938a1b57eb3),
[Part::TopoShape::slices()](../../d8/ded/classPart_1_1TopoShape.html#a808f0de39292b4e84445ed75b263852e),
[MeshCore::PlaneFitSmoothing::Smooth()](../../d4/d74/classMeshCore_1_1PlaneFitSmoothing.html#a8c02774a72bb114362c993f51dc0d7ec),
[MeshCore::PlaneFitSmoothing::SmoothPoints()](../../d4/d74/classMeshCore_1_1PlaneFitSmoothing.html#aa6fba7b76ab58215430b86da7dec700d),
[Sketcher::SketchObject::split()](../../d9/dad/classSketcher_1_1SketchObject.html#ab73e7a53a704168c004b9aa6c9ad7a68),
[Mod.PartDesign.Scripts.FilletArc.Vector::sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[Part::suggestFilletRadius()](../../d2/db9/namespacePart.html#a1903069f8259f815f24930b78481a785),
[FemGui::TaskPostDataAlongLine::TaskPostDataAlongLine()](../../db/dfe/classFemGui_1_1TaskPostDataAlongLine.html#a63d24585168c09609383c5025fc02c61),
[Base::Matrix4D::toAxisAngle()](../../d5/db4/classBase_1_1Matrix4D.html#aebaf3536031474ff723f0a4abd621e55),
[Gui::View3DInventorViewer::toggleClippingPlane()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ae41b2cfdc548e959d744937ff7a85317),
[Gui::PropertyEditor::PropertyRotationItem::toolTip()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#abbb3c671e82d0c8d54f1f6f2b95abe5d),
[Gui::PropertyEditor::PropertyPlacementItem::toolTip()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#add11217c79e909fa0d6a5fa97d739d2f),
[PartGui::Location::toPlacement()](../../db/d6f/classPartGui_1_1Location.html#a3a6283d802f45e675b6ddf9c714c8f47),
[TechDraw::DrawUtil::toR3()](../../da/d23/classTechDraw_1_1DrawUtil.html#adf8b4269fac80cfb6793e8b54873361e),
[Gui::PropertyEditor::PropertyRotationItem::toString()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a13b41010f83aeb8833bf251d9f1a652a),
[Gui::PropertyEditor::PropertyPlacementItem::toString()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a4866bdcbed09d39f47781b1b5aba4cec),
[TechDraw::CosmeticVertex::toString()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#acb9933bf213ddd298b48d573bfa63f2d),
[TechDraw::CenterLine::toString()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a0af372e8042e1f5e9b02fe8d176d38ca),
[TechDraw::Circle::toString()](../../d3/d63/classTechDraw_1_1Circle.html#a61924379310acb95418698663af100f0),
[TechDraw::AOC::toString()](../../d0/d5c/classTechDraw_1_1AOC.html#aad4400a1a3d31738afea85abe57d6917),
[Path::Command::transform()](../../d7/d2e/classPath_1_1Command.html#a86423c625f09285dd820b578462c199e),
[MeshCore::SurfaceFit::Transform()](../../d2/d9a/classMeshCore_1_1SurfaceFit.html#a4e5b025adea5142985b11b1042c8b256),
[Base::Vector3< double
>::TransformToCoordinateSystem()](../../d1/d13/classBase_1_1Vector3.html#a5369dfa0fb3929e42263f871a865324b),
[Data::ComplexGeoData::transformToInside()](../../d8/daf/classData_1_1ComplexGeoData.html#a8b0cc05d2cf2ab2a1bb36e7f2a70949e),
[MeshCore::MeshSearchNeighbours::TriangleCutsSphere()](../../d1/d7c/classMeshCore_1_1MeshSearchNeighbours.html#acb9381777434d3f7ca91c066aaee5124),
[DraftGui.DraftToolBar::update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar::update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[PartDesign::Groove::updateAxis()](../../d7/de3/classPartDesign_1_1Groove.html#a064b27171c35a5be3b681e2856208747),
[PartDesign::Helix::updateAxis()](../../d3/d78/classPartDesign_1_1Helix.html#aa8bfed8d9b7d87cdebf9e491a6193fd6),
[PartDesign::Revolution::updateAxis()](../../d2/de6/classPartDesign_1_1Revolution.html#a07ae95f9e32e5240284db567e6984b0d),
[TechDrawGui::TaskCosmeticLine::updateCosmeticLine()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a8f118f269d306e8675de346600f24e77),
[FemGui::ViewProviderFemConstraintBearing::updateData()](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#a3b3cf2fa05760751890d9e1cf51f178f),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintForce::updateData()](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#ad691cf23756106d6b0ea043ddebd1b94),
[FemGui::ViewProviderFemConstraintGear::updateData()](../../d1/d2f/classFemGui_1_1ViewProviderFemConstraintGear.html#a56f097a322b6fe5b2b4b7eead3374c49),
[FemGui::ViewProviderFemConstraintPulley::updateData()](../../d8/dfc/classFemGui_1_1ViewProviderFemConstraintPulley.html#a7ba40d63d4dff464026a808438d3630b),
[FemGui::ViewProviderFemConstraintTransform::updateData()](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#a2adf8aba7f15f7b95399068ab39c47b8),
[FemGui::ViewProviderFemPostPlaneFunction::updateData()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#a6ec898b1ee3b9ae2983c1f424b2a55f4),
[FemGui::ViewProviderFemPostSphereFunction::updateData()](../../d4/da4/classFemGui_1_1ViewProviderFemPostSphereFunction.html#a9fac4b851c890977a0c56223e6dcf40d),
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
[DraftGui.DraftToolBar::updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
[Gui::ViewProviderDragger::updateTransform()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5f8676364e82e30b6e558c8f25e06b88),
[SketcherGui::DrawSketchHandlerLineSet::updateTransitionData()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a87c661c6611a6c685accb1c089fdeba8),
[DraftGui.DraftToolBar::validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
[Gui::PropertyEditor::PropertyRotationItem::value()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a863981824fc5e2a970540f4e707913d1),
[Gui::PropertyEditor::PropertyPlacementItem::value()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a02b71a4429874d510e780c4a2375a1be),
[MeshGui::ViewProviderMeshTransformDemolding::valueChangedCallback()](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#a0866accd492d2de4c56bf1948fcf999c),
[Path::PathSegmentWalker::walk()](../../d0/d7b/classPath_1_1PathSegmentWalker.html#a2d2253be4424a16caf28ec136b658dc6),
[Points::PlyWriter::write()](../../d4/d57/classPoints_1_1PlyWriter.html#afcad40b7eec0e6e291d5bb1ffc6b0014),
[Points::PcdWriter::write()](../../df/dc2/classPoints_1_1PcdWriter.html#a29a665c849f6da4f82ba12eb6bf06095),
[CDxfWrite::writeAngularDimBlock()](../../d6/d47/classCDxfWrite.html#a4a915e13347bfc87d7b55859523ab4cd),
[CDxfWrite::writeDiametricDimBlock()](../../d6/d47/classCDxfWrite.html#a1099141d6c71739945175a349d98129c),
[PartGui::DlgExtrusion::writeParametersToFeature()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8d059573a157c9f9128d55b3c9a9fcc1),
[CDxfWrite::writeRadialDimBlock()](../../d6/d47/classCDxfWrite.html#aa7f3fe99f84d1fd3ece63a019ba76dc5),
and
[TechDraw::Vertex::y()](../../dd/db1/classTechDraw_1_1Vertex.html#a4f280b6d443364dada10f1de7feb3029).

## ◆ z

template<class _Precision >

_Precision [Base::Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision
>::z  
---  
  
z-coordinate

Referenced by
[PartGui::DlgRevolution::accept()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a92a90c8ff44e8e2f6774d0713d47bbbd),
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[ReenGui::FitBSplineSurfaceWidget::accept()](../../d9/d48/classReenGui_1_1FitBSplineSurfaceWidget.html#af94ddfaebc20a805f34a94face578ce6),
[CmdSketcherConstrainAngle::activated()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a0d48a74c0960a5a240c1a39137f070a3),
[Base::BoundBox3< _Precision
>::Add()](../../d8/d12/classBase_1_1BoundBox3.html#ac9052e09ea4470fc68fb18b70ac608af),
[Mod.PartDesign.Scripts.FilletArc.Vector::add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[Base::InventorBuilder::addBoundingBox()](../../db/d7f/classBase_1_1InventorBuilder.html#a7fa4b2eb43c7d1a8df907bc949462fec),
[MeshCore::MeshFastBuilder::AddFacet()](../../d3/d1d/classMeshCore_1_1MeshFastBuilder.html#a309ce02230a45347d21e2f8a861e9cc6),
[Points::PointsGrid::AddPoint()](../../d1/d4d/classPoints_1_1PointsGrid.html#a3c132db635cb686576c2b85a342891a7),
[MeshCore::MeshPointGrid::AddPoint()](../../dc/de4/classMeshCore_1_1MeshPointGrid.html#a58ee74fcf8e6719b3633d5329c06604a),
[Gui::SelectionSingleton::addSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a90a0ee6e4826630e0e35ba1deb5e98fa),
[Base::Builder3D::addSingleArrow()](../../d6/d1b/classBase_1_1Builder3D.html#a000b4d9d1342d22dcb7c0ded96ad45b2),
[Base::InventorBuilder::addSingleArrow()](../../db/d7f/classBase_1_1InventorBuilder.html#a075ebfc1e2f098e0e0bcf104b3cbb916),
[Base::Builder3D::addSingleLine()](../../d6/d1b/classBase_1_1Builder3D.html#accf2a8116bd1142069e93a4eac808d7b),
[Base::InventorBuilder::addSingleLine()](../../db/d7f/classBase_1_1InventorBuilder.html#a404c84909791311b5fe386216c074d65),
[Base::InventorBuilder::addSinglePlane()](../../db/d7f/classBase_1_1InventorBuilder.html#a7b3b6c4b92eb6b42f4ceab91ad24bc43),
[Base::Builder3D::addSingleTriangle()](../../d6/d1b/classBase_1_1Builder3D.html#a536ca5856ad41bf83a85d68af4ec5f68),
[Base::InventorBuilder::addSingleTriangle()](../../db/d7f/classBase_1_1InventorBuilder.html#aa559cd33d73da4c7f081923dd5c9ea51),
[Base::Builder3D::addTransformation()](../../d6/d1b/classBase_1_1Builder3D.html#ac722adc9f5581af07ee4fb411e5bb7f5),
[Base::InventorBuilder::addTransformation()](../../db/d7f/classBase_1_1InventorBuilder.html#a6a994fa52660b07970bb2d9213f0257c),
[MeshCore::MeshTopoAlgorithm::AdjustEdgesToCurvatureDirection()](../../d6/d22/classMeshCore_1_1MeshTopoAlgorithm.html#a9d434d84a9f0707b8c6ca3b4c35a0c26),
[CmdSketcherConstrainAngle::applyConstraint()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a5602881a59f6c0a0a83a30641560aeb7),
[FemGui::ViewProviderFemMesh::applyDisplacementToNodes()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a2d65b42122fa5ff20cdd2cb783b7e8c5),
[automotive_design.revolved_area_solid::axis_line()](../../d4/ded/classautomotive__design_1_1revolved__area__solid.html#ae7714359aef57b10dc9d110c4c95109c),
[automotive_design.surface_of_revolution::axis_line()](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#ac11430bfca20d807bd7fbb1de4555324),
[automotive_design.revolved_face_solid::axis_line()](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a88ba8cae1c9e693beda33bf96a0423ca),
[ifc4.ifcrevolvedareasolid::axisdirectioninxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a34e620e30709c7c4e2c619daa7704ece),
[ifc2x3.ifcsurfaceofrevolution::axisline()](../../db/d1b/classifc2x3_1_1ifcsurfaceofrevolution.html#a0689126db6a08f9f1183f65515b53370),
[ifc2x3.ifcrevolvedareasolid::axisline()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#ad7a180e86495ea93d5acb25ffcc33ffa),
[ifc4.ifcsurfaceofrevolution::axisline()](../../d4/de7/classifc4_1_1ifcsurfaceofrevolution.html#adf527bd278ddce78734fc2b01bec7b37),
[ifc4.ifcrevolvedareasolid::axisline()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a45efcb80c8963331649e13f991ec7534),
[PathScripts.PathDressupHoldingTags.Tag::bottom()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aaae502deebbb0cc7adf2f1dd338d9ac8),
[Base::BoundBox3< _Precision
>::BoundBox3()](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38),
[TechDraw::CenterLine::calcEndPoints2Points()](../../d5/dd5/classTechDraw_1_1CenterLine.html#aedb72634306a11f9eb49ffac16eb7e2b),
[MeshGui::ViewProviderMeshTransformDemolding::calcNormalVector()](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#ac95395413a936658e653faa60c9a3795),
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[TechDraw::CenterLine::CenterLine()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ae57d1c63055e3adaa4d445554084481e),
[MeshCore::MeshGeomFacet::CenterOfCircumCircle()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#afa4800556683c823c6e8a947b0f6b26d),
[MeshCore::MeshGeomFacet::CenterOfInscribedCircle()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#af8a76150bc765b0331bc42004f012cb9),
[DraftGui.DraftToolBar::changeZValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a33ea2715914aa73b36107598fe5702c5),
[MeshCore::MeshGrid::CheckPosition()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a93306eb31fbf0f2fd27f197bf226ba83),
[PathScripts.PathDressupTag.TagSolid::cloneAt()](../../d2/dc0/classPathScripts_1_1PathDressupTag_1_1TagSolid.html#a0da4c220cd1980731ce8fbb646cc8e13),
[PartDesign::FeatureExtrude::computeDirection()](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a3af51bee887de0bc89953128cb0a4d1c),
[Part::Extrusion::computeFinalParameters()](../../db/d6c/classPart_1_1Extrusion.html#a4b4ddc216eb6449e2b21480a430f5df8),
[MeshCore::MeshCurvature::ComputePerVertex()](../../d3/d7e/classMeshCore_1_1MeshCurvature.html#a8b29abff540cab896736a08bbb74189f),
[TechDraw::CosmeticEdge::CosmeticEdge()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a6e49936bd5b7832d1024b04c2399095f),
[Import::ExportOCAF::createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[PathScripts.PathDressupHoldingTags.Tag::createSolidsAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a2cb6cc02ae81caafbb137dfe20ebfdd8),
[Mod.PartDesign.Scripts.FilletArc.Vector::cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[cSimTool::cSimTool()](../../d3/d31/classcSimTool.html#a3b1d2577bcdde16048e83c1c5c75621c),
[MeshCore::MeshInfo::DetailedEdgeInfo()](../../d3/d42/classMeshCore_1_1MeshInfo.html#aae041af175b0080900634a908c05a0c8),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[Base::CoordinateSystem::displacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970),
[Base::Vector3< double
>::DistanceToLine()](../../d1/d13/classBase_1_1Vector3.html#af38176c3192c969e1ae2255a84885b8a),
[MeshCore::MeshGeomFacet::DistanceToLineSegment()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a275420989c96287043bc6b9ae1232111),
[MeshCore::MeshGeomFacet::DistanceToPoint()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a58f664bc14e352bdd067e05688d20910),
[Base::Vector3< _Precision
>::Dot()](../../d1/d13/classBase_1_1Vector3.html#a876a8620ec4213d4bc580190328ad899),
[Mod.PartDesign.Scripts.FilletArc.Vector::dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[SketcherGui::EditModeConstraintCoinManager::drawConstraintIcons()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a20c4280c68dc704bd2652d6097b0383a),
[TechDraw::GeometryUtils::edgeFromGeneric()](../../d5/d83/classTechDraw_1_1GeometryUtils.html#a06fdb57b76577f20da4b79ab357aac24),
[PartDesign::Pad::execute()](../../d9/d14/classPartDesign_1_1Pad.html#a17b37a5aaa299709fbb066564ef25b3e),
[PartDesign::Pocket::execute()](../../d1/d89/classPartDesign_1_1Pocket.html#aac791837d2ea389e30768f0fb6d25935),
[Drawing::ProjectionAlgos::execute()](../../db/d32/classDrawing_1_1ProjectionAlgos.html#a014d5c556a4982a188e47e4e713ff883),
[Part::Mirroring::execute()](../../dc/dac/classPart_1_1Mirroring.html#aed38846265cf2381aae85d15dfb74be7),
[PartDesign::Hole::execute()](../../dd/dd0/classPartDesign_1_1Hole.html#ad3161d80bf31dc136534283281a5b3ad),
[TechDraw::ProjectionAlgos::execute()](../../dd/d7c/classTechDraw_1_1ProjectionAlgos.html#a014d5c556a4982a188e47e4e713ff883),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[Import::ImpExpDxfWrite::exportAngularDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a020d31516ae6342bc1160de1daabf79a),
[Import::ImpExpDxfWrite::exportDiametricDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#abb723df58a935f6b0590238bc09f7ad5),
[Import::ImpExpDxfWrite::exportLinearDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a469a35bb67d953bd7fc2193a70efa083),
[Import::ImpExpDxfWrite::exportRadialDim()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#aeccef9eee470f21a95169ed063af94e4),
[Import::ImpExpDxfWrite::exportText()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#aa372554ea19f3fd6ff21c048f8bef37c),
[Mesh::Facet::Facet()](../../d7/d79/classMesh_1_1Facet.html#aed4f45fccca652d2000ff55e1a06583c),
[Fem::FemPostDataAlongLineFilter::FemPostDataAlongLineFilter()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ac595ec7511d8d0a5111b5461ef0fa446),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[MeshCoreFit::CylinderFit::findBestSolDirection()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a6e0db1db743acde2daf19bc60f9d1e0c),
[MeshCore::CylinderFit::Fit()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a2b728f7c295c98d85f6159610ff36bc4),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[VisualPathSegmentVisitor::g38()](../../de/d18/classVisualPathSegmentVisitor.html#aefd30507eff704570080c7fe03b6d11d),
[PartDesign::Helix::generateHelixPath()](../../d3/d78/classPartDesign_1_1Helix.html#a04dd9590e1c0afe9dd3f1066ab9f0395),
[Part::GeomLine::GeomLine()](../../d5/d30/classPart_1_1GeomLine.html#a5a8457c1f4e91bf66c8070d86eb9887a),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[Fem::Constraint::getBasePoint()](../../d0/d11/classFem_1_1Constraint.html#a53b58263b54f9ab82afbc002761ccd24),
[TechDraw::DrawViewSection::getCSFromBase()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a761c0e9c4fe742ad0f6250428875ecd4),
[Path::Toolpath::getCycleTime()](../../d6/d0c/classPath_1_1Toolpath.html#a6adb7debbb92c2d09e8b280b00003696),
[MeshCoreFit::CylinderFit::GetDistanceToCylinder()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a7e37395d2a64271694828d763d1582d4),
[MeshCoreFit::SphereFit::GetDistanceToSphere()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#aca8b41099e947b212fee4dd15118fb69),
[Mesh::MeshObject::getEigenSystem()](../../d8/dcc/classMesh_1_1MeshObject.html#a786294ab69d0aedecf59d3d3fb208d80),
[MeshCore::MeshKernel::GetGravityPoint()](../../dd/d95/classMeshCore_1_1MeshKernel.html#a0cce71449b9303e9e2509487f487b290),
[MeshCore::CylinderFit::GetInitialAxisFromNormals()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a94896bef3d7356707b274d1d34c101f4),
[MeshCore::PlaneFit::GetLocalPoints()](../../db/dab/classMeshCore_1_1PlaneFit.html#afea00501e51e679c09dc7ca9064d4555),
[Part::Feature::getLocation()](../../d7/d7e/classPart_1_1Feature.html#a84164b4adfe9b6ecef87da8d7aa1ac9d),
[Part::FeatureReference::getLocation()](../../d2/da1/classPart_1_1FeatureReference.html#aee6f4d426e17d5a0193108fd06f7309c),
[Base::BoundBox3< _Precision
>::GetOctantFromVector()](../../d8/d12/classBase_1_1BoundBox3.html#ae68b2abe794808185a01fd6cb01fad42),
[MeshGui::PlaneFitParameter::getParameter()](../../da/d31/classMeshGui_1_1PlaneFitParameter.html#acc96292a875e15e9e792e59994f02a71),
[MeshGui::CylinderFitParameter::getParameter()](../../d6/d6d/classMeshGui_1_1CylinderFitParameter.html#ab93a68400083131e275c6f9d3af94fab),
[Mesh::MeshObject::getPoint()](../../d8/dcc/classMesh_1_1MeshObject.html#a3b5cfb389c3be7ecad0809494f54418d),
[Mesh::MeshObject::getPointNormal()](../../d8/dcc/classMesh_1_1MeshObject.html#ab3953ee00afa96512b922acb9ea5ec12),
[Mesh::MeshObject::getPointNormals()](../../d8/dcc/classMesh_1_1MeshObject.html#a16c59852a6633307010cc619c4d10143),
[Mesh::MeshObject::getPoints()](../../d8/dcc/classMesh_1_1MeshObject.html#a4b7287613ca9dbab79d581af2a0632e6),
[TechDraw::DrawViewPart::getProjectionCS()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ae1dd72b98fa563bf72d6c39f49577632),
[Base::Rotation::getRawValue()](../../d4/d18/classBase_1_1Rotation.html#afe860f0bcfaec728e99861e4c65904aa),
[PartDesignGui::ViewProviderDatum::getRelevantBoundBox()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a8437c5be88154b9cb0bd2bae5ef94db3),
[TechDraw::DrawViewSection::getSectionCS()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aefc378d8464959b191ac4ff96f6bca12),
[Base::BoundBox3< _Precision
>::GetSideFromRay()](../../d8/d12/classBase_1_1BoundBox3.html#a900e54e09a7e5ba1909a10a0d83c40ea),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[MeshCore::AbstractPolygonTriangulator::GetTransformToFitPlane()](../../d9/d6e/classMeshCore_1_1AbstractPolygonTriangulator.html#aaaa240d0f1a906bdc7cc01c81dea9250),
[TechDraw::DrawGeomHatch::getTrimmedLinesSection()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a2fe5d2f18fe5801e37a1cfdb967fbce3),
[Gui::LocationWidget::getUserDirection()](../../d9/d9a/classGui_1_1LocationWidget.html#a928aeb60d1d1a95d4d336c6901fb950b),
[Gui::LocationDialog::getUserDirection()](../../dc/d22/classGui_1_1LocationDialog.html#aa52301a6aec2f1b750929d7444765c33),
[Base::Rotation::getValue()](../../d4/d18/classBase_1_1Rotation.html#af95c57a06636f68b2a6cc779dc042edd),
[TechDraw::DrawProjGroupItem::getViewAxis()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a66cab4b4ebd52d41889c7fdb9c854821),
[TechDraw::getViewAxis()](../../d7/d31/namespaceTechDraw.html#ad612c2d90cb50e87312099ea9824c509),
[MeshCore::MeshKernel::GetVolume()](../../dd/d95/classMeshCore_1_1MeshKernel.html#a919704318d645c2a0d30cd9fa2203439),
[Fem::FemMesh::getVolume()](../../d3/d2e/classFem_1_1FemMesh.html#a86dfe0bdac5ccbc115b39af5780ee2b1),
[Base::Matrix4D::Hat()](../../d5/db4/classBase_1_1Matrix4D.html#ae5b666346437729d9c62741a35497aa7),
[MeshCore::MeshGeomEdge::IntersectBoundingBox()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#aa33bee65b66dc0904e254e42f20bf02d),
[MeshCore::MeshGeomFacet::IntersectBoundingBox()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0a6b404c351030f6727713ab4b9fa805),
[TechDraw::AOC::intersectsArc()](../../d0/d5c/classTechDraw_1_1AOC.html#a061b7f38a3cd0dca1c8c08a03c7a05fe),
[TechDraw::BSpline::intersectsArc()](../../d6/d09/classTechDraw_1_1BSpline.html#a5af43bc17061b8e8f6598dec030ea659),
[MeshCore::MeshGeomFacet::IntersectWithFacet()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a4324352edc96819d5ce83009cd1ed2df),
[Base::BoundBox3< _Precision
>::IntersectWithLine()](../../d8/d12/classBase_1_1BoundBox3.html#aa1b97e4eab9eecfd4711d01a3b9ed533),
[MeshCore::MeshGeomFacet::IntersectWithPlane()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a1a60849171e88c8fcf54e341b36a56eb),
[Gui::ViewVolumeProjection::inverse()](../../d8/d4d/classGui_1_1ViewVolumeProjection.html#a1d7fe268b671119971278bdf467133f2),
[Base::BoundBox3< _Precision
>::IsCutLine()](../../d8/d12/classBase_1_1BoundBox3.html#a55a718fe21f7a5240ac7b6651b4c5822),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#a755404902a0ec9b28e954657ba887307),
[cSimTool::isInside()](../../d3/d31/classcSimTool.html#ad2e9adbe06388f51b1ba05025d6021a3),
[TechDraw::DrawViewPart::isIso()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#af3b5d2ae674b8b2b423edc3b12833e29),
[Part::Geom2dConic::isReversed()](../../d8/d0d/classPart_1_1Geom2dConic.html#aec5c8932c68cc202319386c05d360e0e),
[Part::Geom2dArcOfConic::isReversed()](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html#ac8038187938c29d508ec52019b36f556),
[TechDraw::legacyViewAxis1()](../../d7/d31/namespaceTechDraw.html#a6c5c5a402ebdc68e1048cb62d6ef595f),
[Mod.PartDesign.Scripts.FilletArc.Vector::length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Points::PointsAlgos::LoadAscii()](../../d8/d62/classPoints_1_1PointsAlgos.html#a75d94f79566c5ebb47f14fbafa6be26e),
[MeshCore::MeshInput::LoadInventor()](../../d9/d08/classMeshCore_1_1MeshInput.html#acf19f4238be1fd7d9f3b260af125d599),
[MeshCore::MeshInput::LoadPLY()](../../d9/d08/classMeshCore_1_1MeshInput.html#a8f60cc2825d0ffd59075b0892d92417b),
[PartGui::Location::Location()](../../db/d6f/classPartGui_1_1Location.html#a2f77946d77e8f18590ccf3f7e73a18b4),
[MeshPart::MeshAlgos::LoftOnCurve()](../../db/d67/classMeshPart_1_1MeshAlgos.html#af6d0bd2cf1dd2ca04dfb7a7f853f2aba),
[PartDesign::Feature::makePlnFromPlane()](../../d7/d51/classPartDesign_1_1Feature.html#a6ab00d23c99b505b5bf57dedac353631),
[Base::Rotation::makeRotationByAxes()](../../d4/d18/classBase_1_1Rotation.html#a0b7c436d3243f3703959c7f6be8ecad2),
[Part::Geometry::mirror()](../../dc/df0/classPart_1_1Geometry.html#af5e2f1761b12dcf915ffb3bc9f2e20fe),
[TechDraw::mirrorShapeVec()](../../d7/d31/namespaceTechDraw.html#a94c08edd68671f2042041c91350f1e36),
[Base::Matrix4D::move()](../../d5/db4/classBase_1_1Matrix4D.html#ac833395bac6936432368efa5595387bd),
[TechDraw::moveShape()](../../d7/d31/namespaceTechDraw.html#a6984b4017e3ad0b59304844e743f064a),
[Mod.PartDesign.Scripts.FilletArc.Vector::mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector::norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[Mesh::MeshObject::offsetSpecial()](../../d8/dcc/classMesh_1_1MeshObject.html#a79fce33947d4de9f9de6f883f1897688),
[MeshPart::MeshAlgos::offsetSpecial()](../../db/d67/classMeshPart_1_1MeshAlgos.html#ade65ddc063ac090bae47a7a6ef797f93),
[Gui::Dialog::Transform::on_applyButton_clicked()](../../d0/d8f/classGui_1_1Dialog_1_1Transform.html#aa736a36e69d76427b945f434e46f3a2a),
[Gui::ViewProviderOrigin::onChanged()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[Fem::FemPostDataAlongLineFilter::onChanged()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ae418afcb8e18abba84d16c2a645a434e),
[PathGui::ViewProviderPath::onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
[PathGui::PathSelectionObserver::onSelectionChanged()](../../db/d77/classPathGui_1_1PathSelectionObserver.html#a647466bb806e71c512362f4dafc43e7b),
[Base::Vector3< _Precision
>::operator&()](../../d1/d13/classBase_1_1Vector3.html#ab377fb85d034e0486a08805cdf56b629),
[Base::operator*()](../../db/d07/namespaceBase.html#ac7d409d67697b8ea931e0febfe6e26de),
[Base::Matrix4D::operator*()](../../d5/db4/classBase_1_1Matrix4D.html#ab8a45ff4ced15d460ae0b11239629d52),
[Base::Vector3< _Precision
>::operator+()](../../d1/d13/classBase_1_1Vector3.html#a217bd5ebf8797d0930fda829c3f1698f),
[Base::Vector3< _Precision
>::operator-()](../../d1/d13/classBase_1_1Vector3.html#ab8cca8856cabb105f7e2d002078776e4),
[MeshCore::MeshPoint::operator<()](../../dd/db5/classMeshCore_1_1MeshPoint.html#af48745635582de4c6c517382120f6440),
[DrawingGui::orthoview::orthoview()](../../db/df8/classDrawingGui_1_1orthoview.html#afc8be37cc7e9325e722e05f2736af13d),
[Base::Matrix4D::Outer()](../../d5/db4/classBase_1_1Matrix4D.html#a8e19dc5e655bc920f9527c62c1ecf7aa),
[MeshCore::PlaneSurfaceFit::Parameters()](../../d9/df5/classMeshCore_1_1PlaneSurfaceFit.html#a2c0e5c7c7155ea8eb77c28af1589c1b4),
[MeshCore::CylinderSurfaceFit::Parameters()](../../d1/d68/classMeshCore_1_1CylinderSurfaceFit.html#a77a6a4645558df8448d8284ebe34417b),
[MeshGui::SoFCMeshPickNode::pick()](../../d1/d1b/classMeshGui_1_1SoFCMeshPickNode.html#ac140e23964b3171e35ff15585cd3ba14),
[Attacher::AttachEngine::placementFactory()](../../d2/d85/classAttacher_1_1AttachEngine.html#a0eff77539401a8d4a04554a970bd85b4),
[DraftGui.DraftToolBar::pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[MeshCore::SurfaceFit::PolynomFit()](../../d2/d9a/classMeshCore_1_1SurfaceFit.html#a7dc8000c3b6f4bcae7320a4c8a48d489),
[Points::PointsGrid::Pos()](../../d1/d4d/classPoints_1_1PointsGrid.html#aaa5c87982921d2673a7ac3227d2b6714),
[Inspection::MeshInspectGrid::Pos()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#ad94d0cf1a82a11f6b649619db7e1f5e3),
[MeshCore::MeshFacetGrid::Pos()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#ade0d241d31a50d7dd2be2defca3acc1e),
[MeshCore::MeshPointGrid::Pos()](../../dc/de4/classMeshCore_1_1MeshPointGrid.html#a5780dcbbe5bda437bf2b11407cf4c4bb),
[Points::PointsGrid::Position()](../../d1/d4d/classPoints_1_1PointsGrid.html#a5dc29f08827b2e5b849da258c39e0b49),
[MeshCore::MeshGrid::Position()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a8b0dcdb55de3e3c2f8bce7e3a618c0a9),
[MeshCore::MeshFacetGrid::PosWithCheck()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#a59cc6fc0efed46133e4b0580b5fe4ac8),
[Reen::ParameterCorrection::ProjectControlPointsOnPlane()](../../dd/d71/classReen_1_1ParameterCorrection.html#a54d70272eced8a72c72f8c11a11ac568),
[MeshPart::CurveProjectorSimple::projectCurve()](../../db/d5f/classMeshPart_1_1CurveProjectorSimple.html#a5932b3a0d0a1ee7119cc7f7b5f180ef8),
[MeshPart::CurveProjectorShape::projectCurve()](../../dc/d83/classMeshPart_1_1CurveProjectorShape.html#a78cb49a17db5b6adcb772e9589d32580),
[MeshPart::MeshProjection::projectEdgeToEdge()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#a322496a26bba88d2ff370beef12fdc3b),
[TechDraw::DrawViewPart::projectPoint()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#afbe98e95b0bd7b0cec45b29d29ce46b2),
[TechDraw::LandmarkDimension::projectPoint()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a55be6d3789c069c9509a7ae087324d99),
[MeshCore::SphereFit::ProjectToSphere()](../../dc/dce/classMeshCore_1_1SphereFit.html#ad019d88b25f67f7893cdf7179f1cd6c5),
[MeshCoreFit::SphereFit::ProjectToSphere()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#ad019d88b25f67f7893cdf7179f1cd6c5),
[CDxfWrite::putArrow()](../../d6/d47/classCDxfWrite.html#af14654282595c1d9d2a47b4ac6427bbb),
[CDxfWrite::putText()](../../d6/d47/classCDxfWrite.html#a5af170abde99f5eebff5afac269622fd),
[Points::E57Reader::read()](../../d2/dfb/classPoints_1_1E57Reader.html#a7af6bb0bc50ff56c203f0cb0aa04d458),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[Path::Toolpath::recalculate()](../../d6/d0c/classPath_1_1Toolpath.html#a6fcb5afb3f1023ef686cd87b4f69c0f9),
[PathGui::ViewProviderPath::recomputeBoundingBox()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a4a681a533fc16dba93a80bc3fdfc21c3),
[DraftGui.DraftToolBar::reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[TechDraw::CosmeticVertex::Restore()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a11aa1f69e9211c240d61949a237056a1),
[TechDraw::CenterLine::Restore()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
[TechDraw::Vertex::Restore()](../../dd/db1/classTechDraw_1_1Vertex.html#a8db190000b0c2b933006ee8c4d94f511),
[TechDraw::Circle::Restore()](../../d3/d63/classTechDraw_1_1Circle.html#a0c95eda08d536f7de7c3a3abb3007e76),
[TechDraw::AOC::Restore()](../../d0/d5c/classTechDraw_1_1AOC.html#a6adb7fceabe6a5089727723cff4b2760),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::Geometry::rotate()](../../dc/df0/classPart_1_1Geometry.html#a3c7ebf21592da6737fccb28bf9508a75),
[TechDraw::DrawViewSection::rotateCSArbitrary()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a66a852d7e827780ebf6e1d46439d49e2),
[Base::Vector3< _Precision
>::RotateX()](../../d1/d13/classBase_1_1Vector3.html#ae4b74aa1b2b0b0b8a3919f337dd680f6),
[Base::Vector3< _Precision
>::RotateY()](../../d1/d13/classBase_1_1Vector3.html#a35cf612a380c8d5dddeaa0730f44023c),
[Base::Matrix4D::rotLine()](../../d5/db4/classBase_1_1Matrix4D.html#aff3583443a5de61928925fa6b8af6f21),
[PartDesign::Helix::safePitch()](../../d3/d78/classPartDesign_1_1Helix.html#a85474d1c32f51cf49c0be48c600993eb),
[Part::GeomLine::Save()](../../d5/d30/classPart_1_1GeomLine.html#a88fd00890c6c4e7729b05c279a64656d),
[Part::GeomLineSegment::Save()](../../d9/d6f/classPart_1_1GeomLineSegment.html#acc377c70086de1bfbfd88e523b663529),
[Robot::Robot6Axis::Save()](../../dc/d5f/classRobot_1_1Robot6Axis.html#a7cf092c9dc75bf16fe3b6a01d9fa03d4),
[Robot::Waypoint::Save()](../../d1/dc7/classRobot_1_1Waypoint.html#a2d0f51a0e8e89f1148887af8e2eb0537),
[TechDraw::CosmeticVertex::Save()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#aee8e2101aa119ae2dc4750442745264c),
[TechDraw::CenterLine::Save()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[TechDraw::Vertex::Save()](../../dd/db1/classTechDraw_1_1Vertex.html#aed3011b8fc0de22659800304c3f1b0af),
[TechDraw::Circle::Save()](../../d3/d63/classTechDraw_1_1Circle.html#ab3a64b9c96ec1f8dc658f0432955bfa5),
[TechDraw::AOC::Save()](../../d0/d5c/classTechDraw_1_1AOC.html#a4627154c0a8d5886ee4ee54231107de2),
[App::PropertyPlacement::Save()](../../da/d51/classApp_1_1PropertyPlacement.html#ae1314101350bc9e76b9d692693c8e9e1),
[App::PropertyRotation::Save()](../../df/d76/classApp_1_1PropertyRotation.html#ad9e882ab49bd192e84f62de9a64c62ce),
[MeshCore::MeshOutput::Save3MFModel()](../../db/d14/classMeshCore_1_1MeshOutput.html#a37bb55249af3cbca138ae4536bf71325),
[MeshCore::MeshOutput::SaveAsciiPLY()](../../db/d14/classMeshCore_1_1MeshOutput.html#a4f5628a8d90a67d09484426b71f30a6a),
[MeshCore::MeshOutput::SaveAsciiSTL()](../../db/d14/classMeshCore_1_1MeshOutput.html#a978a9f0a89ca5ce4d828305f005de62b),
[MeshCore::MeshOutput::SaveAsymptote()](../../db/d14/classMeshCore_1_1MeshOutput.html#a31276c848ed13571a0e7f6f932e5a45e),
[MeshCore::MeshOutput::SaveBinaryPLY()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3f47cee51e773e3eb9310e1bf3ed8bf8),
[MeshCore::MeshOutput::SaveBinarySTL()](../../db/d14/classMeshCore_1_1MeshOutput.html#aa319df520ea268406d3a19a1c4a4f198),
[MeshCore::MeshOutput::SaveIDTF()](../../db/d14/classMeshCore_1_1MeshOutput.html#ad297d3f6095f421beb22932929190fbb),
[MeshCore::MeshOutput::SaveMeshNode()](../../db/d14/classMeshCore_1_1MeshOutput.html#a77cd49917f9394aadcd355c5247546f0),
[MeshCore::MeshOutput::SaveNastran()](../../db/d14/classMeshCore_1_1MeshOutput.html#a832d24717641893b591f5b4d99db9e3f),
[MeshCore::MeshOutput::SaveOBJ()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3d771358cea3ae77d666c54aba2692b5),
[MeshCore::MeshOutput::SaveOFF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8b4f5b020dd2b94b087ff831b7aee3c4),
[Import::ExportOCAF::saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[MeshCore::MeshOutput::SaveSMF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a7b44d31efb50a5d64b2b08fbcc91963f),
[MeshCore::MeshOutput::SaveVRML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8fc229d0641d58846478dbcaa077e8db),
[MeshCore::MeshOutput::SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
[MeshCore::MeshOutput::SaveXML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8a89241b7984ceab819293e9b7385c20),
[Base::Matrix4D::scale()](../../d5/db4/classBase_1_1Matrix4D.html#a3121f149e2b6034c29235b776f44989b),
[TechDraw::CenterLine::scaledGeometry()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a104bfe6bf49d7b364f65000352e670ea),
[MeshCore::MeshAlgorithm::SearchFacetsFromPolyline()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a72f7307406aa5146e43c481b5b3a25d7),
[MeshCore::MeshFacetGrid::SearchNearestFromPoint()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#afbb767d3a8804d125b5d7b80db72d471),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[TechDraw::DrawViewSection::sectionExec()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a79c8f60f63dd54684af4cad42f91ee4e),
[Part::GeomConic::setCenter()](../../d1/d86/classPart_1_1GeomConic.html#a0ef572424983321dada7f64d0aa1a3b9),
[Part::GeomArcOfConic::setCenter()](../../db/d48/classPart_1_1GeomArcOfConic.html#a8a2755a6bbbed714049540421198bb8a),
[MeshPartGui::ViewProviderCrossSections::setCoords()](../../dc/dfe/classMeshPartGui_1_1ViewProviderCrossSections.html#acdea9634b2faaa0d83425fd4ede721c7),
[PartGui::ViewProviderCrossSections::setCoords()](../../d8/df0/classPartGui_1_1ViewProviderCrossSections.html#a5e651bd86ec7aa11c84537275b1af31d),
[PartGui::DlgExtrusion::setDir()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a0519f8635962170f77bf009e2071a389),
[PartGui::DlgRevolution::setDirection()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a4df42abdf4af0ef46cb8cfcdca995c9c),
[Gui::LocationWidget::setDirection()](../../d9/d9a/classGui_1_1LocationWidget.html#a2af475de798c64df6995f659a2e7ab40),
[Gui::LocationUi< Ui
>::setDirection()](../../db/da1/classGui_1_1LocationUi.html#a13961053ead815e1adb59564608b8b8a),
[Gui::LocationImpUi< Ui
>::setDirection()](../../df/d30/classGui_1_1LocationImpUi.html#a95f67606fb3dbaab6d199980cb091c63),
[RobotGui::ViewProviderRobotObject::setDragger()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a7a94208ad67ec05ebc9013cac68d34f4),
[Path::Command::setFromPlacement()](../../d7/d2e/classPath_1_1Command.html#a62372d49bbf1003cc81fe7035c7b592e),
[Part::GeomLine::setLine()](../../d5/d30/classPart_1_1GeomLine.html#a602d118b05d480b3f1df2c16f9129bab),
[Part::GeomConic::setLocation()](../../d1/d86/classPart_1_1GeomConic.html#af9bbec6989f1ae76e3e6cff0fb02a05a),
[Part::GeomArcOfConic::setLocation()](../../db/d48/classPart_1_1GeomArcOfConic.html#a1f2b7ce2d1b354cda0ed3c33275d6ec6),
[Part::GeomEllipse::setMajorAxisDir()](../../db/d52/classPart_1_1GeomEllipse.html#a05d29bbfe1e80f91559e12fb8b2cfc36),
[Part::GeomArcOfEllipse::setMajorAxisDir()](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#acb1e2d5a06a4a7b7e8d8ddee835e11b4),
[Part::GeomArcOfHyperbola::setMajorAxisDir()](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#a59725dadb45c4d7afd0562b646c36f79),
[App::PropertyVector::setPyObject()](../../d5/d2b/classApp_1_1PropertyVector.html#a4e4eae3cb50d20fece89b7aac9fa6324),
[Part::TopoShape::setShapePlacement()](../../d8/ded/classPart_1_1TopoShape.html#a8ae38d04353d5ccc4c60beaad3a4a497),
[Gui::Dialog::Transform::setTransformStrategy()](../../d0/d8f/classGui_1_1Dialog_1_1Transform.html#ae3b140a0d601a95674bcbda4e88aa6d4),
[TechDrawGui::TaskSectionView::setUiEdit()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a43dc3542cf896d0778a028ae2be230ce),
[TechDrawGui::TaskCosmeticLine::setUiEdit()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a99ac5dc7728cfedeee3aedf2b9559791),
[TechDrawGui::TaskSectionView::setUiPrimary()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a07485a3822d8c672d6e4580fe4bf858c),
[TechDrawGui::TaskCosmeticLine::setUiPrimary()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a4b1f902a521e9cd5fdf56889d51e52a3),
[PartDesign::Pipe::setupAlgorithm()](../../da/d61/classPartDesign_1_1Pipe.html#aee88e3fe184997d50ac86c9f99b113f2),
[MeshCoreFit::SphereFit::setupObservation()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#a56ac7d52481e7015dd415262b344b470),
[MeshCoreFit::CylinderFit::setupObservation()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a856fae3fea7c099c0972d1f07a89b8c9),
[Gui::PropertyEditor::PropertyRotationItem::setValue()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a65660d1593a8c2f7dabca98e9464c6cc),
[Gui::PropertyEditor::PropertyPlacementItem::setValue()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a7f8e70acbf194633b6b3422b87a07ab3),
[Base::Rotation::setValue()](../../d4/d18/classBase_1_1Rotation.html#a62c0b4012cb383de60d0e4a225c39550),
[Gui::ManualAlignment::setViewingDirections()](../../d7/d97/classGui_1_1ManualAlignment.html#ad3be3a6882c973db3ae9d21b40a85772),
[Part::GeomArcOfConic::setXAxisDir()](../../db/d48/classPart_1_1GeomArcOfConic.html#afdcf8bd89f0e40ba453289cbf098b364),
[MeshGui::ViewProviderMeshOrientation::showDefects()](../../d1/d8e/classMeshGui_1_1ViewProviderMeshOrientation.html#acad074355a307b6f0e8059ae22ba8d54),
[MeshGui::ViewProviderMeshNonManifolds::showDefects()](../../d5/d95/classMeshGui_1_1ViewProviderMeshNonManifolds.html#aa021d71ade5620d8dc36c94220862be8),
[MeshGui::ViewProviderMeshNonManifoldPoints::showDefects()](../../d6/d60/classMeshGui_1_1ViewProviderMeshNonManifoldPoints.html#ad648ec1aee86628d91e6aec48eafaa42),
[MeshGui::ViewProviderMeshDuplicatedFaces::showDefects()](../../d1/d9b/classMeshGui_1_1ViewProviderMeshDuplicatedFaces.html#a435c5361ffb8312295cc076da55d56a8),
[MeshGui::ViewProviderMeshDegenerations::showDefects()](../../d2/da9/classMeshGui_1_1ViewProviderMeshDegenerations.html#a954810db894668aaea3d6a26f310f2ea),
[MeshGui::ViewProviderMeshDuplicatedPoints::showDefects()](../../d5/d26/classMeshGui_1_1ViewProviderMeshDuplicatedPoints.html#af52e3e5a78f9c0ecceab7bb945b1c075),
[MeshGui::ViewProviderMeshIndices::showDefects()](../../dd/d71/classMeshGui_1_1ViewProviderMeshIndices.html#abcb21eec9d9285a3d13ee103e03beaaa),
[MeshGui::ViewProviderMeshFolds::showDefects()](../../d8/d06/classMeshGui_1_1ViewProviderMeshFolds.html#a1a9474aafd32ff0b730a7c795a8fc5e9),
[MeshGui::ViewProviderMeshNode::showOpenEdges()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a7db6427662808c81110a3efc5e523064),
[Part::TopoShape::slice()](../../d8/ded/classPart_1_1TopoShape.html#af54879971e721f27d014b938a1b57eb3),
[Part::TopoShape::slices()](../../d8/ded/classPart_1_1TopoShape.html#a808f0de39292b4e84445ed75b263852e),
[MeshCore::PlaneFitSmoothing::Smooth()](../../d4/d74/classMeshCore_1_1PlaneFitSmoothing.html#a8c02774a72bb114362c993f51dc0d7ec),
[MeshCore::PlaneFitSmoothing::SmoothPoints()](../../d4/d74/classMeshCore_1_1PlaneFitSmoothing.html#aa6fba7b76ab58215430b86da7dec700d),
[importSH3D.SH3DHandler::startElement()](../../d8/de6/classimportSH3D_1_1SH3DHandler.html#a9a512563447c10428d4e0e65fbbc95f7),
[Mod.PartDesign.Scripts.FilletArc.Vector::sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[FemGui::TaskPostDataAlongLine::TaskPostDataAlongLine()](../../db/dfe/classFemGui_1_1TaskPostDataAlongLine.html#a63d24585168c09609383c5025fc02c61),
[Base::Matrix4D::toAxisAngle()](../../d5/db4/classBase_1_1Matrix4D.html#aebaf3536031474ff723f0a4abd621e55),
[Gui::View3DInventorViewer::toggleClippingPlane()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ae41b2cfdc548e959d744937ff7a85317),
[Gui::PropertyEditor::PropertyRotationItem::toolTip()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#abbb3c671e82d0c8d54f1f6f2b95abe5d),
[Gui::PropertyEditor::PropertyPlacementItem::toolTip()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#add11217c79e909fa0d6a5fa97d739d2f),
[PathScripts.PathDressupHoldingTags.Tag::top()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#abe7b229a9b4e1207f20627c3546cfe1c),
[PartGui::Location::toPlacement()](../../db/d6f/classPartGui_1_1Location.html#a3a6283d802f45e675b6ddf9c714c8f47),
[TechDraw::DrawUtil::toR3()](../../da/d23/classTechDraw_1_1DrawUtil.html#adf8b4269fac80cfb6793e8b54873361e),
[Gui::PropertyEditor::PropertyRotationItem::toString()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a13b41010f83aeb8833bf251d9f1a652a),
[Gui::PropertyEditor::PropertyPlacementItem::toString()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a4866bdcbed09d39f47781b1b5aba4cec),
[TechDraw::CosmeticVertex::toString()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#acb9933bf213ddd298b48d573bfa63f2d),
[TechDraw::CenterLine::toString()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a0af372e8042e1f5e9b02fe8d176d38ca),
[TechDraw::Circle::toString()](../../d3/d63/classTechDraw_1_1Circle.html#a61924379310acb95418698663af100f0),
[TechDraw::AOC::toString()](../../d0/d5c/classTechDraw_1_1AOC.html#aad4400a1a3d31738afea85abe57d6917),
[Path::Command::transform()](../../d7/d2e/classPath_1_1Command.html#a86423c625f09285dd820b578462c199e),
[MeshCore::SurfaceFit::Transform()](../../d2/d9a/classMeshCore_1_1SurfaceFit.html#a4e5b025adea5142985b11b1042c8b256),
[Base::Vector3< double
>::TransformToCoordinateSystem()](../../d1/d13/classBase_1_1Vector3.html#a5369dfa0fb3929e42263f871a865324b),
[Data::ComplexGeoData::transformToInside()](../../d8/daf/classData_1_1ComplexGeoData.html#a8b0cc05d2cf2ab2a1bb36e7f2a70949e),
[MeshCore::MeshSearchNeighbours::TriangleCutsSphere()](../../d1/d7c/classMeshCore_1_1MeshSearchNeighbours.html#acb9381777434d3f7ca91c066aaee5124),
[DraftGui.DraftToolBar::update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar::update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[PartDesign::Groove::updateAxis()](../../d7/de3/classPartDesign_1_1Groove.html#a064b27171c35a5be3b681e2856208747),
[PartDesign::Helix::updateAxis()](../../d3/d78/classPartDesign_1_1Helix.html#aa8bfed8d9b7d87cdebf9e491a6193fd6),
[PartDesign::Revolution::updateAxis()](../../d2/de6/classPartDesign_1_1Revolution.html#a07ae95f9e32e5240284db567e6984b0d),
[TechDrawGui::TaskCosmeticLine::updateCosmeticLine()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a8f118f269d306e8675de346600f24e77),
[FemGui::ViewProviderFemConstraintBearing::updateData()](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#a3b3cf2fa05760751890d9e1cf51f178f),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintForce::updateData()](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#ad691cf23756106d6b0ea043ddebd1b94),
[FemGui::ViewProviderFemConstraintGear::updateData()](../../d1/d2f/classFemGui_1_1ViewProviderFemConstraintGear.html#a56f097a322b6fe5b2b4b7eead3374c49),
[FemGui::ViewProviderFemConstraintPulley::updateData()](../../d8/dfc/classFemGui_1_1ViewProviderFemConstraintPulley.html#a7ba40d63d4dff464026a808438d3630b),
[FemGui::ViewProviderFemConstraintTransform::updateData()](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#a2adf8aba7f15f7b95399068ab39c47b8),
[FemGui::ViewProviderFemPostPlaneFunction::updateData()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#a6ec898b1ee3b9ae2983c1f424b2a55f4),
[FemGui::ViewProviderFemPostSphereFunction::updateData()](../../d4/da4/classFemGui_1_1ViewProviderFemPostSphereFunction.html#a9fac4b851c890977a0c56223e6dcf40d),
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
[DraftGui.DraftToolBar::updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
[Gui::ViewProviderDragger::updateTransform()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5f8676364e82e30b6e558c8f25e06b88),
[DraftGui.DraftToolBar::validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
[Gui::PropertyEditor::PropertyRotationItem::value()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a863981824fc5e2a970540f4e707913d1),
[Gui::PropertyEditor::PropertyPlacementItem::value()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a02b71a4429874d510e780c4a2375a1be),
[MeshGui::ViewProviderMeshTransformDemolding::valueChangedCallback()](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#a0866accd492d2de4c56bf1948fcf999c),
[Path::PathSegmentWalker::walk()](../../d0/d7b/classPath_1_1PathSegmentWalker.html#a2d2253be4424a16caf28ec136b658dc6),
[ifc2x3.ifcrevolvedareasolid::wr32()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a2d005a905b9bcd1b1d7fc934f7085073),
[Points::PlyWriter::write()](../../d4/d57/classPoints_1_1PlyWriter.html#afcad40b7eec0e6e291d5bb1ffc6b0014),
[Points::PcdWriter::write()](../../df/dc2/classPoints_1_1PcdWriter.html#a29a665c849f6da4f82ba12eb6bf06095),
[CDxfWrite::writeAngularDimBlock()](../../d6/d47/classCDxfWrite.html#a4a915e13347bfc87d7b55859523ab4cd),
[CDxfWrite::writeDiametricDimBlock()](../../d6/d47/classCDxfWrite.html#a1099141d6c71739945175a349d98129c),
[PartGui::DlgExtrusion::writeParametersToFeature()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8d059573a157c9f9128d55b3c9a9fcc1),
and
[CDxfWrite::writeRadialDimBlock()](../../d6/d47/classCDxfWrite.html#aa7f3fe99f84d1fd3ece63a019ba76dc5).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Builder3D.h
  * FreeCAD/src/Base/Vector3D.h
  * FreeCAD/src/Base/Vector3D.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

