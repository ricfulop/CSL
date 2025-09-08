---
url: https://freecad.github.io/SourceDoc/d2/de2/classApp_1_1PropertyXLink.html
scraped_at: 2025-09-08T14:56:52.251423
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html)

[List of all members](../../df/ddf/classApp_1_1PropertyXLink-members.html) | Public Member Functions | Static Public Member Functions | Protected Member Functions | Protected Attributes | Friends

App::PropertyXLink Class Reference

[Link](../../df/d9b/classApp_1_1Link.html) to an (sub)object in the same or
different document.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#details)

`#include <PropertyLinks.h>`

##  Public Member Functions  
  
---  
virtual [bool](../../d9/db9/classbool.html) | [adjustLink](../../d2/de2/classApp_1_1PropertyXLink.html#a33bbd1956612a56e1967fdd7d6c533ff) (const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList) override  
| Called to adjust the link to avoid potential cyclic dependency.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a33bbd1956612a56e1967fdd7d6c533ff)  
  
virtual void | [afterRestore](../../d2/de2/classApp_1_1PropertyXLink.html#a01ca28793b37026f539afb49f397aec2) () override  
| Called at the beginning of
[Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5)
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a01ca28793b37026f539afb49f397aec2)  
  
virtual [int](../../d1/da0/classint.html) | [checkRestore](../../d2/de2/classApp_1_1PropertyXLink.html#aff57f99ddc399ce82d8f17da884a1052) (std::string *msg=nullptr) const override  
| Test if the link is restored unchanged.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#aff57f99ddc399ce82d8f17da884a1052)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d2/de2/classApp_1_1PropertyXLink.html#a6e7ddbe8a1061c36145bd0180b47c7f1) (void) const override  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a6e7ddbe8a1061c36145bd0180b47c7f1)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnImportExternal](../../d2/de2/classApp_1_1PropertyXLink.html#a145fcf5a76cec92e8ca60bad28e6fe76) (const std::map< std::string, std::string > &nameMap) const override  
| Return a copy of the property if any changes caused by importing external
object.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a145fcf5a76cec92e8ca60bad28e6fe76)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLabelChange](../../d2/de2/classApp_1_1PropertyXLink.html#a9c9b89ffa3e4be3e0e5a046e6371e557) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &ref, const char *newLabel) const override  
| Update object label reference in this property.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a9c9b89ffa3e4be3e0e5a046e6371e557)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLinkReplace](../../d2/de2/classApp_1_1PropertyXLink.html#aa713c66bf6fd8a5a03ec1f94b233e8bb) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *[parent](../../d2/de2/classApp_1_1PropertyXLink.html#af0c960e7a1887137537ee5687fe0fba0), [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj) const override  
| Return a copy of the property if the link replacement affects this property.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#aa713c66bf6fd8a5a03ec1f94b233e8bb)  
  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [getDocument](../../d2/de2/classApp_1_1PropertyXLink.html#a60e7fe76c5724b6cd312b8285debcde2) () const  
const char * | [getDocumentPath](../../d2/de2/classApp_1_1PropertyXLink.html#a5660c90a2bc17861c700704fba7cefad) () const  
const char * | [getFilePath](../../d2/de2/classApp_1_1PropertyXLink.html#acdf3aef6ba4592a11efc846bb61d524d) () const  
virtual void | [getLinks](../../d2/de2/classApp_1_1PropertyXLink.html#a6d1b6fbac4089fed0e84c4e617cf1f50) (std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [bool](../../d9/db9/classbool.html) all=false, std::vector< std::string > *subs=nullptr, [bool](../../d9/db9/classbool.html) newStyle=true) const override  
| Obtain the linked objects.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a6d1b6fbac4089fed0e84c4e617cf1f50)  
  
const char * | [getObjectName](../../d2/de2/classApp_1_1PropertyXLink.html#a22c29a4b6e7481845ef68a86832d189b) () const  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d2/de2/classApp_1_1PropertyXLink.html#ac41751baabdd2bcb04a996719004377e) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#ac41751baabdd2bcb04a996719004377e)  
  
const std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > & | [getShadowSubs](../../d2/de2/classApp_1_1PropertyXLink.html#a8a98785ff5c5db6351198200920e0ec1) () const  
const char * | [getSubName](../../d2/de2/classApp_1_1PropertyXLink.html#a2bcc6ebd15be27ffa28a103acdd1f868) ([bool](../../d9/db9/classbool.html) newStyle=true) const  
std::vector< std::string > | [getSubValues](../../d2/de2/classApp_1_1PropertyXLink.html#a2246895403f7f20c7e35566b68844bf9) ([bool](../../d9/db9/classbool.html) newStyle) const  
const std::vector< std::string > & | [getSubValues](../../d2/de2/classApp_1_1PropertyXLink.html#a6a73ddf81fd55ce432348c25878c2563) (void) const  
std::vector< std::string > | [getSubValuesStartsWith](../../d2/de2/classApp_1_1PropertyXLink.html#a8069726983a2304e6b1a765b75903a5b) (const char *, [bool](../../d9/db9/classbool.html) newStyle=false) const  
[bool](../../d9/db9/classbool.html) | [hasSubName](../../d2/de2/classApp_1_1PropertyXLink.html#aee08c617cbbfb95fdcc7ecde4459dc24) () const  
virtual void | [onContainerRestored](../../d2/de2/classApp_1_1PropertyXLink.html#a907c0f4bd96da3bad11eb35ac11acf3f) () override  
| Called before calling
[DocumentObject::onDocumentRestored()](../../d2/de4/classApp_1_1DocumentObject.html#a0ee8399fa0b176c64895150691a4b604
"get called after a document has been fully restored")
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a907c0f4bd96da3bad11eb35ac11acf3f)  
  
[PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) * | [parent](../../d2/de2/classApp_1_1PropertyXLink.html#af0c960e7a1887137537ee5687fe0fba0) () const  
virtual void | [Paste](../../d2/de2/classApp_1_1PropertyXLink.html#a6d593eed6217cccfdad4a79a4c752c27) (const [Property](../../d0/da9/classApp_1_1Property.html) &from) override  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a6d593eed6217cccfdad4a79a4c752c27)  
  
|
[PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#af5bf51d11efd27dbabae85588c322a7d)
([bool](../../d9/db9/classbool.html) allowPartial=false,
[PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)
*[parent](../../d2/de2/classApp_1_1PropertyXLink.html#af0c960e7a1887137537ee5687fe0fba0)=nullptr)  
virtual [bool](../../d9/db9/classbool.html) | [referenceChanged](../../d2/de2/classApp_1_1PropertyXLink.html#a64775c79df3f1636f0c8b75b61f7cbff) () const override  
| Test if the element reference has changed after restore.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a64775c79df3f1636f0c8b75b61f7cbff)  
  
virtual void | [Restore](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c)  
  
virtual void | [Save](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8)  
  
virtual void | [setAllowPartial](../../d2/de2/classApp_1_1PropertyXLink.html#af69aa75e548072c713a0b180cadab17e) ([bool](../../d9/db9/classbool.html) enable) override  
virtual void | [setPyObject](../../d2/de2/classApp_1_1PropertyXLink.html#adb26821a0a3916e6252bc6b4f0c5637e) ([PyObject](../../df/d1b/classPyObject.html) *) override  
void | [setSubName](../../d2/de2/classApp_1_1PropertyXLink.html#a576472096f84a71a74169e29ac6eb41b) (const char *subname)  
void | [setSubValues](../../d2/de2/classApp_1_1PropertyXLink.html#ab317a05477f1ee776d1c4f765b70b1cd) (std::vector< std::string > &&SubList, std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > &&ShadowSubList={})  
void | [setSyncSubObject](../../d2/de2/classApp_1_1PropertyXLink.html#ad597b3718a0a6b23eb99c39d8173f8a5) ([bool](../../d9/db9/classbool.html) enable)  
void | [setValue](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *) override  
| Sets the property.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7)  
  
void | [setValue](../../d2/de2/classApp_1_1PropertyXLink.html#a0aee61347281a5a90b7553e4d5c76b47) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, const char *subname)  
void | [setValue](../../d2/de2/classApp_1_1PropertyXLink.html#a087dbd77330cd073a00455377b0dc518) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, const std::vector< std::string > &SubList, std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > &&ShadowSubList={})  
void | [setValue](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > &&SubList, std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > &&ShadowSubList={})  
void | [setValue](../../d2/de2/classApp_1_1PropertyXLink.html#a08df921d547d315b596fe24b593f8637) (std::string &&[filePath](../../d2/de2/classApp_1_1PropertyXLink.html#a1d8a3774745a9c560df18df4d3871bb4), std::string &&[objectName](../../d2/de2/classApp_1_1PropertyXLink.html#a92ddffaf513f7a5d9eecc05df6c42e40), std::vector< std::string > &&SubList, std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > &&ShadowSubList={})  
virtual void | [updateElementReference](../../d2/de2/classApp_1_1PropertyXLink.html#a94e60fa4261d661b629b5c0d35215dff) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *feature, [bool](../../d9/db9/classbool.html) reverse=false, [bool](../../d9/db9/classbool.html) notify=false) override  
| [Link](../../df/d9b/classApp_1_1Link.html) type property interface APIs
These APIs are moved here so that any type of property can have the property
link behavior, e.g.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a94e60fa4261d661b629b5c0d35215dff)  
  
virtual [bool](../../d9/db9/classbool.html) | [upgrade](../../d2/de2/classApp_1_1PropertyXLink.html#ab593a78066f09572d98eac5046d8accf) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *typeName)  
virtual | [~PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#ae8daad6014c712dc6527596d60db8c49) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyLinkGlobal](../../d6/da0/classApp_1_1PropertyLinkGlobal.html)  
|
[PropertyLinkGlobal](../../d6/da0/classApp_1_1PropertyLinkGlobal.html#abc13af83f13e8392e195a66067c4afc8)
()  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html)  
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
  
  
##  Static Public Member Functions  
  
---  
static std::map< [App::Document](../../d8/d3e/classApp_1_1Document.html) *, std::set< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > > | [getDocumentInList](../../d2/de2/classApp_1_1PropertyXLink.html#ad702be5a5d5a8c7cdf8f10cd4c22f26d) ([App::Document](../../d8/d3e/classApp_1_1Document.html) *doc=nullptr)  
static std::map< [App::Document](../../d8/d3e/classApp_1_1Document.html) *, std::set< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > > | [getDocumentOutList](../../d2/de2/classApp_1_1PropertyXLink.html#af1f6b642c153368da2ec154538106914) ([App::Document](../../d8/d3e/classApp_1_1Document.html) *doc=nullptr)  
static [bool](../../d9/db9/classbool.html) | [hasXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a9b5a3af810860e7117ad6f11e5d4c7e1) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) *doc)  
static [bool](../../d9/db9/classbool.html) | [hasXLink](../../d2/de2/classApp_1_1PropertyXLink.html#af3eb189627d94c9b9ff1c6d79d4eef83) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, std::vector< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > *unsaved=nullptr)  
static void | [restoreDocument](../../d2/de2/classApp_1_1PropertyXLink.html#a5ef57584d28afeba3785b8d5dada73b5) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &doc)  
static [bool](../../d9/db9/classbool.html) | [supportXLink](../../d2/de2/classApp_1_1PropertyXLink.html#a3eec738eb9480c2a52fc5791de8a6d80) (const [App::Property](../../d0/da9/classApp_1_1Property.html) *prop)  
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
  
##  Protected Member Functions  
  
---  
virtual void | [aboutToSetValue](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57) () override  
| Gets called by all
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7
"Sets the property.") methods before the value has changed.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57)  
  
void | [copyTo](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c) ([PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html) &other, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *linked=nullptr, std::vector< std::string > *subs=nullptr) const  
void | [detach](../../d2/de2/classApp_1_1PropertyXLink.html#a46ab216473399ea97b072f5926911380) ()  
virtual void | [hasSetValue](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a) () override  
| Gets called by all
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7
"Sets the property.") methods after the value has changed.
[More...](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a)  
  
void | [restoreLink](../../d2/de2/classApp_1_1PropertyXLink.html#a232e8182760d7ae2717d555416e4b4ce) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
void | [unlink](../../d2/de2/classApp_1_1PropertyXLink.html#a112a0063bb96d28de578e871764a267e) ()  
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
  
  
##  Protected Attributes  
  
---  
[DocInfoPtr](../../dd/dc2/namespaceApp.html#a1752a0f247a3d9b40c49fb0d930114d5) | [docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031)  
std::string | [docName](../../d2/de2/classApp_1_1PropertyXLink.html#ac8e815dae93a8ad87b95c9ca4dbe22af)  
std::string | [filePath](../../d2/de2/classApp_1_1PropertyXLink.html#a1d8a3774745a9c560df18df4d3871bb4)  
std::string | [objectName](../../d2/de2/classApp_1_1PropertyXLink.html#a92ddffaf513f7a5d9eecc05df6c42e40)  
[PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) * | [parentProp](../../d2/de2/classApp_1_1PropertyXLink.html#ae83a809758609c669421a9ae2efc7c68)  
std::string | [stamp](../../d2/de2/classApp_1_1PropertyXLink.html#ab28b1f882f83732430330601752406fe)  
![-](../../closed.png) Protected Attributes inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
std::bitset< 32 > | [StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67)  
| Status bits of the property The first 8 bits are used for the base system
the rest can be used in descendent classes to mark special statuses on the
objects.
[More...](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67)  
  
  
##  Friends  
  
---  
class | [DocInfo](../../d2/de2/classApp_1_1PropertyXLink.html#a369cdf50b9058a05c8062deaef85826b)  
class | [PropertyXLinkSubList](../../d2/de2/classApp_1_1PropertyXLink.html#a96e41a54666fce9dffb5f8da4acabb48)  
  
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
![-](../../closed.png) Public Attributes inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
boost::signals2::signal< void(const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChanged](../../d0/da9/classApp_1_1Property.html#a9e9e25207ee1e619c75f835f9853cf74)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

[Link](../../df/d9b/classApp_1_1Link.html) to an (sub)object in the same or
different document.

## Constructor & Destructor Documentation

## ◆ PropertyXLink()

PropertyXLink::PropertyXLink  | ( | [bool](../../d9/db9/classbool.html) | _allowPartial_ = `false`,   
---|---|---|---  
|  | [PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) *  | _parent_ = `nullptr`  
| ) | |   
  
## ◆ ~PropertyXLink()

| PropertyXLink::~PropertyXLink  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[unlink()](../../d2/de2/classApp_1_1PropertyXLink.html#a112a0063bb96d28de578e871764a267e).

## Member Function Documentation

## ◆ aboutToSetValue()

| void PropertyXLink::aboutToSetValue  | ( | void  | | ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
Gets called by all
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7
"Sets the property.") methods before the value has changed.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d).

References
[App::Property::aboutToSetChildValue()](../../d0/da9/classApp_1_1Property.html#a9e3dfa9cc1ea03167fbe8c12f811f546),
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
and
[parentProp](../../d2/de2/classApp_1_1PropertyXLink.html#ae83a809758609c669421a9ae2efc7c68).

Referenced by
[detach()](../../d2/de2/classApp_1_1PropertyXLink.html#a46ab216473399ea97b072f5926911380),
[restoreLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a232e8182760d7ae2717d555416e4b4ce),
[setSubName()](../../d2/de2/classApp_1_1PropertyXLink.html#a576472096f84a71a74169e29ac6eb41b),
and
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10).

## ◆ adjustLink()

| [bool](../../d9/db9/classbool.html) PropertyXLink::adjustLink  | ( | const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _inList_| ) |   
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

Reimplemented from
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#aebfbbd1933b83fa53b46133da128c17a).

References
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7).

## ◆ afterRestore()

| void PropertyXLink::afterRestore  | ( | | ) |   
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
[afterRestore()](../../d2/de2/classApp_1_1PropertyXLink.html#a01ca28793b37026f539afb49f397aec2
"Called at the beginning of Document::afterRestore\(\)") to parse and restore
subname references, which may contain sub-object reference from external
document, and there will be special mapping required during object import.

Another example is
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
which only parse the restored expression in
[afterRestore()](../../d2/de2/classApp_1_1PropertyXLink.html#a01ca28793b37026f539afb49f397aec2
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

## ◆ checkRestore()

| [int](../../d1/da0/classint.html) PropertyXLink::checkRestore  | ( | std::string *  | _msg_ = `nullptr`| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Test if the link is restored unchanged.

Parameters

     msg| optional error message  
---|---  
  
Returns

    For external linked object, return 2 in case the link is missing, and 1 if the time stamp has changed. 

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a8d5f5505568090ea83840b00a7f140b9).

References
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031),
[filePath](../../d2/de2/classApp_1_1PropertyXLink.html#a1d8a3774745a9c560df18df4d3871bb4),
[App::PropertyLinkBase::LinkAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5faa22f8833820bace817e74b03e6089f45),
[objectName](../../d2/de2/classApp_1_1PropertyXLink.html#a92ddffaf513f7a5d9eecc05df6c42e40),
[App::Document::PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
[stamp](../../d2/de2/classApp_1_1PropertyXLink.html#ab28b1f882f83732430330601752406fe),
and
[App::PropertyLinkBase::testFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7aecf32bcda9d645f8a37ece5c3598ef).

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyXLink::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Reimplemented from
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a11d683872f0c6070dbef87552842d762).

References
[copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c).

## ◆ CopyOnImportExternal()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyXLink::CopyOnImportExternal  | ( | const std::map< std::string, std::string > & | _nameMap_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Return a copy of the property if any changes caused by importing external
object.

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab29ca627684ca9a3ed573a24eb8da131).

References
[copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::PropertyLinkBase::tryImport()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a2bf156dd3396caaad6204f5269698e7a),
and
[App::PropertyLinkBase::tryImportSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a368e7609bf8ee24fd6b574c392e8c6d4).

## ◆ CopyOnLabelChange()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyXLink::CopyOnLabelChange  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
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

    Returns a copy of the property if its link reference is affected. The copy will later be assgiend to this property by calling its [Paste()](../../d2/de2/classApp_1_1PropertyXLink.html#a6d593eed6217cccfdad4a79a4c752c27 "Paste the value from the property \(mainly for Undo/Redo and transactions\)"). 

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a0d1a5adbda3ed0d03313b8827548c1d6).

References
[copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
and
[App::PropertyLinkBase::updateLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ac2fd4f8ba5aeea8846f1ffc1d55e02da).

## ◆ CopyOnLinkReplace()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyXLink::CopyOnLinkReplace  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
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

Reimplemented from
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#ae33affee6371a40629ea84b1782c2cb5).

References
[copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[parent()](../../d2/de2/classApp_1_1PropertyXLink.html#af0c960e7a1887137537ee5687fe0fba0),
and
[App::PropertyLinkBase::tryReplaceLinkSubs()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ae7aa54cba5888dcd26d60876dd7672cc).

## ◆ copyTo()

| void PropertyXLink::copyTo  | ( | [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html) & | _other_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _linked_ = `nullptr`,   
|  | std::vector< std::string > *  | _subs_ = `nullptr`  
| ) | |  const  
protected  
  
References
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031),
[docName](../../d2/de2/classApp_1_1PropertyXLink.html#ac8e815dae93a8ad87b95c9ca4dbe22af),
[filePath](../../d2/de2/classApp_1_1PropertyXLink.html#a1d8a3774745a9c560df18df4d3871bb4),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::Document::getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[objectName](../../d2/de2/classApp_1_1PropertyXLink.html#a92ddffaf513f7a5d9eecc05df6c42e40).

Referenced by
[Copy()](../../d2/de2/classApp_1_1PropertyXLink.html#a6e7ddbe8a1061c36145bd0180b47c7f1),
[CopyOnImportExternal()](../../d2/de2/classApp_1_1PropertyXLink.html#a145fcf5a76cec92e8ca60bad28e6fe76),
[App::PropertyXLinkSubList::CopyOnImportExternal()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a583fcb98efbbb8211cfdd20437688de1),
[CopyOnLabelChange()](../../d2/de2/classApp_1_1PropertyXLink.html#a9c9b89ffa3e4be3e0e5a046e6371e557),
[App::PropertyXLinkSubList::CopyOnLabelChange()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#af9fed844cfcceb8be5f643a0146f7c25),
[CopyOnLinkReplace()](../../d2/de2/classApp_1_1PropertyXLink.html#aa713c66bf6fd8a5a03ec1f94b233e8bb),
and
[App::PropertyXLinkSubList::CopyOnLinkReplace()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4aeacb995d8cd9f1ddd3309d87703960).

## ◆ detach()

| void PropertyXLink::detach  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[aboutToSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57),
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031),
[hasSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a),
[App::PropertyLink::resetLink()](../../d4/d77/classApp_1_1PropertyLink.html#a0461c85fa8e082a75df6e848f94d8c39),
and
[updateElementReference()](../../d2/de2/classApp_1_1PropertyXLink.html#a94e60fa4261d661b629b5c0d35215dff).

## ◆ getDocument()

[App::Document](../../d8/d3e/classApp_1_1Document.html) * PropertyXLink::getDocument  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
References
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031).

## ◆ getDocumentInList()

| std::map< [App::Document](../../d8/d3e/classApp_1_1Document.html) *, std::set< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > > PropertyXLink::getDocumentInList  | ( | [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_ = `nullptr`| ) |   
---|---|---|---|---|---  
static  
  
References
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[App::Property::PropNoPersist](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ae221473138e52da3001d1de060205179),
[App::Property::PropTransient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a49215d8e9f6a5a24523e5ce094fb867e),
[App::DocumentObject::testStatus()](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120),
and
[App::Property::Transient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a14e77d5a09c2b0796490e697b68560e5).

Referenced by
[Gui::Document::canClose()](../../de/d4e/classGui_1_1Document.html#a9d5a988c5980ecdafede499fa261d135),
and
[Gui::Document::detachView()](../../de/d4e/classGui_1_1Document.html#a320afb4cc20d4c593cbe18accc44e3e5).

## ◆ getDocumentOutList()

| std::map< [App::Document](../../d8/d3e/classApp_1_1Document.html) *, std::set< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > > PropertyXLink::getDocumentOutList  | ( | [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_ = `nullptr`| ) |   
---|---|---|---|---|---  
static  
  
References
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[App::Property::PropNoPersist](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ae221473138e52da3001d1de060205179),
[App::Property::PropTransient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a49215d8e9f6a5a24523e5ce094fb867e),
[App::DocumentObject::testStatus()](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120),
and
[App::Property::Transient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a14e77d5a09c2b0796490e697b68560e5).

Referenced by
[StdCmdDelete::activated()](../../da/dc8/classStdCmdDelete.html#a120710ae4a8c0f26451596002a176ee7),
and
[App::Document::getDependentDocuments()](../../d8/d3e/classApp_1_1Document.html#adb6cbc200401458d8b96701838e7db43).

## ◆ getDocumentPath()

const char * PropertyXLink::getDocumentPath  | ( | | ) |  const  
---|---|---|---|---  
  
References
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031),
and
[filePath](../../d2/de2/classApp_1_1PropertyXLink.html#a1d8a3774745a9c560df18df4d3871bb4).

## ◆ getFilePath()

const char * App::PropertyXLink::getFilePath  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getLinks()

| void PropertyXLink::getLinks  | ( | std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ ,   
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
  
Reimplemented from
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a4750ce6a3916cee3e9746a683bbf4330).

References
[getSubValues()](../../d2/de2/classApp_1_1PropertyXLink.html#a6a73ddf81fd55ce432348c25878c2563),
and
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e).

## ◆ getObjectName()

const char * PropertyXLink::getObjectName  | ( | | ) |  const  
---|---|---|---|---  
  
References
[objectName](../../d2/de2/classApp_1_1PropertyXLink.html#a92ddffaf513f7a5d9eecc05df6c42e40).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyXLink::getPyObject  | ( | void  | | ) |   
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
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#accebd677bd5e10d5f9b576e2d0d72bf6).

Reimplemented in
[App::PropertyXLinkSub](../../d4/da0/classApp_1_1PropertyXLinkSub.html#ad996567330d5c7b6255da532d74ae9b5).

References
[App::PropertyString::getPyObject()](../../dd/df8/classApp_1_1PropertyString.html#aa6e72d76ecb8d448e1e8016f72f0dd66),
[getSubValues()](../../d2/de2/classApp_1_1PropertyXLink.html#a6a73ddf81fd55ce432348c25878c2563),
and
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

## ◆ getShadowSubs()

const std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > & App::PropertyXLink::getShadowSubs  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getSubName()

const char * PropertyXLink::getSubName  | ( | [bool](../../d9/db9/classbool.html) | _newStyle_ = `true`| ) |  const  
---|---|---|---|---|---  
  
## ◆ getSubValues() [1/2]

std::vector< std::string > PropertyXLink::getSubValues  | ( | [bool](../../d9/db9/classbool.html) | _newStyle_| ) |  const  
---|---|---|---|---|---  
  
## ◆ getSubValues() [2/2]

const std::vector< std::string > & App::PropertyXLink::getSubValues  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[App::PropertyXLinkSubList::CopyOnLinkReplace()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4aeacb995d8cd9f1ddd3309d87703960),
[getLinks()](../../d2/de2/classApp_1_1PropertyXLink.html#a6d1b6fbac4089fed0e84c4e617cf1f50),
[getPyObject()](../../d2/de2/classApp_1_1PropertyXLink.html#ac41751baabdd2bcb04a996719004377e),
and
[App::PropertyXLinkSub::getPyObject()](../../d4/da0/classApp_1_1PropertyXLinkSub.html#ad996567330d5c7b6255da532d74ae9b5).

## ◆ getSubValuesStartsWith()

std::vector< std::string > PropertyXLink::getSubValuesStartsWith  | ( | const char *  | _starter_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _newStyle_ = `false`  
| ) | |  const  
  
## ◆ hasSetValue()

| void PropertyXLink::hasSetValue  | ( | void  | | ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
Gets called by all
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7
"Sets the property.") methods after the value has changed.

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763).

References
[App::Property::hasSetChildValue()](../../d0/da9/classApp_1_1Property.html#a35de61d1f853c6adb4e150c6cbb97ede),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
and
[parentProp](../../d2/de2/classApp_1_1PropertyXLink.html#ae83a809758609c669421a9ae2efc7c68).

Referenced by
[detach()](../../d2/de2/classApp_1_1PropertyXLink.html#a46ab216473399ea97b072f5926911380),
[restoreLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a232e8182760d7ae2717d555416e4b4ce),
[setSubName()](../../d2/de2/classApp_1_1PropertyXLink.html#a576472096f84a71a74169e29ac6eb41b),
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10),
and
[updateElementReference()](../../d2/de2/classApp_1_1PropertyXLink.html#a94e60fa4261d661b629b5c0d35215dff).

## ◆ hasSubName()

[bool](../../d9/db9/classbool.html) App::PropertyXLink::hasSubName  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ hasXLink() [1/2]

| [bool](../../d9/db9/classbool.html) PropertyXLink::hasXLink  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[StdCmdDuplicateSelection::activated()](../../d4/d75/classStdCmdDuplicateSelection.html#a1ffe671eebc9f7e4c99740df06eaf0a9),
[App::Document::copyObject()](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0),
[Gui::MainWindow::createMimeDataFromSelection()](../../d5/d2f/classGui_1_1MainWindow.html#a1471665356b86fc81addf133db22c977),
[hasXLink()](../../d2/de2/classApp_1_1PropertyXLink.html#af3eb189627d94c9b9ff1c6d79d4eef83),
[StdCmdLinkImportAll::isActive()](../../d1/d95/classStdCmdLinkImportAll.html#a061965b212d6f01f3fb4452aeb30a140),
and
[App::Document::mustExecute()](../../d8/d3e/classApp_1_1Document.html#aaaf7a0d2a67cc06d760a16c352117189).

## ◆ hasXLink() [2/2]

| [bool](../../d9/db9/classbool.html) PropertyXLink::hasXLink  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ ,   
---|---|---|---  
|  | std::vector< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > *  | _unsaved_ = `nullptr`  
| ) | |   
static  
  
References
[hasXLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a9b5a3af810860e7117ad6f11e5d4c7e1).

## ◆ onContainerRestored()

| void PropertyXLink::onContainerRestored  | ( | | ) |   
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

## ◆ parent()

[PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) * App::PropertyXLink::parent  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[PathScripts.PathSimulatorGui.CAMSimTaskUi::accept()](../../d9/ddf/classPathScripts_1_1PathSimulatorGui_1_1CAMSimTaskUi.html#a4f458ca1ce80e66e440c5ac24dc22c8d),
[CopyOnLinkReplace()](../../d2/de2/classApp_1_1PropertyXLink.html#aa713c66bf6fd8a5a03ec1f94b233e8bb),
[Mod.PartDesign.WizardShaft.Shaft.Shaft::equilibrium()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#abf673f8921374b011ced4c4a770d44e6),
[PathScripts.PathSimulatorGui.CAMSimTaskUi::reject()](../../d9/ddf/classPathScripts_1_1PathSimulatorGui_1_1CAMSimTaskUi.html#a3ab3f3b4e171363a14dc6cc0a5edd790),
[Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
and
[PathScripts.PathOpGui.TaskPanelPage::setParent()](../../d1/d18/classPathScripts_1_1PathOpGui_1_1TaskPanelPage.html#a98bc030e5415979bcaa07140a675a6e3).

## ◆ Paste()

| void PropertyXLink::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Reimplemented from
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a31b305bd16358bc6459e33bf47e1c2b6).

References
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Application::getDocument()](../../da/dbf/classApp_1_1Application.html#a17472bb3dfacd07074016c3bcc4a270d),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
[App::PropertyLinkBase::LinkAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5faa22f8833820bace817e74b03e6089f45),
[App::PropertyLinkBase::setFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f),
and
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7).

## ◆ referenceChanged()

| [bool](../../d9/db9/classbool.html) PropertyXLink::referenceChanged  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Test if the element reference has changed after restore.

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af56b87f577368963c8aeec5a5fc74ee0).

## ◆ Restore()

| void PropertyXLink::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8
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

Reimplemented from
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4).

References
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[Base::XMLReader::getName()](../../dc/d95/classBase_1_1XMLReader.html#aa529233af401d7719226293c506792f8),
[App::Document::getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[App::PropertyLinkBase::importSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
[Base::XMLReader::isVerbose()](../../dc/d95/classBase_1_1XMLReader.html#a89fa30d380593281c1e22864653a8b0a),
[App::PropertyLinkBase::LinkAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5faa22f8833820bace817e74b03e6089f45),
[App::PropertyLinkBase::LinkRestoreLabel](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fa5a4bc69cb609a1f93370ec11e29dc403),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[parent()](../../d2/de2/classApp_1_1PropertyXLink.html#af0c960e7a1887137537ee5687fe0fba0),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[Base::XMLReader::readEndElement()](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3),
[App::PropertyLinkBase::setFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f),
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7),
and
[stamp](../../d2/de2/classApp_1_1PropertyXLink.html#ab28b1f882f83732430330601752406fe).

## ◆ restoreDocument()

| void PropertyXLink::restoreDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_| ) |   
---|---|---|---|---|---  
static  
  
References
[App::DocInfo::restoreDocument()](../../d7/d23/classApp_1_1DocInfo.html#adbe834c3373cedf88409bac61bb0302e).

Referenced by
[App::Application::openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728).

## ◆ restoreLink()

| void PropertyXLink::restoreLink  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _lValue_| ) |   
---|---|---|---|---|---  
protected  
  
References
[aboutToSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57),
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[hasSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[App::PropertyLinkBase::LinkDetached](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5facbc01e4b149e5b3049e9916b0181a7da),
[App::PropertyLinkBase::LinkRestoring](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fa1de51bd54c0f62a03f8a15c70ed4a365),
[App::PropertyLinkBase::setFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f),
[stamp](../../d2/de2/classApp_1_1PropertyXLink.html#ab28b1f882f83732430330601752406fe),
and
[updateElementReference()](../../d2/de2/classApp_1_1PropertyXLink.html#a94e60fa4261d661b629b5c0d35215dff).

## ◆ Save()

| void PropertyXLink::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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

Reimplemented from
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a89ed9d7172c31abd43b9ce7e99424ed8).

References
[Base::Writer::decInd()](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92),
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031),
[Base::Persistence::encodeAttribute()](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec),
[App::PropertyLinkBase::exportSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a08eab53abe5c11c895d4ecea426485ad),
[filePath](../../d2/de2/classApp_1_1PropertyXLink.html#a1d8a3774745a9c560df18df4d3871bb4),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::DocInfo::getDocPath()](../../d7/d23/classApp_1_1DocInfo.html#a9a066a626c84cb4c5ce152b9449b64f3),
[Base::Writer::incInd()](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5),
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
[App::PropertyLinkBase::LinkAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5faa22f8833820bace817e74b03e6089f45),
[objectName](../../d2/de2/classApp_1_1PropertyXLink.html#a92ddffaf513f7a5d9eecc05df6c42e40),
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205),
and
[App::PropertyLinkBase::testFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7aecf32bcda9d645f8a37ece5c3598ef).

## ◆ setAllowPartial()

| void PropertyXLink::setAllowPartial  | ( | [bool](../../d9/db9/classbool.html) | _enable_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a26441b0567312a6b71c03f2f16dee982).

References
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031),
[filePath](../../d2/de2/classApp_1_1PropertyXLink.html#a1d8a3774745a9c560df18df4d3871bb4),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::Application::isRestoring()](../../da/dbf/classApp_1_1Application.html#aa808751cb4b819afd2b2cab35c85cd1e),
[App::PropertyLinkBase::LinkAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5faa22f8833820bace817e74b03e6089f45),
[objectName](../../d2/de2/classApp_1_1PropertyXLink.html#a92ddffaf513f7a5d9eecc05df6c42e40),
[App::Application::openDocument()](../../da/dbf/classApp_1_1Application.html#a4ad1dd5f7c7ea3e47e6ccee518ca437c),
[App::Document::PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
and
[App::PropertyLinkBase::setFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f).

## ◆ setPyObject()

| void PropertyXLink::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _value_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a8df27dbc0e724558a372f813a7eda649).

References
[App::PropertyString::getStrValue()](../../dd/df8/classApp_1_1PropertyString.html#a7fdb947ab6f9552c1dd95a8e634c83c2),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[App::PropertyString::setPyObject()](../../dd/df8/classApp_1_1PropertyString.html#ac9b0f60fd6949cfd514653838e78840b),
and
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7).

## ◆ setSubName()

void PropertyXLink::setSubName  | ( | const char *  | _subname_| ) |   
---|---|---|---|---|---  
  
References
[aboutToSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57),
[hasSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[setSubValues()](../../d2/de2/classApp_1_1PropertyXLink.html#ab317a05477f1ee776d1c4f765b70b1cd).

## ◆ setSubValues()

void PropertyXLink::setSubValues  | ( | std::vector< std::string > && | _SubList_ ,   
---|---|---|---  
|  | std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > && | _ShadowSubList_ = `{}`  
| ) | |   
  
References
[App::PropertyLinkBase::checkLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[updateElementReference()](../../d2/de2/classApp_1_1PropertyXLink.html#a94e60fa4261d661b629b5c0d35215dff).

Referenced by
[setSubName()](../../d2/de2/classApp_1_1PropertyXLink.html#a576472096f84a71a74169e29ac6eb41b),
and
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10).

## ◆ setSyncSubObject()

void PropertyXLink::setSyncSubObject  | ( | [bool](../../d9/db9/classbool.html) | _enable_| ) |   
---|---|---|---|---|---  
  
References
[App::PropertyLinkBase::LinkSyncSubObject](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fab29bedf78f3fa832237ffa3a544e88c8).

## ◆ setValue() [1/5]

| void PropertyXLink::setValue  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _lValue_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Sets the property.

Reimplemented from
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1).

References
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7).

Referenced by
[adjustLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a33bbd1956612a56e1967fdd7d6c533ff),
[Paste()](../../d2/de2/classApp_1_1PropertyXLink.html#a6d593eed6217cccfdad4a79a4c752c27),
[Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[setPyObject()](../../d2/de2/classApp_1_1PropertyXLink.html#adb26821a0a3916e6252bc6b4f0c5637e),
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7),
and
[App::PropertyXLinkSub::upgrade()](../../d4/da0/classApp_1_1PropertyXLinkSub.html#a0f3a85600e83e0f36d654f72939d9add).

## ◆ setValue() [2/5]

void PropertyXLink::setValue  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _lValue_ ,   
---|---|---|---  
|  | const char *  | _subname_  
| ) | |   
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7).

## ◆ setValue() [3/5]

void PropertyXLink::setValue  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _link_ ,   
---|---|---|---  
|  | const std::vector< std::string > & | _SubList_ ,   
|  | std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > && | _ShadowSubList_ = `{}`  
| ) | |   
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7).

## ◆ setValue() [4/5]

void PropertyXLink::setValue  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _lValue_ ,   
---|---|---|---  
|  | std::vector< std::string > && | _SubList_ ,   
|  | std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > && | _ShadowSubList_ = `{}`  
| ) | |   
  
References
[aboutToSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57),
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031),
[filePath](../../d2/de2/classApp_1_1PropertyXLink.html#a1d8a3774745a9c560df18df4d3871bb4),
[App::DocInfo::get()](../../d7/d23/classApp_1_1DocInfo.html#aaa708c0148a14d954611470e84dbaa5a),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::Document::getFileName()](../../d8/d3e/classApp_1_1Document.html#a6710d0e8dbf515ba6f04a0f6be31c21d),
[App::Document::getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[hasSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[App::PropertyLinkBase::LinkDetached](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5facbc01e4b149e5b3049e9916b0181a7da),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[objectName](../../d2/de2/classApp_1_1PropertyXLink.html#a92ddffaf513f7a5d9eecc05df6c42e40),
[App::PropertyLinkBase::setFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f),
[setSubValues()](../../d2/de2/classApp_1_1PropertyXLink.html#ab317a05477f1ee776d1c4f765b70b1cd),
[stamp](../../d2/de2/classApp_1_1PropertyXLink.html#ab28b1f882f83732430330601752406fe),
and
[unlink()](../../d2/de2/classApp_1_1PropertyXLink.html#a112a0063bb96d28de578e871764a267e).

## ◆ setValue() [5/5]

void PropertyXLink::setValue  | ( | std::string && | _filePath_ ,   
---|---|---|---  
|  | std::string && | _objectName_ ,   
|  | std::vector< std::string > && | _SubList_ ,   
|  | std::vector< [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) > && | _ShadowSubList_ = `{}`  
| ) | |   
  
References
[aboutToSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57),
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031),
[filePath](../../d2/de2/classApp_1_1PropertyXLink.html#a1d8a3774745a9c560df18df4d3871bb4),
[App::DocInfo::get()](../../d7/d23/classApp_1_1DocInfo.html#aaa708c0148a14d954611470e84dbaa5a),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::Document::getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
[hasSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a),
[App::Hidden](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a7acdf85c69cc3c5305456a293524386e),
[App::PropertyLinkBase::LinkDetached](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5facbc01e4b149e5b3049e9916b0181a7da),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[objectName](../../d2/de2/classApp_1_1PropertyXLink.html#a92ddffaf513f7a5d9eecc05df6c42e40),
[App::PropertyLinkBase::setFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f),
[setSubValues()](../../d2/de2/classApp_1_1PropertyXLink.html#ab317a05477f1ee776d1c4f765b70b1cd),
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a47de90d490d26c6ae3a5d051f69967a7),
[stamp](../../d2/de2/classApp_1_1PropertyXLink.html#ab28b1f882f83732430330601752406fe),
and
[unlink()](../../d2/de2/classApp_1_1PropertyXLink.html#a112a0063bb96d28de578e871764a267e).

## ◆ supportXLink()

| [bool](../../d9/db9/classbool.html) PropertyXLink::supportXLink  | ( | const [App::Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
static  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
and
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127).

Referenced by
[Gui::Dialog::DlgPropertyLink::init()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#a0f9c31263c267be5f9d378e4f49cfa8a).

## ◆ unlink()

| void PropertyXLink::unlink  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[docInfo](../../d2/de2/classApp_1_1PropertyXLink.html#af019bff7e98d2778ec5d031af046e031),
[objectName](../../d2/de2/classApp_1_1PropertyXLink.html#a92ddffaf513f7a5d9eecc05df6c42e40),
and
[App::PropertyLink::resetLink()](../../d4/d77/classApp_1_1PropertyLink.html#a0461c85fa8e082a75df6e848f94d8c39).

Referenced by
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10),
and
[~PropertyXLink()](../../d2/de2/classApp_1_1PropertyXLink.html#ae8daad6014c712dc6527596d60db8c49).

## ◆ updateElementReference()

| void PropertyXLink::updateElementReference  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _feature_ ,   
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
[hasSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a),
and
[femsolver.signal::notify()](../../dc/de2/group__FEM.html#ga6389100f2d948a9fe194b395ac11f82c).

Referenced by
[detach()](../../d2/de2/classApp_1_1PropertyXLink.html#a46ab216473399ea97b072f5926911380),
[restoreLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a232e8182760d7ae2717d555416e4b4ce),
and
[setSubValues()](../../d2/de2/classApp_1_1PropertyXLink.html#ab317a05477f1ee776d1c4f765b70b1cd).

## ◆ upgrade()

| [bool](../../d9/db9/classbool.html) PropertyXLink::upgrade  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_ ,   
---|---|---|---  
|  | const char *  | _typeName_  
| ) | |   
virtual  
  
Reimplemented in
[App::PropertyXLinkSub](../../d4/da0/classApp_1_1PropertyXLinkSub.html#a0f3a85600e83e0f36d654f72939d9add).

References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Property::getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a),
and
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4).

Referenced by
[App::PropertyXLinkSub::upgrade()](../../d4/da0/classApp_1_1PropertyXLinkSub.html#a0f3a85600e83e0f36d654f72939d9add).

## Friends And Related Function Documentation

## ◆ DocInfo

| [friend](../../d7/d23/classfriend.html) class
[DocInfo](../../d7/d23/classApp_1_1DocInfo.html)  
---  
friend  
  
## ◆ PropertyXLinkSubList

| [friend](../../d7/d23/classfriend.html) class
[PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html)  
---  
friend  
  
## Member Data Documentation

## ◆ docInfo

|
[DocInfoPtr](../../dd/dc2/namespaceApp.html#a1752a0f247a3d9b40c49fb0d930114d5)
App::PropertyXLink::docInfo  
---  
protected  
  
Referenced by
[checkRestore()](../../d2/de2/classApp_1_1PropertyXLink.html#aff57f99ddc399ce82d8f17da884a1052),
[copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c),
[detach()](../../d2/de2/classApp_1_1PropertyXLink.html#a46ab216473399ea97b072f5926911380),
[getDocument()](../../d2/de2/classApp_1_1PropertyXLink.html#a60e7fe76c5724b6cd312b8285debcde2),
[getDocumentPath()](../../d2/de2/classApp_1_1PropertyXLink.html#a5660c90a2bc17861c700704fba7cefad),
[restoreLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a232e8182760d7ae2717d555416e4b4ce),
[Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[setAllowPartial()](../../d2/de2/classApp_1_1PropertyXLink.html#af69aa75e548072c713a0b180cadab17e),
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10),
and
[unlink()](../../d2/de2/classApp_1_1PropertyXLink.html#a112a0063bb96d28de578e871764a267e).

## ◆ docName

| std::string App::PropertyXLink::docName  
---  
protected  
  
Referenced by
[copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c).

## ◆ filePath

| std::string App::PropertyXLink::filePath  
---  
protected  
  
Referenced by
[checkRestore()](../../d2/de2/classApp_1_1PropertyXLink.html#aff57f99ddc399ce82d8f17da884a1052),
[copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c),
[getDocumentPath()](../../d2/de2/classApp_1_1PropertyXLink.html#a5660c90a2bc17861c700704fba7cefad),
[Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[setAllowPartial()](../../d2/de2/classApp_1_1PropertyXLink.html#af69aa75e548072c713a0b180cadab17e),
and
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10).

## ◆ objectName

| std::string App::PropertyXLink::objectName  
---  
protected  
  
Referenced by
[checkRestore()](../../d2/de2/classApp_1_1PropertyXLink.html#aff57f99ddc399ce82d8f17da884a1052),
[copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c),
[getObjectName()](../../d2/de2/classApp_1_1PropertyXLink.html#a22c29a4b6e7481845ef68a86832d189b),
[Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[setAllowPartial()](../../d2/de2/classApp_1_1PropertyXLink.html#af69aa75e548072c713a0b180cadab17e),
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10),
and
[unlink()](../../d2/de2/classApp_1_1PropertyXLink.html#a112a0063bb96d28de578e871764a267e).

## ◆ parentProp

| [PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)*
App::PropertyXLink::parentProp  
---  
protected  
  
Referenced by
[aboutToSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#ac8bf30f84126a4cb9b575aca74573a57),
and
[hasSetValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a005b7fbba77642fecc45a00730c66b0a).

## ◆ stamp

| std::string App::PropertyXLink::stamp  
---  
protected  
  
Referenced by
[checkRestore()](../../d2/de2/classApp_1_1PropertyXLink.html#aff57f99ddc399ce82d8f17da884a1052),
[Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[restoreLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a232e8182760d7ae2717d555416e4b4ce),
and
[setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyLinks.h
  * FreeCAD/src/App/PropertyLinks.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

