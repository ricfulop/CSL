---
url: https://freecad.github.io/SourceDoc/d2/d02/structApp_1_1PropertyData.html
scraped_at: 2025-09-08T14:55:34.726353
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyData](../../d2/d02/structApp_1_1PropertyData.html)

[List of all members](../../d9/dea/structApp_1_1PropertyData-members.html) | Classes | Public Member Functions | Public Attributes

App::PropertyData Struct Reference

`#include <PropertyContainer.h>`

##  Classes  
  
---  
struct | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html)  
struct | [PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html)  
  
##  Public Member Functions  
  
---  
void | [addProperty](../../d2/d02/structApp_1_1PropertyData.html#a7d03b124a06a1399d8337f580c9acd2a) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const char *PropName, [Property](../../d0/da9/classApp_1_1Property.html) *Prop, const char *PropertyGroup=nullptr, [PropertyType](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48)=[Prop_None](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a32c18d11cda25e1ac1b1692aa36423e0), const char *PropertyDocu=nullptr)  
const [PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html) * | [findProperty](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const char *PropName) const  
const [PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html) * | [findProperty](../../d2/d02/structApp_1_1PropertyData.html#a00fcce252ca13b47286bab0a89863bf7) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
const char * | [getDocumentation](../../d2/d02/structApp_1_1PropertyData.html#ac5fa377a98454621a8b23dde9dd57dad) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const char *name) const  
const char * | [getDocumentation](../../d2/d02/structApp_1_1PropertyData.html#a423d1f8308c47352b2cfb45ef08021ac) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
const char * | [getGroup](../../d2/d02/structApp_1_1PropertyData.html#a4c0fd744dc4ee79240f8ff63bc1895cc) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const char *name) const  
const char * | [getGroup](../../d2/d02/structApp_1_1PropertyData.html#a6e1be631f04dc7ef38c4d8d671847107) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
const char * | [getName](../../d2/d02/structApp_1_1PropertyData.html#a4dc58677d9d6ccb3577d49d7f4c7673b) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
[Property](../../d0/da9/classApp_1_1Property.html) * | [getPropertyByName](../../d2/d02/structApp_1_1PropertyData.html#ac91725ecc43ae8b7a032d0dbcd91ae41) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const char *name) const  
void | [getPropertyList](../../d2/d02/structApp_1_1PropertyData.html#ac697b4d2ae7f2258097b5d63d508379f) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > &List) const  
void | [getPropertyMap](../../d2/d02/structApp_1_1PropertyData.html#aa53fb59fabeac2789a00247260af211e) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > &Map) const  
void | [getPropertyNamedList](../../d2/d02/structApp_1_1PropertyData.html#a62858579f4b81973d1661262e8c79146) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, std::vector< std::pair< const char *, [Property](../../d0/da9/classApp_1_1Property.html) * > > &List) const  
short | [getType](../../d2/d02/structApp_1_1PropertyData.html#aa2ad51209f1f219d2858735fe8114b5e) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const char *name) const  
short | [getType](../../d2/d02/structApp_1_1PropertyData.html#aaf3d180ed1cce49e71783b6252bbcce1) ([OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) offsetBase, const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
void | [merge](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13) ([PropertyData](../../d2/d02/structApp_1_1PropertyData.html) *other=nullptr) const  
void | [split](../../d2/d02/structApp_1_1PropertyData.html#a54a70f401aaa3cd992b833647676b8bf) ([PropertyData](../../d2/d02/structApp_1_1PropertyData.html) *other)  
  
##  Public Attributes  
  
---  
[bool](../../d9/db9/classbool.html) | [parentMerged](../../d2/d02/structApp_1_1PropertyData.html#a59fb6fbb338c3bf1dd1a9ef233abe4a5) = false  
const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) * | [parentPropertyData](../../d2/d02/structApp_1_1PropertyData.html#a0adc14b3b28df5f2248e240a016309ab)  
bmi::multi_index_container< [PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html), bmi::indexed_by< bmi::sequenced<>, bmi::hashed_unique< bmi::member< [PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html), const char *, &[PropertySpec::Name](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#a9dbe0f666a30b7c33574047635aa4aef) >, [CStringHasher](../../d9/d20/structApp_1_1CStringHasher.html), [CStringHasher](../../d9/d20/structApp_1_1CStringHasher.html) >, bmi::hashed_unique< bmi::member< [PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html), short, &[PropertySpec::Offset](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#ad44bea49f5dc300be1b2f06e1f1ba8c1) > > > > | [propertyData](../../d2/d02/structApp_1_1PropertyData.html#a13fb3132cda5a10dd3158fb9783b3963)  
  
## Member Function Documentation

## ◆ addProperty()

void PropertyData::addProperty  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const char *  | _PropName_ ,   
|  | [Property](../../d0/da9/classApp_1_1Property.html) *  | _Prop_ ,   
|  | const char *  | _PropertyGroup_ = `nullptr`,   
|  | [PropertyType](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48) | _Type_ = `[Prop_None](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a32c18d11cda25e1ac1b1692aa36423e0)`,   
|  | const char *  | _PropertyDocu_ = `nullptr`  
| ) | |   
  
References
[App::PropertyData::OffsetBase::getOffsetTo()](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html#af01bc2bb0b6325a207dcdaded849d6bc),
[parentMerged](../../d2/d02/structApp_1_1PropertyData.html#a59fb6fbb338c3bf1dd1a9ef233abe4a5),
and
[propertyData](../../d2/d02/structApp_1_1PropertyData.html#a13fb3132cda5a10dd3158fb9783b3963).

Referenced by
[DocumentObject.Box::init()](../../d9/d5e/classDocumentObject_1_1Box.html#a6b1f9e4a9bd9b577a53891b93193bf6f),
and
[DocumentObject.DocumentObject::onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882).

## ◆ findProperty() [1/2]

const [PropertyData::PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html) * PropertyData::findProperty  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const char *  | _PropName_  
| ) | |  const  
  
References
[merge()](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13),
and
[propertyData](../../d2/d02/structApp_1_1PropertyData.html#a13fb3132cda5a10dd3158fb9783b3963).

Referenced by
[getDocumentation()](../../d2/d02/structApp_1_1PropertyData.html#a423d1f8308c47352b2cfb45ef08021ac),
[getGroup()](../../d2/d02/structApp_1_1PropertyData.html#a6e1be631f04dc7ef38c4d8d671847107),
[getName()](../../d2/d02/structApp_1_1PropertyData.html#a4dc58677d9d6ccb3577d49d7f4c7673b),
[getPropertyByName()](../../d2/d02/structApp_1_1PropertyData.html#ac91725ecc43ae8b7a032d0dbcd91ae41),
and
[getType()](../../d2/d02/structApp_1_1PropertyData.html#aaf3d180ed1cce49e71783b6252bbcce1).

## ◆ findProperty() [2/2]

const [PropertyData::PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html) * PropertyData::findProperty  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_  
| ) | |  const  
  
References
[App::PropertyData::OffsetBase::getOffsetTo()](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html#af01bc2bb0b6325a207dcdaded849d6bc),
[merge()](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13),
and
[propertyData](../../d2/d02/structApp_1_1PropertyData.html#a13fb3132cda5a10dd3158fb9783b3963).

## ◆ getDocumentation() [1/2]

const char * PropertyData::getDocumentation  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const char *  | _name_  
| ) | |  const  
  
References
[App::PropertyData::PropertySpec::Docu](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#ab02ab41a4f9b90bb071098acada917e2),
and
[findProperty()](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7).

Referenced by
[App::PropertyContainer::getPropertyDocumentation()](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912).

## ◆ getDocumentation() [2/2]

const char * PropertyData::getDocumentation  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_  
| ) | |  const  
  
References
[App::PropertyData::PropertySpec::Docu](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#ab02ab41a4f9b90bb071098acada917e2),
and
[findProperty()](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7).

## ◆ getGroup() [1/2]

const char * PropertyData::getGroup  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const char *  | _name_  
| ) | |  const  
  
References
[findProperty()](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7),
and
[App::PropertyData::PropertySpec::Group](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#a5a1f071e89e536e2ea7ecff53890f285).

Referenced by
[App::PropertyContainer::getPropertyGroup()](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356).

## ◆ getGroup() [2/2]

const char * PropertyData::getGroup  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_  
| ) | |  const  
  
References
[findProperty()](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7),
and
[App::PropertyData::PropertySpec::Group](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#a5a1f071e89e536e2ea7ecff53890f285).

## ◆ getName()

const char * PropertyData::getName  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_  
| ) | |  const  
  
References
[findProperty()](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7),
and
[App::PropertyData::PropertySpec::Name](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#a9dbe0f666a30b7c33574047635aa4aef).

Referenced by
[App::PropertyContainer::getPropertyName()](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981).

## ◆ getPropertyByName()

[Property](../../d0/da9/classApp_1_1Property.html) * PropertyData::getPropertyByName  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const char *  | _name_  
| ) | |  const  
  
References
[findProperty()](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7),
[App::PropertyData::OffsetBase::getOffset()](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html#a53b3dc5f50209abf2aa3c80d844ccc43),
and
[App::PropertyData::PropertySpec::Offset](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#ad44bea49f5dc300be1b2f06e1f1ba8c1).

Referenced by
[App::PropertyContainer::getPropertyByName()](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2).

## ◆ getPropertyList()

void PropertyData::getPropertyList  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > & | _List_  
| ) | |  const  
  
References
[App::PropertyData::OffsetBase::getOffset()](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html#a53b3dc5f50209abf2aa3c80d844ccc43),
[merge()](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13),
and
[propertyData](../../d2/d02/structApp_1_1PropertyData.html#a13fb3132cda5a10dd3158fb9783b3963).

Referenced by
[App::PropertyContainer::getPropertyList()](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a).

## ◆ getPropertyMap()

void PropertyData::getPropertyMap  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > & | _Map_  
| ) | |  const  
  
References
[App::PropertyData::OffsetBase::getOffset()](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html#a53b3dc5f50209abf2aa3c80d844ccc43),
[merge()](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13),
and
[propertyData](../../d2/d02/structApp_1_1PropertyData.html#a13fb3132cda5a10dd3158fb9783b3963).

Referenced by
[App::PropertyContainer::getPropertyMap()](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8).

## ◆ getPropertyNamedList()

void PropertyData::getPropertyNamedList  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | std::vector< std::pair< const char *, [Property](../../d0/da9/classApp_1_1Property.html) * > > & | _List_  
| ) | |  const  
  
References
[App::PropertyData::OffsetBase::getOffset()](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html#a53b3dc5f50209abf2aa3c80d844ccc43),
[merge()](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13),
and
[propertyData](../../d2/d02/structApp_1_1PropertyData.html#a13fb3132cda5a10dd3158fb9783b3963).

Referenced by
[App::PropertyContainer::getPropertyNamedList()](../../d5/d48/classApp_1_1PropertyContainer.html#ac1db173138f821f169de2b20111c935f).

## ◆ getType() [1/2]

short PropertyData::getType  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const char *  | _name_  
| ) | |  const  
  
References
[findProperty()](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7),
and
[App::PropertyData::PropertySpec::Type](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#a6244b48b04beb90601c0eab74414ac4f).

Referenced by
[PathScripts.PathToolEdit.ToolEditor::updateToolType()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a2ab9dc5c3f1a484ce30b642df4879fa3),
and
[PathScripts.PathToolEdit.ToolEditor::updateUI()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a901452eb82081a083d2b5d97ab8fe306).

## ◆ getType() [2/2]

short PropertyData::getType  | ( | [OffsetBase](../../d1/d6d/structApp_1_1PropertyData_1_1OffsetBase.html) | _offsetBase_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_  
| ) | |  const  
  
References
[findProperty()](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7),
and
[App::PropertyData::PropertySpec::Type](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#a6244b48b04beb90601c0eab74414ac4f).

Referenced by
[PathScripts.PathToolEdit.ToolEditor::updateToolType()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a2ab9dc5c3f1a484ce30b642df4879fa3),
and
[PathScripts.PathToolEdit.ToolEditor::updateUI()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a901452eb82081a083d2b5d97ab8fe306).

## ◆ merge()

void PropertyData::merge  | ( | [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) *  | _other_ = `nullptr`| ) |  const  
---|---|---|---|---|---  
  
References
[merge()](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13),
[parentMerged](../../d2/d02/structApp_1_1PropertyData.html#a59fb6fbb338c3bf1dd1a9ef233abe4a5),
[parentPropertyData](../../d2/d02/structApp_1_1PropertyData.html#a0adc14b3b28df5f2248e240a016309ab),
and
[propertyData](../../d2/d02/structApp_1_1PropertyData.html#a13fb3132cda5a10dd3158fb9783b3963).

Referenced by
[findProperty()](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7),
[getPropertyList()](../../d2/d02/structApp_1_1PropertyData.html#ac697b4d2ae7f2258097b5d63d508379f),
[getPropertyMap()](../../d2/d02/structApp_1_1PropertyData.html#aa53fb59fabeac2789a00247260af211e),
[getPropertyNamedList()](../../d2/d02/structApp_1_1PropertyData.html#a62858579f4b81973d1661262e8c79146),
and
[merge()](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13).

## ◆ split()

void PropertyData::split  | ( | [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) *  | _other_| ) |   
---|---|---|---|---|---  
  
References
[parentMerged](../../d2/d02/structApp_1_1PropertyData.html#a59fb6fbb338c3bf1dd1a9ef233abe4a5),
[parentPropertyData](../../d2/d02/structApp_1_1PropertyData.html#a0adc14b3b28df5f2248e240a016309ab),
and
[propertyData](../../d2/d02/structApp_1_1PropertyData.html#a13fb3132cda5a10dd3158fb9783b3963).

## Member Data Documentation

## ◆ parentMerged

| [bool](../../d9/db9/classbool.html) App::PropertyData::parentMerged = false  
---  
mutable  
  
Referenced by
[addProperty()](../../d2/d02/structApp_1_1PropertyData.html#a7d03b124a06a1399d8337f580c9acd2a),
[merge()](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13),
and
[split()](../../d2/d02/structApp_1_1PropertyData.html#a54a70f401aaa3cd992b833647676b8bf).

## ◆ parentPropertyData

const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html)*
App::PropertyData::parentPropertyData  
---  
  
Referenced by
[merge()](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13),
and
[split()](../../d2/d02/structApp_1_1PropertyData.html#a54a70f401aaa3cd992b833647676b8bf).

## ◆ propertyData

| bmi::multi_index_container<
[PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html),
bmi::indexed_by< bmi::sequenced<>, bmi::hashed_unique<
bmi::member<[PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html),
const char*,
&[PropertySpec::Name](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#a9dbe0f666a30b7c33574047635aa4aef)>,
[CStringHasher](../../d9/d20/structApp_1_1CStringHasher.html),
[CStringHasher](../../d9/d20/structApp_1_1CStringHasher.html) >,
bmi::hashed_unique<
bmi::member<[PropertySpec](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html),
short,
&[PropertySpec::Offset](../../d2/d3c/structApp_1_1PropertyData_1_1PropertySpec.html#ad44bea49f5dc300be1b2f06e1f1ba8c1)>
> > > App::PropertyData::propertyData  
---  
mutable  
  
Referenced by
[addProperty()](../../d2/d02/structApp_1_1PropertyData.html#a7d03b124a06a1399d8337f580c9acd2a),
[findProperty()](../../d2/d02/structApp_1_1PropertyData.html#af131294c6582bbbd292723cdc52022d7),
[getPropertyList()](../../d2/d02/structApp_1_1PropertyData.html#ac697b4d2ae7f2258097b5d63d508379f),
[getPropertyMap()](../../d2/d02/structApp_1_1PropertyData.html#aa53fb59fabeac2789a00247260af211e),
[getPropertyNamedList()](../../d2/d02/structApp_1_1PropertyData.html#a62858579f4b81973d1661262e8c79146),
[merge()](../../d2/d02/structApp_1_1PropertyData.html#a0e2de231b0c3cf9476c8f36b58884a13),
and
[split()](../../d2/d02/structApp_1_1PropertyData.html#a54a70f401aaa3cd992b833647676b8bf).

* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/App/PropertyContainer.h
  * FreeCAD/src/App/PropertyContainer.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

