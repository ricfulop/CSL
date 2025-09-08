---
url: https://freecad.github.io/SourceDoc/da/dd9/classApp_1_1LinkBaseExtension.html
scraped_at: 2025-09-08T14:54:57.690221
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html)

[List of all members](../../dd/d6b/classApp_1_1LinkBaseExtension-members.html) | Classes | Public Types | Public Member Functions

App::LinkBaseExtension Class Reference

`#include <Link.h>`

##  Classes  
  
---  
struct | [PropInfo](../../d5/d5c/structApp_1_1LinkBaseExtension_1_1PropInfo.html)  
  
##  Public Types  
  
---  
enum | { [LinkModeNone](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072aafe335c4df45183d3fa18ac78ace9f94) , [LinkModeAutoDelete](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a08b1dbd9efdf88a06237ff2ac39c446d) , [LinkModeAutoLink](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a9bd4d4c7531fb158311f3cf5ef9e6ab0) , [LinkModeAutoUnlink](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a237a00c8484b2c285be54ed640eef3bb) }  
  
##  Public Member Functions  
  
---  
|
[LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#acb03b8359e3c3e0391973dcf74f840ae)
()  
virtual | [~LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#a7eced285bdf5596f8d8a365af89495d1) ()  
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
  
## Parameter definition  
  
---  
Parameter definition (Name, Type,
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") Type, Default,
[Document](../../d8/d3e/classApp_1_1Document.html "The document class.")). The
variadic is here so that the parameter can be extended by adding extra fields.
See LINK_PARAM_EXT() for an example  
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
  
virtual void | [onExtendedDocumentRestored](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34) () override  
| get called after a document has been fully restored
[More...](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34)  
  
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
  
static [int](../../d1/da0/classint.html) | [getArrayIndex](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa6e99dda072f004deb3521501cd206c7) (const char *subname, const char **psubname=nullptr)  
static [bool](../../d9/db9/classbool.html) | [setupCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *linked, std::vector< boost::signals2::scoped_connection > *[copyOnChangeConns](../../da/dd9/classApp_1_1LinkBaseExtension.html#a21465cba234d91bab295dcb2df4090be), [bool](../../d9/db9/classbool.html) checkExisting)  
static [bool](../../d9/db9/classbool.html) | [isCopyOnChangeProperty](../../da/dd9/classApp_1_1LinkBaseExtension.html#a832eacdf828db96b92137a17f223243d) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const [Property](../../d0/da9/classApp_1_1Property.html) &prop)  
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
  
## Member Typedef Documentation

## ◆ LinkPropMap

typedef std::map<const
[Property](../../d0/da9/classApp_1_1Property.html)*,std::pair<[LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html)*,[int](../../d1/da0/classint.html)>
>
[App::LinkBaseExtension::LinkPropMap](../../da/dd9/classApp_1_1LinkBaseExtension.html#a8ee0fabc29b406872bfe59bb7c8a38d1)  
---  
  
## ◆ PropInfoMap

typedef std::map<std::string,
[PropInfo](../../d5/d5c/structApp_1_1LinkBaseExtension_1_1PropInfo.html)>
[App::LinkBaseExtension::PropInfoMap](../../da/dd9/classApp_1_1LinkBaseExtension.html#abd1b628a76cbd308ad37524ca47a9873)  
---  
  
## Member Enumeration Documentation

## ◆ anonymous enum

anonymous enum  
---  
  
Enumerator  
---  
LinkModeNone |   
LinkModeAutoDelete |   
LinkModeAutoLink |   
LinkModeAutoUnlink |   
  
## ◆ LinkCopyOnChangeType

enum
[App::LinkBaseExtension::LinkCopyOnChangeType](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3)  
---  
  
Enumerator  
---  
CopyOnChangeDisabled |   
CopyOnChangeEnabled |   
CopyOnChangeOwned |   
CopyOnChangeTracking |   
  
## ◆ OnChangeCopyOptions

| enum class
[App::LinkBaseExtension::OnChangeCopyOptions](../../da/dd9/classApp_1_1LinkBaseExtension.html#a284b55cf6075068951bb6f2c2655d465)  
---  
strong  
  
Options used in
[setOnChangeCopyObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23adb75875d01a895d0e35c28a808aa9
"Include or exclude object from list of objects to copy on change.") Multiple
options can be combined by bitwise or operator.

Enumerator  
---  
Exclude | If set, then exclude the input from object list to copy on change, or else, include the input object.   
ApplyAll | If set , then apply the setting to all links to the input object, or else, apply only to this link.   
  
## ◆ PropIndex

enum
[App::LinkBaseExtension::PropIndex](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac670080a44f59910e0e07651223ab0e9)  
---  
  
Enumerator  
---  
PropMax |   
  
## Constructor & Destructor Documentation

## ◆ LinkBaseExtension()

LinkBaseExtension::LinkBaseExtension  | ( | void  | | ) |   
---|---|---|---|---|---  
  
References
[App::Global](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a4cc6684df7b4a92b1dec6fce3264fac8),
[App::Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6),
[App::Prop_NoPersist](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a5e81a968f442a788999b25e00d9d14ca),
[App::Prop_Output](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a2f4f0fc70a512ce25e4c7ecb43a0eaa7),
and
[App::Prop_ReadOnly](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a9bea209c7050543e2ceadef7ba0e9e75).

## ◆ ~LinkBaseExtension()

| LinkBaseExtension::~LinkBaseExtension  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ cacheChildLabel()

void LinkBaseExtension::cacheChildLabel  | ( | [int](../../d1/da0/classint.html) | _enable_ = `-1`| ) |  const  
---|---|---|---|---|---  
  
References
[enableLabelCache](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac2826bedf498b1b8bb0b1c2ff5e67cfc),
and
[myLabelCache](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac42b7b06168e417f71c6891ceff944dd).

Referenced by
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b).

## ◆ checkCopyOnChange()

| void LinkBaseExtension::checkCopyOnChange  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
---|---|---|---  
|  | const [App::Property](../../d0/da9/classApp_1_1Property.html) & | _prop_  
| ) | |   
protected  
  
References
[App::Property::Copy()](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de),
[CopyOnChangeDisabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aeb00fa1d41a505499c3758d5734d3a52),
[CopyOnChangeOwned](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aaa55e109c2c95bfe6369f6ee98da5f0b),
[CopyOnChangeTracking](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aa2112a0d8e4d199a95950b29d4b0bada),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::Property::getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
[isCopyOnChangeProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a832eacdf828db96b92137a17f223243d),
[App::Document::isPerformingTransaction()](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2),
and
[makeCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a89cc7109764a089298c635a71a86b49a).

Referenced by
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ checkGeoElementMap()

| void LinkBaseExtension::checkGeoElementMap  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _linked_ ,   
|  | [PyObject](../../df/d1b/classPyObject.html) **  | _pyObj_ ,   
|  | const char *  | _postfix_  
| ) | |  const  
protected  
  
References
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2).

Referenced by
[extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a).

## ◆ detachElement()

| void LinkBaseExtension::detachElement  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
protected  
  
References
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[LinkModeAutoDelete](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a08b1dbd9efdf88a06237ff2ac39c446d),
and
[LinkModeAutoUnlink](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a237a00c8484b2c285be54ed640eef3bb).

Referenced by
[detachElements()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a60e10d23859162418791403de334bc9a),
and
[setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4).

## ◆ detachElements()

| void LinkBaseExtension::detachElements  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[detachElement()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ab752d9d1940adf9ab44ce4f332a9af94).

Referenced by
[onExtendedUnsetupObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#abb164bab7e57290101417c27910f0715),
and
[setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4).

## ◆ elementNameFromIndex()

void LinkBaseExtension::elementNameFromIndex  | ( | [int](../../d1/da0/classint.html) | _idx_ ,   
---|---|---|---  
|  | std::ostream & | _ss_  
| ) | |  const  
  
References
[elementNameFromIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ab6e1b35f106202ea5678702db336a819),
and
[App::GroupExtension::getGroupOfObject()](../../da/d3a/classApp_1_1GroupExtension.html#a04dde88db0fd3983e66bcf8444a3e07b).

Referenced by
[elementNameFromIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ab6e1b35f106202ea5678702db336a819),
and
[expandSubname()](../../da/dd9/classApp_1_1LinkBaseExtension.html#afe70635a884db59e1d026c499bc13b8e).

## ◆ expandSubname()

void LinkBaseExtension::expandSubname  | ( | std::string & | _subname_| ) |  const  
---|---|---|---|---|---  
  
References
[elementNameFromIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ab6e1b35f106202ea5678702db336a819),
and
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b).

## ◆ extensionExecute()

| [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * LinkBaseExtension::extensionExecute  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#aa8a99ad96497244412b31eb8cfd4079e).

References
[CopyOnChangeDisabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aeb00fa1d41a505499c3758d5734d3a52),
[CopyOnChangeTracking](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aa2112a0d8e4d199a95950b29d4b0bada),
[App::DocumentObjectExtension::extensionExecute()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#aa8a99ad96497244412b31eb8cfd4079e),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::Document::getObjectByID()](../../d8/d3e/classApp_1_1Document.html#affd903adb0b7171d0a8005d4f68fed26),
[App::ExtensionContainer::getPropertyByName()](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897),
[App::DocumentObject::getPyObject()](../../d2/de4/classApp_1_1DocumentObject.html#a1adfcfb2169b5c31374e07346256648f),
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1),
[App::PropertyPythonObject::getValue()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a1884e8da237c298d82d78d1b80e320cf),
[hasCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#af6aabb3cea66fc6ac9c5786dc8bbc1b4),
[isCopyOnChangeProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a832eacdf828db96b92137a17f223243d),
[props](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6ed208f30a395cfbbebc6b6722832ba1),
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e),
and
[syncCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4591b8c9e098285eceedfdc81e04381f).

## ◆ extensionGetLinkedObject()

| [bool](../../d9/db9/classbool.html) LinkBaseExtension::extensionGetLinkedObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _ret_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recursive_ ,   
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ ,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ ,   
|  | [int](../../d1/da0/classint.html) | _depth_  
| ) | |  const  
overridevirtual  
  
Get the linked object.

See also

    [DocumentObject::getLinkedObject()](../../d2/de4/classApp_1_1DocumentObject.html#ad7c7fb6359b4d1497b06f869327154a1 "Return the linked object with optional transformation.")

Returns

    Return turn if handled, the linked object is returned in `ret`

Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab6fc58714d6b5b2ecaa09f7ff6cc005f).

References
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[getTransform()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa78286a7bc1a3dfdb80c98f58726d827),
and
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1).

## ◆ extensionGetPropertyByName()

| [Property](../../d0/da9/classApp_1_1Property.html) * LinkBaseExtension::extensionGetPropertyByName  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
find a property by its name

Reimplemented from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html#ade0ea67a01018f91ef56838a3a557156).

References
[checkingProperty](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2df270984021644e590df20fdb586615),
[App::Extension::extensionGetPropertyByName()](../../d8/dc7/classApp_1_1Extension.html#ade0ea67a01018f91ef56838a3a557156),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
and
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1).

## ◆ extensionGetSubObject()

| [bool](../../d9/db9/classbool.html) LinkBaseExtension::extensionGetSubObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _ret_ ,   
---|---|---|---  
|  | const char *  | _subname_ ,   
|  | [PyObject](../../df/d1b/classPyObject.html) **  | _pyObj_ = `nullptr`,   
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ = `false`,   
|  | [int](../../d1/da0/classint.html) | _depth_ = `0`  
| ) | |  const  
overridevirtual  
  
Get the sub object by name.

See also

    [DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6 "Get the sub element/object by name.")

Returns

    Return turn if handled, the sub object is returned in `ret`

Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ae3b4c124bec333326bb9b0f0ad9600a7).

References
[checkGeoElementMap()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad6ede45b16c53f9facd69b1ed5ae10e1),
[DraftVecUtils::equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
[getScaleVector()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a546fb70b58ec1b41d2552d21e48f53a3),
[App::DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6),
[getTransform()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa78286a7bc1a3dfdb80c98f58726d827),
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1),
[Data::ComplexGeoData::indexPostfix()](../../d8/daf/classData_1_1ComplexGeoData.html#a8448d65b469a1242914a4d529d948fb3),
[Data::ComplexGeoData::isMappedElement()](../../d8/daf/classData_1_1ComplexGeoData.html#aadc45184e2b6b321a28496c323e66c08),
[mySubElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a62871732d45530e4f92a221f2ab62dc9),
and
[Base::Matrix4D::scale()](../../d5/db4/classBase_1_1Matrix4D.html#aa0838e1c628e3f405a83904679acec56).

Referenced by
[flattenSubname()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1e8f17cfe27ff1ee2968200036d5a431).

## ◆ extensionGetSubObjects()

| [bool](../../d9/db9/classbool.html) LinkBaseExtension::extensionGetSubObjects  | ( | std::vector< std::string > & | _ret_ ,   
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

References
[App::DocumentObject::getSubObjects()](../../d2/de4/classApp_1_1DocumentObject.html#a43e45965f79f8e68bda39c77764b61a0),
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1),
[mySubElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a62871732d45530e4f92a221f2ab62dc9),
and
[App::Extension::name()](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016).

## ◆ extensionHasChildElement()

| [bool](../../d9/db9/classbool.html) LinkBaseExtension::extensionHasChildElement  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a7ab4deac14dc40ce2e2675516baf156c).

References
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1),
and
[App::DocumentObject::hasChildElement()](../../d2/de4/classApp_1_1DocumentObject.html#a54805cb13103f36e16706bbea568e98c).

## ◆ extensionIsElementVisible()

| [int](../../d1/da0/classint.html) LinkBaseExtension::extensionIsElementVisible  | ( | const char *  | _element_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#adab10ac2801e93d6efde2c3d8cbc97db).

References
[getArrayIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa6e99dda072f004deb3521501cd206c7),
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1),
and
[App::DocumentObject::isElementVisible()](../../d2/de4/classApp_1_1DocumentObject.html#adaba073ae0d9e6aa00dc123c3ce8e0b5).

## ◆ extensionMustExecute()

| short LinkBaseExtension::extensionMustExecute  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af09cb831d7b6ba0300042f83af2f2ec6).

References
[getLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#acd90ba2231bd4cb62e7fd04b09f918e1).

## ◆ extensionOnChanged()

| void LinkBaseExtension::extensionOnChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _p_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html#a7f65954e27171964985beec0a5a21149).

References
[App::Extension::extensionOnChanged()](../../d8/dc7/classApp_1_1Extension.html#a7f65954e27171964985beec0a5a21149),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[App::Property::testStatus()](../../d0/da9/classApp_1_1Property.html#aa0757bcb7ff02f8ece1205afd8a05775),
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979),
and
[App::Property::User3](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aed76ddc4019f764ff7dbcb726007d14e).

## ◆ extensionSetElementVisible()

| [int](../../d1/da0/classint.html) LinkBaseExtension::extensionSetElementVisible  | ( | const char *  | _element_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _visible_  
| ) | |   
overridevirtual  
  
Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a59f60f1750805a02264f996c78967eae).

References
[getArrayIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa6e99dda072f004deb3521501cd206c7),
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1),
[myHiddenElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4b1ae2c71421c0cb58f600f39b19201e),
[App::DocumentObject::setElementVisible()](../../d2/de4/classApp_1_1DocumentObject.html#aad32b734a723878ba361804e983041a9),
and
[App::Property::User3](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aed76ddc4019f764ff7dbcb726007d14e).

## ◆ flattenSubname()

const char * LinkBaseExtension::flattenSubname  | ( | const char *  | _subname_| ) |  const  
---|---|---|---|---|---  
  
References
[extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a).

## ◆ getArrayIndex()

| [int](../../d1/da0/classint.html) LinkBaseExtension::getArrayIndex  | ( | const char *  | _subname_ ,   
---|---|---|---  
|  | const char **  | _psubname_ = `nullptr`  
| ) | |   
static  
  
References
[Data::ComplexGeoData::isMappedElement()](../../d8/daf/classData_1_1ComplexGeoData.html#aadc45184e2b6b321a28496c323e66c08).

Referenced by
[extensionIsElementVisible()](../../da/dd9/classApp_1_1LinkBaseExtension.html#acf07fd549eb15bb1f7a3533b2ee58925),
[extensionSetElementVisible()](../../da/dd9/classApp_1_1LinkBaseExtension.html#af0547afce075bf3860bd9afe3052a61b),
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
[Gui::ViewProviderLink::getElementPicked()](../../d6/d59/classGui_1_1ViewProviderLink.html#aa91a21df3ac8db004ca030c1bf57620b),
and
[Gui::LinkView::linkGetDetailPath()](../../da/d11/classGui_1_1LinkView.html#ae5489d900837b0dca02cf4f610e8a2b0).

## ◆ getContainer() [1/2]

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * LinkBaseExtension::getContainer  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
and
[App::Extension::getExtendedContainer()](../../d8/dc7/classApp_1_1Extension.html#a178c40e2783b6e2d1f75b3c04feeabcf).

Referenced by
[App::LinkElement::canDelete()](../../d0/d3e/classApp_1_1LinkElement.html#ae8715b080d90984e81724538ae3bda71),
[detachElement()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ab752d9d1940adf9ab44ce4f332a9af94),
[extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693),
[extensionGetLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad62f820b24b6540c9121d0fefb5e3054),
[extensionGetPropertyByName()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9673e9e742c402f3fb8c1ad6f5cdadad),
[extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a),
[extensionOnChanged()](../../da/dd9/classApp_1_1LinkBaseExtension.html#acfd0dd3d0677653d2da7fc2a4cdcd3c5),
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
[getOnChangeCopyObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a20adee6736980e9459b96c6306986d56),
[makeCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a89cc7109764a089298c635a71a86b49a),
[onExtendedDocumentRestored()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34),
[setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4),
[setOnChangeCopyObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23adb75875d01a895d0e35c28a808aa9),
[syncCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4591b8c9e098285eceedfdc81e04381f),
[syncElementList()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a7478fd88f7d95f23e3618e144028a66f),
and
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ getContainer() [2/2]

const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * LinkBaseExtension::getContainer  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
and
[App::Extension::getExtendedContainer()](../../d8/dc7/classApp_1_1Extension.html#a178c40e2783b6e2d1f75b3c04feeabcf).

## ◆ getElementIndex()

[int](../../d1/da0/classint.html) LinkBaseExtension::getElementIndex  | ( | const char *  | _subname_ ,   
---|---|---|---  
|  | const char **  | _psubname_ = `nullptr`  
| ) | |  const  
  
References
[cacheChildLabel()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a373305ffe3887c3d2f57d04b8585e685),
[enableLabelCache](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac2826bedf498b1b8bb0b1c2ff5e67cfc),
[DraftVecUtils::equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
[getArrayIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa6e99dda072f004deb3521501cd206c7),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1),
[Data::ComplexGeoData::isMappedElement()](../../d8/daf/classData_1_1ComplexGeoData.html#aadc45184e2b6b321a28496c323e66c08),
[myLabelCache](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac42b7b06168e417f71c6891ceff944dd),
and
[App::Extension::name()](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016).

Referenced by
[expandSubname()](../../da/dd9/classApp_1_1LinkBaseExtension.html#afe70635a884db59e1d026c499bc13b8e),
[extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a),
[extensionIsElementVisible()](../../da/dd9/classApp_1_1LinkBaseExtension.html#acf07fd549eb15bb1f7a3533b2ee58925),
[extensionSetElementVisible()](../../da/dd9/classApp_1_1LinkBaseExtension.html#af0547afce075bf3860bd9afe3052a61b),
and
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b).

## ◆ getExtensionPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * LinkBaseExtension::getExtensionPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a254f58c97024cd7e86fec56544fb77b1).

References
[App::Extension::ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3).

## ◆ getLink()

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * LinkBaseExtension::getLink  | ( | [int](../../d1/da0/classint.html) | _depth_ = `0`| ) |  const  
---|---|---|---|---|---  
  
References
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4).

Referenced by
[extensionMustExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae673c0469dcbdbe20c38ec986b1a1915),
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1),
and
[TechDraw::ShapeExtractor::getXShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4e820635335afa9ce7506faaf4274cbd).

## ◆ getLinkedChildren()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > LinkBaseExtension::getLinkedChildren  | ( | [bool](../../d9/db9/classbool.html) | _filter_ = `true`| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[TechDraw::ShapeExtractor::getXShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4e820635335afa9ce7506faaf4274cbd).

## ◆ getOnChangeCopyObjects()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > LinkBaseExtension::getOnChangeCopyObjects  | ( | std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > *  | _excludes_ = `nullptr`,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _src_ = `nullptr`  
| ) | |   
  
References
[CopyOnChangeDisabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aeb00fa1d41a505499c3758d5734d3a52),
[App::Document::DepSort](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a434619a08d5df25eeb3522b258263926),
[DraftVecUtils::equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
and
[App::Document::getDependencyList()](../../d8/d3e/classApp_1_1Document.html#a07ea2bb44ac29a4c0e89963ac28af323).

Referenced by
[makeCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a89cc7109764a089298c635a71a86b49a),
[onExtendedDocumentRestored()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34),
and
[syncCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4591b8c9e098285eceedfdc81e04381f).

## ◆ getProperty() [1/2]

[Property](../../d0/da9/classApp_1_1Property.html) * LinkBaseExtension::getProperty  | ( | const char *  | _name_| ) |   
---|---|---|---|---|---  
  
References
[getProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1bd7ade30a2e3669a12939c330352967),
and
[getPropertyInfoMap()](../../da/dd9/classApp_1_1LinkBaseExtension.html#af5361e9b169789363271fbd670700fbc).

## ◆ getProperty() [2/2]

[Property](../../d0/da9/classApp_1_1Property.html) * LinkBaseExtension::getProperty  | ( | [int](../../d1/da0/classint.html) | _idx_| ) |   
---|---|---|---|---|---  
  
Referenced by
[getProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a128a03065fbcbd2cf57f71fcfc852e03).

## ◆ getPropertyInfo()

| const std::vector< [LinkBaseExtension::PropInfo](../../d5/d5c/structApp_1_1LinkBaseExtension_1_1PropInfo.html) > & LinkBaseExtension::getPropertyInfo  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Referenced by
[getPropertyInfoMap()](../../da/dd9/classApp_1_1LinkBaseExtension.html#af5361e9b169789363271fbd670700fbc),
and
[setProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770).

## ◆ getPropertyInfoMap()

| const [LinkBaseExtension::PropInfoMap](../../da/dd9/classApp_1_1LinkBaseExtension.html#abd1b628a76cbd308ad37524ca47a9873) & LinkBaseExtension::getPropertyInfoMap  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
References
[getPropertyInfo()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a8c41e710c1ae424ef1f4fef8cf99bf54).

Referenced by
[getProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a128a03065fbcbd2cf57f71fcfc852e03).

## ◆ getScaleVector()

[Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) LinkBaseExtension::getScaleVector  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a),
[getTransform()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa78286a7bc1a3dfdb80c98f58726d827),
and
[TechDraw::ShapeExtractor::getXShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4e820635335afa9ce7506faaf4274cbd).

## ◆ getSubElements()

const std::vector< std::string > & App::LinkBaseExtension::getSubElements  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getSubName()

const char * App::LinkBaseExtension::getSubName  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1).

## ◆ getTransform()

[Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) LinkBaseExtension::getTransform  | ( | [bool](../../d9/db9/classbool.html) | _transform_| ) |  const  
---|---|---|---|---|---  
  
References
[getScaleVector()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a546fb70b58ec1b41d2552d21e48f53a3),
and
[Base::Matrix4D::scale()](../../d5/db4/classBase_1_1Matrix4D.html#aa0838e1c628e3f405a83904679acec56).

Referenced by
[extensionGetLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad62f820b24b6540c9121d0fefb5e3054),
and
[extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a).

## ◆ getTrueLinkedObject()

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * LinkBaseExtension::getTrueLinkedObject  | ( | [bool](../../d9/db9/classbool.html) | _recurse_ ,   
---|---|---|---  
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ = `nullptr`,   
|  | [int](../../d1/da0/classint.html) | _depth_ = `0`,   
|  | [bool](../../d9/db9/classbool.html) | _noElement_ = `false`  
| ) | |  const  
  
References
[App::Extension::extensionIsDerivedFrom()](../../d8/dc7/classApp_1_1Extension.html#ad635be48204f8f5fb9c75103cd89fb20),
[getLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#acd90ba2231bd4cb62e7fd04b09f918e1),
[getSubName()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3217de1bc2559882937299e3d11a2904),
and
[linkTransform()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac6f97ab8d9ff54b06d63d743fcb065a6).

Referenced by
[extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693),
[extensionGetLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad62f820b24b6540c9121d0fefb5e3054),
[extensionGetPropertyByName()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9673e9e742c402f3fb8c1ad6f5cdadad),
[extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a),
[extensionGetSubObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a666a0bbcc82f6538d3dfca95e4937ad5),
[extensionHasChildElement()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aff055283d9be0810467d1e9540243415),
[extensionIsElementVisible()](../../da/dd9/classApp_1_1LinkBaseExtension.html#acf07fd549eb15bb1f7a3533b2ee58925),
[extensionSetElementVisible()](../../da/dd9/classApp_1_1LinkBaseExtension.html#af0547afce075bf3860bd9afe3052a61b),
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
[linkedPlainGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad1a36871ddcd463c8c399b6d1ed25d02),
and
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae6497034c56291d32f554560d4b25532).

## ◆ hasPlacement()

[bool](../../d9/db9/classbool.html) App::LinkBaseExtension::hasPlacement  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[TechDraw::ShapeExtractor::getXShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4e820635335afa9ce7506faaf4274cbd).

## ◆ isCopyOnChangeProperty()

| [bool](../../d9/db9/classbool.html) LinkBaseExtension::isCopyOnChangeProperty  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) & | _prop_  
| ) | |   
static  
  
References
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::Property::getGroup()](../../d0/da9/classApp_1_1Property.html#ab815066b984a7d6c133b4c947a989fee),
[App::Property::PropDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a610d527a8ef20b533504b5121a983d80),
and
[App::Property::testStatus()](../../d0/da9/classApp_1_1Property.html#aa0757bcb7ff02f8ece1205afd8a05775).

Referenced by
[checkCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6521528d36c644c2b1de74a2f74d82c0),
[PartDesign::SubShapeBinder::checkCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3698bc706a89765ff35db75048a08698),
[extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693),
[PartDesign::SubShapeBinder::setupCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3f0c1dcf0ed5800b1865c2c42f4e25f7),
and
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83).

## ◆ isLinkedToConfigurableObject()

[bool](../../d9/db9/classbool.html) LinkBaseExtension::isLinkedToConfigurableObject  | ( | | ) |  const  
---|---|---|---|---  
  
References
[App::Property::CopyOnChange](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a300baf70d0747fc9f320701a04ba5499).

## ◆ isLinkMutated()

[bool](../../d9/db9/classbool.html) LinkBaseExtension::isLinkMutated  | ( | | ) |  const  
---|---|---|---|---  
  
Check if the linked object is a copy on change.

References
[CopyOnChangeDisabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aeb00fa1d41a505499c3758d5734d3a52).

## ◆ linkedPlainGroup()

[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html) * LinkBaseExtension::linkedPlainGroup  | ( | | ) |  const  
---|---|---|---|---  
  
References
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1),
and
[mySubElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a62871732d45530e4f92a221f2ab62dc9).

Referenced by
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979),
and
[updateGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa4c9b7b4b1601759cac34c3c598bcac2).

## ◆ linkTransform()

[bool](../../d9/db9/classbool.html) LinkBaseExtension::linkTransform  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1).

## ◆ makeCopyOnChange()

| [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * LinkBaseExtension::makeCopyOnChange  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[CopyOnChangeEnabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3a8fa884bdd8522db0d1a18950eaafc7d2),
[CopyOnChangeOwned](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aaa55e109c2c95bfe6369f6ee98da5f0b),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[getOnChangeCopyObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a20adee6736980e9459b96c6306986d56),
[LinkModeAutoDelete](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a08b1dbd9efdf88a06237ff2ac39c446d),
[monitorOnChangeCopyObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a7ac95d82682691991817630089d96c55),
[App::PartialObject](../../dd/dc2/namespaceApp.html#a6ea56730deb62adcdfb038475dab9d3aadddc278250236b1498067f68f109203f),
and
[pauseCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23ef6afd46f9056a388196678639e591).

Referenced by
[checkCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6521528d36c644c2b1de74a2f74d82c0),
and
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae6497034c56291d32f554560d4b25532).

## ◆ monitorOnChangeCopyObjects()

void LinkBaseExtension::monitorOnChangeCopyObjects  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_| ) |   
---|---|---|---|---|---  
  
References
[CopyOnChangeDisabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aeb00fa1d41a505499c3758d5734d3a52),
and
[copyOnChangeSrcConns](../../da/dd9/classApp_1_1LinkBaseExtension.html#a47e3a97f435df7d96ac7e5ac7776b3fa).

Referenced by
[makeCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a89cc7109764a089298c635a71a86b49a),
[onExtendedDocumentRestored()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34),
and
[syncCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4591b8c9e098285eceedfdc81e04381f).

## ◆ onExtendedDocumentRestored()

| void LinkBaseExtension::onExtendedDocumentRestored  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
get called after a document has been fully restored

Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af01de2fab2226a8e3e88dd1db479c3a8).

Reimplemented in
[App::LinkExtension](../../d6/d45/classApp_1_1LinkExtension.html#abf7e1de9b6ffa356efe37a1b6e04e66f).

References
[CopyOnChangeDisabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aeb00fa1d41a505499c3758d5734d3a52),
[Data::ComplexGeoData::findElementName()](../../d8/daf/classData_1_1ComplexGeoData.html#a7a2ff773f05abdf81ee7194a81788085),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[getOnChangeCopyObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a20adee6736980e9459b96c6306986d56),
[hasOldSubElement](../../da/dd9/classApp_1_1LinkBaseExtension.html#af6a787363806414aba20b21c71a0e597),
[monitorOnChangeCopyObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a7ac95d82682691991817630089d96c55),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[myHiddenElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4b1ae2c71421c0cb58f600f39b19201e),
[mySubElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a62871732d45530e4f92a221f2ab62dc9),
[App::DocumentObjectExtension::onExtendedDocumentRestored()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af01de2fab2226a8e3e88dd1db479c3a8),
[pauseCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23ef6afd46f9056a388196678639e591),
and
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ onExtendedUnsetupObject()

| void LinkBaseExtension::onExtendedUnsetupObject  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
get called when object is going to be removed from the document

Reimplemented from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a0cf88b507c8a513d5ae2dc63a7221133).

References
[detachElements()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a60e10d23859162418791403de334bc9a).

## ◆ parseSubName()

| void LinkBaseExtension::parseSubName  | ( | | ) |  const  
---|---|---|---|---  
protected  
  
References
[Data::ComplexGeoData::findElementName()](../../d8/daf/classData_1_1ComplexGeoData.html#a7a2ff773f05abdf81ee7194a81788085),
[mySubElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a62871732d45530e4f92a221f2ab62dc9),
and
[mySubName](../../da/dd9/classApp_1_1LinkBaseExtension.html#a62b9a4e2a74ec7ced7d11a9290811cfe).

Referenced by
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ setLink()

void LinkBaseExtension::setLink  | ( | [int](../../d1/da0/classint.html) | _index_ ,   
---|---|---|---  
|  | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
|  | const char *  | _subname_ = `nullptr`,   
|  | const std::vector< std::string > & | _subs_ = `std::vector<std::string>()`  
| ) | |   
  
References
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[detachElement()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ab752d9d1940adf9ab44ce4f332a9af94),
[detachElements()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a60e10d23859162418791403de334bc9a),
[DraftVecUtils::find()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf764683bba7871d8f3d64db4fb2a41a9),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::Document::getUniqueObjectName()](../../d8/d3e/classApp_1_1Document.html#a8bc7c3b871147cf18529b0a1e9f44ac9),
[App::Document::isAnyRestoring()](../../d8/d3e/classApp_1_1Document.html#ad76082433b2ec1d09d842514de7dfe38),
[App::DocumentObject::Label](../../d2/de4/classApp_1_1DocumentObject.html#a7259f450fea1a74073e626115d46110d),
[LinkModeAutoLink](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a9bd4d4c7531fb158311f3cf5ef9e6ab0),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

## ◆ setOnChangeCopyObject()

void LinkBaseExtension::setOnChangeCopyObject  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [OnChangeCopyOptions](../../da/dd9/classApp_1_1LinkBaseExtension.html#a284b55cf6075068951bb6f2c2655d465) | _options_  
| ) | |   
  
Include or exclude object from list of objects to copy on change.

Parameters

     obj| input object   
---|---  
options| control options.  
  
See also

    [OnChangeCopyOptions](../../da/dd9/classApp_1_1LinkBaseExtension.html#a284b55cf6075068951bb6f2c2655d465 "Options used in setOnChangeCopyObject\(\) Multiple options can be combined by bitwise or operator."). 

References
[ApplyAll](../../da/dd9/classApp_1_1LinkBaseExtension.html#a284b55cf6075068951bb6f2c2655d465ac3fb0da5f54a7ad9f5cf12d1f3f46aa7),
[Exclude](../../da/dd9/classApp_1_1LinkBaseExtension.html#a284b55cf6075068951bb6f2c2655d465a843f2812f595e7ec7c5036e89fde02d6),
and
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017).

## ◆ setProperty()

| void LinkBaseExtension::setProperty  | ( | [int](../../d1/da0/classint.html) | _idx_ ,   
---|---|---|---  
|  | [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_  
| ) | |   
virtual  
  
References
[App::Extension::extensionGetPropertyName()](../../d8/dc7/classApp_1_1Extension.html#a670480fa1d036c8217ef4b817f2c41a6),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[Base::Type::getName()](../../dc/dee/classBase_1_1Type.html#a861a2f6bd2cd2c2df7846e202f0ce137),
[App::Property::getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a),
[getPropertyInfo()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a8c41e710c1ae424ef1f4fef8cf99bf54),
[App::Global](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263a4cc6684df7b4a92b1dec6fce3264fac8),
[App::Property::Hidden](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014adef773114327b6ad987a0c47a4262a54),
[App::Property::Immutable](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a59d0f940edf009b9ffbe01ed43d767cc),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
[App::Property::isValidName()](../../d0/da9/classApp_1_1Property.html#ad8541be7b1fddd7f21f2ce3e18e8c06d),
[App::Property::LockDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ac134907b347ed2484e41577a88d9a06e),
[App::PropertyEnumeration::setEnums()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a5571099202eda6dacf748996eedf6551),
and
[App::Property::setStatus()](../../d0/da9/classApp_1_1Property.html#a2f10dba2d265461344c6df7d0a40ad4e).

## ◆ setupCopyOnChange() [1/2]

| [bool](../../d9/db9/classbool.html) LinkBaseExtension::setupCopyOnChange  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _linked_ ,   
|  | std::vector< boost::signals2::scoped_connection > *  | _copyOnChangeConns_ ,   
|  | [bool](../../d9/db9/classbool.html) | _checkExisting_  
| ) | |   
static  
  
References
[App::DocumentObject::addDynamicProperty()](../../d2/de4/classApp_1_1DocumentObject.html#abf2aa7beac95fbed58ef392808477218),
[App::Property::CopyOnChange](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a300baf70d0747fc9f320701a04ba5499),
[copyOnChangeConns](../../da/dd9/classApp_1_1LinkBaseExtension.html#a21465cba234d91bab295dcb2df4090be),
[App::Property::getGroup()](../../d0/da9/classApp_1_1Property.html#ab815066b984a7d6c133b4c947a989fee),
[App::ExtensionContainer::getPropertyByName()](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897),
[App::ExtensionContainer::getPropertyList()](../../d6/d76/classApp_1_1ExtensionContainer.html#a4b980230637c28a4159575a8955c9fe6),
[props](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6ed208f30a395cfbbebc6b6722832ba1),
[App::DocumentObject::removeDynamicProperty()](../../d2/de4/classApp_1_1DocumentObject.html#a00938d679f9f65e7ee4e9ef02d399c84),
and
[App::Property::User3](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aed76ddc4019f764ff7dbcb726007d14e).

Referenced by
[extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693),
[PartDesign::SubShapeBinder::setupCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3f0c1dcf0ed5800b1865c2c42f4e25f7),
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae6497034c56291d32f554560d4b25532),
and
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ setupCopyOnChange() [2/2]

| void LinkBaseExtension::setupCopyOnChange  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _checkSource_ = `false`  
| ) | |   
protected  
  
References
[copyOnChangeConns](../../da/dd9/classApp_1_1LinkBaseExtension.html#a21465cba234d91bab295dcb2df4090be),
[CopyOnChangeDisabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aeb00fa1d41a505499c3758d5734d3a52),
[CopyOnChangeOwned](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aaa55e109c2c95bfe6369f6ee98da5f0b),
[copyOnChangeSrcConns](../../da/dd9/classApp_1_1LinkBaseExtension.html#a47e3a97f435df7d96ac7e5ac7776b3fa),
[getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1),
[hasCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#af6aabb3cea66fc6ac9c5786dc8bbc1b4),
[makeCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a89cc7109764a089298c635a71a86b49a),
[pauseCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23ef6afd46f9056a388196678639e591),
and
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e).

## ◆ slotChangedPlainGroup()

| void LinkBaseExtension::slotChangedPlainGroup  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) & | _obj_ ,   
---|---|---|---  
|  | const [App::Property](../../d0/da9/classApp_1_1Property.html) & | _prop_  
| ) | |   
protected  
  
References
[updateGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa4c9b7b4b1601759cac34c3c598bcac2).

Referenced by
[updateGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa4c9b7b4b1601759cac34c3c598bcac2).

## ◆ syncCopyOnChange()

void LinkBaseExtension::syncCopyOnChange  | ( | | ) |   
---|---|---|---|---  
  
References
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Property::CopyOnChange](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a300baf70d0747fc9f320701a04ba5499),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[getOnChangeCopyObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a20adee6736980e9459b96c6306986d56),
[LinkModeAutoDelete](../../da/dd9/classApp_1_1LinkBaseExtension.html#a3a36f3b6f223ad01d1dea74e3a1cf072a08b1dbd9efdf88a06237ff2ac39c446d),
[monitorOnChangeCopyObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a7ac95d82682691991817630089d96c55),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[pauseCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23ef6afd46f9056a388196678639e591).

Referenced by
[extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693).

## ◆ syncElementList()

| void LinkBaseExtension::syncElementList  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[App::Property::Hidden](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014adef773114327b6ad987a0c47a4262a54),
and
[App::Property::Immutable](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a59d0f940edf009b9ffbe01ed43d767cc).

Referenced by
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ update()

| void LinkBaseExtension::update  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_  
| ) | |   
protected  
  
References
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[checkCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6521528d36c644c2b1de74a2f74d82c0),
[connCopyOnChangeSource](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae4a3d98edb220e932755a48778845365),
[CopyOnChangeDisabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aeb00fa1d41a505499c3758d5734d3a52),
[CopyOnChangeEnabled](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3a8fa884bdd8522db0d1a18950eaafc7d2),
[CopyOnChangeOwned](../../da/dd9/classApp_1_1LinkBaseExtension.html#a0948cfc0a3ae76a790a648f3683269b3aaa55e109c2c95bfe6369f6ee98da5f0b),
[enableLabelCache](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac2826bedf498b1b8bb0b1c2ff5e67cfc),
[getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa9df72d4f6276f9ad12d06374d25b017),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::Property::getType()](../../d0/da9/classApp_1_1Property.html#abc4967c88a5fc83c27a47f9534fdd510),
[App::Property::Hidden](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014adef773114327b6ad987a0c47a4262a54),
[App::Document::isAnyRestoring()](../../d8/d3e/classApp_1_1Document.html#ad76082433b2ec1d09d842514de7dfe38),
[App::Document::isPerformingTransaction()](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2),
[linkedPlainGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad1a36871ddcd463c8c399b6d1ed25d02),
[myHiddenElements](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4b1ae2c71421c0cb58f600f39b19201e),
[myLabelCache](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac42b7b06168e417f71c6891ceff944dd),
[App::Property::Output](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a10640ff2cae2c1fda52dac13fc9a47a6),
[parseSubName()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a8d813820d26ae9a33bab7dacd2271c96),
[pauseCopyOnChange](../../da/dd9/classApp_1_1LinkBaseExtension.html#a23ef6afd46f9056a388196678639e591),
[App::Prop_Output](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a2f4f0fc70a512ce25e4c7ecb43a0eaa7),
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e),
[syncElementList()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a7478fd88f7d95f23e3618e144028a66f),
[App::Property::testStatus()](../../d0/da9/classApp_1_1Property.html#aa0757bcb7ff02f8ece1205afd8a05775),
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979),
[updateGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa4c9b7b4b1601759cac34c3c598bcac2),
and
[App::Property::User3](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aed76ddc4019f764ff7dbcb726007d14e).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchAxisSystem.AxisSystemTaskPanel::addElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a68544065aac91fa78a8bddb3e6ed5a99),
[ArchComponent.ComponentTaskPanel::addElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a21a385085defc9e8ccca8b2261a57314),
[ArchSectionPlane.SectionPlaneTaskPanel::addElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a6317c0ca7eb0c28e60b863f96ddeb81f),
[DraftGui.FacebinderTaskPanel::addElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a7642fdc6d6fa90afec25930af3b0a66e),
[femtaskpanels.task_result_mechanical._TaskPanel::calculate()](../../d1/d11/classfemtaskpanels_1_1task__result__mechanical_1_1__TaskPanel.html#aa2b98b5a9e12d62038ea9cc00366ecb6),
[Spreadsheet_legacy.SpreadsheetView::changeCell()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a897cda21a4a4f34431c371a31579706e),
[draftguitools.gui_edit.Edit::endEditing()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#ab9797631ba43c7855016e2552c21834f),
[extensionOnChanged()](../../da/dd9/classApp_1_1LinkBaseExtension.html#acfd0dd3d0677653d2da7fc2a4cdcd3c5),
[draftguitools.gui_trackers.boxTracker::height()](../../d5/dca/classdraftguitools_1_1gui__trackers_1_1boxTracker.html#a25f7d7bbd56b5ff5ef5da124e515dd00),
[onExtendedDocumentRestored()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34),
[draftguitools.gui_trackers.rectangleTracker::p3()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a1bf47cdde1ea165a58946f1a5fdc6c8e),
[Plot.Plot::plot()](../../d3/d54/classPlot_1_1Plot.html#a8b670f38324a7fae1c7128e117cba688),
[Spreadsheet_legacy.SpreadsheetView::recompute()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a1d8b8256ad183347aedaf40a269c2d3a),
[ArchAxisSystem.AxisSystemTaskPanel::removeElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a27e3fe8ffbc52acfd92f2d333626a76d),
[ArchComponent.ComponentTaskPanel::removeElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#ad9d18ffd3ef7556affab6b62a6acceb5),
[ArchSectionPlane.SectionPlaneTaskPanel::removeElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a544dbf3def03e06b86e6f32c390fd46a),
[DraftGui.FacebinderTaskPanel::removeElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a8ce5c644e81d1fbb3907e351e2050a0a),
[draftguitools.gui_trackers.gridTracker::reset()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a2c6f7e1d0a817adacef8297962691a9c),
[ArchNesting.Nester::run()](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102),
[draftguitools.gui_trackers.gridTracker::setMainlines()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#ac1c96a4a6282724211bc61a37ffa5a05),
[draftguitools.gui_trackers.gridTracker::setSize()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a6bb2d86a97781159c083a23a30f9fb9a),
[draftguitools.gui_trackers.gridTracker::setSpacing()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a67fe5637d9f2b95d4c6c6a717f41e6e4),
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979),
and
[draftguitools.gui_edit_arch_objects.ArchWallGuiTools::update_object_from_edit_points()](../../d1/d46/classdraftguitools_1_1gui__edit__arch__objects_1_1ArchWallGuiTools.html#a1340bdc87e40eb0a04ba856255ae0f93).

## ◆ updateGroup()

| void LinkBaseExtension::updateGroup  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705),
[App::DocumentObject::getFullName()](../../d2/de4/classApp_1_1DocumentObject.html#ab9ad25e711d56a5d6c8ba0f7638a8a62),
[linkedPlainGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad1a36871ddcd463c8c399b6d1ed25d02),
[plainGroupConns](../../da/dd9/classApp_1_1LinkBaseExtension.html#aed3c9454003b4f724af4311cde44d4a3),
and
[slotChangedPlainGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a59f78d9a479a5b5f6d9aee47a942b592).

Referenced by
[slotChangedPlainGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a59f78d9a479a5b5f6d9aee47a942b592),
and
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## Member Data Documentation

## ◆ checkingProperty

| [bool](../../d9/db9/classbool.html) App::LinkBaseExtension::checkingProperty
= false  
---  
mutableprotected  
  
Referenced by
[extensionGetPropertyByName()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9673e9e742c402f3fb8c1ad6f5cdadad).

## ◆ connCopyOnChangeSource

| boost::signals2::scoped_connection
App::LinkBaseExtension::connCopyOnChangeSource  
---  
protected  
  
Referenced by
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ copyOnChangeConns

| std::vector<boost::signals2::scoped_connection>
App::LinkBaseExtension::copyOnChangeConns  
---  
protected  
  
Referenced by
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae6497034c56291d32f554560d4b25532).

## ◆ copyOnChangeSrcConns

| std::vector<boost::signals2::scoped_connection>
App::LinkBaseExtension::copyOnChangeSrcConns  
---  
protected  
  
Referenced by
[monitorOnChangeCopyObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a7ac95d82682691991817630089d96c55),
and
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae6497034c56291d32f554560d4b25532).

## ◆ enableLabelCache

| [bool](../../d9/db9/classbool.html) App::LinkBaseExtension::enableLabelCache  
---  
mutableprotected  
  
Referenced by
[cacheChildLabel()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a373305ffe3887c3d2f57d04b8585e685),
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
and
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ hasCopyOnChange

| [bool](../../d9/db9/classbool.html) App::LinkBaseExtension::hasCopyOnChange  
---  
protected  
  
Referenced by
[extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693),
and
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae6497034c56291d32f554560d4b25532).

## ◆ hasOldSubElement

| [bool](../../d9/db9/classbool.html) App::LinkBaseExtension::hasOldSubElement  
---  
protected  
  
Referenced by
[onExtendedDocumentRestored()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34).

## ◆ myHiddenElements

| std::unordered_set<const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>
App::LinkBaseExtension::myHiddenElements  
---  
protected  
  
Referenced by
[extensionSetElementVisible()](../../da/dd9/classApp_1_1LinkBaseExtension.html#af0547afce075bf3860bd9afe3052a61b),
[onExtendedDocumentRestored()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34),
and
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ myLabelCache

| std::unordered_map<std::string,[int](../../d1/da0/classint.html)>
App::LinkBaseExtension::myLabelCache  
---  
mutableprotected  
  
Referenced by
[cacheChildLabel()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a373305ffe3887c3d2f57d04b8585e685),
[getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
and
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ mySubElements

| std::vector<std::string> App::LinkBaseExtension::mySubElements  
---  
mutableprotected  
  
Referenced by
[extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a),
[extensionGetSubObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a666a0bbcc82f6538d3dfca95e4937ad5),
[linkedPlainGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad1a36871ddcd463c8c399b6d1ed25d02),
[onExtendedDocumentRestored()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34),
and
[parseSubName()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a8d813820d26ae9a33bab7dacd2271c96).

## ◆ mySubName

| std::string App::LinkBaseExtension::mySubName  
---  
mutableprotected  
  
Referenced by
[parseSubName()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a8d813820d26ae9a33bab7dacd2271c96).

## ◆ pauseCopyOnChange

| [bool](../../d9/db9/classbool.html)
App::LinkBaseExtension::pauseCopyOnChange = false  
---  
protected  
  
Referenced by
[makeCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a89cc7109764a089298c635a71a86b49a),
[onExtendedDocumentRestored()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34),
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae6497034c56291d32f554560d4b25532),
[syncCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4591b8c9e098285eceedfdc81e04381f),
and
[update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ plainGroupConns

| std::unordered_map<const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*,
boost::signals2::scoped_connection> App::LinkBaseExtension::plainGroupConns  
---  
protected  
  
Referenced by
[updateGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa4c9b7b4b1601759cac34c3c598bcac2).

## ◆ prevLinkedObjectID

| long App::LinkBaseExtension::prevLinkedObjectID = 0  
---  
protected  
  
## ◆ props

| std::vector<[Property](../../d0/da9/classApp_1_1Property.html) *>
App::LinkBaseExtension::props  
---  
protected  
  
Referenced by
[PathScripts.PathSetupSheetGui.OpTaskPanel::accept()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#abf41762321cdf0582942161477eba1da),
[extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693),
[setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e),
[PathScripts.PathPropertyBagGui.TaskPanel::setupUi()](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#a0e7d9c2f42ae50ec45505059011deba5),
and
[PathScripts.PathSetupSheetGui.OpTaskPanel::setupUi()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a03e427ec6574bd249d859f5bd2496576).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Link.h
  * FreeCAD/src/App/Link.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

