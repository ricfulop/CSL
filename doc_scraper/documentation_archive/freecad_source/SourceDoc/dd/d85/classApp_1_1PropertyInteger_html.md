---
url: https://freecad.github.io/SourceDoc/dd/d85/classApp_1_1PropertyInteger.html
scraped_at: 2025-09-08T14:55:55.910486
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html)

[List of all members](../../d1/d18/classApp_1_1PropertyInteger-members.html) | Public Member Functions

App::PropertyInteger Class Reference

Integer properties This is the father of all properties handling Integers.
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#details)

`#include <PropertyStandard.h>`

##  Public Member Functions  
  
---  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../dd/d85/classApp_1_1PropertyInteger.html#ab2dc80248124960dfddd1a23eff815ac) (void) const  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#ab2dc80248124960dfddd1a23eff815ac)  
  
virtual const char * | [getEditorName](../../dd/d85/classApp_1_1PropertyInteger.html#a69288b56dc31fa23037e6ed67210e2fb) (void) const  
| Get the class name of the associated property editor item.
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#a69288b56dc31fa23037e6ed67210e2fb)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../dd/d85/classApp_1_1PropertyInteger.html#af3dc5d89e0377b785478fbfb2f0f1064) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#af3dc5d89e0377b785478fbfb2f0f1064)  
  
virtual const boost::any | [getPathValue](../../dd/d85/classApp_1_1PropertyInteger.html#a78d1a2705a515581e6b74c9fae27094b) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &) const  
| Get value of property.
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#a78d1a2705a515581e6b74c9fae27094b)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../dd/d85/classApp_1_1PropertyInteger.html#a3d8ee4bcbcec07a42be8a5af16644ba9) (void)  
| This method returns the Python wrapper for a C++ object.
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#a3d8ee4bcbcec07a42be8a5af16644ba9)  
  
long | [getValue](../../dd/d85/classApp_1_1PropertyInteger.html#a4af3c36604f96057c6d64ccc74126042) (void) const  
| This method returns a string representation of the property.
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#a4af3c36604f96057c6d64ccc74126042)  
  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../dd/d85/classApp_1_1PropertyInteger.html#a70d2499769026e10fba6bc7a711aebb2) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const  
| Compare if this property has the same content as the given one.
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#a70d2499769026e10fba6bc7a711aebb2)  
  
virtual void | [Paste](../../dd/d85/classApp_1_1PropertyInteger.html#a09abc5b0039b42f2b7c71fa707abcba9) (const [Property](../../d0/da9/classApp_1_1Property.html) &from)  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#a09abc5b0039b42f2b7c71fa707abcba9)  
  
|
[PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#a64d3cfd19669b9573d56ee9ce233ac47)
()  
virtual void | [Restore](../../dd/d85/classApp_1_1PropertyInteger.html#a172043a2979b6d97bc1f79cf82fdfb02) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#a172043a2979b6d97bc1f79cf82fdfb02)  
  
virtual void | [Save](../../dd/d85/classApp_1_1PropertyInteger.html#a0c826cdd034a3b4bda67fb25b37cad70) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#a0c826cdd034a3b4bda67fb25b37cad70)  
  
virtual void | [setPathValue](../../dd/d85/classApp_1_1PropertyInteger.html#a86cf2a8be4f311966bb89cdec37a0991) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, const boost::any &value)  
| Set value of property.
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#a86cf2a8be4f311966bb89cdec37a0991)  
  
virtual void | [setPyObject](../../dd/d85/classApp_1_1PropertyInteger.html#a01766b286f7ee23f14008042a2465044) ([PyObject](../../df/d1b/classPyObject.html) *)  
void | [setValue](../../dd/d85/classApp_1_1PropertyInteger.html#ac542ac41f9bad4ff220e906d7342d8ee) (long)  
| Sets the property.
[More...](../../dd/d85/classApp_1_1PropertyInteger.html#ac542ac41f9bad4ff220e906d7342d8ee)  
  
virtual | [~PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#ab265fd8a6f9811a3747d950efe348002) ()  
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

Integer properties This is the father of all properties handling Integers.

## Constructor & Destructor Documentation

## ◆ PropertyInteger()

PropertyInteger::PropertyInteger  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[Copy()](../../dd/d85/classApp_1_1PropertyInteger.html#ab2dc80248124960dfddd1a23eff815ac).

## ◆ ~PropertyInteger()

| PropertyInteger::~PropertyInteger  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyInteger::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

References
[PropertyInteger()](../../dd/d85/classApp_1_1PropertyInteger.html#a64d3cfd19669b9573d56ee9ce233ac47).

## ◆ getEditorName()

| virtual const char * App::PropertyInteger::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

Reimplemented in
[App::PropertyIntegerConstraint](../../d2/dc8/classApp_1_1PropertyIntegerConstraint.html#a91f4dac53b547b4964f7178500f70565).

## ◆ getMemSize()

| virtual unsigned [int](../../d1/da0/classint.html) App::PropertyInteger::getMemSize  | ( | void  | | ) |  const  
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

| virtual const boost::any App::PropertyInteger::getPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Get value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyInteger::getPyObject  | ( | void  | | ) |   
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

long PropertyInteger::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
This method returns a string representation of the property.

Referenced by
[TechDraw::DrawViewPart::buildGeometryObject()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a859efd3dcccfd849656ff8b436ce6d58),
[PartGui::ViewProvider2DObjectGrid::createGrid()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a6872b82ce1aa46b6532e864681e262ae),
[PartGui::DlgPrimitives::DlgPrimitives()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a27827c66a9f047547fe0b7169251b97d),
[TechDrawGui::QGIWeldSymbol::drawTile()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a95de553829cc9844a9e95b1bdbd36e76),
[App::FunctionExpression::evalAggregate()](../../d6/da3/classApp_1_1FunctionExpression.html#ad9267dc1decdafaaa129f1bd51de07e4),
[Mesh::FillHoles::execute()](../../d2/ddd/classMesh_1_1FillHoles.html#a21a0e0e99c2dcd82f9918fe67def820b),
[Mesh::RemoveComponents::execute()](../../da/d7a/classMesh_1_1RemoveComponents.html#a552facf8870d9ef3b36e1dee379fac07),
[Mesh::Sphere::execute()](../../d1/d57/classMesh_1_1Sphere.html#ae830b723d9c2977e6080c9e87f3ec139),
[Mesh::Ellipsoid::execute()](../../d2/dd6/classMesh_1_1Ellipsoid.html#aa7094fc5c9ce3b03b37b1875e8962b68),
[Mesh::Cylinder::execute()](../../df/def/classMesh_1_1Cylinder.html#a7f0a6253a8936e26fdd2794992f9cbb4),
[Mesh::Cone::execute()](../../d4/dbc/classMesh_1_1Cone.html#a23701269832147c5746476d7e6b3b8af),
[Mesh::Torus::execute()](../../de/da3/classMesh_1_1Torus.html#a9ca70ccb5548f0852b54fe55f58f27a9),
[Points::Structured::execute()](../../d0/d43/classPoints_1_1Structured.html#a777464aea8c27ad6f8c525fb1f8ce15c),
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12),
[Fem::FemMeshShapeNetgenObject::execute()](../../d9/df4/classFem_1_1FemMeshShapeNetgenObject.html#ad38e08d369e0a9c44588e98bc5ffb3ed),
[Part::Loft::execute()](../../d3/d52/classPart_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[PartDesign::Prism::execute()](../../d9/daf/classPartDesign_1_1Prism.html#afbe0d9e86e58c4781f3f58aed9371937),
[Raytracing::LuxFeature::execute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a235b146fb9255cb705a6b86fb6967c3d),
[Raytracing::RayFeature::execute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[Surface::Filling::execute()](../../d8/df7/classSurface_1_1Filling.html#ab31cd9c2fd6bd4e15a80b7065c071eae),
[TechDraw::DrawViewDimExtent::execute()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#ac856c6f8b2f5504087090cc122d82891),
[Surface::Extend::execute()](../../d1/d22/classSurface_1_1Extend.html#a50a4d6f3fb960ba8acaa558639be59f0),
[PartGui::ViewProviderPartExt::getElementColors()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a15bdce85211acfec231620d1fea14805),
[TechDraw::DrawPage::getNextBalloonIndex()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a4b0e13f2dfa8d0547dc48bca3ab9cd0b),
[FemGui::TaskFemConstraint::getScale()](../../df/d80/classFemGui_1_1TaskFemConstraint.html#ab2fe87e42a6de75ba2d17ef6f60d33b0),
[Path::FeatureAreaView::getShapes()](../../d3/db4/classPath_1_1FeatureAreaView.html#a8bdeb47d6e84b6cfb93ce2eb43e7bbe9),
[TechDrawGui::QGIWeldSymbol::getTileFeats()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#ad1cf6ecee1beb9d4de4271fbee2031b6),
[TechDrawGui::TaskWeldingSymbol::getTileFeats()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#a170ad235c08c6ea3b7b1efb808d905cc),
[PartDesign::Scaled::getTransformations()](../../db/dce/classPartDesign_1_1Scaled.html#a114f3de4184f1d8b572ed057609c03d6),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[PartDesign::LinearPattern::handleChangedPropertyType()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a9a99c3eb9dc74e11d68f4794666e6270),
[PartDesign::PolarPattern::handleChangedPropertyType()](../../da/d5b/classPartDesign_1_1PolarPattern.html#af05898fa5e67a75fbb102a48e07be8ef),
[TechDraw::DrawTile::handleChangedPropertyType()](../../da/d56/classTechDraw_1_1DrawTile.html#a449be4339583f4d9d8e4cedea6a7dce4),
[TechDraw::DrawViewAnnotation::handleChangedPropertyType()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#adb0aa91e33022736bcb8d124cd9b295b),
[TechDrawGui::ViewProviderLeader::handleChangedPropertyType()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9f55c50ca1618be5224195b46784c99b),
[TechDrawGui::ViewProviderRichAnno::handleChangedPropertyType()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a2b7fcb5bb4cd203d5d467e29142523a3),
[PartDesignGui::ViewProviderDatumCoordinateSystem::onChanged()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a48324f18ce89cf9a307a32d54e3cfcc3),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[Gui::ViewProviderMeasureDistance::onChanged()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a55ba8a09c4ee671752b6e88c3561d9e1),
[Fem::ConstraintPressure::onChanged()](../../dd/d5e/classFem_1_1ConstraintPressure.html#a05ca046143c094c241c12702f7b820f7),
[Fem::ConstraintSpring::onChanged()](../../dc/d42/classFem_1_1ConstraintSpring.html#ae67112c14de2dc75f749842b6591fcf8),
[Fem::FemPostDataAlongLineFilter::onChanged()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ae418afcb8e18abba84d16c2a645a434e),
[FemGui::ViewProviderFemConstraint::onChanged()](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a3d33c13c95f3a907325ad1c399dc5a14),
[FemGui::ViewProviderFemMesh::onChanged()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ab319d4e3659d8c99309bd397af321308),
[MeshGui::ViewProviderMesh::onChanged()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae9ec71d871b59be4a532fb2be2cb8d52),
[PartDesignGui::ViewProviderDatumPoint::onChanged()](../../dc/d9d/classPartDesignGui_1_1ViewProviderDatumPoint.html#ada6d519997cb6ca57d88957962fc1377),
[PathGui::ViewProviderPath::onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[Sandbox::SandboxObject::onChanged()](../../da/dd9/classSandbox_1_1SandboxObject.html#ae3e3d04a08a28cb8060a72df914f3685),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartGui::ViewProviderPartExt::setHighlightedFaces()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ae3121cead5ae89980439ae2b9dfe4b3a),
[setPathValue()](../../dd/d85/classApp_1_1PropertyInteger.html#a86cf2a8be4f311966bb89cdec37a0991),
[PartDesignGui::TaskBoxPrimitives::TaskBoxPrimitives()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aee4936dd78a78c4d0f6fcc168d1a9c13),
[FemGui::TaskTetParameter::TaskTetParameter()](../../d9/d36/classFemGui_1_1TaskTetParameter.html#a29dc9ca508fcde30e91d9b0e306b34ce),
[FemGui::ViewProviderFemConstraintContact::updateData()](../../d9/d3d/classFemGui_1_1ViewProviderFemConstraintContact.html#a3ecf76e65206672a9355c60a533550c8),
[FemGui::ViewProviderFemConstraintDisplacement::updateData()](../../d7/d3f/classFemGui_1_1ViewProviderFemConstraintDisplacement.html#afb4b851d45e12b8639d1c4bedcaba4db),
[FemGui::ViewProviderFemConstraintFixed::updateData()](../../d4/d9c/classFemGui_1_1ViewProviderFemConstraintFixed.html#ab0717083d8637965bcafa54bfd839893),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintForce::updateData()](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#ad691cf23756106d6b0ea043ddebd1b94),
[FemGui::ViewProviderFemConstraintHeatflux::updateData()](../../d0/dea/classFemGui_1_1ViewProviderFemConstraintHeatflux.html#a3f1a55d2e70a5dca6b97d52c3e103aa0),
[FemGui::ViewProviderFemConstraintPlaneRotation::updateData()](../../d7/d0a/classFemGui_1_1ViewProviderFemConstraintPlaneRotation.html#a2b385e8a4903df418ef331257ad13a64),
[FemGui::ViewProviderFemConstraintPressure::updateData()](../../d4/d18/classFemGui_1_1ViewProviderFemConstraintPressure.html#a0280a478dea5288d50ba390ed1a50ca7),
[FemGui::ViewProviderFemConstraintSpring::updateData()](../../d5/d4f/classFemGui_1_1ViewProviderFemConstraintSpring.html#a44c1119dd7d0bef3d9ef9c3229057e53),
[FemGui::ViewProviderFemConstraintTemperature::updateData()](../../d1/df6/classFemGui_1_1ViewProviderFemConstraintTemperature.html#a4c6f2f24780c8171d293ec933ae942ac),
[FemGui::ViewProviderFemConstraintTransform::updateData()](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#a2adf8aba7f15f7b95399068ab39c47b8),
[FemGui::ViewProviderFemMesh::updateData()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a2b42be80762272d7f6be0b30e7d6a3f5),
[PartGui::ViewProviderChamfer::updateData()](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a33e0d402eb35a8d3bf589039003c4f0d),
[PathGui::ViewProviderPath::updateShowConstraints()](../../db/d31/classPathGui_1_1ViewProviderPath.html#af157d0410d852ca2fc864da7bc95be5e),
[PathGui::ViewProviderPath::updateVisual()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ab5ef44e05264d65aecc762660f342d58),
[Gui::PropertyEditor::PropertyIntegerItem::value()](../../de/d3b/classGui_1_1PropertyEditor_1_1PropertyIntegerItem.html#af8403087a42310e8e396c69ba89b31dc),
[Gui::PropertyEditor::PropertyIntegerConstraintItem::value()](../../d6/d39/classGui_1_1PropertyEditor_1_1PropertyIntegerConstraintItem.html#a2b469055bba9c4ee087df3e587dcf857),
and
[PartDesignGui::ViewProviderDatumCoordinateSystem::ViewProviderDatumCoordinateSystem()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a53832f895c08903546a696bd6e667100).

## ◆ isSame()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyInteger::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

## ◆ Paste()

| void PropertyInteger::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
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

| void PropertyInteger::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../dd/d85/classApp_1_1PropertyInteger.html#a0c826cdd034a3b4bda67fb25b37cad70
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
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
and
[setValue()](../../dd/d85/classApp_1_1PropertyInteger.html#ac542ac41f9bad4ff220e906d7342d8ee).

Referenced by
[PartDesign::LinearPattern::handleChangedPropertyType()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a9a99c3eb9dc74e11d68f4794666e6270),
[PartDesign::PolarPattern::handleChangedPropertyType()](../../da/d5b/classPartDesign_1_1PolarPattern.html#af05898fa5e67a75fbb102a48e07be8ef),
[TechDraw::DrawTile::handleChangedPropertyType()](../../da/d56/classTechDraw_1_1DrawTile.html#a449be4339583f4d9d8e4cedea6a7dce4),
[TechDraw::DrawViewAnnotation::handleChangedPropertyType()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#adb0aa91e33022736bcb8d124cd9b295b),
[TechDrawGui::ViewProviderLeader::handleChangedPropertyType()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9f55c50ca1618be5224195b46784c99b),
and
[TechDrawGui::ViewProviderRichAnno::handleChangedPropertyType()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a2b7fcb5bb4cd203d5d467e29142523a3).

## ◆ Save()

| void PropertyInteger::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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

| void PropertyInteger::setPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | const boost::any & | _value_  
| ) | |   
virtual  
  
Set value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22).

References
[getValue()](../../dd/d85/classApp_1_1PropertyInteger.html#a4af3c36604f96057c6d64ccc74126042),
[setValue()](../../dd/d85/classApp_1_1PropertyInteger.html#ac542ac41f9bad4ff220e906d7342d8ee),
and
[App::Property::verifyPath()](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7).

## ◆ setPyObject()

| void PropertyInteger::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

Reimplemented in
[App::PropertyIntegerConstraint](../../d2/dc8/classApp_1_1PropertyIntegerConstraint.html#a59de0c197b75f6ad9e00c93bb02611b3).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

## ◆ setValue()

void PropertyInteger::setValue  | ( | long  | _lValue_| ) |   
---|---|---|---|---|---  
  
Sets the property.

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

Referenced by
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12),
[TechDraw::DrawPage::getNextBalloonIndex()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a4b0e13f2dfa8d0547dc48bca3ab9cd0b),
[PartDesign::LinearPattern::handleChangedPropertyType()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a9a99c3eb9dc74e11d68f4794666e6270),
[PartDesign::PolarPattern::handleChangedPropertyType()](../../da/d5b/classPartDesign_1_1PolarPattern.html#af05898fa5e67a75fbb102a48e07be8ef),
[TechDraw::DrawTile::handleChangedPropertyType()](../../da/d56/classTechDraw_1_1DrawTile.html#a449be4339583f4d9d8e4cedea6a7dce4),
[TechDraw::DrawViewAnnotation::handleChangedPropertyType()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#adb0aa91e33022736bcb8d124cd9b295b),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[Fem::ConstraintContact::onChanged()](../../db/d7c/classFem_1_1ConstraintContact.html#a2470d9364e84ea3c15f5873073f26539),
[Fem::ConstraintDisplacement::onChanged()](../../d5/d1c/classFem_1_1ConstraintDisplacement.html#a8525892f2c7183b75c1d8f2052f82401),
[Fem::ConstraintFixed::onChanged()](../../d1/d43/classFem_1_1ConstraintFixed.html#a2b9b87e9151f1571ab9cff619ec5547c),
[Fem::ConstraintFluidBoundary::onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Fem::ConstraintForce::onChanged()](../../d6/d63/classFem_1_1ConstraintForce.html#aa19098735f62c480439948314f6532b3),
[Fem::ConstraintHeatflux::onChanged()](../../de/dce/classFem_1_1ConstraintHeatflux.html#a0caeab069cf3e2fc8246aa163735d1e9),
[Fem::ConstraintInitialTemperature::onChanged()](../../da/d91/classFem_1_1ConstraintInitialTemperature.html#aa21e4c9c6cc31312e5147bbe1f8fcf05),
[Fem::ConstraintPlaneRotation::onChanged()](../../d7/d08/classFem_1_1ConstraintPlaneRotation.html#a668aafd16c5cf0565dde1072dd55a34a),
[Fem::ConstraintPressure::onChanged()](../../dd/d5e/classFem_1_1ConstraintPressure.html#a05ca046143c094c241c12702f7b820f7),
[Fem::ConstraintSpring::onChanged()](../../dc/d42/classFem_1_1ConstraintSpring.html#ae67112c14de2dc75f749842b6591fcf8),
[Fem::ConstraintTemperature::onChanged()](../../d7/dff/classFem_1_1ConstraintTemperature.html#a74f2f9e94a2d9011490c09caab3c0da9),
[Fem::ConstraintTransform::onChanged()](../../d8/d3c/classFem_1_1ConstraintTransform.html#a38b893dee34272ad6bf0c6126aad561f),
[PartDesignGui::ViewProviderDatumPoint::onChanged()](../../dc/d9d/classPartDesignGui_1_1ViewProviderDatumPoint.html#ada6d519997cb6ca57d88957962fc1377),
[PartDesignGui::ViewProviderSubShapeBinder::onChanged()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[PartDesignGui::TaskBoxPrimitives::onPrismPolygonChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a3a30191951932ad49bef38d08c4292fa),
[TechDraw::DrawWeldSymbol::onSettingDocument()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#aebf48eba403fab933cfaba6f325c6bc2),
[Sandbox::SandboxObject::resetValue()](../../da/dd9/classSandbox_1_1SandboxObject.html#a9cf9176b0f4b455d64dea16575b4846c),
[Restore()](../../dd/d85/classApp_1_1PropertyInteger.html#a172043a2979b6d97bc1f79cf82fdfb02),
[Sandbox::DocumentTestThread::run()](../../d5/d8a/classSandbox_1_1DocumentTestThread.html#a27751a48ad75c90b8b678641eb975cde),
[Spreadsheet::Sheet::setIntegerProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a396a15ce1feb26825369fc32d38c028e),
[Sandbox::SandboxObject::setIntValue()](../../da/dd9/classSandbox_1_1SandboxObject.html#a4a9142b5ebbbf3927c628df3423dbda8),
[setPathValue()](../../dd/d85/classApp_1_1PropertyInteger.html#a86cf2a8be4f311966bb89cdec37a0991),
[PathGui::ViewProviderPath::updateShowConstraints()](../../db/d31/classPathGui_1_1ViewProviderPath.html#af157d0410d852ca2fc864da7bc95be5e),
[PathGui::ViewProviderPath::updateVisual()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ab5ef44e05264d65aecc762660f342d58),
[PartDesignGui::ViewProviderDatum::ViewProviderDatum()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#adf0685fe5a17533d5150eee8e625d03a),
and
[PartGui::DlgProjectionOnSurface::~DlgProjectionOnSurface()](../../d2/da4/classPartGui_1_1DlgProjectionOnSurface.html#a7d2e3355dfa8759dd537d765c4bc8e96).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyStandard.h
  * FreeCAD/src/App/PropertyStandard.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

