---
url: https://freecad.github.io/SourceDoc/dd/dc2/classBase_1_1ViewProjMatrix.html
scraped_at: 2025-09-08T15:18:12.312510
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [ViewProjMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html)

[List of all members](../../d9/d9d/classBase_1_1ViewProjMatrix-members.html) | Public Member Functions | Protected Attributes

Base::ViewProjMatrix Class Reference

The [ViewProjMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html "The
ViewProjMatrix class returns the result of the multiplication of the 3D vector
and the view trans...") class returns the result of the multiplication of the
3D vector and the view transformation matrix.
[More...](../../dd/dc2/classBase_1_1ViewProjMatrix.html#details)

`#include <ViewProj.h>`

##  Public Member Functions  
  
---  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [getProjectionMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a9c88e958a0eabeaa0942715bec0606bb) () const  
| Calculate the projection (+ mapping) matrix.
[More...](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a9c88e958a0eabeaa0942715bec0606bb)  
  
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [inverse](../../dd/dc2/classBase_1_1ViewProjMatrix.html#aeca63d8a99d75084623b791f7ddecedf) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclPt) const  
| Convert a 2D point on the projection plane in 3D space.
[More...](../../dd/dc2/classBase_1_1ViewProjMatrix.html#aeca63d8a99d75084623b791f7ddecedf)  
  
[Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) | [inverse](../../dd/dc2/classBase_1_1ViewProjMatrix.html#ae9f20859b62da577c761b873751255eb) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclPt) const  
| Convert a 2D point on the projection plane in 3D space.
[More...](../../dd/dc2/classBase_1_1ViewProjMatrix.html#ae9f20859b62da577c761b873751255eb)  
  
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [operator()](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a2ab5f7d1c73f3e080d25dd4ecbe1af10) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclPt) const  
| Convert 3D point to 2D projection plane.
[More...](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a2ab5f7d1c73f3e080d25dd4ecbe1af10)  
  
[Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) | [operator()](../../dd/dc2/classBase_1_1ViewProjMatrix.html#acbb267b3278e425ae7e338bb6434b635) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclPt) const  
| Convert 3D point to 2D projection plane.
[More...](../../dd/dc2/classBase_1_1ViewProjMatrix.html#acbb267b3278e425ae7e338bb6434b635)  
  
|
[ViewProjMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a142a4cfdb0cbee29908ec0b07f8085c0)
(const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rclMtx)  
![-](../../closed.png) Public Member Functions inherited from
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html)  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [getComposedProjectionMatrix](../../de/daf/classBase_1_1ViewProjMethod.html#a304b653764af8d3dc70afda41f570c2f) () const  
| Calculate the composed projection matrix.
[More...](../../de/daf/classBase_1_1ViewProjMethod.html#a304b653764af8d3dc70afda41f570c2f)  
  
virtual [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [getProjectionMatrix](../../de/daf/classBase_1_1ViewProjMethod.html#ae30c910881bad2a3d4acfe896f012a6e) () const =0  
| Calculate the projection (+ mapping) matrix.
[More...](../../de/daf/classBase_1_1ViewProjMethod.html#ae30c910881bad2a3d4acfe896f012a6e)  
  
const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | [getTransform](../../de/daf/classBase_1_1ViewProjMethod.html#ad66898cdcdcdb1653736c2930568783a) () const  
virtual [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [inverse](../../de/daf/classBase_1_1ViewProjMethod.html#a9ef0f551ec2a1d352cb7a084b2b27c87) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclPt) const =0  
| Convert a 2D point on the projection plane in 3D space.
[More...](../../de/daf/classBase_1_1ViewProjMethod.html#a9ef0f551ec2a1d352cb7a084b2b27c87)  
  
virtual [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) | [inverse](../../de/daf/classBase_1_1ViewProjMethod.html#a10eafa0b0e6ed6471f54f0430be7c161) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclPt) const =0  
| Convert a 2D point on the projection plane in 3D space.
[More...](../../de/daf/classBase_1_1ViewProjMethod.html#a10eafa0b0e6ed6471f54f0430be7c161)  
  
virtual [bool](../../d9/db9/classbool.html) | [isValid](../../de/daf/classBase_1_1ViewProjMethod.html#a889df391c806bf27ce6c3d47e81c1a74) () const  
virtual [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [operator()](../../de/daf/classBase_1_1ViewProjMethod.html#a8687d681b532a9edfe6fb116f115a9b1) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclPt) const =0  
| Convert 3D point to 2D projection plane.
[More...](../../de/daf/classBase_1_1ViewProjMethod.html#a8687d681b532a9edfe6fb116f115a9b1)  
  
virtual [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) | [operator()](../../de/daf/classBase_1_1ViewProjMethod.html#ac0952edb36da2eacb57ca71a58e310c9) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclPt) const =0  
| Convert 3D point to 2D projection plane.
[More...](../../de/daf/classBase_1_1ViewProjMethod.html#ac0952edb36da2eacb57ca71a58e310c9)  
  
[ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html) & | [operator=](../../de/daf/classBase_1_1ViewProjMethod.html#ac0b430e2a89529c0a2686b84d864670e) (const [ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html) &)=default  
void | [setTransform](../../de/daf/classBase_1_1ViewProjMethod.html#aa4fcdfec04d41e5ffd00a31276482187) (const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &)  
| Apply an additional transformation to the input points.
[More...](../../de/daf/classBase_1_1ViewProjMethod.html#aa4fcdfec04d41e5ffd00a31276482187)  
  
|
[ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#a00acaa738ba7673d4af7afde39915c88)
(const [ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html)
&)=default  
virtual | [~ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#a1daf8d726bb6fcfee0aa03baa6034d86) ()=default  
  
##  Protected Attributes  
  
---  
[bool](../../d9/db9/classbool.html) | [isOrthographic](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a80a6bb19fdac36a58d2ce7887a4ac45b)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Protected Member Functions inherited from
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html)  
void | [transformInput](../../de/daf/classBase_1_1ViewProjMethod.html#a8b9363eea34c10bab6011fb03cffce2f) (const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &, [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &) const  
void | [transformInput](../../de/daf/classBase_1_1ViewProjMethod.html#a0d4e7b5b68a466fa99e9fc4f9863924b) (const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &, [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &) const  
|
[ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#a5d0e28fc9104dafc798d47c45633a76e)
()  
  
## Detailed Description

The [ViewProjMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html "The
ViewProjMatrix class returns the result of the multiplication of the 3D vector
and the view trans...") class returns the result of the multiplication of the
3D vector and the view transformation matrix.

## Constructor & Destructor Documentation

## ◆ ViewProjMatrix()

ViewProjMatrix::ViewProjMatrix  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtx_| ) |   
---|---|---|---|---|---  
  
References
[isOrthographic](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a80a6bb19fdac36a58d2ce7887a4ac45b).

## Member Function Documentation

## ◆ getProjectionMatrix()

| [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) ViewProjMatrix::getProjectionMatrix  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Calculate the projection (+ mapping) matrix.

Implements
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#ae30c910881bad2a3d4acfe896f012a6e).

References
[isOrthographic](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a80a6bb19fdac36a58d2ce7887a4ac45b),
[Base::Matrix4D::move()](../../d5/db4/classBase_1_1Matrix4D.html#ac26497380187a175bcd5e43a0c81740f),
and
[Base::Matrix4D::scale()](../../d5/db4/classBase_1_1Matrix4D.html#aa0838e1c628e3f405a83904679acec56).

## ◆ inverse() [1/2]

| [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) ViewProjMatrix::inverse  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Convert a 2D point on the projection plane in 3D space.

Implements
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#a9ef0f551ec2a1d352cb7a084b2b27c87).

References
[isOrthographic](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a80a6bb19fdac36a58d2ce7887a4ac45b),
and [Base::Vector3< _Precision
>::Set()](../../d1/d13/classBase_1_1Vector3.html#a961b4f52c806809737f1d6fe18c8f9f6).

## ◆ inverse() [2/2]

| [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) ViewProjMatrix::inverse  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Convert a 2D point on the projection plane in 3D space.

Implements
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#a10eafa0b0e6ed6471f54f0430be7c161).

References
[isOrthographic](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a80a6bb19fdac36a58d2ce7887a4ac45b),
and [Base::Vector3< _Precision
>::Set()](../../d1/d13/classBase_1_1Vector3.html#a961b4f52c806809737f1d6fe18c8f9f6).

## ◆ operator()() [1/2]

| [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) ViewProjMatrix::operator()  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Convert 3D point to 2D projection plane.

Implements
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#a8687d681b532a9edfe6fb116f115a9b1).

References
[isOrthographic](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a80a6bb19fdac36a58d2ce7887a4ac45b),
and
[Base::ViewProjMethod::transformInput()](../../de/daf/classBase_1_1ViewProjMethod.html#a0d4e7b5b68a466fa99e9fc4f9863924b).

## ◆ operator()() [2/2]

| [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) ViewProjMatrix::operator()  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Convert 3D point to 2D projection plane.

Implements
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#ac0952edb36da2eacb57ca71a58e310c9).

References
[isOrthographic](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a80a6bb19fdac36a58d2ce7887a4ac45b),
and
[Base::ViewProjMethod::transformInput()](../../de/daf/classBase_1_1ViewProjMethod.html#a0d4e7b5b68a466fa99e9fc4f9863924b).

## Member Data Documentation

## ◆ isOrthographic

| [bool](../../d9/db9/classbool.html) Base::ViewProjMatrix::isOrthographic  
---  
protected  
  
Referenced by
[getProjectionMatrix()](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a9c88e958a0eabeaa0942715bec0606bb),
[inverse()](../../dd/dc2/classBase_1_1ViewProjMatrix.html#ae9f20859b62da577c761b873751255eb),
[operator()()](../../dd/dc2/classBase_1_1ViewProjMatrix.html#acbb267b3278e425ae7e338bb6434b635),
and
[ViewProjMatrix()](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a142a4cfdb0cbee29908ec0b07f8085c0).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/ViewProj.h
  * FreeCAD/src/Base/ViewProj.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

