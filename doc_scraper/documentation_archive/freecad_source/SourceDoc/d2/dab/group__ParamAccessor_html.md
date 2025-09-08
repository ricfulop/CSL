---
url: https://freecad.github.io/SourceDoc/d2/dab/group__ParamAccessor.html
scraped_at: 2025-09-08T14:52:11.857999
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Macros

Field accessors

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Path](../../dc/db4/group__PATH.html) » [Parameters helper
macros](../../dc/dbe/group__ParamHelper.html)

To abstract parameter field details. More...

##  Macros  
  
---  
#define | [PARAM_FARG](../../d2/dab/group__ParamAccessor.html#gac679008b4caad9a26946c76ae89cbcc1)(_param) [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(ARG,_param)  
#define | [PARAM_FDEF](../../d2/dab/group__ParamAccessor.html#gaf4a1c13b0e98a1acb4573c92a9491fd4)(_param) [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(DEF,_param)  
#define | [PARAM_FDOC](../../d2/dab/group__ParamAccessor.html#ga2cda1b691aa51ec3520b587182fd641a)(_param) [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(DOC,_param)  
#define | [PARAM_FENUM_PREFIX](../../d2/dab/group__ParamAccessor.html#ga63e49af28c0eba81b775ae758409a1cc)(_param) BOOST_PP_TUPLE_ELEM(1,[PARAM_FINFO](../../d2/dab/group__ParamAccessor.html#ga2151f807167209a5e8cbcff8cfd897b2)(_param))  
#define | [PARAM_FENUM_TYPE](../../d2/dab/group__ParamAccessor.html#gaedd8c6e8bc510f0a8bdf24d829fa327f)(_param) BOOST_PP_TUPLE_ELEM(0,[PARAM_FINFO](../../d2/dab/group__ParamAccessor.html#ga2151f807167209a5e8cbcff8cfd897b2)(_param))  
#define | [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(_idx, _param) BOOST_PP_TUPLE_ELEM(PARAM_I##_idx,_param)  
#define | [PARAM_FINFO](../../d2/dab/group__ParamAccessor.html#ga2151f807167209a5e8cbcff8cfd897b2)(_param) [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(INFO,_param)  
#define | [PARAM_FNAME](../../d2/dab/group__ParamAccessor.html#ga0f62d401e0639f5bd438b3aa8d34633c)(_param) [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(NAME,_param)  
#define | [PARAM_FPROP](../../d2/dab/group__ParamAccessor.html#ga777e58665ae90ed497631a7cced4fa69)(_param) [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(PROP,_param)  
#define | [PARAM_FSEQ](../../d2/dab/group__ParamAccessor.html#ga23f3d66f4e1d603c08edb40640f0e000)(_param) [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(SEQ,_param)  
#define | [PARAM_FTYPE](../../d2/dab/group__ParamAccessor.html#ga8056d65a9144418b4282ac302300d2cf)(_param) [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(TYPE,_param)  
#define | [PARAM_IARG](../../d2/dab/group__ParamAccessor.html#gaa34dc07380d9ae9596b79b12d406ef24) 1  
#define | [PARAM_IDEF](../../d2/dab/group__ParamAccessor.html#ga9107039e341ce443b64ba7c68329e456) 3  
#define | [PARAM_IDOC](../../d2/dab/group__ParamAccessor.html#ga5a437bfd2d6528ffc5fa41784e9c0d7f) 4  
#define | [PARAM_IINFO](../../d2/dab/group__ParamAccessor.html#gab29b82b4e6112edd2ae21e75f9fed3d0) 6  
#define | [PARAM_INAME](../../d2/dab/group__ParamAccessor.html#ga83de3d8da8d99f2c5452290dc8ca1ac6) 2  
#define | [PARAM_IPROP](../../d2/dab/group__ParamAccessor.html#gadc5effb212d80fea7cb30d88def9d797) 5  
#define | [PARAM_ISEQ](../../d2/dab/group__ParamAccessor.html#gad5291e85e0bc574dfa4f6a3806184184) 5  
#define | [PARAM_ITYPE](../../d2/dab/group__ParamAccessor.html#ga61f895e41be2d96b02daedc509b87093) 0  
  
## Detailed Description

To abstract parameter field details.

## Macro Definition Documentation

## ◆ PARAM_FARG

#define PARAM_FARG | ( |  | _param| ) |  [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(ARG,_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_FDEF

#define PARAM_FDEF | ( |  | _param| ) |  [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(DEF,_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_FDOC

#define PARAM_FDOC | ( |  | _param| ) |  [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(DOC,_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_FENUM_PREFIX

#define PARAM_FENUM_PREFIX | ( |  | _param| ) |  BOOST_PP_TUPLE_ELEM(1,[PARAM_FINFO](../../d2/dab/group__ParamAccessor.html#ga2151f807167209a5e8cbcff8cfd897b2)(_param))  
---|---|---|---|---|---  
  
## ◆ PARAM_FENUM_TYPE

#define PARAM_FENUM_TYPE | ( |  | _param| ) |  BOOST_PP_TUPLE_ELEM(0,[PARAM_FINFO](../../d2/dab/group__ParamAccessor.html#ga2151f807167209a5e8cbcff8cfd897b2)(_param))  
---|---|---|---|---|---  
  
## ◆ PARAM_FIELD

#define PARAM_FIELD | ( |  | _idx,   
---|---|---|---  
|  |  | _param   
| ) | |  BOOST_PP_TUPLE_ELEM(PARAM_I##_idx,_param)  
  
## ◆ PARAM_FINFO

#define PARAM_FINFO | ( |  | _param| ) |  [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(INFO,_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_FNAME

#define PARAM_FNAME | ( |  | _param| ) |  [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(NAME,_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_FPROP

#define PARAM_FPROP | ( |  | _param| ) |  [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(PROP,_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_FSEQ

#define PARAM_FSEQ | ( |  | _param| ) |  [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(SEQ,_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_FTYPE

#define PARAM_FTYPE | ( |  | _param| ) |  [PARAM_FIELD](../../d2/dab/group__ParamAccessor.html#ga3d0c3d0779007babdbcf53207f0a54e8)(TYPE,_param)  
---|---|---|---|---|---  
  
## ◆ PARAM_IARG

#define PARAM_IARG 1  
---  
  
## ◆ PARAM_IDEF

#define PARAM_IDEF 3  
---  
  
## ◆ PARAM_IDOC

#define PARAM_IDOC 4  
---  
  
## ◆ PARAM_IINFO

#define PARAM_IINFO 6  
---  
  
## ◆ PARAM_INAME

#define PARAM_INAME 2  
---  
  
## ◆ PARAM_IPROP

#define PARAM_IPROP 5  
---  
  
## ◆ PARAM_ISEQ

#define PARAM_ISEQ 5  
---  
  
## ◆ PARAM_ITYPE

#define PARAM_ITYPE 0  
---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

