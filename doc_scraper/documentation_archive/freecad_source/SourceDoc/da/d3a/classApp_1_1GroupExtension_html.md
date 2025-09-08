---
url: https://freecad.github.io/SourceDoc/da/d3a/classApp_1_1GroupExtension.html
scraped_at: 2025-09-08T14:54:52.584485
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html)

[List of all members](../../d3/d21/classApp_1_1GroupExtension-members.html) | Public Member Functions

App::GroupExtension Class Reference

`#include <GroupExtension.h>`

##  Public Member Functions  
  
---  
|
[GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#afd7849b2e26ce7e3ba33ba850054854a)
(void)  
| Constructor.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#afd7849b2e26ce7e3ba33ba850054854a)  
  
virtual | [~GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a63e13d300db274dc5f6280a0e0c38b99) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html)  
|
[DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a6166756be21e41923ff0cf27ca4cb13d)
()  
virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [extensionExecute](../../d4/d81/classApp_1_1DocumentObjectExtension.html#aa8a99ad96497244412b31eb8cfd4079e) ()  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetLinkedObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab6fc58714d6b5b2ecaa09f7ff6cc005f) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, [bool](../../d9/db9/classbool.html) recursive, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const  
| Get the linked object.
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab6fc58714d6b5b2ecaa09f7ff6cc005f)  
  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ae3b4c124bec333326bb9b0f0ad9600a7) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const  
| Get the sub object by name.
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ae3b4c124bec333326bb9b0f0ad9600a7)  
  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObjects](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2427868f8594561b0bd0b246b8938dd9) (std::vector< std::string > &ret, [int](../../d1/da0/classint.html) reason) const  
| Get name references of all sub objects.
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2427868f8594561b0bd0b246b8938dd9)  
  
virtual [bool](../../d9/db9/classbool.html) | [extensionHasChildElement](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a7ab4deac14dc40ce2e2675516baf156c) () const  
virtual [int](../../d1/da0/classint.html) | [extensionIsElementVisible](../../d4/d81/classApp_1_1DocumentObjectExtension.html#adab10ac2801e93d6efde2c3d8cbc97db) (const char *)  
virtual short | [extensionMustExecute](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af09cb831d7b6ba0300042f83af2f2ec6) ()  
virtual [int](../../d1/da0/classint.html) | [extensionSetElementVisible](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a59f60f1750805a02264f996c78967eae) (const char *, [bool](../../d9/db9/classbool.html))  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getExtendedObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705) ()  
const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getExtendedObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af6e17e520cf9b556992786cb5d57e911) () const  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getExtensionPyObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a254f58c97024cd7e86fec56544fb77b1) () override  
virtual const char * | [getViewProviderExtensionName](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ad1f73fbadf4f1160c349488b328ae128) () const  
| returns the type name of the ViewProviderExtension which is automatically
attached to the viewprovider object when it is initiated
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ad1f73fbadf4f1160c349488b328ae128)  
  
virtual void | [onExtendedDocumentRestored](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af01de2fab2226a8e3e88dd1db479c3a8) ()  
| get called after a document has been fully restored
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af01de2fab2226a8e3e88dd1db479c3a8)  
  
virtual void | [onExtendedSettingDocument](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ad4ad4158178cd5cf9c7d3786d21dcf15) ()  
| get called after setting the document
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ad4ad4158178cd5cf9c7d3786d21dcf15)  
  
virtual void | [onExtendedSetupObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab86867c2b2e774c2a15819ca6ef97b89) ()  
| get called after a brand new object was created
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab86867c2b2e774c2a15819ca6ef97b89)  
  
virtual void | [onExtendedUnsetupObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a0cf88b507c8a513d5ae2dc63a7221133) ()  
| get called when object is going to be removed from the document
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a0cf88b507c8a513d5ae2dc63a7221133)  
  
