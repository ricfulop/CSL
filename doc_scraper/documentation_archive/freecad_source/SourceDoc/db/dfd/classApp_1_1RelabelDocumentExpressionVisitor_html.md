---
url: https://freecad.github.io/SourceDoc/db/dfd/classApp_1_1RelabelDocumentExpressionVisitor.html
scraped_at: 2025-09-08T14:57:02.051667
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [RelabelDocumentExpressionVisitor](../../db/dfd/classApp_1_1RelabelDocumentExpressionVisitor.html)

[List of all members](../../dc/dfe/classApp_1_1RelabelDocumentExpressionVisitor-members.html) | Public Member Functions

App::RelabelDocumentExpressionVisitor Class Reference

`#include <ExpressionVisitors.h>`

##  Public Member Functions  
  
---  
|
[RelabelDocumentExpressionVisitor](../../db/dfd/classApp_1_1RelabelDocumentExpressionVisitor.html#a19b5eeea5dfd6fdf01c22d3347216871)
(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &doc)  
void | [visit](../../db/dfd/classApp_1_1RelabelDocumentExpressionVisitor.html#aa37c20588af574df4ceaa95468660f18) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &node)  
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
  
## Constructor & Destructor Documentation

## ◆ RelabelDocumentExpressionVisitor()

App::RelabelDocumentExpressionVisitor::RelabelDocumentExpressionVisitor  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_| ) |   
---|---|---|---|---|---  
  
## Member Function Documentation

## ◆ visit()

| void App::RelabelDocumentExpressionVisitor::visit  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _node_| ) |   
---|---|---|---|---|---  
virtual  
  
Implements
[App::ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html#ae17dbcdd0cdb64200575f035b24897ae).

References
[App::Document::getOldLabel()](../../d8/d3e/classApp_1_1Document.html#a1ff3b7f5aeefa7af1449d0f23616d4fc),
[App::PropertyString::getStrValue()](../../dd/df8/classApp_1_1PropertyString.html#a7fdb947ab6f9552c1dd95a8e634c83c2),
[App::Document::Label](../../d8/d3e/classApp_1_1Document.html#a195e9cb1707d0c92d938ec751d8b0a81),
and
[App::ExpressionVisitor::relabeledDocument()](../../d8/d68/classApp_1_1ExpressionVisitor.html#aa7ef2044ce4192301ceb1564d435fd6c).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/ExpressionVisitors.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

