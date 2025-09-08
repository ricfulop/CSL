---
url: https://freecad.github.io/SourceDoc/d5/d61/classBase_1_1Axis.html
scraped_at: 2025-09-08T15:15:37.664202
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Axis](../../d5/d61/classBase_1_1Axis.html)

[List of all members](../../df/dbb/classBase_1_1Axis-members.html) | Public Member Functions

Base::Axis Class Reference

The [Axis](../../d5/d61/classBase_1_1Axis.html "The Axis class.") class.
[More...](../../d5/d61/classBase_1_1Axis.html#details)

`#include <Axis.h>`

##  Public Member Functions  
  
---  
|
[Axis](../../d5/d61/classBase_1_1Axis.html#a6c75518dd377795286113256c19e1ebd)
()  
| default constructor
[More...](../../d5/d61/classBase_1_1Axis.html#a6c75518dd377795286113256c19e1ebd)  
  
|
[Axis](../../d5/d61/classBase_1_1Axis.html#a1b1be7f8d4a3c5afcb808922de5d1f8c)
(const [Axis](../../d5/d61/classBase_1_1Axis.html) &)  
|
[Axis](../../d5/d61/classBase_1_1Axis.html#a6fa658996e62506bc00a1763130d7371)
(const
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e)
&Orig, const
[Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e)
&Dir)  
const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | [getBase](../../d5/d61/classBase_1_1Axis.html#a62b47dae4e268abd7864512238e9c99a) () const  
const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | [getDirection](../../d5/d61/classBase_1_1Axis.html#a6308021e5e03eb134158c93ab63b6a67) () const  
void | [move](../../d5/d61/classBase_1_1Axis.html#a27ce30580e7d1a667a5cd19315806f78) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &MovVec)  
[bool](../../d9/db9/classbool.html) | [operator!=](../../d5/d61/classBase_1_1Axis.html#a615b2c5052dbbf0dd634435723ecd7fb) (const [Axis](../../d5/d61/classBase_1_1Axis.html) &) const  
[Axis](../../d5/d61/classBase_1_1Axis.html) | [operator*](../../d5/d61/classBase_1_1Axis.html#a14b173ca79afbd654fe52c7516aa34ec) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &p) const  
[Axis](../../d5/d61/classBase_1_1Axis.html) & | [operator*=](../../d5/d61/classBase_1_1Axis.html#a98afa9619a103f49592ed4f89769e3f6) (const [Placement](../../d1/d10/classBase_1_1Placement.html) &p)  
| Operators.
[More...](../../d5/d61/classBase_1_1Axis.html#a98afa9619a103f49592ed4f89769e3f6)  
  
[Axis](../../d5/d61/classBase_1_1Axis.html) & | [operator=](../../d5/d61/classBase_1_1Axis.html#a8b63f0806afbfa717c76acb15d855d9b) (const [Axis](../../d5/d61/classBase_1_1Axis.html) &)  
[bool](../../d9/db9/classbool.html) | [operator==](../../d5/d61/classBase_1_1Axis.html#a6c9795f0f60f34596a7170298bc28839) (const [Axis](../../d5/d61/classBase_1_1Axis.html) &) const  
void | [reverse](../../d5/d61/classBase_1_1Axis.html#a5550e8e7cb649af26d8061e78138f1ba) ()  
[Axis](../../d5/d61/classBase_1_1Axis.html) | [reversed](../../d5/d61/classBase_1_1Axis.html#a4734890cdc92ccdde65069fc5329d0a6) () const  
void | [setBase](../../d5/d61/classBase_1_1Axis.html#aee269e870703d1ba8e019352cd1ef446) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &Orig)  
void | [setDirection](../../d5/d61/classBase_1_1Axis.html#a1541dfba8e577785325efffbe5c6d01b) (const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &Dir)  
|
[~Axis](../../d5/d61/classBase_1_1Axis.html#a7b6e232557c4b17e3ecc425ea47a7c1c)
()  
| Destruction.
[More...](../../d5/d61/classBase_1_1Axis.html#a7b6e232557c4b17e3ecc425ea47a7c1c)  
  
  
## Detailed Description

The [Axis](../../d5/d61/classBase_1_1Axis.html "The Axis class.") class.

## Constructor & Destructor Documentation

## ◆ Axis() [1/3]

Axis::Axis  | ( | | ) |   
---|---|---|---|---  
  
default constructor

## ◆ Axis() [2/3]

Axis::Axis  | ( | const [Axis](../../d5/d61/classBase_1_1Axis.html) & | _that_| ) |   
---|---|---|---|---|---  
  
## ◆ Axis() [3/3]

Axis::Axis  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _Orig_ ,   
---|---|---|---  
|  | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _Dir_  
| ) | |   
  
## ◆ ~Axis()

Base::Axis::~Axis  | ( | | ) |   
---|---|---|---|---  
  
Destruction.

## Member Function Documentation

## ◆ getBase()

const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & Base::Axis::getBase  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Base::CoordinateSystem::displacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
and
[Base::CoordinateSystem::transformTo()](../../d1/d66/classBase_1_1CoordinateSystem.html#a558771f4a8922fe4ae72c200222de704).

## ◆ getDirection()

const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & Base::Axis::getDirection  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Base::CoordinateSystem::displacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#a8aab6d1121b6a2a18551cde8199fb970),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[Base::CoordinateSystem::setXDirection()](../../d1/d66/classBase_1_1CoordinateSystem.html#a7f2a242ff6094d1743686222ed37192d),
[Base::CoordinateSystem::setYDirection()](../../d1/d66/classBase_1_1CoordinateSystem.html#ad0bcb826af0de6e8e256cae84dccbd26),
and
[Base::CoordinateSystem::transform()](../../d1/d66/classBase_1_1CoordinateSystem.html#a657dcb4562b4fc19a0db0f2724b7f31d).

## ◆ move()

void Axis::move  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _MovVec_| ) |   
---|---|---|---|---|---  
  
Referenced by
[draftguitools.gui_circulararray.CircularArray::Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
and
[draftguitools.gui_polararray.PolarArray::Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) Axis::operator!=  | ( | const [Axis](../../d5/d61/classBase_1_1Axis.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator*()

[Axis](../../d5/d61/classBase_1_1Axis.html) Axis::operator*  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _p_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator*=()

[Axis](../../d5/d61/classBase_1_1Axis.html) & Axis::operator*=  | ( | const [Placement](../../d1/d10/classBase_1_1Placement.html) & | _p_| ) |   
---|---|---|---|---|---  
  
Operators.

## ◆ operator=()

[Axis](../../d5/d61/classBase_1_1Axis.html) & Axis::operator=  | ( | const [Axis](../../d5/d61/classBase_1_1Axis.html) & | _New_| ) |   
---|---|---|---|---|---  
  
## ◆ operator==()

[bool](../../d9/db9/classbool.html) Axis::operator==  | ( | const [Axis](../../d5/d61/classBase_1_1Axis.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
## ◆ reverse()

void Axis::reverse  | ( | | ) |   
---|---|---|---|---  
  
## ◆ reversed()

[Axis](../../d5/d61/classBase_1_1Axis.html) Axis::reversed  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ setBase()

void Base::Axis::setBase  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _Orig_| ) |   
---|---|---|---|---|---  
  
Referenced by
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[Base::CoordinateSystem::setAxes()](../../d1/d66/classBase_1_1CoordinateSystem.html#aa739d8948fc7bc060cd5fdbc22f90d93),
and
[Base::CoordinateSystem::setPlacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#aab4206e93f3d31f3e8db6fc5aab88132).

## ◆ setDirection()

void Base::Axis::setDirection  | ( | const [Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _Dir_| ) |   
---|---|---|---|---|---  
  
Referenced by
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[Base::CoordinateSystem::setAxes()](../../d1/d66/classBase_1_1CoordinateSystem.html#aa739d8948fc7bc060cd5fdbc22f90d93),
[Base::CoordinateSystem::setPlacement()](../../d1/d66/classBase_1_1CoordinateSystem.html#aab4206e93f3d31f3e8db6fc5aab88132),
and
[Base::CoordinateSystem::transform()](../../d1/d66/classBase_1_1CoordinateSystem.html#a657dcb4562b4fc19a0db0f2724b7f31d).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Axis.h
  * FreeCAD/src/Base/Axis.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

