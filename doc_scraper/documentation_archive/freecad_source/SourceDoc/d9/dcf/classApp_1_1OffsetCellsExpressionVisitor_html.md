---
url: https://freecad.github.io/SourceDoc/d9/dcf/classApp_1_1OffsetCellsExpressionVisitor.html
scraped_at: 2025-09-08T14:55:16.606559
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [OffsetCellsExpressionVisitor](../../d9/dcf/classApp_1_1OffsetCellsExpressionVisitor.html)

[List of all members](../../d6/d97/classApp_1_1OffsetCellsExpressionVisitor-members.html) | Public Member Functions

App::OffsetCellsExpressionVisitor< P > Class Template Reference

`#include <ExpressionVisitors.h>`

##  Public Member Functions  
  
---  
|
[OffsetCellsExpressionVisitor](../../d9/dcf/classApp_1_1OffsetCellsExpressionVisitor.html#a193b9e251aa64eac75326bfdc4b86e30)
(P
&[prop](../../d3/d26/classApp_1_1ExpressionModifier.html#a41710f1669f00e6ea1e6147d32c1f4fd),
[int](../../d1/da0/classint.html) rowOffset, [int](../../d1/da0/classint.html)
colOffset)  
void | [visit](../../d9/dcf/classApp_1_1OffsetCellsExpressionVisitor.html#acd77e6aba9264896c9d24bbfb709363b) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &node)  
![-](../../closed.png) Public Member Functions inherited from
[App::ExpressionModifier< P
>](../../d3/d26/classApp_1_1ExpressionModifier.html)  
virtual void | [aboutToChange](../../d3/d26/classApp_1_1ExpressionModifier.html#ae4fbeea272841bf0cec58d962cae11d9) () override  
virtual [int](../../d1/da0/classint.html) | [changed](../../d3/d26/classApp_1_1ExpressionModifier.html#ad378a374707110a69eabe92478d8ad08) () const override  
|
[ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html#ab6573d6dc66bcee8e96cc401c139b5c1)
(P &_prop)  
virtual [App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) * | [getPropertyLink](../../d3/d26/classApp_1_1ExpressionModifier.html#ac03922db1b8dbcdbe1fc96ffa906a4fd) () override  
virtual void | [reset](../../d3/d26/classApp_1_1ExpressionModifier.html#ad11640180616ad4cdf3b18e9966da188) () override  
virtual | [~ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html#a4a74ef9978abd5363b6c48c057e3c885) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html)  
virtual void | [aboutToChange](../../d8/d68/classApp_1_1ExpressionVisitor.html#ae9d73e7357058a579c776b6523c6a873) ()  
virtual [int](../../d1/da0/classint.html) | [changed](../../d8/d68/classApp_1_1ExpressionVisitor.html#a302e279e154e090e5d9320696b60cb65) () const  
virtual [App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) * | [getPropertyLink](../../d8/d68/classApp_1_1ExpressionVisitor.html#a66476aaa07f4dd08eb4012b66ef1417e) ()  
virtual void | [reset](../../d8/d68/classApp_1_1ExpressionVisitor.html#ae2944cf33bfce1141669a91c5ac32ab0) ()  
virtual void | [visit](../../d8/d68/classApp_1_1ExpressionVisitor.html#ae17dbcdd0cdb64200575f035b24897ae) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e)=0  
virtual | [~ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html#ab63e036d6775692d5686b48131df69d7) ()  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Protected Member Functions inherited from
[App::ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html)  
[bool](../../d9/db9/classbool.html) | [adjustLinks](../../d8/d68/classApp_1_1ExpressionVisitor.html#a6f81f1f1cb51103177d885f837e615e9) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e, const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList)  
void | [collectReplacement](../../d8/d68/classApp_1_1ExpressionVisitor.html#ad29bac289477cc4039dcd9f177b640a4) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e, std::map< [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj) const  
void | [getIdentifiers](../../d8/d68/classApp_1_1ExpressionVisitor.html#a8b45f86ba125dc8aca795a59a463e8d1) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e, std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [bool](../../d9/db9/classbool.html) > &)  
void | [importSubNames](../../d8/d68/classApp_1_1ExpressionVisitor.html#a8044cb89e1937833db844207c110e9d2) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e, const [ObjectIdentifier::SubNameMap](../../dd/d13/classApp_1_1ObjectIdentifier.html#af60f586ff5580cd84c3d6828bdc3a767) &subNameMap)  
void | [moveCells](../../d8/d68/classApp_1_1ExpressionVisitor.html#afe6a46688e78f0bdec4d4396dc540f2a) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e, const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) &address, [int](../../d1/da0/classint.html) rowCount, [int](../../d1/da0/classint.html) colCount)  
void | [offsetCells](../../d8/d68/classApp_1_1ExpressionVisitor.html#aa8ee2b18bb634505962645c280dd7cfb) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e, [int](../../d1/da0/classint.html) rowOffset, [int](../../d1/da0/classint.html) colOffset)  
[bool](../../d9/db9/classbool.html) | [relabeledDocument](../../d8/d68/classApp_1_1ExpressionVisitor.html#aa7ef2044ce4192301ceb1564d435fd6c) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e, const std::string &oldName, const std::string &newName)  
[bool](../../d9/db9/classbool.html) | [renameObjectIdentifier](../../d8/d68/classApp_1_1ExpressionVisitor.html#a4aa49136b116318da6efe47039299333) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e, const std::map< [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &, const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &)  
[bool](../../d9/db9/classbool.html) | [updateElementReference](../../d8/d68/classApp_1_1ExpressionVisitor.html#acb69874ccbfb1fd40dacea06aabe00c3) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *feature, [bool](../../d9/db9/classbool.html) reverse)  
void | [updateLabelReference](../../d8/d68/classApp_1_1ExpressionVisitor.html#a477ea5575436e9d62e4a8f06d51eec48) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &ref, const char *newLabel)  
![-](../../closed.png) Protected Attributes inherited from
[App::ExpressionModifier< P
>](../../d3/d26/classApp_1_1ExpressionModifier.html)  
P & | [prop](../../d3/d26/classApp_1_1ExpressionModifier.html#a41710f1669f00e6ea1e6147d32c1f4fd)  
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) * | [propLink](../../d3/d26/classApp_1_1ExpressionModifier.html#aeafc4d8288401b65bbc7ec8fd8bd8ad0)  
[AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)< P >::AtomicPropertyChange | [signaller](../../d3/d26/classApp_1_1ExpressionModifier.html#a410f360b761c56665a369a31177659ef)  
  
## Constructor & Destructor Documentation

## ◆ OffsetCellsExpressionVisitor()

template<class P >

[App::OffsetCellsExpressionVisitor](../../d9/dcf/classApp_1_1OffsetCellsExpressionVisitor.html)< P >::OffsetCellsExpressionVisitor  | ( | P & | _prop_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _rowOffset_ ,   
|  | [int](../../d1/da0/classint.html) | _colOffset_  
| ) | |   
  
## Member Function Documentation

## ◆ visit()

template<class P >

| void [App::OffsetCellsExpressionVisitor](../../d9/dcf/classApp_1_1OffsetCellsExpressionVisitor.html)< P >::visit  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _node_| ) |   
---|---|---|---|---|---  
virtual  
  
Implements
[App::ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html#ae17dbcdd0cdb64200575f035b24897ae).

References
[App::ExpressionVisitor::offsetCells()](../../d8/d68/classApp_1_1ExpressionVisitor.html#aa8ee2b18bb634505962645c280dd7cfb).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/ExpressionVisitors.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

