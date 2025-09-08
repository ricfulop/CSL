---
url: https://freecad.github.io/SourceDoc/d4/df2/classApp_1_1PropertyEnumeration.html
scraped_at: 2025-09-08T14:55:40.804826
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html)

[List of all members](../../db/d5a/classApp_1_1PropertyEnumeration-members.html) | Public Member Functions

App::PropertyEnumeration Class Reference

[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") wrapper around an
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.") object.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#details)

`#include <PropertyStandard.h>`

##  Public Member Functions  
  
---  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d4/df2/classApp_1_1PropertyEnumeration.html#a716562a2a85ac80ba5672855ed1364b0) (void) const  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a716562a2a85ac80ba5672855ed1364b0)  
  
const char * | [getEditorName](../../d4/df2/classApp_1_1PropertyEnumeration.html#a34911d749d232ae75515883964b6cc4b) (void) const  
| Get the class name of the associated property editor item.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a34911d749d232ae75515883964b6cc4b)  
  
const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) & | [getEnum](../../d4/df2/classApp_1_1PropertyEnumeration.html#ac81c577b97c17913a6908c0167964aa8) (void) const  
| Returns [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.") object.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#ac81c577b97c17913a6908c0167964aa8)  
  
std::vector< std::string > | [getEnumVector](../../d4/df2/classApp_1_1PropertyEnumeration.html#ab98d3234da7219edb03d55e0bda87cb3) (void) const  
| get all possible enum values as vector of strings
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#ab98d3234da7219edb03d55e0bda87cb3)  
  
virtual const boost::any | [getPathValue](../../d4/df2/classApp_1_1PropertyEnumeration.html#a84463f3456e11890c7e3061dc1592a74) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &) const  
| Get value of property.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a84463f3456e11890c7e3061dc1592a74)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d4/df2/classApp_1_1PropertyEnumeration.html#a0ec441a65e99e532943b16cc889214dd) (void)  
| This method returns the Python wrapper for a C++ object.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a0ec441a65e99e532943b16cc889214dd)  
  
virtual [bool](../../d9/db9/classbool.html) | [getPyPathValue](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1cf1f360d2873e83ce77ce6cf97f8322) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, Py::Object &r) const  
| Get Python value of property.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1cf1f360d2873e83ce77ce6cf97f8322)  
  
long | [getValue](../../d4/df2/classApp_1_1PropertyEnumeration.html#af97fd601b63a723fca0e6c8c02635fe4) (void) const  
| Returns current value of the enumeration as an integer.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#af97fd601b63a723fca0e6c8c02635fe4)  
  
const char * | [getValueAsString](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae19cdd746f7271aa737c0cbe47197690) (void) const  
| get the value as string
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae19cdd746f7271aa737c0cbe47197690)  
  
[bool](../../d9/db9/classbool.html) | [hasEnums](../../d4/df2/classApp_1_1PropertyEnumeration.html#aeeb0045bba218b1846b1ca92d317a0b2) () const  
| get the pointer to the enum list
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#aeeb0045bba218b1846b1ca92d317a0b2)  
  
[bool](../../d9/db9/classbool.html) | [isPartOf](../../d4/df2/classApp_1_1PropertyEnumeration.html#abc6a7716d982c075d736196f2fb3e2bd) (const char *value) const  
| checks if a string is included in the enumeration
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#abc6a7716d982c075d736196f2fb3e2bd)  
  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d4/df2/classApp_1_1PropertyEnumeration.html#a516c0ea146e0da67db130812b58f5e49) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const  
| Compare if this property has the same content as the given one.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a516c0ea146e0da67db130812b58f5e49)  
  
[bool](../../d9/db9/classbool.html) | [isValid](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae3687462586d34e96fcf655314af1ca8) (void) const  
| Returns true if the instance is in a usable state.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae3687462586d34e96fcf655314af1ca8)  
  
[bool](../../d9/db9/classbool.html) | [isValue](../../d4/df2/classApp_1_1PropertyEnumeration.html#a26894afd907692c6ec2a6bc74078a1e8) (const char *value) const  
| checks if the property is set to a certain string value
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a26894afd907692c6ec2a6bc74078a1e8)  
  
virtual void | [Paste](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae2c1a5b1f45a128b3a82bcab504a7d52) (const [Property](../../d0/da9/classApp_1_1Property.html) &from)  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae2c1a5b1f45a128b3a82bcab504a7d52)  
  
|
[PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a3c201ec3de9000a4aa7c01d4450e23df)
()  
| Standard constructor.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a3c201ec3de9000a4aa7c01d4450e23df)  
  
|
[PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a31c28dc8fdc0b27402f09458773ffa07)
(const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) &e)  
| Obvious constructor.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a31c28dc8fdc0b27402f09458773ffa07)  
  
virtual void | [Restore](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c)  
  
virtual void | [Save](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4cf9cdfd4e14e6901973762b7b47a663) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4cf9cdfd4e14e6901973762b7b47a663)  
  
