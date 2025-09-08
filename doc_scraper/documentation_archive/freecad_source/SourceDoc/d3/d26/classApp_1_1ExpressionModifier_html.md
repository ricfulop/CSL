---
url: https://freecad.github.io/SourceDoc/d3/d26/classApp_1_1ExpressionModifier.html
scraped_at: 2025-09-08T14:54:39.473445
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html)

[List of all members](../../d0/d7e/classApp_1_1ExpressionModifier-members.html) | Public Member Functions | Protected Attributes

App::ExpressionModifier< P > Class Template Reference

`#include <Expression.h>`

##  Public Member Functions  
  
---  
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
  
##  Protected Attributes  
  
---  
P & | [prop](../../d3/d26/classApp_1_1ExpressionModifier.html#a41710f1669f00e6ea1e6147d32c1f4fd)  
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) * | [propLink](../../d3/d26/classApp_1_1ExpressionModifier.html#aeafc4d8288401b65bbc7ec8fd8bd8ad0)  
[AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)< P >::AtomicPropertyChange | [signaller](../../d3/d26/classApp_1_1ExpressionModifier.html#a410f360b761c56665a369a31177659ef)  
  
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

## ◆ ExpressionModifier()

template<class P >

[App::ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html)< P >::ExpressionModifier  | ( | P & | __prop_| ) |   
---|---|---|---|---|---  
  
## ◆ ~ExpressionModifier()

template<class P >

| virtual [App::ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html)< P >::~[ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html) | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ aboutToChange()

template<class P >

| virtual void [App::ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html)< P >::aboutToChange  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html#ae9d73e7357058a579c776b6523c6a873).

References [App::ExpressionModifier< P
>::signaller](../../d3/d26/classApp_1_1ExpressionModifier.html#a410f360b761c56665a369a31177659ef).

## ◆ changed()

template<class P >

| virtual [int](../../d1/da0/classint.html) [App::ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html)< P >::changed  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html#a302e279e154e090e5d9320696b60cb65).

Referenced by
[Spreadsheet::PropertySheet::insertColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a265014a33975e005189793fb75251c56),
[Spreadsheet::PropertySheet::insertRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aa84f3f19aed8b5355d16cece5eb4a5d9),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
[Spreadsheet::PropertySheet::removeColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ada4ceb76fd79dc130476fe307f77e0a1),
[Spreadsheet::PropertySheet::removeRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5ff589d68c79b8387678e38007f8733f),
and
[Spreadsheet::PropertySheet::updateElementReference()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a35d58b0bf7eac198ffdae31e16f3173f).

## ◆ getPropertyLink()

template<class P >

| virtual [App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html) * [App::ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html)< P >::getPropertyLink  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html#a66476aaa07f4dd08eb4012b66ef1417e).

References [App::ExpressionModifier< P
>::propLink](../../d3/d26/classApp_1_1ExpressionModifier.html#aeafc4d8288401b65bbc7ec8fd8bd8ad0).

## ◆ reset()

template<class P >

| virtual void [App::ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html)< P >::reset  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html#ae2944cf33bfce1141669a91c5ac32ab0).

Referenced by
[Spreadsheet::PropertySheet::insertColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a265014a33975e005189793fb75251c56),
[Spreadsheet::PropertySheet::insertRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aa84f3f19aed8b5355d16cece5eb4a5d9),
[Spreadsheet::PropertySheet::removeColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ada4ceb76fd79dc130476fe307f77e0a1),
[Spreadsheet::PropertySheet::removeRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5ff589d68c79b8387678e38007f8733f),
and
[draftguitools.gui_trackers.gridTracker::set()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a1499cdcfd43fe110d46cd9c72c52b356).

## Member Data Documentation

## ◆ prop

template<class P >

| P&
[App::ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html)< P
>::prop  
---  
protected  
  
Referenced by
[PathScripts.PathGui.QuantitySpinBox::attachTo()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a5e9cf40f8eebcec079cce737d16e7ba2),
[PathScripts.PathGui.QuantitySpinBox::expression()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a7cacc0f52eee6defe471445d1e033c09),
[PathScripts.PathGui.QuantitySpinBox::setMinimum()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#abe63fa96792984b9db4e9d65b1917c7b),
[PathScripts.PathGui.QuantitySpinBox::updateProperty()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a8b9b202d7b495b666cb1f6b41ab2beb4),
and
[PathScripts.PathGui.QuantitySpinBox::updateSpinBox()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a64f2463956148b67f6fe2c4173a96c4d).

## ◆ propLink

template<class P >

| [App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)*
[App::ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html)< P
>::propLink  
---  
protected  
  
Referenced by [App::ExpressionModifier< P
>::getPropertyLink()](../../d3/d26/classApp_1_1ExpressionModifier.html#ac03922db1b8dbcdbe1fc96ffa906a4fd).

## ◆ signaller

template<class P >

|
[AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)<P>::AtomicPropertyChange
[App::ExpressionModifier](../../d3/d26/classApp_1_1ExpressionModifier.html)< P
>::signaller  
---  
protected  
  
Referenced by [App::ExpressionModifier< P
>::aboutToChange()](../../d3/d26/classApp_1_1ExpressionModifier.html#ae4fbeea272841bf0cec58d962cae11d9).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/Expression.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

