---
url: https://freecad.github.io/SourceDoc/d0/d5a/classautomotive__design_1_1relative__event__occurrence.html
scraped_at: 2025-09-08T15:11:40.637083
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [relative_event_occurrence](../../d0/d5a/classautomotive__design_1_1relative__event__occurrence.html)

[List of all members](../../d8/ddb/classautomotive__design_1_1relative__event__occurrence-members.html) | Public Member Functions | Public Attributes

automotive_design.relative_event_occurrence Class Reference

##  Public Member Functions  
  
---  
def | [base_event](../../d0/d5a/classautomotive__design_1_1relative__event__occurrence.html#a09fe351659df3e1521a1ab62fd0b706d) ()  
def | [offset](../../d0/d5a/classautomotive__design_1_1relative__event__occurrence.html#a40785ae20783bccb000331d1392bb10a) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.event_occurrence](../../d9/dec/classautomotive__design_1_1event__occurrence.html)  
def | [description](../../d9/dec/classautomotive__design_1_1event__occurrence.html#a167d7e353205ca47c5066c25fd4e9098) ()  
def | [id](../../d9/dec/classautomotive__design_1_1event__occurrence.html#a29a63f3a5161b92078681da979434ca4) ()  
def | [name](../../d9/dec/classautomotive__design_1_1event__occurrence.html#a41814a63ae3770e477565fc84d958c07) ()  
  
##  Public Attributes  
  
---  
|
[base_event](../../d0/d5a/classautomotive__design_1_1relative__event__occurrence.html#af1d15f2027c8237de8e3238cc93566d6)  
|
[offset](../../d0/d5a/classautomotive__design_1_1relative__event__occurrence.html#a1fc658aed969c99303ef76d681e7c08c)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.event_occurrence](../../d9/dec/classautomotive__design_1_1event__occurrence.html)  
|
[description](../../d9/dec/classautomotive__design_1_1event__occurrence.html#a05977a815597c0e1f6cbbb4898814094)  
|
[id](../../d9/dec/classautomotive__design_1_1event__occurrence.html#a1c398ebff481d05636e042efae8d0d11)  
|
[name](../../d9/dec/classautomotive__design_1_1event__occurrence.html#ab78abb5d12ff69e2ff52a7760e828fd7)  
  
## Detailed Description

    
    
    Entity relative_event_occurrence definition.
    
        :param base_event
        :type base_event:event_occurrence
    
        :param offset
        :type offset:time_measure_with_unit

## Member Function Documentation

## ◆ base_event()

def automotive_design.relative_event_occurrence.base_event  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.relative_event_occurrence._base_event,
and automotive_design.relative_event_occurrence._base_event.

## ◆ offset()

def automotive_design.relative_event_occurrence.offset  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.relative_event_occurrence._offset,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.parallel_offset._offset,
automotive_design.relative_event_occurrence._offset, and
automotive_design.parallel_offset._offset.

Referenced by
[gzip_utf8.GzipFile.read()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a1997270eadc9247814e6a68f6a8a3ba1),
[gzip_utf8.GzipFile.readline()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a17112c17fb6431a0d56b0108931c73e0),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[gzip_utf8.GzipFile.rewind()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#aee93e6718f3bf10452ff5254970d7886),
[gzip_utf8.GzipFile.seek()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ac5b53848e16b6ba800ed9ac8d3f737c3),
and
[gzip_utf8.GzipFile.write()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a3148c5b71cccbdfce05d52d31114810e).

## Member Data Documentation

## ◆ base_event

automotive_design.relative_event_occurrence.base_event  
---  
  
## ◆ offset

automotive_design.relative_event_occurrence.offset  
---  
  
Referenced by
[gzip_utf8.GzipFile.read()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a1997270eadc9247814e6a68f6a8a3ba1),
[gzip_utf8.GzipFile.readline()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a17112c17fb6431a0d56b0108931c73e0),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[gzip_utf8.GzipFile.rewind()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#aee93e6718f3bf10452ff5254970d7886),
[gzip_utf8.GzipFile.seek()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ac5b53848e16b6ba800ed9ac8d3f737c3),
and
[gzip_utf8.GzipFile.write()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a3148c5b71cccbdfce05d52d31114810e).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

