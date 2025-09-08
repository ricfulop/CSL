---
url: https://freecad.github.io/SourceDoc/de/dbf/classApp_1_1Transaction.html
scraped_at: 2025-09-08T14:57:09.136740
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Transaction](../../de/dbf/classApp_1_1Transaction.html)

[List of all members](../../d7/d93/classApp_1_1Transaction-members.html) | Public Member Functions | Static Public Member Functions | Public Attributes

App::Transaction Class Reference

Represents a atomic transaction of the document.
[More...](../../de/dbf/classApp_1_1Transaction.html#details)

`#include <Transactions.h>`

##  Public Member Functions  
  
---  
void | [addObjectChange](../../de/dbf/classApp_1_1Transaction.html#a49570b3477b90ad3f35dae121668ea87) (const [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *Obj, const [Property](../../d0/da9/classApp_1_1Property.html) *Prop)  
void | [addObjectDel](../../de/dbf/classApp_1_1Transaction.html#aaa52509516281edac9af07edc57bb707) (const [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *Obj)  
void | [addObjectNew](../../de/dbf/classApp_1_1Transaction.html#a33d72374a75b0138c6a5c9d71c858cff) ([TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *Obj)  
void | [addOrRemoveProperty](../../de/dbf/classApp_1_1Transaction.html#a13b0dfb6149502294662f69042e250d8) ([TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *Obj, const [Property](../../d0/da9/classApp_1_1Property.html) *pcProp, [bool](../../d9/db9/classbool.html) add)  
void | [apply](../../de/dbf/classApp_1_1Transaction.html#adf449c4d4c6750a7956c0f3d2b01ab80) ([Document](../../d8/d3e/classApp_1_1Document.html) &Doc, [bool](../../d9/db9/classbool.html) forward)  
| apply the content to the document
[More...](../../de/dbf/classApp_1_1Transaction.html#adf449c4d4c6750a7956c0f3d2b01ab80)  
  
[int](../../d1/da0/classint.html) | [getID](../../de/dbf/classApp_1_1Transaction.html#a883839e0722bbe62ec52d22bd176483a) (void) const  
| Return the transaction ID.
[More...](../../de/dbf/classApp_1_1Transaction.html#a883839e0722bbe62ec52d22bd176483a)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../de/dbf/classApp_1_1Transaction.html#ae95719b55aff8b6a974ee4dbbc263ea2) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?
[More...](../../de/dbf/classApp_1_1Transaction.html#ae95719b55aff8b6a974ee4dbbc263ea2)  
  
[bool](../../d9/db9/classbool.html) | [hasObject](../../de/dbf/classApp_1_1Transaction.html#acd5fbc8d2dc85e4608fddd65dfbd0ae6) (const [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *Obj) const  
| check if this object is used in a transaction
[More...](../../de/dbf/classApp_1_1Transaction.html#acd5fbc8d2dc85e4608fddd65dfbd0ae6)  
  
[bool](../../d9/db9/classbool.html) | [isEmpty](../../de/dbf/classApp_1_1Transaction.html#a9fa349671f837afc3603fd6b2d071405) () const  
| Returns true if the transaction list is empty; otherwise returns false.
[More...](../../de/dbf/classApp_1_1Transaction.html#a9fa349671f837afc3603fd6b2d071405)  
  
virtual void | [Restore](../../de/dbf/classApp_1_1Transaction.html#aa36b93a360af29f8d5d225cc0fc13422) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../de/dbf/classApp_1_1Transaction.html#aa36b93a360af29f8d5d225cc0fc13422)  
  
virtual void | [Save](../../de/dbf/classApp_1_1Transaction.html#aeb77b2f00b307e4ae1f5d64b86172749) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../de/dbf/classApp_1_1Transaction.html#aeb77b2f00b307e4ae1f5d64b86172749)  
  
|
[Transaction](../../de/dbf/classApp_1_1Transaction.html#a1cfc68ea05a831b2aabd6c6f2ee04512)
([int](../../d1/da0/classint.html) id=0)  
| Construction.
[More...](../../de/dbf/classApp_1_1Transaction.html#a1cfc68ea05a831b2aabd6c6f2ee04512)  
  
virtual | [~Transaction](../../de/dbf/classApp_1_1Transaction.html#a362b0d2524d0c799165190517192dca9) ()  
| Construction.
[More...](../../de/dbf/classApp_1_1Transaction.html#a362b0d2524d0c799165190517192dca9)  
  
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
  
  
##  Static Public Member Functions  
  
---  
static [int](../../d1/da0/classint.html) | [getLastID](../../de/dbf/classApp_1_1Transaction.html#a40df9cf53bada527779dd522a9208e16) (void)  
static [int](../../d1/da0/classint.html) | [getNewID](../../de/dbf/classApp_1_1Transaction.html#addd5e67511d134c5faf11d907a7187d2) (void)  
| Generate a new unique transaction ID.
[More...](../../de/dbf/classApp_1_1Transaction.html#addd5e67511d134c5faf11d907a7187d2)  
  
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
  
##  Public Attributes  
  
---  
std::string | [Name](../../de/dbf/classApp_1_1Transaction.html#a6245b49f541ec20247d3b46c18152f9a)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

Represents a atomic transaction of the document.

## Constructor & Destructor Documentation

## ◆ Transaction()

Transaction::Transaction  | ( | [int](../../d1/da0/classint.html) | _id_ = `0`| ) |   
---|---|---|---|---|---  
  
Construction.

Parameters

     id| transaction id. If zero, then it will be generated automatically as a monotonically increasing index across the entire application. User can pass in a transaction id to group multiple transactions from different document, so that they can be undo/redo together.   
---|---  
  
## ◆ ~Transaction()

| Transaction::~Transaction  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Construction.

A destructor.

A more elaborate description of the destructor.

References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
and
[App::TransactionObject::New](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a6e80d4f3ab64d122c3427f320222dce8).

## Member Function Documentation

## ◆ addObjectChange()

void Transaction::addObjectChange  | ( | const [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _Obj_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _Prop_  
| ) | |   
  
References
[App::TransactionObject::Chn](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16ab8e7273c6754ae7dff2cc71fb8734b29),
[App::TransactionFactory::createTransaction()](../../d1/dd6/classApp_1_1TransactionFactory.html#a8821bd6f94ff32feea26aefae911648b),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
[App::TransactionFactory::instance()](../../d1/dd6/classApp_1_1TransactionFactory.html#a878e27df0be7d047788f31b16c1b5ba6),
[App::TransactionObject::setProperty()](../../d9/d02/classApp_1_1TransactionObject.html#ad234dbb98feea5e3fb448aa2b0825207),
and
[App::TransactionObject::status](../../d9/d02/classApp_1_1TransactionObject.html#a1f7180a94863f92b71034c3e11fb4d90).

Referenced by
[App::Document::onBeforeChangeProperty()](../../d8/d3e/classApp_1_1Document.html#a92ee224a3cd40ef4da74e81d732c8fcb),
and
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33).

## ◆ addObjectDel()

void Transaction::addObjectDel  | ( | const [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _Obj_| ) |   
---|---|---|---|---|---  
  
References
[App::TransactionObject::Chn](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16ab8e7273c6754ae7dff2cc71fb8734b29),
[App::TransactionFactory::createTransaction()](../../d1/dd6/classApp_1_1TransactionFactory.html#a8821bd6f94ff32feea26aefae911648b),
[App::TransactionObject::Del](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a4c5a4349fe7bb049c60f5534350acf48),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
[App::TransactionFactory::instance()](../../d1/dd6/classApp_1_1TransactionFactory.html#a878e27df0be7d047788f31b16c1b5ba6),
[App::TransactionObject::New](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a6e80d4f3ab64d122c3427f320222dce8),
and
[App::TransactionObject::status](../../d9/d02/classApp_1_1TransactionObject.html#a1f7180a94863f92b71034c3e11fb4d90).

Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
and
[Gui::Document::slotTransactionAppend()](../../de/d4e/classGui_1_1Document.html#a8f4d208373fe26556f80553a8aa062f1).

## ◆ addObjectNew()

void Transaction::addObjectNew  | ( | [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _Obj_| ) |   
---|---|---|---|---|---  
  
References
[App::TransactionFactory::createTransaction()](../../d1/dd6/classApp_1_1TransactionFactory.html#a8821bd6f94ff32feea26aefae911648b),
[App::TransactionObject::Del](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a4c5a4349fe7bb049c60f5534350acf48),
[App::TransactionalObject::detachFromDocument()](../../d8/d00/classApp_1_1TransactionalObject.html#a17f7538441e315b11eca8ebc047e11f4),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
[App::TransactionFactory::instance()](../../d1/dd6/classApp_1_1TransactionFactory.html#a878e27df0be7d047788f31b16c1b5ba6),
[App::TransactionObject::New](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16a6e80d4f3ab64d122c3427f320222dce8),
and
[App::TransactionObject::status](../../d9/d02/classApp_1_1TransactionObject.html#a1f7180a94863f92b71034c3e11fb4d90).

Referenced by
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
and
[Gui::Document::slotTransactionRemove()](../../de/d4e/classGui_1_1Document.html#acf76be063eb0e3252ed3c37782417e29).

## ◆ addOrRemoveProperty()

void Transaction::addOrRemoveProperty  | ( | [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _Obj_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _pcProp_ ,   
|  | [bool](../../d9/db9/classbool.html) | _add_  
| ) | |   
  
References
[App::TransactionObject::addOrRemoveProperty()](../../d9/d02/classApp_1_1TransactionObject.html#a1a9c63db207f7e24ed6918877c134764),
[App::TransactionObject::Chn](../../d9/d02/classApp_1_1TransactionObject.html#af12b889a3756cb44c346cf06cbb7fe16ab8e7273c6754ae7dff2cc71fb8734b29),
[App::TransactionFactory::createTransaction()](../../d1/dd6/classApp_1_1TransactionFactory.html#a8821bd6f94ff32feea26aefae911648b),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
[App::TransactionFactory::instance()](../../d1/dd6/classApp_1_1TransactionFactory.html#a878e27df0be7d047788f31b16c1b5ba6),
and
[App::TransactionObject::status](../../d9/d02/classApp_1_1TransactionObject.html#a1f7180a94863f92b71034c3e11fb4d90).

Referenced by
[App::Document::addOrRemovePropertyOfObject()](../../d8/d3e/classApp_1_1Document.html#ac4060590326f48e4fb73a542d2bd6d02).

## ◆ apply()

void Transaction::apply  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) & | _Doc_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _forward_  
| ) | |   
  
apply the content to the document

References
[Name](../../de/dbf/classApp_1_1Transaction.html#a6245b49f541ec20247d3b46c18152f9a).

## ◆ getID()

[int](../../d1/da0/classint.html) Transaction::getID  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Return the transaction ID.

Referenced by
[App::Document::abortTransaction()](../../d8/d3e/classApp_1_1Document.html#a01f60ab9bc840c591e8f3b6f78e51041),
[App::Document::commitTransaction()](../../d8/d3e/classApp_1_1Document.html#a1ebcf21ffc49ae09b241f2bcab6bfe01),
[App::Document::getAvailableUndos()](../../d8/d3e/classApp_1_1Document.html#acac169e323a61d08b4c48d31337ab672),
[App::Document::getTransactionID()](../../d8/d3e/classApp_1_1Document.html#a5225cf38810fc5cb88614651b7a7927c),
[App::Document::redo()](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003),
[App::Document::renameTransaction()](../../d8/d3e/classApp_1_1Document.html#a558ba4c9f9ba3652ff53273d95b8f575),
and
[App::Document::undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078).

## ◆ getLastID()

| [int](../../d1/da0/classint.html) Transaction::getLastID  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[App::Application::getActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a320164bff61415b44f26af228fe99c6a).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) Transaction::getMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9).

## ◆ getNewID()

| [int](../../d1/da0/classint.html) Transaction::getNewID  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Generate a new unique transaction ID.

Referenced by
[App::Application::setActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a78fddfc24e060908e047c5472857c3ff).

## ◆ hasObject()

[bool](../../d9/db9/classbool.html) Transaction::hasObject  | ( | const [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _Obj_| ) |  const  
---|---|---|---|---|---  
  
check if this object is used in a transaction

## ◆ isEmpty()

[bool](../../d9/db9/classbool.html) Transaction::isEmpty  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Returns true if the transaction list is empty; otherwise returns false.

## ◆ Restore()

| void Transaction::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_| ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc).

## ◆ Save()

| void Transaction::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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

## Member Data Documentation

## ◆ Name

std::string App::Transaction::Name  
---  
  
Referenced by
[apply()](../../de/dbf/classApp_1_1Transaction.html#adf449c4d4c6750a7956c0f3d2b01ab80),
[App::Document::getAvailableUndoNames()](../../d8/d3e/classApp_1_1Document.html#af22136a16daca121025484f1dc8865d5),
[App::Document::redo()](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003),
[App::Document::renameTransaction()](../../d8/d3e/classApp_1_1Document.html#a558ba4c9f9ba3652ff53273d95b8f575),
and
[App::Document::undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Transactions.h
  * FreeCAD/src/App/Transactions.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

