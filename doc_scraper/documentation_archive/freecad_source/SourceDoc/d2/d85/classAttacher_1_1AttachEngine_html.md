---
url: https://freecad.github.io/SourceDoc/d2/d85/classAttacher_1_1AttachEngine.html
scraped_at: 2025-09-08T14:58:43.498150
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Attacher](../../d2/d62/namespaceAttacher.html)
  * [AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html)

[List of all members](../../d7/de8/classAttacher_1_1AttachEngine-members.html) | Public Member Functions | Static Public Member Functions | Public Attributes | Static Public Attributes | Protected Member Functions | Static Protected Member Functions

Attacher::AttachEngine Class Referenceabstract

The [AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html "The
AttachEngine class is the placement calculation routine, modes, hints and so
on.") class is the placement calculation routine, modes, hints and so on.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#details)

`#include <Attacher.h>`

##  Public Member Functions  
  
---  
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
  
  
##  Static Public Member Functions  
  
---  
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
  
##  Public Attributes  
  
---  
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
  
##  Static Public Attributes  
  
---  
static const char * | [eMapModeStrings](../../d2/d85/classAttacher_1_1AttachEngine.html#aaa7b52587d36c82d204a43f6dec6d4f0) []  
static const char * | [eRefTypeStrings](../../d2/d85/classAttacher_1_1AttachEngine.html#a32f23fd69b09ea00c6811ce532464d44) []  
  
##  Protected Member Functions  
  
---  
[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) | [cat](../../d2/d85/classAttacher_1_1AttachEngine.html#a07d6c1c6c0ef130022069b3b5d896e53) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt1)  
[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) | [cat](../../d2/d85/classAttacher_1_1AttachEngine.html#ae38db8a8939b5e5a80c519d9dc67c5e9) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt1, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt2)  
[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) | [cat](../../d2/d85/classAttacher_1_1AttachEngine.html#a046e1038ddffa659e0f1d7961ade8fd9) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt1, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt2, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt3)  
[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) | [cat](../../d2/d85/classAttacher_1_1AttachEngine.html#acd8b0b9a1dcda2023bbc6ea36e4de041) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt1, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt2, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt3, [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) rt4)  
  
##  Static Protected Member Functions  
  
---  
static void | [readLinks](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7) (const [App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html) &[references](../../d2/d85/classAttacher_1_1AttachEngine.html#a2f564cef240bdc9c972cbd5ad447da28), std::vector< [App::GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html) * > &geofs, std::vector< const TopoDS_Shape * > &shapes, std::vector< TopoDS_Shape > &storage, std::vector< [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) > &types)  
|
[AttachEngine3D::readLinks](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7
"AttachEngine3D::readLinks.").
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7)  
  
static void | [throwWrongMode](../../d2/d85/classAttacher_1_1AttachEngine.html#a54359fdaacb65497384e7b41f1800c50) ([eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) mmode)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

The [AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html "The
AttachEngine class is the placement calculation routine, modes, hints and so
on.") class is the placement calculation routine, modes, hints and so on.

It can be used separately, without deriving from AttachableObject.

## Constructor & Destructor Documentation

## ◆ AttachEngine()

AttachEngine::AttachEngine  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~AttachEngine()

| virtual Attacher::AttachEngine::~AttachEngine  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ calculateAttachedPlacement()

| virtual [Base::Placement](../../d1/d10/classBase_1_1Placement.html) Attacher::AttachEngine::calculateAttachedPlacement  | ( | const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) & | _origPlacement_| ) |  const  
---|---|---|---|---|---  
pure virtual  
  
Implemented in
[Attacher::AttachEngine3D](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEnginePlane](../../d9/d34/classAttacher_1_1AttachEnginePlane.html#ae2a2666d6b3c4d03e24c8400e8bdd490),
[Attacher::AttachEngineLine](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
and
[Attacher::AttachEnginePoint](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a8ca116a405c93c0a9b1c0f70dd398c49).

## ◆ cat() [1/4]

| [refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) Attacher::AttachEngine::cat  | ( | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _rt1_| ) |   
---|---|---|---|---|---  
protected  
  
## ◆ cat() [2/4]

| [refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) Attacher::AttachEngine::cat  | ( | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _rt1_ ,   
---|---|---|---  
|  | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _rt2_  
| ) | |   
protected  
  
## ◆ cat() [3/4]

| [refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) Attacher::AttachEngine::cat  | ( | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _rt1_ ,   
---|---|---|---  
|  | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _rt2_ ,   
|  | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _rt3_  
| ) | |   
protected  
  
## ◆ cat() [4/4]

| [refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) Attacher::AttachEngine::cat  | ( | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _rt1_ ,   
---|---|---|---  
|  | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _rt2_ ,   
|  | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _rt3_ ,   
|  | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _rt4_  
| ) | |   
protected  
  
## ◆ copy()

| virtual [AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html) * Attacher::AttachEngine::copy  | ( | | ) |  const  
---|---|---|---|---  
pure virtual  
  
Implemented in
[Attacher::AttachEngine3D](../../d1/db7/classAttacher_1_1AttachEngine3D.html#aa7d97c451cce1ed38fea80d163cec51a),
[Attacher::AttachEnginePlane](../../d9/d34/classAttacher_1_1AttachEnginePlane.html#a90028fda42c7faa6e1f7fcd1e3b176f1),
[Attacher::AttachEngineLine](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a92a12f25724d41ac0d4cd2599e5eec83),
and
[Attacher::AttachEnginePoint](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a424a145ad414042262d25f45d4f9ea2e).

## ◆ downgradeType()

| [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) AttachEngine::downgradeType  | ( | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _type_| ) |   
---|---|---|---|---|---  
static  
  
downgradeType converts a more-specific type into a less-specific type (e.g.

rtCircle->rtCurve, rtCurve->rtEdge, rtEdge->rtAnything)

Parameters

     type|   
---|---  
  
Returns

    the downgraded type. 

References
[Attacher::rtAnything](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7dd1102755b58238cc225e81005bfa57),
[Attacher::rtCircle](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a5ef28220d2bbc64118e291de7a3002bc),
[Attacher::rtConic](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a60e58cadaba8ad9f34525bac7cd0cdae),
[Attacher::rtConicalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a4a7c3c2a81920a940e12200352874bb5),
[Attacher::rtCurve](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a779b0d75fa4a0665cdf2bf370c8fef49),
[Attacher::rtCylindricalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738adca16f64a04f699cded8fd8872b355df),
[Attacher::rtEdge](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a80465fa5307ae1503bbdf08ab0aa55b3),
[Attacher::rtEllipse](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738af90593d78196f13888d5896c22402180),
[Attacher::rtFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7f4ce91f652aada5d77a26d7503ab56c),
[Attacher::rtFlagHasPlacement](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738ae063749f0a203938e8d6fae4906de6f6),
[Attacher::rtFlatFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a6d6eaaa2c32936e59155ccf7c73a5a30),
[Attacher::rtHyperbola](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a0883a5675ecccbb9319269711780fa47),
[Attacher::rtLine](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a605a5d2b20587133d59bac87dcb5bdaf),
[Attacher::rtParabola](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738aa14d8a88277d9adc6e12f7b713414f1b),
[Attacher::rtPart](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738ad506738ccf8a39328354da3ab61e5399),
[Attacher::rtSolid](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738add0a306d000e83a436ad4e1ca1ce3bcf),
[Attacher::rtSphericalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738aa427b3720abf0d02da26c259aefbf51e),
[Attacher::rtSurfaceRev](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a29a3eb150ccf5342a0599d32e093b190),
[Attacher::rtToroidalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a38952bba064d1de310d0d5dcbd655f7d),
[Attacher::rtVertex](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738aa5f9a31dffdc2f9dfdc6b8ca231d19c6),
and
[Attacher::rtWire](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7e192c84329dfdb3be167e6ca3580497).

Referenced by
[getTypeRank()](../../d2/d85/classAttacher_1_1AttachEngine.html#a8ba1752e7ffaff93ed700b144669221e),
and
[isShapeOfType()](../../d2/d85/classAttacher_1_1AttachEngine.html#aa9a280ee7181ce08a499ec2e914584cb).

## ◆ EnableAllSupportedModes()

void AttachEngine::EnableAllSupportedModes  | ( | void  | | ) |   
---|---|---|---|---|---  
  
EnableAllModes enables all modes that have shape type lists filled.

The function acts on modeEnabled array.

References
[Attacher::mmDummy_NumberOfModes](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a37e43c9399a491fc43e9cc24a84fe7ec),
[modeEnabled](../../d2/d85/classAttacher_1_1AttachEngine.html#aa29c3f0cfbad298b493c1ff31e770917),
and
[modeRefTypes](../../d2/d85/classAttacher_1_1AttachEngine.html#ad17d478d795b1c623547f08be6fcb438).

## ◆ getInertialPropsOfShape()

| GProp_GProps AttachEngine::getInertialPropsOfShape  | ( | const std::vector< const TopoDS_Shape * > & | _shapes_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
and
[Attacher::AttachEnginePoint::calculateAttachedPlacement()](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a8ca116a405c93c0a9b1c0f70dd398c49).

## ◆ getModeByName()

| [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) AttachEngine::getModeByName  | ( | const std::string & | _modeName_| ) |   
---|---|---|---|---|---  
static  
  
References
[eMapModeStrings](../../d2/d85/classAttacher_1_1AttachEngine.html#aaa7b52587d36c82d204a43f6dec6d4f0),
and
[Attacher::mmDummy_NumberOfModes](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a37e43c9399a491fc43e9cc24a84fe7ec).

## ◆ getModeName()

| std::string AttachEngine::getModeName  | ( | [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) | _mmode_| ) |   
---|---|---|---|---|---  
static  
  
getModeName

Parameters

     mmode|   
---|---  
  
Returns

    returns a string that identifies the attachment mode in enum property. 

References
[eMapModeStrings](../../d2/d85/classAttacher_1_1AttachEngine.html#aaa7b52587d36c82d204a43f6dec6d4f0),
and
[Attacher::mmDummy_NumberOfModes](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a37e43c9399a491fc43e9cc24a84fe7ec).

Referenced by
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a).

## ◆ getRefTypeByName()

| [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) AttachEngine::getRefTypeByName  | ( | const std::string & | _typeName_| ) |   
---|---|---|---|---|---  
static  
  
References
[eRefTypeStrings](../../d2/d85/classAttacher_1_1AttachEngine.html#a32f23fd69b09ea00c6811ce532464d44),
[Attacher::rtDummy_numberOfShapeTypes](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a98ce104efe7501c0a4f2d6e6ff4486a9),
and
[Attacher::rtFlagHasPlacement](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738ae063749f0a203938e8d6fae4906de6f6).

## ◆ getRefTypeName()

| std::string AttachEngine::getRefTypeName  | ( | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _shapeType_| ) |   
---|---|---|---|---|---  
static  
  
References
[eRefTypeStrings](../../d2/d85/classAttacher_1_1AttachEngine.html#a32f23fd69b09ea00c6811ce532464d44),
[Attacher::rtDummy_numberOfShapeTypes](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a98ce104efe7501c0a4f2d6e6ff4486a9),
and
[Attacher::rtFlagHasPlacement](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738ae063749f0a203938e8d6fae4906de6f6).

## ◆ getShapeType() [1/2]

| [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) AttachEngine::getShapeType  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const std::string & | _subshape_  
| ) | |   
static  
  
getShapeType by link content.

Will include rtFlagHasPlacement, if applies.

Parameters

     obj|   
---|---  
subshape| (input). Can be empty string (then, whole object will be used for
shape type testing)  
  
Returns

    

References
[readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
and
[App::PropertyLinkSubList::setValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f).

## ◆ getShapeType() [2/2]

| [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) AttachEngine::getShapeType  | ( | const TopoDS_Shape & | _sh_| ) |   
---|---|---|---|---|---  
static  
  
getShapeType by shape.

Will never set rtFlagHasPlacement.

Parameters

     sh|   
---|---  
  
Returns

    

References
[getShapeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#ad79155676af730dce23e51110b9e8d75),
[Attacher::rtAnything](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7dd1102755b58238cc225e81005bfa57),
[Attacher::rtCircle](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a5ef28220d2bbc64118e291de7a3002bc),
[Attacher::rtConicalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a4a7c3c2a81920a940e12200352874bb5),
[Attacher::rtCurve](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a779b0d75fa4a0665cdf2bf370c8fef49),
[Attacher::rtCylindricalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738adca16f64a04f699cded8fd8872b355df),
[Attacher::rtEllipse](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738af90593d78196f13888d5896c22402180),
[Attacher::rtFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7f4ce91f652aada5d77a26d7503ab56c),
[Attacher::rtFlatFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a6d6eaaa2c32936e59155ccf7c73a5a30),
[Attacher::rtHyperbola](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a0883a5675ecccbb9319269711780fa47),
[Attacher::rtLine](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a605a5d2b20587133d59bac87dcb5bdaf),
[Attacher::rtParabola](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738aa14d8a88277d9adc6e12f7b713414f1b),
[Attacher::rtSolid](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738add0a306d000e83a436ad4e1ca1ce3bcf),
[Attacher::rtSphericalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738aa427b3720abf0d02da26c259aefbf51e),
[Attacher::rtSurfaceRev](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a29a3eb150ccf5342a0599d32e093b190),
[Attacher::rtToroidalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a38952bba064d1de310d0d5dcbd655f7d),
[Attacher::rtVertex](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738aa5f9a31dffdc2f9dfdc6b8ca231d19c6),
and
[Attacher::rtWire](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7e192c84329dfdb3be167e6ca3580497).

Referenced by
[getShapeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#ad79155676af730dce23e51110b9e8d75),
and
[readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7).

## ◆ getTypeRank()

| [int](../../d1/da0/classint.html) AttachEngine::getTypeRank  | ( | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _type_| ) |   
---|---|---|---|---|---  
static  
  
getTypeRank determines, how specific is the supplied shape type.

The ranks are outlined in definition of eRefType. The ranks are defined by
implementation of
[downgradeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#a33503fd1ae1a48d6def706cd9619d53b
"downgradeType converts a more-specific type into a less-specific type
\(e.g.").

Parameters

     type|   
---|---  
  
Returns

    number of times the type can be [downgradeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#a33503fd1ae1a48d6def706cd9619d53b "downgradeType converts a more-specific type into a less-specific type \(e.g.") before it becomes rtAnything 

References
[downgradeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#a33503fd1ae1a48d6def706cd9619d53b),
[Attacher::rtAnything](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7dd1102755b58238cc225e81005bfa57),
and
[Attacher::rtFlagHasPlacement](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738ae063749f0a203938e8d6fae4906de6f6).

Referenced by
[isShapeOfType()](../../d2/d85/classAttacher_1_1AttachEngine.html#aa9a280ee7181ce08a499ec2e914584cb).

## ◆ isShapeOfType()

| [int](../../d1/da0/classint.html) AttachEngine::isShapeOfType  | ( | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _shapeType_ ,   
---|---|---|---  
|  | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _requirement_  
| ) | |   
static  
  
isShapeOfType tests if a shape fulfills the requirement of a mode, and returns
a score of how spot on was the requirement.

Parameters

     shapeType| (use return value of [AttachEngine::getShapeType](../../d2/d85/classAttacher_1_1AttachEngine.html#ad79155676af730dce23e51110b9e8d75 "getShapeType by shape."))   
---|---  
requirement|  
  
Returns

    : -1 - doesn't fulfill, 0 - compatible topology, but incompatible specific (e.g. rtLine, rtCircle); 1 - valid by generic type (e.g. rtCircle is rtEdge), 2 and up - more and more specific match (according to rank of requirement) 

References
[downgradeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#a33503fd1ae1a48d6def706cd9619d53b),
[getTypeRank()](../../d2/d85/classAttacher_1_1AttachEngine.html#a8ba1752e7ffaff93ed700b144669221e),
[Attacher::rtAnything](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7dd1102755b58238cc225e81005bfa57),
and
[Attacher::rtFlagHasPlacement](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738ae063749f0a203938e8d6fae4906de6f6).

Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
and
[suggestMapModes()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac70320562312629b182476560d8ce145).

## ◆ placementFactory()

[Base::Placement](../../d1/d10/classBase_1_1Placement.html) AttachEngine::placementFactory  | ( | const gp_Dir & | _ZAxis_ ,   
---|---|---|---  
|  | gp_Vec  | _XAxis_ ,   
|  | gp_Pnt  | _Origin_ ,   
|  | gp_Pnt  | _refOrg_ = `gp_Pnt()`,   
|  | [bool](../../d9/db9/classbool.html) | _useRefOrg_Line_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _useRefOrg_Plane_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _makeYVertical_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _makeLegacyFlatFaceOrientation_ = `false`,   
|  | [Base::Placement](../../d1/d10/classBase_1_1Placement.html) *  | _placeOfRef_ = `nullptr`  
| ) | |  const  
  
placementFactory calculates placement from Z axis direction, optional X axis
direction, and origin point.

Parameters

     ZAxis| (input) mandatory. Z axis of the returned placement will strictly coincide with ZAxis.  
---|---  
XAxis| (input) optional (i.e., can be zero). Sets the preferred X axis
orientation. If it is not perpendicular to ZAxis, it will be forced to be. If
XAxis is zero, the effect is equivalent to setting makeYVertical to true.  
Origin| (input) mandatory.  
refOrg| (input). The point that will be used in case any of useRefOrg_XX
parameters is true.  
useRefOrg_Line| (input). If true, Origin will be moved along ZAxis to be as
close as possible to refOrg.  
useRefOrg_Plane| (input). If true, Origin will be moved in XAxis-YAxis plane
to be as close as possible to refOrg.  
makeYVertical| (input). If true, XAxis is ignored, and X and Y axes are
defined in order to make Y axis go as upwards as possible. If ZAxis is
strictly upwards, XY will match global XY. If ZAxis is strictly downwards,
XAxis will be the reversed global X axis.  
makeLegacyFlatFaceOrientation| (input). Modifies the behavior of makeYVertical
to match the logic that was used in mapping of sketches to flat faces in
FreeCAD prior to introduction of
[Attacher](../../d2/d62/namespaceAttacher.html "Attacher.h, Attacher.cpp
contain the functionality of deriving placement from a set of geometric
sube..."). Set makeYVertical to true if using this.  
  
Returns

    the resulting placement. ReverseXY property of [Attacher](../../d2/d62/namespaceAttacher.html "Attacher.h, Attacher.cpp contain the functionality of deriving placement from a set of geometric sube...") will be automatically applied. 

References
[Base::Placement::getRotation()](../../d1/d10/classBase_1_1Placement.html#af5b5009ff533f306ed03d5259bfb6797),
[mapReverse](../../d2/d85/classAttacher_1_1AttachEngine.html#a7fa7730029ff930975e66aa8f6d7ad20),
[Base::Rotation::multVec()](../../d4/d18/classBase_1_1Rotation.html#a3cdb5a5eb357dd8a1c974f7374fe4a87),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
and
[Attacher::AttachEnginePoint::calculateAttachedPlacement()](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a8ca116a405c93c0a9b1c0f70dd398c49).

## ◆ readLinks()

| void AttachEngine::readLinks  | ( | const [App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html) & | _references_ ,   
---|---|---|---  
|  | std::vector< [App::GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html) * > & | _geofs_ ,   
|  | std::vector< const TopoDS_Shape * > & | _shapes_ ,   
|  | std::vector< TopoDS_Shape > & | _storage_ ,   
|  | std::vector< [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) > & | _types_  
| ) | |   
staticprotected  
  
[AttachEngine3D::readLinks](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7
"AttachEngine3D::readLinks.").

Parameters

     parts|   
---|---  
shapes|  
storage| is a buffer storing what some of the pointers in shapes point to. It
is needed, since subshapes are copied in the process (but copying a whole
shape of an object can potentially be slow).  
  
References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[Base::Placement::getRotation()](../../d1/d10/classBase_1_1Placement.html#af5b5009ff533f306ed03d5259bfb6797),
[getShapeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#ad79155676af730dce23e51110b9e8d75),
[App::PropertyLinkSubList::getSubValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a9a725b9517a6ff87f8811a75d71aa9ef),
[Base::BaseClass::getTypeId()](../../df/d4d/classBase_1_1BaseClass.html#addbd3a4f09fce7ce5c6bf021e4c1d566),
[App::PropertyPlacement::getValue()](../../da/d51/classApp_1_1PropertyPlacement.html#a430fb2b0baee33f2967118bbbc7e6d74),
[App::PropertyLinkSubList::getValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#af073aea1824333723ab0d962040d8713),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
[Base::Placement::multVec()](../../d1/d10/classBase_1_1Placement.html#a7d3c9f9cb3aee926050a6000c5acbb09),
[Base::Rotation::multVec()](../../d4/d18/classBase_1_1Rotation.html#a3cdb5a5eb357dd8a1c974f7374fe4a87),
[App::GeoFeature::Placement](../../d7/d75/classApp_1_1GeoFeature.html#a1bb7798d3563d653aaae37376e5e4167),
[references](../../d2/d85/classAttacher_1_1AttachEngine.html#a2f564cef240bdc9c972cbd5ad447da28),
[Attacher::rtFlagHasPlacement](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738ae063749f0a203938e8d6fae4906de6f6),
[verifyReferencesAreSafe()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac8843a2175ebae4cc4d23f006d61abe1),
[Base::ConsoleSingleton::Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[Attacher::AttachEnginePoint::calculateAttachedPlacement()](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a8ca116a405c93c0a9b1c0f70dd398c49),
[getShapeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac859e617fee1a4f39a2f9186c36f0bb8),
and
[suggestMapModes()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac70320562312629b182476560d8ce145).

## ◆ setUp() [1/2]

| void AttachEngine::setUp  | ( | const [App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html) & | _references_ ,   
---|---|---|---  
|  | [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) | _mapMode_ = `[mmDeactivated](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82abc8bf0ab13257ac3324c75d4fd9f7d12)`,   
|  | [bool](../../d9/db9/classbool.html) | _mapReverse_ = `false`,   
|  | double  | _attachParameter_ = `0.0`,   
|  | double  | _surfU_ = `0.0`,   
|  | double  | _surfV_ = `0.0`,   
|  | const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) & | _attachmentOffset_ = `[Base::Placement](../../d1/d10/classBase_1_1Placement.html)()`  
| ) | |   
virtual  
  
References
[attachmentOffset](../../d2/d85/classAttacher_1_1AttachEngine.html#ab79229efd69c8547445b7067e1d27f4a),
[attachParameter](../../d2/d85/classAttacher_1_1AttachEngine.html#afb490e0a43d9e8085f9bd1a5bebd84a3),
[mapMode](../../d2/d85/classAttacher_1_1AttachEngine.html#abcc4689b53e6119536c3316535c0a5d0),
[mapReverse](../../d2/d85/classAttacher_1_1AttachEngine.html#a7fa7730029ff930975e66aa8f6d7ad20),
[App::PropertyLinkSubList::Paste()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a3dfbcd135189c2b3e6e7c6136ed572a1),
[references](../../d2/d85/classAttacher_1_1AttachEngine.html#a2f564cef240bdc9c972cbd5ad447da28),
[surfU](../../d2/d85/classAttacher_1_1AttachEngine.html#a1c3383d5af6dd41870166c33d0cb599e),
and
[surfV](../../d2/d85/classAttacher_1_1AttachEngine.html#a639afedaf2c8ece6b62188ce4c6a3604).

Referenced by
[Attacher::AttachEnginePlane::calculateAttachedPlacement()](../../d9/d34/classAttacher_1_1AttachEnginePlane.html#ae2a2666d6b3c4d03e24c8400e8bdd490),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[Attacher::AttachEnginePoint::calculateAttachedPlacement()](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a8ca116a405c93c0a9b1c0f70dd398c49),
[setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#a4a5d84dcfbda71c97e067e9550f0bf15),
and
[SketcherGui::SuggestAutoMapMode()](../../d6/d44/namespaceSketcherGui.html#a21c0eeb3a6a37afe433d190fc7a22c18).

## ◆ setUp() [2/2]

| void AttachEngine::setUp  | ( | const [AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html) & | _another_| ) |   
---|---|---|---|---|---  
virtual  
  
References
[attachmentOffset](../../d2/d85/classAttacher_1_1AttachEngine.html#ab79229efd69c8547445b7067e1d27f4a),
[attachParameter](../../d2/d85/classAttacher_1_1AttachEngine.html#afb490e0a43d9e8085f9bd1a5bebd84a3),
[mapMode](../../d2/d85/classAttacher_1_1AttachEngine.html#abcc4689b53e6119536c3316535c0a5d0),
[mapReverse](../../d2/d85/classAttacher_1_1AttachEngine.html#a7fa7730029ff930975e66aa8f6d7ad20),
[references](../../d2/d85/classAttacher_1_1AttachEngine.html#a2f564cef240bdc9c972cbd5ad447da28),
[setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8),
[surfU](../../d2/d85/classAttacher_1_1AttachEngine.html#a1c3383d5af6dd41870166c33d0cb599e),
and
[surfV](../../d2/d85/classAttacher_1_1AttachEngine.html#a639afedaf2c8ece6b62188ce4c6a3604).

## ◆ suggestMapModes()

| void AttachEngine::suggestMapModes  | ( | [SuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html) & | _result_| ) |  const  
---|---|---|---|---|---  
virtual  
  
suggestMapModes is the procedure that knows everything about mapping modes.

It returns the most appropriate mapping mode, as well as list of all modes
that will accept the set of references. In case no modes apply, extra
information regarding reasons is returned in msg.

Parameters

     result| (output). Returns results of suggestion, such as best fit mode, list of all modes that apply, hints, etc.   
---|---  
  
References
[isShapeOfType()](../../d2/d85/classAttacher_1_1AttachEngine.html#aa9a280ee7181ce08a499ec2e914584cb),
[Attacher::mmDeactivated](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82abc8bf0ab13257ac3324c75d4fd9f7d12),
[Attacher::mmDummy_NumberOfModes](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a37e43c9399a491fc43e9cc24a84fe7ec),
[modeEnabled](../../d2/d85/classAttacher_1_1AttachEngine.html#aa29c3f0cfbad298b493c1ff31e770917),
[modeRefTypes](../../d2/d85/classAttacher_1_1AttachEngine.html#ad17d478d795b1c623547f08be6fcb438),
[readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[references](../../d2/d85/classAttacher_1_1AttachEngine.html#a2f564cef240bdc9c972cbd5ad447da28),
[Attacher::SuggestResult::srIncompatibleGeometry](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0ea205b288c2244f00b6759c8cb9b20980c),
[Attacher::SuggestResult::srLinkBroken](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0ea01ae847eda7c703e82a60b7795913123),
[Attacher::SuggestResult::srNoModesFit](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0eaea3cb6f66abac565559cb3437ab1bfee),
and
[Attacher::SuggestResult::srOK](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0ea072ce366fcfb69c28680b9673c3f765d).

Referenced by
[SketcherGui::SuggestAutoMapMode()](../../d6/d44/namespaceSketcherGui.html#a21c0eeb3a6a37afe433d190fc7a22c18).

## ◆ throwWrongMode()

| void AttachEngine::throwWrongMode  | ( | [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) | _mmode_| ) |   
---|---|---|---|---|---  
staticprotected  
  
References
[eMapModeStrings](../../d2/d85/classAttacher_1_1AttachEngine.html#aaa7b52587d36c82d204a43f6dec6d4f0),
and
[Attacher::mmDummy_NumberOfModes](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a37e43c9399a491fc43e9cc24a84fe7ec).

Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
and
[Attacher::AttachEnginePoint::calculateAttachedPlacement()](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a8ca116a405c93c0a9b1c0f70dd398c49).

## ◆ verifyReferencesAreSafe()

| void AttachEngine::verifyReferencesAreSafe  | ( | const [App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html) & | _references_| ) |   
---|---|---|---|---|---  
static  
  
verifyReferencesAreSafe: checks if pointers in references still point to
objects contained in open documents.

This guarantees the links are valid. Throws
[Base::Exception](../../d8/df7/classBase_1_1Exception.html) if invalid links
are found.

References
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::Application::getDocuments()](../../da/dbf/classApp_1_1Application.html#a955aad8188b482bb46f74a46b1946e3a),
[App::PropertyLinkSubList::getValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#af073aea1824333723ab0d962040d8713),
and
[references](../../d2/d85/classAttacher_1_1AttachEngine.html#a2f564cef240bdc9c972cbd5ad447da28).

Referenced by
[readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7).

## Member Data Documentation

## ◆ attachmentOffset

[Base::Placement](../../d1/d10/classBase_1_1Placement.html)
Attacher::AttachEngine::attachmentOffset  
---  
  
Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[Attacher::AttachEnginePoint::calculateAttachedPlacement()](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a8ca116a405c93c0a9b1c0f70dd398c49),
and
[setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8).

## ◆ attachParameter

double Attacher::AttachEngine::attachParameter  
---  
  
Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
and
[setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8).

## ◆ eMapModeStrings

| const char * AttachEngine::eMapModeStrings  
---  
static  
  
Referenced by
[getModeByName()](../../d2/d85/classAttacher_1_1AttachEngine.html#a4091635de78a89e0bb9364f6f2bc01bd),
[getModeName()](../../d2/d85/classAttacher_1_1AttachEngine.html#aafcb7d54cafef2090b9d080dc78ec766),
and
[throwWrongMode()](../../d2/d85/classAttacher_1_1AttachEngine.html#a54359fdaacb65497384e7b41f1800c50).

## ◆ eRefTypeStrings

| const char * AttachEngine::eRefTypeStrings  
---  
static  
  
**Initial value:**

= {

"Any",

"Vertex",

"Edge",

"Face",

"Line",

"Curve",

"Circle",

"Conic",

"Ellipse",

"Parabola",

"Hyperbola",

"Plane",

"Sphere",

"Revolve",

"Cylinder",

"Torus",

"Cone",

"Object",

"Solid",

"Wire",

nullptr

}

Referenced by
[getRefTypeByName()](../../d2/d85/classAttacher_1_1AttachEngine.html#aa42f4f1f63bc6bf266e5586eb2868d76),
and
[getRefTypeName()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab8165768b01961787f77c40cdf4040f9).

## ◆ mapMode

[eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82)
Attacher::AttachEngine::mapMode  
---  
  
Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[Attacher::AttachEnginePoint::calculateAttachedPlacement()](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a8ca116a405c93c0a9b1c0f70dd398c49),
and
[setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8).

## ◆ mapReverse

[bool](../../d9/db9/classbool.html) Attacher::AttachEngine::mapReverse  
---  
  
Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[placementFactory()](../../d2/d85/classAttacher_1_1AttachEngine.html#a0eff77539401a8d4a04554a970bd85b4),
and
[setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8).

## ◆ modeEnabled

std::vector<[bool](../../d9/db9/classbool.html)>
Attacher::AttachEngine::modeEnabled  
---  
  
modeEnabled is an indicator, whether some mode is ever suggested or not.

Set to false to suppress suggesting some mode, like so:
modeEnabled[mmModeIDontLike] = false;

Referenced by
[EnableAllSupportedModes()](../../d2/d85/classAttacher_1_1AttachEngine.html#a4d261c40e168eb7a650bd499dfce1351),
and
[suggestMapModes()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac70320562312629b182476560d8ce145).

## ◆ modeRefTypes

std::vector<[refTypeStringList](../../d2/d62/namespaceAttacher.html#a1e956a433ed003aff07cf368d39f79ba)>
Attacher::AttachEngine::modeRefTypes  
---  
  
Referenced by
[Attacher::AttachEngineLine::AttachEngineLine()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a76ed26cbfbbb53867d650900560b36c7),
[Attacher::AttachEnginePlane::AttachEnginePlane()](../../d9/d34/classAttacher_1_1AttachEnginePlane.html#a83d27db62c4f4372d93e629e583da547),
[Attacher::AttachEnginePoint::AttachEnginePoint()](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a1a1b82b5e9ff25fd122dc674ae1ab04b),
[EnableAllSupportedModes()](../../d2/d85/classAttacher_1_1AttachEngine.html#a4d261c40e168eb7a650bd499dfce1351),
[AttacherGui::getRefListForMode()](../../d9/d53/namespaceAttacherGui.html#a23410823e9ff27aa82b030d72d3d6d42),
and
[suggestMapModes()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac70320562312629b182476560d8ce145).

## ◆ references

[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html)
Attacher::AttachEngine::references  
---  
  
Referenced by
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[Attacher::AttachEnginePoint::calculateAttachedPlacement()](../../d8/df8/classAttacher_1_1AttachEnginePoint.html#a8ca116a405c93c0a9b1c0f70dd398c49),
[femguiutils.selection_widgets.GeometryElementsSelection::get_allitems_text()](../../d2/df2/classfemguiutils_1_1selection__widgets_1_1GeometryElementsSelection.html#a444e505c938231d3a5854edb835fd2e0),
[femguiutils.selection_widgets.GeometryElementsSelection::get_references()](../../d2/df2/classfemguiutils_1_1selection__widgets_1_1GeometryElementsSelection.html#a860eb6c4e5eaf389b1c71d7dca066c14),
[femguiutils.selection_widgets.GeometryElementsSelection::has_equal_references_shape_types()](../../d2/df2/classfemguiutils_1_1selection__widgets_1_1GeometryElementsSelection.html#a1b54dea60cf8d78f0b232c7821b8684f),
[readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[femguiutils.selection_widgets.GeometryElementsSelection::remove_all_references()](../../d2/df2/classfemguiutils_1_1selection__widgets_1_1GeometryElementsSelection.html#a25645ea6619400db76b7c3f79a776d7b),
[femguiutils.selection_widgets.GeometryElementsSelection::remove_selected_reference()](../../d2/df2/classfemguiutils_1_1selection__widgets_1_1GeometryElementsSelection.html#a37c9204fa945de0f994f04d1dda32209),
[femguiutils.selection_widgets.GeometryElementsSelection::select_clicked_reference_shape()](../../d2/df2/classfemguiutils_1_1selection__widgets_1_1GeometryElementsSelection.html#a0516da8ad7e0d11ec31b6e832f604f70),
[femguiutils.selection_widgets.GeometryElementsSelection::selectionParser()](../../d2/df2/classfemguiutils_1_1selection__widgets_1_1GeometryElementsSelection.html#ab06d852768ce4702c4865309e46065bd),
[setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8),
[suggestMapModes()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac70320562312629b182476560d8ce145),
and
[verifyReferencesAreSafe()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac8843a2175ebae4cc4d23f006d61abe1).

## ◆ surfU

double Attacher::AttachEngine::surfU  
---  
  
Referenced by
[setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8).

## ◆ surfV

double Attacher::AttachEngine::surfV  
---  
  
Referenced by
[setUp()](../../d2/d85/classAttacher_1_1AttachEngine.html#adf472fd6bdeb076b4730f1550e2873b8).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Part/App/Attacher.h
  * FreeCAD/src/Mod/Part/App/Attacher.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

