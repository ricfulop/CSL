---
url: https://freecad.github.io/SourceDoc/d7/d78/group__ParamCommon.html
scraped_at: 2025-09-08T14:52:14.869601
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Modules | Macros

Common helpers

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Path](../../dc/db4/group__PATH.html) » [Parameters helper
macros](../../dc/dbe/group__ParamHelper.html)

##  Modules  
  
---  
| [Enum convert helpers](../../dc/dd3/group__ParamEnumHelper.html)  
  
##  Macros  
  
---  
#define | [PARAM_ARGS](../../d7/d78/group__ParamCommon.html#ga5a0a1fd4aef02bdd6765193c429a45b2)(_src, _seq) BOOST_PP_SEQ_FOR_EACH_I(PARAM_ARGS_,_src,_seq)  
| Declare the parameters as function argument list without defaults.
[More...](../../d7/d78/group__ParamCommon.html#ga5a0a1fd4aef02bdd6765193c429a45b2)  
  
#define | [PARAM_ARGS_DEF](../../d7/d78/group__ParamCommon.html#ga19abef94c6175c1689763728c1141f5c)(_src, _seq) BOOST_PP_SEQ_FOR_EACH_I(PARAM_ARGS_DEF_,_src,_seq)  
| Declare the parameters as function argument list with defaults.
[More...](../../d7/d78/group__ParamCommon.html#ga19abef94c6175c1689763728c1141f5c)  
  
#define | [PARAM_DECLARE](../../d7/d78/group__ParamCommon.html#gab05ad84c49b86ccc9ea593e2201bcc35)(_src, _seq) BOOST_PP_SEQ_FOR_EACH(PARAM_DECLARE_,_src,_seq)  
| Declares parameters using the given field as name.
[More...](../../d7/d78/group__ParamCommon.html#gab05ad84c49b86ccc9ea593e2201bcc35)  
  
#define | [PARAM_DECLARE_INIT](../../d7/d78/group__ParamCommon.html#gabc2a244c81dfbe284e8b6e1001e48de5)(_src, _seq) BOOST_PP_SEQ_FOR_EACH(PARAM_DECLARE_INIT_,_src,_seq)  
| Declares parameters with initialization to default using the given field as
name.
[More...](../../d7/d78/group__ParamCommon.html#gabc2a244c81dfbe284e8b6e1001e48de5)  
  
#define | [PARAM_INIT](../../d7/d78/group__ParamCommon.html#ga696ff575d541d135f55614b9480d10b3)(_src, _seq) BOOST_PP_SEQ_FOR_EACH_I(PARAM_INIT_,_src,_seq)  
| Constructor initialization.
[More...](../../d7/d78/group__ParamCommon.html#ga696ff575d541d135f55614b9480d10b3)  
  
#define | [PARAM_OP](../../d7/d78/group__ParamCommon.html#gaf6c6c2b84807e70a8772524b6aa218f5)(_src, _op, _dst, _seq) BOOST_PP_SEQ_FOR_EACH(PARAM_COPY_,(_src,_op,_dst),_seq)  
| Perform operation on two instance of each parameter in a sequence.
[More...](../../d7/d78/group__ParamCommon.html#gaf6c6c2b84807e70a8772524b6aa218f5)  
  
#define | [PARAM_TYPE](../../d7/d78/group__ParamCommon.html#ga9b3252991c1587ea7d281c50b7a5317c)(_param) [PARAM_TYPED](../../dc/d97/group__ParamLooper.html#ga357913297c9387d9223f839800ffd504)(PARAM_TYPE_,_param)  
| Obtain parameter type.
[More...](../../d7/d78/group__ParamCommon.html#ga9b3252991c1587ea7d281c50b7a5317c)  
  
  
## Detailed Description

## Macro Definition Documentation

## ◆ PARAM_ARGS

#define PARAM_ARGS | ( |  | _src,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH_I(PARAM_ARGS_,_src,_seq)  
  
Declare the parameters as function argument list without defaults.

  * `_src:` macro to generate source field. See [here](../../d7/d78/group__ParamCommon.html#ParamSrc) for more details

Expand to:

type1 _src(_param1), type2 _src(_param2) ...

## ◆ PARAM_ARGS_DEF

#define PARAM_ARGS_DEF | ( |  | _src,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH_I(PARAM_ARGS_DEF_,_src,_seq)  
  
Declare the parameters as function argument list with defaults.

  * `_src:` macro to generate source field. See [here](../../d7/d78/group__ParamCommon.html#ParamSrc) for more details

Expand to:

type1 _src(_param1)=def1, type2 _src(_param1)=def2 ...

## ◆ PARAM_DECLARE

#define PARAM_DECLARE | ( |  | _src,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH(PARAM_DECLARE_,_src,_seq)  
  
Declares parameters using the given field as name.

  * `_src:Macro` to generate source variable. The signature must be `_src(_param)<\tt>, where `_param` is the tuple defining the parameter. You pass any of the [parameter](../../d2/dab/group__ParamAccessor.html)accessors" to directly access the field. Or, supply your own macro to append any prefix as you like. For example: 

#define MY_SRC(_param) BOOST_PP_CAT(my,PARAM_FNAME(_param))

->

my##<name>

`

Expands to:

type1 _src(_param1);type2 _src(_param2); ...

## ◆ PARAM_DECLARE_INIT

#define PARAM_DECLARE_INIT | ( |  | _src,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH(PARAM_DECLARE_INIT_,_src,_seq)  
  
Declares parameters with initialization to default using the given field as
name.

  * `_src:` macro to generate source field. See [here](../../d7/d78/group__ParamCommon.html#ParamSrc) for more details

Expands to:

type1 _src(_param1)=_def1;type2 _src(_param2)=_def2; ...

## ◆ PARAM_INIT

#define PARAM_INIT | ( |  | _src,   
---|---|---|---  
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH_I(PARAM_INIT_,_src,_seq)  
  
Constructor initialization.

  * `_src:` macro to generate source field. See [here](../../d7/d78/group__ParamCommon.html#ParamSrc) for more details

Expand to,

_src(_param1)(def1), _src(_param1)(def2)...

## ◆ PARAM_OP

#define PARAM_OP | ( |  | _src,   
---|---|---|---  
|  |  | _op,   
|  |  | _dst,   
|  |  | _seq   
| ) | |  BOOST_PP_SEQ_FOR_EACH(PARAM_COPY_,(_src,_op,_dst),_seq)  
  
Perform operation on two instance of each parameter in a sequence.

  * `_src:` Macro to generate source variable. The signature must be `_src(_param)<\tt>, where `_param` is the tuple defining the parameter. You pass any of the [parameter accessors](../../d2/dab/group__ParamAccessor.html) to directly access the field. Or, supply your own macro to append any prefix as you like. `
  * ` `_op:` a boolean operator `
  * ` `_dst:` Same as `_src` above.`

Expands to:

_src(_param1) _op _src(_param2);

## ◆ PARAM_TYPE

#define PARAM_TYPE | ( |  | _param| ) |  [PARAM_TYPED](../../dc/d97/group__ParamLooper.html#ga357913297c9387d9223f839800ffd504)(PARAM_TYPE_,_param)  
---|---|---|---|---|---  
  
Obtain parameter type.

The main purpose is to alias enum type to short

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

