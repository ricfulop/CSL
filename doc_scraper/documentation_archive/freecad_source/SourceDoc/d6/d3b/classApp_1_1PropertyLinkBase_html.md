---
url: https://freecad.github.io/SourceDoc/d6/d3b/classApp_1_1PropertyLinkBase.html
scraped_at: 2025-09-08T14:56:02.957578
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)

[List of all members](../../d3/d77/classApp_1_1PropertyLinkBase-members.html) | Public Types | Public Member Functions | Static Public Member Functions | Protected Member Functions | Friends

App::PropertyLinkBase Class Referenceabstract

Parent class of all link type properties.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#details)

`#include <PropertyLinks.h>`

##  Public Types  
  
---  
enum | [LinkFlags](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5f) {   
[LinkAllowExternal](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fad0f16a963cb6d4ee03471a56eb0d2b2e)
,
[LinkDetached](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5facbc01e4b149e5b3049e9916b0181a7da)
,
[LinkRestoring](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fa1de51bd54c0f62a03f8a15c70ed4a365)
,
[LinkAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5faa22f8833820bace817e74b03e6089f45)
,  
[LinkRestoreLabel](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fa5a4bc69cb609a1f93370ec11e29dc403)
,
[LinkSyncSubObject](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fab29bedf78f3fa832237ffa3a544e88c8)  
}  
typedef std::pair< std::string, std::string > | [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620)  
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
virtual [bool](../../d9/db9/classbool.html) | [adjustLink](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1ce35c00cf2495906301c94a0ea22c80) (const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList)=0  
| Called to adjust the link to avoid potential cyclic dependency.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1ce35c00cf2495906301c94a0ea22c80)  
  
virtual void | [breakLink](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9559e2b5adeb74b5dfa23960095b86a9) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) clear)=0  
| Called to reset this link property.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9559e2b5adeb74b5dfa23960095b86a9)  
  
void | [checkLabelReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b) (const std::vector< std::string > &subs, [bool](../../d9/db9/classbool.html) reset=true)  
| Check subnames for label registration.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b)  
  
virtual [int](../../d1/da0/classint.html) | [checkRestore](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a8d5f5505568090ea83840b00a7f140b9) (std::string *msg=nullptr) const  
| Test if the link is restored unchanged.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a8d5f5505568090ea83840b00a7f140b9)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnImportExternal](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab29ca627684ca9a3ed573a24eb8da131) (const std::map< std::string, std::string > &nameMap) const  
| Return a copy of the property if any changes caused by importing external
linked object.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab29ca627684ca9a3ed573a24eb8da131)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLabelChange](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a0d1a5adbda3ed0d03313b8827548c1d6) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &ref, const char *newLabel) const  
| Update object label reference in this property.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a0d1a5adbda3ed0d03313b8827548c1d6)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLinkReplace](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ad21232bfd601a848542b503d73d14a9c) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj) const =0  
| Return a copy of the property if the link replacement affects this property.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ad21232bfd601a848542b503d73d14a9c)  
  
void | [getLinkedElements](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a973b1ddfd9b981181395dfb2a305f36d) (std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > &elements, [bool](../../d9/db9/classbool.html) newStyle=true, [bool](../../d9/db9/classbool.html) all=true) const  
| Helper function to return a map of linked object and its subname references.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a973b1ddfd9b981181395dfb2a305f36d)  
  
template<class T >  
void | [getLinkedObjects](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1db655ff563d9cd96529cf687b3c77ea) (T &inserter, [bool](../../d9/db9/classbool.html) all=false) const  
| Helper function to return linked objects using an std::inserter.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1db655ff563d9cd96529cf687b3c77ea)  
  
virtual void | [getLinks](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9ea079fa62ec12eb6f20360e7016f43c) (std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [bool](../../d9/db9/classbool.html) all=false, std::vector< std::string > *subs=nullptr, [bool](../../d9/db9/classbool.html) newStyle=true) const =0  
| Obtain the linked objects.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9ea079fa62ec12eb6f20360e7016f43c)  
  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a80edc3aa77b975c9862ca4ff78179407) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const override  
| Compare if this property has the same content as the given one.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a80edc3aa77b975c9862ca4ff78179407)  
  
std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > | [linkedElements](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af46505016f8488c705e72657917f1630) ([bool](../../d9/db9/classbool.html) newStyle=true, [bool](../../d9/db9/classbool.html) all=true) const  
| Helper function to return a map of linked object and its subname references.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af46505016f8488c705e72657917f1630)  
  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [linkedObjects](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a888cdc4caeaef9a38b3479c34e472bdd) ([bool](../../d9/db9/classbool.html) all=false) const  
| Helper function to return all linked objects of this property.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a888cdc4caeaef9a38b3479c34e472bdd)  
  
|
[PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6dd04e8d33dd47193b8fc86308f1eea7)
()  
virtual [bool](../../d9/db9/classbool.html) | [referenceChanged](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af56b87f577368963c8aeec5a5fc74ee0) () const  
| Test if the element reference has changed after restore.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af56b87f577368963c8aeec5a5fc74ee0)  
  
void | [registerLabelReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a513f32162e505cf9fa6cad8a2d234a1f) (std::vector< std::string > &&labels, [bool](../../d9/db9/classbool.html) reset=true)  
| Register label reference for future object relabel update.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a513f32162e505cf9fa6cad8a2d234a1f)  
  
void | [setAllowExternal](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6a771360ff664dd0f0b740ef566f4254) ([bool](../../d9/db9/classbool.html) allow)  
| Enable/disable temporary holding external object without throwing exception.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6a771360ff664dd0f0b740ef566f4254)  
  