virtual | [~DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a0157751167592aa320110ad2d85fbf66) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
|
[Extension](../../d8/dc7/classApp_1_1Extension.html#add927117e09bb09a0d83e3cd3439a15d)
()  
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) * | [getExtendedContainer](../../d8/dc7/classApp_1_1Extension.html#a178c40e2783b6e2d1f75b3c04feeabcf) ()  
const [App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) * | [getExtendedContainer](../../d8/dc7/classApp_1_1Extension.html#a565ab575fe6be7b373b0b933885268d4) () const  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getExtensionPyObject](../../d8/dc7/classApp_1_1Extension.html#a77ffed10ef0c284b3a702caf46570168) ()  
virtual void | [initExtension](../../d8/dc7/classApp_1_1Extension.html#a1ae201ccac2b97ba9107151b9e507def) ([App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) *obj)  
[bool](../../d9/db9/classbool.html) | [isPythonExtension](../../d8/dc7/classApp_1_1Extension.html#ad4a437742b2739a79a657255b2c19321) ()  
std::string | [name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016) () const  
virtual | [~Extension](../../d8/dc7/classApp_1_1Extension.html#a52c2b4e48fa3f78511b72d55fefcb48c) ()  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [extensionGetPropertyByName](../../d8/dc7/classApp_1_1Extension.html#ade0ea67a01018f91ef56838a3a557156) (const char *[name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016)) const  
| find a property by its name
[More...](../../d8/dc7/classApp_1_1Extension.html#ade0ea67a01018f91ef56838a3a557156)  
  
virtual const char * | [extensionGetPropertyName](../../d8/dc7/classApp_1_1Extension.html#a670480fa1d036c8217ef4b817f2c41a6) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the name of a property
[More...](../../d8/dc7/classApp_1_1Extension.html#a670480fa1d036c8217ef4b817f2c41a6)  
  
virtual void | [extensionGetPropertyMap](../../d8/dc7/classApp_1_1Extension.html#ab0787c477eac6d231ac91e912abc192a) (std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > &Map) const  
| get all properties of the class (including properties of the parent)
[More...](../../d8/dc7/classApp_1_1Extension.html#ab0787c477eac6d231ac91e912abc192a)  
  
virtual void | [extensionGetPropertyList](../../d8/dc7/classApp_1_1Extension.html#a9cc010d4ba4318211f3f6b328116d359) (std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > &List) const  
| get all properties of the class (including properties of the parent)
[More...](../../d8/dc7/classApp_1_1Extension.html#a9cc010d4ba4318211f3f6b328116d359)  
  
virtual short | [extensionGetPropertyType](../../d8/dc7/classApp_1_1Extension.html#aea49212c18ec8617c4b43a03c73dba17) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Type of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#aea49212c18ec8617c4b43a03c73dba17)  
  
virtual short | [extensionGetPropertyType](../../d8/dc7/classApp_1_1Extension.html#ab6c4d7b5439181459122280af2c138c8) (const char *[name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016)) const  
| get the Type of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#ab6c4d7b5439181459122280af2c138c8)  
  
virtual const char * | [extensionGetPropertyGroup](../../d8/dc7/classApp_1_1Extension.html#ab6c159292f4f6ed2a46ceb380177634d) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#ab6c159292f4f6ed2a46ceb380177634d)  
  
virtual const char * | [extensionGetPropertyGroup](../../d8/dc7/classApp_1_1Extension.html#a21e92d567142b377a337a901bb8943fc) (const char *[name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016)) const  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#a21e92d567142b377a337a901bb8943fc)  
  
virtual const char * | [extensionGetPropertyDocumentation](../../d8/dc7/classApp_1_1Extension.html#aa2d9bdeef59b8216c6bcb8f5d8ee53f3) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#aa2d9bdeef59b8216c6bcb8f5d8ee53f3)  
  
virtual const char * | [extensionGetPropertyDocumentation](../../d8/dc7/classApp_1_1Extension.html#a33043a15492e987791e91d16c0079be3) (const char *[name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016)) const  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#a33043a15492e987791e91d16c0079be3)  
  
virtual void | [extensionSave](../../d8/dc7/classApp_1_1Extension.html#a94c65f4a8cf93d9a149726049885aafd) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &) const  
virtual void | [extensionRestore](../../d8/dc7/classApp_1_1Extension.html#ab1a7fb60166532ef2838ee0722c5955f) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &)  
[bool](../../d9/db9/classbool.html) | [extensionIsDerivedFrom](../../d8/dc7/classApp_1_1Extension.html#ad635be48204f8f5fb9c75103cd89fb20) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
  
## Object handling <br>  
  
---  
[PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html) | [Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb)  
| Properties.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb)  
  
virtual [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [addObject](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea) (const char *sType, const char *pObjectName)  
| Adds an object of _sType_ with _pObjectName_ to the document this group
belongs to and append it to this group as well.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea)  
  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [addObject](../../da/d3a/classApp_1_1GroupExtension.html#a583eea19b9a0e1af43bb8aa8fdf9dbad) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [addObjects](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj)  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [setObjects](../../da/d3a/classApp_1_1GroupExtension.html#a0466cc49b83d1a3157799150b6d299af) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj)  
virtual [bool](../../d9/db9/classbool.html) | [allowObject](../../da/d3a/classApp_1_1GroupExtension.html#a935f7c2af21dd8b1ef7e0ae74a7b9e5f) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [removeObject](../../da/d3a/classApp_1_1GroupExtension.html#a8cd07a1279068b8c8f68d2a7b477ac34) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Removes an object from this group.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a8cd07a1279068b8c8f68d2a7b477ac34)  
  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [removeObjects](../../da/d3a/classApp_1_1GroupExtension.html#aa991d1bc084e4918a5ab22257c0fa676) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj)  
| Removes objects from this group.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#aa991d1bc084e4918a5ab22257c0fa676)  
  
virtual void | [removeObjectsFromDocument](../../da/d3a/classApp_1_1GroupExtension.html#af7405cb3abccba3302792487e514a4e1) ()  
| Removes all children objects from this group and the document.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#af7405cb3abccba3302792487e514a4e1)  
  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getObject](../../da/d3a/classApp_1_1GroupExtension.html#a334d367aa8c90d6ecf457792e37ca961) (const char *Name) const  
| Returns the object of this group with _Name_.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a334d367aa8c90d6ecf457792e37ca961)  
  
virtual [bool](../../d9/db9/classbool.html) | [hasObject](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) recursive=false) const  
| Checks whether the object _obj_ is part of this group.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a)  
  
[bool](../../d9/db9/classbool.html) | [isChildOf](../../da/d3a/classApp_1_1GroupExtension.html#ad19ccc7fc052d71da1b11e6f736ca7c3) (const [GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html) *group, [bool](../../d9/db9/classbool.html) recursive=true) const  
| Checks whether this group object is a child (or sub-child if enabled) of the
given group object.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#ad19ccc7fc052d71da1b11e6f736ca7c3)  
  
const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | [getObjects](../../da/d3a/classApp_1_1GroupExtension.html#ab7df48295e51c05fcb9eaa3ac2857938) () const  
| Returns a list of all objects this group does have.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#ab7df48295e51c05fcb9eaa3ac2857938)  
  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getObjectsOfType](../../da/d3a/classApp_1_1GroupExtension.html#a55c23aac201dfbc053a5eeaf8bd37e5f) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) &typeId) const  
| Returns a list of all objects of _typeId_ this group does have.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a55c23aac201dfbc053a5eeaf8bd37e5f)  
  
[int](../../d1/da0/classint.html) | [countObjectsOfType](../../da/d3a/classApp_1_1GroupExtension.html#a20dc1c6c322878e94281f7a7f56b4173) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) &typeId) const  
| Returns the number of objects of _typeId_ this group does have.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a20dc1c6c322878e94281f7a7f56b4173)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getExtensionPyObject](../../da/d3a/classApp_1_1GroupExtension.html#a860f82302ebbf404b14cca69adc9ff36) (void) override  
virtual void | [extensionOnChanged](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f) (const [Property](../../d0/da9/classApp_1_1Property.html) *p) override  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObject](../../da/d3a/classApp_1_1GroupExtension.html#a9f6afe4878329f62b99288df7224cec2) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const override  
| Get the sub object by name.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a9f6afe4878329f62b99288df7224cec2)  
  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObjects](../../da/d3a/classApp_1_1GroupExtension.html#a7abcd2dfce52f226f31f5996d5d360e2) (std::vector< std::string > &ret, [int](../../d1/da0/classint.html) reason) const override  
| Get name references of all sub objects.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a7abcd2dfce52f226f31f5996d5d360e2)  
  
virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [extensionExecute](../../da/d3a/classApp_1_1GroupExtension.html#a9b7579e56fb5b01cb0475a982541ff07) (void) override  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getAllChildren](../../da/d3a/classApp_1_1GroupExtension.html#a65e76eb95d529bdfe44189441bcf1495) () const  
void | [getAllChildren](../../da/d3a/classApp_1_1GroupExtension.html#a659c18eb455814e2dbe04a79a59947f6) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, std::set< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &) const  
static [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getGroupOfObject](../../da/d3a/classApp_1_1GroupExtension.html#a04dde88db0fd3983e66bcf8444a3e07b) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Returns the object group of the document which the given object _obj_ is
part of.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a04dde88db0fd3983e66bcf8444a3e07b)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Protected Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
void | [initExtensionType](../../d8/dc7/classApp_1_1Extension.html#a12ec705423cb1952b395a4d135f2f734) ([Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html))  
![-](../../closed.png) Static Protected Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
static void | [initExtensionSubclass](../../d8/dc7/classApp_1_1Extension.html#ad89245f6dbe32a71396c452ea8148ce7) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Base::Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Protected Attributes inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
[bool](../../d9/db9/classbool.html) | [m_isPythonExtension](../../d8/dc7/classApp_1_1Extension.html#aed35b8360543786d3d1ce3437234d706) = false  
Py::SmartPtr | [ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3)  
  
## Constructor & Destructor Documentation

## ◆ GroupExtension()

GroupExtension::GroupExtension  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Constructor.

References
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb),
[App::Extension::initExtensionType()](../../d8/dc7/classApp_1_1Extension.html#a12ec705423cb1952b395a4d135f2f734),
[App::Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6),
[App::Prop_None](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a32c18d11cda25e1ac1b1692aa36423e0),
and
[App::Prop_Transient](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a6eefec5f03fa1d639e7fc26c5804ccf6).

Referenced by
[PartDesign::Body::addObject()](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605).

## ◆ ~GroupExtension()

| GroupExtension::~GroupExtension  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ addObject() [1/2]

| [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * GroupExtension::addObject  | ( | const char *  | _sType_ ,   
---|---|---|---  
|  | const char *  | _pObjectName_  
| ) | |   
virtual  
  
Adds an object of _sType_ with _pObjectName_ to the document this group
belongs to and append it to this group as well.

References
[addObject()](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea),
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[allowObject()](../../da/d3a/classApp_1_1GroupExtension.html#a935f7c2af21dd8b1ef7e0ae74a7b9e5f),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
and
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33).

Referenced by
[addObject()](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea),
[addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
[ArchBuildingPart.BuildingPart::autogroup()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a45c3834ac8f02df7fc30569fc90c4285),
[ArchPanel.NestTaskPanel::getContainer()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ad25ef9b5aade32a390de4a8bd34bafda),
and
[ArchPanel.NestTaskPanel::getShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a52edae24a9d124678d48b157749b5f04).

## ◆ addObject() [2/2]

| std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > GroupExtension::addObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605).

References
[addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[ArchBuildingPart.BuildingPart::autogroup()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a45c3834ac8f02df7fc30569fc90c4285),
[ArchPanel.NestTaskPanel::getContainer()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ad25ef9b5aade32a390de4a8bd34bafda),
and
[ArchPanel.NestTaskPanel::getShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a52edae24a9d124678d48b157749b5f04).

## ◆ addObjects()

| std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > GroupExtension::addObjects  | ( | std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | _obj_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d),
and
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#ac875c27af27eb9f1bf001ee92aa51e5d).

References
[addObject()](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea),
[allowObject()](../../da/d3a/classApp_1_1GroupExtension.html#a935f7c2af21dd8b1ef7e0ae74a7b9e5f),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
[App::GeoFeatureGroupExtension::getGroupOfObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13),
[getGroupOfObject()](../../da/d3a/classApp_1_1GroupExtension.html#a04dde88db0fd3983e66bcf8444a3e07b),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb),
[hasObject()](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a),
[removeObject()](../../da/d3a/classApp_1_1GroupExtension.html#a8cd07a1279068b8c8f68d2a7b477ac34),
and
[App::PropertyLinkList::setValues()](../../d3/d8c/classApp_1_1PropertyLinkList.html#af7e153c0a4b95bb6b79a5b2b357d5a48).

Referenced by
[addObject()](../../da/d3a/classApp_1_1GroupExtension.html#a583eea19b9a0e1af43bb8aa8fdf9dbad),
and
[setObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a0466cc49b83d1a3157799150b6d299af).

## ◆ allowObject()

| virtual [bool](../../d9/db9/classbool.html) App::GroupExtension::allowObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | | ) |   
---|---|---|---|---|---  
virtual  
  
Referenced by
[addObject()](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea),
[addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
and
[App::GeoFeatureGroupExtension::addObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d).

## ◆ countObjectsOfType()

[int](../../d1/da0/classint.html) GroupExtension::countObjectsOfType  | ( | const [Base::Type](../../dc/dee/classBase_1_1Type.html) & | _typeId_| ) |  const  
---|---|---|---|---|---  
  
Returns the number of objects of _typeId_ this group does have.

References [App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
and
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb).

## ◆ extensionExecute()

| [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * GroupExtension::extensionExecute  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#aa8a99ad96497244412b31eb8cfd4079e).

Reimplemented in
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#ae02f4d3ece4b2ce9710f93692832a4c3).

References
[App::DocumentObjectExtension::extensionExecute()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#aa8a99ad96497244412b31eb8cfd4079e).

Referenced by
[App::OriginGroupExtension::extensionExecute()](../../da/d09/classApp_1_1OriginGroupExtension.html#ae02f4d3ece4b2ce9710f93692832a4c3).

## ◆ extensionGetSubObject()

| [bool](../../d9/db9/classbool.html) GroupExtension::extensionGetSubObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _ret_ ,   
---|---|---|---  
|  | const char *  | _subname_ ,   
|  | [PyObject](../../df/d1b/classPyObject.html) **  | _pyObj_ ,   
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ ,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ ,   
|  | [int](../../d1/da0/classint.html) | _depth_  
| ) | |  const  
overridevirtual  
  
Get the sub object by name.

See also

    [DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6 "Get the sub element/object by name.")

Returns

    Return turn if handled, the sub object is returned in `ret`

Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ae3b4c124bec333326bb9b0f0ad9600a7).

Reimplemented in
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
and
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11).

References
[App::PropertyLinkList::find()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a78dd87dbd5dab90eefc3762d35112139),
[App::Extension::getExtendedContainer()](../../d8/dc7/classApp_1_1Extension.html#a178c40e2783b6e2d1f75b3c04feeabcf),
[App::DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
and
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb).

## ◆ extensionGetSubObjects()

| [bool](../../d9/db9/classbool.html) GroupExtension::extensionGetSubObjects  | ( | std::vector< std::string > & | _ret_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _reason_  
| ) | |  const  
overridevirtual  
  
Get name references of all sub objects.

See also

    [DocumentObject::getSubObjects()](../../d2/de4/classApp_1_1DocumentObject.html#a43e45965f79f8e68bda39c77764b61a0 "Return name reference of all sub-objects.")

Returns

    Return turn if handled, the sub object is returned in `ret`

Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2427868f8594561b0bd0b246b8938dd9).

Reimplemented in
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a049b0b8b248680cbdc858bd5e44603aa).

References [App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
and
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb).

## ◆ extensionOnChanged()

| void GroupExtension::extensionOnChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _p_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html#a7f65954e27171964985beec0a5a21149).

Reimplemented in
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487),
and
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42).

References
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
[App::Extension::extensionOnChanged()](../../d8/dc7/classApp_1_1Extension.html#a7f65954e27171964985beec0a5a21149),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
[App::PropertyListsT< T, ListT, ParentT
>::getValue()](../../d1/d0e/classApp_1_1PropertyListsT.html#a064f87de752ea68f9a660c10ba3dcf4b),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb),
[App::PropertyLinkList::setValues()](../../d3/d8c/classApp_1_1PropertyLinkList.html#af7e153c0a4b95bb6b79a5b2b357d5a48),
[App::Property::testStatus()](../../d0/da9/classApp_1_1Property.html#aa0757bcb7ff02f8ece1205afd8a05775),
and
[App::Property::User3](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aed76ddc4019f764ff7dbcb726007d14e).

Referenced by
[App::GeoFeatureGroupExtension::extensionOnChanged()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487).

## ◆ getAllChildren() [1/2]

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > GroupExtension::getAllChildren  | ( | | ) |  const  
---|---|---|---|---  
  
References
[getAllChildren()](../../da/d3a/classApp_1_1GroupExtension.html#a65e76eb95d529bdfe44189441bcf1495).

Referenced by
[getAllChildren()](../../da/d3a/classApp_1_1GroupExtension.html#a65e76eb95d529bdfe44189441bcf1495),
and
[Mod.Show.Containers.Container::hasObject()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a616554ac02ef293148b14b0baf178282).

## ◆ getAllChildren() [2/2]

void GroupExtension::getAllChildren  | ( | std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _res_ ,   
---|---|---|---  
|  | std::set< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _rset_  
| ) | |  const  
  
References [App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
and
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb).

Referenced by
[Mod.Show.Containers.Container::hasObject()](../../db/d52/classMod_1_1Show_1_1Containers_1_1Container.html#a616554ac02ef293148b14b0baf178282).

## ◆ getExtensionPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * GroupExtension::getExtensionPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a254f58c97024cd7e86fec56544fb77b1).

References
[App::Extension::ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3).

## ◆ getGroupOfObject()

| [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * GroupExtension::getGroupOfObject  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
static  
  
Returns the object group of the document which the given object _obj_ is part
of.

In case this object is not part of a group 0 is returned.

Note

    This only returns objects that are normal groups, not any special derived type like GeoFeatureGroups or OriginGroups. To retrieve those please use their appropriate functions 

Referenced by
[PartDesign::Body::addObject()](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605),
[addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
[App::LinkBaseExtension::elementNameFromIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ab6e1b35f106202ea5678702db336a819),
[PartDesignGui::ViewProviderDatum::getRelevantBoundBox()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#ab70e87f8a87a50222337b00c4ef6d945),
and
[Gui::LinkView::setChildren()](../../da/d11/classGui_1_1LinkView.html#a4c8367560952e061e0dd7f66038088c3).

## ◆ getObject()

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * GroupExtension::getObject  | ( | const char *  | _Name_| ) |  const  
---|---|---|---|---|---  
  
Returns the object of this group with _Name_.

If the group doesn't have such an object 0 is returned.

Note

    This method might return 0 even if the document this group belongs to contains an object with this name. 

References
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
[App::Document::getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
and
[hasObject()](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a).

## ◆ getObjects()

const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & GroupExtension::getObjects  | ( | | ) |  const  
---|---|---|---|---  
  
Returns a list of all objects this group does have.

References [App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
and
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb).

## ◆ getObjectsOfType()

std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > GroupExtension::getObjectsOfType  | ( | const [Base::Type](../../dc/dee/classBase_1_1Type.html) & | _typeId_| ) |  const  
---|---|---|---|---|---  
  
Returns a list of all objects of _typeId_ this group does have.

References [App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
and
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb).

## ◆ hasObject()

| [bool](../../d9/db9/classbool.html) GroupExtension::hasObject  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recursive_ = `false`  
| ) | |  const  
virtual  
  
Checks whether the object _obj_ is part of this group.

Parameters

     obj| the object to check for.   
---|---  
recursive| if true check also if the obj is child of some sub group (default
is false).  
  
Reimplemented in
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#af5c6fb37f5c5c0461b41667428f62ba3).

References
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
and
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb).

Referenced by
[addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
[App::GeoFeatureGroupExtension::addObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d),
[getObject()](../../da/d3a/classApp_1_1GroupExtension.html#a334d367aa8c90d6ecf457792e37ca961),
and
[App::OriginGroupExtension::hasObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#af5c6fb37f5c5c0461b41667428f62ba3).

## ◆ isChildOf()

[bool](../../d9/db9/classbool.html) GroupExtension::isChildOf  | ( | const [GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html) *  | _group_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recursive_ = `true`  
| ) | |  const  
  
Checks whether this group object is a child (or sub-child if enabled) of the
given group object.

References
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705).

## ◆ removeObject()

| std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > GroupExtension::removeObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
virtual  
  
Removes an object from this group.

Returns all objects that have been removed.

References
[removeObjects()](../../da/d3a/classApp_1_1GroupExtension.html#aa991d1bc084e4918a5ab22257c0fa676),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
and
[App::GeoFeatureGroupExtension::addObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d).

## ◆ removeObjects()

| std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > GroupExtension::removeObjects  | ( | std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | _obj_| ) |   
---|---|---|---|---|---  
virtual  
  
Removes objects from this group.

Returns all objects that have been removed.

Reimplemented in
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a38ac880c5d19aba50ba8726162bbe2bb).

References [App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb),
and
[App::PropertyLinkList::setValues()](../../d3/d8c/classApp_1_1PropertyLinkList.html#af7e153c0a4b95bb6b79a5b2b357d5a48).

Referenced by
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
and
[removeObject()](../../da/d3a/classApp_1_1GroupExtension.html#a8cd07a1279068b8c8f68d2a7b477ac34).

## ◆ removeObjectsFromDocument()

| void GroupExtension::removeObjectsFromDocument  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Removes all children objects from this group and the document.

References [App::PropertyListsT< T, ListT, ParentT
>::getSize()](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
and
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb).

## ◆ setObjects()

| std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > GroupExtension::setObjects  | ( | std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | _obj_| ) |   
---|---|---|---|---|---  
virtual  
  
References
[addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
[Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb),
and
[App::PropertyLinkList::setValues()](../../d3/d8c/classApp_1_1PropertyLinkList.html#af7e153c0a4b95bb6b79a5b2b357d5a48).

Referenced by
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55).

## Member Data Documentation

## ◆ Group

[PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html) App::GroupExtension::Group  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Properties.

Referenced by
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[PartDesign::Body::addObject()](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605),
[addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
[App::GeoFeatureGroupExtension::addObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d),
[countObjectsOfType()](../../da/d3a/classApp_1_1GroupExtension.html#a20dc1c6c322878e94281f7a7f56b4173),
[PartDesignGui::ViewProviderBody::dropObject()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3e245daa7cd5dbb26f3603f2e93f68fe),
[Drawing::FeatureClip::execute()](../../d5/d4a/classDrawing_1_1FeatureClip.html#afed75650f49849b96c65ef93795800e5),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[PartDesign::Boolean::execute()](../../d2/d81/classPartDesign_1_1Boolean.html#a471715716cd89abfe18b9f50b7728567),
[Import::ExportOCAF::exportObject()](../../d2/dda/classImport_1_1ExportOCAF.html#a44829a66a0a0a1481f0b17eb8f29331b),
[Gui::ViewProviderGeoFeatureGroupExtension::extensionClaimChildren()](../../d2/de9/classGui_1_1ViewProviderGeoFeatureGroupExtension.html#ad44762aa4bd4aa7ae5734d717c8925ed),
[App::GeoFeatureGroupExtension::extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[extensionGetSubObject()](../../da/d3a/classApp_1_1GroupExtension.html#a9f6afe4878329f62b99288df7224cec2),
[App::GeoFeatureGroupExtension::extensionGetSubObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a049b0b8b248680cbdc858bd5e44603aa),
[extensionGetSubObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a7abcd2dfce52f226f31f5996d5d360e2),
[App::GeoFeatureGroupExtension::extensionOnChanged()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487),
[extensionOnChanged()](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f),
[getAllChildren()](../../da/d3a/classApp_1_1GroupExtension.html#a659c18eb455814e2dbe04a79a59947f6),
[PartDesign::Body::getNextSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#a0c9db11c1cca8a2a0c7247d7d3498242),
[getObjects()](../../da/d3a/classApp_1_1GroupExtension.html#ab7df48295e51c05fcb9eaa3ac2857938),
[getObjectsOfType()](../../da/d3a/classApp_1_1GroupExtension.html#a55c23aac201dfbc053a5eeaf8bd37e5f),
[PartDesign::Body::getPrevSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#aface61e57526fc0ce72faff92c3e0841),
[TechDraw::ShapeExtractor::getShapes2d()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a7b6b34e0c817f34b537bdb53b36956f1),
[TechDraw::ShapeExtractor::getShapesFromObject()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4043c946e78f533e4f060cb3b87b5691),
[PartDesign::Body::getSubObject()](../../dd/db8/classPartDesign_1_1Body.html#aecc131a5ce7f03c5041a475003456b38),
[GroupExtension()](../../da/d3a/classApp_1_1GroupExtension.html#afd7849b2e26ce7e3ba33ba850054854a),
[Fem::FemAnalysis::handleChangedPropertyName()](../../de/d36/classFem_1_1FemAnalysis.html#a77d4363b7c6734ec7754d6c4de10a481),
[Part::BodyBase::handleChangedPropertyName()](../../da/dc8/classPart_1_1BodyBase.html#a2038d6fd9d31b5033c193ca7a95d0b33),
[PartDesign::Boolean::handleChangedPropertyName()](../../d2/d81/classPartDesign_1_1Boolean.html#ad635959d9d69278a1c46fbd6cc0f78f4),
[hasObject()](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a),
[PartDesign::Body::insertObject()](../../dd/db8/classPartDesign_1_1Body.html#a5cbb7aa1f902c8b111a9c9a428072c09),
[Part::BodyBase::isAfter()](../../da/dc8/classPart_1_1BodyBase.html#a9a200c47ffd7f95eb5584fd6bf54dfe3),
[PartDesign::Boolean::mustExecute()](../../d2/d81/classPartDesign_1_1Boolean.html#acc9ed4028be42a906bc3c46697efe969),
[Drawing::FeaturePage::onBeforeChange()](../../db/d0f/classDrawing_1_1FeaturePage.html#a7c55c251b8fe8c83f98a5e0defb88070),
[Drawing::FeaturePage::onChanged()](../../db/d0f/classDrawing_1_1FeaturePage.html#a9c6b6897f29ff589163044d51b7e5c04),
[PartDesign::Body::onChanged()](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[PartDesignGui::ViewProvider::onChanged()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a257ca77e2256cbd8df847cedc5892289),
[PartDesignGui::ViewProviderBoolean::onDelete()](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#aabf46492095e0512b7b9ef7b475f8228),
[PartDesign::Body::onDocumentRestored()](../../dd/db8/classPartDesign_1_1Body.html#aa6affc475d3884d9570838e731749605),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[PartDesign::Body::removeObject()](../../dd/db8/classPartDesign_1_1Body.html#a207956cf2a361690d971c7e604fc8bf1),
[removeObjects()](../../da/d3a/classApp_1_1GroupExtension.html#aa991d1bc084e4918a5ab22257c0fa676),
[App::GeoFeatureGroupExtension::removeObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a38ac880c5d19aba50ba8726162bbe2bb),
[removeObjectsFromDocument()](../../da/d3a/classApp_1_1GroupExtension.html#af7405cb3abccba3302792487e514a4e1),
[setObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a0466cc49b83d1a3157799150b6d299af),
[PartDesignGui::ViewProviderBody::setVisualBodyMode()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a50b3de515b84c2e3e19b840ef5fc8187),
[PartDesignGui::TaskBooleanParameters::TaskBooleanParameters()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#afee7fbe402fa60d00581ce385bc8cb3c),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[PartDesignGui::ViewProviderBody::unifyVisualProperty()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a9622d1e6a23c6497bea610755aea5713),
and
[PartDesignGui::ViewProviderBody::updateData()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a2a541fb893a7130314f3c7161c33477e).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/GroupExtension.h
  * FreeCAD/src/App/GroupExtension.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

