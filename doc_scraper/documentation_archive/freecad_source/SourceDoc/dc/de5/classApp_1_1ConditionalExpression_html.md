---
url: https://freecad.github.io/SourceDoc/dc/de5/classApp_1_1ConditionalExpression.html
scraped_at: 2025-09-08T14:54:12.389175
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ConditionalExpression](../../dc/de5/classApp_1_1ConditionalExpression.html)

[List of all members](../../d5/d09/classApp_1_1ConditionalExpression-members.html) | Public Member Functions | Protected Attributes

App::ConditionalExpression Class Reference

`#include <ExpressionParser.h>`

##  Public Member Functions  
  
---  
|
[ConditionalExpression](../../dc/de5/classApp_1_1ConditionalExpression.html#a084a6cd8f6078931930c1460611f1f89)
(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)
*_owner=nullptr, [Expression](../../dc/d5c/classApp_1_1Expression.html)
*_condition=nullptr, [Expression](../../dc/d5c/classApp_1_1Expression.html)
*_trueExpr=nullptr, [Expression](../../dc/d5c/classApp_1_1Expression.html)
*_falseExpr=nullptr)  
virtual [bool](../../d9/db9/classbool.html) | [isTouched](../../dc/de5/classApp_1_1ConditionalExpression.html#a30a886bf35a3522fa5031e22d1e6c168) () const override  
virtual [int](../../d1/da0/classint.html) | [priority](../../dc/de5/classApp_1_1ConditionalExpression.html#a1916c277039109a57f0ebc38fa5a386d) () const override  
virtual [Expression](../../dc/d5c/classApp_1_1Expression.html) * | [simplify](../../dc/de5/classApp_1_1ConditionalExpression.html#a31fe77944946842cf469cd7bdd93995c) () const override  
virtual | [~ConditionalExpression](../../dc/de5/classApp_1_1ConditionalExpression.html#abec02b67255a18ca8000c698ae9217c8) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html)  
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
  
  
##  Protected Attributes  
  
---  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [condition](../../dc/de5/classApp_1_1ConditionalExpression.html#a8e695910f8af21be3367e04173318f68)  
| Condition.
[More...](../../dc/de5/classApp_1_1ConditionalExpression.html#a8e695910f8af21be3367e04173318f68)  
  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [falseExpr](../../dc/de5/classApp_1_1ConditionalExpression.html#a19c7990d31016ed87fd8e80295a40a0a)  
| [Expression](../../dc/d5c/classApp_1_1Expression.html "Base class for
expressions.") if abs(condition) is < 0.5.
[More...](../../dc/de5/classApp_1_1ConditionalExpression.html#a19c7990d31016ed87fd8e80295a40a0a)  
  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [trueExpr](../../dc/de5/classApp_1_1ConditionalExpression.html#ab0d1007c6bc43ee3fad1e4e490d095d3)  
| [Expression](../../dc/d5c/classApp_1_1Expression.html "Base class for
expressions.") if abs(condition) is > 0.5.
[More...](../../dc/de5/classApp_1_1ConditionalExpression.html#ab0d1007c6bc43ee3fad1e4e490d095d3)  
  
![-](../../closed.png) Protected Attributes inherited from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html)  
[ComponentList](../../dc/d5c/classApp_1_1Expression.html#ae5c26c23fa1701412faad43c4482332b) | [components](../../dc/d5c/classApp_1_1Expression.html#a1b83ce423e1e318a0af92d193127aacd)  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35)  
| The document object used to access unqualified variables (i.e local scope)
[More...](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Types inherited from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html)  
typedef std::vector< [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * > | [ComponentList](../../dc/d5c/classApp_1_1Expression.html#ae5c26c23fa1701412faad43c4482332b)  
enum | [DepOption](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74) { [DepNormal](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab030e4fe983000e80dcbe765ca125d5c) , [DepHidden](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab28124d65567e1e919055d51d4d1fd4e) , [DepAll](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74acefbcf98504a7d00a297d5aa59e81f83) }  
![-](../../closed.png) Static Public Member Functions inherited from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html)  
static [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * | [createComponent](../../dc/d5c/classApp_1_1Expression.html#a832fd4778f27454794945d882c9c7518) (const std::string &n)  
static [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * | [createComponent](../../dc/d5c/classApp_1_1Expression.html#af1f60fcdc34ca5c1664977aa50a94f75) ([Expression](../../dc/d5c/classApp_1_1Expression.html) *e1, [Expression](../../dc/d5c/classApp_1_1Expression.html) *e2=nullptr, [Expression](../../dc/d5c/classApp_1_1Expression.html) *e3=nullptr, [bool](../../d9/db9/classbool.html) isRange=false)  
static [Expression](../../dc/d5c/classApp_1_1Expression.html) * | [parse](../../dc/d5c/classApp_1_1Expression.html#a377c20925f92aab0265eb9e3e0b35c97) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *[owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35), const std::string &buffer)  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
![-](../../closed.png) Public Attributes inherited from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html)  
std::string | [comment](../../dc/d5c/classApp_1_1Expression.html#ae1d5ddb3f258e498436b4ea0d5427a97)  
[friend](../../d7/d23/classfriend.html) | [ExpressionVisitor](../../dc/d5c/classApp_1_1Expression.html#a8152374a586410580356f2b209ebeb10)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Constructor & Destructor Documentation

## ◆ ConditionalExpression()

ConditionalExpression::ConditionalExpression  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | __owner_ = `nullptr`,   
---|---|---|---  
|  | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | __condition_ = `nullptr`,   
|  | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | __trueExpr_ = `nullptr`,   
|  | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | __falseExpr_ = `nullptr`  
| ) | |   
  
Referenced by
[simplify()](../../dc/de5/classApp_1_1ConditionalExpression.html#a31fe77944946842cf469cd7bdd93995c).

## ◆ ~ConditionalExpression()

| ConditionalExpression::~ConditionalExpression  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[condition](../../dc/de5/classApp_1_1ConditionalExpression.html#a8e695910f8af21be3367e04173318f68),
[falseExpr](../../dc/de5/classApp_1_1ConditionalExpression.html#a19c7990d31016ed87fd8e80295a40a0a),
and
[trueExpr](../../dc/de5/classApp_1_1ConditionalExpression.html#ab0d1007c6bc43ee3fad1e4e490d095d3).

## Member Function Documentation

## ◆ isTouched()

| [bool](../../d9/db9/classbool.html) ConditionalExpression::isTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html#ae17d3a0ad8b07160c01a9b55b1844802).

References
[falseExpr](../../dc/de5/classApp_1_1ConditionalExpression.html#a19c7990d31016ed87fd8e80295a40a0a),
[App::Expression::isTouched()](../../dc/d5c/classApp_1_1Expression.html#ae17d3a0ad8b07160c01a9b55b1844802),
and
[trueExpr](../../dc/de5/classApp_1_1ConditionalExpression.html#ab0d1007c6bc43ee3fad1e4e490d095d3).

## ◆ priority()

| [int](../../d1/da0/classint.html) ConditionalExpression::priority  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html#a4393008057438a9a4df99ad89788bd01).

## ◆ simplify()

| [Expression](../../dc/d5c/classApp_1_1Expression.html) * ConditionalExpression::simplify  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Implements
[App::Expression](../../dc/d5c/classApp_1_1Expression.html#a1c84dd5e6ffe86c4f720e179859d5ca3).

References
[ConditionalExpression()](../../dc/de5/classApp_1_1ConditionalExpression.html#a084a6cd8f6078931930c1460611f1f89),
[falseExpr](../../dc/de5/classApp_1_1ConditionalExpression.html#a19c7990d31016ed87fd8e80295a40a0a),
[App::Expression::owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35),
[App::Expression::simplify()](../../dc/d5c/classApp_1_1Expression.html#a1c84dd5e6ffe86c4f720e179859d5ca3),
and
[trueExpr](../../dc/de5/classApp_1_1ConditionalExpression.html#ab0d1007c6bc43ee3fad1e4e490d095d3).

## Member Data Documentation

## ◆ condition

| [Expression](../../dc/d5c/classApp_1_1Expression.html)*
App::ConditionalExpression::condition  
---  
protected  
  
Condition.

Referenced by
[~ConditionalExpression()](../../dc/de5/classApp_1_1ConditionalExpression.html#abec02b67255a18ca8000c698ae9217c8).

## ◆ falseExpr

| [Expression](../../dc/d5c/classApp_1_1Expression.html)*
App::ConditionalExpression::falseExpr  
---  
protected  
  
[Expression](../../dc/d5c/classApp_1_1Expression.html "Base class for
expressions.") if abs(condition) is < 0.5.

Referenced by
[isTouched()](../../dc/de5/classApp_1_1ConditionalExpression.html#a30a886bf35a3522fa5031e22d1e6c168),
[simplify()](../../dc/de5/classApp_1_1ConditionalExpression.html#a31fe77944946842cf469cd7bdd93995c),
and
[~ConditionalExpression()](../../dc/de5/classApp_1_1ConditionalExpression.html#abec02b67255a18ca8000c698ae9217c8).

## ◆ trueExpr

| [Expression](../../dc/d5c/classApp_1_1Expression.html)*
App::ConditionalExpression::trueExpr  
---  
protected  
  
[Expression](../../dc/d5c/classApp_1_1Expression.html "Base class for
expressions.") if abs(condition) is > 0.5.

Referenced by
[isTouched()](../../dc/de5/classApp_1_1ConditionalExpression.html#a30a886bf35a3522fa5031e22d1e6c168),
[simplify()](../../dc/de5/classApp_1_1ConditionalExpression.html#a31fe77944946842cf469cd7bdd93995c),
and
[~ConditionalExpression()](../../dc/de5/classApp_1_1ConditionalExpression.html#abec02b67255a18ca8000c698ae9217c8).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ExpressionParser.h
  * FreeCAD/src/App/Expression.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

