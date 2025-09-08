---
url: https://freecad.github.io/SourceDoc/d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html
scraped_at: 2025-09-08T14:55:14.622228
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)
  * [ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html)

[List of all members](../../dd/df5/structApp_1_1ObjectIdentifier_1_1ResolveResults-members.html) | Public Member Functions | Public Attributes

App::ObjectIdentifier::ResolveResults Struct Reference

`#include <ObjectIdentifier.h>`

##  Public Member Functions  
  
---  
void | [getProperty](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a6cdae993b6aead3910694b1b6bc3c866) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &oi)  
std::string | [resolveErrorString](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ab5f56590f87b6dbf5f3b3e610e08f2b8) () const  
|
[ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ac68d2770dbaa3768a52327848a0fad41)
(const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &oi)  
| Construct and initialize a
[ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html)
object, given an
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) instance.
[More...](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ac68d2770dbaa3768a52327848a0fad41)  
  
  
##  Public Attributes  
  
---  
std::bitset< 32 > | [flags](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aa10a3243feddcb1bbc55206d09c8a016)  
[int](../../d1/da0/classint.html) | [propertyIndex](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a068329372c72559cc628c71c4b6e1035)  
std::string | [propertyName](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a43b1f13706450b0cb1344c1aab70e8d9)  
[int](../../d1/da0/classint.html) | [propertyType](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a4a562c0f1a5d62d4e4eacc75d8fde46f)  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [resolvedDocument](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ab75d5ea9ec179f8eaad81531325f15c3)  
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | [resolvedDocumentName](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aa89b20df1e8259f4a2c894718722980a)  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [resolvedDocumentObject](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a75f904af9d27c4e217e770d631b6bff7)  
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | [resolvedDocumentObjectName](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ad48dd81380d0620942822e0769064bcd)  
[App::Property](../../d0/da9/classApp_1_1Property.html) * | [resolvedProperty](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aed491da2fa165a239384e218f652f500)  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [resolvedSubObject](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a881b7ed3fb003986669471252d1da082)  
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | [subObjectName](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aa5013797852c67c1750195f9512e85e5)  
  
## Constructor & Destructor Documentation

## ◆ ResolveResults()

ObjectIdentifier::ResolveResults::ResolveResults  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _oi_| ) |   
---|---|---|---|---|---  
  
Construct and initialize a
[ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html)
object, given an
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) instance.

The constructor will invoke the
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)'s
[resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed
"Resolve the object identifier to a concrete document, documentobject, and
property.") method to initialize the object's data.

References
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## Member Function Documentation

## ◆ getProperty()

void ObjectIdentifier::ResolveResults::getProperty  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _oi_| ) |   
---|---|---|---|---|---  
  
References
[App::ObjectIdentifier::resolveProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9341d67d505f43d14f829d379ffed02e).

Referenced by
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ resolveErrorString()

std::string ObjectIdentifier::ResolveResults::resolveErrorString  | ( | | ) |  const  
---|---|---|---|---  
  
References
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[App::ObjectIdentifier::subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36),
and
[App::ObjectIdentifier::String::toString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a7609abad389a5b852573213fd66a491f).

## Member Data Documentation

## ◆ flags

std::bitset<32> App::ObjectIdentifier::ResolveResults::flags  
---  
  
Referenced by
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ propertyIndex

[int](../../d1/da0/classint.html)
App::ObjectIdentifier::ResolveResults::propertyIndex  
---  
  
Referenced by
[App::ObjectIdentifier::getPyValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a51896520089a0ba883333f2a6bcb56c6),
[App::ObjectIdentifier::getValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c),
[App::ObjectIdentifier::relativeTo()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af3818694d759d01636c69ca3ba6203ad),
and
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ propertyName

std::string App::ObjectIdentifier::ResolveResults::propertyName  
---  
  
Referenced by
[PathScripts.PathSetupSheetGui.OpTaskPanel::accept()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#abf41762321cdf0582942161477eba1da),
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
and
[PathScripts.PathSetupSheetGui.OpTaskPanel::setupUi()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a03e427ec6574bd249d859f5bd2496576).

## ◆ propertyType

[int](../../d1/da0/classint.html)
App::ObjectIdentifier::ResolveResults::propertyType  
---  
  
Referenced by
[App::ObjectIdentifier::getPyValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a51896520089a0ba883333f2a6bcb56c6),
[App::ObjectIdentifier::getValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c),
[PathScripts.PathPropertyBagGui.PropertyCreate::propertyIsEnumeration()](../../dd/d6e/classPathScripts_1_1PathPropertyBagGui_1_1PropertyCreate.html#af395a1d9ff86d449c86c84581e94d0ea),
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
and
[App::ObjectIdentifier::setValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a208a7e99d236e98ca3e6165ce858480b).

## ◆ resolvedDocument

[App::Document](../../d8/d3e/classApp_1_1Document.html)*
App::ObjectIdentifier::ResolveResults::resolvedDocument  
---  
  
Referenced by
[App::ObjectIdentifier::relativeTo()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af3818694d759d01636c69ca3ba6203ad),
and
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ resolvedDocumentName

[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)
App::ObjectIdentifier::ResolveResults::resolvedDocumentName  
---  
  
Referenced by
[App::ObjectIdentifier::relativeTo()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af3818694d759d01636c69ca3ba6203ad),
and
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ resolvedDocumentObject

[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*
App::ObjectIdentifier::ResolveResults::resolvedDocumentObject  
---  
  
Referenced by
[App::ObjectIdentifier::relativeTo()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af3818694d759d01636c69ca3ba6203ad),
and
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ resolvedDocumentObjectName

[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)
App::ObjectIdentifier::ResolveResults::resolvedDocumentObjectName  
---  
  
Referenced by
[App::ObjectIdentifier::relativeTo()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af3818694d759d01636c69ca3ba6203ad),
and
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ resolvedProperty

[App::Property](../../d0/da9/classApp_1_1Property.html)*
App::ObjectIdentifier::ResolveResults::resolvedProperty  
---  
  
Referenced by
[App::ObjectIdentifier::getPyValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a51896520089a0ba883333f2a6bcb56c6),
[App::ObjectIdentifier::getValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c),
and
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ resolvedSubObject

[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*
App::ObjectIdentifier::ResolveResults::resolvedSubObject  
---  
  
Referenced by
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ subObjectName

[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)
App::ObjectIdentifier::ResolveResults::subObjectName  
---  
  
Referenced by
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/App/ObjectIdentifier.h
  * FreeCAD/src/App/ObjectIdentifier.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