virtual void | [setAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a26441b0567312a6b71c03f2f16dee982) ([bool](../../d9/db9/classbool.html) enable)  
[bool](../../d9/db9/classbool.html) | [testFlag](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7aecf32bcda9d645f8a37ece5c3598ef) ([int](../../d1/da0/classint.html) flag) const  
void | [unregisterElementReference](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aa5ec8a97f53a0928274e9d585a50fd29) ()  
| Clear internal element reference registration.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aa5ec8a97f53a0928274e9d585a50fd29)  
  
void | [unregisterLabelReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aeae2e1785793525c8dd1ae4d26151700) ()  
| Clear internal label references registration.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aeae2e1785793525c8dd1ae4d26151700)  
  
virtual void | [updateElementReference](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6447c82dc0b81cea703a9a235a2448c3) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *feature, [bool](../../d9/db9/classbool.html) reverse=false, [bool](../../d9/db9/classbool.html) notify=false)  
| [Link](../../df/d9b/classApp_1_1Link.html) type property interface APIs
These APIs are moved here so that any type of property can have the property
link behavior, e.g.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6447c82dc0b81cea703a9a235a2448c3)  
  
virtual | [~PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aadb029b9c4d709bffd43d43642e1eaca) ()  
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
[App::ScopedLink](../../df/d30/classApp_1_1ScopedLink.html)  
[LinkScope](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263) | [getScope](../../df/d30/classApp_1_1ScopedLink.html#a820666ea293f55369d42dff0b47f30c1) () const  
| Get the links scope Retrieve what kind of links are allowed.
[More...](../../df/d30/classApp_1_1ScopedLink.html#a820666ea293f55369d42dff0b47f30c1)  
  
void | [setScope](../../df/d30/classApp_1_1ScopedLink.html#a27dac823725787d1ba0db6c7186de85e) ([LinkScope](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263) scope)  
| Set the links scope Allows to define what kind of links are allowed.
[More...](../../df/d30/classApp_1_1ScopedLink.html#a27dac823725787d1ba0db6c7186de85e)  
  
  
##  Static Public Member Functions  
  
---  
static void | [breakLinks](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3a7f63103cb074017ba1d159ada3cc44) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *link, const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [bool](../../d9/db9/classbool.html) clear)  
| Helper function for breaking link properties.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3a7f63103cb074017ba1d159ada3cc44)  
  
static const char * | [exportSubName](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a08eab53abe5c11c895d4ecea426485ad) (std::string &output, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const char *subname, [bool](../../d9/db9/classbool.html) first_obj=false)  
| Helper function to export a subname reference.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a08eab53abe5c11c895d4ecea426485ad)  
  
static void | [getLabelReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab56a3785dd388ecb7db50c9c0f8c8cce) (std::vector< std::string > &labels, const char *subname)  
| Helper function to extract labels from a subname reference.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab56a3785dd388ecb7db50c9c0f8c8cce)  
  
static std::string | [importSubName](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *sub, [bool](../../d9/db9/classbool.html) &restoreLabel)  
| Helper function to import a subname reference.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e)  
  
static void | [restoreLabelReference](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, std::string &sub, [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) *shadow=nullptr)  
| Helper function to restore label references during import.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb)  
  
static [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [tryImport](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a2bf156dd3396caaad6204f5269698e7a) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) *doc, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::map< std::string, std::string > &nameMap)  
| Helper function for link import operation.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a2bf156dd3396caaad6204f5269698e7a)  
  
static std::string | [tryImportSubName](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a368e7609bf8ee24fd6b574c392e8c6d4) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const char *sub, const [App::Document](../../d8/d3e/classApp_1_1Document.html) *doc, const std::map< std::string, std::string > &nameMap)  
| Helper function for link import operation.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a368e7609bf8ee24fd6b574c392e8c6d4)  
  
static std::pair< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::string > | [tryReplaceLink](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95) (const [App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *owner, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj, const char *sub=nullptr)  
| Helper functions.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95)  
  
static std::pair< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > | [tryReplaceLinkSubs](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ae7aa54cba5888dcd26d60876dd7672cc) (const [App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *owner, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj, const std::vector< std::string > &subs)  
| Helper function to check and replace a link with multiple subname
references.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ae7aa54cba5888dcd26d60876dd7672cc)  
  
static void | [updateElementReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a4ead775f36d2ccf4564fb59713a20d94) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *feature, [bool](../../d9/db9/classbool.html) reverse=false)  
| Update all element references in all link properties of _feature_.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a4ead775f36d2ccf4564fb59713a20d94)  
  
static std::string | [updateLabelReference](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ac2fd4f8ba5aeea8846f1ffc1d55e02da) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *linked, const char *subname, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &ref, const char *newLabel)  
| Helper function to update subname reference on label change.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ac2fd4f8ba5aeea8846f1ffc1d55e02da)  
  
static std::vector< std::pair< [Property](../../d0/da9/classApp_1_1Property.html) *, std::unique_ptr< [Property](../../d0/da9/classApp_1_1Property.html) > > > | [updateLabelReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a352aa734ca82348678cc710b1eead0ef) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const char *newLabel)  
| Helper function to collect changed property when an object re-label.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a352aa734ca82348678cc710b1eead0ef)  
  
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
  
##  Protected Member Functions  
  
---  
virtual void | [hasSetValue](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763) () override  
| Gets called by all setValue() methods after the value has changed.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763)  
  
void | [setFlag](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f) ([int](../../d1/da0/classint.html) flag, [bool](../../d9/db9/classbool.html) value=true)  
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
  
  
##  Friends  
  
---  
class | [DocInfo](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a369cdf50b9058a05c8062deaef85826b)  
  
##  Additional Inherited Members  
  
---  
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

Parent class of all link type properties.

## Member Typedef Documentation

## ◆ ShadowSub

typedef std::pair<std::string,std::string>
[App::PropertyLinkBase::ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620)  
---  
  
## Member Enumeration Documentation

## ◆ LinkFlags

enum
[App::PropertyLinkBase::LinkFlags](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5f)  
---  
  
