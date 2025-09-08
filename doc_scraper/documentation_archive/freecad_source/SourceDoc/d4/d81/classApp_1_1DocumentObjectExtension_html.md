---
url: https://freecad.github.io/SourceDoc/d4/d81/classApp_1_1DocumentObjectExtension.html
scraped_at: 2025-09-08T14:54:18.409935
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html)

[List of all members](../../da/d83/classApp_1_1DocumentObjectExtension-members.html) | Public Member Functions

App::DocumentObjectExtension Class Reference

[Extension](../../d8/dc7/classApp_1_1Extension.html "Base class for all
extension that can be added to a DocumentObject.") with special document
object calls.
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#details)

`#include <DocumentObjectExtension.h>`

##  Public Member Functions  
  
---  
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
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Protected Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
virtual void | [extensionOnChanged](../../d8/dc7/classApp_1_1Extension.html#a7f65954e27171964985beec0a5a21149) (const [Property](../../d0/da9/classApp_1_1Property.html) *p)  
void | [initExtensionType](../../d8/dc7/classApp_1_1Extension.html#a12ec705423cb1952b395a4d135f2f734) ([Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html))  
![-](../../closed.png) Static Protected Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
static void | [initExtensionSubclass](../../d8/dc7/classApp_1_1Extension.html#ad89245f6dbe32a71396c452ea8148ce7) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Base::Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Protected Attributes inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
[bool](../../d9/db9/classbool.html) | [m_isPythonExtension](../../d8/dc7/classApp_1_1Extension.html#aed35b8360543786d3d1ce3437234d706) = false  
Py::SmartPtr | [ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3)  
  
## Detailed Description

[Extension](../../d8/dc7/classApp_1_1Extension.html "Base class for all
extension that can be added to a DocumentObject.") with special document
object calls.

## Constructor & Destructor Documentation

## ◆ DocumentObjectExtension()

DocumentObjectExtension::DocumentObjectExtension  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~DocumentObjectExtension()

| DocumentObjectExtension::~DocumentObjectExtension  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ extensionExecute()

| [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * DocumentObjectExtension::extensionExecute  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#ae02f4d3ece4b2ce9710f93692832a4c3),
[Part::AttachExtension](../../dc/d47/classPart_1_1AttachExtension.html#a513814f48543318105c5230f517cfab2),
[Part::PrismExtension](../../d3/dbb/classPart_1_1PrismExtension.html#a8f4a3e41f6c2cc8a5f106fb13f73416b),
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a9b7579e56fb5b01cb0475a982541ff07),
and
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693).

References
[App::DocumentObject::StdReturn](../../d2/de4/classApp_1_1DocumentObject.html#af53a1c6a086c5dfe228aaefeeb7316d2).

Referenced by
[Part::AttachExtension::extensionExecute()](../../dc/d47/classPart_1_1AttachExtension.html#a513814f48543318105c5230f517cfab2),
[Part::PrismExtension::extensionExecute()](../../d3/dbb/classPart_1_1PrismExtension.html#a8f4a3e41f6c2cc8a5f106fb13f73416b),
[App::GroupExtension::extensionExecute()](../../da/d3a/classApp_1_1GroupExtension.html#a9b7579e56fb5b01cb0475a982541ff07),
and
[App::LinkBaseExtension::extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693).

## ◆ extensionGetLinkedObject()

| [bool](../../d9/db9/classbool.html) DocumentObjectExtension::extensionGetLinkedObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _ret_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recursive_ ,   
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ ,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ ,   
|  | [int](../../d1/da0/classint.html) | _depth_  
| ) | |  const  
virtual  
  
Get the linked object.

See also

    [DocumentObject::getLinkedObject()](../../d2/de4/classApp_1_1DocumentObject.html#ad7c7fb6359b4d1497b06f869327154a1 "Return the linked object with optional transformation.")

Returns

    Return turn if handled, the linked object is returned in `ret`

Reimplemented in
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad62f820b24b6540c9121d0fefb5e3054).

## ◆ extensionGetSubObject()

| [bool](../../d9/db9/classbool.html) DocumentObjectExtension::extensionGetSubObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _ret_ ,   
---|---|---|---  
|  | const char *  | _subname_ ,   
|  | [PyObject](../../df/d1b/classPyObject.html) **  | _pyObj_ ,   
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ ,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ ,   
|  | [int](../../d1/da0/classint.html) | _depth_  
| ) | |  const  
virtual  
  
Get the sub object by name.

See also

    [DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6 "Get the sub element/object by name.")

Returns

    Return turn if handled, the sub object is returned in `ret`

Reimplemented in
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a9f6afe4878329f62b99288df7224cec2),
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11),
and
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a).

## ◆ extensionGetSubObjects()

| [bool](../../d9/db9/classbool.html) DocumentObjectExtension::extensionGetSubObjects  | ( | std::vector< std::string > & | _ret_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _reason_  
| ) | |  const  
virtual  
  
Get name references of all sub objects.

See also

    [DocumentObject::getSubObjects()](../../d2/de4/classApp_1_1DocumentObject.html#a43e45965f79f8e68bda39c77764b61a0 "Return name reference of all sub-objects.")

Returns

    Return turn if handled, the sub object is returned in `ret`

Reimplemented in
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a049b0b8b248680cbdc858bd5e44603aa),
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a7abcd2dfce52f226f31f5996d5d360e2),
and
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#a666a0bbcc82f6538d3dfca95e4937ad5).

## ◆ extensionHasChildElement()

| virtual [bool](../../d9/db9/classbool.html) App::DocumentObjectExtension::extensionHasChildElement  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reimplemented in
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#aff055283d9be0810467d1e9540243415).

## ◆ extensionIsElementVisible()

| virtual [int](../../d1/da0/classint.html) App::DocumentObjectExtension::extensionIsElementVisible  | ( | const char *  | | ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#acf07fd549eb15bb1f7a3533b2ee58925).

## ◆ extensionMustExecute()

| short [int](../../d1/da0/classint.html) DocumentObjectExtension::extensionMustExecute  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#ad2e1bce76ecdcd255084312b108a9bf5),
[Part::AttachExtension](../../dc/d47/classPart_1_1AttachExtension.html#ad7cbf556235941da1ba3faed0535d656),
[Part::PrismExtension](../../d3/dbb/classPart_1_1PrismExtension.html#a453fe13add0ad7646860fabec9db3b19),
and
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#ae673c0469dcbdbe20c38ec986b1a1915).

Referenced by
[App::OriginGroupExtension::extensionMustExecute()](../../da/d09/classApp_1_1OriginGroupExtension.html#ad2e1bce76ecdcd255084312b108a9bf5).

## ◆ extensionSetElementVisible()

| virtual [int](../../d1/da0/classint.html) App::DocumentObjectExtension::extensionSetElementVisible  | ( | const char *  | ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) |   
| ) | |   
virtual  
  
Reimplemented in
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#af0547afce075bf3860bd9afe3052a61b).

## ◆ getExtendedObject() [1/2]

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * DocumentObjectExtension::getExtendedObject  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
and
[App::Extension::getExtendedContainer()](../../d8/dc7/classApp_1_1Extension.html#a178c40e2783b6e2d1f75b3c04feeabcf).

Referenced by
[PartDesign::Body::addObject()](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605),
[App::GroupExtension::addObject()](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea),
[App::GroupExtension::addObjects()](../../da/d3a/classApp_1_1GroupExtension.html#a5accdb378a9e7d47297547508ccec569),
[App::GeoFeatureGroupExtension::addObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d),
[Part::AttachExtension::extensionOnChanged()](../../dc/d47/classPart_1_1AttachExtension.html#ac73db2d8f32ca41b89157b47edce44c1),
[App::GeoFeatureGroupExtension::extensionOnChanged()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487),
[App::GroupExtension::extensionOnChanged()](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f),
[App::OriginGroupExtension::extensionOnChanged()](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42),
[TechDraw::CosmeticExtension::getCenterLineBySelection()](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#a33eb9064d32134b529754ed0dae507a1),
[TechDraw::CosmeticExtension::getCosmeticEdgeBySelection()](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#af868531e12158a223a247a082cd3303a),
[TechDraw::CosmeticExtension::getCosmeticVertexBySelection()](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#a114e682a6eff69fd18c5f1bc680d104a),
[TechDraw::CosmeticExtension::getGeomFormatBySelection()](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#ad72180a0fd98345e78d0b29a6d66254c),
[App::GroupExtension::getObject()](../../da/d3a/classApp_1_1GroupExtension.html#a334d367aa8c90d6ecf457792e37ca961),
[App::OriginGroupExtension::getOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2),
[Part::AttachExtension::getPlacement()](../../dc/d47/classPart_1_1AttachExtension.html#a57a65104519f09db8905d56fc1eca72b),
[App::GeoFeatureGroupExtension::globalGroupPlacement()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a585dae79f685156866b19a53eb93e77c),
[App::GroupExtension::hasObject()](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a),
[App::GroupExtension::isChildOf()](../../da/d3a/classApp_1_1GroupExtension.html#ad19ccc7fc052d71da1b11e6f736ca7c3),
[App::OriginGroupExtension::onExtendedSetupObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cbdf0475e8306ed1f6fab7bb2a071cb),
and
[App::LinkBaseExtension::updateGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa4c9b7b4b1601759cac34c3c598bcac2).

## ◆ getExtendedObject() [2/2]

const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * DocumentObjectExtension::getExtendedObject  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
and
[App::Extension::getExtendedContainer()](../../d8/dc7/classApp_1_1Extension.html#a178c40e2783b6e2d1f75b3c04feeabcf).

## ◆ getExtensionPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * DocumentObjectExtension::getExtensionPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html#a77ffed10ef0c284b3a702caf46570168).

Reimplemented in
[Part::AttachExtension](../../dc/d47/classPart_1_1AttachExtension.html#a155d047fcb333e7b8f42c4082f8bb12c),
[TechDraw::CosmeticExtension](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#a14c4a05d3113aca24f35203981ec15db),
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a860f82302ebbf404b14cca69adc9ff36),
and
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#af1063baf3790a0275959a311d0c7a93f).

References
[App::Extension::ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3).

## ◆ getViewProviderExtensionName()

| virtual const char * App::DocumentObjectExtension::getViewProviderExtensionName  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
returns the type name of the ViewProviderExtension which is automatically
attached to the viewprovider object when it is initiated

## ◆ onExtendedDocumentRestored()

| void DocumentObjectExtension::onExtendedDocumentRestored  | ( | | ) |   
---|---|---|---|---  
virtual  
  
get called after a document has been fully restored

Reimplemented in
[Part::AttachExtension](../../dc/d47/classPart_1_1AttachExtension.html#a6af7f6139ae7d3aef649ff3e89d05d75),
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34),
and
[App::LinkExtension](../../d6/d45/classApp_1_1LinkExtension.html#abf7e1de9b6ffa356efe37a1b6e04e66f).

Referenced by
[App::LinkBaseExtension::onExtendedDocumentRestored()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34).

## ◆ onExtendedSettingDocument()

| void DocumentObjectExtension::onExtendedSettingDocument  | ( | | ) |   
---|---|---|---|---  
virtual  
  
get called after setting the document

## ◆ onExtendedSetupObject()

| void DocumentObjectExtension::onExtendedSetupObject  | ( | | ) |   
---|---|---|---|---  
virtual  
  
get called after a brand new object was created

Reimplemented in
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cbdf0475e8306ed1f6fab7bb2a071cb).

Referenced by
[App::OriginGroupExtension::onExtendedSetupObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cbdf0475e8306ed1f6fab7bb2a071cb).

## ◆ onExtendedUnsetupObject()

| void DocumentObjectExtension::onExtendedUnsetupObject  | ( | | ) |   
---|---|---|---|---  
virtual  
  
get called when object is going to be removed from the document

Reimplemented in
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#abb164bab7e57290101417c27910f0715),
and
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a7d908f67bb05fe69e9c30add43aeae27).

Referenced by
[App::OriginGroupExtension::onExtendedUnsetupObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a7d908f67bb05fe69e9c30add43aeae27).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/DocumentObjectExtension.h
  * FreeCAD/src/App/DocumentObjectExtension.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

