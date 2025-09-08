---
url: https://freecad.github.io/SourceDoc/d7/dfc/classBase_1_1ViewOrthoProjMatrix.html
scraped_at: 2025-09-08T15:18:11.326007
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [ViewOrthoProjMatrix](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html)

[List of all members](../../d4/df1/classBase_1_1ViewOrthoProjMatrix-members.html) | Public Member Functions

Base::ViewOrthoProjMatrix Class Reference

The [ViewOrthoProjMatrix](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html
"The ViewOrthoProjMatrix class returns the result of the multiplication of the
3D vector and the trans...") class returns the result of the multiplication of
the 3D vector and the transformation matrix.
[More...](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#details)

`#include <ViewProj.h>`

##  Public Member Functions  
  
---  
[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [getProjectionMatrix](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#a910cb9e05cf5ca5a8f7164b33b8ee9e6) () const  
| Calculate the projection (+ mapping) matrix.
[More...](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#a910cb9e05cf5ca5a8f7164b33b8ee9e6)  
  
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [inverse](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#a77bc2996fc046bd455ba492643911289) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclPt) const  
| Convert a 2D point on the projection plane in 3D space.
[More...](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#a77bc2996fc046bd455ba492643911289)  
  
[Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) | [inverse](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#a10c757cc63c435c8486584e55b5be877) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclPt) const  
| Convert a 2D point on the projection plane in 3D space.
[More...](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#a10c757cc63c435c8486584e55b5be877)  
  
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [operator()](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#aa49d54ca0a502e53b2c0098159c5547d) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &rclPt) const  
| Convert 3D point to 2D projection plane.
[More...](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#aa49d54ca0a502e53b2c0098159c5547d)  
  
[Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) | [operator()](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#adfa9a0b6157556a2cb93a490002ad8e4) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rclPt) const  
| Convert 3D point to 2D projection plane.
[More...](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#adfa9a0b6157556a2cb93a490002ad8e4)  
  
|
[ViewOrthoProjMatrix](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#a170e1159fa92fa60b53b89ecbbb44660)
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

The [ViewOrthoProjMatrix](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html
"The ViewOrthoProjMatrix class returns the result of the multiplication of the
3D vector and the trans...") class returns the result of the multiplication of
the 3D vector and the transformation matrix.

Unlike [ViewProjMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html "The
ViewProjMatrix class returns the result of the multiplication of the 3D vector
and the view trans...") this class is not supposed to project points onto a
viewport but project points onto a plane in 3D.

## Constructor & Destructor Documentation

## ◆ ViewOrthoProjMatrix()

ViewOrthoProjMatrix::ViewOrthoProjMatrix  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rclMtx_| ) |   
---|---|---|---|---|---  
  
## Member Function Documentation

## ◆ getProjectionMatrix()

| [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) ViewOrthoProjMatrix::getProjectionMatrix  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Calculate the projection (+ mapping) matrix.

Implements
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#ae30c910881bad2a3d4acfe896f012a6e).

## ◆ inverse() [1/2]

| [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) ViewOrthoProjMatrix::inverse  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Convert a 2D point on the projection plane in 3D space.

Implements
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#a9ef0f551ec2a1d352cb7a084b2b27c87).

## ◆ inverse() [2/2]

| [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) ViewOrthoProjMatrix::inverse  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Convert a 2D point on the projection plane in 3D space.

Implements
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#a10eafa0b0e6ed6471f54f0430be7c161).

## ◆ operator()() [1/2]

| [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) ViewOrthoProjMatrix::operator()  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Convert 3D point to 2D projection plane.

Implements
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#a8687d681b532a9edfe6fb116f115a9b1).

## ◆ operator()() [2/2]

| [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) ViewOrthoProjMatrix::operator()  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Convert 3D point to 2D projection plane.

Implements
[Base::ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#ac0952edb36da2eacb57ca71a58e310c9).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/ViewProj.h
  * FreeCAD/src/Base/ViewProj.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