Enumerator  
---  
LinkAllowExternal |   
LinkDetached |   
LinkRestoring |   
LinkAllowPartial |   
LinkRestoreLabel |   
LinkSyncSubObject |   
  
## Constructor & Destructor Documentation

## ◆ PropertyLinkBase()

PropertyLinkBase::PropertyLinkBase  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~PropertyLinkBase()

| PropertyLinkBase::~PropertyLinkBase  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[unregisterElementReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aa5ec8a97f53a0928274e9d585a50fd29),
and
[unregisterLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aeae2e1785793525c8dd1ae4d26151700).

## Member Function Documentation

## ◆ adjustLink()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyLinkBase::adjustLink  | ( | const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _inList_| ) |   
---|---|---|---|---|---  
pure virtual  
  
Called to adjust the link to avoid potential cyclic dependency.

Parameters

     inList| recursive in-list of the would-be parent  
---|---  
  
Returns

    Return whether the link has been adjusted

This function tries to correct the link to avoid any (sub)object inside in-
list. If the adjustment is impossible, exception will be raised

Implemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a6ef128439add23206d190bedd151f02e),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#aebfbbd1933b83fa53b46133da128c17a),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#ab77dc0f1a32bada11823d2c918324da1),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#ac5e4b8833d9c02383d6ce017ca6a7730),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab5bc8a3cb854f5b7643bfdcc4d0cb525),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a33bbd1956612a56e1967fdd7d6c533ff),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a2fbece18bdf273d6c6d427c6cce98da7),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad19a81a5a5f1c88bb669f91604c4fab3).

## ◆ breakLink()

| virtual void App::PropertyLinkBase::breakLink  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _clear_  
| ) | |   
pure virtual  
  
Called to reset this link property.

Parameters

     obj| reset link property if it is linked to this object   
---|---  
clear| if true, then also reset property if the owner of this property is
_obj_  
  
See also

    [breakLinks()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3a7f63103cb074017ba1d159ada3cc44 "Helper function for breaking link properties.")

Implemented in
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a5ba319a4ccf1773412d1d5023482ceda),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa0c652f1384e33bace3fb708d26d57c7),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a53e073970cf9ad76667d02027bb78c84),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#af3659c9cd764ba67a9b4eb61ac10d328),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad8d3af63e632d9e26194e66ed0eaaa68),
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a148b326bca33a5b23cc9434f24b569c2),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ac599df35e52d91896bca5289d1c3c322).

Referenced by
[breakLinks()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3a7f63103cb074017ba1d159ada3cc44).

## ◆ breakLinks()

| void PropertyLinkBase::breakLinks  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _link_ ,   
---|---|---|---  
|  | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ ,   
|  | [bool](../../d9/db9/classbool.html) | _clear_  
| ) | |   
static  
  
Helper function for breaking link properties.

Parameters

     link| reset link property if it is linked to this object   
---|---  
objs| the objects to check for the link properties  
clear| if true, then also reset property if the owner of the link property is
_link_  
  
[App::Document::breakDependency()](../../d8/d3e/classApp_1_1Document.html#af9123db5f932f908555bd61c8db2fb53)
calls this function to break the link property

References
[breakLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9559e2b5adeb74b5dfa23960095b86a9),
and
[App::DocInfo::breakLinks()](../../d7/d23/classApp_1_1DocInfo.html#a9eeca81cb964af7cf2d763d2ae31e199).

Referenced by
[App::Document::breakDependency()](../../d8/d3e/classApp_1_1Document.html#af9123db5f932f908555bd61c8db2fb53).

## ◆ checkLabelReferences()

void PropertyLinkBase::checkLabelReferences  | ( | const std::vector< std::string > & | _subs_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _reset_ = `true`  
| ) | |   
  
Check subnames for label registration.

Parameters

     subs| subname references   
---|---  
reset| if true, then calls unregisterLabelReference() before registering  
  
Check the give subname references and extract any label reference inside (by
calling
[getLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab56a3785dd388ecb7db50c9c0f8c8cce
"Helper function to extract labels from a subname reference.")), and register
them.

References
[getLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab56a3785dd388ecb7db50c9c0f8c8cce),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[registerLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a513f32162e505cf9fa6cad8a2d234a1f),
and
[unregisterLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aeae2e1785793525c8dd1ae4d26151700).

Referenced by
[App::PropertyLinkSubList::addValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17cad50fa5ecc14fafcfc99e3cba7bbd),
[App::PropertyXLink::setSubValues()](../../d2/de2/classApp_1_1PropertyXLink.html#ab317a05477f1ee776d1c4f765b70b1cd),
[App::PropertyLinkSub::setValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9072c1b8bf3ee43a0d82c0e266cc1f33),
[App::PropertyLinkSubList::setValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f),
and
[App::PropertyLinkSubList::setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7).

## ◆ checkRestore()

| virtual [int](../../d1/da0/classint.html) App::PropertyLinkBase::checkRestore  | ( | std::string *  | _msg_ = `nullptr`| ) |  const  
---|---|---|---|---|---  
virtual  
  
Test if the link is restored unchanged.

Parameters

     msg| optional error message  
---|---  
  
Returns

    For external linked object, return 2 in case the link is missing, and 1 if the time stamp has changed. 

Reimplemented in
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#aff57f99ddc399ce82d8f17da884a1052),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a99d92e5122a717c23ebe1834086da5e6),
and
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#ad045569aa3548d2240da8004ebdc6dec).

## ◆ CopyOnImportExternal()

| virtual [Property](../../d0/da9/classApp_1_1Property.html) * App::PropertyLinkBase::CopyOnImportExternal  | ( | const std::map< std::string, std::string > & | _nameMap_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Return a copy of the property if any changes caused by importing external
linked object.

Parameters

     nameMap| a map from the original external object name to the imported new object name  
---|---  
  
Returns

    Returns a copy of the property with the updated link reference if affected. The copy will later be assgiend to this property by calling its [Paste()](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be "Paste the value from the property \(mainly for Undo/Redo and transactions\)"). 

Reimplemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a11bdfc2d9abf09bf1fe331f571a06b52),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a048f449b304bded2a609bc32bc3d3107),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a7d7f8cd3cb3ce4405391586167328afc),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a145fcf5a76cec92e8ca60bad28e6fe76),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a583fcb98efbbb8211cfdd20437688de1),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a91a6447d90678a4b4b73a6b701de9588).

