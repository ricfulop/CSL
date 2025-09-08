---
url: https://freecad.github.io/SourceDoc/d7/daa/classautomotive__design_1_1substring__expression.html
scraped_at: 2025-09-08T15:13:24.106199
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [substring_expression](../../d7/daa/classautomotive__design_1_1substring__expression.html)

[List of all members](../../de/d88/classautomotive__design_1_1substring__expression-members.html) | Public Member Functions

automotive_design.substring_expression Class Reference

##  Public Member Functions  
  
---  
def | [index1](../../d7/daa/classautomotive__design_1_1substring__expression.html#a4fdbe3070eaa14bc333f30410bd29866) ()  
def | [index2](../../d7/daa/classautomotive__design_1_1substring__expression.html#acc3608b5a6a0129e543cc47f6abf5b56) ()  
def | [operand](../../d7/daa/classautomotive__design_1_1substring__expression.html#af41ff3117f63d3a5fc31b5334f872344) ()  
def | [wr1](../../d7/daa/classautomotive__design_1_1substring__expression.html#ae42f045ef3b42b7bdfe476af38354c92) (self)  
def | [wr2](../../d7/daa/classautomotive__design_1_1substring__expression.html#a326ba91b8171959d77b5998acfe172ea) (self)  
def | [wr3](../../d7/daa/classautomotive__design_1_1substring__expression.html#a9c46e67719c57c00c4509ea1e5d9fa45) (self)  
def | [wr4](../../d7/daa/classautomotive__design_1_1substring__expression.html#a59c6b5c40c9e5f7a25756c07613352ae) (self)  
def | [wr1](../../d3/d52/classautomotive__design_1_1generic__expression.html#aea35213a5e29cdc6cc6a201099976f3e) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.multiple_arity_generic_expression](../../d0/d0a/classautomotive__design_1_1multiple__arity__generic__expression.html)  
def | [operands](../../d0/d0a/classautomotive__design_1_1multiple__arity__generic__expression.html#ad60a877aa162b6fec898e83f7b4f6802) ()  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.multiple_arity_generic_expression](../../d0/d0a/classautomotive__design_1_1multiple__arity__generic__expression.html)  
|
[operands](../../d0/d0a/classautomotive__design_1_1multiple__arity__generic__expression.html#af5f9602d3b4df221c5fa6d277596f1df)  
  
## Detailed Description

    
    
    Entity substring_expression definition.
    
        :param operand
        :type operand:generic_expression
    
        :param index1
        :type index1:generic_expression
    
        :param index2
        :type index2:generic_expression

## Member Function Documentation

## ◆ index1()

def automotive_design.substring_expression.index1  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.substring_expression.wr1()](../../d7/daa/classautomotive__design_1_1substring__expression.html#ae42f045ef3b42b7bdfe476af38354c92),
and
[automotive_design.substring_expression.wr3()](../../d7/daa/classautomotive__design_1_1substring__expression.html#a9c46e67719c57c00c4509ea1e5d9fa45).

## ◆ index2()

def automotive_design.substring_expression.index2  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.substring_expression.wr1()](../../d7/daa/classautomotive__design_1_1substring__expression.html#ae42f045ef3b42b7bdfe476af38354c92),
and
[automotive_design.substring_expression.wr4()](../../d7/daa/classautomotive__design_1_1substring__expression.html#a59c6b5c40c9e5f7a25756c07613352ae).

## ◆ operand()

def automotive_design.substring_expression.operand  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.index_expression.wr1()](../../d8/d62/classautomotive__design_1_1index__expression.html#a33cd6562421dd35dd68ed821911fa212),
and
[automotive_design.substring_expression.wr1()](../../d7/daa/classautomotive__design_1_1substring__expression.html#ae42f045ef3b42b7bdfe476af38354c92).

## ◆ wr1()

def automotive_design.substring_expression.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.generic_expression](../../d3/d52/classautomotive__design_1_1generic__expression.html#aea35213a5e29cdc6cc6a201099976f3e).

References
[automotive_design.substring_expression.index1()](../../d7/daa/classautomotive__design_1_1substring__expression.html#a4fdbe3070eaa14bc333f30410bd29866),
[automotive_design.substring_expression.index2()](../../d7/daa/classautomotive__design_1_1substring__expression.html#acc3608b5a6a0129e543cc47f6abf5b56),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.unary_generic_expression.operand,
[automotive_design.unary_generic_expression.operand](../../d0/d3e/classautomotive__design_1_1unary__generic__expression.html#a7c62536d30a150a503d090d2a0dfed36),
[automotive_design.index_expression.operand()](../../d8/d62/classautomotive__design_1_1index__expression.html#aafcdd43ed52e191ad1f9215db73c4e9e),
and
[automotive_design.substring_expression.operand()](../../d7/daa/classautomotive__design_1_1substring__expression.html#af41ff3117f63d3a5fc31b5334f872344).

## ◆ wr2()

def automotive_design.substring_expression.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ wr3()

def automotive_design.substring_expression.wr3  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.substring_expression.index1()](../../d7/daa/classautomotive__design_1_1substring__expression.html#a4fdbe3070eaa14bc333f30410bd29866),
and
[automotive_design.is_int_expr()](../../d4/ddf/namespaceautomotive__design.html#ae2d12b4b398f78fc93cc2db4c84f380a).

## ◆ wr4()

def automotive_design.substring_expression.wr4  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.substring_expression.index2()](../../d7/daa/classautomotive__design_1_1substring__expression.html#acc3608b5a6a0129e543cc47f6abf5b56),
and
[automotive_design.is_int_expr()](../../d4/ddf/namespaceautomotive__design.html#ae2d12b4b398f78fc93cc2db4c84f380a).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

