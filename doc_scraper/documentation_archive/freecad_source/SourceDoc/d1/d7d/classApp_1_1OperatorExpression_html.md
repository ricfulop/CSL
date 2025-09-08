---
url: https://freecad.github.io/SourceDoc/d1/d7d/classApp_1_1OperatorExpression.html
scraped_at: 2025-09-08T14:55:17.671610
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [OperatorExpression](../../d1/d7d/classApp_1_1OperatorExpression.html)

[List of all members](../../de/d04/classApp_1_1OperatorExpression-members.html) | Public Types | Public Member Functions | Protected Member Functions | Protected Attributes

App::OperatorExpression Class Reference

Class implementing an infix expression.
[More...](../../d1/d7d/classApp_1_1OperatorExpression.html#details)

`#include <ExpressionParser.h>`

##  Public Types  
  
---  
enum | [Operator](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1) {   
[NONE](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1af4f9da055ba06b725ea79ff7e57cba59)
,
[ADD](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1a0bfbc5b863e53b891ec510a33507d14d)
,
[SUB](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1ab2ba51fffb2414017436a180dc7525ca)
,
[MUL](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1adbbc3fc88f7c77e538cb6974499daf58)
,  
[DIV](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1a8ce9d53eec9fdefa45e0e48d6faa7e08)
,
[MOD](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1a5aa4a78093d709e343e33e6c4dd87c25)
,
[POW](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1aa79060f800c28332a57f7d0e646b37d8)
,
[EQ](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1aa506ff992a35d13b0e9cdd22e9fedef5)
,  
[NEQ](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1afe5a7683304205767eab162812ae2667)
,
[LT](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1ae6e9d576da242ca3f0c0bc3c4daa1d5b)
,
[GT](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1a3e860411f7e643b8a2fa9de93d047b99)
,
[LTE](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1a28f0e2ec81eb363c11cab901d52e5a82)
,  
[GTE](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1ac1c25dbdaa1272879347a6068295aba0)
,
[UNIT](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1a5ed373034986b7425796cac54918b448)
,
[NEG](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1ab024136cfa45cbe097519e6010c40a29)
,
[POS](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1a5b6233d79c86af25a8a784a38862d49a)  
}  
![-](../../closed.png) Public Types inherited from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html)  
typedef std::vector< [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * > | [ComponentList](../../dc/d5c/classApp_1_1Expression.html#ae5c26c23fa1701412faad43c4482332b)  
enum | [DepOption](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74) { [DepNormal](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab030e4fe983000e80dcbe765ca125d5c) , [DepHidden](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab28124d65567e1e919055d51d4d1fd4e) , [DepAll](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74acefbcf98504a7d00a297d5aa59e81f83) }  
  
##  Public Member Functions  
  
---  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [getLeft](../../d1/d7d/classApp_1_1OperatorExpression.html#abddd60d75959a53810c1099c34fe382c) () const  
[Operator](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1) | [getOperator](../../d1/d7d/classApp_1_1OperatorExpression.html#abf43aaec1641c7188a8a46fd1b0c9cef) () const  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [getRight](../../d1/d7d/classApp_1_1OperatorExpression.html#acddd8b9cf2a7622b5894a705bd9e1992) () const  
virtual [bool](../../d9/db9/classbool.html) | [isTouched](../../d1/d7d/classApp_1_1OperatorExpression.html#aa9da888a5ee4fc18cf44a337d7de3824) () const override  
| Determine whether the expression is touched or not, i.e relies on properties
that are touched.
[More...](../../d1/d7d/classApp_1_1OperatorExpression.html#aa9da888a5ee4fc18cf44a337d7de3824)  
  
|
[OperatorExpression](../../d1/d7d/classApp_1_1OperatorExpression.html#a18afa9e859a5e513b7a84862d783342e)
(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)
*_owner=nullptr, [Expression](../../dc/d5c/classApp_1_1Expression.html)
*_left=nullptr,
[Operator](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1)
_op=[NONE](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1af4f9da055ba06b725ea79ff7e57cba59),
[Expression](../../dc/d5c/classApp_1_1Expression.html) *_right=nullptr)  
virtual [int](../../d1/da0/classint.html) | [priority](../../d1/d7d/classApp_1_1OperatorExpression.html#a2bc8aa32f215cf3d64622e4b4c442148) () const override  
| Return the operators priority.
[More...](../../d1/d7d/classApp_1_1OperatorExpression.html#a2bc8aa32f215cf3d64622e4b4c442148)  
  
virtual [Expression](../../dc/d5c/classApp_1_1Expression.html) * | [simplify](../../d1/d7d/classApp_1_1OperatorExpression.html#a350f104eaa83275378734a4bc3239ae5) () const override  
| [Simplify](../../de/df0/classSimplify.html) the expression.
[More...](../../d1/d7d/classApp_1_1OperatorExpression.html#a350f104eaa83275378734a4bc3239ae5)  
  
virtual | [~OperatorExpression](../../d1/d7d/classApp_1_1OperatorExpression.html#afbbfa978776f2b44e1531b9bcec1e7f4) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::UnitExpression](../../d2/d4a/classApp_1_1UnitExpression.html)  
const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) & | [getQuantity](../../d2/d4a/classApp_1_1UnitExpression.html#a6ab1e151072a0bd00aa0b7b4dab54aed) () const  
double | [getScaler](../../d2/d4a/classApp_1_1UnitExpression.html#a0b19debb8b0cefe5d1065dd4196c4417) () const  
const [Base::Unit](../../d2/d37/classBase_1_1Unit.html) & | [getUnit](../../d2/d4a/classApp_1_1UnitExpression.html#a1f1367ed790a4b87995b6437ae666b11) () const  
const std::string | [getUnitString](../../d2/d4a/classApp_1_1UnitExpression.html#a898382a024140004f12cec2e13f4fa24) () const  
double | [getValue](../../d2/d4a/classApp_1_1UnitExpression.html#ab2045fdff22bc6d6f23e9f3f0c3684ea) () const  
void | [setQuantity](../../d2/d4a/classApp_1_1UnitExpression.html#a9a6f1d44a562c11f454b8925fe5782db) (const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) &_quantity)  
void | [setUnit](../../d2/d4a/classApp_1_1UnitExpression.html#a24313eae0ccdb43d0562bd086d17d8e8) (const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) &_quantity)  
| Set unit information.
[More...](../../d2/d4a/classApp_1_1UnitExpression.html#a24313eae0ccdb43d0562bd086d17d8e8)  
  
virtual [Expression](../../dc/d5c/classApp_1_1Expression.html) * | [simplify](../../d2/d4a/classApp_1_1UnitExpression.html#aaa0bdce434a89041387f498edf923a6b) () const override  
| [Simplify](../../de/df0/classSimplify.html) the expression.
[More...](../../d2/d4a/classApp_1_1UnitExpression.html#aaa0bdce434a89041387f498edf923a6b)  
  
|
[UnitExpression](../../d2/d4a/classApp_1_1UnitExpression.html#acf63b2dc39c86b57e2bf3742e53ed0cb)
(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)
*_owner=nullptr, const
[Base::Quantity](../../d8/d18/classBase_1_1Quantity.html)
&_quantity=[Base::Quantity](../../d8/d18/classBase_1_1Quantity.html)(), const
std::string &_unitStr=std::string())  
|
[~UnitExpression](../../d2/d4a/classApp_1_1UnitExpression.html#a5fa428c3967811253f72e4b3776e7f0a)
()  
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
  
  
##  Protected Member Functions  
  
---  
virtual [bool](../../d9/db9/classbool.html) | [isCommutative](../../d1/d7d/classApp_1_1OperatorExpression.html#ad6a30a90302dc88a837cc057ae74057b) () const  
virtual [bool](../../d9/db9/classbool.html) | [isLeftAssociative](../../d1/d7d/classApp_1_1OperatorExpression.html#a93621ad764251f52c8315e4a327adc1d) () const  
virtual [bool](../../d9/db9/classbool.html) | [isRightAssociative](../../d1/d7d/classApp_1_1OperatorExpression.html#aac0223050550fb84b0a4c1da1086678b) () const  
  
##  Protected Attributes  
  
---  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [left](../../d1/d7d/classApp_1_1OperatorExpression.html#a34169e4146e98ca692ec785f9071e6ae)  
| Left operand.
[More...](../../d1/d7d/classApp_1_1OperatorExpression.html#a34169e4146e98ca692ec785f9071e6ae)  
  
[Operator](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1) | [op](../../d1/d7d/classApp_1_1OperatorExpression.html#aadf8d26f32d94dc9a7e2d4bd9205f674)  
| Operator working on left and right.
[More...](../../d1/d7d/classApp_1_1OperatorExpression.html#aadf8d26f32d94dc9a7e2d4bd9205f674)  
  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [right](../../d1/d7d/classApp_1_1OperatorExpression.html#a8a19fb3351b7c8173a66bd035fe56df8)  
| Right operand.
[More...](../../d1/d7d/classApp_1_1OperatorExpression.html#a8a19fb3351b7c8173a66bd035fe56df8)  
  
![-](../../closed.png) Protected Attributes inherited from
[App::UnitExpression](../../d2/d4a/classApp_1_1UnitExpression.html)  
[PyObject](../../df/d1b/classPyObject.html) * | [cache](../../d2/d4a/classApp_1_1UnitExpression.html#a1723a34b26ed58d62b369b55666c80ce) = nullptr  
![-](../../closed.png) Protected Attributes inherited from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html)  
[ComponentList](../../dc/d5c/classApp_1_1Expression.html#ae5c26c23fa1701412faad43c4482332b) | [components](../../dc/d5c/classApp_1_1Expression.html#a1b83ce423e1e318a0af92d193127aacd)  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35)  
| The document object used to access unqualified variables (i.e local scope)
[More...](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35)  
  
  
##  Additional Inherited Members  
  
---  
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
  
## Detailed Description

Class implementing an infix expression.

## Member Enumeration Documentation

## ◆ Operator

enum
[App::OperatorExpression::Operator](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1)  
---  
  
Enumerator  
---  
NONE |   
ADD |   
SUB |   
MUL |   
DIV |   
MOD |   
POW |   
EQ |   
NEQ |   
LT |   
GT |   
LTE |   
GTE |   
UNIT |   
NEG |   
POS |   
  
## Constructor & Destructor Documentation

## ◆ OperatorExpression()

OperatorExpression::OperatorExpression  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | __owner_ = `nullptr`,   
---|---|---|---  
|  | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | __left_ = `nullptr`,   
|  | [Operator](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1) | __op_ = `[NONE](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1af4f9da055ba06b725ea79ff7e57cba59)`,   
|  | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | __right_ = `nullptr`  
| ) | |   
  
## ◆ ~OperatorExpression()

| OperatorExpression::~OperatorExpression  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ getLeft()

[Expression](../../dc/d5c/classApp_1_1Expression.html) * App::OperatorExpression::getLeft  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::ExpressionParser::parseUnit()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a5ce9e4984820d693ee32429e0f37db9c).

## ◆ getOperator()

[Operator](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1) App::OperatorExpression::getOperator  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::ExpressionParser::parseUnit()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a5ce9e4984820d693ee32429e0f37db9c).

## ◆ getRight()

[Expression](../../dc/d5c/classApp_1_1Expression.html) * App::OperatorExpression::getRight  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::ExpressionParser::parseUnit()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a5ce9e4984820d693ee32429e0f37db9c).

## ◆ isCommutative()

| [bool](../../d9/db9/classbool.html) OperatorExpression::isCommutative  | ( | | ) |  const  
---|---|---|---|---  
protectedvirtual  
  
## ◆ isLeftAssociative()

| [bool](../../d9/db9/classbool.html) OperatorExpression::isLeftAssociative  | ( | | ) |  const  
---|---|---|---|---  
protectedvirtual  
  
## ◆ isRightAssociative()

| [bool](../../d9/db9/classbool.html) OperatorExpression::isRightAssociative  | ( | | ) |  const  
---|---|---|---|---  
protectedvirtual  
  
## ◆ isTouched()

| [bool](../../d9/db9/classbool.html) OperatorExpression::isTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Determine whether the expression is touched or not, i.e relies on properties
that are touched.

Reimplemented from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html#ae17d3a0ad8b07160c01a9b55b1844802).

## ◆ priority()

| [int](../../d1/da0/classint.html) OperatorExpression::priority  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Return the operators priority.

This is used to add parentheses where needed when creating a string
representation of the expression.

Returns

    The operator's priority. 

Reimplemented from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html#a4393008057438a9a4df99ad89788bd01).

## ◆ simplify()

| [Expression](../../dc/d5c/classApp_1_1Expression.html) * OperatorExpression::simplify  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
[Simplify](../../de/df0/classSimplify.html) the expression.

For OperatorExpressions, we return a
[NumberExpression](../../d4/d2a/classApp_1_1NumberExpression.html "Class
implementing a number with an optional unit.") if both the left and right side
can be simplified to NumberExpressions. In this case we can calculate the
final value of the expression.

Returns

    Simplified expression. 

Reimplemented from
[App::UnitExpression](../../d2/d4a/classApp_1_1UnitExpression.html#aaa0bdce434a89041387f498edf923a6b).

References
[App::Expression::eval()](../../dc/d5c/classApp_1_1Expression.html#aef48bca09d540f5a8b3d41bcfd4dda1d),
[App::Expression::owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35),
[App::Expression::simplify()](../../dc/d5c/classApp_1_1Expression.html#a1c84dd5e6ffe86c4f720e179859d5ca3),
and
[draftgeoutils.general::v1()](../../d9/dfd/group__draftgeoutils.html#ga07ad5262ee7b26511c5c3592f2681804).

## Member Data Documentation

## ◆ left

| [Expression](../../dc/d5c/classApp_1_1Expression.html)*
App::OperatorExpression::left  
---  
protected  
  
Left operand.

## ◆ op

|
[Operator](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1)
App::OperatorExpression::op  
---  
protected  
  
Operator working on left and right.

## ◆ right

| [Expression](../../dc/d5c/classApp_1_1Expression.html)*
App::OperatorExpression::right  
---  
protected  
  
Right operand.

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ExpressionParser.h
  * FreeCAD/src/App/Expression.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

