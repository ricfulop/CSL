---
url: https://freecad.github.io/SourceDoc/d9/d92/classApp_1_1PropertyLinkSubList.html
scraped_at: 2025-09-08T14:56:16.209391
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html)

[List of all members](../../d6/d83/classApp_1_1PropertyLinkSubList-members.html) | Public Types | Public Member Functions

App::PropertyLinkSubList Class Reference

`#include <PropertyLinks.h>`

##  Public Types  
  
---  
typedef std::pair< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > | [SubSet](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a505e6fb22604ccc4dce91aab5f7c592a)  
![-](../../closed.png) Public Types inherited from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)  
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
void | [addValue](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17cad50fa5ecc14fafcfc99e3cba7bbd) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::vector< std::string > &SubList={}, [bool](../../d9/db9/classbool.html) reset=false)  
virtual [bool](../../d9/db9/classbool.html) | [adjustLink](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab5bc8a3cb854f5b7643bfdcc4d0cb525) (const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList) override  
| Called to adjust the link to avoid potential cyclic dependency.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab5bc8a3cb854f5b7643bfdcc4d0cb525)  
  
virtual void | [afterRestore](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a54c5bae021df3175a6bc3c37fae06e01) () override  
| Called at the beginning of
[Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5)
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a54c5bae021df3175a6bc3c37fae06e01)  
  
virtual void | [breakLink](../../d9/d92/classApp_1_1PropertyLinkSubList.html#af3659c9cd764ba67a9b4eb61ac10d328) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) clear) override  
| Called to reset this link property.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#af3659c9cd764ba67a9b4eb61ac10d328)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab28f0a208ed6e4b6dafce9d09555dcb7) (void) const override  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab28f0a208ed6e4b6dafce9d09555dcb7)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnImportExternal](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a7d7f8cd3cb3ce4405391586167328afc) (const std::map< std::string, std::string > &nameMap) const override  
| Return a copy of the property if any changes caused by importing external
object.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a7d7f8cd3cb3ce4405391586167328afc)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLabelChange](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a832033ed5b5810a9add720cd72ca6cef) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &ref, const char *newLabel) const override  
| Update object label reference in this property.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a832033ed5b5810a9add720cd72ca6cef)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLinkReplace](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ae849b6086e5b7731cefac897c3c5b3ec) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj) const override  
| Return a copy of the property if the link replacement affects this property.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ae849b6086e5b7731cefac897c3c5b3ec)  
  
virtual const char * | [getEditorName](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a90a55f07008b2770f8f94acf4cce8aae) (void) const override  
| Get the class name of the associated property editor item.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a90a55f07008b2770f8f94acf4cce8aae)  
  
virtual void | [getLinks](../../d9/d92/classApp_1_1PropertyLinkSubList.html#afeb6881f95c7f7f897fb2bfd0ee3895b) (std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [bool](../../d9/db9/classbool.html) all=false, std::vector< std::string > *subs=nullptr, [bool](../../d9/db9/classbool.html) newStyle=true) const override  
| Obtain the linked objects.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#afeb6881f95c7f7f897fb2bfd0ee3895b)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a05d3ff3e3e2e736467523e3fbc715df0) (void) const override  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a05d3ff3e3e2e736467523e3fbc715df0)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a07c5d74e2725f2d1e804d3706d239e2e) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a07c5d74e2725f2d1e804d3706d239e2e)  
  
const std::string | [getPyReprString](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac644eeeab4af18d5ec980d4f9640fe3b) () const  
const std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > & | [getShadowSubs](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a938c0909c322300dd3ab0bac5ea3aec9) () const  
[int](../../d1/da0/classint.html) | [getSize](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aed336221f52dede47a507aed1f382dd7) (void) const  
std::vector< [SubSet](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a505e6fb22604ccc4dce91aab5f7c592a) > | [getSubListValues](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa208d82fb9a55d891ce9354a9386852b) ([bool](../../d9/db9/classbool.html) newStyle=false) const  
std::vector< std::string > | [getSubValues](../../d9/d92/classApp_1_1PropertyLinkSubList.html#abc93806562f9a38a2ab45afea623fd66) ([bool](../../d9/db9/classbool.html) newStyle) const  
const std::vector< std::string > & | [getSubValues](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a9a725b9517a6ff87f8811a75d71aa9ef) (void) const  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getValue](../../d9/d92/classApp_1_1PropertyLinkSubList.html#add029017b408a53cc8fcaa6967af394e) () const  
| getValue emulates the action of a single-object link.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#add029017b408a53cc8fcaa6967af394e)  
  
const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | [getValues](../../d9/d92/classApp_1_1PropertyLinkSubList.html#af073aea1824333723ab0d962040d8713) (void) const  
virtual void | [onContainerRestored](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a1cd3b87ac48e486bbc2ea858e069ff98) () override  
| Called before calling
[DocumentObject::onDocumentRestored()](../../d2/de4/classApp_1_1DocumentObject.html#a0ee8399fa0b176c64895150691a4b604
"get called after a document has been fully restored")
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a1cd3b87ac48e486bbc2ea858e069ff98)  
  
virtual void | [Paste](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a3dfbcd135189c2b3e6e7c6136ed572a1) (const [Property](../../d0/da9/classApp_1_1Property.html) &from) override  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a3dfbcd135189c2b3e6e7c6136ed572a1)  
  
|
[PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a49e1373bc0627069ce85513ed8bdb480)
()  
| A constructor.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a49e1373bc0627069ce85513ed8bdb480)  
  
virtual [bool](../../d9/db9/classbool.html) | [referenceChanged](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a5fd01b6a881d77b42dbc299edac1de0a) () const override  
| Test if the element reference has changed after restore.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a5fd01b6a881d77b42dbc299edac1de0a)  
  
[int](../../d1/da0/classint.html) | [removeValue](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a6e6084e9fe235dbf474585762125e351) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *lValue)  
| Removes all occurrences of _lValue_ in the property together with its sub-
elements and returns the number of entries removed.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a6e6084e9fe235dbf474585762125e351)  
  
virtual void | [Restore](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b)  
  
virtual void | [Save](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e)  
  
virtual void | [setPyObject](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a495ec38be0d7ceb20aa9b3d5a520fdfa) ([PyObject](../../df/d1b/classPyObject.html) *) override  
void | [setSize](../../d9/d92/classApp_1_1PropertyLinkSubList.html#acda76fad9dcfaade00cb6bdcd63219d7) ([int](../../d1/da0/classint.html) newSize)  
void | [setSubListValues](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a4e3800926a177586d370a9a8529ec46f) (const std::vector< [SubSet](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a505e6fb22604ccc4dce91aab5f7c592a) > &)  
void | [setSyncSubObject](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aba6cc3f25d7e70f397f5b51c1656a4ac) ([bool](../../d9/db9/classbool.html) enable)  
void | [setValue](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a6429e5fa2a685d8904a37e30d78ecb6c) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *lValue, const std::vector< std::string > &SubList=std::vector< std::string >())  
| setValue: PropertyLinkSub-compatible overload
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a6429e5fa2a685d8904a37e30d78ecb6c)  
  
