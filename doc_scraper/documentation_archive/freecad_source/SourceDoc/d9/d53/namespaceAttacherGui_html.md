---
url: https://freecad.github.io/SourceDoc/d9/d53/namespaceAttacherGui.html
scraped_at: 2025-09-08T14:58:50.463427
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Typedefs | Functions | Variables

AttacherGui Namespace Reference

AttacherTexts.h, .cpp - files that contain user-friendly translatable names of
attachment modes, as well as help texts, and the like.
[More...](../../d9/d53/namespaceAttacherGui.html#details)

##  Classes  
  
---  
class | [AttacherGuiPy](../../d9/d27/classAttacherGui_1_1AttacherGuiPy.html)  
  
##  Typedefs  
  
---  
typedef std::vector< QString > | [TextSet](../../d9/d53/namespaceAttacherGui.html#a04587e69dfb8e24b0e6aa9d0072b240a)  
  
##  Functions  
  
---  
QStringList | [getRefListForMode](../../d9/d53/namespaceAttacherGui.html#a23410823e9ff27aa82b030d72d3d6d42) ([AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html) &attacher, [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) mmode)  
QString | [getShapeTypeText](../../d9/d53/namespaceAttacherGui.html#a068550542e3bc24e606c15b9beebf2ad) ([eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) [type](../../d9/d98/classtype.html))  
[TextSet](../../d9/d53/namespaceAttacherGui.html#a04587e69dfb8e24b0e6aa9d0072b240a) | [getUIStrings](../../d9/d53/namespaceAttacherGui.html#a4633c8769798583ed5a439779508c2cc) ([Base::Type](../../dc/dee/classBase_1_1Type.html) attacherType, [Attacher::eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) mmode)  
| getUIStrings
[More...](../../d9/d53/namespaceAttacherGui.html#a4633c8769798583ed5a439779508c2cc)  
  
[TextSet](../../d9/d53/namespaceAttacherGui.html#a04587e69dfb8e24b0e6aa9d0072b240a) | [TwoStrings](../../d9/d53/namespaceAttacherGui.html#a47c5505b5b9b53ea5c914e59625829d8) (QString str1, QString str2)  
  
##  Variables  
  
---  
struct {  
const char *
[AttacherGui::comment](../../d9/d53/namespaceAttacherGui.html#a0ae82ee39005cf664b1d82d445872cd0)  
const char *
[AttacherGui::txt](../../d9/d53/namespaceAttacherGui.html#a52a2f6bec391e10d28977fca2540d6ca)  
} | [eRefTypeStrings](../../d9/d53/namespaceAttacherGui.html#aeeeb7a60f149f33103f64685dab1d0e8) []  
  
## Detailed Description

AttacherTexts.h, .cpp - files that contain user-friendly translatable names of
attachment modes, as well as help texts, and the like.

## Typedef Documentation

## ◆ TextSet

typedef std::vector<QString>
[AttacherGui::TextSet](../../d9/d53/namespaceAttacherGui.html#a04587e69dfb8e24b0e6aa9d0072b240a)  
---  
  
## Function Documentation

## ◆ getRefListForMode()

QStringList PartGuiExport AttacherGui::getRefListForMode  | ( | [AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html) & | _attacher_ ,   
---|---|---|---  
|  | [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) | _mmode_  
| ) | |   
  
References
[getShapeTypeText()](../../d9/d53/namespaceAttacherGui.html#a068550542e3bc24e606c15b9beebf2ad),
and
[Attacher::AttachEngine::modeRefTypes](../../d2/d85/classAttacher_1_1AttachEngine.html#ad17d478d795b1c623547f08be6fcb438).

## ◆ getShapeTypeText()

QString PartGuiExport AttacherGui::getShapeTypeText  | ( | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) | _type_| ) |   
---|---|---|---|---|---  
  
References
[comment](../../d9/d53/namespaceAttacherGui.html#a0ae82ee39005cf664b1d82d445872cd0),
[eRefTypeStrings](../../d9/d53/namespaceAttacherGui.html#aeeeb7a60f149f33103f64685dab1d0e8),
[Attacher::rtDummy_numberOfShapeTypes](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a98ce104efe7501c0a4f2d6e6ff4486a9),
[Attacher::rtFlagHasPlacement](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738ae063749f0a203938e8d6fae4906de6f6),
and
[txt](../../d9/d53/namespaceAttacherGui.html#a52a2f6bec391e10d28977fca2540d6ca).

Referenced by
[getRefListForMode()](../../d9/d53/namespaceAttacherGui.html#a23410823e9ff27aa82b030d72d3d6d42),
and
[AttacherGui::AttacherGuiPy::sGetRefTypeUserFriendlyName()](../../d9/d27/classAttacherGui_1_1AttacherGuiPy.html#a6e25d5bdd5122a487a6be9de84085ded).

## ◆ getUIStrings()

[TextSet](../../d9/d53/namespaceAttacherGui.html#a04587e69dfb8e24b0e6aa9d0072b240a) PartGuiExport AttacherGui::getUIStrings  | ( | [Base::Type](../../dc/dee/classBase_1_1Type.html) | _attacherType_ ,   
---|---|---|---  
|  | [Attacher::eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) | _mmode_  
| ) | |   
  
getUIStrings

Parameters

     attacherType|   
---|---  
mmode|  
  
Returns

    vector of two QStrings: first is the name of attachment mode. e.g. "Tangent to surface"; second is tooltip-style explanation of the mode, like "Plane is tangent to a surface at vertex." 

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::Type::getName()](../../dc/dee/classBase_1_1Type.html#a861a2f6bd2cd2c2df7846e202f0ce137),
[Base::Type::isDerivedFrom()](../../dc/dee/classBase_1_1Type.html#abb24fc578ec80e158584f46d4a5042c7),
[Attacher::mm0CenterOfCurvature](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82ad0e25262e6c9be292384e12970ca1bf0),
[Attacher::mm0CenterOfMass](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a4794e735aed469729e1000d083e220f2),
[Attacher::mm0Focus1](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a4d57898ccd1632b1a8c9ceadfa1e0146),
[Attacher::mm0Focus2](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aa2e56b95cb3c3ccef07e0a79612a745f),
[Attacher::mm0Intersection](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a8840a551b0753a0beba2565d7ceb1cd7),
[Attacher::mm0OnEdge](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aa1c2019a9f0d65810bebc17b45d416fd),
[Attacher::mm0Origin](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a2c7dac902620e661bfc07e1c99096742),
[Attacher::mm0ProximityPoint1](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a3cbda25e90b22477456a283c824626b0),
[Attacher::mm0ProximityPoint2](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a7c3d38e7c48a269e61cad65c66270019),
[Attacher::mm0Vertex](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a75fe35ee7d57ed5f399620d1ff9d96b9),
[Attacher::mm1Asymptote1](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a1830e6bd30b259c3e09e8bec7fc961a2),
[Attacher::mm1Asymptote2](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a468b71c251416a433d5135bc14bec350),
[Attacher::mm1AxisCurv](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a0f5d52243b69fd9cf217bded0ca5957e),
[Attacher::mm1AxisInertia1](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a7687df1936877203cbc504d22b6df129),
[Attacher::mm1AxisInertia2](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a94db15079d83ecc9b47b80b95513bbac),
[Attacher::mm1AxisInertia3](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aea76d95230aaf8424249dddbf6a9e405),
[Attacher::mm1AxisX](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a1548f8c192885740d2b018a0b5d3b35c),
[Attacher::mm1AxisY](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a1f3002d821b77453255f665726becef7),
[Attacher::mm1AxisZ](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82acc2626ccab190da4a20386880af2f611),
[Attacher::mm1Binormal](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a1a0aebceeeae94cc735c8018927d57e2),
[Attacher::mm1Directrix1](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82ab5ba3de2d974d5cddf958e4a2ba39a41),
[Attacher::mm1Directrix2](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aaa47696cc543467c442383b63f7f1c43),
[Attacher::mm1FaceNormal](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a4b3ef847e6122d8c88fde034b5fe3e08),
[Attacher::mm1Intersection](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aa063b849c4abf90b4831a32d9429375e),
[Attacher::mm1Normal](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a0d5e1870ceb2e55087defa6ddc474953),
[Attacher::mm1Proximity](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a84503c2a1ba1fa102ed06f9cc408e32d),
[Attacher::mm1Tangent](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a4aeb856b3485bcf7ce5a51f93ed1357c),
[Attacher::mm1TangentU](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aeac3322168ba3478932b471d556c14df),
[Attacher::mm1TangentV](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a9a78fcce8b0921609d2845398287fa5d),
[Attacher::mm1TwoPoints](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82ac6c7837dd6e14bfad8514aa5a144a31d),
[Attacher::mmConcentric](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a035372810e0f68d8711d723cf8f9c0f5),
[Attacher::mmDeactivated](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82abc8bf0ab13257ac3324c75d4fd9f7d12),
[Attacher::mmFlatFace](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82af8af2848130f8ac142620cf912d8755f),
[Attacher::mmFolding](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a0e4132f968fb6039d56652a651c385c3),
[Attacher::mmFrenetNB](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a50b6a19efd009bf18abcfca10f34c8e8),
[Attacher::mmFrenetTB](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a130683fb8ad0f2a97fdc18d2a6fa4352),
[Attacher::mmFrenetTN](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a8ddde32b5f399cc8a8814f92e3293185),
[Attacher::mmInertialCS](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a7758a2d618e7938555ff085e0dfbd65e),
[Attacher::mmNormalToPath](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a947e8fd0cc9ab519e9923be64d75f4f1),
[Attacher::mmObjectXY](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a5d105247b9d3f4167adf890dc464f0bf),
[Attacher::mmObjectXZ](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a0c22d6d5383ce07e9b10450f07119f64),
[Attacher::mmObjectYZ](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a9a91069f17c58d38f77e3a5e9ddf817c),
[Attacher::mmOXY](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a65c971cc68fd949545cbf3a9cb1edb9e),
[Attacher::mmOXZ](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a1dbb562d93bd7ddba16bc84df4cdee0d),
[Attacher::mmOYX](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aa15f1cadb9e13e1975d213c5edbafa85),
[Attacher::mmOYZ](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a5628ce4452926044a8fede0a1c03e7a9),
[Attacher::mmOZX](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a038e1a6e263274e2492e4fbae093e611),
[Attacher::mmOZY](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82af9571f560687d2f0f477cf20527f549f),
[Attacher::mmRevolutionSection](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a66814148fbb488e008f2a1f0af13a02d),
[Attacher::mmTangentPlane](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a9f35a684358e8f1a6829fef8bc880d21),
[Attacher::mmThreePointsNormal](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aba0c0455ce5850e81f64a2b42ad42060),
[Attacher::mmThreePointsPlane](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aa8bc48b94a4fb97f6d68dd798b9c6430),
[Attacher::mmTranslate](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a41cfa0fb8ec599584a182588516a499c),
[TwoStrings()](../../d9/d53/namespaceAttacherGui.html#a47c5505b5b9b53ea5c914e59625829d8),
and
[Base::ConsoleSingleton::Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

Referenced by
[AttacherGui::AttacherGuiPy::sGetModeStrings()](../../d9/d27/classAttacherGui_1_1AttacherGuiPy.html#a8fc6f693da46263c05484d0b874ff294).

## ◆ TwoStrings()

[TextSet](../../d9/d53/namespaceAttacherGui.html#a04587e69dfb8e24b0e6aa9d0072b240a) AttacherGui::TwoStrings  | ( | QString  | _str1_ ,   
---|---|---|---  
|  | QString  | _str2_  
| ) | |   
  
Referenced by
[getUIStrings()](../../d9/d53/namespaceAttacherGui.html#a4633c8769798583ed5a439779508c2cc).

## Variable Documentation

## ◆ comment

const char* AttacherGui::comment  
---  
  
Referenced by
[getShapeTypeText()](../../d9/d53/namespaceAttacherGui.html#a068550542e3bc24e606c15b9beebf2ad).

## ◆

struct { ... } AttacherGui::eRefTypeStrings[]  
---  
  
**Initial value:**

= {

QT_TRANSLATE_NOOP3("Attacher", "Any", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Vertex", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Edge", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Face", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Line", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Curve", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Circle", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Conic", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Ellipse", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Parabola", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Hyperbola", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Plane", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Sphere", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Revolve", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Cylinder", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Torus", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Cone", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Object", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Solid", "Attacher reference type"),

QT_TRANSLATE_NOOP3("Attacher", "Wire", "Attacher reference type"),

{nullptr, nullptr},

{nullptr, nullptr},

{nullptr, nullptr}

}

Referenced by
[getShapeTypeText()](../../d9/d53/namespaceAttacherGui.html#a068550542e3bc24e606c15b9beebf2ad).

## ◆ txt

const char* AttacherGui::txt  
---  
  
Referenced by
[getShapeTypeText()](../../d9/d53/namespaceAttacherGui.html#a068550542e3bc24e606c15b9beebf2ad).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

