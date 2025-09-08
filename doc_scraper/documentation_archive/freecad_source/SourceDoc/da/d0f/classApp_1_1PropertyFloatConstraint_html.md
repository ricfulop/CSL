---
url: https://freecad.github.io/SourceDoc/da/d0f/classApp_1_1PropertyFloatConstraint.html
scraped_at: 2025-09-08T14:55:48.811395
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyFloatConstraint](../../da/d0f/classApp_1_1PropertyFloatConstraint.html)

[List of all members](../../d7/de4/classApp_1_1PropertyFloatConstraint-members.html) | Classes | Public Member Functions

App::PropertyFloatConstraint Class Reference

Constraint float properties This property fulfills the need of a constraint
float.
[More...](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#details)

`#include <PropertyStandard.h>`

##  Classes  
  
---  
struct | [Constraints](../../db/dfe/structApp_1_1PropertyFloatConstraint_1_1Constraints.html)  
| Constraint methods.
[More...](../../db/dfe/structApp_1_1PropertyFloatConstraint_1_1Constraints.html#details)  
  
  
##  Public Member Functions  
  
---  
const [Constraints](../../db/dfe/structApp_1_1PropertyFloatConstraint_1_1Constraints.html) * | [getConstraints](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a523e414a4e5df9d9a6c96d75423c1c4a) (void) const  
| get the constraint struct
[More...](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a523e414a4e5df9d9a6c96d75423c1c4a)  
  
virtual const char * | [getEditorName](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a3f5130569b81c7c30f8dbd32bd687061) (void) const  
| Get the class name of the associated property editor item.
[More...](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a3f5130569b81c7c30f8dbd32bd687061)  
  
double | [getMaximum](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#abbacf28d098e5e0f5e34556a83a6c293) () const  
double | [getMinimum](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a3abe6c5fbbf7bdf15d90922c3a96087a) () const  
double | [getStepSize](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a1e96b272b0429d34e7adcd8edc782c91) () const  
|
[PropertyFloatConstraint](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#adef6de9aeecdeb8dd76c4e13cb550930)
(void)  
| Value Constructor Construct with explicit Values.
[More...](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#adef6de9aeecdeb8dd76c4e13cb550930)  
  
void | [setConstraints](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a2f80258285396a1a90d9c4466c615088) (const [Constraints](../../db/dfe/structApp_1_1PropertyFloatConstraint_1_1Constraints.html) *sConstrain)  
| setting the boundaries This sets the constraint struct.
[More...](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a2f80258285396a1a90d9c4466c615088)  
  
virtual void | [setPyObject](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#acb90ab8757a5dfcc66fbe2e468f0d342) ([PyObject](../../df/d1b/classPyObject.html) *)  
virtual | [~PropertyFloatConstraint](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#ace7d967c1816eb46595a3bd0216ba0ed) ()  
| A destructor.
[More...](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#ace7d967c1816eb46595a3bd0216ba0ed)  
  
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

Constraint float properties This property fulfills the need of a constraint
float.

It holds basically a state (float) and a struct of boundaries. If the
boundaries is not set it acts basically like a
[PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html "Float properties
This is the father of all properties handling floats.") and does no checking
The constraints struct can be created on the heap or built-in.

## Constructor & Destructor Documentation

## ◆ PropertyFloatConstraint()

PropertyFloatConstraint::PropertyFloatConstraint  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Value Constructor Construct with explicit Values.

## ◆ ~PropertyFloatConstraint()

| PropertyFloatConstraint::~PropertyFloatConstraint  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ getConstraints()

const [PropertyFloatConstraint::Constraints](../../db/dfe/structApp_1_1PropertyFloatConstraint_1_1Constraints.html) * PropertyFloatConstraint::getConstraints  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
get the constraint struct

Referenced by
[FemGui::ViewProviderFemPostPlaneFunction::onChanged()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#aff4da6a421671244ed9f106adbaee37a),
and
[FemGui::TaskPostScalarClip::TaskPostScalarClip()](../../df/d2a/classFemGui_1_1TaskPostScalarClip.html#ab3c128515f1c8b3ab10aef3edd773832).

## ◆ getEditorName()

| virtual const char * App::PropertyFloatConstraint::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a3a0dd8a67f208ac5a258ee5755b0cd33).

Reimplemented in
[App::PropertyPrecision](../../d5/de5/classApp_1_1PropertyPrecision.html#ac2c734c673b528f52ab537b0cb3629d2).

## ◆ getMaximum()

double PropertyFloatConstraint::getMaximum  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getMinimum()

double PropertyFloatConstraint::getMinimum  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getStepSize()

double PropertyFloatConstraint::getStepSize  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ setConstraints()

void PropertyFloatConstraint::setConstraints  | ( | const [Constraints](../../db/dfe/structApp_1_1PropertyFloatConstraint_1_1Constraints.html) *  | _sConstrain_| ) |   
---|---|---|---|---|---  
  
setting the boundaries This sets the constraint struct.

It can be dynamically allocated or set as an static in the class the property
belongs to:

const
[Constraints](../../db/dfe/structApp_1_1PropertyFloatConstraint_1_1Constraints.html
"Constraint methods.") percent = {0.0,100.0,1.0}

Referenced by
[TechDraw::DrawPage::DrawPage()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a47a086fa134ba2f9e4f6a8121cb25ad2),
[TechDraw::DrawViewBalloon::DrawViewBalloon()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a2aa449f36b009ff5a461c4702bbe22cb),
[App::FeatureTest::FeatureTest()](../../df/dea/classApp_1_1FeatureTest.html#a71e331e5bda8a32669e0da873fb28c31),
[PartDesign::Helix::Helix()](../../d3/d78/classPartDesign_1_1Helix.html#af5b3edc469728ac5981e35e29412b61c),
[App::PropertyPrecision::PropertyPrecision()](../../d5/de5/classApp_1_1PropertyPrecision.html#aa7243c812a5ec9fcdd0c5aa93bfc2bf7),
[setPyObject()](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#acb90ab8757a5dfcc66fbe2e468f0d342),
[PartDesignGui::ViewProviderDatumCoordinateSystem::ViewProviderDatumCoordinateSystem()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a53832f895c08903546a696bd6e667100),
[FemGui::ViewProviderFemMesh::ViewProviderFemMesh()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a357c245ca2e9b478429c31fd3401e9d7),
[FemGui::ViewProviderFemPostPlaneFunction::ViewProviderFemPostPlaneFunction()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#aa66925aa45db6811cee9b19fe136fb66),
[Gui::ViewProviderLink::ViewProviderLink()](../../d6/d59/classGui_1_1ViewProviderLink.html#ac80b32ec9821edd74f1e39d58951773d),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
and
[PointsGui::ViewProviderPoints::ViewProviderPoints()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ac5af34ec9fcf964cf09f3f7eaee50fca).

## ◆ setPyObject()

| void PropertyFloatConstraint::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf2edab1753863426d8b78dd15dab006).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
and
[setConstraints()](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a2f80258285396a1a90d9c4466c615088).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyStandard.h
  * FreeCAD/src/App/PropertyStandard.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

