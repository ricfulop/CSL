---
url: https://freecad.github.io/SourceDoc/d5/d76/classApp_1_1DynamicProperty.html
scraped_at: 2025-09-08T14:54:31.456016
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html)

[List of all members](../../da/d70/classApp_1_1DynamicProperty-members.html) | Classes | Public Member Functions

App::DynamicProperty Class Reference

This class implements an interface to add properties at run-time to an object
derived from
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html "Base
class of all classes with properties.").
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#details)

`#include <DynamicProperty.h>`

##  Classes  
  
---  
struct | [PropData](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html)  
  
##  Public Member Functions  
  
---  
|
[DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html#a7450e8d228a2eeecbb4ae860ea72330a)
()  
virtual | [~DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html#a2209b1b9843c10cba9b20d8d77538017) ()  
Access properties  
void | [getPropertyList](../../d5/d76/classApp_1_1DynamicProperty.html#a4ba0df7e18f1b4b88088307283b5de62) (std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > &List) const  
| Get all properties of the class (including parent)
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#a4ba0df7e18f1b4b88088307283b5de62)  
  
void | [getPropertyNamedList](../../d5/d76/classApp_1_1DynamicProperty.html#ac5df12664197fc01d96a78a9f6d2a1cd) (std::vector< std::pair< const char *, [Property](../../d0/da9/classApp_1_1Property.html) * > > &List) const  
| get all properties with their names
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#ac5df12664197fc01d96a78a9f6d2a1cd)  
  
void | [getPropertyMap](../../d5/d76/classApp_1_1DynamicProperty.html#a9423e1c11e7e1c07b658b2311cf4a1f6) (std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > &Map) const  
| Get all properties of the class (including parent)
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#a9423e1c11e7e1c07b658b2311cf4a1f6)  
  
[Property](../../d0/da9/classApp_1_1Property.html) * | [getDynamicPropertyByName](../../d5/d76/classApp_1_1DynamicProperty.html#a41130d5c69a0c4cf3f4e19dab20de459) (const char *name) const  
| Find a dynamic property by its name.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#a41130d5c69a0c4cf3f4e19dab20de459)  
  
[Property](../../d0/da9/classApp_1_1Property.html) * | [addDynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e) ([PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) &pc, const char *[type](../../d9/d98/classtype.html), const char *name=nullptr, const char *group=nullptr, const char *doc=nullptr, short attr=0, [bool](../../d9/db9/classbool.html) ro=false, [bool](../../d9/db9/classbool.html) hidden=false)  
[bool](../../d9/db9/classbool.html) | [addProperty](../../d5/d76/classApp_1_1DynamicProperty.html#afaada5859108dac4c73627edc1d5369e) ([Property](../../d0/da9/classApp_1_1Property.html) *prop)  
| Add a pre-existing property.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#afaada5859108dac4c73627edc1d5369e)  
  
[bool](../../d9/db9/classbool.html) | [removeDynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html#a8e4c6ca6912ea2f53be583ba0ff7d7b6) (const char *name)  
[bool](../../d9/db9/classbool.html) | [removeProperty](../../d5/d76/classApp_1_1DynamicProperty.html#af906db4cf3595f2ae0999166c31b3bdd) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
| Remove pre-existing property, which will not be deleted.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#af906db4cf3595f2ae0999166c31b3bdd)  
  
std::vector< std::string > | [getDynamicPropertyNames](../../d5/d76/classApp_1_1DynamicProperty.html#a099c755e5d1963937dee9184cd718453) () const  
| Get a list of all dynamic properties.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#a099c755e5d1963937dee9184cd718453)  
  
const char * | [getPropertyName](../../d5/d76/classApp_1_1DynamicProperty.html#ab367905c95b0b6ca675b14c9be23d7cf) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| Get the name of a property.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#ab367905c95b0b6ca675b14c9be23d7cf)  
  
  
## Property attributes  
  
---  
short | [getPropertyType](../../d5/d76/classApp_1_1DynamicProperty.html#a335e7f88a53ed325d69d3b7177731266) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| Get the attributes of a property.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#a335e7f88a53ed325d69d3b7177731266)  
  
short | [getPropertyType](../../d5/d76/classApp_1_1DynamicProperty.html#adc4a1351e47e1be0d6d9fca63a8d96eb) (const char *name) const  
| Get the attributes of a named property.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#adc4a1351e47e1be0d6d9fca63a8d96eb)  
  
const char * | [getPropertyGroup](../../d5/d76/classApp_1_1DynamicProperty.html#aa46af4e48d92adc936b42a9188b7fcd0) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| Get the group name of a property.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#aa46af4e48d92adc936b42a9188b7fcd0)  
  
const char * | [getPropertyGroup](../../d5/d76/classApp_1_1DynamicProperty.html#a58b9218eff7e37aef77425544bdcf700) (const char *name) const  
| Get the group name of a named property.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#a58b9218eff7e37aef77425544bdcf700)  
  
const char * | [getPropertyDocumentation](../../d5/d76/classApp_1_1DynamicProperty.html#a165ad3da898b9a9e30a87ea2d23279c5) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| Get the documentation of a property.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#a165ad3da898b9a9e30a87ea2d23279c5)  
  
const char * | [getPropertyDocumentation](../../d5/d76/classApp_1_1DynamicProperty.html#ad01f8bc9cfc410df8002d065ff9355ec) (const char *name) const  
| Get the documentation of a named property.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#ad01f8bc9cfc410df8002d065ff9355ec)  
  
void | [clear](../../d5/d76/classApp_1_1DynamicProperty.html#a5652a7ebe27b0a95717eccbbd105a921) ()  
| Remove all properties.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#a5652a7ebe27b0a95717eccbbd105a921)  
  
size_t | [size](../../d5/d76/classApp_1_1DynamicProperty.html#ae15930d92741040ccd8b0a6309112ada) () const  
| Get property count.
[More...](../../d5/d76/classApp_1_1DynamicProperty.html#ae15930d92741040ccd8b0a6309112ada)  
  
void | [save](../../d5/d76/classApp_1_1DynamicProperty.html#a6e38d28a7d5937858b56fdfa3a717086) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop, [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
[Property](../../d0/da9/classApp_1_1Property.html) * | [restore](../../d5/d76/classApp_1_1DynamicProperty.html#aabd3c2d0b261a6a0bb4aa55500ea09ca) ([PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) &pc, const char *PropName, const char *TypeName, [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
[PropData](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html) | [getDynamicPropertyData](../../d5/d76/classApp_1_1DynamicProperty.html#ad069ab9f281d0df4248e00cac35dc83e) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
[bool](../../d9/db9/classbool.html) | [changeDynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html#ae38f1e9ff49700adc986f1a243293259) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop, const char *group, const char *doc)  
  
## Detailed Description

This class implements an interface to add properties at run-time to an object
derived from
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html "Base
class of all classes with properties.").

The additional properties are made persistent.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ DynamicProperty()

DynamicProperty::DynamicProperty  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~DynamicProperty()

| DynamicProperty::~DynamicProperty  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[clear()](../../d5/d76/classApp_1_1DynamicProperty.html#a5652a7ebe27b0a95717eccbbd105a921).

## Member Function Documentation

## ◆ addDynamicProperty()

[Property](../../d0/da9/classApp_1_1Property.html) * DynamicProperty::addDynamicProperty  | ( | [PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) & | _pc_ ,   
---|---|---|---  
|  | const char *  | _type_ ,   
|  | const char *  | _name_ = `nullptr`,   
|  | const char *  | _group_ = `nullptr`,   
|  | const char *  | _doc_ = `nullptr`,   
|  | short  | _attr_ = `0`,   
|  | [bool](../../d9/db9/classbool.html) | _ro_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _hidden_ = `false`  
| ) | |   
  
Add a dynamic property of the type _type_ and with the name _name_. _Group_
gives the grouping name which appears in the property editor and _doc_ shows
the tooltip there. With _attr_ , _ro_ and _hidden_ the behaviour of the
property can be controlled. _attr_ is an OR'ed value of the PropertyType
enumeration. If no special attribute should be set Prop_None can be set (or
leave the default of 0). For convenience the attributes for 'Read-Only' and
'Hidden' can also be controlled with the values _ro_ or _hidden_. This means,

[addDynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e)(..., ..., "Base","blah", [Prop_ReadOnly](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a9bea209c7050543e2ceadef7ba0e9e75) | [Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6));

is equivalent to

[addDynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e)(...,
..., "Base","blah",
[Prop_None](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a32c18d11cda25e1ac1b1692aa36423e0),
true, true);

References
[Base::Type::createInstance()](../../dc/dee/classBase_1_1Type.html#a2d1d33a2453ee324e07ce2412a542e44),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[ParameterGrp::GetBool()](../../d4/d97/classParameterGrp.html#a603e85aad05116d3331f865715297d08),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::PropertyContainer::getFullName()](../../d5/d48/classApp_1_1PropertyContainer.html#a331110f1aeffb0a907ac2b74f78cc69d),
[Base::Tools::getIdentifier()](../../d6/dda/structBase_1_1Tools.html#a49653de3f8677d06572f26f1f002641d),
[App::Application::GetParameterGroupByPath()](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202),
[App::PropertyContainer::getPropertyByName()](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2),
[Base::Type::getTypeIfDerivedFrom()](../../dc/dee/classBase_1_1Type.html#ae69252049934864817d7932cc246a593),
[Base::Type::isBad()](../../dc/dee/classBase_1_1Type.html#ab091b5ccf4f8e3c7c59cb05dde3c2fcb),
[App::Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6),
[App::Prop_ReadOnly](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a9bea209c7050543e2ceadef7ba0e9e75),
[App::Property::PropDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a610d527a8ef20b533504b5121a983d80),
[App::Property::setContainer()](../../d0/da9/classApp_1_1Property.html#aa03e6562bf3996db1700b0e636425257),
[App::Application::signalAppendDynamicProperty](../../da/dbf/classApp_1_1Application.html#a38e4cf45b905fcaafc05d550ddb83fd9),
and
[App::Property::StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67).

Referenced by
[App::PropertyContainer::addDynamicProperty()](../../d5/d48/classApp_1_1PropertyContainer.html#aeb460dcdedde87f84dbab68d0865bfa6),
and
[restore()](../../d5/d76/classApp_1_1DynamicProperty.html#aabd3c2d0b261a6a0bb4aa55500ea09ca).

## ◆ addProperty()

[bool](../../d9/db9/classbool.html) DynamicProperty::addProperty  | ( | [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
  
Add a pre-existing property.

The property is not treated as dynamic, and will not trigger signal.

Returns

    Return false if there is a property exist with the same name. 

References
[App::Property::getDocumentation()](../../d0/da9/classApp_1_1Property.html#ada9481ae19a85f023c5597d57f8c809b),
[App::Property::getGroup()](../../d0/da9/classApp_1_1Property.html#ab815066b984a7d6c133b4c947a989fee),
[App::Property::getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a),
[App::Property::getType()](../../d0/da9/classApp_1_1Property.html#abc4967c88a5fc83c27a47f9534fdd510),
and
[App::Property::hasName()](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f).

Referenced by
[DocumentObject.Box::init()](../../d9/d5e/classDocumentObject_1_1Box.html#a6b1f9e4a9bd9b577a53891b93193bf6f),
and
[DocumentObject.DocumentObject::onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882).

## ◆ changeDynamicProperty()

[bool](../../d9/db9/classbool.html) DynamicProperty::changeDynamicProperty  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_ ,   
---|---|---|---  
|  | const char *  | _group_ ,   
|  | const char *  | _doc_  
| ) | |   
  
## ◆ clear()

void DynamicProperty::clear  | ( | | ) |   
---|---|---|---|---  
  
Remove all properties.

Referenced by
[~DynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a2209b1b9843c10cba9b20d8d77538017).

## ◆ getDynamicPropertyByName()

[Property](../../d0/da9/classApp_1_1Property.html) * DynamicProperty::getDynamicPropertyByName  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
  
Find a dynamic property by its name.

Referenced by
[App::PropertyContainer::getPropertyByName()](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2).

## ◆ getDynamicPropertyData()

[DynamicProperty::PropData](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html) DynamicProperty::getDynamicPropertyData  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
  
## ◆ getDynamicPropertyNames()

std::vector< std::string > DynamicProperty::getDynamicPropertyNames  | ( | | ) |  const  
---|---|---|---|---  
  
Get a list of all dynamic properties.

## ◆ getPropertyDocumentation() [1/2]

const char * DynamicProperty::getPropertyDocumentation  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
  
Get the documentation of a named property.

## ◆ getPropertyDocumentation() [2/2]

const char * DynamicProperty::getPropertyDocumentation  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
  
Get the documentation of a property.

Referenced by
[App::PropertyContainer::getPropertyDocumentation()](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912).

## ◆ getPropertyGroup() [1/2]

const char * DynamicProperty::getPropertyGroup  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
  
Get the group name of a named property.

## ◆ getPropertyGroup() [2/2]

const char * DynamicProperty::getPropertyGroup  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
  
Get the group name of a property.

Referenced by
[App::PropertyContainer::getPropertyGroup()](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356).

## ◆ getPropertyList()

void DynamicProperty::getPropertyList  | ( | std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > & | _List_| ) |  const  
---|---|---|---|---|---  
  
Get all properties of the class (including parent)

Referenced by
[App::PropertyContainer::getPropertyList()](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a).

## ◆ getPropertyMap()

void DynamicProperty::getPropertyMap  | ( | std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > & | _Map_| ) |  const  
---|---|---|---|---|---  
  
Get all properties of the class (including parent)

Referenced by
[App::PropertyContainer::getPropertyMap()](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8).

## ◆ getPropertyName()

const char * DynamicProperty::getPropertyName  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
  
Get the name of a property.

Referenced by
[App::PropertyContainer::getPropertyName()](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981).

## ◆ getPropertyNamedList()

void DynamicProperty::getPropertyNamedList  | ( | std::vector< std::pair< const char *, [Property](../../d0/da9/classApp_1_1Property.html) * > > & | _List_| ) |  const  
---|---|---|---|---|---  
  
get all properties with their names

Referenced by
[App::PropertyContainer::getPropertyNamedList()](../../d5/d48/classApp_1_1PropertyContainer.html#ac1db173138f821f169de2b20111c935f).

## ◆ getPropertyType() [1/2]

short DynamicProperty::getPropertyType  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
  
Get the attributes of a named property.

References
[App::Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6),
and
[App::Prop_ReadOnly](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a9bea209c7050543e2ceadef7ba0e9e75).

## ◆ getPropertyType() [2/2]

short DynamicProperty::getPropertyType  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
  
Get the attributes of a property.

References
[App::Property::getType()](../../d0/da9/classApp_1_1Property.html#abc4967c88a5fc83c27a47f9534fdd510).

## ◆ removeDynamicProperty()

[bool](../../d9/db9/classbool.html) DynamicProperty::removeDynamicProperty  | ( | const char *  | _name_| ) |   
---|---|---|---|---|---  
  
Removes a dynamic property by name. Returns true if the property is part of
the container, otherwise false is returned.

References
[App::Property::destroy()](../../d0/da9/classApp_1_1Property.html#a3a8325b864cd82b562eb553fe2be6d1c),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::Property::LockDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ac134907b347ed2484e41577a88d9a06e),
[App::Property::PropDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a610d527a8ef20b533504b5121a983d80),
and
[App::Application::signalRemoveDynamicProperty](../../da/dbf/classApp_1_1Application.html#a7b56714fdb016b0b5fde4f03f77cbce0).

## ◆ removeProperty()

[bool](../../d9/db9/classbool.html) DynamicProperty::removeProperty  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
  
Remove pre-existing property, which will not be deleted.

## ◆ restore()

[Property](../../d0/da9/classApp_1_1Property.html) * DynamicProperty::restore  | ( | [PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) & | _pc_ ,   
---|---|---|---  
|  | const char *  | _PropName_ ,   
|  | const char *  | _TypeName_ ,   
|  | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_  
| ) | |   
  
References
[addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
and
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910).

Referenced by
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
and
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e).

## ◆ save()

void DynamicProperty::save  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_ ,   
---|---|---|---  
|  | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | _writer_  
| ) | |  const  
  
References
[Base::Persistence::encodeAttribute()](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

Referenced by
[Mod.Show.mTempoVis.TempoVis::modify()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a356b61cdf305ec299725a94d8854c54d),
[Mod.Show.mTempoVis.TempoVis::modifyVPProperty()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#aa63b8d331e9128477a94f01fbc77debe),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::onSaveStyle()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a62078ac8e29f972f667a11bf889acd64),
[App::PropertyContainer::Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482),
and
[Mod.Show.mTempoVis.TempoVis::saveCamera()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a5e350c94234cc5048fcf0c3c645b5b5f).

## ◆ size()

size_t App::DynamicProperty::size  | ( | | ) |  const  
---|---|---|---|---  
  
Get property count.

Referenced by
[gzip_utf8.GzipFile::close()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a5c40910b0ce0286256128c6dae8a2c9b),
[PathScripts.PostUtils.GCodeEditorDialog::done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
and
[gzip_utf8.GzipFile::write()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a3148c5b71cccbdfce05d52d31114810e).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/DynamicProperty.h
  * FreeCAD/src/App/DynamicProperty.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

