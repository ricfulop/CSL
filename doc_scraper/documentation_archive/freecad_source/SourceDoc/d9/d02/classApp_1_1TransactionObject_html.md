---
url: https://freecad.github.io/SourceDoc/d9/d02/classApp_1_1TransactionObject.html
scraped_at: 2025-09-08T14:57:14.183158
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html)

[List of all members](../../d4/dd8/classApp_1_1TransactionObject-members.html) | Classes | Public Member Functions | Protected Types | Protected Attributes | Friends

App::TransactionObject Class Reference

Represents an entry for an object in a
[Transaction](../../de/dbf/classApp_1_1Transaction.html "Represents a atomic
transaction of the document.").
[More...](../../d9/d02/classApp_1_1TransactionObject.html#details)

`#include <Transactions.h>`

##  Classes  
  
---  
struct | [PropData](../../d7/dd3/structApp_1_1TransactionObject_1_1PropData.html)  
  
##  Public Member Functions  
  
---  
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
  
  
##  Protected Types  
  
---  
enum | [Status](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16) { [New](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a6e80d4f3ab64d122c3427f320222dce8) , [Del](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a4c5a4349fe7bb049c60f5534350acf48) , [Chn](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16ab8e7273c6754ae7dff2cc71fb8734b29) }  
  
##  Protected Attributes  
  
---  
enum [App::TransactionObject::Status](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16) | [status](../../d9/d02/classApp_1_1TransactionObject.html#a1f7180a94863f92b71034c3e11fb4d90)  
  
##  Friends  
  
---  
class | [Transaction](../../d9/d02/classApp_1_1TransactionObject.html#a49982aa325e19f0956d42fde9132caa2)  
  
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
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

Represents an entry for an object in a
[Transaction](../../de/dbf/classApp_1_1Transaction.html "Represents a atomic
transaction of the document.").

## Member Enumeration Documentation

## ◆ Status

| enum
[App::TransactionObject::Status](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16)  
---  
protected  
  
Enumerator  
---  
New |   
Del |   
Chn |   
  
## Constructor & Destructor Documentation

## ◆ TransactionObject()

TransactionObject::TransactionObject  | ( | | ) |   
---|---|---|---|---  
  
Construction.

A constructor.

A more elaborate description of the constructor.

## ◆ ~TransactionObject()

| TransactionObject::~TransactionObject  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Destruction.

A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ addOrRemoveProperty()

void TransactionObject::addOrRemoveProperty  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _pcProp_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _add_  
| ) | |   
  
References
[App::Property::Copy()](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::PropertyContainer::getDynamicPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#aa6ac51c527bc5f13d8d6d5ddc4e51f2e),
[App::Property::getID()](../../d0/da9/classApp_1_1Property.html#ad9f8fd8cb3f719b81661ad69f5047a44),
[App::Property::getStatus()](../../d0/da9/classApp_1_1Property.html#a4df77b9a46967312e4a885f1a7386c16),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
and
[App::DynamicProperty::PropData::property](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#a176e2cbcdbcaca063384507c694fe1c9).

Referenced by
[App::Transaction::addOrRemoveProperty()](../../de/dbf/classApp_1_1Transaction.html#a13b0dfb6149502294662f69042e250d8).

## ◆ applyChn()

| void TransactionObject::applyChn  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) & | _Doc_ ,   
---|---|---|---  
|  | [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _pcObj_ ,   
|  | [bool](../../d9/db9/classbool.html) | _Forward_  
| ) | |   
virtual  
  
References
[App::PropertyContainer::addDynamicProperty()](../../d5/d48/classApp_1_1PropertyContainer.html#aeb460dcdedde87f84dbab68d0865bfa6),
[Chn](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16ab8e7273c6754ae7dff2cc71fb8734b29),
[App::PropertyContainer::getDynamicPropertyByName()](../../d5/d48/classApp_1_1PropertyContainer.html#aa61e4c2e94abf8310ff9d790e4b54564),
[App::ExtensionContainer::getPropertyName()](../../d6/d76/classApp_1_1ExtensionContainer.html#a5d91112962ee5c459efa09469ebce4d0),
[New](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a6e80d4f3ab64d122c3427f320222dce8),
[App::PropertyContainer::removeDynamicProperty()](../../d5/d48/classApp_1_1PropertyContainer.html#a7e5425268a06b3e8a12f45abbbcfd653),
[App::Property::setStatusValue()](../../d0/da9/classApp_1_1Property.html#a32cf2f8513b5a66b0b39c839c559f20b),
and
[status](../../d9/d02/classApp_1_1TransactionObject.html#a1f7180a94863f92b71034c3e11fb4d90).

## ◆ applyDel()

| void TransactionObject::applyDel  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) & | _Doc_ ,   
---|---|---|---  
|  | [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _pcObj_  
| ) | |   
virtual  
  
Reimplemented in
[Gui::TransactionViewProvider](../../dc/dce/classGui_1_1TransactionViewProvider.html#a7afe38964b05c0b226e9e986cb7280a0),
and
[App::TransactionDocumentObject](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#aa6dbacdda12f6e29943a201964b1dfc0).

## ◆ applyNew()

| void TransactionObject::applyNew  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) & | _Doc_ ,   
---|---|---|---  
|  | [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _pcObj_  
| ) | |   
virtual  
  
Reimplemented in
[Gui::TransactionViewProvider](../../dc/dce/classGui_1_1TransactionViewProvider.html#af0c926787c34851929d2cc19c8b61f5c),
and
[App::TransactionDocumentObject](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#a65baa755e299835ac422f261e1c269f1).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) TransactionObject::getMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9).

## ◆ Restore()

| void TransactionObject::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_| ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc).

## ◆ Save()

| void TransactionObject::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
virtual  
  
This method is used to save properties to an XML document.

A good example you'll find in PropertyStandard.cpp, e.g. the vector:

void
[PropertyVector::Save](../../d5/d2b/classApp_1_1PropertyVector.html#aee8aca3fc2bc388fac3c529adbbb8a10
"This method is used to save properties to an XML document.") (Writer &writer)
const

{

writer << writer.ind() << "<PropertyVector valueX=\"" << _cVec.x <<

"\" valueY=\"" << _cVec.y <<

"\" valueZ=\"" << _cVec.z <<"\"/>" << endl;

}

The writer.ind() expression writes the indentation, just for pretty printing
of the XML. As you see, the writing of the XML document is not done with a DOM
implementation because of performance reasons. Therefore the programmer has to
take care that a valid XML document is written. This means closing tags and
writing UTF-8.

See also

    [Base::Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This is an important helper class for the store and retrieval system of persistent o...")

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436).

## ◆ setProperty()

void TransactionObject::setProperty  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _pcProp_| ) |   
---|---|---|---|---|---  
  
References
[App::Property::Copy()](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::PropertyContainer::getDynamicPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#aa6ac51c527bc5f13d8d6d5ddc4e51f2e),
[App::Property::getID()](../../d0/da9/classApp_1_1Property.html#ad9f8fd8cb3f719b81661ad69f5047a44),
[App::Property::getStatus()](../../d0/da9/classApp_1_1Property.html#a4df77b9a46967312e4a885f1a7386c16),
and
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

Referenced by
[App::Transaction::addObjectChange()](../../de/dbf/classApp_1_1Transaction.html#a49570b3477b90ad3f35dae121668ea87).

## Friends And Related Function Documentation

## ◆ Transaction

| [friend](../../d7/d23/classfriend.html) class
[Transaction](../../de/dbf/classApp_1_1Transaction.html)  
---  
friend  
  
## Member Data Documentation

## ◆ status

| enum
[App::TransactionObject::Status](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16)
App::TransactionObject::status  
---  
protected  
  
Referenced by
[App::Transaction::addObjectChange()](../../de/dbf/classApp_1_1Transaction.html#a49570b3477b90ad3f35dae121668ea87),
[App::Transaction::addObjectDel()](../../de/dbf/classApp_1_1Transaction.html#aaa52509516281edac9af07edc57bb707),
[App::Transaction::addObjectNew()](../../de/dbf/classApp_1_1Transaction.html#a33d72374a75b0138c6a5c9d71c858cff),
[App::Transaction::addOrRemoveProperty()](../../de/dbf/classApp_1_1Transaction.html#a13b0dfb6149502294662f69042e250d8),
[applyChn()](../../d9/d02/classApp_1_1TransactionObject.html#ae828131a91ad93ac2f20a51eeadecf70),
[App::TransactionDocumentObject::applyDel()](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#aa6dbacdda12f6e29943a201964b1dfc0),
[Gui::TransactionViewProvider::applyNew()](../../dc/dce/classGui_1_1TransactionViewProvider.html#af0c926787c34851929d2cc19c8b61f5c),
[App::TransactionDocumentObject::applyNew()](../../d2/dd9/classApp_1_1TransactionDocumentObject.html#a65baa755e299835ac422f261e1c269f1),
[package_list.PackageListFilter::filterAcceptsRow()](../../d3/d7c/classpackage__list_1_1PackageListFilter.html#ac6c224ec61dac5c46121a0fc4cf1cb17),
and
[package_list.PackageListFilter::setStatusFilter()](../../d3/d7c/classpackage__list_1_1PackageListFilter.html#a22cd720e4853ae43b7d7f39758f2ff99).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Transactions.h
  * FreeCAD/src/App/Transactions.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