void | [setValue](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, const char *)  
| Sets the property.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f)  
  
void | [setValues](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7) (const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, const std::vector< const char * > &)  
void | [setValues](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a80bd9cad2a6b8ee3f81125eba1c82e06) (const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, const std::vector< std::string > &, std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > &&ShadowSubList={})  
void | [setValues](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab4601dd38e356b8329be954ce57f160f) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &&, std::vector< std::string > &&subs, std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > &&ShadowSubList={})  
virtual void | [updateElementReference](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *feature, [bool](../../d9/db9/classbool.html) reverse=false, [bool](../../d9/db9/classbool.html) notify=false) override  
| [Link](../../df/d9b/classApp_1_1Link.html) type property interface APIs
These APIs are moved here so that any type of property can have the property
link behavior, e.g.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca)  
  
[bool](../../d9/db9/classbool.html) | [upgrade](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *typeName)  
virtual | [~PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17189b0ae71b797884f1ca041cfe263f) ()  
| A destructor.
[More...](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17189b0ae71b797884f1ca041cfe263f)  
  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)  
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
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Public Member Functions inherited from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)  
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
![-](../../closed.png) Public Attributes inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
boost::signals2::signal< void(const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChanged](../../d0/da9/classApp_1_1Property.html#a9e9e25207ee1e619c75f835f9853cf74)  
![-](../../closed.png) Protected Member Functions inherited from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)  
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
  
  
## Member Typedef Documentation

## ◆ SubSet

typedef
std::pair<[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*,
std::vector<std::string> >
[App::PropertyLinkSubList::SubSet](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a505e6fb22604ccc4dce91aab5f7c592a)  
---  
  
## Constructor & Destructor Documentation

## ◆ PropertyLinkSubList()

PropertyLinkSubList::PropertyLinkSubList  | ( | | ) |   
---|---|---|---|---  
  
A constructor.

A more elaborate description of the constructor.

Referenced by
[Copy()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab28f0a208ed6e4b6dafce9d09555dcb7).

## ◆ ~PropertyLinkSubList()

| PropertyLinkSubList::~PropertyLinkSubList  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
and
[App::DocumentObject::testStatus()](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120).

## Member Function Documentation

## ◆ addValue()

void PropertyLinkSubList::addValue  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const std::vector< std::string > & | _SubList_ = `{}`,   
|  | [bool](../../d9/db9/classbool.html) | _reset_ = `false`  
| ) | |   
  
References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::PropertyLinkBase::checkLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[App::DocumentObject::testStatus()](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120),
and
[updateElementReference()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca).

Referenced by
[PartDesignGui::TaskPipeScaling::referenceSelected()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#ac9f1c0754a7abf2a4e59c0218c73829a).

## ◆ adjustLink()

| [bool](../../d9/db9/classbool.html) PropertyLinkSubList::adjustLink  | ( | const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _inList_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Called to adjust the link to avoid potential cyclic dependency.

Parameters

     inList| recursive in-list of the would-be parent  
---|---  
  
Returns

    Return whether the link has been adjusted

This function tries to correct the link to avoid any (sub)object inside in-
list. If the adjustment is impossible, exception will be raised

Implements
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1ce35c00cf2495906301c94a0ea22c80).

References
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
and
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7).

## ◆ afterRestore()

| void PropertyLinkSubList::afterRestore  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
Called at the beginning of
[Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5)

This function is called without dependency sorting, because some types of link
property can only reconstructs the linking information inside this function.

One example use case of this function is
[PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html "the Link
Property with sub elements This property links an object and a defined
sequence of sub eleme...") that uses
[afterRestore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a54c5bae021df3175a6bc3c37fae06e01
"Called at the beginning of Document::afterRestore\(\)") to parse and restore
subname references, which may contain sub-object reference from external
document, and there will be special mapping required during object import.

Another example is
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
which only parse the restored expression in
[afterRestore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a54c5bae021df3175a6bc3c37fae06e01
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

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f).

References
[App::PropertyLinkBase::LinkRestoreLabel](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fa5a4bc69cb609a1f93370ec11e29dc403),
[App::PropertyLinkBase::restoreLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb),
[App::PropertyLinkBase::setFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f),
and
[App::PropertyLinkBase::testFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7aecf32bcda9d645f8a37ece5c3598ef).

## ◆ breakLink()

| void PropertyLinkSubList::breakLink  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _clear_  
| ) | |   
overridevirtual  
  
Called to reset this link property.

Parameters

     obj| reset link property if it is linked to this object   
---|---  
clear| if true, then also reset property if the owner of this property is
_obj_  
  
See also

    [breakLinks()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3a7f63103cb074017ba1d159ada3cc44 "Helper function for breaking link properties.")

Implements
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9559e2b5adeb74b5dfa23960095b86a9).

References
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
and
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7).

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyLinkSubList::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

References
[PropertyLinkSubList()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a49e1373bc0627069ce85513ed8bdb480).

## ◆ CopyOnImportExternal()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyLinkSubList::CopyOnImportExternal  | ( | const std::map< std::string, std::string > & | _nameMap_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Return a copy of the property if any changes caused by importing external
object.

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab29ca627684ca9a3ed573a24eb8da131).

References
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[App::PropertyLinkBase::tryImport()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a2bf156dd3396caaad6204f5269698e7a),
and
[App::PropertyLinkBase::tryImportSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a368e7609bf8ee24fd6b574c392e8c6d4).

## ◆ CopyOnLabelChange()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyLinkSubList::CopyOnLabelChange  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const std::string & | _ref_ ,   
|  | const char *  | _newLabel_  
| ) | |  const  
overridevirtual  
  
Update object label reference in this property.

Parameters

     obj| the object owner of the changing label   
---|---  
ref| subname reference to old label  
newLabel| the future new label  
  
Returns

    Returns a copy of the property if its link reference is affected. The copy will later be assgiend to this property by calling its [Paste()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a3dfbcd135189c2b3e6e7c6136ed572a1 "Paste the value from the property \(mainly for Undo/Redo and transactions\)"). 

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a0d1a5adbda3ed0d03313b8827548c1d6).

References
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[App::PropertyLinkBase::updateLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ac2fd4f8ba5aeea8846f1ffc1d55e02da).

## ◆ CopyOnLinkReplace()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyLinkSubList::CopyOnLinkReplace  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _oldObj_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _newObj_  
| ) | |  const  
overridevirtual  
  
Return a copy of the property if the link replacement affects this property.

Parameters

     owner| the parent object whose link property is to be replace. Note that The parent may not be the container of this property. [Link](../../df/d9b/classApp_1_1Link.html) sub property can use this opportunity to adjust its relative links.   
