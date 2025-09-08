---
url: https://freecad.github.io/SourceDoc/de/df0/classApp_1_1GeoFeatureGroupExtension.html
scraped_at: 2025-09-08T14:54:51.756735
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html)

[List of all members](../../d5/d8f/classApp_1_1GeoFeatureGroupExtension-members.html) | Public Member Functions | Static Public Member Functions

App::GeoFeatureGroupExtension Class Reference

The base class for placeable group of DocumentObjects.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#details)

`#include <GeoFeatureGroupExtension.h>`

##  Public Member Functions  
  
---  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [addObjects](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj) override  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObject](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const override  
| Get the sub object by name.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40)  
  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObjects](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a049b0b8b248680cbdc858bd5e44603aa) (std::vector< std::string > &ret, [int](../../d1/da0/classint.html) reason) const override  
| Get name references of all sub objects.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a049b0b8b248680cbdc858bd5e44603aa)  
  
virtual void | [extensionOnChanged](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487) (const [Property](../../d0/da9/classApp_1_1Property.html) *p) override  
|
[GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a234c2d5269575c55406a5c8e18879772)
(void)  
| Constructor.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a234c2d5269575c55406a5c8e18879772)  
  
[Base::Placement](../../d1/d10/classBase_1_1Placement.html) | [globalGroupPlacement](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a585dae79f685156866b19a53eb93e77c) ()  
| Calculates the global placement of this group.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a585dae79f685156866b19a53eb93e77c)  
  
virtual void | [initExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a74933934579b51ddd24efdd5be7bb3ba) ([ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) *obj) override  
[PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html) & | [placement](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a4cd1b76960dc22c7a5d5775c54ba76fb) ()  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [removeObjects](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a38ac880c5d19aba50ba8726162bbe2bb) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj) override  
| Removes objects from this group.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a38ac880c5d19aba50ba8726162bbe2bb)  
  
virtual void | [transformPlacement](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#af259333fef3bdbc93a30be16d92c2953) (const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) &transform)  
| transformPlacement applies transform to placement of this shape.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#af259333fef3bdbc93a30be16d92c2953)  
  
virtual | [~GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a4129a0acf45d43fa3a4f0bf7806e14db) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html)  
|
[GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#afd7849b2e26ce7e3ba33ba850054854a)
(void)  
| Constructor.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#afd7849b2e26ce7e3ba33ba850054854a)  
  
virtual | [~GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a63e13d300db274dc5f6280a0e0c38b99) ()  
virtual [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [addObject](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea) (const char *sType, const char *pObjectName)  
| Adds an object of _sType_ with _pObjectName_ to the document this group
belongs to and append it to this group as well.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea)  
  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [addObject](../../da/d3a/classApp_1_1GroupExtension.html#a583eea19b9a0e1af43bb8aa8fdf9dbad) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [setObjects](../../da/d3a/classApp_1_1GroupExtension.html#a0466cc49b83d1a3157799150b6d299af) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj)  
virtual [bool](../../d9/db9/classbool.html) | [allowObject](../../da/d3a/classApp_1_1GroupExtension.html#a935f7c2af21dd8b1ef7e0ae74a7b9e5f) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [removeObject](../../da/d3a/classApp_1_1GroupExtension.html#a8cd07a1279068b8c8f68d2a7b477ac34) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Removes an object from this group.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a8cd07a1279068b8c8f68d2a7b477ac34)  
  
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
virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [extensionExecute](../../da/d3a/classApp_1_1GroupExtension.html#a9b7579e56fb5b01cb0475a982541ff07) (void) override  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getAllChildren](../../da/d3a/classApp_1_1GroupExtension.html#a65e76eb95d529bdfe44189441bcf1495) () const  
void | [getAllChildren](../../da/d3a/classApp_1_1GroupExtension.html#a659c18eb455814e2dbe04a79a59947f6) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, std::set< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &) const  
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
  
##  Static Public Member Functions  
  
---  
static [bool](../../d9/db9/classbool.html) | [areLinksValid](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a70b51273c4f85b5dd33399ccd08c7b8c) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Checks if the links of the given object comply with all GeoFeatureGroup
requirements, that means if normal links are only within the parent
GeoFeatureGroup.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a70b51273c4f85b5dd33399ccd08c7b8c)  
  
static std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getCSRelevantLinks](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a9c85d48c46398d16073136acabc1c621) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Collects all links that are relevant for the coordinate system, meaning all
recursive links to obj and from obj excluding expressions and stopping the
recursion at other geofeaturegroups.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a9c85d48c46398d16073136acabc1c621)  
  
static [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getGroupOfObject](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Returns the geo feature group which contains this object.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13)  
  
static void | [getInvalidLinkObjects](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a391e01ee323c3d9c25c8d74aa8271ae2) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &vec)  
static [bool](../../d9/db9/classbool.html) | [isLinkValid](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a89659fb6caa61f4cf9971b0170efcdc7) ([App::Property](../../d0/da9/classApp_1_1Property.html) *link)  
| Checks if the given link complies with all GeoFeatureGroup requirements,
that means if normal links are only within the parent GeoFeatureGroup.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a89659fb6caa61f4cf9971b0170efcdc7)  
  
