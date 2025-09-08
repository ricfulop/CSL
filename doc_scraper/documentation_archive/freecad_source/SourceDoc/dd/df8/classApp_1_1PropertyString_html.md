---
url: https://freecad.github.io/SourceDoc/dd/df8/classApp_1_1PropertyString.html
scraped_at: 2025-09-08T14:56:44.132525
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyString](../../dd/df8/classApp_1_1PropertyString.html)

[List of all members](../../d6/d99/classApp_1_1PropertyString-members.html) | Public Member Functions

App::PropertyString Class Reference

String properties This is the father of all properties handling Strings.
[More...](../../dd/df8/classApp_1_1PropertyString.html#details)

`#include <PropertyStandard.h>`

##  Public Member Functions  
  
---  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../dd/df8/classApp_1_1PropertyString.html#abff429e61e5545bd5b7e94fc7a318ba5) (void) const  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../dd/df8/classApp_1_1PropertyString.html#abff429e61e5545bd5b7e94fc7a318ba5)  
  
virtual const char * | [getEditorName](../../dd/df8/classApp_1_1PropertyString.html#a6d09fe56505033a027f3422fbeedbe12) (void) const  
| Get the class name of the associated property editor item.
[More...](../../dd/df8/classApp_1_1PropertyString.html#a6d09fe56505033a027f3422fbeedbe12)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../dd/df8/classApp_1_1PropertyString.html#a1dacdc31bef9c42aa5da1b0cc1c628bc) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../dd/df8/classApp_1_1PropertyString.html#a1dacdc31bef9c42aa5da1b0cc1c628bc)  
  
const boost::any | [getPathValue](../../dd/df8/classApp_1_1PropertyString.html#a850b24499238db2470453d2db7000fac) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path) const  
| Get value of property.
[More...](../../dd/df8/classApp_1_1PropertyString.html#a850b24499238db2470453d2db7000fac)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../dd/df8/classApp_1_1PropertyString.html#aa6e72d76ecb8d448e1e8016f72f0dd66) (void)  
| This method returns the Python wrapper for a C++ object.
[More...](../../dd/df8/classApp_1_1PropertyString.html#aa6e72d76ecb8d448e1e8016f72f0dd66)  
  
const std::string & | [getStrValue](../../dd/df8/classApp_1_1PropertyString.html#a7fdb947ab6f9552c1dd95a8e634c83c2) (void) const  
const char * | [getValue](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485) (void) const  
[bool](../../d9/db9/classbool.html) | [isEmpty](../../dd/df8/classApp_1_1PropertyString.html#a60f5c44e1aa7580af6c77b57a526368d) (void)  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../dd/df8/classApp_1_1PropertyString.html#a33f0ebb36205838e6f94328870e60ac6) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const  
| Compare if this property has the same content as the given one.
[More...](../../dd/df8/classApp_1_1PropertyString.html#a33f0ebb36205838e6f94328870e60ac6)  
  
virtual void | [Paste](../../dd/df8/classApp_1_1PropertyString.html#a181a70a04d92e6c994a55550abf484c9) (const [Property](../../d0/da9/classApp_1_1Property.html) &from)  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../dd/df8/classApp_1_1PropertyString.html#a181a70a04d92e6c994a55550abf484c9)  
  
|
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html#a63e7a9187eec0dec6227120b9845e072)
(void)  
| A constructor.
[More...](../../dd/df8/classApp_1_1PropertyString.html#a63e7a9187eec0dec6227120b9845e072)  
  
virtual void | [Restore](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1)  
  
virtual void | [Save](../../dd/df8/classApp_1_1PropertyString.html#a22cfc259b6c352cd5f14b3a400704164) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../dd/df8/classApp_1_1PropertyString.html#a22cfc259b6c352cd5f14b3a400704164)  
  
void | [setPathValue](../../dd/df8/classApp_1_1PropertyString.html#abedefbc95eb8ac85e06453ac11806bec) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, const boost::any &value)  
| Set value of property.
[More...](../../dd/df8/classApp_1_1PropertyString.html#abedefbc95eb8ac85e06453ac11806bec)  
  
virtual void | [setPyObject](../../dd/df8/classApp_1_1PropertyString.html#ac9b0f60fd6949cfd514653838e78840b) ([PyObject](../../df/d1b/classPyObject.html) *)  
virtual void | [setValue](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e) (const char *sString)  
void | [setValue](../../dd/df8/classApp_1_1PropertyString.html#a5752b42514e639687f9f832d5063a2c6) (const std::string &sString)  
virtual | [~PropertyString](../../dd/df8/classApp_1_1PropertyString.html#ad74ad3fc034475e54de5c8eecf8bdda6) ()  
| A destructor.
[More...](../../dd/df8/classApp_1_1PropertyString.html#ad74ad3fc034475e54de5c8eecf8bdda6)  
  
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

String properties This is the father of all properties handling Strings.

## Constructor & Destructor Documentation

## ◆ PropertyString()

PropertyString::PropertyString  | ( | void  | | ) |   
---|---|---|---|---|---  
  
A constructor.

A more elaborate description of the constructor.

Referenced by
[Copy()](../../dd/df8/classApp_1_1PropertyString.html#abff429e61e5545bd5b7e94fc7a318ba5).

## ◆ ~PropertyString()

| PropertyString::~PropertyString  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyString::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

Reimplemented in
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a90a82f3560b30c57524eba73104a45e3).

References
[PropertyString()](../../dd/df8/classApp_1_1PropertyString.html#a63e7a9187eec0dec6227120b9845e072).

## ◆ getEditorName()

| virtual const char * App::PropertyString::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

Reimplemented in
[App::PropertyFile](../../d9/d86/classApp_1_1PropertyFile.html#ac3494f9267e386fa8cec4f87232316be),
and
[App::PropertyFont](../../df/d8c/classApp_1_1PropertyFont.html#ab9a098db6ead92fbfd290c8708cec1e3).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) PropertyString::getMemSize  | ( | void  | | ) |  const  
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

Reimplemented in
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a8487b7c73af09eed5681c133040fb417).

Referenced by
[App::PropertyPersistentObject::getMemSize()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a8487b7c73af09eed5681c133040fb417).

## ◆ getPathValue()

| const boost::any PropertyString::getPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Get value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea).

References
[App::Property::verifyPath()](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyString::getPyObject  | ( | void  | | ) |   
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

Reimplemented in
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#afd3cb0bbe7979346fb4b2e39cf7b076f).

Referenced by
[App::PropertyXLink::getPyObject()](../../d2/de2/classApp_1_1PropertyXLink.html#ac41751baabdd2bcb04a996719004377e),
[App::PropertyXLinkSub::getPyObject()](../../d4/da0/classApp_1_1PropertyXLinkSub.html#ad996567330d5c7b6255da532d74ae9b5),
and
[App::PropertyEnumeration::getPyPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1cf1f360d2873e83ce77ce6cf97f8322).

## ◆ getStrValue()

const std::string & App::PropertyString::getStrValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[TechDraw::DrawViewDimension::getFormattedDimensionValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a92f36b1b5e044976e4a117424b000985),
[TechDraw::DrawViewDimension::getFormattedToleranceValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aac71dbd0561262809d791806fc44775d),
[TechDraw::DrawViewDimension::getFormattedToleranceValues()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a8235b120b82f24a29c6be38d6afff542),
[Gui::ViewProviderPart::getIcon()](../../d9/d6c/classGui_1_1ViewProviderPart.html#afba5f47c9f0f811fe7983cac5c6f5fa3),
[App::Document::onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
[App::PropertyLinkBase::restoreLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb),
[App::Document::saveAs()](../../d8/d3e/classApp_1_1Document.html#a99cf956cb95ce19b87c4ea7e1d5087ee),
[App::Document::saveCopy()](../../d8/d3e/classApp_1_1Document.html#acbad1e96391e2f6067dfdf23a9bdb044),
[App::PropertyXLink::setPyObject()](../../d2/de2/classApp_1_1PropertyXLink.html#adb26821a0a3916e6252bc6b4f0c5637e),
[TechDrawGui::QGIViewBalloon::setViewPartFeature()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6f17a801836429d822e8998b0edfbff5),
[App::RelabelDocumentExpressionVisitor::visit()](../../db/dfd/classApp_1_1RelabelDocumentExpressionVisitor.html#aa37c20588af574df4ceaa95468660f18),
and
[MeshPartGui::Mesh2ShapeGmsh::writeProject()](../../db/d4d/classMeshPartGui_1_1Mesh2ShapeGmsh.html#a3931d67654b40d307417d697e6291ab3).

## ◆ getValue()

const char * PropertyString::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[MeshGui::Segmentation::accept()](../../da/d24/classMeshGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[MeshGui::SegmentationBestFit::accept()](../../d8/dc7/classMeshGui_1_1SegmentationBestFit.html#a22c228aaefd47e1621d12b98efd38ad8),
[PartGui::SweepWidget::accept()](../../d0/dda/classPartGui_1_1SweepWidget.html#ac9e4d005b6e7ecc3ddae3c22258fd8a5),
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[Gui::ExpressionBinding::apply()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a0f027ccb09e2a67dd2aba44d35edb2d2),
[Gui::ViewProviderOriginFeature::attach()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#aac32ddea00ce5374fa432bad0540355a),
[Gui::Document::canClose()](../../de/d4e/classGui_1_1Document.html#a9d5a988c5980ecdafede499fa261d135),
[SurfaceGui::FillingPanel::checkOpenCommand()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#af89e0fc6c9df9e0a5f3e4e966fcbd76f),
[SurfaceGui::FillingEdgePanel::checkOpenCommand()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a5a9ee6e2c42e74538ab2ca085fe087cb),
[SurfaceGui::FillingVertexPanel::checkOpenCommand()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a90551017148fdaedcce1af12566687da),
[SurfaceGui::GeomFillSurface::checkOpenCommand()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#a184573c3baebee00c61b77bdad207b9e),
[SurfaceGui::SectionsPanel::checkOpenCommand()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#ab9168c66c4f0a26633cbaa855d1743a7),
[Part::Extrusion::computeFinalParameters()](../../db/d6c/classPart_1_1Extrusion.html#a4b4ddc216eb6449e2b21480a430f5df8),
[Import::ExportOCAF::createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[Gui::Document::createView()](../../de/d4e/classGui_1_1Document.html#a1235bbc0ddca0b8c9465d9d491d79541),
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[SpreadsheetGui::DlgBindSheet::DlgBindSheet()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#accc9c51aedc023f92d7d5a21304b0b62),
[Gui::DocumentObjectData::DocumentObjectData()](../../d6/d82/classGui_1_1DocumentObjectData.html#aef9adb6717b71286982c27610e989f18),
[PartDesignGui::ViewProviderDatum::doubleClicked()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a588caea71c3f6afedfddf98adfb9f038),
[TechDrawGui::QGIViewPart::drawHighlight()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#aac8834c3546b27902b1c3543d4a8e32e),
[Gui::ViewProviderAnnotationLabel::drawImage()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a37530affd46043649525097fa5ff8e05),
[TechDrawGui::QGIViewPart::drawSectionLine()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a513e571f325b7c7cac09bdec0d1c512d),
[TechDrawGui::QGIWeldSymbol::drawTailText()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#ade5f6fb54a953f66e157e6d363160707),
[TechDrawGui::QGIWeldSymbol::drawTile()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a95de553829cc9844a9e95b1bdbd36e76),
[Gui::ElementColors::ElementColors()](../../db/d21/classGui_1_1ElementColors.html#a7d0d5836a9361c145408b75cf8b0b33c),
[Mesh::Export::execute()](../../d6/d40/classMesh_1_1Export.html#a56265dded005a8be13258af1b273ed51),
[Mesh::SetOperations::execute()](../../d3/d8f/classMesh_1_1SetOperations.html#a5fbee709af3e7da8f267824be4c4b370),
[Drawing::FeatureClip::execute()](../../d5/d4a/classDrawing_1_1FeatureClip.html#afed75650f49849b96c65ef93795800e5),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Drawing::FeatureViewAnnotation::execute()](../../d6/de7/classDrawing_1_1FeatureViewAnnotation.html#a74171a078f54a6d0ee13242e3b014751),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Drawing::FeatureViewSymbol::execute()](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#a3563b4ff57807e29d705c04a53b7cd0b),
[Inspection::Feature::execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[Part::CurveNet::execute()](../../d9/d41/classPart_1_1CurveNet.html#ab3d3703fdaab33d94b764c62d6739ce6),
[Part::ImportBrep::execute()](../../d8/d3e/classPart_1_1ImportBrep.html#a3fbd619fb350dff418fffd6b6f185ca7),
[Part::ImportIges::execute()](../../d2/d1d/classPart_1_1ImportIges.html#a1d947e212fdeb8ed2b8bb8ef3fae1041),
[Part::ImportStep::execute()](../../d4/de2/classPart_1_1ImportStep.html#a3c81f94deddd927756144ef4e8040678),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[TechDraw::DrawParametricTemplate::execute()](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#acc1380e0737504ec1d64b2bbca2380e6),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDraw::DrawViewSpreadsheet::execute()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a2d98f05816771e2b3a057443ea2f981c),
[Part::Face::execute()](../../dc/dbf/classPart_1_1Face.html#a7e0c10e1928c118064cc40586322ca36),
[Part::Revolution::execute()](../../d3/d17/classPart_1_1Revolution.html#a0406e2da5876bbf2351991c6b48b7185),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[TechDraw::DrawViewSymbol::execute()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a44eea88d3e8522c41e9dcee9acff10ce),
[MeshGui::ViewProviderMesh::exportMesh()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a7e475ac2c734112a916b21ec3ffa8f8c),
[App::OriginGroupExtension::extensionGetSubObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11),
[Part::AttachExtension::extensionOnChanged()](../../dc/d47/classPart_1_1AttachExtension.html#ac73db2d8f32ca41b89157b47edce44c1),
[PartGui::FaceColors::FaceColors()](../../db/d9e/classPartGui_1_1FaceColors.html#a5aef3588ddb084101d511fc687ac45d7),
[PartGui::DlgExtrusion::findShapes()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8976c72de1970766d8d2dc5391e34903),
[Fem::FemPostDataAlongLineFilter::GetAxisData()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ac3850d76cbd006a0d9f86f6971463cf2),
[TechDraw::DrawGeomHatch::getDecodedSpecsFromFile()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9310adb90d17a4212adfe5751cb9d55c),
[TechDraw::DrawProjGroup::getDirsFromFront()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a66cbbc8038fcab5532278784cbac867b),
[TechDraw::DrawSVGTemplate::getEditableTextsFromTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a5d4fd489066be062afb816f45960c214),
[Drawing::FeaturePage::getEditableTextsFromTemplate()](../../db/d0f/classDrawing_1_1FeaturePage.html#af1b06dab1d22245e410d1a251f5eda96),
[App::Document::getFileName()](../../d8/d3e/classApp_1_1Document.html#a6710d0e8dbf515ba6f04a0f6be31c21d),
[Spreadsheet::Cell::getFormattedQuantity()](../../d5/d22/classSpreadsheet_1_1Cell.html#a66a4fb5ffaa93232823dfbe49833ab7b),
[Gui::LinkInfo::getLinkedLabel()](../../d4/da4/classGui_1_1LinkInfo.html#a159af4c143bfb19a75233b87d6a780c8),
[TechDrawGui::TaskGeomHatch::getParameters()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#aeb7fd1b271e9d19d70da0b903137a3e0),
[Fem::FemPostDataAtPointFilter::GetPointData()](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#a72628069cbee6b9a5952177708496fd9),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[Import::ImportOCAF2::ImportOCAF2()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a1778a18213d37ff08892e030cb9cbd2c),
[TechDraw::DrawHatch::isBitmapHatch()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a6cd818ffc795a57c95dff46e117be1dc),
[App::Document::isSaved()](../../d8/d3e/classApp_1_1Document.html#a730da4f4ddab904051e5f1a031577b27),
[TechDraw::DrawHatch::isSvgHatch()](../../d0/d97/classTechDraw_1_1DrawHatch.html#ab74a45f89d5d30095178c7b1621bd5fe),
[TechDrawGui::TaskLinkDim::loadToTree()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#a78901c66da67bb8e9a3a97469e4f61d4),
[MeshGui::MeshSplit::makeCopy()](../../d9/de5/classMeshGui_1_1MeshSplit.html#aae5f989f78a6a83f6f2f1f8dabfd1a56),
[TechDraw::DrawViewSection::makeLineSets()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a8673a58822bb65ebe493c128d2aef29e),
[TechDrawGui::QGITile::makeSymbol()](../../d6/d9b/classTechDrawGui_1_1QGITile.html#a5851fb4b25a7accc37d273a1c924a4b1),
[TechDrawGui::QGIRichAnno::mouseDoubleClickEvent()](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#ae314ffc101d4592c4a492f380ce72655),
[App::Document::onBeforeChange()](../../d8/d3e/classApp_1_1Document.html#a84bc36d18a86fca95c88aa31308f0bf3),
[Gui::ViewProviderAnnotation::onChanged()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#a789aabe3e009284175581640dec663c3),
[Gui::ViewProviderTextDocument::onChanged()](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a8d87ca622183dd3077563ad3d45c479b),
[Drawing::FeatureViewSymbol::onChanged()](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#aaf6475415e3e3e4e35ad6d1cd034f7fc),
[TechDraw::DrawTileWeld::onChanged()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a4241390f45c70002f410b5c78a4d0452),
[TechDraw::DrawGeomHatch::onChanged()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9942ef5dd5ecef6dba83a1245a0840ca),
[TechDraw::DrawHatch::onChanged()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a655588bfe5d6ff663e4aefc40c118a58),
[TechDraw::DrawPage::onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawViewDetail::onChanged()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewSection::onChanged()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[TechDraw::DrawViewSymbol::onChanged()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#adb3364984aac5da2ff804a43845ceee4),
[Drawing::FeaturePage::onDocumentRestored()](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e),
[Raytracing::LuxProject::onDocumentRestored()](../../d5/de6/classRaytracing_1_1LuxProject.html#af2f620cf5c7c096d24b4ad220123c909),
[Raytracing::RayProject::onDocumentRestored()](../../d2/d89/classRaytracing_1_1RayProject.html#a9d83bff4b32c1801a8ba907221d45295),
[TechDraw::DrawTileWeld::onDocumentRestored()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a7a4b1b5d8aac6cdb9a3a16997934c000),
[TechDraw::DrawGeomHatch::onDocumentRestored()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a236c7efbf2e991277bd53a914eb247bb),
[TechDraw::DrawHatch::onDocumentRestored()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a3437412caff103d7c68842db2e694a7b),
[TechDraw::DrawViewSection::onDocumentRestored()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a639636de121b31e8f97a010b214fb71e),
[TechDrawGui::TaskWeldingSymbol::onFlipSidesClicked()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#ad0e10139d821a4f81e7de9959eb62215),
[Gui::MDIView::onRelabel()](../../df/d23/classGui_1_1MDIView.html#afcbfda847bb899e50b614fe491b76cf9),
[DrawingGui::DrawingView::onRelabel()](../../da/d65/classDrawingGui_1_1DrawingView.html#aa6defb7630d57ca8d919679b10ea424e),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[SurfaceGui::FillingPanel::onSelectionChanged()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#ac8f46981ec84ea0a20faf5791db7cb4b),
[SurfaceGui::FillingEdgePanel::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a13eada025c84a3c28016f3c3974d089d),
[SurfaceGui::FillingVertexPanel::onSelectionChanged()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a67388941ba03ae81ee5e15d8043bbc02),
[SurfaceGui::GeomFillSurface::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#acd70791d15b148166826bac85bc802e9),
[SurfaceGui::SectionsPanel::onSelectionChanged()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#a919af91b2e734c27e20773a1f737a49c),
[App::Application::openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
[TechDrawGui::QGSPage::postProcessXml()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#ac4055009ba04a7f89f6c9a935e4ce0a5),
[TechDraw::DrawSVGTemplate::processTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a9b2032d4f9db58231ae4ad79ca5b3778),
[App::Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
[App::OriginGroupExtension::relinkToOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#af4330ed14ea93ff3cbf7d0f952cf5e49),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
[App::VRMLObject::RestoreDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a90cb824c6253de535ec16e1935455599),
[Sandbox::DocumentSaverThread::run()](../../d9/d1c/classSandbox_1_1DocumentSaverThread.html#a4eda162d7f2ad445c7e4ef89b8071ed6),
[App::Document::save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
[App::VRMLObject::SaveDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a5dc3cc5b304d0866d30a0ad975cc4ccd),
[TechDrawGui::TaskHatch::saveHatchState()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#a51dcb76a4ea06574a94e4e4eaf492e2b),
[TechDrawGui::TaskSectionView::saveSectionState()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a6766d05bef0b8b54751ef23c124d3eb2),
[Import::ExportOCAF::saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[TechDraw::DrawViewSection::sectionExec()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a79c8f60f63dd54684af4cad42f91ee4e),
[Part::AttachExtension::setAttacher()](../../dc/d47/classPart_1_1AttachExtension.html#a1e4d65c3b672b1760b037891d419e065),
[SurfaceGui::FillingPanel::setEditedObject()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#aaaeba016fe808b6dc4d3ddfc9788d380),
[Gui::ExpressionBinding::setExpression()](../../dc/d5a/classGui_1_1ExpressionBinding.html#ab4b4f84605e7bf21c036c6a9a09fbb2f),
[RobotGui::TaskEdge2TracParameter::setHideShowObject()](../../d0/dbf/classRobotGui_1_1TaskEdge2TracParameter.html#a4f0db452c19a0f88335d993d587a371b),
[Import::ImportOCAF2::setMode()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a865601fce708b9141eb0bbf40b3e96f8),
[App::PropertyLinkSub::setPyObject()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9965507bfcc6e28d251ffb62f234df77),
[App::PropertyLinkSubList::setPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a495ec38be0d7ceb20aa9b3d5a520fdfa),
[TechDrawGui::QGIRichAnno::setTextItem()](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#a27fd9afb78b8c22eeadd556d985030fe),
[TechDrawGui::TaskSectionView::setUiEdit()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a43dc3542cf896d0778a028ae2be230ce),
[TechDrawGui::TaskWeldingSymbol::setUiEdit()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#aa3e9fde175112fd5b2308f32bd93a33c),
[TechDrawGui::TaskRichAnno::setUiEdit()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a3659e9cb13bc53ae36a3d7d16479d017),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[TechDraw::DrawHatch::setupFileIncluded()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a0846fb8f0861b48c08a9b869612e130b),
[TechDraw::DrawGeomHatch::setupPatIncluded()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a60fb2b1d4310efa884589ce415b086c9),
[TechDraw::DrawViewSection::setupPatIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#af26e22d3b0683c955561590968b25275),
[TechDraw::DrawViewSection::setupSvgIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a3736e6db938d365a0866d6704bcb3fe0),
[TechDraw::DrawTileWeld::setupSymbolIncluded()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a9a0ec49268483ff93a086ca6a58c58da),
[PartDesignGui::TaskDressUpParameters::setupTransaction()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a6f99d504a2dbb11111be017f2bfe4bbf),
[DrawingGui::ViewProviderDrawingPage::showDrawingView()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#af7cd2898c5d4d289f22f0fb7c232984f),
[SpreadsheetGui::ViewProviderSheet::showSpreadsheetView()](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a912de2c5ce615efc6d1e3f70f3674f1b),
[Gui::AutoSaver::slotCreateDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#ac494a904b86d92d32163dab8049b0d80),
[TechDrawGui::TaskBalloon::TaskBalloon()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#a21f34d1bf15390ec9c984c7c75ab9996),
[TechDrawGui::TaskDimension::TaskDimension()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a01dec85a4db02858073f304508300ff3),
[FemGui::TaskObjectName::TaskObjectName()](../../d3/d6b/classFemGui_1_1TaskObjectName.html#ae998f7ddece0813597d374c662db31b7),
[PartDesignGui::TaskPipeOrientation::TaskPipeOrientation()](../../d8/df3/classPartDesignGui_1_1TaskPipeOrientation.html#ac6d362fde0b1452a942b513494180d97),
[PartDesignGui::TaskPipeParameters::TaskPipeParameters()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#ad8be386ff75b6d3c414ffbe505e48561),
[App::PropertyLinkBase::tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95),
[TechDraw::DrawProjGroupItem::unsetupObject()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a74c1e831d9704f99007d0b9398001f90),
[SpreadsheetGui::SheetView::updateCell()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#afe16747ee261395854ecdfb7d5326901),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[DrawingGui::ViewProviderDrawingPage::updateData()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a885c2ea64eae6ad57aeed5d42a1a05dd),
and
[App::Document::~Document()](../../d8/d3e/classApp_1_1Document.html#ac2e3f62307dc22baac21ddc10fa1609c).

## ◆ isEmpty()

[bool](../../d9/db9/classbool.html) App::PropertyString::isEmpty  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Referenced by
[TechDraw::DrawGeomHatch::makeLineSets()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a0736be1ff7a1996022a4d944f9d82e19),
[TechDraw::DrawViewSection::makeLineSets()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a8673a58822bb65ebe493c128d2aef29e),
[TechDraw::DrawTileWeld::onChanged()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a4241390f45c70002f410b5c78a4d0452),
[TechDraw::DrawGeomHatch::onChanged()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9942ef5dd5ecef6dba83a1245a0840ca),
[TechDraw::DrawHatch::onChanged()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a655588bfe5d6ff663e4aefc40c118a58),
[TechDraw::DrawViewSection::onChanged()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[TechDraw::DrawTileWeld::onDocumentRestored()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a7a4b1b5d8aac6cdb9a3a16997934c000),
[TechDraw::DrawGeomHatch::onDocumentRestored()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a236c7efbf2e991277bd53a914eb247bb),
[TechDraw::DrawHatch::onDocumentRestored()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a3437412caff103d7c68842db2e694a7b),
[TechDraw::DrawViewSection::onDocumentRestored()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a639636de121b31e8f97a010b214fb71e),
[TechDraw::DrawHatch::setupFileIncluded()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a0846fb8f0861b48c08a9b869612e130b),
[TechDraw::DrawGeomHatch::setupPatIncluded()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a60fb2b1d4310efa884589ce415b086c9),
and
[TechDraw::DrawViewSection::setupPatIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#af26e22d3b0683c955561590968b25275).

## ◆ isSame()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyString::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

Reimplemented in
[App::PropertyFont](../../df/d8c/classApp_1_1PropertyFont.html#a9bf6ebb41630ff61cecf13cf6436afca).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

## ◆ Paste()

| void PropertyString::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
virtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be).

Reimplemented in
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aa32598aecbbb59a82597e21ef43b3273).

References
[setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

## ◆ Restore()

| void PropertyString::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../dd/df8/classApp_1_1PropertyString.html#a22cfc259b6c352cd5f14b3a400704164
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

Reimplemented in
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a13c0f90fcb93033f1114904553aaee4c).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[Base::XMLReader::getName()](../../dc/d95/classBase_1_1XMLReader.html#aa529233af401d7719226293c506792f8),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
and
[setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

Referenced by
[App::PropertyPersistentObject::Restore()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a13c0f90fcb93033f1114904553aaee4c).

## ◆ Save()

| void PropertyString::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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

Reimplemented in
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aaab9b1d794bd67a605f6aef13f00e9f7).

References
[Base::Persistence::encodeAttribute()](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

Referenced by
[App::PropertyPersistentObject::Save()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aaab9b1d794bd67a605f6aef13f00e9f7).

## ◆ setPathValue()

| void PropertyString::setPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | const boost::any & | _value_  
| ) | |   
virtual  
  
Set value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22).

References
[App::pyObjectFromAny()](../../dd/dc2/namespaceApp.html#a0fd92b74207e681fd5b4a27a5c70f0c0),
[setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
and
[App::Property::verifyPath()](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7).

## ◆ setPyObject()

| void PropertyString::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

References
[setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

Referenced by
[App::PropertyLinkSub::setPyObject()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9965507bfcc6e28d251ffb62f234df77),
[App::PropertyLinkSubList::setPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a495ec38be0d7ceb20aa9b3d5a520fdfa),
and
[App::PropertyXLink::setPyObject()](../../d2/de2/classApp_1_1PropertyXLink.html#adb26821a0a3916e6252bc6b4f0c5637e).

## ◆ setValue() [1/2]

| void PropertyString::setValue  | ( | const char *  | _sString_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a117bd17a68a39872c084cf4e48401922).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::Application::closeActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a65f9fb03ff7053cfb14dd230451ae0a9),
[DraftVecUtils::find()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf764683bba7871d8f3d64db4fb2a41a9),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[ParameterGrp::GetBool()](../../d4/d97/classParameterGrp.html#a603e85aad05116d3331f865715297d08),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[ParameterGrp::GetGroup()](../../d4/d97/classParameterGrp.html#a47f104b383bc5ce440588d1dd60e867e),
[Base::Tools::getUniqueName()](../../d6/dda/structBase_1_1Tools.html#a2e5fcd4db818dbcce127c0695ffe937b),
[App::Application::GetUserParameter()](../../da/dbf/classApp_1_1Application.html#adb4f3ab9508bc0a64c2dbed546348c47),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
[App::Document::Importing](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3fcdf22c3e8c2aea788606a837c7d522),
[App::Document::Restoring](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3ad0fd87f9bec83cb5d1b8096b3b09ec),
[App::Application::setActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a78fddfc24e060908e047c5472857c3ff),
and
[App::PropertyLinkBase::updateLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a352aa734ca82348678cc710b1eead0ef).

Referenced by
[FemGui::TaskDlgCreateNodeSet::accept()](../../d9/d8f/classFemGui_1_1TaskDlgCreateNodeSet.html#aae7b7afa431004b899003fe789f532bb),
[MeshGui::Segmentation::accept()](../../da/d24/classMeshGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[MeshGui::SegmentationBestFit::accept()](../../d8/dc7/classMeshGui_1_1SegmentationBestFit.html#a22c228aaefd47e1621d12b98efd38ad8),
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[TechDrawGui::TaskCustomizeFormat::accept()](../../db/dde/classTechDrawGui_1_1TaskCustomizeFormat.html#ac65e54467705d01196d828596c6ed2d0),
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[TechDrawGui::TaskRichAnno::commonFeatureUpdate()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ab5a728afdf435f4c1631b56211559576),
[TechDrawGui::QGSPage::createBalloon()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#afa6582dc212925fd365ed71b38127d78),
[Gui::PointMarker::customEvent()](../../d6/deb/classGui_1_1PointMarker.html#af3aff66aa9cfaaff337386e66a61c0f4),
[PartGui::DlgProjectionOnSurface::DlgProjectionOnSurface()](../../d2/da4/classPartGui_1_1DlgProjectionOnSurface.html#a280d8ac8bf690484a268f54625c2c7e2),
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12),
[Drawing::FeatureClip::execute()](../../d5/d4a/classDrawing_1_1FeatureClip.html#afed75650f49849b96c65ef93795800e5),
[Drawing::FeatureViewAnnotation::execute()](../../d6/de7/classDrawing_1_1FeatureViewAnnotation.html#a74171a078f54a6d0ee13242e3b014751),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Drawing::FeatureViewSymbol::execute()](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#a3563b4ff57807e29d705c04a53b7cd0b),
[Raytracing::LuxFeature::execute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a235b146fb9255cb705a6b86fb6967c3d),
[Raytracing::RayFeature::execute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[TechDraw::DrawViewSpreadsheet::execute()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a2d98f05816771e2b3a057443ea2f981c),
[TechDraw::DrawViewSymbol::execute()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a44eea88d3e8522c41e9dcee9acff10ce),
[App::PropertyXLink::getPyObject()](../../d2/de2/classApp_1_1PropertyXLink.html#ac41751baabdd2bcb04a996719004377e),
[App::PropertyXLinkSub::getPyObject()](../../d4/da0/classApp_1_1PropertyXLinkSub.html#ad996567330d5c7b6255da532d74ae9b5),
[App::PropertyEnumeration::getPyPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1cf1f360d2873e83ce77ce6cf97f8322),
[Part::ImportIgesParts()](../../d2/db9/namespacePart.html#a10322b892abc3b1779054dacf1a49e53),
[MeshPartGui::Mesh2ShapeGmsh::loadOutput()](../../db/d4d/classMeshPartGui_1_1Mesh2ShapeGmsh.html#a44307c501da72ba058c29e10998ef358),
[Import::ImportOCAF2::loadShapes()](../../d9/ddd/classImport_1_1ImportOCAF2.html#afa667a1c5c88cd6565d91740bf38ea61),
[MeshGui::MeshSplit::makeCopy()](../../d9/de5/classMeshGui_1_1MeshSplit.html#aae5f989f78a6a83f6f2f1f8dabfd1a56),
[TechDrawGui::QGIRichAnno::mouseDoubleClickEvent()](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#ae314ffc101d4592c4a492f380ce72655),
[TechDraw::DrawSVGTemplate::onChanged()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#afa43ef4d1bf529675b75c5d31fff582b),
[TechDraw::DrawViewDetail::onChanged()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewSection::onChanged()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[App::Document::onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
[Drawing::FeaturePage::onDocumentRestored()](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e),
[Raytracing::LuxProject::onDocumentRestored()](../../d5/de6/classRaytracing_1_1LuxProject.html#af2f620cf5c7c096d24b4ad220123c909),
[Raytracing::RayProject::onDocumentRestored()](../../d2/d89/classRaytracing_1_1RayProject.html#a9d83bff4b32c1801a8ba907221d45295),
[TechDrawGui::TaskGeomHatch::onFileChanged()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#ac0cd5c474ae673fe795d53e569ccf5e3),
[App::Application::openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
[Paste()](../../dd/df8/classApp_1_1PropertyString.html#a181a70a04d92e6c994a55550abf484c9),
[TechDrawGui::TaskGeomHatch::reject()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a18ae3da7ea9b2d55123cd563ed408217),
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
[Restore()](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[TechDrawGui::TaskHatch::restoreHatchState()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ad4a3916be744e9438b81e65cddfb14d3),
[TechDrawGui::TaskSectionView::restoreSectionState()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a31ebe04f8add6f5d1c665c9b7c12c238),
[Sandbox::DocumentTestThread::run()](../../d5/d8a/classSandbox_1_1DocumentTestThread.html#a27751a48ad75c90b8b678641eb975cde),
[App::Document::save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
[App::Document::saveAs()](../../d8/d3e/classApp_1_1Document.html#a99cf956cb95ce19b87c4ea7e1d5087ee),
[DrawingGui::orthoview::set_data()](../../db/df8/classDrawingGui_1_1orthoview.html#a3395e8771fab71cac84a95eeae04c721),
[Part::AttachExtension::setAttacher()](../../dc/d47/classPart_1_1AttachExtension.html#a1e4d65c3b672b1760b037891d419e065),
[Gui::DocumentItem::setData()](../../df/d15/classGui_1_1DocumentItem.html#a5326e93665664b6b41b5bbf1b3389cb6),
[App::LinkBaseExtension::setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4),
[setPathValue()](../../dd/df8/classApp_1_1PropertyString.html#abedefbc95eb8ac85e06453ac11806bec),
[setPyObject()](../../dd/df8/classApp_1_1PropertyString.html#ac9b0f60fd6949cfd514653838e78840b),
[Spreadsheet::Sheet::setStringProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a217878fa6e8ba03d534f5f22e44bce17),
[App::Origin::setupObject()](../../d9/d8b/classApp_1_1Origin.html#af5708fed01b27a82a33d8b06d02e89e6),
[Part::Face::setupObject()](../../dc/dbf/classPart_1_1Face.html#ac21ea7f5cfc94b6dc0473be52f3b2009),
[setValue()](../../dd/df8/classApp_1_1PropertyString.html#a5752b42514e639687f9f832d5063a2c6),
[MeshGui::Annotation::show()](../../dd/d2d/classMeshGui_1_1Annotation.html#a8e675bcb0e642864e58f2d9f3b482ca8),
[TechDrawGui::TaskDetail::updateDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a9531ab9a77b992bbde7893f620cddd9f),
[TechDrawGui::TaskWeldingSymbol::updateTiles()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#aac480071122ff57d72a8cba865b1c94c),
and
[TechDrawGui::TaskGeomHatch::updateValues()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a12acdd2beb497c2bfd197b8d8234f389).

## ◆ setValue() [2/2]

void PropertyString::setValue  | ( | const std::string & | _sString_| ) |   
---|---|---|---|---|---  
  
References
[setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyStandard.h
  * FreeCAD/src/App/PropertyStandard.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

