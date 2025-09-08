---
url: https://freecad.github.io/SourceDoc/d5/df9/structApp_1_1Expression_1_1Component.html
scraped_at: 2025-09-08T14:54:37.466706
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Expression](../../dc/d5c/classApp_1_1Expression.html)
  * [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html)

[List of all members](../../de/d31/structApp_1_1Expression_1_1Component-members.html) | Public Member Functions | Public Attributes

App::Expression::Component Struct Reference

`#include <ExpressionParser.h>`

##  Public Member Functions  
  
---  
|
[Component](../../d5/df9/structApp_1_1Expression_1_1Component.html#a4ed56a3f088fa2bd43ad995ff48e8c3e)
(const [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html)
&other)  
|
[Component](../../d5/df9/structApp_1_1Expression_1_1Component.html#ae9c505dd285d89ea01b506a9656e6058)
(const
[ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html)
&[comp](../../d5/df9/structApp_1_1Expression_1_1Component.html#a94fca1ad12abb65a07ce46b7d86323ad))  
|
[Component](../../d5/df9/structApp_1_1Expression_1_1Component.html#a2fc92671f01a95805d4c9c681d19db9f)
(const std::string &n)  
|
[Component](../../d5/df9/structApp_1_1Expression_1_1Component.html#a3d256c4ce032f643c24480f681cc52dc)
([Expression](../../dc/d5c/classApp_1_1Expression.html)
*[e1](../../d5/df9/structApp_1_1Expression_1_1Component.html#a11a453a4609f87b7b441c619e4fc6521),
[Expression](../../dc/d5c/classApp_1_1Expression.html)
*[e2](../../d5/df9/structApp_1_1Expression_1_1Component.html#aaf1181d8d97e37d5e83987fe6ff5436d),
[Expression](../../dc/d5c/classApp_1_1Expression.html)
*[e3](../../d5/df9/structApp_1_1Expression_1_1Component.html#a1f6253abbd2650d7cb7ec1aa99640b69),
[bool](../../d9/db9/classbool.html) isRange=false)  
[Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * | [copy](../../d5/df9/structApp_1_1Expression_1_1Component.html#a3c96e791fef0caa82d1dcc8d2b7c47ec) () const  
void | [del](../../d5/df9/structApp_1_1Expression_1_1Component.html#aa3b85278581997ecc4206d983cde0222) (const [Expression](../../dc/d5c/classApp_1_1Expression.html) *[owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35), Py::Object &pyobj) const  
[Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * | [eval](../../d5/df9/structApp_1_1Expression_1_1Component.html#a1357746aca36a0eea0e74f06f33356e8) () const  
Py::Object | [get](../../d5/df9/structApp_1_1Expression_1_1Component.html#a105ce2f55b1e32a78b7fe55f0be9789d) (const [Expression](../../dc/d5c/classApp_1_1Expression.html) *[owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35), const Py::Object &pyobj) const  
[bool](../../d9/db9/classbool.html) | [isTouched](../../d5/df9/structApp_1_1Expression_1_1Component.html#a5bcb4e846136883d4e4967f50917edda) () const  
[Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) & | [operator=](../../d5/df9/structApp_1_1Expression_1_1Component.html#afa738c6afd0ec6e1914499de235501da) (const [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) &)=delete  
void | [set](../../d5/df9/structApp_1_1Expression_1_1Component.html#a8f3a5ce94e26009bf81a428ec7726910) (const [Expression](../../dc/d5c/classApp_1_1Expression.html) *[owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35), Py::Object &pyobj, const Py::Object &value) const  
void | [toString](../../d5/df9/structApp_1_1Expression_1_1Component.html#af4a0ab6ec60fd3d073eafd68be9124fc) (std::ostream &ss, [bool](../../d9/db9/classbool.html) persistent) const  
void | [visit](../../d5/df9/structApp_1_1Expression_1_1Component.html#a67103ef42986cdaf5ad8eb718f21f849) ([ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html) &v)  
|
[~Component](../../d5/df9/structApp_1_1Expression_1_1Component.html#afe1a8f36278afe38cd43a9fd754291e4)
()  
  
##  Public Attributes  
  
---  
[ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [comp](../../d5/df9/structApp_1_1Expression_1_1Component.html#a94fca1ad12abb65a07ce46b7d86323ad)  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [e1](../../d5/df9/structApp_1_1Expression_1_1Component.html#a11a453a4609f87b7b441c619e4fc6521)  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [e2](../../d5/df9/structApp_1_1Expression_1_1Component.html#aaf1181d8d97e37d5e83987fe6ff5436d)  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [e3](../../d5/df9/structApp_1_1Expression_1_1Component.html#a1f6253abbd2650d7cb7ec1aa99640b69)  
  
## Constructor & Destructor Documentation

## ◆ Component() [1/4]

Expression::Component::Component  | ( | const std::string & | _n_| ) |   
---|---|---|---|---|---  
  
## ◆ Component() [2/4]

Expression::Component::Component  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _e1_ ,   
---|---|---|---  
|  | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _e2_ ,   
|  | [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _e3_ ,   
|  | [bool](../../d9/db9/classbool.html) | _isRange_ = `false`  
| ) | |   
  
References
[comp](../../d5/df9/structApp_1_1Expression_1_1Component.html#a94fca1ad12abb65a07ce46b7d86323ad),
[e2](../../d5/df9/structApp_1_1Expression_1_1Component.html#aaf1181d8d97e37d5e83987fe6ff5436d),
[e3](../../d5/df9/structApp_1_1Expression_1_1Component.html#a1f6253abbd2650d7cb7ec1aa99640b69),
and
[App::ObjectIdentifier::RangeComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ac4a5968e4f45d718d0d8b5a75895ca62).

## ◆ Component() [3/4]

Expression::Component::Component  | ( | const [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) & | _comp_| ) |   
---|---|---|---|---|---  
  
## ◆ Component() [4/4]

Expression::Component::Component  | ( | const [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) & | _other_| ) |   
---|---|---|---|---|---  
  
## ◆ ~Component()

Expression::Component::~Component  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ copy()

[Expression::Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * Expression::Component::copy  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ del()

void Expression::Component::del  | ( | const [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _owner_ ,   
---|---|---|---  
|  | Py::Object & | _pyobj_  
| ) | |  const  
  
References
[App::Expression::owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35),
and
[draftgeoutils.general::v1()](../../d9/dfd/group__draftgeoutils.html#ga07ad5262ee7b26511c5c3592f2681804).

## ◆ eval()

[Expression::Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * Expression::Component::eval  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ get()

Py::Object Expression::Component::get  | ( | const [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _owner_ ,   
---|---|---|---  
|  | const Py::Object & | _pyobj_  
| ) | |  const  
  
References
[App::Expression::owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35),
and
[draftgeoutils.general::v1()](../../d9/dfd/group__draftgeoutils.html#ga07ad5262ee7b26511c5c3592f2681804).

Referenced by
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297).

## ◆ isTouched()

[bool](../../d9/db9/classbool.html) Expression::Component::isTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
## ◆ operator=()

| [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) & App::Expression::Component::operator=  | ( | const [Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) & | | ) |   
---|---|---|---|---|---  
delete  
  
## ◆ set()

void Expression::Component::set  | ( | const [Expression](../../dc/d5c/classApp_1_1Expression.html) *  | _owner_ ,   
---|---|---|---  
|  | Py::Object & | _pyobj_ ,   
|  | const Py::Object & | _value_  
| ) | |  const  
  
References
[App::Expression::owner](../../dc/d5c/classApp_1_1Expression.html#a67ab4d0b4744456d8be2c96ad2c05d35),
and
[draftgeoutils.general::v1()](../../d9/dfd/group__draftgeoutils.html#ga07ad5262ee7b26511c5c3592f2681804).

Referenced by
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297).

## ◆ toString()

void Expression::Component::toString  | ( | std::ostream & | _ss_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _persistent_  
| ) | |  const  
  
## ◆ visit()

void Expression::Component::visit  | ( | [ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html) & | _v_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ comp

[ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html)
App::Expression::Component::comp  
---  
  
Referenced by
[Component()](../../d5/df9/structApp_1_1Expression_1_1Component.html#a3d256c4ce032f643c24480f681cc52dc).

## ◆ e1

[Expression](../../dc/d5c/classApp_1_1Expression.html)*
App::Expression::Component::e1  
---  
  
## ◆ e2

[Expression](../../dc/d5c/classApp_1_1Expression.html)*
App::Expression::Component::e2  
---  
  
Referenced by
[Component()](../../d5/df9/structApp_1_1Expression_1_1Component.html#a3d256c4ce032f643c24480f681cc52dc).

## ◆ e3

[Expression](../../dc/d5c/classApp_1_1Expression.html)*
App::Expression::Component::e3  
---  
  
Referenced by
[Component()](../../d5/df9/structApp_1_1Expression_1_1Component.html#a3d256c4ce032f643c24480f681cc52dc).

* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/App/ExpressionParser.h
  * FreeCAD/src/App/Expression.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

