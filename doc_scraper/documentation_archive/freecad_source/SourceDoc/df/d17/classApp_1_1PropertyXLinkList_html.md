---
url: https://freecad.github.io/SourceDoc/df/d17/classApp_1_1PropertyXLinkList.html
scraped_at: 2025-09-08T14:56:54.128920
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyXLinkList](../../df/d17/classApp_1_1PropertyXLinkList.html)

[List of all members](../../d0/d7d/classApp_1_1PropertyXLinkList-members.html) | Public Member Functions

App::PropertyXLinkList Class Reference

[Link](../../df/d9b/classApp_1_1Link.html) to one or more
(sub)[object(s)](../../dc/dd8/classobject.html) of one or more
[object(s)](../../dc/dd8/classobject.html) from the same or different
document. [More...](../../df/d17/classApp_1_1PropertyXLinkList.html#details)

`#include <PropertyLinks.h>`

##  Public Member Functions  
  
---  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../df/d17/classApp_1_1PropertyXLinkList.html#a91d0fb67e3e4623edf333125710ff985) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../df/d17/classApp_1_1PropertyXLinkList.html#a91d0fb67e3e4623edf333125710ff985)  
  
|
[PropertyXLinkList](../../df/d17/classApp_1_1PropertyXLinkList.html#aaf1f30a3d4098783c53261f6432cdaf8)
()  
virtual void | [setPyObject](../../df/d17/classApp_1_1PropertyXLinkList.html#a2f618a6e3542cb338064a4d268277290) ([PyObject](../../df/d1b/classPyObject.html) *) override  
virtual | [~PropertyXLinkList](../../df/d17/classApp_1_1PropertyXLinkList.html#a39bf97457c8ed73d9eaad8e62d2900cd) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html)  
virtual void | [aboutToSetChildValue](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a9ac18b822a3fad41bc1d69342db5cf44) ([Property](../../d0/da9/classApp_1_1Property.html) &) override  
| Called before a child property changing value.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a9ac18b822a3fad41bc1d69342db5cf44)  
  
void | [addValue](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a6b7dec7e9284698fd08b62daba38f267) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::vector< std::string > &SubList={}, [bool](../../d9/db9/classbool.html) reset=false)  
void | [addValue](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a91e5e534b886db50520e0b006556b76a) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, std::vector< std::string > &&SubList={}, [bool](../../d9/db9/classbool.html) reset=false)  
virtual [bool](../../d9/db9/classbool.html) | [adjustLink](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a2fbece18bdf273d6c6d427c6cce98da7) (const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList) override  
| Called to adjust the link to avoid potential cyclic dependency.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a2fbece18bdf273d6c6d427c6cce98da7)  
  
virtual void | [afterRestore](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a3a9916bc1df1cc05d0362053e9ded4b1) () override  
| Called at the beginning of
[Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5)
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a3a9916bc1df1cc05d0362053e9ded4b1)  
  
virtual void | [breakLink](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad8d3af63e632d9e26194e66ed0eaaa68) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) clear) override  
| Called to reset this link property.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad8d3af63e632d9e26194e66ed0eaaa68)  
  
virtual [int](../../d1/da0/classint.html) | [checkRestore](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a99d92e5122a717c23ebe1834086da5e6) (std::string *msg=nullptr) const override  
| Test if the link is restored unchanged.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a99d92e5122a717c23ebe1834086da5e6)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad3ce8f501efd0cdd27a89018b7fe7672) (void) const override  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad3ce8f501efd0cdd27a89018b7fe7672)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnImportExternal](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a583fcb98efbbb8211cfdd20437688de1) (const std::map< std::string, std::string > &nameMap) const override  
| Return a copy of the property if any changes caused by importing external
linked object.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a583fcb98efbbb8211cfdd20437688de1)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLabelChange](../../db/de6/classApp_1_1PropertyXLinkSubList.html#af9fed844cfcceb8be5f643a0146f7c25) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &ref, const char *newLabel) const override  
| Update object label reference in this property.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#af9fed844cfcceb8be5f643a0146f7c25)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLinkReplace](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4aeacb995d8cd9f1ddd3309d87703960) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj) const override  
| Return a copy of the property if the link replacement affects this property.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4aeacb995d8cd9f1ddd3309d87703960)  
  
virtual const char * | [getEditorName](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a5d7a3cac74d30de8e1a220abf8fb8b7f) (void) const override  
| Get the class name of the associated property editor item.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a5d7a3cac74d30de8e1a220abf8fb8b7f)  
  
