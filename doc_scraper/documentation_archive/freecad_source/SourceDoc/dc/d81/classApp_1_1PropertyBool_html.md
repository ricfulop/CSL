---
url: https://freecad.github.io/SourceDoc/dc/d81/classApp_1_1PropertyBool.html
scraped_at: 2025-09-08T14:55:28.753759
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html)

[List of all members](../../db/da3/classApp_1_1PropertyBool-members.html) | Public Member Functions

App::PropertyBool Class Reference

Bool properties This is the father of all properties handling booleans.
[More...](../../dc/d81/classApp_1_1PropertyBool.html#details)

`#include <PropertyStandard.h>`

##  Public Member Functions  
  
---  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../dc/d81/classApp_1_1PropertyBool.html#a9971031594a20af7bffe75225510b743) (void) const  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../dc/d81/classApp_1_1PropertyBool.html#a9971031594a20af7bffe75225510b743)  
  
virtual const char * | [getEditorName](../../dc/d81/classApp_1_1PropertyBool.html#ac100a4def344f24aa36677f56121d088) (void) const  
| Get the class name of the associated property editor item.
[More...](../../dc/d81/classApp_1_1PropertyBool.html#ac100a4def344f24aa36677f56121d088)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../dc/d81/classApp_1_1PropertyBool.html#aa07a81452563bf739d36dcaec51429a3) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../dc/d81/classApp_1_1PropertyBool.html#aa07a81452563bf739d36dcaec51429a3)  
  
const boost::any | [getPathValue](../../dc/d81/classApp_1_1PropertyBool.html#ad5e2c285aa19b7472c8dfdd754636418) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path) const  
| Get value of property.
[More...](../../dc/d81/classApp_1_1PropertyBool.html#ad5e2c285aa19b7472c8dfdd754636418)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../dc/d81/classApp_1_1PropertyBool.html#a163886db763f486562607f282dab5c43) (void)  
| This method returns the Python wrapper for a C++ object.
[More...](../../dc/d81/classApp_1_1PropertyBool.html#a163886db763f486562607f282dab5c43)  
  
[bool](../../d9/db9/classbool.html) | [getValue](../../dc/d81/classApp_1_1PropertyBool.html#a62b86902ce1909a052a84b28f3e226c7) (void) const  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../dc/d81/classApp_1_1PropertyBool.html#abd96cbaefa1ebf8b44b844bfc4a60989) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const  
| Compare if this property has the same content as the given one.
[More...](../../dc/d81/classApp_1_1PropertyBool.html#abd96cbaefa1ebf8b44b844bfc4a60989)  
  
virtual void | [Paste](../../dc/d81/classApp_1_1PropertyBool.html#a884f68fe6a0d3bd3eddd54fe8f8abd32) (const [Property](../../d0/da9/classApp_1_1Property.html) &from)  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../dc/d81/classApp_1_1PropertyBool.html#a884f68fe6a0d3bd3eddd54fe8f8abd32)  
  
|
[PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#a2eef451420487acf6c16f16b61046de4)
(void)  
| A constructor.
[More...](../../dc/d81/classApp_1_1PropertyBool.html#a2eef451420487acf6c16f16b61046de4)  
  
virtual void | [Restore](../../dc/d81/classApp_1_1PropertyBool.html#a198b7cda570cfdad094c8886cd995778) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../dc/d81/classApp_1_1PropertyBool.html#a198b7cda570cfdad094c8886cd995778)  
  
virtual void | [Save](../../dc/d81/classApp_1_1PropertyBool.html#a8c59652996dcffd9f4a2d503afaccd29) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../dc/d81/classApp_1_1PropertyBool.html#a8c59652996dcffd9f4a2d503afaccd29)  
  
void | [setPathValue](../../dc/d81/classApp_1_1PropertyBool.html#a21b072ecae3082e2c8dfb2605469f9ef) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, const boost::any &value)  
| Set value of property.
[More...](../../dc/d81/classApp_1_1PropertyBool.html#a21b072ecae3082e2c8dfb2605469f9ef)  
  
virtual void | [setPyObject](../../dc/d81/classApp_1_1PropertyBool.html#addcd7e7adacdc4cbbf4140b2f81e6066) ([PyObject](../../df/d1b/classPyObject.html) *)  
void | [setValue](../../dc/d81/classApp_1_1PropertyBool.html#a8067462e38e7bb949ae31a86ec8ed17c) ([bool](../../d9/db9/classbool.html) lValue)  
virtual | [~PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#ac2e22fb13f801e51ea99f9d516a89705) ()  
| A destructor.
[More...](../../dc/d81/classApp_1_1PropertyBool.html#ac2e22fb13f801e51ea99f9d516a89705)  
  
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

Bool properties This is the father of all properties handling booleans.

## Constructor & Destructor Documentation

## ◆ PropertyBool()

PropertyBool::PropertyBool  | ( | void  | | ) |   
---|---|---|---|---|---  
  
A constructor.

A more elaborate description of the constructor.

Referenced by
[Copy()](../../dc/d81/classApp_1_1PropertyBool.html#a9971031594a20af7bffe75225510b743).

## ◆ ~PropertyBool()

| PropertyBool::~PropertyBool  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyBool::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

References
[PropertyBool()](../../dc/d81/classApp_1_1PropertyBool.html#a2eef451420487acf6c16f16b61046de4).

## ◆ getEditorName()

| virtual const char * App::PropertyBool::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

## ◆ getMemSize()

| virtual unsigned [int](../../d1/da0/classint.html) App::PropertyBool::getMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").

See also

    [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence class and root of the type system.")

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a933a44c77e539e1942227d1f266d3330).

## ◆ getPathValue()

| const boost::any PropertyBool::getPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Get value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea).

References
[App::Property::verifyPath()](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyBool::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
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

## ◆ getValue()

[bool](../../d9/db9/classbool.html) PropertyBool::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[FemGui::TaskDlgFemConstraintFluidBoundary::accept()](../../da/d17/classFemGui_1_1TaskDlgFemConstraintFluidBoundary.html#a92106711f12fb0fb783c7e411d8f3923),
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[PartDesign::Body::addObject()](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605),
[TechDraw::DrawLeaderLine::adjustLastSegment()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#af9979a970967304c97ce041e0bda2cfc),
[PartDesignGui::TaskHelixParameters::apply()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#ac943cca36559194f55b17ffc2b2a91ac),
[Gui::ViewProviderLink::applyMaterial()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2116838fd198dca3f32851993fc65e2a),
[Gui::ViewProviderOriginFeature::attach()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#aac32ddea00ce5374fa432bad0540355a),
[PartGui::ViewProvider2DObjectGrid::attach()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a3b56803e591faa31c7b83d7962d7e5e5),
[Gui::ViewProviderDocumentObject::attach()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a915f1f11451e769f91b1137d1527fc57),
[TechDraw::DrawProjGroupItem::autoPosition()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#aed7c8d696a4a2b4f3a172ebc3789cbf7),
[TechDraw::DrawViewPart::buildGeometryObject()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a859efd3dcccfd849656ff8b436ce6d58),
[PartDesign::SubShapeBinder::canLoadPartial()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a0faf56fc6f85e668bb1128a8631e9a9a),
[TechDraw::DrawPage::canUpdate()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a8f1af10c86de8fa62a94ba4fb227d33b),
[PartDesignGui::TaskHoleParameters::changedObject()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#af6c0941c01c80d87e2f97344958003be),
[PartDesign::SubShapeBinder::checkPropertyStatus()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ae25cb348741e0731acc8f3de49e9cd7b),
[PartDesign::FeatureExtrude::computeDirection()](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a3af51bee887de0bc89953128cb0a4d1c),
[Part::Extrusion::computeFinalParameters()](../../db/d6c/classPart_1_1Extrusion.html#a4b4ddc216eb6449e2b21480a430f5df8),
[SketcherGui::DrawSketchHandler::createAutoConstraints()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#aaeb21f657e7a40232d0b9e275295765c),
[PartGui::ViewProvider2DObjectGrid::createGrid()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a6872b82ce1aa46b6532e864681e262ae),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[Gui::ViewProviderTextDocument::doubleClicked()](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a5e666f0a1cab99aba3ce00094a9cb351),
[TechDrawGui::QGILeaderLine::draw()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#ab20089120a1417e5a55af3e140e7acbd),
[TechDrawGui::QGIViewImage::draw()](../../d9/ddb/classTechDrawGui_1_1QGIViewImage.html#a5aefc1e7dc0a816005586bfd0adf8a6c),
[TechDrawGui::QGIViewDimension::drawAngle()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a27c4e7cb613ec0563614d25f802cf6e9),
[TechDrawGui::QGIViewPart::drawCenterLines()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a3e50cd4cfc6f211f7b2979615c13f1f7),
[TechDrawGui::QGIViewDimension::drawDiameter()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4f99cea83cd1e147dee58d5e4d2c9a65),
[TechDrawGui::QGIViewDimension::drawDistance()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a9ca8dc402df9510b7e7537bac4a53e5b),
[Gui::ViewProviderAnnotationLabel::drawImage()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a37530affd46043649525097fa5ff8e05),
[TechDrawGui::QGIViewDimension::drawRadius()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#ab82446f086e3e9ecda97fa4e7f933562),
[TechDrawGui::QGIViewSection::drawSectionFace()](../../d7/d73/classTechDrawGui_1_1QGIViewSection.html#a23b734cc85fce28a0a42c4d061686cb4),
[TechDrawGui::QGIWeldSymbol::drawTile()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a95de553829cc9844a9e95b1bdbd36e76),
[Mesh::Cylinder::execute()](../../df/def/classMesh_1_1Cylinder.html#a7f0a6253a8936e26fdd2794992f9cbb4),
[Mesh::Cone::execute()](../../d4/dbc/classMesh_1_1Cone.html#a23701269832147c5746476d7e6b3b8af),
[PartDesign::Pad::execute()](../../d9/d14/classPartDesign_1_1Pad.html#a17b37a5aaa299709fbb066564ef25b3e),
[PartDesign::Pocket::execute()](../../d1/d89/classPartDesign_1_1Pocket.html#aac791837d2ea389e30768f0fb6d25935),
[Drawing::FeatureClip::execute()](../../d5/d4a/classDrawing_1_1FeatureClip.html#afed75650f49849b96c65ef93795800e5),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Drawing::FeatureProjection::execute()](../../d8/d73/classDrawing_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Fem::FemMeshShapeNetgenObject::execute()](../../d9/df4/classFem_1_1FemMeshShapeNetgenObject.html#ad38e08d369e0a9c44588e98bc5ffb3ed),
[Part::Loft::execute()](../../d3/d52/classPart_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[Part::Sweep::execute()](../../df/dc6/classPart_1_1Sweep.html#a7fdf28d346eb1b3b838ed0dea5bb40d8),
[Part::Thickness::execute()](../../db/d73/classPart_1_1Thickness.html#a773b84ae5c846c3cfc1c099ab47887da),
[PartDesign::Fillet::execute()](../../d0/d50/classPartDesign_1_1Fillet.html#a3d2e483fe0b72a9d09d5945fe7e36e65),
[PartDesign::Groove::execute()](../../d7/de3/classPartDesign_1_1Groove.html#a0f3365a4df79cd6d9ec8137b32c9530c),
[PartDesign::Helix::execute()](../../d3/d78/classPartDesign_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[PartDesign::Hole::execute()](../../dd/dd0/classPartDesign_1_1Hole.html#ad3161d80bf31dc136534283281a5b3ad),
[PartDesign::Loft::execute()](../../d0/deb/classPartDesign_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[PartDesign::Revolution::execute()](../../d2/de6/classPartDesign_1_1Revolution.html#a1e5564f51ec710663a8002d5018b76f8),
[PartDesign::Thickness::execute()](../../d4/d22/classPartDesign_1_1Thickness.html#a773b84ae5c846c3cfc1c099ab47887da),
[Path::FeatureCompound::execute()](../../d2/d43/classPath_1_1FeatureCompound.html#a0db05b4845d8e9cf2dc1ab83a02a875b),
[Path::FeatureShape::execute()](../../da/d9b/classPath_1_1FeatureShape.html#a62d47b3cb3d7ed9081cdfc0966c71c3e),
[Robot::Edge2TracObject::execute()](../../d8/df5/classRobot_1_1Edge2TracObject.html#a05d96baf25af72c1c01f165a8dac7f63),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[Surface::Filling::execute()](../../d8/df7/classSurface_1_1Filling.html#ab31cd9c2fd6bd4e15a80b7065c071eae),
[Surface::Sewing::execute()](../../d2/d52/classSurface_1_1Sewing.html#a956109125cae787085423aeb93d8e1f3),
[TechDraw::FeatureProjection::execute()](../../dd/ddc/classTechDraw_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Part::Offset::execute()](../../d0/dda/classPart_1_1Offset.html#a342f29a6b5381db240304b9384b313dd),
[Part::Offset2D::execute()](../../d7/dcf/classPart_1_1Offset2D.html#a3eb29bb0e6404263cb3470d7ec24ea4a),
[Part::Revolution::execute()](../../d3/d17/classPart_1_1Revolution.html#a0406e2da5876bbf2351991c6b48b7185),
[PartDesign::Chamfer::execute()](../../da/d6f/classPartDesign_1_1Chamfer.html#a3fc5f1e2196c59afb44e876fd05d4710),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[PartGui::ViewProviderSplineExtension::extensionOnChanged()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#a136922fdf38b223d79d10d64a60380ae),
[PartGui::ViewProviderSplineExtension::extensionSetupContextMenu()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#a9d9a2018c8e8f0aa8b7681aa66090d7b),
[PartGui::ViewProviderSplineExtension::extensionUpdateData()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#ac0f6ab010c3a75a975e8ca3ad2ef60e2),
[TechDraw::DrawViewPart::extractFaces()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aaaaf9f3bc41bcad927258ed1fdb53baa),
[PartDesign::Helix::generateHelixPath()](../../d3/d78/classPartDesign_1_1Helix.html#a04dd9590e1c0afe9dd3f1066ab9f0395),
[PartDesign::DressUp::getAddSubShape()](../../df/de5/classPartDesign_1_1DressUp.html#ad0ea5289ebf6d00059754a3cd95b7981),
[PathGui::ViewProviderPath::getBoundColor()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a98a3ef4085a9babf25db6f74aa95bdc0),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[Gui::ViewProviderLink::getElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2b9c2eef2778031596f93f33b2980102),
[TechDraw::DrawViewDimension::getFormattedDimensionValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a92f36b1b5e044976e4a117424b000985),
[TechDraw::DrawViewDimension::getFormattedToleranceValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aac71dbd0561262809d791806fc44775d),
[TechDraw::DrawViewDimension::getFormattedToleranceValues()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a8235b120b82f24a29c6be38d6afff542),
[TechDrawGui::ViewProviderPage::getFrameState()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a9b1ceada49b9856664ccfbf1e1935f30),
[FemGui::TaskFemConstraintFluidBoundary::getHeatTransferring()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#ac3e8db10a90349dcbe9c3d5a0658c50f),
[PartDesign::ProfileBased::getReversedAngle()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a3b3aa636b6181cd9edacd1f7b1412f0b),
[TechDraw::DrawLeaderLine::getScale()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a5df9ab095a761eaef57045a431cbb972),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[PartDesign::ProfileBased::getVerifiedFace()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a4172d89f228cd87e6517a0518401b11a),
[TechDraw::DrawViewPart::getVisibleFaceEdges()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ab7ab634f849e8211772cbbd1ed3233fb),
[TechDraw::DrawProjGroup::getXYPosition()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aaeadc17847095c9f9d5ff6db786e04bd),
[TechDraw::DrawViewDimension::hasOverUnderTolerance()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aaaa8ffab8600c2fb49f4e6cc42b8ff60),
[TechDraw::DrawViewDimension::haveTolerance()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a23fb6a5052c6642d4bb60576868e25d7),
[TechDraw::DrawView::isLocked()](../../d6/d1c/classTechDraw_1_1DrawView.html#abd90c9cc4add5e701f943c5689549097),
[Gui::ViewProviderGeometryObject::isSelectable()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a1d9af3261374f6349b80de8143f37f28),
[Gui::ViewProviderLink::isSelectable()](../../d6/d59/classGui_1_1ViewProviderLink.html#ae7302fe3f47eecd4610145dc35a13791),
[TechDrawGui::QGIView::isVisible()](../../d1/d99/classTechDrawGui_1_1QGIView.html#aa29fba41538cd9190f6d1da126aad9a4),
[Part::Section::makeOperation()](../../d8/dea/classPart_1_1Section.html#ae39baa3f76015f35aa3cdc129f98a251),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[Gui::ViewProviderTextDocument::onChanged()](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a8d87ca622183dd3077563ad3d45c479b),
[Fem::ConstraintFluidBoundary::onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Fem::ConstraintForce::onChanged()](../../d6/d63/classFem_1_1ConstraintForce.html#aa19098735f62c480439948314f6532b3),
[Fem::ConstraintGear::onChanged()](../../d8/d55/classFem_1_1ConstraintGear.html#a971506b4ca246c3378e2755160ed4772),
[Fem::ConstraintPulley::onChanged()](../../d3/dec/classFem_1_1ConstraintPulley.html#a6c23af9b8ba29b03f25163da9b75a41f),
[Fem::FemPostClipFilter::onChanged()](../../dc/d06/classFem_1_1FemPostClipFilter.html#a696285744236a6bf6e8c14f735034705),
[Fem::FemPostScalarClipFilter::onChanged()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a6c5243b230b4dac2cde71f28d04dcd53),
[FemGui::ViewProviderFemMesh::onChanged()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ab319d4e3659d8c99309bd397af321308),
[InspectionGui::ViewProviderInspection::onChanged()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a75537f17b213bb2c7ea45b374ed65375),
[MeshGui::ViewProviderMesh::onChanged()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae9ec71d871b59be4a532fb2be2cb8d52),
[MeshGui::ViewProviderMeshNode::onChanged()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a6f37857950fa14e1e1978c56706d0797),
[PartGui::ViewProvider2DObjectGrid::onChanged()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a04a16b5ac49a2b5df31304da0a4318ee),
[PartDesign::Hole::onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[PathGui::ViewProviderPath::onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[RobotGui::ViewProviderRobotObject::onChanged()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a41cfa5ba4f24dacf46491cc903e5a715),
[PartDesign::SubShapeBinder::onChanged()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a525834748579d35e2e8ecbf9cd18bf3d),
[PartDesignGui::ViewProviderSubShapeBinder::onChanged()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[Surface::Extend::onChanged()](../../d1/d22/classSurface_1_1Extend.html#ac33fb0ebd31edae770d009cc24c58df9),
[TechDraw::DrawPage::onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[PartDesign::Helix::proposeParameters()](../../d3/d78/classPartDesign_1_1Helix.html#a278b5c14eacce6ed801c4722006744d9),
[PartDesign::FeatureAddSub::refineShapeIfActive()](../../d0/dd5/classPartDesign_1_1FeatureAddSub.html#aaae99d37d5947319bfe6b58d97557182),
[PartDesign::Boolean::refineShapeIfActive()](../../d2/d81/classPartDesign_1_1Boolean.html#a7dc39f0b971b8f5e3334ea0948592509),
[PartDesign::Transformed::refineShapeIfActive()](../../dd/de1/classPartDesign_1_1Transformed.html#a9109aa5c8c7c9f3439b54476c3d921de),
[SketcherGui::DrawSketchHandlerLine::releaseButton()](../../dd/d65/classSketcherGui_1_1DrawSketchHandlerLine.html#a9ee080f22c2c3bf2f6e826f4cc36f91a),
[SketcherGui::DrawSketchHandlerLineSet::releaseButton()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a040aa2a8cc28c52db550115a16ef693c),
[MeshGui::ViewProviderMesh::removeFacets()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#aef4f7c4dfe1a66027828a011eea2651f),
[TechDrawGui::TaskProjGroup::saveGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#af012f644413f9c531a249a2fcb76d888),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
[PartGui::ViewProvider2DObjectGrid::setEdit()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a9fa0acb41e43ce0dd79d58330cd10ffe),
[TechDrawGui::ViewProviderPage::setGrid()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a31f4fdf0be6391e13a47115c059f69cd),
[setPathValue()](../../dc/d81/classApp_1_1PropertyBool.html#a21b072ecae3082e2c8dfb2605469f9ef),
[TechDrawGui::QGIRichAnno::setTextItem()](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#a27fd9afb78b8c22eeadd556d985030fe),
[TechDrawGui::TaskWeldingSymbol::setUiEdit()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#aa3e9fde175112fd5b2308f32bd93a33c),
[TechDrawGui::TaskRichAnno::setUiEdit()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a3659e9cb13bc53ae36a3d7d16479d017),
[PartDesign::Pipe::setupAlgorithm()](../../da/d61/classPartDesign_1_1Pipe.html#aee88e3fe184997d50ac86c9f99b113f2),
[Gui::DocumentItem::showHidden()](../../df/d15/classGui_1_1DocumentItem.html#ab08d3106925612e8b9830623f2dc4864),
[Gui::ViewProviderDocumentObject::showInTree()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7a74cd8717daf43e557ee87654f4d7a),
[TechDraw::DrawProjGroupItem::showLock()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a145138581e310d20f4203e46354ab756),
[PartGui::TaskAttacher::TaskAttacher()](../../df/d45/classPartGui_1_1TaskAttacher.html#ae3b7e331323f8a005efc1e55579240a6),
[TechDrawGui::TaskBalloon::TaskBalloon()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#a21f34d1bf15390ec9c984c7c75ab9996),
[PartDesignGui::TaskChamferParameters::TaskChamferParameters()](../../d1/d5d/classPartDesignGui_1_1TaskChamferParameters.html#a30a85de6338f5d8a399de49cb4fe9014),
[TechDrawGui::TaskDimension::TaskDimension()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a01dec85a4db02858073f304508300ff3),
[PartDesignGui::TaskDraftParameters::TaskDraftParameters()](../../d6/d74/classPartDesignGui_1_1TaskDraftParameters.html#aafff6d5bd22406878791e8ccad20b907),
[FemGui::TaskFemConstraintBearing::TaskFemConstraintBearing()](../../d5/d79/classFemGui_1_1TaskFemConstraintBearing.html#a5c48324835803c2f89e0c8a226dec9b0),
[FemGui::TaskFemConstraintDisplacement::TaskFemConstraintDisplacement()](../../d6/d75/classFemGui_1_1TaskFemConstraintDisplacement.html#ad9efd945714cedc7f6f182b3b811e089),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[FemGui::TaskFemConstraintForce::TaskFemConstraintForce()](../../d2/d46/classFemGui_1_1TaskFemConstraintForce.html#a3db3abe3cbf9a61635e1683630a55762),
[FemGui::TaskFemConstraintGear::TaskFemConstraintGear()](../../d9/d4d/classFemGui_1_1TaskFemConstraintGear.html#a9e613a0869b02375ab20ef330813dd1f),
[FemGui::TaskFemConstraintPressure::TaskFemConstraintPressure()](../../dc/dd9/classFemGui_1_1TaskFemConstraintPressure.html#a00c65ac2686efb36884dcf8c6a10d76e),
[FemGui::TaskFemConstraintPulley::TaskFemConstraintPulley()](../../d3/d33/classFemGui_1_1TaskFemConstraintPulley.html#a0ae13b3d3671f9f5b94b36ca4f1bef14),
[PartDesignGui::TaskFilletParameters::TaskFilletParameters()](../../db/d91/classPartDesignGui_1_1TaskFilletParameters.html#a6d39adf6b643a77ee3cecf31cdac126d),
[PartDesignGui::TaskHoleParameters::TaskHoleParameters()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#aed07ebf7cad6b7cff0c7597137c91662),
[PartDesignGui::TaskLoftParameters::TaskLoftParameters()](../../d3/dd7/classPartDesignGui_1_1TaskLoftParameters.html#ab30560915d7d39e4ff4d50b1befc36bf),
[PartDesignGui::TaskPipeOrientation::TaskPipeOrientation()](../../d8/df3/classPartDesignGui_1_1TaskPipeOrientation.html#ac6d362fde0b1452a942b513494180d97),
[TechDrawGui::TaskProjGroup::TaskProjGroup()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a81c03636578c0dd7befcb158dd86bc28),
[PartDesignGui::TaskRevolutionParameters::TaskRevolutionParameters()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#a5509b04d5cfc1da7d5314c4a038a01e2),
[SketcherGui::TaskSketcherGeneral::TaskSketcherGeneral()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#acb35aefc057b31af4b7c6e9c87e1f0d4),
[FemGui::TaskTetParameter::TaskTetParameter()](../../d9/d36/classFemGui_1_1TaskTetParameter.html#a29dc9ca508fcde30e91d9b0e306b34ce),
[PartDesignGui::TaskThicknessParameters::TaskThicknessParameters()](../../de/d75/classPartDesignGui_1_1TaskThicknessParameters.html#a43c1b021112c8995623c941d9d59a5ef),
[RobotGui::TaskTrajectoryDressUpParameter::TaskTrajectoryDressUpParameter()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#a291e8c4303c14a45405f67a846976168),
[PartGui::ThicknessWidget::ThicknessWidget()](../../d5/d25/classPartGui_1_1ThicknessWidget.html#aa0023d59e7ac0b3735f1fbd0c5019a8a),
[TechDrawGui::MDIViewPage::toggleKeepUpdated()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a501e9ef7784b1ffc2192a98fdfd42324),
[PartGui::ViewProvider2DObjectGrid::unsetEdit()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a036451869ccec14b115760e67eeea52a),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
[Gui::ViewProviderMeasureDistance::updateData()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a260762ea126ca4a70b60e5a825f2448d),
[FemGui::ViewProviderFemConstraintBearing::updateData()](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#a3b3cf2fa05760751890d9e1cf51f178f),
[FemGui::ViewProviderFemConstraintDisplacement::updateData()](../../d7/d3f/classFemGui_1_1ViewProviderFemConstraintDisplacement.html#afb4b851d45e12b8639d1c4bedcaba4db),
[FemGui::ViewProviderFemConstraintPressure::updateData()](../../d4/d18/classFemGui_1_1ViewProviderFemConstraintPressure.html#a0280a478dea5288d50ba390ed1a50ca7),
[FemGui::ViewProviderFemMesh::updateData()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a2b42be80762272d7f6be0b30e7d6a3f5),
[MeshGui::ViewProviderIndexedFaceSet::updateData()](../../d8/d12/classMeshGui_1_1ViewProviderIndexedFaceSet.html#a18d4f21152ed2f96bfcec096aa0e639c),
[MeshGui::ViewProviderMeshFaceSet::updateData()](../../df/de9/classMeshGui_1_1ViewProviderMeshFaceSet.html#a1a79e8c47f1e048e3027f7908856d85f),
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f),
[PartDesign::ShapeBinder::updatedShape()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a126f8b03ab46e56d65b7fbd3d41b98e8),
and
[PartGui::ViewProvider2DObjectGrid::updateGridExtent()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a114a939dd1485906f2d12080317792af).

## ◆ isSame()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyBool::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

## ◆ Paste()

| void PropertyBool::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
virtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

## ◆ Restore()

| void PropertyBool::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../dc/d81/classApp_1_1PropertyBool.html#a8c59652996dcffd9f4a2d503afaccd29
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
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
and
[setValue()](../../dc/d81/classApp_1_1PropertyBool.html#a8067462e38e7bb949ae31a86ec8ed17c).

## ◆ Save()

| void PropertyBool::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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

References
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ setPathValue()

| void PropertyBool::setPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | const boost::any & | _value_  
| ) | |   
virtual  
  
Set value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22).

References
[getValue()](../../dc/d81/classApp_1_1PropertyBool.html#a62b86902ce1909a052a84b28f3e226c7),
[setValue()](../../dc/d81/classApp_1_1PropertyBool.html#a8067462e38e7bb949ae31a86ec8ed17c),
and
[App::Property::verifyPath()](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7).

## ◆ setPyObject()

| void PropertyBool::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

References
[setValue()](../../dc/d81/classApp_1_1PropertyBool.html#a8067462e38e7bb949ae31a86ec8ed17c).

## ◆ setValue()

void PropertyBool::setValue  | ( | [bool](../../d9/db9/classbool.html) | _lValue_| ) |   
---|---|---|---|---|---  
  
References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

Referenced by
[PartDesignGui::TaskDlgBooleanParameters::accept()](../../df/ded/classPartDesignGui_1_1TaskDlgBooleanParameters.html#ac73e06d1d9df4f99b255a706d2a5409f),
[PartDesignGui::ViewProviderSubShapeBinder::attach()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#af413076e01667efda51a06a5ce1b6638),
[Gui::ViewProviderDocumentObject::attach()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a915f1f11451e769f91b1137d1527fc57),
[TechDrawGui::TaskProjGroup::AutoDistributeClicked()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#ae38b7ea40b031895834fbce113cd0943),
[PartDesign::Boolean::Boolean()](../../d2/d81/classPartDesign_1_1Boolean.html#ac032e9c86b0a2605c320402f47850319),
[TechDrawGui::TaskRichAnno::commonFeatureUpdate()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ab5a728afdf435f4c1631b56211559576),
[ReverseEngineeringGui::SegmentationManual::createSegment()](../../dc/d04/classReverseEngineeringGui_1_1SegmentationManual.html#a95ac22eb241f58d992ffe08f784eb5d0),
[TechDraw::DrawViewSection::getParameters()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a67beb353938e343cc5a31cf6a3acbfa5),
[DrawingGui::orthoview::hidden()](../../db/df8/classDrawingGui_1_1orthoview.html#aa1eb5b39dccefda9f885b7b93c0f75df),
[PartDesignGui::TaskDressUpParameters::hideObject()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#af899ee96527f085fc3568e108714caba),
[TechDrawGui::QGIView::isVisible()](../../d1/d99/classTechDrawGui_1_1QGIView.html#a6fea8197de9d4bc71a04aa2bd1880c48),
[PartDesign::Hole::onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[Gui::ViewProviderDocumentObject::onChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[Gui::ViewProviderLink::onChanged()](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[SketcherGui::TaskSketcherGeneral::onToggleAutoconstraints()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#af98d9afa099d5ca20ac3210bf8574264),
[SketcherGui::TaskSketcherGeneral::onToggleAvoidRedundant()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#a56f09d15b77d56e0754f7ae96662c6ca),
[SketcherGui::TaskSketcherGeneral::onToggleGridSnap()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#a1861231853393c92e66a48f11e36410d),
[SketcherGui::TaskSketcherGeneral::onToggleGridView()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#af1c47ffc82198d2b624a74afb311ea56),
[PartDesign::Helix::proposeParameters()](../../d3/d78/classPartDesign_1_1Helix.html#a278b5c14eacce6ed801c4722006744d9),
[MeshGui::ViewProviderMesh::removeFacets()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#aef4f7c4dfe1a66027828a011eea2651f),
[Restore()](../../dc/d81/classApp_1_1PropertyBool.html#a198b7cda570cfdad094c8886cd995778),
[TechDraw::DrawViewDimension::Restore()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#afb1057b5d67039082147ba14225f1c82),
[TechDrawGui::TaskProjGroup::restoreGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a348f413a63a7fd86ebf8978fee5d028f),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[Gui::AlignmentGroup::setAlignable()](../../dc/d5e/classGui_1_1AlignmentGroup.html#a921830caf78e809033bc775808106cbb),
[SketcherGui::ViewProviderSketch::setEdit()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ad28c651e806a00fca15332d4c04b47c9),
[Gui::ViewProviderLink::setElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#af274c7d8619bfae997be5ea17b7c72b3),
[TechDrawGui::ViewProviderPage::setFrameState()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ad83075829d6d27e06c95ede993f7a421),
[setPathValue()](../../dc/d81/classApp_1_1PropertyBool.html#a21b072ecae3082e2c8dfb2605469f9ef),
[setPyObject()](../../dc/d81/classApp_1_1PropertyBool.html#addcd7e7adacdc4cbbf4140b2f81e6066),
[Gui::DocumentItem::setShowHidden()](../../df/d15/classGui_1_1DocumentItem.html#aabbf058f0836116ff32d800cf6c3244c),
[PartDesign::ProfileBased::setupObject()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#ace3e681c5be8bc26572497dea2ed09cd),
[PartDesign::SubShapeBinder::setupObject()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a788801f841b2c6dfcb6493aa6a69aacd),
[Gui::ViewProviderDocumentObject::show()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae42de285d193c43881fa6019b902fec1),
[PartDesignGui::TaskDressUpParameters::showObject()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a8de298ef5f0b2f224b75f7a8a3f806ee),
[DrawingGui::orthoview::smooth()](../../db/df8/classDrawingGui_1_1orthoview.html#a833632e71b68c14dd6e32e233a592d6e),
[Sketcher::SketchObject::solve()](../../d9/dad/classSketcher_1_1SketchObject.html#a0bcef04719586a7122d762061b2d4ac4),
[PartGui::ViewProviderSplineExtension::toggleControlPoints()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#a5c4215951ba842b8d04b191dcda4f9f3),
[TechDrawGui::MDIViewPage::toggleKeepUpdated()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a501e9ef7784b1ffc2192a98fdfd42324),
[SketcherGui::ViewProviderSketch::unsetEdit()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a292cf2c15b300787b74fa8b2bc248388),
[Gui::ViewProviderGeometryObject::ViewProviderGeometryObject()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a2b9a89fc4a6101419f4783032d3edfcb),
[PointsGui::ViewProviderPoints::ViewProviderPoints()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ac5af34ec9fcf964cf09f3f7eaee50fca),
[RobotGui::TaskTrajectoryDressUpParameter::writeValues()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#a475203e163d2ff851526f84ef0e4011f),
and
[PartGui::DlgProjectionOnSurface::~DlgProjectionOnSurface()](../../d2/da4/classPartGui_1_1DlgProjectionOnSurface.html#a7d2e3355dfa8759dd537d765c4bc8e96).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyStandard.h
  * FreeCAD/src/App/PropertyStandard.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

