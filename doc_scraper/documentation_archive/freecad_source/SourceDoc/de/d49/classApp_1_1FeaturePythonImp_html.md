---
url: https://freecad.github.io/SourceDoc/de/d49/classApp_1_1FeaturePythonImp.html
scraped_at: 2025-09-08T14:54:44.515078
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [FeaturePythonImp](../../de/d49/classApp_1_1FeaturePythonImp.html)

[List of all members](../../d4/d75/classApp_1_1FeaturePythonImp-members.html) | Public Types | Public Member Functions

App::FeaturePythonImp Class Reference

`#include <FeaturePython.h>`

##  Public Types  
  
---  
enum | [ValueT](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04) { [NotImplemented](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ac8f4291625102a15d99a85b736bad059) = 0 , [Accepted](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ae0caca590bddcc9b2789db6f8bc24eab) = 1 , [Rejected](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04a81c1f4b1ff226929d10c34fa0622986d) = 2 }  
  
##  Public Member Functions  
  
---  
[ValueT](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04) | [allowDuplicateLabel](../../de/d49/classApp_1_1FeaturePythonImp.html#a43829c54fcc922a6b758f2378550ea5a) () const  
[ValueT](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04) | [canLinkProperties](../../de/d49/classApp_1_1FeaturePythonImp.html#af7f05cebcab3e184f1004f5fedb3081e) () const  
[int](../../d1/da0/classint.html) | [canLoadPartial](../../de/d49/classApp_1_1FeaturePythonImp.html#a88e2035789dd79a4aad1031fefe2a5e4) () const  
[bool](../../d9/db9/classbool.html) | [editProperty](../../de/d49/classApp_1_1FeaturePythonImp.html#a9e60644e5d2e9d289ef89da5d120138b) (const char *propName)  
[bool](../../d9/db9/classbool.html) | [execute](../../de/d49/classApp_1_1FeaturePythonImp.html#ac1d17c03bc1f7d0fc643444b0a2fd069) ()  
|
[FeaturePythonImp](../../de/d49/classApp_1_1FeaturePythonImp.html#aa5b833ee96c622dc76b0dc91644f5cdb)
([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
[bool](../../d9/db9/classbool.html) | [getLinkedObject](../../de/d49/classApp_1_1FeaturePythonImp.html#a1c801863ae32581043ec7077fd800407) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, [bool](../../d9/db9/classbool.html) recurse, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const  
[PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../de/d49/classApp_1_1FeaturePythonImp.html#af877b3f03df018c75e235106966f3d1b) (void)  
[bool](../../d9/db9/classbool.html) | [getSubObject](../../de/d49/classApp_1_1FeaturePythonImp.html#ac3df43ec698cb0686ea045b6932b0354) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const  
[bool](../../d9/db9/classbool.html) | [getSubObjects](../../de/d49/classApp_1_1FeaturePythonImp.html#a0cf78f9d418836d904886eb38fdb5233) (std::vector< std::string > &ret, [int](../../d1/da0/classint.html) reason) const  
std::string | [getViewProviderName](../../de/d49/classApp_1_1FeaturePythonImp.html#a5b00ab85c59b31c9e0f8319cf1900984) ()  
[ValueT](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04) | [hasChildElement](../../de/d49/classApp_1_1FeaturePythonImp.html#a39a7fcd6bd878af2928f645a6c344d75) () const  
| return true to activate tree view group object handling
[More...](../../de/d49/classApp_1_1FeaturePythonImp.html#a39a7fcd6bd878af2928f645a6c344d75)  
  
void | [init](../../de/d49/classApp_1_1FeaturePythonImp.html#ad920e85b43e3f2baa3e1587990130764) ([PyObject](../../df/d1b/classPyObject.html) *pyobj)  
[int](../../d1/da0/classint.html) | [isElementVisible](../../de/d49/classApp_1_1FeaturePythonImp.html#a7118f8fde3ec8ad7ce5cb15f02e7f9c2) (const char *) const  
| Get sub-element visibility.
[More...](../../de/d49/classApp_1_1FeaturePythonImp.html#a7118f8fde3ec8ad7ce5cb15f02e7f9c2)  
  
[bool](../../d9/db9/classbool.html) | [mustExecute](../../de/d49/classApp_1_1FeaturePythonImp.html#a2819dc998f51e0469fbd519387f7c7c2) () const  
void | [onBeforeChange](../../de/d49/classApp_1_1FeaturePythonImp.html#a6954506f6c66d7ea68b8835851f3731a) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
[bool](../../d9/db9/classbool.html) | [onBeforeChangeLabel](../../de/d49/classApp_1_1FeaturePythonImp.html#acfea0a8a6c744c2ec720a0609ee590b6) (std::string &newLabel)  
void | [onChanged](../../de/d49/classApp_1_1FeaturePythonImp.html#a31e2aa2e633c8db8d05057f71dc42a17) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
void | [onDocumentRestored](../../de/d49/classApp_1_1FeaturePythonImp.html#a9ca4d860d98f2a439d1be269b37fe84f) ()  
[ValueT](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04) | [redirectSubName](../../de/d49/classApp_1_1FeaturePythonImp.html#aab242ba739e239fe38f7e42e1e9084c4) (std::ostringstream &ss, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *topParent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *child) const  
[int](../../d1/da0/classint.html) | [setElementVisible](../../de/d49/classApp_1_1FeaturePythonImp.html#a80870ebddcc83803c66aa86179589095) (const char *, [bool](../../d9/db9/classbool.html))  
| Set sub-element visibility.
[More...](../../de/d49/classApp_1_1FeaturePythonImp.html#a80870ebddcc83803c66aa86179589095)  
  
|
[~FeaturePythonImp](../../de/d49/classApp_1_1FeaturePythonImp.html#a93bd704e1d8db6b131cf03c65f92f815)
()  
  
## Member Enumeration Documentation

## ◆ ValueT

enum
[App::FeaturePythonImp::ValueT](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04)  
---  
  
Enumerator  
---  
NotImplemented |   
Accepted |   
Rejected |   
  
## Constructor & Destructor Documentation

## ◆ FeaturePythonImp()

FeaturePythonImp::FeaturePythonImp  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _o_| ) |   
---|---|---|---|---|---  
  
## ◆ ~FeaturePythonImp()

FeaturePythonImp::~FeaturePythonImp  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ allowDuplicateLabel()

[FeaturePythonImp::ValueT](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04) FeaturePythonImp::allowDuplicateLabel  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Accepted](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ae0caca590bddcc9b2789db6f8bc24eab),
[allowDuplicateLabel()](../../de/d49/classApp_1_1FeaturePythonImp.html#a43829c54fcc922a6b758f2378550ea5a),
[NotImplemented](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ac8f4291625102a15d99a85b736bad059),
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce),
and
[Rejected](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04a81c1f4b1ff226929d10c34fa0622986d).

Referenced by
[allowDuplicateLabel()](../../de/d49/classApp_1_1FeaturePythonImp.html#a43829c54fcc922a6b758f2378550ea5a),
and [App::FeaturePythonT< FeatureT
>::allowDuplicateLabel()](../../d2/d2f/classApp_1_1FeaturePythonT.html#acfa7ff0dabb096c033fdd64b3f977211).

## ◆ canLinkProperties()

[FeaturePythonImp::ValueT](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04) FeaturePythonImp::canLinkProperties  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Accepted](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ae0caca590bddcc9b2789db6f8bc24eab),
[canLinkProperties()](../../de/d49/classApp_1_1FeaturePythonImp.html#af7f05cebcab3e184f1004f5fedb3081e),
[NotImplemented](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ac8f4291625102a15d99a85b736bad059),
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce),
and
[Rejected](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04a81c1f4b1ff226929d10c34fa0622986d).

Referenced by
[canLinkProperties()](../../de/d49/classApp_1_1FeaturePythonImp.html#af7f05cebcab3e184f1004f5fedb3081e),
and [App::FeaturePythonT< FeatureT
>::canLinkProperties()](../../d2/d2f/classApp_1_1FeaturePythonT.html#aa6eed1ed82f93836b53def008f8efa47).

## ◆ canLoadPartial()

[int](../../d1/da0/classint.html) FeaturePythonImp::canLoadPartial  | ( | | ) |  const  
---|---|---|---|---  
  
References
[canLoadPartial()](../../de/d49/classApp_1_1FeaturePythonImp.html#a88e2035789dd79a4aad1031fefe2a5e4),
and
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by
[canLoadPartial()](../../de/d49/classApp_1_1FeaturePythonImp.html#a88e2035789dd79a4aad1031fefe2a5e4),
and [App::FeaturePythonT< FeatureT
>::canLoadPartial()](../../d2/d2f/classApp_1_1FeaturePythonT.html#a99ca8e0b5d3c159f43fcd9c69801bfdf).

## ◆ editProperty()

[bool](../../d9/db9/classbool.html) FeaturePythonImp::editProperty  | ( | const char *  | _propName_| ) |   
---|---|---|---|---|---  
  
References
[editProperty()](../../de/d49/classApp_1_1FeaturePythonImp.html#a9e60644e5d2e9d289ef89da5d120138b),
and
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by
[editProperty()](../../de/d49/classApp_1_1FeaturePythonImp.html#a9e60644e5d2e9d289ef89da5d120138b),
and [App::FeaturePythonT< FeatureT
>::editProperty()](../../d2/d2f/classApp_1_1FeaturePythonT.html#a8a5cd6480fbd3d0ac3fab0031b84e68e).

## ◆ execute()

[bool](../../d9/db9/classbool.html) FeaturePythonImp::execute  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Calls the
[execute()](../../de/d49/classApp_1_1FeaturePythonImp.html#ac1d17c03bc1f7d0fc643444b0a2fd069)
method of the Python feature class. If the Python feature class doesn't have
an
[execute()](../../de/d49/classApp_1_1FeaturePythonImp.html#ac1d17c03bc1f7d0fc643444b0a2fd069)
method or if it returns False this method also return false and true
otherwise.

References
[execute()](../../de/d49/classApp_1_1FeaturePythonImp.html#ac1d17c03bc1f7d0fc643444b0a2fd069),
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce),
and
[Base::PyException::ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

Referenced by
[draftobjects.facebinder.Facebinder::addSubobjects()](../../d9/d57/classdraftobjects_1_1facebinder_1_1Facebinder.html#a50c77c202a034ce7109bb93322ff6e4e),
[PathScripts.PathDressupDogbone.ObjectDressup::boneStateList()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#af7788dd97e3ca711047ebc4472cf9f21),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[execute()](../../de/d49/classApp_1_1FeaturePythonImp.html#ac1d17c03bc1f7d0fc643444b0a2fd069),
[App::FeaturePythonT< FeatureT
>::execute()](../../d2/d2f/classApp_1_1FeaturePythonT.html#aff89f1dafffac9466b7f498c2fc00e4f),
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

[bool](../../d9/db9/classbool.html) FeaturePythonImp::getLinkedObject  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _ret_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recurse_ ,   
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ ,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ ,   
|  | [int](../../d1/da0/classint.html) | _depth_  
| ) | |  const  
  
References
[getLinkedObject()](../../de/d49/classApp_1_1FeaturePythonImp.html#a1c801863ae32581043ec7077fd800407),
and
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by
[getLinkedObject()](../../de/d49/classApp_1_1FeaturePythonImp.html#a1c801863ae32581043ec7077fd800407),
and [App::FeaturePythonT< FeatureT
>::getLinkedObject()](../../d2/d2f/classApp_1_1FeaturePythonT.html#ad86b5c211527f9522f1f2c49862b7d53).

## ◆ getPyObject()

[PyObject](../../df/d1b/classPyObject.html) * FeaturePythonImp::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Referenced by [App::FeaturePythonT< FeatureT
>::getPyObject()](../../d2/d2f/classApp_1_1FeaturePythonT.html#a1fbe74b16782db87a7c6e86307ee0c9d).

## ◆ getSubObject()

[bool](../../d9/db9/classbool.html) FeaturePythonImp::getSubObject  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _ret_ ,   
---|---|---|---  
|  | const char *  | _subname_ ,   
|  | [PyObject](../../df/d1b/classPyObject.html) **  | _pyObj_ ,   
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ ,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ ,   
|  | [int](../../d1/da0/classint.html) | _depth_  
| ) | |  const  
  
References
[getSubObject()](../../de/d49/classApp_1_1FeaturePythonImp.html#ac3df43ec698cb0686ea045b6932b0354),
and
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by
[getSubObject()](../../de/d49/classApp_1_1FeaturePythonImp.html#ac3df43ec698cb0686ea045b6932b0354),
and [App::FeaturePythonT< FeatureT
>::getSubObject()](../../d2/d2f/classApp_1_1FeaturePythonT.html#ad6348fc3b6c457be2a119f27f8569b9c).

## ◆ getSubObjects()

[bool](../../d9/db9/classbool.html) FeaturePythonImp::getSubObjects  | ( | std::vector< std::string > & | _ret_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _reason_  
| ) | |  const  
  
References
[getSubObjects()](../../de/d49/classApp_1_1FeaturePythonImp.html#a0cf78f9d418836d904886eb38fdb5233),
and
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by [App::FeaturePythonT< FeatureT
>::getSubObjects()](../../d2/d2f/classApp_1_1FeaturePythonT.html#ac30b8195c30df404205ea2d408d35e93),
and
[getSubObjects()](../../de/d49/classApp_1_1FeaturePythonImp.html#a0cf78f9d418836d904886eb38fdb5233).

## ◆ getViewProviderName()

std::string FeaturePythonImp::getViewProviderName  | ( | void  | | ) |   
---|---|---|---|---|---  
  
References
[getViewProviderName()](../../de/d49/classApp_1_1FeaturePythonImp.html#a5b00ab85c59b31c9e0f8319cf1900984),
and
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by
[getViewProviderName()](../../de/d49/classApp_1_1FeaturePythonImp.html#a5b00ab85c59b31c9e0f8319cf1900984),
and [App::FeaturePythonT< FeatureT
>::getViewProviderNameOverride()](../../d2/d2f/classApp_1_1FeaturePythonT.html#afc869a51e2c9d5a6ba64dd5cbeca1626).

## ◆ hasChildElement()

[FeaturePythonImp::ValueT](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04) FeaturePythonImp::hasChildElement  | ( | | ) |  const  
---|---|---|---|---  
  
return true to activate tree view group object handling

References
[Accepted](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ae0caca590bddcc9b2789db6f8bc24eab),
[hasChildElement()](../../de/d49/classApp_1_1FeaturePythonImp.html#a39a7fcd6bd878af2928f645a6c344d75),
[NotImplemented](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ac8f4291625102a15d99a85b736bad059),
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce),
and
[Rejected](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04a81c1f4b1ff226929d10c34fa0622986d).

Referenced by
[hasChildElement()](../../de/d49/classApp_1_1FeaturePythonImp.html#a39a7fcd6bd878af2928f645a6c344d75),
and [App::FeaturePythonT< FeatureT
>::hasChildElement()](../../d2/d2f/classApp_1_1FeaturePythonT.html#aeea601faec7150c1f670fe6af9e5cff4).

## ◆ init()

void FeaturePythonImp::init  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _pyobj_| ) |   
---|---|---|---|---|---  
  
Referenced by [App::FeaturePythonT< FeatureT
>::onChanged()](../../d2/d2f/classApp_1_1FeaturePythonT.html#aefbf8694218d25f4b90d8ffe7fe796ee),
and
[DocumentObject.DocumentObject::onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882).

## ◆ isElementVisible()

[int](../../d1/da0/classint.html) FeaturePythonImp::isElementVisible  | ( | const char *  | _element_| ) |  const  
---|---|---|---|---|---  
  
Get sub-element visibility.

References
[isElementVisible()](../../de/d49/classApp_1_1FeaturePythonImp.html#a7118f8fde3ec8ad7ce5cb15f02e7f9c2),
and
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by
[isElementVisible()](../../de/d49/classApp_1_1FeaturePythonImp.html#a7118f8fde3ec8ad7ce5cb15f02e7f9c2),
and [App::FeaturePythonT< FeatureT
>::isElementVisible()](../../d2/d2f/classApp_1_1FeaturePythonT.html#a9d85e138815855c3a2ca59e1a5200ade).

## ◆ mustExecute()

[bool](../../d9/db9/classbool.html) FeaturePythonImp::mustExecute  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
References
[mustExecute()](../../de/d49/classApp_1_1FeaturePythonImp.html#a2819dc998f51e0469fbd519387f7c7c2),
and
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by
[mustExecute()](../../de/d49/classApp_1_1FeaturePythonImp.html#a2819dc998f51e0469fbd519387f7c7c2),
and [App::FeaturePythonT< FeatureT
>::mustExecute()](../../d2/d2f/classApp_1_1FeaturePythonT.html#a628caf1f6979184cd03e24423272c87e).

## ◆ onBeforeChange()

void FeaturePythonImp::onBeforeChange  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
  
References
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by [App::FeaturePythonT< FeatureT
>::onBeforeChange()](../../d2/d2f/classApp_1_1FeaturePythonT.html#ada52b433943e87c0e8fcfc300d966c27),
and
[PathScripts.PathGui.QuantitySpinBox::updateProperty()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a8b9b202d7b495b666cb1f6b41ab2beb4).

## ◆ onBeforeChangeLabel()

[bool](../../d9/db9/classbool.html) FeaturePythonImp::onBeforeChangeLabel  | ( | std::string & | _newLabel_| ) |   
---|---|---|---|---|---  
  
References
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by [App::FeaturePythonT< FeatureT
>::onBeforeChangeLabel()](../../d2/d2f/classApp_1_1FeaturePythonT.html#aa81525a29caefd4b2ba4b27113e673a4).

## ◆ onChanged()

void FeaturePythonImp::onChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
  
References
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft::attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire::execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[App::FeaturePythonT< FeatureT
>::onChanged()](../../d2/d2f/classApp_1_1FeaturePythonT.html#aefbf8694218d25f4b90d8ffe7fe796ee),
[ArchBuildingPart.ViewProviderBuildingPart::updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut::updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet::updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel::updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer::updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy::updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ onDocumentRestored()

void FeaturePythonImp::onDocumentRestored  | ( | | ) |   
---|---|---|---|---  
  
References
[onDocumentRestored()](../../de/d49/classApp_1_1FeaturePythonImp.html#a9ca4d860d98f2a439d1be269b37fe84f),
and
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce).

Referenced by
[onDocumentRestored()](../../de/d49/classApp_1_1FeaturePythonImp.html#a9ca4d860d98f2a439d1be269b37fe84f),
and [App::FeaturePythonT< FeatureT
>::onDocumentRestored()](../../d2/d2f/classApp_1_1FeaturePythonT.html#a2943a9b8ea93ef154174081e41f6421a).

## ◆ redirectSubName()

[FeaturePythonImp::ValueT](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04) FeaturePythonImp::redirectSubName  | ( | std::ostringstream & | _ss_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _topParent_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _child_  
| ) | |  const  
  
References
[Accepted](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ae0caca590bddcc9b2789db6f8bc24eab),
[App::DocumentObject::getPyObject()](../../d2/de4/classApp_1_1DocumentObject.html#a1adfcfb2169b5c31374e07346256648f),
[NotImplemented](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04ac8f4291625102a15d99a85b736bad059),
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce),
[redirectSubName()](../../de/d49/classApp_1_1FeaturePythonImp.html#aab242ba739e239fe38f7e42e1e9084c4),
and
[Rejected](../../de/d49/classApp_1_1FeaturePythonImp.html#afee0fc86e50b0b0f78fdba95d94b6e04a81c1f4b1ff226929d10c34fa0622986d).

Referenced by
[redirectSubName()](../../de/d49/classApp_1_1FeaturePythonImp.html#aab242ba739e239fe38f7e42e1e9084c4),
and [App::FeaturePythonT< FeatureT
>::redirectSubName()](../../d2/d2f/classApp_1_1FeaturePythonT.html#ad0b427a0b27f479faea6770d9fdd49a7).

## ◆ setElementVisible()

[int](../../d1/da0/classint.html) FeaturePythonImp::setElementVisible  | ( | const char *  | _element_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _visible_  
| ) | |   
  
Set sub-element visibility.

References
[Base::pyCall()](../../db/d07/namespaceBase.html#a46ca2753e6fc62a58852766e10eff1ce),
and
[setElementVisible()](../../de/d49/classApp_1_1FeaturePythonImp.html#a80870ebddcc83803c66aa86179589095).

Referenced by
[setElementVisible()](../../de/d49/classApp_1_1FeaturePythonImp.html#a80870ebddcc83803c66aa86179589095),
and [App::FeaturePythonT< FeatureT
>::setElementVisible()](../../d2/d2f/classApp_1_1FeaturePythonT.html#a40faf0c5d9ea646f5fbbb77eed1785f1).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/FeaturePython.h
  * FreeCAD/src/App/FeaturePython.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

