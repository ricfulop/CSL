---
url: https://freecad.github.io/SourceDoc/dc/d5f/structApp_1_1Meta_1_1Version.html
scraped_at: 2025-09-08T14:53:39.223525
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Meta](../../d9/dcf/namespaceApp_1_1Meta.html)
  * [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html)

[List of all members](../../dc/d7f/structApp_1_1Meta_1_1Version-members.html) | Public Member Functions | Public Attributes

App::Meta::Version Struct Reference

A semantic version structure providing comparison operators and conversion to
and from std::string.
[More...](../../dc/d5f/structApp_1_1Meta_1_1Version.html#details)

`#include <Metadata.h>`

##  Public Member Functions  
  
---  
[bool](../../d9/db9/classbool.html) | [operator!=](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ab739ec0a18e0319d6df78c83b12829d1) (const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) &) const  
[bool](../../d9/db9/classbool.html) | [operator<](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a355d9606d141ec3e29531425b64b0293) (const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) &) const  
[bool](../../d9/db9/classbool.html) | [operator<=](../../dc/d5f/structApp_1_1Meta_1_1Version.html#aa903e07443e59d32ceceaa27f4f7590c) (const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) &) const  
[bool](../../d9/db9/classbool.html) | [operator==](../../dc/d5f/structApp_1_1Meta_1_1Version.html#adc350a3df00416080351ab69f06016ee) (const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) &) const  
[bool](../../d9/db9/classbool.html) | [operator>](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a19068ce459e2700a7f243112d16a19f3) (const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) &) const  
[bool](../../d9/db9/classbool.html) | [operator>=](../../dc/d5f/structApp_1_1Meta_1_1Version.html#af01290e72fba218c10aa5677ccbf00e1) (const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) &) const  
std::string | [str](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ab2531908583c5de80b92562cc44b2af2) () const  
|
[Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a359637fd012bd72bbe6487730a8bc1b8)
()  
|
[Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html#af5a741f6ae172384c792fefd4df00bdd)
(const std::string &semanticString)  
|
[Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a2a068c82642f9df6b8612a0bf8adc34a)
([int](../../d1/da0/classint.html)
[major](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a075579d99ac184de80654d64868821d1),
[int](../../d1/da0/classint.html)
[minor](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a4a3fd0eb246556324e29ae34a7c0948b)=0,
[int](../../d1/da0/classint.html)
[patch](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ad159e6385868363580a0b1139f4f10fc)=0,
const std::string
&[suffix](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a951572a0730bcdbb12f8201a66c97c93)=std::string())  
  
##  Public Attributes  
  
---  
[int](../../d1/da0/classint.html) | [major](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a075579d99ac184de80654d64868821d1)  
[int](../../d1/da0/classint.html) | [minor](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a4a3fd0eb246556324e29ae34a7c0948b)  
[int](../../d1/da0/classint.html) | [patch](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ad159e6385868363580a0b1139f4f10fc)  
std::string | [suffix](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a951572a0730bcdbb12f8201a66c97c93)  
  
## Detailed Description

A semantic version structure providing comparison operators and conversion to
and from std::string.

## Constructor & Destructor Documentation

## ◆ Version() [1/3]

Meta::Version::Version  | ( | | ) |   
---|---|---|---|---  
  
## ◆ Version() [2/3]

Meta::Version::Version  | ( | [int](../../d1/da0/classint.html) | _major_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _minor_ = `0`,   
|  | [int](../../d1/da0/classint.html) | _patch_ = `0`,   
|  | const std::string & | _suffix_ = `std::string()`  
| ) | |   
  
## ◆ Version() [3/3]

| Meta::Version::Version  | ( | const std::string & | _semanticString_| ) |   
---|---|---|---|---|---  
explicit  
  
References
[major](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a075579d99ac184de80654d64868821d1),
[minor](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a4a3fd0eb246556324e29ae34a7c0948b),
[patch](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ad159e6385868363580a0b1139f4f10fc),
and
[suffix](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a951572a0730bcdbb12f8201a66c97c93).

## Member Function Documentation

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) Meta::Version::operator!=  | ( | const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) & | _rhs_| ) |  const  
---|---|---|---|---|---  
  
References
[major](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a075579d99ac184de80654d64868821d1),
[minor](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a4a3fd0eb246556324e29ae34a7c0948b),
[patch](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ad159e6385868363580a0b1139f4f10fc),
and
[suffix](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a951572a0730bcdbb12f8201a66c97c93).

## ◆ operator<()

[bool](../../d9/db9/classbool.html) Meta::Version::operator< | ( | const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) & | _rhs_| ) |  const  
---|---|---|---|---|---  
  
References
[major](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a075579d99ac184de80654d64868821d1),
[minor](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a4a3fd0eb246556324e29ae34a7c0948b),
[patch](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ad159e6385868363580a0b1139f4f10fc),
and
[suffix](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a951572a0730bcdbb12f8201a66c97c93).

