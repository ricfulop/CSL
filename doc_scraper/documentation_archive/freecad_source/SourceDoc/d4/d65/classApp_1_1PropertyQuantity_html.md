---
url: https://freecad.github.io/SourceDoc/d4/d65/classApp_1_1PropertyQuantity.html
scraped_at: 2025-09-08T14:56:38.065933
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html)

[List of all members](../../d4/d6f/classApp_1_1PropertyQuantity-members.html) | Public Member Functions | Protected Member Functions

App::PropertyQuantity Class Reference

Float with Unit property This is a property for float with a predefined Unit
associated. [More...](../../d4/d65/classApp_1_1PropertyQuantity.html#details)

`#include <PropertyUnits.h>`

##  Public Member Functions  
  
---  
virtual const char * | [getEditorName](../../d4/d65/classApp_1_1PropertyQuantity.html#aca6dbdcb93d7a5800c0367974810fdf5) (void) const  
| Get the class name of the associated property editor item.
[More...](../../d4/d65/classApp_1_1PropertyQuantity.html#aca6dbdcb93d7a5800c0367974810fdf5)  
  
virtual const boost::any | [getPathValue](../../d4/d65/classApp_1_1PropertyQuantity.html#ae735a34c955df358ef20a0c70b7b5c97) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path) const  
| Get value of property.
[More...](../../d4/d65/classApp_1_1PropertyQuantity.html#ae735a34c955df358ef20a0c70b7b5c97)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d4/d65/classApp_1_1PropertyQuantity.html#af17e8d34d40a187543b30789adef4cc7) (void)  
| This method returns the Python wrapper for a C++ object.
[More...](../../d4/d65/classApp_1_1PropertyQuantity.html#af17e8d34d40a187543b30789adef4cc7)  
  
[Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) | [getQuantityValue](../../d4/d65/classApp_1_1PropertyQuantity.html#aa6023e0701e1890deeb98712ff37bd02) (void) const  
const [Base::Unit](../../d2/d37/classBase_1_1Unit.html) & | [getUnit](../../d4/d65/classApp_1_1PropertyQuantity.html#a8b965c3c89e7d1a63535f80e6b20ea4e) (void) const  
double | [getValue](../../d4/d65/classApp_1_1PropertyQuantity.html#a49df4b1070e01e10bef464cf672747c6) (void) const  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d4/d65/classApp_1_1PropertyQuantity.html#a223868a557555d8f3ea7e1eb647af452) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const  
| Compare if this property has the same content as the given one.
[More...](../../d4/d65/classApp_1_1PropertyQuantity.html#a223868a557555d8f3ea7e1eb647af452)  
  
|
[PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#af46f93de7de4746ca1eea0e7cabaa2c8)
(void)  
virtual void | [setPathValue](../../d4/d65/classApp_1_1PropertyQuantity.html#af017ce248b34f5378b3a714aa270c421) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, const boost::any &value)  
| Set value of property.
[More...](../../d4/d65/classApp_1_1PropertyQuantity.html#af017ce248b34f5378b3a714aa270c421)  
  
virtual void | [setPyObject](../../d4/d65/classApp_1_1PropertyQuantity.html#a72be43d71c5e5a5e0a174c01df176dc9) ([PyObject](../../df/d1b/classPyObject.html) *)  
void | [setUnit](../../d4/d65/classApp_1_1PropertyQuantity.html#a3d785d0e495642246354a3dcc4d6b8fb) (const [Base::Unit](../../d2/d37/classBase_1_1Unit.html) &u)  
void | [setValue](../../d4/d65/classApp_1_1PropertyQuantity.html#a3d2646f79d896325882adf321f2244e9) (double lValue)  
virtual | [~PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#ab4bb0e51360420ac96d3b0cd61256f73) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html)  
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
  
  
##  Protected Member Functions  
  
---  
[Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) | [createQuantityFromPy](../../d4/d65/classApp_1_1PropertyQuantity.html#a0b83c57020da799acbf3b702ffd63141) ([PyObject](../../df/d1b/classPyObject.html) *value)  
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

Float with Unit property This is a property for float with a predefined Unit
associated.

## Constructor & Destructor Documentation

## ◆ PropertyQuantity()

App::PropertyQuantity::PropertyQuantity  | ( | void  | | ) |   
---|---|---|---|---|---  
  
## ◆ ~PropertyQuantity()

| virtual App::PropertyQuantity::~PropertyQuantity  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ createQuantityFromPy()

| [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) PropertyQuantity::createQuantityFromPy  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
protected  
  
Referenced by
[setPyObject()](../../d4/d65/classApp_1_1PropertyQuantity.html#a72be43d71c5e5a5e0a174c01df176dc9),
and
[App::PropertyQuantityConstraint::setPyObject()](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#a299ac9ee7870f29d5c3640a14114fcbe).

## ◆ getEditorName()

| const char * PropertyQuantity::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a3a0dd8a67f208ac5a258ee5755b0cd33).

Reimplemented in
[App::PropertyQuantityConstraint](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#aa887d76bf141becf6238408ee1b1e64a),
and
[App::PropertyAngle](../../d1/d5d/classApp_1_1PropertyAngle.html#a696bab3cd50bef40c0f33aa62b6de163).

## ◆ getPathValue()

| const boost::any PropertyQuantity::getPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Get value of property.

Reimplemented from
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a429075152c75dbbd46e4bf5d7aeaac7d).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyQuantity::getPyObject  | ( | void  | | ) |   
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
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a5b0bcb3b6460df02b89fb8469b1738c9).

## ◆ getQuantityValue()

[Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) PropertyQuantity::getQuantityValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[PartGui::DlgPrimitives::DlgPrimitives()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a27827c66a9f047547fe0b7169251b97d),
[App::FunctionExpression::evalAggregate()](../../d6/da3/classApp_1_1FunctionExpression.html#ad9267dc1decdafaaa129f1bd51de07e4),
[PartDesignGui::TaskBoxPrimitives::onCylinderXSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a86d82d270b60a8432e7d0dde84c18faf),
[PartDesignGui::TaskBoxPrimitives::onCylinderYSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a73f5a1b7f5cd33180352b92a06b78d53),
[PartDesignGui::TaskBoxPrimitives::onPrismXSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a23b3eea757a08d4b2736fedb9c929066),
and
[PartDesignGui::TaskBoxPrimitives::onPrismYSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ab96618398004458953e2f5d0e1924d6a).

## ◆ getUnit()

const [Base::Unit](../../d2/d37/classBase_1_1Unit.html) & App::PropertyQuantity::getUnit  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[Spreadsheet::Cell::getFormattedQuantity()](../../d5/d22/classSpreadsheet_1_1Cell.html#a66a4fb5ffaa93232823dfbe49833ab7b),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
and
[Gui::ExpressionSpinBox::openFormulaDialog()](../../d7/d1b/classGui_1_1ExpressionSpinBox.html#a1d92694d4771392035736efe5c2f67b4).

## ◆ getValue()

double App::PropertyQuantity::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
References
[App::PropertyFloat::getValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#ae6c1d258b368a93c6fe4e6aa3f2a0842).

Referenced by
[PartDesignGui::TaskHelixParameters::apply()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#ac943cca36559194f55b17ffc2b2a91ac),
[Gui::InputField::bind()](../../da/dfa/classGui_1_1InputField.html#a17038da6cfd54acfc8f86b6597edb8a4),
[TechDraw::DrawViewPart::buildGeometryObject()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a859efd3dcccfd849656ff8b436ce6d58),
[TechDraw::DrawProjGroup::calculateAutomaticScale()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#af5bbe9c992fa0e9fc83461af6931f0e0),
[PartDesignGui::TaskHoleParameters::changedObject()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#af6c0941c01c80d87e2f97344958003be),
[Part::Extrusion::computeFinalParameters()](../../db/d6c/classPart_1_1Extrusion.html#a4b4ddc216eb6449e2b21480a430f5df8),
[PartGui::ViewProvider2DObjectGrid::createGrid()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a6872b82ce1aa46b6532e864681e262ae),
[Gui::PointMarker::customEvent()](../../d6/deb/classGui_1_1PointMarker.html#af3aff66aa9cfaaff337386e66a61c0f4),
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[TechDrawGui::QGILeaderLine::draw()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#ab20089120a1417e5a55af3e140e7acbd),
[TechDrawGui::QGIViewBalloon::drawBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6d26eb06a692339e02c1b57545903f29),
[TechDrawGui::QGIViewClip::drawClip()](../../d4/dcc/classTechDrawGui_1_1QGIViewClip.html#a272bbbc60a11ba7d9c687cff260df23d),
[TechDrawGui::QGIViewPart::drawHighlight()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#aac8834c3546b27902b1c3543d4a8e32e),
[TechDrawGui::QGIViewPart::drawPainterPath()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a7a2d4282b68e4e5e75149cc304943432),
[TechDrawGui::QGIViewSection::drawSectionFace()](../../d7/d73/classTechDrawGui_1_1QGIViewSection.html#a23b734cc85fce28a0a42c4d061686cb4),
[TechDrawGui::QGIViewPart::drawSectionLine()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a513e571f325b7c7cac09bdec0d1c512d),
[TechDrawGui::QGIViewPart::drawViewPart()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#add7c40ff3fc3fcc84308bb29225f8cc9),
[Mesh::Sphere::execute()](../../d1/d57/classMesh_1_1Sphere.html#ae830b723d9c2977e6080c9e87f3ec139),
[Mesh::Ellipsoid::execute()](../../d2/dd6/classMesh_1_1Ellipsoid.html#aa7094fc5c9ce3b03b37b1875e8962b68),
[Mesh::Cylinder::execute()](../../df/def/classMesh_1_1Cylinder.html#a7f0a6253a8936e26fdd2794992f9cbb4),
[Mesh::Cone::execute()](../../d4/dbc/classMesh_1_1Cone.html#a23701269832147c5746476d7e6b3b8af),
[Mesh::Torus::execute()](../../de/da3/classMesh_1_1Torus.html#a9ca70ccb5548f0852b54fe55f58f27a9),
[Mesh::Cube::execute()](../../df/d68/classMesh_1_1Cube.html#a5c7921255a963127e0496b550023f3ed),
[PartDesign::Pad::execute()](../../d9/d14/classPartDesign_1_1Pad.html#a17b37a5aaa299709fbb066564ef25b3e),
[PartDesign::Pocket::execute()](../../d1/d89/classPartDesign_1_1Pocket.html#aac791837d2ea389e30768f0fb6d25935),
[Part::Box::execute()](../../dc/d80/classPart_1_1Box.html#a69ab4139d085049cababf9b1692cf32d),
[Part::Circle::execute()](../../de/de4/classPart_1_1Circle.html#a5353d0accb2b7c67b656632ebc23952a),
[Part::Thickness::execute()](../../db/d73/classPart_1_1Thickness.html#a773b84ae5c846c3cfc1c099ab47887da),
[Part::Vertex::execute()](../../de/d96/classPart_1_1Vertex.html#a7f12d1239e070829c3743d2332687312),
[Part::Line::execute()](../../d3/dfe/classPart_1_1Line.html#a8a26cfef78179c3a17428b413ee487c8),
[Part::Plane::execute()](../../d0/d1c/classPart_1_1Plane.html#a92e30b6f8e6e4524886e10623f383ccf),
[Part::Sphere::execute()](../../dc/d57/classPart_1_1Sphere.html#aa2804abc812bb4e89a84ea2da733cb7a),
[Part::Ellipsoid::execute()](../../d4/dc8/classPart_1_1Ellipsoid.html#a1de2ad502eba83e4f20716aa3b81aced),
[Part::Cylinder::execute()](../../dd/d12/classPart_1_1Cylinder.html#abca3126f8a79336ae295c92cc4512e8d),
[Part::Prism::execute()](../../dc/d69/classPart_1_1Prism.html#aee3abdd806303810dee9bcb407871e8e),
[Part::RegularPolygon::execute()](../../d2/d69/classPart_1_1RegularPolygon.html#ab826050ea7815c765e6f0615554e01f0),
[Part::Cone::execute()](../../d2/d8f/classPart_1_1Cone.html#a9b18609878daf577bf7fd4cd4646ade0),
[Part::Torus::execute()](../../db/d42/classPart_1_1Torus.html#afcaa637ebac3164019e7dcb9bf15a800),
[Part::Helix::execute()](../../df/d49/classPart_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[Part::Spiral::execute()](../../d2/d3f/classPart_1_1Spiral.html#a3c18221bf2911fbbb3d36d7ace6e2215),
[Part::Wedge::execute()](../../d5/dc5/classPart_1_1Wedge.html#aaae12d496990fab3b982bbd54e79aa10),
[Part::Ellipse::execute()](../../d6/d22/classPart_1_1Ellipse.html#ac17650b02feac6d7001b52dad51c0803),
[PartDesign::Fillet::execute()](../../d0/d50/classPartDesign_1_1Fillet.html#a3d2e483fe0b72a9d09d5945fe7e36e65),
[PartDesign::Groove::execute()](../../d7/de3/classPartDesign_1_1Groove.html#a0f3365a4df79cd6d9ec8137b32c9530c),
[PartDesign::Helix::execute()](../../d3/d78/classPartDesign_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[PartDesign::Hole::execute()](../../dd/dd0/classPartDesign_1_1Hole.html#ad3161d80bf31dc136534283281a5b3ad),
[PartDesign::Box::execute()](../../df/d97/classPartDesign_1_1Box.html#a91f171c242cb7c31d3381981af2fab95),
[PartDesign::Cylinder::execute()](../../dc/d28/classPartDesign_1_1Cylinder.html#ab62f3f3e2d1c87dd9c4073378f2ca916),
[PartDesign::Sphere::execute()](../../db/d9d/classPartDesign_1_1Sphere.html#aeef6f98884ffd7532acd0274c29b1e8f),
[PartDesign::Cone::execute()](../../d4/d2b/classPartDesign_1_1Cone.html#a242c7c4d99e524f88ffca87982764ddf),
[PartDesign::Ellipsoid::execute()](../../d4/de1/classPartDesign_1_1Ellipsoid.html#abe018702f319a19bfd7faaba06b60109),
[PartDesign::Torus::execute()](../../dd/de1/classPartDesign_1_1Torus.html#a0fe8ad351f212fb151f6aab09438c4fd),
[PartDesign::Prism::execute()](../../d9/daf/classPartDesign_1_1Prism.html#afbe0d9e86e58c4781f3f58aed9371937),
[PartDesign::Wedge::execute()](../../dc/dd3/classPartDesign_1_1Wedge.html#aea929c12fd19cab20657b5dc80ced3ac),
[PartDesign::Revolution::execute()](../../d2/de6/classPartDesign_1_1Revolution.html#a1e5564f51ec710663a8002d5018b76f8),
[PartDesign::Thickness::execute()](../../d4/d22/classPartDesign_1_1Thickness.html#a773b84ae5c846c3cfc1c099ab47887da),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[PartDesign::Chamfer::execute()](../../da/d6f/classPartDesign_1_1Chamfer.html#a3fc5f1e2196c59afb44e876fd05d4710),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewMulti::execute()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a9d04a96ccac9fad6d125e478b91b7f30),
[PartDesign::Helix::generateHelixPath()](../../d3/d78/classPartDesign_1_1Helix.html#a04dd9590e1c0afe9dd3f1066ab9f0395),
[TechDrawGui::TaskDetail::getAnchorScene()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ac47e200bf1be3381e59b3c6c4610494d),
[TechDrawGui::QGILeaderLine::getAttachFromFeature()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#abe5ebf7cb3ea4310c9b8012b78605819),
[TechDraw::DrawLeaderLine::getAttachPoint()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a9261e3547b115ed0159d5255c9265aa7),
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686),
[TechDrawGui::TaskCenterLine::getCenterWidth()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a5a1caf08786b5e3c3e8f97f44cc74f9d),
[TechDraw::DrawViewDimension::getFormattedDimensionValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a92f36b1b5e044976e4a117424b000985),
[TechDraw::DrawViewDimension::getFormattedToleranceValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aac71dbd0561262809d791806fc44775d),
[TechDraw::DrawViewDimension::getFormattedToleranceValues()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a8235b120b82f24a29c6be38d6afff542),
[TechDraw::DrawSVGTemplate::getHeight()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a243f711bf0ed8c994942fa5c4e4851e2),
[TechDraw::DrawTemplate::getHeight()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a381c01cd744ce59ee41369a78dc6e9a0),
[TechDraw::DrawViewBalloon::getOrigin()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a9bb633e28d9dde87e273f8d56660167b),
[TechDraw::DrawViewBalloon::getOriginOffset()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a27905f37307418edb8330d322a83fc40),
[TechDraw::DrawViewAnnotation::getRect()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#a4e6ad66a92200e1f96748ea766163ce1),
[TechDraw::DrawViewClip::getRect()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#ac4c01aac638f31f6daba83dd15c21d6e),
[TechDraw::DrawProjGroup::getRect()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a453245d708f8e3998ed6ad4cb4d55a25),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[TechDraw::DrawSVGTemplate::getWidth()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a767c2827eefcf4278af3421d1e1f82e8),
[TechDraw::DrawTemplate::getWidth()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a09f7a8d7d7536a1bb1e4a384ad78d479),
[TechDraw::DrawProjGroup::getXYPosition()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aaeadc17847095c9f9d5ff6db786e04bd),
[TechDraw::DrawViewDimension::handleChangedPropertyType()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ae012f9df13a4f5578d96a5e50ccb1b2d),
[PartDesign::Helix::handleChangedPropertyType()](../../d3/d78/classPartDesign_1_1Helix.html#a9e6fc22b84b2f26eef4b4880af00b063),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[TechDraw::DrawViewBalloon::handleChangedPropertyType()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a71fe79a13079b298255b09846c9b6582),
[TechDraw::DrawViewDimension::hasOverUnderTolerance()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aaaa8ffab8600c2fb49f4e6cc42b8ff60),
[PartDesign::FeatureExtrude::hasTaperedAngle()](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a35c9fe97f5f373cdf91998dbfe8f3c82),
[TechDraw::DrawViewDimension::haveTolerance()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a23fb6a5052c6642d4bb60576868e25d7),
[PartGui::ViewProviderPartExt::loadParameter()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ac9b18640b083f65180c44c787ed4b240),
[TechDraw::DrawViewPart::makeGeometryForShape()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a3a32bd31e44e86739efc955a8bef4fde),
[Part::PrismExtension::makePrism()](../../d3/dbb/classPart_1_1PrismExtension.html#ab74dd7d421fc1cf531230b55c8313ca2),
[Gui::ViewProviderAnnotation::onChanged()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#a789aabe3e009284175581640dec663c3),
[Fem::FemPostSphereFunction::onChanged()](../../d5/dcb/classFem_1_1FemPostSphereFunction.html#abffccabdacd9cbbe6e61e799c8385c59),
[PartDesign::Hole::onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[TechDraw::DrawProjGroup::onChanged()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
[TechDrawGui::TaskDetail::onHighlightMoved()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a3381234d250275d524d73913667bbe23),
[TechDrawGui::TaskCosVertex::onTrackerFinished()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#a70cc99622328e6c5e42c84caec735981),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::Circle::Restore()](../../de/de4/classPart_1_1Circle.html#a31f09d03f0ee6b6f7a9e98b20b7223d4),
[Part::Ellipse::Restore()](../../d6/d22/classPart_1_1Ellipse.html#a90f7d460c9b3b2d2cf7b07282ad83efd),
[TechDrawGui::QGIView::rotateView()](../../d1/d99/classTechDrawGui_1_1QGIView.html#ae6adfc66b757fd59dd8a05055f9c8cb3),
[TechDrawGui::QGIViewAnnotation::rotateView()](../../d4/d5b/classTechDrawGui_1_1QGIViewAnnotation.html#ac95a43fc6179f77d0379cfeabb79a582),
[TechDrawGui::QGIViewImage::rotateView()](../../d9/ddb/classTechDrawGui_1_1QGIViewImage.html#a179005cbbacd254bec7f85797c160f9e),
[TechDrawGui::QGIViewSymbol::rotateView()](../../d1/da0/classTechDrawGui_1_1QGIViewSymbol.html#a93b2fef5c1c68a11763a7bf9602ef4f4),
[PartDesign::Helix::safePitch()](../../d3/d78/classPartDesign_1_1Helix.html#a85474d1c32f51cf49c0be48c600993eb),
[TechDrawGui::TaskProjGroup::saveGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#af012f644413f9c531a249a2fcb76d888),
[TechDrawGui::TaskLeaderLine::saveState()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a44043828f863d0b6365714da62ee59d1),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[TechDraw::DrawViewSection::sectionExec()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a79c8f60f63dd54684af4cad42f91ee4e),
[TechDraw::DrawViewSection::sectionLineEnds()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a4f8580c4dea1570bca8520f11f871ebe),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[TechDrawGui::ViewProviderPage::setGrid()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a31f4fdf0be6391e13a47115c059f69cd),
[TechDrawGui::QGILeaderLine::setLeaderFeature()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#a5d832bdd1e02595cd4cdfe8a16801bf1),
[TechDraw::DrawView::setPosition()](../../d6/d1c/classTechDraw_1_1DrawView.html#ae35a85434655d71af47e6a90cdf7388d),
[TechDrawGui::TaskLeaderLine::setUiEdit()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0eed6886711ee111f1ee0a8e314d6e21),
[TechDrawGui::TaskRichAnno::setUiEdit()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a3659e9cb13bc53ae36a3d7d16479d017),
[TechDrawGui::QGIViewBalloon::setViewPartFeature()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6f17a801836429d822e8998b0edfbff5),
[TechDrawGui::TaskBalloon::TaskBalloon()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#a21f34d1bf15390ec9c984c7c75ab9996),
[PartDesignGui::TaskBoxPrimitives::TaskBoxPrimitives()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aee4936dd78a78c4d0f6fcc168d1a9c13),
[TechDrawGui::TaskDimension::TaskDimension()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a01dec85a4db02858073f304508300ff3),
[PartDesignGui::TaskDraftParameters::TaskDraftParameters()](../../d6/d74/classPartDesignGui_1_1TaskDraftParameters.html#aafff6d5bd22406878791e8ccad20b907),
[PartDesignGui::TaskFilletParameters::TaskFilletParameters()](../../db/d91/classPartDesignGui_1_1TaskFilletParameters.html#a6d39adf6b643a77ee3cecf31cdac126d),
[PartDesignGui::TaskHoleParameters::TaskHoleParameters()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#aed07ebf7cad6b7cff0c7597137c91662),
[TechDrawGui::TaskLeaderLine::TaskLeaderLine()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a873d04472b6a0de7f250ac13eef14913),
[TechDrawGui::TaskProjGroup::TaskProjGroup()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a81c03636578c0dd7befcb158dd86bc28),
[PartDesignGui::TaskRevolutionParameters::TaskRevolutionParameters()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#a5509b04d5cfc1da7d5314c4a038a01e2),
[TechDrawGui::TaskRichAnno::TaskRichAnno()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#acfd26140dce1c41560c4391c78b2fb06),
[SketcherGui::TaskSketcherGeneral::TaskSketcherGeneral()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#acb35aefc057b31af4b7c6e9c87e1f0d4),
[PartDesignGui::TaskThicknessParameters::TaskThicknessParameters()](../../de/d75/classPartDesignGui_1_1TaskThicknessParameters.html#a43c1b021112c8995623c941d9d59a5ef),
[RobotGui::TaskTrajectoryDressUpParameter::TaskTrajectoryDressUpParameter()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#a291e8c4303c14a45405f67a846976168),
[PartGui::ThicknessWidget::ThicknessWidget()](../../d5/d25/classPartGui_1_1ThicknessWidget.html#aa0023d59e7ac0b3735f1fbd0c5019a8a),
[PartDesignGui::ViewProviderAddSub::updateAddSubShapeIndicator()](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#a27d23424ce72a0f362904d73928fbc6c),
[ImageGui::ViewProviderImagePlane::updateData()](../../db/d5a/classImageGui_1_1ViewProviderImagePlane.html#ae91df03af7efab412ed649b8db50463e),
[PartDesignGui::ViewProviderDatumLine::updateData()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a7ebcf854d3c32486f47eb377a39f4fa7),
[PartDesignGui::ViewProviderDatumPlane::updateData()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a0a10ea46fffce183ae92074bd2c6d754),
[TechDrawGui::QGIView::updateView()](../../d1/d99/classTechDrawGui_1_1QGIView.html#a6881a2f1863f810acf1ca4728ddcf32d),
and
[PartGui::ViewProviderPartExt::updateVisual()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a96cb6b96c8dfb082a135a31c4f554167).

## ◆ isSame()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyQuantity::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a386b26cdbb4e26dfd8e6340d3bb9ca5e).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

## ◆ setPathValue()

| void PropertyQuantity::setPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | const boost::any & | _value_  
| ) | |   
virtual  
  
Set value of property.

Reimplemented from
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#ac5c0dfec5810e2860c64bb7186b2462a).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::anyToQuantity()](../../dd/dc2/namespaceApp.html#a93c04feddbea432de5b61b5851b914de),
and
[setValue()](../../d4/d65/classApp_1_1PropertyQuantity.html#a3d2646f79d896325882adf321f2244e9).

## ◆ setPyObject()

| void PropertyQuantity::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf2edab1753863426d8b78dd15dab006).

Reimplemented in
[App::PropertyQuantityConstraint](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#a299ac9ee7870f29d5c3640a14114fcbe).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[createQuantityFromPy()](../../d4/d65/classApp_1_1PropertyQuantity.html#a0b83c57020da799acbf3b702ffd63141),
[Base::Quantity::getUnit()](../../d8/d18/classBase_1_1Quantity.html#acf401f989cc46b7c864565e89113ede4),
[Base::Quantity::getValue()](../../d8/d18/classBase_1_1Quantity.html#a692b9e4043999d2c24737886639df7d0),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
and
[App::PropertyFloat::setValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#aeb4937e13aff58a04f81fdadf544f7d9).

## ◆ setUnit()

void App::PropertyQuantity::setUnit  | ( | const [Base::Unit](../../d2/d37/classBase_1_1Unit.html) & | _u_| ) |   
---|---|---|---|---|---  
  
Referenced by
[PartDesign::Chamfer::Chamfer()](../../da/d6f/classPartDesign_1_1Chamfer.html#a75b4114d662ce32435766510a7daef43),
[TechDraw::DrawViewDimension::DrawViewDimension()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aa6fad2118f8e0478d358978ef57e2dc4),
[App::FeatureTest::FeatureTest()](../../df/dea/classApp_1_1FeatureTest.html#a71e331e5bda8a32669e0da873fb28c31),
[PartDesign::Fillet::Fillet()](../../d0/d50/classPartDesign_1_1Fillet.html#a92e209863666263c8d36c82a3c7fed15),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewDimension::onDocumentRestored()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a899ec15c087cd8a0c38e05fda6f4a647),
and
[Spreadsheet::Sheet::setQuantityProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a1200f02d91cc685af952ac5c7d369010).

## ◆ setValue()

void App::PropertyQuantity::setValue  | ( | double  | _lValue_| ) |   
---|---|---|---|---|---  
  
References
[App::PropertyFloat::setValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#aeb4937e13aff58a04f81fdadf544f7d9).

Referenced by
[TechDraw::DrawProjGroupItem::autoPosition()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#aed7c8d696a4a2b4f3a172ebc3789cbf7),
[TechDrawGui::TaskRichAnno::createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[TechDrawGui::QGSPage::createBalloon()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#afa6582dc212925fd365ed71b38127d78),
[App::MeasureDistance::execute()](../../d7/d61/classApp_1_1MeasureDistance.html#aa328f58f37764c36e03ee8356325ea72),
[PartDesign::Helix::execute()](../../d3/d78/classPartDesign_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[TechDraw::DrawViewDimension::handleChangedPropertyType()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ae012f9df13a4f5578d96a5e50ccb1b2d),
[Mesh::Sphere::handleChangedPropertyType()](../../d1/d57/classMesh_1_1Sphere.html#af43262e6edb32fd6dcd686d877728c3a),
[Part::Thickness::handleChangedPropertyType()](../../db/d73/classPart_1_1Thickness.html#a013b39370d11b7cb467ed7223d33d7a9),
[PartDesign::Helix::handleChangedPropertyType()](../../d3/d78/classPartDesign_1_1Helix.html#a9e6fc22b84b2f26eef4b4880af00b063),
[TechDraw::DrawViewAnnotation::handleChangedPropertyType()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#adb0aa91e33022736bcb8d124cd9b295b),
[TechDrawGui::ViewProviderBalloon::handleChangedPropertyType()](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a4a6246398d610494e2171cbbb1b8eb44),
[TechDrawGui::ViewProviderDimension::handleChangedPropertyType()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a3ca6d7598ea8430e71e0f852c349b339),
[TechDrawGui::ViewProviderLeader::handleChangedPropertyType()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9f55c50ca1618be5224195b46784c99b),
[TechDrawGui::ViewProviderRichAnno::handleChangedPropertyType()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a2b7fcb5bb4cd203d5d467e29142523a3),
[TechDrawGui::ViewProviderViewPart::handleChangedPropertyType()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a1dbd73f06f25bca49644056da29aa920),
[TechDraw::DrawProjGroup::handleChangedPropertyType()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a9a45f879e7b7c0cc6a6787be1c021f46),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[TechDraw::DrawViewBalloon::handleChangedPropertyType()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a71fe79a13079b298255b09846c9b6582),
[PartGui::ViewProviderPartExt::loadParameter()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ac9b18640b083f65180c44c787ed4b240),
[PartDesignGui::TaskBoxPrimitives::onBoxHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a107f8b74cdb3bf1a45ed032a9aaf383d),
[PartDesignGui::TaskBoxPrimitives::onBoxLengthChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#abf84392ef886c69cd8a222960378acc5),
[PartDesignGui::TaskBoxPrimitives::onBoxWidthChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa371979bffbc04a3a8e1ad0a927cef13),
[PartDesign::Hole::onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[TechDraw::DrawProjGroup::onChanged()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[PartDesignGui::TaskBoxPrimitives::onConeAngleChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a7728be961d4a469c0fcb7ec45aeb20af),
[PartDesignGui::TaskBoxPrimitives::onConeHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a436d997cc5ea0b81530da2cb38c1ca35),
[PartDesignGui::TaskBoxPrimitives::onConeRadius1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa3ee11ef5378be9cb7953ddc8f7a584d),
[PartDesignGui::TaskBoxPrimitives::onConeRadius2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a1fa0b97630162d71685b15ea1f566a50),
[PartDesignGui::TaskBoxPrimitives::onCylinderAngleChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a059ada94b80ad3d590e7d4a876873fd1),
[PartDesignGui::TaskBoxPrimitives::onCylinderHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a145b7ffb358a2329d635d9241f8fa33e),
[PartDesignGui::TaskBoxPrimitives::onCylinderRadiusChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a50f3f9f57898d01184274ec84003fe24),
[PartDesignGui::TaskBoxPrimitives::onCylinderXSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a86d82d270b60a8432e7d0dde84c18faf),
[PartDesignGui::TaskBoxPrimitives::onCylinderYSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a73f5a1b7f5cd33180352b92a06b78d53),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidAngle1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a9d43a4073114d3c77de0c3e83548e2c1),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidAngle2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a0fbf7eea3dc32497b8711a646862a8c1),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidAngle3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a73425d913722a9494da32e334929c6d5),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidRadius1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a46c8bb8b6d9f426492b669c354baea99),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidRadius2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#accbe8caafcb8faa22c9c7553aa3fda23),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidRadius3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a35f2c2ddfe3b72affe6fb4545fab11e4),
[PartDesignGui::TaskBoxPrimitives::onPrismCircumradiusChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a8701cee98cd45d672cffe4010a21ba56),
[PartDesignGui::TaskBoxPrimitives::onPrismHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ab037232d561cffcd013f608ed88ce79f),
[PartDesignGui::TaskBoxPrimitives::onPrismXSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a23b3eea757a08d4b2736fedb9c929066),
[PartDesignGui::TaskBoxPrimitives::onPrismYSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ab96618398004458953e2f5d0e1924d6a),
[SketcherGui::TaskSketcherGeneral::onSetGridSize()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#ab9354aa968807a2ca71f8a881164f409),
[PartDesignGui::TaskBoxPrimitives::onSphereAngle1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa5bfc9f1b87ced6adf49875eba7e90a2),
[PartDesignGui::TaskBoxPrimitives::onSphereAngle2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a27858521e805c7390d3f9039c535cdcf),
[PartDesignGui::TaskBoxPrimitives::onSphereAngle3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aea9a6950dd79c79bd8cb360b2b8c8784),
[PartDesignGui::TaskBoxPrimitives::onSphereRadiusChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a72d9233055fc77ee491dbc8f5587c09c),
[PartDesignGui::TaskBoxPrimitives::onTorusAngle1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ae2e874e2dad51362fd1a56aff1ba6880),
[PartDesignGui::TaskBoxPrimitives::onTorusAngle2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a600166782c2b17052d6236a2406a1439),
[PartDesignGui::TaskBoxPrimitives::onTorusAngle3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a5a528983f97adab406c5123f6474f620),
[PartDesignGui::TaskBoxPrimitives::onTorusRadius1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a10c0def5dec5ab5ea0c5705f8cf5768a),
[PartDesignGui::TaskBoxPrimitives::onTorusRadius2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ac449268708c99e4c2f03997e3f9553be),
[PartDesignGui::TaskBoxPrimitives::onWedgeX2maxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a1f13f84786f7ef305f26838d9f7e2081),
[PartDesignGui::TaskBoxPrimitives::onWedgeX2minChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a86463e53d3b0a78c4080b51ba415c388),
[PartDesignGui::TaskBoxPrimitives::onWedgeXmaxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a66204103a06869337ca64985a9b8d6dc),
[PartDesignGui::TaskBoxPrimitives::onWedgeXminChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa5c59aeea355f23727b8bdd8d1a515e5),
[PartDesignGui::TaskBoxPrimitives::onWedgeYmaxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#af07f3d7a82a59fdbfa665ddd905c3be5),
[PartDesignGui::TaskBoxPrimitives::onWedgeYminChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa6fe7277dd6ab536363d7954a7d8c84b),
[PartDesignGui::TaskBoxPrimitives::onWedgeZ2maxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#af872884d5d9ecf66a5767b3ab9635383),
[PartDesignGui::TaskBoxPrimitives::onWedgeZ2minChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a57934914e027c65459bd684f13251463),
[PartDesignGui::TaskBoxPrimitives::onWedgeZmaxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa944b296adfac1bcf2f85eaa84b36e89),
[PartDesignGui::TaskBoxPrimitives::onWedgeZminChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a23f1c00dbdb3b7bbc85dc9728096fcc4),
[TechDraw::DrawSVGTemplate::processTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a9b2032d4f9db58231ae4ad79ca5b3778),
[PartDesign::Helix::proposeParameters()](../../d3/d78/classPartDesign_1_1Helix.html#a278b5c14eacce6ed801c4722006744d9),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::Circle::Restore()](../../de/de4/classPart_1_1Circle.html#a31f09d03f0ee6b6f7a9e98b20b7223d4),
[Part::Ellipse::Restore()](../../d6/d22/classPart_1_1Ellipse.html#a90f7d460c9b3b2d2cf7b07282ad83efd),
[TechDrawGui::TaskProjGroup::restoreGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a348f413a63a7fd86ebf8978fee5d028f),
[TechDrawGui::TaskLeaderLine::restoreState()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a119496553ef9c0aa3c285685dbc202ff),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[TechDraw::DrawViewBalloon::setOrigin()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a4976c3df5bccf5549523c6960c912624),
[setPathValue()](../../d4/d65/classApp_1_1PropertyQuantity.html#af017ce248b34f5378b3a714aa270c421),
[TechDraw::DrawView::setPosition()](../../d6/d1c/classTechDraw_1_1DrawView.html#ae35a85434655d71af47e6a90cdf7388d),
[Spreadsheet::Sheet::setQuantityProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a1200f02d91cc685af952ac5c7d369010),
[TechDrawGui::TaskProjGroup::spacingChanged()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a898e358b0ef66513b1b38788aa5374ec),
[TechDrawGui::TaskRichAnno::updateAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#adc9c72650392178995bfd8adf6344831),
[TechDrawGui::TaskLeaderLine::updateLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0797a29d0a4ef849d5643c1ed982acb2),
and
[RobotGui::TaskTrajectoryDressUpParameter::writeValues()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#a475203e163d2ff851526f84ef0e4011f).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyUnits.h
  * FreeCAD/src/App/PropertyUnits.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

