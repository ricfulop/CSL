---
url: https://freecad.github.io/SourceDoc/d2/dd9/classApp_1_1TransactionDocumentObject.html
scraped_at: 2025-09-08T14:57:11.130528
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [TransactionDocumentObject](../../d2/dd9/classApp_1_1TransactionDocumentObject.html)

[List of all members](../../de/d9f/classApp_1_1TransactionDocumentObject-members.html) | Public Member Functions

App::TransactionDocumentObject Class Reference

Represents an entry for a document object in a transaction.
[More...](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#details)

`#include <Transactions.h>`

##  Public Member Functions  
  
---  
void | [applyDel](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#aa6dbacdda12f6e29943a201964b1dfc0) ([Document](../../d8/d3e/classApp_1_1Document.html) &Doc, [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *pcObj)  
void | [applyNew](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#a65baa755e299835ac422f261e1c269f1) ([Document](../../d8/d3e/classApp_1_1Document.html) &Doc, [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *pcObj)  
|
[TransactionDocumentObject](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#a20e9c44e582cb367580cca9ad2c9ae10)
()  
| Construction.
[More...](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#a20e9c44e582cb367580cca9ad2c9ae10)  
  
virtual | [~TransactionDocumentObject](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#a89c8f2c63ef0fcedba252c57ad3ededf) ()  
| Destruction.
[More...](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#a89c8f2c63ef0fcedba252c57ad3ededf)  
  
![-](../../closed.png) Public Member Functions inherited from
[App::TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html)  
void | [addOrRemoveProperty](../../d9/d02/classApp_1_1TransactionObject.html#a1a9c63db207f7e24ed6918877c134764) (const [Property](../../d0/da9/classApp_1_1Property.html) *pcProp, [bool](../../d9/db9/classbool.html) add)  
virtual void | [applyChn](../../d9/d02/classApp_1_1TransactionObject.html#ae828131a91ad93ac2f20a51eeadecf70) ([Document](../../d8/d3e/classApp_1_1Document.html) &Doc, [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *pcObj, [bool](../../d9/db9/classbool.html) Forward)  
virtual void | [applyDel](../../d9/d02/classApp_1_1TransactionObject.html#a767c3b6d0d10ee49494289d8abf6a110) ([Document](../../d8/d3e/classApp_1_1Document.html) &Doc, [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *pcObj)  
virtual void | [applyNew](../../d9/d02/classApp_1_1TransactionObject.html#a3db6f824a0be768498b436418f52ba7c) ([Document](../../d8/d3e/classApp_1_1Document.html) &Doc, [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *pcObj)  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d9/d02/classApp_1_1TransactionObject.html#a3a43e98f7d1bf137d920be96bc8a4587) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?
[More...](../../d9/d02/classApp_1_1TransactionObject.html#a3a43e98f7d1bf137d920be96bc8a4587)  
  
virtual void | [Restore](../../d9/d02/classApp_1_1TransactionObject.html#abfde1f093dc2aed8ca598fecdedb6a7c) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../d9/d02/classApp_1_1TransactionObject.html#abfde1f093dc2aed8ca598fecdedb6a7c)  
  
virtual void | [Save](../../d9/d02/classApp_1_1TransactionObject.html#abc2454a0ce4e5fa73563fc8f0b9ac3fa) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../d9/d02/classApp_1_1TransactionObject.html#abc2454a0ce4e5fa73563fc8f0b9ac3fa)  
  
void | [setProperty](../../d9/d02/classApp_1_1TransactionObject.html#ad234dbb98feea5e3fb448aa2b0825207) (const [Property](../../d0/da9/classApp_1_1Property.html) *pcProp)  
|
[TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html#a4f2e3cb3c0f84044a4d96b8ce868e83e)
()  
| Construction.
[More...](../../d9/d02/classApp_1_1TransactionObject.html#a4f2e3cb3c0f84044a4d96b8ce868e83e)  
  
virtual | [~TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html#abeccace5075af9c2b088f7c95ed3988f) ()  
| Destruction.
[More...](../../d9/d02/classApp_1_1TransactionObject.html#abeccace5075af9c2b088f7c95ed3988f)  
  
![-](../../closed.png) Public Member Functions inherited from
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html)  
void | [dumpToStream](../../d9/d25/classBase_1_1Persistence.html#a3f09f422620031b240b4f01c044b49c7) (std::ostream &stream, [int](../../d1/da0/classint.html) compression)  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9) () const =0  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?
[More...](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9)  
  
virtual [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getTypeId](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596) (void) const  
virtual void | [Restore](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc) ([XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &)=0  
| This method is used to restore properties from an XML document.
[More...](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc)  
  
virtual void | [RestoreDocFile](../../d9/d25/classBase_1_1Persistence.html#a65260f99c6e0449f6caca2bc71efe37b) ([Reader](../../d1/d1f/classBase_1_1Reader.html) &)  
| This method is used to restore large amounts of data from a file In this
method you simply stream in your
[SaveDocFile()](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45
"This method is used to save large amounts of data to a binary file.") saved
data.
[More...](../../d9/d25/classBase_1_1Persistence.html#a65260f99c6e0449f6caca2bc71efe37b)  
  
void | [restoreFromStream](../../d9/d25/classBase_1_1Persistence.html#acf69a699ddf6fc30ff05fa70a27cc2dd) (std::istream &stream)  
virtual void | [Save](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436) ([Writer](../../dd/d4d/classBase_1_1Writer.html) &) const =0  
| This method is used to save properties to an XML document.
[More...](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436)  
  
virtual void | [SaveDocFile](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45) ([Writer](../../dd/d4d/classBase_1_1Writer.html) &) const  
| This method is used to save large amounts of data to a binary file.
[More...](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45)  
  
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
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html)  
static void * | [create](../../d9/d25/classBase_1_1Persistence.html#a8cecc55259bc79661a33a2d8df9764b7) (void)  
static std::string | [encodeAttribute](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec) (const std::string &)  
| Encodes an attribute upon saving.
[More...](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec)  
  
static [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56) (void)  
static void | [init](../../d9/d25/classBase_1_1Persistence.html#a4e9f73ac099dd794f6c87946f61cee0e) (void)  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
![-](../../closed.png) Protected Types inherited from
[App::TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html)  
enum | [Status](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16) { [New](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a6e80d4f3ab64d122c3427f320222dce8) , [Del](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a4c5a4349fe7bb049c60f5534350acf48) , [Chn](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16ab8e7273c6754ae7dff2cc71fb8734b29) }  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Protected Attributes inherited from
[App::TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html)  
enum [App::TransactionObject::Status](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16) | [status](../../d9/d02/classApp_1_1TransactionObject.html#a1f7180a94863f92b71034c3e11fb4d90)  
  
## Detailed Description

Represents an entry for a document object in a transaction.

## Constructor & Destructor Documentation

## ◆ TransactionDocumentObject()

TransactionDocumentObject::TransactionDocumentObject  | ( | | ) |   
---|---|---|---|---  
  
Construction.

A constructor.

A more elaborate description of the constructor.

## ◆ ~TransactionDocumentObject()

| TransactionDocumentObject::~TransactionDocumentObject  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Destruction.

A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ applyDel()

| void TransactionDocumentObject::applyDel  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) & | _Doc_ ,   
---|---|---|---  
|  | [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _pcObj_  
| ) | |   
virtual  
  
Reimplemented from
[App::TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html#a767c3b6d0d10ee49494289d8abf6a110).

References
[App::TransactionObject::Del](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a4c5a4349fe7bb049c60f5534350acf48),
and
[App::TransactionObject::status](../../d9/d02/classApp_1_1TransactionObject.html#a1f7180a94863f92b71034c3e11fb4d90).

## ◆ applyNew()

| void TransactionDocumentObject::applyNew  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) & | _Doc_ ,   
---|---|---|---  
|  | [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _pcObj_  
| ) | |   
virtual  
  
Reimplemented from
[App::TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html#a3db6f824a0be768498b436418f52ba7c).

References
[App::TransactionObject::New](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a6e80d4f3ab64d122c3427f320222dce8),
and
[App::TransactionObject::status](../../d9/d02/classApp_1_1TransactionObject.html#a1f7180a94863f92b71034c3e11fb4d90).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Transactions.h
  * FreeCAD/src/App/Transactions.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