virtual void | [getLinks](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a474c20d3ad36ebec314c141803e0ca3b) (std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [bool](../../d9/db9/classbool.html) all=false, std::vector< std::string > *subs=nullptr, [bool](../../d9/db9/classbool.html) newStyle=true) const override  
| Obtain the linked objects.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a474c20d3ad36ebec314c141803e0ca3b)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a19431f105396ee0ea39fb438e0f72fef) (void) const override  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a19431f105396ee0ea39fb438e0f72fef)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../db/de6/classApp_1_1PropertyXLinkSubList.html#aa9ee16bcedb194655b91e5d93730bf22) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#aa9ee16bcedb194655b91e5d93730bf22)  
  
const std::string | [getPyReprString](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a49dc28e937c8ffb0a0739ee83deaeb0a) () const  
const std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > & | [getShadowSubs](../../db/de6/classApp_1_1PropertyXLinkSubList.html#af2ed55fa424587f4b9a0672c491916e3) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj) const  
[int](../../d1/da0/classint.html) | [getSize](../../db/de6/classApp_1_1PropertyXLinkSubList.html#abecbcd6edeca7e713074af9d848a1ec7) (void) const  
const std::list< [PropertyXLinkSub](../../d4/da0/classApp_1_1PropertyXLinkSub.html) > & | [getSubListValues](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a0c41c01c6d36b237ab0d5b7989538a94) () const  
const std::vector< std::string > & | [getSubValues](../../db/de6/classApp_1_1PropertyXLinkSubList.html#af88b167b8a553075a661242a1176a955) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj) const  
std::vector< std::string > | [getSubValues](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad0a97d0ba8810e5b17f637def2661363) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) newStyle) const  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getValue](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a2522ad7f58a842decff226eaf2ab1dc0) () const  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getValues](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a5773d0caaaf0663739702bc96d63404a) (void) const  
virtual void | [hasSetChildValue](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a8d97a9deb398fd86589410728dc222bf) ([Property](../../d0/da9/classApp_1_1Property.html) &) override  
| Called when a child property has changed value.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a8d97a9deb398fd86589410728dc222bf)  
  
virtual void | [onContainerRestored](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ae5784f7e4394d2d7be363cca3abaf2d4) () override  
| Called before calling
[DocumentObject::onDocumentRestored()](../../d2/de4/classApp_1_1DocumentObject.html#a0ee8399fa0b176c64895150691a4b604
"get called after a document has been fully restored")
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ae5784f7e4394d2d7be363cca3abaf2d4)  
  
virtual void | [Paste](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4ac663947ed88fa49f3a874273098fe4) (const [Property](../../d0/da9/classApp_1_1Property.html) &from) override  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4ac663947ed88fa49f3a874273098fe4)  
  
|
[PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#acd588eab820577f9b98bef530b8f4aea)
()  
virtual [bool](../../d9/db9/classbool.html) | [referenceChanged](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a00709d08884ac1fa1952b0836d822a2b) () const override  
| Test if the element reference has changed after restore.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a00709d08884ac1fa1952b0836d822a2b)  
  
[int](../../d1/da0/classint.html) | [removeValue](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a8d5f65ef531c3e77be92d92ed82d6a13) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *lValue)  
| Removes all occurrences of _lValue_ in the property together with its sub-
elements and returns the number of entries removed.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a8d5f65ef531c3e77be92d92ed82d6a13)  
  
virtual void | [Restore](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a1a047c1c95612cfc2e4ca4a91491d995) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a1a047c1c95612cfc2e4ca4a91491d995)  
  
virtual void | [Save](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a456f78573d34d76300c400382a36960d) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a456f78573d34d76300c400382a36960d)  
  
void | [set1Value](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a0760be6f2e7246ec19c223f163cbe17d) ([int](../../d1/da0/classint.html) idx, [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *value, const std::vector< std::string > &SubList={})  
virtual void | [setAllowPartial](../../db/de6/classApp_1_1PropertyXLinkSubList.html#af1e65ab203efb67b27a0a5ed306d2c66) ([bool](../../d9/db9/classbool.html) enable) override  
virtual void | [setPyObject](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a7160ec1120efe0609b40286324fc861f) ([PyObject](../../df/d1b/classPyObject.html) *) override  
void | [setSubListValues](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a41195d6938e517464945473cc5074134) (const std::vector< [PropertyLinkSubList::SubSet](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a505e6fb22604ccc4dce91aab5f7c592a) > &)  
void | [setSyncSubObject](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4934dfe5f9f434c49cc424b673084306) ([bool](../../d9/db9/classbool.html) enable)  
void | [setValue](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a378366e23d693d5c97f1d2782dd3be11) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *lValue, const std::vector< std::string > &SubList={})  
| setValue: PropertyLinkSub-compatible overload
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a378366e23d693d5c97f1d2782dd3be11)  
  