---|---  
oldObj| object to be replaced  
newObj| object to replace with  
  
Returns

    Return a copy of the property that is adjusted for the link replacement operation. 

Implements
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ad21232bfd601a848542b503d73d14a9c).

References
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[App::PropertyLinkBase::tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95).

## ◆ getEditorName()

| virtual const char * App::PropertyLinkSubList::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

## ◆ getLinks()

| void PropertyLinkSubList::getLinks  | ( | std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _all_ = `false`,   
|  | std::vector< std::string > *  | _subs_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _newStyle_ = `true`  
| ) | |  const  
overridevirtual  
  
Obtain the linked objects.

Parameters

     objs| hold the returned linked objects on output   
---|---  
all| if true, then return all the linked object regardless of this LinkScope.
If false, then return only if the LinkScope is not hidden.  
sub| if given, then return subname references.  
newStyle| whether to return new or old style subname reference  
  
Implements
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9ea079fa62ec12eb6f20360e7016f43c).

References
[getSubValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a9a725b9517a6ff87f8811a75d71aa9ef),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
and
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) PropertyLinkSubList::getMemSize  | ( | void  | | ) |  const  
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

References
[getSize()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aed336221f52dede47a507aed1f382dd7).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyLinkSubList::getPyObject  | ( | void  | | ) |   
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

References
[getPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a07c5d74e2725f2d1e804d3706d239e2e),
[getSize()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aed336221f52dede47a507aed1f382dd7),
[getSubListValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa208d82fb9a55d891ce9354a9386852b),
and
[DraftVecUtils::tup()](../../dc/dc3/group__DRAFTVECUTILS.html#gada8f1f6ff2e9aca9a3ff9384ae3bbd27).

Referenced by
[getPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a07c5d74e2725f2d1e804d3706d239e2e).

## ◆ getPyReprString()

const string PropertyLinkSubList::getPyReprString  | ( | | ) |  const  
---|---|---|---|---  
  
References
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
and
[App::Document::getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d).

Referenced by
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346).

## ◆ getShadowSubs()

const std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > & App::PropertyLinkSubList::getShadowSubs  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getSize()

