---
url: https://freecad.github.io/SourceDoc/d8/d68/classApp_1_1ExpressionVisitor.html
scraped_at: 2025-09-08T14:54:40.486637
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html)

[List of all members](../../d4/d73/classApp_1_1ExpressionVisitor-members.html) | Public Member Functions | Protected Member Functions

App::ExpressionVisitor Class Referenceabstract

`#include <Expression.h>`

##  Public Member Functions  
  
---  
virtual void | [aboutToChange](../../d8/d68/classApp_1_1ExpressionVisitor.html#ae9d73e7357058a579c776b6523c6a873) ()  
virtual [int](../../d1/da0/classint.html) | [changed](../../d8/d68/classApp_1_1ExpressionVisitor.html#a302e279e154e090e5d9320696b60cb65) () const  
virtual [App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) * | [getPropertyLink](../../d8/d68/classApp_1_1ExpressionVisitor.html#a66476aaa07f4dd08eb4012b66ef1417e) ()  
virtual void | [reset](../../d8/d68/classApp_1_1ExpressionVisitor.html#ae2944cf33bfce1141669a91c5ac32ab0) ()  
virtual void | [visit](../../d8/d68/classApp_1_1ExpressionVisitor.html#ae17dbcdd0cdb64200575f035b24897ae) ([Expression](../../dc/d5c/classApp_1_1Expression.html) &e)=0  
virtual | [~ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html#ab63e036d6775692d5686b48131df69d7) ()  
  
##  Protected Member Functions  
  
---  
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

## ◆ ~ExpressionVisitor()

| virtual App::ExpressionVisitor::~ExpressionVisitor  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ aboutToChange()

| virtual void App::ExpressionVisitor::aboutToChange  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Reimplemented in [App::ExpressionModifier< P
>](../../d3/d26/classApp_1_1ExpressionModifier.html#ae4fbeea272841bf0cec58d962cae11d9).

## ◆ adjustLinks()

| [bool](../../d9/db9/classbool.html) ExpressionVisitor::adjustLinks  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_ ,   
---|---|---|---  
|  | const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _inList_  
| ) | |   
protected  
  
## ◆ changed()

| virtual [int](../../d1/da0/classint.html) App::ExpressionVisitor::changed  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reimplemented in [App::ExpressionModifier< P
>](../../d3/d26/classApp_1_1ExpressionModifier.html#ad378a374707110a69eabe92478d8ad08).

## ◆ collectReplacement()

| void ExpressionVisitor::collectReplacement  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_ ,   
---|---|---|---  
|  | std::map< [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > & | _paths_ ,   
|  | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _oldObj_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _newObj_  
| ) | |  const  
protected  
  
## ◆ getIdentifiers()

| void ExpressionVisitor::getIdentifiers  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_ ,   
---|---|---|---  
|  | std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [bool](../../d9/db9/classbool.html) > & | _ids_  
| ) | |   
protected  
  
## ◆ getPropertyLink()

| virtual [App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) * App::ExpressionVisitor::getPropertyLink  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Reimplemented in [App::ExpressionModifier< P
>](../../d3/d26/classApp_1_1ExpressionModifier.html#ac03922db1b8dbcdbe1fc96ffa906a4fd).

## ◆ importSubNames()

| void ExpressionVisitor::importSubNames  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_ ,   
---|---|---|---  
|  | const [ObjectIdentifier::SubNameMap](../../dd/d13/classApp_1_1ObjectIdentifier.html#af60f586ff5580cd84c3d6828bdc3a767) & | _subNameMap_  
| ) | |   
protected  
  
## ◆ moveCells()

| void ExpressionVisitor::moveCells  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_ ,   
---|---|---|---  
|  | const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) & | _address_ ,   
|  | [int](../../d1/da0/classint.html) | _rowCount_ ,   
|  | [int](../../d1/da0/classint.html) | _colCount_  
| ) | |   
protected  
  
Referenced by [App::MoveCellsExpressionVisitor< P
>::visit()](../../db/d01/classApp_1_1MoveCellsExpressionVisitor.html#ae2d99b6311207d68a82f6185e3d05fe5).

## ◆ offsetCells()

| void ExpressionVisitor::offsetCells  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _rowOffset_ ,   
|  | [int](../../d1/da0/classint.html) | _colOffset_  
| ) | |   
protected  
  
Referenced by [App::OffsetCellsExpressionVisitor< P
>::visit()](../../d9/dcf/classApp_1_1OffsetCellsExpressionVisitor.html#acd77e6aba9264896c9d24bbfb709363b).

## ◆ relabeledDocument()

| [bool](../../d9/db9/classbool.html) ExpressionVisitor::relabeledDocument  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_ ,   
---|---|---|---  
|  | const std::string & | _oldName_ ,   
|  | const std::string & | _newName_  
| ) | |   
protected  
  
Referenced by
[App::RelabelDocumentExpressionVisitor::visit()](../../db/dfd/classApp_1_1RelabelDocumentExpressionVisitor.html#aa37c20588af574df4ceaa95468660f18).

## ◆ renameObjectIdentifier()

| [bool](../../d9/db9/classbool.html) ExpressionVisitor::renameObjectIdentifier  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_ ,   
---|---|---|---  
|  | const std::map< [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > & | _paths_ ,   
|  | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_  
| ) | |   
protected  
  
Referenced by [App::RenameObjectIdentifierExpressionVisitor< P
>::visit()](../../d9/d52/classApp_1_1RenameObjectIdentifierExpressionVisitor.html#a4438b83a01fe79a809a656736b04286b).

## ◆ reset()

| virtual void App::ExpressionVisitor::reset  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Reimplemented in [App::ExpressionModifier< P
>](../../d3/d26/classApp_1_1ExpressionModifier.html#ad11640180616ad4cdf3b18e9966da188).

Referenced by
[draftguitools.gui_trackers.gridTracker::set()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a1499cdcfd43fe110d46cd9c72c52b356).

## ◆ updateElementReference()

| [bool](../../d9/db9/classbool.html) ExpressionVisitor::updateElementReference  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _feature_ ,   
|  | [bool](../../d9/db9/classbool.html) | _reverse_  
| ) | |   
protected  
  
Referenced by [App::UpdateElementReferenceExpressionVisitor< P
>::visit()](../../d3/d63/classApp_1_1UpdateElementReferenceExpressionVisitor.html#a699cc53051632b8a1d3799f5b52eca20).

## ◆ updateLabelReference()

| void ExpressionVisitor::updateLabelReference  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
|  | const std::string & | _ref_ ,   
|  | const char *  | _newLabel_  
| ) | |   
protected  
  
## ◆ visit()

| virtual void App::ExpressionVisitor::visit  | ( | [Expression](../../dc/d5c/classApp_1_1Expression.html) & | _e_| ) |   
---|---|---|---|---|---  
pure virtual  
  
Implemented in
[GetIdentifiersExpressionVisitor](../../da/d35/classGetIdentifiersExpressionVisitor.html#ae4e2ee048ae03f3ec98f6e9807dbd7f8),
[AdjustLinksExpressionVisitor](../../d2/dfa/classAdjustLinksExpressionVisitor.html#a107aaf772feed375a13a19a9453c7caa),
[ImportSubNamesExpressionVisitor](../../d9/d49/classImportSubNamesExpressionVisitor.html#a834f8c90120e9e8f51d0028de289d3c8),
[UpdateLabelExpressionVisitor](../../d3/d25/classUpdateLabelExpressionVisitor.html#a95c349330b431b4c1d1568177abc2bcf),
[ReplaceObjectExpressionVisitor](../../d8/da6/classReplaceObjectExpressionVisitor.html#a8f3001501d73eb4090f44a4a3a7b3717),
[App::RenameObjectIdentifierExpressionVisitor< P
>](../../d9/d52/classApp_1_1RenameObjectIdentifierExpressionVisitor.html#a4438b83a01fe79a809a656736b04286b),
[App::UpdateElementReferenceExpressionVisitor< P
>](../../d3/d63/classApp_1_1UpdateElementReferenceExpressionVisitor.html#a699cc53051632b8a1d3799f5b52eca20),
[App::RelabelDocumentExpressionVisitor](../../db/dfd/classApp_1_1RelabelDocumentExpressionVisitor.html#aa37c20588af574df4ceaa95468660f18),
[App::MoveCellsExpressionVisitor< P
>](../../db/d01/classApp_1_1MoveCellsExpressionVisitor.html#ae2d99b6311207d68a82f6185e3d05fe5),
and [App::OffsetCellsExpressionVisitor< P
>](../../d9/dcf/classApp_1_1OffsetCellsExpressionVisitor.html#acd77e6aba9264896c9d24bbfb709363b).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Expression.h
  * FreeCAD/src/App/Expression.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

