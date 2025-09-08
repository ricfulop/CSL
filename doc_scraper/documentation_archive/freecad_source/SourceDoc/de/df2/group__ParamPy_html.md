---
url: https://freecad.github.io/SourceDoc/de/df2/group__ParamPy.html
scraped_at: 2025-09-08T14:52:16.881149
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Modules | Macros

Python helper

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Path](../../dc/db4/group__PATH.html) » [Parameters helper
macros](../../dc/dbe/group__ParamHelper.html)

Helper macros for Python bindings. More...

##  Modules  
  
---  
| [Python doc helper](../../da/d6a/group__ParamDoc.html)  
| Generate argument doc string for Python.  
  
  
##  Macros  
  
---  
#define | [PARAM_FIELD_STRINGS](../../de/df2/group__ParamPy.html#ga0ab546c416e39ca277cce3bd29027716)(_field, _seq) BOOST_PP_SEQ_FOR_EACH_I(PARAM_FIELD_STRINGS_,_field,_seq)  
| Expand to a list of stringified fields.
[More...](../../de/df2/group__ParamPy.html#ga0ab546c416e39ca277cce3bd29027716)  
  
#define | [PARAM_FIELDS](../../de/df2/group__ParamPy.html#gacf06ec8275cf1f9ab549f61630d84448)(_src, _seq) BOOST_PP_SEQ_FOR_EACH_I(PARAM_FIELDS_,_src,_seq)  
| Expand to a list of the given field in the parameter sequence.
[More...](../../de/df2/group__ParamPy.html#gacf06ec8275cf1f9ab549f61630d84448)  
  
#define | [PARAM_PY_DECLARE](../../de/df2/group__ParamPy.html#ga213f61961402fcfc4cba23de16d99841)(_src, _seq) BOOST_PP_SEQ_FOR_EACH(PARAM_PY_DECLARE_,_src,_seq)  
| Declare field variables for Python C type without initialization.
[More...](../../de/df2/group__ParamPy.html#ga213f61961402fcfc4cba23de16d99841)  
  
#define | [PARAM_PY_DECLARE_INIT](../../de/df2/group__ParamPy.html#gaf25380e028d24037df82d7650b5d8e39)(_src, _seq) BOOST_PP_SEQ_FOR_EACH(PARAM_PY_DECLARE_INIT_,_src,_seq)  
| Declare field variables of Python c type with initialization to default.
[More...](../../de/df2/group__ParamPy.html#gaf25380e028d24037df82d7650b5d8e39)  
  
#define | [PARAM_PY_DICT_SET_VALUE](../../de/df2/group__ParamPy.html#ga59bc5199c7d90ce8062dc058649a3fe4)(_dict, _field, _src, _seq) BOOST_PP_SEQ_FOR_EACH(PARAM_PY_DICT_SET_VALUE_,(_dict,_field,_src),_seq)  
| Populate a Python dict with a structure variable.
[More...](../../de/df2/group__ParamPy.html#ga59bc5199c7d90ce8062dc058649a3fe4)  
  
#define | [PARAM_PY_FIELDS](../../de/df2/group__ParamPy.html#ga1081ee8f98b23f101a0a0d49ba3d9c8d)(_src, _seq) BOOST_PP_SEQ_FOR_EACH_I(PARAM_PY_FIELDS_,_src,_seq)  
| Expand to a comma separated list of the given field in the sequence.
[More...](../../de/df2/group__ParamPy.html#ga1081ee8f98b23f101a0a0d49ba3d9c8d)  
  
#define | [PARAM_PY_KWDS](../../de/df2/group__ParamPy.html#gaa7bb46460b702db83d34bcbef78aeb38)(_seq) [PARAM_FOREACH](../../dc/d97/group__ParamLooper.html#ga63f4fe0971668bd066da5762e02065d3)(PARAM_PY_KWDS_,_seq)  
| Generate a format string for keywords based argument.
[More...](../../de/df2/group__ParamPy.html#gaa7bb46460b702db83d34bcbef78aeb38)  
  
#define | [PARAM_REF](../../de/df2/group__ParamPy.html#gab23d3c2b3c41daafc277ebe98e159aa0)(_src, _seq) BOOST_PP_SEQ_FOR_EACH_I(PARAM_REF_,_src,_seq)  
| Generate a list of field references.
[More...](../../de/df2/group__ParamPy.html#gab23d3c2b3c41daafc277ebe98e159aa0)  
  
  
## Detailed Description

Helper macros for Python bindings.

## Macro Definition Documentation

## ◆ PARAM_FIELD_STRINGS

#define PARAM_FIELD_STRINGS | ( |  | _field,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH_I(PARAM_FIELD_STRINGS_,_field,_seq)  
  
Expand to a list of stringified fields.

## ◆ PARAM_FIELDS

#define PARAM_FIELDS | ( |  | _src,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH_I(PARAM_FIELDS_,_src,_seq)  
  
Expand to a list of the given field in the parameter sequence.

  * `_src:` macro to generate source field. See [here](../../d7/d78/group__ParamCommon.html#ParamSrc) for more details

For example, [PARAM_FIELDS(PARAM_FARG,
_seq)](../../de/df2/group__ParamPy.html#gacf06ec8275cf1f9ab549f61630d84448
"Expand to a list of the given field in the parameter sequence.") expands to:

arg1,arg2 ...

## ◆ PARAM_PY_DECLARE

#define PARAM_PY_DECLARE | ( |  | _src,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH(PARAM_PY_DECLARE_,_src,_seq)  
  
Declare field variables for Python C type without initialization.

## ◆ PARAM_PY_DECLARE_INIT

#define PARAM_PY_DECLARE_INIT | ( |  | _src,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH(PARAM_PY_DECLARE_INIT_,_src,_seq)  
  
Declare field variables of Python c type with initialization to default.

## ◆ PARAM_PY_DICT_SET_VALUE

#define PARAM_PY_DICT_SET_VALUE | ( |  | _dict,   
---|---|---|---  
|  |  | _field,   
|  |  | _src,   
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH(PARAM_PY_DICT_SET_VALUE_,(_dict,_field,_src),_seq)  
  
Populate a Python dict with a structure variable.

  * `_dict:` the Python dictionary object 
  * `_field:` specifies the [field](../..//home/benj5378/development/FreeCAD/src/Mod/Path/App/ParamsHelper.h#ParamField) to use as key 
  * `_src:` macro to generate source field. See [here](../../d7/d78/group__ParamCommon.html#ParamSrc) for more details

Roughly translated to:

PyDict_SetItem(_dict,#_field1,_src(_param));

PyDict_SetItem(_dict,#_field2,_src(_param));

...

## ◆ PARAM_PY_FIELDS

#define PARAM_PY_FIELDS | ( |  | _src,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH_I(PARAM_PY_FIELDS_,_src,_seq)  
  
Expand to a comma separated list of the given field in the sequence.

  * `_src:` macro to generate source field. See [here](../../d7/d78/group__ParamCommon.html#ParamSrc) for more details

The field will be casted from python C to C type

## ◆ PARAM_PY_KWDS

#define PARAM_PY_KWDS | ( |  | _seq| ) |  [PARAM_FOREACH](../../dc/d97/group__ParamLooper.html#ga63f4fe0971668bd066da5762e02065d3)(PARAM_PY_KWDS_,_seq)  
---|---|---|---|---|---  
  
Generate a format string for keywords based argument.

## ◆ PARAM_REF

#define PARAM_REF | ( |  | _src,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH_I(PARAM_REF_,_src,_seq)  
  
Generate a list of field references.

  * `_src:` macro to generate source field. See [here](../../d7/d78/group__ParamCommon.html#ParamSrc) for

more details Expand to:

&_src(_param1), &_src(_param1) ...

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

