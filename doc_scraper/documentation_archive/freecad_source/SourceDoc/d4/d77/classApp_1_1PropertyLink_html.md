---
url: https://freecad.github.io/SourceDoc/d4/d77/classApp_1_1PropertyLink.html
scraped_at: 2025-09-08T14:56:01.922111
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html)

[List of all members](../../d7/db4/classApp_1_1PropertyLink-members.html) | Public Member Functions

App::PropertyLink Class Reference

The general [Link](../../df/d9b/classApp_1_1Link.html)
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") Main Purpose of this
property is to [Link](../../df/d9b/classApp_1_1Link.html) Objects and Features
in a document. [More...](../../d4/d77/classApp_1_1PropertyLink.html#details)

`#include <PropertyLinks.h>`

##  Public Member Functions  
  
---  
virtual [bool](../../d9/db9/classbool.html) | [adjustLink](../../d4/d77/classApp_1_1PropertyLink.html#aebfbbd1933b83fa53b46133da128c17a) (const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList) override  
| Called to adjust the link to avoid potential cyclic dependency.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#aebfbbd1933b83fa53b46133da128c17a)  
  
virtual void | [breakLink](../../d4/d77/classApp_1_1PropertyLink.html#a5ba319a4ccf1773412d1d5023482ceda) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) clear) override  
| Called to reset this link property.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a5ba319a4ccf1773412d1d5023482ceda)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d4/d77/classApp_1_1PropertyLink.html#a11d683872f0c6070dbef87552842d762) (void) const override  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a11d683872f0c6070dbef87552842d762)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLinkReplace](../../d4/d77/classApp_1_1PropertyLink.html#ae33affee6371a40629ea84b1782c2cb5) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj) const override  
| Return a copy of the property if the link replacement affects this property.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#ae33affee6371a40629ea84b1782c2cb5)  
  
virtual const char * | [getEditorName](../../d4/d77/classApp_1_1PropertyLink.html#a1bd98f29491b7e75ac5f9e2a8a3063a4) (void) const override  
| Get the class name of the associated property editor item.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a1bd98f29491b7e75ac5f9e2a8a3063a4)  
  
virtual void | [getLinks](../../d4/d77/classApp_1_1PropertyLink.html#a4750ce6a3916cee3e9746a683bbf4330) (std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [bool](../../d9/db9/classbool.html) all=false, std::vector< std::string > *subs=nullptr, [bool](../../d9/db9/classbool.html) newStyle=true) const override  
| Obtain the linked objects.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a4750ce6a3916cee3e9746a683bbf4330)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d4/d77/classApp_1_1PropertyLink.html#a7467d6db2f6e7842e417ecc0d0f85bb7) (void) const override  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a7467d6db2f6e7842e417ecc0d0f85bb7)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d4/d77/classApp_1_1PropertyLink.html#accebd677bd5e10d5f9b576e2d0d72bf6) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#accebd677bd5e10d5f9b576e2d0d72bf6)  
  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getValue](../../d4/d77/classApp_1_1PropertyLink.html#ad60389b7b386213e260bff14287ec6b7) ([Base::Type](../../dc/dee/classBase_1_1Type.html) t) const  
| Returns the link type checked.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#ad60389b7b386213e260bff14287ec6b7)  
  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getValue](../../d4/d77/classApp_1_1PropertyLink.html#a1977d393d8e53d0e3d712c78ac851869) (void) const  
| This method returns the linked
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.").
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a1977d393d8e53d0e3d712c78ac851869)  
  
template<typename _type >  
_type | [getValue](../../d4/d77/classApp_1_1PropertyLink.html#a155037bf8a55646007f8ccece2b0bcd6) (void) const  
| Returns the link type checked.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a155037bf8a55646007f8ccece2b0bcd6)  
  
virtual void | [Paste](../../d4/d77/classApp_1_1PropertyLink.html#a31b305bd16358bc6459e33bf47e1c2b6) (const [Property](../../d0/da9/classApp_1_1Property.html) &from) override  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a31b305bd16358bc6459e33bf47e1c2b6)  
  
|
[PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a797df0fe915ebf8aa1f7ae2cfc8260d2)
()  
| A constructor.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a797df0fe915ebf8aa1f7ae2cfc8260d2)  
  
void | [resetLink](../../d4/d77/classApp_1_1PropertyLink.html#a0461c85fa8e082a75df6e848f94d8c39) ()  
virtual void | [Restore](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4)  
  
virtual void | [Save](../../d4/d77/classApp_1_1PropertyLink.html#a89ed9d7172c31abd43b9ce7e99424ed8) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a89ed9d7172c31abd43b9ce7e99424ed8)  
  
virtual void | [setPyObject](../../d4/d77/classApp_1_1PropertyLink.html#a8df27dbc0e724558a372f813a7eda649) ([PyObject](../../df/d1b/classPyObject.html) *) override  
virtual void | [setValue](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
| Sets the property.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1)  
  
virtual | [~PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#adb6e576152567b3139b32b6beacf1dfd) ()  
| A destructor.
[More...](../../d4/d77/classApp_1_1PropertyLink.html#adb6e576152567b3139b32b6beacf1dfd)  
  
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

The general [Link](../../df/d9b/classApp_1_1Link.html)
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") Main Purpose of this
property is to [Link](../../df/d9b/classApp_1_1Link.html) Objects and Features
in a document.

Like all links this property is scope aware, meaning it does define which
objects are allowed to be linked depending of the GeoFeatureGroup where it is
in. Default is Local.

Note

    Links that are invalid in respect to the scope of this property is set to are not rejected. They are only detected to be invalid and prevent the feature from recomputing. 

## Constructor & Destructor Documentation

## ◆ PropertyLink()

PropertyLink::PropertyLink  | ( | | ) |   
---|---|---|---|---  
  
A constructor.

A more elaborate description of the constructor.

Referenced by
[Copy()](../../d4/d77/classApp_1_1PropertyLink.html#a11d683872f0c6070dbef87552842d762),
and
[CopyOnLinkReplace()](../../d4/d77/classApp_1_1PropertyLink.html#ae33affee6371a40629ea84b1782c2cb5).

## ◆ ~PropertyLink()

| PropertyLink::~PropertyLink  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

References
[resetLink()](../../d4/d77/classApp_1_1PropertyLink.html#a0461c85fa8e082a75df6e848f94d8c39).

## Member Function Documentation

## ◆ adjustLink()

| [bool](../../d9/db9/classbool.html) PropertyLink::adjustLink  | ( | const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _inList_| ) |   
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

Reimplemented in
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a33bbd1956612a56e1967fdd7d6c533ff).

## ◆ breakLink()

| void PropertyLink::breakLink  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
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
[setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1).

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyLink::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

Reimplemented in
[App::PropertyPlacementLink](../../d8/db5/classApp_1_1PropertyPlacementLink.html#a79a279154ca0a57b537a595f7ead7d9b),
and
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a6e7ddbe8a1061c36145bd0180b47c7f1).

References
[PropertyLink()](../../d4/d77/classApp_1_1PropertyLink.html#a797df0fe915ebf8aa1f7ae2cfc8260d2).

## ◆ CopyOnLinkReplace()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyLink::CopyOnLinkReplace  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
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

Reimplemented in
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#aa713c66bf6fd8a5a03ec1f94b233e8bb).

References
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[PropertyLink()](../../d4/d77/classApp_1_1PropertyLink.html#a797df0fe915ebf8aa1f7ae2cfc8260d2),
and
[App::PropertyLinkBase::tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95).

## ◆ getEditorName()

| virtual const char * App::PropertyLink::getEditorName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Get the class name of the associated property editor item.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983).

Reimplemented in
[App::PropertyXLinkSub](../../d4/da0/classApp_1_1PropertyXLinkSub.html#af18a39f9a42ea4ae3e720c2660c11c52).

## ◆ getLinks()

| void PropertyLink::getLinks  | ( | std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ ,   
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

Reimplemented in
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a6d1b6fbac4089fed0e84c4e617cf1f50).

References
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e).

## ◆ getMemSize()

| virtual unsigned [int](../../d1/da0/classint.html) App::PropertyLink::getMemSize  | ( | void  | | ) |  const  
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

| [PyObject](../../df/d1b/classPyObject.html) * PropertyLink::getPyObject  | ( | void  | | ) |   
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

Reimplemented in
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#ac41751baabdd2bcb04a996719004377e),
and
[App::PropertyXLinkSub](../../d4/da0/classApp_1_1PropertyXLinkSub.html#ad996567330d5c7b6255da532d74ae9b5).

## ◆ getValue() [1/3]

[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * PropertyLink::getValue  | ( | [Base::Type](../../dc/dee/classBase_1_1Type.html) | _t_| ) |  const  
---|---|---|---|---|---  
  
Returns the link type checked.

## ◆ getValue() [2/3]

[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * PropertyLink::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
This method returns the linked
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.").

Referenced by
[FemGui::TaskDlgMeshShapeNetgen::accept()](../../dc/db4/classFemGui_1_1TaskDlgMeshShapeNetgen.html#aa88c49eb6c4ad7cd760e8fcb2c3181be),
[MeshPartGui::Tessellation::accept()](../../d7/d65/classMeshPartGui_1_1Tessellation.html#a222ec7598711d0c506f4897d9a996bd1),
[TechDrawGui::MDIViewPage::addChildrenToPage()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#aad0e8f131364d2c566d30b9b71459f82),
[TechDrawGui::QGSPage::addRichAnno()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#afd389b13fcebe704242da768d5f43e50),
[TechDrawGui::QGSPage::addWeldSymbol()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#ab4551ef1803974a53ffb7a2d9d993e2a),
[Part::Extrusion::calculateShapeNormal()](../../db/d6c/classPart_1_1Extrusion.html#a9068fcaf96e864a90a04b860140de9c9),
[TechDrawGui::MDIViewPage::centerOnPage()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a9c9b5bcaa0ccd63883749691513df54b),
[FemGui::ViewProviderFemPostPipeline::claimChildren()](../../df/d95/classFemGui_1_1ViewProviderFemPostPipeline.html#ac5626a9e2850eeb26ecff5a70bf2d941),
[PathGui::ViewProviderAreaView::claimChildren()](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#af7f604bd9905d7b5488f874185e867d9),
[TechDrawGui::ViewProviderPage::claimChildren()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#abaf1943763d885917f20c4a78a8e2ef5),
[App::PropertyXLinkSubList::CopyOnLinkReplace()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4aeacb995d8cd9f1ddd3309d87703960),
[FemGui::TaskCreateNodeSet::DefineNodes()](../../da/d68/classFemGui_1_1TaskCreateNodeSet.html#a6bd7d00ad2d337fbb90c45d927e80c71),
[PartDesignGui::ViewProviderBody::dropObject()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3e245daa7cd5dbb26f3603f2e93f68fe),
[Mesh::Curvature::execute()](../../d2/d39/classMesh_1_1Curvature.html#a76bfebcb28cee108275564ade910411c),
[Mesh::HarmonizeNormals::execute()](../../d8/d1c/classMesh_1_1HarmonizeNormals.html#a7f4d3c74b5c71fcb87e8467ae09a78f0),
[Mesh::FlipNormals::execute()](../../d3/d05/classMesh_1_1FlipNormals.html#a781c0a4c289cd3fecb312a743d04c2a6),
[Mesh::FixNonManifolds::execute()](../../d5/d33/classMesh_1_1FixNonManifolds.html#a1ee7ec392eeb5cb3a206989d21b3e3bc),
[Mesh::FixDuplicatedFaces::execute()](../../d9/d63/classMesh_1_1FixDuplicatedFaces.html#affadc4a69ba22744612248e94059ea13),
[Mesh::FixDuplicatedPoints::execute()](../../d1/d7b/classMesh_1_1FixDuplicatedPoints.html#abb108a05948e9906cefd394da59fdf77),
[Mesh::FixDegenerations::execute()](../../db/d8f/classMesh_1_1FixDegenerations.html#a3425c9ffba4deeb1c73c7fe910429687),
[Mesh::FixDeformations::execute()](../../d1/dbc/classMesh_1_1FixDeformations.html#a8c0ddd5b2e77c30a2466dc1fd08cdc7a),
[Mesh::FixIndices::execute()](../../d3/deb/classMesh_1_1FixIndices.html#a83eddf2883e3fc904c150d124d8aa01f),
[Mesh::FillHoles::execute()](../../d2/ddd/classMesh_1_1FillHoles.html#a21a0e0e99c2dcd82f9918fe67def820b),
[Mesh::RemoveComponents::execute()](../../da/d7a/classMesh_1_1RemoveComponents.html#a552facf8870d9ef3b36e1dee379fac07),
[Mesh::Export::execute()](../../d6/d40/classMesh_1_1Export.html#a56265dded005a8be13258af1b273ed51),
[Mesh::SegmentByMesh::execute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#a0fd4604225620a5902f526c867f0a7ed),
[Mesh::SetOperations::execute()](../../d3/d8f/classMesh_1_1SetOperations.html#a5fbee709af3e7da8f267824be4c4b370),
[Drawing::FeatureProjection::execute()](../../d8/d73/classDrawing_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Fem::FemMeshShapeNetgenObject::execute()](../../d9/df4/classFem_1_1FemMeshShapeNetgenObject.html#ad38e08d369e0a9c44588e98bc5ffb3ed),
[Fem::FemMeshShapeObject::execute()](../../d0/d41/classFem_1_1FemMeshShapeObject.html#a52f6bff1d5da5dc0dc05d3d0a4a90e72),
[Fem::FemPostPipeline::execute()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a37a7074a69af004117f82d72be1701f8),
[Inspection::Feature::execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[Part::Mirroring::execute()](../../dc/dac/classPart_1_1Mirroring.html#aed38846265cf2381aae85d15dfb74be7),
[Part::Boolean::execute()](../../da/d3a/classPart_1_1Boolean.html#ab93d1734459a414d09ccec9df8df7831),
[Part::Refine::execute()](../../d4/d0a/classPart_1_1Refine.html#aa138404bf1cbb4270a6e4a9d02dffac7),
[Part::Reverse::execute()](../../d4/d24/classPart_1_1Reverse.html#a22150a83fa78387e05f60dd1e08d31f8),
[PartDesign::FeatureBase::execute()](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a7cc09059c368f65475f0fa3f05bc06f5),
[PartDesign::Transformed::execute()](../../dd/de1/classPartDesign_1_1Transformed.html#aef9667071a3f6bb2ed13226f84629049),
[Path::FeatureAreaView::execute()](../../d3/db4/classPath_1_1FeatureAreaView.html#a181be122ea1283aac8cb22d51edc5686),
[Raytracing::LuxFeature::execute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a235b146fb9255cb705a6b86fb6967c3d),
[Raytracing::RayFeature::execute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[TechDraw::DrawViewSpreadsheet::execute()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a2d98f05816771e2b3a057443ea2f981c),
[TechDraw::FeatureProjection::execute()](../../dd/ddc/classTechDraw_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Part::Offset::execute()](../../d0/dda/classPart_1_1Offset.html#a342f29a6b5381db240304b9384b313dd),
[Part::Offset2D::execute()](../../d7/dcf/classPart_1_1Offset2D.html#a3eb29bb0e6404263cb3470d7ec24ea4a),
[Part::Revolution::execute()](../../d3/d17/classPart_1_1Revolution.html#a0406e2da5876bbf2351991c6b48b7185),
[PartDesign::Body::execute()](../../dd/db8/classPartDesign_1_1Body.html#a4abca6b2645adade81347d0e850a2659),
[TechDraw::DrawProjGroup::execute()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a53036ad3632d51fe082b67c8f829b54f),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[TechDrawGui::QGSPage::findParent()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#aa36872a18b939b5400ece0e09997fd0f),
[TechDraw::DrawProjGroup::getAnchor()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a1d309c494ece7ab3a4bf8b18527c47f0),
[TechDraw::DrawProjGroup::getAnchorDirection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a6b386f82419d9dff8f039eb92b53cd31),
[TechDrawGui::QGIProjGroup::getAnchorQItem()](../../db/d20/classTechDrawGui_1_1QGIProjGroup.html#a1f5592e205f0656b762b632c977b8745),
[TechDraw::DrawViewSection::getBaseDPGI()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#af83079c6b71a10b1c2986ecb0b30375c),
[TechDraw::DrawViewSection::getBaseDVP()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aae6243e0a6dd3abfd5bd02e1066dcfbb),
[TechDraw::DrawLeaderLine::getBaseView()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#abf1bafffae33b7cbb428bf467bf85c95),
[TechDraw::DrawRichAnno::getBaseView()](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#a786e30f49fa7adf2ade909e51d44cf2c),
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686),
[Part::BodyBase::getFullModel()](../../da/dc8/classPart_1_1BodyBase.html#ac7ff3e940968deef95cbf20182b1e62f),
[Fem::FemPostFilter::getInputData()](../../d8/d6f/classFem_1_1FemPostFilter.html#ae3dbe91d8a70d85554e49b2f9d3a079b),
[PartDesign::Body::getNextSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#a0c9db11c1cca8a2a0c7247d7d3498242),
[TechDraw::DrawPage::getPageHeight()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ac3db535fcb4092f6a10886b734610eab),
[TechDraw::DrawPage::getPageOrientation()](../../d9/d5a/classTechDraw_1_1DrawPage.html#acfcfcccb6fbd3ebc861e8c7ffd06d301),
[TechDraw::DrawPage::getPageWidth()](../../d9/d5a/classTechDraw_1_1DrawPage.html#abe7626bfbc51068143aa7d089fecb586),
[TechDraw::DrawTile::getParent()](../../da/d56/classTechDraw_1_1DrawTile.html#a6628e12f815b7bdb0e2c2b23230755d7),
[PartDesign::Body::getPrevSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#aface61e57526fc0ce72faff92c3e0841),
[Path::FeatureAreaView::getShapes()](../../d3/db4/classPath_1_1FeatureAreaView.html#a8bdeb47d6e84b6cfb93ce2eb43e7bbe9),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[TechDrawGui::QGIViewBalloon::getSourceView()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a0284857b25ce3933abc4a8bd7bf85860),
[TechDraw::DrawViewBalloon::getViewPart()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#af0563fa2613b74e99b671440cfb99729),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[TechDraw::DrawProjGroup::hasAnchor()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#ab79287a428f2f378c9d4087b21c67092),
[TechDraw::DrawPage::hasValidTemplate()](../../d9/d5a/classTechDraw_1_1DrawPage.html#addb0ce93dfeaa39ce5808639fc3ff9fb),
[Part::BodyBase::isAfter()](../../da/dc8/classPart_1_1BodyBase.html#a9a200c47ffd7f95eb5584fd6bf54dfe3),
[TechDraw::DrawWeldSymbol::isTailRightSide()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#a146cec4168e615dc4ddad1ea3eefbf2e),
[TechDrawGui::MDIViewPage::matchSceneRectToTemplate()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#acb333b23748e37400ee751b9bd066b0f),
[Mesh::Curvature::mustExecute()](../../d2/d39/classMesh_1_1Curvature.html#a6af7b48ccba04340a5a6a2d1b683b86f),
[Mesh::Export::mustExecute()](../../d6/d40/classMesh_1_1Export.html#af08e8f0650d1a809006084471fe51e10),
[Mesh::SegmentByMesh::mustExecute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#ae266a9b9fa667055d01165b431ea99eb),
[Mesh::SetOperations::mustExecute()](../../d3/d8f/classMesh_1_1SetOperations.html#a4f5806f8ade3aad44cb8e973436418aa),
[Part::Boolean::mustExecute()](../../da/d3a/classPart_1_1Boolean.html#af3f085bc4a0685aa0b35b9ed302909ed),
[Fem::FemPostClipFilter::onChanged()](../../dc/d06/classFem_1_1FemPostClipFilter.html#a696285744236a6bf6e8c14f735034705),
[Fem::FemPostCutFilter::onChanged()](../../da/d89/classFem_1_1FemPostCutFilter.html#a682758b8e3c1c8cf8b272d2244321913),
[Fem::FemPostPipeline::onChanged()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a333b47057bc9b7691cc0c9db9b0c79ba),
[PartDesign::FeatureBase::onChanged()](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a628a37fc8716ca08f0c67bb727ac3b76),
[PartDesign::DressUp::onChanged()](../../df/de5/classPartDesign_1_1DressUp.html#a7f7a173d69576711009fb17aeb08f6bc),
[PartDesign::Body::onChanged()](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[TechDraw::DrawViewSection::onChanged()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[PartGui::ViewProviderBoolean::onDelete()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#a373d00ad4fff430f80363ff4e3fa7eec),
[PartGui::ViewProviderMirror::onDelete()](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a952479217b74ad64994248d817c055fd),
[PartGui::ViewProviderFillet::onDelete()](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a923e0a83b084654171dd99eecdc464dd),
[PartGui::ViewProviderChamfer::onDelete()](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a475ba4ccc420a1807fc61b5fe01f462d),
[PartGui::ViewProviderRevolution::onDelete()](../../dc/d27/classPartGui_1_1ViewProviderRevolution.html#a60400330db6dc99c3795e9ac308e1aa2),
[PathGui::ViewProviderAreaView::onDelete()](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a81773c64dfc95d972592c1ff76a798d9),
[PartDesignGui::ViewProvider::onDelete()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ae369224b0333fe874ef00f3a7d168fe7),
[PartDesign::Body::onDocumentRestored()](../../dd/db8/classPartDesign_1_1Body.html#aa6affc475d3884d9570838e731749605),
[FemGui::TaskCreateNodeSet::onSelectionChanged()](../../da/d68/classFemGui_1_1TaskCreateNodeSet.html#ad2deb16f6c0659bcef35f11d21ea6972),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[PartDesign::DressUp::positionByBaseFeature()](../../df/de5/classPartDesign_1_1DressUp.html#ad0f7b71428ae5784d44e9a75f810ff3c),
[TechDrawGui::MDIViewPage::print()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#aea81462518a2663a6eeec8b001abea4c),
[PartGui::OffsetWidget::reject()](../../d9/d6d/classPartGui_1_1OffsetWidget.html#ab7d737c4b146e651782a10b5669b873c),
[PartDesignGui::TaskDlgFeatureParameters::reject()](../../df/d42/classPartDesignGui_1_1TaskDlgFeatureParameters.html#ab22141db4eb33119ad64ed387063f830),
[PartDesignGui::relinkToBody()](../../dc/d12/namespacePartDesignGui.html#a5bd0f34409b95d9ccc03b0b80655b0fd),
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
[PartDesign::Body::removeObject()](../../dd/db8/classPartDesign_1_1Body.html#a207956cf2a361690d971c7e604fc8bf1),
[App::Document::save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
[TechDraw::DrawProjGroup::setAnchorDirection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a2c029d1ede27331ee73642a306a76b57),
[TechDrawGui::ViewProviderPage::setTemplateMarkers()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#afc5258258f9e246ab22a52bb8bbbe03a),
[TechDrawGui::TaskLeaderLine::setUiEdit()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0eed6886711ee111f1ee0a8e314d6e21),
[TechDrawGui::TaskRichAnno::setUiEdit()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a3659e9cb13bc53ae36a3d7d16479d017),
[PartDesignGui::Workbench::setupContextMenu()](../../d4/d0c/classPartDesignGui_1_1Workbench.html#adf13eeb6b7f53fc0ce4c900cbca9712e),
[TechDrawGui::QGIViewBalloon::setViewPartFeature()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6f17a801836429d822e8998b0edfbff5),
[FemGui::TaskCreateNodeSet::TaskCreateNodeSet()](../../da/d68/classFemGui_1_1TaskCreateNodeSet.html#a1086e9019942d2317e5a5dc3285cb67e),
[TechDrawGui::TaskDetail::TaskDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a778a8671814ffb63e1a612302df298ce),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[TechDrawGui::TaskLeaderLine::TaskLeaderLine()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a873d04472b6a0de7f250ac13eef14913),
[TechDrawGui::TaskRichAnno::TaskRichAnno()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#acfd26140dce1c41560c4391c78b2fb06),
[TechDrawGui::TaskSectionView::TaskSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a8aa3d86a98175927e7dd69b2eea5b82e),
[TechDrawGui::TaskWeldingSymbol::TaskWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#aaf7cb244a051a9f8977d8ca2e0f00a17),
[TechDraw::DrawPage::unsetupObject()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ad65529c32a2d36f88a87e6734f093fcf),
[TechDraw::DrawViewDetail::unsetupObject()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#a94df756e01896f5fc84f7b68edf0cd87),
[PartGui::ViewProviderBoolean::updateData()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#ae38d6575df4dd650428a3d5873874d94),
[PartGui::ViewProviderFillet::updateData()](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a681e5f4afcfbf90240da46de01068325),
[PartGui::ViewProviderChamfer::updateData()](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a33e0d402eb35a8d3bf589039003c4f0d),
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
[TechDrawGui::ViewProviderLeader::updateData()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9885aee56382e6ad1e6e69b583197aa1),
[PartDesignGui::ViewProviderBody::updateData()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a2a541fb893a7130314f3c7161c33477e),
[TechDrawGui::MDIViewPage::updateTemplate()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5dad0574c1df0a7c6398e90173300461),
and
[App::PropertyLinkSubList::upgrade()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b).

## ◆ getValue() [3/3]

template<typename _type >

_type App::PropertyLink::getValue  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Returns the link type checked.

## ◆ Paste()

| void PropertyLink::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be).

Reimplemented in
[App::PropertyPlacementLink](../../d8/db5/classApp_1_1PropertyPlacementLink.html#aa08172316e8d59b648dcc5ac8266d56e),
and
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a6d593eed6217cccfdad4a79a4c752c27).

References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
and
[setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1).

## ◆ resetLink()

void PropertyLink::resetLink  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
and
[App::DocumentObject::testStatus()](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120).

Referenced by
[App::PropertyXLink::detach()](../../d2/de2/classApp_1_1PropertyXLink.html#a46ab216473399ea97b072f5926911380),
[App::PropertyXLink::unlink()](../../d2/de2/classApp_1_1PropertyXLink.html#a112a0063bb96d28de578e871764a267e),
and
[~PropertyLink()](../../d4/d77/classApp_1_1PropertyLink.html#adb6e576152567b3139b32b6beacf1dfd).

## ◆ Restore()

| void PropertyLink::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d4/d77/classApp_1_1PropertyLink.html#a89ed9d7172c31abd43b9ce7e99424ed8
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

Reimplemented in
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c).

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[Base::XMLReader::getName()](../../dc/d95/classBase_1_1XMLReader.html#aa529233af401d7719226293c506792f8),
[App::Document::getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
[Base::XMLReader::isVerbose()](../../dc/d95/classBase_1_1XMLReader.html#a89fa30d380593281c1e22864653a8b0a),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1),
and
[Base::ConsoleSingleton::Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

Referenced by
[TechDraw::DrawViewBalloon::handleChangedPropertyName()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a8f43bff2ef5b6712e7fd0546b639e6ef),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[App::PropertyLinkSubList::upgrade()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b),
and
[App::PropertyXLink::upgrade()](../../d2/de2/classApp_1_1PropertyXLink.html#ab593a78066f09572d98eac5046d8accf).

## ◆ Save()

| void PropertyLink::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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

Reimplemented in
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8).

References
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ setPyObject()

| void PropertyLink::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

Reimplemented in
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#adb26821a0a3916e6252bc6b4f0c5637e).

References
[setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1).

## ◆ setValue()

| void PropertyLink::setValue  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _lValue_| ) |   
---|---|---|---|---|---  
virtual  
  
Sets the property.

Reimplemented in
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7).

References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[App::PropertyLinkBase::LinkAllowExternal](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fad0f16a963cb6d4ee03471a56eb0d2b2e),
and
[App::PropertyLinkBase::testFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7aecf32bcda9d645f8a37ece5c3598ef).

Referenced by
[PartDesign::Body::addObject()](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605),
[TechDraw::DrawProjGroup::addProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acfc4e756c8714973996318393180f483),
[breakLink()](../../d4/d77/classApp_1_1PropertyLink.html#a5ba319a4ccf1773412d1d5023482ceda),
[PathGui::ViewProviderAreaView::dragObject()](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a3149f241f25662de8f6ff77377188f5e),
[PathGui::ViewProviderAreaView::dropObject()](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a42e56c173ddcbe847f69e2765497244a),
[PartDesignGui::ViewProviderBody::dropObject()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3e245daa7cd5dbb26f3603f2e93f68fe),
[Fem::FemPostPipeline::onChanged()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a333b47057bc9b7691cc0c9db9b0c79ba),
[PartDesign::DressUp::onChanged()](../../df/de5/classPartDesign_1_1DressUp.html#a7f7a173d69576711009fb17aeb08f6bc),
[PartDesign::Body::onChanged()](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[TechDraw::DrawWeldSymbol::onSettingDocument()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#aebf48eba403fab933cfaba6f325c6bc2),
[DrawingGui::orthoview::orthoview()](../../db/df8/classDrawingGui_1_1orthoview.html#afc8be37cc7e9325e722e05f2736af13d),
[Paste()](../../d4/d77/classApp_1_1PropertyLink.html#a31b305bd16358bc6459e33bf47e1c2b6),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
[App::OriginGroupExtension::relinkToOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#af4330ed14ea93ff3cbf7d0f952cf5e49),
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
[PartDesign::Body::removeObject()](../../dd/db8/classPartDesign_1_1Body.html#a207956cf2a361690d971c7e604fc8bf1),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[PartDesign::Body::setBaseProperty()](../../dd/db8/classPartDesign_1_1Body.html#abbb8bb2a283a57b6d6f2230dcacd7be3),
[setPyObject()](../../d4/d77/classApp_1_1PropertyLink.html#a8df27dbc0e724558a372f813a7eda649),
[TechDraw::DrawPage::unsetupObject()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ad65529c32a2d36f88a87e6734f093fcf),
[TechDraw::DrawProjGroupItem::unsetupObject()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a74c1e831d9704f99007d0b9398001f90),
and
[PartGui::DlgExtrusion::validate()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a9434547a26c67894da218387403f1c86).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyLinks.h
  * FreeCAD/src/App/PropertyLinks.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

