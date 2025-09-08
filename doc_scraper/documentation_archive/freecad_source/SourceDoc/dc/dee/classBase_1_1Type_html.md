---
url: https://freecad.github.io/SourceDoc/dc/dee/classBase_1_1Type.html
scraped_at: 2025-09-08T15:17:32.211601
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Type](../../dc/dee/classBase_1_1Type.html)

[List of all members](../../dd/db0/classBase_1_1Type-members.html) | Public Types | Public Member Functions | Static Public Member Functions | Static Protected Member Functions

Base::Type Class Reference

[Type](../../dc/dee/classBase_1_1Type.html "Type system class Many of the
classes in the FreeCAD must have their type information registered befo...")
system class Many of the classes in the FreeCAD must have their type
information registered before any instances are created (including, but not
limited to: App::Feature,
[App::Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties."),
[Gui::ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html "General
interface for all visual stuff in FreeCAD This class is used to generate and
handle all aroun...") ).
[More...](../../dc/dee/classBase_1_1Type.html#details)

`#include <Type.h>`

##  Public Types  
  
---  
typedef void *(* | [instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495)) ()  
  
##  Public Member Functions  
  
---  
void * | [createInstance](../../dc/dee/classBase_1_1Type.html#a2d1d33a2453ee324e07ce2412a542e44) ()  
| creates a instance of this type
[More...](../../dc/dee/classBase_1_1Type.html#a2d1d33a2453ee324e07ce2412a542e44)  
  
unsigned [int](../../d1/da0/classint.html) | [getKey](../../dc/dee/classBase_1_1Type.html#a9b9623ec1a23a7ac7002ce6c6138ed71) () const  
const char * | [getName](../../dc/dee/classBase_1_1Type.html#a861a2f6bd2cd2c2df7846e202f0ce137) () const  
const [Type](../../dc/dee/classBase_1_1Type.html) | [getParent](../../dc/dee/classBase_1_1Type.html#a70b006492a4446c1065a97eae91efa1d) () const  
[bool](../../d9/db9/classbool.html) | [isBad](../../dc/dee/classBase_1_1Type.html#ab091b5ccf4f8e3c7c59cb05dde3c2fcb) () const  
[bool](../../d9/db9/classbool.html) | [isDerivedFrom](../../dc/dee/classBase_1_1Type.html#abb24fc578ec80e158584f46d4a5042c7) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
[bool](../../d9/db9/classbool.html) | [operator!=](../../dc/dee/classBase_1_1Type.html#a563bb9e63a4829f69fd2176d7265d073) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
[bool](../../d9/db9/classbool.html) | [operator<](../../dc/dee/classBase_1_1Type.html#a2bfc2cafb8a86bb232698da9c2ca9836) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
[bool](../../d9/db9/classbool.html) | [operator<=](../../dc/dee/classBase_1_1Type.html#acbc06cfb97a6d225c362b0d6f785159e) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
void | [operator=](../../dc/dee/classBase_1_1Type.html#a4ab719148b209f2ce5074b1ddf76d721) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html))  
[bool](../../d9/db9/classbool.html) | [operator==](../../dc/dee/classBase_1_1Type.html#ad39ea5416318e26afd419cc6daad2697) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
[bool](../../d9/db9/classbool.html) | [operator>](../../dc/dee/classBase_1_1Type.html#ac9cce9ec1830357203245faccb0488ed) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
[bool](../../d9/db9/classbool.html) | [operator>=](../../dc/dee/classBase_1_1Type.html#ac98ee38dc8208295ebef6a1bb0b56a99) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
|
[Type](../../dc/dee/classBase_1_1Type.html#a78339313d36891f18427c431ea84e306)
()  
| A constructor.
[More...](../../dc/dee/classBase_1_1Type.html#a78339313d36891f18427c431ea84e306)  
  
|
[Type](../../dc/dee/classBase_1_1Type.html#a26ce658f5055f20610491addb5983ad6)
(const [Type](../../dc/dee/classBase_1_1Type.html)
&[type](../../d9/d98/classtype.html))  
| Construction.
[More...](../../dc/dee/classBase_1_1Type.html#a26ce658f5055f20610491addb5983ad6)  
  
virtual | [~Type](../../dc/dee/classBase_1_1Type.html#a79b5e86eb2dd658180797a1b798194a8) ()  
| Destruction.
[More...](../../dc/dee/classBase_1_1Type.html#a79b5e86eb2dd658180797a1b798194a8)  
  
  
##  Static Public Member Functions  
  
---  
static [Type](../../dc/dee/classBase_1_1Type.html) | [badType](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76) ()  
static void * | [createInstanceByName](../../dc/dee/classBase_1_1Type.html#a93ec2844e72854fbb5902df8a6d7f61d) (const char *TypeName, [bool](../../d9/db9/classbool.html) bLoadModule=false)  
| creates a instance of the named type
[More...](../../dc/dee/classBase_1_1Type.html#a93ec2844e72854fbb5902df8a6d7f61d)  
  
static const [Type](../../dc/dee/classBase_1_1Type.html) | [createType](../../dc/dee/classBase_1_1Type.html#abdc2ccb5c9c300a5278b39db5e321cc0) (const [Type](../../dc/dee/classBase_1_1Type.html) parent, const char *name, [instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
static void | [destruct](../../dc/dee/classBase_1_1Type.html#aeb333337bdff5ab1d455a8c0f8c516a4) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [fromKey](../../dc/dee/classBase_1_1Type.html#ae36aa06b768ac9880d3725ff1cd685b8) (unsigned [int](../../d1/da0/classint.html) key)  
static [Type](../../dc/dee/classBase_1_1Type.html) | [fromName](../../dc/dee/classBase_1_1Type.html#a7fd6fce9272b7886af7a58d2af987c42) (const char *name)  
static [int](../../d1/da0/classint.html) | [getAllDerivedFrom](../../dc/dee/classBase_1_1Type.html#a32edae0aa23297e8f02e8ea935126e80) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html), std::vector< [Type](../../dc/dee/classBase_1_1Type.html) > &List)  
static [int](../../d1/da0/classint.html) | [getNumTypes](../../dc/dee/classBase_1_1Type.html#ab758d6200355a1c74a78cd26706e3d1d) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getTypeIfDerivedFrom](../../dc/dee/classBase_1_1Type.html#ae69252049934864817d7932cc246a593) (const char *name, const [Type](../../dc/dee/classBase_1_1Type.html) parent, [bool](../../d9/db9/classbool.html) bLoadModule=false)  
| Returns the given named type if is derived from parent type, otherwise
return bad type.
[More...](../../dc/dee/classBase_1_1Type.html#ae69252049934864817d7932cc246a593)  
  
static void | [importModule](../../dc/dee/classBase_1_1Type.html#a7e5b01ed0f09e28b038003caa13c3830) (const char *TypeName)  
static void | [init](../../dc/dee/classBase_1_1Type.html#a55b0a9918023eafb441abf1678c8185c) ()  
  
##  Static Protected Member Functions  
  
---  
static std::string | [getModuleName](../../dc/dee/classBase_1_1Type.html#a646b7c4d2779cf5c384b5dfe576c98d0) (const char *ClassName)  
  
## Detailed Description

[Type](../../dc/dee/classBase_1_1Type.html "Type system class Many of the
classes in the FreeCAD must have their type information registered befo...")
system class Many of the classes in the FreeCAD must have their type
information registered before any instances are created (including, but not
limited to: App::Feature,
[App::Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties."),
[Gui::ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html "General
interface for all visual stuff in FreeCAD This class is used to generate and
handle all aroun...") ).

The use of [Type](../../dc/dee/classBase_1_1Type.html "Type system class Many
of the classes in the FreeCAD must have their type information registered
befo...") to store this information provides lots of various functionality for
working with class hierarchies, comparing class types, instantiating objects
from classnames, etc etc.

It is for instance possible to do things like this:

void getRightFeature(Base::Base * anode)

{

assert(anode->getTypeId().isDerivedFrom(App::Feature::getClassTypeId()));

if (anode->getTypeId() == Mesh::MeshFeature::getClassTypeId()) {

// do something..

}

else if (anode->getTypeId() == Part::PartFeature::getClassTypeId()) {

// do something..

}

else {

[Base::Console](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729
"Access to the Console This method is used to gain access to the one and only
instance of the
ConsoleS...")().[Warning](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326
"Prints a warning Message.")("getRightFeature", "Unknown feature type %s!\n",

anode->getTypeId().getName());

}

}

A notable feature of the [Type](../../dc/dee/classBase_1_1Type.html "Type
system class Many of the classes in the FreeCAD must have their type
information registered befo...") class is that it is only 16 bits long and
therefore should be passed around by value for efficiency reasons.

One important note about the use of [Type](../../dc/dee/classBase_1_1Type.html
"Type system class Many of the classes in the FreeCAD must have their type
information registered befo...") to register class information: super classes
must be registered before any of their derived classes are.

## Member Typedef Documentation

## ◆ instantiationMethod

typedef void *(* Base::Type::instantiationMethod) ()  
---  
  
## Constructor & Destructor Documentation

## ◆ Type() [1/2]

Type::Type  | ( | const [Type](../../dc/dee/classBase_1_1Type.html) & | _type_| ) |   
---|---|---|---|---|---  
  
Construction.

Referenced by
[ArchPanel.CommandPanelSheet::Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftobjects.draft_annotation.DraftAnnotation::add_missing_properties_0v19()](../../d4/dca/classdraftobjects_1_1draft__annotation_1_1DraftAnnotation.html#a345b51b0cfae010e7e5574f0a84dd2f3),
[ArchStructure.StructSelectionObserver::addSelection()](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#ac984e4631db3078ffee1dc0fee52df74),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchComponent.Component::execute()](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0),
[draftobjects.layer.LayerContainer::execute()](../../de/d4d/classdraftobjects_1_1layer_1_1LayerContainer.html#a960d8cd7f03fe7426f8cac669671b513),
[ArchSchedule.CommandArchSchedule::IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[draftobjects.layer.Layer::set_properties()](../../d0/ddc/classdraftobjects_1_1layer_1_1Layer.html#aa6a95fe93a36b884d61ef2c668de002e),
and
[ArchReference.ArchReference::setProperties()](../../d3/d06/classArchReference_1_1ArchReference.html#a41a26333eb23a48bdb3271bed98296e5).

## ◆ Type() [2/2]

Type::Type  | ( | | ) |   
---|---|---|---|---  
  
A constructor.

A more elaborate description of the constructor.

Referenced by
[ArchPanel.CommandPanelSheet::Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftobjects.draft_annotation.DraftAnnotation::add_missing_properties_0v19()](../../d4/dca/classdraftobjects_1_1draft__annotation_1_1DraftAnnotation.html#a345b51b0cfae010e7e5574f0a84dd2f3),
[ArchStructure.StructSelectionObserver::addSelection()](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#ac984e4631db3078ffee1dc0fee52df74),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchComponent.Component::execute()](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0),
[draftobjects.layer.LayerContainer::execute()](../../de/d4d/classdraftobjects_1_1layer_1_1LayerContainer.html#a960d8cd7f03fe7426f8cac669671b513),
[ArchSchedule.CommandArchSchedule::IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[draftobjects.layer.Layer::set_properties()](../../d0/ddc/classdraftobjects_1_1layer_1_1Layer.html#aa6a95fe93a36b884d61ef2c668de002e),
and
[ArchReference.ArchReference::setProperties()](../../d3/d06/classArchReference_1_1ArchReference.html#a41a26333eb23a48bdb3271bed98296e5).

## ◆ ~Type()

| Type::~Type  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Destruction.

A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ badType()

| [Type](../../dc/dee/classBase_1_1Type.html) Type::badType  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[Gui::SelectionSingleton::countObjectsOfType()](../../d4/dca/classGui_1_1SelectionSingleton.html#ae52f2add17825f666164895491c3917f),
[createInstanceByName()](../../dc/dee/classBase_1_1Type.html#a93ec2844e72854fbb5902df8a6d7f61d),
[fromKey()](../../dc/dee/classBase_1_1Type.html#ae36aa06b768ac9880d3725ff1cd685b8),
[fromName()](../../dc/dee/classBase_1_1Type.html#a7fd6fce9272b7886af7a58d2af987c42),
[Gui::SelectionSingleton::getObjectList()](../../d4/dca/classGui_1_1SelectionSingleton.html#aa30d7537c528c5829337d4ec05357bfd),
[Gui::SelectionSingleton::getObjectsOfType()](../../d4/dca/classGui_1_1SelectionSingleton.html#a702f9861ac1b749133550fec78c3f101),
[getTypeIfDerivedFrom()](../../dc/dee/classBase_1_1Type.html#ae69252049934864817d7932cc246a593),
[Gui::DAG::FilterOrigin::goFilter()](../../d5/dff/classGui_1_1DAG_1_1FilterOrigin.html#a52a1c4f0ed387fbd9ed995e99f71818e),
[Gui::DAG::FilterTyped::goFilter()](../../dd/d76/classGui_1_1DAG_1_1FilterTyped.html#a6014b0c63b3c4341c7a94965dbcf39a5),
[Base::BaseClass::init()](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7),
[App::Extension::initExtensionSubclass()](../../d8/dc7/classApp_1_1Extension.html#ad89245f6dbe32a71396c452ea8148ce7),
[Base::BaseClass::initSubclass()](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2),
and
[isDerivedFrom()](../../dc/dee/classBase_1_1Type.html#abb24fc578ec80e158584f46d4a5042c7).

## ◆ createInstance()

void * Type::createInstance  | ( | | ) |   
---|---|---|---|---  
  
creates a instance of this type

Referenced by
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[Part::PropertyGeometryList::Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[TechDraw::PropertyCenterLineList::Restore()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList::Restore()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList::Restore()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
[TechDraw::PropertyGeomFormatList::Restore()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807),
[App::ExtensionContainer::restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab),
and
[Sandbox::DocumentObjectProtectorPy::setattr()](../../d3/d95/classSandbox_1_1DocumentObjectProtectorPy.html#ac8490e2b3e2c078a8bb27eb6bb608f56).

## ◆ createInstanceByName()

| void * Type::createInstanceByName  | ( | const char *  | _TypeName_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _bLoadModule_ = `false`  
| ) | |   
static  
  
creates a instance of the named type

References
[badType()](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76),
[fromName()](../../dc/dee/classBase_1_1Type.html#a7fd6fce9272b7886af7a58d2af987c42),
and
[importModule()](../../dc/dee/classBase_1_1Type.html#a7e5b01ed0f09e28b038003caa13c3830).

Referenced by
[MeshGui::DlgEvaluateMeshImp::addViewProvider()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a40061f032d5f55a73a2c0eb3a699e886),
[Part::AttachExtension::changeAttacherType()](../../dc/d47/classPart_1_1AttachExtension.html#a0785648a30100b85d565b428468ac356),
[Gui::FreeCADGui_subgraphFromObject()](../../d9/dad/namespaceGui.html#a1562062f6fcff8f9ec05618c80435514),
and
[App::PropertyPersistentObject::setValue()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a117bd17a68a39872c084cf4e48401922).

## ◆ createType()

| const [Type](../../dc/dee/classBase_1_1Type.html) Type::createType  | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _parent_ ,   
---|---|---|---  
|  | const char *  | _name_ ,   
|  | [instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) | _method_ = `nullptr`  
| ) | |   
static  
  
References
[getKey()](../../dc/dee/classBase_1_1Type.html#a9b9623ec1a23a7ac7002ce6c6138ed71).

Referenced by
[Base::BaseClass::init()](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7),
[App::Extension::initExtensionSubclass()](../../d8/dc7/classApp_1_1Extension.html#ad89245f6dbe32a71396c452ea8148ce7),
and
[Base::BaseClass::initSubclass()](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2).

## ◆ destruct()

| void Type::destruct  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[App::Application::destruct()](../../da/dbf/classApp_1_1Application.html#a2429ab2a8f4255a5ce2d970aa74ba7f3).

## ◆ fromKey()

| [Type](../../dc/dee/classBase_1_1Type.html) Type::fromKey  | ( | unsigned [int](../../d1/da0/classint.html) | _key_| ) |   
---|---|---|---|---|---  
static  
  
References
[badType()](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76).

## ◆ fromName()

| [Type](../../dc/dee/classBase_1_1Type.html) Type::fromName  | ( | const char *  | _name_| ) |   
---|---|---|---|---|---  
static  
  
References
[badType()](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76).

Referenced by
[PartGui::Mirroring::accept()](../../db/d41/classPartGui_1_1Mirroring.html#a65b4bef12c8f1db83eee1cd6799f2794),
[StdCmdAlignment::activated()](../../df/d17/classStdCmdAlignment.html#a44409be4abd266d5d5e34dacb5484101),
[Gui::Application::activateWorkbench()](../../d9/da8/classGui_1_1Application.html#ac3b3b8a91ba204c6180dab0dccc1a6d8),
[FemGui::ViewProviderFemAnalysis::canDragObject()](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a2d0a02dafcabd5a3d2217137fe2fe63c),
[Part::AttachExtension::changeAttacherType()](../../dc/d47/classPart_1_1AttachExtension.html#a0785648a30100b85d565b428468ac356),
[Part::FaceMaker::ConstructFromType()](../../df/dde/classPart_1_1FaceMaker.html#ac03e77a98786c3ceefc95bacb431f060),
[Gui::SelectionSingleton::countObjectsOfType()](../../d4/dca/classGui_1_1SelectionSingleton.html#ae52f2add17825f666164895491c3917f),
[createInstanceByName()](../../dc/dee/classBase_1_1Type.html#a93ec2844e72854fbb5902df8a6d7f61d),
[Gui::Dialog::DlgAddProperty::DlgAddProperty()](../../d3/d89/classGui_1_1Dialog_1_1DlgAddProperty.html#a54a1e5a0ea475b11a47a9a7ba164f89f),
[Part::AttachExtension::extHandleChangedPropertyName()](../../dc/d47/classPart_1_1AttachExtension.html#a660e1d33e4a6e9d23e2178b45395d9fe),
[PartGui::ViewProviderBoolean::getIcon()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#a61052fd656138212b0088e7a8d081599),
[Fem::FemPostFilter::getInputData()](../../d8/d6f/classFem_1_1FemPostFilter.html#ae3dbe91d8a70d85554e49b2f9d3a079b),
[Gui::SelectionSingleton::getObjectsOfType()](../../d4/dca/classGui_1_1SelectionSingleton.html#a702f9861ac1b749133550fec78c3f101),
[TechDrawGui::QGVPage::getStyleType()](../../dd/dba/classTechDrawGui_1_1QGVPage.html#a062026ca10b83ed8280b1bc6be30327d),
[getTypeIfDerivedFrom()](../../dc/dee/classBase_1_1Type.html#ae69252049934864817d7932cc246a593),
[Gui::View3DInventorPy::getViewProvidersOfType()](../../d3/df7/classGui_1_1View3DInventorPy.html#acc845bf386bd5e69dabfd9a99329745f),
[Gui::DAG::FilterOrigin::goFilter()](../../d5/dff/classGui_1_1DAG_1_1FilterOrigin.html#a52a1c4f0ed387fbd9ed995e99f71818e),
[Gui::DAG::FilterTyped::goFilter()](../../dd/d76/classGui_1_1DAG_1_1FilterTyped.html#a6014b0c63b3c4341c7a94965dbcf39a5),
[Fem::FemAnalysis::handleChangedPropertyName()](../../de/d36/classFem_1_1FemAnalysis.html#a77d4363b7c6734ec7754d6c4de10a481),
[Part::Circle::handleChangedPropertyName()](../../de/de4/classPart_1_1Circle.html#aac14a5128cb8850c0cd7f37ffc71e22a),
[Part::Ellipse::handleChangedPropertyName()](../../d6/d22/classPart_1_1Ellipse.html#a7448b87a31bf68edc8d6a6909613615b),
[Part::BodyBase::handleChangedPropertyName()](../../da/dc8/classPart_1_1BodyBase.html#a2038d6fd9d31b5033c193ca7a95d0b33),
[PartDesign::Boolean::handleChangedPropertyName()](../../d2/d81/classPartDesign_1_1Boolean.html#ad635959d9d69278a1c46fbd6cc0f78f4),
[Surface::Extend::handleChangedPropertyName()](../../d1/d22/classSurface_1_1Extend.html#aa2e1ed26c2018e7234938836df41545c),
[TechDraw::DrawViewBalloon::handleChangedPropertyName()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a8f43bff2ef5b6712e7fd0546b639e6ef),
[PartGui::ViewProvider2DObjectGrid::handleChangedPropertyType()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a4c2d97cecf5419da9ce703e47f8c1e6a),
[PartDesign::Transformed::handleChangedPropertyType()](../../dd/de1/classPartDesign_1_1Transformed.html#a9e4288037e29095bf566a11f3f13fe12),
[Part::Primitive::handleChangedPropertyType()](../../d2/d31/classPart_1_1Primitive.html#a1e49f13eafbcb2ce0de44916a8407cf7),
[App::Extension::initExtensionSubclass()](../../d8/dc7/classApp_1_1Extension.html#ad89245f6dbe32a71396c452ea8148ce7),
[Base::BaseClass::initSubclass()](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2),
[Gui::Node_Object::Node_Object()](../../d0/de8/structGui_1_1Node__Object.html#a543f285e93048b566b5def886e19335d),
[Gui::View3DInventor::OnChange()](../../da/d75/classGui_1_1View3DInventor.html#ab90bd3cd58679e0b888a0bf930791e24),
[Gui::GraphicsView3D::OnChange()](../../df/d0b/classGui_1_1GraphicsView3D.html#a2ced2b0dd60f0a3c0d6b2a7c627a182a),
[FemGui::ViewProviderFemPostObject::onChanged()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a5d27aeff234b60ec0214c939556b26c5),
[Gui::NavigationStyle::openPopupMenu()](../../d2/d1c/classGui_1_1NavigationStyle.html#a6831ec68eec376f2b9e8f4ea5a54f7bc),
[Gui::Dialog::find_placement::operator()()](../../db/d20/classGui_1_1Dialog_1_1find__placement.html#a52917723bad2ec3993bd7adbe3804722),
[Gui::Dialog::find_transform::operator()()](../../df/d26/classGui_1_1Dialog_1_1find__transform.html#a5c40eb4158fa6c4af1c3e27a25a18595),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
[Part::Geometry::Restore()](../../dc/df0/classPart_1_1Geometry.html#a1aae6b35e6fba2cbf794c5391847c77b),
[Part::PropertyGeometryList::Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[TechDraw::PropertyCenterLineList::Restore()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList::Restore()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList::Restore()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
[TechDraw::PropertyGeomFormatList::Restore()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807),
[App::ExtensionContainer::restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab),
[Gui::TreeView::rowsInserted()](../../d9/ddf/classGui_1_1TreeView.html#a14fe0e1762ce6ca1f12f092b7d9477f0),
[Gui::Application::sActivateView()](../../d9/da8/classGui_1_1Application.html#a940e36f245a720dd958186b5962f16dc),
[Gui::Application::sActiveView()](../../d9/da8/classGui_1_1Application.html#a395485b4d2f85231d2762749059164f1),
[Gui::View3DInventorPy::setNavigationType()](../../d3/df7/classGui_1_1View3DInventorPy.html#aeae7743fabfade61d16dac1ddbdca7b4),
[App::PropertyPersistentObject::setValue()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a117bd17a68a39872c084cf4e48401922),
[AttacherGui::AttacherGuiPy::sGetModeStrings()](../../d9/d27/classAttacherGui_1_1AttacherGuiPy.html#a8fc6f693da46263c05484d0b874ff294),
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239),
[App::PropertyLinkSubList::upgrade()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b),
and
[InspectionGui::VisualInspection::VisualInspection()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#aa13e595beac41fb1b077d794cd7fc0bc).

## ◆ getAllDerivedFrom()

| [int](../../d1/da0/classint.html) Type::getAllDerivedFrom  | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_ ,   
---|---|---|---  
|  | std::vector< [Type](../../dc/dee/classBase_1_1Type.html) > & | _List_  
| ) | |   
static  
  
Referenced by
[Gui::Dialog::DlgAddProperty::DlgAddProperty()](../../d3/d89/classGui_1_1Dialog_1_1DlgAddProperty.html#a54a1e5a0ea475b11a47a9a7ba164f89f),
[Gui::UserNavigationStyle::getUserFriendlyNames()](../../d3/de8/classGui_1_1UserNavigationStyle.html#a6182d45703e51b60a19f87af927fbc86),
and
[Gui::View3DInventorPy::listNavigationTypes()](../../d3/df7/classGui_1_1View3DInventorPy.html#af405ff4c12945637c92230889b88754f).

## ◆ getKey()

unsigned [int](../../d1/da0/classint.html) Base::Type::getKey  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[createType()](../../dc/dee/classBase_1_1Type.html#abdc2ccb5c9c300a5278b39db5e321cc0),
[Gui::PropertyView::onTimer()](../../d8/d18/classGui_1_1PropertyView.html#aa53958cefcade980c3ffe795f787d6de),
[operator!=()](../../dc/dee/classBase_1_1Type.html#a563bb9e63a4829f69fd2176d7265d073),
[operator<()](../../dc/dee/classBase_1_1Type.html#a2bfc2cafb8a86bb232698da9c2ca9836),
[operator<=()](../../dc/dee/classBase_1_1Type.html#acbc06cfb97a6d225c362b0d6f785159e),
[operator==()](../../dc/dee/classBase_1_1Type.html#ad39ea5416318e26afd419cc6daad2697),
[operator>()](../../dc/dee/classBase_1_1Type.html#ac9cce9ec1830357203245faccb0488ed),
and
[operator>=()](../../dc/dee/classBase_1_1Type.html#ac98ee38dc8208295ebef6a1bb0b56a99).

## ◆ getModuleName()

| string Type::getModuleName  | ( | const char *  | _ClassName_| ) |   
---|---|---|---|---|---  
staticprotected  
  
Referenced by
[importModule()](../../dc/dee/classBase_1_1Type.html#a7e5b01ed0f09e28b038003caa13c3830).

## ◆ getName()

const char * Type::getName  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[PartDesignGui::TaskDlgFeatureParameters::accept()](../../df/d42/classPartDesignGui_1_1TaskDlgFeatureParameters.html#abfc2d8ecb714c2b558cc8feb07fa55c3),
[StdCmdToggleSelectability::activated()](../../d6/d27/classStdCmdToggleSelectability.html#a0ce2e8138a2c546adb161b8804521a28),
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a77502422ab7bde4fb01ab4474fd930af),
[Gui::View3DInventor::customEvent()](../../da/d75/classGui_1_1View3DInventor.html#aaecd3db84b1c65974ddf1bc692d25686),
[Gui::DocumentObjectItem::displayStatusInfo()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a235f26b8fbf37e4e4efccdae9cbbada0),
[Gui::ViewProvider::eventCallback()](../../d3/db3/classGui_1_1ViewProvider.html#a2c9bbafc597aa5e02ebe9f8aac8a2c99),
[Gui::View3DInventorPy::getNavigationType()](../../d3/df7/classGui_1_1View3DInventorPy.html#a94606713a2f513eaecc2cb27066d18da),
[App::OriginGroupExtension::getOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2),
[AttacherGui::getUIStrings()](../../d9/d53/namespaceAttacherGui.html#a4633c8769798583ed5a439779508c2cc),
[PartDesign::Fillet::handleChangedPropertyType()](../../d0/d50/classPartDesign_1_1Fillet.html#a4dec9f6780093c637468b21782cc0347),
[Part::Part2DObject::handleChangedPropertyType()](../../d9/d57/classPart_1_1Part2DObject.html#a3b4551d03504c25446ede14dcf2309e3),
[PartDesign::Chamfer::handleChangedPropertyType()](../../da/d6f/classPartDesign_1_1Chamfer.html#a8efe172f26b587a447f0bb5b183ae67b),
[TechDraw::DrawPage::handleChangedPropertyType()](../../d9/d5a/classTechDraw_1_1DrawPage.html#adde1799122996153278b2c68d4fa9b80),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[Gui::Dialog::DlgPropertyLink::init()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#a0f9c31263c267be5f9d378e4f49cfa8a),
[App::Extension::name()](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016),
[Gui::ViewProviderLink::onChanged()](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[Base::XMLReader::readFiles()](../../dc/d95/classBase_1_1XMLReader.html#a53b94bea9a61011f67ee6f5e98e53f16),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[Part::GeometryPersistenceExtension::Save()](../../de/db6/classPart_1_1GeometryPersistenceExtension.html#af4b4cb8e926350eb9cf1f7c78ce2a7c8),
[Part::AttachExtension::setAttacher()](../../dc/d47/classPart_1_1AttachExtension.html#a1e4d65c3b672b1760b037891d419e065),
[InspectionGui::ViewProviderInspection::setDistances()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a44c21c9eb69fa551a912211602ee0e70),
and
[App::LinkBaseExtension::setProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770).

## ◆ getNumTypes()

| [int](../../d1/da0/classint.html) Type::getNumTypes  | ( | | ) |   
---|---|---|---|---  
static  
  
## ◆ getParent()

const [Type](../../dc/dee/classBase_1_1Type.html) Type::getParent  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Gui::Dialog::DlgPropertyLink::init()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#a0f9c31263c267be5f9d378e4f49cfa8a),
and
[isDerivedFrom()](../../dc/dee/classBase_1_1Type.html#abb24fc578ec80e158584f46d4a5042c7).

## ◆ getTypeIfDerivedFrom()

| [Type](../../dc/dee/classBase_1_1Type.html) Type::getTypeIfDerivedFrom  | ( | const char *  | _name_ ,   
---|---|---|---  
|  | const [Type](../../dc/dee/classBase_1_1Type.html) | _parent_ ,   
|  | [bool](../../d9/db9/classbool.html) | _bLoadModule_ = `false`  
| ) | |   
static  
  
Returns the given named type if is derived from parent type, otherwise return
bad type.

References
[badType()](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76),
[fromName()](../../dc/dee/classBase_1_1Type.html#a7fd6fce9272b7886af7a58d2af987c42),
and
[importModule()](../../dc/dee/classBase_1_1Type.html#a7e5b01ed0f09e28b038003caa13c3830).

Referenced by
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[Gui::WorkbenchManager::createWorkbench()](../../d1/daa/classGui_1_1WorkbenchManager.html#a39b8fc7724a24f5e7c63d9d4268f09dd),
[Gui::View3DInventorViewer::setNavigationType()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a989c1b0476cdaa63adadbc7ee70a84a3),
and
[Gui::Document::slotNewObject()](../../de/d4e/classGui_1_1Document.html#a73fa9bf80a6dc858e853771c6e3f4cdb).

## ◆ importModule()

| void Type::importModule  | ( | const char *  | _TypeName_| ) |   
---|---|---|---|---|---  
static  
  
References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[getModuleName()](../../dc/dee/classBase_1_1Type.html#a646b7c4d2779cf5c384b5dfe576c98d0),
[Base::Interpreter()](../../db/d07/namespaceBase.html#a2ee9c987b769c5d1ed5f2fe69b21d2c9),
[Base::InterpreterSingleton::loadModule()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#af59e1b874f05bcb2792ec395788578be),
and
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964).

Referenced by
[createInstanceByName()](../../dc/dee/classBase_1_1Type.html#a93ec2844e72854fbb5902df8a6d7f61d),
[getTypeIfDerivedFrom()](../../dc/dee/classBase_1_1Type.html#ae69252049934864817d7932cc246a593),
and
[App::PropertyPersistentObject::setValue()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a117bd17a68a39872c084cf4e48401922).

## ◆ init()

| void Type::init  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[App::Application::initTypes()](../../da/dbf/classApp_1_1Application.html#a7fd51c3ba729d368d8f150a720af49e1),
and
[DocumentObject.DocumentObject::onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882).

## ◆ isBad()

[bool](../../d9/db9/classbool.html) Base::Type::isBad  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[Part::FaceMaker::ConstructFromType()](../../df/dde/classPart_1_1FaceMaker.html#ac03e77a98786c3ceefc95bacb431f060),
[Gui::Dialog::DlgPropertyLink::init()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#a0f9c31263c267be5f9d378e4f49cfa8a),
[App::Extension::initExtension()](../../d8/dc7/classApp_1_1Extension.html#a1ae201ccac2b97ba9107151b9e507def),
[App::Extension::initExtensionType()](../../d8/dc7/classApp_1_1Extension.html#a12ec705423cb1952b395a4d135f2f734),
[App::Extension::name()](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016),
[App::ExtensionContainer::restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab),
and
[Gui::Document::setActiveView()](../../de/d4e/classGui_1_1Document.html#a1933003b2ee08a001a5858c0e8d71e93).

## ◆ isDerivedFrom()

[bool](../../d9/db9/classbool.html) Type::isDerivedFrom  | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |  const  
---|---|---|---|---|---  
  
References
[badType()](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76),
and
[getParent()](../../dc/dee/classBase_1_1Type.html#a70b006492a4446c1065a97eae91efa1d).

Referenced by
[PartDesignGui::TaskDlgFeatureParameters::accept()](../../df/d42/classPartDesignGui_1_1TaskDlgFeatureParameters.html#abfc2d8ecb714c2b558cc8feb07fa55c3),
[PartDesignGui::TaskDlgSketchBasedParameters::accept()](../../da/def/classPartDesignGui_1_1TaskDlgSketchBasedParameters.html#a781c55f79eb60cc2c7472679f26dcce7),
[StdCmdGroup::activated()](../../d0/de4/classStdCmdGroup.html#a44a9faa66df180f400cd830bb538771d),
[Gui::Application::activateWorkbench()](../../d9/da8/classGui_1_1Application.html#ac3b3b8a91ba204c6180dab0dccc1a6d8),
[MeshGui::DlgEvaluateMeshImp::addViewProvider()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a40061f032d5f55a73a2c0eb3a699e886),
[SketcherGui::FilletSelection::allow()](../../dd/d6f/classSketcherGui_1_1FilletSelection.html#a2d300c4873259393e235ef5a3845825b),
[SketcherGui::TrimmingSelection::allow()](../../de/d39/classSketcherGui_1_1TrimmingSelection.html#a981ac86ae1dbd466c3f25a6ffb7774f8),
[PartDesignGui::ReferenceSelection::allow()](../../dd/d1c/classPartDesignGui_1_1ReferenceSelection.html#aba5a74db909e196f326ebb626e1ba150),
[SketcherGui::ExternalSelection::allow()](../../d3/dff/classSketcherGui_1_1ExternalSelection.html#a8cb2852af5a0bfc42d8844d3f5d1edde),
[Gui::QuantitySpinBox::apply()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#ac3ec986d0729752d078f3c57a18f7cca),
[PartDesignGui::collectMovableDependencies()](../../dc/d12/namespacePartDesignGui.html#a134e411f38de8ca01fe259064cdcc27b),
[Gui::Document::createView()](../../de/d4e/classGui_1_1Document.html#a1235bbc0ddca0b8c9465d9d491d79541),
[MeshGui::ViewProviderMeshCurvature::curvatureInfoCallback()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd81924b9ccb33db4d9fb1fe49f1f934),
[Sketcher::SketchObject::evaluateSupport()](../../d9/dad/classSketcher_1_1SketchObject.html#ae2d3e03c3503536535164dfea9630169),
[Drawing::FeatureProjection::execute()](../../d8/d73/classDrawing_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Inspection::Feature::execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[PartDesign::Pipe::execute()](../../da/d61/classPartDesign_1_1Pipe.html#a860c1038a89156936a4d1fd44481cfbd),
[Raytracing::LuxFeature::execute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a235b146fb9255cb705a6b86fb6967c3d),
[Raytracing::RayFeature::execute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[Robot::Edge2TracObject::execute()](../../d8/df5/classRobot_1_1Edge2TracObject.html#a05d96baf25af72c1c01f165a8dac7f63),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[Surface::Filling::execute()](../../d8/df7/classSurface_1_1Filling.html#ab31cd9c2fd6bd4e15a80b7065c071eae),
[TechDraw::DrawViewSpreadsheet::execute()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a2d98f05816771e2b3a057443ea2f981c),
[TechDraw::FeatureProjection::execute()](../../dd/ddc/classTechDraw_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[PartDesign::Body::execute()](../../dd/db8/classPartDesign_1_1Body.html#a4abca6b2645adade81347d0e850a2659),
[Surface::Extend::execute()](../../d1/d22/classSurface_1_1Extend.html#a50a4d6f3fb960ba8acaa558639be59f0),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[MeshGui::ViewProviderMesh::faceInfoCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae3d2f360b9f432962521c1bb1b77dd98),
[MeshGui::ViewProviderMesh::fillHoleCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ad3cdb2b5549c092780ef6b1bb252cc02),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[PartDesign::Feature::getBaseObject()](../../d7/d51/classPartDesign_1_1Feature.html#a4b32fcefa87c31a546571d96cfd41413),
[InspectionGui::ViewProviderInspection::getIcon()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a76d57438c1350bd9a432557f0c23dc5e),
[Fem::FemPostFilter::getInputData()](../../d8/d6f/classFem_1_1FemPostFilter.html#ae3dbe91d8a70d85554e49b2f9d3a079b),
[TechDraw::ShapeExtractor::getShapesFromObject()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4043c946e78f533e4f060cb3b87b5691),
[PartDesign::Transformed::getSketchObject()](../../dd/de1/classPartDesign_1_1Transformed.html#a7b52a3658c0f24c04278bc8c1fcc55fd),
[PartDesign::ProfileBased::getSupportFace()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a021db5d3d85698ee0d5a4f8d8a4391a5),
[PartDesign::MultiTransform::getTransformations()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a33b71497cd61478ec6fb8d660b759b6b),
[PartDesign::Scaled::getTransformations()](../../db/dce/classPartDesign_1_1Scaled.html#a114f3de4184f1d8b572ed057609c03d6),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[AttacherGui::getUIStrings()](../../d9/d53/namespaceAttacherGui.html#a4633c8769798583ed5a439779508c2cc),
[PartGui::ViewProvider2DObjectGrid::handleChangedPropertyType()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a4c2d97cecf5419da9ce703e47f8c1e6a),
[PartDesign::Transformed::handleChangedPropertyType()](../../dd/de1/classPartDesign_1_1Transformed.html#a9e4288037e29095bf566a11f3f13fe12),
[Part::Primitive::handleChangedPropertyType()](../../d2/d31/classPart_1_1Primitive.html#a1e49f13eafbcb2ce0de44916a8407cf7),
[Gui::Dialog::DlgPropertyLink::init()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#a0f9c31263c267be5f9d378e4f49cfa8a),
[InspectionGui::ViewProviderInspection::inspectCallback()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a4e6895f19ff09d06e34c94fe7df62517),
[InspectionGui::ViewProviderInspection::inspectDistance()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac0352eb6e4af339e08975b253269b0ab),
[PartDesign::Feature::isDatum()](../../d7/d51/classPartDesign_1_1Feature.html#ae76e0e61b446d25dde1053d691c87081),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
[PartDesignGui::isFeatureMovable()](../../dc/d12/namespacePartDesignGui.html#a6b3f9e577dd13e884d8aca2e0ce6a6c8),
[TechDrawGui::QGIProjGroup::itemChange()](../../db/d20/classTechDrawGui_1_1QGIProjGroup.html#aa1611210aac32505ffac13b3c321ba65),
[PartDesignGui::TaskFeaturePick::makeCopy()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a9e9b1a639025522ada407aaa6b19596e),
[MeshGui::ViewProviderMesh::markPartCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a6eb548accf81ef25b6aa376ac7fa53a8),
[Gui::TreeView::mouseDoubleClickEvent()](../../d9/ddf/classGui_1_1TreeView.html#ad2e4760d9a018ee92f83e36adbadcfa7),
[Gui::Dialog::DlgMaterialPropertiesImp::on_ambientColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a49825eab8b369a08e23c6e14f3929301),
[Gui::Dialog::DlgMaterialPropertiesImp::on_diffuseColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a9ccc20c9c5d253b5e9ed7fbe4d34f13e),
[Gui::Dialog::DlgMaterialPropertiesImp::on_emissiveColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aa448adcda1877165e407fafcf0354cf3),
[Gui::Dialog::DlgMaterialPropertiesImp::on_shininess_valueChanged()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#af0d5014718205e140eb9e8799167d518),
[Gui::Dialog::DlgMaterialPropertiesImp::on_specularColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a458ce64d9a0930c339444dff48ac809f),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[Gui::ManualAlignment::probePickedCallback()](../../d7/d97/classGui_1_1ManualAlignment.html#af255c1f31bf62293781d8a04cbecbceb),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[App::ExtensionContainer::registerExtension()](../../d6/d76/classApp_1_1ExtensionContainer.html#a007eb07d5313eaa01d14462d7b7d960d),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[SketcherGui::DrawSketchHandlerTrimming::releaseButton()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a19ae638451e1d23b50c23409a6eeded1),
[PartDesignGui::relinkToOrigin()](../../dc/d12/namespacePartDesignGui.html#a04b9ca5c57afc44a5ab6f8bc71f9a681),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::ExtensionContainer::restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab),
[PartGui::FaceColors::Private::selectionCallback()](../../d4/d4b/classFaceColors_1_1Private.html#a5ff66514ce5125d41dd193313edfdb8e),
[Gui::Document::setHide()](../../de/d4e/classGui_1_1Document.html#a210ce66ce252fecbfb7107f60c37429c),
[Gui::Document::setShow()](../../de/d4e/classGui_1_1Document.html#ab3f9186bfa28a712509d5fcc077754ef),
[Gui::Application::setupContextMenu()](../../d9/da8/classGui_1_1Application.html#a926aeecf53a279bac2bc10675733c48d),
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643),
[Gui::Document::slotDeletedObject()](../../de/d4e/classGui_1_1Document.html#a02acfc1218f2666ad7e6b80c804abc99),
[Gui::ManualAlignment::slotDeletedObject()](../../d7/d97/classGui_1_1ManualAlignment.html#a175a5f2e149be360e8a143456cd48ae1),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[Gui::TaskView::TaskSelectLinkProperty::TaskSelectLinkProperty()](../../d3/d1b/classGui_1_1TaskView_1_1TaskSelectLinkProperty.html#a6ec8c7b8e4d45bde4f8ce5968bdd91b4),
[Gui::SelectionFilter::test()](../../d3/de7/classGui_1_1SelectionFilter.html#a5e11b2a1c8e404cf6236ee475fe5e0dc),
[Gui::PropertyEditor::PropertyMatrixItem::toolTip()](../../d6/d20/classGui_1_1PropertyEditor_1_1PropertyMatrixItem.html#a0d3887efda4155ea320aba09ee6af779),
[Gui::PropertyEditor::PropertyRotationItem::toolTip()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#abbb3c671e82d0c8d54f1f6f2b95abe5d),
[Gui::PropertyEditor::PropertyPlacementItem::toolTip()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#add11217c79e909fa0d6a5fa97d739d2f),
[Gui::PropertyEditor::PropertyMaterialItem::toolTip()](../../da/d17/classGui_1_1PropertyEditor_1_1PropertyMaterialItem.html#a493166d2591c115bc095c5866bd5e4a0),
[Gui::PropertyEditor::PropertyMaterialListItem::toolTip()](../../d9/d3e/classGui_1_1PropertyEditor_1_1PropertyMaterialListItem.html#a420082fd5b1643a150fb0650377990cc),
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239),
[MeshGui::ViewProviderMeshCurvature::updateData()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a50f18a08491899786bd7afbcffe50033),
[PartGui::ViewProviderBoolean::updateData()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#ae38d6575df4dd650428a3d5873874d94),
[PartGui::ViewProviderMultiFuse::updateData()](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a2dd30d90dd627899aae55dd7f6082bfd),
[PartGui::ViewProviderMultiCommon::updateData()](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#afd2565caa649c9122a8da1bad7217b88),
[PartGui::ViewProviderCompound::updateData()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a864f55403bd4a3b5a81834205fe9561d),
[PartGui::ViewProviderCustom::updateData()](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
[PathGui::ViewProviderArea::updateData()](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a33f43f1d72596152fa4d6944b59360b0),
[PathGui::ViewProviderAreaView::updateData()](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a5681f9ff35ad2a07e43b5847ebe09f15),
[PathGui::ViewProviderPathShape::updateData()](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#ac696ef550f0e27b0665de391ca5891a9),
[SketcherGui::ViewProviderCustom::updateData()](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
[Sketcher::SketchObject::validateExternalLinks()](../../d9/dad/classSketcher_1_1SketchObject.html#aeb60483adfd2364036d7264a10392ee9),
[Gui::PropertyEditor::PropertyStringItem::value()](../../dd/d22/classGui_1_1PropertyEditor_1_1PropertyStringItem.html#af7d6ebf7226ead072d520b62051d77ed),
[Gui::PropertyEditor::PropertyFontItem::value()](../../de/df5/classGui_1_1PropertyEditor_1_1PropertyFontItem.html#ad4b2d0d05eea1344b23cf64e5af0bf85),
[Gui::PropertyEditor::PropertyIntegerItem::value()](../../de/d3b/classGui_1_1PropertyEditor_1_1PropertyIntegerItem.html#af8403087a42310e8e396c69ba89b31dc),
[Gui::PropertyEditor::PropertyIntegerConstraintItem::value()](../../d6/d39/classGui_1_1PropertyEditor_1_1PropertyIntegerConstraintItem.html#a2b469055bba9c4ee087df3e587dcf857),
[Gui::PropertyEditor::PropertyFloatItem::value()](../../db/df4/classGui_1_1PropertyEditor_1_1PropertyFloatItem.html#a3504141c979ff4cb5f9ea5cf54a05be9),
[Gui::PropertyEditor::PropertyUnitItem::value()](../../d7/d5d/classGui_1_1PropertyEditor_1_1PropertyUnitItem.html#a77537bbfa6f70779bae14ec0c8af8ce7),
[Gui::PropertyEditor::PropertyFloatConstraintItem::value()](../../d2/d0a/classGui_1_1PropertyEditor_1_1PropertyFloatConstraintItem.html#acbaae4a3b13384b2e824bc1162c4c668),
[Gui::PropertyEditor::PropertyBoolItem::value()](../../d4/dc0/classGui_1_1PropertyEditor_1_1PropertyBoolItem.html#a656033aba09820501b40c49cfd240a45),
[Gui::PropertyEditor::PropertyVectorItem::value()](../../dc/d86/classGui_1_1PropertyEditor_1_1PropertyVectorItem.html#a5856c2d9815846f5c63baf8785c77e0e),
[Gui::PropertyEditor::PropertyVectorListItem::value()](../../dc/d19/classGui_1_1PropertyEditor_1_1PropertyVectorListItem.html#a8043a12f10c28a8bf2ef6ba93a7812cb),
[Gui::PropertyEditor::PropertyVectorDistanceItem::value()](../../db/dd4/classGui_1_1PropertyEditor_1_1PropertyVectorDistanceItem.html#a022f31e7063dd604bec6e771a36d0c96),
[Gui::PropertyEditor::PropertyMatrixItem::value()](../../d6/d20/classGui_1_1PropertyEditor_1_1PropertyMatrixItem.html#afcae29df2122fd2d492f14d7bfc3f781),
[Gui::PropertyEditor::PropertyRotationItem::value()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a863981824fc5e2a970540f4e707913d1),
[Gui::PropertyEditor::PropertyPlacementItem::value()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a02b71a4429874d510e780c4a2375a1be),
[Gui::PropertyEditor::PropertyEnumItem::value()](../../d1/dd0/classGui_1_1PropertyEditor_1_1PropertyEnumItem.html#a94427cf59c1c81076fda89e8f9f0dd7f),
[Gui::PropertyEditor::PropertyStringListItem::value()](../../d7/d2f/classGui_1_1PropertyEditor_1_1PropertyStringListItem.html#ac7e887e41792012af96be518db34a533),
[Gui::PropertyEditor::PropertyFloatListItem::value()](../../de/d74/classGui_1_1PropertyEditor_1_1PropertyFloatListItem.html#a36c1a4829509db372d7f393525345529),
[Gui::PropertyEditor::PropertyIntegerListItem::value()](../../d4/d5f/classGui_1_1PropertyEditor_1_1PropertyIntegerListItem.html#a579b1460c152751041d4d9bdede76c69),
[Gui::PropertyEditor::PropertyColorItem::value()](../../d9/d81/classGui_1_1PropertyEditor_1_1PropertyColorItem.html#acf049af57cd349ad168116b0e0ab7e26),
[Gui::PropertyEditor::PropertyMaterialItem::value()](../../da/d17/classGui_1_1PropertyEditor_1_1PropertyMaterialItem.html#acdc82f103ed6664a083e9fa11532c4cc),
[Gui::PropertyEditor::PropertyMaterialListItem::value()](../../d9/d3e/classGui_1_1PropertyEditor_1_1PropertyMaterialListItem.html#a7440116fc91a842840573c86ddbee0ab),
[Gui::PropertyEditor::PropertyFileItem::value()](../../d3/d1f/classGui_1_1PropertyEditor_1_1PropertyFileItem.html#a803bcb00934c3d895af5520cfea041f1),
[Gui::PropertyEditor::PropertyPathItem::value()](../../de/d04/classGui_1_1PropertyEditor_1_1PropertyPathItem.html#a78946d13ccf37898411e45d4d9730537),
[Gui::PropertyEditor::PropertyTransientFileItem::value()](../../de/d80/classGui_1_1PropertyEditor_1_1PropertyTransientFileItem.html#a7ec4af498f59a81de2414fdaced5669f),
[SketcherGui::PropertyConstraintListItem::value()](../../dd/d04/classSketcherGui_1_1PropertyConstraintListItem.html#afbd28ea5bf2d11eedc5c916575b9a5a1),
and
[MeshPartGui::CurveOnMeshHandler::Private::vertexCallback()](../../d2/d9f/classCurveOnMeshHandler_1_1Private.html#a373137b450a6003db4057cc546930264).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) Base::Type::operator!=  | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |  const  
---|---|---|---|---|---  
  
References
[getKey()](../../dc/dee/classBase_1_1Type.html#a9b9623ec1a23a7ac7002ce6c6138ed71).

## ◆ operator<()

[bool](../../d9/db9/classbool.html) Base::Type::operator< | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |  const  
---|---|---|---|---|---  
  
References
[getKey()](../../dc/dee/classBase_1_1Type.html#a9b9623ec1a23a7ac7002ce6c6138ed71).

## ◆ operator<=()

[bool](../../d9/db9/classbool.html) Base::Type::operator<=  | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |  const  
---|---|---|---|---|---  
  
References
[getKey()](../../dc/dee/classBase_1_1Type.html#a9b9623ec1a23a7ac7002ce6c6138ed71).

## ◆ operator=()

void Base::Type::operator=  | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |   
---|---|---|---|---|---  
  
## ◆ operator==()

[bool](../../d9/db9/classbool.html) Base::Type::operator==  | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |  const  
---|---|---|---|---|---  
  
References
[getKey()](../../dc/dee/classBase_1_1Type.html#a9b9623ec1a23a7ac7002ce6c6138ed71).

## ◆ operator>()

[bool](../../d9/db9/classbool.html) Base::Type::operator> | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |  const  
---|---|---|---|---|---  
  
References
[getKey()](../../dc/dee/classBase_1_1Type.html#a9b9623ec1a23a7ac7002ce6c6138ed71).

## ◆ operator>=()

[bool](../../d9/db9/classbool.html) Base::Type::operator>=  | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |  const  
---|---|---|---|---|---  
  
References
[getKey()](../../dc/dee/classBase_1_1Type.html#a9b9623ec1a23a7ac7002ce6c6138ed71).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Type.h
  * FreeCAD/src/Base/Type.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

