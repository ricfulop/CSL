---
url: https://freecad.github.io/SourceDoc/dc/d5c/classApp_1_1Expression.html
scraped_at: 2025-09-08T14:54:36.503003
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Expression](../../dc/d5c/classApp_1_1Expression.html)

[List of all members](../../da/d26/classApp_1_1Expression-members.html) | Classes | Public Types | Public Member Functions | Static Public Member Functions | Public Attributes | Protected Attributes

App::Expression Class Referenceabstract

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class for expressions.
[More...](../../dc/d5c/classApp_1_1Expression.html#details)

`#include <Expression.h>`

##  Classes  
  
---  
struct | [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html)  
class | [Exception](../../d1/d66/classApp_1_1Expression_1_1Exception.html)  
  
##  Public Types  
  
---  
typedef std::vector< [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * > | [ComponentList](../../dc/d5c/classApp_1_1Expression.html#ae5c26c23fa1701412faad43c4482332b)  
enum | [DepOption](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74) { [DepNormal](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab030e4fe983000e80dcbe765ca125d5c) , [DepHidden](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab28124d65567e1e919055d51d4d1fd4e) , [DepAll](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74acefbcf98504a7d00a297d5aa59e81f83) }  
  
##  Public Member Functions  
  
---  
virtual void | [addComponent](../../dc/d5c/classApp_1_1Expression.html#a3fa7e813bc2a7840b9e56c1aaea4a276) ([Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) *component)  
[bool](../../d9/db9/classbool.html) | [adjustLinks](../../dc/d5c/classApp_1_1Expression.html#af8dab25510279b4940ec20c5c050005b) (const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList)  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [copy](../../dc/d5c/classApp_1_1Expression.html#a2210f1ec2e2443ff5c328e45efb921fa) () const  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [eval](../../dc/d5c/classApp_1_1Expression.html#aef48bca09d540f5a8b3d41bcfd4dda1d) () const  
|
[Expression](../../dc/d5c/classApp_1_1Expression.html#aa86a31cda60278d865356d6cdcfb9874)
(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)
*_owner)  
void | [getDepObjects](../../dc/d5c/classApp_1_1Expression.html#a1eac6a293066f71fa91fcd7d3915e5d2) (std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, [bool](../../d9/db9/classbool.html) > &, std::vector< std::string > *labels=nullptr) const  
std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, [bool](../../d9/db9/classbool.html) > | [getDepObjects](../../dc/d5c/classApp_1_1Expression.html#ac208fa671cb7877e27de4c7455a5b54d) (std::vector< std::string > *labels=nullptr) const  
void | [getDeps](../../dc/d5c/classApp_1_1Expression.html#aaf7a179b1fd47392d7284d7c89fae870) ([ExpressionDeps](../../dd/dc2/namespaceApp.html#a24de460e732424fd4a8b00cd2a377086) &deps, [int](../../d1/da0/classint.html) option=[DepNormal](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab030e4fe983000e80dcbe765ca125d5c)) const  
[ExpressionDeps](../../dd/dc2/namespaceApp.html#a24de460e732424fd4a8b00cd2a377086) | [getDeps](../../dc/d5c/classApp_1_1Expression.html#abc1ff37d79dc1f8b1f6d005aa9ca5223) ([int](../../d1/da0/classint.html) option=[DepNormal](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab030e4fe983000e80dcbe765ca125d5c)) const  
std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [bool](../../d9/db9/classbool.html) > | [getIdentifiers](../../dc/d5c/classApp_1_1Expression.html#aa4c82c6f4c790b957fe4a5195c665ff3) () const  
void | [getIdentifiers](../../dc/d5c/classApp_1_1Expression.html#ae09856686b038d239e5b5e4ddb5f1217) (std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [bool](../../d9/db9/classbool.html) > &) const  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getOwner](../../dc/d5c/classApp_1_1Expression.html#a0ef3b9243a427d7c1a181ac2ed170a18) () const  
Py::Object | [getPyValue](../../dc/d5c/classApp_1_1Expression.html#ad2bf8c4dd181d646f6bececf47e8e2f4) () const  
boost::any | [getValueAsAny](../../dc/d5c/classApp_1_1Expression.html#afc4d61a7da39a366a5488343ad8155d7) () const  
[bool](../../d9/db9/classbool.html) | [hasComponent](../../dc/d5c/classApp_1_1Expression.html#a59b9dbc3219ff7b4b7ea42c6895e85d4) () const  
[ExpressionPtr](../../dd/dc2/namespaceApp.html#a87d84b6ef4dda5737e574e95320bc07f) | [importSubNames](../../dc/d5c/classApp_1_1Expression.html#a6b338d5ca7344c41547dfe77019cf1e1) (const std::map< std::string, std::string > &nameMap) const  
[bool](../../d9/db9/classbool.html) | [isSame](../../dc/d5c/classApp_1_1Expression.html#a0629cfd92afb2d9aff38fda6d3b30c24) (const [Expression](../../dc/d5c/classApp_1_1Expression.html) &other, [bool](../../d9/db9/classbool.html) checkComment=true) const  
virtual [bool](../../d9/db9/classbool.html) | [isTouched](../../dc/d5c/classApp_1_1Expression.html#ae17d3a0ad8b07160c01a9b55b1844802) () const  
virtual [int](../../d1/da0/classint.html) | [priority](../../dc/d5c/classApp_1_1Expression.html#a4393008057438a9a4df99ad89788bd01) () const  
[ExpressionPtr](../../dd/dc2/namespaceApp.html#a87d84b6ef4dda5737e574e95320bc07f) | [replaceObject](../../dc/d5c/classApp_1_1Expression.html#ae8b79b427cc93dbcb58855e1f8fa3746) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj) const  
virtual [Expression](../../dc/d5c/classApp_1_1Expression.html) * | [simplify](../../dc/d5c/classApp_1_1Expression.html#a1c84dd5e6ffe86c4f720e179859d5ca3) () const =0  
std::string | [toString](../../dc/d5c/classApp_1_1Expression.html#aeeb0fc484ec620affaf4fbd402cc3067) ([bool](../../d9/db9/classbool.html) persistent=false, [bool](../../d9/db9/classbool.html) checkPriority=false, [int](../../d1/da0/classint.html) indent=0) const  
void | [toString](../../dc/d5c/classApp_1_1Expression.html#a2f388147f635590db5c232f9068485e1) (std::ostream &os, [bool](../../d9/db9/classbool.html) persistent=false, [bool](../../d9/db9/classbool.html) checkPriority=false, [int](../../d1/da0/classint.html) indent=0) const  
[ExpressionPtr](../../dd/dc2/namespaceApp.html#a87d84b6ef4dda5737e574e95320bc07f) | [updateLabelReference](../../dc/d5c/classApp_1_1Expression.html#af62b084e6469e8b5bc8f823f53bb68b4) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &ref, const char *newLabel) const  
void | [visit](../../dc/d5c/classApp_1_1Expression.html#a8fab83c92843f933070eec6e5618010d) ([ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html) &v)  
virtual | [~Expression](../../dc/d5c/classApp_1_1Expression.html#a3e99570b177da619eeb2c5787cbb148e) ()  
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
static [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * | [createComponent](../../dc/d5c/classApp_1_1Expression.html#a832fd4778f27454794945d882c9c7518) (const std::string &n)  
static [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * | [createComponent](../../dc/d5c/classApp_1_1Expression.html#af1f60fcdc34ca5c1664977aa50a94f75) ([Expression](../../dc/d5c/classApp_1_1Expression.html) *e1, [Expression](../../dc/d5c/classApp_1_1Expression.html) *e2=nullptr, [Expression](../../dc/d5c/classApp_1_1Expression.html) *e3=nullptr, [bool](../../d9/db9/classbool.html) isRange=false)  
static [Expression](../../dc/d5c/classApp_1_1Expression.html) * | [parse](../../dc/d5c/classApp_1_1Expression.html#a377c20925f92aab0265eb9e3e0b35c97) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *[owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35), const std::string &buffer)  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
  
##  Public Attributes  
  
---  
std::string | [comment](../../dc/d5c/classApp_1_1Expression.html#ae1d5ddb3f258e498436b4ea0d5427a97)  
[friend](../../d7/d23/classfriend.html) | [ExpressionVisitor](../../dc/d5c/classApp_1_1Expression.html#a8152374a586410580356f2b209ebeb10)  
  
##  Protected Attributes  
  
---  
[ComponentList](../../dc/d5c/classApp_1_1Expression.html#ae5c26c23fa1701412faad43c4482332b) | [components](../../dc/d5c/classApp_1_1Expression.html#a1b83ce423e1e318a0af92d193127aacd)  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35)  
| The document object used to access unqualified variables (i.e local scope)
[More...](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class for expressions.

## Member Typedef Documentation

## ◆ ComponentList

typedef
std::vector<[Component](../../d5/df9/structApp_1_1Expression_1_1Component.html)*>
[App::Expression::ComponentList](../../dc/d5c/classApp_1_1Expression.html#ae5c26c23fa1701412faad43c4482332b)  
---  
  
## Member Enumeration Documentation

## ◆ DepOption

enum
[App::Expression::DepOption](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74)  
---  
  
Enumerator  
---  
DepNormal |   
DepHidden |   
DepAll |   
  
## Constructor & Destructor Documentation

## ◆ Expression()

Expression::Expression  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | __owner_| ) |   
---|---|---|---|---|---  
  
## ◆ ~Expression()

| Expression::~Expression  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ addComponent()

| void Expression::addComponent  | ( | [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) *  | _component_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::VariableExpression](../../df/d0f/classApp_1_1VariableExpression.html#a13fe7b9451d199e5b1b2047b48b941a0).

Referenced by
[App::VariableExpression::addComponent()](../../df/d0f/classApp_1_1VariableExpression.html#a13fe7b9451d199e5b1b2047b48b941a0).

## ◆ adjustLinks()

[bool](../../d9/db9/classbool.html) Expression::adjustLinks  | ( | const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _inList_| ) |   
---|---|---|---|---|---  
  
References
[visit()](../../dc/d5c/classApp_1_1Expression.html#a8fab83c92843f933070eec6e5618010d).

Referenced by
[AdjustLinksExpressionVisitor::visit()](../../d2/dfa/classAdjustLinksExpressionVisitor.html#a107aaf772feed375a13a19a9453c7caa).

## ◆ copy()

[Expression](../../dc/d5c/classApp_1_1Expression.html) * Expression::copy  | ( | | ) |  const  
---|---|---|---|---  
  
References
[comment](../../dc/d5c/classApp_1_1Expression.html#ae1d5ddb3f258e498436b4ea0d5427a97),
and
[components](../../dc/d5c/classApp_1_1Expression.html#a1b83ce423e1e318a0af92d193127aacd).

Referenced by
[importSubNames()](../../dc/d5c/classApp_1_1Expression.html#a6b338d5ca7344c41547dfe77019cf1e1),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
[replaceObject()](../../dc/d5c/classApp_1_1Expression.html#ae8b79b427cc93dbcb58855e1f8fa3746),
[App::NumberExpression::simplify()](../../d4/d2a/classApp_1_1NumberExpression.html#a7801a41e631544f7d0d5717c1682beba),
[App::VariableExpression::simplify()](../../df/d0f/classApp_1_1VariableExpression.html#a6c9709ab5ef6619c4cca213517af0a4b),
[App::StringExpression::simplify()](../../d7/dd9/classApp_1_1StringExpression.html#a4dcc77a15b51c648cba8ec3c4d380220),
[App::RangeExpression::simplify()](../../da/d8b/classApp_1_1RangeExpression.html#ac6054f53b78a3a10d6c4c5d908925e09),
and
[updateLabelReference()](../../dc/d5c/classApp_1_1Expression.html#af62b084e6469e8b5bc8f823f53bb68b4).

## ◆ createComponent() [1/2]

| [Expression::Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * Expression::createComponent  | ( | const std::string & | _n_| ) |   
---|---|---|---|---|---  
static  
  
## ◆ createComponent() [2/2]

| [Expression::Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * Expression::createComponent  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _e1_ ,   
---|---|---|---  
|  | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _e2_ = `nullptr`,   
|  | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _e3_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _isRange_ = `false`  
| ) | |   
static  
  
## ◆ eval()

[Expression](../../dc/d5c/classApp_1_1Expression.html) * Expression::eval  | ( | | ) |  const  
---|---|---|---|---  
  
References
[App::expressionFromPy()](../../dd/dc2/namespaceApp.html#ad411837c38675c15be1c469ce9acdbb5),
[getPyValue()](../../dc/d5c/classApp_1_1Expression.html#ad2bf8c4dd181d646f6bececf47e8e2f4),
and
[owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35).

Referenced by
[App::OperatorExpression::simplify()](../../d1/d7d/classApp_1_1OperatorExpression.html#a350f104eaa83275378734a4bc3239ae5),
and
[App::FunctionExpression::simplify()](../../d6/da3/classApp_1_1FunctionExpression.html#a3241421502813b3053a26db4fd247ed3).

## ◆ getDepObjects() [1/2]

void Expression::getDepObjects  | ( | std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, [bool](../../d9/db9/classbool.html) > & | _deps_ ,   
---|---|---|---  
|  | std::vector< std::string > *  | _labels_ = `nullptr`  
| ) | |  const  
  
References
[App::ObjectIdentifier::getDep()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad17db8546af0eff5ebf0bda00c7fd948),
and
[getIdentifiers()](../../dc/d5c/classApp_1_1Expression.html#aa4c82c6f4c790b957fe4a5195c665ff3).

## ◆ getDepObjects() [2/2]

std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, [bool](../../d9/db9/classbool.html) > Expression::getDepObjects  | ( | std::vector< std::string > *  | _labels_ = `nullptr`| ) |  const  
---|---|---|---|---|---  
  
References
[getDepObjects()](../../dc/d5c/classApp_1_1Expression.html#ac208fa671cb7877e27de4c7455a5b54d).

Referenced by
[getDepObjects()](../../dc/d5c/classApp_1_1Expression.html#ac208fa671cb7877e27de4c7455a5b54d).

## ◆ getDeps() [1/2]

void Expression::getDeps  | ( | [ExpressionDeps](../../dd/dc2/namespaceApp.html#a24de460e732424fd4a8b00cd2a377086) & | _deps_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _option_ = `[DepNormal](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab030e4fe983000e80dcbe765ca125d5c)`  
| ) | |  const  
  
References
[DepHidden](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab28124d65567e1e919055d51d4d1fd4e),
[DepNormal](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab030e4fe983000e80dcbe765ca125d5c),
[App::ObjectIdentifier::getDep()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad17db8546af0eff5ebf0bda00c7fd948),
and
[getIdentifiers()](../../dc/d5c/classApp_1_1Expression.html#aa4c82c6f4c790b957fe4a5195c665ff3).

Referenced by
[getDeps()](../../dc/d5c/classApp_1_1Expression.html#abc1ff37d79dc1f8b1f6d005aa9ca5223),
and
[importSubNames()](../../dc/d5c/classApp_1_1Expression.html#a6b338d5ca7344c41547dfe77019cf1e1).

## ◆ getDeps() [2/2]

[ExpressionDeps](../../dd/dc2/namespaceApp.html#a24de460e732424fd4a8b00cd2a377086) Expression::getDeps  | ( | [int](../../d1/da0/classint.html) | _option_ = `[DepNormal](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab030e4fe983000e80dcbe765ca125d5c)`| ) |  const  
---|---|---|---|---|---  
  
References
[getDeps()](../../dc/d5c/classApp_1_1Expression.html#aaf7a179b1fd47392d7284d7c89fae870).

## ◆ getIdentifiers() [1/2]

std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [bool](../../d9/db9/classbool.html) > Expression::getIdentifiers  | ( | | ) |  const  
---|---|---|---|---  
  
References
[getIdentifiers()](../../dc/d5c/classApp_1_1Expression.html#aa4c82c6f4c790b957fe4a5195c665ff3).

Referenced by
[getDepObjects()](../../dc/d5c/classApp_1_1Expression.html#a1eac6a293066f71fa91fcd7d3915e5d2),
[getDeps()](../../dc/d5c/classApp_1_1Expression.html#aaf7a179b1fd47392d7284d7c89fae870),
[getIdentifiers()](../../dc/d5c/classApp_1_1Expression.html#aa4c82c6f4c790b957fe4a5195c665ff3),
[updateLabelReference()](../../dc/d5c/classApp_1_1Expression.html#af62b084e6469e8b5bc8f823f53bb68b4),
and
[GetIdentifiersExpressionVisitor::visit()](../../da/d35/classGetIdentifiersExpressionVisitor.html#ae4e2ee048ae03f3ec98f6e9807dbd7f8).

## ◆ getIdentifiers() [2/2]

void Expression::getIdentifiers  | ( | std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [bool](../../d9/db9/classbool.html) > & | _deps_| ) |  const  
---|---|---|---|---|---  
  
References
[visit()](../../dc/d5c/classApp_1_1Expression.html#a8fab83c92843f933070eec6e5618010d).

## ◆ getOwner()

[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * App::Expression::getOwner  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::FunctionExpression::evaluate()](../../d6/da3/classApp_1_1FunctionExpression.html#aea533bde72fab9803b76f53f0b02aac0).

## ◆ getPyValue()

Py::Object Expression::getPyValue  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[eval()](../../dc/d5c/classApp_1_1Expression.html#aef48bca09d540f5a8b3d41bcfd4dda1d),
[App::FunctionExpression::evaluate()](../../d6/da3/classApp_1_1FunctionExpression.html#aea533bde72fab9803b76f53f0b02aac0),
and
[getValueAsAny()](../../dc/d5c/classApp_1_1Expression.html#afc4d61a7da39a366a5488343ad8155d7).

## ◆ getValueAsAny()

[App::any](../../dd/dc2/namespaceApp.html#a208090b7fcb0b5ccff253a02d5819dd3) Expression::getValueAsAny  | ( | | ) |  const  
---|---|---|---|---  
  
References
[getPyValue()](../../dc/d5c/classApp_1_1Expression.html#ad2bf8c4dd181d646f6bececf47e8e2f4),
and
[App::pyObjectToAny()](../../dd/dc2/namespaceApp.html#ac51cca1568f7ffd55146499492ae1700).

## ◆ hasComponent()

[bool](../../d9/db9/classbool.html) App::Expression::hasComponent  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ importSubNames()

[ExpressionPtr](../../dd/dc2/namespaceApp.html#a87d84b6ef4dda5737e574e95320bc07f) Expression::importSubNames  | ( | const std::map< std::string, std::string > & | _nameMap_| ) |  const  
---|---|---|---|---|---  
  
References
[copy()](../../dc/d5c/classApp_1_1Expression.html#a2210f1ec2e2443ff5c328e45efb921fa),
[DepAll](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74acefbcf98504a7d00a297d5aa59e81f83),
[getDeps()](../../dc/d5c/classApp_1_1Expression.html#aaf7a179b1fd47392d7284d7c89fae870),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35),
and
[App::PropertyLinkBase::tryImportSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a368e7609bf8ee24fd6b574c392e8c6d4).

Referenced by
[ImportSubNamesExpressionVisitor::visit()](../../d9/d49/classImportSubNamesExpressionVisitor.html#a834f8c90120e9e8f51d0028de289d3c8).

## ◆ isSame()

[bool](../../d9/db9/classbool.html) Expression::isSame  | ( | const [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _other_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _checkComment_ = `true`  
| ) | |  const  
  
References
[comment](../../dc/d5c/classApp_1_1Expression.html#ae1d5ddb3f258e498436b4ea0d5427a97),
[Base::BaseClass::getTypeId()](../../df/d4d/classBase_1_1BaseClass.html#addbd3a4f09fce7ce5c6bf021e4c1d566),
and
[toString()](../../dc/d5c/classApp_1_1Expression.html#aeeb0fc484ec620affaf4fbd402cc3067).

## ◆ isTouched()

| virtual [bool](../../d9/db9/classbool.html) App::Expression::isTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::OperatorExpression](../../d1/d7d/classApp_1_1OperatorExpression.html#aa9da888a5ee4fc18cf44a337d7de3824),
[App::ConditionalExpression](../../dc/de5/classApp_1_1ConditionalExpression.html#a30a886bf35a3522fa5031e22d1e6c168),
[App::FunctionExpression](../../d6/da3/classApp_1_1FunctionExpression.html#abadfadf53b3f5d62be639a28aeda4906),
[App::VariableExpression](../../df/d0f/classApp_1_1VariableExpression.html#a30d24a5ccb5a517237ddba1477458080),
and
[App::RangeExpression](../../da/d8b/classApp_1_1RangeExpression.html#a93b55327da44e753b97eca89a2ec8c7c).

Referenced by
[App::ConditionalExpression::isTouched()](../../dc/de5/classApp_1_1ConditionalExpression.html#a30a886bf35a3522fa5031e22d1e6c168).

## ◆ parse()

| [Expression](../../dc/d5c/classApp_1_1Expression.html) * Expression::parse  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _owner_ ,   
---|---|---|---  
|  | const std::string & | _buffer_  
| ) | |   
static  
  
References
[owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35),
and
[App::ExpressionParser::parse()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a9ce0a4421a2d7654d72187f76d5e8874).

Referenced by
[SpreadsheetGui::DlgSheetConf::accept()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#aa4fefe42d2485471443e738600091ce0),
[App::PropertyExpressionEngine::afterRestore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[BOPTools.GeneralFuseResult.GeneralFuseResult::explodeCompounds()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#acaa64b16d29f0065ce1379f8dc572649),
[StdCmdExpression::pasteExpressions()](../../d2/dae/classStdCmdExpression.html#abab137615ab802f7688ff0b623022b9f),
[SpreadsheetGui::DlgSheetConf::prepare()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#abfbeb695362f8ae8074215c61a254de3),
[App::Metadata::satisfies()](../../db/dfe/classApp_1_1Metadata.html#a022c52baf660a45a8870dd2e7042f13c),
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede),
and
[BOPTools.GeneralFuseResult.GeneralFuseResult::splitAggregates()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ac2dd77595b00ad1c612310df00438702).

## ◆ priority()

| [int](../../d1/da0/classint.html) Expression::priority  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reimplemented in
[App::OperatorExpression](../../d1/d7d/classApp_1_1OperatorExpression.html#a2bc8aa32f215cf3d64622e4b4c442148),
and
[App::ConditionalExpression](../../dc/de5/classApp_1_1ConditionalExpression.html#a1916c277039109a57f0ebc38fa5a386d).

Referenced by
[toString()](../../dc/d5c/classApp_1_1Expression.html#a2f388147f635590db5c232f9068485e1).

## ◆ replaceObject()

[ExpressionPtr](../../dd/dc2/namespaceApp.html#a87d84b6ef4dda5737e574e95320bc07f) Expression::replaceObject  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _oldObj_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _newObj_  
| ) | |  const  
  
References
[copy()](../../dc/d5c/classApp_1_1Expression.html#a2210f1ec2e2443ff5c328e45efb921fa),
and
[visit()](../../dc/d5c/classApp_1_1Expression.html#a8fab83c92843f933070eec6e5618010d).

## ◆ simplify()

| virtual [Expression](../../dc/d5c/classApp_1_1Expression.html) * App::Expression::simplify  | ( | | ) |  const  
---|---|---|---|---  
pure virtual  
  
Implemented in
[App::UnitExpression](../../d2/d4a/classApp_1_1UnitExpression.html#aaa0bdce434a89041387f498edf923a6b),
[App::NumberExpression](../../d4/d2a/classApp_1_1NumberExpression.html#a7801a41e631544f7d0d5717c1682beba),
[App::OperatorExpression](../../d1/d7d/classApp_1_1OperatorExpression.html#a350f104eaa83275378734a4bc3239ae5),
[App::ConditionalExpression](../../dc/de5/classApp_1_1ConditionalExpression.html#a31fe77944946842cf469cd7bdd93995c),
[App::FunctionExpression](../../d6/da3/classApp_1_1FunctionExpression.html#a3241421502813b3053a26db4fd247ed3),
[App::VariableExpression](../../df/d0f/classApp_1_1VariableExpression.html#a6c9709ab5ef6619c4cca213517af0a4b),
[App::PyObjectExpression](../../d9/dcd/classApp_1_1PyObjectExpression.html#a6d4fc0006f2b9030d10b8810cd8cc6f9),
[App::StringExpression](../../d7/dd9/classApp_1_1StringExpression.html#a4dcc77a15b51c648cba8ec3c4d380220),
and
[App::RangeExpression](../../da/d8b/classApp_1_1RangeExpression.html#ac6054f53b78a3a10d6c4c5d908925e09).

Referenced by
[App::ExpressionParser::parseUnit()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a5ce9e4984820d693ee32429e0f37db9c),
[App::OperatorExpression::simplify()](../../d1/d7d/classApp_1_1OperatorExpression.html#a350f104eaa83275378734a4bc3239ae5),
[App::ConditionalExpression::simplify()](../../dc/de5/classApp_1_1ConditionalExpression.html#a31fe77944946842cf469cd7bdd93995c),
and
[App::FunctionExpression::simplify()](../../d6/da3/classApp_1_1FunctionExpression.html#a3241421502813b3053a26db4fd247ed3).

## ◆ toString() [1/2]

std::string Expression::toString  | ( | [bool](../../d9/db9/classbool.html) | _persistent_ = `false`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _checkPriority_ = `false`,   
|  | [int](../../d1/da0/classint.html) | _indent_ = `0`  
| ) | |  const  
  
References
[toString()](../../dc/d5c/classApp_1_1Expression.html#aeeb0fc484ec620affaf4fbd402cc3067).

Referenced by
[isSame()](../../dc/d5c/classApp_1_1Expression.html#a0629cfd92afb2d9aff38fda6d3b30c24),
and
[toString()](../../dc/d5c/classApp_1_1Expression.html#aeeb0fc484ec620affaf4fbd402cc3067).

## ◆ toString() [2/2]

void Expression::toString  | ( | std::ostream & | _os_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _persistent_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _checkPriority_ = `false`,   
|  | [int](../../d1/da0/classint.html) | _indent_ = `0`  
| ) | |  const  
  
References
[priority()](../../dc/d5c/classApp_1_1Expression.html#a4393008057438a9a4df99ad89788bd01).

## ◆ updateLabelReference()

[ExpressionPtr](../../dd/dc2/namespaceApp.html#a87d84b6ef4dda5737e574e95320bc07f) Expression::updateLabelReference  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const std::string & | _ref_ ,   
|  | const char *  | _newLabel_  
| ) | |  const  
  
References
[copy()](../../dc/d5c/classApp_1_1Expression.html#a2210f1ec2e2443ff5c328e45efb921fa),
[getIdentifiers()](../../dc/d5c/classApp_1_1Expression.html#aa4c82c6f4c790b957fe4a5195c665ff3),
and
[visit()](../../dc/d5c/classApp_1_1Expression.html#a8fab83c92843f933070eec6e5618010d).

Referenced by
[UpdateLabelExpressionVisitor::visit()](../../d3/d25/classUpdateLabelExpressionVisitor.html#a95c349330b431b4c1d1568177abc2bcf).

## ◆ visit()

void Expression::visit  | ( | [ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html) & | _v_| ) |   
---|---|---|---|---|---  
  
Referenced by
[adjustLinks()](../../dc/d5c/classApp_1_1Expression.html#af8dab25510279b4940ec20c5c050005b),
[getIdentifiers()](../../dc/d5c/classApp_1_1Expression.html#ae09856686b038d239e5b5e4ddb5f1217),
[replaceObject()](../../dc/d5c/classApp_1_1Expression.html#ae8b79b427cc93dbcb58855e1f8fa3746),
and
[updateLabelReference()](../../dc/d5c/classApp_1_1Expression.html#af62b084e6469e8b5bc8f823f53bb68b4).

## Member Data Documentation

## ◆ comment

std::string App::Expression::comment  
---  
  
Referenced by
[copy()](../../dc/d5c/classApp_1_1Expression.html#a2210f1ec2e2443ff5c328e45efb921fa),
[addonmanager_macro.Macro::fill_details_from_code()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a49b8d021a9b8255f8a490e880eb15489),
[addonmanager_macro.Macro::fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
and
[isSame()](../../dc/d5c/classApp_1_1Expression.html#a0629cfd92afb2d9aff38fda6d3b30c24).

## ◆ components

|
[ComponentList](../../dc/d5c/classApp_1_1Expression.html#ae5c26c23fa1701412faad43c4482332b)
App::Expression::components  
---  
protected  
  
Referenced by
[copy()](../../dc/d5c/classApp_1_1Expression.html#a2210f1ec2e2443ff5c328e45efb921fa).

## ◆ ExpressionVisitor

[friend](../../d7/d23/classfriend.html) App::Expression::ExpressionVisitor  
---  
  
## ◆ owner

| [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*
App::Expression::owner  
---  
protected  
  
The document object used to access unqualified variables (i.e local scope)

Referenced by
[App::Expression::Component::del()](../../d5/df9/structApp_1_1Expression_1_1Component.html#aa3b85278581997ecc4206d983cde0222),
[eval()](../../dc/d5c/classApp_1_1Expression.html#aef48bca09d540f5a8b3d41bcfd4dda1d),
[App::FunctionExpression::evalAggregate()](../../d6/da3/classApp_1_1FunctionExpression.html#ad9267dc1decdafaaa129f1bd51de07e4),
[App::Expression::Component::get()](../../d5/df9/structApp_1_1Expression_1_1Component.html#a105ce2f55b1e32a78b7fe55f0be9789d),
[App::RangeExpression::getRange()](../../da/d8b/classApp_1_1RangeExpression.html#a1fee8772a70c049b0fb2ce7c629e8fd9),
[importSubNames()](../../dc/d5c/classApp_1_1Expression.html#a6b338d5ca7344c41547dfe77019cf1e1),
[App::RangeExpression::isTouched()](../../da/d8b/classApp_1_1RangeExpression.html#a93b55327da44e753b97eca89a2ec8c7c),
[parse()](../../dc/d5c/classApp_1_1Expression.html#a377c20925f92aab0265eb9e3e0b35c97),
[App::Expression::Component::set()](../../d5/df9/structApp_1_1Expression_1_1Component.html#a8f3a5ce94e26009bf81a428ec7726910),
[App::UnitExpression::simplify()](../../d2/d4a/classApp_1_1UnitExpression.html#aaa0bdce434a89041387f498edf923a6b),
[App::OperatorExpression::simplify()](../../d1/d7d/classApp_1_1OperatorExpression.html#a350f104eaa83275378734a4bc3239ae5),
[App::ConditionalExpression::simplify()](../../dc/de5/classApp_1_1ConditionalExpression.html#a31fe77944946842cf469cd7bdd93995c),
and
[App::FunctionExpression::simplify()](../../d6/da3/classApp_1_1FunctionExpression.html#a3241421502813b3053a26db4fd247ed3).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Expression.h
  * FreeCAD/src/App/Expression.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

