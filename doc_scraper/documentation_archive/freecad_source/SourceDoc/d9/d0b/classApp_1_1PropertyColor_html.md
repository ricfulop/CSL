---
url: https://freecad.github.io/SourceDoc/d9/d0b/classApp_1_1PropertyColor.html
scraped_at: 2025-09-08T14:55:31.750999
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html)

[List of all members](../../dc/d30/classApp_1_1PropertyColor-members.html) | Public Member Functions

App::PropertyColor Class Reference

[Color](../../d3/d3a/classApp_1_1Color.html "Color class.") properties This is
the father of all properties handling colors.
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#details)

`#include <PropertyStandard.h>`

##  Public Member Functions  
  
---  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d9/d0b/classApp_1_1PropertyColor.html#ab957657dcd3846e19a36a68ba488480f) (void) const  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#ab957657dcd3846e19a36a68ba488480f)  
  
virtual const char * | [getEditorName](../../d9/d0b/classApp_1_1PropertyColor.html#aacd84999061807220844be7fff48153e) (void) const  
| Get the class name of the associated property editor item.
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#aacd84999061807220844be7fff48153e)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d9/d0b/classApp_1_1PropertyColor.html#acfb47acb28b9927f07d24bcb1248c317) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#acfb47acb28b9927f07d24bcb1248c317)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d9/d0b/classApp_1_1PropertyColor.html#a582beb9405c28ab69e9e52f70b99ce5b) (void)  
| This method returns the Python wrapper for a C++ object.
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#a582beb9405c28ab69e9e52f70b99ce5b)  
  
const [Color](../../d3/d3a/classApp_1_1Color.html) & | [getValue](../../d9/d0b/classApp_1_1PropertyColor.html#ad5edc545f1f19ec00b51f42cdbc62bb6) (void) const  
| This method returns a string representation of the property.
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#ad5edc545f1f19ec00b51f42cdbc62bb6)  
  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d9/d0b/classApp_1_1PropertyColor.html#adeb2113cc4d951709b1cb609cbadc977) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const  
| Compare if this property has the same content as the given one.
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#adeb2113cc4d951709b1cb609cbadc977)  
  
virtual void | [Paste](../../d9/d0b/classApp_1_1PropertyColor.html#a6f089f8323aec6afbf91c66680581c69) (const [Property](../../d0/da9/classApp_1_1Property.html) &from)  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#a6f089f8323aec6afbf91c66680581c69)  
  
|
[PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#a906fcc6f20fbb8fec4fe9463bfad40b3)
()  
| A constructor.
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#a906fcc6f20fbb8fec4fe9463bfad40b3)  
  
virtual void | [Restore](../../d9/d0b/classApp_1_1PropertyColor.html#a4e375cae7bed77bacf0a6dd30794212e) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#a4e375cae7bed77bacf0a6dd30794212e)  
  
virtual void | [Save](../../d9/d0b/classApp_1_1PropertyColor.html#a0b4dc7c8284cd7511308f8bb55dc56d0) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#a0b4dc7c8284cd7511308f8bb55dc56d0)  
  
virtual void | [setPyObject](../../d9/d0b/classApp_1_1PropertyColor.html#a6e633e7e63cde42f29ea066464910433) ([PyObject](../../df/d1b/classPyObject.html) *)  
void | [setValue](../../d9/d0b/classApp_1_1PropertyColor.html#a4aab2001271a7767ba2e47c681286b27) (const [Color](../../d3/d3a/classApp_1_1Color.html) &col)  
| Sets the property.
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#a4aab2001271a7767ba2e47c681286b27)  
  
void | [setValue](../../d9/d0b/classApp_1_1PropertyColor.html#a1166db77e62578bf82da1c82a7ec653c) (float r, float g, float b, float a=0.0f)  
void | [setValue](../../d9/d0b/classApp_1_1PropertyColor.html#a299328360c0e247d3199c7eb4dbc33b6) (uint32_t rgba)  
virtual | [~PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#afdf7e79d2761c66a449c5de767f6b1ca) ()  
| A destructor.
[More...](../../d9/d0b/classApp_1_1PropertyColor.html#afdf7e79d2761c66a449c5de767f6b1ca)  
  
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

[Color](../../d3/d3a/classApp_1_1Color.html "Color class.") properties This is
the father of all properties handling colors.

## Constructor & Destructor Documentation

## ◆ PropertyColor()

PropertyColor::PropertyColor  | ( | | ) |   
---|---|---|---|---  
  
A constructor.

A more elaborate description of the constructor.

Referenced by
[Copy()](../../d9/d0b/classApp_1_1PropertyColor.html#ab957657dcd3846e19a36a68ba488480f).

## ◆ ~PropertyColor()

| PropertyColor::~PropertyColor  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyColor::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

References
[PropertyColor()](../../d9/d0b/classApp_1_1PropertyColor.html#a906fcc6f20fbb8fec4fe9463bfad40b3).

## ◆ getEditorName()

| virtual const char * App::PropertyColor::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

## ◆ getMemSize()

| virtual unsigned [int](../../d1/da0/classint.html) App::PropertyColor::getMemSize  | ( | void  | | ) |  const  
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

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyColor::getPyObject  | ( | void  | | ) |   
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

const [Color](../../d3/d3a/classApp_1_1Color.html) & PropertyColor::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
This method returns a string representation of the property.

Referenced by
[MeshGui::ViewProviderFace::attach()](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#ad7b2603bd549bbf7120aa424fc0adf77),
[MeshGui::ViewProviderMesh::deselectFacet()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a06eaae52efbc33b134f1826ef1a3b776),
[Gui::ViewProviderAnnotationLabel::drawImage()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a37530affd46043649525097fa5ff8e05),
[TechDrawGui::QGIViewSection::drawSectionFace()](../../d7/d73/classTechDrawGui_1_1QGIViewSection.html#a23b734cc85fce28a0a42c4d061686cb4),
[TechDrawGui::QGIViewPart::drawViewPart()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#add7c40ff3fc3fcc84308bb29225f8cc9),
[Drawing::FeatureViewAnnotation::execute()](../../d6/de7/classDrawing_1_1FeatureViewAnnotation.html#a74171a078f54a6d0ee13242e3b014751),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Raytracing::LuxFeature::execute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a235b146fb9255cb705a6b86fb6967c3d),
[Raytracing::RayFeature::execute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[ImportGui::ExportOCAFGui::findColors()](../../d7/dd1/classImportGui_1_1ExportOCAFGui.html#a1c4f907241651d44fa92f9d57984d5b6),
[PartGui::ViewProviderPartExt::getElementColors()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a15bdce85211acfec231620d1fea14805),
[TechDrawGui::TaskGeomHatch::getParameters()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#aeb7fd1b271e9d19d70da0b903137a3e0),
[App::PropertyColorList::getPyValue()](../../d0/dc7/classApp_1_1PropertyColorList.html#a1185ac555445591be3ab82499256987f),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[PartDesignGui::ViewProviderShapeBinder::highlightReferences()](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#a88fdfde939bae5a7f7d2ed7d3865a9a8),
[SurfaceGui::ViewProviderGeomFillSurface::highlightReferences()](../../d8/d03/classSurfaceGui_1_1ViewProviderGeomFillSurface.html#afd24c1bff0f16348ac08835e3514b73e),
[PartDesignGui::ViewProviderDressUp::highlightReferences()](../../dd/dfd/classPartDesignGui_1_1ViewProviderDressUp.html#ac12fbf092e55153a3af0847db4101b5e),
[FemGui::ViewProviderFemConstraintOnBoundary::highlightReferences()](../../da/d5f/classFemGui_1_1ViewProviderFemConstraintOnBoundary.html#a1586daa50943e93d852dadff457479f0),
[SurfaceGui::ViewProviderFilling::highlightReferences()](../../d0/dac/classSurfaceGui_1_1ViewProviderFilling.html#a78761462883c0d6cc686968c9a1e9c1b),
[SurfaceGui::ViewProviderSections::highlightReferences()](../../da/dd0/classSurfaceGui_1_1ViewProviderSections.html#ab3aac75f431bc26a632a1fe69f407903),
[MeshGui::ViewProviderMesh::highlightSegments()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#aa17a124626e50184e9d881c8fc6a1d40),
[MeshGui::ViewProviderMesh::highlightSelection()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a93b0740e9914a3c681a260e277e71a29),
[Gui::ViewProviderAnnotation::onChanged()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#a789aabe3e009284175581640dec663c3),
[Gui::ViewProviderAnnotationLabel::onChanged()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a53d7de6d67521a3dadb7ae43c96869bc),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[Gui::ViewProviderMeasureDistance::onChanged()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a55ba8a09c4ee671752b6e88c3561d9e1),
[FemGui::ViewProviderFemConstraint::onChanged()](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a3d33c13c95f3a907325ad1c399dc5a14),
[FemGui::ViewProviderFemMesh::onChanged()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ab319d4e3659d8c99309bd397af321308),
[MeshGui::ViewProviderMesh::onChanged()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae9ec71d871b59be4a532fb2be2cb8d52),
[MeshGui::ViewProviderMeshNode::onChanged()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a6f37857950fa14e1e1978c56706d0797),
[PathGui::ViewProviderPath::onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[TechDrawGui::QGIViewDimension::prefNormalColor()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a5c66d03c084c654168e059c57e052a19),
[PartGui::FaceColors::Private::Private()](../../d4/d4b/classFaceColors_1_1Private.html#aa6e3aabbd50fa1add6f4c6373e0d09ba),
[FemGui::ViewProviderFemMesh::resetColorByElementId()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a87d18ae1cc7dee4be9ecca5e211e4066),
[FemGui::ViewProviderFemMesh::resetColorByNodeId()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a167688e05bf26ddc561293fa2f264413),
[MeshGui::ViewProviderMesh::resetFacetTransparency()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#aded6f71523786276c5d9754acdbde999),
[TechDrawGui::TaskHatch::saveHatchState()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#a51dcb76a4ea06574a94e4e4eaf492e2b),
[MeshGui::ViewProviderMesh::setFacetTransparency()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#afc1af77d4f47d5a553c59f187877985f),
[TechDrawGui::TaskLeaderLine::setUiEdit()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0eed6886711ee111f1ee0a8e314d6e21),
[TechDrawGui::TaskRichAnno::setUiEdit()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a3659e9cb13bc53ae36a3d7d16479d017),
[TechDrawGui::TaskBalloon::TaskBalloon()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#a21f34d1bf15390ec9c984c7c75ab9996),
[TechDrawGui::TaskDimension::TaskDimension()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a01dec85a4db02858073f304508300ff3),
[MeshGui::ViewProviderMesh::tryColorPerVertexOrFace()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a35e34f80556c9ce8764399827cf9f5c3),
[MeshGui::ViewProviderMesh::unhighlightSelection()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a977181475bed61198479e2ff57f48745),
[PartGui::ViewProviderBoolean::updateData()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#ae38d6575df4dd650428a3d5873874d94),
[PartGui::ViewProviderChamfer::updateData()](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a33e0d402eb35a8d3bf589039003c4f0d),
and
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed).

## ◆ isSame()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyColor::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

## ◆ Paste()

| void PropertyColor::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
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

| void PropertyColor::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d9/d0b/classApp_1_1PropertyColor.html#a0b4dc7c8284cd7511308f8bb55dc56d0
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
[Base::XMLReader::getAttributeAsUnsigned()](../../dc/d95/classBase_1_1XMLReader.html#ac384789d0b975c7caee3762a236d951c),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
and
[setValue()](../../d9/d0b/classApp_1_1PropertyColor.html#a4aab2001271a7767ba2e47c681286b27).

## ◆ Save()

| void PropertyColor::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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

## ◆ setPyObject()

| void PropertyColor::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

References
[App::Color::a](../../d3/d3a/classApp_1_1Color.html#a6fee1c51422d3526256e50cfacfea28f),
[App::Color::b](../../d3/d3a/classApp_1_1Color.html#a80db35212156aad08612f92a82d60340),
[App::Color::g](../../d3/d3a/classApp_1_1Color.html#a95e979ab4c74614e16a24752023b3910),
[App::Color::r](../../d3/d3a/classApp_1_1Color.html#ac6aecf7a9aabad5c63b67ef031ec6df4),
[App::Color::setPackedValue()](../../d3/d3a/classApp_1_1Color.html#a967e60ab823022f2867963ea17f5ac1a),
and
[setValue()](../../d9/d0b/classApp_1_1PropertyColor.html#a4aab2001271a7767ba2e47c681286b27).

Referenced by
[App::PropertyColorList::getPyValue()](../../d0/dc7/classApp_1_1PropertyColorList.html#a1185ac555445591be3ab82499256987f).

## ◆ setValue() [1/3]

void PropertyColor::setValue  | ( | const [Color](../../d3/d3a/classApp_1_1Color.html) & | _col_| ) |   
---|---|---|---|---|---  
  
Sets the property.

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

Referenced by
[TechDrawGui::TaskHatch::createHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ac9d417f22f5d5ed524f63d10cd4e63ef),
[TechDrawGui::ViewProviderViewSection::getParameters()](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a8df1d57ca5c99b2d2a16f980618fd6a0),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartDesignGui::ViewProviderSubShapeBinder::onChanged()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[TechDrawGui::TaskGeomHatch::reject()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a18ae3da7ea9b2d55123cd563ed408217),
[Restore()](../../d9/d0b/classApp_1_1PropertyColor.html#a4e375cae7bed77bacf0a6dd30794212e),
[TechDrawGui::TaskHatch::restoreHatchState()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ad4a3916be744e9438b81e65cddfb14d3),
[setPyObject()](../../d9/d0b/classApp_1_1PropertyColor.html#a6e633e7e63cde42f29ea066464910433),
[TechDrawGui::TaskRichAnno::updateAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#adc9c72650392178995bfd8adf6344831),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[TechDrawGui::TaskHatch::updateHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#a885b8fcb16ca312a825e37d5f4ee11b4),
[TechDrawGui::TaskLeaderLine::updateLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0797a29d0a4ef849d5643c1ed982acb2),
[TechDrawGui::TaskGeomHatch::updateValues()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a12acdd2beb497c2bfd197b8d8234f389),
[PartDesignGui::ViewProviderDatum::ViewProviderDatum()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#adf0685fe5a17533d5150eee8e625d03a),
and
[FemGui::ViewProviderFemMesh::ViewProviderFemMesh()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a357c245ca2e9b478429c31fd3401e9d7).

## ◆ setValue() [2/3]

void PropertyColor::setValue  | ( | float  | _r_ ,   
---|---|---|---  
|  | float  | _g_ ,   
|  | float  | _b_ ,   
|  | float  | _a_ = `0.0f`  
| ) | |   
  
References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

## ◆ setValue() [3/3]

void PropertyColor::setValue  | ( | uint32_t  | _rgba_| ) |   
---|---|---|---|---|---  
  
References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyStandard.h
  * FreeCAD/src/App/PropertyStandard.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

