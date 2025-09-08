---
url: https://freecad.github.io/SourceDoc/dd/d94/structApp_1_1CellAddress.html
scraped_at: 2025-09-08T14:53:49.269731
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [CellAddress](../../dd/d94/structApp_1_1CellAddress.html)

[List of all members](../../df/d2e/structApp_1_1CellAddress-members.html) | Public Types | Public Member Functions | Static Public Attributes | Protected Member Functions

App::CellAddress Struct Reference

`#include <Range.h>`

##  Public Types  
  
---  
enum class | [Cell](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457d) {   
[Absolute](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457dab51ca26c6c89cfc9bec338f7a0d3e0c8) = 1 , [ShowRow](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457da9e3485ea601b88929849497aaeef743e) = 2 , [ShowColumn](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457da4660c9a61cc740f69cf4a57ebec570ac) = 4 , [ShowRowColumn](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457da61f9d5e0dd1062ffc2e63db7c7de6345) = ShowRow | ShowColumn ,   
[ShowFull](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457daba9363fe738be46bc510592388082a95) = Absolute | ShowRow | ShowColumn   
}  
  
##  Public Member Functions  
  
---  
|
[CellAddress](../../dd/d94/structApp_1_1CellAddress.html#ac7e83a542aff14632b3fb73fabce12d0)
(const char *address)  
|
[CellAddress](../../dd/d94/structApp_1_1CellAddress.html#a34ba9bd77ecd7a5f95c5122dfbb92365)
(const std::string &address)  
|
[CellAddress](../../dd/d94/structApp_1_1CellAddress.html#a913e97ee9a5e2803cb17dc5a2943f178)
([int](../../d1/da0/classint.html)
[row](../../dd/d94/structApp_1_1CellAddress.html#a2da9b96fa1f929f491dc9d74b93ceea6)=-1,
[int](../../d1/da0/classint.html)
[col](../../dd/d94/structApp_1_1CellAddress.html#a1076b5b4b1899f89f3e79a03abe48ddb)=-1,
[bool](../../d9/db9/classbool.html) absRow=false,
[bool](../../d9/db9/classbool.html) absCol=false)  
[int](../../d1/da0/classint.html) | [col](../../dd/d94/structApp_1_1CellAddress.html#a1076b5b4b1899f89f3e79a03abe48ddb) () const  
[bool](../../d9/db9/classbool.html) | [isAbsoluteCol](../../dd/d94/structApp_1_1CellAddress.html#a086a76545a4347dc8b61ff65d9e3e5dd) () const  
[bool](../../d9/db9/classbool.html) | [isAbsoluteRow](../../dd/d94/structApp_1_1CellAddress.html#af68bd149c7917dad0b76a6719a4c8276) () const  
[bool](../../d9/db9/classbool.html) | [isValid](../../dd/d94/structApp_1_1CellAddress.html#a8f8854230ec272ceccea78aa6405ef7d) ()  
[bool](../../d9/db9/classbool.html) | [operator!=](../../dd/d94/structApp_1_1CellAddress.html#a4d9d091e08ec1189795b57785b95e9a1) (const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) &other) const  
[bool](../../d9/db9/classbool.html) | [operator<](../../dd/d94/structApp_1_1CellAddress.html#a008214cd9450ef8767ece4f76e997721) (const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) &other) const  
[bool](../../d9/db9/classbool.html) | [operator==](../../dd/d94/structApp_1_1CellAddress.html#ada0d7339870ae922dcb96701cb2e9858) (const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) &other) const  
[bool](../../d9/db9/classbool.html) | [operator>](../../dd/d94/structApp_1_1CellAddress.html#acf8ef4e48a852dc4c3ad4442678af310) (const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) &other) const  
[bool](../../d9/db9/classbool.html) | [parseAbsoluteAddress](../../dd/d94/structApp_1_1CellAddress.html#ac349f371300d7b3ee08549f491db7f0a) (const char *txt)  
[int](../../d1/da0/classint.html) | [row](../../dd/d94/structApp_1_1CellAddress.html#a2da9b96fa1f929f491dc9d74b93ceea6) () const  
void | [setCol](../../dd/d94/structApp_1_1CellAddress.html#abf7d37650eb95083454a3bfb4d819b25) ([int](../../d1/da0/classint.html) c, [bool](../../d9/db9/classbool.html) clip=false)  
void | [setRow](../../dd/d94/structApp_1_1CellAddress.html#a44173fedb6c84bad2cd8bdab1636cf56) ([int](../../d1/da0/classint.html) r, [bool](../../d9/db9/classbool.html) clip=false)  
std::string | [toString](../../dd/d94/structApp_1_1CellAddress.html#ade22dc6292d5004bb7fdd315ce64fc8d) ([Cell](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457d)=[Cell::ShowFull](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457daba9363fe738be46bc510592388082a95)) const  
| Convert given _cell_ address into its string representation.
[More...](../../dd/d94/structApp_1_1CellAddress.html#ade22dc6292d5004bb7fdd315ce64fc8d)  
  
  
##  Static Public Attributes  
  
---  
static const [int](../../d1/da0/classint.html) | [MAX_COLUMNS](../../dd/d94/structApp_1_1CellAddress.html#a01078a498612c29225b3842d0e47356f) = 26 * 26 + 26  
static const [int](../../d1/da0/classint.html) | [MAX_ROWS](../../dd/d94/structApp_1_1CellAddress.html#a42516da60a77984ac34c98586179f9da) = 16384  
  
##  Protected Member Functions  
  
---  
unsigned [int](../../d1/da0/classint.html) | [asInt](../../dd/d94/structApp_1_1CellAddress.html#ae1d620b3f90f827972cf708e8aab7554) () const  
  
## Member Enumeration Documentation

## ◆ Cell

| enum class
[App::CellAddress::Cell](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457d)  
---  
strong  
  
Enumerator  
---  
Absolute |   
ShowRow |   
ShowColumn |   
ShowRowColumn |   
ShowFull |   
  
## Constructor & Destructor Documentation

## ◆ CellAddress() [1/3]

App::CellAddress::CellAddress  | ( | [int](../../d1/da0/classint.html) | _row_ = `-1`,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _col_ = `-1`,   
|  | [bool](../../d9/db9/classbool.html) | _absRow_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _absCol_ = `false`  
| ) | |   
  
## ◆ CellAddress() [2/3]

App::CellAddress::CellAddress  | ( | const char *  | _address_| ) |   
---|---|---|---|---|---  
  
References
[App::stringToAddress()](../../dd/dc2/namespaceApp.html#ac31050416f7fd21ed326ecb0534e4e60).

## ◆ CellAddress() [3/3]

App::CellAddress::CellAddress  | ( | const std::string & | _address_| ) |   
---|---|---|---|---|---  
  
References
[App::stringToAddress()](../../dd/dc2/namespaceApp.html#ac31050416f7fd21ed326ecb0534e4e60).

## Member Function Documentation

## ◆ asInt()

| unsigned [int](../../d1/da0/classint.html) App::CellAddress::asInt  | ( | | ) |  const  
---|---|---|---|---  
protected  
  
Referenced by
[operator!=()](../../dd/d94/structApp_1_1CellAddress.html#a4d9d091e08ec1189795b57785b95e9a1),
[operator<()](../../dd/d94/structApp_1_1CellAddress.html#a008214cd9450ef8767ece4f76e997721),
[operator==()](../../dd/d94/structApp_1_1CellAddress.html#ada0d7339870ae922dcb96701cb2e9858),
and
[operator>()](../../dd/d94/structApp_1_1CellAddress.html#acf8ef4e48a852dc4c3ad4442678af310).

## ◆ col()

[int](../../d1/da0/classint.html) App::CellAddress::col  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[SpreadsheetGui::DlgSheetConf::accept()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#aa4fefe42d2485471443e738600091ce0),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Spreadsheet::PropertySheet::getRange()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#adfb27dcec7bdf5e5f79ff4cced029a2e),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[Spreadsheet::PropertySheet::mergeCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad33ba60621c10ca7fbfa5f257ab351e1),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
[SpreadsheetGui::SheetTableView::pasteClipboard()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a515807fe0797c9e6f83f28139009c68a),
[SpreadsheetGui::DlgSheetConf::prepare()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#abfbeb695362f8ae8074215c61a254de3),
[App::Range::Range()](../../dd/dc1/classApp_1_1Range.html#aebaca32b6c237dd7cda121fc2579acba),
[SpreadsheetGui::SheetView::select()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a88439f59c04e53982c193a9360d4f405),
[SpreadsheetGui::SheetView::setCurrentIndex()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a1b9cb2bb51510708409551b824e32067),
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede),
and
[Spreadsheet::PropertySheet::splitCell()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad4722b806c7d1df5b35340be8f879d4a).

## ◆ isAbsoluteCol()

[bool](../../d9/db9/classbool.html) App::CellAddress::isAbsoluteCol  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isAbsoluteRow()

[bool](../../d9/db9/classbool.html) App::CellAddress::isAbsoluteRow  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isValid()

[bool](../../d9/db9/classbool.html) App::CellAddress::isValid  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Referenced by
[SpreadsheetGui::DlgBindSheet::accept()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#ad6e5cb0995aaa1341a57bdb97ed49cbd),
[Spreadsheet::PropertySheet::getPyValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a345cfadf9398442bb9a94bd6d1fc10f0),
[Spreadsheet::PropertySheet::getRange()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#adfb27dcec7bdf5e5f79ff4cced029a2e),
and
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) App::CellAddress::operator!=  | ( | const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
References
[asInt()](../../dd/d94/structApp_1_1CellAddress.html#ae1d620b3f90f827972cf708e8aab7554).

## ◆ operator<()

[bool](../../d9/db9/classbool.html) App::CellAddress::operator< | ( | const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
References
[asInt()](../../dd/d94/structApp_1_1CellAddress.html#ae1d620b3f90f827972cf708e8aab7554).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) App::CellAddress::operator==  | ( | const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
References
[asInt()](../../dd/d94/structApp_1_1CellAddress.html#ae1d620b3f90f827972cf708e8aab7554).

## ◆ operator>()

[bool](../../d9/db9/classbool.html) App::CellAddress::operator> | ( | const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
References
[asInt()](../../dd/d94/structApp_1_1CellAddress.html#ae1d620b3f90f827972cf708e8aab7554).

## ◆ parseAbsoluteAddress()

[bool](../../d9/db9/classbool.html) App::CellAddress::parseAbsoluteAddress  | ( | const char *  | _txt_| ) |   
---|---|---|---|---|---  
  
References
[App::stringToAddress()](../../dd/dc2/namespaceApp.html#ac31050416f7fd21ed326ecb0534e4e60).

Referenced by
[App::ObjectIdentifier::verify()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ae666a62d2fc3b423b86f3d370e6edb11).

## ◆ row()

[int](../../d1/da0/classint.html) App::CellAddress::row  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[SpreadsheetGui::DlgSheetConf::accept()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#aa4fefe42d2485471443e738600091ce0),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Spreadsheet::PropertySheet::getRange()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#adfb27dcec7bdf5e5f79ff4cced029a2e),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[Spreadsheet::PropertySheet::mergeCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad33ba60621c10ca7fbfa5f257ab351e1),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
[SpreadsheetGui::SheetTableView::pasteClipboard()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a515807fe0797c9e6f83f28139009c68a),
[SpreadsheetGui::DlgSheetConf::prepare()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#abfbeb695362f8ae8074215c61a254de3),
[App::Range::Range()](../../dd/dc1/classApp_1_1Range.html#aebaca32b6c237dd7cda121fc2579acba),
[SpreadsheetGui::SheetView::select()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a88439f59c04e53982c193a9360d4f405),
[SpreadsheetGui::SheetView::setCurrentIndex()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a1b9cb2bb51510708409551b824e32067),
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede),
and
[Spreadsheet::PropertySheet::splitCell()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad4722b806c7d1df5b35340be8f879d4a).

## ◆ setCol()

void App::CellAddress::setCol  | ( | [int](../../d1/da0/classint.html) | _c_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _clip_ = `false`  
| ) | |   
  
Referenced by
[Spreadsheet::PropertySheet::getRange()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#adfb27dcec7bdf5e5f79ff4cced029a2e),
and
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede).

## ◆ setRow()

void App::CellAddress::setRow  | ( | [int](../../d1/da0/classint.html) | _r_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _clip_ = `false`  
| ) | |   
  
Referenced by
[Spreadsheet::PropertySheet::getRange()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#adfb27dcec7bdf5e5f79ff4cced029a2e),
[SpreadsheetGui::DlgSheetConf::prepare()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#abfbeb695362f8ae8074215c61a254de3),
and
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede).

## ◆ toString()

std::string App::CellAddress::toString  | ( | [Cell](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457d) | _cell_ = `[Cell::ShowFull](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457daba9363fe738be46bc510592388082a95)`| ) |  const  
---|---|---|---|---|---  
  
Convert given _cell_ address into its string representation.

Returns

    Address given as a string. 

Referenced by
[SpreadsheetGui::DlgSheetConf::accept()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#aa4fefe42d2485471443e738600091ce0),
[App::Range::address()](../../dd/dc1/classApp_1_1Range.html#a74c22ecd2bcbccc0b0e187e0968765a9),
[SpreadsheetGui::SheetView::confirmAliasChanged()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a417a33ce8aa3a831fed85c08876f84ba),
[SpreadsheetGui::SheetViewPy::currentIndex()](../../d7/d63/classSpreadsheetGui_1_1SheetViewPy.html#af76132ac3ca04587ef088fdbac2434de),
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[SpreadsheetGui::DlgSheetConf::DlgSheetConf()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#ae5a809ca03b0e1ead7ddcbe721aa1098),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[App::Range::fromCellString()](../../dd/dc1/classApp_1_1Range.html#ac44f4d906f5e0a0d6ce5b49aba48caa9),
[Spreadsheet::Sheet::getAddressFromAlias()](../../d0/da8/classSpreadsheet_1_1Sheet.html#ac379f22600dd6dae503aac7f3ef654d4),
[Spreadsheet::Cell::getFormattedQuantity()](../../d5/d22/classSpreadsheet_1_1Cell.html#a66a4fb5ffaa93232823dfbe49833ab7b),
[Spreadsheet::PropertySheet::getPyValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a345cfadf9398442bb9a94bd6d1fc10f0),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[SpreadsheetGui::DlgSheetConf::onDiscard()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#a92ca45c8345d8a43a3b95fd019804c86),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
[SpreadsheetGui::DlgSheetConf::prepare()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#abfbeb695362f8ae8074215c61a254de3),
[App::Range::rangeString()](../../dd/dc1/classApp_1_1Range.html#a35751c0975e7651240ae38353757c46a),
[SpreadsheetGui::SheetViewPy::selectedCells()](../../d7/d63/classSpreadsheetGui_1_1SheetViewPy.html#a4fb5b2f73a7eafaa492ce0c3a0b837b7),
[App::Range::toCellString()](../../dd/dc1/classApp_1_1Range.html#ad28821b37eedaeda44ee6ea4572d02c6),
and
[Spreadsheet::Sheet::updateProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a9a0640fab46ed529fc1c4de49b0bb699).

## Member Data Documentation

## ◆ MAX_COLUMNS

| const [int](../../d1/da0/classint.html) App::CellAddress::MAX_COLUMNS = 26 *
26 + 26  
---  
static  
  
## ◆ MAX_ROWS

| const [int](../../d1/da0/classint.html) App::CellAddress::MAX_ROWS = 16384  
---  
static  
  
Referenced by
[App::validRow()](../../dd/dc2/namespaceApp.html#a37792adfdb0ec511543d5922508376f3).

* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/App/Range.h
  * FreeCAD/src/App/Range.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

