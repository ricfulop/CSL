---
url: https://freecad.github.io/SourceDoc/dd/d0f/classautomotive__design_1_1interval__expression.html
scraped_at: 2025-09-08T15:06:45.394497
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [interval_expression](../../dd/d0f/classautomotive__design_1_1interval__expression.html)

[List of all members](../../d5/dff/classautomotive__design_1_1interval__expression-members.html) | Public Member Functions

automotive_design.interval_expression Class Reference

##  Public Member Functions  
  
---  
def | [interval_high](../../dd/d0f/classautomotive__design_1_1interval__expression.html#ad27326488f8f0d661d115720cf4af569) ()  
def | [interval_item](../../dd/d0f/classautomotive__design_1_1interval__expression.html#ac9ffe93c5bde8361c32d671f879ce566) ()  
def | [interval_low](../../dd/d0f/classautomotive__design_1_1interval__expression.html#a570f3687e5234129c27876f73be462d8) ()  
def | [wr1](../../dd/d0f/classautomotive__design_1_1interval__expression.html#a1fe921c409991707a9fe6364747065f8) (self)  
def | [wr2](../../dd/d0f/classautomotive__design_1_1interval__expression.html#afc4003d98129f7ee8947af19b7545ad8) (self)  
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

    
    
    Entity interval_expression definition.
    
        :param interval_low
        :type interval_low:generic_expression
    
        :param interval_item
        :type interval_item:generic_expression
    
        :param interval_high
        :type interval_high:generic_expression

## Member Function Documentation

## ◆ interval_high()

def automotive_design.interval_expression.interval_high  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.interval_expression.wr1()](../../dd/d0f/classautomotive__design_1_1interval__expression.html#a1fe921c409991707a9fe6364747065f8).

## ◆ interval_item()

def automotive_design.interval_expression.interval_item  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.interval_expression.wr1()](../../dd/d0f/classautomotive__design_1_1interval__expression.html#a1fe921c409991707a9fe6364747065f8).

## ◆ interval_low()

def automotive_design.interval_expression.interval_low  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.interval_expression.wr1()](../../dd/d0f/classautomotive__design_1_1interval__expression.html#a1fe921c409991707a9fe6364747065f8).

## ◆ wr1()

def automotive_design.interval_expression.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.generic_expression](../../d3/d52/classautomotive__design_1_1generic__expression.html#aea35213a5e29cdc6cc6a201099976f3e).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.interval_expression.interval_high(),
[automotive_design.interval_expression.interval_high()](../../dd/d0f/classautomotive__design_1_1interval__expression.html#ad27326488f8f0d661d115720cf4af569),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.interval_expression.interval_item(),
[automotive_design.interval_expression.interval_item()](../../dd/d0f/classautomotive__design_1_1interval__expression.html#ac9ffe93c5bde8361c32d671f879ce566),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.interval_expression.interval_low(),
and
[automotive_design.interval_expression.interval_low()](../../dd/d0f/classautomotive__design_1_1interval__expression.html#a570f3687e5234129c27876f73be462d8).

## ◆ wr2()

def automotive_design.interval_expression.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

