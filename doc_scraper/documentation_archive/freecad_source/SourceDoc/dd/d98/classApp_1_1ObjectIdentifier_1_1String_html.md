---
url: https://freecad.github.io/SourceDoc/dd/d98/classApp_1_1ObjectIdentifier_1_1String.html
scraped_at: 2025-09-08T14:55:15.621063
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)
  * [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)

[List of all members](../../d9/d33/classApp_1_1ObjectIdentifier_1_1String-members.html) | Public Member Functions | Friends

App::ObjectIdentifier::String Class Reference

`#include <ObjectIdentifier.h>`

##  Public Member Functions  
  
---  
void | [checkImport](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a8c71508a5ae7a8b7387e35abe09dac6f) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090), const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj=nullptr, [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) *objName=nullptr)  
|
[FC_DEFAULT_CTORS](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a7691f0d9365d5c72fbfbf9a945b3e857)
([String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html))  
const std::string & | [getString](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b) () const  
| Returns the string.
[More...](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b)  
  
[bool](../../d9/db9/classbool.html) | [isForceIdentifier](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a32064d2f8a40ae9d4965cc8893ee8563) () const  
[bool](../../d9/db9/classbool.html) | [isRealString](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ab39f355cd6d30feb9bae70fecdb63b18) () const  
| Return true is string need to be quoted.
[More...](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ab39f355cd6d30feb9bae70fecdb63b18)  
  
| [operator const char
*](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a7cf16491d793317e610973ab4fc1f3fb)
() const  
| [operator
std::string](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a2ac760305c4fb2c42661423258096575)
() const  
[bool](../../d9/db9/classbool.html) | [operator!=](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9777c2dece53621214f4e8c9ba224944) (const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &other) const  
[bool](../../d9/db9/classbool.html) | [operator<](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a6c3d26d04650e5094f9dd6f89fa9f7ed) (const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &other) const  
[bool](../../d9/db9/classbool.html) | [operator==](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ad37abe743a62b02f00734cbd5853726e) (const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &other) const  
[bool](../../d9/db9/classbool.html) | [operator>](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ad64ed66f7cced5d00dca6ecd1c5f4ce7) (const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &other) const  
[bool](../../d9/db9/classbool.html) | [operator>=](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a3ba634c769ae9216c8537ec622c01417) (const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &other) const  
|
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#aabcac67f2dc026d76620cc9561e1269d)
(const std::string &s="", [bool](../../d9/db9/classbool.html)
_isRealString=false, [bool](../../d9/db9/classbool.html)
_forceIdentifier=false)  
|
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a2a4f7a643fb518c4079b35ea10675949)
(std::string &&s, [bool](../../d9/db9/classbool.html) _isRealString=false,
[bool](../../d9/db9/classbool.html) _forceIdentifier=false)  
std::string | [toString](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a7609abad389a5b852573213fd66a491f) ([bool](../../d9/db9/classbool.html) toPython=false) const  
| Returns a possibly quoted string.
[More...](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a7609abad389a5b852573213fd66a491f)  
  
  
##  Friends  
  
---  
class | [ObjectIdentifier](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a33910ad2ce88bf67e7e0e97f08c9d5d2)  
  
## Constructor & Destructor Documentation

## ◆ String() [1/2]

App::ObjectIdentifier::String::String  | ( | const std::string & | _s_ = `""`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | __isRealString_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | __forceIdentifier_ = `false`  
| ) | |   
  
## ◆ String() [2/2]

App::ObjectIdentifier::String::String  | ( | std::string && | _s_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | __isRealString_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | __forceIdentifier_ = `false`  
| ) | |   
  
## Member Function Documentation

## ◆ checkImport()

void ObjectIdentifier::String::checkImport  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _owner_ ,   
---|---|---|---  
|  | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ = `nullptr`,   
|  | [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) *  | _objName_ = `nullptr`  
| ) | |   
  
