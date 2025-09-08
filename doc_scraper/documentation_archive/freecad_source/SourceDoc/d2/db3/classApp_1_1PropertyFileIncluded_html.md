---
url: https://freecad.github.io/SourceDoc/d2/db3/classApp_1_1PropertyFileIncluded.html
scraped_at: 2025-09-08T14:55:46.865607
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html)

[List of all members](../../d2/df7/classApp_1_1PropertyFileIncluded-members.html) | Public Member Functions | Protected Member Functions

App::PropertyFileIncluded Class Reference

File include properties This property doesn't only save the file name like
[PropertyFile](../../d9/d86/classApp_1_1PropertyFile.html "File properties
This property holds a file name.") it also includes the file itself into the
document.
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#details)

`#include <PropertyFile.h>`

##  Public Member Functions  
  
---  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a8357945cf4e3e84abd535ef6d53d4f99) () const  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a8357945cf4e3e84abd535ef6d53d4f99)  
  
virtual const char * | [getEditorName](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a288709e5f74e8e8a254bd8afade804e5) () const  
| Get the class name of the associated property editor item.
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a288709e5f74e8e8a254bd8afade804e5)  
  
std::string | [getExchangeTempFile](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a73f7c9a5c1633254cda5d292da6b10a5) () const  
| get a temp file name in the transient path of the document.
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a73f7c9a5c1633254cda5d292da6b10a5)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d2/db3/classApp_1_1PropertyFileIncluded.html#acf0627e62bf073aac01348d2781a5048) () const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#acf0627e62bf073aac01348d2781a5048)  
  
std::string | [getOriginalFileName](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a35bbec79184ede0db21bf1f7322e9eb7) () const  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a6b927db483c9f01bd4cfca56fabfbd7f) ()  
| This method returns the Python wrapper for a C++ object.
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a6b927db483c9f01bd4cfca56fabfbd7f)  
  
const char * | [getValue](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ae1079cece76c8aa298541ed243cfdbef) () const  
[bool](../../d9/db9/classbool.html) | [isEmpty](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5e2ee981e19cd7df32fe99f6fbe5114d) (void) const  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a048b1c82d308cbef3911301fd596c4ef) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const  
| Compare if this property has the same content as the given one.
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a048b1c82d308cbef3911301fd596c4ef)  
  
virtual void | [Paste](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e) (const [Property](../../d0/da9/classApp_1_1Property.html) &from)  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e)  
  
|
[PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aaaf895d521778c6f82c8cb315f9d4865)
()  
virtual void | [Restore](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd)  
  
virtual void | [RestoreDocFile](../../d2/db3/classApp_1_1PropertyFileIncluded.html#abaa879168b2300ffb4fdb20d3fdd4ef0) ([Base::Reader](../../d1/d1f/classBase_1_1Reader.html) &reader)  
| This method is used to restore large amounts of data from a file In this
method you simply stream in your
[SaveDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa23e081d9346621336c5c258f40c4a82
"This method is used to save large amounts of data to a binary file.") saved
data.
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#abaa879168b2300ffb4fdb20d3fdd4ef0)  
  
virtual void | [Save](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8)  
  
virtual void | [SaveDocFile](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa23e081d9346621336c5c258f40c4a82) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save large amounts of data to a binary file.
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa23e081d9346621336c5c258f40c4a82)  
  
virtual void | [setPyObject](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a885362f14defce5319c6408c6d3e6619) ([PyObject](../../df/d1b/classPyObject.html) *)  
void | [setValue](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa) (const char *sFile, const char *sName=nullptr)  
virtual | [~PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aad2fd02cf9b745baa5028ac4c0c61ab2) ()  
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
  
  
##  Protected Member Functions  
  
---  
void | [aboutToSetValue](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ab556673fad52c8535774ab736c61a40f) ()  
| Gets called by all
[setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa)
methods before the value has changed.
[More...](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ab556673fad52c8535774ab736c61a40f)  
  
std::string | [getDocTransientPath](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5f4e5ed4004ee3084755508e6c3b071a) () const  
std::string | [getUniqueFileName](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ac6b94c77254825a17621686c38efd006) (const std::string &, const std::string &) const  
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

