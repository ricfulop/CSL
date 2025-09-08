---
url: https://freecad.github.io/SourceDoc/d9/d07/classBase_1_1UnderflowError.html
scraped_at: 2025-09-08T15:17:36.173818
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [UnderflowError](../../d9/d07/classBase_1_1UnderflowError.html)

[List of all members](../../d6/dae/classBase_1_1UnderflowError-members.html) | Public Member Functions

Base::UnderflowError Class Reference

The [UnderflowError](../../d9/d07/classBase_1_1UnderflowError.html "The
UnderflowError can be used to indicate underflows of numbers.") can be used to
indicate underflows of numbers.
[More...](../../d9/d07/classBase_1_1UnderflowError.html#details)

`#include <Exception.h>`

##  Public Member Functions  
  
---  
[PyObject](../../df/d1b/classPyObject.html) * | [getPyExceptionType](../../d9/d07/classBase_1_1UnderflowError.html#a39a6fcbfec18fcf2b29ed95732605f79) () const override  
| returns the corresponding python exception type
[More...](../../d9/d07/classBase_1_1UnderflowError.html#a39a6fcbfec18fcf2b29ed95732605f79)  
  
|
[UnderflowError](../../d9/d07/classBase_1_1UnderflowError.html#a3536f6b97ac714f95b306be7c103ca2d)
()  
| Construction.
[More...](../../d9/d07/classBase_1_1UnderflowError.html#a3536f6b97ac714f95b306be7c103ca2d)  
  
|
[UnderflowError](../../d9/d07/classBase_1_1UnderflowError.html#acf779bff980fb450fd0d3c757a2f956a)
(const char *sMessage)  
|
[UnderflowError](../../d9/d07/classBase_1_1UnderflowError.html#a67cc29d9a61657f314177af02d1f6202)
(const std::string &sMessage)  
virtual | [~UnderflowError](../../d9/d07/classBase_1_1UnderflowError.html#a0d0b1750b686cee6a4c04c5481747f5b) () throw ()  
| Destruction.
[More...](../../d9/d07/classBase_1_1UnderflowError.html#a0d0b1750b686cee6a4c04c5481747f5b)  
  
![-](../../closed.png) Public Member Functions inherited from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html)  
std::string | [getFile](../../d8/df7/classBase_1_1Exception.html#adb6e652d6ee9cf2000a0ffeb9ce50597) () const  
std::string | [getFunction](../../d8/df7/classBase_1_1Exception.html#a6c5aa03a617f967abd79221910344718) () const  
[int](../../d1/da0/classint.html) | [getLine](../../d8/df7/classBase_1_1Exception.html#add9b14e9f5a48bdaf05487d6a13378be) () const  
std::string | [getMessage](../../d8/df7/classBase_1_1Exception.html#acea06c50f6eeaaaae36f187d99ef9226) () const  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyExceptionType](../../d8/df7/classBase_1_1Exception.html#a8e85d132bd8da6bcd445748d19c903d1) () const  
| returns the corresponding python exception type
[More...](../../d8/df7/classBase_1_1Exception.html#a8e85d132bd8da6bcd445748d19c903d1)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb) ()  
| returns a Python dictionary containing the exception data
[More...](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb)  
  
[bool](../../d9/db9/classbool.html) | [getReported](../../d8/df7/classBase_1_1Exception.html#ad82759cc946e2441cadef6776727be05) () const  
[bool](../../d9/db9/classbool.html) | [getTranslatable](../../d8/df7/classBase_1_1Exception.html#ae930eea23c340668b6621701b70c0e54) () const  
virtual [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getTypeId](../../d8/df7/classBase_1_1Exception.html#ad6856a6fd1d296adfcb2972d4cdf33ee) (void) const  
[Exception](../../d8/df7/classBase_1_1Exception.html) & | [operator=](../../d8/df7/classBase_1_1Exception.html#a73deac583ceab824678f8bdd7f0ea40c) (const [Exception](../../d8/df7/classBase_1_1Exception.html) &inst)  
virtual void | [ReportException](../../d8/df7/classBase_1_1Exception.html#a5703117e47253fbf07d86b702f9fdae4) () const  
| Reports exception. It includes a mechanism to only report an exception once.
[More...](../../d8/df7/classBase_1_1Exception.html#a5703117e47253fbf07d86b702f9fdae4)  
  
void | [setDebugInformation](../../d8/df7/classBase_1_1Exception.html#ae7e93feb4245a77e067796b480cea0c6) (const std::string &file, const [int](../../d1/da0/classint.html) line, const std::string &function)  
| setter methods for including debug information intended to use via macro for
autofilling of debugging information
[More...](../../d8/df7/classBase_1_1Exception.html#ae7e93feb4245a77e067796b480cea0c6)  
  
void | [setMessage](../../d8/df7/classBase_1_1Exception.html#ac112f8e1e18aa8bccc4902daae47c446) (const char *sMessage)  
void | [setMessage](../../d8/df7/classBase_1_1Exception.html#a4ea8dd5f1dea35e138bea6ebcefba850) (const std::string &sMessage)  
virtual void | [setPyException](../../d8/df7/classBase_1_1Exception.html#a58855227991a1be783d3a1e15f1ab7da) () const  
| Sets the Python error indicator and an error message.
[More...](../../d8/df7/classBase_1_1Exception.html#a58855227991a1be783d3a1e15f1ab7da)  
  
virtual void | [setPyObject](../../d8/df7/classBase_1_1Exception.html#afdfd5b57a05575d1ec05297e2f6e656e) ([PyObject](../../df/d1b/classPyObject.html) *pydict)  
| returns sets the exception data from a Python dictionary
[More...](../../d8/df7/classBase_1_1Exception.html#afdfd5b57a05575d1ec05297e2f6e656e)  
  
void | [setReported](../../d8/df7/classBase_1_1Exception.html#a66b0937f234eacc2716c594acbe3ec94) ([bool](../../d9/db9/classbool.html) reported)  
void | [setTranslatable](../../d8/df7/classBase_1_1Exception.html#a776e57a0e4877acfd47b2e2a225a83a9) ([bool](../../d9/db9/classbool.html) translatable)  
virtual const char * | [what](../../d8/df7/classBase_1_1Exception.html#aa330aa854000f17a93919417d977bcac) () const throw ()  
virtual | [~Exception](../../d8/df7/classBase_1_1Exception.html#a9e6152e43a70c1318c392c4dc107281f) () throw ()  
![-](../../closed.png) Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
|
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a84b1d36d0060e74a7b48255bca0d1928)
()  
| Construction.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a84b1d36d0060e74a7b48255bca0d1928)  
  
|
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html#ae41bc09a1498fbd4e952e7a7dd9de791)
(const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) &)=default  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514) ()  
| This method returns the Python wrapper for a C++ object.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514)  
  
virtual [Type](../../dc/dee/classBase_1_1Type.html) | [getTypeId](../../df/d4d/classBase_1_1BaseClass.html#addbd3a4f09fce7ce5c6bf021e4c1d566) () const  
[bool](../../d9/db9/classbool.html) | [isDerivedFrom](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html) & | [operator=](../../df/d4d/classBase_1_1BaseClass.html#ad334dfcaf7aa8b86993eaefac41207c2) (const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) &)=default  
virtual void | [setPyObject](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e) ([PyObject](../../df/d1b/classPyObject.html) *)  
virtual | [~BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a7bd44242e16f121ed78718ee8c234f49) ()  
| Destruction.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a7bd44242e16f121ed78718ee8c234f49)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html)  
static void * | [create](../../d8/df7/classBase_1_1Exception.html#a414ab988781cc35011247bf89a2ab998) (void)  
static [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../d8/df7/classBase_1_1Exception.html#aba0b86e61e79e9ccfd2f572d5162531e) (void)  
static void | [init](../../d8/df7/classBase_1_1Exception.html#aa5f325f865abb611f5fd93277905f978) (void)  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
![-](../../closed.png) Protected Member Functions inherited from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html)  
|
[Exception](../../d8/df7/classBase_1_1Exception.html#a1b78336bb26edf8e784783cc150c5801)
()  
|
[Exception](../../d8/df7/classBase_1_1Exception.html#a5ce04114a730cb532695f09d772286a2)
(const char *sMessage)  
|
[Exception](../../d8/df7/classBase_1_1Exception.html#ac5574f4372bed4081146df21053affaf)
(const [Exception](../../d8/df7/classBase_1_1Exception.html) &inst)  
|
[Exception](../../d8/df7/classBase_1_1Exception.html#a959cb3b6f6373185b22965b4352ec3d4)
(const std::string &sMessage)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

The [UnderflowError](../../d9/d07/classBase_1_1UnderflowError.html "The
UnderflowError can be used to indicate underflows of numbers.") can be used to
indicate underflows of numbers.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ UnderflowError() [1/3]

UnderflowError::UnderflowError  | ( | | ) |   
---|---|---|---|---  
  
Construction.

## ◆ UnderflowError() [2/3]

UnderflowError::UnderflowError  | ( | const char *  | _sMessage_| ) |   
---|---|---|---|---|---  
  
## ◆ UnderflowError() [3/3]

UnderflowError::UnderflowError  | ( | const std::string & | _sMessage_| ) |   
---|---|---|---|---|---  
  
## ◆ ~UnderflowError()

| virtual Base::UnderflowError::~UnderflowError  | ( | | ) |   
---|---|---|---|---  
throw | (|   
| )| |   
virtual  
  
Destruction.

## Member Function Documentation

## ◆ getPyExceptionType()

| [PyObject](../../df/d1b/classPyObject.html) * UnderflowError::getPyExceptionType  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
returns the corresponding python exception type

Reimplemented from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#a8e85d132bd8da6bcd445748d19c903d1).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Exception.h
  * FreeCAD/src/Base/Exception.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