static [bool](../../d9/db9/classbool.html) | [isNonGeoGroup](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a090ae4c150d40ab2679216bf0895e3d6) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Returns true if the given
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") is
[DocumentObjectGroup](../../d8/d75/classApp_1_1DocumentObjectGroup.html) but
not GeoFeatureGroup.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a090ae4c150d40ab2679216bf0895e3d6)  
  
![-](../../closed.png) Static Public Member Functions inherited from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html)  
static [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getGroupOfObject](../../da/d3a/classApp_1_1GroupExtension.html#a04dde88db0fd3983e66bcf8444a3e07b) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Returns the object group of the document which the given object _obj_ is
part of.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a04dde88db0fd3983e66bcf8444a3e07b)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Attributes inherited from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html)  
[PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html) | [Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb)  
| Properties.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb)  
  
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
  
## Detailed Description

The base class for placeable group of DocumentObjects.

It represents a local coordnate system

This class is the FreeCAD way of representing local coordinate systems. It
groups its children beneath it and transforms them all with the
GeoFeatureGroup placement. A few important properties:

  * Every child that belongs to the CS must be in the Group property. Even if a sketch is part of a pad, it must be in the Group property of the same GeoFeatureGroup as pad. This also holds for normal GroupExtensions. They can be added to a GeoFeatureGroup, but all objects that the group holds must also be added to the GeoFeatureGroup
  * Objects can be only in a single GeoFeatureGroup. It is not allowed to have a document object in multiple GeoFeatureGroups
  * PropertyLinks between different GeoFeatureGroups are forbidden. There are special link properties that allow such cross-CS links.
  * Expressions can cross GeoFeatureGroup borders 

## Constructor & Destructor Documentation

## ◆ GeoFeatureGroupExtension()

GeoFeatureGroupExtension::GeoFeatureGroupExtension  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Constructor.

## ◆ ~GeoFeatureGroupExtension()

| GeoFeatureGroupExtension::~GeoFeatureGroupExtension  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ addObjects()

| std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > GeoFeatureGroupExtension::addObjects  | ( | std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | _obj_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569).

Reimplemented in
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#ac875c27af27eb9f1bf001ee92aa51e5d).

