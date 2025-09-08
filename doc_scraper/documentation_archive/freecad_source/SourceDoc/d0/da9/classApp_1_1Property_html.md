---
url: https://freecad.github.io/SourceDoc/d0/da9/classApp_1_1Property.html
scraped_at: 2025-09-08T14:55:24.846725
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Property](../../d0/da9/classApp_1_1Property.html)

[List of all members](../../db/d99/classApp_1_1Property-members.html) | Public Types | Public Member Functions | Static Public Member Functions | Public Attributes | Protected Member Functions | Protected Attributes | Friends

App::Property Class Referenceabstract

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all properties This is the father of all
properties. [More...](../../d0/da9/classApp_1_1Property.html#details)

`#include <Property.h>`

##  Public Types  
  
---  
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
  
##  Public Member Functions  
  
---  
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
  
  
##  Static Public Member Functions  
  
---  
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
  
##  Public Attributes  
  
---  
boost::signals2::signal< void(const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChanged](../../d0/da9/classApp_1_1Property.html#a9e9e25207ee1e619c75f835f9853cf74)  
  
##  Protected Member Functions  
  
---  
virtual void | [aboutToSetValue](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d) (void)  
| Gets called by all setValue() methods before the value has changed.
[More...](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d)  
  
virtual void | [hasSetValue](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d) (void)  
| Gets called by all setValue() methods after the value has changed.
[More...](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d)  
  
virtual void | [verifyPath](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &p) const  
| Verify a path for the current property.
[More...](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7)  
  
  
##  Protected Attributes  
  
---  
std::bitset< 32 > | [StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67)  
| Status bits of the property The first 8 bits are used for the base system
the rest can be used in descendent classes to mark special statuses on the
objects.
[More...](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67)  
  
  
##  Friends  
  
---  
class | [DynamicProperty](../../d0/da9/classApp_1_1Property.html#adf6ce0d47bb0e4936b77e055ae1a1da4)  
class | [PropertyContainer](../../d0/da9/classApp_1_1Property.html#a7ff968ca40027b2b0500a9260b463e3a)  
struct | [PropertyData](../../d0/da9/classApp_1_1Property.html#a10f4390765aceac8cc5d3f89f7b31acb)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all properties This is the father of all
properties.

Properties are objects which are used in the document tree to parametrize e.g.
features and their graphical output. They are also used to gain access from
the scripting facility. /par This abstract base class defines all methods
shared by all possible properties. It is also possible to define user
properties and use them in the framework...

## Member Enumeration Documentation

## ◆ Status

enum
[App::Property::Status](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014)  
---  
  
Enumerator  
---  
Touched |   
Immutable |   
ReadOnly |   
Hidden |   
Transient |   
MaterialEdit |   
NoMaterialListEdit |   
Output |   
LockDynamic |   
NoModify |   
PartialTrigger |   
NoRecompute |   
Single |   
Ordered |   
EvalOnRestore |   
Busy |   
CopyOnChange |   
UserEdit |   
PropStaticBegin |   
PropDynamic |   
PropNoPersist |   
PropNoRecompute |   
PropReadOnly |   
PropTransient |   
PropHidden |   
PropOutput |   
PropStaticEnd |   
User1 |   
User2 |   
User3 |   
User4 |   
  
## Constructor & Destructor Documentation

## ◆ Property()

Property::Property  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~Property()

| Property::~Property  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ aboutToSetChildValue()

| virtual void App::Property::aboutToSetChildValue  | ( | [Property](../../d0/da9/classApp_1_1Property.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
Called before a child property changing value.

Reimplemented in
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#ac7444aaa1de15fcae6a70b0d024723d3),
and
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a9ac18b822a3fad41bc1d69342db5cf44).

Referenced by
[App::PropertyXLink::aboutToSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57).

## ◆ aboutToSetValue()

| void Property::aboutToSetValue  | ( | void  | | ) |   
---|---|---|---|---|---  
protectedvirtual  
  
Gets called by all setValue() methods before the value has changed.

Reimplemented in
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ab556673fad52c8535774ab736c61a40f),
and
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57).

References
[App::PropertyContainer::onBeforeChange()](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057).

Referenced by
[App::PropertyXLinkSubList::aboutToSetChildValue()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a9ac18b822a3fad41bc1d69342db5cf44),
[App::PropertyFileIncluded::aboutToSetValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ab556673fad52c8535774ab736c61a40f),
[App::PropertyXLink::aboutToSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57),
[Sketcher::PropertyConstraintList::acceptGeometry()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#acb51bc9feaf1b68d216e0935eb9713b0),
[App::PropertyLinkSubList::addValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17cad50fa5ecc14fafcfc99e3cba7bbd),
[App::PropertyXLinkContainer::breakLink()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a148b326bca33a5b23cc9434f24b569c2),
[Fem::PropertyFemMesh::Paste()](../../db/da7/classFem_1_1PropertyFemMesh.html#a965e26482afb2059c98dbcfa70230efa),
[Fem::PropertyPostDataObject::Paste()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#acdb90785feaf0796b597c2637f1919d1),
[Mesh::PropertyNormalList::Paste()](../../df/dcd/classMesh_1_1PropertyNormalList.html#aff86a78b6515ca708ca90d2eb8e3170f),
[Mesh::PropertyCurvatureList::Paste()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a80ac8f07bde36bd7effec1a7fa0c5e05),
[Mesh::PropertyMeshKernel::Paste()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#aad26bbf7a9c35e7816c16f17f644c99a),
[Part::PropertyPartShape::Paste()](../../d7/d28/classPart_1_1PropertyPartShape.html#ad3ae131c1102191e8c0eaf5316a3f6cb),
[Path::PropertyPath::Paste()](../../da/d75/classPath_1_1PropertyPath.html#ae758022b28985b00dc1c597e01dc84e4),
[Path::PropertyTool::Paste()](../../d4/d51/classPath_1_1PropertyTool.html#ad2f095ac0f5007bd96c464f6fc193c77),
[Path::PropertyTooltable::Paste()](../../d4/d86/classPath_1_1PropertyTooltable.html#a064394956f97879bc8cac0cdebe0ccfc),
[Points::PropertyGreyValueList::Paste()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a47ed130632df3250ea0d9bbef1ab2034),
[Points::PropertyNormalList::Paste()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#aff86a78b6515ca708ca90d2eb8e3170f),
[Points::PropertyCurvatureList::Paste()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a80ac8f07bde36bd7effec1a7fa0c5e05),
[Points::PropertyPointKernel::Paste()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#ae94d61a1250982c96eb98c548667891d),
[Robot::PropertyTrajectory::Paste()](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#abb7e97000b92c95131bc4c4b31093d7f),
[App::PropertyMatrix::Paste()](../../d8/d77/classApp_1_1PropertyMatrix.html#a040858e6dc324655487a124bc2ccfafa),
[App::PropertyPlacementLink::Paste()](../../d8/db5/classApp_1_1PropertyPlacementLink.html#aa08172316e8d59b648dcc5ac8266d56e),
[App::PropertyPythonObject::Paste()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a086c7bb8deef61645433e76eeb2fe3b0),
[App::PropertyInteger::Paste()](../../dd/d85/classApp_1_1PropertyInteger.html#a09abc5b0039b42f2b7c71fa707abcba9),
[App::PropertyPath::Paste()](../../dc/d24/classApp_1_1PropertyPath.html#a678a941b661da14440f66bccde5a12fe),
[App::PropertyIntegerSet::Paste()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#ab0e793f848a173a0eed7dc1c7cf5df4a),
[App::PropertyMap::Paste()](../../db/d3f/classApp_1_1PropertyMap.html#aefc83d68750955ffb88f7a1b70d983d5),
[App::PropertyFloat::Paste()](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf1f7c4fc4c8bde2ca9b8482180e45ff),
[App::PropertyUUID::Paste()](../../d2/d6c/classApp_1_1PropertyUUID.html#a04253297c6a35fc1036d4a456508807f),
[App::PropertyBool::Paste()](../../dc/d81/classApp_1_1PropertyBool.html#a884f68fe6a0d3bd3eddd54fe8f8abd32),
[App::PropertyColor::Paste()](../../d9/d0b/classApp_1_1PropertyColor.html#a6f089f8323aec6afbf91c66680581c69),
[App::PropertyMaterial::Paste()](../../d0/df5/classApp_1_1PropertyMaterial.html#a289a5c052d01968874da66c93cfa9fe3),
[Inspection::PropertyDistanceList::Paste()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#aefdcf03dac9fd7486f09dcc17905a718),
[Part::PropertyShapeHistory::Paste()](../../de/d7c/classPart_1_1PropertyShapeHistory.html#ad7af995f1b0ed7f92982638217f87538),
[Part::PropertyFilletEdges::Paste()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a8b0df89d4c6a3a5e8d8d062e2fc240ae),
[Spreadsheet::PropertySpreadsheetQuantity::Paste()](../../d2/dd4/classSpreadsheet_1_1PropertySpreadsheetQuantity.html#a2e105319857c2aa18ec56cb5a56b8f10),
[App::PropertyVector::Paste()](../../d5/d2b/classApp_1_1PropertyVector.html#a7ef832b4811885d30b97782e10afe042),
[App::PropertyPlacement::Paste()](../../da/d51/classApp_1_1PropertyPlacement.html#afbd1d98d3c19b17652f2306885da8815),
[App::PropertyRotation::Paste()](../../df/d76/classApp_1_1PropertyRotation.html#ab690c2b3639a616d6c156a391d3d9db8),
[App::PropertyXLinkSubList::Paste()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4ac663947ed88fa49f3a874273098fe4),
[App::PropertyPersistentObject::Paste()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aa32598aecbbb59a82597e21ef43b3273),
[App::PropertyExpressionEngine::renameExpressions()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a02fc7fcac9d0638d3e2385eb88b6cedc),
[App::PropertyMatrix::Restore()](../../d8/d77/classApp_1_1PropertyMatrix.html#ac341d4242623336eafaf73bd16dfe8ad),
[App::PropertyPythonObject::Restore()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a7c4c1053b780d2f149cc99c86d3e39ff),
[App::PropertyEnumeration::Restore()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c),
[App::PropertyString::Restore()](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1),
[App::PropertyMaterial::Restore()](../../d0/df5/classApp_1_1PropertyMaterial.html#a9f1511c5fd99820c649307361c6c8880),
[Mesh::PropertyMeshKernel::Restore()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#ae5fd1c096fb6b3a70935261847e70115),
[Points::PropertyPointKernel::Restore()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a4e72a35a1ea913ffee981734df7e500f),
[App::PropertyVector::Restore()](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c),
[App::PropertyPlacement::Restore()](../../da/d51/classApp_1_1PropertyPlacement.html#a585fd1033be79f3fd3ebd0ae6fe8f734),
[App::PropertyRotation::Restore()](../../df/d76/classApp_1_1PropertyRotation.html#af641d12c42fa3ed2076e9d3f234ef31c),
[App::PropertyPythonObject::RestoreDocFile()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#af97b03d68515ca8bde89d895a1a6b08b),
[Fem::PropertyFemMesh::RestoreDocFile()](../../db/da7/classFem_1_1PropertyFemMesh.html#a57a423cdaccbe74d791cc980d9a9fd1a),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[Mesh::PropertyMeshKernel::RestoreDocFile()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a5150b28419d76cabc4f473f5daa59313),
[Path::PropertyPath::RestoreDocFile()](../../da/d75/classPath_1_1PropertyPath.html#a6ee2ea90ed9f02be32225df050ee9034),
[Points::PropertyPointKernel::RestoreDocFile()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a52466ad6689e8d30234bf5ec71b35646),
[Fem::PropertyPostDataObject::scale()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#ac071ffd68ec6bffde814f0fb88992fa9),
[Sketcher::PropertyConstraintList::set1Value()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#ac694be89d723e789b6f7574bf3cedd68),
[Part::PropertyGeometryList::set1Value()](../../db/dca/classPart_1_1PropertyGeometryList.html#a3a5edbc860880444fb39d59592917cf9),
[App::PropertyMaterial::setAmbientColor()](../../d0/df5/classApp_1_1PropertyMaterial.html#a337c7d6fc94fdc9ba4a4c5ae77f6d213),
[App::PropertyMaterial::setDiffuseColor()](../../d0/df5/classApp_1_1PropertyMaterial.html#a5c8fe036cb3b5bf9c7137b2e7fb4c2ef),
[App::PropertyMaterial::setEmissiveColor()](../../d0/df5/classApp_1_1PropertyMaterial.html#ada4905e18be3bb9a21ebe1b39a452622),
[App::PropertyEnumeration::setEnums()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a5571099202eda6dacf748996eedf6551),
[App::PropertyEnumeration::setEnumVector()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a265272a98d0ae08006973d863d9aba9d),
[App::PropertyQuantity::setPathValue()](../../d4/d65/classApp_1_1PropertyQuantity.html#af017ce248b34f5378b3a714aa270c421),
[Sketcher::PropertyConstraintList::setPathValue()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a2412c655ef32a277f98f2ae6bd659bcb),
[Mesh::PropertyMeshKernel::setPointIndices()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a7e421036a2b600d1b1a359c820ec95d3),
[App::PropertyPythonObject::setPyObject()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#abc4c47fe0adc00e73cf00e56223d058e),
[App::PropertyInteger::setPyObject()](../../dd/d85/classApp_1_1PropertyInteger.html#a01766b286f7ee23f14008042a2465044),
[App::PropertyEnumeration::setPyObject()](../../d4/df2/classApp_1_1PropertyEnumeration.html#aa715a8742ad95f4288e987f2f20d4719),
[App::PropertyIntegerConstraint::setPyObject()](../../d2/dc8/classApp_1_1PropertyIntegerConstraint.html#a59de0c197b75f6ad9e00c93bb02611b3),
[App::PropertyFloat::setPyObject()](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf2edab1753863426d8b78dd15dab006),
[App::PropertyFloatConstraint::setPyObject()](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#acb90ab8757a5dfcc66fbe2e468f0d342),
[App::PropertyQuantity::setPyObject()](../../d4/d65/classApp_1_1PropertyQuantity.html#a72be43d71c5e5a5e0a174c01df176dc9),
[App::PropertyMaterial::setShininess()](../../d0/df5/classApp_1_1PropertyMaterial.html#af40c06051021d1a02c4acd14f744b5d5),
[App::PropertyMaterial::setSpecularColor()](../../d0/df5/classApp_1_1PropertyMaterial.html#a391730862bfa2242449576428fdb8e10),
[App::PropertyMaterial::setTransparency()](../../d0/df5/classApp_1_1PropertyMaterial.html#a26538d6c721c101a7042e56b55131222),
[App::PropertyLink::setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1),
[App::PropertyLinkSub::setValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9072c1b8bf3ee43a0d82c0e266cc1f33),
[App::PropertyBool::setValue()](../../dc/d81/classApp_1_1PropertyBool.html#a8067462e38e7bb949ae31a86ec8ed17c),
[TechDraw::PropertyCenterLineList::setValue()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#ae68d0b3a613078dbdbec3f3e782b09b5),
[App::PropertyMatrix::setValue()](../../d8/d77/classApp_1_1PropertyMatrix.html#a15ef8f5f325db539295a77162cde3c29),
[App::PropertyPlacement::setValue()](../../da/d51/classApp_1_1PropertyPlacement.html#abb1f46e80061be4669b0ca20c83a7b31),
[App::PropertyRotation::setValue()](../../df/d76/classApp_1_1PropertyRotation.html#abbe10359c78a2b1fa074a8ddf0638773),
[App::PropertyUUID::setValue()](../../d2/d6c/classApp_1_1PropertyUUID.html#ab6d9418f4d048c0d0070c9c45a9233d2),
[App::PropertyVector::setValue()](../../d5/d2b/classApp_1_1PropertyVector.html#a866a1f59e997434cbe7e642af74301db),
[Mesh::PropertyNormalList::setValue()](../../df/dcd/classMesh_1_1PropertyNormalList.html#af79004fd1b518c6413ff1d11fca901fd),
[Points::PropertyNormalList::setValue()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#af79004fd1b518c6413ff1d11fca901fd),
[App::PropertyPath::setValue()](../../dc/d24/classApp_1_1PropertyPath.html#ad2d79969f6d45968031a1cd53a0dbc48),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[App::PropertyPersistentObject::setValue()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a117bd17a68a39872c084cf4e48401922),
[App::PropertyEnumeration::setValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a10973c61a7072bba34df37062aaa266d),
[App::PropertyColor::setValue()](../../d9/d0b/classApp_1_1PropertyColor.html#a4aab2001271a7767ba2e47c681286b27),
[Sketcher::PropertyConstraintList::setValue()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#acb1487eba8b8fd05122ef0e9d47679f1),
[Mesh::PropertyCurvatureList::setValue()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a6825a19dcfc3bfedf1718d20bf3d917d),
[Points::PropertyCurvatureList::setValue()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a6825a19dcfc3bfedf1718d20bf3d917d),
[Fem::PropertyFemMesh::setValue()](../../db/da7/classFem_1_1PropertyFemMesh.html#ae8e63278bec724a292ec4e1c3b6e07b7),
[Part::PropertyGeometryList::setValue()](../../db/dca/classPart_1_1PropertyGeometryList.html#a3fb0ae2bda56e1b5990bef9d980d53d9),
[TechDraw::PropertyGeomFormatList::setValue()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a15f264be3fd91839282f2454a1f92421),
[App::PropertyMaterial::setValue()](../../d0/df5/classApp_1_1PropertyMaterial.html#a4514e658133a9730c3ee62029b661c26),
[Mesh::PropertyMeshKernel::setValue()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a9d3aa33f749d3d5ecd9117f19e102609),
[Points::PropertyPointKernel::setValue()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#af9c758e102565b6510741fde550833d9),
[Part::PropertyShapeHistory::setValue()](../../de/d7c/classPart_1_1PropertyShapeHistory.html#ab13fab22f02c23c6667fcb7ec534bb57),
[App::PropertyMap::setValue()](../../db/d3f/classApp_1_1PropertyMap.html#acb8aa4cf5323671d12cdff5ee1554e09),
[Path::PropertyTool::setValue()](../../d4/d51/classPath_1_1PropertyTool.html#adcc535b5f8467c340d5287ca7588a62d),
[Path::PropertyPath::setValue()](../../da/d75/classPath_1_1PropertyPath.html#a66b0a2f5b8c2be68a7459f6ff0f7fccd),
[Path::PropertyTooltable::setValue()](../../d4/d86/classPath_1_1PropertyTooltable.html#abccad12c5ecaad48c6ec7c626d1edcd2),
[Part::PropertyPartShape::setValue()](../../d7/d28/classPart_1_1PropertyPartShape.html#a57ceb747ef13922fe2d4cce37f351c38),
[Robot::PropertyTrajectory::setValue()](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#a8029ad3ec29f20989d54e960598bf040),
[Fem::PropertyPostDataObject::setValue()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a2bf10e103cd77da0fb0180f324c2f871),
[TechDraw::PropertyCosmeticEdgeList::setValue()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#ad328e4ffd5d6fc23f07d07b5038fec0f),
[TechDraw::PropertyCosmeticVertexList::setValue()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a9a3945950d3b7616b40ab27cd92202b1),
[App::PropertyLinkSubList::setValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f),
[App::PropertyFloat::setValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#aeb4937e13aff58a04f81fdadf544f7d9),
[Inspection::PropertyDistanceList::setValue()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a7e8c326f0aa7c3bafd3246bd452d5681),
[Points::PropertyGreyValueList::setValue()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a2dd33f0fdfe14a78502d42dea9209847),
[Spreadsheet::PropertyColumnWidths::setValue()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#aaaf6b3782e9919f475a17bcbfb8e5c72),
[Part::PropertyFilletEdges::setValue()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a3bd1461a2917910d181fabf41251720e),
[Spreadsheet::PropertyRowHeights::setValue()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#ad5b6bd2fee64297348daa9b44051bd52),
[App::PropertyInteger::setValue()](../../dd/d85/classApp_1_1PropertyInteger.html#ac542ac41f9bad4ff220e906d7342d8ee),
[App::PropertyIntegerSet::setValue()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#ab27b4e25de1bef22752455bd8cb7ed23),
[App::PropertyPythonObject::setValue()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#aa7f9b4e9f7ce28c5465c905cc8baa6e6),
[Fem::PropertyFemMesh::setValuePtr()](../../db/da7/classFem_1_1PropertyFemMesh.html#a98f59a0e8b219f5abd4b1fd7cbc20a1e),
[Mesh::PropertyMeshKernel::setValuePtr()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#aeb6e1827257921773ab6b2bb3cfceea0),
[Spreadsheet::PropertyColumnWidths::setValues()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a0515c8aa45e70ed1409dfb4b070c1d01),
[Spreadsheet::PropertyRowHeights::setValues()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a0fc1931e77a169dd3413df6c2d0733b3),
[App::PropertyMap::setValues()](../../db/d3f/classApp_1_1PropertyMap.html#a7e543fd0696a33dec20006c615938510),
[App::PropertyIntegerSet::setValues()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#a33114deb128b23f8e2bff56c3bc98675),
[Mesh::PropertyNormalList::setValues()](../../df/dcd/classMesh_1_1PropertyNormalList.html#a160cd8e84fa526e3cbb2fb135ca0e612),
[Points::PropertyNormalList::setValues()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a160cd8e84fa526e3cbb2fb135ca0e612),
[TechDraw::PropertyCenterLineList::setValues()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a07b5c8f01d0398444e9ee5ab3b019b52),
[TechDraw::PropertyCosmeticEdgeList::setValues()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a0f1a31536f4f635d5d5add78b586c7da),
[TechDraw::PropertyCosmeticVertexList::setValues()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a3704b8b213643bc8a78b8bb16ed1ae8c),
[Mesh::PropertyCurvatureList::setValues()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#ad11bea58b7eb13bd540448bbdf4f2495),
[Points::PropertyCurvatureList::setValues()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#ad11bea58b7eb13bd540448bbdf4f2495),
[App::PropertyLinkSubList::setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7),
[Part::PropertyFilletEdges::setValues()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a9c684a34571d703b5a42f1dee2a182ed),
[Inspection::PropertyDistanceList::setValues()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a2d90d0bd07c2addd2fceddc34a8ae9cc),
[Points::PropertyGreyValueList::setValues()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#ac761f627ad3d5d1afdbb7282040ac107),
[TechDraw::PropertyGeomFormatList::setValues()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#aa486b1faadc067963b4c9771255ddd91),
[Part::PropertyShapeHistory::setValues()](../../de/d7c/classPart_1_1PropertyShapeHistory.html#a57022bcba8c3f0ffdafb44e184e7451c),
[Sketcher::PropertyConstraintList::setValues()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a7886fa7b83544c271a2523424ed5fb54),
[Part::PropertyGeometryList::setValues()](../../db/dca/classPart_1_1PropertyGeometryList.html#a0c7ea8bd070c25a1877ac1edf911edda),
[Mesh::PropertyMeshKernel::startEditing()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a375aa2f5ed037e018b949ae57ee8d3e2),
[Points::PropertyPointKernel::startEditing()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#aeb2249f7cab84a9299a2d197ddf01a2d),
[Mesh::PropertyMeshKernel::swapMesh()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a82d1d54277c0bd59bac872a10a32ca38),
[Fem::PropertyFemMesh::transformGeometry()](../../db/da7/classFem_1_1PropertyFemMesh.html#a50d0dff44b30ea18254759b9dad46650),
[Mesh::PropertyNormalList::transformGeometry()](../../df/dcd/classMesh_1_1PropertyNormalList.html#a064a298f4261410fe6727a3bbd903ca9),
[Mesh::PropertyCurvatureList::transformGeometry()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a698d1e0cfd7a47a876f28ae6239bcfda),
[Mesh::PropertyMeshKernel::transformGeometry()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a2077e18fdbec8449fc028675946c3c71),
[Part::PropertyPartShape::transformGeometry()](../../d7/d28/classPart_1_1PropertyPartShape.html#aa7d347e5acb431ed5b43146266418569),
[Points::PropertyNormalList::transformGeometry()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a064a298f4261410fe6727a3bbd903ca9),
[Points::PropertyCurvatureList::transformGeometry()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a698d1e0cfd7a47a876f28ae6239bcfda),
and
[Points::PropertyPointKernel::transformGeometry()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#aac021bd95beaf0a0c89dda20c8959dc1).

## ◆ afterRestore()

| virtual void App::Property::afterRestore  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Called at the beginning of
[Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5)

This function is called without dependency sorting, because some types of link
property can only reconstructs the linking information inside this function.

One example use case of this function is
[PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html "the Link
Property with sub elements This property links an object and a defined
sequence of sub eleme...") that uses
[afterRestore()](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f
"Called at the beginning of Document::afterRestore\(\)") to parse and restore
subname references, which may contain sub-object reference from external
document, and there will be special mapping required during object import.

Another example is
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
which only parse the restored expression in
[afterRestore()](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f
"Called at the beginning of Document::afterRestore\(\)"). The reason, in
addition to subname mapping like
[PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html "the Link
Property with sub elements This property links an object and a defined
sequence of sub eleme..."), is that it can handle document name adjustment as
well. It internally relies on
[PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html "Link to an
\(sub\)object in the same or different document.") to store the external
document path for external linking. When the external document is restored,
its internal name may change due to name conflict with existing documents.
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
can now auto adjust external references without any problem.

Reimplemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a3f55d05db5c992052bd196642b1c01ea),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a54c5bae021df3175a6bc3c37fae06e01),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a01ca28793b37026f539afb49f397aec2),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a3a9916bc1df1cc05d0362053e9ded4b1),
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a00e6240a9cf8e5b7dbf0cf287cbd4db1),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a094d3eb343aaa42ace2817a85f8dee3a).

## ◆ canonicalPath()

| [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) Property::canonicalPath  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _p_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Convert p to a canonical representation of it.

Reimplemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a21b797539c8eef459b505be492c17f09),
and
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#adb93af9df63a8a2b049bdc3c196dd84d).

Referenced by
[Gui::ExpressionBinding::bind()](../../dc/d5a/classGui_1_1ExpressionBinding.html#aba7b2c918c04b6e3f589e53876cdb761).

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * Property::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
pure virtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implemented in
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a8357945cf4e3e84abd535ef6d53d4f99),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#a0c2e0b02b35205d14165d05b96074ea7),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a7c8ba3c47ff861368b0382f1503bc8f1),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a028ddaaad1b13ebb21dec63fb136c957),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#ad89eaa7878cda05c77ba7d09f8beb2a4),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a0c2e0b02b35205d14165d05b96074ea7),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a7c8ba3c47ff861368b0382f1503bc8f1),
[Points::PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#aef02bf6b476ee564f7b65fbe69894c51),
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#a36afe5d9e1f99ac4d9a0f3862c744756),
[App::PropertyMatrix](../../d8/d77/classApp_1_1PropertyMatrix.html#a3e321ae3665b342336e153d36f66871c),
[App::PropertyPlacementLink](../../d8/db5/classApp_1_1PropertyPlacementLink.html#a79a279154ca0a57b537a595f7ead7d9b),
[App::PropertyPythonObject](../../d7/d1d/classApp_1_1PropertyPythonObject.html#aafee65f725e4939ddcc0bb21c74753c2),
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#ab2dc80248124960dfddd1a23eff815ac),
[App::PropertyPath](../../dc/d24/classApp_1_1PropertyPath.html#a828e441604839c65e4da63ecb0d800b8),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a716562a2a85ac80ba5672855ed1364b0),
[App::PropertyIntegerSet](../../d0/df3/classApp_1_1PropertyIntegerSet.html#ac33614e1ba3bb32fcacfcd167a3f1c73),
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html#a21bee8862041ae0995373d4ce16ffe3b),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#ac7565beb8b32fc7383a55e4052ecdfd7),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#abff429e61e5545bd5b7e94fc7a318ba5),
[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html#ab841e7f4f4078c7c8d59fe0628163b66),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#a9971031594a20af7bffe75225510b743),
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#ab957657dcd3846e19a36a68ba488480f),
[App::PropertyMaterial](../../d0/df5/classApp_1_1PropertyMaterial.html#a829192b062a0c1fbae360cb5aff34858),
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#aee6bb0a4acd93228733ea3e433bb62b9),
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a88f220dc7e2e5d8b1d8ccbdab4119e48),
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#afaf4e9b21ab11da8b54eb530ef26388e),
[Part::PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html#aec4e098df99f58fc48e968d150b5612d),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#aafeeca55dbb9440c2949f9f0b38e7edd),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#afc8ac8e7d8792326bc679dd58ff92091),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#aa1002065599eb52fdb4ee06e0b4099ab),
[Path::PropertyPath](../../da/d75/classPath_1_1PropertyPath.html#ac28141b94d6b8003e3a58e6902e2ea04),
[Path::PropertyTool](../../d4/d51/classPath_1_1PropertyTool.html#a3e2ac2c10b47c02170e584ac712e2e57),
[Path::PropertyTooltable](../../d4/d86/classPath_1_1PropertyTooltable.html#a2711492e78853765b5cce98d221fde68),
[Robot::PropertyTrajectory](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#a0639ae60e2a2ac192868ea10c98982f0),
[Spreadsheet::PropertyColumnWidths](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a53c6f495313e841d5c2084af754b932b),
[Spreadsheet::PropertyRowHeights](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a5cd04d676325ab2725c45b85e4413714),
[Spreadsheet::PropertySpreadsheetQuantity](../../d2/dd4/classSpreadsheet_1_1PropertySpreadsheetQuantity.html#a1c4e3c7cafaf2ae7f08ec03a8bfb63f9),
[TechDraw::PropertyCenterLineList](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a1d015187408300e2159525c6b110039a),
[TechDraw::PropertyCosmeticEdgeList](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#af4d9457d63bae09f70e33039b3721b11),
[TechDraw::PropertyCosmeticVertexList](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a0e5787cf2e099141cc035b9e64db14c0),
[TechDraw::PropertyGeomFormatList](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a987a7d40934ff973337acffac765894b),
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a19a4bb9dfd62c2c0c82fdfc6e5df26c9),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#ae60ac5ec9b71fcd763c369382d8bc29d),
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#ae0507521f63d3d14ef22328483281f64),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#ae4fc87aa899e0a6cb40609b6307f661d),
[App::PropertyPlacementList](../../d1/d76/classApp_1_1PropertyPlacementList.html#a985b20535e733f7c925ad4e6b69dc482),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a11d683872f0c6070dbef87552842d762),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a2be3428447d9bd3203d09534b15d5bbc),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a95437520bba360e4b84bbef5af656eaa),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab28f0a208ed6e4b6dafce9d09555dcb7),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a6e7ddbe8a1061c36145bd0180b47c7f1),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad3ce8f501efd0cdd27a89018b7fe7672),
[App::PropertyIntegerList](../../d7/daa/classApp_1_1PropertyIntegerList.html#ab7258383dcbef07aa1a3470a92fd3786),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#a6d0e515ccde9cd45890e35fc77c630f5),
[App::PropertyStringList](../../d8/d55/classApp_1_1PropertyStringList.html#a1ae3b8dc884712b80aa03518222ca8d0),
[App::PropertyBoolList](../../d1/dcf/classApp_1_1PropertyBoolList.html#ad353bdab1749bfaf38c57fd0326869f0),
[App::PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#a71525d9a6c7ff7da1202b6f3ed6659dd),
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a8117c9f506c1b9abbdd1aa42a8765e7a),
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a90a82f3560b30c57524eba73104a45e3),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#ad5f2ba120e10f33954fdbe97eaaefc4a),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a34e512028d34fc9066b3af09db195244).

Referenced by
[App::TransactionObject::addOrRemoveProperty()](../../d9/d02/classApp_1_1TransactionObject.html#a1a9c63db207f7e24ed6918877c134764),
[App::LinkBaseExtension::checkCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6521528d36c644c2b1de74a2f74d82c0),
[PartGui::ViewProviderCustom::onChanged()](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
[SketcherGui::ViewProviderCustom::onChanged()](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
and
[App::TransactionObject::setProperty()](../../d9/d02/classApp_1_1TransactionObject.html#ad234dbb98feea5e3fb448aa2b0825207).

## ◆ destroy()

| void Property::destroy  | ( | [Property](../../d0/da9/classApp_1_1Property.html) *  | _p_| ) |   
---|---|---|---|---|---  
static  
  
For safe deleting of a dynamic property.

References
[App::PropertyCleaner::add()](../../dc/dce/structApp_1_1PropertyCleaner.html#ae49a4eef588388f0f46dae7906e2a318).

Referenced by
[App::DynamicProperty::removeDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a8e4c6ca6912ea2f53be583ba0ff7d7b6).

## ◆ getContainer()

[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) * App::Property::getContainer  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Get a pointer to the
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html "Base
class of all classes with properties.") derived class the property belongs to.

Referenced by
[App::TransactionObject::addOrRemoveProperty()](../../d9/d02/classApp_1_1TransactionObject.html#a1a9c63db207f7e24ed6918877c134764),
[App::PropertyLinkSubList::addValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17cad50fa5ecc14fafcfc99e3cba7bbd),
[App::PropertyExpressionEngine::adjustLink()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a6ef128439add23206d190bedd151f02e),
[App::PropertyExpressionEngine::afterRestore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1),
[App::PropertyLink::breakLink()](../../d4/d77/classApp_1_1PropertyLink.html#a5ba319a4ccf1773412d1d5023482ceda),
[App::PropertyLinkList::breakLink()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa0c652f1384e33bace3fb708d26d57c7),
[App::PropertyLinkSub::breakLink()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a53e073970cf9ad76667d02027bb78c84),
[App::PropertyLinkSubList::breakLink()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#af3659c9cd764ba67a9b4eb61ac10d328),
[App::PropertyXLinkSubList::breakLink()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad8d3af63e632d9e26194e66ed0eaaa68),
[App::PropertyXLinkContainer::breakLink()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a148b326bca33a5b23cc9434f24b569c2),
[App::PropertyExpressionEngine::canonicalPath()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a21b797539c8eef459b505be492c17f09),
[App::PropertyXLinkContainer::clearDeps()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#ae68afb7d60232d3e41aca30995012143),
[App::PropertyLinkSub::CopyOnImportExternal()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a048f449b304bded2a609bc32bc3d3107),
[App::PropertyLinkSubList::CopyOnImportExternal()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a7d7f8cd3cb3ce4405391586167328afc),
[App::PropertyXLink::CopyOnImportExternal()](../../d2/de2/classApp_1_1PropertyXLink.html#a145fcf5a76cec92e8ca60bad28e6fe76),
[App::PropertyLinkSub::CopyOnLabelChange()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a09c96d3556fa092d37d9f597fbf468c5),
[App::PropertyLinkSubList::CopyOnLabelChange()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a832033ed5b5810a9add720cd72ca6cef),
[App::PropertyXLink::CopyOnLabelChange()](../../d2/de2/classApp_1_1PropertyXLink.html#a9c9b89ffa3e4be3e0e5a046e6371e557),
[App::PropertyLink::CopyOnLinkReplace()](../../d4/d77/classApp_1_1PropertyLink.html#ae33affee6371a40629ea84b1782c2cb5),
[App::PropertyLinkList::CopyOnLinkReplace()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a4406a63b9428c6313f37413a0a8b3821),
[App::PropertyLinkSub::CopyOnLinkReplace()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a24386974f021c3d8d5c3679276b403bb),
[App::PropertyLinkSubList::CopyOnLinkReplace()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ae849b6086e5b7731cefac897c3c5b3ec),
[App::PropertyXLink::CopyOnLinkReplace()](../../d2/de2/classApp_1_1PropertyXLink.html#aa713c66bf6fd8a5a03ec1f94b233e8bb),
[App::PropertyExpressionEngine::execute()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a734f6ae9dbd4df6a8ebafee9a8d8bebd),
[App::PropertyFileIncluded::getDocTransientPath()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5f4e5ed4004ee3084755508e6c3b071a),
[getPaths()](../../d0/da9/classApp_1_1Property.html#a945f1c031f109242e362c5701516ff8e),
[Part::PropertyPartShape::getPaths()](../../d7/d28/classPart_1_1PropertyPartShape.html#a613e891f4e97c366bfce9a191006e3cf),
[App::PropertyExpressionEngine::getPathsToDocumentObject()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#abacf82f2397cd656b8e0cc01e0bc9295),
[App::PropertyExpressionEngine::hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[Spreadsheet::PropertySheet::insertColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a265014a33975e005189793fb75251c56),
[Spreadsheet::PropertySheet::insertRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aa84f3f19aed8b5355d16cece5eb4a5d9),
[App::LinkBaseExtension::isCopyOnChangeProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a832eacdf828db96b92137a17f223243d),
[App::GeoFeatureGroupExtension::isLinkValid()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a89659fb6caa61f4cf9971b0170efcdc7),
[App::ObjectIdentifier::ObjectIdentifier()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2e87192f46ed457637f2b2d05abd01b7),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartGui::PropertyEnumAttacherItem::openTask()](../../dd/db5/classPartGui_1_1PropertyEnumAttacherItem.html#a232e6f966edd003419540ac9e7c9f405),
[App::DocumentObjectT::operator=()](../../d5/d07/classApp_1_1DocumentObjectT.html#aa6d6b6131b81ccd65364482dd799199b),
[Spreadsheet::PropertySheet::removeColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ada4ceb76fd79dc130476fe307f77e0a1),
[Spreadsheet::PropertySheet::removeRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5ff589d68c79b8387678e38007f8733f),
[App::PropertyLink::resetLink()](../../d4/d77/classApp_1_1PropertyLink.html#a0461c85fa8e082a75df6e848f94d8c39),
[App::PropertyString::Restore()](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[Path::PropertyPath::RestoreDocFile()](../../da/d75/classPath_1_1PropertyPath.html#a6ee2ea90ed9f02be32225df050ee9034),
[App::PropertyXLink::restoreLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a232e8182760d7ae2717d555416e4b4ce),
[App::PropertyString::Save()](../../dd/df8/classApp_1_1PropertyString.html#a22cfc259b6c352cd5f14b3a400704164),
[App::PropertyLinkSub::Save()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a828dfbbf362ee9875da57453517b3358),
[App::PropertyLinkSubList::Save()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e),
[App::PropertyXLink::Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[App::PropertyXLinkContainer::Save()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676),
[Fem::PropertyPostDataObject::SaveDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a3ed0c0500e1d89813d4d6854ce5b388b),
[App::PropertyLinkList::set1Value()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a7a16fe45fc1c04feba8b79c9cd463f4d),
[Spreadsheet::Cell::setAlias()](../../d5/d22/classSpreadsheet_1_1Cell.html#a31072bb3341e28b9398d044d34b1a557),
[App::PropertyXLink::setAllowPartial()](../../d2/de2/classApp_1_1PropertyXLink.html#af69aa75e548072c713a0b180cadab17e),
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede),
[App::TransactionObject::setProperty()](../../d9/d02/classApp_1_1TransactionObject.html#ad234dbb98feea5e3fb448aa2b0825207),
[App::LinkBaseExtension::setProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770),
[Part::PropertyGeometryList::setPyObject()](../../db/dca/classPart_1_1PropertyGeometryList.html#a97ddf273f653e0c221d3c2195936383f),
[App::PropertyLinkList::setSize()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a05972fc1163a21a73e4526a071896f92),
[App::PropertyLink::setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1),
[App::PropertyXLink::setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10),
[App::PropertyLinkSub::setValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9072c1b8bf3ee43a0d82c0e266cc1f33),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[App::PropertyLinkSubList::setValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f),
[App::PropertyLinkList::setValues()](../../d3/d8c/classApp_1_1PropertyLinkList.html#af7e153c0a4b95bb6b79a5b2b357d5a48),
[App::PropertyLinkSubList::setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7),
[Gui::RecoveryWriter::shouldWrite()](../../d9/d25/classGui_1_1RecoveryWriter.html#aec0a593c8a632c1e1700c4b8e851372f),
[App::PropertyXLinkContainer::updateDeps()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a83acea46b0d063043f43d99de26dfe29),
[App::PropertyExpressionEngine::updateElementReference()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a00a63354dd2052c675de28c01ff70362),
[Spreadsheet::PropertySheet::updateElementReference()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a35d58b0bf7eac198ffdae31e16f3173f),
[App::PropertyLinkSubList::updateElementReference()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca),
[App::PropertyLinkSubList::upgrade()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b),
[App::PropertyXLinkSubList::upgrade()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2),
[App::PropertyXLinkSub::upgrade()](../../d4/da0/classApp_1_1PropertyXLinkSub.html#a0f3a85600e83e0f36d654f72939d9add),
[App::PropertyLinkList::~PropertyLinkList()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aef7be25314c8c5441d9baa207ddd51c1),
[App::PropertyLinkSub::~PropertyLinkSub()](../../d3/d76/classApp_1_1PropertyLinkSub.html#ac2366078790473115b614fdc02345a4a),
and
[App::PropertyLinkSubList::~PropertyLinkSubList()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17189b0ae71b797884f1ca041cfe263f).

## ◆ getDocumentation()

const char * Property::getDocumentation  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Get the documentation of this property.

References
[App::PropertyContainer::getPropertyDocumentation()](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912).

Referenced by
[App::DynamicProperty::addProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#afaada5859108dac4c73627edc1d5369e),
and
[Gui::PropertyEditor::PropertyItem::toolTip()](../../d6/db3/classGui_1_1PropertyEditor_1_1PropertyItem.html#a735eba49382a210cf025ea4883d4beb2).

## ◆ getEditorName()

| virtual const char * App::Property::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Get the class name of the associated property editor item.

Reimplemented in
[App::PropertyFile](../../d9/d86/classApp_1_1PropertyFile.html#ac3494f9267e386fa8cec4f87232316be),
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a288709e5f74e8e8a254bd8afade804e5),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a533107f37adfd14fd741445e0b4f2000),
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#a5ababff555917752731e5f9b37961b87),
[App::PropertyVectorDistance](../../d7/d1e/classApp_1_1PropertyVectorDistance.html#a771717f36e2805890ee62e7522a2dc73),
[App::PropertyPosition](../../dd/dc2/classApp_1_1PropertyPosition.html#a8edef058848613ec44f22b6b90242a48),
[App::PropertyDirection](../../d8/d4c/classApp_1_1PropertyDirection.html#abfa89d32ef67805c7f601db9fe38de5c),
[App::PropertyMatrix](../../d8/d77/classApp_1_1PropertyMatrix.html#a6601a2eb74355598f70523771021002e),
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#a69288b56dc31fa23037e6ed67210e2fb),
[App::PropertyPath](../../dc/d24/classApp_1_1PropertyPath.html#af5a2677b52b166ee54efae3c4590b321),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a34911d749d232ae75515883964b6cc4b),
[App::PropertyIntegerConstraint](../../d2/dc8/classApp_1_1PropertyIntegerConstraint.html#a91f4dac53b547b4964f7178500f70565),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a3a0dd8a67f208ac5a258ee5755b0cd33),
[App::PropertyFloatConstraint](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#a3f5130569b81c7c30f8dbd32bd687061),
[App::PropertyPrecision](../../d5/de5/classApp_1_1PropertyPrecision.html#ac2c734c673b528f52ab537b0cb3629d2),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#a6d09fe56505033a027f3422fbeedbe12),
[App::PropertyFont](../../df/d8c/classApp_1_1PropertyFont.html#ab9a098db6ead92fbfd290c8708cec1e3),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#ac100a4def344f24aa36677f56121d088),
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#aacd84999061807220844be7fff48153e),
[App::PropertyMaterial](../../d0/df5/classApp_1_1PropertyMaterial.html#a26ab69643a00d4579ff90c1ebb84251b),
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#aca6dbdcb93d7a5800c0367974810fdf5),
[App::PropertyQuantityConstraint](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#aa887d76bf141becf6238408ee1b1e64a),
[App::PropertyAngle](../../d1/d5d/classApp_1_1PropertyAngle.html#a696bab3cd50bef40c0f33aa62b6de163),
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#a82b2bf666a9e0200b77a1a74203c9f8f),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a084057d252fc05436f7881c0986df98c),
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#a7b1b5d90cb0b8cc04b41c40b42003e2f),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#adb4d89095f4b08a557675d021c888d4f),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a1bd98f29491b7e75ac5f9e2a8a3063a4),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a1816e1bcf4421d1c329afe3455a86026),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#ae79ab583f5da4d60ba58f9258d7f8d22),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a90a55f07008b2770f8f94acf4cce8aae),
[App::PropertyXLinkSub](../../d4/da0/classApp_1_1PropertyXLinkSub.html#af18a39f9a42ea4ae3e720c2660c11c52),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a5d7a3cac74d30de8e1a220abf8fb8b7f),
[App::PropertyIntegerList](../../d7/daa/classApp_1_1PropertyIntegerList.html#afb0668d6ec5983c3f9d515101931460b),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#ad779632a643521abaab5e023d1a182af),
[App::PropertyStringList](../../d8/d55/classApp_1_1PropertyStringList.html#a9019dd758c545671f9415e52b2317610),
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#ab3207a968677118c28270ae50f396318),
and
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a6e594a242f968430bbfd0b773c7b19d5).

## ◆ getFullName()

std::string Property::getFullName  | ( | | ) |  const  
---|---|---|---|---  
  
References
[App::PropertyContainer::getFullName()](../../d5/d48/classApp_1_1PropertyContainer.html#a331110f1aeffb0a907ac2b74f78cc69d).

Referenced by
[SpreadsheetGui::DlgSheetConf::accept()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#aa4fefe42d2485471443e738600091ce0),
[StdCmdExpression::copyExpressions()](../../d2/dae/classStdCmdExpression.html#a993561611d4ef520e03fa4784ccbf520),
[App::PropertyExpressionEngine::execute()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a734f6ae9dbd4df6a8ebafee9a8d8bebd),
[Gui::ViewProviderDocumentObject::onChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
[App::PropertyEnumeration::setEnums()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a5571099202eda6dacf748996eedf6551),
[App::PropertyEnumeration::setEnumVector()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a265272a98d0ae08006973d863d9aba9d),
[Sketcher::SketchObject::setExpression()](../../d9/dad/classSketcher_1_1SketchObject.html#ad328e83eeb43879902e8fb12f35a7be6),
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede),
[App::PropertyEnumeration::setPyObject()](../../d4/df2/classApp_1_1PropertyEnumeration.html#aa715a8742ad95f4288e987f2f20d4719),
[Gui::Document::slotChangedObject()](../../de/d4e/classGui_1_1Document.html#a3886f48ebea3c1a519f8f0f1cf3f9d3e),
and
[Gui::Document::slotChangePropertyEditor()](../../de/d4e/classGui_1_1Document.html#a1739ac3e22ce824a933c8340644240a9).

## ◆ getGroup()

const char * Property::getGroup  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Get the group of this property.

References
[App::PropertyContainer::getPropertyGroup()](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356).

Referenced by
[App::DynamicProperty::addProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#afaada5859108dac4c73627edc1d5369e),
[App::LinkBaseExtension::isCopyOnChangeProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a832eacdf828db96b92137a17f223243d),
[Part::Primitive::onChanged()](../../d2/d31/classPart_1_1Primitive.html#ac5544f9b57ebf2a1b626450200a4bec0),
and
[App::LinkBaseExtension::setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e).

## ◆ getID()

int64_t App::Property::getID  | ( | | ) |  const  
---|---|---|---|---  
  
Return a unique ID for the property.

The ID of a property is generated from a monotonically increasing internal
counter. The intention of the ID is to be used as a key for mapping, instead
of using the raw pointer. Because, it is possible for the runtime memory
allocator to reuse just deleted memory, which will cause hard to debug problem
if use pointer as key.

Referenced by
[App::TransactionObject::addOrRemoveProperty()](../../d9/d02/classApp_1_1TransactionObject.html#a1a9c63db207f7e24ed6918877c134764),
and
[App::TransactionObject::setProperty()](../../d9/d02/classApp_1_1TransactionObject.html#ad234dbb98feea5e3fb448aa2b0825207).

## ◆ getMemSize()

| virtual unsigned [int](../../d1/da0/classint.html) App::Property::getMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").

See also

    [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence class and root of the type system.")

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9).

Reimplemented in
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#acf0627e62bf073aac01348d2781a5048),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#a4c9fe5dbd7d6842a0080cb8ea1d29260),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a9bb3a257e38b56ffd6395771c9f49539),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a5fb0c1063d6c1f8ee74d5bb12c114f03),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a3ee505b7da59d00f2abf78020a502ede),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a4c9fe5dbd7d6842a0080cb8ea1d29260),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a1ddc9de25c76ec9ade4d29a77e8b0664),
[Points::PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a75847bb599e4c1d12fb874c6a9775c48),
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#ac815825f1926b909f5138223e5f4a2ec),
[App::PropertyMatrix](../../d8/d77/classApp_1_1PropertyMatrix.html#a3cb1a922e29e35137aec11c7d91614ff),
[App::PropertyPythonObject](../../d7/d1d/classApp_1_1PropertyPythonObject.html#ac0947f60bbe89d193b47e229636004c1),
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#af3dc5d89e0377b785478fbfb2f0f1064),
[App::PropertyPath](../../dc/d24/classApp_1_1PropertyPath.html#a070c6c11a8fd1ecf96644985c9b8700f),
[App::PropertyIntegerSet](../../d0/df3/classApp_1_1PropertyIntegerSet.html#a8de3ce227ab32597ae3c903fedcac66d),
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html#a0a92013a1e026a536da4b4b8a5e74086),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a8c29971099b9581c77eef99b42218ad7),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#a1dacdc31bef9c42aa5da1b0cc1c628bc),
[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html#ae0cbcb1161e090b5ff249c4fc5a70f03),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#aa07a81452563bf739d36dcaec51429a3),
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#acfb47acb28b9927f07d24bcb1248c317),
[App::PropertyMaterial](../../d0/df5/classApp_1_1PropertyMaterial.html#a04fa2896f24ea0bd06223699ef813421),
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#a342c2d3d8b671357fa6654db21f352a3),
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#ae81b5620b77d2cc1831ad44910df1301),
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#ab30094bbea0f04d4ccc0c7f85488815e),
[Part::PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html#a63c36bfe30bbdfccb175cfd21659c3e4),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#a206503fb4c63200740b8d39c1c48f87e),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#ad190366d173d7c806c9072700cbc2cae),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a7d0e216876cfa009eeacb77bffaf9924),
[Path::PropertyPath](../../da/d75/classPath_1_1PropertyPath.html#a070c6c11a8fd1ecf96644985c9b8700f),
[Path::PropertyTool](../../d4/d51/classPath_1_1PropertyTool.html#adf84af3865b017b4e342e1cd8dbc6fbf),
[Path::PropertyTooltable](../../d4/d86/classPath_1_1PropertyTooltable.html#a0b7a308849d743524e7da5bae7979a24),
[Robot::PropertyTrajectory](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#a1bf4c5d61a30a4a92473dda0faffac51),
[TechDraw::PropertyCenterLineList](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a2a7bd2bbdbd92e080d7d599a0e8148b6),
[TechDraw::PropertyCosmeticEdgeList](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a10f0edf85c1bd933f329ccc3ca9d14a8),
[TechDraw::PropertyCosmeticVertexList](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a8e52149fbd49677ea09a15d3d5e09d6b),
[TechDraw::PropertyGeomFormatList](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#ac1dde1b7bc7de9e0ad57bc40f3e3a23a),
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a9c2ed33cbd8061fca8fb90a67aadf4cb),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a125d7701b320054ba27f96a1ce07eeb5),
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#aff4590ccda7a04bc8f92c30b4a3495e6),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a33e86ed95a033c93066f10d03b35fb17),
[App::PropertyPlacementList](../../d1/d76/classApp_1_1PropertyPlacementList.html#a45392f70e5990f85fd629a2c2add51b7),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a7467d6db2f6e7842e417ecc0d0f85bb7),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#ab78285bd88df778df0e28d4a849ab2a6),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a984b975e8df1de6523aa9588ad1a4751),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a05d3ff3e3e2e736467523e3fbc715df0),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a19431f105396ee0ea39fb438e0f72fef),
[App::PropertyIntegerList](../../d7/daa/classApp_1_1PropertyIntegerList.html#a7b812edb54403de064bed5a2dc2ea33d),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#a412587d903efffdb3abcaad4f4c73250),
[App::PropertyStringList](../../d8/d55/classApp_1_1PropertyStringList.html#a9ff58b5b4cdbe716aa81a3b025f782ab),
[App::PropertyBoolList](../../d1/dcf/classApp_1_1PropertyBoolList.html#aac54de337807ec4a440a3452a42f6810),
[App::PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#a84c1f4f40247c1cbce90a85d082206c9),
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a1c04e166a0692a748058db4772118c22),
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a8487b7c73af09eed5681c133040fb417),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#ac720a742459c231434f2c5ee0595abaf),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#adcb04008a5202a2f3eeacc2f10554e88).

Referenced by
[App::PropertyFileIncluded::getMemSize()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#acf0627e62bf073aac01348d2781a5048),
and
[isSame()](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

## ◆ getName()

const char * Property::getName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Get the name of this property in the belonging container With
[hasName()](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f)
it can be checked beforehand if a valid name is set.

Note

    If no name is set this function returns an empty string, i.e. "". 

Referenced by
[App::DynamicProperty::addProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#afaada5859108dac4c73627edc1d5369e),
[Gui::PropertyEditor::PropertyModel::appendProperty()](../../d3/da0/classGui_1_1PropertyEditor_1_1PropertyModel.html#a08e3f797f743b49c806400b30255dbf4),
[Gui::PropertyEditor::PropertyModel::buildUp()](../../d3/da0/classGui_1_1PropertyEditor_1_1PropertyModel.html#aca27cb3408b215833a07d92a37a9ccf3),
[Sketcher::PropertyConstraintList::canonicalPath()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#adb93af9df63a8a2b049bdc3c196dd84d),
[PartDesignGui::TaskHoleParameters::changedObject()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#af6c0941c01c80d87e2f97344958003be),
[App::LinkBaseExtension::checkCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6521528d36c644c2b1de74a2f74d82c0),
[PartDesign::SubShapeBinder::checkCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3698bc706a89765ff35db75048a08698),
[PartGui::ViewProviderSplineExtension::extensionUpdateData()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#ac0f6ab010c3a75a975e8ca3ad2ef60e2),
[Sketcher::PropertyConstraintList::getConstraint()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a14deae8735607e84f5995094be4d6838),
[getPaths()](../../d0/da9/classApp_1_1Property.html#a945f1c031f109242e362c5701516ff8e),
[Part::PropertyPartShape::getPaths()](../../d7/d28/classPart_1_1PropertyPartShape.html#a613e891f4e97c366bfce9a191006e3cf),
[Sketcher::PropertyConstraintList::getPyPathValue()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a54d45466b39acf29cb3ce26e587a522c),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[Spreadsheet::PropertySheet::isBindingPath()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ac3e598b1314e607dff8e216a20473e42),
[App::ObjectIdentifier::ObjectIdentifier()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2e87192f46ed457637f2b2d05abd01b7),
[PartGui::ViewProviderCustom::onChanged()](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
[SketcherGui::ViewProviderCustom::onChanged()](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
[PartDesign::Boolean::onChanged()](../../d2/d81/classPartDesign_1_1Boolean.html#a41c675a8b7f2f6e73b95946b99245f12),
[Gui::PropertyView::onTimer()](../../d8/d18/classGui_1_1PropertyView.html#aa53958cefcade980c3ffe795f787d6de),
[App::DocumentObjectT::operator=()](../../d5/d07/classApp_1_1DocumentObjectT.html#aa6d6b6131b81ccd65364482dd799199b),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[Inspection::PropertyDistanceList::Save()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a2f3aea08bb628f6a4c47cb757e79afec),
[Mesh::PropertyNormalList::Save()](../../df/dcd/classMesh_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Mesh::PropertyCurvatureList::Save()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[Part::PropertyFilletEdges::Save()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a0e7532f6fa496fb602617495364aed71),
[Points::PropertyGreyValueList::Save()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a44c4930cc7950e12f25b7d14d5fa906a),
[Points::PropertyNormalList::Save()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Points::PropertyCurvatureList::Save()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[App::PropertyVectorList::Save()](../../d5/d13/classApp_1_1PropertyVectorList.html#a5f00ee26daf66ffaa7bc7a6974c71467),
[App::PropertyPlacementList::Save()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a7e1537af27ac4c78360e5f75699b3a8e),
[App::PropertyFloatList::Save()](../../dc/d40/classApp_1_1PropertyFloatList.html#ab02594a5872688e133cc4eb300952ed6),
[App::PropertyColorList::Save()](../../d0/dc7/classApp_1_1PropertyColorList.html#a83eefd2fbd347e44e2c0d5e63b1bc2e1),
[App::PropertyMaterialList::Save()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a83f1b747fe9b8b41254e244294809f4a),
[Sketcher::PropertyConstraintList::setPathValue()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a2412c655ef32a277f98f2ae6bd659bcb),
[App::LinkBaseExtension::setProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770),
[ShapeCache::slotChanged()](../../d5/d4b/structShapeCache.html#a841f0e5c7bb644712b460afef8697db0),
[Gui::Document::slotChangedObject()](../../de/d4e/classGui_1_1Document.html#a3886f48ebea3c1a519f8f0f1cf3f9d3e),
[Spreadsheet::SheetObserver::slotChangedObject()](../../db/d2b/classSpreadsheet_1_1SheetObserver.html#afa0379ae388031e7371193ab6c5d6296),
[App::PropertyLinkBase::tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95),
[PartDesignGui::ViewProviderBody::unifyVisualProperty()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a9622d1e6a23c6497bea610755aea5713),
[Gui::ViewProviderAnnotation::updateData()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#acaee4ade8605ecc0ce997f273a931986),
[Gui::ViewProviderAnnotationLabel::updateData()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#aa2e79cd63adfc0a43501b66ffa4438dd),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[Gui::ViewProviderMeasureDistance::updateData()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a260762ea126ca4a70b60e5a825f2448d),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[FemGui::ViewProviderFemConstraintBearing::updateData()](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#a3b3cf2fa05760751890d9e1cf51f178f),
[FemGui::ViewProviderFemConstraintContact::updateData()](../../d9/d3d/classFemGui_1_1ViewProviderFemConstraintContact.html#a3ecf76e65206672a9355c60a533550c8),
[FemGui::ViewProviderFemConstraintDisplacement::updateData()](../../d7/d3f/classFemGui_1_1ViewProviderFemConstraintDisplacement.html#afb4b851d45e12b8639d1c4bedcaba4db),
[FemGui::ViewProviderFemConstraintFixed::updateData()](../../d4/d9c/classFemGui_1_1ViewProviderFemConstraintFixed.html#ab0717083d8637965bcafa54bfd839893),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintForce::updateData()](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#ad691cf23756106d6b0ea043ddebd1b94),
[FemGui::ViewProviderFemConstraintGear::updateData()](../../d1/d2f/classFemGui_1_1ViewProviderFemConstraintGear.html#a56f097a322b6fe5b2b4b7eead3374c49),
[FemGui::ViewProviderFemConstraintHeatflux::updateData()](../../d0/dea/classFemGui_1_1ViewProviderFemConstraintHeatflux.html#a3f1a55d2e70a5dca6b97d52c3e103aa0),
[FemGui::ViewProviderFemConstraintPlaneRotation::updateData()](../../d7/d0a/classFemGui_1_1ViewProviderFemConstraintPlaneRotation.html#a2b385e8a4903df418ef331257ad13a64),
[FemGui::ViewProviderFemConstraintPressure::updateData()](../../d4/d18/classFemGui_1_1ViewProviderFemConstraintPressure.html#a0280a478dea5288d50ba390ed1a50ca7),
[FemGui::ViewProviderFemConstraintPulley::updateData()](../../d8/dfc/classFemGui_1_1ViewProviderFemConstraintPulley.html#a7ba40d63d4dff464026a808438d3630b),
[FemGui::ViewProviderFemConstraintSpring::updateData()](../../d5/d4f/classFemGui_1_1ViewProviderFemConstraintSpring.html#a44c1119dd7d0bef3d9ef9c3229057e53),
[FemGui::ViewProviderFemConstraintTemperature::updateData()](../../d1/df6/classFemGui_1_1ViewProviderFemConstraintTemperature.html#a4c6f2f24780c8171d293ec933ae942ac),
[FemGui::ViewProviderFemConstraintTransform::updateData()](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#a2adf8aba7f15f7b95399068ab39c47b8),
[FemGui::ViewProviderFemPostFunctionProvider::updateData()](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a97688d1ce128f8dd922c10533f41d061),
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239),
[PartDesignGui::ViewProviderDatumCoordinateSystem::updateData()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a4ab1e86010986173acb70e3476f46a36),
[PartDesignGui::ViewProviderDatumLine::updateData()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a7ebcf854d3c32486f47eb377a39f4fa7),
[PartDesignGui::ViewProviderDatumPlane::updateData()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a0a10ea46fffce183ae92074bd2c6d754),
[Gui::ViewProviderDragger::updateData()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a6d433c9fe9d47fa7ab9be6d7e01d6509),
[PartGui::ViewProviderPartExt::updateData()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a5e0cc45b4148eee1b13cc43e9ff2518c),
[PartDesignGui::ViewProvider::updateData()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ae230b789ddc5d513656f4e87964bd01e),
[FemGui::ViewProviderFemPostPipeline::updateData()](../../df/d95/classFemGui_1_1ViewProviderFemPostPipeline.html#af073f80f627dfd4185dd1db10d56e79b),
[App::PropertyXLink::upgrade()](../../d2/de2/classApp_1_1PropertyXLink.html#ab593a78066f09572d98eac5046d8accf),
[App::PropertyXLinkSubList::upgrade()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2),
[App::PropertyXLinkSub::upgrade()](../../d4/da0/classApp_1_1PropertyXLinkSub.html#a0f3a85600e83e0f36d654f72939d9add),
and
[App::ObjectIdentifier::verify()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ae666a62d2fc3b423b86f3d370e6edb11).

## ◆ getPaths()

| void Property::getPaths  | ( | std::vector< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > & | _paths_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Get valid paths for this property; used by auto completer.

Reimplemented in
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a6af5a806aba72b420290e76516158d02),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#a613e891f4e97c366bfce9a191006e3cf),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a72578d93e87ea17b845b8173ac2a5b41),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#aa19d7736475e4226446cd94cf6f52a70),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a533c181be98ff243e893f11f4584b77e),
and
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#afe01f3c5baa6287719368bf4798096f3).

References
[getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
and
[getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a).

## ◆ getPathValue()

| const boost::any Property::getPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Get value of property.

Reimplemented in
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#a78d1a2705a515581e6b74c9fae27094b),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a84463f3456e11890c7e3061dc1592a74),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a429075152c75dbbd46e4bf5d7aeaac7d),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#a850b24499238db2470453d2db7000fac),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#ad5e2c285aa19b7472c8dfdd754636418),
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#ae735a34c955df358ef20a0c70b7b5c97),
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a5bc043e806eede3b4df9d21cbc2f44ef),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#aa15b728cf2f0a7a44b02f5b23fb10cf2),
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a315085c3eeb653dd65334a9d88c50fb8),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a7b199450301358b2d7a0c69f1d9cc174),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a06e19f55576a35cf180838f09991371e),
and
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#a4e2521f266b6bb0046d1182631998458).

Referenced by
[App::PropertyExpressionEngine::execute()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a734f6ae9dbd4df6a8ebafee9a8d8bebd),
[App::PropertyVector::getPathValue()](../../d5/d2b/classApp_1_1PropertyVector.html#a7b199450301358b2d7a0c69f1d9cc174),
[App::PropertyPlacement::getPathValue()](../../da/d51/classApp_1_1PropertyPlacement.html#a06e19f55576a35cf180838f09991371e),
[App::PropertyRotation::getPathValue()](../../df/d76/classApp_1_1PropertyRotation.html#a4e2521f266b6bb0046d1182631998458),
[App::ObjectIdentifier::getValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c),
and
[App::PropertyExpressionEngine::setValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a8297f68f6a223f63bd084feb727ddbe1).

## ◆ getPyPathValue()

| virtual [bool](../../d9/db9/classbool.html) App::Property::getPyPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | ,   
---|---|---|---  
|  | Py::Object & |   
| ) | |  const  
virtual  
  
Get Python value of property.

Reimplemented in
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a54d45466b39acf29cb3ce26e587a522c),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a1cf1f360d2873e83ce77ce6cf97f8322),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a52eed8c59886bb4f3daf36fdab868805),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a462af42ef4eadd19ca7645e961432b1c),
and
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#ab180787d5004b7196676ba10863f49f5).

Referenced by
[App::ObjectIdentifier::getPyValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a51896520089a0ba883333f2a6bcb56c6).

## ◆ getStatus()

unsigned long App::Property::getStatus  | ( | | ) |  const  
---|---|---|---|---  
  
return the status bits

Referenced by
[App::TransactionObject::addOrRemoveProperty()](../../d9/d02/classApp_1_1TransactionObject.html#a1a9c63db207f7e24ed6918877c134764),
and
[App::TransactionObject::setProperty()](../../d9/d02/classApp_1_1TransactionObject.html#ad234dbb98feea5e3fb448aa2b0825207).

## ◆ getType()

short Property::getType  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Get the type of the property in the container.

References
[Hidden](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014adef773114327b6ad987a0c47a4262a54),
[NoRecompute](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a8f31692acbbf9a5b8719e48fa68c5cde),
[Output](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a10640ff2cae2c1fda52dac13fc9a47a6),
[ReadOnly](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a06b1f9ba5fd320622558e264c1c096de),
and
[Transient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a14e77d5a09c2b0796490e697b68560e5).

Referenced by
[App::DynamicProperty::addProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#afaada5859108dac4c73627edc1d5369e),
[App::DynamicProperty::getPropertyType()](../../d5/d76/classApp_1_1DynamicProperty.html#a335e7f88a53ed325d69d3b7177731266),
[App::PropertyContainer::getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510),
[Gui::PropertyView::isPropertyHidden()](../../d8/d18/classGui_1_1PropertyView.html#ade658db91fd3ab831a793c30b7ca4d08),
[Gui::LinkView::onLinkedUpdateData()](../../da/d11/classGui_1_1LinkView.html#aaad340fbfa1074f4c41f7d26076281bd),
[App::LinkBaseExtension::update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979),
[PathScripts.PathToolEdit.ToolEditor::updateToolType()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a2ab9dc5c3f1a484ce30b642df4879fa3),
and
[PathScripts.PathToolEdit.ToolEditor::updateUI()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a901452eb82081a083d2b5d97ab8fe306).

## ◆ hasName()

[bool](../../d9/db9/classbool.html) Property::hasName  | ( | | ) |  const  
---|---|---|---|---  
  
Check if the property has a name set.

If no name is set then
[getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a)
will return an empty string

References
[isValidName()](../../d0/da9/classApp_1_1Property.html#ad8541be7b1fddd7f21f2ce3e18e8c06d).

Referenced by
[App::DynamicProperty::addProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#afaada5859108dac4c73627edc1d5369e),
[App::ObjectIdentifier::ObjectIdentifier()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2e87192f46ed457637f2b2d05abd01b7),
and
[App::DocumentObjectT::operator=()](../../d5/d07/classApp_1_1DocumentObjectT.html#aa6d6b6131b81ccd65364482dd799199b).

## ◆ hasSetChildValue()

| virtual void App::Property::hasSetChildValue  | ( | [Property](../../d0/da9/classApp_1_1Property.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
Called when a child property has changed value.

Reimplemented in
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a21901eb258fbc72a0b96f1072af2912b),
and
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a8d97a9deb398fd86589410728dc222bf).

Referenced by
[App::PropertyXLink::hasSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a).

## ◆ hasSetValue()

| void Property::hasSetValue  | ( | void  | | ) |   
---|---|---|---|---|---  
protectedvirtual  
  
Gets called by all setValue() methods after the value has changed.

Reimplemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ade4669436aaa4ddc2130f8756ca08585).

References
[Busy](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a5738c5d6491eb6a3385e22bb718a868a),
[App::PropertyContainer::onChanged()](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34),
[signalChanged](../../d0/da9/classApp_1_1Property.html#a9e9e25207ee1e619c75f835f9853cf74),
[StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67),
[testStatus()](../../d0/da9/classApp_1_1Property.html#aa0757bcb7ff02f8ece1205afd8a05775),
and
[Touched](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aa7412d0e7e6c015df9a22d89576953fe).

Referenced by
[Sketcher::PropertyConstraintList::acceptGeometry()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#acb51bc9feaf1b68d216e0935eb9713b0),
[Mesh::PropertyMeshKernel::finishEditing()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a20a7b75f7ce2ae3c9a44aa80f3e0009b),
[Points::PropertyPointKernel::finishEditing()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a93cdd367a32abd02fb17e3d13586361b),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[Fem::PropertyFemMesh::Paste()](../../db/da7/classFem_1_1PropertyFemMesh.html#a965e26482afb2059c98dbcfa70230efa),
[Fem::PropertyPostDataObject::Paste()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#acdb90785feaf0796b597c2637f1919d1),
[Mesh::PropertyNormalList::Paste()](../../df/dcd/classMesh_1_1PropertyNormalList.html#aff86a78b6515ca708ca90d2eb8e3170f),
[Mesh::PropertyCurvatureList::Paste()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a80ac8f07bde36bd7effec1a7fa0c5e05),
[Mesh::PropertyMeshKernel::Paste()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#aad26bbf7a9c35e7816c16f17f644c99a),
[Part::PropertyPartShape::Paste()](../../d7/d28/classPart_1_1PropertyPartShape.html#ad3ae131c1102191e8c0eaf5316a3f6cb),
[Path::PropertyPath::Paste()](../../da/d75/classPath_1_1PropertyPath.html#ae758022b28985b00dc1c597e01dc84e4),
[Path::PropertyTool::Paste()](../../d4/d51/classPath_1_1PropertyTool.html#ad2f095ac0f5007bd96c464f6fc193c77),
[Path::PropertyTooltable::Paste()](../../d4/d86/classPath_1_1PropertyTooltable.html#a064394956f97879bc8cac0cdebe0ccfc),
[Points::PropertyGreyValueList::Paste()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a47ed130632df3250ea0d9bbef1ab2034),
[Points::PropertyNormalList::Paste()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#aff86a78b6515ca708ca90d2eb8e3170f),
[Points::PropertyCurvatureList::Paste()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a80ac8f07bde36bd7effec1a7fa0c5e05),
[Points::PropertyPointKernel::Paste()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#ae94d61a1250982c96eb98c548667891d),
[Robot::PropertyTrajectory::Paste()](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#abb7e97000b92c95131bc4c4b31093d7f),
[App::PropertyFileIncluded::Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[App::PropertyMatrix::Paste()](../../d8/d77/classApp_1_1PropertyMatrix.html#a040858e6dc324655487a124bc2ccfafa),
[App::PropertyPythonObject::Paste()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a086c7bb8deef61645433e76eeb2fe3b0),
[App::PropertyInteger::Paste()](../../dd/d85/classApp_1_1PropertyInteger.html#a09abc5b0039b42f2b7c71fa707abcba9),
[App::PropertyPath::Paste()](../../dc/d24/classApp_1_1PropertyPath.html#a678a941b661da14440f66bccde5a12fe),
[App::PropertyIntegerSet::Paste()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#ab0e793f848a173a0eed7dc1c7cf5df4a),
[App::PropertyMap::Paste()](../../db/d3f/classApp_1_1PropertyMap.html#aefc83d68750955ffb88f7a1b70d983d5),
[App::PropertyFloat::Paste()](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf1f7c4fc4c8bde2ca9b8482180e45ff),
[App::PropertyUUID::Paste()](../../d2/d6c/classApp_1_1PropertyUUID.html#a04253297c6a35fc1036d4a456508807f),
[App::PropertyBool::Paste()](../../dc/d81/classApp_1_1PropertyBool.html#a884f68fe6a0d3bd3eddd54fe8f8abd32),
[App::PropertyColor::Paste()](../../d9/d0b/classApp_1_1PropertyColor.html#a6f089f8323aec6afbf91c66680581c69),
[App::PropertyMaterial::Paste()](../../d0/df5/classApp_1_1PropertyMaterial.html#a289a5c052d01968874da66c93cfa9fe3),
[Inspection::PropertyDistanceList::Paste()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#aefdcf03dac9fd7486f09dcc17905a718),
[Part::PropertyShapeHistory::Paste()](../../de/d7c/classPart_1_1PropertyShapeHistory.html#ad7af995f1b0ed7f92982638217f87538),
[Part::PropertyFilletEdges::Paste()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a8b0df89d4c6a3a5e8d8d062e2fc240ae),
[Spreadsheet::PropertySpreadsheetQuantity::Paste()](../../d2/dd4/classSpreadsheet_1_1PropertySpreadsheetQuantity.html#a2e105319857c2aa18ec56cb5a56b8f10),
[App::PropertyVector::Paste()](../../d5/d2b/classApp_1_1PropertyVector.html#a7ef832b4811885d30b97782e10afe042),
[App::PropertyPlacement::Paste()](../../da/d51/classApp_1_1PropertyPlacement.html#afbd1d98d3c19b17652f2306885da8815),
[App::PropertyRotation::Paste()](../../df/d76/classApp_1_1PropertyRotation.html#ab690c2b3639a616d6c156a391d3d9db8),
[App::PropertyPersistentObject::Paste()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aa32598aecbbb59a82597e21ef43b3273),
[App::PropertyFileIncluded::Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd),
[App::PropertyMatrix::Restore()](../../d8/d77/classApp_1_1PropertyMatrix.html#ac341d4242623336eafaf73bd16dfe8ad),
[App::PropertyPythonObject::Restore()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a7c4c1053b780d2f149cc99c86d3e39ff),
[App::PropertyEnumeration::Restore()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c),
[App::PropertyString::Restore()](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1),
[App::PropertyMaterial::Restore()](../../d0/df5/classApp_1_1PropertyMaterial.html#a9f1511c5fd99820c649307361c6c8880),
[Mesh::PropertyMeshKernel::Restore()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#ae5fd1c096fb6b3a70935261847e70115),
[Points::PropertyPointKernel::Restore()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a4e72a35a1ea913ffee981734df7e500f),
[App::PropertyVector::Restore()](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c),
[App::PropertyPlacement::Restore()](../../da/d51/classApp_1_1PropertyPlacement.html#a585fd1033be79f3fd3ebd0ae6fe8f734),
[App::PropertyRotation::Restore()](../../df/d76/classApp_1_1PropertyRotation.html#af641d12c42fa3ed2076e9d3f234ef31c),
[App::PropertyFileIncluded::RestoreDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#abaa879168b2300ffb4fdb20d3fdd4ef0),
[App::PropertyPythonObject::RestoreDocFile()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#af97b03d68515ca8bde89d895a1a6b08b),
[Fem::PropertyFemMesh::RestoreDocFile()](../../db/da7/classFem_1_1PropertyFemMesh.html#a57a423cdaccbe74d791cc980d9a9fd1a),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[Mesh::PropertyMeshKernel::RestoreDocFile()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a5150b28419d76cabc4f473f5daa59313),
[Path::PropertyPath::RestoreDocFile()](../../da/d75/classPath_1_1PropertyPath.html#a6ee2ea90ed9f02be32225df050ee9034),
[Points::PropertyPointKernel::RestoreDocFile()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a52466ad6689e8d30234bf5ec71b35646),
[Fem::PropertyPostDataObject::scale()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#ac071ffd68ec6bffde814f0fb88992fa9),
[Sketcher::PropertyConstraintList::set1Value()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#ac694be89d723e789b6f7574bf3cedd68),
[Part::PropertyGeometryList::set1Value()](../../db/dca/classPart_1_1PropertyGeometryList.html#a3a5edbc860880444fb39d59592917cf9),
[App::PropertyMaterial::setAmbientColor()](../../d0/df5/classApp_1_1PropertyMaterial.html#a337c7d6fc94fdc9ba4a4c5ae77f6d213),
[App::PropertyMaterial::setDiffuseColor()](../../d0/df5/classApp_1_1PropertyMaterial.html#a5c8fe036cb3b5bf9c7137b2e7fb4c2ef),
[App::PropertyMaterial::setEmissiveColor()](../../d0/df5/classApp_1_1PropertyMaterial.html#ada4905e18be3bb9a21ebe1b39a452622),
[App::PropertyEnumeration::setEnums()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a5571099202eda6dacf748996eedf6551),
[App::PropertyEnumeration::setEnumVector()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a265272a98d0ae08006973d863d9aba9d),
[Sketcher::PropertyConstraintList::setPathValue()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a2412c655ef32a277f98f2ae6bd659bcb),
[Mesh::PropertyMeshKernel::setPointIndices()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a7e421036a2b600d1b1a359c820ec95d3),
[App::PropertyPythonObject::setPyObject()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#abc4c47fe0adc00e73cf00e56223d058e),
[App::PropertyInteger::setPyObject()](../../dd/d85/classApp_1_1PropertyInteger.html#a01766b286f7ee23f14008042a2465044),
[App::PropertyEnumeration::setPyObject()](../../d4/df2/classApp_1_1PropertyEnumeration.html#aa715a8742ad95f4288e987f2f20d4719),
[App::PropertyIntegerConstraint::setPyObject()](../../d2/dc8/classApp_1_1PropertyIntegerConstraint.html#a59de0c197b75f6ad9e00c93bb02611b3),
[App::PropertyFloat::setPyObject()](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf2edab1753863426d8b78dd15dab006),
[App::PropertyFloatConstraint::setPyObject()](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#acb90ab8757a5dfcc66fbe2e468f0d342),
[App::PropertyQuantity::setPyObject()](../../d4/d65/classApp_1_1PropertyQuantity.html#a72be43d71c5e5a5e0a174c01df176dc9),
[App::PropertyMaterial::setShininess()](../../d0/df5/classApp_1_1PropertyMaterial.html#af40c06051021d1a02c4acd14f744b5d5),
[App::PropertyMaterial::setSpecularColor()](../../d0/df5/classApp_1_1PropertyMaterial.html#a391730862bfa2242449576428fdb8e10),
[App::PropertyMaterial::setTransparency()](../../d0/df5/classApp_1_1PropertyMaterial.html#a26538d6c721c101a7042e56b55131222),
[App::PropertyBool::setValue()](../../dc/d81/classApp_1_1PropertyBool.html#a8067462e38e7bb949ae31a86ec8ed17c),
[TechDraw::PropertyCenterLineList::setValue()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#ae68d0b3a613078dbdbec3f3e782b09b5),
[App::PropertyMatrix::setValue()](../../d8/d77/classApp_1_1PropertyMatrix.html#a15ef8f5f325db539295a77162cde3c29),
[App::PropertyPlacement::setValue()](../../da/d51/classApp_1_1PropertyPlacement.html#abb1f46e80061be4669b0ca20c83a7b31),
[App::PropertyRotation::setValue()](../../df/d76/classApp_1_1PropertyRotation.html#abbe10359c78a2b1fa074a8ddf0638773),
[App::PropertyUUID::setValue()](../../d2/d6c/classApp_1_1PropertyUUID.html#ab6d9418f4d048c0d0070c9c45a9233d2),
[App::PropertyVector::setValue()](../../d5/d2b/classApp_1_1PropertyVector.html#a866a1f59e997434cbe7e642af74301db),
[Mesh::PropertyNormalList::setValue()](../../df/dcd/classMesh_1_1PropertyNormalList.html#af79004fd1b518c6413ff1d11fca901fd),
[Points::PropertyNormalList::setValue()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#af79004fd1b518c6413ff1d11fca901fd),
[App::PropertyPath::setValue()](../../dc/d24/classApp_1_1PropertyPath.html#ad2d79969f6d45968031a1cd53a0dbc48),
[App::PropertyFileIncluded::setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[App::PropertyPersistentObject::setValue()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a117bd17a68a39872c084cf4e48401922),
[App::PropertyEnumeration::setValue()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a10973c61a7072bba34df37062aaa266d),
[App::PropertyColor::setValue()](../../d9/d0b/classApp_1_1PropertyColor.html#a4aab2001271a7767ba2e47c681286b27),
[Sketcher::PropertyConstraintList::setValue()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#acb1487eba8b8fd05122ef0e9d47679f1),
[Mesh::PropertyCurvatureList::setValue()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a6825a19dcfc3bfedf1718d20bf3d917d),
[Points::PropertyCurvatureList::setValue()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a6825a19dcfc3bfedf1718d20bf3d917d),
[Fem::PropertyFemMesh::setValue()](../../db/da7/classFem_1_1PropertyFemMesh.html#ae8e63278bec724a292ec4e1c3b6e07b7),
[Part::PropertyGeometryList::setValue()](../../db/dca/classPart_1_1PropertyGeometryList.html#a3fb0ae2bda56e1b5990bef9d980d53d9),
[TechDraw::PropertyGeomFormatList::setValue()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a15f264be3fd91839282f2454a1f92421),
[App::PropertyMaterial::setValue()](../../d0/df5/classApp_1_1PropertyMaterial.html#a4514e658133a9730c3ee62029b661c26),
[Mesh::PropertyMeshKernel::setValue()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a9d3aa33f749d3d5ecd9117f19e102609),
[Points::PropertyPointKernel::setValue()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#af9c758e102565b6510741fde550833d9),
[Part::PropertyShapeHistory::setValue()](../../de/d7c/classPart_1_1PropertyShapeHistory.html#ab13fab22f02c23c6667fcb7ec534bb57),
[App::PropertyMap::setValue()](../../db/d3f/classApp_1_1PropertyMap.html#acb8aa4cf5323671d12cdff5ee1554e09),
[Path::PropertyTool::setValue()](../../d4/d51/classPath_1_1PropertyTool.html#adcc535b5f8467c340d5287ca7588a62d),
[Path::PropertyPath::setValue()](../../da/d75/classPath_1_1PropertyPath.html#a66b0a2f5b8c2be68a7459f6ff0f7fccd),
[Path::PropertyTooltable::setValue()](../../d4/d86/classPath_1_1PropertyTooltable.html#abccad12c5ecaad48c6ec7c626d1edcd2),
[Part::PropertyPartShape::setValue()](../../d7/d28/classPart_1_1PropertyPartShape.html#a57ceb747ef13922fe2d4cce37f351c38),
[Robot::PropertyTrajectory::setValue()](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#a8029ad3ec29f20989d54e960598bf040),
[Fem::PropertyPostDataObject::setValue()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a2bf10e103cd77da0fb0180f324c2f871),
[TechDraw::PropertyCosmeticEdgeList::setValue()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#ad328e4ffd5d6fc23f07d07b5038fec0f),
[TechDraw::PropertyCosmeticVertexList::setValue()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a9a3945950d3b7616b40ab27cd92202b1),
[App::PropertyFloat::setValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#aeb4937e13aff58a04f81fdadf544f7d9),
[Inspection::PropertyDistanceList::setValue()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a7e8c326f0aa7c3bafd3246bd452d5681),
[Points::PropertyGreyValueList::setValue()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a2dd33f0fdfe14a78502d42dea9209847),
[Spreadsheet::PropertyColumnWidths::setValue()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#aaaf6b3782e9919f475a17bcbfb8e5c72),
[Part::PropertyFilletEdges::setValue()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a3bd1461a2917910d181fabf41251720e),
[Spreadsheet::PropertyRowHeights::setValue()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#ad5b6bd2fee64297348daa9b44051bd52),
[App::PropertyInteger::setValue()](../../dd/d85/classApp_1_1PropertyInteger.html#ac542ac41f9bad4ff220e906d7342d8ee),
[App::PropertyIntegerSet::setValue()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#ab27b4e25de1bef22752455bd8cb7ed23),
[App::PropertyPythonObject::setValue()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#aa7f9b4e9f7ce28c5465c905cc8baa6e6),
[Fem::PropertyFemMesh::setValuePtr()](../../db/da7/classFem_1_1PropertyFemMesh.html#a98f59a0e8b219f5abd4b1fd7cbc20a1e),
[Mesh::PropertyMeshKernel::setValuePtr()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#aeb6e1827257921773ab6b2bb3cfceea0),
[Spreadsheet::PropertyColumnWidths::setValues()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a0515c8aa45e70ed1409dfb4b070c1d01),
[Spreadsheet::PropertyRowHeights::setValues()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a0fc1931e77a169dd3413df6c2d0733b3),
[App::PropertyMap::setValues()](../../db/d3f/classApp_1_1PropertyMap.html#a7e543fd0696a33dec20006c615938510),
[App::PropertyIntegerSet::setValues()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#a33114deb128b23f8e2bff56c3bc98675),
[Mesh::PropertyNormalList::setValues()](../../df/dcd/classMesh_1_1PropertyNormalList.html#a160cd8e84fa526e3cbb2fb135ca0e612),
[Points::PropertyNormalList::setValues()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a160cd8e84fa526e3cbb2fb135ca0e612),
[TechDraw::PropertyCenterLineList::setValues()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a07b5c8f01d0398444e9ee5ab3b019b52),
[TechDraw::PropertyCosmeticEdgeList::setValues()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a0f1a31536f4f635d5d5add78b586c7da),
[TechDraw::PropertyCosmeticVertexList::setValues()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a3704b8b213643bc8a78b8bb16ed1ae8c),
[Mesh::PropertyCurvatureList::setValues()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#ad11bea58b7eb13bd540448bbdf4f2495),
[Points::PropertyCurvatureList::setValues()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#ad11bea58b7eb13bd540448bbdf4f2495),
[Part::PropertyFilletEdges::setValues()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a9c684a34571d703b5a42f1dee2a182ed),
[Inspection::PropertyDistanceList::setValues()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a2d90d0bd07c2addd2fceddc34a8ae9cc),
[Points::PropertyGreyValueList::setValues()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#ac761f627ad3d5d1afdbb7282040ac107),
[TechDraw::PropertyGeomFormatList::setValues()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#aa486b1faadc067963b4c9771255ddd91),
[Part::PropertyShapeHistory::setValues()](../../de/d7c/classPart_1_1PropertyShapeHistory.html#a57022bcba8c3f0ffdafb44e184e7451c),
[Sketcher::PropertyConstraintList::setValues()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a7886fa7b83544c271a2523424ed5fb54),
[Part::PropertyGeometryList::setValues()](../../db/dca/classPart_1_1PropertyGeometryList.html#a0c7ea8bd070c25a1877ac1edf911edda),
[Mesh::PropertyMeshKernel::swapMesh()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a82d1d54277c0bd59bac872a10a32ca38),
[Fem::PropertyFemMesh::transformGeometry()](../../db/da7/classFem_1_1PropertyFemMesh.html#a50d0dff44b30ea18254759b9dad46650),
[Mesh::PropertyNormalList::transformGeometry()](../../df/dcd/classMesh_1_1PropertyNormalList.html#a064a298f4261410fe6727a3bbd903ca9),
[Mesh::PropertyCurvatureList::transformGeometry()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a698d1e0cfd7a47a876f28ae6239bcfda),
[Mesh::PropertyMeshKernel::transformGeometry()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a2077e18fdbec8449fc028675946c3c71),
[Part::PropertyPartShape::transformGeometry()](../../d7/d28/classPart_1_1PropertyPartShape.html#aa7d347e5acb431ed5b43146266418569),
[Points::PropertyNormalList::transformGeometry()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a064a298f4261410fe6727a3bbd903ca9),
[Points::PropertyCurvatureList::transformGeometry()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a698d1e0cfd7a47a876f28ae6239bcfda),
and
[Points::PropertyPointKernel::transformGeometry()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#aac021bd95beaf0a0c89dda20c8959dc1).

## ◆ isReadOnly()

[bool](../../d9/db9/classbool.html) App::Property::isReadOnly  | ( | | ) |  const  
---|---|---|---|---  
  
References
[ReadOnly](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a06b1f9ba5fd320622558e264c1c096de).

Referenced by
[Gui::ExpressionBinding::apply()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a054996522e83552d345849bb9071b600),
[PartDesignGui::TaskHoleParameters::apply()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#a6cf3edb1b8421a2cf49e4af28635f13c),
[Gui::QuantitySpinBox::apply()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#ac3ec986d0729752d078f3c57a18f7cca),
[PartDesignGui::TaskHoleParameters::changedObject()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#af6c0941c01c80d87e2f97344958003be),
and
[PartDesignGui::TaskHoleParameters::TaskHoleParameters()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#aed07ebf7cad6b7cff0c7597137c91662).

## ◆ isSame()

| [bool](../../d9/db9/classbool.html) Property::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Compare if this property has the same content as the given one.

Reimplemented in
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a048b1c82d308cbef3911301fd596c4ef),
[App::PropertyMatrix](../../d8/d77/classApp_1_1PropertyMatrix.html#a28697d5a9c116da22f000f008905c571),
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#a70d2499769026e10fba6bc7a711aebb2),
[App::PropertyPath](../../dc/d24/classApp_1_1PropertyPath.html#adcdd24fcfaaf72e0bd6f8b57305186e4),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a516c0ea146e0da67db130812b58f5e49),
[App::PropertyIntegerSet](../../d0/df3/classApp_1_1PropertyIntegerSet.html#a5b3dcc5a39a3b54c0450229e4d9f3099),
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html#a232940d7c85e4ebbced00b78426032f4),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a386b26cdbb4e26dfd8e6340d3bb9ca5e),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#a33f0ebb36205838e6f94328870e60ac6),
[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html#aa8a6948ef082a962c3c4d1dac7e93dee),
[App::PropertyFont](../../df/d8c/classApp_1_1PropertyFont.html#a9bf6ebb41630ff61cecf13cf6436afca),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#abd96cbaefa1ebf8b44b844bfc4a60989),
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#adeb2113cc4d951709b1cb609cbadc977),
[App::PropertyMaterial](../../d0/df5/classApp_1_1PropertyMaterial.html#a363ae57fcaef5cc5de4ead589c5744da),
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#a223868a557555d8f3ea7e1eb647af452),
[App::PropertyListsT< T, ListT, ParentT
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyListsT< bool, boost::dynamic_bitset<>
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyListsT< Color
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyListsT< double
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyListsT< long
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyListsT< DocumentObject *, std::vector< DocumentObject * >,
PropertyLinkListBase
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyListsT< Material
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyListsT< Base::Placement
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyListsT< std::string
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyListsT< Base::Vector3d
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a6e4d497b46c90c57f0a6c4f95be4237e),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a3645ce165f801b3aef3bfdda4ada6c83),
and
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a80edc3aa77b975c9862ca4ff78179407).

References
[getMemSize()](../../d0/da9/classApp_1_1Property.html#a933a44c77e539e1942227d1f266d3330),
[Base::StringWriter::getString()](../../dd/ddf/classBase_1_1StringWriter.html#aff861785ca83f8b71be6575059c733db),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
and
[Base::Persistence::Save()](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436).

## ◆ isSinglePrecision()

[bool](../../d9/db9/classbool.html) App::Property::isSinglePrecision  | ( | | ) |  const  
---|---|---|---|---  
  
Gets precision of properties using floating point numbers.

References
[Single](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a9c73483be20c75fd4c35af435a108ff6).

Referenced by
[App::PropertyVectorList::RestoreDocFile()](../../d5/d13/classApp_1_1PropertyVectorList.html#a889f6a81c93feae64c452de8cca4e4f9),
[App::PropertyPlacementList::RestoreDocFile()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a22b5814f0d97c838f30c9abd1c8db26d),
[App::PropertyFloatList::RestoreDocFile()](../../dc/d40/classApp_1_1PropertyFloatList.html#a3ec9c1ade28cff79be19ad914c63c9aa),
[App::PropertyVectorList::SaveDocFile()](../../d5/d13/classApp_1_1PropertyVectorList.html#a36ef88c4cd85ee0fc26f8f49a8342e12),
[App::PropertyPlacementList::SaveDocFile()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a7a5c65d0ae1925916f9bc4af21bf7172),
and
[App::PropertyFloatList::SaveDocFile()](../../dc/d40/classApp_1_1PropertyFloatList.html#a824104f367e47aa1dba79edfe6372d57).

## ◆ isTouched()

[bool](../../d9/db9/classbool.html) App::Property::isTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Test if this property is touched.

Referenced by
[Part::PrismExtension::extensionMustExecute()](../../d3/dbb/classPart_1_1PrismExtension.html#a453fe13add0ad7646860fabec9db3b19),
[App::RangeExpression::isTouched()](../../da/d8b/classApp_1_1RangeExpression.html#a93b55327da44e753b97eca89a2ec8c7c),
[Inspection::Feature::mustExecute()](../../d6/d23/classInspection_1_1Feature.html#a0d724ccdc0ab0a12d64857429f8ed6e5),
[Mesh::Curvature::mustExecute()](../../d2/d39/classMesh_1_1Curvature.html#a6af7b48ccba04340a5a6a2d1b683b86f),
[Mesh::FixDefects::mustExecute()](../../d4/d1f/classMesh_1_1FixDefects.html#a60719ab5d4ea4f23061a3cd88913f9c8),
[Mesh::Export::mustExecute()](../../d6/d40/classMesh_1_1Export.html#af08e8f0650d1a809006084471fe51e10),
[Mesh::Import::mustExecute()](../../d9/d29/classMesh_1_1Import.html#aa1fcc3c110cdd83510ccd3bb6fffe0d1),
[Mesh::SegmentByMesh::mustExecute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#ae266a9b9fa667055d01165b431ea99eb),
[Mesh::SetOperations::mustExecute()](../../d3/d8f/classMesh_1_1SetOperations.html#a4f5806f8ade3aad44cb8e973436418aa),
[Mesh::Sphere::mustExecute()](../../d1/d57/classMesh_1_1Sphere.html#af382230622ae40b9001837c010914d55),
[Mesh::Ellipsoid::mustExecute()](../../d2/dd6/classMesh_1_1Ellipsoid.html#a04b71856c085f1d22a52051fbfbdeab2),
[Mesh::Cylinder::mustExecute()](../../df/def/classMesh_1_1Cylinder.html#a378eb9b322c47ba68f82b63a3ba8a774),
[Mesh::Cone::mustExecute()](../../d4/dbc/classMesh_1_1Cone.html#a3e9ef98790cc1bb43811caad58800b6d),
[Mesh::Torus::mustExecute()](../../de/da3/classMesh_1_1Torus.html#a9ba7a1c1f9c10906a6b2871015a245ed),
[Mesh::Cube::mustExecute()](../../df/d68/classMesh_1_1Cube.html#a17e86f858cd8e0e152bed618bc89f8ab),
[Part::Compound::mustExecute()](../../d7/d98/classPart_1_1Compound.html#a9aa9e6647f6cff757c27044a8761589b),
[Part::Mirroring::mustExecute()](../../dc/dac/classPart_1_1Mirroring.html#a73f8f26306e463477a806f64f8dc6bc9),
[Part::Boolean::mustExecute()](../../da/d3a/classPart_1_1Boolean.html#af3f085bc4a0685aa0b35b9ed302909ed),
[Part::Box::mustExecute()](../../dc/d80/classPart_1_1Box.html#a9f9122055de9f9f54330344d6f0f4d2f),
[Part::Circle::mustExecute()](../../de/de4/classPart_1_1Circle.html#ae53749f4a3ec7d47c793836e8b434e39),
[Part::MultiCommon::mustExecute()](../../d1/df7/classPart_1_1MultiCommon.html#aff038d0605f8d867e78b1f476d13a423),
[Part::CurveNet::mustExecute()](../../d9/d41/classPart_1_1CurveNet.html#a14c067b4244e435b95caed0239061a67),
[Part::MultiFuse::mustExecute()](../../df/dbc/classPart_1_1MultiFuse.html#a78d68db386d413d51ceee293c9c69f72),
[Part::ImportBrep::mustExecute()](../../d8/d3e/classPart_1_1ImportBrep.html#ac9a27ad3e42210d02c9e37e13de11225),
[Part::ImportIges::mustExecute()](../../d2/d1d/classPart_1_1ImportIges.html#a5e6c69a25c001e6fce1c225bb00946d8),
[Part::ImportStep::mustExecute()](../../d4/de2/classPart_1_1ImportStep.html#a4a9b9f2ccd0f686db6f8b17913f497f2),
[Part::Section::mustExecute()](../../d8/dea/classPart_1_1Section.html#a59b8614ab4d782e3a75c19f4eb7ac04c),
[Part::FilletBase::mustExecute()](../../df/d7d/classPart_1_1FilletBase.html#a1605b11985fc17752b770a2d6345912c),
[Part::RuledSurface::mustExecute()](../../d1/d41/classPart_1_1RuledSurface.html#a58f9902136f476eb15446fc2ee5d8736),
[Part::Loft::mustExecute()](../../d3/d52/classPart_1_1Loft.html#a4268e155f3ca5d5454ba26a201b46a8c),
[Part::Sweep::mustExecute()](../../df/dc6/classPart_1_1Sweep.html#abad4b8648adea18b61116ac5bd589f16),
[Part::Thickness::mustExecute()](../../db/d73/classPart_1_1Thickness.html#a5e19889c98eff816988ec695a3630027),
[Part::Vertex::mustExecute()](../../de/d96/classPart_1_1Vertex.html#a070647e2216331349695e034b7953b11),
[Part::Line::mustExecute()](../../d3/dfe/classPart_1_1Line.html#a52dc004fe03c7c0b2533a79e90582b76),
[Part::Plane::mustExecute()](../../d0/d1c/classPart_1_1Plane.html#adeb8f292f17dd8ea85f6a10e4ff5a217),
[Part::Sphere::mustExecute()](../../dc/d57/classPart_1_1Sphere.html#af382230622ae40b9001837c010914d55),
[Part::Ellipsoid::mustExecute()](../../d4/dc8/classPart_1_1Ellipsoid.html#a04b71856c085f1d22a52051fbfbdeab2),
[Part::Cylinder::mustExecute()](../../dd/d12/classPart_1_1Cylinder.html#a378eb9b322c47ba68f82b63a3ba8a774),
[Part::Prism::mustExecute()](../../dc/d69/classPart_1_1Prism.html#acbfb605c398b843511d88049827933f0),
[Part::RegularPolygon::mustExecute()](../../d2/d69/classPart_1_1RegularPolygon.html#ade525f0226ae5b2724a38c311afca7cc),
[Part::Cone::mustExecute()](../../d2/d8f/classPart_1_1Cone.html#a3e9ef98790cc1bb43811caad58800b6d),
[Part::Torus::mustExecute()](../../db/d42/classPart_1_1Torus.html#a9ba7a1c1f9c10906a6b2871015a245ed),
[Part::Helix::mustExecute()](../../df/d49/classPart_1_1Helix.html#a8b11a6cb96966e4d2f78bc2aa6202e8b),
[Part::Spiral::mustExecute()](../../d2/d3f/classPart_1_1Spiral.html#a9cba924aad8fd3e76ff441a3961226f8),
[Part::Wedge::mustExecute()](../../d5/dc5/classPart_1_1Wedge.html#a9ecc8acaa8cad5f383598c95e8f81b9f),
[Part::Ellipse::mustExecute()](../../d6/d22/classPart_1_1Ellipse.html#aadc4a277ba0371628877326ccb173656),
[PartDesign::FeatureExtrude::mustExecute()](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a7416081060d0046a4ee5f75b6cf96745),
[PartDesign::Fillet::mustExecute()](../../d0/d50/classPartDesign_1_1Fillet.html#a5b3a59c8e278d4f36512e98f3c29c5e3),
[PartDesign::Groove::mustExecute()](../../d7/de3/classPartDesign_1_1Groove.html#af2c45ee71298e5f2243c8ea28f2d5f06),
[PartDesign::Helix::mustExecute()](../../d3/d78/classPartDesign_1_1Helix.html#a8b11a6cb96966e4d2f78bc2aa6202e8b),
[PartDesign::Hole::mustExecute()](../../dd/dd0/classPartDesign_1_1Hole.html#aabba1b579d01ed80e02dd3cbe96e268f),
[PartDesign::LinearPattern::mustExecute()](../../d2/d86/classPartDesign_1_1LinearPattern.html#af148fe0fbc866c4e875f348ee00ac15b),
[PartDesign::Loft::mustExecute()](../../d0/deb/classPartDesign_1_1Loft.html#a4268e155f3ca5d5454ba26a201b46a8c),
[PartDesign::Mirrored::mustExecute()](../../d6/d91/classPartDesign_1_1Mirrored.html#ad52caeb5b8f56f79ff493ad0e055fc4c),
[PartDesign::MultiTransform::mustExecute()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a6ac7f7f11d9b701e73a719ba2ca8c273),
[PartDesign::Pipe::mustExecute()](../../da/d61/classPartDesign_1_1Pipe.html#a1be7d941c0a219aac9b3e1f6bce37725),
[PartDesign::PolarPattern::mustExecute()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5ec374b41f2ef38848bc86424ff95740),
[PartDesign::Box::mustExecute()](../../df/d97/classPartDesign_1_1Box.html#ad4c0259f9361582e56b130542f075c94),
[PartDesign::Cylinder::mustExecute()](../../dc/d28/classPartDesign_1_1Cylinder.html#a34b2d2eaaa139e81d104668a55b528df),
[PartDesign::Sphere::mustExecute()](../../db/d9d/classPartDesign_1_1Sphere.html#a7af784560b0e4a7f02feffe2b50e9a20),
[PartDesign::Cone::mustExecute()](../../d4/d2b/classPartDesign_1_1Cone.html#aaf85a9e73ac84c02c4ae965bf301794b),
[PartDesign::Ellipsoid::mustExecute()](../../d4/de1/classPartDesign_1_1Ellipsoid.html#ab9deacc288cf4f1294f063d5fabfaf95),
[PartDesign::Torus::mustExecute()](../../dd/de1/classPartDesign_1_1Torus.html#a9c940d8c26ff13297f4d8352a547fde5),
[PartDesign::Prism::mustExecute()](../../d9/daf/classPartDesign_1_1Prism.html#a22492cb9418358d702012f95e64c5381),
[PartDesign::Wedge::mustExecute()](../../dc/dd3/classPartDesign_1_1Wedge.html#a18c1e204e8024c403d34e3b075a04ed9),
[PartDesign::Revolution::mustExecute()](../../d2/de6/classPartDesign_1_1Revolution.html#a3a2eebb70794151bf41bbfdfd374eae6),
[PartDesign::Scaled::mustExecute()](../../db/dce/classPartDesign_1_1Scaled.html#aa2be088b02bd721f4b4d4b598950958a),
[PartDesign::ProfileBased::mustExecute()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a4b3aef4d73c5e46762d8425eacf4594f),
[PartDesign::Thickness::mustExecute()](../../d4/d22/classPartDesign_1_1Thickness.html#a5e19889c98eff816988ec695a3630027),
[PartDesign::Transformed::mustExecute()](../../dd/de1/classPartDesign_1_1Transformed.html#aca66717047b204e50ad27e3929aea1cb),
[Raytracing::LuxFeature::mustExecute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a3f50e58889e6b8f6038ac7cd53264696),
[Raytracing::LuxProject::mustExecute()](../../d5/de6/classRaytracing_1_1LuxProject.html#a748457d7f93d46b6fa8fb16386969d9f),
[Raytracing::RayFeature::mustExecute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a1f423b19b1164c9526bc19db42232bcb),
[Raytracing::RayProject::mustExecute()](../../d2/d89/classRaytracing_1_1RayProject.html#af0f006304c9fe6e872879522904f0a4c),
[Sketcher::SketchObjectSF::mustExecute()](../../de/da4/classSketcher_1_1SketchObjectSF.html#ae6f07ad80580bdc95ba0bf4b2719b3c6),
[Surface::Cut::mustExecute()](../../d4/d17/classSurface_1_1Cut.html#a55fae0653fcb2808913a690f838f6842),
[Surface::Filling::mustExecute()](../../d8/df7/classSurface_1_1Filling.html#aa4e2a1f2b2ecdfcbd01ac7a1be5eb36b),
[Surface::GeomFillSurface::mustExecute()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a6b2b02a9d8eaa29985780aa19cdd8d5e),
[Surface::Sewing::mustExecute()](../../d2/d52/classSurface_1_1Sewing.html#a4f9f2fc30c894b4b2a23978b2bee7456),
[TechDraw::DrawRichAnno::mustExecute()](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#a0341116c3475965fc7cc3a586c8bd04f),
[TechDraw::DrawViewClip::mustExecute()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a27db71239b73197269ace8ca79e9dcb2),
[TechDraw::DrawViewCollection::mustExecute()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a3ff9756e1b5b8cb29c5b0f775a8d8c01),
[TechDraw::DrawViewSpreadsheet::mustExecute()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a0d02700cc490d94542c4508ccfc9757e),
[Part::Extrusion::mustExecute()](../../db/d6c/classPart_1_1Extrusion.html#a228b96c5264e131bf450cc5bf8674fe1),
[Part::Face::mustExecute()](../../dc/dbf/classPart_1_1Face.html#ae50cc97eb56db33e2878a41283101cc7),
[Part::Offset::mustExecute()](../../d0/dda/classPart_1_1Offset.html#a0d2e23d767643dc89b30cce4c84a1132),
[Part::Offset2D::mustExecute()](../../d7/dcf/classPart_1_1Offset2D.html#aff31be8bdeac470626e5208a65edc610),
[Part::Revolution::mustExecute()](../../d3/d17/classPart_1_1Revolution.html#a2e361e3b8f4ad563de04c16977530c80),
[PartDesign::Body::mustExecute()](../../dd/db8/classPartDesign_1_1Body.html#a7b11bf3c246fb3c0feb327b4cc2eb259),
[PartDesign::FeatureAddSub::mustExecute()](../../d0/dd5/classPartDesign_1_1FeatureAddSub.html#a9d10deea7eb3a39ef2064c07ce89a74b),
[PartDesign::Boolean::mustExecute()](../../d2/d81/classPartDesign_1_1Boolean.html#acc9ed4028be42a906bc3c46697efe969),
[PartDesign::Chamfer::mustExecute()](../../da/d6f/classPartDesign_1_1Chamfer.html#a3f61714b5aa58b68ccb2ac3f0fed02c9),
[Sketcher::SketchObject::mustExecute()](../../d9/dad/classSketcher_1_1SketchObject.html#ad0e97ac78dbd3665e8a8ce21d2b45a2e),
[Surface::Extend::mustExecute()](../../d1/d22/classSurface_1_1Extend.html#a157b5d79910ff33715ba9bca92a5fde4),
[TechDraw::DrawGeomHatch::mustExecute()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a261eed9b0f2c16df4253f8e782cf6e22),
[TechDraw::DrawHatch::mustExecute()](../../d0/d97/classTechDraw_1_1DrawHatch.html#af5ab8197a7fd3f3e1656978578ddd30f),
[TechDraw::DrawLeaderLine::mustExecute()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#aa1f85707a4c5d5974a462a801a9199c5),
[TechDraw::DrawPage::mustExecute()](../../d9/d5a/classTechDraw_1_1DrawPage.html#af83c44feed62a393d9c5ea850bbaed6b),
[TechDraw::DrawProjGroup::mustExecute()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aaa53b26d779cb3e5913afb2637fcf86e),
[TechDraw::DrawProjGroupItem::mustExecute()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a1bac249755bbc6f7881cd128158ae2a8),
[TechDraw::DrawView::mustExecute()](../../d6/d1c/classTechDraw_1_1DrawView.html#aecb782507679f383bfd5a8cb8ca285aa),
[TechDraw::DrawViewArch::mustExecute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#ac0b004990afa16dc78271e9c4cc24066),
[TechDraw::DrawViewBalloon::mustExecute()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#aed4962d1295f9c197a7abf5187884606),
[TechDraw::DrawViewDetail::mustExecute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#aab3cbf1f8a5acb302771e4a23d5914fe),
[TechDraw::DrawViewDimension::mustExecute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a0e048384fc02fd7ef9f4a79bcfeb247b),
[TechDraw::DrawViewDraft::mustExecute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#ad28b6173d701cf3d0b168cfb8505b68a),
[TechDraw::DrawViewImage::mustExecute()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a6ea5454abb51f0c48c8a790dbf5a86c9),
[TechDraw::DrawViewMulti::mustExecute()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a883d222a6968a9cc812f483772dccf3d),
[TechDraw::DrawViewPart::mustExecute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#abd4f001ec919dbcad7113202c3cb9349),
[TechDraw::DrawViewSection::mustExecute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a654004aaa97316eb1174ee24199227b1),
[TechDraw::DrawViewSymbol::mustExecute()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a9f50f90e3bb3f3304e78d31e32202088),
[App::Origin::mustExecute()](../../d9/d8b/classApp_1_1Origin.html#a01df202f898e80abb2fcca9c95f75d10),
[Fem::FemPostClipFilter::mustExecute()](../../dc/d06/classFem_1_1FemPostClipFilter.html#ad9b5a128c02d29ef5fdcc762716240ac),
[Fem::FemPostDataAlongLineFilter::mustExecute()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#af836732e27e998bcfc2791ecf7b78e6b),
[Fem::FemPostDataAtPointFilter::mustExecute()](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#a129b8b6e1e1e568884df55b28887cfa3),
[Fem::FemPostScalarClipFilter::mustExecute()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#ae46d689646a2b308e078cbeac3d32f4f),
[Fem::FemPostWarpVectorFilter::mustExecute()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a2845626ff54c894fcdfc595e3b877cf0),
[Fem::FemPostCutFilter::mustExecute()](../../da/d89/classFem_1_1FemPostCutFilter.html#a8878962978592c040f1f90e389b4b6d0),
[Fem::FemPostPipeline::mustExecute()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a078fd5b14f636a2d1eb723edd86bc761),
[PartDesign::FeatureBase::mustExecute()](../../d2/d7c/classPartDesign_1_1FeatureBase.html#adb39ba7172cf948740e55f8d00daeb96),
[Sandbox::SandboxObject::mustExecute()](../../da/dd9/classSandbox_1_1SandboxObject.html#a020585a3fecab3300bfcc90d7a396db8),
[PartDesign::ShapeBinder::mustExecute()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#ad87d2c4e8ff00afa0730be5b3c7dae94),
and
[TechDrawGui::MDIViewPage::updateTemplate()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5dad0574c1df0a7c6398e90173300461).

## ◆ isValidName()

| [bool](../../d9/db9/classbool.html) Property::isValidName  | ( | const char *  | _name_| ) |   
---|---|---|---|---|---  
static  
  
Check if the passed name is valid.

If _name_ is null or an empty string it's considered invalid, and valid
otherwise.

Referenced by
[hasName()](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f),
[App::LinkBaseExtension::setProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770),
and
[ShapeCache::slotChanged()](../../d5/d4b/structShapeCache.html#a841f0e5c7bb644712b460afef8697db0).

## ◆ onContainerRestored()

| virtual void App::Property::onContainerRestored  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Called before calling
[DocumentObject::onDocumentRestored()](../../d2/de4/classApp_1_1DocumentObject.html#a0ee8399fa0b176c64895150691a4b604
"get called after a document has been fully restored")

This function is called after finished calling
[Property::afterRestore()](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f
"Called at the beginning of Document::afterRestore\(\)") of all properties of
objects. By then, the object dependency information is assumed ready. So,
unlike
[Property::afterRestore()](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f
"Called at the beginning of Document::afterRestore\(\)"), this function is
called on objects with dependency order.

Reimplemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a733f20b00486b5e21694ee2607fdae92),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a1ad3eb4664b30fde709d6af5a8ca10a4),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a1cd3b87ac48e486bbc2ea858e069ff98),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a907c0f4bd96da3bad11eb35ac11acf3f),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ae5784f7e4394d2d7be363cca3abaf2d4),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a1eb52a89dd270eb5d2562665b0bbfdca).

## ◆ Paste()

| void Property::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
pure virtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Implemented in
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#a965e26482afb2059c98dbcfa70230efa),
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#acdb90785feaf0796b597c2637f1919d1),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#aff86a78b6515ca708ca90d2eb8e3170f),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a80ac8f07bde36bd7effec1a7fa0c5e05),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#aad26bbf7a9c35e7816c16f17f644c99a),
[Part::PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html#aaf67c007d98a5d3ea9f01aa8da7bfb3d),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#ad3ae131c1102191e8c0eaf5316a3f6cb),
[Path::PropertyPath](../../da/d75/classPath_1_1PropertyPath.html#ae758022b28985b00dc1c597e01dc84e4),
[Path::PropertyTool](../../d4/d51/classPath_1_1PropertyTool.html#ad2f095ac0f5007bd96c464f6fc193c77),
[Path::PropertyTooltable](../../d4/d86/classPath_1_1PropertyTooltable.html#a064394956f97879bc8cac0cdebe0ccfc),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a47ed130632df3250ea0d9bbef1ab2034),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#aff86a78b6515ca708ca90d2eb8e3170f),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a80ac8f07bde36bd7effec1a7fa0c5e05),
[Points::PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#ae94d61a1250982c96eb98c548667891d),
[Robot::PropertyTrajectory](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#abb7e97000b92c95131bc4c4b31093d7f),
[Spreadsheet::PropertyRowHeights](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a667dc8e0bead95e86f05d3572e736f87),
[TechDraw::PropertyCenterLineList](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a84817a407463a150d9cb12e8ec15d5f4),
[TechDraw::PropertyCosmeticEdgeList](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#acd4d65b2893f3a6d764735ea5ede09d3),
[TechDraw::PropertyCosmeticVertexList](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a222119d0664df6840d3484fcc7d14047),
[TechDraw::PropertyGeomFormatList](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a4b3af7e757bfda0606d6b2bc2a0f7c2e),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a22c36ef831bf3389d2b003b1e2defbab),
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[App::PropertyMatrix](../../d8/d77/classApp_1_1PropertyMatrix.html#a040858e6dc324655487a124bc2ccfafa),
[App::PropertyPlacementLink](../../d8/db5/classApp_1_1PropertyPlacementLink.html#aa08172316e8d59b648dcc5ac8266d56e),
[App::PropertyPythonObject](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a086c7bb8deef61645433e76eeb2fe3b0),
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#a09abc5b0039b42f2b7c71fa707abcba9),
[App::PropertyPath](../../dc/d24/classApp_1_1PropertyPath.html#a678a941b661da14440f66bccde5a12fe),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#ae2c1a5b1f45a128b3a82bcab504a7d52),
[App::PropertyIntegerSet](../../d0/df3/classApp_1_1PropertyIntegerSet.html#ab0e793f848a173a0eed7dc1c7cf5df4a),
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html#aefc83d68750955ffb88f7a1b70d983d5),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf1f7c4fc4c8bde2ca9b8482180e45ff),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#a181a70a04d92e6c994a55550abf484c9),
[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html#a04253297c6a35fc1036d4a456508807f),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#a884f68fe6a0d3bd3eddd54fe8f8abd32),
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#a6f089f8323aec6afbf91c66680581c69),
[App::PropertyMaterial](../../d0/df5/classApp_1_1PropertyMaterial.html#a289a5c052d01968874da66c93cfa9fe3),
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7f06f64a7f7fc8b42cc72470e96b6c46),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a7ef832b4811885d30b97782e10afe042),
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#a1adb31e01fbe8277ff607655f77b3fdb),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#afbd1d98d3c19b17652f2306885da8815),
[App::PropertyPlacementList](../../d1/d76/classApp_1_1PropertyPlacementList.html#a07000cd0e83997a0d246c6463ae175a8),
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#ab690c2b3639a616d6c156a391d3d9db8),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a31b305bd16358bc6459e33bf47e1c2b6),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a4395718ac6e9c8f221569c4de1933ba9),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a5514822b7ffa4a3ebaf2c8a569d0df67),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a3dfbcd135189c2b3e6e7c6136ed572a1),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a6d593eed6217cccfdad4a79a4c752c27),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4ac663947ed88fa49f3a874273098fe4),
[App::PropertyIntegerList](../../d7/daa/classApp_1_1PropertyIntegerList.html#a59b5e62226f10aa81edc3b6b94dfdffc),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#a1e22185187992fb6bc4b1aad9cbffc63),
[App::PropertyStringList](../../d8/d55/classApp_1_1PropertyStringList.html#a035f8cf48a225eb47ac0eb1cedf1fe6d),
[App::PropertyBoolList](../../d1/dcf/classApp_1_1PropertyBoolList.html#abdc3545d43eb32557d3247ed28f1c4eb),
[App::PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#a09999f92abcf033497c84ee02a28a23b),
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#add94172decc9894d19c40eb44148dd1e),
and
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aa32598aecbbb59a82597e21ef43b3273).

Referenced by
[PartDesignGui::TaskFeaturePick::makeCopy()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a9e9b1a639025522ada407aaa6b19596e),
and
[PartDesignGui::ViewProviderBody::unifyVisualProperty()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a9622d1e6a23c6497bea610755aea5713).

## ◆ purgeTouched()

void App::Property::purgeTouched  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Reset this property touched.

Referenced by
[TechDraw::DrawProjGroup::addProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acfc4e756c8714973996318393180f483),
[TechDraw::DrawView::checkScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#ad2da2acbc02345e15a55d357ef545914),
[TechDraw::DrawProjGroup::execute()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a53036ad3632d51fe082b67c8f829b54f),
[TechDraw::DrawProjGroupItem::execute()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a1afd35db151cf4ec222427f08a4f3c2a),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewPart::execute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[TechDraw::DrawView::handleXYLock()](../../d6/d1c/classTechDraw_1_1DrawView.html#a3d108f5068fc2ab85015a47a99aaf1ed),
[TechDraw::DrawViewBalloon::handleXYLock()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a924bf9891e29a267dcd39bd902a3f895),
[TechDraw::DrawView::onChanged()](../../d6/d1c/classTechDraw_1_1DrawView.html#a2980fbae4ce0a12aae609193764465cf),
[TechDraw::DrawViewDetail::onChanged()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[Gui::Application::reopen()](../../d9/da8/classGui_1_1Application.html#a7a21dfd4379a11fd6babb3a2a14d4b1a),
[PathGui::ViewProviderPath::updateShowConstraints()](../../db/d31/classPathGui_1_1ViewProviderPath.html#af157d0410d852ca2fc864da7bc95be5e),
[PathGui::ViewProviderPath::updateVisual()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ab5ef44e05264d65aecc762660f342d58),
and
[TechDraw::DrawView::validateScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#ab9bb446a2ce1a400ffe1aa00daf6cdd0).

## ◆ setContainer()

void Property::setContainer  | ( | [PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *  | _Father_| ) |   
---|---|---|---|---|---  
  
Is called by the framework to set the father (container)

Referenced by
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[Part::Chamfer::execute()](../../d7/d75/classPart_1_1Chamfer.html#a4e556c2713a9af1290a0c53eeedff2f1),
[Part::Compound::execute()](../../d7/d98/classPart_1_1Compound.html#a72d02534883bc8e2b7ccb46218e87087),
[Part::Fillet::execute()](../../d4/da4/classPart_1_1Fillet.html#a3d2e483fe0b72a9d09d5945fe7e36e65),
[Part::Part2DObject::handleChangedPropertyType()](../../d9/d57/classPart_1_1Part2DObject.html#a3b4551d03504c25446ede14dcf2309e3),
[TechDraw::DrawPage::handleChangedPropertyType()](../../d9/d5a/classTechDraw_1_1DrawPage.html#adde1799122996153278b2c68d4fa9b80),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[App::PropertyLinkSubList::upgrade()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b),
[App::PropertyXLinkSubList::upgrade()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2),
[App::PropertyXLinkSub::upgrade()](../../d4/da0/classApp_1_1PropertyXLinkSub.html#a0f3a85600e83e0f36d654f72939d9add),
and
[Gui::ViewProviderDocumentObject::~ViewProviderDocumentObject()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#af764f01205eb1475038ec1b302cd9b35).

## ◆ setPathValue()

| void Property::setPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | const boost::any & | _value_  
| ) | |   
virtual  
  
Set value of property.

Reimplemented in
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#a86cf2a8be4f311966bb89cdec37a0991),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a48af9a6606d16a14476ee19bd9cc28cc),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#ac5c0dfec5810e2860c64bb7186b2462a),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#abedefbc95eb8ac85e06453ac11806bec),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#a21b072ecae3082e2c8dfb2605469f9ef),
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#af017ce248b34f5378b3a714aa270c421),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a2412c655ef32a277f98f2ae6bd659bcb),
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a6d23bb97bf03cce4b60bc747167e5003),
and
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#a7524b793cd14e2a152bc020265b48fa3).

Referenced by
[App::PropertyExpressionEngine::execute()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a734f6ae9dbd4df6a8ebafee9a8d8bebd),
[App::PropertyPlacement::setPathValue()](../../da/d51/classApp_1_1PropertyPlacement.html#a6d23bb97bf03cce4b60bc747167e5003),
and
[App::PropertyRotation::setPathValue()](../../df/d76/classApp_1_1PropertyRotation.html#a7524b793cd14e2a152bc020265b48fa3).

## ◆ setReadOnly()

void Property::setReadOnly  | ( | [bool](../../d9/db9/classbool.html) | _readOnly_| ) |   
---|---|---|---|---|---  
  
Sets property editable/grayed out in property editor.

References
[ReadOnly](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a06b1f9ba5fd320622558e264c1c096de),
and
[setStatus()](../../d0/da9/classApp_1_1Property.html#a2f10dba2d265461344c6df7d0a40ad4e).

Referenced by
[PartDesign::FeatureExtrude::computeDirection()](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a3af51bee887de0bc89953128cb0a4d1c),
[PartDesign::Pad::execute()](../../d9/d14/classPartDesign_1_1Pad.html#a17b37a5aaa299709fbb066564ef25b3e),
[Part::AttachExtension::extensionOnChanged()](../../dc/d47/classPart_1_1AttachExtension.html#ac73db2d8f32ca41b89157b47edce44c1),
[PartDesign::Hole::Hole()](../../dd/dd0/classPartDesign_1_1Hole.html#a4c1598e38f425df417a962a8fe1f8f30),
[PartDesign::Line::onChanged()](../../d0/d2a/classPartDesign_1_1Line.html#a9da12fed7c1a5cfa4af5c06af23c6fff),
[PartDesign::Plane::onChanged()](../../df/df0/classPartDesign_1_1Plane.html#a82dfdf47875b49263a5275ab1ff3c686),
[PartDesign::Hole::onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[Part::Revolution::onChanged()](../../d3/d17/classPart_1_1Revolution.html#a9940a58886c8d7d0b4b009082d81f14c),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
and
[Part::AttachExtension::onExtendedDocumentRestored()](../../dc/d47/classPart_1_1AttachExtension.html#a6af7f6139ae7d3aef649ff3e89d05d75).

## ◆ setSinglePrecision()

void App::Property::setSinglePrecision  | ( | [bool](../../d9/db9/classbool.html) | _single_| ) |   
---|---|---|---|---|---  
  
Sets precision of properties using floating point numbers to single, the
default is double.

References
[Single](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a9c73483be20c75fd4c35af435a108ff6).

## ◆ setStatus()

void Property::setStatus  | ( | [Status](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014) | _pos_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _on_  
| ) | |   
  
References
[setStatusValue()](../../d0/da9/classApp_1_1Property.html#a32cf2f8513b5a66b0b39c839c559f20b),
and
[StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67).

Referenced by
[SpreadsheetGui::DlgSheetConf::accept()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#aa4fefe42d2485471443e738600091ce0),
[MeshGui::ViewProviderMesh::attach()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#adb9b6c0cd97337657aabd81bac13e35e),
[TechDraw::DrawViewAnnotation::DrawViewAnnotation()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#ab1f6da36b5eea808ba75ea9f8bfe9bb5),
[TechDraw::DrawViewBalloon::DrawViewBalloon()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a2aa449f36b009ff5a461c4702bbe22cb),
[TechDraw::DrawViewDimension::DrawViewDimension()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aa6fad2118f8e0478d358978ef57e2dc4),
[TechDraw::DrawViewDimExtent::DrawViewDimExtent()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#a7f429eefbfc67b7cc454405c9595307a),
[Part::AttachExtension::extensionOnChanged()](../../dc/d47/classPart_1_1AttachExtension.html#ac73db2d8f32ca41b89157b47edce44c1),
[Part::Circle::handleChangedPropertyName()](../../de/de4/classPart_1_1Circle.html#aac14a5128cb8850c0cd7f37ffc71e22a),
[Part::Ellipse::handleChangedPropertyName()](../../d6/d22/classPart_1_1Ellipse.html#a7448b87a31bf68edc8d6a6909613615b),
[TechDraw::DrawView::handleXYLock()](../../d6/d1c/classTechDraw_1_1DrawView.html#a3d108f5068fc2ab85015a47a99aaf1ed),
[TechDraw::DrawViewBalloon::handleXYLock()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a924bf9891e29a267dcd39bd902a3f895),
[Part::Box::onChanged()](../../dc/d80/classPart_1_1Box.html#a29bcbc46ec0749e4035fffc5117e1723),
[PartDesign::ProfileBased::onChanged()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a36fd19fd597799ebeccd8eddd104bdf4),
[TechDraw::DrawView::onChanged()](../../d6/d1c/classTechDraw_1_1DrawView.html#a2980fbae4ce0a12aae609193764465cf),
[TechDraw::DrawViewDetail::onChanged()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[PartDesign::FeatureBase::onDocumentRestored()](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a88645629a13677f1034ae2023481c2a1),
[Part::AttachExtension::onExtendedDocumentRestored()](../../dc/d47/classPart_1_1AttachExtension.html#a6af7f6139ae7d3aef649ff3e89d05d75),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Gui::ViewProviderLink::setElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#af274c7d8619bfae997be5ea17b7c72b3),
[App::LinkBaseExtension::setProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770),
[setReadOnly()](../../d0/da9/classApp_1_1Property.html#a8d9c78a46b9b79dc637cf70e1224c222),
[TechDraw::DrawView::setScaleAttribute()](../../d6/d1c/classTechDraw_1_1DrawView.html#a2027c216e3dc8f25f5c40a6b465decf9),
[MeshGui::ViewProviderMesh::updateData()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#acfabc68fbd4cb6188071e498739066d8),
[TechDrawGui::ViewProviderRichAnno::updateData()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a4e1c30466784136f53ab33c2cdee4b16),
[Gui::ViewProviderLink::updateDataPrivate()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2f2113e0017af3819a9064380ed30d0d),
[PartDesign::Chamfer::updateProperties()](../../da/d6f/classPartDesign_1_1Chamfer.html#ae0070da00a2612084082be5bef23e63b),
[PartDesignGui::ViewProviderDatum::ViewProviderDatum()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#adf0685fe5a17533d5150eee8e625d03a),
[Gui::ViewProviderLink::ViewProviderLink()](../../d6/d59/classGui_1_1ViewProviderLink.html#ac80b32ec9821edd74f1e39d58951773d),
and
[Gui::ViewProviderTextDocument::ViewProviderTextDocument()](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a64987c999f5eadaa7f68cd0756578af4).

## ◆ setStatusValue()

void Property::setStatusValue  | ( | unsigned long  | _status_| ) |   
---|---|---|---|---|---  
  
References
[Busy](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a5738c5d6491eb6a3385e22bb718a868a),
[Hidden](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014adef773114327b6ad987a0c47a4262a54),
[App::PropertyContainer::onPropertyStatusChanged()](../../d5/d48/classApp_1_1PropertyContainer.html#a25dc796f1aecab39ceeed8335097b758),
[PropDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a610d527a8ef20b533504b5121a983d80),
[PropHidden](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aab1086519565f4fa2cc26a504daa92d3),
[PropNoPersist](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ae221473138e52da3001d1de060205179),
[PropNoRecompute](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a78b230717c2b517e7875c4211612b764),
[PropOutput](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a7610516494d96a531206dc3e1fe94f57),
[PropReadOnly](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a75dc207c45c9bf592c42415e987e7d5e),
[PropTransient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a49215d8e9f6a5a24523e5ce094fb867e),
[ReadOnly](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a06b1f9ba5fd320622558e264c1c096de),
and
[StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67).

Referenced by
[App::TransactionObject::applyChn()](../../d9/d02/classApp_1_1TransactionObject.html#ae828131a91ad93ac2f20a51eeadecf70),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
and
[setStatus()](../../d0/da9/classApp_1_1Property.html#a2f10dba2d265461344c6df7d0a40ad4e).

## ◆ testStatus()

[bool](../../d9/db9/classbool.html) App::Property::testStatus  | ( | [Status](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014) | _pos_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[Gui::PropertyEditor::PropertyModel::appendProperty()](../../d3/da0/classGui_1_1PropertyEditor_1_1PropertyModel.html#a08e3f797f743b49c806400b30255dbf4),
[PartDesignGui::ViewProviderBody::canDropObjects()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adcc9d80b22970ff32d5f7663363f6c63),
[App::GeoFeatureGroupExtension::extensionOnChanged()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487),
[App::GroupExtension::extensionOnChanged()](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f),
[App::LinkBaseExtension::extensionOnChanged()](../../da/dd9/classApp_1_1LinkBaseExtension.html#acfd0dd3d0677653d2da7fc2a4cdcd3c5),
[App::PropertyMaterial::getEditorName()](../../d0/df5/classApp_1_1PropertyMaterial.html#a26ab69643a00d4579ff90c1ebb84251b),
[App::PropertyMaterialList::getEditorName()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#ab3207a968677118c28270ae50f396318),
[TechDraw::DrawView::handleXYLock()](../../d6/d1c/classTechDraw_1_1DrawView.html#a3d108f5068fc2ab85015a47a99aaf1ed),
[TechDraw::DrawViewBalloon::handleXYLock()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a924bf9891e29a267dcd39bd902a3f895),
[hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
[App::LinkBaseExtension::isCopyOnChangeProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a832eacdf828db96b92137a17f223243d),
[Gui::PropertyView::isPropertyHidden()](../../d8/d18/classGui_1_1PropertyView.html#ade658db91fd3ab831a793c30b7ca4d08),
[Part::Box::onChanged()](../../dc/d80/classPart_1_1Box.html#a29bcbc46ec0749e4035fffc5117e1723),
[Gui::ViewProviderDocumentObject::onChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[PartDesign::SubShapeBinder::onChanged()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a525834748579d35e2e8ecbf9cd18bf3d),
[Gui::LinkView::onLinkedUpdateData()](../../da/d11/classGui_1_1LinkView.html#aaad340fbfa1074f4c41f7d26076281bd),
[Gui::PropertyView::onTimer()](../../d8/d18/classGui_1_1PropertyView.html#aa53958cefcade980c3ffe795f787d6de),
[Gui::ViewProviderDocumentObject::removeDynamicProperty()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a4d47313a825a2051c9a667ed4e7a1346),
[Part::Circle::Restore()](../../de/de4/classPart_1_1Circle.html#a31f09d03f0ee6b6f7a9e98b20b7223d4),
[Part::Ellipse::Restore()](../../d6/d22/classPart_1_1Ellipse.html#a90f7d460c9b3b2d2cf7b07282ad83efd),
[Gui::Document::slotChangedObject()](../../de/d4e/classGui_1_1Document.html#a3886f48ebea3c1a519f8f0f1cf3f9d3e),
[App::LinkBaseExtension::update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979),
and
[Gui::ViewProviderLink::updateDataPrivate()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2f2113e0017af3819a9064380ed30d0d).

## ◆ touch()

void Property::touch  | ( | | ) |   
---|---|---|---|---  
  
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") status handling.

Set the property touched

References
[App::PropertyContainer::onChanged()](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34),
[StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67),
and
[Touched](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aa7412d0e7e6c015df9a22d89576953fe).

Referenced by
[Sketcher::SketchObject::addCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#a2ae92a618d60a264ed20d7a359b89f98),
[Sketcher::SketchObject::addSymmetric()](../../d9/dad/classSketcher_1_1SketchObject.html#afcbb1d6f5a99e52a70fdf6d9d3c9d361),
[Spreadsheet::PropertySheet::afterRestore()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a094d3eb343aaa42ace2817a85f8dee3a),
[Gui::ViewProviderPythonFeatureImp::attach()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a7fe9943f935cd2bd115ffc3814901564),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[Sketcher::PropertyConstraintList::checkGeometry()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a2da6be9cc57e68a9e8aa9eb3c12dd5e5),
[Sketcher::SketchObject::convertToNURBS()](../../d9/dad/classSketcher_1_1SketchObject.html#a23e6660388fbe498a07b07a8c4f065fe),
[Sketcher::SketchObject::deleteAllGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#aadc2acd5b73193824fa27f1c19141d02),
[Sketcher::SketchObject::delGeometriesExclusiveList()](../../d9/dad/classSketcher_1_1SketchObject.html#ab5a3748762c070a9eb006c467947fc3f),
[Sketcher::SketchObject::delGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a40dfaae474c808c67807476529431053),
[App::Document::Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[Gui::ViewProviderTextDocument::doubleClicked()](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a5e666f0a1cab99aba3ce00094a9cb351),
[Fem::Constraint::execute()](../../d0/d11/classFem_1_1Constraint.html#ac7343ea84455e2331eecd8aab10b38ac),
[Part::Feature::execute()](../../d7/d7e/classPart_1_1Feature.html#ac06f7886d25ae7ef0e9e635904f7997c),
[Part::Chamfer::execute()](../../d7/d75/classPart_1_1Chamfer.html#a4e556c2713a9af1290a0c53eeedff2f1),
[Part::Compound::execute()](../../d7/d98/classPart_1_1Compound.html#a72d02534883bc8e2b7ccb46218e87087),
[Part::Fillet::execute()](../../d4/da4/classPart_1_1Fillet.html#a3d2e483fe0b72a9d09d5945fe7e36e65),
[TechDraw::DrawTemplate::execute()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a67d8e151c886e0ef62f246cc3a4e5ff6),
[Sketcher::SketchObject::insertBSplineKnot()](../../d9/dad/classSketcher_1_1SketchObject.html#a48c6d4c74904307c87c4e8f65a9e89af),
[Spreadsheet::PropertySheet::invalidateDependants()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ae30f4ba5574b7048482105523fac6de0),
[Sketcher::SketchObject::modifyBSplineKnotMultiplicity()](../../d9/dad/classSketcher_1_1SketchObject.html#ae318b60c226c883e53725f9ebef29991),
[Fem::ConstraintBearing::onChanged()](../../df/d0a/classFem_1_1ConstraintBearing.html#ae81d9fda05994bd43bf81faf3acae5d6),
[Fem::ConstraintGear::onChanged()](../../d8/d55/classFem_1_1ConstraintGear.html#a971506b4ca246c3378e2755160ed4772),
[Fem::ConstraintPulley::onChanged()](../../d3/dec/classFem_1_1ConstraintPulley.html#a6c23af9b8ba29b03f25163da9b75a41f),
[Fem::ConstraintTransform::onChanged()](../../d8/d3c/classFem_1_1ConstraintTransform.html#a38b893dee34272ad6bf0c6126aad561f),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[Fem::Constraint::onDocumentRestored()](../../d0/d11/classFem_1_1Constraint.html#abfe82aef4be1b70b5f33c93b6ba6da33),
[Fem::FemPostPlaneFunction::onDocumentRestored()](../../dd/d76/classFem_1_1FemPostPlaneFunction.html#a0073f416d7cb5a2ce3f3a97d9459f1c8),
[Part::Datum::onDocumentRestored()](../../db/d0b/classPart_1_1Datum.html#aee993e2bbdc3cc6997f293b29bdad4b3),
[PartDesign::Body::onDocumentRestored()](../../dd/db8/classPartDesign_1_1Body.html#aa6affc475d3884d9570838e731749605),
[App::VRMLObject::RestoreDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a90cb824c6253de535ec16e1935455599),
[App::Document::saveAs()](../../d8/d3e/classApp_1_1Document.html#a99cf956cb95ce19b87c4ea7e1d5087ee),
[Gui::AlignmentGroup::setAlignable()](../../dc/d5e/classGui_1_1AlignmentGroup.html#a921830caf78e809033bc775808106cbb),
[Sketcher::SketchObject::setUpSketch()](../../d9/dad/classSketcher_1_1SketchObject.html#abcb2e853ecf4a1923bdf65d8ecf09e95),
[Sketcher::SketchObject::solve()](../../d9/dad/classSketcher_1_1SketchObject.html#a0bcef04719586a7122d762061b2d4ac4),
[PartGui::ViewProviderPartExt::unsetHighlightedEdges()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a015e0a4c10afc8926e6f3b3bee780966),
[PartGui::ViewProviderPartExt::unsetHighlightedFaces()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#aa6269b29872d4bfbaf6cf5495fdae356),
[PartGui::ViewProviderPartExt::unsetHighlightedPoints()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a1f6ecc30677bbe673cec6ba43269c28f),
[PathGui::ViewProviderPath::updateVisual()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ab5ef44e05264d65aecc762660f342d58),
and
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed).

## ◆ verifyPath()

| void Property::verifyPath  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _p_| ) |  const  
---|---|---|---|---|---  
protectedvirtual  
  
Verify a path for the current property.

Referenced by
[App::PropertyFloat::getPathValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#a429075152c75dbbd46e4bf5d7aeaac7d),
[App::PropertyString::getPathValue()](../../dd/df8/classApp_1_1PropertyString.html#a850b24499238db2470453d2db7000fac),
[App::PropertyBool::getPathValue()](../../dc/d81/classApp_1_1PropertyBool.html#ad5e2c285aa19b7472c8dfdd754636418),
[App::PropertyInteger::setPathValue()](../../dd/d85/classApp_1_1PropertyInteger.html#a86cf2a8be4f311966bb89cdec37a0991),
[App::PropertyFloat::setPathValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#ac5c0dfec5810e2860c64bb7186b2462a),
[App::PropertyString::setPathValue()](../../dd/df8/classApp_1_1PropertyString.html#abedefbc95eb8ac85e06453ac11806bec),
and
[App::PropertyBool::setPathValue()](../../dc/d81/classApp_1_1PropertyBool.html#a21b072ecae3082e2c8dfb2605469f9ef).

## Friends And Related Function Documentation

## ◆ DynamicProperty

| [friend](../../d7/d23/classfriend.html) class
[DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html)  
---  
friend  
  
## ◆ PropertyContainer

| [friend](../../d7/d23/classfriend.html) class
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
---  
friend  
  
## ◆ PropertyData

| [friend](../../d7/d23/classfriend.html) struct
[PropertyData](../../d2/d02/structApp_1_1PropertyData.html)  
---  
friend  
  
## Member Data Documentation

## ◆ signalChanged

boost::signals2::signal<void (const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Property::signalChanged  
---  
  
Referenced by
[hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

## ◆ StatusBits

| std::bitset<32> App::Property::StatusBits  
---  
protected  
  
Status bits of the property The first 8 bits are used for the base system the
rest can be used in descendent classes to mark special statuses on the
objects.

The bits and their meaning are listed below: 0 - object is marked as 'touched'
1 - object is marked as 'immutable' 2 - object is marked as 'read-only' (for
property editor) 3 - object is marked as 'hidden' (for property editor)

Referenced by
[App::PropertyFileIncluded::aboutToSetValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ab556673fad52c8535774ab736c61a40f),
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[App::PropertyFileIncluded::Copy()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a8357945cf4e3e84abd535ef6d53d4f99),
[hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[setStatus()](../../d0/da9/classApp_1_1Property.html#a2f10dba2d265461344c6df7d0a40ad4e),
[setStatusValue()](../../d0/da9/classApp_1_1Property.html#a32cf2f8513b5a66b0b39c839c559f20b),
and
[touch()](../../d0/da9/classApp_1_1Property.html#a9bec8b8a56b405be0dc5e1602b079475).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Property.h
  * FreeCAD/src/App/Property.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