## ◆ CopyOnLabelChange()

| virtual [Property](../../d0/da9/classApp_1_1Property.html) * App::PropertyLinkBase::CopyOnLabelChange  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const std::string & | _ref_ ,   
|  | const char *  | _newLabel_  
| ) | |  const  
virtual  
  
Update object label reference in this property.

Parameters

     obj| the object owner of the changing label   
---|---  
ref| subname reference to old label  
newLabel| the future new label  
  
Returns

    Returns a copy of the property if its link reference is affected. The copy will later be assgiend to this property by calling its [Paste()](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be "Paste the value from the property \(mainly for Undo/Redo and transactions\)"). 

Reimplemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a66d03bca6be021be6445717920c2cc5d),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a09c96d3556fa092d37d9f597fbf468c5),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a832033ed5b5810a9add720cd72ca6cef),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a9c9b89ffa3e4be3e0e5a046e6371e557),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#af9fed844cfcceb8be5f643a0146f7c25),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a68bfc954ffc13f24216d11faae444da4).

## ◆ CopyOnLinkReplace()

| virtual [Property](../../d0/da9/classApp_1_1Property.html) * App::PropertyLinkBase::CopyOnLinkReplace  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _oldObj_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _newObj_  
| ) | |  const  
pure virtual  
  
Return a copy of the property if the link replacement affects this property.

Parameters

     owner| the parent object whose link property is to be replace. Note that The parent may not be the container of this property. [Link](../../df/d9b/classApp_1_1Link.html) sub property can use this opportunity to adjust its relative links.   
---|---  
oldObj| object to be replaced  
newObj| object to replace with  
  
Returns

    Return a copy of the property that is adjusted for the link replacement operation. 

Implemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7d04daa6893b37a24602bb897eec8ed1),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#ae33affee6371a40629ea84b1782c2cb5),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a4406a63b9428c6313f37413a0a8b3821),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a24386974f021c3d8d5c3679276b403bb),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ae849b6086e5b7731cefac897c3c5b3ec),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#aa713c66bf6fd8a5a03ec1f94b233e8bb),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4aeacb995d8cd9f1ddd3309d87703960),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ac7b0e47414a39b37f4bb3f6d8d0ded22).

## ◆ exportSubName()

| const char * PropertyLinkBase::exportSubName  | ( | std::string & | _output_ ,   
---|---|---|---  
|  | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
|  | const char *  | _subname_ ,   
|  | [bool](../../d9/db9/classbool.html) | _first_obj_ = `false`  
| ) | |   
static  
  
Helper function to export a subname reference.

Parameters

     output| output subname if the subname is modified   
---|---  
obj| linked object  
sub| input subname reference  
first_obj| if true, then the first object referenced in subname is obtained by
searching the owner document of obj, otherwise the subname search among obj's
sub-objects.  
  
Returns

    Return output.c_str() if the subname is modified for exporting otherwise, return the input subname

See also

    [importSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e "Helper function to import a subname reference."), [restoreLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb "Helper function to restore label references during import.")

The function go through the input subname reference and changes any sub object
references inside for exporting. If the sub object is referenced by its
internal object name, then the reference is changed from 'objName' to
'objName@docName'. If referenced by label, then it will be changed to
'objName@docName@' instead.
[importSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e
"Helper function to import a subname reference.") and
[restoreLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb
"Helper function to restore label references during import.") can be used
together to restore the reference during import.

References
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
and
[App::Application::getDocument()](../../da/dbf/classApp_1_1Application.html#a17472bb3dfacd07074016c3bcc4a270d).

Referenced by
[App::PropertyLinkSub::Save()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a828dfbbf362ee9875da57453517b3358),
[App::PropertyLinkSubList::Save()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e),
[App::PropertyXLink::Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
and
[App::ObjectIdentifier::toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f).

## ◆ getLabelReferences()

| void PropertyLinkBase::getLabelReferences  | ( | std::vector< std::string > & | _labels_ ,   
---|---|---|---  
|  | const char *  | _subname_  
| ) | |   
static  
  
Helper function to extract labels from a subname reference.

Parameters

     labels| output vector of extracted labels   
---|---  
subname| subname reference  
  
See also

    [registerLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a513f32162e505cf9fa6cad8a2d234a1f "Register label reference for future object relabel update.")

This function is used to extract label from subname reference for registering
of label changes.

Referenced by
[checkLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b),
and
[App::ObjectIdentifier::getDepLabels()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2d8af8b84a0c426af896a2f190b692ce).

## ◆ getLinkedElements()

void App::PropertyLinkBase::getLinkedElements  | ( | std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > & | _elements_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _newStyle_ = `true`,   
|  | [bool](../../d9/db9/classbool.html) | _all_ = `true`  
| ) | |  const  
  
Helper function to return a map of linked object and its subname references.

## ◆ getLinkedObjects()

template<class T >

void App::PropertyLinkBase::getLinkedObjects  | ( | T & | _inserter_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _all_ = `false`  
| ) | |  const  
  
Helper function to return linked objects using an std::inserter.

## ◆ getLinks()

| virtual void App::PropertyLinkBase::getLinks  | ( | std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _all_ = `false`,   
|  | std::vector< std::string > *  | _subs_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _newStyle_ = `true`  
| ) | |  const  
pure virtual  
  
Obtain the linked objects.

Parameters

     objs| hold the returned linked objects on output   
---|---  
all| if true, then return all the linked object regardless of this LinkScope.
If false, then return only if the LinkScope is not hidden.  
sub| if given, then return subname references.  
newStyle| whether to return new or old style subname reference  
  
Implemented in
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a4750ce6a3916cee3e9746a683bbf4330),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a1d790d910805b148e9af595b97864d26),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a161f2ec5e1cbb85d286966066977624b),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#afeb6881f95c7f7f897fb2bfd0ee3895b),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a6d1b6fbac4089fed0e84c4e617cf1f50),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a474c20d3ad36ebec314c141803e0ca3b),
and
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#adc29a7ff5211f6369aeab847422a2e52).

