---
url: https://freecad.github.io/SourceDoc/d6/d45/classApp_1_1LinkExtension.html
scraped_at: 2025-09-08T14:55:00.585971
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [LinkExtension](../../d6/d45/classApp_1_1LinkExtension.html)

[List of all members](../../d9/d96/classApp_1_1LinkExtension-members.html) | Public Member Functions

App::LinkExtension Class Reference

`#include <Link.h>`

##  Public Member Functions  
  
---  
|
[LinkExtension](../../d6/d45/classApp_1_1LinkExtension.html#a7596c73b0b1c524c5df86e10f4725ba8)
()  
virtual | [~LinkExtension](../../d6/d45/classApp_1_1LinkExtension.html#a7e9809d9944b9888f8c73def3e7bfa1f) ()  
Helpers for defining extended parameter  
extended parameter definition (Name, Type, Property_Type, Default,
[Document](../../d8/d3e/classApp_1_1Document.html "The document class."),
Property_Name, Derived_Property_Type, App_Property_Type, Group) This helper
simply reuses Name as Property_Name, Property_Type as Derived_Property_type,
Prop_None as App_Propert_Type Note: Because PropertyView will merge linked
object's properties into ours, we set the default group name as '
[Link](../../df/d9b/classApp_1_1Link.html)' with a leading space to try to
make our group before others  
void | [onExtendedDocumentRestored](../../d6/d45/classApp_1_1LinkExtension.html#abf7e1de9b6ffa356efe37a1b6e04e66f) () override  
| get called after a document has been fully restored
[More...](../../d6/d45/classApp_1_1LinkExtension.html#abf7e1de9b6ffa356efe37a1b6e04e66f)  
  
![-](../../closed.png) Public Member Functions inherited from
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html)  
|
[LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#acb03b8359e3c3e0391973dcf74f840ae)
()  
virtual | [~LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#a7eced285bdf5596f8d8a365af89495d1) ()  
virtual void | [setProperty](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770) ([int](../../d1/da0/classint.html) idx, [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
[Property](../../d0/da9/classApp_1_1Property.html) * | [getProperty](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1bd7ade30a2e3669a12939c330352967) ([int](../../d1/da0/classint.html) idx)  
[Property](../../d0/da9/classApp_1_1Property.html) * | [getProperty](../../da/dd9/classApp_1_1LinkBaseExtension.html#a128a03065fbcbd2cf57f71fcfc852e03) (const char *)  
virtual const std::vector< [PropInfo](../../d5/d5c/structApp_1_1LinkBaseExtension_1_1PropInfo.html) > & | [getPropertyInfo](../../da/dd9/classApp_1_1LinkBaseExtension.html#a8c41e710c1ae424ef1f4fef8cf99bf54) () const  
virtual const [PropInfoMap](../../da/dd9/classApp_1_1LinkBaseExtension.html#abd1b628a76cbd308ad37524ca47a9873) & | [getPropertyInfoMap](../../da/dd9/classApp_1_1LinkBaseExtension.html#af5361e9b169789363271fbd670700fbc) () const  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getLinkedChildren](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0ee53939800d341ba218c46d29afcad1) ([bool](../../d9/db9/classbool.html) filter=true) const  
const char * | [flattenSubname](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1e8f17cfe27ff1ee2968200036d5a431) (const char *subname) const  
void | [expandSubname](../../da/dd9/classApp_1_1LinkBaseExtension.html#afe70635a884db59e1d026c499bc13b8e) (std::string &subname) const  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getLink](../../da/dd9/classApp_1_1LinkBaseExtension.html#acd90ba2231bd4cb62e7fd04b09f918e1) ([int](../../d1/da0/classint.html) depth=0) const  
[Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [getTransform](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa78286a7bc1a3dfdb80c98f58726d827) ([bool](../../d9/db9/classbool.html) transform) const  
[Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) | [getScaleVector](../../da/dd9/classApp_1_1LinkBaseExtension.html#a546fb70b58ec1b41d2552d21e48f53a3) () const  
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html) * | [linkedPlainGroup](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad1a36871ddcd463c8c399b6d1ed25d02) () const  
[bool](../../d9/db9/classbool.html) | [linkTransform](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac6f97ab8d9ff54b06d63d743fcb065a6) () const  
const char * | [getSubName](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3217de1bc2559882937299e3d11a2904) () const  
const std::vector< std::string > & | [getSubElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#afff41feca4945210e21c70bd05415076) () const  
[bool](../../d9/db9/classbool.html) | [extensionGetSubObject](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj=nullptr, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat=nullptr, [bool](../../d9/db9/classbool.html) transform=false, [int](../../d1/da0/classint.html) depth=0) const override  
| Get the sub object by name.
[More...](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a)  
  
[bool](../../d9/db9/classbool.html) | [extensionGetSubObjects](../../da/dd9/classApp_1_1LinkBaseExtension.html#a666a0bbcc82f6538d3dfca95e4937ad5) (std::vector< std::string > &ret, [int](../../d1/da0/classint.html) reason) const override  
| Get name references of all sub objects.
[More...](../../da/dd9/classApp_1_1LinkBaseExtension.html#a666a0bbcc82f6538d3dfca95e4937ad5)  
  
[bool](../../d9/db9/classbool.html) | [extensionGetLinkedObject](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad62f820b24b6540c9121d0fefb5e3054) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, [bool](../../d9/db9/classbool.html) recurse, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const override  
| Get the linked object.
[More...](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad62f820b24b6540c9121d0fefb5e3054)  
  
virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [extensionExecute](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693) (void) override  
virtual short | [extensionMustExecute](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae673c0469dcbdbe20c38ec986b1a1915) (void) override  
virtual void | [extensionOnChanged](../../da/dd9/classApp_1_1LinkBaseExtension.html#acfd0dd3d0677653d2da7fc2a4cdcd3c5) (const [Property](../../d0/da9/classApp_1_1Property.html) *p) override  
virtual void | [onExtendedUnsetupObject](../../da/dd9/classApp_1_1LinkBaseExtension.html#abb164bab7e57290101417c27910f0715) () override  
| get called when object is going to be removed from the document
[More...](../../da/dd9/classApp_1_1LinkBaseExtension.html#abb164bab7e57290101417c27910f0715)  
  
virtual [int](../../d1/da0/classint.html) | [extensionSetElementVisible](../../da/dd9/classApp_1_1LinkBaseExtension.html#af0547afce075bf3860bd9afe3052a61b) (const char *, [bool](../../d9/db9/classbool.html)) override  
virtual [int](../../d1/da0/classint.html) | [extensionIsElementVisible](../../da/dd9/classApp_1_1LinkBaseExtension.html#acf07fd549eb15bb1f7a3533b2ee58925) (const char *) override  
virtual [bool](../../d9/db9/classbool.html) | [extensionHasChildElement](../../da/dd9/classApp_1_1LinkBaseExtension.html#aff055283d9be0810467d1e9540243415) () const override  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getExtensionPyObject](../../da/dd9/classApp_1_1LinkBaseExtension.html#af1063baf3790a0275959a311d0c7a93f) (void) override  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [extensionGetPropertyByName](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9673e9e742c402f3fb8c1ad6f5cdadad) (const char *[name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016)) const override  
| find a property by its name
[More...](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9673e9e742c402f3fb8c1ad6f5cdadad)  
  
[int](../../d1/da0/classint.html) | [getElementIndex](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b) (const char *subname, const char **psubname=nullptr) const  
void | [elementNameFromIndex](../../da/dd9/classApp_1_1LinkBaseExtension.html#ab6e1b35f106202ea5678702db336a819) ([int](../../d1/da0/classint.html) idx, std::ostream &ss) const  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getContainer](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017) ()  
const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getContainer](../../da/dd9/classApp_1_1LinkBaseExtension.html#a57b46869e220d668ce2184446b7d6f80) () const  
void | [setLink](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4) ([int](../../d1/da0/classint.html) index, [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const char *subname=nullptr, const std::vector< std::string > &subs=std::vector< std::string >())  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getTrueLinkedObject](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1) ([bool](../../d9/db9/classbool.html) recurse, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat=nullptr, [int](../../d1/da0/classint.html) depth=0, [bool](../../d9/db9/classbool.html) noElement=false) const  
[bool](../../d9/db9/classbool.html) | [hasPlacement](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae3b16bf34f7f25c9338406bb4708e9e7) () const  
void | [cacheChildLabel](../../da/dd9/classApp_1_1LinkBaseExtension.html#a373305ffe3887c3d2f57d04b8585e685) ([int](../../d1/da0/classint.html) enable=-1) const  
void | [syncCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4591b8c9e098285eceedfdc81e04381f) ()  
void | [setOnChangeCopyObject](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23adb75875d01a895d0e35c28a808aa9) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [OnChangeCopyOptions](../../da/dd9/classApp_1_1LinkBaseExtension.html#a284b55cf6075068951bb6f2c2655d465) options)  
| Include or exclude object from list of objects to copy on change.
[More...](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23adb75875d01a895d0e35c28a808aa9)  
  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getOnChangeCopyObjects](../../da/dd9/classApp_1_1LinkBaseExtension.html#a20adee6736980e9459b96c6306986d56) (std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > *excludes=nullptr, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *src=nullptr)  
[bool](../../d9/db9/classbool.html) | [isLinkedToConfigurableObject](../../da/dd9/classApp_1_1LinkBaseExtension.html#affcce56a557562ffeb5f0ee3a712a560) () const  
void | [monitorOnChangeCopyObjects](../../da/dd9/classApp_1_1LinkBaseExtension.html#a7ac95d82682691991817630089d96c55) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs)  
[bool](../../d9/db9/classbool.html) | [isLinkMutated](../../da/dd9/classApp_1_1LinkBaseExtension.html#aadc31174b5f6ae7279dfe9f8fbca5063) () const  
| Check if the linked object is a copy on change.
[More...](../../da/dd9/classApp_1_1LinkBaseExtension.html#aadc31174b5f6ae7279dfe9f8fbca5063)  
  
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
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Types inherited from
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html)  
enum | { [LinkModeNone](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072aafe335c4df45183d3fa18ac78ace9f94) , [LinkModeAutoDelete](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a08b1dbd9efdf88a06237ff2ac39c446d) , [LinkModeAutoLink](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a9bd4d4c7531fb158311f3cf5ef9e6ab0) , [LinkModeAutoUnlink](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a237a00c8484b2c285be54ed640eef3bb) }  
enum | [PropIndex](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac670080a44f59910e0e07651223ab0e9) { [PropMax](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac670080a44f59910e0e07651223ab0e9a0240d4810ad9f61fee21446ac1716c61) }  
enum | [LinkCopyOnChangeType](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3) { [CopyOnChangeDisabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aeb00fa1d41a505499c3758d5734d3a52) = 0 , [CopyOnChangeEnabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3a8fa884bdd8522db0d1a18950eaafc7d2) = 1 , [CopyOnChangeOwned](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aaa55e109c2c95bfe6369f6ee98da5f0b) = 2 , [CopyOnChangeTracking](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aa2112a0d8e4d199a95950b29d4b0bada) = 3 }  
enum class | [OnChangeCopyOptions](../../da/dd9/classApp_1_1LinkBaseExtension.html#a284b55cf6075068951bb6f2c2655d465) { [Exclude](../../da/dd9/classApp_1_1LinkBaseExtension.html#a284b55cf6075068951bb6f2c2655d465a843f2812f595e7ec7c5036e89fde02d6) = 1 , [ApplyAll](../../da/dd9/classApp_1_1LinkBaseExtension.html#a284b55cf6075068951bb6f2c2655d465ac3fb0da5f54a7ad9f5cf12d1f3f46aa7) = 2 }  
| Options used in
[setOnChangeCopyObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23adb75875d01a895d0e35c28a808aa9
"Include or exclude object from list of objects to copy on change.") Multiple
options can be combined by bitwise or operator.
[More...](../../da/dd9/classApp_1_1LinkBaseExtension.html#a284b55cf6075068951bb6f2c2655d465)  
  
typedef std::map< std::string, [PropInfo](../../d5/d5c/structApp_1_1LinkBaseExtension_1_1PropInfo.html) > | [PropInfoMap](../../da/dd9/classApp_1_1LinkBaseExtension.html#abd1b628a76cbd308ad37524ca47a9873)  
typedef std::map< const [Property](../../d0/da9/classApp_1_1Property.html) *, std::pair< [LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html) *, [int](../../d1/da0/classint.html) > > | [LinkPropMap](../../da/dd9/classApp_1_1LinkBaseExtension.html#a8ee0fabc29b406872bfe59bb7c8a38d1)  
![-](../../closed.png) Static Public Member Functions inherited from
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html)  
static [int](../../d1/da0/classint.html) | [getArrayIndex](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa6e99dda072f004deb3521501cd206c7) (const char *subname, const char **psubname=nullptr)  
static [bool](../../d9/db9/classbool.html) | [setupCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *linked, std::vector< boost::signals2::scoped_connection > *[copyOnChangeConns](../../da/dd9/classApp_1_1LinkBaseExtension.html#a21465cba234d91bab295dcb2df4090be), [bool](../../d9/db9/classbool.html) checkExisting)  
static [bool](../../d9/db9/classbool.html) | [isCopyOnChangeProperty](../../da/dd9/classApp_1_1LinkBaseExtension.html#a832eacdf828db96b92137a17f223243d) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const [Property](../../d0/da9/classApp_1_1Property.html) &prop)  
![-](../../closed.png) Protected Member Functions inherited from
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html)  
void | [parseSubName](../../da/dd9/classApp_1_1LinkBaseExtension.html#a8d813820d26ae9a33bab7dacd2271c96) () const  
void | [update](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, const [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
void | [checkCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6521528d36c644c2b1de74a2f74d82c0) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, const [App::Property](../../d0/da9/classApp_1_1Property.html) &prop)  
void | [setupCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae6497034c56291d32f554560d4b25532) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [bool](../../d9/db9/classbool.html) checkSource=false)  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [makeCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a89cc7109764a089298c635a71a86b49a) ()  
void | [syncElementList](../../da/dd9/classApp_1_1LinkBaseExtension.html#a7478fd88f7d95f23e3618e144028a66f) ()  
void | [detachElement](../../da/dd9/classApp_1_1LinkBaseExtension.html#ab752d9d1940adf9ab44ce4f332a9af94) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
void | [detachElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a60e10d23859162418791403de334bc9a) ()  
void | [checkGeoElementMap](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad6ede45b16c53f9facd69b1ed5ae10e1) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *linked, [PyObject](../../df/d1b/classPyObject.html) **pyObj, const char *postfix) const  
void | [updateGroup](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa4c9b7b4b1601759cac34c3c598bcac2) ()  
void | [slotChangedPlainGroup](../../da/dd9/classApp_1_1LinkBaseExtension.html#a59f78d9a479a5b5f6d9aee47a942b592) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)  
![-](../../closed.png) Protected Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
void | [initExtensionType](../../d8/dc7/classApp_1_1Extension.html#a12ec705423cb1952b395a4d135f2f734) ([Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html))  
![-](../../closed.png) Static Protected Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
static void | [initExtensionSubclass](../../d8/dc7/classApp_1_1Extension.html#ad89245f6dbe32a71396c452ea8148ce7) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Base::Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Protected Attributes inherited from
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html)  
std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > | [props](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6ed208f30a395cfbbebc6b6722832ba1)  
std::unordered_set< const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [myHiddenElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4b1ae2c71421c0cb58f600f39b19201e)  
std::vector< std::string > | [mySubElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a62871732d45530e4f92a221f2ab62dc9)  
std::string | [mySubName](../../da/dd9/classApp_1_1LinkBaseExtension.html#a62b9a4e2a74ec7ced7d11a9290811cfe)  
std::unordered_map< const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, boost::signals2::scoped_connection > | [plainGroupConns](../../da/dd9/classApp_1_1LinkBaseExtension.html#aed3c9454003b4f724af4311cde44d4a3)  
long | [prevLinkedObjectID](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a752e198724793baa3a3c3f9449d304) = 0  
std::unordered_map< std::string, [int](../../d1/da0/classint.html) > | [myLabelCache](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac42b7b06168e417f71c6891ceff944dd)  
[bool](../../d9/db9/classbool.html) | [enableLabelCache](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac2826bedf498b1b8bb0b1c2ff5e67cfc)  
[bool](../../d9/db9/classbool.html) | [hasOldSubElement](../../da/dd9/classApp_1_1LinkBaseExtension.html#af6a787363806414aba20b21c71a0e597)  
std::vector< boost::signals2::scoped_connection > | [copyOnChangeConns](../../da/dd9/classApp_1_1LinkBaseExtension.html#a21465cba234d91bab295dcb2df4090be)  
std::vector< boost::signals2::scoped_connection > | [copyOnChangeSrcConns](../../da/dd9/classApp_1_1LinkBaseExtension.html#a47e3a97f435df7d96ac7e5ac7776b3fa)  
[bool](../../d9/db9/classbool.html) | [hasCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#af6aabb3cea66fc6ac9c5786dc8bbc1b4)  
[bool](../../d9/db9/classbool.html) | [checkingProperty](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2df270984021644e590df20fdb586615) = false  
[bool](../../d9/db9/classbool.html) | [pauseCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23ef6afd46f9056a388196678639e591) = false  
boost::signals2::scoped_connection | [connCopyOnChangeSource](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae4a3d98edb220e932755a48778845365)  
![-](../../closed.png) Protected Attributes inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
[bool](../../d9/db9/classbool.html) | [m_isPythonExtension](../../d8/dc7/classApp_1_1Extension.html#aed35b8360543786d3d1ce3437234d706) = false  
Py::SmartPtr | [ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3)  
  
## Constructor & Destructor Documentation

## ◆ LinkExtension()

LinkExtension::LinkExtension  | ( | void  | | ) |   
---|---|---|---|---|---  
  
## ◆ ~LinkExtension()

| LinkExtension::~LinkExtension  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ onExtendedDocumentRestored()

| void App::LinkExtension::onExtendedDocumentRestored  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
get called after a document has been fully restored

Reimplemented from
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Link.h
  * FreeCAD/src/App/Link.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