References
[App::GroupExtension::allowObject()](../../da/d3a/classApp_1_1GroupExtension.html#a935f7c2af21dd8b1ef7e0ae74a7b9e5f),
[getCSRelevantLinks()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a9c85d48c46398d16073136acabc1c621),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
[getGroupOfObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
[App::GroupExtension::Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb),
[App::GroupExtension::hasObject()](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a),
[App::GroupExtension::removeObject()](../../da/d3a/classApp_1_1GroupExtension.html#a8cd07a1279068b8c8f68d2a7b477ac34),
and
[App::PropertyLinkList::setValues()](../../d3/d8c/classApp_1_1PropertyLinkList.html#af7e153c0a4b95bb6b79a5b2b357d5a48).

Referenced by
[App::OriginGroupExtension::addObjects()](../../da/d09/classApp_1_1OriginGroupExtension.html#ac875c27af27eb9f1bf001ee92aa51e5d),
and
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55).

## ◆ areLinksValid()

| [bool](../../d9/db9/classbool.html) GeoFeatureGroupExtension::areLinksValid  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
static  
  
Checks if the links of the given object comply with all GeoFeatureGroup
requirements, that means if normal links are only within the parent
GeoFeatureGroup.

  

References
[isLinkValid()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a89659fb6caa61f4cf9971b0170efcdc7).

## ◆ extensionGetSubObject()

| [bool](../../d9/db9/classbool.html) GeoFeatureGroupExtension::extensionGetSubObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _ret_ ,   
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
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a9f6afe4878329f62b99288df7224cec2).

Reimplemented in
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11).

References
[extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[App::PropertyLinkList::find()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a78dd87dbd5dab90eefc3762d35112139),
[App::Extension::getExtendedContainer()](../../d8/dc7/classApp_1_1Extension.html#a178c40e2783b6e2d1f75b3c04feeabcf),
[App::DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6),
[App::PropertyPlacement::getValue()](../../da/d51/classApp_1_1PropertyPlacement.html#a430fb2b0baee33f2967118bbbc7e6d74),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
[App::GroupExtension::Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb),
[App::ExtensionContainer::hasExtension()](../../d6/d76/classApp_1_1ExtensionContainer.html#adae9aba02ce19d1611f1bb3447ee936e),
[placement()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a4cd1b76960dc22c7a5d5775c54ba76fb),
and
[Base::Placement::toMatrix()](../../d1/d10/classBase_1_1Placement.html#a17b561d4e993495387875c0aed589c4e).

Referenced by
[extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
and
[App::OriginGroupExtension::extensionGetSubObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11).

## ◆ extensionGetSubObjects()

| [bool](../../d9/db9/classbool.html) GeoFeatureGroupExtension::extensionGetSubObjects  | ( | std::vector< std::string > & | _ret_ ,   
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
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a7abcd2dfce52f226f31f5996d5d360e2).

References [App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
and
[App::GroupExtension::Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb).

## ◆ extensionOnChanged()

| void GeoFeatureGroupExtension::extensionOnChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _p_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f).

Reimplemented in
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42).

References
[App::GroupExtension::extensionOnChanged()](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
[App::GroupExtension::Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb),
[App::Document::Importing](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3fcdf22c3e8c2aea788606a837c7d522),
[App::PropertyLinkList::setValues()](../../d3/d8c/classApp_1_1PropertyLinkList.html#af7e153c0a4b95bb6b79a5b2b357d5a48),
[App::Property::testStatus()](../../d0/da9/classApp_1_1Property.html#aa0757bcb7ff02f8ece1205afd8a05775),
and
[App::Property::User3](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aed76ddc4019f764ff7dbcb726007d14e).

Referenced by
[App::OriginGroupExtension::extensionOnChanged()](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42).

## ◆ getCSRelevantLinks()

| std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > GeoFeatureGroupExtension::getCSRelevantLinks  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
static  
  
Collects all links that are relevant for the coordinate system, meaning all
recursive links to obj and from obj excluding expressions and stopping the
recursion at other geofeaturegroups.

The result is the combination of CSOutList and CSInList.

References
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[addObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d),
and
[removeObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a38ac880c5d19aba50ba8726162bbe2bb).

## ◆ getGroupOfObject()

| [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * GeoFeatureGroupExtension::getGroupOfObject  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
static  
  
Returns the geo feature group which contains this object.

In case this object is not part of any geoFeatureGroup 0 is returned. Unlike
[DocumentObjectGroup::getGroupOfObject](../../da/d3a/classApp_1_1GroupExtension.html#a04dde88db0fd3983e66bcf8444a3e07b
"Returns the object group of the document which the given object obj is part
of.") searches only for GeoFeatureGroups

Parameters

     obj| the object to search for   
---|---  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
and
[App::OriginGroupExtension::getGroupOfObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#aefe03f3ec93fce064aeca10ea5593d1b).

Referenced by
[App::GroupExtension::addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
[addObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d),
[Gui::View3DInventorViewer::checkGroupOnTop()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a1d4b9b9b5d9604967758304ac274d931),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
[getInvalidLinkObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a391e01ee323c3d9c25c8d74aa8271ae2),
[App::GeoFeature::globalPlacement()](../../d7/d75/classApp_1_1GeoFeature.html#a0e704269769e5c10eca911b3e400d0ab),
and
[isLinkValid()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a89659fb6caa61f4cf9971b0170efcdc7).

## ◆ getInvalidLinkObjects()

| void GeoFeatureGroupExtension::getInvalidLinkObjects  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _vec_  
| ) | |   
static  
  
References
[App::Child](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263aa82fea383f121c803741f8de1c209734),
[getGroupOfObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13),
[App::Local](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a509820290d57f333403f490dde7316f4),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122).

## ◆ globalGroupPlacement()

[Base::Placement](../../d1/d10/classBase_1_1Placement.html) GeoFeatureGroupExtension::globalGroupPlacement  | ( | | ) |   
---|---|---|---|---  
  
Calculates the global placement of this group.

The returned placement describes the transformation from the global reference
coordinate system to the local coordinate system of this geo feature group. If
this group has a no parent GeoFeatureGroup the returned placement is the one
of this group. For multiple stacked GeoFeatureGroups the returned
[Placement](../../d7/d32/classApp_1_1Placement.html "Placement Object Handles
the repositioning of data.") is the combination of all parent placements
including the one of this group.

Returns

    [Base::Placement](../../d1/d10/classBase_1_1Placement.html "The Placement class.") The transformation from global reference system to the groups local system 

References
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705).

## ◆ initExtension()

| void GeoFeatureGroupExtension::initExtension  | ( | [ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) *  | _obj_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html#a1ae201ccac2b97ba9107151b9e507def).

References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
and
[App::Extension::initExtension()](../../d8/dc7/classApp_1_1Extension.html#a1ae201ccac2b97ba9107151b9e507def).

Referenced by
[Part::BodyBase::BodyBase()](../../da/dc8/classPart_1_1BodyBase.html#a1800d2e59c2d9be0824c0c1f0f0c525c),
and
[PartDesign::Boolean::Boolean()](../../d2/d81/classPartDesign_1_1Boolean.html#ac032e9c86b0a2605c320402f47850319).

## ◆ isLinkValid()

| [bool](../../d9/db9/classbool.html) GeoFeatureGroupExtension::isLinkValid  | ( | [App::Property](../../d0/da9/classApp_1_1Property.html) *  | _link_| ) |   
---|---|---|---|---|---  
static  
  
Checks if the given link complies with all GeoFeatureGroup requirements, that
means if normal links are only within the parent GeoFeatureGroup.

  

References
[App::Child](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263aa82fea383f121c803741f8de1c209734),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[getGroupOfObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
and
[App::Local](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a509820290d57f333403f490dde7316f4).

Referenced by
[areLinksValid()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a70b51273c4f85b5dd33399ccd08c7b8c).

## ◆ isNonGeoGroup()

| static [bool](../../d9/db9/classbool.html) App::GeoFeatureGroupExtension::isNonGeoGroup  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
static  
  
Returns true if the given
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") is
[DocumentObjectGroup](../../d8/d75/classApp_1_1DocumentObjectGroup.html) but
not GeoFeatureGroup.

## ◆ placement()

[PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html) & GeoFeatureGroupExtension::placement  | ( | | ) |   
---|---|---|---|---  
  
References
[App::Extension::getExtendedContainer()](../../d8/dc7/classApp_1_1Extension.html#a178c40e2783b6e2d1f75b3c04feeabcf).

Referenced by
[extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[App::OriginGroupExtension::extensionGetSubObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11),
[transformPlacement()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#af259333fef3bdbc93a30be16d92c2953),
and
[draftguitools.gui_trimex.Trimex::trimObject()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a5e72e325ef0a53c3fde6c75c2eb56ba6).

## ◆ removeObjects()

| std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > GeoFeatureGroupExtension::removeObjects  | ( | std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | _obj_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Removes objects from this group.

Returns all objects that have been removed.

Reimplemented from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#aa991d1bc084e4918a5ab22257c0fa676).

References
[getCSRelevantLinks()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a9c85d48c46398d16073136acabc1c621),
[App::PropertyListsT< T, ListT, ParentT
>::getValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#a898c6f9fa999bd667a50817d2b5f5938),
[App::GroupExtension::Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb),
and
[App::PropertyLinkList::setValues()](../../d3/d8c/classApp_1_1PropertyLinkList.html#af7e153c0a4b95bb6b79a5b2b357d5a48).

## ◆ transformPlacement()

| void GeoFeatureGroupExtension::transformPlacement  | ( | const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) & | _transform_| ) |   
---|---|---|---|---|---  
virtual  
  
transformPlacement applies transform to placement of this shape.

Override this function to propagate the change of placement to base features.

Parameters

     transform| (input).   
---|---  
  
References
[App::PropertyPlacement::getValue()](../../da/d51/classApp_1_1PropertyPlacement.html#a430fb2b0baee33f2967118bbbc7e6d74),
[placement()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a4cd1b76960dc22c7a5d5775c54ba76fb),
and
[App::PropertyPlacement::setValue()](../../da/d51/classApp_1_1PropertyPlacement.html#abb1f46e80061be4669b0ca20c83a7b31).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/GeoFeatureGroupExtension.h
  * FreeCAD/src/App/GeoFeatureGroupExtension.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

