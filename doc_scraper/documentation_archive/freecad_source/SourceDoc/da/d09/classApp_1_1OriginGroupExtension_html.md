---
url: https://freecad.github.io/SourceDoc/da/d09/classApp_1_1OriginGroupExtension.html
scraped_at: 2025-09-08T14:55:21.692866
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html)

[List of all members](../../d0/dda/classApp_1_1OriginGroupExtension-members.html) | Public Member Functions | Static Public Member Functions | Public Attributes | Protected Member Functions

App::OriginGroupExtension Class Reference

Represents an abstract placeable group of objects with an associated
[Origin](../../d9/d8b/classApp_1_1Origin.html "Base class of all geometric
document objects.").
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#details)

`#include <OriginGroupExtension.h>`

##  Public Member Functions  
  
---  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [addObjects](../../da/d09/classApp_1_1OriginGroupExtension.html#ac875c27af27eb9f1bf001ee92aa51e5d) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj) override  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObject](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const override  
| Get the sub object by name.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11)  
  
virtual short | [extensionMustExecute](../../da/d09/classApp_1_1OriginGroupExtension.html#ad2e1bce76ecdcd255084312b108a9bf5) () override  
| Returns true on changing
[OriginFeature](../../da/dfe/classApp_1_1OriginFeature.html "Plane Object Used
to define planar support for all kind of operations in the document space.")
set.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#ad2e1bce76ecdcd255084312b108a9bf5)  
  
virtual void | [extensionOnChanged](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42) (const [Property](../../d0/da9/classApp_1_1Property.html) *p) override  
[App::Origin](../../d9/d8b/classApp_1_1Origin.html) * | [getOrigin](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2) () const  
| Returns the origin link or throws an exception.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2)  
  
virtual const char * | [getViewProviderName](../../da/d09/classApp_1_1OriginGroupExtension.html#adf1af86f75a6cee95a3976bd4dac91db) () const  
| returns the type name of the ViewProvider
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#adf1af86f75a6cee95a3976bd4dac91db)  
  
virtual [bool](../../d9/db9/classbool.html) | [hasObject](../../da/d09/classApp_1_1OriginGroupExtension.html#af5c6fb37f5c5c0461b41667428f62ba3) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) recursive=false) const override  
| Checks whether the object _obj_ is part of this group.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#af5c6fb37f5c5c0461b41667428f62ba3)  
  
|
[OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a831ac058ccd79dedfbbe9d351fb477a5)
()  
void | [relinkToOrigin](../../da/d09/classApp_1_1OriginGroupExtension.html#af4330ed14ea93ff3cbf7d0f952cf5e49) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
virtual | [~OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a16abb8dcc64ed4de348090f5d9ed1882) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html)  
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
static [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getGroupOfObject](../../da/d09/classApp_1_1OriginGroupExtension.html#aefe03f3ec93fce064aeca10ea5593d1b) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Returns the origin group which contains this object.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#aefe03f3ec93fce064aeca10ea5593d1b)  
  
![-](../../closed.png) Static Public Member Functions inherited from
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html)  
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
  
  
##  Public Attributes  
  
---  
[PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html) | [Origin](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cb9a227750a0219f781a9e0c2dc4cb7)  
| [Origin](../../d9/d8b/classApp_1_1Origin.html "Base class of all geometric
document objects.") linked to the group.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cb9a227750a0219f781a9e0c2dc4cb7)  
  
![-](../../closed.png) Public Attributes inherited from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html)  
[PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html) | [Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb)  
| Properties.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb)  
  
  
##  Protected Member Functions  
  
---  
virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [extensionExecute](../../da/d09/classApp_1_1OriginGroupExtension.html#ae02f4d3ece4b2ce9710f93692832a4c3) () override  
| Checks integrity of the [Origin](../../d9/d8b/classApp_1_1Origin.html "Base
class of all geometric document objects.").
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#ae02f4d3ece4b2ce9710f93692832a4c3)  
  
virtual void | [onExtendedSetupObject](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cbdf0475e8306ed1f6fab7bb2a071cb) () override  
| Creates the corresponding [Origin](../../d9/d8b/classApp_1_1Origin.html
"Base class of all geometric document objects.") object.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cbdf0475e8306ed1f6fab7bb2a071cb)  
  
virtual void | [onExtendedUnsetupObject](../../da/d09/classApp_1_1OriginGroupExtension.html#a7d908f67bb05fe69e9c30add43aeae27) () override  
| Removes all planes and axis if they are still linked to the document.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#a7d908f67bb05fe69e9c30add43aeae27)  
  
![-](../../closed.png) Protected Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
void | [initExtensionType](../../d8/dc7/classApp_1_1Extension.html#a12ec705423cb1952b395a4d135f2f734) ([Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html))  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Protected Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
static void | [initExtensionSubclass](../../d8/dc7/classApp_1_1Extension.html#ad89245f6dbe32a71396c452ea8148ce7) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Base::Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Protected Attributes inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
[bool](../../d9/db9/classbool.html) | [m_isPythonExtension](../../d8/dc7/classApp_1_1Extension.html#aed35b8360543786d3d1ce3437234d706) = false  
Py::SmartPtr | [ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3)  
  
## Detailed Description

Represents an abstract placeable group of objects with an associated
[Origin](../../d9/d8b/classApp_1_1Origin.html "Base class of all geometric
document objects.").

## Constructor & Destructor Documentation

## ◆ OriginGroupExtension()

OriginGroupExtension::OriginGroupExtension  | ( | | ) |   
---|---|---|---|---  
  
References
[App::Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6).

## ◆ ~OriginGroupExtension()

| OriginGroupExtension::~OriginGroupExtension  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ addObjects()

| std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > OriginGroupExtension::addObjects  | ( | std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | _obj_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d).

References
[App::GeoFeatureGroupExtension::addObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d),
and
[relinkToOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#af4330ed14ea93ff3cbf7d0f952cf5e49).

## ◆ extensionExecute()

| [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * OriginGroupExtension::extensionExecute  | ( | void  | | ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
Checks integrity of the [Origin](../../d9/d8b/classApp_1_1Origin.html "Base
class of all geometric document objects.").

Reimplemented from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a9b7579e56fb5b01cb0475a982541ff07).

References
[App::GroupExtension::extensionExecute()](../../da/d3a/classApp_1_1GroupExtension.html#a9b7579e56fb5b01cb0475a982541ff07),
[getOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2),
and
[Base::Exception::what()](../../d8/df7/classBase_1_1Exception.html#aa330aa854000f17a93919417d977bcac).

## ◆ extensionGetSubObject()

| [bool](../../d9/db9/classbool.html) OriginGroupExtension::extensionGetSubObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _ret_ ,   
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
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40).

References
[App::GeoFeatureGroupExtension::extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6),
[App::PropertyPlacement::getValue()](../../da/d51/classApp_1_1PropertyPlacement.html#a430fb2b0baee33f2967118bbbc7e6d74),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[App::DocumentObject::Label](../../d2/de4/classApp_1_1DocumentObject.html#a7259f450fea1a74073e626115d46110d),
[App::GeoFeatureGroupExtension::placement()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a4cd1b76960dc22c7a5d5775c54ba76fb),
and
[Base::Placement::toMatrix()](../../d1/d10/classBase_1_1Placement.html#a17b561d4e993495387875c0aed589c4e).

## ◆ extensionMustExecute()

| short OriginGroupExtension::extensionMustExecute  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
Returns true on changing
[OriginFeature](../../da/dfe/classApp_1_1OriginFeature.html "Plane Object Used
to define planar support for all kind of operations in the document space.")
set.

Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af09cb831d7b6ba0300042f83af2f2ec6).

References
[App::DocumentObjectExtension::extensionMustExecute()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af09cb831d7b6ba0300042f83af2f2ec6),
and
[App::DocumentObject::isTouched()](../../d2/de4/classApp_1_1DocumentObject.html#a6cda42dc4ffac025c03f0953cedc32c7).

## ◆ extensionOnChanged()

| void OriginGroupExtension::extensionOnChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _p_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487).

References
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::GeoFeatureGroupExtension::extensionOnChanged()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
[App::DocumentObject::getFullName()](../../d2/de4/classApp_1_1DocumentObject.html#ab9ad25e711d56a5d6c8ba0f7638a8a62),
[App::DocumentObject::getInList()](../../d2/de4/classApp_1_1DocumentObject.html#a40180ed535a541b857baead4eece53f5),
[App::Document::Importing](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3fcdf22c3e8c2aea788606a837c7d522),
[App::Document::Restoring](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3ad0fd87f9bec83cb5d1b8096b3b09ec),
and
[App::Document::testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87).

## ◆ getGroupOfObject()

| [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * OriginGroupExtension::getGroupOfObject  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
static  
  
Returns the origin group which contains this object.

In case this object is not part of any geoFeatureGroup, 0 is returned.

Parameters

     obj| the object to search for   
---|---  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[getGroupOfObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#aefe03f3ec93fce064aeca10ea5593d1b),
and
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127).

Referenced by
[App::GeoFeatureGroupExtension::getGroupOfObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13),
and
[getGroupOfObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#aefe03f3ec93fce064aeca10ea5593d1b).

## ◆ getOrigin()

[App::Origin](../../d9/d8b/classApp_1_1Origin.html) * OriginGroupExtension::getOrigin  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the origin link or throws an exception.

References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
[App::DocumentObject::getFullName()](../../d2/de4/classApp_1_1DocumentObject.html#ab9ad25e711d56a5d6c8ba0f7638a8a62),
[Base::Type::getName()](../../dc/dee/classBase_1_1Type.html#a861a2f6bd2cd2c2df7846e202f0ce137),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
and
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127).

Referenced by
[extensionExecute()](../../da/d09/classApp_1_1OriginGroupExtension.html#ae02f4d3ece4b2ce9710f93692832a4c3),
[PartDesignGui::TaskRevolutionParameters::fillAxisCombo()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#ac4453a2dda324c1b0e365a7c9d0afb91),
[PartDesignGui::TaskTransformedParameters::fillAxisCombo()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#ad6ce430d06e602964cd7f12725873b88),
[PartDesignGui::TaskTransformedParameters::fillPlanesCombo()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#ac32c32a42e710f2ec1aa6f5e7f6a8d9b),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[hasObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#af5c6fb37f5c5c0461b41667428f62ba3),
[PartDesignGui::relinkToOrigin()](../../dc/d12/namespacePartDesignGui.html#a04b9ca5c57afc44a5ab6f8bc71f9a681),
[relinkToOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#af4330ed14ea93ff3cbf7d0f952cf5e49),
[PartDesignGui::TaskBoxPrimitives::TaskBoxPrimitives()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aee4936dd78a78c4d0f6fcc168d1a9c13),
[PartDesignGui::TaskRevolutionParameters::TaskRevolutionParameters()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#a5509b04d5cfc1da7d5314c4a038a01e2),
[PartDesignGui::ViewProviderBody::updateOriginDatumSize()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3c7c680a5e55c6cc695c82c8b45935c0),
[PartDesignGui::TaskBoxPrimitives::~TaskBoxPrimitives()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a999b4dee6e102f972f0c3b3bb1307d7e),
[PartDesignGui::TaskHelixParameters::~TaskHelixParameters()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#a98cb4720622cec66c85d46a27b65df3b),
[PartDesignGui::TaskLinearPatternParameters::~TaskLinearPatternParameters()](../../da/d31/classPartDesignGui_1_1TaskLinearPatternParameters.html#abd8fe23f24b1d9df85617e19073b621e),
[PartDesignGui::TaskMirroredParameters::~TaskMirroredParameters()](../../d8/d3c/classPartDesignGui_1_1TaskMirroredParameters.html#a9076e03f1dd9d1c76cf8005459c68a98),
[PartDesignGui::TaskPolarPatternParameters::~TaskPolarPatternParameters()](../../d7/d72/classPartDesignGui_1_1TaskPolarPatternParameters.html#afb1b6200d5c009f245e1f5bb4e82e79d),
and
[PartDesignGui::TaskRevolutionParameters::~TaskRevolutionParameters()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#a8599459f7437088540a4a0bcb2fbd986).

## ◆ getViewProviderName()

| virtual const char * App::OriginGroupExtension::getViewProviderName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
returns the type name of the ViewProvider

Reimplemented in
[App::Part](../../da/d8d/classApp_1_1Part.html#a11fd84ec6cafdffb21365168b44f427a),
and
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#a1bc5f1dfdd6f45caea39870264b4f6a3).

## ◆ hasObject()

| [bool](../../d9/db9/classbool.html) OriginGroupExtension::hasObject  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recursive_ = `false`  
| ) | |  const  
overridevirtual  
  
Checks whether the object _obj_ is part of this group.

Parameters

     obj| the object to check for.   
---|---  
recursive| if true check also if the obj is child of some sub group (default
is false).  
  
Reimplemented from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a).

References
[getOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2),
[App::GroupExtension::hasObject()](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a),
and
[hasObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#af5c6fb37f5c5c0461b41667428f62ba3).

Referenced by
[Part::BodyBase::findBodyOf()](../../da/dc8/classPart_1_1BodyBase.html#aa97e09a088d42e23f853450ab5b44989),
[PartDesignGui::getBodyFor()](../../dc/d12/namespacePartDesignGui.html#ae29a36dd1279be7e9c4f08b79bbbce73),
[PartDesign::Feature::getFeatureBody()](../../d7/d51/classPartDesign_1_1Feature.html#a67eefe496bd2b9b2675ea48e02aaa89e),
[PartDesign::Body::getNextSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#a0c9db11c1cca8a2a0c7247d7d3498242),
[PartDesign::Body::getPrevSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#aface61e57526fc0ce72faff92c3e0841),
[hasObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#af5c6fb37f5c5c0461b41667428f62ba3),
[PartDesign::Body::insertObject()](../../dd/db8/classPartDesign_1_1Body.html#a5cbb7aa1f902c8b111a9c9a428072c09),
[Part::BodyBase::isAfter()](../../da/dc8/classPart_1_1BodyBase.html#a9a200c47ffd7f95eb5584fd6bf54dfe3),
[PartDesignGui::Workbench::setupContextMenu()](../../d4/d0c/classPartDesignGui_1_1Workbench.html#adf13eeb6b7f53fc0ce4c900cbca9712e),
[PartDesignGui::ViewProviderBody::slotChangedObjectApp()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ac2b54ba3e85e13c4e5a63fe12dcc17bf),
and
[PartDesignGui::ViewProviderBody::slotChangedObjectGui()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ad65bd2facfeba3ad583f89bcbbb4fdb4).

## ◆ onExtendedSetupObject()

| void OriginGroupExtension::onExtendedSetupObject  | ( | | ) |   
---|---|---|---|---  
overrideprotectedvirtual  
  
Creates the corresponding [Origin](../../d9/d8b/classApp_1_1Origin.html "Base
class of all geometric document objects.") object.

Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab86867c2b2e774c2a15819ca6ef97b89).

References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
and
[App::DocumentObjectExtension::onExtendedSetupObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab86867c2b2e774c2a15819ca6ef97b89).

## ◆ onExtendedUnsetupObject()

| void OriginGroupExtension::onExtendedUnsetupObject  | ( | | ) |   
---|---|---|---|---  
overrideprotectedvirtual  
  
Removes all planes and axis if they are still linked to the document.

Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a0cf88b507c8a513d5ae2dc63a7221133).

References
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::DocumentObject::isRemoving()](../../d2/de4/classApp_1_1DocumentObject.html#a230a706690bd2effb512c36f81139ec2),
[App::DocumentObjectExtension::onExtendedUnsetupObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a0cf88b507c8a513d5ae2dc63a7221133),
and
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33).

## ◆ relinkToOrigin()

void OriginGroupExtension::relinkToOrigin  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[getOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2),
[App::Origin::getOriginFeature()](../../d9/d8b/classApp_1_1Origin.html#ac51255a58d5f06783527b973082ed634),
[App::PropertyLinkSub::getSubValues()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a0777851ecd0b74f3fd232e6c69c7cb32),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[App::OriginFeature::Role](../../da/dfe/classApp_1_1OriginFeature.html#a42ad19c5f98e9fce414e7ce0c6f4afbd),
[App::PropertyLink::setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[addObjects()](../../da/d09/classApp_1_1OriginGroupExtension.html#ac875c27af27eb9f1bf001ee92aa51e5d),
and
[PartDesign::Body::insertObject()](../../dd/db8/classPartDesign_1_1Body.html#a5cbb7aa1f902c8b111a9c9a428072c09).

## Member Data Documentation

## ◆ Origin

[PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html)
App::OriginGroupExtension::Origin  
---  
  
[Origin](../../d9/d8b/classApp_1_1Origin.html "Base class of all geometric
document objects.") linked to the group.

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/OriginGroupExtension.h
  * FreeCAD/src/App/OriginGroupExtension.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

