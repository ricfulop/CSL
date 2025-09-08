---
url: https://freecad.github.io/SourceDoc/d3/dbe/classApp_1_1PropertyFloat.html
scraped_at: 2025-09-08T14:55:47.841577
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html)

[List of all members](../../d2/d9f/classApp_1_1PropertyFloat-members.html) | Public Member Functions

App::PropertyFloat Class Reference

Float properties This is the father of all properties handling floats.
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#details)

`#include <PropertyStandard.h>`

##  Public Member Functions  
  
---  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d3/dbe/classApp_1_1PropertyFloat.html#ac7565beb8b32fc7383a55e4052ecdfd7) (void) const  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#ac7565beb8b32fc7383a55e4052ecdfd7)  
  
virtual const char * | [getEditorName](../../d3/dbe/classApp_1_1PropertyFloat.html#a3a0dd8a67f208ac5a258ee5755b0cd33) (void) const  
| Get the class name of the associated property editor item.
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#a3a0dd8a67f208ac5a258ee5755b0cd33)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d3/dbe/classApp_1_1PropertyFloat.html#a8c29971099b9581c77eef99b42218ad7) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#a8c29971099b9581c77eef99b42218ad7)  
  
const boost::any | [getPathValue](../../d3/dbe/classApp_1_1PropertyFloat.html#a429075152c75dbbd46e4bf5d7aeaac7d) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path) const  
| Get value of property.
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#a429075152c75dbbd46e4bf5d7aeaac7d)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d3/dbe/classApp_1_1PropertyFloat.html#a5b0bcb3b6460df02b89fb8469b1738c9) (void)  
| This method returns the Python wrapper for a C++ object.
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#a5b0bcb3b6460df02b89fb8469b1738c9)  
  
double | [getValue](../../d3/dbe/classApp_1_1PropertyFloat.html#ae6c1d258b368a93c6fe4e6aa3f2a0842) (void) const  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d3/dbe/classApp_1_1PropertyFloat.html#a386b26cdbb4e26dfd8e6340d3bb9ca5e) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const  
| Compare if this property has the same content as the given one.
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#a386b26cdbb4e26dfd8e6340d3bb9ca5e)  
  
virtual void | [Paste](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf1f7c4fc4c8bde2ca9b8482180e45ff) (const [Property](../../d0/da9/classApp_1_1Property.html) &from)  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf1f7c4fc4c8bde2ca9b8482180e45ff)  
  
|
[PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a97d2fbfb3e87278f2f1e64ec88bf1c83)
(void)  
| Value Constructor Construct with explicit Values.
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#a97d2fbfb3e87278f2f1e64ec88bf1c83)  
  
virtual void | [Restore](../../d3/dbe/classApp_1_1PropertyFloat.html#aa6d8ab192c6855fe5506b10e458460cf) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#aa6d8ab192c6855fe5506b10e458460cf)  
  
virtual void | [Save](../../d3/dbe/classApp_1_1PropertyFloat.html#a4d58561153acf13b6eda8b115deb33a7) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#a4d58561153acf13b6eda8b115deb33a7)  
  
void | [setPathValue](../../d3/dbe/classApp_1_1PropertyFloat.html#ac5c0dfec5810e2860c64bb7186b2462a) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, const boost::any &value)  
| Set value of property.
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#ac5c0dfec5810e2860c64bb7186b2462a)  
  
virtual void | [setPyObject](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf2edab1753863426d8b78dd15dab006) ([PyObject](../../df/d1b/classPyObject.html) *)  
void | [setValue](../../d3/dbe/classApp_1_1PropertyFloat.html#aeb4937e13aff58a04f81fdadf544f7d9) (double lValue)  
virtual | [~PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#aff8d7e19e628570f21830ba928cc1025) ()  
| A destructor.
[More...](../../d3/dbe/classApp_1_1PropertyFloat.html#aff8d7e19e628570f21830ba928cc1025)  
  
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

Float properties This is the father of all properties handling floats.

Use this type only in rare cases. Mostly you want to use the more specialized
types like e.g. [PropertyLength](../../d0/d44/classApp_1_1PropertyLength.html
"Length property This is a property for representing lengths."). These
properties also fulfill the needs of the unit system. See PropertyUnits.h for
all properties with units.

## Constructor & Destructor Documentation

## ◆ PropertyFloat()

PropertyFloat::PropertyFloat  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Value Constructor Construct with explicit Values.

Referenced by
[Copy()](../../d3/dbe/classApp_1_1PropertyFloat.html#ac7565beb8b32fc7383a55e4052ecdfd7).

## ◆ ~PropertyFloat()

| PropertyFloat::~PropertyFloat  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyFloat::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

Reimplemented in
[Spreadsheet::PropertySpreadsheetQuantity](../../d2/dd4/classSpreadsheet_1_1PropertySpreadsheetQuantity.html#a1c4e3c7cafaf2ae7f08ec03a8bfb63f9).

References
[PropertyFloat()](../../d3/dbe/classApp_1_1PropertyFloat.html#a97d2fbfb3e87278f2f1e64ec88bf1c83).

## ◆ getEditorName()

| virtual const char * App::PropertyFloat::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

Reimplemented in
[App::PropertyFloatConstraint](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a3f5130569b81c7c30f8dbd32bd687061),
[App::PropertyPrecision](../../d5/de5/classApp_1_1PropertyPrecision.html#ac2c734c673b528f52ab537b0cb3629d2),
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#aca6dbdcb93d7a5800c0367974810fdf5),
[App::PropertyQuantityConstraint](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#aa887d76bf141becf6238408ee1b1e64a),
and
[App::PropertyAngle](../../d1/d5d/classApp_1_1PropertyAngle.html#a696bab3cd50bef40c0f33aa62b6de163).

## ◆ getMemSize()

| virtual unsigned [int](../../d1/da0/classint.html) App::PropertyFloat::getMemSize  | ( | void  | | ) |  const  
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

| const boost::any PropertyFloat::getPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Get value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea).

Reimplemented in
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#ae735a34c955df358ef20a0c70b7b5c97).

References
[App::Property::verifyPath()](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyFloat::getPyObject  | ( | void  | | ) |   
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
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#af17e8d34d40a187543b30789adef4cc7).

## ◆ getValue()

double PropertyFloat::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[PartDesignGui::TaskHelixParameters::apply()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#ac943cca36559194f55b17ffc2b2a91ac),
[Gui::ViewProviderOriginFeature::attach()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#aac32ddea00ce5374fa432bad0540355a),
[PartDesignGui::ViewProviderDatumCoordinateSystem::attach()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a6ce3d34ce823917c149e9e6348346198),
[TechDrawGui::TaskRichAnno::calcTextStartPos()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ae1abe86bd3bc257ecd36cc0212763a37),
[TechDraw::DrawView::checkScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#ad2da2acbc02345e15a55d357ef545914),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[TechDrawGui::QGIViewBalloon::drawBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6d26eb06a692339e02c1b57545903f29),
[TechDrawGui::QGIViewPart::drawHighlight()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#aac8834c3546b27902b1c3543d4a8e32e),
[TechDrawGui::QGIViewPart::drawMatting()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a8ee1ae8bd3c4894661e9911784534607),
[TechDrawGui::QGIViewSection::drawSectionFace()](../../d7/d73/classTechDrawGui_1_1QGIViewSection.html#a23b734cc85fce28a0a42c4d061686cb4),
[TechDrawGui::QGIViewPart::drawViewPart()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#add7c40ff3fc3fcc84308bb29225f8cc9),
[App::FunctionExpression::evalAggregate()](../../d6/da3/classApp_1_1FunctionExpression.html#ad9267dc1decdafaaa129f1bd51de07e4),
[Mesh::FixDegenerations::execute()](../../db/d8f/classMesh_1_1FixDegenerations.html#a3425c9ffba4deeb1c73c7fe910429687),
[Mesh::FixDeformations::execute()](../../d1/dbc/classMesh_1_1FixDeformations.html#a8c0ddd5b2e77c30a2466dc1fd08cdc7a),
[Mesh::FillHoles::execute()](../../d2/ddd/classMesh_1_1FillHoles.html#a21a0e0e99c2dcd82f9918fe67def820b),
[Drawing::FeatureClip::execute()](../../d5/d4a/classDrawing_1_1FeatureClip.html#afed75650f49849b96c65ef93795800e5),
[Drawing::FeatureViewAnnotation::execute()](../../d6/de7/classDrawing_1_1FeatureViewAnnotation.html#a74171a078f54a6d0ee13242e3b014751),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Drawing::FeatureViewSymbol::execute()](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#a3563b4ff57807e29d705c04a53b7cd0b),
[Fem::FemMeshShapeNetgenObject::execute()](../../d9/df4/classFem_1_1FemMeshShapeNetgenObject.html#ad38e08d369e0a9c44588e98bc5ffb3ed),
[Inspection::Feature::execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[PartDesign::Helix::execute()](../../d3/d78/classPartDesign_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[Robot::Edge2TracObject::execute()](../../d8/df5/classRobot_1_1Edge2TracObject.html#a05d96baf25af72c1c01f165a8dac7f63),
[Surface::Filling::execute()](../../d8/df7/classSurface_1_1Filling.html#ab31cd9c2fd6bd4e15a80b7065c071eae),
[Surface::Sewing::execute()](../../d2/d52/classSurface_1_1Sewing.html#a956109125cae787085423aeb93d8e1f3),
[Part::Offset::execute()](../../d0/dda/classPart_1_1Offset.html#a342f29a6b5381db240304b9384b313dd),
[Part::Offset2D::execute()](../../d7/dcf/classPart_1_1Offset2D.html#a3eb29bb0e6404263cb3470d7ec24ea4a),
[Part::Revolution::execute()](../../d3/d17/classPart_1_1Revolution.html#a0406e2da5876bbf2351991c6b48b7185),
[Surface::Extend::execute()](../../d1/d22/classSurface_1_1Extend.html#a50a4d6f3fb960ba8acaa558639be59f0),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[Gui::ViewProviderLink::finishRestoring()](../../d6/d59/classGui_1_1ViewProviderLink.html#ab68540420e3d18c69df6944e857fa198),
[PartDesign::Helix::generateHelixPath()](../../d3/d78/classPartDesign_1_1Helix.html#a04dd9590e1c0afe9dd3f1066ab9f0395),
[TechDraw::DrawViewSection::getDrawableLines()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a099648b5b9b3b5650f425b3284d5d2a8),
[TechDraw::DrawGeomHatch::getFaceOverlay()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a64b931ea5f365c039b0e956a46877f9b),
[TechDraw::DrawViewDetail::getFudgeRadius()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#a6075485677e85fe40992d9d7e14337c6),
[TechDrawGui::TaskGeomHatch::getParameters()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#aeb7fd1b271e9d19d70da0b903137a3e0),
[TechDraw::DrawViewImage::getRect()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#aecd5ac3de2b2f54e49a980bab85e8811),
[TechDraw::DrawView::getScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#afc22d0aa3cc132a6c14323a50082ab1e),
[TechDraw::DrawProjGroupItem::getScale()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a8f2e3744991fded06c52c4e817aed862),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[PartDesign::Scaled::getTransformations()](../../db/dce/classPartDesign_1_1Scaled.html#a114f3de4184f1d8b572ed057609c03d6),
[TechDraw::DrawGeomHatch::getTrimmedLines()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9282d24bc775c7b8870bcbda7dce8cff),
[App::PropertyQuantity::getValue()](../../d4/d65/classApp_1_1PropertyQuantity.html#a49df4b1070e01e10bef464cf672747c6),
[PartGui::ViewProvider2DObjectGrid::handleChangedPropertyType()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a4c2d97cecf5419da9ce703e47f8c1e6a),
[PartDesign::Helix::handleChangedPropertyType()](../../d3/d78/classPartDesign_1_1Helix.html#a9e6fc22b84b2f26eef4b4880af00b063),
[PartDesign::Transformed::handleChangedPropertyType()](../../dd/de1/classPartDesign_1_1Transformed.html#a9e4288037e29095bf566a11f3f13fe12),
[TechDraw::DrawViewAnnotation::handleChangedPropertyType()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#adb0aa91e33022736bcb8d124cd9b295b),
[TechDrawGui::ViewProviderBalloon::handleChangedPropertyType()](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a4a6246398d610494e2171cbbb1b8eb44),
[TechDrawGui::ViewProviderDimension::handleChangedPropertyType()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a3ca6d7598ea8430e71e0f852c349b339),
[TechDrawGui::ViewProviderLeader::handleChangedPropertyType()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9f55c50ca1618be5224195b46784c99b),
[TechDrawGui::ViewProviderRichAnno::handleChangedPropertyType()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a2b7fcb5bb4cd203d5d467e29142523a3),
[TechDrawGui::ViewProviderViewPart::handleChangedPropertyType()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a1dbd73f06f25bca49644056da29aa920),
[Part::Primitive::handleChangedPropertyType()](../../d2/d31/classPart_1_1Primitive.html#a1e49f13eafbcb2ce0de44916a8407cf7),
[TechDraw::DrawPage::handleChangedPropertyType()](../../d9/d5a/classTechDraw_1_1DrawPage.html#adde1799122996153278b2c68d4fa9b80),
[TechDraw::DrawProjGroup::handleChangedPropertyType()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a9a45f879e7b7c0cc6a6787be1c021f46),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[TechDraw::DrawViewBalloon::handleChangedPropertyType()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a71fe79a13079b298255b09846c9b6582),
[PartGui::ViewProviderPartExt::loadParameter()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ac9b18640b083f65180c44c787ed4b240),
[PartGui::OffsetWidget::OffsetWidget()](../../d9/d6d/classPartGui_1_1OffsetWidget.html#ae7bb4b5d03b3c78115b8e3943bb318d1),
[FemGui::ViewProviderFemPostPlaneFunction::onChanged()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#aff4da6a421671244ed9f106adbaee37a),
[PartDesignGui::ViewProviderDatumCoordinateSystem::onChanged()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a48324f18ce89cf9a307a32d54e3cfcc3),
[Gui::ViewProviderAnnotation::onChanged()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#a789aabe3e009284175581640dec663c3),
[Gui::ViewProviderOriginFeature::onChanged()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a86520630c898707677753ccc3877eced),
[Fem::ConstraintBearing::onChanged()](../../df/d0a/classFem_1_1ConstraintBearing.html#ae81d9fda05994bd43bf81faf3acae5d6),
[Fem::ConstraintPulley::onChanged()](../../d3/dec/classFem_1_1ConstraintPulley.html#a6c23af9b8ba29b03f25163da9b75a41f),
[Fem::FemPostScalarClipFilter::onChanged()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a6c5243b230b4dac2cde71f28d04dcd53),
[Fem::FemPostWarpVectorFilter::onChanged()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a64c913cbc86feb708504b94b931f1085),
[FemGui::ViewProviderFemMesh::onChanged()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ab319d4e3659d8c99309bd397af321308),
[FemGui::ViewProviderFemPostFunction::onChanged()](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#ae95be84201f7f51ce6162468c514e33e),
[InspectionGui::ViewProviderInspection::onChanged()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a75537f17b213bb2c7ea45b374ed65375),
[MeshGui::ViewProviderMesh::onChanged()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae9ec71d871b59be4a532fb2be2cb8d52),
[MeshGui::ViewProviderMeshDefects::onChanged()](../../da/d50/classMeshGui_1_1ViewProviderMeshDefects.html#a0d494009344982737533a865b26ce7d4),
[MeshGui::ViewProviderMeshNode::onChanged()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a6f37857950fa14e1e1978c56706d0797),
[PointsGui::ViewProviderPoints::onChanged()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ad91786e290cd4be69ef99a41c85faa32),
[Robot::RobotObject::onChanged()](../../db/d51/classRobot_1_1RobotObject.html#abebfe59d5888146a96594cb7d31ffce8),
[Gui::ViewProviderLink::onChanged()](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[TechDraw::DrawPage::onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawProjGroup::onChanged()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[TechDrawGui::ViewProviderHatch::onChanged()](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#aada265457fade9ade61cbade5aee4f2b),
[TechDrawGui::TaskDetail::onScaleTypeEdit()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#aaf0c48b11d118f0fb2a3ac2fcf661409),
[Robot::RobotObject::Restore()](../../db/d51/classRobot_1_1RobotObject.html#a654870e568b07840a79bd2c8e99e50d1),
[PartDesign::Helix::safePitch()](../../d3/d78/classPartDesign_1_1Helix.html#a85474d1c32f51cf49c0be48c600993eb),
[TechDrawGui::TaskDetail::saveDetailState()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a78c2d2718806789466fe6ac7a05d72bc),
[TechDrawGui::TaskProjGroup::saveGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#af012f644413f9c531a249a2fcb76d888),
[TechDrawGui::TaskHatch::saveHatchState()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#a51dcb76a4ea06574a94e4e4eaf492e2b),
[TechDrawGui::TaskSectionView::scaleTypeChanged()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#aafc15acce6a04dd460d5c2f2877e7ca9),
[PartDesignGui::ViewProviderDatumCoordinateSystem::setExtents()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#aca9445d2a12b85efb9be68e484501cf9),
[setPathValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#ac5c0dfec5810e2860c64bb7186b2462a),
[RobotGui::TaskRobot6Axis::setRobot()](../../d8/d17/classRobotGui_1_1TaskRobot6Axis.html#a65d3953f8a1ba93524ac3e9cb3d73c0c),
[TechDrawGui::QGIRichAnno::setTextItem()](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#a27fd9afb78b8c22eeadd556d985030fe),
[TechDrawGui::TaskRichAnno::setUiEdit()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a3659e9cb13bc53ae36a3d7d16479d017),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[TechDrawGui::QGIViewBalloon::setViewPartFeature()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6f17a801836429d822e8998b0edfbff5),
[TechDrawGui::TaskBalloon::TaskBalloon()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#a21f34d1bf15390ec9c984c7c75ab9996),
[FemGui::TaskFemConstraintBearing::TaskFemConstraintBearing()](../../d5/d79/classFemGui_1_1TaskFemConstraintBearing.html#a5c48324835803c2f89e0c8a226dec9b0),
[FemGui::TaskFemConstraintContact::TaskFemConstraintContact()](../../d6/db7/classFemGui_1_1TaskFemConstraintContact.html#a45a74a3a2db13e3d87edba110a9fd7cd),
[FemGui::TaskFemConstraintDisplacement::TaskFemConstraintDisplacement()](../../d6/d75/classFemGui_1_1TaskFemConstraintDisplacement.html#ad9efd945714cedc7f6f182b3b811e089),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[FemGui::TaskFemConstraintForce::TaskFemConstraintForce()](../../d2/d46/classFemGui_1_1TaskFemConstraintForce.html#a3db3abe3cbf9a61635e1683630a55762),
[FemGui::TaskFemConstraintGear::TaskFemConstraintGear()](../../d9/d4d/classFemGui_1_1TaskFemConstraintGear.html#a9e613a0869b02375ab20ef330813dd1f),
[FemGui::TaskFemConstraintHeatflux::TaskFemConstraintHeatflux()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a8e9e2cb04cc453f24e9d3ea5794cacc1),
[FemGui::TaskFemConstraintInitialTemperature::TaskFemConstraintInitialTemperature()](../../dd/d2a/classFemGui_1_1TaskFemConstraintInitialTemperature.html#a7fdd937b1300d7fc2eefc92ab53ac673),
[FemGui::TaskFemConstraintPressure::TaskFemConstraintPressure()](../../dc/dd9/classFemGui_1_1TaskFemConstraintPressure.html#a00c65ac2686efb36884dcf8c6a10d76e),
[FemGui::TaskFemConstraintPulley::TaskFemConstraintPulley()](../../d3/d33/classFemGui_1_1TaskFemConstraintPulley.html#a0ae13b3d3671f9f5b94b36ca4f1bef14),
[FemGui::TaskFemConstraintSpring::TaskFemConstraintSpring()](../../d9/d3e/classFemGui_1_1TaskFemConstraintSpring.html#a0237d05805437799169e7d15e6c262fa),
[FemGui::TaskFemConstraintTemperature::TaskFemConstraintTemperature()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a33195abb4e64b5b8c79d39c7423d0a22),
[FemGui::TaskFemConstraintTransform::TaskFemConstraintTransform()](../../d9/d9b/classFemGui_1_1TaskFemConstraintTransform.html#aa2ff547501a5af38276cce0666c1920c),
[FemGui::TaskPostScalarClip::TaskPostScalarClip()](../../df/d2a/classFemGui_1_1TaskPostScalarClip.html#ab3c128515f1c8b3ab10aef3edd773832),
[FemGui::TaskTetParameter::TaskTetParameter()](../../d9/d36/classFemGui_1_1TaskTetParameter.html#a29dc9ca508fcde30e91d9b0e306b34ce),
[PartDesignGui::ViewProviderAddSub::updateAddSubShapeIndicator()](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#a27d23424ce72a0f362904d73928fbc6c),
[Gui::ViewProviderMeasureDistance::updateData()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a260762ea126ca4a70b60e5a825f2448d),
[FemGui::ViewProviderFemConstraintBearing::updateData()](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#a3b3cf2fa05760751890d9e1cf51f178f),
[FemGui::ViewProviderFemConstraintGear::updateData()](../../d1/d2f/classFemGui_1_1ViewProviderFemConstraintGear.html#a56f097a322b6fe5b2b4b7eead3374c49),
[FemGui::ViewProviderFemConstraintPulley::updateData()](../../d8/dfc/classFemGui_1_1ViewProviderFemConstraintPulley.html#a7ba40d63d4dff464026a808438d3630b),
[FemGui::ViewProviderFemConstraintTransform::updateData()](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#a2adf8aba7f15f7b95399068ab39c47b8),
[FemGui::ViewProviderFemPostPlaneFunction::updateData()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#a6ec898b1ee3b9ae2983c1f424b2a55f4),
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
[FemGui::ViewProviderFemPostFunctionProvider::updateSize()](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#ad783f019da5429b4ca0669a14d606d72),
[PartGui::ViewProviderPartExt::updateVisual()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a96cb6b96c8dfb082a135a31c4f554167),
[TechDraw::DrawView::validateScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#ab9bb446a2ce1a400ffe1aa00daf6cdd0),
[FemGui::ViewProviderFemMesh::ViewProviderFemMesh()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a357c245ca2e9b478429c31fd3401e9d7),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
and
[PointsGui::ViewProviderPoints::ViewProviderPoints()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ac5af34ec9fcf964cf09f3f7eaee50fca).

## ◆ isSame()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyFloat::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

Reimplemented in
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#a223868a557555d8f3ea7e1eb647af452).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

## ◆ Paste()

| void PropertyFloat::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
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

| void PropertyFloat::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d3/dbe/classApp_1_1PropertyFloat.html#a4d58561153acf13b6eda8b115deb33a7
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
[Base::XMLReader::getAttributeAsFloat()](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
and
[setValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#aeb4937e13aff58a04f81fdadf544f7d9).

Referenced by
[Part::Circle::handleChangedPropertyName()](../../de/de4/classPart_1_1Circle.html#aac14a5128cb8850c0cd7f37ffc71e22a),
[Part::Ellipse::handleChangedPropertyName()](../../d6/d22/classPart_1_1Ellipse.html#a7448b87a31bf68edc8d6a6909613615b),
[Surface::Extend::handleChangedPropertyName()](../../d1/d22/classSurface_1_1Extend.html#aa2e1ed26c2018e7234938836df41545c),
[TechDraw::DrawViewBalloon::handleChangedPropertyName()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a8f43bff2ef5b6712e7fd0546b639e6ef),
[TechDraw::DrawViewDimension::handleChangedPropertyType()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ae012f9df13a4f5578d96a5e50ccb1b2d),
[Mesh::Sphere::handleChangedPropertyType()](../../d1/d57/classMesh_1_1Sphere.html#af43262e6edb32fd6dcd686d877728c3a),
[Mesh::Ellipsoid::handleChangedPropertyType()](../../d2/dd6/classMesh_1_1Ellipsoid.html#ae21b7d81a6bc266b6505fa067ada71fa),
[Mesh::Cylinder::handleChangedPropertyType()](../../df/def/classMesh_1_1Cylinder.html#a698e2724dd6a682861aa49c3ca588abd),
[Mesh::Cone::handleChangedPropertyType()](../../d4/dbc/classMesh_1_1Cone.html#a88dde13a2f1e984c9d54e3f0836df079),
[Mesh::Torus::handleChangedPropertyType()](../../de/da3/classMesh_1_1Torus.html#aec1db0e864c1478a9a5e2fdf4f6c4614),
[Mesh::Cube::handleChangedPropertyType()](../../df/d68/classMesh_1_1Cube.html#a7a48689262a11f3e55ea4c4302f028dc),
[Part::Thickness::handleChangedPropertyType()](../../db/d73/classPart_1_1Thickness.html#a013b39370d11b7cb467ed7223d33d7a9),
[PartGui::ViewProvider2DObjectGrid::handleChangedPropertyType()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a4c2d97cecf5419da9ce703e47f8c1e6a),
[PartDesign::Fillet::handleChangedPropertyType()](../../d0/d50/classPartDesign_1_1Fillet.html#a4dec9f6780093c637468b21782cc0347),
[PartDesign::Helix::handleChangedPropertyType()](../../d3/d78/classPartDesign_1_1Helix.html#a9e6fc22b84b2f26eef4b4880af00b063),
[PartDesign::Transformed::handleChangedPropertyType()](../../dd/de1/classPartDesign_1_1Transformed.html#a9e4288037e29095bf566a11f3f13fe12),
[TechDraw::DrawViewAnnotation::handleChangedPropertyType()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#adb0aa91e33022736bcb8d124cd9b295b),
[TechDrawGui::ViewProviderBalloon::handleChangedPropertyType()](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a4a6246398d610494e2171cbbb1b8eb44),
[TechDrawGui::ViewProviderDimension::handleChangedPropertyType()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a3ca6d7598ea8430e71e0f852c349b339),
[TechDrawGui::ViewProviderLeader::handleChangedPropertyType()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9f55c50ca1618be5224195b46784c99b),
[TechDrawGui::ViewProviderRichAnno::handleChangedPropertyType()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a2b7fcb5bb4cd203d5d467e29142523a3),
[TechDrawGui::ViewProviderViewPart::handleChangedPropertyType()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a1dbd73f06f25bca49644056da29aa920),
[Part::Primitive::handleChangedPropertyType()](../../d2/d31/classPart_1_1Primitive.html#a1e49f13eafbcb2ce0de44916a8407cf7),
[PartDesign::Chamfer::handleChangedPropertyType()](../../da/d6f/classPartDesign_1_1Chamfer.html#a8efe172f26b587a447f0bb5b183ae67b),
[TechDraw::DrawPage::handleChangedPropertyType()](../../d9/d5a/classTechDraw_1_1DrawPage.html#adde1799122996153278b2c68d4fa9b80),
[TechDraw::DrawProjGroup::handleChangedPropertyType()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a9a45f879e7b7c0cc6a6787be1c021f46),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
and
[TechDraw::DrawViewBalloon::handleChangedPropertyType()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a71fe79a13079b298255b09846c9b6582).

## ◆ Save()

| void PropertyFloat::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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

| void PropertyFloat::setPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | const boost::any & | _value_  
| ) | |   
virtual  
  
Set value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22).

Reimplemented in
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#af017ce248b34f5378b3a714aa270c421).

References
[getValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#ae6c1d258b368a93c6fe4e6aa3f2a0842),
[setValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#aeb4937e13aff58a04f81fdadf544f7d9),
and
[App::Property::verifyPath()](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7).

## ◆ setPyObject()

| void PropertyFloat::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

Reimplemented in
[App::PropertyFloatConstraint](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#acb90ab8757a5dfcc66fbe2e468f0d342),
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#a72be43d71c5e5a5e0a174c01df176dc9),
and
[App::PropertyQuantityConstraint](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#a299ac9ee7870f29d5c3640a14114fcbe).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

## ◆ setValue()

void PropertyFloat::setValue  | ( | double  | _lValue_| ) |   
---|---|---|---|---|---  
  
References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

Referenced by
[TechDraw::DrawView::checkScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#ad2da2acbc02345e15a55d357ef545914),
[TechDrawGui::TaskRichAnno::commonFeatureUpdate()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ab5a728afdf435f4c1631b56211559576),
[TechDrawGui::TaskHatch::createHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ac9d417f22f5d5ed524f63d10cd4e63ef),
[FemGui::ViewProviderFemPostPlaneFunction::draggerUpdate()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#a8278598e6c0907c6743b3d0e53366cc0),
[PartDesign::Helix::execute()](../../d3/d78/classPartDesign_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[TechDraw::DrawProjGroup::execute()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a53036ad3632d51fe082b67c8f829b54f),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewPart::execute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[TechDrawGui::ViewProviderGeomHatch::getParameters()](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#adddf5cd28fdee06849c5c3bd464ac067),
[TechDrawGui::ViewProviderViewSection::getParameters()](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a8df1d57ca5c99b2d2a16f980618fd6a0),
[Surface::Extend::handleChangedPropertyName()](../../d1/d22/classSurface_1_1Extend.html#aa2e1ed26c2018e7234938836df41545c),
[PartDesign::Helix::handleChangedPropertyType()](../../d3/d78/classPartDesign_1_1Helix.html#a9e6fc22b84b2f26eef4b4880af00b063),
[TechDraw::DrawPage::handleChangedPropertyType()](../../d9/d5a/classTechDraw_1_1DrawPage.html#adde1799122996153278b2c68d4fa9b80),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[PartGui::ViewProviderPartExt::loadParameter()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ac9b18640b083f65180c44c787ed4b240),
[Gui::ViewProviderOrigin::onChanged()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[Fem::ConstraintBearing::onChanged()](../../df/d0a/classFem_1_1ConstraintBearing.html#ae81d9fda05994bd43bf81faf3acae5d6),
[Fem::ConstraintPulley::onChanged()](../../d3/dec/classFem_1_1ConstraintPulley.html#a6c23af9b8ba29b03f25163da9b75a41f),
[Robot::RobotObject::onChanged()](../../db/d51/classRobot_1_1RobotObject.html#abebfe59d5888146a96594cb7d31ffce8),
[PartDesignGui::ViewProviderSubShapeBinder::onChanged()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[Surface::Extend::onChanged()](../../d1/d22/classSurface_1_1Extend.html#ac33fb0ebd31edae770d009cc24c58df9),
[TechDraw::DrawProjGroup::onChanged()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[TechDraw::DrawView::onChanged()](../../d6/d1c/classTechDraw_1_1DrawView.html#a2980fbae4ce0a12aae609193764465cf),
[TechDraw::DrawViewDetail::onChanged()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[TechDrawGui::TaskDetail::onScaleTypeEdit()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#aaf0c48b11d118f0fb2a3ac2fcf661409),
[TechDrawGui::TaskGeomHatch::reject()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a18ae3da7ea9b2d55123cd563ed408217),
[Restore()](../../d3/dbe/classApp_1_1PropertyFloat.html#aa6d8ab192c6855fe5506b10e458460cf),
[TechDrawGui::TaskDetail::restoreDetailState()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a2bd15a19a7717a5bbbf306d1149fb53d),
[TechDrawGui::TaskProjGroup::restoreGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a348f413a63a7fd86ebf8978fee5d028f),
[TechDrawGui::TaskHatch::restoreHatchState()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ad4a3916be744e9438b81e65cddfb14d3),
[TechDrawGui::TaskSectionView::restoreSectionState()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a31ebe04f8add6f5d1c665c9b7c12c238),
[TechDrawGui::TaskProjGroup::scaleTypeChanged()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#ae8aa2696c9c438de8e953eee7ada9b9c),
[DrawingGui::orthoview::set_projection()](../../db/df8/classDrawingGui_1_1orthoview.html#acd64a222bfeb734c9f23b27860505fca),
[Spreadsheet::Sheet::setFloatProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a082ddc211d51376d6d8c3c77aa4a9bb2),
[setPathValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#ac5c0dfec5810e2860c64bb7186b2462a),
[DrawingGui::orthoview::setPos()](../../db/df8/classDrawingGui_1_1orthoview.html#a41759c0b5b460d739622debce91726bc),
[App::PropertyQuantity::setPyObject()](../../d4/d65/classApp_1_1PropertyQuantity.html#a72be43d71c5e5a5e0a174c01df176dc9),
[App::PropertyQuantityConstraint::setPyObject()](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#a299ac9ee7870f29d5c3640a14114fcbe),
[DrawingGui::orthoview::setScale()](../../db/df8/classDrawingGui_1_1orthoview.html#a0dacd70e31e479cb14dcfd262212f03b),
[App::PropertyQuantity::setValue()](../../d4/d65/classApp_1_1PropertyQuantity.html#a3d2646f79d896325882adf321f2244e9),
[FemGui::ViewProviderFemPostPlaneFunction::updateData()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#a6ec898b1ee3b9ae2983c1f424b2a55f4),
[TechDrawGui::TaskDetail::updateDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a9531ab9a77b992bbde7893f620cddd9f),
[FemGui::ViewProviderFemPostPipeline::updateFunctionSize()](../../df/d95/classFemGui_1_1ViewProviderFemPostPipeline.html#a015e75189dd7b4b8719fce0c264388f5),
[TechDrawGui::TaskHatch::updateHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#a885b8fcb16ca312a825e37d5f4ee11b4),
[FemGui::ViewProviderFemPostFunctionProvider::updateSize()](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#ad783f019da5429b4ca0669a14d606d72),
and
[TechDrawGui::TaskGeomHatch::updateValues()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a12acdd2beb497c2bfd197b8d8234f389).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyStandard.h
  * FreeCAD/src/App/PropertyStandard.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

