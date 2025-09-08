---
url: https://freecad.github.io/SourceDoc/de/daf/classBase_1_1ViewProjMethod.html
scraped_at: 2025-09-08T15:18:13.331239
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html)

[List of all members](../../d3/d7f/classBase_1_1ViewProjMethod-members.html) | Public Member Functions | Protected Member Functions

Base::ViewProjMethod Class Referenceabstract

Abstract base class for all project methods.
[More...](../../de/daf/classBase_1_1ViewProjMethod.html#details)

`#include <ViewProj.h>`

##  Public Member Functions  
  
---  
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
  
##  Protected Member Functions  
  
---  
void | [transformInput](../../de/daf/classBase_1_1ViewProjMethod.html#a8b9363eea34c10bab6011fb03cffce2f) (const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &, [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &) const  
void | [transformInput](../../de/daf/classBase_1_1ViewProjMethod.html#a0d4e7b5b68a466fa99e9fc4f9863924b) (const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &, [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &) const  
|
[ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html#a5d0e28fc9104dafc798d47c45633a76e)
()  
  
## Detailed Description

Abstract base class for all project methods.

## Constructor & Destructor Documentation

## ◆ ViewProjMethod() [1/2]

| Base::ViewProjMethod::ViewProjMethod  | ( | const [ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## ◆ ~ViewProjMethod()

| virtual Base::ViewProjMethod::~ViewProjMethod  | ( | | ) |   
---|---|---|---|---  
virtualdefault  
  
## ◆ ViewProjMethod() [2/2]

| ViewProjMethod::ViewProjMethod  | ( | | ) |   
---|---|---|---|---  
protected  
  
## Member Function Documentation

## ◆ getComposedProjectionMatrix()

[Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) ViewProjMethod::getComposedProjectionMatrix  | ( | | ) |  const  
---|---|---|---|---  
  
Calculate the composed projection matrix.

Calculate the composed projection matrix which is a product of projection
matrix multiplied with input transformation matrix.

References
[getProjectionMatrix()](../../de/daf/classBase_1_1ViewProjMethod.html#ae30c910881bad2a3d4acfe896f012a6e).

Referenced by
[MeshCore::MeshAlgorithm::CheckFacets()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#ac8032a5a0a06cee43035edcb9253b731).

## ◆ getProjectionMatrix()

| virtual [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) Base::ViewProjMethod::getProjectionMatrix  | ( | | ) |  const  
---|---|---|---|---  
pure virtual  
  
Calculate the projection (+ mapping) matrix.

Implemented in
[Base::ViewProjMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a9c88e958a0eabeaa0942715bec0606bb),
[Base::ViewOrthoProjMatrix](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#a910cb9e05cf5ca5a8f7164b33b8ee9e6),
and
[Gui::ViewVolumeProjection](../../d8/d4d/classGui_1_1ViewVolumeProjection.html#a8f9980f2e5fd6d5947b3ffdce8ea95f7).

Referenced by
[getComposedProjectionMatrix()](../../de/daf/classBase_1_1ViewProjMethod.html#a304b653764af8d3dc70afda41f570c2f).

## ◆ getTransform()

const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & Base::ViewProjMethod::getTransform  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ inverse() [1/2]

| virtual [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) Base::ViewProjMethod::inverse  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
pure virtual  
  
Convert a 2D point on the projection plane in 3D space.

Implemented in
[Gui::ViewVolumeProjection](../../d8/d4d/classGui_1_1ViewVolumeProjection.html#a0216e77a04855987d501aaec485c415d),
[Base::ViewProjMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html#aeca63d8a99d75084623b791f7ddecedf),
and
[Base::ViewOrthoProjMatrix](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#a77bc2996fc046bd455ba492643911289).

## ◆ inverse() [2/2]

| virtual [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) Base::ViewProjMethod::inverse  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
pure virtual  
  
Convert a 2D point on the projection plane in 3D space.

Implemented in
[Gui::ViewVolumeProjection](../../d8/d4d/classGui_1_1ViewVolumeProjection.html#a1d7fe268b671119971278bdf467133f2),
[Base::ViewProjMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html#ae9f20859b62da577c761b873751255eb),
and
[Base::ViewOrthoProjMatrix](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#a10c757cc63c435c8486584e55b5be877).

## ◆ isValid()

| [bool](../../d9/db9/classbool.html) ViewProjMethod::isValid  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
## ◆ operator()() [1/2]

| virtual [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) Base::ViewProjMethod::operator()  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
pure virtual  
  
Convert 3D point to 2D projection plane.

Implemented in
[Gui::ViewVolumeProjection](../../d8/d4d/classGui_1_1ViewVolumeProjection.html#a1adb4f476177452e72ebeb31bd79807f),
[Base::ViewProjMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html#a2ab5f7d1c73f3e080d25dd4ecbe1af10),
and
[Base::ViewOrthoProjMatrix](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#aa49d54ca0a502e53b2c0098159c5547d).

## ◆ operator()() [2/2]

| virtual [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) Base::ViewProjMethod::operator()  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rclPt_| ) |  const  
---|---|---|---|---|---  
pure virtual  
  
Convert 3D point to 2D projection plane.

Implemented in
[Gui::ViewVolumeProjection](../../d8/d4d/classGui_1_1ViewVolumeProjection.html#a3a056a53d844ef35d3cb580a94eb4c1b),
[Base::ViewProjMatrix](../../dd/dc2/classBase_1_1ViewProjMatrix.html#acbb267b3278e425ae7e338bb6434b635),
and
[Base::ViewOrthoProjMatrix](../../d7/dfc/classBase_1_1ViewOrthoProjMatrix.html#adfa9a0b6157556a2cb93a490002ad8e4).

## ◆ operator=()

| [ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html) & Base::ViewProjMethod::operator=  | ( | const [ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## ◆ setTransform()

void ViewProjMethod::setTransform  | ( | const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _mat_| ) |   
---|---|---|---|---|---  
  
Apply an additional transformation to the input points.

This method applies an additional transformation to the input points passed
with the () operator.

Parameters

     mat|   
---|---  
  
Referenced by
[MeshGui::ViewProviderMesh::clipMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a2163df57149a01e40800e85a88d3ce20),
and
[MeshGui::ViewProviderMesh::trimMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a99db0ab49ba22437ef202c633d752b52).

## ◆ transformInput() [1/2]

| void ViewProjMethod::transformInput  | ( | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _src_ ,   
---|---|---|---  
|  | [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _dst_  
| ) | |  const  
protected  
  
## ◆ transformInput() [2/2]

| void ViewProjMethod::transformInput  | ( | const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _src_ ,   
---|---|---|---  
|  | [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _dst_  
| ) | |  const  
protected  
  
Referenced by
[Gui::ViewVolumeProjection::operator()()](../../d8/d4d/classGui_1_1ViewVolumeProjection.html#a3a056a53d844ef35d3cb580a94eb4c1b),
and
[Base::ViewProjMatrix::operator()()](../../dd/dc2/classBase_1_1ViewProjMatrix.html#acbb267b3278e425ae7e338bb6434b635).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/ViewProj.h
  * FreeCAD/src/Base/ViewProj.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

