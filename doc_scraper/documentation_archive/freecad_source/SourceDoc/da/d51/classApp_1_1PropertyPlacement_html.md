---
url: https://freecad.github.io/SourceDoc/da/d51/classApp_1_1PropertyPlacement.html
scraped_at: 2025-09-08T14:56:31.025180
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html)

[List of all members](../../d8/d6b/classApp_1_1PropertyPlacement-members.html) | Public Member Functions | Static Public Attributes

App::PropertyPlacement Class Reference

[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") representing a placement.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#details)

`#include <PropertyGeo.h>`

##  Public Member Functions  
  
---  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../da/d51/classApp_1_1PropertyPlacement.html#ae4fc87aa899e0a6cb40609b6307f661d) (void) const override  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#ae4fc87aa899e0a6cb40609b6307f661d)  
  
const char * | [getEditorName](../../da/d51/classApp_1_1PropertyPlacement.html#adb4d89095f4b08a557675d021c888d4f) (void) const override  
| Get the class name of the associated property editor item.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#adb4d89095f4b08a557675d021c888d4f)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../da/d51/classApp_1_1PropertyPlacement.html#a33e86ed95a033c93066f10d03b35fb17) (void) const override  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a33e86ed95a033c93066f10d03b35fb17)  
  
void | [getPaths](../../da/d51/classApp_1_1PropertyPlacement.html#a533c181be98ff243e893f11f4584b77e) (std::vector< [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &paths) const override  
| Get valid paths for this property; used by auto completer.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a533c181be98ff243e893f11f4584b77e)  
  
virtual const boost::any | [getPathValue](../../da/d51/classApp_1_1PropertyPlacement.html#a06e19f55576a35cf180838f09991371e) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path) const override  
| Get value of property.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a06e19f55576a35cf180838f09991371e)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../da/d51/classApp_1_1PropertyPlacement.html#a2c1f9fc6fd155b2c5886ea61c37ea689) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a2c1f9fc6fd155b2c5886ea61c37ea689)  
  
virtual [bool](../../d9/db9/classbool.html) | [getPyPathValue](../../da/d51/classApp_1_1PropertyPlacement.html#a462af42ef4eadd19ca7645e961432b1c) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, Py::Object &res) const override  
| Get Python value of property.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a462af42ef4eadd19ca7645e961432b1c)  
  
const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) & | [getValue](../../da/d51/classApp_1_1PropertyPlacement.html#a430fb2b0baee33f2967118bbbc7e6d74) (void) const  
| This method returns a string representation of the property.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a430fb2b0baee33f2967118bbbc7e6d74)  
  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../da/d51/classApp_1_1PropertyPlacement.html#a3645ce165f801b3aef3bfdda4ada6c83) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const override  
| Compare if this property has the same content as the given one.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a3645ce165f801b3aef3bfdda4ada6c83)  
  
virtual void | [Paste](../../da/d51/classApp_1_1PropertyPlacement.html#afbd1d98d3c19b17652f2306885da8815) (const [Property](../../d0/da9/classApp_1_1Property.html) &from) override  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#afbd1d98d3c19b17652f2306885da8815)  
  
|
[PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a93f52f7245c2fe14411537e115f963e1)
()  
| A constructor.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a93f52f7245c2fe14411537e115f963e1)  
  
