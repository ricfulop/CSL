---
url: https://freecad.github.io/SourceDoc/d5/d2b/classApp_1_1PropertyVector.html
scraped_at: 2025-09-08T14:56:48.106427
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html)

[List of all members](../../d7/dd1/classApp_1_1PropertyVector-members.html) | Public Member Functions

App::PropertyVector Class Reference

Vector properties This is the father of all properties handling Integers.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#details)

`#include <PropertyGeo.h>`

##  Public Member Functions  
  
---  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d5/d2b/classApp_1_1PropertyVector.html#ae60ac5ec9b71fcd763c369382d8bc29d) (void) const override  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#ae60ac5ec9b71fcd763c369382d8bc29d)  
  
const char * | [getEditorName](../../d5/d2b/classApp_1_1PropertyVector.html#a084057d252fc05436f7881c0986df98c) (void) const override  
| Get the class name of the associated property editor item.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a084057d252fc05436f7881c0986df98c)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d5/d2b/classApp_1_1PropertyVector.html#a125d7701b320054ba27f96a1ce07eeb5) (void) const override  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a125d7701b320054ba27f96a1ce07eeb5)  
  
void | [getPaths](../../d5/d2b/classApp_1_1PropertyVector.html#aa19d7736475e4226446cd94cf6f52a70) (std::vector< [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &paths) const override  
| Get valid paths for this property; used by auto completer.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#aa19d7736475e4226446cd94cf6f52a70)  
  
virtual const boost::any | [getPathValue](../../d5/d2b/classApp_1_1PropertyVector.html#a7b199450301358b2d7a0c69f1d9cc174) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path) const override  
| Get value of property.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a7b199450301358b2d7a0c69f1d9cc174)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d5/d2b/classApp_1_1PropertyVector.html#a6955692424d3ff25b5330b487de3e0e0) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a6955692424d3ff25b5330b487de3e0e0)  
  
virtual [bool](../../d9/db9/classbool.html) | [getPyPathValue](../../d5/d2b/classApp_1_1PropertyVector.html#a52eed8c59886bb4f3daf36fdab868805) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, Py::Object &res) const override  
| Get Python value of property.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a52eed8c59886bb4f3daf36fdab868805)  
  
virtual [Base::Unit](../../d2/d37/classBase_1_1Unit.html) | [getUnit](../../d5/d2b/classApp_1_1PropertyVector.html#a54372bab657d675f74c2811569964d91) () const  
const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | [getValue](../../d5/d2b/classApp_1_1PropertyVector.html#acaf0f2669a5dc7cf25a0ae68511aab43) (void) const  
| This method returns a string representation of the property.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#acaf0f2669a5dc7cf25a0ae68511aab43)  
  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d5/d2b/classApp_1_1PropertyVector.html#a6e4d497b46c90c57f0a6c4f95be4237e) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const override  
| Compare if this property has the same content as the given one.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a6e4d497b46c90c57f0a6c4f95be4237e)  
  
virtual void | [Paste](../../d5/d2b/classApp_1_1PropertyVector.html#a7ef832b4811885d30b97782e10afe042) (const [Property](../../d0/da9/classApp_1_1Property.html) &from) override  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a7ef832b4811885d30b97782e10afe042)  
  
|
[PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a45a2bfc3e372c9bc96f5091d50599405)
()  
| A constructor.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a45a2bfc3e372c9bc96f5091d50599405)  
  
virtual void | [Restore](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c)  
  
virtual void | [Save](../../d5/d2b/classApp_1_1PropertyVector.html#aee8aca3fc2bc388fac3c529adbbb8a10) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#aee8aca3fc2bc388fac3c529adbbb8a10)  
  
virtual void | [setPyObject](../../d5/d2b/classApp_1_1PropertyVector.html#a4e4eae3cb50d20fece89b7aac9fa6324) ([PyObject](../../df/d1b/classPyObject.html) *) override  
void | [setValue](../../d5/d2b/classApp_1_1PropertyVector.html#a866a1f59e997434cbe7e642af74301db) (const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &vec)  
| Sets the property.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a866a1f59e997434cbe7e642af74301db)  
  
void | [setValue](../../d5/d2b/classApp_1_1PropertyVector.html#aeb4d63310ecd47acfac9dc15e4118b33) (double x, double y, double z)  
virtual | [~PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a32df83710308ab1237d916c28fb7bf6b) ()  
| A destructor.
[More...](../../d5/d2b/classApp_1_1PropertyVector.html#a32df83710308ab1237d916c28fb7bf6b)  
  
![-](../../closed.png) Public Member Functions inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
virtual void | [aboutToSetChildValue](../../d0/da9/classApp_1_1Property.html#a9e3dfa9cc1ea03167fbe8c12f811f546) ([Property](../../d0/da9/classApp_1_1Property.html) &)  
| Called before a child property changing value.
[More...](../../d0/da9/classApp_1_1Property.html#a9e3dfa9cc1ea03167fbe8c12f811f546)  
  
virtual void | [afterRestore](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f) ()  
| Called at the beginning of
[Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5)
[More...](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f)  
  
virtual [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | [canonicalPath](../../d0/da9/classApp_1_1Property.html#a7a970c03b5e610df341e5cf464100523) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &p) const  
| Convert p to a canonical representation of it.
[More...](../../d0/da9/classApp_1_1Property.html#a7a970c03b5e610df341e5cf464100523)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de) (void) const =0  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de)  
  
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) * | [getContainer](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063) (void) const  
| Get a pointer to the
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html "Base
class of all classes with properties.") derived class the property belongs to.
[More...](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063)  
  
const char * | [getDocumentation](../../d0/da9/classApp_1_1Property.html#ada9481ae19a85f023c5597d57f8c809b) (void) const  
| Get the documentation of this property.
[More...](../../d0/da9/classApp_1_1Property.html#ada9481ae19a85f023c5597d57f8c809b)  
  
virtual const char * | [getEditorName](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983) (void) const  
| Get the class name of the associated property editor item.
[More...](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983)  
  
std::string | [getFullName](../../d0/da9/classApp_1_1Property.html#a0b1289a60e57856c8dae70fafd619dd2) () const  
const char * | [getGroup](../../d0/da9/classApp_1_1Property.html#ab815066b984a7d6c133b4c947a989fee) (void) const  
| Get the group of this property.
[More...](../../d0/da9/classApp_1_1Property.html#ab815066b984a7d6c133b4c947a989fee)  
  
int64_t | [getID](../../d0/da9/classApp_1_1Property.html#ad9f8fd8cb3f719b81661ad69f5047a44) () const  
| Return a unique ID for the property.
[More...](../../d0/da9/classApp_1_1Property.html#ad9f8fd8cb3f719b81661ad69f5047a44)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d0/da9/classApp_1_1Property.html#a933a44c77e539e1942227d1f266d3330) (void) const override  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../d0/da9/classApp_1_1Property.html#a933a44c77e539e1942227d1f266d3330)  
  
const char * | [getName](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a) (void) const  
| Get the name of this property in the belonging container With
[hasName()](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f)
it can be checked beforehand if a valid name is set.
[More...](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a)  
  
virtual void | [getPaths](../../d0/da9/classApp_1_1Property.html#a945f1c031f109242e362c5701516ff8e) (std::vector< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &paths) const  
| Get valid paths for this property; used by auto completer.
[More...](../../d0/da9/classApp_1_1Property.html#a945f1c031f109242e362c5701516ff8e)  
  
virtual const boost::any | [getPathValue](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path) const  
| Get value of property.
[More...](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea)  
  
virtual [bool](../../d9/db9/classbool.html) | [getPyPathValue](../../d0/da9/classApp_1_1Property.html#a55400138b9f116fa42702ed36d0511b1) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &, Py::Object &) const  
| Get Python value of property.
[More...](../../d0/da9/classApp_1_1Property.html#a55400138b9f116fa42702ed36d0511b1)  
  
unsigned long | [getStatus](../../d0/da9/classApp_1_1Property.html#a4df77b9a46967312e4a885f1a7386c16) () const  
| return the status bits
[More...](../../d0/da9/classApp_1_1Property.html#a4df77b9a46967312e4a885f1a7386c16)  
  
short | [getType](../../d0/da9/classApp_1_1Property.html#abc4967c88a5fc83c27a47f9534fdd510) (void) const  
| Get the type of the property in the container.
[More...](../../d0/da9/classApp_1_1Property.html#abc4967c88a5fc83c27a47f9534fdd510)  
  
[bool](../../d9/db9/classbool.html) | [hasName](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f) () const  
| Check if the property has a name set.
[More...](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f)  
  
virtual void | [hasSetChildValue](../../d0/da9/classApp_1_1Property.html#a35de61d1f853c6adb4e150c6cbb97ede) ([Property](../../d0/da9/classApp_1_1Property.html) &)  
| Called when a child property has changed value.
[More...](../../d0/da9/classApp_1_1Property.html#a35de61d1f853c6adb4e150c6cbb97ede)  
  
[bool](../../d9/db9/classbool.html) | [isReadOnly](../../d0/da9/classApp_1_1Property.html#a6f80d875dca2960d861f185d152e0de2) () const  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const  
| Compare if this property has the same content as the given one.
[More...](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d)  
  
[bool](../../d9/db9/classbool.html) | [isSinglePrecision](../../d0/da9/classApp_1_1Property.html#ad35584ef2dcc3838038f69f5f1c765c4) () const  
| Gets precision of properties using floating point numbers.
[More...](../../d0/da9/classApp_1_1Property.html#ad35584ef2dcc3838038f69f5f1c765c4)  
  
[bool](../../d9/db9/classbool.html) | [isTouched](../../d0/da9/classApp_1_1Property.html#afc61f45939514cad9316d170ffa99933) (void) const  
| Test if this property is touched.
[More...](../../d0/da9/classApp_1_1Property.html#afc61f45939514cad9316d170ffa99933)  
  
virtual void | [onContainerRestored](../../d0/da9/classApp_1_1Property.html#a724e44690754d6abaff38d3131420225) ()  
| Called before calling
[DocumentObject::onDocumentRestored()](../../d2/de4/classApp_1_1DocumentObject.html#a0ee8399fa0b176c64895150691a4b604
"get called after a document has been fully restored")
[More...](../../d0/da9/classApp_1_1Property.html#a724e44690754d6abaff38d3131420225)  
  
virtual void | [Paste](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be) (const [Property](../../d0/da9/classApp_1_1Property.html) &from)=0  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be)  
  
|
[Property](../../d0/da9/classApp_1_1Property.html#ab029377b86e5b8ae7513bf93f9c9a955)
()  
void | [purgeTouched](../../d0/da9/classApp_1_1Property.html#ac97a88a6ecc0a6644833aac52fbb4334) (void)  
| Reset this property touched.
[More...](../../d0/da9/classApp_1_1Property.html#ac97a88a6ecc0a6644833aac52fbb4334)  
  
void | [setContainer](../../d0/da9/classApp_1_1Property.html#aa03e6562bf3996db1700b0e636425257) ([PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *Father)  
| Is called by the framework to set the father (container)
[More...](../../d0/da9/classApp_1_1Property.html#aa03e6562bf3996db1700b0e636425257)  
  
virtual void | [setPathValue](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, const boost::any &value)  
| Set value of property.
[More...](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22)  
  
void | [setReadOnly](../../d0/da9/classApp_1_1Property.html#a8d9c78a46b9b79dc637cf70e1224c222) ([bool](../../d9/db9/classbool.html) readOnly)  
| Sets property editable/grayed out in property editor.
[More...](../../d0/da9/classApp_1_1Property.html#a8d9c78a46b9b79dc637cf70e1224c222)  
  
void | [setSinglePrecision](../../d0/da9/classApp_1_1Property.html#a552cc2dfc668452ab086f9c3903991e8) ([bool](../../d9/db9/classbool.html) single)  
| Sets precision of properties using floating point numbers to single, the
default is double.
[More...](../../d0/da9/classApp_1_1Property.html#a552cc2dfc668452ab086f9c3903991e8)  
  
void | [setStatus](../../d0/da9/classApp_1_1Property.html#a2f10dba2d265461344c6df7d0a40ad4e) ([Status](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014) pos, [bool](../../d9/db9/classbool.html) on)  
void | [setStatusValue](../../d0/da9/classApp_1_1Property.html#a32cf2f8513b5a66b0b39c839c559f20b) (unsigned long status)  
[bool](../../d9/db9/classbool.html) | [testStatus](../../d0/da9/classApp_1_1Property.html#aa0757bcb7ff02f8ece1205afd8a05775) ([Status](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014) pos) const  
void | [touch](../../d0/da9/classApp_1_1Property.html#a9bec8b8a56b405be0dc5e1602b079475) ()  
| [Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") status handling.
[More...](../../d0/da9/classApp_1_1Property.html#a9bec8b8a56b405be0dc5e1602b079475)  
  
virtual | [~Property](../../d0/da9/classApp_1_1Property.html#a0148f620477300ca547154581828cc1c) ()  
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
![-](../../closed.png) Public Types inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
enum | [Status](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014) {   
[Touched](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aa7412d0e7e6c015df9a22d89576953fe)
= 0 ,
[Immutable](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a59d0f940edf009b9ffbe01ed43d767cc)
= 1 ,
[ReadOnly](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a06b1f9ba5fd320622558e264c1c096de)
= 2 ,
[Hidden](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014adef773114327b6ad987a0c47a4262a54)
= 3 ,  
[Transient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a14e77d5a09c2b0796490e697b68560e5)
= 4 ,
[MaterialEdit](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a40f41a6380775c2373e89a780bfac551)
= 5 ,
[NoMaterialListEdit](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a5af65723f82e7b7f8d7fa6b2fe543b15)
= 6 ,
[Output](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a10640ff2cae2c1fda52dac13fc9a47a6)
= 7 ,  
[LockDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ac134907b347ed2484e41577a88d9a06e)
= 8 ,
[NoModify](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a420f4e5f5f4d37d09078346493729ad5)
= 9 ,
[PartialTrigger](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a2a08e64817919ee4f7f35341f2e8f7f4)
= 10 ,
[NoRecompute](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a8f31692acbbf9a5b8719e48fa68c5cde)
= 11 ,  
[Single](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a9c73483be20c75fd4c35af435a108ff6)
= 12 ,
[Ordered](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a7a56d6d20d93cd99b4f8032f8dd061fb)
= 13 ,
[EvalOnRestore](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ac1036b7face30993fb92e8ffd37d2636)
= 14 ,
[Busy](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a5738c5d6491eb6a3385e22bb718a868a)
= 15 ,  
[CopyOnChange](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a300baf70d0747fc9f320701a04ba5499)
= 16 ,
[UserEdit](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aad5ce06614de6a327726a7d95436cec4)
= 17 ,
[PropStaticBegin](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ab0d78a081465b31f8462ce404b0aed26)
= 21 ,
[PropDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a610d527a8ef20b533504b5121a983d80)
= 21 ,  
[PropNoPersist](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ae221473138e52da3001d1de060205179)
= 22 ,
[PropNoRecompute](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a78b230717c2b517e7875c4211612b764)
= 23 ,
[PropReadOnly](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a75dc207c45c9bf592c42415e987e7d5e)
= 24 ,
[PropTransient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a49215d8e9f6a5a24523e5ce094fb867e)
= 25 ,  
[PropHidden](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aab1086519565f4fa2cc26a504daa92d3)
= 26 ,
[PropOutput](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a7610516494d96a531206dc3e1fe94f57)
= 27 ,
[PropStaticEnd](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a0a622c3dfc0aeb45722e09c18b8f8a16)
= 28 ,
[User1](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ac99b647298c291251fac190ce52bda0b)
= 28 ,  
[User2](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a5224f0c2368e03cdd6ab193da92a8ba3)
= 29 ,
[User3](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aed76ddc4019f764ff7dbcb726007d14e)
= 30 ,
[User4](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a5f0e01e9cb9ad4119203788f0d6ca516)
= 31  
}  
![-](../../closed.png) Static Public Member Functions inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
static void | [destroy](../../d0/da9/classApp_1_1Property.html#a3a8325b864cd82b562eb553fe2be6d1c) ([Property](../../d0/da9/classApp_1_1Property.html) *p)  
| For safe deleting of a dynamic property.
[More...](../../d0/da9/classApp_1_1Property.html#a3a8325b864cd82b562eb553fe2be6d1c)  
  
static [bool](../../d9/db9/classbool.html) | [isValidName](../../d0/da9/classApp_1_1Property.html#ad8541be7b1fddd7f21f2ce3e18e8c06d) (const char *name)  
| Check if the passed name is valid.
[More...](../../d0/da9/classApp_1_1Property.html#ad8541be7b1fddd7f21f2ce3e18e8c06d)  
  
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
![-](../../closed.png) Public Attributes inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
boost::signals2::signal< void(const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChanged](../../d0/da9/classApp_1_1Property.html#a9e9e25207ee1e619c75f835f9853cf74)  
![-](../../closed.png) Protected Member Functions inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
virtual void | [aboutToSetValue](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d) (void)  
| Gets called by all setValue() methods before the value has changed.
[More...](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d)  
  
virtual void | [hasSetValue](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d) (void)  
| Gets called by all setValue() methods after the value has changed.
[More...](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d)  
  
virtual void | [verifyPath](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &p) const  
| Verify a path for the current property.
[More...](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7)  
  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Protected Attributes inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
std::bitset< 32 > | [StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67)  
| Status bits of the property The first 8 bits are used for the base system
the rest can be used in descendent classes to mark special statuses on the
objects.
[More...](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67)  
  
  
## Detailed Description

Vector properties This is the father of all properties handling Integers.

## Constructor & Destructor Documentation

## ◆ PropertyVector()

PropertyVector::PropertyVector  | ( | | ) |   
---|---|---|---|---  
  
A constructor.

A more elaborate description of the constructor.

Referenced by
[Copy()](../../d5/d2b/classApp_1_1PropertyVector.html#ae60ac5ec9b71fcd763c369382d8bc29d).

## ◆ ~PropertyVector()

| PropertyVector::~PropertyVector  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyVector::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

References
[PropertyVector()](../../d5/d2b/classApp_1_1PropertyVector.html#a45a2bfc3e372c9bc96f5091d50599405).

## ◆ getEditorName()

| const char * App::PropertyVector::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

Reimplemented in
[App::PropertyVectorDistance](../../d7/d1e/classApp_1_1PropertyVectorDistance.html#a771717f36e2805890ee62e7522a2dc73),
[App::PropertyPosition](../../dd/dc2/classApp_1_1PropertyPosition.html#a8edef058848613ec44f22b6b90242a48),
and
[App::PropertyDirection](../../d8/d4c/classApp_1_1PropertyDirection.html#abfa89d32ef67805c7f601db9fe38de5c).

## ◆ getMemSize()

| virtual unsigned [int](../../d1/da0/classint.html) App::PropertyVector::getMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").

See also

    [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence class and root of the type system.")

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a933a44c77e539e1942227d1f266d3330).

## ◆ getPaths()

| void PropertyVector::getPaths  | ( | std::vector< [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > & | _paths_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Get valid paths for this property; used by auto completer.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a945f1c031f109242e362c5701516ff8e).

References
[App::ObjectIdentifier::SimpleComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a14c7ec6dc691f2c26f6df8386bd9db6d).

## ◆ getPathValue()

| const boost::any PropertyVector::getPathValue  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Get value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea).

References
[App::Property::getPathValue()](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea),
and
[getUnit()](../../d5/d2b/classApp_1_1PropertyVector.html#a54372bab657d675f74c2811569964d91).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyVector::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method returns the Python wrapper for a C++ object.

It's in the responsibility of the programmer to do the correct reference
counting. Basically there are two ways how to implement that: Either always
return a new Python object then reference counting is not a matter or return
always the same Python object then the reference counter must be incremented
by one. However, it's absolutely forbidden to return always the same Python
object without incrementing the reference counter.

The default implementation returns 'None'.

Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514).

## ◆ getPyPathValue()

| [bool](../../d9/db9/classbool.html) PropertyVector::getPyPathValue  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | ,   
---|---|---|---  
|  | Py::Object & |   
| ) | |  const  
overridevirtual  
  
Get Python value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a55400138b9f116fa42702ed36d0511b1).

References
[getUnit()](../../d5/d2b/classApp_1_1PropertyVector.html#a54372bab657d675f74c2811569964d91),
and
[getValue()](../../d5/d2b/classApp_1_1PropertyVector.html#acaf0f2669a5dc7cf25a0ae68511aab43).

## ◆ getUnit()

| virtual [Base::Unit](../../d2/d37/classBase_1_1Unit.html) App::PropertyVector::getUnit  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reimplemented in
[App::PropertyVectorDistance](../../d7/d1e/classApp_1_1PropertyVectorDistance.html#a13cf48198fa25c599e0b196be979b17b),
[App::PropertyPosition](../../dd/dc2/classApp_1_1PropertyPosition.html#a75a28e99f348f7085449cacccb6fb57d),
and
[App::PropertyDirection](../../d8/d4c/classApp_1_1PropertyDirection.html#a82a05ebee91913141af4a785076e853e).

Referenced by
[getPathValue()](../../d5/d2b/classApp_1_1PropertyVector.html#a7b199450301358b2d7a0c69f1d9cc174),
and
[getPyPathValue()](../../d5/d2b/classApp_1_1PropertyVector.html#a52eed8c59886bb4f3daf36fdab868805).

## ◆ getValue()

const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & PropertyVector::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
This method returns a string representation of the property.

Referenced by
[TechDraw::DrawViewPart::checkXDirection()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a602f73fc08211bfc4edfa1382bc0ee64),
[PartDesign::FeatureExtrude::computeDirection()](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a3af51bee887de0bc89953128cb0a4d1c),
[Part::Extrusion::computeFinalParameters()](../../db/d6c/classPart_1_1Extrusion.html#a4b4ddc216eb6449e2b21480a430f5df8),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[TechDrawGui::QGIViewPart::drawHighlight()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#aac8834c3546b27902b1c3543d4a8e32e),
[TechDrawGui::QGIViewPart::drawSectionLine()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a513e571f325b7c7cac09bdec0d1c512d),
[Mesh::SegmentByMesh::execute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#a0fd4604225620a5902f526c867f0a7ed),
[App::MeasureDistance::execute()](../../d7/d61/classApp_1_1MeasureDistance.html#aa328f58f37764c36e03ee8356325ea72),
[Drawing::FeatureProjection::execute()](../../d8/d73/classDrawing_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Part::Mirroring::execute()](../../dc/dac/classPart_1_1Mirroring.html#aed38846265cf2381aae85d15dfb74be7),
[PartDesign::Groove::execute()](../../d7/de3/classPartDesign_1_1Groove.html#a0f3365a4df79cd6d9ec8137b32c9530c),
[PartDesign::Revolution::execute()](../../d2/de6/classPartDesign_1_1Revolution.html#a1e5564f51ec710663a8002d5018b76f8),
[Path::FeatureShape::execute()](../../da/d9b/classPath_1_1FeatureShape.html#a62d47b3cb3d7ed9081cdfc0966c71c3e),
[TechDraw::FeatureProjection::execute()](../../dd/ddc/classTechDraw_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Part::Revolution::execute()](../../d3/d17/classPart_1_1Revolution.html#a0406e2da5876bbf2351991c6b48b7185),
[TechDraw::DrawProjGroupItem::execute()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a1afd35db151cf4ec222427f08a4f3c2a),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[TechDraw::DrawViewMulti::execute()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a9d04a96ccac9fad6d125e478b91b7f30),
[PartDesign::Helix::generateHelixPath()](../../d3/d78/classPartDesign_1_1Helix.html#a04dd9590e1c0afe9dd3f1066ab9f0395),
[TechDraw::DrawProjGroup::getAnchorDirection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a6b386f82419d9dff8f039eb92b53cd31),
[TechDrawGui::TaskDetail::getAnchorScene()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ac47e200bf1be3381e59b3c6c4610494d),
[Fem::FemPostDataAlongLineFilter::GetAxisData()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ac3850d76cbd006a0d9f86f6971463cf2),
[TechDraw::DrawViewSection::getCSFromBase()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a761c0e9c4fe742ad0f6250428875ecd4),
[TechDraw::DrawProjGroup::getDirsFromFront()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a66cbbc8038fcab5532278784cbac867b),
[TechDraw::DrawProjGroupItem::getLegacyX()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a1bc574099e0939f27ba53b10f20d147f),
[Fem::Constraint::getPoints()](../../d0/d11/classFem_1_1Constraint.html#a422b5404d038352d227033eaf45cf37c),
[TechDraw::DrawViewPart::getProjectionCS()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ae1dd72b98fa563bf72d6c39f49577632),
[getPyPathValue()](../../d5/d2b/classApp_1_1PropertyVector.html#a52eed8c59886bb4f3daf36fdab868805),
[TechDraw::DrawProjGroupItem::getRotateAngle()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a7089aa4623e73d602fe97394d22ac6de),
[TechDraw::DrawViewSection::getSectionCS()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aefc378d8464959b191ac4ff96f6bca12),
[TechDraw::DrawProjGroupItem::getViewAxis()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a66cab4b4ebd52d41889c7fdb9c854821),
[TechDraw::DrawViewPart::getXDirection()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a0e16d51e16c7c55b75f5cfa00c037fd0),
[TechDraw::DrawProjGroupItem::getXDirection()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a86b744ee5d2b7ff5de819b0f23488498),
[TechDraw::DrawViewSection::getXDirection()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a0cefd62711bac9ca360a2ffc37731820),
[Fem::FemPostDataAlongLineFilter::handleChangedPropertyType()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#a1d60899654f9f7141ff2e7ef7aab1805),
[TechDraw::DrawViewPart::isIso()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#af3b5d2ae674b8b2b423edc3b12833e29),
[Gui::ViewProviderOrigin::onChanged()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[Fem::ConstraintFluidBoundary::onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Fem::ConstraintForce::onChanged()](../../d6/d63/classFem_1_1ConstraintForce.html#aa19098735f62c480439948314f6532b3),
[Fem::ConstraintGear::onChanged()](../../d8/d55/classFem_1_1ConstraintGear.html#a971506b4ca246c3378e2755160ed4772),
[Fem::FemPostDataAlongLineFilter::onChanged()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ae418afcb8e18abba84d16c2a645a434e),
[Fem::FemPostDataAtPointFilter::onChanged()](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#ae4bb2f96ee214db7c2bcb5a0afe0fdc4),
[Fem::FemPostPlaneFunction::onChanged()](../../dd/d76/classFem_1_1FemPostPlaneFunction.html#ab73b39b74f480820feda8b3f5bcad117),
[Fem::FemPostSphereFunction::onChanged()](../../d5/dcb/classFem_1_1FemPostSphereFunction.html#abffccabdacd9cbbe6e61e799c8385c59),
[PathGui::ViewProviderPath::onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[TechDraw::DrawViewPart::onChanged()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a6a340bbf67a96de757e412b21d7a5491),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[PartDesign::Helix::safePitch()](../../d3/d78/classPartDesign_1_1Helix.html#a85474d1c32f51cf49c0be48c600993eb),
[TechDrawGui::TaskDetail::saveDetailState()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a78c2d2718806789466fe6ac7a05d72bc),
[TechDrawGui::TaskProjGroup::saveGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#af012f644413f9c531a249a2fcb76d888),
[TechDrawGui::TaskSectionView::saveSectionState()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a6766d05bef0b8b54751ef23c124d3eb2),
[TechDraw::DrawViewSection::sectionExec()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a79c8f60f63dd54684af4cad42f91ee4e),
[TechDraw::DrawViewSection::sectionLineEnds()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a4f8580c4dea1570bca8520f11f871ebe),
[PartGui::ViewProviderMirror::setEdit()](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a1f2db7361989a26090e6071227f1562a),
[TechDrawGui::TaskSectionView::setUiEdit()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a43dc3542cf896d0778a028ae2be230ce),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[PartDesign::Pipe::setupAlgorithm()](../../da/d61/classPartDesign_1_1Pipe.html#aee88e3fe184997d50ac86c9f99b113f2),
[TechDraw::DrawProjGroup::spin()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#ad43779ef237f0848e22c8b8e5a4184b6),
[PartDesign::Groove::suggestReversed()](../../d7/de3/classPartDesign_1_1Groove.html#a86c15e2b0ef37872b2238a10decec68d),
[PartDesign::Revolution::suggestReversed()](../../d2/de6/classPartDesign_1_1Revolution.html#aad4f95d7725c302b54adaf5654487991),
[FemGui::ViewProviderFemConstraintBearing::updateData()](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#a3b3cf2fa05760751890d9e1cf51f178f),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintForce::updateData()](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#ad691cf23756106d6b0ea043ddebd1b94),
[FemGui::ViewProviderFemConstraintGear::updateData()](../../d1/d2f/classFemGui_1_1ViewProviderFemConstraintGear.html#a56f097a322b6fe5b2b4b7eead3374c49),
[FemGui::ViewProviderFemConstraintPulley::updateData()](../../d8/dfc/classFemGui_1_1ViewProviderFemConstraintPulley.html#a7ba40d63d4dff464026a808438d3630b),
[FemGui::ViewProviderFemConstraintTransform::updateData()](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#a2adf8aba7f15f7b95399068ab39c47b8),
[TechDraw::DrawProjGroup::updateSecondaryDirs()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aab0e5d4fa1e0eaf890c7c6cb2eb06766),
and
[PathGui::ViewProviderPath::updateVisual()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ab5ef44e05264d65aecc762660f342d58).

## ◆ isSame()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyVector::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

## ◆ Paste()

| void PropertyVector::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

## ◆ Restore()

| void PropertyVector::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d5/d2b/classApp_1_1PropertyVector.html#aee8aca3fc2bc388fac3c529adbbb8a10
"This method is used to save properties to an XML document.") written
information. Again the Vector as an example:

void
[PropertyVector::Restore](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c
"This method is used to restore properties from an XML
document.")([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html "The
XML reader class This is an important helper class for the store and retrieval
system of objects ...") &reader)

{

// read my Element

reader.[readElement](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e
"read until a start element is found \(<name>\) or start-end element
\(<name/>\) \(with special name if giv...")("PropertyVector");

// get the value of my Attribute

_cVec.x =
reader.[getAttributeAsFloat](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820
"return the named attribute as a double floating point \(does type
checking\)")("valueX");

_cVec.y =
reader.[getAttributeAsFloat](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820
"return the named attribute as a double floating point \(does type
checking\)")("valueY");

_cVec.z =
reader.[getAttributeAsFloat](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820
"return the named attribute as a double floating point \(does type
checking\)")("valueZ");

}

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[Base::XMLReader::getAttributeAsFloat()](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
and
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e).

Referenced by
[Fem::FemPostDataAlongLineFilter::handleChangedPropertyType()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#a1d60899654f9f7141ff2e7ef7aab1805),
and
[Part::Mirroring::handleChangedPropertyType()](../../dc/dac/classPart_1_1Mirroring.html#a177e7d2117a11729e6babd5c329f4be9).

## ◆ Save()

| void PropertyVector::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
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

References
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ setPyObject()

| void PropertyVector::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

References
[setValue()](../../d5/d2b/classApp_1_1PropertyVector.html#a866a1f59e997434cbe7e642af74301db),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[App::PropertyVectorList::getPyValue()](../../d5/d13/classApp_1_1PropertyVectorList.html#ad0f80e66d1ff38fe21ca46873897f4ea),
[Mesh::PropertyNormalList::setPyObject()](../../df/dcd/classMesh_1_1PropertyNormalList.html#ac56284294ef247339824c9af04dd6041),
and
[Points::PropertyNormalList::setPyObject()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#ac56284294ef247339824c9af04dd6041).

## ◆ setValue() [1/2]

void PropertyVector::setValue  | ( | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _vec_| ) |   
---|---|---|---|---|---  
  
Sets the property.

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[PartDesign::FeatureExtrude::computeDirection()](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a3af51bee887de0bc89953128cb0a4d1c),
[Part::Extrusion::computeFinalParameters()](../../db/d6c/classPart_1_1Extrusion.html#a4b4ddc216eb6449e2b21480a430f5df8),
[Gui::PointMarker::customEvent()](../../d6/deb/classGui_1_1PointMarker.html#af3aff66aa9cfaaff337386e66a61c0f4),
[Part::Revolution::execute()](../../d3/d17/classPart_1_1Revolution.html#a0406e2da5876bbf2351991c6b48b7185),
[TechDraw::DrawProjGroupItem::execute()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a1afd35db151cf4ec222427f08a4f3c2a),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewPart::execute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[Fem::FemPostDataAlongLineFilter::handleChangedPropertyType()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#a1d60899654f9f7141ff2e7ef7aab1805),
[Part::Mirroring::handleChangedPropertyType()](../../dc/dac/classPart_1_1Mirroring.html#a177e7d2117a11729e6babd5c329f4be9),
[Fem::Constraint::onChanged()](../../d0/d11/classFem_1_1Constraint.html#aec25bc397a1a87056079e3cd5a59d778),
[Fem::ConstraintBearing::onChanged()](../../df/d0a/classFem_1_1ConstraintBearing.html#ae81d9fda05994bd43bf81faf3acae5d6),
[Fem::ConstraintFluidBoundary::onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Fem::ConstraintForce::onChanged()](../../d6/d63/classFem_1_1ConstraintForce.html#aa19098735f62c480439948314f6532b3),
[Fem::ConstraintGear::onChanged()](../../d8/d55/classFem_1_1ConstraintGear.html#a971506b4ca246c3378e2755160ed4772),
[Fem::ConstraintTransform::onChanged()](../../d8/d3c/classFem_1_1ConstraintTransform.html#a38b893dee34272ad6bf0c6126aad561f),
[TechDraw::DrawViewPart::onChanged()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a6a340bbf67a96de757e412b21d7a5491),
[DraftUtils::DraftDxfRead::OnReadText()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#a4a48ca0bc35d4c47fc4e374d8ee6bf25),
[Import::ImpExpDxfRead::OnReadText()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#afd452a8d1348c494bfcc4bb9e5d4b01c),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[TechDrawGui::TaskDetail::restoreDetailState()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a2bd15a19a7717a5bbbf306d1149fb53d),
[TechDrawGui::TaskSectionView::restoreSectionState()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a31ebe04f8add6f5d1c665c9b7c12c238),
[TechDraw::DrawProjGroup::rotate()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#ab290c6d615bb2ec5b6fa65ed5516cb5d),
[DrawingGui::orthoview::set_projection()](../../db/df8/classDrawingGui_1_1orthoview.html#acd64a222bfeb734c9f23b27860505fca),
[TechDraw::DrawProjGroup::setAnchorDirection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a2c029d1ede27331ee73642a306a76b57),
[TechDraw::DrawViewSection::setCSFromBase()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a17fe837227e20f28e5f6d515f0d4dda0),
[setPyObject()](../../d5/d2b/classApp_1_1PropertyVector.html#a4e4eae3cb50d20fece89b7aac9fa6324),
[MeshGui::Annotation::show()](../../dd/d2d/classMeshGui_1_1Annotation.html#a8e675bcb0e642864e58f2d9f3b482ca8),
[TechDraw::DrawProjGroup::spin()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#ad43779ef237f0848e22c8b8e5a4184b6),
[PartGui::ViewProviderMirror::unsetEdit()](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a72ba82b453ad60568eb3bd6aa7a518f0),
[PartDesign::Groove::updateAxis()](../../d7/de3/classPartDesign_1_1Groove.html#a064b27171c35a5be3b681e2856208747),
[PartDesign::Helix::updateAxis()](../../d3/d78/classPartDesign_1_1Helix.html#aa8bfed8d9b7d87cdebf9e491a6193fd6),
[PartDesign::Revolution::updateAxis()](../../d2/de6/classPartDesign_1_1Revolution.html#a07ae95f9e32e5240284db567e6984b0d),
[TechDrawGui::TaskDetail::updateDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a9531ab9a77b992bbde7893f620cddd9f),
[PartDesignGui::ViewProviderBody::updateOriginDatumSize()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3c7c680a5e55c6cc695c82c8b45935c0),
and
[Gui::ViewProviderOriginGroupExtension::updateOriginSize()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a254bd812cc1814ed270f1d92e445ad8e).

## ◆ setValue() [2/2]

void PropertyVector::setValue  | ( | double  | _x_ ,   
---|---|---|---  
|  | double  | _y_ ,   
|  | double  | _z_  
| ) | |   
  
References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyGeo.h
  * FreeCAD/src/App/PropertyGeo.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