void | [setEditorName](../../d4/df2/classApp_1_1PropertyEnumeration.html#a8475851879a38feaf8c5c25669135749) (const char *name)  
void | [setEnums](../../d4/df2/classApp_1_1PropertyEnumeration.html#a5571099202eda6dacf748996eedf6551) (const char **plEnums)  
| [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.") methods.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a5571099202eda6dacf748996eedf6551)  
  
void | [setEnums](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1e2e4a75ad2d728cc6c1a23f8d2244c5) (const std::vector< std::string > &Enums)  
| setting the enumaration string as vector of strings This makes the
enumeration custom.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1e2e4a75ad2d728cc6c1a23f8d2244c5)  
  
void | [setEnumVector](../../d4/df2/classApp_1_1PropertyEnumeration.html#a265272a98d0ae08006973d863d9aba9d) (const std::vector< std::string > &)  
| set enum values as vector of strings
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a265272a98d0ae08006973d863d9aba9d)  
  
virtual void | [setPathValue](../../d4/df2/classApp_1_1PropertyEnumeration.html#a48af9a6606d16a14476ee19bd9cc28cc) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, const boost::any &value)  
| Set value of property.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a48af9a6606d16a14476ee19bd9cc28cc)  
  
virtual void | [setPyObject](../../d4/df2/classApp_1_1PropertyEnumeration.html#aa715a8742ad95f4288e987f2f20d4719) ([PyObject](../../df/d1b/classPyObject.html) *)  
virtual [bool](../../d9/db9/classbool.html) | [setPyPathValue](../../d4/df2/classApp_1_1PropertyEnumeration.html#a34a90320cbad71fd49bded88a1ca37ff) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, const Py::Object &value)  
void | [setValue](../../d4/df2/classApp_1_1PropertyEnumeration.html#a10973c61a7072bba34df37062aaa266d) (const char *value)  
| set the enum by a string is slower than
[setValue(long)](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4827d5cd0791e28e17fb22f7b6ce8371
"set directly the enum value In DEBUG checks for boundaries.").
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a10973c61a7072bba34df37062aaa266d)  
  
void | [setValue](../../d4/df2/classApp_1_1PropertyEnumeration.html#aa721dd1b7fac0ff886e9f66b9574357f) (const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) &source)  
| Setter using [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.").
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#aa721dd1b7fac0ff886e9f66b9574357f)  
  
void | [setValue](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4827d5cd0791e28e17fb22f7b6ce8371) (long)  
| set directly the enum value In DEBUG checks for boundaries.
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4827d5cd0791e28e17fb22f7b6ce8371)  
  
virtual | [~PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a8122d14088db1127ba05e604411865cc) ()  
| destructor
[More...](../../d4/df2/classApp_1_1PropertyEnumeration.html#a8122d14088db1127ba05e604411865cc)  
  
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

[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") wrapper around an
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.") object.

## Constructor & Destructor Documentation

## ◆ PropertyEnumeration() [1/2]

PropertyEnumeration::PropertyEnumeration  | ( | | ) |   
---|---|---|---|---  
  
Standard constructor.

Referenced by
[Copy()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a716562a2a85ac80ba5672855ed1364b0).

## ◆ PropertyEnumeration() [2/2]

PropertyEnumeration::PropertyEnumeration  | ( | const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) & | _e_| ) |   
---|---|---|---|---|---  
  
Obvious constructor.

## ◆ ~PropertyEnumeration()

| PropertyEnumeration::~PropertyEnumeration  | ( | | ) |   
---|---|---|---|---  
virtual  
  
destructor

## Member Function Documentation

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyEnumeration::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

References
[PropertyEnumeration()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a3c201ec3de9000a4aa7c01d4450e23df).

## ◆ getEditorName()

| const char * App::PropertyEnumeration::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

## ◆ getEnum()

const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) & PropertyEnumeration::getEnum  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Returns [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.") object.

Referenced by
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12).

## ◆ getEnumVector()

std::vector< std::string > PropertyEnumeration::getEnumVector  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
get all possible enum values as vector of strings

Referenced by
[PartDesignGui::TaskHoleParameters::changedObject()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#af6c0941c01c80d87e2f97344958003be),
[Save()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4cf9cdfd4e14e6901973762b7b47a663),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[PartDesignGui::TaskHoleParameters::TaskHoleParameters()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#aed07ebf7cad6b7cff0c7597137c91662),
and
[FemGui::TaskPostBox::updateEnumerationList()](../../dc/d51/classFemGui_1_1TaskPostBox.html#a4e76081ba79f5c1702744d08957b2f07).

## ◆ getPathValue()

| const boost::any PropertyEnumeration::getPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Get value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea).

References
[getPyPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1cf1f360d2873e83ce77ce6cf97f8322),
[getValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#af97fd601b63a723fca0e6c8c02635fe4),
[getValueAsString()](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae19cdd746f7271aa737c0cbe47197690),
and
[App::pyObjectToAny()](../../dd/dc2/namespaceApp.html#ac51cca1568f7ffd55146499492ae1700).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyEnumeration::getPyObject  | ( | void  | | ) |   
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

References
[getValueAsString()](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae19cdd746f7271aa737c0cbe47197690).

## ◆ getPyPathValue()

| [bool](../../d9/db9/classbool.html) PropertyEnumeration::getPyPathValue  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | ,   
---|---|---|---  
|  | Py::Object & |   
| ) | |  const  
virtual  
  
Get Python value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a55400138b9f116fa42702ed36d0511b1).

References
[App::PropertyString::getPyObject()](../../dd/df8/classApp_1_1PropertyString.html#aa6e72d76ecb8d448e1e8016f72f0dd66),
[getValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#af97fd601b63a723fca0e6c8c02635fe4),
[getValueAsString()](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae19cdd746f7271aa737c0cbe47197690),
and
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

Referenced by
[getPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a84463f3456e11890c7e3061dc1592a74).

## ◆ getValue()

long PropertyEnumeration::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Returns current value of the enumeration as an integer.

Referenced by
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[PartDesignGui::TaskChamferParameters::apply()](../../d1/d5d/classPartDesignGui_1_1TaskChamferParameters.html#a25ef9333841ebe6ef78a1faa9fa48e8d),
[PartDesignGui::TaskHelixParameters::apply()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#ac943cca36559194f55b17ffc2b2a91ac),
[PartDesignGui::TaskHoleParameters::changedObject()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#af6c0941c01c80d87e2f97344958003be),
[SurfaceGui::GeomFillSurface::changeFillType()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#aa2180cd7b8c690d2addc40f808eefafc),
[PartDesign::SubShapeBinder::checkCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3698bc706a89765ff35db75048a08698),
[Part::Extrusion::computeFinalParameters()](../../db/d6c/classPart_1_1Extrusion.html#a4b4ddc216eb6449e2b21480a430f5df8),
[PartGui::ViewProvider2DObjectGrid::createGrid()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a6872b82ce1aa46b6532e864681e262ae),
[PartGui::DlgPrimitives::DlgPrimitives()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a27827c66a9f047547fe0b7169251b97d),
[TechDrawGui::QGIViewDimension::drawAngle()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a27c4e7cb613ec0563614d25f802cf6e9),
[TechDrawGui::QGIViewBalloon::drawBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6d26eb06a692339e02c1b57545903f29),
[TechDrawGui::QGIViewDimension::drawDiameter()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4f99cea83cd1e147dee58d5e4d2c9a65),
[TechDrawGui::QGIViewDimension::drawDistance()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a9ca8dc402df9510b7e7537bac4a53e5b),
[Gui::ViewProviderAnnotationLabel::drawImage()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a37530affd46043649525097fa5ff8e05),
[TechDrawGui::QGIViewDimension::drawRadius()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#ab82446f086e3e9ecda97fa4e7f933562),
[Fem::FemMeshShapeNetgenObject::execute()](../../d9/df4/classFem_1_1FemMeshShapeNetgenObject.html#ad38e08d369e0a9c44588e98bc5ffb3ed),
[Fem::FemPostScalarClipFilter::execute()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a0aa1f4898cacdd829920492771a3931b),
[Fem::FemPostWarpVectorFilter::execute()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#abfd97dfc34d290355149f487d5c93f66),
[Fem::FemPostPipeline::execute()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a37a7074a69af004117f82d72be1701f8),
[Part::RuledSurface::execute()](../../d1/d41/classPart_1_1RuledSurface.html#aaff86f64ccc1eeeb1158727285cacab0),
[Part::Sweep::execute()](../../df/dc6/classPart_1_1Sweep.html#a7fdf28d346eb1b3b838ed0dea5bb40d8),
[Part::Thickness::execute()](../../db/d73/classPart_1_1Thickness.html#a773b84ae5c846c3cfc1c099ab47887da),
[Part::Helix::execute()](../../df/d49/classPart_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[PartDesign::Helix::execute()](../../d3/d78/classPartDesign_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[PartDesign::Pipe::execute()](../../da/d61/classPartDesign_1_1Pipe.html#a860c1038a89156936a4d1fd44481cfbd),
[PartDesign::Thickness::execute()](../../d4/d22/classPartDesign_1_1Thickness.html#a773b84ae5c846c3cfc1c099ab47887da),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[Part::Offset::execute()](../../d0/dda/classPart_1_1Offset.html#a342f29a6b5381db240304b9384b313dd),
[Part::Offset2D::execute()](../../d7/dcf/classPart_1_1Offset2D.html#a3eb29bb0e6404263cb3470d7ec24ea4a),
[PartDesign::Chamfer::execute()](../../da/d6f/classPartDesign_1_1Chamfer.html#a3fc5f1e2196c59afb44e876fd05d4710),
[PartDesign::SubShapeBinder::execute()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ae9fb1ae7a1f62e3c44879de5f6f752a9),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[Part::AttachExtension::extensionOnChanged()](../../dc/d47/classPart_1_1AttachExtension.html#ac73db2d8f32ca41b89157b47edce44c1),
[Gui::ViewProviderLink::finishRestoring()](../../d6/d59/classGui_1_1ViewProviderLink.html#ab68540420e3d18c69df6944e857fa198),
[PathGui::ViewProviderPath::getBoundColor()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a98a3ef4085a9babf25db6f74aa95bdc0),
[Surface::GeomFillSurface::getFillingStyle()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a0aa833e8618fee2e77e3ce53eab49b25),
[getPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a84463f3456e11890c7e3061dc1592a74),
[getPyPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1cf1f360d2873e83ce77ce6cf97f8322),
[PartDesign::ProfileBased::getSupportFace()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a021db5d3d85698ee0d5a4f8d8a4391a5),
[TechDrawGui::QGILeaderLine::makeLeaderPath()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#a0e58599dd22e5be45969ff2847d43522),
[PartDesign::Chamfer::mustExecute()](../../da/d6f/classPartDesign_1_1Chamfer.html#a3f61714b5aa58b68ccb2ac3f0fed02c9),
[Gui::ViewProviderAnnotation::onChanged()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#a789aabe3e009284175581640dec663c3),
[Fem::FemPostScalarClipFilter::onChanged()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a6c5243b230b4dac2cde71f28d04dcd53),
[Fem::FemPostWarpVectorFilter::onChanged()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a64c913cbc86feb708504b94b931f1085),
[Fem::FemPostPipeline::onChanged()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a333b47057bc9b7691cc0c9db9b0c79ba),
[MeshGui::ViewProviderMesh::onChanged()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae9ec71d871b59be4a532fb2be2cb8d52),
[PartDesign::Line::onChanged()](../../d0/d2a/classPartDesign_1_1Line.html#a9da12fed7c1a5cfa4af5c06af23c6fff),
[PartDesign::Plane::onChanged()](../../df/df0/classPartDesign_1_1Plane.html#a82dfdf47875b49263a5275ab1ff3c686),
[PartDesign::Helix::onChanged()](../../d3/d78/classPartDesign_1_1Helix.html#a8f7d2c5809cd60f90231a0350ea5c444),
[PartDesign::Hole::onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[PathGui::ViewProviderPath::onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[PointsGui::ViewProviderPoints::onChanged()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ad91786e290cd4be69ef99a41c85faa32),
[Gui::ViewProviderDocumentObject::onChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[Gui::ViewProviderLink::onChanged()](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartDesign::SubShapeBinder::onChanged()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a525834748579d35e2e8ecbf9cd18bf3d),
[PartDesignGui::ViewProviderBody::onChanged()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922),
[PartDesignGui::ViewProviderBoolean::onChanged()](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#ab446d9f6494af864bd745136c7e20439),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewDimension::onDocumentRestored()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a899ec15c087cd8a0c38e05fda6f4a647),
[Part::AttachExtension::onExtendedDocumentRestored()](../../dc/d47/classPart_1_1AttachExtension.html#a6af7f6139ae7d3aef649ff3e89d05d75),
[Gui::ElementColors::Private::Private()](../../d8/dc9/classElementColors_1_1Private.html#a666b8d911912be6e8e346fcb52592125),
[Restore()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c),
[PartDesign::Helix::safePitch()](../../d3/d78/classPartDesign_1_1Helix.html#a85474d1c32f51cf49c0be48c600993eb),
[TechDrawGui::TaskSectionView::saveSectionState()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a6766d05bef0b8b54751ef23c124d3eb2),
[TechDrawGui::QGILeaderLine::setArrows()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#a8417ba60730341eefd086ac79b6f77ee),
[PartDesignGui::ViewProviderBody::setDisplayMode()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a685366158948c29702fd282bc927fd25),
[SurfaceGui::GeomFillSurface::setEditedObject()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#a5347666bfd43a7cbea08d4c179e33f5d),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[PartDesignGui::ViewProviderBody::setOverrideMode()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ac0025966b6885197861269fee3a65e60),
[TechDrawGui::TaskSectionView::setUiEdit()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a43dc3542cf896d0778a028ae2be230ce),
[TechDrawGui::TaskLeaderLine::setUiEdit()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0eed6886711ee111f1ee0a8e314d6e21),
[TechDrawGui::TaskRichAnno::setUiEdit()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a3659e9cb13bc53ae36a3d7d16479d017),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[TechDrawGui::TaskSectionView::setUiPrimary()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a07485a3822d8c672d6e4580fe4bf858c),
[PartDesign::Pipe::setupAlgorithm()](../../da/d61/classPartDesign_1_1Pipe.html#aee88e3fe184997d50ac86c9f99b113f2),
[PartDesign::SubShapeBinder::setupCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3f0c1dcf0ed5800b1865c2c42f4e25f7),
[PartGui::TaskAttacher::TaskAttacher()](../../df/d45/classPartGui_1_1TaskAttacher.html#ae3b7e331323f8a005efc1e55579240a6),
[TechDrawGui::TaskBalloon::TaskBalloon()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#a21f34d1bf15390ec9c984c7c75ab9996),
[PartDesignGui::TaskBooleanParameters::TaskBooleanParameters()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#afee7fbe402fa60d00581ce385bc8cb3c),
[TechDrawGui::TaskDimension::TaskDimension()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a01dec85a4db02858073f304508300ff3),
[PartDesignGui::TaskHoleParameters::TaskHoleParameters()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#aed07ebf7cad6b7cff0c7597137c91662),
[PartDesignGui::TaskPipeOrientation::TaskPipeOrientation()](../../d8/df3/classPartDesignGui_1_1TaskPipeOrientation.html#ac6d362fde0b1452a942b513494180d97),
[PartDesignGui::TaskPipeParameters::TaskPipeParameters()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#ad8be386ff75b6d3c414ffbe505e48561),
[PartDesignGui::TaskPipeScaling::TaskPipeScaling()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#abec20e41dadf8a6f7e257d83647df874),
[TechDrawGui::TaskProjGroup::TaskProjGroup()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a81c03636578c0dd7befcb158dd86bc28),
[FemGui::TaskTetParameter::TaskTetParameter()](../../d9/d36/classFemGui_1_1TaskTetParameter.html#a29dc9ca508fcde30e91d9b0e306b34ce),
[PartDesignGui::TaskThicknessParameters::TaskThicknessParameters()](../../de/d75/classPartDesignGui_1_1TaskThicknessParameters.html#a43c1b021112c8995623c941d9d59a5ef),
[RobotGui::TaskTrajectoryDressUpParameter::TaskTrajectoryDressUpParameter()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#a291e8c4303c14a45405f67a846976168),
[PartGui::ThicknessWidget::ThicknessWidget()](../../d5/d25/classPartGui_1_1ThicknessWidget.html#aa0023d59e7ac0b3735f1fbd0c5019a8a),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
[Part::AttachExtension::updateAttacherVals()](../../dc/d47/classPart_1_1AttachExtension.html#ab8238095f03465efa5d39c205299c5af),
[PartDesignGui::ViewProviderDatumLine::updateData()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a7ebcf854d3c32486f47eb377a39f4fa7),
[PartDesignGui::ViewProviderDatumPlane::updateData()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a0a10ea46fffce183ae92074bd2c6d754),
[FemGui::TaskPostBox::updateEnumerationList()](../../dc/d51/classFemGui_1_1TaskPostBox.html#a4e76081ba79f5c1702744d08957b2f07),
[PartDesign::Chamfer::updateProperties()](../../da/d6f/classPartDesign_1_1Chamfer.html#ae0070da00a2612084082be5bef23e63b),
[TechDrawGui::TaskProjGroup::updateTask()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a169cab4630d6743fbe22ba80c96235d4),
and
[PathGui::ViewProviderPath::useNewSelectionModel()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac4369bd741dd06af6966ed030a18d363).

## ◆ getValueAsString()

const char * PropertyEnumeration::getValueAsString  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
get the value as string

Referenced by
[FemGui::TaskDlgFemConstraintFluidBoundary::accept()](../../da/d17/classFemGui_1_1TaskDlgFemConstraintFluidBoundary.html#a92106711f12fb0fb783c7e411d8f3923),
[TechDraw::DrawProjGroup::arrangeViewPointers()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a8a8bdca0831ea0e16e664ad17f0a04f8),
[TechDraw::DrawProjGroupItem::autoPosition()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#aed7c8d696a4a2b4f3a172ebc3789cbf7),
[PartDesignGui::TaskHoleParameters::changedObject()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#af6c0941c01c80d87e2f97344958003be),
[TechDrawGui::QGIViewDimension::draw()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a5a804977a329425219739213bc82ec70),
[TechDrawGui::QGIViewBalloon::drawBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6d26eb06a692339e02c1b57545903f29),
[TechDraw::DrawProjGroup::dumpISO()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a64c8445dbe972e26619f07afbe560a6f),
[Fem::FemPostScalarClipFilter::execute()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a0aa1f4898cacdd829920492771a3931b),
[Fem::FemPostWarpVectorFilter::execute()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#abfd97dfc34d290355149f487d5c93f66),
[PartDesign::Hole::execute()](../../dd/dd0/classPartDesign_1_1Hole.html#ad3161d80bf31dc136534283281a5b3ad),
[PartDesign::Boolean::execute()](../../d2/d81/classPartDesign_1_1Boolean.html#a471715716cd89abfe18b9f50b7728567),
[PartDesign::Helix::generateHelixPath()](../../d3/d78/classPartDesign_1_1Helix.html#a04dd9590e1c0afe9dd3f1066ab9f0395),
[TechDraw::DrawPage::getPageOrientation()](../../d9/d5a/classTechDraw_1_1DrawPage.html#acfcfcccb6fbd3ebc861e8c7ffd06d301),
[getPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a84463f3456e11890c7e3061dc1592a74),
[getPyObject()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a0ec441a65e99e532943b16cc889214dd),
[getPyPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1cf1f360d2873e83ce77ce6cf97f8322),
[FemGui::TaskFemConstraintFluidBoundary::getTurbulenceModel()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a3d22e4e08d8df5e7b297b03ab9b81521),
[TechDraw::DrawProjGroup::getViewIndex()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a92924eedc2c197844d6012d822d0bb7b),
[TechDraw::DrawViewSection::getXDirection()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a0cefd62711bac9ca360a2ffc37731820),
[TechDrawGui::QGIProjGroup::itemChange()](../../db/d20/classTechDrawGui_1_1QGIProjGroup.html#aa1611210aac32505ffac13b3c321ba65),
[Fem::ConstraintFluidBoundary::onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Fem::ConstraintTransform::onChanged()](../../d8/d3c/classFem_1_1ConstraintTransform.html#a38b893dee34272ad6bf0c6126aad561f),
[Fem::FemPostScalarClipFilter::onChanged()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a6c5243b230b4dac2cde71f28d04dcd53),
[Fem::FemPostWarpVectorFilter::onChanged()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a64c913cbc86feb708504b94b931f1085),
[PartDesign::Hole::onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[PartDesignGui::ViewProviderBody::onChanged()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922),
[TechDrawGui::ViewProviderProjGroupItem::onDelete()](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#ac4f0ad8f27db7108aaf102177217d998),
[TechDraw::DrawProjGroup::purgeProjections()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a59234a939935212324d52d31af4c479b),
[TechDrawGui::TaskProjGroup::saveGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#af012f644413f9c531a249a2fcb76d888),
[TechDrawGui::TaskSectionView::saveSectionState()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a6766d05bef0b8b54751ef23c124d3eb2),
[Gui::ViewProviderDocumentObject::setActiveMode()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a680b6d8d00fa1135eee59edbda9f3bd0),
[Fem::FemPostScalarClipFilter::setConstraintForField()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#acae0657dd2705f0c3aafa2284bbe2d2e),
[setEnums()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1e2e4a75ad2d728cc6c1a23f8d2244c5),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[FemGui::TaskFemConstraintHeatflux::TaskFemConstraintHeatflux()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a8e9e2cb04cc453f24e9d3ea5794cacc1),
[FemGui::TaskFemConstraintTemperature::TaskFemConstraintTemperature()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a33195abb4e64b5b8c79d39c7423d0a22),
[FemGui::TaskFemConstraintTransform::TaskFemConstraintTransform()](../../d9/d9b/classFemGui_1_1TaskFemConstraintTransform.html#aa2ff547501a5af38276cce0666c1920c),
[PartDesignGui::TaskHoleParameters::TaskHoleParameters()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#aed07ebf7cad6b7cff0c7597137c91662),
[TechDrawGui::TaskSectionView::TaskSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a8aa3d86a98175927e7dd69b2eea5b82e),
[TechDraw::DrawProjGroupItem::unsetupObject()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a74c1e831d9704f99007d0b9398001f90),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintTransform::updateData()](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#a2adf8aba7f15f7b95399068ab39c47b8),
[TechDrawGui::ViewProviderProjGroupItem::updateData()](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#aa193f03d76fb1ecdf199186e888354ce),
[TechDraw::DrawProjGroup::usedProjectionType()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a34227f080eebfad29b97318c09c59dc3),
and
[Gui::PropertyEditor::PropertyEnumItem::value()](../../d1/dd0/classGui_1_1PropertyEditor_1_1PropertyEnumItem.html#a94427cf59c1c81076fda89e8f9f0dd7f).

## ◆ hasEnums()

[bool](../../d9/db9/classbool.html) PropertyEnumeration::hasEnums  | ( | | ) |  const  
---|---|---|---|---  
  
get the pointer to the enum list

## ◆ isPartOf()

[bool](../../d9/db9/classbool.html) PropertyEnumeration::isPartOf  | ( | const char *  | _value_| ) |  const  
---|---|---|---|---|---  
  
checks if a string is included in the enumeration

## ◆ isSame()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyEnumeration::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

## ◆ isValid()

[bool](../../d9/db9/classbool.html) PropertyEnumeration::isValid  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Returns true if the instance is in a usable state.

Referenced by
[PartDesign::Hole::onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[Gui::ViewProviderDocumentObject::setActiveMode()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a680b6d8d00fa1135eee59edbda9f3bd0),
and
[Gui::PropertyEditor::PropertyEnumItem::value()](../../d1/dd0/classGui_1_1PropertyEditor_1_1PropertyEnumItem.html#a94427cf59c1c81076fda89e8f9f0dd7f).

## ◆ isValue()

[bool](../../d9/db9/classbool.html) PropertyEnumeration::isValue  | ( | const char *  | _value_| ) |  const  
---|---|---|---|---|---  
  
checks if the property is set to a certain string value

Referenced by
[TechDraw::DrawProjGroup::arrangeViewPointers()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a8a8bdca0831ea0e16e664ad17f0a04f8),
[TechDraw::DrawView::checkScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#ad2da2acbc02345e15a55d357ef545914),
[TechDraw::DrawProjGroup::execute()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a53036ad3632d51fe082b67c8f829b54f),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDraw::DrawViewPart::execute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[TechDraw::DrawViewDimension::getPrefix()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a5556000b2fe9425f2abe2c87066426c0),
[TechDraw::DrawView::getScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#afc22d0aa3cc132a6c14323a50082ab1e),
[TechDraw::DrawProjGroup::getViewIndex()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a92924eedc2c197844d6012d822d0bb7b),
[TechDraw::DrawViewDimension::isMultiValueSchema()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ad8d876c061bedc8250001349758b1d4d),
[TechDraw::DrawProjGroup::onChanged()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[TechDraw::DrawView::onChanged()](../../d6/d1c/classTechDraw_1_1DrawView.html#a2980fbae4ce0a12aae609193764465cf),
[TechDraw::DrawViewDetail::onChanged()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewSection::onChanged()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[TechDraw::DrawView::prefScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#afc0e7db7510d676055bc131cffc0b59c),
[TechDrawGui::TaskProjGroup::scaleManuallyChanged()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a40ff243eaf44f2528b05976f21fd4f67),
[TechDraw::DrawView::setScaleAttribute()](../../d6/d1c/classTechDraw_1_1DrawView.html#a2027c216e3dc8f25f5c40a6b465decf9),
[TechDrawGui::TaskDimension::TaskDimension()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a01dec85a4db02858073f304508300ff3),
[TechDrawGui::TaskProjGroup::TaskProjGroup()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a81c03636578c0dd7befcb158dd86bc28),
[TechDraw::DrawView::validateScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#ab9bb446a2ce1a400ffe1aa00daf6cdd0),
and
[TechDrawGui::TaskProjGroup::viewToggled()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a53e5f0d366028da306ce2a74f96b0c14).

## ◆ Paste()

| void PropertyEnumeration::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
virtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be).

References
[setValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a10973c61a7072bba34df37062aaa266d).

## ◆ Restore()

| void PropertyEnumeration::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4cf9cdfd4e14e6901973762b7b47a663
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
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[getValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#af97fd601b63a723fca0e6c8c02635fe4),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[Base::XMLReader::readEndElement()](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3),
and
[Base::ConsoleSingleton::Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

Referenced by
[TechDraw::DrawViewBalloon::handleChangedPropertyName()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a8f43bff2ef5b6712e7fd0546b639e6ef).

## ◆ Save()

| void PropertyEnumeration::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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
[Base::Writer::decInd()](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92),
[Base::Persistence::encodeAttribute()](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec),
[getEnumVector()](../../d4/df2/classApp_1_1PropertyEnumeration.html#ab98d3234da7219edb03d55e0bda87cb3),
[Base::Writer::incInd()](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5),
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ setEditorName()

void App::PropertyEnumeration::setEditorName  | ( | const char *  | _name_| ) |   
---|---|---|---|---|---  
  
## ◆ setEnums() [1/2]

void PropertyEnumeration::setEnums  | ( | const char **  | _plEnums_| ) |   
---|---|---|---|---|---  
  
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.") methods.

These all function as per documentation in
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.") setting the enumaration string list The list is a
NULL terminated array of pointers to a const char* string

const char enums[] = {"Black","White","Other",NULL}

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::Property::getFullName()](../../d0/da9/classApp_1_1Property.html#a0b1289a60e57856c8dae70fafd619dd2),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
and
[femsolver.signal::notify()](../../dc/de2/group__FEM.html#ga6389100f2d948a9fe194b395ac11f82c).

Referenced by
[Gui::ViewProviderDocumentObject::attach()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a915f1f11451e769f91b1137d1527fc57),
[PartDesign::Boolean::Boolean()](../../d2/d81/classPartDesign_1_1Boolean.html#ac032e9c86b0a2605c320402f47850319),
[PartDesign::Chamfer::Chamfer()](../../da/d6f/classPartDesign_1_1Chamfer.html#a75b4114d662ce32435766510a7daef43),
[Fem::ConstraintFluidBoundary::ConstraintFluidBoundary()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#ad0ba55c936b2e15550d2fe8732f7be41),
[Fem::ConstraintHeatflux::ConstraintHeatflux()](../../de/dce/classFem_1_1ConstraintHeatflux.html#a58583bd2f3380a6d5acc8bc860e19f50),
[Fem::ConstraintTemperature::ConstraintTemperature()](../../d7/dff/classFem_1_1ConstraintTemperature.html#a7f0bb60b27a35ad74b1de63d3e6d9c14),
[Fem::ConstraintTransform::ConstraintTransform()](../../d8/d3c/classFem_1_1ConstraintTransform.html#ad457f6edd3a6dea3252906be279d3924),
[TechDraw::DrawPage::DrawPage()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a47a086fa134ba2f9e4f6a8121cb25ad2),
[TechDraw::DrawTemplate::DrawTemplate()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#aa9a3d6a604d36d22e11073c8be44f772),
[TechDraw::DrawViewAnnotation::DrawViewAnnotation()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#ab1f6da36b5eea808ba75ea9f8bfe9bb5),
[TechDraw::DrawViewArch::DrawViewArch()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#ae8ba2850a690702279c1ffb5df5ea908),
[TechDraw::DrawViewBalloon::DrawViewBalloon()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a2aa449f36b009ff5a461c4702bbe22cb),
[TechDraw::DrawViewDimension::DrawViewDimension()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aa6fad2118f8e0478d358978ef57e2dc4),
[Part::Extrusion::Extrusion()](../../db/d6c/classPart_1_1Extrusion.html#a3f19cb349b395a336ba3e31c193038a0),
[App::FeatureTest::FeatureTest()](../../df/dea/classApp_1_1FeatureTest.html#a71e331e5bda8a32669e0da873fb28c31),
[Fem::FemMeshShapeNetgenObject::FemMeshShapeNetgenObject()](../../d9/df4/classFem_1_1FemMeshShapeNetgenObject.html#a701aacc418c9f1b3891c2aa533924172),
[Fem::FemPostPipeline::FemPostPipeline()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a013df85decd5bb27524d67b7b8d51eb5),
[Surface::GeomFillSurface::GeomFillSurface()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#ab26e20277f9fbd57449dd019c3c027b9),
[Part::Helix::Helix()](../../df/d49/classPart_1_1Helix.html#af5b3edc469728ac5981e35e29412b61c),
[PartDesign::Helix::Helix()](../../d3/d78/classPartDesign_1_1Helix.html#af5b3edc469728ac5981e35e29412b61c),
[PartDesign::Hole::Hole()](../../dd/dd0/classPartDesign_1_1Hole.html#a4c1598e38f425df417a962a8fe1f8f30),
[Fem::ConstraintFluidBoundary::onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[PartDesign::Hole::onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[Part::RuledSurface::RuledSurface()](../../d1/d41/classPart_1_1RuledSurface.html#a4970a87f24e3d157b5fa7e31d7ba5bed),
[App::LinkBaseExtension::setProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770),
[Robot::TrajectoryDressUpObject::TrajectoryDressUpObject()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#acc30335ea8304b1d2df3cb67295d4474),
[PartDesignGui::ViewProviderBoolean::ViewProviderBoolean()](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#accb99f2dc304e0aec6d077bad7e4b48c),
[TechDrawGui::ViewProviderLeader::ViewProviderLeader()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a138a6a73f5f86c9ea59deec4d925ebe5),
[Gui::ViewProviderLink::ViewProviderLink()](../../d6/d59/classGui_1_1ViewProviderLink.html#ac80b32ec9821edd74f1e39d58951773d),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
[TechDrawGui::ViewProviderRichAnno::ViewProviderRichAnno()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#aa9e7ef3ef91f11afa7845443982c7943),
[TechDrawGui::ViewProviderViewPart::ViewProviderViewPart()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#aa788186aa3b1edf4937b903368b9a626),
and
[Gui::ViewProviderDocumentObject::~ViewProviderDocumentObject()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#af764f01205eb1475038ec1b302cd9b35).

## ◆ setEnums() [2/2]

void PropertyEnumeration::setEnums  | ( | const std::vector< std::string > & | _Enums_| ) |   
---|---|---|---|---|---  
  
setting the enumaration string as vector of strings This makes the enumeration
custom.

References
[getValueAsString()](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae19cdd746f7271aa737c0cbe47197690),
[setEnumVector()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a265272a98d0ae08006973d863d9aba9d),
and
[setValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a10973c61a7072bba34df37062aaa266d).

## ◆ setEnumVector()

void PropertyEnumeration::setEnumVector  | ( | const std::vector< std::string > & | _values_| ) |   
---|---|---|---|---|---  
  
set enum values as vector of strings

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::Property::getFullName()](../../d0/da9/classApp_1_1Property.html#a0b1289a60e57856c8dae70fafd619dd2),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
and
[femsolver.signal::notify()](../../dc/de2/group__FEM.html#ga6389100f2d948a9fe194b395ac11f82c).

Referenced by
[setEnums()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1e2e4a75ad2d728cc6c1a23f8d2244c5).

## ◆ setPathValue()

| void PropertyEnumeration::setPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | const boost::any & | _value_  
| ) | |   
virtual  
  
Set value of property.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22).

References
[App::pyObjectFromAny()](../../dd/dc2/namespaceApp.html#a0fd92b74207e681fd5b4a27a5c70f0c0),
[setPyObject()](../../d4/df2/classApp_1_1PropertyEnumeration.html#aa715a8742ad95f4288e987f2f20d4719),
and
[setValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a10973c61a7072bba34df37062aaa266d).

## ◆ setPyObject()

| void PropertyEnumeration::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::Property::getFullName()](../../d0/da9/classApp_1_1Property.html#a0b1289a60e57856c8dae70fafd619dd2),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

Referenced by
[setPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a48af9a6606d16a14476ee19bd9cc28cc),
and
[setPyPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a34a90320cbad71fd49bded88a1ca37ff).

## ◆ setPyPathValue()

| [bool](../../d9/db9/classbool.html) PropertyEnumeration::setPyPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | const Py::Object & | _value_  
| ) | |   
virtual  
  
References
[setPyObject()](../../d4/df2/classApp_1_1PropertyEnumeration.html#aa715a8742ad95f4288e987f2f20d4719).

## ◆ setValue() [1/3]

void PropertyEnumeration::setValue  | ( | const char *  | _value_| ) |   
---|---|---|---|---|---  
  
set the enum by a string is slower than
[setValue(long)](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4827d5cd0791e28e17fb22f7b6ce8371
"set directly the enum value In DEBUG checks for boundaries.").

Use long if possible

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

Referenced by
[Gui::ViewProviderDocumentObject::attach()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a915f1f11451e769f91b1137d1527fc57),
[SurfaceGui::GeomFillSurface::changeFillType()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#aa2180cd7b8c690d2addc40f808eefafc),
[PartDesign::SubShapeBinder::checkCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3698bc706a89765ff35db75048a08698),
[TechDrawGui::TaskLeaderLine::commonFeatureUpdate()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a7f87ec13ec1881fa82e9c9a0493c604a),
[TechDraw::DrawViewArch::DrawViewArch()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#ae8ba2850a690702279c1ffb5df5ea908),
[Gui::ElementColors::ElementColors()](../../db/d21/classGui_1_1ElementColors.html#a7d0d5836a9361c145408b75cf8b0b33c),
[Fem::FemPostScalarClipFilter::execute()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a0aa1f4898cacdd829920492771a3931b),
[Fem::FemPostWarpVectorFilter::execute()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#abfd97dfc34d290355149f487d5c93f66),
[TechDrawGui::ViewProviderLeader::handleChangedPropertyType()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9f55c50ca1618be5224195b46784c99b),
[TechDrawGui::ViewProviderRichAnno::handleChangedPropertyType()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a2b7fcb5bb4cd203d5d467e29142523a3),
[Part::Part2DObject::handleChangedPropertyType()](../../d9/d57/classPart_1_1Part2DObject.html#a3b4551d03504c25446ede14dcf2309e3),
[PartDesignGui::TaskFeaturePick::makeCopy()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a9e9b1a639025522ada407aaa6b19596e),
[Fem::ConstraintFluidBoundary::onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDrawGui::TaskDetail::onScaleTypeEdit()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#aaf0c48b11d118f0fb2a3ac2fcf661409),
[Paste()](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae2c1a5b1f45a128b3a82bcab504a7d52),
[TechDraw::DrawSVGTemplate::processTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a9b2032d4f9db58231ae4ad79ca5b3778),
[TechDrawGui::TaskProjGroup::projectionTypeChanged()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a81ab26f8c5a6b8a0aed58753142f8d7b),
[PartDesign::Plane::Restore()](../../df/df0/classPartDesign_1_1Plane.html#a0daddf322de5233314e8ec1e5d73f658),
[TechDrawGui::TaskProjGroup::restoreGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a348f413a63a7fd86ebf8978fee5d028f),
[TechDrawGui::TaskSectionView::restoreSectionState()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a31ebe04f8add6f5d1c665c9b7c12c238),
[TechDrawGui::TaskProjGroup::scaleTypeChanged()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#ae8aa2696c9c438de8e953eee7ada9b9c),
[setEnums()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1e2e4a75ad2d728cc6c1a23f8d2244c5),
[setPathValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a48af9a6606d16a14476ee19bd9cc28cc),
[TechDrawGui::TaskRichAnno::updateAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#adc9c72650392178995bfd8adf6344831),
[TechDrawGui::TaskLeaderLine::updateLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0797a29d0a4ef849d5643c1ed982acb2),
[TechDraw::DrawView::validateScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#ab9bb446a2ce1a400ffe1aa00daf6cdd0),
[PartDesignGui::ViewProviderDatumCoordinateSystem::ViewProviderDatumCoordinateSystem()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a53832f895c08903546a696bd6e667100),
[PointsGui::ViewProviderPoints::ViewProviderPoints()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ac5af34ec9fcf964cf09f3f7eaee50fca),
[RobotGui::TaskTrajectoryDressUpParameter::writeValues()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#a475203e163d2ff851526f84ef0e4011f),
and
[Gui::ElementColors::Private::~Private()](../../d8/dc9/classElementColors_1_1Private.html#a2c4c4d93a333c6965b204a1955cc190d).

## ◆ setValue() [2/3]

void PropertyEnumeration::setValue  | ( | const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) & | _source_| ) |   
---|---|---|---|---|---  
  
Setter using [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.").

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

## ◆ setValue() [3/3]

void PropertyEnumeration::setValue  | ( | long  | _value_| ) |   
---|---|---|---|---|---  
  
set directly the enum value In DEBUG checks for boundaries.

Is faster than using [setValue(const
char*)](../../d4/df2/classApp_1_1PropertyEnumeration.html#a10973c61a7072bba34df37062aaa266d
"set the enum by a string is slower than setValue\(long\).").

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

