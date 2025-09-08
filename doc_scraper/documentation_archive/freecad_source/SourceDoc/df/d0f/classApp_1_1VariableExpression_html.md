---
url: https://freecad.github.io/SourceDoc/df/d0f/classApp_1_1VariableExpression.html
scraped_at: 2025-09-08T14:57:04.114852
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [VariableExpression](../../df/d0f/classApp_1_1VariableExpression.html)

[List of all members](../../db/df2/classApp_1_1VariableExpression-members.html) | Public Member Functions | Protected Attributes

App::VariableExpression Class Reference

Class implementing a reference to a property.
[More...](../../df/d0f/classApp_1_1VariableExpression.html#details)

`#include <ExpressionParser.h>`

##  Public Member Functions  
  
---  
virtual void | [addComponent](../../df/d0f/classApp_1_1VariableExpression.html#a13fe7b9451d199e5b1b2047b48b941a0) ([Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) *component) override  
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | [getPath](../../df/d0f/classApp_1_1VariableExpression.html#a1d7c49281c154286bf4540984406bcb2) () const  
const [App::Property](../../d0/da9/classApp_1_1Property.html) * | [getProperty](../../df/d0f/classApp_1_1VariableExpression.html#a8211f23466f283ea3c5e4a149e904c34) () const  
| Find the property this expression referse to.
[More...](../../df/d0f/classApp_1_1VariableExpression.html#a8211f23466f283ea3c5e4a149e904c34)  
  
virtual [bool](../../d9/db9/classbool.html) | [isTouched](../../df/d0f/classApp_1_1VariableExpression.html#a30d24a5ccb5a517237ddba1477458080) () const override  
| Determine if the expression is touched or not, i.e whether the
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") object it refers to is
touched().
[More...](../../df/d0f/classApp_1_1VariableExpression.html#a30d24a5ccb5a517237ddba1477458080)  
  
std::string | [name](../../df/d0f/classApp_1_1VariableExpression.html#a444712b93a41fce90e5623d0fb6973ac) () const  
void | [setPath](../../df/d0f/classApp_1_1VariableExpression.html#a0a80f590f47652f6171d9ad6c330d805) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path)  
virtual [Expression](../../dc/d5c/classApp_1_1Expression.html) * | [simplify](../../df/d0f/classApp_1_1VariableExpression.html#a6c9709ab5ef6619c4cca213517af0a4b) () const override  
| [Simplify](../../de/df0/classSimplify.html) the expression.
[More...](../../df/d0f/classApp_1_1VariableExpression.html#a6c9709ab5ef6619c4cca213517af0a4b)  
  
|
[VariableExpression](../../df/d0f/classApp_1_1VariableExpression.html#a7d2d1f03a0e235a1452d2643484241e2)
(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)
*_owner=nullptr, const
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)
&_var=[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)())  
|
[~VariableExpression](../../df/d0f/classApp_1_1VariableExpression.html#ac86830e329a2ba7ccd5e03a0335613ea)
()  
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
  
  
##  Protected Attributes  
  
---  
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | [var](../../df/d0f/classApp_1_1VariableExpression.html#aba1b3e4bcc120f5f1cf3505e9133e8b9)  
| Variable name  
[More...](../../df/d0f/classApp_1_1VariableExpression.html#aba1b3e4bcc120f5f1cf3505e9133e8b9)  
  
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
  
## Detailed Description

Class implementing a reference to a property.

If the name is unqualified, the owner of the expression is searched. If it is
qualified, the document that contains the owning document object is searched
for other document objects to search. Both labels and internal document names
are searched.

## Constructor & Destructor Documentation

## ◆ VariableExpression()

VariableExpression::VariableExpression  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | __owner_ = `nullptr`,   
---|---|---|---  
|  | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | __var_ = `[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)()`  
| ) | |   
  
## ◆ ~VariableExpression()

VariableExpression::~VariableExpression  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ addComponent()

| void VariableExpression::addComponent  | ( | [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) *  | _component_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html#a3fa7e813bc2a7840b9e56c1aaea4a276).

References
[App::Expression::addComponent()](../../dc/d5c/classApp_1_1Expression.html#a3fa7e813bc2a7840b9e56c1aaea4a276),
[App::ObjectIdentifier::ArrayComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a13e4caad9b9cbb9bd8aa45079e8896a4),
[App::ObjectIdentifier::MapComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ae95e6b1cd5b6d31abe8c46ad38a23f4d),
[App::ObjectIdentifier::RangeComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ac4a5968e4f45d718d0d8b5a75895ca62),
and
[var](../../df/d0f/classApp_1_1VariableExpression.html#aba1b3e4bcc120f5f1cf3505e9133e8b9).

## ◆ getPath()

[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) App::VariableExpression::getPath  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getProperty()

const [Property](../../d0/da9/classApp_1_1Property.html) * VariableExpression::getProperty  | ( | | ) |  const  
---|---|---|---|---  
  
Find the property this expression referse to.

Unqualified names (i.e the name only without any dots) are resolved in the
owning DocumentObjects. Qualified names are looked up in the owning
[Document](../../d8/d3e/classApp_1_1Document.html "The document class."). It
is first looked up by its internal name. If not found, the DocumentObjects'
labels searched.

If something fails, an exception is thrown.

Returns

    The [Property](../../d0/da9/classApp_1_1Property.html "Base class of all properties This is the father of all properties.") object if it is derived from either [PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html "Integer properties This is the father of all properties handling Integers."), [PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html "Float properties This is the father of all properties handling floats."), or [PropertyString](../../dd/df8/classApp_1_1PropertyString.html "String properties This is the father of all properties handling Strings."). 

References
[App::ObjectIdentifier::getProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afc4aaa90cb65a96c83fd931134d26b24),
[App::ObjectIdentifier::resolveErrorString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad22feac2744b1bebc12711be503cf2a4),
and
[var](../../df/d0f/classApp_1_1VariableExpression.html#aba1b3e4bcc120f5f1cf3505e9133e8b9).

## ◆ isTouched()

| [bool](../../d9/db9/classbool.html) VariableExpression::isTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Determine if the expression is touched or not, i.e whether the
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") object it refers to is
touched().

Returns

    True if the [Property](../../d0/da9/classApp_1_1Property.html "Base class of all properties This is the father of all properties.") object is touched, false if not. 

Reimplemented from
[App::Expression](../../dc/d5c/classApp_1_1Expression.html#ae17d3a0ad8b07160c01a9b55b1844802).

References
[App::ObjectIdentifier::isTouched()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a14e3f2b6fbb8fbe073435a5d4830fe13),
and
[var](../../df/d0f/classApp_1_1VariableExpression.html#aba1b3e4bcc120f5f1cf3505e9133e8b9).

## ◆ name()

std::string App::VariableExpression::name  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[draftguitools.gui_groups.Ui_AddNamedGroup::accept()](../../d3/df7/classdraftguitools_1_1gui__groups_1_1Ui__AddNamedGroup.html#a9ea5973817eab7d74792f5b109a01466),
[prototype.Node::addtofreecad()](../../d2/d62/classprototype_1_1Node.html#adc095cc5636da029d1e0d9cef8859701),
[Addon.Addon::disable()](../../d8/d91/classAddon_1_1Addon.html#ae714705a38afe9f13cd2b17580178b31),
[Addon.Addon::enable()](../../d8/d91/classAddon_1_1Addon.html#a79d327ec9a0b4e85e9e96cfad4003ed6),
[addonmanager_macro.Macro::filename()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a5de4e6a1f3c41dce24066111955cd706),
[gzip_utf8.GzipFile::filename()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ab56fe84a4eb08c44e7a0026280c01229),
[addonmanager_macro.Macro::fill_details_from_code()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a49b8d021a9b8255f8a490e880eb15489),
[addonmanager_macro.Macro::fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[Addon.Addon::get_cached_icon_filename()](../../d8/d91/classAddon_1_1Addon.html#a7b026027a2904028032edbe3e99e2cbd),
[ifc4.ifcapproval::hasidentifierorname()](../../df/d91/classifc4_1_1ifcapproval.html#a54f558ba3b17fad5fc6579e9d5f50947),
[addonmanager_macro.Macro::install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
[Addon.Addon::is_disabled()](../../d8/d91/classAddon_1_1Addon.html#a5752a95fcf0c51ed06f9841b381d3e50),
[femsolver.elmer.sifio.Section::keys()](../../db/dab/classfemsolver_1_1elmer_1_1sifio_1_1Section.html#ab5b099447f66f33743850697f0e20de4),
[automotive_design.si_unit::named_unit_dimensions()](../../d5/d77/classautomotive__design_1_1si__unit.html#a68eb7954eb09daa334bc8f2c2abbe5f9),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction::output()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aeedd5f59969cc27432880d1916f3d7f9),
[prototype.Node::pprint()](../../d2/d62/classprototype_1_1Node.html#a5ae181c34e48238d2364b0ba4960c252),
[prototype.Node::pprint2()](../../d2/d62/classprototype_1_1Node.html#aaedcc4ba1fb305c7ddcc025235043cd5),
[PathScripts.PathSetupSheetGui.OpTaskPanel::propertyGroup()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a69cbbaadcb9cff7b526af2c743041d7b),
[PathScripts.PathSetupSheetGui.OpTaskPanel::propertyName()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#ad9bd0e0149d1bc42fc8e89a290de4910),
[PathScripts.PathJobGui.TaskPanel::reject()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a54fd97ba9b0060fa8fed8a43c360da0c),
[addonmanager_macro.Macro::remove()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ad13245288f8beb62d92cb458a2d2ce05),
[Addon.Addon::to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
[ifc2x3.ifcexternalreference::wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc2x3.ifcdocumentreference::wr1()](../../df/dd6/classifc2x3_1_1ifcdocumentreference.html#a7d5fdb1cb0dee567c44834b868c5cdad),
[ifc4.ifcexternalreference::wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
[ifc4.ifcdocumentreference::wr1()](../../d7/d2b/classifc4_1_1ifcdocumentreference.html#a8779d74c67e647441d1fb20c76f44f97),
and
[automotive_design.general_property_association::wr2()](../../d2/df3/classautomotive__design_1_1general__property__association.html#ae7f46462c59bc4e541a5d2511631eb65).

## ◆ setPath()

void VariableExpression::setPath  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |   
---|---|---|---|---|---  
  
References
[var](../../df/d0f/classApp_1_1VariableExpression.html#aba1b3e4bcc120f5f1cf3505e9133e8b9).

## ◆ simplify()

| [Expression](../../dc/d5c/classApp_1_1Expression.html) * VariableExpression::simplify  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
[Simplify](../../de/df0/classSimplify.html) the expression.

Simplification of
[VariableExpression](../../df/d0f/classApp_1_1VariableExpression.html "Class
implementing a reference to a property.") objects is not possible (if it is
instantiated it would be an evaluation instead).

Returns

    A copy of the expression. 

Reimplemented from
[App::UnitExpression](../../d2/d4a/classApp_1_1UnitExpression.html#aaa0bdce434a89041387f498edf923a6b).

References
[App::Expression::copy()](../../dc/d5c/classApp_1_1Expression.html#a2210f1ec2e2443ff5c328e45efb921fa).

## Member Data Documentation

## ◆ var

| [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)
App::VariableExpression::var  
---  
protected  
  
Variable name  

Referenced by
[addComponent()](../../df/d0f/classApp_1_1VariableExpression.html#a13fe7b9451d199e5b1b2047b48b941a0),
[getProperty()](../../df/d0f/classApp_1_1VariableExpression.html#a8211f23466f283ea3c5e4a149e904c34),
[isTouched()](../../df/d0f/classApp_1_1VariableExpression.html#a30d24a5ccb5a517237ddba1477458080),
and
[setPath()](../../df/d0f/classApp_1_1VariableExpression.html#a0a80f590f47652f6171d9ad6c330d805).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ExpressionParser.h
  * FreeCAD/src/App/Expression.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

