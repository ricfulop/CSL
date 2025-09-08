---
url: https://freecad.github.io/SourceDoc/d2/d2f/classApp_1_1FeaturePythonT.html
scraped_at: 2025-09-08T14:54:46.528705
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)

[List of all members](../../db/d69/classApp_1_1FeaturePythonT-members.html) | Public Member Functions

App::FeaturePythonT< FeatureT > Class Template Reference

Generic Python feature class which allows to behave every
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") derived class as Python feature –
simply by subclassing.
[More...](../../d2/d2f/classApp_1_1FeaturePythonT.html#details)

`#include <FeaturePython.h>`

##  Public Member Functions  
  
---  
|
[FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html#a629e64fb42173efd9fac20abce1b659c)
()  
virtual | [~FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html#a60a6b32b27f3534c710c1862f6773185) ()  
  
## methods override DocumentObject  
  
---  
short | [mustExecute](../../d2/d2f/classApp_1_1FeaturePythonT.html#a628caf1f6979184cd03e24423272c87e) () const override  
virtual [DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [execute](../../d2/d2f/classApp_1_1FeaturePythonT.html#aff89f1dafffac9466b7f498c2fc00e4f) (void) override  
| recalculate the Feature
[More...](../../d2/d2f/classApp_1_1FeaturePythonT.html#aff89f1dafffac9466b7f498c2fc00e4f)  
  
virtual const char * | [getViewProviderNameOverride](../../d2/d2f/classApp_1_1FeaturePythonT.html#afc869a51e2c9d5a6ba64dd5cbeca1626) (void) const override  
virtual const char * | [getViewProviderName](../../d2/d2f/classApp_1_1FeaturePythonT.html#a0b418f04a0af74c33b63b91eb70f2ee8) (void) const override  
| returns the type name of the ViewProvider
[More...](../../d2/d2f/classApp_1_1FeaturePythonT.html#a0b418f04a0af74c33b63b91eb70f2ee8)  
  
virtual [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getSubObject](../../d2/d2f/classApp_1_1FeaturePythonT.html#ad6348fc3b6c457be2a119f27f8569b9c) (const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const override  
virtual std::vector< std::string > | [getSubObjects](../../d2/d2f/classApp_1_1FeaturePythonT.html#ac30b8195c30df404205ea2d408d35e93) ([int](../../d1/da0/classint.html) reason=0) const override  
virtual [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getLinkedObject](../../d2/d2f/classApp_1_1FeaturePythonT.html#ad86b5c211527f9522f1f2c49862b7d53) ([bool](../../d9/db9/classbool.html) recurse, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const override  
virtual [bool](../../d9/db9/classbool.html) | [hasChildElement](../../d2/d2f/classApp_1_1FeaturePythonT.html#aeea601faec7150c1f670fe6af9e5cff4) () const override  
| return true to activate tree view group object handling
[More...](../../d2/d2f/classApp_1_1FeaturePythonT.html#aeea601faec7150c1f670fe6af9e5cff4)  
  
virtual [int](../../d1/da0/classint.html) | [isElementVisible](../../d2/d2f/classApp_1_1FeaturePythonT.html#a9d85e138815855c3a2ca59e1a5200ade) (const char *element) const override  
| Get sub-element visibility.
[More...](../../d2/d2f/classApp_1_1FeaturePythonT.html#a9d85e138815855c3a2ca59e1a5200ade)  
  
virtual [int](../../d1/da0/classint.html) | [setElementVisible](../../d2/d2f/classApp_1_1FeaturePythonT.html#a40faf0c5d9ea646f5fbbb77eed1785f1) (const char *element, [bool](../../d9/db9/classbool.html) visible) override  
| Set sub-element visibility.
[More...](../../d2/d2f/classApp_1_1FeaturePythonT.html#a40faf0c5d9ea646f5fbbb77eed1785f1)  
  
virtual [bool](../../d9/db9/classbool.html) | [canLinkProperties](../../d2/d2f/classApp_1_1FeaturePythonT.html#aa6eed1ed82f93836b53def008f8efa47) () const override  
virtual [bool](../../d9/db9/classbool.html) | [allowDuplicateLabel](../../d2/d2f/classApp_1_1FeaturePythonT.html#acfa7ff0dabb096c033fdd64b3f977211) () const override  
virtual [bool](../../d9/db9/classbool.html) | [redirectSubName](../../d2/d2f/classApp_1_1FeaturePythonT.html#ad0b427a0b27f479faea6770d9fdd49a7) (std::ostringstream &ss, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *topParent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *child) const override  
virtual [int](../../d1/da0/classint.html) | [canLoadPartial](../../d2/d2f/classApp_1_1FeaturePythonT.html#a99ca8e0b5d3c159f43fcd9c69801bfdf) () const override  
virtual void | [editProperty](../../d2/d2f/classApp_1_1FeaturePythonT.html#a8a5cd6480fbd3d0ac3fab0031b84e68e) (const char *propName) override  
[PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d2/d2f/classApp_1_1FeaturePythonT.html#a1fbe74b16782db87a7c6e86307ee0c9d) (void) override  
void | [setPyObject](../../d2/d2f/classApp_1_1FeaturePythonT.html#a83b0916baccf11124c147ceba23acb07) ([PyObject](../../df/d1b/classPyObject.html) *obj) override  
|
[FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html#aa1720485499d2bc5ae8a12fbd75842f1)
(const [FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)
&)=delete  
|
[FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html#adb9a8d9256dc9478dbe0eeb14adc6bbe)
([FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html) &&)=delete  
[FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html) & | [operator=](../../d2/d2f/classApp_1_1FeaturePythonT.html#aad490afde2d6a597916e133f86df9421) (const [FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html) &)=delete  
[FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html) & | [operator=](../../d2/d2f/classApp_1_1FeaturePythonT.html#a3551d27407c3424f1996bde6a5b82cf2) ([FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html) &&)=delete  
virtual void | [onBeforeChange](../../d2/d2f/classApp_1_1FeaturePythonT.html#ada52b433943e87c0e8fcfc300d966c27) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) override  
virtual void | [onBeforeChangeLabel](../../d2/d2f/classApp_1_1FeaturePythonT.html#aa81525a29caefd4b2ba4b27113e673a4) (std::string &newLabel) override  
virtual void | [onChanged](../../d2/d2f/classApp_1_1FeaturePythonT.html#aefbf8694218d25f4b90d8ffe7fe796ee) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) override  
virtual void | [onDocumentRestored](../../d2/d2f/classApp_1_1FeaturePythonT.html#a2943a9b8ea93ef154174081e41f6421a) () override  
  
## Detailed Description

template<class [FeatureT](../../d3/d12/classFeatureT.html)>  
class App::FeaturePythonT< FeatureT >

Generic Python feature class which allows to behave every
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") derived class as Python feature –
simply by subclassing.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ FeaturePythonT() [1/3]

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

[App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::FeaturePythonT  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~FeaturePythonT()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::~[FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html) | ( | | ) |   
---|---|---|---|---  
virtual  
  
## ◆ FeaturePythonT() [2/3]

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::FeaturePythonT  | ( | const [FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) > & | | ) |   
---|---|---|---|---|---  
delete  
  
## ◆ FeaturePythonT() [3/3]

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::FeaturePythonT  | ( | [FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) > && | | ) |   
---|---|---|---|---|---  
delete  
  
## Member Function Documentation

## ◆ allowDuplicateLabel()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [bool](../../d9/db9/classbool.html) [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::allowDuplicateLabel  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
References
[App::FeaturePythonImp::Accepted](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ae0caca590bddcc9b2789db6f8bc24eab),
[App::FeaturePythonImp::allowDuplicateLabel()](../../de/d49/classApp_1_1FeaturePythonImp.html#a43829c54fcc922a6b758f2378550ea5a),
and
[App::FeaturePythonImp::Rejected](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04a81c1f4b1ff226929d10c34fa0622986d).

## ◆ canLinkProperties()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [bool](../../d9/db9/classbool.html) [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::canLinkProperties  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
References
[App::FeaturePythonImp::Accepted](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ae0caca590bddcc9b2789db6f8bc24eab),
[App::FeaturePythonImp::canLinkProperties()](../../de/d49/classApp_1_1FeaturePythonImp.html#af7f05cebcab3e184f1004f5fedb3081e),
and
[App::FeaturePythonImp::Rejected](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04a81c1f4b1ff226929d10c34fa0622986d).

## ◆ canLoadPartial()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [int](../../d1/da0/classint.html) [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::canLoadPartial  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
References
[App::FeaturePythonImp::canLoadPartial()](../../de/d49/classApp_1_1FeaturePythonImp.html#a88e2035789dd79a4aad1031fefe2a5e4).

## ◆ editProperty()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual void [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::editProperty  | ( | const char *  | _propName_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
References
[App::FeaturePythonImp::editProperty()](../../de/d49/classApp_1_1FeaturePythonImp.html#a9e60644e5d2e9d289ef89da5d120138b).

## ◆ execute()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::execute  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
recalculate the Feature

References
[App::FeaturePythonImp::execute()](../../de/d49/classApp_1_1FeaturePythonImp.html#ac1d17c03bc1f7d0fc643444b0a2fd069),
and
[App::DocumentObject::StdReturn](../../d2/de4/classApp_1_1DocumentObject.html#af53a1c6a086c5dfe228aaefeeb7316d2).

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

## ◆ getLinkedObject()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::getLinkedObject  | ( | [bool](../../d9/db9/classbool.html) | _recurse_ ,   
---|---|---|---  
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ ,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ ,   
|  | [int](../../d1/da0/classint.html) | _depth_  
| ) | |  const  
overridevirtual  
  
References
[App::FeaturePythonImp::getLinkedObject()](../../de/d49/classApp_1_1FeaturePythonImp.html#a1c801863ae32581043ec7077fd800407).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * App::FeaturePython::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
override  
  
References
[App::FeaturePythonImp::getPyObject()](../../de/d49/classApp_1_1FeaturePythonImp.html#af877b3f03df018c75e235106966f3d1b).

## ◆ getSubObject()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::getSubObject  | ( | const char *  | _subname_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) **  | _pyObj_ ,   
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ ,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ ,   
|  | [int](../../d1/da0/classint.html) | _depth_  
| ) | |  const  
overridevirtual  
  
References
[App::FeaturePythonImp::getSubObject()](../../de/d49/classApp_1_1FeaturePythonImp.html#ac3df43ec698cb0686ea045b6932b0354).

## ◆ getSubObjects()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual std::vector< std::string > [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::getSubObjects  | ( | [int](../../d1/da0/classint.html) | _reason_ = `0`| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
References
[App::FeaturePythonImp::getSubObjects()](../../de/d49/classApp_1_1FeaturePythonImp.html#a0cf78f9d418836d904886eb38fdb5233).

## ◆ getViewProviderName()

| const char * App::PlacementPython::getViewProviderName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
returns the type name of the ViewProvider

## ◆ getViewProviderNameOverride()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual const char * [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::getViewProviderNameOverride  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
References
[App::FeaturePythonImp::getViewProviderName()](../../de/d49/classApp_1_1FeaturePythonImp.html#a5b00ab85c59b31c9e0f8319cf1900984).

## ◆ hasChildElement()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [bool](../../d9/db9/classbool.html) [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::hasChildElement  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
return true to activate tree view group object handling

References
[App::FeaturePythonImp::Accepted](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ae0caca590bddcc9b2789db6f8bc24eab),
[App::FeaturePythonImp::hasChildElement()](../../de/d49/classApp_1_1FeaturePythonImp.html#a39a7fcd6bd878af2928f645a6c344d75),
and
[App::FeaturePythonImp::Rejected](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04a81c1f4b1ff226929d10c34fa0622986d).

## ◆ isElementVisible()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [int](../../d1/da0/classint.html) [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::isElementVisible  | ( | const char *  | _element_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Get sub-element visibility.

References
[App::FeaturePythonImp::isElementVisible()](../../de/d49/classApp_1_1FeaturePythonImp.html#a7118f8fde3ec8ad7ce5cb15f02e7f9c2).

## ◆ mustExecute()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| short [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::mustExecute  | ( | void  | | ) |  const  
---|---|---|---|---|---  
override  
  
References
[App::FeaturePythonImp::mustExecute()](../../de/d49/classApp_1_1FeaturePythonImp.html#a2819dc998f51e0469fbd519387f7c7c2).

## ◆ onBeforeChange()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual void [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::onBeforeChange  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
References
[App::FeaturePythonImp::onBeforeChange()](../../de/d49/classApp_1_1FeaturePythonImp.html#a6954506f6c66d7ea68b8835851f3731a).

Referenced by
[PathScripts.PathGui.QuantitySpinBox::updateProperty()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a8b9b202d7b495b666cb1f6b41ab2beb4).

## ◆ onBeforeChangeLabel()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual void [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::onBeforeChangeLabel  | ( | std::string & | _newLabel_| ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
References
[App::FeaturePythonImp::onBeforeChangeLabel()](../../de/d49/classApp_1_1FeaturePythonImp.html#acfea0a8a6c744c2ec720a0609ee590b6).

## ◆ onChanged()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual void [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::onChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
References
[App::PropertyPythonObject::getValue()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a1884e8da237c298d82d78d1b80e320cf),
[App::FeaturePythonImp::init()](../../de/d49/classApp_1_1FeaturePythonImp.html#ad920e85b43e3f2baa3e1587990130764),
and
[App::FeaturePythonImp::onChanged()](../../de/d49/classApp_1_1FeaturePythonImp.html#a31e2aa2e633c8db8d05057f71dc42a17).

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

| virtual void [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::onDocumentRestored  | ( | | ) |   
---|---|---|---|---  
overrideprotectedvirtual  
  
References
[App::FeaturePythonImp::onDocumentRestored()](../../de/d49/classApp_1_1FeaturePythonImp.html#a9ca4d860d98f2a439d1be269b37fe84f).

## ◆ operator=() [1/2]

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| [FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html) & [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::operator=  | ( | const [FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) > & | | ) |   
---|---|---|---|---|---  
delete  
  
## ◆ operator=() [2/2]

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| [FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html) & [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::operator=  | ( | [FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) > && | | ) |   
---|---|---|---|---|---  
delete  
  
## ◆ redirectSubName()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [bool](../../d9/db9/classbool.html) [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::redirectSubName  | ( | std::ostringstream & | _ss_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _topParent_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _child_  
| ) | |  const  
overridevirtual  
  
References
[App::FeaturePythonImp::Accepted](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ae0caca590bddcc9b2789db6f8bc24eab),
[App::FeaturePythonImp::redirectSubName()](../../de/d49/classApp_1_1FeaturePythonImp.html#aab242ba739e239fe38f7e42e1e9084c4),
and
[App::FeaturePythonImp::Rejected](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04a81c1f4b1ff226929d10c34fa0622986d).

## ◆ setElementVisible()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| virtual [int](../../d1/da0/classint.html) [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::setElementVisible  | ( | const char *  | _element_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _visible_  
| ) | |   
overridevirtual  
  
Set sub-element visibility.

References
[App::FeaturePythonImp::setElementVisible()](../../de/d49/classApp_1_1FeaturePythonImp.html#a80870ebddcc83803c66aa86179589095).

## ◆ setPyObject()

template<class [FeatureT](../../d3/d12/classFeatureT.html) >

| void [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [FeatureT](../../d3/d12/classFeatureT.html) >::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
override  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/FeaturePython.h
  * FreeCAD/src/App/FeaturePython.cpp
  * FreeCAD/src/App/Link.cpp
  * FreeCAD/src/App/Placement.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