References
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::ObjectIdentifier::getDocumentObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a76e0d3d2cbbf5db98d33a9d0917a15ff),
[App::Document::getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
[App::PropertyLinkBase::importSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e),
[App::ObjectIdentifier::owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[App::ExpressionParser::ExpressionImporter::reader()](../../db/df3/classApp_1_1ExpressionParser_1_1ExpressionImporter.html#ad06fb4d46a2ab90d878544f943719304),
[App::PropertyLinkBase::restoreLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb),
and
[toString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a7609abad389a5b852573213fd66a491f).

## ◆ FC_DEFAULT_CTORS()

App::ObjectIdentifier::String::FC_DEFAULT_CTORS  | ( | [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | | ) |   
---|---|---|---|---|---  
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ getString()

const std::string & App::ObjectIdentifier::String::getString  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the string.

Referenced by
[App::ObjectIdentifier::access()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe357711ff3adc68e0a69cbad332a4eb),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[App::ObjectIdentifier::getDepLabels()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2d8af8b84a0c426af896a2f190b692ce),
[App::ObjectIdentifier::getPropertyComponents()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a57264281085e983af84c5dbbfd5871e0),
[App::ObjectIdentifier::getStringList()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8870022fd22c692772be62dd0157b6a7),
[App::ObjectIdentifier::getSubObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1111706c4bc3efd238f0066c4226421b),
[App::ObjectIdentifier::hasDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a58b1475c362d8f38085e711911d2fb4e),
[App::ObjectIdentifier::importSubNames()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954),
[App::ObjectIdentifier::relabeledDocument()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab762f0b511088f1aad35a265a16bf5bc),
[App::ObjectIdentifier::replaceObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a80caff359bff231c8a61c0a77bda725f),
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
[App::ObjectIdentifier::resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f),
[App::ObjectIdentifier::ResolveResults::resolveErrorString()](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ab5f56590f87b6dbf5f3b3e610e08f2b8),
[App::ObjectIdentifier::resolveProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9341d67d505f43d14f829d379ffed02e),
[App::ObjectIdentifier::toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
[App::ObjectIdentifier::toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6),
[App::ObjectIdentifier::updateElementReference()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab8fdf8392daa0dbc35aed2e2d9e90fc3),
and
[App::ObjectIdentifier::updateLabelReference()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8ee527f0da9e9a1d26e8744d048ced67).

## ◆ isForceIdentifier()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::String::isForceIdentifier  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::ObjectIdentifier::resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f),
and
[App::ObjectIdentifier::updateLabelReference()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8ee527f0da9e9a1d26e8744d048ced67).

## ◆ isRealString()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::String::isRealString  | ( | | ) |  const  
---|---|---|---|---  
  
Return true is string need to be quoted.

Referenced by
[App::ObjectIdentifier::getDepLabels()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2d8af8b84a0c426af896a2f190b692ce),
[App::ObjectIdentifier::importSubNames()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954),
[App::ObjectIdentifier::relabeledDocument()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab762f0b511088f1aad35a265a16bf5bc),
[App::ObjectIdentifier::replaceObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a80caff359bff231c8a61c0a77bda725f),
[App::ObjectIdentifier::resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f),
[App::ObjectIdentifier::setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9ae70c738c44b6241add3657ef8af843),
[App::ObjectIdentifier::toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
and
[App::ObjectIdentifier::updateLabelReference()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8ee527f0da9e9a1d26e8744d048ced67).

## ◆ operator const char *()

App::ObjectIdentifier::String::operator const char *  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ operator std::string()

App::ObjectIdentifier::String::operator std::string  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Spreadsheet_legacy.MathParser::hasNext()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a880d2d2a50b45fc7d1a43f93920d7543),
and
[Spreadsheet_legacy.MathParser::peek()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a56d2b8422c194d4440df5d1ae85e04ef).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::String::operator!=  | ( | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator<()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::String::operator< | ( | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator==()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::String::operator==  | ( | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator>()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::String::operator> | ( | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator>=()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::String::operator>=  | ( | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
## ◆ toString()

std::string ObjectIdentifier::String::toString  | ( | [bool](../../d9/db9/classbool.html) | _toPython_ = `false`| ) |  const  
---|---|---|---|---|---  
  
Returns a possibly quoted string.

Get a string representation of this object identifier.

Returns

    [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) representation. 

References
[App::quote()](../../dd/dc2/namespaceApp.html#a841ae9c646da97ed75d34d79bdee5093).

Referenced by
[checkImport()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a8c71508a5ae7a8b7387e35abe09dac6f),
[App::ObjectIdentifier::getStringList()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8870022fd22c692772be62dd0157b6a7),
[App::ObjectIdentifier::ResolveResults::resolveErrorString()](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ab5f56590f87b6dbf5f3b3e610e08f2b8),
[App::ObjectIdentifier::toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
and
[App::ObjectIdentifier::toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

## Friends And Related Function Documentation

## ◆ ObjectIdentifier

| [friend](../../d7/d23/classfriend.html) class
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)  
---  
friend  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ObjectIdentifier.h
  * FreeCAD/src/App/ObjectIdentifier.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

