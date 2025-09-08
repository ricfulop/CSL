---
url: https://freecad.github.io/SourceDoc/dd/dc1/classApp_1_1Range.html
scraped_at: 2025-09-08T14:56:59.081151
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Range](../../dd/dc1/classApp_1_1Range.html)

[List of all members](../../d4/d9b/classApp_1_1Range-members.html) | Public Member Functions

App::Range Class Reference

The [Range](../../dd/dc1/classApp_1_1Range.html "The Range class is a
spreadsheet range iterator.") class is a spreadsheet range iterator.
[More...](../../dd/dc1/classApp_1_1Range.html#details)

`#include <Range.h>`

##  Public Member Functions  
  
---  
std::string | [address](../../dd/dc1/classApp_1_1Range.html#a74c22ecd2bcbccc0b0e187e0968765a9) () const  
| Current cell as a string.
[More...](../../dd/dc1/classApp_1_1Range.html#a74c22ecd2bcbccc0b0e187e0968765a9)  
  
[int](../../d1/da0/classint.html) | [colCount](../../dd/dc1/classApp_1_1Range.html#a3dbc3c03fd52f1bc0f3a3d0642235e41) () const  
| Column count.
[More...](../../dd/dc1/classApp_1_1Range.html#a3dbc3c03fd52f1bc0f3a3d0642235e41)  
  
[int](../../d1/da0/classint.html) | [column](../../dd/dc1/classApp_1_1Range.html#aa0d380059f4d17938f1d6e73efcd55d3) () const  
| Current column.
[More...](../../dd/dc1/classApp_1_1Range.html#aa0d380059f4d17938f1d6e73efcd55d3)  
  
[CellAddress](../../dd/d94/structApp_1_1CellAddress.html) | [from](../../dd/dc1/classApp_1_1Range.html#a0ab280ecf4749fbd80e6a2527d00c401) () const  
| Position of start of range.
[More...](../../dd/dc1/classApp_1_1Range.html#a0ab280ecf4749fbd80e6a2527d00c401)  
  
std::string | [fromCellString](../../dd/dc1/classApp_1_1Range.html#ac44f4d906f5e0a0d6ce5b49aba48caa9) () const  
| [Start](../../d7/d4f/namespaceStart.html) of range as a string.
[More...](../../dd/dc1/classApp_1_1Range.html#ac44f4d906f5e0a0d6ce5b49aba48caa9)  
  
[bool](../../d9/db9/classbool.html) | [next](../../dd/dc1/classApp_1_1Range.html#af124f1124fc82f25050456ce027cbb36) ()  
void | [normalize](../../dd/dc1/classApp_1_1Range.html#a2427e7e0c2617579383b3f48cc51cbd6) ()  
| Make sure the range starts from top left and ends with bottom right corner.
[More...](../../dd/dc1/classApp_1_1Range.html#a2427e7e0c2617579383b3f48cc51cbd6)  
  
[CellAddress](../../dd/d94/structApp_1_1CellAddress.html) | [operator*](../../dd/dc1/classApp_1_1Range.html#a32d659b73cbb3f3fba93723effc16bea) () const  
[bool](../../d9/db9/classbool.html) | [operator<](../../dd/dc1/classApp_1_1Range.html#aa6c49fe2e3049622f7858295da982455) (const [Range](../../dd/dc1/classApp_1_1Range.html) &other) const  
|
[Range](../../dd/dc1/classApp_1_1Range.html#ac72eff312affd05913a63359b6189edb)
(const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html)
&[from](../../dd/dc1/classApp_1_1Range.html#a0ab280ecf4749fbd80e6a2527d00c401),
const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html)
&[to](../../dd/dc1/classApp_1_1Range.html#a62fca56773b5b5376a1cf7f9381795a2),
[bool](../../d9/db9/classbool.html)
[normalize](../../dd/dc1/classApp_1_1Range.html#a2427e7e0c2617579383b3f48cc51cbd6)=false)  
|
[Range](../../dd/dc1/classApp_1_1Range.html#aebaca32b6c237dd7cda121fc2579acba)
(const char *range, [bool](../../d9/db9/classbool.html)
[normalize](../../dd/dc1/classApp_1_1Range.html#a2427e7e0c2617579383b3f48cc51cbd6)=false)  
|
[Range](../../dd/dc1/classApp_1_1Range.html#a1a1234c619707a4640e0146b62296cae)
([int](../../d1/da0/classint.html) _row_begin,
[int](../../d1/da0/classint.html) _col_begin,
[int](../../d1/da0/classint.html) _row_end, [int](../../d1/da0/classint.html)
_col_end, [bool](../../d9/db9/classbool.html)
[normalize](../../dd/dc1/classApp_1_1Range.html#a2427e7e0c2617579383b3f48cc51cbd6)=false)  
std::string | [rangeString](../../dd/dc1/classApp_1_1Range.html#a35751c0975e7651240ae38353757c46a) () const  
| The raneg as a string.
[More...](../../dd/dc1/classApp_1_1Range.html#a35751c0975e7651240ae38353757c46a)  
  
[int](../../d1/da0/classint.html) | [row](../../dd/dc1/classApp_1_1Range.html#a748563ee784177c5d722c190fb1b7584) () const  
| Current row.
[More...](../../dd/dc1/classApp_1_1Range.html#a748563ee784177c5d722c190fb1b7584)  
  
[int](../../d1/da0/classint.html) | [rowCount](../../dd/dc1/classApp_1_1Range.html#a2122bbb6e4b8be585437c718663736f0) () const  
| Row count.
[More...](../../dd/dc1/classApp_1_1Range.html#a2122bbb6e4b8be585437c718663736f0)  
  
[int](../../d1/da0/classint.html) | [size](../../dd/dc1/classApp_1_1Range.html#a4e08949316d99b2a1b50ba639133b831) () const  
| Number of elements in range.
[More...](../../dd/dc1/classApp_1_1Range.html#a4e08949316d99b2a1b50ba639133b831)  
  
[CellAddress](../../dd/d94/structApp_1_1CellAddress.html) | [to](../../dd/dc1/classApp_1_1Range.html#a62fca56773b5b5376a1cf7f9381795a2) () const  
| Position of end of range.
[More...](../../dd/dc1/classApp_1_1Range.html#a62fca56773b5b5376a1cf7f9381795a2)  
  
std::string | [toCellString](../../dd/dc1/classApp_1_1Range.html#ad28821b37eedaeda44ee6ea4572d02c6) () const  
| End of range as a string.
[More...](../../dd/dc1/classApp_1_1Range.html#ad28821b37eedaeda44ee6ea4572d02c6)  
  
  
## Detailed Description

The [Range](../../dd/dc1/classApp_1_1Range.html "The Range class is a
spreadsheet range iterator.") class is a spreadsheet range iterator.

It takes a starting (row, col) and an ending (row, col). Notice that ranges
are always at least one element. The
[next()](../../dd/dc1/classApp_1_1Range.html#af124f1124fc82f25050456ce027cbb36)
functions is therefore used e.g as follows:

do { ... while (range.next());

## Constructor & Destructor Documentation

## ◆ Range() [1/3]

Range::Range  | ( | const char *  | _range_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _normalize_ = `false`  
| ) | |   
  
References
[App::CellAddress::col()](../../dd/d94/structApp_1_1CellAddress.html#a1076b5b4b1899f89f3e79a03abe48ddb),
[from()](../../dd/dc1/classApp_1_1Range.html#a0ab280ecf4749fbd80e6a2527d00c401),
[normalize()](../../dd/dc1/classApp_1_1Range.html#a2427e7e0c2617579383b3f48cc51cbd6),
[App::CellAddress::row()](../../dd/d94/structApp_1_1CellAddress.html#a2da9b96fa1f929f491dc9d74b93ceea6),
and
[to()](../../dd/dc1/classApp_1_1Range.html#a62fca56773b5b5376a1cf7f9381795a2).

## ◆ Range() [2/3]

Range::Range  | ( | [int](../../d1/da0/classint.html) | __row_begin_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | __col_begin_ ,   
|  | [int](../../d1/da0/classint.html) | __row_end_ ,   
|  | [int](../../d1/da0/classint.html) | __col_end_ ,   
|  | [bool](../../d9/db9/classbool.html) | _normalize_ = `false`  
| ) | |   
  
References
[normalize()](../../dd/dc1/classApp_1_1Range.html#a2427e7e0c2617579383b3f48cc51cbd6).

## ◆ Range() [3/3]

Range::Range  | ( | const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) & | _from_ ,   
---|---|---|---  
|  | const [CellAddress](../../dd/d94/structApp_1_1CellAddress.html) & | _to_ ,   
|  | [bool](../../d9/db9/classbool.html) | _normalize_ = `false`  
| ) | |   
  
References
[normalize()](../../dd/dc1/classApp_1_1Range.html#a2427e7e0c2617579383b3f48cc51cbd6).

## Member Function Documentation

## ◆ address()

std::string App::Range::address  | ( | | ) |  const  
---|---|---|---|---  
  
Current cell as a string.

References
[App::CellAddress::toString()](../../dd/d94/structApp_1_1CellAddress.html#ade22dc6292d5004bb7fdd315ce64fc8d).

Referenced by
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede).

## ◆ colCount()

[int](../../d1/da0/classint.html) App::Range::colCount  | ( | | ) |  const  
---|---|---|---|---  
  
Column count.

Referenced by
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
and
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede).

## ◆ column()

[int](../../d1/da0/classint.html) App::Range::column  | ( | | ) |  const  
---|---|---|---|---  
  
Current column.

## ◆ from()

[CellAddress](../../dd/d94/structApp_1_1CellAddress.html) App::Range::from  | ( | | ) |  const  
---|---|---|---|---  
  
Position of start of range.

Referenced by
[operator<()](../../dd/dc1/classApp_1_1Range.html#aa6c49fe2e3049622f7858295da982455),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
[Range()](../../dd/dc1/classApp_1_1Range.html#aebaca32b6c237dd7cda121fc2579acba),
and
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede).

## ◆ fromCellString()

std::string App::Range::fromCellString  | ( | | ) |  const  
---|---|---|---|---  
  
[Start](../../d7/d4f/namespaceStart.html) of range as a string.

References
[App::CellAddress::toString()](../../dd/d94/structApp_1_1CellAddress.html#ade22dc6292d5004bb7fdd315ce64fc8d).

## ◆ next()

[bool](../../d9/db9/classbool.html) Range::next  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede).

## ◆ normalize()

void Range::normalize  | ( | | ) |   
---|---|---|---|---  
  
Make sure the range starts from top left and ends with bottom right corner.

Referenced by
[PathScripts.PathDressupLeadInOut.ObjectDressup::getLeadEnd()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#ac4be8c95d4aa1440fb03c096c4e44e57),
[PathScripts.PathDressupLeadInOut.ObjectDressup::getLeadStart()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#a2d9de34620ee069b425e7f99f0efe9da),
and
[Range()](../../dd/dc1/classApp_1_1Range.html#aebaca32b6c237dd7cda121fc2579acba).

## ◆ operator*()

[CellAddress](../../dd/d94/structApp_1_1CellAddress.html) App::Range::operator*  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ operator<()

[bool](../../d9/db9/classbool.html) App::Range::operator< | ( | const [Range](../../dd/dc1/classApp_1_1Range.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
References
[from()](../../dd/dc1/classApp_1_1Range.html#a0ab280ecf4749fbd80e6a2527d00c401),
and
[to()](../../dd/dc1/classApp_1_1Range.html#a62fca56773b5b5376a1cf7f9381795a2).

## ◆ rangeString()

std::string App::Range::rangeString  | ( | | ) |  const  
---|---|---|---|---  
  
The raneg as a string.

References
[App::CellAddress::toString()](../../dd/d94/structApp_1_1CellAddress.html#ade22dc6292d5004bb7fdd315ce64fc8d).

## ◆ row()

[int](../../d1/da0/classint.html) App::Range::row  | ( | | ) |  const  
---|---|---|---|---  
  
Current row.

## ◆ rowCount()

[int](../../d1/da0/classint.html) App::Range::rowCount  | ( | | ) |  const  
---|---|---|---|---  
  
Row count.

Referenced by
[package_list.PackageListItemModel::append_item()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#ae6ca870990288c91a44d79f370a6b00a),
[package_list.PackageListItemModel::clear()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#a1cb97185b8c8640a9bf5377338ef811f),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
and
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede).

## ◆ size()

[int](../../d1/da0/classint.html) App::Range::size  | ( | | ) |  const  
---|---|---|---|---  
  
Number of elements in range.

Referenced by
[SpreadsheetGui::DlgBindSheet::accept()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#ad6e5cb0995aaa1341a57bdb97ed49cbd),
[gzip_utf8.GzipFile::close()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a5c40910b0ce0286256128c6dae8a2c9b),
[PathScripts.PostUtils.GCodeEditorDialog::done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede),
and
[gzip_utf8.GzipFile::write()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a3148c5b71cccbdfce05d52d31114810e).

## ◆ to()

[CellAddress](../../dd/d94/structApp_1_1CellAddress.html) App::Range::to  | ( | | ) |  const  
---|---|---|---|---  
  
Position of end of range.

Referenced by
[operator<()](../../dd/dc1/classApp_1_1Range.html#aa6c49fe2e3049622f7858295da982455),
[Range()](../../dd/dc1/classApp_1_1Range.html#aebaca32b6c237dd7cda121fc2579acba),
and
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede).

## ◆ toCellString()

std::string App::Range::toCellString  | ( | | ) |  const  
---|---|---|---|---  
  
End of range as a string.

References
[App::CellAddress::toString()](../../dd/d94/structApp_1_1CellAddress.html#ade22dc6292d5004bb7fdd315ce64fc8d).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Range.h
  * FreeCAD/src/App/Range.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

