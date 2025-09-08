---
url: https://freecad.github.io/SourceDoc/df/d75/classBase_1_1TimeInfo.html
scraped_at: 2025-09-08T15:17:29.145872
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html)

[List of all members](../../d2/d55/classBase_1_1TimeInfo-members.html) | Public Member Functions | Static Public Member Functions

Base::TimeInfo Class Reference

[BaseClass](../../df/d4d/classBase_1_1BaseClass.html "BaseClass class and root
of the type system.") class and root of the type system.
[More...](../../df/d75/classBase_1_1TimeInfo.html#details)

`#include <TimeInfo.h>`

##  Public Member Functions  
  
---  
unsigned short | [getMiliseconds](../../df/d75/classBase_1_1TimeInfo.html#aa0d8ae3449554e7a78c46d2a2c3dc2b6) () const  
int64_t | [getSeconds](../../df/d75/classBase_1_1TimeInfo.html#a7a472dacd2bdbfe413cfd7f60fdbcbee) () const  
[bool](../../d9/db9/classbool.html) | [isNull](../../df/d75/classBase_1_1TimeInfo.html#abb2898bed5609b834a1f0d6bf0a3842d) () const  
[bool](../../d9/db9/classbool.html) | [operator!=](../../df/d75/classBase_1_1TimeInfo.html#a42dc59af47f38d6229dbfbb6ade8c0e4) (const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &time) const  
[bool](../../d9/db9/classbool.html) | [operator<](../../df/d75/classBase_1_1TimeInfo.html#ad43195e849654ed258fba1ed3ba38a2a) (const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &time) const  
[bool](../../d9/db9/classbool.html) | [operator<=](../../df/d75/classBase_1_1TimeInfo.html#a4acf9235806d264806fc524027b7d8f2) (const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &time) const  
void | [operator=](../../df/d75/classBase_1_1TimeInfo.html#ad9b2f1e01876cce29085650331cc8591) (const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &time)  
[bool](../../d9/db9/classbool.html) | [operator==](../../df/d75/classBase_1_1TimeInfo.html#ae5a7ace6afa033d76083f665433dc830) (const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &time) const  
[bool](../../d9/db9/classbool.html) | [operator>](../../df/d75/classBase_1_1TimeInfo.html#ac747a7eed063eafbf5d345c84c1d4034) (const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &time) const  
[bool](../../d9/db9/classbool.html) | [operator>=](../../df/d75/classBase_1_1TimeInfo.html#a2900f38fb48681b5f14e7ef5cd753fb4) (const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &time) const  
void | [setCurrent](../../df/d75/classBase_1_1TimeInfo.html#aab570c5858756ea01cafe8ef140beff6) ()  
| sets the object to the actual system time
[More...](../../df/d75/classBase_1_1TimeInfo.html#aab570c5858756ea01cafe8ef140beff6)  
  
void | [setTime_t](../../df/d75/classBase_1_1TimeInfo.html#ae874a0ed3ec680b6f1aefba28ec6974c) (int64_t seconds)  
|
[TimeInfo](../../df/d75/classBase_1_1TimeInfo.html#a1d7ab6bb93daed40392a2ccdce69e1d4)
()  
| Construction.
[More...](../../df/d75/classBase_1_1TimeInfo.html#a1d7ab6bb93daed40392a2ccdce69e1d4)  
  
|
[TimeInfo](../../df/d75/classBase_1_1TimeInfo.html#a6c0b8d7562c6d33432ed14cbc89ff144)
(const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &)=default  
virtual | [~TimeInfo](../../df/d75/classBase_1_1TimeInfo.html#a553ed66820f2e871447475f953cc5a54) ()  
| Destruction.
[More...](../../df/d75/classBase_1_1TimeInfo.html#a553ed66820f2e871447475f953cc5a54)  
  
  
##  Static Public Member Functions  
  
---  
static std::string | [currentDateTimeString](../../df/d75/classBase_1_1TimeInfo.html#a395c874b184fdb4fc9ffc90fb4714371) ()  
static std::string | [diffTime](../../df/d75/classBase_1_1TimeInfo.html#a8b5ce5eead960b6c7b9b18c373dfe4c1) (const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &timeStart, const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &timeEnd=[TimeInfo](../../df/d75/classBase_1_1TimeInfo.html)())  
static float | [diffTimeF](../../df/d75/classBase_1_1TimeInfo.html#a91c634b9014abe8449a4a478f01f655f) (const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &timeStart, const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) &timeEnd=[TimeInfo](../../df/d75/classBase_1_1TimeInfo.html)())  
static [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) | [null](../../df/d75/classBase_1_1TimeInfo.html#a1f75ecad31f55a21884ea6a36af41a67) ()  
  
## Detailed Description

[BaseClass](../../df/d4d/classBase_1_1BaseClass.html "BaseClass class and root
of the type system.") class and root of the type system.

## Constructor & Destructor Documentation

## ◆ TimeInfo() [1/2]

TimeInfo::TimeInfo  | ( | | ) |   
---|---|---|---|---  
  
Construction.

A constructor.

A more elaborate description of the constructor.

References
[setCurrent()](../../df/d75/classBase_1_1TimeInfo.html#aab570c5858756ea01cafe8ef140beff6).

## ◆ TimeInfo() [2/2]

| Base::TimeInfo::TimeInfo  | ( | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## ◆ ~TimeInfo()

| TimeInfo::~TimeInfo  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Destruction.

A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ currentDateTimeString()

| std::string TimeInfo::currentDateTimeString  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[Cloud::Module::cloudSave()](../../d9/d80/classCloud_1_1Module.html#a6849376c6a9d04c93cd195d3c6bd9f71),
[App::Document::Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
and
[App::Document::save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c).

## ◆ diffTime()

| std::string TimeInfo::diffTime  | ( | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _timeStart_ ,   
---|---|---|---  
|  | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _timeEnd_ = `[TimeInfo](../../df/d75/classBase_1_1TimeInfo.html)()`  
| ) | |   
static  
  
References
[diffTimeF()](../../df/d75/classBase_1_1TimeInfo.html#a91c634b9014abe8449a4a478f01f655f).

Referenced by
[Sketcher::Sketch::setUpSketch()](../../d9/d9b/classSketcher_1_1Sketch.html#aecd77c1e32780817ae5b1f15036993d2),
and
[Sketcher::Sketch::solve()](../../d9/d9b/classSketcher_1_1Sketch.html#a1c59ce1dfdd62862e4ef98fe0aad50d5).

## ◆ diffTimeF()

| float TimeInfo::diffTimeF  | ( | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _timeStart_ ,   
---|---|---|---  
|  | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _timeEnd_ = `[TimeInfo](../../df/d75/classBase_1_1TimeInfo.html)()`  
| ) | |   
static  
  
References
[getMiliseconds()](../../df/d75/classBase_1_1TimeInfo.html#aa0d8ae3449554e7a78c46d2a2c3dc2b6),
and
[getSeconds()](../../df/d75/classBase_1_1TimeInfo.html#a7a472dacd2bdbfe413cfd7f60fdbcbee).

Referenced by
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[GCS::System::diagnose()](../../db/d28/classGCS_1_1System.html#ae239feb89ff7b144d842d954d5fbcf74),
[diffTime()](../../df/d75/classBase_1_1TimeInfo.html#a8b5ce5eead960b6c7b9b18c373dfe4c1),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
[Fem::FemVTKTools::readVTKMesh()](../../d6/d26/classFem_1_1FemVTKTools.html#a5c072865883df9f3a7141773d33534e6),
[Sketcher::Sketch::solve()](../../d9/d9b/classSketcher_1_1Sketch.html#a1c59ce1dfdd62862e4ef98fe0aad50d5),
[PartGui::ViewProviderPartExt::updateVisual()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a96cb6b96c8dfb082a135a31c4f554167),
[Fem::FemVTKTools::writeResult()](../../d6/d26/classFem_1_1FemVTKTools.html#afe10808623915c79b6e74786a6f6d0e3),
and
[Fem::FemVTKTools::writeVTKMesh()](../../d6/d26/classFem_1_1FemVTKTools.html#afd566b7765038482398e5775f8babc02).

## ◆ getMiliseconds()

unsigned short Base::TimeInfo::getMiliseconds  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[diffTimeF()](../../df/d75/classBase_1_1TimeInfo.html#a91c634b9014abe8449a4a478f01f655f).

## ◆ getSeconds()

int64_t Base::TimeInfo::getSeconds  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[diffTimeF()](../../df/d75/classBase_1_1TimeInfo.html#a91c634b9014abe8449a4a478f01f655f).

## ◆ isNull()

[bool](../../d9/db9/classbool.html) TimeInfo::isNull  | ( | | ) |  const  
---|---|---|---|---  
  
References
[null()](../../df/d75/classBase_1_1TimeInfo.html#a1f75ecad31f55a21884ea6a36af41a67).

## ◆ null()

| [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) TimeInfo::null  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[isNull()](../../df/d75/classBase_1_1TimeInfo.html#abb2898bed5609b834a1f0d6bf0a3842d),
[Base::FileInfo::lastModified()](../../dd/d34/classBase_1_1FileInfo.html#aa87adf0f1e8c32d54ff01bbcf64dfff8),
and
[Base::FileInfo::lastRead()](../../dd/d34/classBase_1_1FileInfo.html#a8d2e7762c1ce1c3ca606d2d3bda0bff0).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) Base::TimeInfo::operator!=  | ( | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _time_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator<()

[bool](../../d9/db9/classbool.html) Base::TimeInfo::operator< | ( | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _time_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator<=()

[bool](../../d9/db9/classbool.html) Base::TimeInfo::operator<=  | ( | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _time_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator=()

void Base::TimeInfo::operator=  | ( | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _time_| ) |   
---|---|---|---|---|---  
  
## ◆ operator==()

[bool](../../d9/db9/classbool.html) Base::TimeInfo::operator==  | ( | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _time_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator>()

[bool](../../d9/db9/classbool.html) Base::TimeInfo::operator> | ( | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _time_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator>=()

[bool](../../d9/db9/classbool.html) Base::TimeInfo::operator>=  | ( | const [TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) & | _time_| ) |  const  
---|---|---|---|---|---  
  
## ◆ setCurrent()

void TimeInfo::setCurrent  | ( | | ) |   
---|---|---|---|---  
  
sets the object to the actual system time

Referenced by
[TimeInfo()](../../df/d75/classBase_1_1TimeInfo.html#a1d7ab6bb93daed40392a2ccdce69e1d4).

## ◆ setTime_t()

void TimeInfo::setTime_t  | ( | int64_t  | _seconds_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Base::FileInfo::lastModified()](../../dd/d34/classBase_1_1FileInfo.html#aa87adf0f1e8c32d54ff01bbcf64dfff8),
and
[Base::FileInfo::lastRead()](../../dd/d34/classBase_1_1FileInfo.html#a8d2e7762c1ce1c3ca606d2d3bda0bff0).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/TimeInfo.h
  * FreeCAD/src/Base/TimeInfo.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

