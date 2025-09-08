---
url: https://freecad.github.io/SourceDoc/d1/dc2/classBase_1_1FileException.html
scraped_at: 2025-09-08T15:16:09.823528
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [FileException](../../d1/dc2/classBase_1_1FileException.html)

[List of all members](../../dd/dcf/classBase_1_1FileException-members.html) | Public Member Functions | Protected Member Functions | Protected Attributes

Base::FileException Class Reference

File exception handling class This class is specialized to go with exception
thrown in case of File IO Problems.
[More...](../../d1/dc2/classBase_1_1FileException.html#details)

`#include <Exception.h>`

##  Public Member Functions  
  
---  
|
[FileException](../../d1/dc2/classBase_1_1FileException.html#a3b8bb7023e7a1f72141449feaffa6a2c)
()  
| standard construction
[More...](../../d1/dc2/classBase_1_1FileException.html#a3b8bb7023e7a1f72141449feaffa6a2c)  
  
|
[FileException](../../d1/dc2/classBase_1_1FileException.html#a278297d63334abcf8d6c84a3c6ebbc24)
(const char *sMessage, const char *sFileName=nullptr)  
| With massage and file name.
[More...](../../d1/dc2/classBase_1_1FileException.html#a278297d63334abcf8d6c84a3c6ebbc24)  
  
|
[FileException](../../d1/dc2/classBase_1_1FileException.html#aed8ff529f974ce63883db2fc6a1317c9)
(const char *sMessage, const
[FileInfo](../../dd/d34/classBase_1_1FileInfo.html) &File)  
| With massage and file name.
[More...](../../d1/dc2/classBase_1_1FileException.html#aed8ff529f974ce63883db2fc6a1317c9)  
  
|
[FileException](../../d1/dc2/classBase_1_1FileException.html#a1475e26637462b3cc3362e2fb3424734)
(const [FileException](../../d1/dc2/classBase_1_1FileException.html) &inst)  
| Construction.
[More...](../../d1/dc2/classBase_1_1FileException.html#a1475e26637462b3cc3362e2fb3424734)  
  
std::string | [getFileName](../../d1/dc2/classBase_1_1FileException.html#a85d7bd985f2af2646f9faa62c6228bf3) () const  
| Get file name for use with translatable message.
[More...](../../d1/dc2/classBase_1_1FileException.html#a85d7bd985f2af2646f9faa62c6228bf3)  
  
[PyObject](../../df/d1b/classPyObject.html) * | [getPyExceptionType](../../d1/dc2/classBase_1_1FileException.html#a96ff5d1876f039597f1a483964622ebd) () const override  
| returns the corresponding python exception type
[More...](../../d1/dc2/classBase_1_1FileException.html#a96ff5d1876f039597f1a483964622ebd)  
  
[PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d1/dc2/classBase_1_1FileException.html#af518f2b1282226fb40c4367c3aca0ae6) () override  
| returns a Python dictionary containing the exception data
[More...](../../d1/dc2/classBase_1_1FileException.html#af518f2b1282226fb40c4367c3aca0ae6)  
  
[FileException](../../d1/dc2/classBase_1_1FileException.html) & | [operator=](../../d1/dc2/classBase_1_1FileException.html#a3205d260dde6b88a6f8b7b6ca32552eb) (const [FileException](../../d1/dc2/classBase_1_1FileException.html) &inst)  
| Assignment operator.
[More...](../../d1/dc2/classBase_1_1FileException.html#a3205d260dde6b88a6f8b7b6ca32552eb)  
  
void | [ReportException](../../d1/dc2/classBase_1_1FileException.html#aaad485c53871c810d664df1fa89e8368) () const override  
| Report generation.
[More...](../../d1/dc2/classBase_1_1FileException.html#aaad485c53871c810d664df1fa89e8368)  
  
void | [setPyObject](../../d1/dc2/classBase_1_1FileException.html#ae17c092fdac1087551869fd28dc9d6d4) ([PyObject](../../df/d1b/classPyObject.html) *pydict) override  
| returns sets the exception data from a Python dictionary
[More...](../../d1/dc2/classBase_1_1FileException.html#ae17c092fdac1087551869fd28dc9d6d4)  
  
const char * | [what](../../d1/dc2/classBase_1_1FileException.html#ae6dc5fb38c5d24c07c2b625dd8c77792) () const override throw ()  
| Description of the exception.
[More...](../../d1/dc2/classBase_1_1FileException.html#ae6dc5fb38c5d24c07c2b625dd8c77792)  
  
virtual | [~FileException](../../d1/dc2/classBase_1_1FileException.html#a133a8d94746cb7a35e768a2f93e86bed) () throw ()  
| Destruction.
[More...](../../d1/dc2/classBase_1_1FileException.html#a133a8d94746cb7a35e768a2f93e86bed)  
  
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
  
  
##  Protected Member Functions  
  
---  
void | [setFileName](../../d1/dc2/classBase_1_1FileException.html#a0412edf20db63572bee4728e4209fe97) (const char *sFileName=nullptr)  
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
  
##  Protected Attributes  
  
---  
[FileInfo](../../dd/d34/classBase_1_1FileInfo.html) | [file](../../d1/dc2/classBase_1_1FileException.html#ac1a0860a501f1f7d1929577ca9c8d453)  
  
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
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

File exception handling class This class is specialized to go with exception
thrown in case of File IO Problems.

Author

    Juergen Riegel 

## Constructor & Destructor Documentation

## ◆ FileException() [1/4]

FileException::FileException  | ( | const char *  | _sMessage_ ,   
---|---|---|---  
|  | const char *  | _sFileName_ = `nullptr`  
| ) | |   
  
With massage and file name.

References
[setFileName()](../../d1/dc2/classBase_1_1FileException.html#a0412edf20db63572bee4728e4209fe97).

## ◆ FileException() [2/4]

FileException::FileException  | ( | const char *  | _sMessage_ ,   
---|---|---|---  
|  | const [FileInfo](../../dd/d34/classBase_1_1FileInfo.html) & | _File_  
| ) | |   
  
With massage and file name.

References
[Base::FileInfo::filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
and
[setFileName()](../../d1/dc2/classBase_1_1FileException.html#a0412edf20db63572bee4728e4209fe97).

## ◆ FileException() [3/4]

FileException::FileException  | ( | | ) |   
---|---|---|---|---  
  
standard construction

## ◆ FileException() [4/4]

FileException::FileException  | ( | const [FileException](../../d1/dc2/classBase_1_1FileException.html) & | _inst_| ) |   
---|---|---|---|---|---  
  
Construction.

## ◆ ~FileException()

| virtual Base::FileException::~FileException  | ( | | ) |   
---|---|---|---|---  
throw | (|   
| )| |   
virtual  
  
Destruction.

## Member Function Documentation

## ◆ getFileName()

std::string FileException::getFileName  | ( | | ) |  const  
---|---|---|---|---  
  
Get file name for use with translatable message.

References
[file](../../d1/dc2/classBase_1_1FileException.html#ac1a0860a501f1f7d1929577ca9c8d453),
and
[Base::FileInfo::fileName()](../../dd/d34/classBase_1_1FileInfo.html#a8ae2069796787d27306bb49bd70e3e3a).

## ◆ getPyExceptionType()

| [PyObject](../../df/d1b/classPyObject.html) * FileException::getPyExceptionType  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
returns the corresponding python exception type

Reimplemented from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#a8e85d132bd8da6bcd445748d19c903d1).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * FileException::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
returns a Python dictionary containing the exception data

Reimplemented from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb).

References
[file](../../d1/dc2/classBase_1_1FileException.html#ac1a0860a501f1f7d1929577ca9c8d453),
[Base::FileInfo::fileName()](../../dd/d34/classBase_1_1FileInfo.html#a8ae2069796787d27306bb49bd70e3e3a),
and
[Base::Exception::getPyObject()](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb).

## ◆ operator=()

[FileException](../../d1/dc2/classBase_1_1FileException.html) & FileException::operator=  | ( | const [FileException](../../d1/dc2/classBase_1_1FileException.html) & | _inst_| ) |   
---|---|---|---|---|---  
  
Assignment operator.

References
[file](../../d1/dc2/classBase_1_1FileException.html#ac1a0860a501f1f7d1929577ca9c8d453),
and
[Base::Exception::operator=()](../../d8/df7/classBase_1_1Exception.html#a73deac583ceab824678f8bdd7f0ea40c).

## ◆ ReportException()

| void FileException::ReportException  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Report generation.

Reimplemented from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#a5703117e47253fbf07d86b702f9fdae4).

## ◆ setFileName()

| void FileException::setFileName  | ( | const char *  | _sFileName_ = `nullptr`| ) |   
---|---|---|---|---|---  
protected  
  
References
[file](../../d1/dc2/classBase_1_1FileException.html#ac1a0860a501f1f7d1929577ca9c8d453),
and
[Base::FileInfo::setFile()](../../dd/d34/classBase_1_1FileInfo.html#ad254d88b127a0e93086c58f9c0487616).

Referenced by
[FileException()](../../d1/dc2/classBase_1_1FileException.html#a278297d63334abcf8d6c84a3c6ebbc24),
and
[setPyObject()](../../d1/dc2/classBase_1_1FileException.html#ae17c092fdac1087551869fd28dc9d6d4).

## ◆ setPyObject()

| void FileException::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _pydict_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
returns sets the exception data from a Python dictionary

Reimplemented from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#afdfd5b57a05575d1ec05297e2f6e656e).

References
[setFileName()](../../d1/dc2/classBase_1_1FileException.html#a0412edf20db63572bee4728e4209fe97),
and
[Base::Exception::setPyObject()](../../d8/df7/classBase_1_1Exception.html#afdfd5b57a05575d1ec05297e2f6e656e).

## ◆ what()

| const char * FileException::what  | ( | void  | | ) |  const  
---|---|---|---|---|---  
throw | (|   
| )| |   
overridevirtual  
  
Description of the exception.

Reimplemented from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#aa330aa854000f17a93919417d977bcac).

## Member Data Documentation

## ◆ file

| [FileInfo](../../dd/d34/classBase_1_1FileInfo.html)
Base::FileException::file  
---  
protected  
  
Referenced by
[exportIFCHelper.ContextCreator::createAutomaticProject()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a148406623b830e96b625e4cc9ac25bd2),
[exportIFCHelper.ContextCreator::createCustomProject()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a34f97033698a98007b430b629d694626),
[exportIFCHelper.ContextCreator::createGeometricRepresentationContext()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a6a54d0b2f20650b6a7ce05d57d2ae8e3),
[exportIFCHelper.ContextCreator::createGeometricRepresentationSubContext()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a706ac46037632ab6fb9ea483bf3e4095),
[exportIFCHelper.ContextCreator::createMapConversion()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#aac779e6f884db286129eb07b8622645b),
[exportIFCHelper.ContextCreator::createTargetCRS()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#ab3bc2c1c6282b286bd93af440fda7afc),
[exportIFCHelper.ContextCreator::createTrueNorth()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a8491dc7a339dce3412310dd42a65fd01),
[getFileName()](../../d1/dc2/classBase_1_1FileException.html#a85d7bd985f2af2646f9faa62c6228bf3),
[getPyObject()](../../d1/dc2/classBase_1_1FileException.html#af518f2b1282226fb40c4367c3aca0ae6),
[operator=()](../../d1/dc2/classBase_1_1FileException.html#a3205d260dde6b88a6f8b7b6ca32552eb),
[importIFClegacy.IfcFile::read()](../../d1/daa/classimportIFClegacy_1_1IfcFile.html#a9ad8d00537a61e0be429282c1c56fbdf),
and
[setFileName()](../../d1/dc2/classBase_1_1FileException.html#a0412edf20db63572bee4728e4209fe97).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Exception.h
  * FreeCAD/src/Base/Exception.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

