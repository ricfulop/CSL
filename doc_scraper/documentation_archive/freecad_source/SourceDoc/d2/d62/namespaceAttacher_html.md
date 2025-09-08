---
url: https://freecad.github.io/SourceDoc/d2/d62/namespaceAttacher.html
scraped_at: 2025-09-08T14:58:42.442033
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Typedefs | Enumerations

Attacher Namespace Reference

Attacher.h, Attacher.cpp contain the functionality of deriving placement from
a set of geometric subelements.
[More...](../../d2/d62/namespaceAttacher.html#details)

##  Classes  
  
---  
class | [AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html)  
| The [AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html "The
AttachEngine class is the placement calculation routine, modes, hints and so
on.") class is the placement calculation routine, modes, hints and so on.
[More...](../../d2/d85/classAttacher_1_1AttachEngine.html#details)  
  
class | [AttachEngine3D](../../d1/db7/classAttacher_1_1AttachEngine3D.html)  
class | [AttachEngineLine](../../dc/dd1/classAttacher_1_1AttachEngineLine.html)  
class | [AttachEnginePlane](../../d9/d34/classAttacher_1_1AttachEnginePlane.html)  
class | [AttachEnginePoint](../../d8/df8/classAttacher_1_1AttachEnginePoint.html)  
class | [ExceptionCancel](../../d6/dd2/classAttacher_1_1ExceptionCancel.html)  
struct | [SuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html)  
| The [SuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html "The
SuggestResult struct is a container for output information of AttachEngine
mode suggesting routin...") struct is a container for output information of
[AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html "The
AttachEngine class is the placement calculation routine, modes, hints and so
on.") mode suggesting routine.
[More...](../../d6/d4f/structAttacher_1_1SuggestResult.html#details)  
  
  
##  Typedefs  
  
---  
typedef std::vector< [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) > | [refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849)  
typedef std::vector< [refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) > | [refTypeStringList](../../d2/d62/namespaceAttacher.html#a1e956a433ed003aff07cf368d39f79ba)  
  
##  Enumerations  
  
---  
enum | [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) {   
[mmDeactivated](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82abc8bf0ab13257ac3324c75d4fd9f7d12)
,
[mmTranslate](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a41cfa0fb8ec599584a182588516a499c)
,
[mmObjectXY](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a5d105247b9d3f4167adf890dc464f0bf)
,
[mmObjectXZ](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a0c22d6d5383ce07e9b10450f07119f64)
,  
[mmObjectYZ](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a9a91069f17c58d38f77e3a5e9ddf817c)
,
[mmFlatFace](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82af8af2848130f8ac142620cf912d8755f)
,
[mmTangentPlane](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a9f35a684358e8f1a6829fef8bc880d21)
,
[mmNormalToPath](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a947e8fd0cc9ab519e9923be64d75f4f1)
,  
[mmFrenetNB](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a50b6a19efd009bf18abcfca10f34c8e8)
,
[mmFrenetTN](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a8ddde32b5f399cc8a8814f92e3293185)
,
[mmFrenetTB](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a130683fb8ad0f2a97fdc18d2a6fa4352)
,
[mmConcentric](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a035372810e0f68d8711d723cf8f9c0f5)
,  
[mmRevolutionSection](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a66814148fbb488e008f2a1f0af13a02d)
,
[mmThreePointsPlane](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aa8bc48b94a4fb97f6d68dd798b9c6430)
,
[mmThreePointsNormal](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aba0c0455ce5850e81f64a2b42ad42060)
,
[mmFolding](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a0e4132f968fb6039d56652a651c385c3)
,  
[mm1AxisX](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a1548f8c192885740d2b018a0b5d3b35c)
,
[mm1AxisY](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a1f3002d821b77453255f665726becef7)
,
[mm1AxisZ](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82acc2626ccab190da4a20386880af2f611)
,
[mm1AxisCurv](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a0f5d52243b69fd9cf217bded0ca5957e)
,  
[mm1Directrix1](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82ab5ba3de2d974d5cddf958e4a2ba39a41)
,
[mm1Directrix2](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aaa47696cc543467c442383b63f7f1c43)
,
[mm1Asymptote1](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a1830e6bd30b259c3e09e8bec7fc961a2)
,
[mm1Asymptote2](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a468b71c251416a433d5135bc14bec350)
,  
[mm1Tangent](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a4aeb856b3485bcf7ce5a51f93ed1357c)
,
[mm1Normal](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a0d5e1870ceb2e55087defa6ddc474953)
,
[mm1Binormal](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a1a0aebceeeae94cc735c8018927d57e2)
,
[mm1TangentU](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aeac3322168ba3478932b471d556c14df)
,  
[mm1TangentV](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a9a78fcce8b0921609d2845398287fa5d)
,
[mm1TwoPoints](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82ac6c7837dd6e14bfad8514aa5a144a31d)
,
[mm1Intersection](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aa063b849c4abf90b4831a32d9429375e)
,
[mm1Proximity](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a84503c2a1ba1fa102ed06f9cc408e32d)
,  
[mm0Origin](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a2c7dac902620e661bfc07e1c99096742)
,
[mm0Focus1](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a4d57898ccd1632b1a8c9ceadfa1e0146)
,
[mm0Focus2](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aa2e56b95cb3c3ccef07e0a79612a745f)
,
[mm0OnEdge](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aa1c2019a9f0d65810bebc17b45d416fd)
,  
[mm0CenterOfCurvature](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82ad0e25262e6c9be292384e12970ca1bf0)
,
[mm0CenterOfMass](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a4794e735aed469729e1000d083e220f2)
,
[mm0Intersection](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a8840a551b0753a0beba2565d7ceb1cd7)
,
[mm0Vertex](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a75fe35ee7d57ed5f399620d1ff9d96b9)
,  
[mm0ProximityPoint1](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a3cbda25e90b22477456a283c824626b0)
,
[mm0ProximityPoint2](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a7c3d38e7c48a269e61cad65c66270019)
,
[mm1AxisInertia1](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a7687df1936877203cbc504d22b6df129)
,
[mm1AxisInertia2](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a94db15079d83ecc9b47b80b95513bbac)
,  
[mm1AxisInertia3](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aea76d95230aaf8424249dddbf6a9e405)
,
[mmInertialCS](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a7758a2d618e7938555ff085e0dfbd65e)
,
[mm1FaceNormal](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a4b3ef847e6122d8c88fde034b5fe3e08)
,
[mmOZX](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a038e1a6e263274e2492e4fbae093e611)
,  
[mmOZY](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82af9571f560687d2f0f477cf20527f549f)
,
[mmOXY](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a65c971cc68fd949545cbf3a9cb1edb9e)
,
[mmOXZ](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a1dbb562d93bd7ddba16bc84df4cdee0d)
,
[mmOYZ](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a5628ce4452926044a8fede0a1c03e7a9)
,  
[mmOYX](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82aa15f1cadb9e13e1975d213c5edbafa85)
,
[mmDummy_NumberOfModes](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82a37e43c9399a491fc43e9cc24a84fe7ec)  
}  
enum | [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) {   
[rtAnything](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7dd1102755b58238cc225e81005bfa57)
,
[rtVertex](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738aa5f9a31dffdc2f9dfdc6b8ca231d19c6)
,
[rtEdge](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a80465fa5307ae1503bbdf08ab0aa55b3)
,
[rtFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7f4ce91f652aada5d77a26d7503ab56c)
,  
[rtLine](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a605a5d2b20587133d59bac87dcb5bdaf)
,
[rtCurve](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a779b0d75fa4a0665cdf2bf370c8fef49)
,
[rtCircle](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a5ef28220d2bbc64118e291de7a3002bc)
,
[rtConic](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a60e58cadaba8ad9f34525bac7cd0cdae)
,  
[rtEllipse](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738af90593d78196f13888d5896c22402180)
,
[rtParabola](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738aa14d8a88277d9adc6e12f7b713414f1b)
,
[rtHyperbola](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a0883a5675ecccbb9319269711780fa47)
,
[rtFlatFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a6d6eaaa2c32936e59155ccf7c73a5a30)
,  
[rtSphericalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738aa427b3720abf0d02da26c259aefbf51e)
,
[rtSurfaceRev](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a29a3eb150ccf5342a0599d32e093b190)
,
[rtCylindricalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738adca16f64a04f699cded8fd8872b355df)
,
[rtToroidalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a38952bba064d1de310d0d5dcbd655f7d)
,  
[rtConicalFace](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a4a7c3c2a81920a940e12200352874bb5)
,
[rtPart](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738ad506738ccf8a39328354da3ab61e5399)
,
[rtSolid](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738add0a306d000e83a436ad4e1ca1ce3bcf)
,
[rtWire](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a7e192c84329dfdb3be167e6ca3580497)
,  
[rtDummy_numberOfShapeTypes](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738a98ce104efe7501c0a4f2d6e6ff4486a9)
,
[rtFlagHasPlacement](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738ae063749f0a203938e8d6fae4906de6f6)
= 0x0100  
}  
| The eRefType enum lists the types of references.
[More...](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738)  
  
  
## Detailed Description

Attacher.h, Attacher.cpp contain the functionality of deriving placement from
a set of geometric subelements.

Examples are: sketch attachment, datum plane placement.

## Typedef Documentation

## ◆ refTypeString

typedef
std::vector<[eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738)>
[Attacher::refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849)  
---  
  
## ◆ refTypeStringList

typedef
std::vector<[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849)>
[Attacher::refTypeStringList](../../d2/d62/namespaceAttacher.html#a1e956a433ed003aff07cf368d39f79ba)  
---  
  
## Enumeration Type Documentation

## ◆ eMapMode

enum
[Attacher::eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82)  
---  
  
Enumerator  
---  
mmDeactivated |   
mmTranslate |   
mmObjectXY |   
mmObjectXZ |   
mmObjectYZ |   
mmFlatFace |   
mmTangentPlane |   
mmNormalToPath |   
mmFrenetNB |   
mmFrenetTN |   
mmFrenetTB |   
mmConcentric |   
mmRevolutionSection |   
mmThreePointsPlane |   
mmThreePointsNormal |   
mmFolding |   
mm1AxisX |   
mm1AxisY |   
mm1AxisZ |   
mm1AxisCurv |   
mm1Directrix1 |   
mm1Directrix2 |   
mm1Asymptote1 |   
mm1Asymptote2 |   
mm1Tangent |   
mm1Normal |   
mm1Binormal |   
mm1TangentU |   
mm1TangentV |   
mm1TwoPoints |   
mm1Intersection |   
mm1Proximity |   
mm0Origin |   
mm0Focus1 |   
mm0Focus2 |   
mm0OnEdge |   
mm0CenterOfCurvature |   
mm0CenterOfMass |   
mm0Intersection |   
mm0Vertex |   
mm0ProximityPoint1 |   
mm0ProximityPoint2 |   
mm1AxisInertia1 |   
mm1AxisInertia2 |   
mm1AxisInertia3 |   
mmInertialCS |   
mm1FaceNormal |   
mmOZX |   
mmOZY |   
mmOXY |   
mmOXZ |   
mmOYZ |   
mmOYX |   
mmDummy_NumberOfModes |   
  
## ◆ eRefType

enum
[Attacher::eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738)  
---  
  
The eRefType enum lists the types of references.

If adding one, see also
[AttachEngine::eRefTypeStrings](../../d2/d85/classAttacher_1_1AttachEngine.html#a32f23fd69b09ea00c6811ce532464d44),
[AttachEngine::getShapeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#ad79155676af730dce23e51110b9e8d75
"getShapeType by shape."),
[AttachEngine::downgradeType()](../../d2/d85/classAttacher_1_1AttachEngine.html#a33503fd1ae1a48d6def706cd9619d53b
"downgradeType converts a more-specific type into a less-specific type
\(e.g."), AttacherTexts.cpp/getShTypeText()

Enumerator  
---  
rtAnything |   
rtVertex |   
rtEdge |   
rtFace |   
rtLine |   
rtCurve |   
rtCircle |   
rtConic |   
rtEllipse |   
rtParabola |   
rtHyperbola |   
rtFlatFace |   
rtSphericalFace |   
rtSurfaceRev |   
rtCylindricalFace |   
rtToroidalFace |   
rtConicalFace |   
rtPart |   
rtSolid |   
rtWire |   
rtDummy_numberOfShapeTypes |   
rtFlagHasPlacement |   
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

