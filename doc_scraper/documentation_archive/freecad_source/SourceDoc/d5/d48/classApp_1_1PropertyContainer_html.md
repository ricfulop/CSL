---
url: https://freecad.github.io/SourceDoc/d5/d48/classApp_1_1PropertyContainer.html
scraped_at: 2025-09-08T14:54:32.543188
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)

[List of all members](../../dd/d76/classApp_1_1PropertyContainer-members.html) | Public Member Functions | Protected Member Functions | Static Protected Member Functions | Protected Attributes | Friends

App::PropertyContainer Class Reference

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all classes with properties.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#details)

`#include <PropertyContainer.h>`

##  Public Member Functions  
  
---  
virtual [App::Property](../../d0/da9/classApp_1_1Property.html) * | [addDynamicProperty](../../d5/d48/classApp_1_1PropertyContainer.html#aeb460dcdedde87f84dbab68d0865bfa6) (const char *[type](../../d9/d98/classtype.html), const char *name=nullptr, const char *group=nullptr, const char *doc=nullptr, short attr=0, [bool](../../d9/db9/classbool.html) ro=false, [bool](../../d9/db9/classbool.html) hidden=false)  
[bool](../../d9/db9/classbool.html) | [changeDynamicProperty](../../d5/d48/classApp_1_1PropertyContainer.html#a322267f4f7ee6ee360535cdc5dce3612) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop, const char *group, const char *doc)  
virtual void | [editProperty](../../d5/d48/classApp_1_1PropertyContainer.html#a001e36affede2983bb0ac4852f2fc617) (const char *)  
virtual [App::Property](../../d0/da9/classApp_1_1Property.html) * | [getDynamicPropertyByName](../../d5/d48/classApp_1_1PropertyContainer.html#aa61e4c2e94abf8310ff9d790e4b54564) (const char *name) const  
[DynamicProperty::PropData](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html) | [getDynamicPropertyData](../../d5/d48/classApp_1_1PropertyContainer.html#aa6ac51c527bc5f13d8d6d5ddc4e51f2e) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
virtual std::vector< std::string > | [getDynamicPropertyNames](../../d5/d48/classApp_1_1PropertyContainer.html#a71fa8d125dc74b919e994a79985f601b) () const  
virtual std::string | [getFullName](../../d5/d48/classApp_1_1PropertyContainer.html#a331110f1aeffb0a907ac2b74f78cc69d) () const  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d5/d48/classApp_1_1PropertyContainer.html#a8c5a34456c147122cd31f15a1b3c5694) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a8c5a34456c147122cd31f15a1b3c5694)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [getPropertyByName](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2) (const char *name) const  
| find a property by its name
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2)  
  
virtual const char * | [getPropertyDocumentation](../../d5/d48/classApp_1_1PropertyContainer.html#ad0513de3a16613c999042b9e6f7a2b50) (const char *name) const  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ad0513de3a16613c999042b9e6f7a2b50)  
  
virtual const char * | [getPropertyDocumentation](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912)  
  
virtual const char * | [getPropertyGroup](../../d5/d48/classApp_1_1PropertyContainer.html#a88ec0df8c43f5dd99b8ec7290dfc0c4a) (const char *name) const  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a88ec0df8c43f5dd99b8ec7290dfc0c4a)  
  
virtual const char * | [getPropertyGroup](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356)  
  
virtual void | [getPropertyList](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a) (std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > &List) const  
| get all properties of the class (including properties of the parent)
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a)  
  
virtual void | [getPropertyMap](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8) (std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > &Map) const  
| get all properties of the class (including properties of the parent)
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8)  
  
virtual const char * | [getPropertyName](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the name of a property
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981)  
  
virtual void | [getPropertyNamedList](../../d5/d48/classApp_1_1PropertyContainer.html#ac1db173138f821f169de2b20111c935f) (std::vector< std::pair< const char *, [Property](../../d0/da9/classApp_1_1Property.html) * > > &List) const  
| get all properties with their names, may contain duplicates and aliases
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ac1db173138f821f169de2b20111c935f)  
  
const char * | [getPropertyPrefix](../../d5/d48/classApp_1_1PropertyContainer.html#afd2652f19f3b1db90309c5a69713507c) () const  
virtual short | [getPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#a4bd6348aaae6cbfbcbf45bd5077e4dc4) (const char *name) const  
| get the Type of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a4bd6348aaae6cbfbcbf45bd5077e4dc4)  
  
virtual short | [getPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Type of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510)  
  
[bool](../../d9/db9/classbool.html) | [isHidden](../../d5/d48/classApp_1_1PropertyContainer.html#a1a89b20166f4e4a3feea04a84179d1ed) (const char *name) const  
| check if the named property is hidden
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a1a89b20166f4e4a3feea04a84179d1ed)  
  
[bool](../../d9/db9/classbool.html) | [isHidden](../../d5/d48/classApp_1_1PropertyContainer.html#a70f7657757146a64ef861f0490b02374) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| check if the property is hidden
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a70f7657757146a64ef861f0490b02374)  
  
[bool](../../d9/db9/classbool.html) | [isReadOnly](../../d5/d48/classApp_1_1PropertyContainer.html#a7375800ad653da01d4b5a98f5fb69799) (const char *name) const  
| check if the named property is read-only
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a7375800ad653da01d4b5a98f5fb69799)  
  
[bool](../../d9/db9/classbool.html) | [isReadOnly](../../d5/d48/classApp_1_1PropertyContainer.html#ae9a54472ac2185af2717b4b220439082) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| check if the property is read-only
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ae9a54472ac2185af2717b4b220439082)  
  
virtual void | [onPropertyStatusChanged](../../d5/d48/classApp_1_1PropertyContainer.html#a25dc796f1aecab39ceeed8335097b758) (const [Property](../../d0/da9/classApp_1_1Property.html) &prop, unsigned long oldStatus)  
|
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#af08e2297f31f338356f8eb8f2000ff97)
()  
| A constructor.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#af08e2297f31f338356f8eb8f2000ff97)  
  
virtual [bool](../../d9/db9/classbool.html) | [removeDynamicProperty](../../d5/d48/classApp_1_1PropertyContainer.html#a7e5425268a06b3e8a12f45abbbcfd653) (const char *name)  
virtual void | [Restore](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944)  
  
virtual void | [Save](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482)  
  
void | [setPropertyPrefix](../../d5/d48/classApp_1_1PropertyContainer.html#aeac678dd3506bf850148f891fe368446) (const char *prefix)  
void | [setPropertyStatus](../../d5/d48/classApp_1_1PropertyContainer.html#a6be7980b23d8805f2b19daf2b70778ed) (unsigned char bit, [bool](../../d9/db9/classbool.html) value)  
| set the Status bit of all properties at once
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a6be7980b23d8805f2b19daf2b70778ed)  
  
virtual | [~PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#abca525c7322e6aa891390002c1b8b309) ()  
| A destructor.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#abca525c7322e6aa891390002c1b8b309)  
  
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
  
  
##  Protected Member Functions  
  
---  
virtual const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) & | [getPropertyData](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84) (void) const  
virtual void | [handleChangedPropertyName](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *TypeName, const char *PropName)  
|
[PropertyContainer::handleChangedPropertyName](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573
"PropertyContainer::handleChangedPropertyName is called during restore to
possibly fix reading of olde...") is called during restore to possibly fix
reading of older versions of this property container.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573)  
  
virtual void | [handleChangedPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *TypeName, [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
|
[PropertyContainer::handleChangedPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923
"PropertyContainer::handleChangedPropertyType is called during restore to
possibly fix reading of olde...") is called during restore to possibly fix
reading of older versions of the property container.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923)  
  
virtual void | [onBeforeChange](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057) (const [Property](../../d0/da9/classApp_1_1Property.html) *)  
| get called before the value is changed
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057)  
  
virtual void | [onChanged](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34) (const [Property](../../d0/da9/classApp_1_1Property.html) *)  
| get called by the container when a property has changed
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34)  
  
  
##  Static Protected Member Functions  
  
---  
static const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) * | [getPropertyDataPtr](../../d5/d48/classApp_1_1PropertyContainer.html#a8649f534ecaa91393925fa514ed29e4b) (void)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
##  Protected Attributes  
  
---  
[DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html) | [dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99)  
  
##  Friends  
  
---  
class | [DynamicProperty](../../d5/d48/classApp_1_1PropertyContainer.html#adf6ce0d47bb0e4936b77e055ae1a1da4)  
class | [Property](../../d5/d48/classApp_1_1PropertyContainer.html#a386f5a9cf65610cb62143865e5637272)  
  
##  Additional Inherited Members  
  
---  
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
  
## Detailed Description

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all classes with properties.

## Constructor & Destructor Documentation

## ◆ PropertyContainer()

PropertyContainer::PropertyContainer  | ( | | ) |   
---|---|---|---|---  
  
A constructor.

A more elaborate description of the constructor.

## ◆ ~PropertyContainer()

| PropertyContainer::~PropertyContainer  | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ addDynamicProperty()

| [App::Property](../../d0/da9/classApp_1_1Property.html) * PropertyContainer::addDynamicProperty  | ( | const char *  | _type_ ,   
---|---|---|---  
|  | const char *  | _name_ = `nullptr`,   
|  | const char *  | _group_ = `nullptr`,   
|  | const char *  | _doc_ = `nullptr`,   
|  | short  | _attr_ = `0`,   
|  | [bool](../../d9/db9/classbool.html) | _ro_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _hidden_ = `false`  
| ) | |   
virtual  
  
Reimplemented in
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#abf2aa7beac95fbed58ef392808477218),
and
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a0b66cab9ff390bb91593786721612aef).

References
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
and
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99).

Referenced by
[Gui::ViewProviderDocumentObject::addDynamicProperty()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a0b66cab9ff390bb91593786721612aef),
and
[App::TransactionObject::applyChn()](../../d9/d02/classApp_1_1TransactionObject.html#ae828131a91ad93ac2f20a51eeadecf70).

## ◆ changeDynamicProperty()

[bool](../../d9/db9/classbool.html) App::PropertyContainer::changeDynamicProperty  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_ ,   
---|---|---|---  
|  | const char *  | _group_ ,   
|  | const char *  | _doc_  
| ) | |   
  
## ◆ editProperty()

| virtual void App::PropertyContainer::editProperty  | ( | const char *  | | ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ getDynamicPropertyByName()

| virtual [App::Property](../../d0/da9/classApp_1_1Property.html) * App::PropertyContainer::getDynamicPropertyByName  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#abc0bcc742f7ac495fd6c3a44fe7e6e60).

Referenced by
[App::TransactionObject::applyChn()](../../d9/d02/classApp_1_1TransactionObject.html#ae828131a91ad93ac2f20a51eeadecf70),
[Gui::ViewProviderDocumentObject::removeDynamicProperty()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a4d47313a825a2051c9a667ed4e7a1346),
and
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83).

## ◆ getDynamicPropertyData()

[DynamicProperty::PropData](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html) App::PropertyContainer::getDynamicPropertyData  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[App::TransactionObject::addOrRemoveProperty()](../../d9/d02/classApp_1_1TransactionObject.html#a1a9c63db207f7e24ed6918877c134764),
and
[App::TransactionObject::setProperty()](../../d9/d02/classApp_1_1TransactionObject.html#ad234dbb98feea5e3fb448aa2b0825207).

## ◆ getDynamicPropertyNames()

| virtual std::vector< std::string > App::PropertyContainer::getDynamicPropertyNames  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
## ◆ getFullName()

| virtual std::string App::PropertyContainer::getFullName  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reimplemented in
[App::Document](../../d8/d3e/classApp_1_1Document.html#af007ba04581112132745321d40e89d75),
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#ab9ad25e711d56a5d6c8ba0f7638a8a62),
and
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a0943bc30138036868c395bd324c321b2).

Referenced by
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[App::Property::getFullName()](../../d0/da9/classApp_1_1Property.html#a0b1289a60e57856c8dae70fafd619dd2),
and
[App::PropertyLinkBase::tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) PropertyContainer::getMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9).

Reimplemented in
[TechDraw::DrawParametricTemplate](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#a20ecb322cb917b1296743d6ee09498e4),
[TechDraw::DrawSVGTemplate](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a3922fe662498c7af4bcba1534cc8a3ee),
[TechDraw::DrawTemplate](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a8061d4341f265a7eecd653cbbeffc563),
[App::Document](../../d8/d3e/classApp_1_1Document.html#a5a28fe2ed0a864dcd294f81bf2fa3043),
and
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a904bc155ca037a1eb404b3778b8cd603).

References
[getPropertyMap()](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8).

Referenced by
[App::Document::getMemSize()](../../d8/d3e/classApp_1_1Document.html#a5a28fe2ed0a864dcd294f81bf2fa3043).

## ◆ getPropertyByName()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyContainer::getPropertyByName  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
find a property by its name

Reimplemented in
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#af40fb7fff53d89116462ae1816d43478),
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897),
and
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a17a9af10ec6818cb73aff3e1fdc9c5f7).

References
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[App::DynamicProperty::getDynamicPropertyByName()](../../d5/d76/classApp_1_1DynamicProperty.html#a41130d5c69a0c4cf3f4e19dab20de459),
[App::PropertyData::getPropertyByName()](../../d2/d02/structApp_1_1PropertyData.html#ac91725ecc43ae8b7a032d0dbcd91ae41),
and
[getPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84).

Referenced by
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[App::ExtensionContainer::getPropertyByName()](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897),
[getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a4bd6348aaae6cbfbcbf45bd5077e4dc4),
and
[Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944).

## ◆ getPropertyData()

| const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) & PropertyContainer::getPropertyData  | ( | void  | | ) |  const  
---|---|---|---|---|---  
protectedvirtual  
  
Referenced by
[getPropertyByName()](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2),
[getPropertyDocumentation()](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912),
[getPropertyGroup()](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356),
[getPropertyList()](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a),
[getPropertyMap()](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8),
[getPropertyName()](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981),
and
[getPropertyNamedList()](../../d5/d48/classApp_1_1PropertyContainer.html#ac1db173138f821f169de2b20111c935f).

## ◆ getPropertyDataPtr()

| const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) * PropertyContainer::getPropertyDataPtr  | ( | void  | | ) |   
---|---|---|---|---|---  
staticprotected  
  
## ◆ getPropertyDocumentation() [1/2]

| const char * PropertyContainer::getPropertyDocumentation  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")

Reimplemented in
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#afd218927cb4c252f090dd1f377ced7de).

References
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[App::PropertyData::getDocumentation()](../../d2/d02/structApp_1_1PropertyData.html#ac5fa377a98454621a8b23dde9dd57dad),
[getPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84),
and
[App::DynamicProperty::getPropertyDocumentation()](../../d5/d76/classApp_1_1DynamicProperty.html#a165ad3da898b9a9e30a87ea2d23279c5).

## ◆ getPropertyDocumentation() [2/2]

| const char * PropertyContainer::getPropertyDocumentation  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")

Reimplemented in
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a4f2af686b6d232b650bf512e0bbdc223).

References
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[App::PropertyData::getDocumentation()](../../d2/d02/structApp_1_1PropertyData.html#ac5fa377a98454621a8b23dde9dd57dad),
[getPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84),
and
[App::DynamicProperty::getPropertyDocumentation()](../../d5/d76/classApp_1_1DynamicProperty.html#a165ad3da898b9a9e30a87ea2d23279c5).

Referenced by
[App::Property::getDocumentation()](../../d0/da9/classApp_1_1Property.html#ada9481ae19a85f023c5597d57f8c809b),
and
[App::ExtensionContainer::getPropertyDocumentation()](../../d6/d76/classApp_1_1ExtensionContainer.html#a4f2af686b6d232b650bf512e0bbdc223).

## ◆ getPropertyGroup() [1/2]

| const char * PropertyContainer::getPropertyGroup  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")

Reimplemented in
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a4fba6aeb529e0bbe523bb2cd62d191fc).

References
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[App::PropertyData::getGroup()](../../d2/d02/structApp_1_1PropertyData.html#a4c0fd744dc4ee79240f8ff63bc1895cc),
[getPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84),
and
[App::DynamicProperty::getPropertyGroup()](../../d5/d76/classApp_1_1DynamicProperty.html#aa46af4e48d92adc936b42a9188b7fcd0).

## ◆ getPropertyGroup() [2/2]

| const char * PropertyContainer::getPropertyGroup  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")

Reimplemented in
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a0667cf5204a8854212a23fd5d53f5b1d).

References
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[App::PropertyData::getGroup()](../../d2/d02/structApp_1_1PropertyData.html#a4c0fd744dc4ee79240f8ff63bc1895cc),
[getPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84),
and
[App::DynamicProperty::getPropertyGroup()](../../d5/d76/classApp_1_1DynamicProperty.html#aa46af4e48d92adc936b42a9188b7fcd0).

Referenced by
[App::Property::getGroup()](../../d0/da9/classApp_1_1Property.html#ab815066b984a7d6c133b4c947a989fee),
and
[App::ExtensionContainer::getPropertyGroup()](../../d6/d76/classApp_1_1ExtensionContainer.html#a0667cf5204a8854212a23fd5d53f5b1d).

## ◆ getPropertyList()

| void PropertyContainer::getPropertyList  | ( | std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > & | _List_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get all properties of the class (including properties of the parent)

Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a849803da0f88ed79a6d4d24ec0e66b01),
and
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a4b980230637c28a4159575a8955c9fe6).

References
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[getPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84),
[App::PropertyData::getPropertyList()](../../d2/d02/structApp_1_1PropertyData.html#ac697b4d2ae7f2258097b5d63d508379f),
and
[App::DynamicProperty::getPropertyList()](../../d5/d76/classApp_1_1DynamicProperty.html#a4ba0df7e18f1b4b88088307283b5de62).

Referenced by
[App::ExtensionContainer::getPropertyList()](../../d6/d76/classApp_1_1ExtensionContainer.html#a4b980230637c28a4159575a8955c9fe6),
[PartDesignGui::isAnyNonPartDesignLinksTo()](../../dc/d12/namespacePartDesignGui.html#a763622795328f1193ce61804dc4c61b6),
[Gui::Application::reopen()](../../d9/da8/classGui_1_1Application.html#a7a21dfd4379a11fd6babb3a2a14d4b1a),
and
[setPropertyStatus()](../../d5/d48/classApp_1_1PropertyContainer.html#a6be7980b23d8805f2b19daf2b70778ed).

## ◆ getPropertyMap()

| void PropertyContainer::getPropertyMap  | ( | std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > & | _Map_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get all properties of the class (including properties of the parent)

Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a7190982dc42a5f66d3740ff5df29a294),
and
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a12d88a996edd035623450a5b8da10d03).

References
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[getPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84),
[App::PropertyData::getPropertyMap()](../../d2/d02/structApp_1_1PropertyData.html#aa53fb59fabeac2789a00247260af211e),
and
[App::DynamicProperty::getPropertyMap()](../../d5/d76/classApp_1_1DynamicProperty.html#a9423e1c11e7e1c07b658b2311cf4a1f6).

Referenced by
[getMemSize()](../../d5/d48/classApp_1_1PropertyContainer.html#a8c5a34456c147122cd31f15a1b3c5694),
[App::ExtensionContainer::getPropertyMap()](../../d6/d76/classApp_1_1ExtensionContainer.html#a12d88a996edd035623450a5b8da10d03),
and
[Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482).

## ◆ getPropertyName()

| const char * PropertyContainer::getPropertyName  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the name of a property

Reimplemented in
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a5d91112962ee5c459efa09469ebce4d0).

References
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[App::PropertyData::getName()](../../d2/d02/structApp_1_1PropertyData.html#a4dc58677d9d6ccb3577d49d7f4c7673b),
[getPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84),
and
[App::DynamicProperty::getPropertyName()](../../d5/d76/classApp_1_1DynamicProperty.html#ab367905c95b0b6ca675b14c9be23d7cf).

Referenced by
[App::ExtensionContainer::getPropertyName()](../../d6/d76/classApp_1_1ExtensionContainer.html#a5d91112962ee5c459efa09469ebce4d0).

## ◆ getPropertyNamedList()

| void PropertyContainer::getPropertyNamedList  | ( | std::vector< std::pair< const char *, [Property](../../d0/da9/classApp_1_1Property.html) * > > & | _List_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get all properties with their names, may contain duplicates and aliases

Reimplemented in
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#a2a3000c9994ba2a4720dc0768d4fa2c2).

References
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[getPropertyData()](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84),
[App::PropertyData::getPropertyNamedList()](../../d2/d02/structApp_1_1PropertyData.html#a62858579f4b81973d1661262e8c79146),
and
[App::DynamicProperty::getPropertyNamedList()](../../d5/d76/classApp_1_1DynamicProperty.html#ac5df12664197fc01d96a78a9f6d2a1cd).

## ◆ getPropertyPrefix()

const char * App::PropertyContainer::getPropertyPrefix  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getPropertyType() [1/2]

| short PropertyContainer::getPropertyType  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Type of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")

Reimplemented in
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#afc5151a1d5fa7822d9f6fd1bb4bc4004).

References
[getPropertyByName()](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2),
and
[getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510).

## ◆ getPropertyType() [2/2]

| short PropertyContainer::getPropertyType  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
virtual  
  
get the Type of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")

Reimplemented in
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#afd7697c47292ff6d6b7fce5bff86941f).

References
[App::Property::getType()](../../d0/da9/classApp_1_1Property.html#abc4967c88a5fc83c27a47f9534fdd510).

Referenced by
[getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a4bd6348aaae6cbfbcbf45bd5077e4dc4),
[App::ExtensionContainer::getPropertyType()](../../d6/d76/classApp_1_1ExtensionContainer.html#afd7697c47292ff6d6b7fce5bff86941f),
[isHidden()](../../d5/d48/classApp_1_1PropertyContainer.html#a70f7657757146a64ef861f0490b02374),
[isReadOnly()](../../d5/d48/classApp_1_1PropertyContainer.html#ae9a54472ac2185af2717b4b220439082),
and
[Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482).

## ◆ handleChangedPropertyName()

| void PropertyContainer::handleChangedPropertyName  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_ ,   
---|---|---|---  
|  | const char *  | _TypeName_ ,   
|  | const char *  | _PropName_  
| ) | |   
protectedvirtual  
  
[PropertyContainer::handleChangedPropertyName](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573
"PropertyContainer::handleChangedPropertyName is called during restore to
possibly fix reading of olde...") is called during restore to possibly fix
reading of older versions of this property container.

This method is typically called if the property on file has changed its name
in more recent versions.

The default implementation does nothing.

Parameters

     reader| The XML stream to read from.   
---|---  
TypeName| Name of property type on file.  
PropName| Name of property on file that does not exist in the container
anymore.  
  
Reimplemented in
[Fem::FemAnalysis](../../de/d36/classFem_1_1FemAnalysis.html#a77d4363b7c6734ec7754d6c4de10a481),
[Part::Circle](../../de/de4/classPart_1_1Circle.html#aac14a5128cb8850c0cd7f37ffc71e22a),
[Part::Ellipse](../../d6/d22/classPart_1_1Ellipse.html#a7448b87a31bf68edc8d6a6909613615b),
[PartDesign::ProfileBased](../../d8/d2f/classPartDesign_1_1ProfileBased.html#afbb7de5553cfce71f0d90927bedb61c9),
[App::Link](../../df/d9b/classApp_1_1Link.html#ad53bdeb93737a9d485d330f162c9373f),
[App::LinkElement](../../d0/d3e/classApp_1_1LinkElement.html#ab31c0206eafe2dc7d40c4287b9936a5a),
[Part::BodyBase](../../da/dc8/classPart_1_1BodyBase.html#a2038d6fd9d31b5033c193ca7a95d0b33),
[Part::Datum](../../db/d0b/classPart_1_1Datum.html#ad9affe075e94c4bceb410d5da48f2bc9),
[Part::Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html#ae7acc5eb90cfc5c1a97294ffd8a56c7c),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#ade4a5ba89c272644f606dc521471b9f6),
[PartDesign::Boolean](../../d2/d81/classPartDesign_1_1Boolean.html#ad635959d9d69278a1c46fbd6cc0f78f4),
[PartDesign::FeaturePrimitive](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a21a731f08dad1203dc6e0fbc5147c65e),
[Surface::Extend](../../d1/d22/classSurface_1_1Extend.html#aa2e1ed26c2018e7234938836df41545c),
[TechDraw::DrawViewBalloon](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a8f43bff2ef5b6712e7fd0546b639e6ef),
and
[TechDraw::DrawViewPart](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a29f8883b4bf72d388a134eb7ffce4d53).

Referenced by
[Fem::FemAnalysis::handleChangedPropertyName()](../../de/d36/classFem_1_1FemAnalysis.html#a77d4363b7c6734ec7754d6c4de10a481),
[PartDesign::ProfileBased::handleChangedPropertyName()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#afbb7de5553cfce71f0d90927bedb61c9),
[Part::BodyBase::handleChangedPropertyName()](../../da/dc8/classPart_1_1BodyBase.html#a2038d6fd9d31b5033c193ca7a95d0b33),
[Surface::Extend::handleChangedPropertyName()](../../d1/d22/classSurface_1_1Extend.html#aa2e1ed26c2018e7234938836df41545c),
[TechDraw::DrawViewBalloon::handleChangedPropertyName()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a8f43bff2ef5b6712e7fd0546b639e6ef),
[TechDraw::DrawViewPart::handleChangedPropertyName()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a29f8883b4bf72d388a134eb7ffce4d53),
and
[Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944).

## ◆ handleChangedPropertyType()

| void PropertyContainer::handleChangedPropertyType  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_ ,   
---|---|---|---  
|  | const char *  | _TypeName_ ,   
|  | [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_  
| ) | |   
protectedvirtual  
  
[PropertyContainer::handleChangedPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923
"PropertyContainer::handleChangedPropertyType is called during restore to
possibly fix reading of olde...") is called during restore to possibly fix
reading of older versions of the property container.

This method is typically called if the property on file has changed its type
in more recent versions.

The default implementation does nothing.

Parameters

     reader| The XML stream to read from.   
---|---  
TypeName| Name of property type on file.  
prop| Pointer to property to restore. Its type differs from TypeName.  
  
Reimplemented in
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ae012f9df13a4f5578d96a5e50ccb1b2d),
[Fem::FemPostDataAlongLineFilter](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#a1d60899654f9f7141ff2e7ef7aab1805),
[Mesh::Sphere](../../d1/d57/classMesh_1_1Sphere.html#af43262e6edb32fd6dcd686d877728c3a),
[Mesh::Ellipsoid](../../d2/dd6/classMesh_1_1Ellipsoid.html#ae21b7d81a6bc266b6505fa067ada71fa),
[Mesh::Cylinder](../../df/def/classMesh_1_1Cylinder.html#a698e2724dd6a682861aa49c3ca588abd),
[Mesh::Cone](../../d4/dbc/classMesh_1_1Cone.html#a88dde13a2f1e984c9d54e3f0836df079),
[Mesh::Torus](../../de/da3/classMesh_1_1Torus.html#aec1db0e864c1478a9a5e2fdf4f6c4614),
[Mesh::Cube](../../df/d68/classMesh_1_1Cube.html#a7a48689262a11f3e55ea4c4302f028dc),
[Part::Mirroring](../../dc/dac/classPart_1_1Mirroring.html#a177e7d2117a11729e6babd5c329f4be9),
[Part::Thickness](../../db/d73/classPart_1_1Thickness.html#a013b39370d11b7cb467ed7223d33d7a9),
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a4c2d97cecf5419da9ce703e47f8c1e6a),
[PartDesign::Fillet](../../d0/d50/classPartDesign_1_1Fillet.html#a4dec9f6780093c637468b21782cc0347),
[PartDesign::Helix](../../d3/d78/classPartDesign_1_1Helix.html#a9e6fc22b84b2f26eef4b4880af00b063),
[PartDesign::LinearPattern](../../d2/d86/classPartDesign_1_1LinearPattern.html#a9a99c3eb9dc74e11d68f4794666e6270),
[PartDesign::Loft](../../d0/deb/classPartDesign_1_1Loft.html#ad4ac633608d2e7a2ca80e98958160339),
[PartDesign::Pipe](../../da/d61/classPartDesign_1_1Pipe.html#a21ddc40aa9d476ee1455154c2e09f7ab),
[PartDesign::PolarPattern](../../da/d5b/classPartDesign_1_1PolarPattern.html#af05898fa5e67a75fbb102a48e07be8ef),
[PartDesign::Transformed](../../dd/de1/classPartDesign_1_1Transformed.html#a9e4288037e29095bf566a11f3f13fe12),
[TechDraw::DrawTile](../../da/d56/classTechDraw_1_1DrawTile.html#a449be4339583f4d9d8e4cedea6a7dce4),
[TechDraw::DrawViewAnnotation](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#adb0aa91e33022736bcb8d124cd9b295b),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a4a6246398d610494e2171cbbb1b8eb44),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a3ca6d7598ea8430e71e0f852c349b339),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9f55c50ca1618be5224195b46784c99b),
[TechDrawGui::ViewProviderRichAnno](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a2b7fcb5bb4cd203d5d467e29142523a3),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a1dbd73f06f25bca49644056da29aa920),
[App::Part](../../da/d8d/classApp_1_1Part.html#a1ac1cee5e3d630cb4259859238fc9acd),
[Part::Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html#a3b4551d03504c25446ede14dcf2309e3),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#a1e49f13eafbcb2ce0de44916a8407cf7),
[PartDesign::Chamfer](../../da/d6f/classPartDesign_1_1Chamfer.html#a8efe172f26b587a447f0bb5b183ae67b),
[PartDesign::ShapeBinder](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#ae4e96cdb35155567c8bbc77cb4dd3fd3),
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ada8edbc772ee47a87c785f17ab69df0f),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#adde1799122996153278b2c68d4fa9b80),
[TechDraw::DrawProjGroup](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a9a45f879e7b7c0cc6a6787be1c021f46),
[TechDraw::DrawView](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
and
[TechDraw::DrawViewBalloon](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a71fe79a13079b298255b09846c9b6582).

Referenced by
[Mesh::Sphere::handleChangedPropertyType()](../../d1/d57/classMesh_1_1Sphere.html#af43262e6edb32fd6dcd686d877728c3a),
[Mesh::Ellipsoid::handleChangedPropertyType()](../../d2/dd6/classMesh_1_1Ellipsoid.html#ae21b7d81a6bc266b6505fa067ada71fa),
[Mesh::Cylinder::handleChangedPropertyType()](../../df/def/classMesh_1_1Cylinder.html#a698e2724dd6a682861aa49c3ca588abd),
[Mesh::Cone::handleChangedPropertyType()](../../d4/dbc/classMesh_1_1Cone.html#a88dde13a2f1e984c9d54e3f0836df079),
[Mesh::Torus::handleChangedPropertyType()](../../de/da3/classMesh_1_1Torus.html#aec1db0e864c1478a9a5e2fdf4f6c4614),
[Mesh::Cube::handleChangedPropertyType()](../../df/d68/classMesh_1_1Cube.html#a7a48689262a11f3e55ea4c4302f028dc),
[Part::Mirroring::handleChangedPropertyType()](../../dc/dac/classPart_1_1Mirroring.html#a177e7d2117a11729e6babd5c329f4be9),
[Part::Thickness::handleChangedPropertyType()](../../db/d73/classPart_1_1Thickness.html#a013b39370d11b7cb467ed7223d33d7a9),
[PartGui::ViewProvider2DObjectGrid::handleChangedPropertyType()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a4c2d97cecf5419da9ce703e47f8c1e6a),
[PartDesign::Fillet::handleChangedPropertyType()](../../d0/d50/classPartDesign_1_1Fillet.html#a4dec9f6780093c637468b21782cc0347),
[PartDesign::Helix::handleChangedPropertyType()](../../d3/d78/classPartDesign_1_1Helix.html#a9e6fc22b84b2f26eef4b4880af00b063),
[PartDesign::Loft::handleChangedPropertyType()](../../d0/deb/classPartDesign_1_1Loft.html#ad4ac633608d2e7a2ca80e98958160339),
[PartDesign::Pipe::handleChangedPropertyType()](../../da/d61/classPartDesign_1_1Pipe.html#a21ddc40aa9d476ee1455154c2e09f7ab),
[PartDesign::Transformed::handleChangedPropertyType()](../../dd/de1/classPartDesign_1_1Transformed.html#a9e4288037e29095bf566a11f3f13fe12),
[TechDrawGui::ViewProviderBalloon::handleChangedPropertyType()](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a4a6246398d610494e2171cbbb1b8eb44),
[TechDrawGui::ViewProviderDimension::handleChangedPropertyType()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a3ca6d7598ea8430e71e0f852c349b339),
[TechDrawGui::ViewProviderLeader::handleChangedPropertyType()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9f55c50ca1618be5224195b46784c99b),
[TechDrawGui::ViewProviderRichAnno::handleChangedPropertyType()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a2b7fcb5bb4cd203d5d467e29142523a3),
[TechDrawGui::ViewProviderViewPart::handleChangedPropertyType()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a1dbd73f06f25bca49644056da29aa920),
[Part::Part2DObject::handleChangedPropertyType()](../../d9/d57/classPart_1_1Part2DObject.html#a3b4551d03504c25446ede14dcf2309e3),
[Part::Primitive::handleChangedPropertyType()](../../d2/d31/classPart_1_1Primitive.html#a1e49f13eafbcb2ce0de44916a8407cf7),
[PartDesign::Chamfer::handleChangedPropertyType()](../../da/d6f/classPartDesign_1_1Chamfer.html#a8efe172f26b587a447f0bb5b183ae67b),
[PartDesign::ShapeBinder::handleChangedPropertyType()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#ae4e96cdb35155567c8bbc77cb4dd3fd3),
[PartDesign::SubShapeBinder::handleChangedPropertyType()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ada8edbc772ee47a87c785f17ab69df0f),
and
[Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944).

## ◆ isHidden() [1/2]

[bool](../../d9/db9/classbool.html) PropertyContainer::isHidden  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
  
check if the named property is hidden

References
[getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510),
and
[App::Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6).

## ◆ isHidden() [2/2]

[bool](../../d9/db9/classbool.html) PropertyContainer::isHidden  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
  
check if the property is hidden

References
[getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510),
and
[App::Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6).

Referenced by
[Gui::Dialog::find_placement::operator()()](../../db/d20/classGui_1_1Dialog_1_1find__placement.html#a52917723bad2ec3993bd7adbe3804722).

## ◆ isReadOnly() [1/2]

[bool](../../d9/db9/classbool.html) PropertyContainer::isReadOnly  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
  
check if the named property is read-only

References
[getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510),
and
[App::Prop_ReadOnly](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a9bea209c7050543e2ceadef7ba0e9e75).

## ◆ isReadOnly() [2/2]

[bool](../../d9/db9/classbool.html) PropertyContainer::isReadOnly  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
  
check if the property is read-only

References
[getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510),
and
[App::Prop_ReadOnly](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a9bea209c7050543e2ceadef7ba0e9e75).

Referenced by
[Gui::Dialog::find_placement::operator()()](../../db/d20/classGui_1_1Dialog_1_1find__placement.html#a52917723bad2ec3993bd7adbe3804722),
and
[Gui::PropertyEditor::PropertyItem::setPropertyData()](../../d6/db3/classGui_1_1PropertyEditor_1_1PropertyItem.html#a9187fc6a2caad2f43e2cca20fa54e00c).

## ◆ onBeforeChange()

| virtual void App::PropertyContainer::onBeforeChange  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | | ) |   
---|---|---|---|---|---  
protectedvirtual  
  
get called before the value is changed

Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#aefc3f174999bdd4648769e65cfbcf399),
[Gui::ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html#a4ffbd2052a9e36ebb8047bb5f855c650),
[Drawing::FeaturePage](../../db/d0f/classDrawing_1_1FeaturePage.html#a7c55c251b8fe8c83f98a5e0defb88070),
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a8951ceface32a935d5305d79aa1626eb),
[Part::BodyBase](../../da/dc8/classPart_1_1BodyBase.html#a3bfb2f868776a6dddcc69f83842e8f44),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#ac9e00650dfe413e2c360aeb310020556),
[App::Document](../../d8/d3e/classApp_1_1Document.html#a84bc36d18a86fca95c88aa31308f0bf3),
and
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#a06538b0ebeb63aad6aa62794efd626aa).

Referenced by
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[Gui::ViewProvider::onBeforeChange()](../../d3/db3/classGui_1_1ViewProvider.html#a4ffbd2052a9e36ebb8047bb5f855c650),
and
[PathScripts.PathGui.QuantitySpinBox::updateProperty()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a8b9b202d7b495b666cb1f6b41ab2beb4).

## ◆ onChanged()

| virtual void App::PropertyContainer::onChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | | ) |   
---|---|---|---|---|---  
protectedvirtual  
  
get called by the container when a property has changed

Reimplemented in
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf),
[FemGui::ViewProviderFemPostPlaneFunction](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#aff4da6a421671244ed9f106adbaee37a),
[Part::Circle](../../de/de4/classPart_1_1Circle.html#aac82db0865d1e2eb55342a84cf91872e),
[Part::Vertex](../../de/d96/classPart_1_1Vertex.html#a9421cb9911928eae246b23f3590bc3ee),
[Part::Line](../../d3/dfe/classPart_1_1Line.html#ab63d1eeff0a1ad1773c06cca1d731017),
[Part::Ellipse](../../d6/d22/classPart_1_1Ellipse.html#aebecb9c21eca867973512232a720cc63),
[PartDesignGui::ViewProviderDatumCoordinateSystem](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a48324f18ce89cf9a307a32d54e3cfcc3),
[Surface::GeomFillSurface](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a3bfc3e08b782ee0cb3ccb98f8dd1600f),
[PartDesign::Chamfer](../../da/d6f/classPartDesign_1_1Chamfer.html#a778fc5826d5950fba6fb6e5a2d2208dd),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a838e11f3f3d9b47452ece92f8057bff1),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#abbbfdc1b1e66ea1ea4ba8a483794161d),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#aa4c52719f57d011b0a4f3bef4c68a016),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a74a77269f6962a4a975229ac51c582c7),
[TechDrawGui::ViewProviderRichAnno](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a338b45f77e146a3a179b2f7922de8d8d),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#acad7ad25b7e30c03fc13738bce5db1de),
[Gui::ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html#a825924c3bb8e3aaed03215ef12867392),
[Gui::ViewProviderAnnotation](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#a789aabe3e009284175581640dec663c3),
[Gui::ViewProviderAnnotationLabel](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a53d7de6d67521a3dadb7ae43c96869bc),
[Gui::ViewProviderGeometryObject](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[Gui::ViewProviderMeasureDistance](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a55ba8a09c4ee671752b6e88c3561d9e1),
[Gui::ViewProviderOrigin](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[Gui::ViewProviderOriginFeature](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a86520630c898707677753ccc3877eced),
[Gui::ViewProviderTextDocument](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a8d87ca622183dd3077563ad3d45c479b),
[Drawing::FeatureClip](../../d5/d4a/classDrawing_1_1FeatureClip.html#a2f703cc6f8d0f4d9e953a80ec936b8f0),
[Drawing::FeaturePage](../../db/d0f/classDrawing_1_1FeaturePage.html#a9c6b6897f29ff589163044d51b7e5c04),
[Drawing::FeatureViewSymbol](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#aaf6475415e3e3e4e35ad6d1cd034f7fc),
[Fem::Constraint](../../d0/d11/classFem_1_1Constraint.html#aec25bc397a1a87056079e3cd5a59d778),
[Fem::ConstraintBearing](../../df/d0a/classFem_1_1ConstraintBearing.html#ae81d9fda05994bd43bf81faf3acae5d6),
[Fem::ConstraintContact](../../db/d7c/classFem_1_1ConstraintContact.html#a2470d9364e84ea3c15f5873073f26539),
[Fem::ConstraintDisplacement](../../d5/d1c/classFem_1_1ConstraintDisplacement.html#a8525892f2c7183b75c1d8f2052f82401),
[Fem::ConstraintFixed](../../d1/d43/classFem_1_1ConstraintFixed.html#a2b9b87e9151f1571ab9cff619ec5547c),
[Fem::ConstraintFluidBoundary](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Fem::ConstraintForce](../../d6/d63/classFem_1_1ConstraintForce.html#aa19098735f62c480439948314f6532b3),
[Fem::ConstraintGear](../../d8/d55/classFem_1_1ConstraintGear.html#a971506b4ca246c3378e2755160ed4772),
[Fem::ConstraintHeatflux](../../de/dce/classFem_1_1ConstraintHeatflux.html#a0caeab069cf3e2fc8246aa163735d1e9),
[Fem::ConstraintInitialTemperature](../../da/d91/classFem_1_1ConstraintInitialTemperature.html#aa21e4c9c6cc31312e5147bbe1f8fcf05),
[Fem::ConstraintPlaneRotation](../../d7/d08/classFem_1_1ConstraintPlaneRotation.html#a668aafd16c5cf0565dde1072dd55a34a),
[Fem::ConstraintPressure](../../dd/d5e/classFem_1_1ConstraintPressure.html#a05ca046143c094c241c12702f7b820f7),
[Fem::ConstraintPulley](../../d3/dec/classFem_1_1ConstraintPulley.html#a6c23af9b8ba29b03f25163da9b75a41f),
[Fem::ConstraintSpring](../../dc/d42/classFem_1_1ConstraintSpring.html#ae67112c14de2dc75f749842b6591fcf8),
[Fem::ConstraintTemperature](../../d7/dff/classFem_1_1ConstraintTemperature.html#a74f2f9e94a2d9011490c09caab3c0da9),
[Fem::ConstraintTransform](../../d8/d3c/classFem_1_1ConstraintTransform.html#a38b893dee34272ad6bf0c6126aad561f),
[Fem::FemMeshObject](../../d5/d68/classFem_1_1FemMeshObject.html#aeea4f2e58af23fcd160a31ccea76cc6e),
[Fem::FemPostClipFilter](../../dc/d06/classFem_1_1FemPostClipFilter.html#a696285744236a6bf6e8c14f735034705),
[Fem::FemPostDataAlongLineFilter](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ae418afcb8e18abba84d16c2a645a434e),
[Fem::FemPostDataAtPointFilter](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#ae4bb2f96ee214db7c2bcb5a0afe0fdc4),
[Fem::FemPostScalarClipFilter](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a6c5243b230b4dac2cde71f28d04dcd53),
[Fem::FemPostWarpVectorFilter](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a64c913cbc86feb708504b94b931f1085),
[Fem::FemPostCutFilter](../../da/d89/classFem_1_1FemPostCutFilter.html#a682758b8e3c1c8cf8b272d2244321913),
[Fem::FemPostFunctionProvider](../../dd/d47/classFem_1_1FemPostFunctionProvider.html#a5d57b8e7aadfb627843050d88d933911),
[Fem::FemPostPlaneFunction](../../dd/d76/classFem_1_1FemPostPlaneFunction.html#ab73b39b74f480820feda8b3f5bcad117),
[Fem::FemPostSphereFunction](../../d5/dcb/classFem_1_1FemPostSphereFunction.html#abffccabdacd9cbbe6e61e799c8385c59),
[Fem::FemPostPipeline](../../d5/d4b/classFem_1_1FemPostPipeline.html#a333b47057bc9b7691cc0c9db9b0c79ba),
[FemGui::ViewProviderFemConstraint](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a3d33c13c95f3a907325ad1c399dc5a14),
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ab319d4e3659d8c99309bd397af321308),
[FemGui::ViewProviderFemPostFunctionProvider](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a13a3a3015d78a539b51f342fa516670c),
[FemGui::ViewProviderFemPostFunction](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#ae95be84201f7f51ce6162468c514e33e),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a5d27aeff234b60ec0214c939556b26c5),
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a75537f17b213bb2c7ea45b374ed65375),
[Mesh::Feature](../../dd/dce/classMesh_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae9ec71d871b59be4a532fb2be2cb8d52),
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[MeshGui::ViewProviderMeshDefects](../../da/d50/classMeshGui_1_1ViewProviderMeshDefects.html#a0d494009344982737533a865b26ce7d4),
[MeshGui::ViewProviderMeshNode](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a6f37857950fa14e1e1978c56706d0797),
[Part::Mirroring](../../dc/dac/classPart_1_1Mirroring.html#aa4148eb536fa6f15fb2fc21f3fe839b4),
[Part::Box](../../dc/d80/classPart_1_1Box.html#a29bcbc46ec0749e4035fffc5117e1723),
[Part::RuledSurface](../../d1/d41/classPart_1_1RuledSurface.html#a143afeec2aafb3207cd29e9ef6fc5934),
[Part::Loft](../../d3/d52/classPart_1_1Loft.html#acc65fe857c50b113cb06e0d092c83fd5),
[Part::Sweep](../../df/dc6/classPart_1_1Sweep.html#a67f346ffecb66556a70c38c9184cdd56),
[Part::Helix](../../df/d49/classPart_1_1Helix.html#a8f7d2c5809cd60f90231a0350ea5c444),
[Part::Spiral](../../d2/d3f/classPart_1_1Spiral.html#a2f38f985d7c148ee3acec62a8358b4b7),
[Part::Wedge](../../d5/dc5/classPart_1_1Wedge.html#a609125d1bc02031accfc330fc2e79d08),
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a04a16b5ac49a2b5df31304da0a4318ee),
[PartGui::ViewProviderCustom](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
[PartGui::ViewProviderPartReference](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#a8af0748ed20158c08efa16db288d3f81),
[PartDesign::Line](../../d0/d2a/classPartDesign_1_1Line.html#a9da12fed7c1a5cfa4af5c06af23c6fff),
[PartDesign::Plane](../../df/df0/classPartDesign_1_1Plane.html#a82dfdf47875b49263a5275ab1ff3c686),
[PartDesign::FeatureBase](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a628a37fc8716ca08f0c67bb727ac3b76),
[PartDesign::DressUp](../../df/de5/classPartDesign_1_1DressUp.html#a7f7a173d69576711009fb17aeb08f6bc),
[PartDesign::Helix](../../d3/d78/classPartDesign_1_1Helix.html#a8f7d2c5809cd60f90231a0350ea5c444),
[PartDesign::Hole](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[PartDesign::ProfileBased](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a36fd19fd597799ebeccd8eddd104bdf4),
[PartDesignGui::ViewProviderDatumPoint](../../dc/d9d/classPartDesignGui_1_1ViewProviderDatumPoint.html#ada6d519997cb6ca57d88957962fc1377),
[Path::Feature](../../d5/dd9/classPath_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[PathGui::ViewProviderPath](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[PointsGui::ViewProviderPoints](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ad91786e290cd4be69ef99a41c85faa32),
[Robot::Edge2TracObject](../../d8/df5/classRobot_1_1Edge2TracObject.html#a3e8b60d7dcc4abe17a0e640a0e0ef5e9),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#abebfe59d5888146a96594cb7d31ffce8),
[Robot::TrajectoryDressUpObject](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a58ad4466b7239a951a9b9b4d30b7f1d3),
[Robot::TrajectoryObject](../../d7/db5/classRobot_1_1TrajectoryObject.html#aded21cc1ebf027aa6b39e81759687ea3),
[RobotGui::ViewProviderRobotObject](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a41cfa5ba4f24dacf46491cc903e5a715),
[Sandbox::SandboxObject](../../da/dd9/classSandbox_1_1SandboxObject.html#ae3e3d04a08a28cb8060a72df914f3685),
[SketcherGui::ViewProviderCustom](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#a50d56147d2f6d3cf3329413baef6e66d),
[TechDraw::DrawParametricTemplate](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#a98d6a8c0896aca4d3fa549700b8a4eb6),
[TechDraw::DrawRichAnno](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#aca7c4594d99963f20955aaaea06f9fbc),
[TechDraw::DrawSVGTemplate](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#afa43ef4d1bf529675b75c5d31fff582b),
[TechDraw::DrawTemplate](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a6d7ffefeb992220357cf4dab59576919),
[TechDraw::DrawTile](../../da/d56/classTechDraw_1_1DrawTile.html#a0a7ecfbee9fbaf70d3d69acfd16c62e7),
[TechDraw::DrawTileWeld](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a4241390f45c70002f410b5c78a4d0452),
[TechDraw::DrawViewAnnotation](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#a6566da76a48d680dc1cc90db63e0c60a),
[TechDraw::DrawViewClip](../../dd/de8/classTechDraw_1_1DrawViewClip.html#afb0fdb6bcca35df389d3cd1632191706),
[TechDraw::DrawViewCollection](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a5897d64ff7b47d70c7f4bddce6ac17ce),
[TechDraw::DrawViewDimExtent](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#a33e7b8c64f2983f2b81608bd1ebfc494),
[TechDraw::DrawViewSpreadsheet](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#ab3c3a1352fddadb8dea1ef9ec40acd91),
[TechDraw::DrawWeldSymbol](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#ad0b71b97ee45320fc8e8634e98b935cb),
[TechDrawGui::ViewProviderImage](../../d3/d5b/classTechDrawGui_1_1ViewProviderImage.html#ad13417ef59c1aeb04fbc4fbcc6aa57d2),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a23482323e8ec6da0cb3dd93b00203e73),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a86b7b59890bb041b58c8e5564383e631),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a0387c427509686ba2dff332930fb5efe),
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[Gui::ViewProviderPart](../../d9/d6c/classGui_1_1ViewProviderPart.html#a5e76f3437483472cd66247d0eb98aa1a),
[Gui::ViewProviderPlacement](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a471b5fcc496e5d153b398a0675e2c93e),
[Part::BodyBase](../../da/dc8/classPart_1_1BodyBase.html#aad727053c5bb43ee6f065f3d0b458f16),
[Part::Revolution](../../d3/d17/classPart_1_1Revolution.html#a9940a58886c8d7d0b4b009082d81f14c),
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#a17178c5bf097534e84b20380ad13563b),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#ac5544f9b57ebf2a1b626450200a4bec0),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[PartDesign::Point](../../da/d0d/classPartDesign_1_1Point.html#a559cef769b27bcf8efeef552583f9aa4),
[PartDesign::Boolean](../../d2/d81/classPartDesign_1_1Boolean.html#a41c675a8b7f2f6e73b95946b99245f12),
[PartDesign::FeaturePrimitive](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a86c00f82005801a22585584fb378e4e5),
[PartDesign::ShapeBinder](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a984513ae894c80494f6a0c3b0725f48f),
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a525834748579d35e2e8ecbf9cd18bf3d),
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a257ca77e2256cbd8df847cedc5892289),
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922),
[PartDesignGui::ViewProviderBoolean](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#ab446d9f6494af864bd745136c7e20439),
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ae317a35c18a1f9b333a14655c35eb8dc),
[Surface::Extend](../../d1/d22/classSurface_1_1Extend.html#ac33fb0ebd31edae770d009cc24c58df9),
[TechDraw::DrawGeomHatch](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9942ef5dd5ecef6dba83a1245a0840ca),
[TechDraw::DrawHatch](../../d0/d97/classTechDraw_1_1DrawHatch.html#a655588bfe5d6ff663e4aefc40c118a58),
[TechDraw::DrawLeaderLine](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a289014293fbb3c42b8c46416e261530a),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawProjGroup](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[TechDraw::DrawProjGroupItem](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#aea5cc872256320be7112396d84b3fee5),
[TechDraw::DrawView](../../d6/d1c/classTechDraw_1_1DrawView.html#a2980fbae4ce0a12aae609193764465cf),
[TechDraw::DrawViewBalloon](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#aed3817b8e495aca5729e5bed436cca6c),
[TechDraw::DrawViewDetail](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewImage](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a42774ac4ebd8f4fc4819cf4833e779aa),
[TechDraw::DrawViewMulti](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#aa73d9e1a0934d049da29a63f2c5ddddd),
[TechDraw::DrawViewPart](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a6a340bbf67a96de757e412b21d7a5491),
[TechDraw::DrawViewSection](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[TechDraw::DrawViewSymbol](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#adb3364984aac5da2ff804a43845ceee4),
[TechDraw::LandmarkDimension](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a9c8e7f17abdc4acecdc7e6670328f7a6),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#af947ca7438432b3448358f4ebcf6bbc1),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a1a42e7ea4d5eb17c7e1f536cad241cc3),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#aada265457fade9ade61cbade5aee4f2b),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a498b66c6f2b5af184c95c4a07bc6f98e),
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#a7b5d5197907bbf4cc9c65c1004a1da83),
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#ad571ff1df010fb7f617689f0e4ff360d),
[App::MeasureDistance](../../d7/d61/classApp_1_1MeasureDistance.html#abbccf44662823af983d2786da162cc43),
[App::TextDocument](../../d9/de9/classApp_1_1TextDocument.html#affdf6c8a48df5cea53213040c487e5f8),
[App::Document](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
and
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#aa9fcfd8db6b2ffdf46274b18b45811cf).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft::attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire::execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[App::Property::hasSetValue()](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d),
[App::ExtensionContainer::onChanged()](../../d6/d76/classApp_1_1ExtensionContainer.html#ad571ff1df010fb7f617689f0e4ff360d),
[App::Property::touch()](../../d0/da9/classApp_1_1Property.html#a9bec8b8a56b405be0dc5e1602b079475),
[ArchBuildingPart.ViewProviderBuildingPart::updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut::updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet::updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel::updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer::updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy::updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ onPropertyStatusChanged()

| void PropertyContainer::onPropertyStatusChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _prop_ ,   
---|---|---|---  
|  | unsigned long  | _oldStatus_  
| ) | |   
virtual  
  
Reimplemented in
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#aa158bb0312285eb7672f123e8a1359de),
and
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#a89e5f59efb767cc633a6837305d04479).

Referenced by
[App::Property::setStatusValue()](../../d0/da9/classApp_1_1Property.html#a32cf2f8513b5a66b0b39c839c559f20b).

## ◆ removeDynamicProperty()

| virtual [bool](../../d9/db9/classbool.html) App::PropertyContainer::removeDynamicProperty  | ( | const char *  | _name_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#a00938d679f9f65e7ee4e9ef02d399c84),
and
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a4d47313a825a2051c9a667ed4e7a1346).

Referenced by
[App::TransactionObject::applyChn()](../../d9/d02/classApp_1_1TransactionObject.html#ae828131a91ad93ac2f20a51eeadecf70),
and
[Gui::ViewProviderDocumentObject::removeDynamicProperty()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a4d47313a825a2051c9a667ed4e7a1346).

## ◆ Restore()

| void PropertyContainer::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482
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
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#a654870e568b07840a79bd2c8e99e50d1),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a2e81a7dc633df4672dac82d4e8e1792a),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#ae08e5863309e25cd88e07e2be87c9f48),
[Gui::ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html#a4e6bcf20d9aa065b34edc83e9619ba51),
[Part::Box](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::Circle](../../de/de4/classPart_1_1Circle.html#a31f09d03f0ee6b6f7a9e98b20b7223d4),
[Part::Ellipse](../../d6/d22/classPart_1_1Ellipse.html#a90f7d460c9b3b2d2cf7b07282ad83efd),
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#af020d668456d6c40964757726bb9d1aa),
[PartDesign::Plane](../../df/df0/classPartDesign_1_1Plane.html#a0daddf322de5233314e8ec1e5d73f658),
[PartDesign::Fillet](../../d0/d50/classPartDesign_1_1Fillet.html#ab91b894b378df78eb983a34f62c5cc46),
[PartDesign::Hole](../../dd/dd0/classPartDesign_1_1Hole.html#ada1c34ac1dc39bd284a23e440d663312),
[PartDesign::ProfileBased](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a911a7f2f77e2adb2277a344a4ffb33f2),
[PartDesign::Transformed](../../dd/de1/classPartDesign_1_1Transformed.html#a4e823053076cbcb1c6a8add13d191405),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#af3c51f0c54d5a9ec82ef35950ce21d83),
[App::Document](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a004bf684691accc570954af96e2e3d48),
[Part::Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html#a24712341d8edfa206b25b21bdda998a2),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#ad739d09a91f363ecaac5bce84d2271f7),
[PartDesign::Chamfer](../../da/d6f/classPartDesign_1_1Chamfer.html#aa7e36b44d9a038c47691655463d2eaf4),
and
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#afb1057b5d67039082147ba14225f1c82).

References
[Base::XMLReader::clearPartialRestoreProperty()](../../dc/d95/classBase_1_1XMLReader.html#a3c89a7778a60cc6bc5709aa7e93d7bd4),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[Base::XMLReader::getAttributeAsUnsigned()](../../dc/d95/classBase_1_1XMLReader.html#ac384789d0b975c7caee3762a236d951c),
[App::Property::getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a),
[getPropertyByName()](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2),
[handleChangedPropertyName()](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573),
[handleChangedPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[App::Property::PropTransient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a49215d8e9f6a5a24523e5ce094fb867e),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[Base::XMLReader::readEndElement()](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3),
[App::DynamicProperty::restore()](../../d5/d76/classApp_1_1DynamicProperty.html#aabd3c2d0b261a6a0bb4aa55500ea09ca),
[Base::XMLReader::setPartialRestore()](../../dc/d95/classBase_1_1XMLReader.html#adaf7e17e8787a7f2bc25ba0c62bbd389),
[App::Property::setStatusValue()](../../d0/da9/classApp_1_1Property.html#a32cf2f8513b5a66b0b39c839c559f20b),
[App::Property::StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67),
[Base::XMLReader::testStatus()](../../dc/d95/classBase_1_1XMLReader.html#a1f076d2b8f0c7ff3257cfa6fc595c06c),
and
[App::Property::Transient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a14e77d5a09c2b0796490e697b68560e5).

Referenced by
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
and
[App::ExtensionContainer::Restore()](../../d6/d76/classApp_1_1ExtensionContainer.html#a004bf684691accc570954af96e2e3d48).

## ◆ Save()

| void PropertyContainer::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
virtual  
  
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
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#ab1443831f8c6492a77f0f9483688c5b6),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a914f9773505d35bfd655e97abffb6d7b),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#abee995466100ec91a1ae0f2baa2feec3),
[App::Document](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0),
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#aceb2a532b12d3ad6806562eb64bfcf06),
and
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5).

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::Writer::decInd()](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92),
[dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[getPropertyMap()](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8),
[getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510),
[Base::Writer::incInd()](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5),
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
[App::Prop_Transient](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a6eefec5f03fa1d639e7fc26c5804ccf6),
[App::Property::PropDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a610d527a8ef20b533504b5121a983d80),
[App::Property::PropNoPersist](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ae221473138e52da3001d1de060205179),
[App::DynamicProperty::save()](../../d5/d76/classApp_1_1DynamicProperty.html#a6e38d28a7d5937858b56fdfa3a717086),
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205),
and
[App::Property::Transient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a14e77d5a09c2b0796490e697b68560e5).

Referenced by
[App::Document::Save()](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0),
and
[App::ExtensionContainer::Save()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5).

## ◆ setPropertyPrefix()

void App::PropertyContainer::setPropertyPrefix  | ( | const char *  | _prefix_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Gui::ViewProviderLink::onChanged()](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1).

## ◆ setPropertyStatus()

void PropertyContainer::setPropertyStatus  | ( | unsigned char  | _bit_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _value_  
| ) | |   
  
set the Status bit of all properties at once

References
[getPropertyList()](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a).

## Friends And Related Function Documentation

## ◆ DynamicProperty

| [friend](../../d7/d23/classfriend.html) class
[DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html)  
---  
friend  
  
## ◆ Property

| [friend](../../d7/d23/classfriend.html) class
[Property](../../d0/da9/classApp_1_1Property.html)  
---  
friend  
  
## Member Data Documentation

## ◆ dynamicProps

| [DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html)
App::PropertyContainer::dynamicProps  
---  
protected  
  
Referenced by
[addDynamicProperty()](../../d5/d48/classApp_1_1PropertyContainer.html#aeb460dcdedde87f84dbab68d0865bfa6),
[getPropertyByName()](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2),
[getPropertyDocumentation()](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912),
[getPropertyGroup()](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356),
[getPropertyList()](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a),
[getPropertyMap()](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8),
[getPropertyName()](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981),
[getPropertyNamedList()](../../d5/d48/classApp_1_1PropertyContainer.html#ac1db173138f821f169de2b20111c935f),
[Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
and
[Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyContainer.h
  * FreeCAD/src/App/PropertyContainer.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