[int](../../d1/da0/classint.html) PropertyLinkSubList::getSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[Measure::Measurement::addReference3D()](../../d6/d84/classMeasure_1_1Measurement.html#a3bcf491038f843ac79c89cdff8925555),
[Measure::Measurement::angle()](../../d6/d84/classMeasure_1_1Measurement.html#a14819c13176bdf930004bef6f290385b),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[Measure::Measurement::delta()](../../d6/d84/classMeasure_1_1Measurement.html#ae7ad27b4e881bd7ad077a64018fed4eb),
[Surface::Filling::execute()](../../d8/df7/classSurface_1_1Filling.html#ab31cd9c2fd6bd4e15a80b7065c071eae),
[getMemSize()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a05d3ff3e3e2e736467523e3fbc715df0),
[getPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a07c5d74e2725f2d1e804d3706d239e2e),
[Measure::Measurement::has3DReferences()](../../d6/d84/classMeasure_1_1Measurement.html#af5ed451628e40c3bb51dcf2b76253a9e),
[TechDraw::DrawViewDimension::has3DReferences()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2e4688e6ea3ee4cd7178a9670b5363ee),
[Measure::Measurement::length()](../../d6/d84/classMeasure_1_1Measurement.html#a3f3068c7bbf6c06438658dea6f675c17),
[Measure::Measurement::massCenter()](../../d6/d84/classMeasure_1_1Measurement.html#a1c65790f4b19fbcd61b814beaad8f4bc),
[Surface::GeomFillSurface::onChanged()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a3bfc3e08b782ee0cb3ccb98f8dd1600f),
[Sketcher::SketchObject::onChanged()](../../d9/dad/classSketcher_1_1SketchObject.html#a838e11f3f3d9b47452ece92f8057bff1),
[Measure::Measurement::radius()](../../d6/d84/classMeasure_1_1Measurement.html#aad95ee25271e89c1fe3618604b5a07af),
[Save()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e),
and
[PartGui::TaskAttacher::TaskAttacher()](../../df/d45/classPartGui_1_1TaskAttacher.html#ae3b7e331323f8a005efc1e55579240a6).

## ◆ getSubListValues()

std::vector< [PropertyLinkSubList::SubSet](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a505e6fb22604ccc4dce91aab5f7c592a) > PropertyLinkSubList::getSubListValues  | ( | [bool](../../d9/db9/classbool.html) | _newStyle_ = `false`| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[PartDesignGui::TaskPipeParameters::accept()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a3547d74f52eaf53d3ccd2f28aac74d06),
[SurfaceGui::FillingPanel::accept()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#a310725e1fbda946f1edfb97d9fd46fbb),
[SurfaceGui::FillingEdgePanel::accept()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a8f8ff8037f61c7d70836740c12cf9e3f),
[SurfaceGui::SectionsPanel::accept()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#a08a26215cfddf89b23a47f3b37f8fbe5),
[SurfaceGui::GeomFillSurface::EdgeSelection::allow()](../../d7/d85/classSurfaceGui_1_1GeomFillSurface_1_1EdgeSelection.html#a9db046f5cffbdc64fc7cf1743c72b592),
[PartDesign::Loft::execute()](../../d0/deb/classPartDesign_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[PartDesign::Pipe::execute()](../../da/d61/classPartDesign_1_1Pipe.html#a860c1038a89156936a4d1fd44481cfbd),
[Surface::Sewing::execute()](../../d2/d52/classSurface_1_1Sewing.html#a956109125cae787085423aeb93d8e1f3),
[getPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a07c5d74e2725f2d1e804d3706d239e2e),
[Surface::GeomFillSurface::getWire()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#acb54e9fd0d6302521906069a06003c6e),
[SurfaceGui::ViewProviderGeomFillSurface::highlightReferences()](../../d8/d03/classSurfaceGui_1_1ViewProviderGeomFillSurface.html#afd24c1bff0f16348ac08835e3514b73e),
[FemGui::ViewProviderFemConstraintOnBoundary::highlightReferences()](../../da/d5f/classFemGui_1_1ViewProviderFemConstraintOnBoundary.html#a1586daa50943e93d852dadff457479f0),
[PartDesignGui::ViewProviderLoft::highlightSection()](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#aef670c0f855e6e36a97aa14355df92bb),
[SurfaceGui::FillingPanel::onSelectionChanged()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#ac8f46981ec84ea0a20faf5791db7cb4b),
[SurfaceGui::FillingEdgePanel::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a13eada025c84a3c28016f3c3974d089d),
[SurfaceGui::FillingVertexPanel::onSelectionChanged()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a67388941ba03ae81ee5e15d8043bbc02),
[SurfaceGui::FillingPanel::open()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#a0a7ed831326e1924933b443e06751a9a),
[SurfaceGui::FillingEdgePanel::open()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a4c12a940ee6c3e013632a7b2efbc97a2),
[SurfaceGui::FillingVertexPanel::open()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#ad233d1ed7e2853c5eee29adb5120d629),
[SurfaceGui::SectionsPanel::open()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#a8517fcc91b9bbe5abaf1f8e64a54df8b),
[SurfaceGui::FillingPanel::reject()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#ab361010fe94b9fee424a62a879eca2ee),
[SurfaceGui::FillingEdgePanel::reject()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#ac70c63defdcfcccfefe1af868074cd44),
[SurfaceGui::FillingVertexPanel::reject()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a11f4fa7ea9554d081b4d63bfdda21a08),
[SurfaceGui::SectionsPanel::reject()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#ae8ce0557e212f783381a1e654e430211),
[SurfaceGui::FillingPanel::slotDeletedObject()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#aff0e8482af6676061ab59d7247826eac),
[SurfaceGui::FillingEdgePanel::slotDeletedObject()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a587afe899d7c039374dc3f9420fb6b36),
[SurfaceGui::FillingVertexPanel::slotDeletedObject()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a9d16f3e5bb245b4c78876b86eb8733f3),
[SurfaceGui::SectionsPanel::slotDeletedObject()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#a9d4aa26a9c4767a97ba15c5a2861bff0),
[PartDesignGui::TaskLoftParameters::TaskLoftParameters()](../../d3/dd7/classPartDesignGui_1_1TaskLoftParameters.html#ab30560915d7d39e4ff4d50b1befc36bf),
and
[PartDesignGui::TaskPipeScaling::TaskPipeScaling()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#abec20e41dadf8a6f7e257d83647df874).

## ◆ getSubValues() [1/2]

std::vector< std::string > PropertyLinkSubList::getSubValues  | ( | [bool](../../d9/db9/classbool.html) | _newStyle_| ) |  const  
---|---|---|---|---|---  
  
## ◆ getSubValues() [2/2]

const std::vector< std::string > & App::PropertyLinkSubList::getSubValues  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[PartDesignGui::TaskDlgDatumParameters::accept()](../../dd/d39/classPartDesignGui_1_1TaskDlgDatumParameters.html#a6058f5550a571d2b4b0cce7208169bba),
[Sketcher::SketchObject::addExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#a700c729d94352b4b144eb083980a702c),
[Measure::Measurement::addReference3D()](../../d6/d84/classMeasure_1_1Measurement.html#a3bcf491038f843ac79c89cdff8925555),
[Measure::Measurement::angle()](../../d6/d84/classMeasure_1_1Measurement.html#a14819c13176bdf930004bef6f290385b),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[TechDraw::DrawViewDimension::checkReferences2D()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a6b3599cd70d672c8aa6e16e304bbb1a4),
[Sketcher::SketchObject::delAllExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#ae20c5b24ce66380931e7da7299dabd6e),
[Sketcher::SketchObject::delExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#a51f4b69d9928669abe729269157d2224),
[Measure::Measurement::delta()](../../d6/d84/classMeasure_1_1Measurement.html#ae7ad27b4e881bd7ad077a64018fed4eb),
[TechDrawGui::TaskLinkDim::dimReferencesSelection()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#ad288819866bf63e2ae639ced390e3338),
[Surface::Sections::execute()](../../d7/d6e/classSurface_1_1Sections.html#a2c9525c3b5343d49da189cd26cd2ad4e),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[Fem::Constraint::getCylinder()](../../d0/d11/classFem_1_1Constraint.html#afd8df029f4c681eea22b6cc20ac0951a),
[PartDesign::ShapeBinder::getFilteredReferences()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a60be3190092c35ac6740f45a4b808dee),
[getLinks()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#afeb6881f95c7f7f897fb2bfd0ee3895b),
[Fem::Constraint::getPoints()](../../d0/d11/classFem_1_1Constraint.html#a422b5404d038352d227033eaf45cf37c),
[TechDraw::DrawViewDimension::getPointsEdgeVert()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#af66b90afc565ab105dff3a850b9ccbc0),
[TechDraw::DrawViewDimension::getPointsOneEdge()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a74fb8170cf274981663bb1989bb972ca),
[TechDraw::DrawViewDimension::getPointsTwoEdges()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f77703f9d3c576d674a7468b231e1ae),
[TechDraw::DrawViewDimension::getPointsTwoVerts()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a3aeea1b6e40d2eba51a724b38db66455),
[TechDraw::DrawViewDimension::getRefType()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a27b3d5169b19453d9df8afe6df2f3e99),
[TechDraw::DrawViewDimExtent::getSubNames()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#a5a3c05bc72ba9515c6f639caa9a1cb94),
[Measure::Measurement::getType()](../../d6/d84/classMeasure_1_1Measurement.html#a2e7bf6dd1301498b0f377660f031c850),
[TechDraw::DrawViewDimension::has2DReferences()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aab80ab22970edd40b48d4bb5632f2f08),
[TechDraw::DrawViewDimension::leaderIntersectsArc()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a8b9b8816642306a8caaf5a22cdd8b629),
[Measure::Measurement::length()](../../d6/d84/classMeasure_1_1Measurement.html#a3f3068c7bbf6c06438658dea6f675c17),
[TechDraw::DrawDimHelper::makeExtentDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#a80cb2086c17599fd498ea2b4401c743c),
[Measure::Measurement::massCenter()](../../d6/d84/classMeasure_1_1Measurement.html#a1c65790f4b19fbcd61b814beaad8f4bc),
[Fem::Constraint::onChanged()](../../d0/d11/classFem_1_1Constraint.html#aec25bc397a1a87056079e3cd5a59d778),
[FemGui::TaskFemConstraint::onReferenceDeleted()](../../df/d80/classFemGui_1_1TaskFemConstraint.html#a77ab2d7a405e8d25d1e0f7592b3731cd),
[FemGui::TaskFemConstraintBearing::onSelectionChanged()](../../d5/d79/classFemGui_1_1TaskFemConstraintBearing.html#ad7d11c8ea8c33f91e89e2821903366d2),
[SurfaceGui::FillingPanel::onSelectionChanged()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#ac8f46981ec84ea0a20faf5791db7cb4b),
[SurfaceGui::FillingEdgePanel::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a13eada025c84a3c28016f3c3974d089d),
[SurfaceGui::FillingVertexPanel::onSelectionChanged()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a67388941ba03ae81ee5e15d8043bbc02),
[SurfaceGui::GeomFillSurface::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#acd70791d15b148166826bac85bc802e9),
[Measure::Measurement::radius()](../../d6/d84/classMeasure_1_1Measurement.html#aad95ee25271e89c1fe3618604b5a07af),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[PartDesignGui::relinkToBody()](../../dc/d12/namespacePartDesignGui.html#a5bd0f34409b95d9ccc03b0b80655b0fd),
[TechDraw::DrawViewDimension::setAll3DMeasurement()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a6ec72b92df3fe7467d4c141e76a5e88a),
[SurfaceGui::FillingPanel::setEditedObject()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#aaaeba016fe808b6dc4d3ddfc9788d380),
[SurfaceGui::FillingEdgePanel::setEditedObject()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#aa23402d795184e9f546a933ef0820357),
[SurfaceGui::FillingVertexPanel::setEditedObject()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a927aea6ee02478a495e928a20a2c3014),
[SurfaceGui::GeomFillSurface::setEditedObject()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#a5347666bfd43a7cbea08d4c179e33f5d),
[SurfaceGui::SectionsPanel::setEditedObject()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#acbe617b52e00f4d86e607c6bc5619d59),
[SketcherGui::SuggestAutoMapMode()](../../d6/d44/namespaceSketcherGui.html#a21c0eeb3a6a37afe433d190fc7a22c18),
[PartGui::TaskAttacher::TaskAttacher()](../../df/d45/classPartGui_1_1TaskAttacher.html#ae3b7e331323f8a005efc1e55579240a6),
[FemGui::TaskFemConstraintBearing::TaskFemConstraintBearing()](../../d5/d79/classFemGui_1_1TaskFemConstraintBearing.html#a5c48324835803c2f89e0c8a226dec9b0),
[FemGui::TaskFemConstraintContact::TaskFemConstraintContact()](../../d6/db7/classFemGui_1_1TaskFemConstraintContact.html#a45a74a3a2db13e3d87edba110a9fd7cd),
[FemGui::TaskFemConstraintDisplacement::TaskFemConstraintDisplacement()](../../d6/d75/classFemGui_1_1TaskFemConstraintDisplacement.html#ad9efd945714cedc7f6f182b3b811e089),
[FemGui::TaskFemConstraintFixed::TaskFemConstraintFixed()](../../df/db3/classFemGui_1_1TaskFemConstraintFixed.html#a7c338f2bd4c3f2e78a6b647ef4e103f7),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[FemGui::TaskFemConstraintForce::TaskFemConstraintForce()](../../d2/d46/classFemGui_1_1TaskFemConstraintForce.html#a3db3abe3cbf9a61635e1683630a55762),
[FemGui::TaskFemConstraintHeatflux::TaskFemConstraintHeatflux()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a8e9e2cb04cc453f24e9d3ea5794cacc1),
[FemGui::TaskFemConstraintInitialTemperature::TaskFemConstraintInitialTemperature()](../../dd/d2a/classFemGui_1_1TaskFemConstraintInitialTemperature.html#a7fdd937b1300d7fc2eefc92ab53ac673),
[FemGui::TaskFemConstraintPlaneRotation::TaskFemConstraintPlaneRotation()](../../db/dc3/classFemGui_1_1TaskFemConstraintPlaneRotation.html#a8381f2d19ed24b3321d83ce4ff4f8257),
[FemGui::TaskFemConstraintPressure::TaskFemConstraintPressure()](../../dc/dd9/classFemGui_1_1TaskFemConstraintPressure.html#a00c65ac2686efb36884dcf8c6a10d76e),
[FemGui::TaskFemConstraintSpring::TaskFemConstraintSpring()](../../d9/d3e/classFemGui_1_1TaskFemConstraintSpring.html#a0237d05805437799169e7d15e6c262fa),
[FemGui::TaskFemConstraintTemperature::TaskFemConstraintTemperature()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a33195abb4e64b5b8c79d39c7423d0a22),
[FemGui::TaskFemConstraintTransform::TaskFemConstraintTransform()](../../d9/d9b/classFemGui_1_1TaskFemConstraintTransform.html#aa2ff547501a5af38276cce0666c1920c),
[App::PropertyXLinkSubList::upgrade()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2),
and
[Sketcher::SketchObject::validateExternalLinks()](../../d9/dad/classSketcher_1_1SketchObject.html#aeb60483adfd2364036d7264a10392ee9).

## ◆ getValue()

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * PropertyLinkSubList::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
getValue emulates the action of a single-object link.

Returns

    reference to object, if the link is to only one object. NULL if the link is empty, or links to subelements of more than one document object. 

Referenced by
[PartDesignGui::TaskShapeBinder::accept()](../../d0/d2a/classPartDesignGui_1_1TaskShapeBinder.html#a5881c04fc2f30c53555576224fab3d45),
[Sketcher::SketchObject::evaluateSupport()](../../d9/dad/classSketcher_1_1SketchObject.html#ae2d3e03c3503536535164dfea9630169),
[TechDraw::DrawViewDimExtent::execute()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#ac856c6f8b2f5504087090cc122d82891),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[PartDesign::ProfileBased::getBaseObject()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a401f7d69c600f553aa66a01f8414ef5b),
[PartDesign::ProfileBased::getSupportFace()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a021db5d3d85698ee0d5a4f8d8a4391a5),
[PartDesign::ProfileBased::positionByPrevious()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#acdddc3b78089a2b2dbd5c567998c9039),
[SketcherGui::SketchSelection::setUp()](../../dc/d2d/structSketcherGui_1_1SketchSelection.html#a984c246a92a7277cf097f37bd61e542c),
and
[Part::AttachExtension::updateAttacherVals()](../../dc/d47/classPart_1_1AttachExtension.html#ab8238095f03465efa5d39c205299c5af).

## ◆ getValues()

const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & App::PropertyLinkSubList::getValues  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[PartDesignGui::TaskDlgDatumParameters::accept()](../../dd/d39/classPartDesignGui_1_1TaskDlgDatumParameters.html#a6058f5550a571d2b4b0cce7208169bba),
[PartDesignGui::TaskDlgLoftParameters::accept()](../../dd/d46/classPartDesignGui_1_1TaskDlgLoftParameters.html#af9021d68a6d00252a3646f95a7408a79),
[PartDesignGui::TaskPipeParameters::accept()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a3547d74f52eaf53d3ccd2f28aac74d06),
[Sketcher::SketchObject::addExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#a700c729d94352b4b144eb083980a702c),
[Measure::Measurement::addReference3D()](../../d6/d84/classMeasure_1_1Measurement.html#a3bcf491038f843ac79c89cdff8925555),
[Measure::Measurement::angle()](../../d6/d84/classMeasure_1_1Measurement.html#a14819c13176bdf930004bef6f290385b),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[TechDraw::DrawViewDimension::checkReferences2D()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a6b3599cd70d672c8aa6e16e304bbb1a4),
[PartDesignGui::ViewProviderLoft::claimChildren()](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#ac368f091664f727043f69262f84d3d3a),
[PartDesignGui::ViewProviderPipe::claimChildren()](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a4c581523b2a518090737db2569d91dfa),
[Sketcher::SketchObject::delAllExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#ae20c5b24ce66380931e7da7299dabd6e),
[Sketcher::SketchObject::delExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#a51f4b69d9928669abe729269157d2224),
[Measure::Measurement::delta()](../../d6/d84/classMeasure_1_1Measurement.html#ae7ad27b4e881bd7ad077a64018fed4eb),
[TechDrawGui::TaskLinkDim::dimReferencesSelection()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#ad288819866bf63e2ae639ced390e3338),
[Surface::Cut::execute()](../../d4/d17/classSurface_1_1Cut.html#adade24c19d386572d09157489463f785),
[Surface::Sections::execute()](../../d7/d6e/classSurface_1_1Sections.html#a2c9525c3b5343d49da189cd26cd2ad4e),
[TechDraw::LandmarkDimension::execute()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a628476bf5d4492109e6d1e947c15aa6d),
[TechDrawGui::QGSPage::findParent()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#aa36872a18b939b5400ece0e09997fd0f),
[TechDraw::LandmarkDimension::get2DPoints()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#acd30a454f2b01db4bd5ec4d7bbb6c5a0),
[Fem::Constraint::getCylinder()](../../d0/d11/classFem_1_1Constraint.html#afd8df029f4c681eea22b6cc20ac0951a),
[PartDesign::ShapeBinder::getFilteredReferences()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a60be3190092c35ac6740f45a4b808dee),
[Fem::Constraint::getPoints()](../../d0/d11/classFem_1_1Constraint.html#a422b5404d038352d227033eaf45cf37c),
[Measure::Measurement::getType()](../../d6/d84/classMeasure_1_1Measurement.html#a2e7bf6dd1301498b0f377660f031c850),
[TechDraw::DrawViewDimension::getViewPart()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a5dd383becefb8e0f57e6598d5d9e1565),
[TechDraw::LandmarkDimension::getViewPart()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#aeffb196bc5419c2d415371cc526c6215),
[TechDraw::DrawViewDimension::has2DReferences()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aab80ab22970edd40b48d4bb5632f2f08),
[TechDraw::LandmarkDimension::has2DReferences()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a2613e741b1ebe8bfe5bb956b9c400447),
[PartDesignGui::ViewProviderPipe::highlightReferences()](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a2e74844f6fab155463ff9eac2900b2ba),
[Measure::Measurement::length()](../../d6/d84/classMeasure_1_1Measurement.html#a3f3068c7bbf6c06438658dea6f675c17),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::loadDefaults()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a891f1e17c68d3e761fb4eb7839772ad7),
[Measure::Measurement::massCenter()](../../d6/d84/classMeasure_1_1Measurement.html#a1c65790f4b19fbcd61b814beaad8f4bc),
[Fem::Constraint::onChanged()](../../d0/d11/classFem_1_1Constraint.html#aec25bc397a1a87056079e3cd5a59d778),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::LandmarkDimension::onDocumentRestored()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a849ea840f2577855fc6365b0481bd8cc),
[FemGui::TaskFemConstraint::onReferenceDeleted()](../../df/d80/classFemGui_1_1TaskFemConstraint.html#a77ab2d7a405e8d25d1e0f7592b3731cd),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::onSaveStyle()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a62078ac8e29f972f667a11bf889acd64),
[FemGui::TaskFemConstraintBearing::onSelectionChanged()](../../d5/d79/classFemGui_1_1TaskFemConstraintBearing.html#ad7d11c8ea8c33f91e89e2821903366d2),
[SurfaceGui::FillingPanel::onSelectionChanged()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#ac8f46981ec84ea0a20faf5791db7cb4b),
[SurfaceGui::FillingEdgePanel::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a13eada025c84a3c28016f3c3974d089d),
[SurfaceGui::FillingVertexPanel::onSelectionChanged()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a67388941ba03ae81ee5e15d8043bbc02),
[SurfaceGui::GeomFillSurface::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#acd70791d15b148166826bac85bc802e9),
[Measure::Measurement::radius()](../../d6/d84/classMeasure_1_1Measurement.html#aad95ee25271e89c1fe3618604b5a07af),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[PartDesignGui::TaskPipeParameters::referenceSelected()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a0c0361901e8218cb0848f5c13d58bb3d),
[PartDesignGui::TaskPipeScaling::referenceSelected()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#ac9f1c0754a7abf2a4e59c0218c73829a),
[PartDesignGui::relinkToBody()](../../dc/d12/namespacePartDesignGui.html#a5bd0f34409b95d9ccc03b0b80655b0fd),
[TechDraw::DrawViewDimension::setAll3DMeasurement()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a6ec72b92df3fe7467d4c141e76a5e88a),
[SurfaceGui::FillingPanel::setEditedObject()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#aaaeba016fe808b6dc4d3ddfc9788d380),
[SurfaceGui::FillingEdgePanel::setEditedObject()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#aa23402d795184e9f546a933ef0820357),
[SurfaceGui::FillingVertexPanel::setEditedObject()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a927aea6ee02478a495e928a20a2c3014),
[SurfaceGui::GeomFillSurface::setEditedObject()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#a5347666bfd43a7cbea08d4c179e33f5d),
[SurfaceGui::SectionsPanel::setEditedObject()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#acbe617b52e00f4d86e607c6bc5619d59),
[FemGui::TaskFemConstraintBearing::TaskFemConstraintBearing()](../../d5/d79/classFemGui_1_1TaskFemConstraintBearing.html#a5c48324835803c2f89e0c8a226dec9b0),
[FemGui::TaskFemConstraintContact::TaskFemConstraintContact()](../../d6/db7/classFemGui_1_1TaskFemConstraintContact.html#a45a74a3a2db13e3d87edba110a9fd7cd),
[FemGui::TaskFemConstraintDisplacement::TaskFemConstraintDisplacement()](../../d6/d75/classFemGui_1_1TaskFemConstraintDisplacement.html#ad9efd945714cedc7f6f182b3b811e089),
[FemGui::TaskFemConstraintFixed::TaskFemConstraintFixed()](../../df/db3/classFemGui_1_1TaskFemConstraintFixed.html#a7c338f2bd4c3f2e78a6b647ef4e103f7),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[FemGui::TaskFemConstraintForce::TaskFemConstraintForce()](../../d2/d46/classFemGui_1_1TaskFemConstraintForce.html#a3db3abe3cbf9a61635e1683630a55762),
[FemGui::TaskFemConstraintHeatflux::TaskFemConstraintHeatflux()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a8e9e2cb04cc453f24e9d3ea5794cacc1),
[FemGui::TaskFemConstraintInitialTemperature::TaskFemConstraintInitialTemperature()](../../dd/d2a/classFemGui_1_1TaskFemConstraintInitialTemperature.html#a7fdd937b1300d7fc2eefc92ab53ac673),
[FemGui::TaskFemConstraintPlaneRotation::TaskFemConstraintPlaneRotation()](../../db/dc3/classFemGui_1_1TaskFemConstraintPlaneRotation.html#a8381f2d19ed24b3321d83ce4ff4f8257),
[FemGui::TaskFemConstraintPressure::TaskFemConstraintPressure()](../../dc/dd9/classFemGui_1_1TaskFemConstraintPressure.html#a00c65ac2686efb36884dcf8c6a10d76e),
[FemGui::TaskFemConstraintSpring::TaskFemConstraintSpring()](../../d9/d3e/classFemGui_1_1TaskFemConstraintSpring.html#a0237d05805437799169e7d15e6c262fa),
[FemGui::TaskFemConstraintTemperature::TaskFemConstraintTemperature()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a33195abb4e64b5b8c79d39c7423d0a22),
[FemGui::TaskFemConstraintTransform::TaskFemConstraintTransform()](../../d9/d9b/classFemGui_1_1TaskFemConstraintTransform.html#aa2ff547501a5af38276cce0666c1920c),
[Part::Part2DObject::transformPlacement()](../../d9/d57/classPart_1_1Part2DObject.html#ac943e32302f22b54d748ce9b04ecbdfe),
[App::PropertyXLinkSubList::upgrade()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2),
[Sketcher::SketchObject::validateExternalLinks()](../../d9/dad/classSketcher_1_1SketchObject.html#aeb60483adfd2364036d7264a10392ee9),
and
[Attacher::AttachEngine::verifyReferencesAreSafe()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac8843a2175ebae4cc4d23f006d61abe1).

## ◆ onContainerRestored()

| void PropertyLinkSubList::onContainerRestored  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
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

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a724e44690754d6abaff38d3131420225).

References
[App::PropertyLinkBase::unregisterElementReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aa5ec8a97f53a0928274e9d585a50fd29).

## ◆ Paste()

| void PropertyLinkSubList::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be).

References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
and
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7).

Referenced by
[Attacher::AttachEngine::setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8).

## ◆ referenceChanged()

| [bool](../../d9/db9/classbool.html) PropertyLinkSubList::referenceChanged  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Test if the element reference has changed after restore.

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af56b87f577368963c8aeec5a5fc74ee0).

## ◆ removeValue()

[int](../../d1/da0/classint.html) PropertyLinkSubList::removeValue  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _lValue_| ) |   
---|---|---|---|---|---  
  
Removes all occurrences of _lValue_ in the property together with its sub-
elements and returns the number of entries removed.

References
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7).

Referenced by
[PartDesignGui::TaskPipeScaling::referenceSelected()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#ac9f1c0754a7abf2a4e59c0218c73829a).

## ◆ Restore()

| void PropertyLinkSubList::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e
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
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[Base::XMLReader::getName()](../../dc/d95/classBase_1_1XMLReader.html#aa529233af401d7719226293c506792f8),
[App::Document::getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[App::PropertyLinkBase::importSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e),
[Base::XMLReader::isVerbose()](../../dc/d95/classBase_1_1XMLReader.html#a89fa30d380593281c1e22864653a8b0a),
[App::PropertyLinkBase::LinkRestoreLabel](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fa5a4bc69cb609a1f93370ec11e29dc403),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[Base::XMLReader::readEndElement()](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3),
[App::PropertyLinkBase::setFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f),
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7),
and
[Base::ConsoleSingleton::Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

Referenced by
[PartDesign::ShapeBinder::handleChangedPropertyType()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#ae4e96cdb35155567c8bbc77cb4dd3fd3),
and
[App::PropertyXLinkSubList::upgrade()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2).

## ◆ Save()

| void PropertyLinkSubList::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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
[Base::Writer::decInd()](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92),
[Base::Persistence::encodeAttribute()](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec),
[App::PropertyLinkBase::exportSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a08eab53abe5c11c895d4ecea426485ad),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[getSize()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aed336221f52dede47a507aed1f382dd7),
[Base::Writer::incInd()](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5),
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ setPyObject()

| void PropertyLinkSubList::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

References
[App::PropertyLinkSub::getSubValues()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a0777851ecd0b74f3fd232e6c69c7cb32),
[App::PropertyLinkSub::getValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#af444cc21b2476f99a94fa2e982c4ae86),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
[App::PropertyString::setPyObject()](../../dd/df8/classApp_1_1PropertyString.html#ac9b0f60fd6949cfd514653838e78840b),
[App::PropertyLinkSub::setPyObject()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9965507bfcc6e28d251ffb62f234df77),
[App::PropertyListsT< T, ListT, ParentT
>::setPyObject()](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
[setValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f),
and
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7).

## ◆ setSize()

void PropertyLinkSubList::setSize  | ( | [int](../../d1/da0/classint.html) | _newSize_| ) |   
---|---|---|---|---|---  
  
## ◆ setSubListValues()

void PropertyLinkSubList::setSubListValues  | ( | const std::vector< [SubSet](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a505e6fb22604ccc4dce91aab5f7c592a) > & | _values_| ) |   
---|---|---|---|---|---  
  
References
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7).

Referenced by
[PartDesignGui::TaskPipeParameters::accept()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a3547d74f52eaf53d3ccd2f28aac74d06).

## ◆ setSyncSubObject()

void PropertyLinkSubList::setSyncSubObject  | ( | [bool](../../d9/db9/classbool.html) | _enable_| ) |   
---|---|---|---|---|---  
  
References
[App::PropertyLinkBase::LinkSyncSubObject](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fab29bedf78f3fa832237ffa3a544e88c8).

## ◆ setValue() [1/2]

void PropertyLinkSubList::setValue  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _lValue_ ,   
---|---|---|---  
|  | const std::vector< std::string > & | _SubList_ = `std::vector<std::string>()`  
| ) | |   
  
setValue: PropertyLinkSub-compatible overload

Parameters

     SubList|   
---|---  
  
References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::PropertyLinkBase::checkLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[App::DocumentObject::testStatus()](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120),
and
[updateElementReference()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca).

## ◆ setValue() [2/2]

void PropertyLinkSubList::setValue  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _lValue_ ,   
---|---|---|---  
|  | const char *  | _SubName_  
| ) | |   
  
Sets the property.

setValue(0, whatever) clears the property

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::PropertyLinkBase::checkLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[App::DocumentObject::testStatus()](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120),
and
[updateElementReference()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca).

Referenced by
[TechDraw::LandmarkDimension::execute()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a628476bf5d4492109e6d1e947c15aa6d),
[Attacher::AttachEngine::getShapeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac859e617fee1a4f39a2f9186c36f0bb8),
[PartDesignGui::TaskFeaturePick::makeCopy()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a9e9b1a639025522ada407aaa6b19596e),
[TechDraw::DrawDimHelper::makeExtentDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#a80cb2086c17599fd498ea2b4401c743c),
[setPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a495ec38be0d7ceb20aa9b3d5a520fdfa),
[TechDrawGui::TaskLinkDim::updateDims()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#acff44dd09f905319bf7234cd9c0afd2e),
and
[upgrade()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b).

## ◆ setValues() [1/3]

void PropertyLinkSubList::setValues  | ( | const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _lValue_ ,   
---|---|---|---  
|  | const std::vector< const char * > & | _lSubNames_  
| ) | |   
  
References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::PropertyLinkBase::checkLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[App::DocumentObject::testStatus()](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120),
and
[updateElementReference()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca).

Referenced by
[PartDesignGui::TaskDlgDatumParameters::accept()](../../dd/d39/classPartDesignGui_1_1TaskDlgDatumParameters.html#a6058f5550a571d2b4b0cce7208169bba),
[Sketcher::SketchObject::addExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#a700c729d94352b4b144eb083980a702c),
[Measure::Measurement::addReference3D()](../../d6/d84/classMeasure_1_1Measurement.html#a3bcf491038f843ac79c89cdff8925555),
[adjustLink()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab5bc8a3cb854f5b7643bfdcc4d0cb525),
[breakLink()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#af3659c9cd764ba67a9b4eb61ac10d328),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[Measure::Measurement::clear()](../../d6/d84/classMeasure_1_1Measurement.html#a8ed5fe7b184512cd11d0dbd67a7500d4),
[Sketcher::SketchObject::delAllExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#ae20c5b24ce66380931e7da7299dabd6e),
[Sketcher::SketchObject::delExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#a51f4b69d9928669abe729269157d2224),
[Gui::SelectionSingleton::getAsPropertyLinkSubList()](../../d4/dca/classGui_1_1SelectionSingleton.html#afb9f02208306ba2a93ac45d0b9572a90),
[TechDraw::DrawDimHelper::makeDistDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#abbb31fd885c91f55267b7f8fd3945c1a),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::onLoadStyle()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a1ba62c7eca1bc9f408549242e3def48b),
[FemGui::TaskFemConstraint::onReferenceDeleted()](../../df/d80/classFemGui_1_1TaskFemConstraint.html#a77ab2d7a405e8d25d1e0f7592b3731cd),
[FemGui::TaskFemConstraintBearing::onSelectionChanged()](../../d5/d79/classFemGui_1_1TaskFemConstraintBearing.html#ad7d11c8ea8c33f91e89e2821903366d2),
[SurfaceGui::FillingPanel::onSelectionChanged()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#ac8f46981ec84ea0a20faf5791db7cb4b),
[SurfaceGui::FillingEdgePanel::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a13eada025c84a3c28016f3c3974d089d),
[SurfaceGui::FillingVertexPanel::onSelectionChanged()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a67388941ba03ae81ee5e15d8043bbc02),
[SurfaceGui::GeomFillSurface::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#acd70791d15b148166826bac85bc802e9),
[Paste()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a3dfbcd135189c2b3e6e7c6136ed572a1),
[removeValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a6e6084e9fe235dbf474585762125e351),
[Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[setPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a495ec38be0d7ceb20aa9b3d5a520fdfa),
[setSubListValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a4e3800926a177586d370a9a8529ec46f),
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a80bd9cad2a6b8ee3f81125eba1c82e06),
[TechDrawGui::TaskLinkDim::updateDims()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#acff44dd09f905319bf7234cd9c0afd2e),
[upgrade()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b),
and
[Sketcher::SketchObject::validateExternalLinks()](../../d9/dad/classSketcher_1_1SketchObject.html#aeb60483adfd2364036d7264a10392ee9).

## ◆ setValues() [2/3]

void PropertyLinkSubList::setValues  | ( | const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _lValue_ ,   
---|---|---|---  
|  | const std::vector< std::string > & | _lSubNames_ ,   
|  | std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > && | _ShadowSubList_ = `{}`  
| ) | |   
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7).

Referenced by
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::onLoadStyle()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a1ba62c7eca1bc9f408549242e3def48b).

## ◆ setValues() [3/3]

void PropertyLinkSubList::setValues  | ( | std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > && | _lValue_ ,   
---|---|---|---  
|  | std::vector< std::string > && | _subs_ ,   
|  | std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > && | _ShadowSubList_ = `{}`  
| ) | |   
  
References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::PropertyLinkBase::checkLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[App::DocumentObject::testStatus()](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120),
and
[updateElementReference()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a964cd44e91d84fc9e14671a756eb76ca).

Referenced by
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::onLoadStyle()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a1ba62c7eca1bc9f408549242e3def48b).

## ◆ updateElementReference()

| void PropertyLinkSubList::updateElementReference  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _feature_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _reverse_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _notify_ = `false`  
| ) | |   
overridevirtual  
  
[Link](../../df/d9b/classApp_1_1Link.html) type property interface APIs These
APIs are moved here so that any type of property can have the property link
behavior, e.g.

the
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
Called to update the element reference of this link property

See also

    _updateElementReference() 

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6447c82dc0b81cea703a9a235a2448c3).

References
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[femsolver.signal::notify()](../../dc/de2/group__FEM.html#ga6389100f2d948a9fe194b395ac11f82c),
and
[App::PropertyLinkBase::unregisterElementReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aa5ec8a97f53a0928274e9d585a50fd29).

Referenced by
[addValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17cad50fa5ecc14fafcfc99e3cba7bbd),
[setValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f),
and
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7).

## ◆ upgrade()

[bool](../../d9/db9/classbool.html) PropertyLinkSubList::upgrade  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_ ,   
---|---|---|---  
|  | const char *  | _typeName_  
| ) | |   
  
References
[Base::Type::fromName()](../../dc/dee/classBase_1_1Type.html#a7fd6fce9272b7886af7a58d2af987c42),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::PropertyListsT< T, ListT, ParentT
>::getSize()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyLinkSub::getSubValues()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a0777851ecd0b74f3fd232e6c69c7cb32),
[App::PropertyLink::getValue()](../../d4/d77/classApp_1_1PropertyLink.html#a1977d393d8e53d0e3d712c78ac851869),
[App::PropertyLinkSub::getValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#af444cc21b2476f99a94fa2e982c4ae86),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::Property::setContainer()](../../d0/da9/classApp_1_1Property.html#aa03e6562bf3996db1700b0e636425257),
[setValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f),
and
[setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7).

Referenced by
[PartDesign::Loft::handleChangedPropertyType()](../../d0/deb/classPartDesign_1_1Loft.html#ad4ac633608d2e7a2ca80e98958160339),
and
[PartDesign::Pipe::handleChangedPropertyType()](../../da/d61/classPartDesign_1_1Pipe.html#a21ddc40aa9d476ee1455154c2e09f7ab).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyLinks.h
  * FreeCAD/src/App/PropertyLinks.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