Referenced by
[Gui::Dialog::DlgPropertyLink::getLinksFromProperty()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#ae8f1f2b2b0c06e3d1b20222e0dd3380d),
and
[isSame()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a80edc3aa77b975c9862ca4ff78179407).

## ◆ hasSetValue()

| void PropertyLinkBase::hasSetValue  | ( | void  | | ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
Gets called by all setValue() methods after the value has changed.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

Reimplemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ade4669436aaa4ddc2130f8756ca08585).

References
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
and
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d).

Referenced by
[App::PropertyLinkSubList::addValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17cad50fa5ecc14fafcfc99e3cba7bbd),
[App::PropertyXLinkContainer::breakLink()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a148b326bca33a5b23cc9434f24b569c2),
[App::PropertyXLinkSubList::hasSetChildValue()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a8d97a9deb398fd86589410728dc222bf),
[App::PropertyExpressionEngine::hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
[App::PropertyXLink::hasSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a),
[App::PropertyPlacementLink::Paste()](../../d8/db5/classApp_1_1PropertyPlacementLink.html#aa08172316e8d59b648dcc5ac8266d56e),
[App::PropertyXLinkSubList::Paste()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4ac663947ed88fa49f3a874273098fe4),
[App::PropertyLink::setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1),
[App::PropertyLinkSub::setValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9072c1b8bf3ee43a0d82c0e266cc1f33),
[App::PropertyLinkSubList::setValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f),
[App::PropertyLinkSubList::setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7),
[App::PropertyLinkSub::updateElementReference()](../../d3/d76/classApp_1_1PropertyLinkSub.html#ae5a908ece2ba229bba6411905dd68f82),
and
[App::PropertyLinkSubList::updateElementReference()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca).

## ◆ importSubName()

| std::string PropertyLinkBase::importSubName  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_ ,   
---|---|---|---  
|  | const char *  | _sub_ ,   
|  | [bool](../../d9/db9/classbool.html) & | _restoreLabel_  
| ) | |   
static  
  
Helper function to import a subname reference.

Parameters

     reader| the import reader   
---|---  
sub| input subname reference  
restoreLabel| output indicate whether post process is required after restore.  
  
See also

    [exportSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a08eab53abe5c11c895d4ecea426485ad "Helper function to export a subname reference."), [restoreLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb "Helper function to restore label references during import.")

Returns

    return either an updated subname reference or the input reference if no change. If restoreLabel is set to true on output, it means there are some label reference changes that must be corrected after restore, by calling [restoreLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb "Helper function to restore label references during import.") in property's [afterRestore()](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f "Called at the beginning of Document::afterRestore\(\)"). 

References
[Base::XMLReader::doNameMapping()](../../dc/d95/classBase_1_1XMLReader.html#a1d431382d6f452a2a87cb9c7462d6e72),
and
[Base::XMLReader::getName()](../../dc/d95/classBase_1_1XMLReader.html#aa529233af401d7719226293c506792f8).

Referenced by
[App::ObjectIdentifier::String::checkImport()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a8c71508a5ae7a8b7387e35abe09dac6f),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
and
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c).

## ◆ isSame()

| [bool](../../d9/db9/classbool.html) PropertyLinkBase::isSame  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _other_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Compare if this property has the same content as the given one.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

Reimplemented in [App::PropertyListsT< DocumentObject *, std::vector<
DocumentObject * >, PropertyLinkListBase
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109).

References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[getLinks()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9ea079fa62ec12eb6f20360e7016f43c),
[App::ScopedLink::getScope()](../../df/d30/classApp_1_1ScopedLink.html#a820666ea293f55369d42dff0b47f30c1),
and
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127).

## ◆ linkedElements()

std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > App::PropertyLinkBase::linkedElements  | ( | [bool](../../d9/db9/classbool.html) | _newStyle_ = `true`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _all_ = `true`  
| ) | |  const  
  
Helper function to return a map of linked object and its subname references.

## ◆ linkedObjects()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > App::PropertyLinkBase::linkedObjects  | ( | [bool](../../d9/db9/classbool.html) | _all_ = `false`| ) |  const  
---|---|---|---|---|---  
  
Helper function to return all linked objects of this property.

## ◆ referenceChanged()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyLinkBase::referenceChanged  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Test if the element reference has changed after restore.

Reimplemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#af2b60f6411ba6c62236a29c0769b76bd),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a841afee60c53207a8f66e42e7a60753d),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a5fd01b6a881d77b42dbc299edac1de0a),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a64775c79df3f1636f0c8b75b61f7cbff),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a00709d08884ac1fa1952b0836d822a2b),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a14741763e93a2cafcddc31871617285a).

## ◆ registerLabelReferences()

void PropertyLinkBase::registerLabelReferences  | ( | std::vector< std::string > && | _labels_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _reset_ = `true`  
| ) | |   
  
Register label reference for future object relabel update.

Parameters

     labels| labels to be registered   
---|---  
reset| if true, then calls unregisterLabelReference() before registering  
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[unregisterLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aeae2e1785793525c8dd1ae4d26151700).

Referenced by
[checkLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b),
[App::PropertyExpressionEngine::hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
and
[Spreadsheet::PropertySheet::hasSetValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ade4669436aaa4ddc2130f8756ca08585).

## ◆ restoreLabelReference()

| void PropertyLinkBase::restoreLabelReference  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | std::string & | _sub_ ,   
|  | [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) *  | _shadow_ = `nullptr`  
| ) | |   
static  
  
Helper function to restore label references during import.

Parameters

     obj| linked object   
---|---  
sub| subname reference  
shadow| optional shadow subname reference  
  
See also

    [exportSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a08eab53abe5c11c895d4ecea426485ad "Helper function to export a subname reference."), [importSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e "Helper function to import a subname reference.")

When exporting and importing (i.e. copy and paste) objects into the same
document, the new object must be renamed, both the internal name and the
label. Therefore, the link reference of the new objects must be corrected
accordingly. The basic idea is that when exporting object, all object name
references are changed to 'objName@docName', and label references are changed
to 'objName@docName@'. During import, MergeDocument will maintain a map from
objName@docName to object's new name. Object name reference can be restored on
spot by consulting the map, while label reference will be restored later in
property's
[afterRestore()](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f
"Called at the beginning of Document::afterRestore\(\)") function, which calls
this function to do the string parsing.

References
[App::PropertyString::getStrValue()](../../dd/df8/classApp_1_1PropertyString.html#a7fdb947ab6f9552c1dd95a8e634c83c2),
[App::DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6),
and
[App::DocumentObject::Label](../../d2/de4/classApp_1_1DocumentObject.html#a7259f450fea1a74073e626115d46110d).

Referenced by
[App::PropertyLinkSub::afterRestore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a3f55d05db5c992052bd196642b1c01ea),
[App::PropertyLinkSubList::afterRestore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a54c5bae021df3175a6bc3c37fae06e01),
[App::PropertyXLink::afterRestore()](../../d2/de2/classApp_1_1PropertyXLink.html#a01ca28793b37026f539afb49f397aec2),
and
[App::ObjectIdentifier::String::checkImport()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a8c71508a5ae7a8b7387e35abe09dac6f).

## ◆ setAllowExternal()

void PropertyLinkBase::setAllowExternal  | ( | [bool](../../d9/db9/classbool.html) | _allow_| ) |   
---|---|---|---|---|---  
  
Enable/disable temporary holding external object without throwing exception.

Warning, non-PropertyXLink related property does not have internal tracking of
external objects, therefore the link will not by auto broken when external
document is closed. Only use this for temporary case, or if you handle
signalDeleteDocument yourself, or use one of the
[PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html "Link to an
\(sub\)object in the same or different document.") related property.

References
[LinkAllowExternal](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fad0f16a963cb6d4ee03471a56eb0d2b2e),
and
[setFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f).

Referenced by
[App::PropertyXLinkSubList::setPyObject()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a7160ec1120efe0609b40286324fc861f),
and
[App::PropertyXLinkList::setPyObject()](../../df/d17/classApp_1_1PropertyXLinkList.html#a2f618a6e3542cb338064a4d268277290).

## ◆ setAllowPartial()

| virtual void App::PropertyLinkBase::setAllowPartial  | ( | [bool](../../d9/db9/classbool.html) | _enable_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#af69aa75e548072c713a0b180cadab17e),
and
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#af1e65ab203efb67b27a0a5ed306d2c66).

## ◆ setFlag()

| void App::PropertyLinkBase::setFlag  | ( | [int](../../d1/da0/classint.html) | _flag_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _value_ = `true`  
| ) | |   
protected  
  
Referenced by
[App::PropertyLinkSub::afterRestore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a3f55d05db5c992052bd196642b1c01ea),
[App::PropertyLinkSubList::afterRestore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a54c5bae021df3175a6bc3c37fae06e01),
[App::PropertyXLink::afterRestore()](../../d2/de2/classApp_1_1PropertyXLink.html#a01ca28793b37026f539afb49f397aec2),
[App::PropertyXLink::Paste()](../../d2/de2/classApp_1_1PropertyXLink.html#a6d593eed6217cccfdad4a79a4c752c27),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[App::PropertyXLinkSubList::Restore()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a1a047c1c95612cfc2e4ca4a91491d995),
[App::PropertyXLink::restoreLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a232e8182760d7ae2717d555416e4b4ce),
[setAllowExternal()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6a771360ff664dd0f0b740ef566f4254),
[App::PropertyXLink::setAllowPartial()](../../d2/de2/classApp_1_1PropertyXLink.html#af69aa75e548072c713a0b180cadab17e),
[App::PropertyXLinkSubList::setAllowPartial()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#af1e65ab203efb67b27a0a5ed306d2c66),
and
[App::PropertyXLink::setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10).

## ◆ testFlag()

[bool](../../d9/db9/classbool.html) App::PropertyLinkBase::testFlag  | ( | [int](../../d1/da0/classint.html) | _flag_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[App::PropertyXLinkSubList::addValue()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a91e5e534b886db50520e0b006556b76a),
[App::PropertyLinkSub::afterRestore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a3f55d05db5c992052bd196642b1c01ea),
[App::PropertyLinkSubList::afterRestore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a54c5bae021df3175a6bc3c37fae06e01),
[App::PropertyXLink::afterRestore()](../../d2/de2/classApp_1_1PropertyXLink.html#a01ca28793b37026f539afb49f397aec2),
[App::PropertyXLink::checkRestore()](../../d2/de2/classApp_1_1PropertyXLink.html#aff57f99ddc399ce82d8f17da884a1052),
[App::PropertyXLinkSubList::Copy()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad3ce8f501efd0cdd27a89018b7fe7672),
[App::PropertyExpressionEngine::hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
[Spreadsheet::PropertySheet::hasSetValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ade4669436aaa4ddc2130f8756ca08585),
[App::PropertyXLinkSubList::Paste()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4ac663947ed88fa49f3a874273098fe4),
[App::PropertyXLink::Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[App::PropertyXLinkSubList::Save()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a456f78573d34d76300c400382a36960d),
[App::PropertyXLinkSubList::set1Value()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a0760be6f2e7246ec19c223f163cbe17d),
[App::PropertyLink::setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1),
[App::PropertyLinkSub::setValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9072c1b8bf3ee43a0d82c0e266cc1f33),
[App::PropertyLinkList::setValues()](../../d3/d8c/classApp_1_1PropertyLinkList.html#af7e153c0a4b95bb6b79a5b2b357d5a48),
[App::PropertyXLinkSubList::setValues()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a47d377efbb84d5b9671d95726132302a),
[App::PropertyXLinkContainer::updateDeps()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a83acea46b0d063043f43d99de26dfe29),
and
[App::PropertyXLinkSubList::upgrade()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2).

## ◆ tryImport()

| [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * PropertyLinkBase::tryImport  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_ ,   
---|---|---|---  
|  | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
|  | const std::map< std::string, std::string > & | _nameMap_  
| ) | |   
static  
  
Helper function for link import operation.

Parameters

     doc| owner document of the imported objects   
---|---  
obj| the linked object  
nameMap| a name map from source object to its imported counter part  
  
Returns

    Return the imported object if found, or the input `obj` if no change. 

See also

    tryImportSubNames

This function searches for the name map and tries to find the imported object
from the given source object.

Referenced by
[App::PropertyLinkSub::CopyOnImportExternal()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a048f449b304bded2a609bc32bc3d3107),
[App::PropertyLinkSubList::CopyOnImportExternal()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a7d7f8cd3cb3ce4405391586167328afc),
and
[App::PropertyXLink::CopyOnImportExternal()](../../d2/de2/classApp_1_1PropertyXLink.html#a145fcf5a76cec92e8ca60bad28e6fe76).

## ◆ tryImportSubName()

| std::string PropertyLinkBase::tryImportSubName  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const char *  | _sub_ ,   
|  | const [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_ ,   
|  | const std::map< std::string, std::string > & | _nameMap_  
| ) | |   
static  
  
Helper function for link import operation.

Parameters

     obj| the linked object   
---|---  
sub| subname reference  
doc| importing document  
nameMap| a name map from source object to its imported counter part  
  
Returns

    Return a changed subname reference, or empty string if no change.

[Link](../../df/d9b/classApp_1_1Link.html) import operation will go through
all link property and imports all externally linked object. After import, the
link property must be changed to point to the newly imported objects, which
should happen inside the API
[CopyOnImportExternal()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab29ca627684ca9a3ed573a24eb8da131
"Return a copy of the property if any changes caused by importing external
linked object."). This function helps to rewrite subname reference to point to
the correct sub objects that are imported.

Referenced by
[App::PropertyLinkSub::CopyOnImportExternal()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a048f449b304bded2a609bc32bc3d3107),
[App::PropertyLinkSubList::CopyOnImportExternal()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a7d7f8cd3cb3ce4405391586167328afc),
[App::PropertyXLink::CopyOnImportExternal()](../../d2/de2/classApp_1_1PropertyXLink.html#a145fcf5a76cec92e8ca60bad28e6fe76),
and
[App::Expression::importSubNames()](../../dc/d5c/classApp_1_1Expression.html#a6b338d5ca7344c41547dfe77019cf1e1).

## ◆ tryReplaceLink()

| std::pair< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::string > PropertyLinkBase::tryReplaceLink  | ( | const [App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *  | _owner_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
|  | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _oldObj_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _newObj_ ,   
|  | const char *  | _sub_ = `nullptr`  
| ) | |   
static  
  
Helper functions.

Helper function to check and replace a link

Parameters

     owner| the owner of the current property   
---|---  
obj| the current linked object  
parent| the parent of the changing link property, may or may not be equal to
`owner`  
oldObj| the object to be replaced  
newObj| the object to replace with  
sub| optional the current subname reference  
  
Returns

    Returns a pair(obj,subname). If no replacement is found, pair.first will be NULL

Say a group has one of its child object replaced with another. Any existing
link sub reference that refer to the original child object through the group
will be broken. This helper function is used to check and correct any link sub
reference.

References
[App::PropertyContainer::getFullName()](../../d5/d48/classApp_1_1PropertyContainer.html#a331110f1aeffb0a907ac2b74f78cc69d),
[App::DocumentObject::getFullName()](../../d2/de4/classApp_1_1DocumentObject.html#ab9ad25e711d56a5d6c8ba0f7638a8a62),
[App::Property::getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[App::DocumentObject::Label](../../d2/de4/classApp_1_1DocumentObject.html#a7259f450fea1a74073e626115d46110d),
and
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

Referenced by
[App::PropertyLink::CopyOnLinkReplace()](../../d4/d77/classApp_1_1PropertyLink.html#ae33affee6371a40629ea84b1782c2cb5),
[App::PropertyLinkList::CopyOnLinkReplace()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a4406a63b9428c6313f37413a0a8b3821),
[App::PropertyLinkSubList::CopyOnLinkReplace()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ae849b6086e5b7731cefac897c3c5b3ec),
[App::ObjectIdentifier::replaceObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a80caff359bff231c8a61c0a77bda725f),
and
[tryReplaceLinkSubs()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ae7aa54cba5888dcd26d60876dd7672cc).

## ◆ tryReplaceLinkSubs()

| std::pair< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > PropertyLinkBase::tryReplaceLinkSubs  | ( | const [App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *  | _owner_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
|  | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _oldObj_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _newObj_ ,   
|  | const std::vector< std::string > & | _subs_  
| ) | |   
static  
  
Helper function to check and replace a link with multiple subname references.

Parameters

     owner| the owner of the current property   
---|---  
obj| the current linked object  
parent| the parent of the changing link property, may or may not be equal to
`owner`  
oldObj| the object to be replaced  
newObj| the object to replace with  
subs| the current subname references  
  
Returns

    Returns the a pair(obj,subs). If no replacement is found, pair.first will be NULL 

See also

    [tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95 "Helper functions.")

References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95).

Referenced by
[App::PropertyLinkSub::CopyOnLinkReplace()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a24386974f021c3d8d5c3679276b403bb),
and
[App::PropertyXLink::CopyOnLinkReplace()](../../d2/de2/classApp_1_1PropertyXLink.html#aa713c66bf6fd8a5a03ec1f94b233e8bb).

## ◆ unregisterElementReference()

void PropertyLinkBase::unregisterElementReference  | ( | | ) |   
---|---|---|---|---  
  
Clear internal element reference registration.

Referenced by
[App::PropertyExpressionEngine::hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
[Spreadsheet::PropertySheet::hasSetValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ade4669436aaa4ddc2130f8756ca08585),
[App::PropertyExpressionEngine::onContainerRestored()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a733f20b00486b5e21694ee2607fdae92),
[App::PropertyLinkSub::onContainerRestored()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a1ad3eb4664b30fde709d6af5a8ca10a4),
[App::PropertyLinkSubList::onContainerRestored()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a1cd3b87ac48e486bbc2ea858e069ff98),
[Spreadsheet::PropertySheet::onContainerRestored()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a1eb52a89dd270eb5d2562665b0bbfdca),
[App::PropertyExpressionEngine::updateElementReference()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a00a63354dd2052c675de28c01ff70362),
[Spreadsheet::PropertySheet::updateElementReference()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a35d58b0bf7eac198ffdae31e16f3173f),
[App::PropertyLinkSubList::updateElementReference()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca),
and
[~PropertyLinkBase()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aadb029b9c4d709bffd43d43642e1eaca).

## ◆ unregisterLabelReferences()

void PropertyLinkBase::unregisterLabelReferences  | ( | | ) |   
---|---|---|---|---  
  
Clear internal label references registration.

Referenced by
[checkLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b),
[registerLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a513f32162e505cf9fa6cad8a2d234a1f),
and
[~PropertyLinkBase()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aadb029b9c4d709bffd43d43642e1eaca).

## ◆ updateElementReference()

| virtual void App::PropertyLinkBase::updateElementReference  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _feature_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _reverse_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _notify_ = `false`  
| ) | |   
virtual  
  
[Link](../../df/d9b/classApp_1_1Link.html) type property interface APIs These
APIs are moved here so that any type of property can have the property link
behavior, e.g.

the
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
Called to update the element reference of this link property

See also

    _updateElementReference() 

Reimplemented in
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a00a63354dd2052c675de28c01ff70362),
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a35d58b0bf7eac198ffdae31e16f3173f),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#ae5a908ece2ba229bba6411905dd68f82),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a94e60fa4261d661b629b5c0d35215dff),
and
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad139ceb8061df8903e132dd84e2b050c).

References
[femsolver.signal::notify()](../../dc/de2/group__FEM.html#ga6389100f2d948a9fe194b395ac11f82c).

## ◆ updateElementReferences()

| void PropertyLinkBase::updateElementReferences  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _feature_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _reverse_ = `false`  
| ) | |   
static  
  
Update all element references in all link properties of _feature_.

## ◆ updateLabelReference()

| std::string PropertyLinkBase::updateLabelReference  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _linked_ ,   
---|---|---|---  
|  | const char *  | _subname_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
|  | const std::string & | _ref_ ,   
|  | const char *  | _newLabel_  
| ) | |   
static  
  
Helper function to update subname reference on label change.

Parameters

     linked| linked object   
---|---  
subname| subname reference  
obj| the object that owns the label  
ref| label reference in the format of '$<old_label>.', which is the format
used in subname reference for label reference. This parameter is provided for
easy search of label reference.  
newLabel| new label  
  
Returns

    Returns an updated subname reference, or empty string if no change.

This function helps to update subname reference on label change. It is usually
called inside
[CopyOnLabelChange()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a0d1a5adbda3ed0d03313b8827548c1d6
"Update object label reference in this property."), the API for handling label
change, which is called just before label change. In other word, when called,
the sub object can still be reached using the original label references, but
not the new labels.

References
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
and
[App::DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6).

Referenced by
[App::PropertyLinkSub::CopyOnLabelChange()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a09c96d3556fa092d37d9f597fbf468c5),
[App::PropertyLinkSubList::CopyOnLabelChange()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a832033ed5b5810a9add720cd72ca6cef),
[App::PropertyXLink::CopyOnLabelChange()](../../d2/de2/classApp_1_1PropertyXLink.html#a9c9b89ffa3e4be3e0e5a046e6371e557),
and
[App::ObjectIdentifier::updateLabelReference()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8ee527f0da9e9a1d26e8744d048ced67).

## ◆ updateLabelReferences()

| std::vector< std::pair< [Property](../../d0/da9/classApp_1_1Property.html) *, std::unique_ptr< [Property](../../d0/da9/classApp_1_1Property.html) > > > PropertyLinkBase::updateLabelReferences  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const char *  | _newLabel_  
| ) | |   
static  
  
Helper function to collect changed property when an object re-label.

Parameters

     obj| the object that owns the label   
---|---  
newLabel| the new label  
  
Returns

    return a map from the affected property to a copy of it with updated subname references 

References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

Referenced by
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

## Friends And Related Function Documentation

## ◆ DocInfo

| [friend](../../d7/d23/classfriend.html) class
[DocInfo](../../d7/d23/classApp_1_1DocInfo.html)  
---  
friend  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyLinks.h
  * FreeCAD/src/App/PropertyLinks.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