virtual void | [Restore](../../da/d51/classApp_1_1PropertyPlacement.html#a585fd1033be79f3fd3ebd0ae6fe8f734) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a585fd1033be79f3fd3ebd0ae6fe8f734)  
  
virtual void | [Save](../../da/d51/classApp_1_1PropertyPlacement.html#ae1314101350bc9e76b9d692693c8e9e1) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#ae1314101350bc9e76b9d692693c8e9e1)  
  
void | [setPathValue](../../da/d51/classApp_1_1PropertyPlacement.html#a6d23bb97bf03cce4b60bc747167e5003) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, const boost::any &value) override  
| Set value of property.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a6d23bb97bf03cce4b60bc747167e5003)  
  
virtual void | [setPyObject](../../da/d51/classApp_1_1PropertyPlacement.html#a30868378554db499b38da470bfa520d7) ([PyObject](../../df/d1b/classPyObject.html) *) override  
void | [setValue](../../da/d51/classApp_1_1PropertyPlacement.html#abb1f46e80061be4669b0ca20c83a7b31) (const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) &pos)  
| Sets the property.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#abb1f46e80061be4669b0ca20c83a7b31)  
  
[bool](../../d9/db9/classbool.html) | [setValueIfChanged](../../da/d51/classApp_1_1PropertyPlacement.html#a9b73e52a783165d75383c7d80a1cc8fe) (const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) &pos, double tol=1e-7, double atol=1e-12)  
| Sets property only if changed.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a9b73e52a783165d75383c7d80a1cc8fe)  
  
virtual | [~PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a453210b1c733eadf3915efcc113b7f1c) ()  
| A destructor.
[More...](../../da/d51/classApp_1_1PropertyPlacement.html#a453210b1c733eadf3915efcc113b7f1c)  
  
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
  
  
##  Static Public Attributes  
  
---  
static const [Placement](../../d7/d32/classApp_1_1Placement.html) | [Null](../../da/d51/classApp_1_1PropertyPlacement.html#a9217eb51a6905360dd85f1459454e418)  
  
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

[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") representing a placement.

Encapsulates a [Base::Placement](../../d1/d10/classBase_1_1Placement.html "The
Placement class.") in a [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")

## Constructor & Destructor Documentation

## ◆ PropertyPlacement()

PropertyPlacement::PropertyPlacement  | ( | | ) |   
---|---|---|---|---  
  
A constructor.

A more elaborate description of the constructor.

Referenced by
[Copy()](../../da/d51/classApp_1_1PropertyPlacement.html#ae4fc87aa899e0a6cb40609b6307f661d).

## ◆ ~PropertyPlacement()

| PropertyPlacement::~PropertyPlacement  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyPlacement::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

References
[PropertyPlacement()](../../da/d51/classApp_1_1PropertyPlacement.html#a93f52f7245c2fe14411537e115f963e1).

## ◆ getEditorName()

| const char * App::PropertyPlacement::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

## ◆ getMemSize()

| virtual unsigned [int](../../d1/da0/classint.html) App::PropertyPlacement::getMemSize  | ( | void  | | ) |  const  
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

| void PropertyPlacement::getPaths  | ( | std::vector< [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > & | _paths_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Get valid paths for this property; used by auto completer.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a945f1c031f109242e362c5701516ff8e).

References
[App::ObjectIdentifier::SimpleComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a14c7ec6dc691f2c26f6df8386bd9db6d).

## ◆ getPathValue()

| const boost::any PropertyPlacement::getPathValue  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Get value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea).

References
[App::Property::getPathValue()](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea),
and
[Base::toDegrees()](../../db/d07/namespaceBase.html#a7656a834111b8ec3a4e1528ce0d3c058).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyPlacement::getPyObject  | ( | void  | | ) |   
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

| [bool](../../d9/db9/classbool.html) PropertyPlacement::getPyPathValue  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | ,   
---|---|---|---  
|  | Py::Object & |   
| ) | |  const  
overridevirtual  
  
Get Python value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a55400138b9f116fa42702ed36d0511b1).

References
[DraftVecUtils::angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
and
[Base::toDegrees()](../../db/d07/namespaceBase.html#a7656a834111b8ec3a4e1528ce0d3c058).

## ◆ getValue()

const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) & PropertyPlacement::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
This method returns a string representation of the property.

Referenced by
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[Import::ExportOCAF::createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[RobotGui::ViewProviderRobotObject::DraggerMotionCallback()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#ab57900054501852091b1b43c40febafb),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[Mesh::Sphere::execute()](../../d1/d57/classMesh_1_1Sphere.html#ae830b723d9c2977e6080c9e87f3ec139),
[Mesh::Ellipsoid::execute()](../../d2/dd6/classMesh_1_1Ellipsoid.html#aa7094fc5c9ce3b03b37b1875e8962b68),
[Mesh::Cylinder::execute()](../../df/def/classMesh_1_1Cylinder.html#a7f0a6253a8936e26fdd2794992f9cbb4),
[Mesh::Cone::execute()](../../d4/dbc/classMesh_1_1Cone.html#a23701269832147c5746476d7e6b3b8af),
[Mesh::Torus::execute()](../../de/da3/classMesh_1_1Torus.html#a9ca70ccb5548f0852b54fe55f58f27a9),
[Mesh::Cube::execute()](../../df/d68/classMesh_1_1Cube.html#a5c7921255a963127e0496b550023f3ed),
[Path::FeatureCompound::execute()](../../d2/d43/classPath_1_1FeatureCompound.html#a0db05b4845d8e9cf2dc1ab83a02a875b),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[App::GeoFeatureGroupExtension::extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[App::OriginGroupExtension::extensionGetSubObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[Part::Datum::getBasePoint()](../../db/d0b/classPart_1_1Datum.html#a616fe8e09f6a099b06a100535175c50c),
[PartDesign::Line::getDirection()](../../d0/d2a/classPartDesign_1_1Line.html#af89a81d14e0ccb27353122f43844600c),
[Part::Feature::getLocation()](../../d7/d7e/classPart_1_1Feature.html#a84164b4adfe9b6ecef87da8d7aa1ac9d),
[Part::FeatureReference::getLocation()](../../d2/da1/classPart_1_1FeatureReference.html#aee6f4d426e17d5a0193108fd06f7309c),
[PartDesign::Plane::getNormal()](../../df/df0/classPartDesign_1_1Plane.html#ad208270773ba2e063212171e36895e6e),
[Sketcher::SketchAnalysis::getOpenVertices()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#ab5e084231887ad48de90a03ec8aa3f62),
[PartDesign::Point::getPoint()](../../da/d0d/classPartDesign_1_1Point.html#a425bd8831010df262ca4482511fca22a),
[Part::Datum::getShape()](../../db/d0b/classPart_1_1Datum.html#ae9a416dc1bded6e9d81bdd7ae92540ca),
[Part::Datum::getSubObject()](../../db/d0b/classPart_1_1Datum.html#ac5c48627e7edd4fde0e66a86603a0ca8),
[Part::Feature::getSubObject()](../../d7/d7e/classPart_1_1Feature.html#adf8612028b19407896b5ba0e1fab0d5d),
[PartDesign::Body::getSubObject()](../../dd/db8/classPartDesign_1_1Body.html#aecc131a5ce7f03c5041a475003456b38),
[PartDesign::CoordinateSystem::getSubObject()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#aeb5d09866ebc21adafb8ee43acc9205b),
[PartDesign::SubShapeBinder::getSubObject()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#afb7e01deac9646afcd5dc1b2aa07042b),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[PartDesign::CoordinateSystem::getXAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a04498f548e650362eb2c094f89f5470b),
[PartDesign::CoordinateSystem::getYAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a38beb2d58454d7cb970b4dfb222fe8d3),
[PartDesign::CoordinateSystem::getZAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a4b9edd67bb7f8c895a9f5bd726fb92e2),
[PartDesign::ShapeBinder::hasPlacementChanged()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a6d80126d976410405532fabeced0feaa),
[Gui::ViewProviderLink::initDraggingPlacement()](../../d6/d59/classGui_1_1ViewProviderLink.html#a1386127ddc37cfa7078215b347149a71),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
[PartGui::Location::Location()](../../db/d6f/classPartGui_1_1Location.html#a2f77946d77e8f18590ccf3f7e73a18b4),
[Mesh::Feature::onChanged()](../../dd/dce/classMesh_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Points::Feature::onChanged()](../../d8/de3/classPoints_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Robot::RobotObject::onChanged()](../../db/d51/classRobot_1_1RobotObject.html#abebfe59d5888146a96594cb7d31ffce8),
[Part::Feature::onChanged()](../../d7/d7e/classPart_1_1Feature.html#a17178c5bf097534e84b20380ad13563b),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
[Part::Compound2::onDocumentRestored()](../../d5/dab/classPart_1_1Compound2.html#ac69720b1ba091dcdfac8b07ffbbf6048),
[PartDesign::DressUp::positionByBaseFeature()](../../df/de5/classPartDesign_1_1DressUp.html#ad0f7b71428ae5784d44e9a75f810ff3c),
[PartDesign::ProfileBased::positionByPrevious()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#acdddc3b78089a2b2dbd5c567998c9039),
[PartDesign::MultiTransform::positionBySupport()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a3d4f1facdf2a2ca1233b9e6e09ec7710),
[PartDesign::Transformed::positionBySupport()](../../dd/de1/classPartDesign_1_1Transformed.html#a99fa3cb882eea77aa22da310efdafdb7),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[PathGui::ViewProviderPath::recomputeBoundingBox()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a4a681a533fc16dba93a80bc3fdfc21c3),
[Robot::RobotObject::Restore()](../../db/d51/classRobot_1_1RobotObject.html#a654870e568b07840a79bd2c8e99e50d1),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Import::ExportOCAF::saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[RobotGui::ViewProviderRobotObject::setAxisTo()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#aed595606c9254fe301f2c69741204058),
[RobotGui::ViewProviderRobotObject::setDragger()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a7a94208ad67ec05ebc9013cac68d34f4),
[Gui::ViewProviderDragger::setEdit()](../../d3/d04/classGui_1_1ViewProviderDragger.html#ae112bfbf937f2ec8a8efd24fd432acc5),
[Gui::ViewProviderDragger::setEditViewer()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5746c8658c714b1910627ea804ca2353),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[RobotGui::TaskRobot6Axis::setRobot()](../../d8/d17/classRobotGui_1_1TaskRobot6Axis.html#a65d3953f8a1ba93524ac3e9cb3d73c0c),
[RobotGui::TaskTrajectory::setTo()](../../d1/da4/classRobotGui_1_1TaskTrajectory.html#a0635acee88443077361adc1cb529b6d2),
[RobotGui::TaskTrajectory::TaskTrajectory()](../../d1/da4/classRobotGui_1_1TaskTrajectory.html#aaf520e286c3dbc0e533b6c0252a9c0ec),
[RobotGui::TaskTrajectoryDressUpParameter::TaskTrajectoryDressUpParameter()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#a291e8c4303c14a45405f67a846976168),
[RobotGui::TrajectorySimulate::TrajectorySimulate()](../../d6/d2d/classRobotGui_1_1TrajectorySimulate.html#aff1b9df7981e9754bd422899e51b597d),
[App::GeoFeatureGroupExtension::transformPlacement()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#af259333fef3bdbc93a30be16d92c2953),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
[RobotGui::ViewProviderTrajectory::updateData()](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#a653032eb34a2fc66e326c0d0e9066287),
and
[PartDesign::ShapeBinder::updatedShape()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a126f8b03ab46e56d65b7fbd3d41b98e8).

## ◆ isSame()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyPlacement::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

## ◆ Paste()

| void PropertyPlacement::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
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

| void PropertyPlacement::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../da/d51/classApp_1_1PropertyPlacement.html#ae1314101350bc9e76b9d692693c8e9e1
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
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
and
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e).

Referenced by
[Part::AttachExtension::extHandleChangedPropertyName()](../../dc/d47/classPart_1_1AttachExtension.html#a660e1d33e4a6e9d23e2178b45395d9fe).

## ◆ Save()

| void PropertyPlacement::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ setPathValue()

| void PropertyPlacement::setPathValue  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | const boost::any & | _value_  
| ) | |   
overridevirtual  
  
Set value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22).

References
[App::Property::setPathValue()](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22),
and
[Base::toRadians()](../../db/d07/namespaceBase.html#a9d35925dcea870ab41e90d560f61bacf).

## ◆ setPyObject()

| void PropertyPlacement::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

References
[Base::Placement::fromMatrix()](../../d1/d10/classBase_1_1Placement.html#a4ddd9ad8b2ce05003b4cfe79b3c253df),
and
[setValue()](../../da/d51/classApp_1_1PropertyPlacement.html#abb1f46e80061be4669b0ca20c83a7b31).

Referenced by
[App::PropertyPlacementList::getPyValue()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a484851efa9ed5f430cc13d9a20c820b7).

## ◆ setValue()

void PropertyPlacement::setValue  | ( | const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) & | _pos_| ) |   
---|---|---|---|---|---  
  
Sets the property.

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

Referenced by
[RobotGui::ViewProviderRobotObject::DraggerMotionCallback()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#ab57900054501852091b1b43c40febafb),
[Part::Reverse::execute()](../../d4/d24/classPart_1_1Reverse.html#a22150a83fa78387e05f60dd1e08d31f8),
[PartDesign::ShapeBinder::execute()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a2886a69e9359a73fe242378c2a7b5a27),
[Mesh::Feature::onChanged()](../../dd/dce/classMesh_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Points::Feature::onChanged()](../../d8/de3/classPoints_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Robot::RobotObject::onChanged()](../../db/d51/classRobot_1_1RobotObject.html#abebfe59d5888146a96594cb7d31ffce8),
[Part::Feature::onChanged()](../../d7/d7e/classPart_1_1Feature.html#a17178c5bf097534e84b20380ad13563b),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
[Part::Compound2::onDocumentRestored()](../../d5/dab/classPart_1_1Compound2.html#ac69720b1ba091dcdfac8b07ffbbf6048),
[PartDesign::DressUp::positionByBaseFeature()](../../df/de5/classPartDesign_1_1DressUp.html#ad0f7b71428ae5784d44e9a75f810ff3c),
[PartDesign::ProfileBased::positionByPrevious()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#acdddc3b78089a2b2dbd5c567998c9039),
[Part::AttachExtension::positionBySupport()](../../dc/d47/classPart_1_1AttachExtension.html#acfee0e89764260b525e01995a6c947ab),
[PartDesign::MultiTransform::positionBySupport()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a3d4f1facdf2a2ca1233b9e6e09ec7710),
[PartDesign::Transformed::positionBySupport()](../../dd/de1/classPartDesign_1_1Transformed.html#a99fa3cb882eea77aa22da310efdafdb7),
[Robot::RobotObject::Restore()](../../db/d51/classRobot_1_1RobotObject.html#a654870e568b07840a79bd2c8e99e50d1),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[setPyObject()](../../da/d51/classApp_1_1PropertyPlacement.html#a30868378554db499b38da470bfa520d7),
[App::Origin::setupObject()](../../d9/d8b/classApp_1_1Origin.html#af5708fed01b27a82a33d8b06d02e89e6),
[setValueIfChanged()](../../da/d51/classApp_1_1PropertyPlacement.html#a9b73e52a783165d75383c7d80a1cc8fe),
[App::GeoFeatureGroupExtension::transformPlacement()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#af259333fef3bdbc93a30be16d92c2953),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
and
[RobotGui::TaskTrajectoryDressUpParameter::writeValues()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#a475203e163d2ff851526f84ef0e4011f).

## ◆ setValueIfChanged()

[bool](../../d9/db9/classbool.html) PropertyPlacement::setValueIfChanged  | ( | const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) & | _pos_ ,   
---|---|---|---  
|  | double  | _tol_ = `1e-7`,   
|  | double  | _atol_ = `1e-12`  
| ) | |   
  
Sets property only if changed.

Parameters

     pos| input placement   
---|---  
tol| position tolerance  
atol| angular tolerance  
  
References
[setValue()](../../da/d51/classApp_1_1PropertyPlacement.html#abb1f46e80061be4669b0ca20c83a7b31).

Referenced by
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f).

## Member Data Documentation

## ◆ Null

| const [Placement](../../d7/d32/classApp_1_1Placement.html)
App::PropertyPlacement::Null  
---  
static  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyGeo.h
  * FreeCAD/src/App/PropertyGeo.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