File include properties This property doesn't only save the file name like
[PropertyFile](../../d9/d86/classApp_1_1PropertyFile.html "File properties
This property holds a file name.") it also includes the file itself into the
document.

The file doesn't get loaded into memory, it gets copied from the document
archive into the document transient directory. There it is accessible for the
algorithms. You get the transient path through
[getDocTransientPath()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5f4e5ed4004ee3084755508e6c3b071a)
It's allowed to read the file, it's not allowed to write the file directly in
the transient path! That would undermine the Undo/Redo framework. It's only
allowed to use
[setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa)
to change the file. If you give a file name outside the transient dir to
[setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa)
it will copy the file. If you give a file name in the transient path it will
just rename and use the same file. You can use
[getExchangeTempFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a73f7c9a5c1633254cda5d292da6b10a5
"get a temp file name in the transient path of the document.") to get a file
name in the transient dir to write a new file version.

## Constructor & Destructor Documentation

## ◆ PropertyFileIncluded()

PropertyFileIncluded::PropertyFileIncluded  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[Copy()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a8357945cf4e3e84abd535ef6d53d4f99).

## ◆ ~PropertyFileIncluded()

| PropertyFileIncluded::~PropertyFileIncluded  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[Base::FileInfo::ReadWrite](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a4c66903b9ac6c5788840b9e36d1b5911).

## Member Function Documentation

## ◆ aboutToSetValue()

| void PropertyFileIncluded::aboutToSetValue  | ( | void  | | ) |   
---|---|---|---|---|---  
protectedvirtual  
  
Gets called by all
[setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa)
methods before the value has changed.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67).

Referenced by
[Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd),
[RestoreDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#abaa879168b2300ffb4fdb20d3fdd4ef0),
and
[setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa).

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyFileIncluded::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::FileInfo::filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
[getUniqueFileName()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ac6b94c77254825a17621686c38efd006),
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964),
[PropertyFileIncluded()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aaaf895d521778c6f82c8cb315f9d4865),
[Base::FileInfo::ReadWrite](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a4c66903b9ac6c5788840b9e36d1b5911),
[Base::FileInfo::setPermissions()](../../dd/d34/classBase_1_1FileInfo.html#a5e5820903b5f70e76899d9962c0c6f23),
and
[App::Property::StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67).

## ◆ getDocTransientPath()

| std::string PropertyFileIncluded::getDocTransientPath  | ( | | ) |  const  
---|---|---|---|---  
protected  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
and
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127).

