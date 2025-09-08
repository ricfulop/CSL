---
url: https://freecad.github.io/SourceDoc/d7/d3f/classApp_1_1FeatureCustomT.html
scraped_at: 2025-09-08T14:54:43.522028
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)

[List of all members](../../de/df9/classApp_1_1FeatureCustomT-members.html) | Public Member Functions

App::FeatureCustomT< FeatureT > Class Template Reference

[FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html "FeatureCustomT
is a template class to be used with DocumentObject or any of its subclasses as
templat...") is a template class to be used with
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") or any of its subclasses as template
parameter. [More...](../../d7/d3f/classApp_1_1FeatureCustomT.html#details)

`#include <FeatureCustom.h>`

##  Public Member Functions  
  
---  
|
[FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html#a615165ba0fb0f30153f749024c5e6e2a)
()  
virtual | [~FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html#a09d30e2d47d21ebdddd083e9ea2ebc3d) ()  
  
## methods override DocumentObject  
  
---  
short | [mustExecute](../../d7/d3f/classApp_1_1FeatureCustomT.html#acb1eb43ed23431506a2dffabab26fa49) () const  
virtual [DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [execute](../../d7/d3f/classApp_1_1FeatureCustomT.html#a85b3c27fb1653e62def96afd83130001) (void)  
| recalculate the Feature
[More...](../../d7/d3f/classApp_1_1FeatureCustomT.html#a85b3c27fb1653e62def96afd83130001)  
  
virtual const char * | [getViewProviderName](../../d7/d3f/classApp_1_1FeatureCustomT.html#a995179e00b8498c1b23aa577dc779f46) (void) const  
| returns the type name of the ViewProvider
[More...](../../d7/d3f/classApp_1_1FeatureCustomT.html#a995179e00b8498c1b23aa577dc779f46)  
  
[PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d7/d3f/classApp_1_1FeatureCustomT.html#a3d7833553035937c3bad8e510178fea2) (void)  
void | [setPyObject](../../d7/d3f/classApp_1_1FeatureCustomT.html#a4f9341a2ab09bf9ef59f227418511afc) ([PyObject](../../df/d1b/classPyObject.html) *obj)  
virtual void | [onBeforeChange](../../d7/d3f/classApp_1_1FeatureCustomT.html#a95a71ecd0244748d2887585b95a2b7d3) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
virtual void | [onChanged](../../d7/d3f/classApp_1_1FeatureCustomT.html#a1dd739f646e30108053da973728b4545) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
virtual void | [onDocumentRestored](../../d7/d3f/classApp_1_1FeatureCustomT.html#af1c7e5d79a16e42cab25b46123cd7bb6) ()  
virtual void | [onSettingDocument](../../d7/d3f/classApp_1_1FeatureCustomT.html#a665be2ad60e1794e79070e3ded1d6754) ()  
|
[FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html#a08b4d43ce2f14f646434842bbcbd956a)
(const [FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)
&)=delete  
|
[FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html#aaa9f84bde6144ce1f4714eaf8857acd2)
([FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html) &&)=delete  
[FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html) & | [operator=](../../d7/d3f/classApp_1_1FeatureCustomT.html#a1157b0e144ecdfbda2a85b98bff133a5) (const [FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html) &)=delete  
[FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html) & | [operator=](../../d7/d3f/classApp_1_1FeatureCustomT.html#aa3763e64787ea5fcaea51bfeb55f6212) ([FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html) &&)=delete  
  
## Detailed Description

template<class [FeatureT](../../d3/d12/classFeatureT.html)>  
class App::FeatureCustomT< FeatureT >

[FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html "FeatureCustomT
is a template class to be used with DocumentObject or any of its subclasses as
templat...") is a template class to be used with
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") or any of its subclasses as template
parameter.

[FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html "FeatureCustomT
is a template class to be used with DocumentObject or any of its subclasses as
templat...") offers a way to add or remove a property at runtime. This class
is similar to [FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)
with the difference that it has no support for in Python written feature
classes.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ FeatureCustomT() [1/3]

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

[App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::FeatureCustomT  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~FeatureCustomT()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::~[FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html) | ( | | ) |   
---|---|---|---|---  
virtual  
  
## ◆ FeatureCustomT() [2/3]

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::FeatureCustomT  | ( | const [FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) > & | | ) |   
---|---|---|---|---|---  
protecteddelete  
  
## ◆ FeatureCustomT() [3/3]

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::FeatureCustomT  | ( | [FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) > && | | ) |   
---|---|---|---|---|---  
protecteddelete  
  
## Member Function Documentation

## ◆ execute()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::execute  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
recalculate the Feature

Referenced by
[draftobjects.facebinder.Facebinder::addSubobjects()](../../d9/d57/classdraftobjects_1_1facebinder_1_1Facebinder.html#a50c77c202a034ce7109bb93322ff6e4e),
[PathScripts.PathDressupDogbone.ObjectDressup::boneStateList()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#af7788dd97e3ca711047ebc4472cf9f21),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[PathScripts.PathDressupHoldingTags.ObjectTagDressup::generateTags()](../../de/dd2/classPathScripts_1_1PathDressupHoldingTags_1_1ObjectTagDressup.html#a0937c170df6457d4d7aa799c876584ae),
[ArchPanel.PanelCut::getWires()](../../d6/dbd/classArchPanel_1_1PanelCut.html#a61534af5c2a0125dde05e08a22025195),
[ArchSchedule.CommandArchSchedule::IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[Mod.PartDesign.Scripts.DistanceBolt.DistanceBolt::onChanged()](../../d8/d9d/classMod_1_1PartDesign_1_1Scripts_1_1DistanceBolt_1_1DistanceBolt.html#a5899c4fe94fa654ae168588d09ec3674),
[Mod.PartDesign.Scripts.Epitrochoid.Epitrochoid::onChanged()](../../da/d92/classMod_1_1PartDesign_1_1Scripts_1_1Epitrochoid_1_1Epitrochoid.html#a666d03d55a3758fd5b580ecdf83ff046),
[Mod.PartDesign.Scripts.Parallelepiped.Parallelepiped::onChanged()](../../da/db1/classMod_1_1PartDesign_1_1Scripts_1_1Parallelepiped_1_1Parallelepiped.html#a7d58a665dbdb613ccf9830254b6b3a28),
[Mod.PartDesign.Scripts.Parallelepiped.BoxCylinder::onChanged()](../../dc/dc9/classMod_1_1PartDesign_1_1Scripts_1_1Parallelepiped_1_1BoxCylinder.html#a32f2314f8a81f2034ba5fb8902079e75),
[Mod.PartDesign.Scripts.Spring.MySpring::onChanged()](../../d3/d4c/classMod_1_1PartDesign_1_1Scripts_1_1Spring_1_1MySpring.html#a45b49877108608c2473da154cbf7980d),
[FeaturePython.DistanceBolt::onChanged()](../../d9/d7d/classFeaturePython_1_1DistanceBolt.html#a644c14797e2ed9043537de3c86f7fdf1),
[PathScripts.PathStock.StockFromBase::onChanged()](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#a2c3dfa73d2881d73e95ac79cb572e9b9),
[PathScripts.PathStock.StockCreateBox::onChanged()](../../d9/dd6/classPathScripts_1_1PathStock_1_1StockCreateBox.html#ae190342a16a7a1c726c7748b85bc36d7),
[PathScripts.PathStock.StockCreateCylinder::onChanged()](../../da/de2/classPathScripts_1_1PathStock_1_1StockCreateCylinder.html#aaee43a8f62bd342d2b16ff4268dd33c9),
[draftobjects.draftlink.DraftLink::onDocumentRestored()](../../d6/d1d/classdraftobjects_1_1draftlink_1_1DraftLink.html#ac93069a613e26475296ba7eba274a783),
[draftobjects.patharray.PathArray::onDocumentRestored()](../../de/dbe/classdraftobjects_1_1patharray_1_1PathArray.html#a6a3f3b5a3444a8e2bc12d61152100fd5),
and
[draftobjects.pathtwistedarray.PathTwistedArray::onDocumentRestored()](../../da/d1a/classdraftobjects_1_1pathtwistedarray_1_1PathTwistedArray.html#a780c1e365112f239b177875caa78103b).

## ◆ getPyObject()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

[PyObject](../../df/d1b/classPyObject.html) * [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
  
## ◆ getViewProviderName()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual const char * [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::getViewProviderName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
returns the type name of the ViewProvider

## ◆ mustExecute()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

short [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::mustExecute  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
## ◆ onBeforeChange()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual void [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::onBeforeChange  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
protectedvirtual  
  
Referenced by
[PathScripts.PathGui.QuantitySpinBox::updateProperty()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a8b9b202d7b495b666cb1f6b41ab2beb4).

## ◆ onChanged()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual void [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::onChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
protectedvirtual  
  
Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft::attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire::execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[ArchBuildingPart.ViewProviderBuildingPart::updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut::updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet::updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel::updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer::updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy::updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ onDocumentRestored()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual void [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::onDocumentRestored  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
## ◆ onSettingDocument()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual void [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::onSettingDocument  | ( | void  | | ) |   
---|---|---|---|---|---  
protectedvirtual  
  
## ◆ operator=() [1/2]

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| [FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html) & [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::operator=  | ( | const [FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) > & | | ) |   
---|---|---|---|---|---  
protecteddelete  
  
## ◆ operator=() [2/2]

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| [FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html) & [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::operator=  | ( | [FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) > && | | ) |   
---|---|---|---|---|---  
protecteddelete  
  
## ◆ setPyObject()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

void [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/FeatureCustom.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