## ◆ operator<=()

[bool](../../d9/db9/classbool.html) Meta::Version::operator<=  | ( | const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) & | _rhs_| ) |  const  
---|---|---|---|---|---  
  
References
[major](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a075579d99ac184de80654d64868821d1),
[minor](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a4a3fd0eb246556324e29ae34a7c0948b),
[patch](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ad159e6385868363580a0b1139f4f10fc),
and
[suffix](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a951572a0730bcdbb12f8201a66c97c93).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) Meta::Version::operator==  | ( | const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) & | _rhs_| ) |  const  
---|---|---|---|---|---  
  
References
[major](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a075579d99ac184de80654d64868821d1),
[minor](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a4a3fd0eb246556324e29ae34a7c0948b),
[patch](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ad159e6385868363580a0b1139f4f10fc),
and
[suffix](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a951572a0730bcdbb12f8201a66c97c93).

## ◆ operator>()

[bool](../../d9/db9/classbool.html) Meta::Version::operator> | ( | const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) & | _rhs_| ) |  const  
---|---|---|---|---|---  
  
References
[major](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a075579d99ac184de80654d64868821d1),
[minor](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a4a3fd0eb246556324e29ae34a7c0948b),
[patch](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ad159e6385868363580a0b1139f4f10fc),
and
[suffix](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a951572a0730bcdbb12f8201a66c97c93).

## ◆ operator>=()

[bool](../../d9/db9/classbool.html) Meta::Version::operator>=  | ( | const [Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) & | _rhs_| ) |  const  
---|---|---|---|---|---  
  
References
[major](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a075579d99ac184de80654d64868821d1),
[minor](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a4a3fd0eb246556324e29ae34a7c0948b),
[patch](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ad159e6385868363580a0b1139f4f10fc),
and
[suffix](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a951572a0730bcdbb12f8201a66c97c93).

## ◆ str()

std::string Meta::Version::str  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Gui::Dialog::AboutDialog::on_copyButton_clicked()](../../d5/de0/classGui_1_1Dialog_1_1AboutDialog.html#a907ddd1537ac512ba4859ee2fb4575a6).

## Member Data Documentation

## ◆ major

[int](../../d1/da0/classint.html) App::Meta::Version::major  
---  
  
Referenced by
[operator!=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ab739ec0a18e0319d6df78c83b12829d1),
[operator<()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a355d9606d141ec3e29531425b64b0293),
[operator<=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#aa903e07443e59d32ceceaa27f4f7590c),
[operator==()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#adc350a3df00416080351ab69f06016ee),
[operator>()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a19068ce459e2700a7f243112d16a19f3),
[operator>=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#af01290e72fba218c10aa5677ccbf00e1),
and
[Version()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#af5a741f6ae172384c792fefd4df00bdd).

## ◆ minor

[int](../../d1/da0/classint.html) App::Meta::Version::minor  
---  
  
Referenced by
[operator!=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ab739ec0a18e0319d6df78c83b12829d1),
[operator<()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a355d9606d141ec3e29531425b64b0293),
[operator<=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#aa903e07443e59d32ceceaa27f4f7590c),
[operator==()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#adc350a3df00416080351ab69f06016ee),
[operator>()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a19068ce459e2700a7f243112d16a19f3),
[operator>=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#af01290e72fba218c10aa5677ccbf00e1),
and
[Version()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#af5a741f6ae172384c792fefd4df00bdd).

## ◆ patch

[int](../../d1/da0/classint.html) App::Meta::Version::patch  
---  
  
Referenced by
[operator!=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ab739ec0a18e0319d6df78c83b12829d1),
[operator<()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a355d9606d141ec3e29531425b64b0293),
[operator<=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#aa903e07443e59d32ceceaa27f4f7590c),
[operator==()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#adc350a3df00416080351ab69f06016ee),
[operator>()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a19068ce459e2700a7f243112d16a19f3),
[operator>=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#af01290e72fba218c10aa5677ccbf00e1),
and
[Version()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#af5a741f6ae172384c792fefd4df00bdd).

## ◆ suffix

std::string App::Meta::Version::suffix  
---  
  
Referenced by
[operator!=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#ab739ec0a18e0319d6df78c83b12829d1),
[operator<()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a355d9606d141ec3e29531425b64b0293),
[operator<=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#aa903e07443e59d32ceceaa27f4f7590c),
[operator==()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#adc350a3df00416080351ab69f06016ee),
[operator>()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#a19068ce459e2700a7f243112d16a19f3),
[operator>=()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#af01290e72fba218c10aa5677ccbf00e1),
and
[Version()](../../dc/d5f/structApp_1_1Meta_1_1Version.html#af5a741f6ae172384c792fefd4df00bdd).

* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/App/Metadata.h
  * FreeCAD/src/App/Metadata.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

