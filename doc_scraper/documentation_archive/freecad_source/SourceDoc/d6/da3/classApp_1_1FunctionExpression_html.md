---
url: https://freecad.github.io/SourceDoc/d6/da3/classApp_1_1FunctionExpression.html
scraped_at: 2025-09-08T14:54:49.575161
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [FunctionExpression](../../d6/da3/classApp_1_1FunctionExpression.html)

[List of all members](../../d1/da6/classApp_1_1FunctionExpression-members.html) | Public Types | Public Member Functions | Static Public Member Functions | Static Protected Member Functions | Protected Attributes

App::FunctionExpression Class Reference

Class implementing various functions, e.g sin, cos, etc.
[More...](../../d6/da3/classApp_1_1FunctionExpression.html#details)

`#include <ExpressionParser.h>`

##  Public Types  
  
---  
enum | [Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658) {   
[NONE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a2bbe942c44dc7bdda86ce170aad0b4fa)
,
[ACOS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a276e53bd5bc98ed43a56f5ca6b7964be)
,
[ASIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a0d51a64df26841bd69c1215df262843b)
,
[ATAN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a1fb71ce660de19d227304711d1d8866e)
,  
[ABS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a6804d3fbcab38a404006d035cc4e1f4f)
,
[EXP](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a98485d2edab862d50036742cf22c5e25)
,
[LOG](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a584442cca2c253588e2919a6250cf8c4)
,
[LOG10](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a6645db0e4ed76f776fb0a2e90a5fa11f)
,  
[SIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a8cb871e1b4297efc01a6c7bb8b91a1de)
,
[SINH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a4bf7a873227153a605236337c8306240)
,
[TAN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a8642f76a8b6ba35cd1b4a20c615cf75f)
,
[TANH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a99f98d2742d51c6391122e486d0f9999)
,  
[SQRT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658af3f4842894f781437eb8fd562a4521cc)
,
[COS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a95716a81b64bb477b3112c6fb8ac6ddc)
,
[COSH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a7bccae7f391ed9c60f28644106ed1de7)
,
[ATAN2](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658adf3ec31eb0b1129f2a3f8fc6ebb93730)
,  
[MOD](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a189154be19979d1ed093ac38dbe6f04a)
,
[POW](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a0d71bdf3ebcabe8f1be5342d80c2e8b7)
,
[ROUND](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aa1b17d8ff51ae98515e480ebb8f42a93)
,
[TRUNC](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a05a3b2ede4be6c42ced9cf08a3109bfe)
,  
[CEIL](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658af87d783d5a2d13c5fb343b11d7131864)
,
[FLOOR](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a34299dd51d772f631fd115e5c88f631c)
,
[HYPOT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ae6d3982535c8eb6bc881e06e9e737ea1)
,
[CATH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ac2347403aa1e3ac6151b89e7b117f790)
,  
[LIST](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a59d141f026bec92e3bada80f92aa1185)
,
[TUPLE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aea83ba876162a835ecdca70d8ac90b3c)
,
[MSCALE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aed8970081f629373fcdb8bb07dffa1e8)
,
[MINVERT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ab93f185810757ef04030b81fb271f7ce)
,  
[CREATE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a65e69aa96cb0b8a50daa77b5e7ead82c)
,
[STR](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aff93140d7ec86ca9e5ad4a626a82ccd4)
,
[HIDDENREF](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aa8ffc9a30b770655e24289ed8d680c2c)
,
[HREF](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a1f8de8f0cc5297db89c1b14cc73c38d8)
,  
[AGGREGATES](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a5a6e1f1261bb7cec90804706e99621a7)
,
[SUM](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a11a0e7bf8e83c21de7f87e694d164318)
,
[AVERAGE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ad0be26e589bd55d1668ccbfb5e6f0f3b)
,
[STDDEV](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a91dc31754bad8359d9bc294ba356fd0b)
,  
[COUNT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a288c5d4e96ea10990315720b7534bfd3)
,
[MIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a485f8f4a9582feca008856cea0cf4cd4)
,
[MAX](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a24e9b1553580ddc2888c0033a5b3131d)
,
[LAST](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a81ad3a28905f500c15b14aa5b906b353)  
}  
![-](../../closed.png) Public Types inherited from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html)  
typedef std::vector< [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * > | [ComponentList](../../dc/d5c/classApp_1_1Expression.html#ae5c26c23fa1701412faad43c4482332b)  
enum | [DepOption](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74) { [DepNormal](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab030e4fe983000e80dcbe765ca125d5c) , [DepHidden](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74ab28124d65567e1e919055d51d4d1fd4e) , [DepAll](../../dc/d5c/classApp_1_1Expression.html#af66fb3c502713d959f642f47a4236e74acefbcf98504a7d00a297d5aa59e81f83) }  
  
##  Public Member Functions  
  
---  
|
[FunctionExpression](../../d6/da3/classApp_1_1FunctionExpression.html#a45d042440b95ab0b07f7729d39d9730c)
(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)
*_owner=nullptr,
[Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658)
_f=[NONE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a2bbe942c44dc7bdda86ce170aad0b4fa),
std::string &&name=std::string(), std::vector<
[Expression](../../dc/d5c/classApp_1_1Expression.html) * > _args=std::vector<
[Expression](../../dc/d5c/classApp_1_1Expression.html) * >())  
const std::vector< [Expression](../../dc/d5c/classApp_1_1Expression.html) * > & | [getArgs](../../d6/da3/classApp_1_1FunctionExpression.html#a4c7fd5a4621cb166d8c922341af53404) () const  
[Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658) | [getFunction](../../d6/da3/classApp_1_1FunctionExpression.html#a54f00b3921d71b245d73163af56c57a3) () const  
virtual [bool](../../d9/db9/classbool.html) | [isTouched](../../d6/da3/classApp_1_1FunctionExpression.html#abadfadf53b3f5d62be639a28aeda4906) () const override  
| Determine whether the expressions is considered touched, i.e one or both of
its arguments are touched.
[More...](../../d6/da3/classApp_1_1FunctionExpression.html#abadfadf53b3f5d62be639a28aeda4906)  
  
virtual [Expression](../../dc/d5c/classApp_1_1Expression.html) * | [simplify](../../d6/da3/classApp_1_1FunctionExpression.html#a3241421502813b3053a26db4fd247ed3) () const override  
| Try to simplify the expression, i.e calculate all constant expressions.
[More...](../../d6/da3/classApp_1_1FunctionExpression.html#a3241421502813b3053a26db4fd247ed3)  
  
virtual | [~FunctionExpression](../../d6/da3/classApp_1_1FunctionExpression.html#a8e7f195861233650f20629f7c5dfcecf) ()  
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
  
  
##  Static Public Member Functions  
  
---  
static Py::Object | [evaluate](../../d6/da3/classApp_1_1FunctionExpression.html#aea533bde72fab9803b76f53f0b02aac0) (const [Expression](../../dc/d5c/classApp_1_1Expression.html) *[owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35), [int](../../d1/da0/classint.html) [type](../../d9/d98/classtype.html), const std::vector< [Expression](../../dc/d5c/classApp_1_1Expression.html) * > &[args](../../d6/da3/classApp_1_1FunctionExpression.html#a07655b987610a59c80cf9e6f80ca899e))  
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
  
##  Static Protected Member Functions  
  
---  
static Py::Object | [evalAggregate](../../d6/da3/classApp_1_1FunctionExpression.html#ad9267dc1decdafaaa129f1bd51de07e4) (const [Expression](../../dc/d5c/classApp_1_1Expression.html) *[owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35), [int](../../d1/da0/classint.html) [type](../../d9/d98/classtype.html), const std::vector< [Expression](../../dc/d5c/classApp_1_1Expression.html) * > &[args](../../d6/da3/classApp_1_1FunctionExpression.html#a07655b987610a59c80cf9e6f80ca899e))  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
##  Protected Attributes  
  
---  
std::vector< [Expression](../../dc/d5c/classApp_1_1Expression.html) * > | [args](../../d6/da3/classApp_1_1FunctionExpression.html#a07655b987610a59c80cf9e6f80ca899e)  
[Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658) | [f](../../d6/da3/classApp_1_1FunctionExpression.html#a0e8038112f35e7d5c8d568af8c92cbee)  
| Function to execute.
[More...](../../d6/da3/classApp_1_1FunctionExpression.html#a0e8038112f35e7d5c8d568af8c92cbee)  
  
std::string | [fname](../../d6/da3/classApp_1_1FunctionExpression.html#a5ccaf6f85e85bc8083fc5509bde6c298)  
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
![-](../../closed.png) Public Attributes inherited from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html)  
std::string | [comment](../../dc/d5c/classApp_1_1Expression.html#ae1d5ddb3f258e498436b4ea0d5427a97)  
[friend](../../d7/d23/classfriend.html) | [ExpressionVisitor](../../dc/d5c/classApp_1_1Expression.html#a8152374a586410580356f2b209ebeb10)  
  
## Detailed Description

Class implementing various functions, e.g sin, cos, etc.

## Member Enumeration Documentation

## ◆ Function

enum
[App::FunctionExpression::Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658)  
---  
  
Enumerator  
---  
NONE |   
ACOS |   
ASIN |   
ATAN |   
ABS |   
EXP |   
LOG |   
LOG10 |   
SIN |   
SINH |   
TAN |   
TANH |   
SQRT |   
COS |   
COSH |   
ATAN2 |   
MOD |   
POW |   
ROUND |   
TRUNC |   
CEIL |   
FLOOR |   
HYPOT |   
CATH |   
LIST |   
TUPLE |   
MSCALE |   
MINVERT |   
CREATE |   
STR |   
HIDDENREF |   
HREF |   
AGGREGATES |   
SUM |   
AVERAGE |   
STDDEV |   
COUNT |   
MIN |   
MAX |   
LAST |   
  
## Constructor & Destructor Documentation

## ◆ FunctionExpression()

FunctionExpression::FunctionExpression  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | __owner_ = `nullptr`,   
---|---|---|---  
|  | [Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658) | __f_ = `[NONE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a2bbe942c44dc7bdda86ce170aad0b4fa)`,   
|  | std::string && | _name_ = `std::string()`,   
|  | std::vector< [Expression](../../dc/d5c/classApp_1_1Expression.html) * > | __args_ = `std::vector<[Expression](../../dc/d5c/classApp_1_1Expression.html)*>()`  
| ) | |   
  
References
[ABS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a6804d3fbcab38a404006d035cc4e1f4f),
[ACOS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a276e53bd5bc98ed43a56f5ca6b7964be),
[AGGREGATES](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a5a6e1f1261bb7cec90804706e99621a7),
[args](../../d6/da3/classApp_1_1FunctionExpression.html#a07655b987610a59c80cf9e6f80ca899e),
[ASIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a0d51a64df26841bd69c1215df262843b),
[ATAN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a1fb71ce660de19d227304711d1d8866e),
[ATAN2](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658adf3ec31eb0b1129f2a3f8fc6ebb93730),
[AVERAGE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ad0be26e589bd55d1668ccbfb5e6f0f3b),
[CATH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ac2347403aa1e3ac6151b89e7b117f790),
[CEIL](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658af87d783d5a2d13c5fb343b11d7131864),
[COS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a95716a81b64bb477b3112c6fb8ac6ddc),
[COSH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a7bccae7f391ed9c60f28644106ed1de7),
[COUNT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a288c5d4e96ea10990315720b7534bfd3),
[CREATE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a65e69aa96cb0b8a50daa77b5e7ead82c),
[EXP](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a98485d2edab862d50036742cf22c5e25),
[FLOOR](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a34299dd51d772f631fd115e5c88f631c),
[HIDDENREF](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aa8ffc9a30b770655e24289ed8d680c2c),
[HREF](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a1f8de8f0cc5297db89c1b14cc73c38d8),
[HYPOT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ae6d3982535c8eb6bc881e06e9e737ea1),
[LAST](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a81ad3a28905f500c15b14aa5b906b353),
[LIST](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a59d141f026bec92e3bada80f92aa1185),
[LOG](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a584442cca2c253588e2919a6250cf8c4),
[LOG10](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a6645db0e4ed76f776fb0a2e90a5fa11f),
[MAX](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a24e9b1553580ddc2888c0033a5b3131d),
[MIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a485f8f4a9582feca008856cea0cf4cd4),
[MINVERT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ab93f185810757ef04030b81fb271f7ce),
[MOD](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a189154be19979d1ed093ac38dbe6f04a),
[MSCALE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aed8970081f629373fcdb8bb07dffa1e8),
[NONE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a2bbe942c44dc7bdda86ce170aad0b4fa),
[POW](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a0d71bdf3ebcabe8f1be5342d80c2e8b7),
[ROUND](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aa1b17d8ff51ae98515e480ebb8f42a93),
[SIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a8cb871e1b4297efc01a6c7bb8b91a1de),
[SINH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a4bf7a873227153a605236337c8306240),
[SQRT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658af3f4842894f781437eb8fd562a4521cc),
[STDDEV](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a91dc31754bad8359d9bc294ba356fd0b),
[STR](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aff93140d7ec86ca9e5ad4a626a82ccd4),
[SUM](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a11a0e7bf8e83c21de7f87e694d164318),
[TAN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a8642f76a8b6ba35cd1b4a20c615cf75f),
[TANH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a99f98d2742d51c6391122e486d0f9999),
[TRUNC](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a05a3b2ede4be6c42ced9cf08a3109bfe),
and
[TUPLE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aea83ba876162a835ecdca70d8ac90b3c).

Referenced by
[simplify()](../../d6/da3/classApp_1_1FunctionExpression.html#a3241421502813b3053a26db4fd247ed3).

## ◆ ~FunctionExpression()

| FunctionExpression::~FunctionExpression  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[args](../../d6/da3/classApp_1_1FunctionExpression.html#a07655b987610a59c80cf9e6f80ca899e).

## Member Function Documentation

## ◆ evalAggregate()

| Py::Object FunctionExpression::evalAggregate  | ( | const [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _owner_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _type_ ,   
|  | const std::vector< [Expression](../../dc/d5c/classApp_1_1Expression.html) * > & | _args_  
| ) | |   
staticprotected  
  
References
[args](../../d6/da3/classApp_1_1FunctionExpression.html#a07655b987610a59c80cf9e6f80ca899e),
[AVERAGE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ad0be26e589bd55d1668ccbfb5e6f0f3b),
[COUNT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a288c5d4e96ea10990315720b7534bfd3),
[Base::BaseClass::getClassTypeId()](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca),
[App::ExtensionContainer::getPropertyByName()](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897),
[App::PropertyQuantity::getQuantityValue()](../../d4/d65/classApp_1_1PropertyQuantity.html#aa6023e0701e1890deeb98712ff37bd02),
[App::RangeExpression::getRange()](../../da/d8b/classApp_1_1RangeExpression.html#a1fee8772a70c049b0fb2ce7c629e8fd9),
[App::PropertyInteger::getValue()](../../dd/d85/classApp_1_1PropertyInteger.html#a4af3c36604f96057c6d64ccc74126042),
[App::PropertyFloat::getValue()](../../d3/dbe/classApp_1_1PropertyFloat.html#ae6c1d258b368a93c6fe4e6aa3f2a0842),
[MAX](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a24e9b1553580ddc2888c0033a5b3131d),
[MIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a485f8f4a9582feca008856cea0cf4cd4),
[App::Expression::owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35),
[App::pyFromQuantity()](../../dd/dc2/namespaceApp.html#a1f508e13586e74f78640fce6b915e8ca),
[App::pyToQuantity()](../../dd/dc2/namespaceApp.html#af26e6a7b37963f3cbe423ae4f898748f),
[STDDEV](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a91dc31754bad8359d9bc294ba356fd0b),
and
[SUM](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a11a0e7bf8e83c21de7f87e694d164318).

Referenced by
[evaluate()](../../d6/da3/classApp_1_1FunctionExpression.html#aea533bde72fab9803b76f53f0b02aac0).

## ◆ evaluate()

| Py::Object FunctionExpression::evaluate  | ( | const [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _owner_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _type_ ,   
|  | const std::vector< [Expression](../../dc/d5c/classApp_1_1Expression.html) * > & | _args_  
| ) | |   
static  
  
References
[ABS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a6804d3fbcab38a404006d035cc4e1f4f),
[ACOS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a276e53bd5bc98ed43a56f5ca6b7964be),
[AGGREGATES](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a5a6e1f1261bb7cec90804706e99621a7),
[args](../../d6/da3/classApp_1_1FunctionExpression.html#a07655b987610a59c80cf9e6f80ca899e),
[ASIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a0d51a64df26841bd69c1215df262843b),
[ATAN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a1fb71ce660de19d227304711d1d8866e),
[ATAN2](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658adf3ec31eb0b1129f2a3f8fc6ebb93730),
[CATH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ac2347403aa1e3ac6151b89e7b117f790),
[CEIL](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658af87d783d5a2d13c5fb343b11d7131864),
[COS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a95716a81b64bb477b3112c6fb8ac6ddc),
[COSH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a7bccae7f391ed9c60f28644106ed1de7),
[CREATE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a65e69aa96cb0b8a50daa77b5e7ead82c),
[evalAggregate()](../../d6/da3/classApp_1_1FunctionExpression.html#ad9267dc1decdafaaa129f1bd51de07e4),
[EXP](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a98485d2edab862d50036742cf22c5e25),
[FLOOR](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a34299dd51d772f631fd115e5c88f631c),
[Base::fmod()](../../db/d07/namespaceBase.html#a88f1583f404c912bde71485622495394),
[Base::BaseClass::getClassTypeId()](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca),
[App::Expression::getOwner()](../../dc/d5c/classApp_1_1Expression.html#a0ef3b9243a427d7c1a181ac2ed170a18),
[App::Expression::getPyValue()](../../dc/d5c/classApp_1_1Expression.html#ad2bf8c4dd181d646f6bececf47e8e2f4),
[HIDDENREF](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aa8ffc9a30b770655e24289ed8d680c2c),
[HREF](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a1f8de8f0cc5297db89c1b14cc73c38d8),
[HYPOT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ae6d3982535c8eb6bc881e06e9e737ea1),
[LIST](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a59d141f026bec92e3bada80f92aa1185),
[LOG](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a584442cca2c253588e2919a6250cf8c4),
[LOG10](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a6645db0e4ed76f776fb0a2e90a5fa11f),
[MINVERT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ab93f185810757ef04030b81fb271f7ce),
[MOD](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a189154be19979d1ed093ac38dbe6f04a),
[MSCALE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aed8970081f629373fcdb8bb07dffa1e8),
[POW](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a0d71bdf3ebcabe8f1be5342d80c2e8b7),
[Base::pow()](../../db/d07/namespaceBase.html#ab7fea8267976ceb4298adf5e4b022588),
[App::pyToQuantity()](../../dd/dc2/namespaceApp.html#af26e6a7b37963f3cbe423ae4f898748f),
[ROUND](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aa1b17d8ff51ae98515e480ebb8f42a93),
[SIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a8cb871e1b4297efc01a6c7bb8b91a1de),
[SINH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a4bf7a873227153a605236337c8306240),
[SQRT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658af3f4842894f781437eb8fd562a4521cc),
[STR](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aff93140d7ec86ca9e5ad4a626a82ccd4),
[TAN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a8642f76a8b6ba35cd1b4a20c615cf75f),
[TANH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a99f98d2742d51c6391122e486d0f9999),
[TRUNC](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a05a3b2ede4be6c42ced9cf08a3109bfe),
[TUPLE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aea83ba876162a835ecdca70d8ac90b3c),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[Spreadsheet_legacy.Spreadsheet::evaluate()](../../d2/d6d/classSpreadsheet__legacy_1_1Spreadsheet.html#a2f1aaa05ba46c7085371328c93ed4d26),
and
[Spreadsheet_legacy.Spreadsheet::isNumeric()](../../d2/d6d/classSpreadsheet__legacy_1_1Spreadsheet.html#acf77c1896a706224f52d15e21c96f62e).

## ◆ getArgs()

const std::vector< [Expression](../../dc/d5c/classApp_1_1Expression.html) * > & App::FunctionExpression::getArgs  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getFunction()

[Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658) App::FunctionExpression::getFunction  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isTouched()

| [bool](../../d9/db9/classbool.html) FunctionExpression::isTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Determine whether the expressions is considered touched, i.e one or both of
its arguments are touched.

Returns

    True if touched, false if not. 

Reimplemented from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html#ae17d3a0ad8b07160c01a9b55b1844802).

References
[args](../../d6/da3/classApp_1_1FunctionExpression.html#a07655b987610a59c80cf9e6f80ca899e).

## ◆ simplify()

| [Expression](../../dc/d5c/classApp_1_1Expression.html) * FunctionExpression::simplify  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Try to simplify the expression, i.e calculate all constant expressions.

Returns

    A simplified expression. 

Reimplemented from
[App::UnitExpression](../../d2/d4a/classApp_1_1UnitExpression.html#aaa0bdce434a89041387f498edf923a6b).

References
[args](../../d6/da3/classApp_1_1FunctionExpression.html#a07655b987610a59c80cf9e6f80ca899e),
[App::Expression::eval()](../../dc/d5c/classApp_1_1Expression.html#aef48bca09d540f5a8b3d41bcfd4dda1d),
[fname](../../d6/da3/classApp_1_1FunctionExpression.html#a5ccaf6f85e85bc8083fc5509bde6c298),
[FunctionExpression()](../../d6/da3/classApp_1_1FunctionExpression.html#a45d042440b95ab0b07f7729d39d9730c),
[App::Expression::owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35),
and
[App::Expression::simplify()](../../dc/d5c/classApp_1_1Expression.html#a1c84dd5e6ffe86c4f720e179859d5ca3).

## Member Data Documentation

## ◆ args

| std::vector<[Expression](../../dc/d5c/classApp_1_1Expression.html) *>
App::FunctionExpression::args  
---  
protected  
  
Referenced by
[evalAggregate()](../../d6/da3/classApp_1_1FunctionExpression.html#ad9267dc1decdafaaa129f1bd51de07e4),
[evaluate()](../../d6/da3/classApp_1_1FunctionExpression.html#aea533bde72fab9803b76f53f0b02aac0),
[FunctionExpression()](../../d6/da3/classApp_1_1FunctionExpression.html#a45d042440b95ab0b07f7729d39d9730c),
[isTouched()](../../d6/da3/classApp_1_1FunctionExpression.html#abadfadf53b3f5d62be639a28aeda4906),
[MengerSponge.MengerThread::run()](../../d4/def/classMengerSponge_1_1MengerThread.html#a0035f5bc1bc7b57417fbd8a27438e99f),
[simplify()](../../d6/da3/classApp_1_1FunctionExpression.html#a3241421502813b3053a26db4fd247ed3),
and
[~FunctionExpression()](../../d6/da3/classApp_1_1FunctionExpression.html#a8e7f195861233650f20629f7c5dfcecf).

## ◆ f

|
[Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658)
App::FunctionExpression::f  
---  
protected  
  
Function to execute.

## ◆ fname

| std::string App::FunctionExpression::fname  
---  
protected  
  
Referenced by
[simplify()](../../d6/da3/classApp_1_1FunctionExpression.html#a3241421502813b3053a26db4fd247ed3).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ExpressionParser.h
  * FreeCAD/src/App/Expression.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

