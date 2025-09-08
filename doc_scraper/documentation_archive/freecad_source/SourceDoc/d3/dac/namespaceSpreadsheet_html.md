---
url: https://freecad.github.io/SourceDoc/d3/dac/namespaceSpreadsheet.html
scraped_at: 2025-09-08T14:57:00.050160
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Typedefs | Functions

Spreadsheet Namespace Reference

##  Classes  
  
---  
class | [Cell](../../d5/d22/classSpreadsheet_1_1Cell.html)  
class | [DisplayUnit](../../d8/d2a/classSpreadsheet_1_1DisplayUnit.html)  
class | [Module](../../da/d10/classSpreadsheet_1_1Module.html)  
class | [PropertyColumnWidths](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html)  
class | [PropertyRowHeights](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html)  
class | [PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html)  
class | [PropertySpreadsheetQuantity](../../d2/dd4/classSpreadsheet_1_1PropertySpreadsheetQuantity.html)  
| [Spreadsheet](../../d3/dac/namespaceSpreadsheet.html) quantity property This
is a property for quantities, and unlike its ancestor implements
[Copy()](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de
"Returns a new copy of the property \(mainly for Undo/Redo and
transactions\)") and
[Paste()](../../d2/dd4/classSpreadsheet_1_1PropertySpreadsheetQuantity.html#a2e105319857c2aa18ec56cb5a56b8f10)
methods.
[More...](../../d2/dd4/classSpreadsheet_1_1PropertySpreadsheetQuantity.html#details)  
  
class | [Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html)  
class | [SheetObserver](../../db/d2b/classSpreadsheet_1_1SheetObserver.html)  
  
##  Typedefs  
  
---  
typedef [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html) > | [SheetPython](../../d3/dac/namespaceSpreadsheet.html#a53ae59a7c3d10406ab8a39c929201861)  
  
##  Functions  
  
---  
SpreadsheetExport std::string | [columnName](../../d3/dac/namespaceSpreadsheet.html#af97af2a594f163e00d6ff9e13270c3f8) ([int](../../d1/da0/classint.html) col)  
| Encode _col_ as a string.
[More...](../../d3/dac/namespaceSpreadsheet.html#af97af2a594f163e00d6ff9e13270c3f8)  
  
SpreadsheetExport void | [createRectangles](../../d3/dac/namespaceSpreadsheet.html#a101ef91e68ae4c7e6318bd6050795046) (std::set< std::pair< [int](../../d1/da0/classint.html), [int](../../d1/da0/classint.html) > > &cells, std::map< std::pair< [int](../../d1/da0/classint.html), [int](../../d1/da0/classint.html) >, std::pair< [int](../../d1/da0/classint.html), [int](../../d1/da0/classint.html) > > &rectangles)  
[PyObject](../../df/d1b/classPyObject.html) * | [initModule](../../d3/dac/namespaceSpreadsheet.html#a5ef7c574c87d22dca75e0d2457e5acd8) ()  
SpreadsheetExport std::string | [quote](../../d3/dac/namespaceSpreadsheet.html#a3cd73de5b6a9e7008be11fde2c63dbce) (const std::string &input)  
SpreadsheetExport std::string | [rowName](../../d3/dac/namespaceSpreadsheet.html#ae4d8879d8cc6fb7b7b17d95621bb2858) ([int](../../d1/da0/classint.html) row)  
| Encode _row_ as a string.
[More...](../../d3/dac/namespaceSpreadsheet.html#ae4d8879d8cc6fb7b7b17d95621bb2858)  
  
SpreadsheetExport std::string | [unquote](../../d3/dac/namespaceSpreadsheet.html#aba76ba1415fb2f07b70906500b76988c) (const std::string &input)  
  
## Typedef Documentation

## ◆ SheetPython

typedef
[App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)<[Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html)>
[Spreadsheet::SheetPython](../../d3/dac/namespaceSpreadsheet.html#a53ae59a7c3d10406ab8a39c929201861)  
---  
  
## Function Documentation

## ◆ columnName()

std::string Spreadsheet::columnName  | ( | [int](../../d1/da0/classint.html) | _col_| ) |   
---|---|---|---|---|---  
  
Encode _col_ as a string.

Parameters

     col| Column given as a 0-based column position.  
---|---  
  
Returns

    String with column position, with "A" being the first column, "B" being the second and so on. 

Referenced by
[SpreadsheetGui::SheetTableView::insertColumns()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#ab91b636542c4367d2ce281d3ba5e8b58),
[SpreadsheetGui::SheetTableView::insertColumnsAfter()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a8cebcff7b6ae0e8fad3175aa4cf22946),
[SpreadsheetGui::SheetTableView::removeColumns()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#aa41dca227d456e2ffd972fa88c4ff6d2),
and
[Spreadsheet::PropertyColumnWidths::Save()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a976f43505863b7470c1eb93726de2d5e).

## ◆ createRectangles()

void Spreadsheet::createRectangles  | ( | std::set< std::pair< [int](../../d1/da0/classint.html), [int](../../d1/da0/classint.html) > > & | _cells_ ,   
---|---|---|---  
|  | std::map< std::pair< [int](../../d1/da0/classint.html), [int](../../d1/da0/classint.html) >, std::pair< [int](../../d1/da0/classint.html), [int](../../d1/da0/classint.html) > > & | _rectangles_  
| ) | |   
  
## ◆ initModule()

[PyObject](../../df/d1b/classPyObject.html) * Spreadsheet::initModule  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::InterpreterSingleton::addModule()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#af556d495376be43c3d93c9a44e6c15d3),
and
[Base::Interpreter()](../../db/d07/namespaceBase.html#a2ee9c987b769c5d1ed5f2fe69b21d2c9).

## ◆ quote()

std::string Spreadsheet::quote  | ( | const std::string & | _input_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Spreadsheet::Sheet::getCharsFromPrefs()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a144aba1b77f58bcd343d16c12d4df49c).

## ◆ rowName()

std::string Spreadsheet::rowName  | ( | [int](../../d1/da0/classint.html) | _row_| ) |   
---|---|---|---|---|---  
  
Encode _row_ as a string.

Parameters

     row| Row given as a 0-based row position.  
---|---  
  
Returns

    String with row position, with "1" being the first row. 

Referenced by
[SpreadsheetGui::SheetTableView::insertRows()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a29b12a5e738d689dd11833a7cf3b474e),
[SpreadsheetGui::SheetTableView::insertRowsAfter()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#ac591ed9234eab84fa028bce688dc3b56),
[SpreadsheetGui::SheetTableView::removeRows()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a7599cef797de900e763493224292cdea),
and
[Spreadsheet::PropertyRowHeights::Save()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a7dbc1225885f9daac0294390384589d6).

## ◆ unquote()

std::string Spreadsheet::unquote  | ( | const std::string & | _input_| ) |   
---|---|---|---|---|---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