Referenced by
[getExchangeTempFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a73f7c9a5c1633254cda5d292da6b10a5),
[Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd),
[Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
and
[setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa).

## ◆ getEditorName()

| virtual const char * App::PropertyFileIncluded::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

## ◆ getExchangeTempFile()

std::string PropertyFileIncluded::getExchangeTempFile  | ( | | ) |  const  
---|---|---|---|---  
  
get a temp file name in the transient path of the document.

Using this file for new Version of the file and set this file with
[setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa)
is the fastest way to change the File.

References
[getDocTransientPath()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5f4e5ed4004ee3084755508e6c3b071a),
[Base::FileInfo::getTempFileName()](../../dd/d34/classBase_1_1FileInfo.html#a8378231b746bc06c6d1e35ca68837b74),
and
[getValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ae1079cece76c8aa298541ed243cfdbef).

Referenced by
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDraw::DrawHatch::replaceFileIncluded()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a2ecf95708ba982876944decf0bcb9812),
[TechDraw::DrawViewImage::replaceImageIncluded()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#af2f2591cbc41f4175f8bcee32049e81d),
[TechDraw::DrawGeomHatch::replacePatIncluded()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#ad77f5e3676e0ba1f3437bee6ca9faa7f),
[TechDraw::DrawViewSection::replacePatIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aba984603979c151ad1722cd482551637),
[TechDraw::DrawViewSection::replaceSvgIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a32311f95c465aa53c64ce49bf5ccd47a),
[TechDraw::DrawTileWeld::replaceSymbolIncluded()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a42d66700100b5f4fcf93eba676bcfd02),
[TechDraw::DrawHatch::setupFileIncluded()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a0846fb8f0861b48c08a9b869612e130b),
[TechDraw::DrawViewImage::setupImageIncluded()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a70665b6da416755ac2cdb36d9c9ecf6d),
[TechDraw::DrawGeomHatch::setupPatIncluded()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a60fb2b1d4310efa884589ce415b086c9),
[TechDraw::DrawViewSection::setupPatIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#af26e22d3b0683c955561590968b25275),
[TechDraw::DrawViewSection::setupSvgIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a3736e6db938d365a0866d6704bcb3fe0),
and
[TechDraw::DrawTileWeld::setupSymbolIncluded()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a9a0ec49268483ff93a086ca6a58c58da).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) PropertyFileIncluded::getMemSize  | ( | void  | | ) |  const  
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

References
[App::Property::getMemSize()](../../d0/da9/classApp_1_1Property.html#a933a44c77e539e1942227d1f266d3330).

## ◆ getOriginalFileName()

std::string PropertyFileIncluded::getOriginalFileName  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::VRMLObject::onChanged()](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyFileIncluded::getPyObject  | ( | void  | | ) |   
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

## ◆ getUniqueFileName()

| std::string PropertyFileIncluded::getUniqueFileName  | ( | const std::string & | _path_ ,   
---|---|---|---  
|  | const std::string & | _filename_  
| ) | |  const  
protected  
  
References
[Base::FileInfo::exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[Base::FileInfo::filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
[Base::Uuid::getValue()](../../d6/d43/classBase_1_1Uuid.html#a95e42ab3b423ce44ba132708f1def69f),
and
[Base::FileInfo::setFile()](../../dd/d34/classBase_1_1FileInfo.html#ad254d88b127a0e93086c58f9c0487616).

Referenced by
[Copy()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a8357945cf4e3e84abd535ef6d53d4f99),
and
[Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e).

## ◆ getValue()

const char * PropertyFileIncluded::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[TechDrawGui::QGISVGTemplate::createClickHandles()](../../d4/d36/classTechDrawGui_1_1QGISVGTemplate.html#a2bcf2fb5e0c80557b727afaaadbb2777),
[Gui::Dialog::DlgEditFileIncludePropertyExternal::Do()](../../d8/d45/classGui_1_1Dialog_1_1DlgEditFileIncludePropertyExternal.html#ace09d54687de7aa93c318fba862bd3bc),
[TechDrawGui::QGISVGTemplate::draw()](../../d4/d36/classTechDrawGui_1_1QGISVGTemplate.html#ab8cf6b0952c0909886812eba624c217b),
[TechDrawGui::QGIViewPart::drawViewPart()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#add7c40ff3fc3fcc84308bb29225f8cc9),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDraw::DrawGeomHatch::getDecodedSpecsFromFile()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9310adb90d17a4212adfe5751cb9d55c),
[getExchangeTempFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a73f7c9a5c1633254cda5d292da6b10a5),
[TechDraw::DrawViewSection::makeLineSets()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a8673a58822bb65ebe493c128d2aef29e),
[Drawing::FeaturePage::onChanged()](../../db/d0f/classDrawing_1_1FeaturePage.html#a9c6b6897f29ff589163044d51b7e5c04),
[Robot::RobotObject::onChanged()](../../db/d51/classRobot_1_1RobotObject.html#abebfe59d5888146a96594cb7d31ffce8),
[TechDraw::DrawSVGTemplate::onChanged()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#afa43ef4d1bf529675b75c5d31fff582b),
[Drawing::FeaturePage::onDocumentRestored()](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e),
[Raytracing::LuxProject::onDocumentRestored()](../../d5/de6/classRaytracing_1_1LuxProject.html#af2f620cf5c7c096d24b4ad220123c909),
[Raytracing::RayProject::onDocumentRestored()](../../d2/d89/classRaytracing_1_1RayProject.html#a9d83bff4b32c1801a8ba907221d45295),
[TechDrawGui::QGSPage::postProcessXml()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#ac4055009ba04a7f89f6c9a935e4ce0a5),
[App::VRMLObject::RestoreDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a90cb824c6253de535ec16e1935455599),
[TechDraw::DrawViewSection::setupPatIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#af26e22d3b0683c955561590968b25275),
[TechDraw::DrawViewSection::setupSvgIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a3736e6db938d365a0866d6704bcb3fe0),
[TechDraw::DrawTileWeld::setupSymbolIncluded()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a9a0ec49268483ff93a086ca6a58c58da),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[ImageGui::ViewProviderImagePlane::updateData()](../../db/d5a/classImageGui_1_1ViewProviderImagePlane.html#ae91df03af7efab412ed649b8db50463e),
and
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747).

## ◆ isEmpty()

[bool](../../d9/db9/classbool.html) App::PropertyFileIncluded::isEmpty  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[TechDrawGui::QGIViewPart::drawViewPart()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#add7c40ff3fc3fcc84308bb29225f8cc9),
[TechDraw::DrawGeomHatch::makeLineSets()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a0736be1ff7a1996022a4d944f9d82e19),
[TechDraw::DrawViewSection::makeLineSets()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a8673a58822bb65ebe493c128d2aef29e),
[TechDraw::DrawTileWeld::onDocumentRestored()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a7a4b1b5d8aac6cdb9a3a16997934c000),
[TechDraw::DrawGeomHatch::onDocumentRestored()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a236c7efbf2e991277bd53a914eb247bb),
[TechDraw::DrawHatch::onDocumentRestored()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a3437412caff103d7c68842db2e694a7b),
[TechDraw::DrawViewSection::onDocumentRestored()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a639636de121b31e8f97a010b214fb71e),
[TechDraw::DrawHatch::replaceFileIncluded()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a2ecf95708ba982876944decf0bcb9812),
[TechDraw::DrawViewImage::replaceImageIncluded()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#af2f2591cbc41f4175f8bcee32049e81d),
[TechDraw::DrawGeomHatch::replacePatIncluded()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#ad77f5e3676e0ba1f3437bee6ca9faa7f),
[TechDraw::DrawViewSection::replacePatIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aba984603979c151ad1722cd482551637),
[TechDraw::DrawViewSection::replaceSvgIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a32311f95c465aa53c64ce49bf5ccd47a),
[TechDraw::DrawTileWeld::replaceSymbolIncluded()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a42d66700100b5f4fcf93eba676bcfd02),
[TechDraw::DrawHatch::setupFileIncluded()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a0846fb8f0861b48c08a9b869612e130b),
and
[TechDraw::DrawGeomHatch::setupPatIncluded()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a60fb2b1d4310efa884589ce415b086c9).

## ◆ isSame()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyFileIncluded::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

## ◆ Paste()

| void PropertyFileIncluded::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
virtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be).

References
[aboutToSetValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ab556673fad52c8535774ab736c61a40f),
[Base::FileInfo::copyTo()](../../dd/d34/classBase_1_1FileInfo.html#a47907e1927f6ff3b767f83ac846ef8e1),
[Base::FileInfo::deleteFile()](../../dd/d34/classBase_1_1FileInfo.html#aafd7a8df3d22c3e48523afe865115b9c),
[Base::FileInfo::dirPath()](../../dd/d34/classBase_1_1FileInfo.html#a931384d1da89e1295bb158617f3f5712),
[Base::FileInfo::exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[Base::FileInfo::fileName()](../../dd/d34/classBase_1_1FileInfo.html#a8ae2069796787d27306bb49bd70e3e3a),
[Base::FileInfo::filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
[getDocTransientPath()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5f4e5ed4004ee3084755508e6c3b071a),
[getUniqueFileName()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ac6b94c77254825a17621686c38efd006),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
[Base::FileInfo::ReadOnly](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a2a81c484ad2171f79da987b019813a9c),
[Base::FileInfo::ReadWrite](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a4c66903b9ac6c5788840b9e36d1b5911),
[Base::FileInfo::renameFile()](../../dd/d34/classBase_1_1FileInfo.html#ac5067c657858a93f81d2fbfdd4fdf8eb),
[Base::FileInfo::setFile()](../../dd/d34/classBase_1_1FileInfo.html#ad254d88b127a0e93086c58f9c0487616),
and
[Base::FileInfo::setPermissions()](../../dd/d34/classBase_1_1FileInfo.html#a5e5820903b5f70e76899d9962c0c6f23).

## ◆ Restore()

| void PropertyFileIncluded::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8
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
[aboutToSetValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ab556673fad52c8535774ab736c61a40f),
[Base::XMLReader::addFile()](../../dc/d95/classBase_1_1XMLReader.html#adf371fa6365af1b80097055bebf87dfe),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[getDocTransientPath()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5f4e5ed4004ee3084755508e6c3b071a),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
[Base::XMLReader::readBinFile()](../../dc/d95/classBase_1_1XMLReader.html#a9c7fc15570f69a6db6e1961770928912),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[Base::XMLReader::readEndElement()](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3),
[Base::FileInfo::ReadOnly](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a2a81c484ad2171f79da987b019813a9c),
and
[Base::FileInfo::setPermissions()](../../dd/d34/classBase_1_1FileInfo.html#a5e5820903b5f70e76899d9962c0c6f23).

## ◆ RestoreDocFile()

| void PropertyFileIncluded::RestoreDocFile  | ( | [Base::Reader](../../d1/d1f/classBase_1_1Reader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore large amounts of data from a file In this
method you simply stream in your
[SaveDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa23e081d9346621336c5c258f40c4a82
"This method is used to save large amounts of data to a binary file.") saved
data.

Again you have to apply for the call of this method in the
[Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd
"This method is used to restore properties from an XML document.") call:

void
PropertyMeshKernel::Restore([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html
"The XML reader class This is an important helper class for the store and
retrieval system of objects ...") &reader)

{

reader.[readElement](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e
"read until a start element is found \(<name>\) or start-end element
\(<name/>\) \(with special name if giv...")("Mesh");

std::string file
(reader.[getAttribute](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788
"return the named attribute as a double floating point \(does type
checking\)")("file") );

if(file == "")

{

// read XML

MeshCore::MeshDocXML restorer(*_pcMesh);

restorer.Restore(reader);

}else{

// initiate a file read

reader.[addFile](../../dc/d95/classBase_1_1XMLReader.html#adf371fa6365af1b80097055bebf87dfe
"add a read request of a persistent object")(file.c_str(),this);

}

}

After you issued the reader.addFile() your
[RestoreDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#abaa879168b2300ffb4fdb20d3fdd4ef0
"This method is used to restore large amounts of data from a file In this
method you simply stream in ...") is called:

void
PropertyMeshKernel::RestoreDocFile([Base::Reader](../../d1/d1f/classBase_1_1Reader.html)
&reader)

{

_pcMesh->Read( reader );

}

See also

    [Base::Reader](../../d1/d1f/classBase_1_1Reader.html),[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html "The XML reader class This is an important helper class for the store and retrieval system of objects ...")

Reimplemented from
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#a65260f99c6e0449f6caca2bc71efe37b).

References
[aboutToSetValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ab556673fad52c8535774ab736c61a40f),
[Base::FileInfo::exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
[Base::FileInfo::isWritable()](../../dd/d34/classBase_1_1FileInfo.html#a550b75d516c531e941faffbd70054862),
[Base::FileInfo::ReadOnly](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a2a81c484ad2171f79da987b019813a9c),
and
[Base::FileInfo::setPermissions()](../../dd/d34/classBase_1_1FileInfo.html#a5e5820903b5f70e76899d9962c0c6f23).

## ◆ Save()

| void PropertyFileIncluded::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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
[Base::Writer::addFile()](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55),
[Base::Writer::decInd()](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92),
[Base::Persistence::encodeAttribute()](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec),
[Base::FileInfo::exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[Base::FileInfo::filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
[getDocTransientPath()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5f4e5ed4004ee3084755508e6c3b071a),
[Base::Writer::incInd()](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5),
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
[Base::Writer::insertBinFile()](../../dd/d4d/classBase_1_1Writer.html#aafe5f2af569301dbae674de29e757de4),
[Base::Writer::isForceXML()](../../dd/d4d/classBase_1_1Writer.html#a2312714b18983912a3b4b01121bab5d6),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ SaveDocFile()

| void PropertyFileIncluded::SaveDocFile  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
virtual  
  
This method is used to save large amounts of data to a binary file.

Sometimes it makes no sense to write property data as XML. In case the amount
of data is too big or the data type has a more effective way to save itself.
In this cases it is possible to write the data in a separate file inside the
document archive. In case you want do so you have to re-implement
[SaveDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa23e081d9346621336c5c258f40c4a82
"This method is used to save large amounts of data to a binary file."). First,
you have to inform the framework in
[Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8
"This method is used to save properties to an XML document.") that you want do
so. Here an example from the [Mesh](../../dc/d48/namespaceMesh.html "The
namespace of the Mesh Application layer library.") module which can save a
(pontetionaly big) triangle mesh:

void PropertyMeshKernel::Save
([Base::Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This
is an important helper class for the store and retrieval system of persistent
o...") &writer) const

{

if
(writer.[isForceXML](../../dd/d4d/classBase_1_1Writer.html#a2312714b18983912a3b4b01121bab5d6
"check on state")())

{

writer <<
writer.[ind](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368
"get the current indentation")() << "<Mesh>" << std::endl;

MeshCore::MeshDocXML saver(*_pcMesh);

saver.Save(writer);

}else{

writer <<
writer.[ind](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368
"get the current indentation")() << "<Mesh file=\"" <<
writer.[addFile](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55
"add a write request of a persistent object")("MeshKernel.bms", this) <<
"\"/>" << std::endl;

}

The writer.isForceXML() is an indication to force you to write XML. Regardless
of size and effectiveness. The second part informs the Base::writer through
writer.addFile("MeshKernel.bms", this) that this object wants to write a file
with the given name. The method addFile() returns a unique name that then is
written in the XML stream. This allows your
[RestoreDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#abaa879168b2300ffb4fdb20d3fdd4ef0
"This method is used to restore large amounts of data from a file In this
method you simply stream in ...") method to identify and read the file again.
Later your
[SaveDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa23e081d9346621336c5c258f40c4a82
"This method is used to save large amounts of data to a binary file.") method
is called as many times as you issued the addFile() call:

void PropertyMeshKernel::SaveDocFile
([Base::Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This
is an important helper class for the store and retrieval system of persistent
o...") &writer) const

{

_pcMesh->Write( writer );

}

In this method you can simply stream your content to the file
([Base::Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This
is an important helper class for the store and retrieval system of persistent
o...") inheriting from ostream).

Reimplemented from
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45).

References
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ setPyObject()

| void PropertyFileIncluded::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

References
[App::getNameFromFile()](../../dd/dc2/namespaceApp.html#a5eae26b4d4d1f65b38010f05f469f745),
[App::isIOFile()](../../dd/dc2/namespaceApp.html#aa30a0c906e85d254331e50de42132364),
and
[setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa).

## ◆ setValue()

void PropertyFileIncluded::setValue  | ( | const char *  | _sFile_ ,   
---|---|---|---  
|  | const char *  | _sName_ = `nullptr`  
| ) | |   
  
References
[aboutToSetValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ab556673fad52c8535774ab736c61a40f),
[Base::FileInfo::dirPath()](../../dd/d34/classBase_1_1FileInfo.html#a931384d1da89e1295bb158617f3f5712),
[Base::FileInfo::exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[Base::FileInfo::extension()](../../dd/d34/classBase_1_1FileInfo.html#afb9db1389fb6645d1f423ce0871468b5),
[Base::FileInfo::fileName()](../../dd/d34/classBase_1_1FileInfo.html#a8ae2069796787d27306bb49bd70e3e3a),
[Base::FileInfo::fileNamePure()](../../dd/d34/classBase_1_1FileInfo.html#aee95cfa273dadbe71b450f3b834a4894),
[Base::FileInfo::filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
[getDocTransientPath()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5f4e5ed4004ee3084755508e6c3b071a),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
[Base::FileInfo::ReadOnly](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a2a81c484ad2171f79da987b019813a9c),
[Base::FileInfo::ReadWrite](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a4c66903b9ac6c5788840b9e36d1b5911),
and
[Base::FileInfo::setFile()](../../dd/d34/classBase_1_1FileInfo.html#ad254d88b127a0e93086c58f9c0487616).

Referenced by
[Gui::Dialog::DlgEditFileIncludePropertyExternal::Do()](../../d8/d45/classGui_1_1Dialog_1_1DlgEditFileIncludePropertyExternal.html#ace09d54687de7aa93c318fba862bd3bc),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDraw::DrawHatch::replaceFileIncluded()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a2ecf95708ba982876944decf0bcb9812),
[TechDraw::DrawViewImage::replaceImageIncluded()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#af2f2591cbc41f4175f8bcee32049e81d),
[TechDraw::DrawGeomHatch::replacePatIncluded()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#ad77f5e3676e0ba1f3437bee6ca9faa7f),
[TechDraw::DrawViewSection::replacePatIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aba984603979c151ad1722cd482551637),
[TechDraw::DrawViewSection::replaceSvgIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a32311f95c465aa53c64ce49bf5ccd47a),
[TechDraw::DrawTileWeld::replaceSymbolIncluded()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a42d66700100b5f4fcf93eba676bcfd02),
[setPyObject()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a885362f14defce5319c6408c6d3e6619),
[TechDraw::DrawHatch::setupFileIncluded()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a0846fb8f0861b48c08a9b869612e130b),
[TechDraw::DrawViewImage::setupImageIncluded()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a70665b6da416755ac2cdb36d9c9ecf6d),
[TechDraw::DrawGeomHatch::setupPatIncluded()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a60fb2b1d4310efa884589ce415b086c9),
[TechDraw::DrawViewSection::setupPatIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#af26e22d3b0683c955561590968b25275),
[TechDraw::DrawViewSection::setupSvgIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a3736e6db938d365a0866d6704bcb3fe0),
and
[TechDraw::DrawTileWeld::setupSymbolIncluded()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a9a0ec49268483ff93a086ca6a58c58da).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyFile.h
  * FreeCAD/src/App/PropertyFile.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

