---
url: https://freecad.github.io/SourceDoc/d0/dc7/classApp_1_1PropertyColorList.html
scraped_at: 2025-09-08T14:55:32.756695
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html)

[List of all members](../../db/da1/classApp_1_1PropertyColorList-members.html) | Public Member Functions | Protected Member Functions

App::PropertyColorList Class Reference

`#include <PropertyStandard.h>`

##  Public Member Functions  
  
---  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d0/dc7/classApp_1_1PropertyColorList.html#a71525d9a6c7ff7da1202b6f3ed6659dd) (void) const override  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d0/dc7/classApp_1_1PropertyColorList.html#a71525d9a6c7ff7da1202b6f3ed6659dd)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d0/dc7/classApp_1_1PropertyColorList.html#a84c1f4f40247c1cbce90a85d082206c9) (void) const override  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../d0/dc7/classApp_1_1PropertyColorList.html#a84c1f4f40247c1cbce90a85d082206c9)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d0/dc7/classApp_1_1PropertyColorList.html#a07d36d2877e6004fba77c18f6a6e5610) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../d0/dc7/classApp_1_1PropertyColorList.html#a07d36d2877e6004fba77c18f6a6e5610)  
  
virtual void | [Paste](../../d0/dc7/classApp_1_1PropertyColorList.html#a09999f92abcf033497c84ee02a28a23b) (const [Property](../../d0/da9/classApp_1_1Property.html) &from) override  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d0/dc7/classApp_1_1PropertyColorList.html#a09999f92abcf033497c84ee02a28a23b)  
  
|
[PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#abc9447c601732a763b03771db2d754fa)
()  
| A constructor.
[More...](../../d0/dc7/classApp_1_1PropertyColorList.html#abc9447c601732a763b03771db2d754fa)  
  
virtual void | [Restore](../../d0/dc7/classApp_1_1PropertyColorList.html#af8af562580107a8bcd34a2e88b650a73) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../d0/dc7/classApp_1_1PropertyColorList.html#af8af562580107a8bcd34a2e88b650a73)  
  
virtual void | [RestoreDocFile](../../d0/dc7/classApp_1_1PropertyColorList.html#a48a1edd98f727583fd23c99bb503f0ec) ([Base::Reader](../../d1/d1f/classBase_1_1Reader.html) &reader) override  
| This method is used to restore large amounts of data from a file In this
method you simply stream in your
[SaveDocFile()](../../d0/dc7/classApp_1_1PropertyColorList.html#a7e0b4a92693212f1c9f9217e081b5843
"This method is used to save large amounts of data to a binary file.") saved
data.
[More...](../../d0/dc7/classApp_1_1PropertyColorList.html#a48a1edd98f727583fd23c99bb503f0ec)  
  
virtual void | [Save](../../d0/dc7/classApp_1_1PropertyColorList.html#a83eefd2fbd347e44e2c0d5e63b1bc2e1) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../d0/dc7/classApp_1_1PropertyColorList.html#a83eefd2fbd347e44e2c0d5e63b1bc2e1)  
  
virtual void | [SaveDocFile](../../d0/dc7/classApp_1_1PropertyColorList.html#a7e0b4a92693212f1c9f9217e081b5843) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save large amounts of data to a binary file.
[More...](../../d0/dc7/classApp_1_1PropertyColorList.html#a7e0b4a92693212f1c9f9217e081b5843)  
  
virtual | [~PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#afd1cef8d9331fc0e5690046cf17f91df) ()  
| A destructor.
[More...](../../d0/dc7/classApp_1_1PropertyColorList.html#afd1cef8d9331fc0e5690046cf17f91df)  
  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyListsT< Color >](../../d1/d0e/classApp_1_1PropertyListsT.html)  
virtual [int](../../d1/da0/classint.html) | [getSize](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194) (void) const override  
const std::vector< [Color](../../d3/d3a/classApp_1_1Color.html) > & | [getValue](../../d1/d0e/classApp_1_1PropertyListsT.html#a064f87de752ea68f9a660c10ba3dcf4b) (void) const  
const std::vector< [Color](../../d3/d3a/classApp_1_1Color.html) > & | [getValues](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938) (void) const  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const override  
| Compare if this property has the same content as the given one.
[More...](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109)  
  
[const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) | [operator[]](../../d1/d0e/classApp_1_1PropertyListsT.html#a8d9939f872f9aa1ff103027249f99036) ([int](../../d1/da0/classint.html) idx) const  
virtual void | [set1Value](../../d1/d0e/classApp_1_1PropertyListsT.html#ada9ee7ea1e2127ba7456b9a4a4697d80) ([int](../../d1/da0/classint.html) index, [const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) value)  
virtual void | [setPyObject](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2) ([PyObject](../../df/d1b/classPyObject.html) *value) override  
virtual void | [setSize](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9) ([int](../../d1/da0/classint.html) newSize) override  
virtual void | [setSize](../../d1/d0e/classApp_1_1PropertyListsT.html#a3d8817fe93f3db9c3d32dcecafbfd061) ([int](../../d1/da0/classint.html) newSize, [const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) def)  
void | [setValue](../../d1/d0e/classApp_1_1PropertyListsT.html#a39353cb8c1c869664480e455fc076f19) (const std::vector< [Color](../../d3/d3a/classApp_1_1Color.html) > &newValues=std::vector< [Color](../../d3/d3a/classApp_1_1Color.html) >())  
void | [setValue](../../d1/d0e/classApp_1_1PropertyListsT.html#abaaa23d8c4ff48e19290cf81a62f6e94) ([const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) value)  
virtual void | [setValues](../../d1/d0e/classApp_1_1PropertyListsT.html#a8744f95234dbfb9431759906c2a76cd4) (const std::vector< [Color](../../d3/d3a/classApp_1_1Color.html) > &newValues=std::vector< [Color](../../d3/d3a/classApp_1_1Color.html) >())  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyLists](../../d4/da1/classApp_1_1PropertyLists.html)  
[bool](../../d9/db9/classbool.html) | [isOrderRelevant](../../d4/da1/classApp_1_1PropertyLists.html#aa0474e2ed9b9e29e81505e63c0e68c00) () const  
void | [setOrderRelevant](../../d4/da1/classApp_1_1PropertyLists.html#a94db90a0679ccd3f455311ef8abd6ae5) ([bool](../../d9/db9/classbool.html) on)  
virtual void | [setPyObject](../../d4/da1/classApp_1_1PropertyLists.html#a47e37fe20890a5258c0351c6f3244d60) ([PyObject](../../df/d1b/classPyObject.html) *obj) override  
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
  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyListsBase](../../d7/d8e/classApp_1_1PropertyListsBase.html)  
void | [clearTouchList](../../d7/d8e/classApp_1_1PropertyListsBase.html#aaca8b243e8c7606d81aa0bbadf1fefa1) ()  
virtual [int](../../d1/da0/classint.html) | [getSize](../../d7/d8e/classApp_1_1PropertyListsBase.html#acbdccea70aaba518e3af5ac37580d54d) (void) const =0  
const std::set< [int](../../d1/da0/classint.html) > & | [getTouchList](../../d7/d8e/classApp_1_1PropertyListsBase.html#a7ff4978224bd672331d098bfeeb07f09) () const  
virtual void | [setSize](../../d7/d8e/classApp_1_1PropertyListsBase.html#a59f18e45d11306be56f29104af5b2160) ([int](../../d1/da0/classint.html) newSize)=0  
  
##  Protected Member Functions  
  
---  
[Color](../../d3/d3a/classApp_1_1Color.html) | [getPyValue](../../d0/dc7/classApp_1_1PropertyColorList.html#a1185ac555445591be3ab82499256987f) ([PyObject](../../df/d1b/classPyObject.html) *) const override  
![-](../../closed.png) Protected Member Functions inherited from
[App::PropertyListsT< Color >](../../d1/d0e/classApp_1_1PropertyListsT.html)  
virtual [Color](../../d3/d3a/classApp_1_1Color.html) | [getPyValue](../../d1/d0e/classApp_1_1PropertyListsT.html#a0048578553b52a7697ca08bcd71249b0) ([PyObject](../../df/d1b/classPyObject.html) *item) const=0  
void | [setPyValues](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e) (const std::vector< [PyObject](../../df/d1b/classPyObject.html) * > &vals, const std::vector< [int](../../d1/da0/classint.html) > &indices) override  
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
  
virtual void | [setPyValues](../../d7/d8e/classApp_1_1PropertyListsBase.html#a33a3c42a6dd5aa648329c817e8689921) (const std::vector< [PyObject](../../df/d1b/classPyObject.html) * > &vals, const std::vector< [int](../../d1/da0/classint.html) > &indices)  
![-](../../closed.png) Protected Member Functions inherited from
[App::AtomicPropertyChangeInterface< PropertyListsT< Color, std::vector< Color
>, PropertyLists >
>](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)  
|
[AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#aab004d1fbf131c11d570dcfcad7c22e1)
()  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Types inherited from [App::PropertyListsT< Color
>](../../d1/d0e/classApp_1_1PropertyListsT.html)  
typedef [AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)< [PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< [Color](../../d3/d3a/classApp_1_1Color.html), std::vector< [Color](../../d3/d3a/classApp_1_1Color.html) >, [PropertyLists](../../d4/da1/classApp_1_1PropertyLists.html) > >::AtomicPropertyChange | [atomic_change](../../d1/d0e/classApp_1_1PropertyListsT.html#ac461d1a7873429bac88827a89d979438)  
typedef ListT::const_reference | [const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5)  
typedef std::vector< [Color](../../d3/d3a/classApp_1_1Color.html) > | [list_type](../../d1/d0e/classApp_1_1PropertyListsT.html#ab1c519424072c713a1b2d32b5e9264af)  
typedef [PropertyLists](../../d4/da1/classApp_1_1PropertyLists.html) | [parent_type](../../d1/d0e/classApp_1_1PropertyListsT.html#a423c6bad5d316ae7195a68d4ff5dc946)  
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
![-](../../closed.png) Public Attributes inherited from [App::PropertyListsT<
Color >](../../d1/d0e/classApp_1_1PropertyListsT.html)  
[friend](../../d7/d23/classfriend.html) | [atomic_change](../../d1/d0e/classApp_1_1PropertyListsT.html#a0eb905df14c931335baa2fcfcb851bca)  
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
  
![-](../../closed.png) Protected Attributes inherited from
[App::AtomicPropertyChangeInterface< PropertyListsT< Color, std::vector< Color
>, PropertyLists >
>](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)  
[bool](../../d9/db9/classbool.html) | [hasChanged](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a1e6d78782f81aef5d1efe58ac219e2df)  
[int](../../d1/da0/classint.html) | [signalCounter](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a07e13a81f4f601365b04cc8806d075f9)  
| Counter for invoking transaction start/stop.
[More...](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a07e13a81f4f601365b04cc8806d075f9)  
  
  
## Constructor & Destructor Documentation

## ◆ PropertyColorList()

PropertyColorList::PropertyColorList  | ( | | ) |   
---|---|---|---|---  
  
A constructor.

A more elaborate description of the constructor.

Referenced by
[Copy()](../../d0/dc7/classApp_1_1PropertyColorList.html#a71525d9a6c7ff7da1202b6f3ed6659dd).

## ◆ ~PropertyColorList()

| PropertyColorList::~PropertyColorList  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyColorList::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

References
[PropertyColorList()](../../d0/dc7/classApp_1_1PropertyColorList.html#abc9447c601732a763b03771db2d754fa).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) PropertyColorList::getMemSize  | ( | void  | | ) |  const  
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

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyColorList::getPyObject  | ( | void  | | ) |   
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

References [App::PropertyListsT< Color
>::getSize()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194).

## ◆ getPyValue()

| [Color](../../d3/d3a/classApp_1_1Color.html) PropertyColorList::getPyValue  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _item_| ) |  const  
---|---|---|---|---|---  
overrideprotectedvirtual  
  
Implements [App::PropertyListsT< Color
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a0048578553b52a7697ca08bcd71249b0).

References
[App::PropertyColor::getValue()](../../d9/d0b/classApp_1_1PropertyColor.html#ad5edc545f1f19ec00b51f42cdbc62bb6),
and
[App::PropertyColor::setPyObject()](../../d9/d0b/classApp_1_1PropertyColor.html#a6e633e7e63cde42f29ea066464910433).

## ◆ Paste()

| void PropertyColorList::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be).

References [App::PropertyListsT< Color
>::setValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8744f95234dbfb9431759906c2a76cd4).

## ◆ Restore()

| void PropertyColorList::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d0/dc7/classApp_1_1PropertyColorList.html#a83eefd2fbd347e44e2c0d5e63b1bc2e1
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
[Base::XMLReader::addFile()](../../dc/d95/classBase_1_1XMLReader.html#adf371fa6365af1b80097055bebf87dfe),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
and
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e).

## ◆ RestoreDocFile()

| void PropertyColorList::RestoreDocFile  | ( | [Base::Reader](../../d1/d1f/classBase_1_1Reader.html) & | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method is used to restore large amounts of data from a file In this
method you simply stream in your
[SaveDocFile()](../../d0/dc7/classApp_1_1PropertyColorList.html#a7e0b4a92693212f1c9f9217e081b5843
"This method is used to save large amounts of data to a binary file.") saved
data.

Again you have to apply for the call of this method in the
[Restore()](../../d0/dc7/classApp_1_1PropertyColorList.html#af8af562580107a8bcd34a2e88b650a73
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
[RestoreDocFile()](../../d0/dc7/classApp_1_1PropertyColorList.html#a48a1edd98f727583fd23c99bb503f0ec
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

References [App::PropertyListsT< Color
>::setValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8744f95234dbfb9431759906c2a76cd4).

## ◆ Save()

| void PropertyColorList::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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
[Base::Writer::addFile()](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55),
[App::Property::getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a),
[App::PropertyListsT< Color
>::getSize()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
[Base::Writer::isForceXML()](../../dd/d4d/classBase_1_1Writer.html#a2312714b18983912a3b4b01121bab5d6),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ SaveDocFile()

| void PropertyColorList::SaveDocFile  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
This method is used to save large amounts of data to a binary file.

Sometimes it makes no sense to write property data as XML. In case the amount
of data is too big or the data type has a more effective way to save itself.
In this cases it is possible to write the data in a separate file inside the
document archive. In case you want do so you have to re-implement
[SaveDocFile()](../../d0/dc7/classApp_1_1PropertyColorList.html#a7e0b4a92693212f1c9f9217e081b5843
"This method is used to save large amounts of data to a binary file."). First,
you have to inform the framework in
[Save()](../../d0/dc7/classApp_1_1PropertyColorList.html#a83eefd2fbd347e44e2c0d5e63b1bc2e1
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
[RestoreDocFile()](../../d0/dc7/classApp_1_1PropertyColorList.html#a48a1edd98f727583fd23c99bb503f0ec
"This method is used to restore large amounts of data from a file In this
method you simply stream in ...") method to identify and read the file again.
Later your
[SaveDocFile()](../../d0/dc7/classApp_1_1PropertyColorList.html#a7e0b4a92693212f1c9f9217e081b5843
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

References [App::PropertyListsT< Color
>::getSize()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyStandard.h
  * FreeCAD/src/App/PropertyStandard.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

