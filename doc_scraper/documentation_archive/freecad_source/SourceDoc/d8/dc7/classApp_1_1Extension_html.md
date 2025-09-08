---
url: https://freecad.github.io/SourceDoc/d8/dc7/classApp_1_1Extension.html
scraped_at: 2025-09-08T14:54:19.421657
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Extension](../../d8/dc7/classApp_1_1Extension.html)

[List of all members](../../d9/d5a/classApp_1_1Extension-members.html) | Public Member Functions

App::Extension Class Reference

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class for all extension that can be added to a
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.").
[More...](../../d8/dc7/classApp_1_1Extension.html#details)

`#include <Extension.h>`

##  Public Member Functions  
  
---  
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
Access properties  
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
  
Persistence  
virtual void | [extensionSave](../../d8/dc7/classApp_1_1Extension.html#a94c65f4a8cf93d9a149726049885aafd) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &) const  
virtual void | [extensionRestore](../../d8/dc7/classApp_1_1Extension.html#ab1a7fb60166532ef2838ee0722c5955f) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &)  
  
## TypeHandling  
  
---  
class | [App::ExtensionContainer](../../d8/dc7/classApp_1_1Extension.html#ac7d4a8df8b2fcf0f567385578f700579)  
[bool](../../d9/db9/classbool.html) | [m_isPythonExtension](../../d8/dc7/classApp_1_1Extension.html#aed35b8360543786d3d1ce3437234d706) = false  
Py::SmartPtr | [ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3)  
[bool](../../d9/db9/classbool.html) | [extensionIsDerivedFrom](../../d8/dc7/classApp_1_1Extension.html#ad635be48204f8f5fb9c75103cd89fb20) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
static void | [initExtensionSubclass](../../d8/dc7/classApp_1_1Extension.html#ad89245f6dbe32a71396c452ea8148ce7) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Base::Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
virtual void | [extensionOnChanged](../../d8/dc7/classApp_1_1Extension.html#a7f65954e27171964985beec0a5a21149) (const [Property](../../d0/da9/classApp_1_1Property.html) *p)  
void | [initExtensionType](../../d8/dc7/classApp_1_1Extension.html#a12ec705423cb1952b395a4d135f2f734) ([Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html))  
  
## Detailed Description

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class for all extension that can be added to a
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.").

For general documentation on why extension system exists and how to use it see
the [ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html
"Container which can hold extensions.") documentation. Following is a
description howto create custom extensions.

Extensions are like every other FreeCAD object and based on properties. All
information storage and persistence should be achieved by use of those.
Additional any number of methods can be added to provide functionality around
the properties. There are 3 small difference to normal objects:

  1. They must be derived from [Extension](../../d8/dc7/classApp_1_1Extension.html "Base class for all extension that can be added to a DocumentObject.") class
  2. Properties must be handled with special extension macros
  3. Extensions must be initialised This works as simple as 

class MyExtension : public [Extension](../../d8/dc7/classApp_1_1Extension.html
"Base class for all extension that can be added to a DocumentObject.") {

EXTENSION_PROPERTY_HEADER(MyExtension);

PropertyInt MyProp;

virtual bool
overridableMethod([DocumentObject](../../d6/d23/namespaceDocumentObject.html)*
obj) {};

};

EXTENSION_PROPERTY_SOURCE(App::MyExtension,
[App::Extension](../../d8/dc7/classApp_1_1Extension.html "Base class for all
extension that can be added to a DocumentObject."))

MyExtension::MyExtension() {

EXTENSION_ADD_PROPERTY(MyProp, (0)) *

[initExtension](../../d8/dc7/classApp_1_1Extension.html#a1ae201ccac2b97ba9107151b9e507def)(MyExtension::getExtensionClassTypeId());

}

typedef ExtensionPythonT<MyExtension> MyExtensionPython;

The special python extension type created above is important, as only those
python extensions can be added to an object from python. It does not work to
add the c++ version directly there.

Note that every method of the extension becomes part of the extended object
when added from c++. This means one should carefully design the API and make
only necessary methods public or protected. Every internal method should be
private.

The automatic availability of methods in the class does not hold for the
python interface, only for c++ classes. This is like every where else in
FreeCAD, there is no automatic creation of python API from c++ classes. Hence
the extension creator must also create a custom python object of its
extension, which works exactly like the normal FreeCAD python object workflow.
There is nothing special at all for extension python objects, the normal xml +
imp.cpp approach is used. It must only be taken care that the objects father
is the correct extension base class. Of course also make sure your extension
returns the correct python object in its "getPyObject" call. Every method you
create in the extensions python will be later added to an extended object.
This happens automatically for both, c++ and python extension, if
"getPyObject" returns the correct python object. No extra work needs to be
done.

A special case that needs to be handled for extensions is the possibility of
overridden methods. Often it is desired to customise extension behaviour by
allowing the user to override methods provided by the extension. On c++ side
this is trivial, such methods are simply marked as "virtual" and can than be
overridden in any derived class. This is more involved for the python
interface and here special care needs to be taken.

As already seen above one needs to create a special ExtensionPythonT<> object
for extension from python. This is done exactly for the purpose of allowing to
have overridable methods. The
[ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html "Generic
Python extension class which allows every extension derived class to behave as
a Python exten...") wrapper adds a proxy property which holds a
[PyObject](../../df/d1b/classPyObject.html) which itself will contain the
implementations for the overridden methods. This design is equal to the
ObjectPythonT<> design of normal document objects. As this wrapper inherits
the c++ extension class it can also override the virtual functions the user
designed to be overridden. What it should do at a call of the virtual method
is to check if this method is implemented in the proxy object and if so call
it, and if not call the normal c++ version. It is the extensions creators
responsibility to implement this check and call behaviour for every
overridable method. This is done by creating a custom wrapper just like
ExtensionPythonT<> and overriding all virtual methods.

template<typename ExtensionT> class MyExtensionPythonT : public
[ExtensionT](../../df/d73/classExtensionT.html) {

public:

MyExtensionPythonT() {}

virtual ~MyExtensionPythonT() {}

virtual bool
overridableMethod([DocumentObject](../../d6/d23/namespaceDocumentObject.html)*
obj) override {

Py::Object pyobj = Py::asObject(obj->getPyObject());

EXTENSION_PROXY_ONEARG(allowObject, pyobj);

if(result.isNone())

ExtensionT::allowObject(obj);

if(result.isBoolean())

return result.isTrue();

return false;

};

};

@Note As seen in the code there are multiple helper macros to ease the
repetitive work of querying and calling methods of the proxy object. See the
macro documentation for how to use them.

To ensure that your wrapper is used when a extension is created from python
the extension type must be exposed as follows:

typedef
[ExtensionPythonT<MyExtensionPythonT<MyExtension>](../../d7/d86/classApp_1_1ExtensionPythonT.html
"Generic Python extension class which allows every extension derived class to
behave as a Python exten...")> MyExtensionPython;

This boilerplate is absolutely necessary to allow overridable methods in
python and it is the extension creator's responsibility to ensure full
implementation.

## Constructor & Destructor Documentation

## ◆ Extension()

Extension::Extension  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~Extension()

| Extension::~Extension  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3).

## Member Function Documentation

## ◆ extensionGetPropertyByName()

| [Property](../../d0/da9/classApp_1_1Property.html) * Extension::extensionGetPropertyByName  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
find a property by its name

Reimplemented in
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9673e9e742c402f3fb8c1ad6f5cdadad).

Referenced by
[App::LinkBaseExtension::extensionGetPropertyByName()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9673e9e742c402f3fb8c1ad6f5cdadad).

## ◆ extensionGetPropertyDocumentation() [1/2]

| const char * Extension::extensionGetPropertyDocumentation  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")

## ◆ extensionGetPropertyDocumentation() [2/2]

| const char * Extension::extensionGetPropertyDocumentation  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")

## ◆ extensionGetPropertyGroup() [1/2]

| const char * Extension::extensionGetPropertyGroup  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")

## ◆ extensionGetPropertyGroup() [2/2]

| const char * Extension::extensionGetPropertyGroup  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")

## ◆ extensionGetPropertyList()

| void Extension::extensionGetPropertyList  | ( | std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > & | _List_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get all properties of the class (including properties of the parent)

## ◆ extensionGetPropertyMap()

| void Extension::extensionGetPropertyMap  | ( | std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > & | _Map_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get all properties of the class (including properties of the parent)

## ◆ extensionGetPropertyName()

| const char * Extension::extensionGetPropertyName  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the name of a property

Referenced by
[App::LinkBaseExtension::setProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770).

## ◆ extensionGetPropertyType() [1/2]

| short [int](../../d1/da0/classint.html) Extension::extensionGetPropertyType  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Type of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")

## ◆ extensionGetPropertyType() [2/2]

| short [int](../../d1/da0/classint.html) Extension::extensionGetPropertyType  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Type of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")

## ◆ extensionIsDerivedFrom()

[bool](../../d9/db9/classbool.html) App::Extension::extensionIsDerivedFrom  | ( | const [Base::Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[App::LinkBaseExtension::getTrueLinkedObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ac819857582a99f5787a1cd5c3b5b26b1).

## ◆ extensionOnChanged()

| virtual void App::Extension::extensionOnChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _p_| ) |   
---|---|---|---|---|---  
protectedvirtual  
  
Reimplemented in
[Part::AttachExtension](../../dc/d47/classPart_1_1AttachExtension.html#ac73db2d8f32ca41b89157b47edce44c1),
[Part::PrismExtension](../../d3/dbb/classPart_1_1PrismExtension.html#ae032c7a9c8dbca5b1afae0de00363d9f),
[Gui::ViewProviderLinkObserver](../../d5/d06/classGui_1_1ViewProviderLinkObserver.html#a36e17a83913add9aba46e3c18199dfb2),
[PartGui::ViewProviderSplineExtension](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#a136922fdf38b223d79d10d64a60380ae),
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487),
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f),
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#acfd0dd3d0677653d2da7fc2a4cdcd3c5),
and
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42).

Referenced by
[Part::AttachExtension::extensionOnChanged()](../../dc/d47/classPart_1_1AttachExtension.html#ac73db2d8f32ca41b89157b47edce44c1),
[Part::PrismExtension::extensionOnChanged()](../../d3/dbb/classPart_1_1PrismExtension.html#ae032c7a9c8dbca5b1afae0de00363d9f),
[PartGui::ViewProviderSplineExtension::extensionOnChanged()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#a136922fdf38b223d79d10d64a60380ae),
[App::GroupExtension::extensionOnChanged()](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f),
and
[App::LinkBaseExtension::extensionOnChanged()](../../da/dd9/classApp_1_1LinkBaseExtension.html#acfd0dd3d0677653d2da7fc2a4cdcd3c5).

## ◆ extensionRestore()

| virtual void App::Extension::extensionRestore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ extensionSave()

| virtual void App::Extension::extensionSave  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
virtual  
  
## ◆ getExtendedContainer() [1/2]

[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) * App::Extension::getExtendedContainer  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[App::GeoFeatureGroupExtension::extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[App::GroupExtension::extensionGetSubObject()](../../da/d3a/classApp_1_1GroupExtension.html#a9f6afe4878329f62b99288df7224cec2),
[Gui::ViewProviderLinkObserver::extensionModeSwitchChange()](../../d5/d06/classGui_1_1ViewProviderLinkObserver.html#a31b474837d67d6d098ad152a2583da17),
[Gui::ViewProviderLinkObserver::extensionOnChanged()](../../d5/d06/classGui_1_1ViewProviderLinkObserver.html#a36e17a83913add9aba46e3c18199dfb2),
[Gui::ViewProviderLinkObserver::extensionReattach()](../../d5/d06/classGui_1_1ViewProviderLinkObserver.html#ab5b0003ca86e9d206720db4e4af11e5b),
[App::LinkBaseExtension::getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a57b46869e220d668ce2184446b7d6f80),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af6e17e520cf9b556992786cb5d57e911),
[Gui::ViewProviderExtension::getExtendedViewProvider()](../../d5/db8/classGui_1_1ViewProviderExtension.html#a3bc1434c0b8c077a46c3c8ead596c11e),
and
[App::GeoFeatureGroupExtension::placement()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a4cd1b76960dc22c7a5d5775c54ba76fb).

## ◆ getExtendedContainer() [2/2]

const [App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) * App::Extension::getExtendedContainer  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getExtensionPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * Extension::getExtensionPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[Gui::ViewProviderExtension](../../d5/db8/classGui_1_1ViewProviderExtension.html#ad4af3c8695fe1fba17e177f39390f5ec),
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a254f58c97024cd7e86fec56544fb77b1),
[Part::AttachExtension](../../dc/d47/classPart_1_1AttachExtension.html#a155d047fcb333e7b8f42c4082f8bb12c),
[TechDraw::CosmeticExtension](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#a14c4a05d3113aca24f35203981ec15db),
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a860f82302ebbf404b14cca69adc9ff36),
and
[App::LinkBaseExtension](../../da/dd9/classApp_1_1LinkBaseExtension.html#af1063baf3790a0275959a311d0c7a93f).

References
[ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3).

## ◆ initExtension()

| void Extension::initExtension  | ( | [App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) *  | _obj_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a74933934579b51ddd24efdd5be7bb3ba).

References
[Base::Type::isBad()](../../dc/dee/classBase_1_1Type.html#ab091b5ccf4f8e3c7c59cb05dde3c2fcb),
and
[App::ExtensionContainer::registerExtension()](../../d6/d76/classApp_1_1ExtensionContainer.html#a007eb07d5313eaa01d14462d7b7d960d).

Referenced by
[Part::Cylinder::Cylinder()](../../dd/d12/classPart_1_1Cylinder.html#a01dc978cb576f834b9545e43d4dad2a2),
[PartDesign::Cylinder::Cylinder()](../../dc/d28/classPartDesign_1_1Cylinder.html#a7aa3ff5473e8dcabe9a85c97ad971eb3),
[PartDesign::FeaturePrimitive::FeaturePrimitive()](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#aabeb2147e16220313a1c8b9841789380),
[App::GeoFeatureGroupExtension::initExtension()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a74933934579b51ddd24efdd5be7bb3ba),
[App::Link::Link()](../../df/d9b/classApp_1_1Link.html#aaa7d89775e277b9041d59133bd07d43d),
[App::LinkElement::LinkElement()](../../d0/d3e/classApp_1_1LinkElement.html#a798d5faabb622c3f410d12c0e0ac04eb),
[App::LinkGroup::LinkGroup()](../../de/d15/classApp_1_1LinkGroup.html#abb625a0644ad804d3fd87b227f37443b),
[Part::Prism::Prism()](../../dc/d69/classPart_1_1Prism.html#aa84930a585c7817f74a14d95ea74cb5a),
[PartDesign::Prism::Prism()](../../d9/daf/classPartDesign_1_1Prism.html#aadee90492364a044a7c2c59cf8109997),
[PartDesignGui::ViewProvider::ViewProvider()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#aa9e2dc9a40d2e0f70d562c32078a8293),
[PartDesignGui::ViewProviderBody::ViewProviderBody()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a0ff2a0f3f43bc41de3c5da6d9a05dc6b),
[PartDesignGui::ViewProviderBoolean::ViewProviderBoolean()](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#accb99f2dc304e0aec6d077bad7e4b48c),
[PartDesignGui::ViewProviderDatum::ViewProviderDatum()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#adf0685fe5a17533d5150eee8e625d03a),
and
[SketcherGui::ViewProviderSketch::ViewProviderSketch()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ada41c9affbe80077616db98a10a89641).

## ◆ initExtensionSubclass()

| void Extension::initExtensionSubclass  | ( | [Base::Type](../../dc/dee/classBase_1_1Type.html) & | _toInit_ ,   
---|---|---|---  
|  | const char *  | _ClassName_ ,   
|  | const char *  | _ParentName_ ,   
|  | [Base::Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) | _method_ = `nullptr`  
| ) | |   
staticprotected  
  
References
[Base::Type::badType()](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76),
[Base::Type::createType()](../../dc/dee/classBase_1_1Type.html#abdc2ccb5c9c300a5278b39db5e321cc0),
and
[Base::Type::fromName()](../../dc/dee/classBase_1_1Type.html#a7fd6fce9272b7886af7a58d2af987c42).

## ◆ initExtensionType()

| void Extension::initExtensionType  | ( | [Base::Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |   
---|---|---|---|---|---  
protected  
  
References
[Base::Type::isBad()](../../dc/dee/classBase_1_1Type.html#ab091b5ccf4f8e3c7c59cb05dde3c2fcb).

Referenced by
[App::GroupExtension::GroupExtension()](../../da/d3a/classApp_1_1GroupExtension.html#afd7849b2e26ce7e3ba33ba850054854a).

## ◆ isPythonExtension()

[bool](../../d9/db9/classbool.html) App::Extension::isPythonExtension  | ( | | ) |   
---|---|---|---|---  
  
## ◆ name()

std::string Extension::name  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Base::Type::getName()](../../dc/dee/classBase_1_1Type.html#a861a2f6bd2cd2c2df7846e202f0ce137),
and
[Base::Type::isBad()](../../dc/dee/classBase_1_1Type.html#ab091b5ccf4f8e3c7c59cb05dde3c2fcb).

Referenced by
[draftguitools.gui_groups.Ui_AddNamedGroup::accept()](../../d3/df7/classdraftguitools_1_1gui__groups_1_1Ui__AddNamedGroup.html#a9ea5973817eab7d74792f5b109a01466),
[prototype.Node::addtofreecad()](../../d2/d62/classprototype_1_1Node.html#adc095cc5636da029d1e0d9cef8859701),
[Addon.Addon::disable()](../../d8/d91/classAddon_1_1Addon.html#ae714705a38afe9f13cd2b17580178b31),
[Addon.Addon::enable()](../../d8/d91/classAddon_1_1Addon.html#a79d327ec9a0b4e85e9e96cfad4003ed6),
[App::LinkBaseExtension::extensionGetSubObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a666a0bbcc82f6538d3dfca95e4937ad5),
[PartDesignGui::ViewProviderDressUp::featureName()](../../dd/dfd/classPartDesignGui_1_1ViewProviderDressUp.html#a3abbd64851bfd174fb0f088d853826a4),
[addonmanager_macro.Macro::filename()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a5de4e6a1f3c41dce24066111955cd706),
[gzip_utf8.GzipFile::filename()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ab56fe84a4eb08c44e7a0026280c01229),
[addonmanager_macro.Macro::fill_details_from_code()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a49b8d021a9b8255f8a490e880eb15489),
[addonmanager_macro.Macro::fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[Addon.Addon::get_cached_icon_filename()](../../d8/d91/classAddon_1_1Addon.html#a7b026027a2904028032edbe3e99e2cbd),
[App::LinkBaseExtension::getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
[ifc4.ifcapproval::hasidentifierorname()](../../df/d91/classifc4_1_1ifcapproval.html#a54f558ba3b17fad5fc6579e9d5f50947),
[addonmanager_macro.Macro::install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
[Addon.Addon::is_disabled()](../../d8/d91/classAddon_1_1Addon.html#a5752a95fcf0c51ed06f9841b381d3e50),
[femsolver.elmer.sifio.Section::keys()](../../db/dab/classfemsolver_1_1elmer_1_1sifio_1_1Section.html#ab5b099447f66f33743850697f0e20de4),
[automotive_design.si_unit::named_unit_dimensions()](../../d5/d77/classautomotive__design_1_1si__unit.html#a68eb7954eb09daa334bc8f2c2abbe5f9),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction::output()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aeedd5f59969cc27432880d1916f3d7f9),
[prototype.Node::pprint()](../../d2/d62/classprototype_1_1Node.html#a5ae181c34e48238d2364b0ba4960c252),
[prototype.Node::pprint2()](../../d2/d62/classprototype_1_1Node.html#aaedcc4ba1fb305c7ddcc025235043cd5),
[PathScripts.PathSetupSheetGui.OpTaskPanel::propertyGroup()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a69cbbaadcb9cff7b526af2c743041d7b),
[PathScripts.PathSetupSheetGui.OpTaskPanel::propertyName()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#ad9bd0e0149d1bc42fc8e89a290de4910),
[PathScripts.PathJobGui.TaskPanel::reject()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a54fd97ba9b0060fa8fed8a43c360da0c),
[addonmanager_macro.Macro::remove()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ad13245288f8beb62d92cb458a2d2ce05),
[Sketcher::SketchObject::renameConstraint()](../../d9/dad/classSketcher_1_1SketchObject.html#a4010450c69e93e84c7345c32977a6000),
[Addon.Addon::to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
[ifc2x3.ifcexternalreference::wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc2x3.ifcdocumentreference::wr1()](../../df/dd6/classifc2x3_1_1ifcdocumentreference.html#a7d5fdb1cb0dee567c44834b868c5cdad),
[ifc4.ifcexternalreference::wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
[ifc4.ifcdocumentreference::wr1()](../../d7/d2b/classifc4_1_1ifcdocumentreference.html#a8779d74c67e647441d1fb20c76f44f97),
and
[automotive_design.general_property_association::wr2()](../../d2/df3/classautomotive__design_1_1general__property__association.html#ae7f46462c59bc4e541a5d2511631eb65).

## Friends And Related Function Documentation

## ◆ App::ExtensionContainer

| [friend](../../d7/d23/classfriend.html) class
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html)  
---  
friend  
  
## Member Data Documentation

## ◆ ExtensionPythonObject

| Py::SmartPtr App::Extension::ExtensionPythonObject  
---  
protected  
  
Referenced by
[getExtensionPyObject()](../../d8/dc7/classApp_1_1Extension.html#a77ffed10ef0c284b3a702caf46570168),
[Gui::ViewProviderExtension::getExtensionPyObject()](../../d5/db8/classGui_1_1ViewProviderExtension.html#ad4af3c8695fe1fba17e177f39390f5ec),
[App::DocumentObjectExtension::getExtensionPyObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a254f58c97024cd7e86fec56544fb77b1),
[Part::AttachExtension::getExtensionPyObject()](../../dc/d47/classPart_1_1AttachExtension.html#a155d047fcb333e7b8f42c4082f8bb12c),
[TechDraw::CosmeticExtension::getExtensionPyObject()](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#a14c4a05d3113aca24f35203981ec15db),
[App::GroupExtension::getExtensionPyObject()](../../da/d3a/classApp_1_1GroupExtension.html#a860f82302ebbf404b14cca69adc9ff36),
[App::LinkBaseExtension::getExtensionPyObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#af1063baf3790a0275959a311d0c7a93f),
and
[~Extension()](../../d8/dc7/classApp_1_1Extension.html#a52c2b4e48fa3f78511b72d55fefcb48c).

## ◆ m_isPythonExtension

| [bool](../../d9/db9/classbool.html) App::Extension::m_isPythonExtension =
false  
---  
protected  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Extension.h
  * FreeCAD/src/App/Extension.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

