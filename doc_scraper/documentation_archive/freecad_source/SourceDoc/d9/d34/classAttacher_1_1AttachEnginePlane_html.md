---
url: https://freecad.github.io/SourceDoc/d9/d34/classAttacher_1_1AttachEnginePlane.html
scraped_at: 2025-09-08T14:58:46.458414
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Attacher](../../d2/d62/namespaceAttacher.html)
  * [AttachEnginePlane](../../d9/d34/classAttacher_1_1AttachEnginePlane.html)

[List of all members](../../dd/d65/classAttacher_1_1AttachEnginePlane-members.html) | Public Member Functions

Attacher::AttachEnginePlane Class Reference

`#include <Attacher.h>`

##  Public Member Functions  
  
---  
|
[AttachEnginePlane](../../d9/d34/classAttacher_1_1AttachEnginePlane.html#a83d27db62c4f4372d93e629e583da547)
()  
virtual [Base::Placement](../../d1/d10/classBase_1_1Placement.html) | [calculateAttachedPlacement](../../d9/d34/classAttacher_1_1AttachEnginePlane.html#ae2a2666d6b3c4d03e24c8400e8bdd490) (const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) &origPlacement) const  
virtual [AttachEnginePlane](../../d9/d34/classAttacher_1_1AttachEnginePlane.html) * | [copy](../../d9/d34/classAttacher_1_1AttachEnginePlane.html#a90028fda42c7faa6e1f7fcd1e3b176f1) () const  
![-](../../closed.png) Public Member Functions inherited from
[Attacher::AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html)  
|
[AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html#ab24739203247504dc16d1e88660531f2)
()  
virtual [Base::Placement](../../d1/d10/classBase_1_1Placement.html) | [calculateAttachedPlacement](../../d2/d85/classAttacher_1_1AttachEngine.html#a507ca433ee1950d6c8d82e900b0cd417) (const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) &origPlacement) const =0  
virtual [AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html) * | [copy](../../d2/d85/classAttacher_1_1AttachEngine.html#a124062ad2deca719d267b209de1d4461) () const =0  
void | [EnableAllSupportedModes](../../d2/d85/classAttacher_1_1AttachEngine.html#a4d261c40e168eb7a650bd499dfce1351) (void)  
| EnableAllModes enables all modes that have shape type lists filled.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#a4d261c40e168eb7a650bd499dfce1351)  
  
[Base::Placement](../../d1/d10/classBase_1_1Placement.html) | [placementFactory](../../d2/d85/classAttacher_1_1AttachEngine.html#a0eff77539401a8d4a04554a970bd85b4) (const gp_Dir &ZAxis, gp_Vec XAxis, gp_Pnt Origin, gp_Pnt refOrg=gp_Pnt(), [bool](../../d9/db9/classbool.html) useRefOrg_Line=false, [bool](../../d9/db9/classbool.html) useRefOrg_Plane=false, [bool](../../d9/db9/classbool.html) makeYVertical=false, [bool](../../d9/db9/classbool.html) makeLegacyFlatFaceOrientation=false, [Base::Placement](../../d1/d10/classBase_1_1Placement.html) *placeOfRef=nullptr) const  
| placementFactory calculates placement from Z axis direction, optional X axis
direction, and origin point.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#a0eff77539401a8d4a04554a970bd85b4)  
  
virtual void | [setUp](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8) (const [App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html) &[references](../../d2/d85/classAttacher_1_1AttachEngine.html#a2f564cef240bdc9c972cbd5ad447da28), [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) [mapMode](../../d2/d85/classAttacher_1_1AttachEngine.html#abcc4689b53e6119536c3316535c0a5d0)=[mmDeactivated](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82abc8bf0ab13257ac3324c75d4fd9f7d12), [bool](../../d9/db9/classbool.html) [mapReverse](../../d2/d85/classAttacher_1_1AttachEngine.html#a7fa7730029ff930975e66aa8f6d7ad20)=false, double [attachParameter](../../d2/d85/classAttacher_1_1AttachEngine.html#afb490e0a43d9e8085f9bd1a5bebd84a3)=0.0, double [surfU](../../d2/d85/classAttacher_1_1AttachEngine.html#a1c3383d5af6dd41870166c33d0cb599e)=0.0, double [surfV](../../d2/d85/classAttacher_1_1AttachEngine.html#a639afedaf2c8ece6b62188ce4c6a3604)=0.0, const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) &[attachmentOffset](../../d2/d85/classAttacher_1_1AttachEngine.html#ab79229efd69c8547445b7067e1d27f4a)=[Base::Placement](../../d1/d10/classBase_1_1Placement.html)())  
virtual void | [setUp](../../d2/d85/classAttacher_1_1AttachEngine.html#a4a5d84dcfbda71c97e067e9550f0bf15) (const [AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html) &another)  
virtual void | [suggestMapModes](../../d2/d85/classAttacher_1_1AttachEngine.html#ac70320562312629b182476560d8ce145) ([SuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html) &result) const  
| suggestMapModes is the procedure that knows everything about mapping modes.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#ac70320562312629b182476560d8ce145)  
  
virtual | [~AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html#af8b991935e13ce576444a2c7e52af839) ()  
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
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Public Member Functions inherited from
[Attacher::AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html)  
static [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | [downgradeType](../../d2/d85/classAttacher_1_1AttachEngine.html#a33503fd1ae1a48d6def706cd9619d53b) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) [type](../../d9/d98/classtype.html))  
| downgradeType converts a more-specific type into a less-specific type (e.g.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#a33503fd1ae1a48d6def706cd9619d53b)  
  
static GProp_GProps | [getInertialPropsOfShape](../../d2/d85/classAttacher_1_1AttachEngine.html#ac5150b1d78b2bdc93fc5507b205e6b34) (const std::vector< const TopoDS_Shape * > &shapes)  
static [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) | [getModeByName](../../d2/d85/classAttacher_1_1AttachEngine.html#a4091635de78a89e0bb9364f6f2bc01bd) (const std::string &modeName)  
static std::string | [getModeName](../../d2/d85/classAttacher_1_1AttachEngine.html#aafcb7d54cafef2090b9d080dc78ec766) ([eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) mmode)  
| getModeName
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#aafcb7d54cafef2090b9d080dc78ec766)  
  
static [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | [getRefTypeByName](../../d2/d85/classAttacher_1_1AttachEngine.html#aa42f4f1f63bc6bf266e5586eb2868d76) (const std::string &typeName)  
static std::string | [getRefTypeName](../../d2/d85/classAttacher_1_1AttachEngine.html#ab8165768b01961787f77c40cdf4040f9) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) shapeType)  
static [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | [getShapeType](../../d2/d85/classAttacher_1_1AttachEngine.html#ac859e617fee1a4f39a2f9186c36f0bb8) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &subshape)  
| getShapeType by link content.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#ac859e617fee1a4f39a2f9186c36f0bb8)  
  
static [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | [getShapeType](../../d2/d85/classAttacher_1_1AttachEngine.html#ad79155676af730dce23e51110b9e8d75) (const TopoDS_Shape &sh)  
| getShapeType by shape.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#ad79155676af730dce23e51110b9e8d75)  
  
static [int](../../d1/da0/classint.html) | [getTypeRank](../../d2/d85/classAttacher_1_1AttachEngine.html#a8ba1752e7ffaff93ed700b144669221e) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) [type](../../d9/d98/classtype.html))  
| getTypeRank determines, how specific is the supplied shape type.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#a8ba1752e7ffaff93ed700b144669221e)  
  
static [int](../../d1/da0/classint.html) | [isShapeOfType](../../d2/d85/classAttacher_1_1AttachEngine.html#aa9a280ee7181ce08a499ec2e914584cb) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) shapeType, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) requirement)  
| isShapeOfType tests if a shape fulfills the requirement of a mode, and
returns a score of how spot on was the requirement.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#aa9a280ee7181ce08a499ec2e914584cb)  
  
static void | [verifyReferencesAreSafe](../../d2/d85/classAttacher_1_1AttachEngine.html#ac8843a2175ebae4cc4d23f006d61abe1) (const [App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html) &[references](../../d2/d85/classAttacher_1_1AttachEngine.html#a2f564cef240bdc9c972cbd5ad447da28))  
| verifyReferencesAreSafe: checks if pointers in references still point to
objects contained in open documents.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#ac8843a2175ebae4cc4d23f006d61abe1)  
  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
![-](../../closed.png) Public Attributes inherited from
[Attacher::AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html)  
[Base::Placement](../../d1/d10/classBase_1_1Placement.html) | [attachmentOffset](../../d2/d85/classAttacher_1_1AttachEngine.html#ab79229efd69c8547445b7067e1d27f4a)  
double | [attachParameter](../../d2/d85/classAttacher_1_1AttachEngine.html#afb490e0a43d9e8085f9bd1a5bebd84a3)  
[eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) | [mapMode](../../d2/d85/classAttacher_1_1AttachEngine.html#abcc4689b53e6119536c3316535c0a5d0)  
[bool](../../d9/db9/classbool.html) | [mapReverse](../../d2/d85/classAttacher_1_1AttachEngine.html#a7fa7730029ff930975e66aa8f6d7ad20)  
std::vector< [bool](../../d9/db9/classbool.html) > | [modeEnabled](../../d2/d85/classAttacher_1_1AttachEngine.html#aa29c3f0cfbad298b493c1ff31e770917)  
| modeEnabled is an indicator, whether some mode is ever suggested or not.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#aa29c3f0cfbad298b493c1ff31e770917)  
  
std::vector< [refTypeStringList](../../d2/d62/namespaceAttacher.html#a1e956a433ed003aff07cf368d39f79ba) > | [modeRefTypes](../../d2/d85/classAttacher_1_1AttachEngine.html#ad17d478d795b1c623547f08be6fcb438)  
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html) | [references](../../d2/d85/classAttacher_1_1AttachEngine.html#a2f564cef240bdc9c972cbd5ad447da28)  
double | [surfU](../../d2/d85/classAttacher_1_1AttachEngine.html#a1c3383d5af6dd41870166c33d0cb599e)  
double | [surfV](../../d2/d85/classAttacher_1_1AttachEngine.html#a639afedaf2c8ece6b62188ce4c6a3604)  
![-](../../closed.png) Static Public Attributes inherited from
[Attacher::AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html)  
static const char * | [eMapModeStrings](../../d2/d85/classAttacher_1_1AttachEngine.html#aaa7b52587d36c82d204a43f6dec6d4f0) []  
static const char * | [eRefTypeStrings](../../d2/d85/classAttacher_1_1AttachEngine.html#a32f23fd69b09ea00c6811ce532464d44) []  
![-](../../closed.png) Protected Member Functions inherited from
[Attacher::AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html)  
[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) | [cat](../../d2/d85/classAttacher_1_1AttachEngine.html#a07d6c1c6c0ef130022069b3b5d896e53) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt1)  
[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) | [cat](../../d2/d85/classAttacher_1_1AttachEngine.html#ae38db8a8939b5e5a80c519d9dc67c5e9) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt1, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt2)  
[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) | [cat](../../d2/d85/classAttacher_1_1AttachEngine.html#a046e1038ddffa659e0f1d7961ade8fd9) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt1, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt2, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt3)  
[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) | [cat](../../d2/d85/classAttacher_1_1AttachEngine.html#acd8b0b9a1dcda2023bbc6ea36e4de041) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt1, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt2, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt3, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt4)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Attacher::AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html)  
static void | [readLinks](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7) (const [App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html) &[references](../../d2/d85/classAttacher_1_1AttachEngine.html#a2f564cef240bdc9c972cbd5ad447da28), std::vector< [App::GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html) * > &geofs, std::vector< const TopoDS_Shape * > &shapes, std::vector< TopoDS_Shape > &storage, std::vector< [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) > &types)  
|
[AttachEngine3D::readLinks](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7
"AttachEngine3D::readLinks.").
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7)  
  
static void | [throwWrongMode](../../d2/d85/classAttacher_1_1AttachEngine.html#a54359fdaacb65497384e7b41f1800c50) ([eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) mmode)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Constructor & Destructor Documentation

## ◆ AttachEnginePlane()

AttachEnginePlane::AttachEnginePlane  | ( | | ) |   
---|---|---|---|---  
  
References
[Attacher::AttachEngine::modeRefTypes](../../d2/d85/classAttacher_1_1AttachEngine.html#ad17d478d795b1c623547f08be6fcb438).

Referenced by
[copy()](../../d9/d34/classAttacher_1_1AttachEnginePlane.html#a90028fda42c7faa6e1f7fcd1e3b176f1).

## Member Function Documentation

## ◆ calculateAttachedPlacement()

| [Base::Placement](../../d1/d10/classBase_1_1Placement.html) AttachEnginePlane::calculateAttachedPlacement  | ( | const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) & | _origPlacement_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Implements
[Attacher::AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html#a507ca433ee1950d6c8d82e900b0cd417).

References
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
and
[Attacher::AttachEngine::setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8).

## ◆ copy()

| [AttachEnginePlane](../../d9/d34/classAttacher_1_1AttachEnginePlane.html) * AttachEnginePlane::copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Implements
[Attacher::AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html#a124062ad2deca719d267b209de1d4461).

References
[AttachEnginePlane()](../../d9/d34/classAttacher_1_1AttachEnginePlane.html#a83d27db62c4f4372d93e629e583da547).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Part/App/Attacher.h
  * FreeCAD/src/Mod/Part/App/Attacher.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

