---
url: https://freecad.github.io/SourceDoc/da/d47/classApp_1_1Material.html
scraped_at: 2025-09-08T14:55:03.593623
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Material](../../da/d47/classApp_1_1Material.html)

[List of all members](../../d5/dec/classApp_1_1Material-members.html) | Public Types

App::Material Class Reference

[Material](../../da/d47/classApp_1_1Material.html "Material class.") class.
[More...](../../da/d47/classApp_1_1Material.html#details)

`#include <Material.h>`

##  Public Types  
  
---  
enum | [MaterialType](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241) {   
[BRASS](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a2c357c15b6c9017439c9fef54b9db5ed)
,
[BRONZE](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a50946cc5da9fe6b0e3144fdb3bc071b7)
,
[COPPER](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241ad4374c4cc638136b7a0505e1d0137f6a)
,
[GOLD](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a9afa4a525de2e7a47192e7d2814baa1f)
,  
[PEWTER](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a1e92076c6e7405ebe2741718323c4159)
,
[PLASTER](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a7c3016b3ea00b3045c629b54f2f9a942)
,
[PLASTIC](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241af74735722c174afeedd12c3c0ce91193)
,
[SILVER](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a93032e7f81750f861c91aa2c8ed22a3d)
,  
[STEEL](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a82c5744dadd01d18e391f68ea1ddcade)
,
[STONE](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241ae9dac3ba1cb868fc07721a2930fc6ef3)
,
[SHINY_PLASTIC](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241afd0e451e47bf6d64c28936f3e145cd4a)
,
[SATIN](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a9477b3997a7aea0ef5ba71dc6f428bc9)
,  
[METALIZED](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241ae993b11ae1dfa7340a1af091fceb9e37)
,
[NEON_GNC](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241abc8192b0711a53b6cc330c40e5385d4c)
,
[CHROME](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241aced535cbf70a5107dd5770a83145f89b)
,
[ALUMINIUM](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241ada8daaa569af36631f6c721e3e8bb0d9)
,  
[OBSIDIAN](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241afdaec3965f270b94fe3c52707cb74e53)
,
[NEON_PHC](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a419fb3dbea5daa68ad348b446b3fc20e)
,
[JADE](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a5ffd4cab54869c54eb03470fb128b432)
,
[RUBY](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a835273d11c5e23aa84521a7e880c4c7a)
,  
[EMERALD](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241a07b0d3e6ec8a9d4510b7e589d47cd911)
,
[DEFAULT](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241ab3a48940792adfe33ae24754e605955b)
,
[USER_DEFINED](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241ad0877fb43ad20e8f30b897f33fe863d6)  
}  
  
##  Public Member Functions  
  
---  
Constructors  
|
[Material](../../da/d47/classApp_1_1Material.html#ae6b828e32a19f05a2e3950a3e0ef49dd)
()  
| Sets the USER_DEFINED material type.
[More...](../../da/d47/classApp_1_1Material.html#ae6b828e32a19f05a2e3950a3e0ef49dd)  
  
|
[Material](../../da/d47/classApp_1_1Material.html#a293a54030eca57b89d3c70ea71a698d4)
(const char *MatName)  
| Defines the colors and shininess for the material _MatName_.
[More...](../../da/d47/classApp_1_1Material.html#a293a54030eca57b89d3c70ea71a698d4)  
  
|
[Material](../../da/d47/classApp_1_1Material.html#a5f67c47559f4695ca951a86b47f347d8)
(const
[MaterialType](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241)
MatType)  
| Does basically the same as the constructor above unless that it accepts a
MaterialType as argument.
[More...](../../da/d47/classApp_1_1Material.html#a5f67c47559f4695ca951a86b47f347d8)  
  
|
[~Material](../../da/d47/classApp_1_1Material.html#a2008d99959bf8d347de27303ff9dd131)
()  
void | [set](../../da/d47/classApp_1_1Material.html#a4913b1e76d8a1b5ae84d80f82acbbb7d) (const char *MatName)  
| Set a material by name There are some standard materials defined which are:
[More...](../../da/d47/classApp_1_1Material.html#a4913b1e76d8a1b5ae84d80f82acbbb7d)  
  
void | [setType](../../da/d47/classApp_1_1Material.html#a143ff71f3577aecbd550f386ecbf4fd3) (const [MaterialType](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241) MatType)  
| This method is provided for convenience which does basically the same as the
method above unless that it accepts a MaterialType as argument.
[More...](../../da/d47/classApp_1_1Material.html#a143ff71f3577aecbd550f386ecbf4fd3)  
  
[MaterialType](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241) | [getType](../../da/d47/classApp_1_1Material.html#a74e39645f5caaedae0c84599fc784b6b) () const  
| Returns the currently set material type.
[More...](../../da/d47/classApp_1_1Material.html#a74e39645f5caaedae0c84599fc784b6b)  
  
  
## Properties  
  
---  
[Color](../../d3/d3a/classApp_1_1Color.html) | [ambientColor](../../da/d47/classApp_1_1Material.html#a3ff32aed1e85b102a9495e7dd5b65e95)  
| Defines the ambient color.
[More...](../../da/d47/classApp_1_1Material.html#a3ff32aed1e85b102a9495e7dd5b65e95)  
  
[Color](../../d3/d3a/classApp_1_1Color.html) | [diffuseColor](../../da/d47/classApp_1_1Material.html#a78a980def4511812a3759e21735865d9)  
| Defines the diffuse color.
[More...](../../da/d47/classApp_1_1Material.html#a78a980def4511812a3759e21735865d9)  
  
[Color](../../d3/d3a/classApp_1_1Color.html) | [specularColor](../../da/d47/classApp_1_1Material.html#a9d66afde7cfdb49496fbf8e18541bb44)  
| Defines the specular color.
[More...](../../da/d47/classApp_1_1Material.html#a9d66afde7cfdb49496fbf8e18541bb44)  
  
[Color](../../d3/d3a/classApp_1_1Color.html) | [emissiveColor](../../da/d47/classApp_1_1Material.html#a138e48aa0876626c9836d51937b288c7)  
| Defines the emissive color.
[More...](../../da/d47/classApp_1_1Material.html#a138e48aa0876626c9836d51937b288c7)  
  
float | [shininess](../../da/d47/classApp_1_1Material.html#ae7d9bdcbf5dee7b523505f29c604ba03)  
float | [transparency](../../da/d47/classApp_1_1Material.html#a3941dcb7c9f802454faf285375fdfd02)  
[bool](../../d9/db9/classbool.html) | [operator==](../../da/d47/classApp_1_1Material.html#a365898efac819243a5d49162cb39052a) (const [Material](../../da/d47/classApp_1_1Material.html) &m) const  
[bool](../../d9/db9/classbool.html) | [operator!=](../../da/d47/classApp_1_1Material.html#a788ac6f687e61b5fd95553e400345274) (const [Material](../../da/d47/classApp_1_1Material.html) &m) const  
  
## Detailed Description

[Material](../../da/d47/classApp_1_1Material.html "Material class.") class.

## Member Enumeration Documentation

## ◆ MaterialType

enum
[App::Material::MaterialType](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241)  
---  
  
Enumerator  
---  
BRASS |   
BRONZE |   
COPPER |   
GOLD |   
PEWTER |   
PLASTER |   
PLASTIC |   
SILVER |   
STEEL |   
STONE |   
SHINY_PLASTIC |   
SATIN |   
METALIZED |   
NEON_GNC |   
CHROME |   
ALUMINIUM |   
OBSIDIAN |   
NEON_PHC |   
JADE |   
RUBY |   
EMERALD |   
DEFAULT |   
USER_DEFINED |   
  
## Constructor & Destructor Documentation

## ◆ Material() [1/3]

App::Material::Material  | ( | | ) |   
---|---|---|---|---  
  
Sets the USER_DEFINED material type.

The user must set the colors afterwards.

## ◆ Material() [2/3]

App::Material::Material  | ( | const char *  | _MatName_| ) |   
---|---|---|---|---|---  
  
Defines the colors and shininess for the material _MatName_.

If _MatName_ isn't defined then USER_DEFINED is set and the user must define
the colors itself.

## ◆ Material() [3/3]

App::Material::Material  | ( | const [MaterialType](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241) | _MatType_| ) |   
---|---|---|---|---|---  
  
Does basically the same as the constructor above unless that it accepts a
MaterialType as argument.

## ◆ ~Material()

App::Material::~Material  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ getType()

[MaterialType](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241) App::Material::getType  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the currently set material type.

Referenced by
[PathScripts.PathToolEdit.ToolEditor::updateToolType()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a2ab9dc5c3f1a484ce30b642df4879fa3),
and
[PathScripts.PathToolEdit.ToolEditor::updateUI()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a901452eb82081a083d2b5d97ab8fe306).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) App::Material::operator!=  | ( | const [Material](../../da/d47/classApp_1_1Material.html) & | _m_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator==()

[bool](../../d9/db9/classbool.html) App::Material::operator==  | ( | const [Material](../../da/d47/classApp_1_1Material.html) & | _m_| ) |  const  
---|---|---|---|---|---  
  
## ◆ set()

void App::Material::set  | ( | const char *  | _MatName_| ) |   
---|---|---|---|---|---  
  
Set a material by name There are some standard materials defined which are:

  * Brass 
  * Bronze 
  * Copper 
  * Gold 
  * Pewter 
  * Plaster 
  * Plastic 
  * Silver 
  * Steel 
  * Stone 
  * Shiny plastic 
  * Satin 
  * Metalized 
  * Neon GNC 
  * Chrome 
  * Aluminium 
  * Obsidian 
  * Neon PHC 
  * Jade 
  * Ruby 
  * Emerald Furthermore there two additional modes _Default_ which defines a kind of grey metallic and user defined that does nothing. The [Color](../../d3/d3a/classApp_1_1Color.html "Color class.") and the other properties of the material are defined in the range [0-1]. If _MatName_ is an unknown material name then the type USER_DEFINED is set and the material doesn't get changed. 

Referenced by
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297).

## ◆ setType()

void App::Material::setType  | ( | const [MaterialType](../../da/d47/classApp_1_1Material.html#a33be553596ff2e5db8a5ffa31931c241) | _MatType_| ) |   
---|---|---|---|---|---  
  
This method is provided for convenience which does basically the same as the
method above unless that it accepts a MaterialType as argument.

## Member Data Documentation

## ◆ ambientColor

[Color](../../d3/d3a/classApp_1_1Color.html) App::Material::ambientColor  
---  
  
Defines the ambient color.

Referenced by
[Gui::Dialog::DlgMaterialPropertiesImp::on_ambientColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a49825eab8b369a08e23c6e14f3929301),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[MeshGui::ViewProviderMeshCurvature::onChanged()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643),
[MeshGui::ViewProviderMeshCurvature::ViewProviderMeshCurvature()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a7204bf34002b635b512efe925c011963),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
and
[PartGui::ViewProviderPartReference::ViewProviderPartReference()](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#af78fff593f8cef1f9cc78450928722cd).

## ◆ diffuseColor

[Color](../../d3/d3a/classApp_1_1Color.html) App::Material::diffuseColor  
---  
  
Defines the diffuse color.

Referenced by
[Gui::ViewProviderLink::getElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2b9c2eef2778031596f93f33b2980102),
[Gui::Dialog::DlgMaterialPropertiesImp::on_diffuseColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a9ccc20c9c5d253b5e9ed7fbe4d34f13e),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[MeshGui::ViewProviderMesh::onChanged()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae9ec71d871b59be4a532fb2be2cb8d52),
[MeshGui::ViewProviderMeshNode::onChanged()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a6f37857950fa14e1e1978c56706d0797),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[Gui::ViewProviderLink::setElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#af274c7d8619bfae997be5ea17b7c72b3),
[Gui::LinkView::setMaterial()](../../da/d11/classGui_1_1LinkView.html#a3881060944b7eec683ed8898dc53fce0),
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643),
[Gui::PropertyEditor::PropertyMaterialListItem::toolTip()](../../d9/d3e/classGui_1_1PropertyEditor_1_1PropertyMaterialListItem.html#a420082fd5b1643a150fb0650377990cc),
[Gui::ViewProviderLink::ViewProviderLink()](../../d6/d59/classGui_1_1ViewProviderLink.html#ac80b32ec9821edd74f1e39d58951773d),
[MeshGui::ViewProviderMeshCurvature::ViewProviderMeshCurvature()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a7204bf34002b635b512efe925c011963),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
and
[PartGui::ViewProviderPartReference::ViewProviderPartReference()](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#af78fff593f8cef1f9cc78450928722cd).

## ◆ emissiveColor

[Color](../../d3/d3a/classApp_1_1Color.html) App::Material::emissiveColor  
---  
  
Defines the emissive color.

Referenced by
[Gui::Dialog::DlgMaterialPropertiesImp::on_emissiveColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aa448adcda1877165e407fafcf0354cf3),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[MeshGui::ViewProviderMeshCurvature::onChanged()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643),
[MeshGui::ViewProviderMeshCurvature::ViewProviderMeshCurvature()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a7204bf34002b635b512efe925c011963),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
and
[PartGui::ViewProviderPartReference::ViewProviderPartReference()](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#af78fff593f8cef1f9cc78450928722cd).

## ◆ shininess

float App::Material::shininess  
---  
  
Referenced by
[Gui::Dialog::DlgMaterialPropertiesImp::on_shininess_valueChanged()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#af0d5014718205e140eb9e8799167d518),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[MeshGui::ViewProviderMeshCurvature::onChanged()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643),
[MeshGui::ViewProviderMeshCurvature::ViewProviderMeshCurvature()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a7204bf34002b635b512efe925c011963),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
and
[PartGui::ViewProviderPartReference::ViewProviderPartReference()](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#af78fff593f8cef1f9cc78450928722cd).

## ◆ specularColor

[Color](../../d3/d3a/classApp_1_1Color.html) App::Material::specularColor  
---  
  
Defines the specular color.

Referenced by
[Gui::Dialog::DlgMaterialPropertiesImp::on_specularColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a458ce64d9a0930c339444dff48ac809f),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[MeshGui::ViewProviderMeshCurvature::onChanged()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643),
[MeshGui::ViewProviderMeshCurvature::ViewProviderMeshCurvature()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a7204bf34002b635b512efe925c011963),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
and
[PartGui::ViewProviderPartReference::ViewProviderPartReference()](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#af78fff593f8cef1f9cc78450928722cd).

## ◆ transparency

float App::Material::transparency  
---  
  
Referenced by
[Gui::ViewProviderLink::getElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2b9c2eef2778031596f93f33b2980102),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[MeshGui::ViewProviderMeshCurvature::onChanged()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[Gui::LinkView::setMaterial()](../../da/d11/classGui_1_1LinkView.html#a3881060944b7eec683ed8898dc53fce0),
[MeshGui::ViewProviderMeshCurvature::ViewProviderMeshCurvature()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a7204bf34002b635b512efe925c011963),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
[PartGui::ViewProviderPartReference::ViewProviderPartReference()](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#af78fff593f8cef1f9cc78450928722cd),
and
[automotive_design.surface_style_transparent::wr1()](../../d7/da2/classautomotive__design_1_1surface__style__transparent.html#a9149a82927fe7c4af474acca6dc18fc7).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/Material.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

