---
url: https://freecad.github.io/SourceDoc/d1/d20/group__ParamProperty.html
scraped_at: 2025-09-08T14:52:18.868383
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Macros

Property Macros

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Path](../../dc/db4/group__PATH.html) » [Parameters helper
macros](../../dc/dbe/group__ParamHelper.html)

Helper macros for FreeCAD properties. More...

##  Macros  
  
---  
#define | [PARAM_PROP_ADD](../../d1/d20/group__ParamProperty.html#ga97cc22ea1ee7d5887712dbd179ea376c)(_group, _seq) BOOST_PP_SEQ_FOR_EACH_I(PARAM_PROP_ADD_TYPED,_group,_seq)  
| Add FreeCAD properties.
[More...](../../d1/d20/group__ParamProperty.html#ga97cc22ea1ee7d5887712dbd179ea376c)  
  
#define | [PARAM_PROP_ARGS](../../d1/d20/group__ParamProperty.html#ga11d40998437793e9a7f483281c1f61bb)(_seq) [PARAM_FOREACH_I](../../dc/d97/group__ParamLooper.html#ga969dfbbc7b31aad9cd6cdbf118a09602)(PARAM_PROP_ARGS_,_seq)  
| Expand the property list as function arguments.
[More...](../../d1/d20/group__ParamProperty.html#ga11d40998437793e9a7f483281c1f61bb)  
  
#define | [PARAM_PROP_bool](../../d1/d20/group__ParamProperty.html#gaeac2ac4e5b67593f4b1e7cf6bc0dc27f)(_param) [App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
#define | [PARAM_PROP_DECLARE](../../d1/d20/group__ParamProperty.html#ga8e9a56a640eb87b931c203be10d85d9b)(_seq) [PARAM_FOREACH](../../dc/d97/group__ParamLooper.html#ga63f4fe0971668bd066da5762e02065d3)(PARAM_PROP_DECLARE_,_seq)  
| Declare FreeCAD properties.
[More...](../../d1/d20/group__ParamProperty.html#ga8e9a56a640eb87b931c203be10d85d9b)  
  
#define | [PARAM_PROP_double](../../d1/d20/group__ParamProperty.html#ga20a1b0d53632cfd83dd0b422ccf4e3eb)(_param) [PARAM_FPROP](../../d2/dab/group__ParamAccessor.html#ga777e58665ae90ed497631a7cced4fa69)(_param) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
#define | [PARAM_PROP_enum](../../d1/d20/group__ParamProperty.html#gac31652a3dbbfcbbd5614a42a64465c0f)(_param) [App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
#define | [PARAM_PROP_enum2](../../d1/d20/group__ParamProperty.html#gac3893557f08c3fbf23e3278ad5c2b31b)(_param) [App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
#define | [PARAM_PROP_long](../../d1/d20/group__ParamProperty.html#ga2b45b0b040be33b11ae31e92718d7e7d)(_param) [App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
#define | [PARAM_PROP_short](../../d1/d20/group__ParamProperty.html#ga44475ac982a5879170f0b897034a9941)(_param) [App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
  
## Detailed Description

Helper macros for FreeCAD properties.

## Macro Definition Documentation

## ◆ PARAM_PROP_ADD

#define PARAM_PROP_ADD | ( |  | _group,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH_I(PARAM_PROP_ADD_TYPED,_group,_seq)  
  
Add FreeCAD properties.

## ◆ PARAM_PROP_ARGS

#define PARAM_PROP_ARGS | ( |  | _seq| ) |  [PARAM_FOREACH_I](../../dc/d97/group__ParamLooper.html#ga969dfbbc7b31aad9cd6cdbf118a09602)(PARAM_PROP_ARGS_,_seq)  
---|---|---|---|---|---  
  
Expand the property list as function arguments.

Expand to:

name1.getValue(), name2.getValue() ...

## ◆ PARAM_PROP_bool

#define PARAM_PROP_bool | ( |  | _param| ) |  [App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_PROP_DECLARE

#define PARAM_PROP_DECLARE | ( |  | _seq| ) |  [PARAM_FOREACH](../../dc/d97/group__ParamLooper.html#ga63f4fe0971668bd066da5762e02065d3)(PARAM_PROP_DECLARE_,_seq)  
---|---|---|---|---|---  
  
Declare FreeCAD properties.

## ◆ PARAM_PROP_double

#define PARAM_PROP_double | ( |  | _param| ) |  [PARAM_FPROP](../../d2/dab/group__ParamAccessor.html#ga777e58665ae90ed497631a7cced4fa69)(_param) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_PROP_enum

#define PARAM_PROP_enum | ( |  | _param| ) |  [App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_PROP_enum2

#define PARAM_PROP_enum2 | ( |  | _param| ) |  [App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_PROP_long

#define PARAM_PROP_long | ( |  | _param| ) |  [App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_PROP_short

#define PARAM_PROP_short | ( |  | _param| ) |  [App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html) [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param)  
---|---|---|---|---|---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