void | [setValue](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a3800e6c7a9eeb19855cfd1fe3febafa1) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, const char *)  
| Sets the property.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a3800e6c7a9eeb19855cfd1fe3febafa1)  
  
void | [setValues](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad66133b3aa9deca7007ded162b52cf44) (const std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > &)  
void | [setValues](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a46bfe829735552a759b7a318914cc71d) (const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &)  
void | [setValues](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a82210325a201b5eff6a3107024a698cb) (const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, const std::vector< const char * > &)  
void | [setValues](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a88e8efa9c41dbee50dada33db2318597) (const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, const std::vector< std::string > &)  
void | [setValues](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a47d377efbb84d5b9671d95726132302a) (std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > &&)  
virtual void | [updateElementReference](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad139ceb8061df8903e132dd84e2b050c) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *feature, [bool](../../d9/db9/classbool.html) reverse=false, [bool](../../d9/db9/classbool.html) notify=false) override  
| [Link](../../df/d9b/classApp_1_1Link.html) type property interface APIs
These APIs are moved here so that any type of property can have the property
link behavior, e.g.
[More...](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ad139ceb8061df8903e132dd84e2b050c)  
  
[bool](../../d9/db9/classbool.html) | [upgrade](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *typeName)  
virtual | [~PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#ae52ecdb4576a72329a6f8c70ff367978) ()  
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
  
![-](../../closed.png) Protected Member Functions inherited from
[App::AtomicPropertyChangeInterface< PropertyXLinkSubList
>](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)  
|
[AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#aab004d1fbf131c11d570dcfcad7c22e1)
()  
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
[App::AtomicPropertyChangeInterface< PropertyXLinkSubList
>](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)  
[bool](../../d9/db9/classbool.html) | [hasChanged](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a1e6d78782f81aef5d1efe58ac219e2df)  
[int](../../d1/da0/classint.html) | [signalCounter](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a07e13a81f4f601365b04cc8806d075f9)  
| Counter for invoking transaction start/stop.
[More...](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a07e13a81f4f601365b04cc8806d075f9)  
  
  
## Detailed Description

[Link](../../df/d9b/classApp_1_1Link.html) to one or more
(sub)[object(s)](../../dc/dd8/classobject.html) of one or more
[object(s)](../../dc/dd8/classobject.html) from the same or different
document.

The only difference for
[PropertyXLinkList](../../df/d17/classApp_1_1PropertyXLinkList.html "Link to
one or more \(sub\)object\(s\) of one or more object\(s\) from the same or
different document.") and
[PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html
"Link to one or more \(sub\)object\(s\) of one or more object\(s\) from the
same or different document.") is in their
[getPyObject()](../../df/d17/classApp_1_1PropertyXLinkList.html#a91d0fb67e3e4623edf333125710ff985
"This method returns the Python wrapper for a C++ object.").
[PropertyXLinkList](../../df/d17/classApp_1_1PropertyXLinkList.html "Link to
one or more \(sub\)object\(s\) of one or more object\(s\) from the same or
different document.") will return a list of object is there is no sub-
object/sub-elements in the property.

## Constructor & Destructor Documentation

## ◆ PropertyXLinkList()

PropertyXLinkList::PropertyXLinkList  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~PropertyXLinkList()

| PropertyXLinkList::~PropertyXLinkList  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyXLinkList::getPyObject  | ( | void  | | ) |   
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
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#aa9ee16bcedb194655b91e5d93730bf22).

References
[App::PropertyXLinkSubList::getPyObject()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#aa9ee16bcedb194655b91e5d93730bf22).

## ◆ setPyObject()

| void PropertyXLinkList::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a7160ec1120efe0609b40286324fc861f).

References [App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
[App::PropertyLinkBase::setAllowExternal()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6a771360ff664dd0f0b740ef566f4254),
[App::PropertyXLinkSubList::setPyObject()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a7160ec1120efe0609b40286324fc861f),
[App::PropertyListsT< T, ListT, ParentT
>::setPyObject()](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
and
[App::PropertyXLinkSubList::setValues()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a46bfe829735552a759b7a318914cc71d).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyLinks.h
  * FreeCAD/src/App/PropertyLinks.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

