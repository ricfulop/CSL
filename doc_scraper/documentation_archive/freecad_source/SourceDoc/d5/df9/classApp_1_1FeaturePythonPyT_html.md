---
url: https://freecad.github.io/SourceDoc/d5/df9/classApp_1_1FeaturePythonPyT.html
scraped_at: 2025-09-08T14:54:45.481481
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [FeaturePythonPyT](../../d5/df9/classApp_1_1FeaturePythonPyT.html)

[List of all members](../../da/d6e/classApp_1_1FeaturePythonPyT-members.html) | Public Member Functions | Static Public Attributes

App::FeaturePythonPyT< FeaturePyT > Class Template Reference

`#include <FeaturePythonPyImp.h>`

##  Public Member Functions  
  
---  
|
[FeaturePythonPyT](../../d5/df9/classApp_1_1FeaturePythonPyT.html#a50f6604611a89046c7772340ee9415ba)
([Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html) *pcObject,
PyTypeObject
*T=&[Type](../../d5/df9/classApp_1_1FeaturePythonPyT.html#a30564b7cd97268ab1c5ec82087341bb3))  
virtual | [~FeaturePythonPyT](../../d5/df9/classApp_1_1FeaturePythonPyT.html#af1295b8e7219f8a960f1252b93923532) ()  
  
##  Static Public Attributes  
  
---  
static PyTypeObject | [Type](../../d5/df9/classApp_1_1FeaturePythonPyT.html#a30564b7cd97268ab1c5ec82087341bb3)  
| Type structure of
[FeaturePythonPyT](../../d5/df9/classApp_1_1FeaturePythonPyT.html).
[More...](../../d5/df9/classApp_1_1FeaturePythonPyT.html#a30564b7cd97268ab1c5ec82087341bb3)  
  
  
##  Protected Attributes  
  
---  
callbacks and implementers for the python object methods  
[PyObject](../../df/d1b/classPyObject.html) * | [dict_methods](../../d5/df9/classApp_1_1FeaturePythonPyT.html#a458e273745eeadb61915522519f104e3)  
  
## Detailed Description

template<class [FeaturePyT](../../d1/d78/classFeaturePyT.html)>  
class App::FeaturePythonPyT< FeaturePyT >

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ FeaturePythonPyT()

template<class [FeaturePyT](../../d1/d78/classFeaturePyT.html) >

[App::FeaturePythonPyT](../../d5/df9/classApp_1_1FeaturePythonPyT.html)< [FeaturePyT](../../d1/d78/classFeaturePyT.html) >::FeaturePythonPyT  | ( | [Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html) *  | _pcObject_ ,   
---|---|---|---  
|  | PyTypeObject *  | _T_ = `&[Type](../../d5/df9/classApp_1_1FeaturePythonPyT.html#a30564b7cd97268ab1c5ec82087341bb3)`  
| ) | |   
  
References [App::FeaturePythonPyT< FeaturePyT
>::dict_methods](../../d5/df9/classApp_1_1FeaturePythonPyT.html#a458e273745eeadb61915522519f104e3).

## ◆ ~FeaturePythonPyT()

template<class [FeaturePyT](../../d1/d78/classFeaturePyT.html) >

| [App::FeaturePythonPyT](../../d5/df9/classApp_1_1FeaturePythonPyT.html)<
[FeaturePyT](../../d1/d78/classFeaturePyT.html)
>::~[FeaturePythonPyT](../../d5/df9/classApp_1_1FeaturePythonPyT.html)  
---  
virtual  
  
## Member Data Documentation

## ◆ dict_methods

template<class [FeaturePyT](../../d1/d78/classFeaturePyT.html) >

| [PyObject](../../df/d1b/classPyObject.html)*
[App::FeaturePythonPyT](../../d5/df9/classApp_1_1FeaturePythonPyT.html)<
[FeaturePyT](../../d1/d78/classFeaturePyT.html) >::dict_methods  
---  
protected  
  
Referenced by [App::FeaturePythonPyT< FeaturePyT
>::FeaturePythonPyT()](../../d5/df9/classApp_1_1FeaturePythonPyT.html#a50f6604611a89046c7772340ee9415ba).

## ◆ Type

template<class [FeaturePyT](../../d1/d78/classFeaturePyT.html) >

| PyTypeObject
[App::FeaturePythonPyT](../../d5/df9/classApp_1_1FeaturePythonPyT.html)<
[FeaturePyT](../../d1/d78/classFeaturePyT.html) >::Type  
---  
static  
  
Type structure of
[FeaturePythonPyT](../../d5/df9/classApp_1_1FeaturePythonPyT.html).

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

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/FeaturePythonPyImp.h
  * FreeCAD/src/App/FeaturePythonPyImp.inl

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

