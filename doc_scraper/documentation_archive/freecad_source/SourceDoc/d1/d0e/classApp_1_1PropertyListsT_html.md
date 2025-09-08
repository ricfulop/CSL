---
url: https://freecad.github.io/SourceDoc/d1/d0e/classApp_1_1PropertyListsT.html
scraped_at: 2025-09-08T14:56:22.996146
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)

[List of all members](../../d5/d6c/classApp_1_1PropertyListsT-members.html) | Public Types | Public Member Functions | Public Attributes | Protected Member Functions

App::PropertyListsT< T, ListT, ParentT > Class Template Referenceabstract

Helper class to implement
[PropertyLists](../../d4/da1/classApp_1_1PropertyLists.html "Base class of all
property lists.").
[More...](../../d1/d0e/classApp_1_1PropertyListsT.html#details)

`#include <Property.h>`

##  Public Types  
  
---  
typedef [AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)< [PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT > >::AtomicPropertyChange | [atomic_change](../../d1/d0e/classApp_1_1PropertyListsT.html#ac461d1a7873429bac88827a89d979438)  
typedef ListT::const_reference | [const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5)  
typedef ListT | [list_type](../../d1/d0e/classApp_1_1PropertyListsT.html#ab1c519424072c713a1b2d32b5e9264af)  
typedef ParentT | [parent_type](../../d1/d0e/classApp_1_1PropertyListsT.html#a423c6bad5d316ae7195a68d4ff5dc946)  
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
  
##  Public Member Functions  
  
---  
virtual [int](../../d1/da0/classint.html) | [getSize](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194) (void) const override  
const ListT & | [getValue](../../d1/d0e/classApp_1_1PropertyListsT.html#a064f87de752ea68f9a660c10ba3dcf4b) (void) const  
const ListT & | [getValues](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938) (void) const  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const override  
| Compare if this property has the same content as the given one.
[More...](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109)  
  
[const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) | [operator[]](../../d1/d0e/classApp_1_1PropertyListsT.html#a8d9939f872f9aa1ff103027249f99036) ([int](../../d1/da0/classint.html) idx) const  
virtual void | [set1Value](../../d1/d0e/classApp_1_1PropertyListsT.html#ada9ee7ea1e2127ba7456b9a4a4697d80) ([int](../../d1/da0/classint.html) index, [const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) value)  
virtual void | [setPyObject](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2) ([PyObject](../../df/d1b/classPyObject.html) *value) override  
virtual void | [setSize](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9) ([int](../../d1/da0/classint.html) newSize) override  
virtual void | [setSize](../../d1/d0e/classApp_1_1PropertyListsT.html#a3d8817fe93f3db9c3d32dcecafbfd061) ([int](../../d1/da0/classint.html) newSize, [const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) def)  
void | [setValue](../../d1/d0e/classApp_1_1PropertyListsT.html#a39353cb8c1c869664480e455fc076f19) (const ListT &newValues=ListT())  
void | [setValue](../../d1/d0e/classApp_1_1PropertyListsT.html#abaaa23d8c4ff48e19290cf81a62f6e94) ([const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) value)  
virtual void | [setValues](../../d1/d0e/classApp_1_1PropertyListsT.html#a8744f95234dbfb9431759906c2a76cd4) (const ListT &newValues=ListT())  
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
  
##  Public Attributes  
  
---  
[friend](../../d7/d23/classfriend.html) | [atomic_change](../../d1/d0e/classApp_1_1PropertyListsT.html#a0eb905df14c931335baa2fcfcb851bca)  
![-](../../closed.png) Public Attributes inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
boost::signals2::signal< void(const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChanged](../../d0/da9/classApp_1_1Property.html#a9e9e25207ee1e619c75f835f9853cf74)  
  
##  Protected Member Functions  
  
---  
virtual T | [getPyValue](../../d1/d0e/classApp_1_1PropertyListsT.html#a0048578553b52a7697ca08bcd71249b0) ([PyObject](../../df/d1b/classPyObject.html) *item) const =0  
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
[App::AtomicPropertyChangeInterface< PropertyListsT< T, std::vector< T >,
PropertyLists >
>](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)  
|
[AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#aab004d1fbf131c11d570dcfcad7c22e1)
()  
  
##  Additional Inherited Members  
  
---  
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
[App::AtomicPropertyChangeInterface< PropertyListsT< T, std::vector< T >,
PropertyLists >
>](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)  
[bool](../../d9/db9/classbool.html) | [hasChanged](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a1e6d78782f81aef5d1efe58ac219e2df)  
[int](../../d1/da0/classint.html) | [signalCounter](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a07e13a81f4f601365b04cc8806d075f9)  
| Counter for invoking transaction start/stop.
[More...](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a07e13a81f4f601365b04cc8806d075f9)  
  
  
## Detailed Description

template<class T, class ListT = std::vector<T>, class ParentT = PropertyLists>  
class App::PropertyListsT< T, ListT, ParentT >

Helper class to implement
[PropertyLists](../../d4/da1/classApp_1_1PropertyLists.html "Base class of all
property lists.").

## Member Typedef Documentation

## ◆ atomic_change

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

typedef
[AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)<[PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)<T,ListT,ParentT>>::AtomicPropertyChange
[App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT,
ParentT >::atomic_change  
---  
  
## ◆ const_reference

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

typedef ListT::const_reference
[App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT,
ParentT >::const_reference  
---  
  
## ◆ list_type

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

typedef ListT
[App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT,
ParentT >::list_type  
---  
  
## ◆ parent_type

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

typedef ParentT
[App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT,
ParentT >::parent_type  
---  
  
## Member Function Documentation

## ◆ getPyValue()

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

| virtual T [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::getPyValue  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _item_| ) |  const  
---|---|---|---|---|---  
protectedpure virtual  
  
Implemented in
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#ad0f80e66d1ff38fe21ca46873897f4ea),
[App::PropertyPlacementList](../../d1/d76/classApp_1_1PropertyPlacementList.html#a484851efa9ed5f430cc13d9a20c820b7),
[App::PropertyBoolList](../../d1/dcf/classApp_1_1PropertyBoolList.html#ad50cbd85fe79e8c81ed7e2775b3065a0),
[App::PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#a1185ac555445591be3ab82499256987f),
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a4f80734f14139984b3b97b0acb4563d0),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a1dff0cfef5f1726834499af38e35af8b),
[App::PropertyIntegerList](../../d7/daa/classApp_1_1PropertyIntegerList.html#a72e5932bc9b39e3cbb85bb23b9c308be),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#a27483de4f04619adaa31cbd405255969),
and
[App::PropertyStringList](../../d8/d55/classApp_1_1PropertyStringList.html#a0ace5f1f9c4d70f6047e77347ba05e36).

Referenced by [App::PropertyListsT< T, ListT, ParentT
>::setPyObject()](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
and [App::PropertyListsT< T, ListT, ParentT
>::setPyValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e).

## ◆ getSize()

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

| virtual [int](../../d1/da0/classint.html) [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::getSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Implements
[App::PropertyListsBase](../../d7/d8e/classApp_1_1PropertyListsBase.html#acbdccea70aaba518e3af5ac37580d54d).

Referenced by
[TechDraw::DrawPage::addView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ac3e23be3a1fe6b9e35a45c680e33dd8a),
[TechDraw::DrawViewCollection::addView()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#afb1979ff19a65dddafe401d198cd67e7),
[Gui::ViewProviderLink::applyMaterial()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2116838fd198dca3f32851993fc65e2a),
[MeshGui::ViewProviderMesh::canHighlightColors()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a4ecd94eb5619800f1ba36eb7648552bf),
[Part::Loft::execute()](../../d3/d52/classPart_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[Part::Sweep::execute()](../../df/dc6/classPart_1_1Sweep.html#a7fdf28d346eb1b3b838ed0dea5bb40d8),
[Fem::FemVTKTools::exportFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a37e8a3dd86851c4ce056f3cfa7ad0d89),
[PartGui::ViewProviderPartExt::getElementColors()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a15bdce85211acfec231620d1fea14805),
[Gui::ViewProviderLink::getElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2b9c2eef2778031596f93f33b2980102),
[MeshGui::ViewProviderMesh::highlightColors()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a0877e142c07a2d4419b39cb8b01c9f85),
[Drawing::FeaturePage::onBeforeChange()](../../db/d0f/classDrawing_1_1FeaturePage.html#a7c55c251b8fe8c83f98a5e0defb88070),
[App::VRMLObject::onChanged()](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf),
[Drawing::FeaturePage::onChanged()](../../db/d0f/classDrawing_1_1FeaturePage.html#a9c6b6897f29ff589163044d51b7e5c04),
[MeshGui::ViewProviderMesh::removeFacets()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#aef4f7c4dfe1a66027828a011eea2651f),
[App::GroupExtension::removeObjectsFromDocument()](../../da/d3a/classApp_1_1GroupExtension.html#af7405cb3abccba3302792487e514a4e1),
[TechDraw::DrawPage::removeView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a47c86c19ddcbaabe9a680e836c437012),
[TechDraw::DrawViewCollection::removeView()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a1a2307b12204f3ddcb9d15d0c39a313e),
[App::VRMLObject::Restore()](../../df/df6/classApp_1_1VRMLObject.html#ae08e5863309e25cd88e07e2be87c9f48),
[App::VRMLObject::RestoreDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a90cb824c6253de535ec16e1935455599),
[App::VRMLObject::SaveDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a5dc3cc5b304d0866d30a0ad975cc4ccd),
[App::PropertyListsT< T, ListT, ParentT
>::set1Value()](../../d1/d0e/classApp_1_1PropertyListsT.html#ada9ee7ea1e2127ba7456b9a4a4697d80),
[PartDesignGui::ViewProviderTransformed::startEditing()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#aca65c3594f90b54775e4c73ededd1ffc),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[Gui::ViewProviderLink::updateElementList()](../../d6/d59/classGui_1_1ViewProviderLink.html#a052097f0154c16d7e207c626e115cddf),
and
[App::PropertyLinkSubList::upgrade()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b).

## ◆ getValue()

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

const ListT & [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
References [App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938).

Referenced by
[App::GroupExtension::extensionOnChanged()](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f),
and [App::PropertyListsT< T, ListT, ParentT
>::isSame()](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109).

## ◆ getValues()

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

const ListT & [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::getValues  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[TechDrawGui::MDIViewPage::addChildrenToPage()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#aad0e8f131364d2c566d30b9b71459f82),
[PartDesign::Body::addObject()](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605),
[Path::FeatureCompound::addObject()](../../d2/d43/classPath_1_1FeatureCompound.html#a7f4cc741ab67fbdd81b7c8aff793eb42),
[App::GroupExtension::addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
[App::GeoFeatureGroupExtension::addObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d),
[TechDraw::DrawProjGroup::addProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acfc4e756c8714973996318393180f483),
[TechDraw::DrawPage::addView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ac3e23be3a1fe6b9e35a45c680e33dd8a),
[TechDraw::DrawViewClip::addView()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a36206122f495194d04ea207c607c43f4),
[TechDraw::DrawViewCollection::addView()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#afb1979ff19a65dddafe401d198cd67e7),
[TechDraw::DrawLeaderLine::adjustLastSegment()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#af9979a970967304c97ce041e0bda2cfc),
[TechDraw::DrawProjGroup::arrangeViewPointers()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a8a8bdca0831ea0e16e664ad17f0a04f8),
[TechDraw::DrawProjGroup::autoPositionChildren()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a03769f635f816aacf77c54e1b71445d7),
[Gui::ViewProviderColorBuilder::buildNodes()](../../d0/d90/classGui_1_1ViewProviderColorBuilder.html#aa1ebd83b01910468d091e57f1f59920e),
[TechDrawGui::TaskRichAnno::calcTextStartPos()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ae1abe86bd3bc257ecd36cc0212763a37),
[TechDraw::DrawViewDimExtent::checkReferences2D()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#adfd8a7badbf1f348c3965817c2897a07),
[FemGui::ViewProviderFemPostPipeline::claimChildren()](../../df/d95/classFemGui_1_1ViewProviderFemPostPipeline.html#ac5626a9e2850eeb26ecff5a70bf2d941),
[PartGui::ViewProviderSweep::claimChildren()](../../d7/d5f/classPartGui_1_1ViewProviderSweep.html#a91b5fe397c600d5fe79e69c62c3ac22e),
[PartDesignGui::ViewProviderMultiTransform::claimChildren()](../../d6/d05/classPartDesignGui_1_1ViewProviderMultiTransform.html#af5e53bee082a9a57e0e69dd5e6070035),
[TechDrawGui::ViewProviderProjGroup::claimChildren()](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a702e5f00c38dcb77490c48b4018d093e),
[TechDrawGui::ViewProviderViewClip::claimChildren()](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#ab19cf412f22ca45bce0de2d22f88b7bb),
[TechDrawGui::ViewProviderPage::claimChildren()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#abaf1943763d885917f20c4a78a8e2ef5),
[TechDraw::DrawViewCollection::countChildren()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a5474d7126e47e209e9b7c929422d4287),
[App::GroupExtension::countObjectsOfType()](../../da/d3a/classApp_1_1GroupExtension.html#a20dc1c6c322878e94281f7a7f56b4173),
[PartGui::ViewProviderMultiFuse::dragObject()](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a32b33e83e13994afaf935e456e0b57f0),
[PartGui::ViewProviderMultiCommon::dragObject()](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#a1e67ab8efea8e70aaba3b8c11520b457),
[PartGui::ViewProviderCompound::dragObject()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a8ac5bc65eca40dc6643130c34aba6204),
[PartGui::ViewProviderFace::dragObject()](../../d9/dba/classPartGui_1_1ViewProviderFace.html#a8ee9184812e792b5581aece499e8383c),
[PathGui::ViewProviderArea::dragObject()](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a21aec54554c05f358ef3b348e5bbd7bf),
[PathGui::ViewProviderPathShape::dragObject()](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#ad50efc30b828dbc7635de3f3fa82af31),
[PartGui::ViewProviderMultiFuse::dropObject()](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a586957f2b53d8314a6b029c210db1b1f),
[PartGui::ViewProviderMultiCommon::dropObject()](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#a7e7159c88b68bce0a30ef2b3b9112441),
[PartGui::ViewProviderCompound::dropObject()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#afa57525b6024724ed1a6de30e19c8439),
[PartGui::ViewProviderFace::dropObject()](../../d9/dba/classPartGui_1_1ViewProviderFace.html#a13281a3ef2aa0f0751e28766b637caf3),
[PathGui::ViewProviderArea::dropObject()](../../d3/d66/classPathGui_1_1ViewProviderArea.html#acaa0088c9df488727e02cd749f22f457),
[PathGui::ViewProviderPathShape::dropObject()](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#a264c4c2055e7bb5a27daaad6d8466668),
[PartDesignGui::ViewProviderBody::dropObject()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3e245daa7cd5dbb26f3603f2e93f68fe),
[TechDraw::DrawProjGroup::dumpISO()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a64c8445dbe972e26619f07afbe560a6f),
[Drawing::FeatureClip::execute()](../../d5/d4a/classDrawing_1_1FeatureClip.html#afed75650f49849b96c65ef93795800e5),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Drawing::FeatureViewAnnotation::execute()](../../d6/de7/classDrawing_1_1FeatureViewAnnotation.html#a74171a078f54a6d0ee13242e3b014751),
[Drawing::FeatureViewSymbol::execute()](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#a3563b4ff57807e29d705c04a53b7cd0b),
[Fem::FemPostPipeline::execute()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a37a7074a69af004117f82d72be1701f8),
[Inspection::Feature::execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[Part::Compound::execute()](../../d7/d98/classPart_1_1Compound.html#a72d02534883bc8e2b7ccb46218e87087),
[Part::MultiCommon::execute()](../../d1/df7/classPart_1_1MultiCommon.html#ab89bf89ceaef91d77ba170a7e548040d),
[Part::MultiFuse::execute()](../../df/dbc/classPart_1_1MultiFuse.html#affac0f86cba2c15642f4d8a64a01c337),
[Part::Loft::execute()](../../d3/d52/classPart_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[Part::Sweep::execute()](../../df/dc6/classPart_1_1Sweep.html#a7fdf28d346eb1b3b838ed0dea5bb40d8),
[PartDesign::Transformed::execute()](../../dd/de1/classPartDesign_1_1Transformed.html#aef9667071a3f6bb2ed13226f84629049),
[Path::FeatureArea::execute()](../../da/d1e/classPath_1_1FeatureArea.html#af00ad2b6bd7ffa0f8db73f7b51b94fbc),
[Path::FeatureCompound::execute()](../../d2/d43/classPath_1_1FeatureCompound.html#a0db05b4845d8e9cf2dc1ab83a02a875b),
[Path::FeatureShape::execute()](../../da/d9b/classPath_1_1FeatureShape.html#a62d47b3cb3d7ed9081cdfc0966c71c3e),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[Robot::TrajectoryCompound::execute()](../../df/de7/classRobot_1_1TrajectoryCompound.html#a230683c181418d56d66a986fe5063a3a),
[TechDraw::DrawViewClip::execute()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a31cd0c2306b266d607e29672b3825340),
[TechDraw::DrawViewDimExtent::execute()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#ac856c6f8b2f5504087090cc122d82891),
[Part::Face::execute()](../../dc/dbf/classPart_1_1Face.html#a7e0c10e1928c118064cc40586322ca36),
[PartDesign::Boolean::execute()](../../d2/d81/classPartDesign_1_1Boolean.html#a471715716cd89abfe18b9f50b7728567),
[TechDraw::DrawViewMulti::execute()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a9d04a96ccac9fad6d125e478b91b7f30),
[TechDraw::DrawViewSymbol::execute()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a44eea88d3e8522c41e9dcee9acff10ce),
[TechDraw::LandmarkDimension::execute()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a628476bf5d4492109e6d1e947c15aa6d),
[Fem::FemVTKTools::exportFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a37e8a3dd86851c4ce056f3cfa7ad0d89),
[Import::ExportOCAF::exportObject()](../../d2/dda/classImport_1_1ExportOCAF.html#a44829a66a0a0a1481f0b17eb8f29331b),
[Gui::ViewProviderGeoFeatureGroupExtension::extensionClaimChildren()](../../d2/de9/classGui_1_1ViewProviderGeoFeatureGroupExtension.html#ad44762aa4bd4aa7ae5734d717c8925ed),
[App::GeoFeatureGroupExtension::extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[App::GroupExtension::extensionGetSubObject()](../../da/d3a/classApp_1_1GroupExtension.html#a9f6afe4878329f62b99288df7224cec2),
[App::GeoFeatureGroupExtension::extensionGetSubObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a049b0b8b248680cbdc858bd5e44603aa),
[App::GroupExtension::extensionGetSubObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a7abcd2dfce52f226f31f5996d5d360e2),
[App::GeoFeatureGroupExtension::extensionOnChanged()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487),
[App::GroupExtension::extensionOnChanged()](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f),
[TechDrawGui::MDIViewPage::findMissingViews()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a008268149662b6262a0a1aa91cb12d5a),
[TechDrawGui::QGSPage::findParent()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#aa36872a18b939b5400ece0e09997fd0f),
[App::GroupExtension::getAllChildren()](../../da/d3a/classApp_1_1GroupExtension.html#a659c18eb455814e2dbe04a79a59947f6),
[TechDraw::DrawProjGroup::getAllSources()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a8edac304b81ce90c236c3bd15ec7c1ee),
[TechDraw::DrawViewPart::getAllSources()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aa77b2d57a02bff6131429b1ff2df9066),
[TechDraw::DrawPage::getAllViews()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a5e94239ad9e3ffb6b034ec2eddd4beb2),
[PartDesign::Transformed::getBaseObject()](../../dd/de1/classPartDesign_1_1Transformed.html#aba5db649de61d67db332e2cd71a86d09),
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686),
[TechDraw::DrawViewClip::getChildViewNames()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#aec9acaae16e2f82bdcc0994a767559ef),
[TechDrawGui::QGEPath::getDeltasFromLeader()](../../d9/da7/classTechDrawGui_1_1QGEPath.html#a59c9f7dddcda624bf7724c39938353f2),
[TechDraw::DrawLeaderLine::getKinkPoint()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a9ad287a5d948a9644b7cbe79528e16be),
[Fem::FemPostPipeline::getLastPostObject()](../../d5/d4b/classFem_1_1FemPostPipeline.html#af3f3004a86c520de646e7c2fbabe41db),
[PartDesign::Body::getNextSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#a0c9db11c1cca8a2a0c7247d7d3498242),
[App::GroupExtension::getObjects()](../../da/d3a/classApp_1_1GroupExtension.html#ab7df48295e51c05fcb9eaa3ac2857938),
[App::GroupExtension::getObjectsOfType()](../../da/d3a/classApp_1_1GroupExtension.html#a55c23aac201dfbc053a5eeaf8bd37e5f),
[App::Origin::getOriginFeature()](../../d9/d8b/classApp_1_1Origin.html#ac51255a58d5f06783527b973082ed634),
[TechDraw::DrawViewDimExtent::getPointsTwoVerts()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#ad71b5d1172020e7c0e21a5815a2c545e),
[PartDesign::Body::getPrevSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#aface61e57526fc0ce72faff92c3e0841),
[TechDraw::DrawProjGroup::getProjObj()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a20beaf391d87e04ad8b2cd1db7c78b6d),
[TechDraw::DrawViewAnnotation::getRect()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#a4e6ad66a92200e1f96748ea766163ce1),
[TechDraw::DrawViewCollection::getRect()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a8bf6370b982b95b15e5c16954ab353bb),
[TechDraw::ShapeExtractor::getShapes2d()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a7b6b34e0c817f34b537bdb53b36956f1),
[TechDraw::ShapeExtractor::getShapesFromObject()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4043c946e78f533e4f060cb3b87b5691),
[PartDesign::Transformed::getSketchObject()](../../dd/de1/classPartDesign_1_1Transformed.html#a7b52a3658c0f24c04278bc8c1fcc55fd),
[PartDesign::Body::getSubObject()](../../dd/db8/classPartDesign_1_1Body.html#aecc131a5ce7f03c5041a475003456b38),
[TechDraw::DrawLeaderLine::getTailPoint()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#adad4a832160f419f1980e51367240499),
[TechDraw::DrawLeaderLine::getTileOrigin()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a550fc46519d2e26a13302aa7cb0b8a8e),
[PartDesign::MultiTransform::getTransformations()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a33b71497cd61478ec6fb8d660b759b6b),
[PartDesignGui::TaskMultiTransformParameters::getTransformFeatures()](../../d1/df7/classPartDesignGui_1_1TaskMultiTransformParameters.html#a756a4192dafe0879c9141f33ac24f62f),
[App::PropertyListsT< T, ListT, ParentT
>::getValue()](../../d1/d0e/classApp_1_1PropertyListsT.html#a064f87de752ea68f9a660c10ba3dcf4b),
[TechDraw::DrawProjGroup::getViewsAsDPGI()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a98c03a15a9d615eec7dde4b3a735bea1),
[TechDrawGui::QGILeaderLine::getWayPointsFromFeature()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#a1f75c823bd5229f85a626e8846c4bb24),
[App::Origin::hasObject()](../../d9/d8b/classApp_1_1Origin.html#afd6b442d0bd144e6389fee183c41fc94),
[Path::FeatureCompound::hasObject()](../../d2/d43/classPath_1_1FeatureCompound.html#a3f892efda42bef0ee8701284808fd40e),
[App::GroupExtension::hasObject()](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a),
[TechDraw::DrawProjGroup::hasProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a90a7b1897caccb65feab45425c10448d),
[PartDesignGui::ViewProviderShapeBinder::highlightReferences()](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#a88fdfde939bae5a7f7d2ed7d3865a9a8),
[PartDesignGui::ViewProviderDressUp::highlightReferences()](../../dd/dfd/classPartDesignGui_1_1ViewProviderDressUp.html#ac12fbf092e55153a3af0847db4101b5e),
[FemGui::ViewProviderFemConstraintOnBoundary::highlightReferences()](../../da/d5f/classFemGui_1_1ViewProviderFemConstraintOnBoundary.html#a1586daa50943e93d852dadff457479f0),
[Fem::FemPostPipeline::holdsPostObject()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a94eafead77c98694f9809031dcfb4cec),
[PartDesignGui::TaskTransformedParameters::indexesMoved()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#a3b5b194d9abce483eb434ae97ede1fac),
[PartDesign::Body::insertObject()](../../dd/db8/classPartDesign_1_1Body.html#a5cbb7aa1f902c8b111a9c9a428072c09),
[Part::BodyBase::isAfter()](../../da/dc8/classPart_1_1BodyBase.html#a9a200c47ffd7f95eb5584fd6bf54dfe3),
[PartDesign::Body::isMemberOfMultiTransform()](../../dd/db8/classPartDesign_1_1Body.html#a9a9ab9d38f99b313ee96c4720f7bff6b),
[TechDraw::DrawViewClip::isViewInClip()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#ab3f27abce9a47c81b315f5765829df8f),
[TechDrawGui::TaskLinkDim::loadAvailDims()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#a3e6b427c8a0b62b4199b25d3eb07f58b),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::loadDefaults()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a891f1e17c68d3e761fb4eb7839772ad7),
[TechDraw::DrawViewCollection::lockChildren()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#aaa1ac5e3f6521d9db1e7fbc0e81bb55b),
[TechDrawGui::QGIViewAnnotation::mouseDoubleClickEvent()](../../d4/d5b/classTechDrawGui_1_1QGIViewAnnotation.html#a0b2aec7a7e987b6deaca89c24d426c8d),
[App::VRMLObject::onChanged()](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf),
[Fem::FemPostPipeline::onChanged()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a333b47057bc9b7691cc0c9db9b0c79ba),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartDesign::Body::onChanged()](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[PartDesignGui::ViewProvider::onChanged()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a257ca77e2256cbd8df847cedc5892289),
[TechDraw::DrawPage::onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawViewMulti::onChanged()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#aa73d9e1a0934d049da29a63f2c5ddddd),
[Gui::ViewProviderOrigin::onDelete()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#af088d91593fa59ce593fd49716356f32),
[PartGui::ViewProviderMultiFuse::onDelete()](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#ab048345dbd6162a3f90389c7fa398e02),
[PartGui::ViewProviderMultiCommon::onDelete()](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#a26b5c231ca52bd3221b392cabee8f431),
[PartGui::ViewProviderCompound::onDelete()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#adfb588dd213e7d043ac042a7dda8050e),
[PartDesignGui::ViewProviderMultiTransform::onDelete()](../../d6/d05/classPartDesignGui_1_1ViewProviderMultiTransform.html#a85c1d63c3e95cdacf8d7e40cec2f3567),
[PathGui::ViewProviderArea::onDelete()](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a5672119b22fe16ed78c9732c2e5fbc62),
[PathGui::ViewProviderPathShape::onDelete()](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#acdc1c8af04392a2750bef73c0c1f5463),
[PartDesignGui::ViewProviderBoolean::onDelete()](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#aabf46492095e0512b7b9ef7b475f8228),
[PartDesign::Body::onDocumentRestored()](../../dd/db8/classPartDesign_1_1Body.html#aa6affc475d3884d9570838e731749605),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::onSaveStyle()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a62078ac8e29f972f667a11bf889acd64),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[SurfaceGui::FillingPanel::onSelectionChanged()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#ac8f46981ec84ea0a20faf5791db7cb4b),
[SurfaceGui::FillingEdgePanel::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a13eada025c84a3c28016f3c3974d089d),
[TechDrawGui::TaskLeaderLine::onTrackerClicked()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a581dcc144a5b4017a6356a89dda30abe),
[PartDesignGui::TaskTransformedParameters::originalSelected()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#adb918122e8572632cc17114506d98ccd),
[TechDrawGui::MDIViewPage::orphanExists()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#af53edffe3018bd0dfa04f4cdee23c85f),
[PartDesign::MultiTransform::positionBySupport()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a3d4f1facdf2a2ca1233b9e6e09ec7710),
[PartGui::FaceColors::Private::Private()](../../d4/d4b/classFaceColors_1_1Private.html#aa6e3aabbd50fa1add6f4c6373e0d09ba),
[TechDraw::DrawProjGroup::purgeProjections()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a59234a939935212324d52d31af4c479b),
[TechDraw::DrawViewCollection::rebuildViewList()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a2cddd1c4b006821c3ec11a31dedf7338),
[TechDraw::DrawProjGroup::recomputeChildren()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a3226a8c41024eacaed2182c83ba78341),
[PartDesignGui::relinkToBody()](../../dc/d12/namespacePartDesignGui.html#a5bd0f34409b95d9ccc03b0b80655b0fd),
[MeshGui::ViewProviderMesh::removeFacets()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#aef4f7c4dfe1a66027828a011eea2651f),
[Path::FeatureCompound::removeObject()](../../d2/d43/classPath_1_1FeatureCompound.html#a539fe11e5380f928b17ae81b6a3addb4),
[PartDesign::Body::removeObject()](../../dd/db8/classPartDesign_1_1Body.html#a207956cf2a361690d971c7e604fc8bf1),
[App::GroupExtension::removeObjects()](../../da/d3a/classApp_1_1GroupExtension.html#aa991d1bc084e4918a5ab22257c0fa676),
[App::GeoFeatureGroupExtension::removeObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a38ac880c5d19aba50ba8726162bbe2bb),
[App::GroupExtension::removeObjectsFromDocument()](../../da/d3a/classApp_1_1GroupExtension.html#af7405cb3abccba3302792487e514a4e1),
[TechDraw::DrawProjGroup::removeProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a23d2d0cb8a3447cdb912202f46f27aae),
[TechDraw::DrawPage::removeView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a47c86c19ddcbaabe9a680e836c437012),
[TechDraw::DrawViewClip::removeView()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a11d07aa588710572d1b48dfa6aebd923),
[TechDraw::DrawViewCollection::removeView()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a1a2307b12204f3ddcb9d15d0c39a313e),
[App::VRMLObject::Restore()](../../df/df6/classApp_1_1VRMLObject.html#ae08e5863309e25cd88e07e2be87c9f48),
[App::VRMLObject::Save()](../../df/df6/classApp_1_1VRMLObject.html#abee995466100ec91a1ae0f2baa2feec3),
[TechDrawGui::TaskProjGroup::saveGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#af012f644413f9c531a249a2fcb76d888),
[TechDrawGui::TaskLeaderLine::saveState()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a44043828f863d0b6365714da62ee59d1),
[MeshGui::ViewProviderMesh::setColorPerFace()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#aa6225440cb53360110a3a9ec360e09d2),
[MeshGui::ViewProviderMesh::setColorPerVertex()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a53b48db900828adb5b7a0d8ecff7d4d7),
[SurfaceGui::FillingPanel::setEditedObject()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#aaaeba016fe808b6dc4d3ddfc9788d380),
[SurfaceGui::FillingEdgePanel::setEditedObject()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#aa23402d795184e9f546a933ef0820357),
[Gui::ViewProviderLink::setElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#af274c7d8619bfae997be5ea17b7c72b3),
[App::PropertyLinkSubList::setPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a495ec38be0d7ceb20aa9b3d5a520fdfa),
[App::PropertyXLinkList::setPyObject()](../../df/d17/classApp_1_1PropertyXLinkList.html#a2f618a6e3542cb338064a4d268277290),
[PointsGui::ViewProviderPoints::setVertexColorMode()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a0590b3a0a0a4163816892685f5f9a73d),
[PartDesignGui::ViewProviderBody::setVisualBodyMode()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a50b3de515b84c2e3e19b840ef5fc8187),
[PartDesignGui::TaskBooleanParameters::TaskBooleanParameters()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#afee7fbe402fa60d00581ce385bc8cb3c),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[FemGui::TaskFemConstraintTransform::TaskFemConstraintTransform()](../../d9/d9b/classFemGui_1_1TaskFemConstraintTransform.html#aa2ff547501a5af38276cce0666c1920c),
[PartDesignGui::TaskMultiTransformParameters::TaskMultiTransformParameters()](../../d1/df7/classPartDesignGui_1_1TaskMultiTransformParameters.html#afe3826324b5f7c771d0deb67ac6fa26e),
[PathGui::TaskWidgetPathCompound::TaskWidgetPathCompound()](../../d0/db3/classPathGui_1_1TaskWidgetPathCompound.html#a5d2bb2b5eee81005b4e24fb81432adda),
[PartDesignGui::ViewProviderBody::unifyVisualProperty()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a9622d1e6a23c6497bea610755aea5713),
[App::Origin::unsetupObject()](../../d9/d8b/classApp_1_1Origin.html#ace2a648f85e06a55346df50a6fad40fe),
[TechDraw::DrawViewCollection::unsetupObject()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a33815aa3bc978248b9ec92b423ba7c45),
[TechDraw::DrawViewDimExtent::unsetupObject()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#abc5c45571551383c8db0194bec4bcec6),
[TechDraw::DrawPage::unsetupObject()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ad65529c32a2d36f88a87e6734f093fcf),
[TechDraw::LandmarkDimension::unsetupObject()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a238125d961e1b341b853671cf6e62c1e),
[TechDraw::DrawProjGroup::updateChildrenEnforce()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a53d6b329649586210ae8e5f6eb6e6a2c),
[TechDraw::DrawProjGroup::updateChildrenLock()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aa9ea74d38f2710c6690b5a69879ae23b),
[TechDraw::DrawProjGroup::updateChildrenScale()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a34817922d5abecc72163f2b968e3a627),
[TechDraw::DrawProjGroup::updateChildrenSource()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5765aa3026040998e1c20dd4b71123f4),
[FemGui::ViewProviderFemConstraintContact::updateData()](../../d9/d3d/classFemGui_1_1ViewProviderFemConstraintContact.html#a3ecf76e65206672a9355c60a533550c8),
[FemGui::ViewProviderFemConstraintFixed::updateData()](../../d4/d9c/classFemGui_1_1ViewProviderFemConstraintFixed.html#ab0717083d8637965bcafa54bfd839893),
[FemGui::ViewProviderFemConstraintFluidBoundary::updateData()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintForce::updateData()](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#ad691cf23756106d6b0ea043ddebd1b94),
[FemGui::ViewProviderFemConstraintHeatflux::updateData()](../../d0/dea/classFemGui_1_1ViewProviderFemConstraintHeatflux.html#a3f1a55d2e70a5dca6b97d52c3e103aa0),
[FemGui::ViewProviderFemConstraintPlaneRotation::updateData()](../../d7/d0a/classFemGui_1_1ViewProviderFemConstraintPlaneRotation.html#a2b385e8a4903df418ef331257ad13a64),
[FemGui::ViewProviderFemConstraintPressure::updateData()](../../d4/d18/classFemGui_1_1ViewProviderFemConstraintPressure.html#a0280a478dea5288d50ba390ed1a50ca7),
[FemGui::ViewProviderFemConstraintSpring::updateData()](../../d5/d4f/classFemGui_1_1ViewProviderFemConstraintSpring.html#a44c1119dd7d0bef3d9ef9c3229057e53),
[FemGui::ViewProviderFemConstraintTemperature::updateData()](../../d1/df6/classFemGui_1_1ViewProviderFemConstraintTemperature.html#a4c6f2f24780c8171d293ec933ae942ac),
[FemGui::ViewProviderFemConstraintTransform::updateData()](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#a2adf8aba7f15f7b95399068ab39c47b8),
[PartGui::ViewProviderBoolean::updateData()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#ae38d6575df4dd650428a3d5873874d94),
[PartGui::ViewProviderMultiFuse::updateData()](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a2dd30d90dd627899aae55dd7f6082bfd),
[PartGui::ViewProviderMultiCommon::updateData()](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#afd2565caa649c9122a8da1bad7217b88),
[PartGui::ViewProviderCompound::updateData()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a864f55403bd4a3b5a81834205fe9561d),
[PartGui::ViewProviderFillet::updateData()](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a681e5f4afcfbf90240da46de01068325),
[PartGui::ViewProviderChamfer::updateData()](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a33e0d402eb35a8d3bf589039003c4f0d),
[PartDesignGui::ViewProviderBody::updateData()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a2a541fb893a7130314f3c7161c33477e),
[TechDraw::DrawProjGroup::updateSecondaryDirs()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aab0e5d4fa1e0eaf890c7c6cb2eb06766),
[TechDraw::DrawProjGroup::updateViews()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a080b64dfe4a1d4456558102c2c8def62),
[App::PropertyLinkSubList::upgrade()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b),
and
[App::PropertyXLinkSubList::upgrade()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2).

## ◆ isSame()

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

| virtual [bool](../../d9/db9/classbool.html) [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

References
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
and [App::PropertyListsT< T, ListT, ParentT
>::getValue()](../../d1/d0e/classApp_1_1PropertyListsT.html#a064f87de752ea68f9a660c10ba3dcf4b).

## ◆ operator[]()

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

[const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::operator[]  | ( | [int](../../d1/da0/classint.html) | _idx_| ) |  const  
---|---|---|---|---|---  
  
## ◆ set1Value()

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

| virtual void [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::set1Value  | ( | [int](../../d1/da0/classint.html) | _index_ ,   
---|---|---|---  
|  | [const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) | _value_  
| ) | |   
virtual  
  
References [App::PropertyListsT< T, ListT, ParentT
>::getSize()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< T, ListT, ParentT
>::setSize()](../../d1/d0e/classApp_1_1PropertyListsT.html#a3d8817fe93f3db9c3d32dcecafbfd061),
and [App::AtomicPropertyChangeInterface< P
>::AtomicPropertyChange::tryInvoke()](../../d6/d47/classApp_1_1AtomicPropertyChangeInterface_1_1AtomicPropertyChange.html#aea1f8110dc9360b614cf110f210bd1c5).

Referenced by
[App::VRMLObject::onChanged()](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf),
[App::VRMLObject::RestoreDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a90cb824c6253de535ec16e1935455599),
and [App::PropertyListsT< T, ListT, ParentT
>::setPyValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e).

## ◆ setPyObject()

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

| virtual void [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::PropertyLists](../../d4/da1/classApp_1_1PropertyLists.html#a47e37fe20890a5258c0351c6f3244d60).

Reimplemented in
[App::PropertyBoolList](../../d1/dcf/classApp_1_1PropertyBoolList.html#a4ab8f10b4974f5651b2cb3779de59543).

References [App::PropertyListsT< T, ListT, ParentT
>::getPyValue()](../../d1/d0e/classApp_1_1PropertyListsT.html#a0048578553b52a7697ca08bcd71249b0),
and [App::PropertyListsT< T, ListT, ParentT
>::setValue()](../../d1/d0e/classApp_1_1PropertyListsT.html#abaaa23d8c4ff48e19290cf81a62f6e94).

Referenced by
[App::PropertyLinkSubList::setPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a495ec38be0d7ceb20aa9b3d5a520fdfa),
and
[App::PropertyXLinkList::setPyObject()](../../df/d17/classApp_1_1PropertyXLinkList.html#a2f618a6e3542cb338064a4d268277290).

## ◆ setPyValues()

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

| void [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::setPyValues  | ( | const std::vector< [PyObject](../../df/d1b/classPyObject.html) * > & | _vals_ ,   
---|---|---|---  
|  | const std::vector< [int](../../d1/da0/classint.html) > & | _indices_  
| ) | |   
overrideprotectedvirtual  
  
Reimplemented from
[App::PropertyListsBase](../../d7/d8e/classApp_1_1PropertyListsBase.html#a33a3c42a6dd5aa648329c817e8689921).

References [App::PropertyListsT< T, ListT, ParentT
>::getPyValue()](../../d1/d0e/classApp_1_1PropertyListsT.html#a0048578553b52a7697ca08bcd71249b0),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[App::PropertyListsT< T, ListT, ParentT
>::set1Value()](../../d1/d0e/classApp_1_1PropertyListsT.html#ada9ee7ea1e2127ba7456b9a4a4697d80),
[App::PropertyListsT< T, ListT, ParentT
>::setValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8744f95234dbfb9431759906c2a76cd4),
and [App::AtomicPropertyChangeInterface< P
>::AtomicPropertyChange::tryInvoke()](../../d6/d47/classApp_1_1AtomicPropertyChangeInterface_1_1AtomicPropertyChange.html#aea1f8110dc9360b614cf110f210bd1c5).

## ◆ setSize() [1/2]

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

| virtual void [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::setSize  | ( | [int](../../d1/da0/classint.html) | _newSize_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Implements
[App::PropertyListsBase](../../d7/d8e/classApp_1_1PropertyListsBase.html#a59f18e45d11306be56f29104af5b2160).

Reimplemented in
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a05972fc1163a21a73e4526a071896f92).

## ◆ setSize() [2/2]

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

| virtual void [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::setSize  | ( | [int](../../d1/da0/classint.html) | _newSize_ ,   
---|---|---|---  
|  | [const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) | _def_  
| ) | |   
virtual  
  
Reimplemented in
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a76e08f284f203a340dddff0590bb2c53).

Referenced by
[App::VRMLObject::onChanged()](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf),
[App::VRMLObject::Restore()](../../df/df6/classApp_1_1VRMLObject.html#ae08e5863309e25cd88e07e2be87c9f48),
[App::PropertyListsT< T, ListT, ParentT
>::set1Value()](../../d1/d0e/classApp_1_1PropertyListsT.html#ada9ee7ea1e2127ba7456b9a4a4697d80),
and
[Gui::ViewProviderLink::updateElementList()](../../d6/d59/classGui_1_1ViewProviderLink.html#a052097f0154c16d7e207c626e115cddf).

## ◆ setValue() [1/2]

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

void [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::setValue  | ( | const ListT & | _newValues_ = `ListT()`| ) |   
---|---|---|---|---|---  
  
References [App::PropertyListsT< T, ListT, ParentT
>::setValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8744f95234dbfb9431759906c2a76cd4).

## ◆ setValue() [2/2]

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

void [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::setValue  | ( | [const_reference](../../d1/d0e/classApp_1_1PropertyListsT.html#a278531d54ed118c2cd42004f678070a5) | _value_| ) |   
---|---|---|---|---|---  
  
References [App::PropertyListsT< T, ListT, ParentT
>::setValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8744f95234dbfb9431759906c2a76cd4).

Referenced by
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[TechDraw::DrawViewMulti::onChanged()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#aa73d9e1a0934d049da29a63f2c5ddddd),
[DraftUtils::DraftDxfRead::OnReadText()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#a4a48ca0bc35d4c47fc4e374d8ee6bf25),
[Import::ImpExpDxfRead::OnReadText()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#afd452a8d1348c494bfcc4bb9e5d4b01c),
[App::PropertyListsT< T, ListT, ParentT
>::setPyObject()](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
and
[Gui::ViewProviderLink::updateDataPrivate()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2f2113e0017af3819a9064380ed30d0d).

## ◆ setValues()

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

| virtual void [App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT, ParentT >::setValues  | ( | const ListT & | _newValues_ = `ListT()`| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#af7e153c0a4b95bb6b79a5b2b357d5a48).

References [App::AtomicPropertyChangeInterface< P
>::AtomicPropertyChange::tryInvoke()](../../d6/d47/classApp_1_1AtomicPropertyChangeInterface_1_1AtomicPropertyChange.html#aea1f8110dc9360b614cf110f210bd1c5).

Referenced by
[TechDraw::DrawLeaderLine::adjustLastSegment()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#af9979a970967304c97ce041e0bda2cfc),
[Fem::ConstraintFluidBoundary::ConstraintFluidBoundary()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#ad0ba55c936b2e15550d2fe8732f7be41),
[Fem::ConstraintHeatflux::ConstraintHeatflux()](../../de/dce/classFem_1_1ConstraintHeatflux.html#a58583bd2f3380a6d5acc8bc860e19f50),
[Fem::ConstraintTemperature::ConstraintTemperature()](../../d7/dff/classFem_1_1ConstraintTemperature.html#a7f0bb60b27a35ad74b1de63d3e6d9c14),
[Fem::ConstraintTransform::ConstraintTransform()](../../d8/d3c/classFem_1_1ConstraintTransform.html#ad457f6edd3a6dea3252906be279d3924),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[Fem::FemPostDataAlongLineFilter::GetAxisData()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ac3850d76cbd006a0d9f86f6971463cf2),
[Fem::FemPostDataAtPointFilter::GetPointData()](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#a72628069cbee6b9a5952177708496fd9),
[PartDesignGui::ViewProviderShapeBinder::highlightReferences()](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#a88fdfde939bae5a7f7d2ed7d3865a9a8),
[PartDesignGui::ViewProviderDressUp::highlightReferences()](../../dd/dfd/classPartDesignGui_1_1ViewProviderDressUp.html#ac12fbf092e55153a3af0847db4101b5e),
[FemGui::ViewProviderFemConstraintOnBoundary::highlightReferences()](../../da/d5f/classFemGui_1_1ViewProviderFemConstraintOnBoundary.html#a1586daa50943e93d852dadff457479f0),
[Fem::FemVTKTools::importFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a06964ad44830b32163bedb9351fad2c8),
[Fem::ConstraintContact::onChanged()](../../db/d7c/classFem_1_1ConstraintContact.html#a2470d9364e84ea3c15f5873073f26539),
[Fem::ConstraintDisplacement::onChanged()](../../d5/d1c/classFem_1_1ConstraintDisplacement.html#a8525892f2c7183b75c1d8f2052f82401),
[Fem::ConstraintFixed::onChanged()](../../d1/d43/classFem_1_1ConstraintFixed.html#a2b9b87e9151f1571ab9cff619ec5547c),
[Fem::ConstraintFluidBoundary::onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Fem::ConstraintHeatflux::onChanged()](../../de/dce/classFem_1_1ConstraintHeatflux.html#a0caeab069cf3e2fc8246aa163735d1e9),
[Fem::ConstraintInitialTemperature::onChanged()](../../da/d91/classFem_1_1ConstraintInitialTemperature.html#aa21e4c9c6cc31312e5147bbe1f8fcf05),
[Fem::ConstraintPlaneRotation::onChanged()](../../d7/d08/classFem_1_1ConstraintPlaneRotation.html#a668aafd16c5cf0565dde1072dd55a34a),
[Fem::ConstraintPressure::onChanged()](../../dd/d5e/classFem_1_1ConstraintPressure.html#a05ca046143c094c241c12702f7b820f7),
[Fem::ConstraintSpring::onChanged()](../../dc/d42/classFem_1_1ConstraintSpring.html#ae67112c14de2dc75f749842b6591fcf8),
[Fem::ConstraintTemperature::onChanged()](../../d7/dff/classFem_1_1ConstraintTemperature.html#a74f2f9e94a2d9011490c09caab3c0da9),
[Fem::ConstraintTransform::onChanged()](../../d8/d3c/classFem_1_1ConstraintTransform.html#a38b893dee34272ad6bf0c6126aad561f),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::onLoadStyle()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a1ba62c7eca1bc9f408549242e3def48b),
[SurfaceGui::FillingPanel::onSelectionChanged()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#ac8f46981ec84ea0a20faf5791db7cb4b),
[SurfaceGui::FillingEdgePanel::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a13eada025c84a3c28016f3c3974d089d),
[MeshGui::ViewProviderMesh::removeFacets()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#aef4f7c4dfe1a66027828a011eea2651f),
[TechDrawGui::TaskLeaderLine::restoreState()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a119496553ef9c0aa3c285685dbc202ff),
[Gui::ViewProviderLink::setElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#af274c7d8619bfae997be5ea17b7c72b3),
[App::PropertyListsT< T, ListT, ParentT
>::setPyValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
[App::PropertyListsT< T, ListT, ParentT
>::setValue()](../../d1/d0e/classApp_1_1PropertyListsT.html#abaaa23d8c4ff48e19290cf81a62f6e94),
[PartGui::ViewProviderBoolean::updateData()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#ae38d6575df4dd650428a3d5873874d94),
[PartGui::ViewProviderMultiFuse::updateData()](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a2dd30d90dd627899aae55dd7f6082bfd),
[PartGui::ViewProviderMultiCommon::updateData()](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#afd2565caa649c9122a8da1bad7217b88),
[PartGui::ViewProviderCompound::updateData()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a864f55403bd4a3b5a81834205fe9561d),
[PartGui::ViewProviderFillet::updateData()](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a681e5f4afcfbf90240da46de01068325),
and
[PartGui::ViewProviderChamfer::updateData()](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a33e0d402eb35a8d3bf589039003c4f0d).

## Member Data Documentation

## ◆ atomic_change

template<class T , class ListT = std::vector<T>, class ParentT =
PropertyLists>

[friend](../../d7/d23/classfriend.html)
[App::PropertyListsT](../../d1/d0e/classApp_1_1PropertyListsT.html)< T, ListT,
ParentT >::atomic_change  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/Property.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

