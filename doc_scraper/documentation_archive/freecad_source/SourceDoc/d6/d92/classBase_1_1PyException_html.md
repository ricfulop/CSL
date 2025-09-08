---
url: https://freecad.github.io/SourceDoc/d6/d92/classBase_1_1PyException.html
scraped_at: 2025-09-08T15:16:56.037878
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [PyException](../../d6/d92/classBase_1_1PyException.html)

[List of all members](../../d7/d5f/classBase_1_1PyException-members.html) | Public Member Functions | Static Public Member Functions

Base::PyException Class Reference

`#include <Interpreter.h>`

##  Public Member Functions  
  
---  
const std::string & | [getErrorType](../../d6/d92/classBase_1_1PyException.html#a51070481bbd1a6e09d0726dc8f9a8f2a) () const  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyExceptionType](../../d6/d92/classBase_1_1PyException.html#a0ba2ac9a473c1e8f344b92d2639130f8) (void) const override  
| returns the corresponding python exception type
[More...](../../d6/d92/classBase_1_1PyException.html#a0ba2ac9a473c1e8f344b92d2639130f8)  
  
const std::string & | [getStackTrace](../../d6/d92/classBase_1_1PyException.html#aa3fe9375162dff818a3b524a71beef81) () const  
| this function returns the stack trace
[More...](../../d6/d92/classBase_1_1PyException.html#aa3fe9375162dff818a3b524a71beef81)  
  
|
[PyException](../../d6/d92/classBase_1_1PyException.html#a8fabfe8bd217541fc4c1f5ad217ce95e)
()  
| constructor does the whole job
[More...](../../d6/d92/classBase_1_1PyException.html#a8fabfe8bd217541fc4c1f5ad217ce95e)  
  
|
[PyException](../../d6/d92/classBase_1_1PyException.html#a86457424b1cde739794c0cc4efd89185)
(const Py::Object &obj)  
void | [raiseException](../../d6/d92/classBase_1_1PyException.html#a8f4e6f2c289fb9af6af8315ce6538c29) ()  
void | [ReportException](../../d6/d92/classBase_1_1PyException.html#ae319a800388911635841231b22e7be61) () const override  
| Reports exception. It includes a mechanism to only report an exception once.
[More...](../../d6/d92/classBase_1_1PyException.html#ae319a800388911635841231b22e7be61)  
  
virtual void | [setPyException](../../d6/d92/classBase_1_1PyException.html#a78dc7a21d8f08e9afc9997fb142c4253) () const override  
| Sets the Python error indicator and an error message.
[More...](../../d6/d92/classBase_1_1PyException.html#a78dc7a21d8f08e9afc9997fb142c4253)  
  
|
[~PyException](../../d6/d92/classBase_1_1PyException.html#a17f3cfacb59ca1ed8ad66f715aa79db8)
() throw ()  
![-](../../closed.png) Public Member Functions inherited from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html)  
std::string | [getFile](../../d8/df7/classBase_1_1Exception.html#adb6e652d6ee9cf2000a0ffeb9ce50597) () const  
std::string | [getFunction](../../d8/df7/classBase_1_1Exception.html#a6c5aa03a617f967abd79221910344718) () const  
[int](../../d1/da0/classint.html) | [getLine](../../d8/df7/classBase_1_1Exception.html#add9b14e9f5a48bdaf05487d6a13378be) () const  
std::string | [getMessage](../../d8/df7/classBase_1_1Exception.html#acea06c50f6eeaaaae36f187d99ef9226) () const  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyExceptionType](../../d8/df7/classBase_1_1Exception.html#a8e85d132bd8da6bcd445748d19c903d1) () const  
| returns the corresponding python exception type
[More...](../../d8/df7/classBase_1_1Exception.html#a8e85d132bd8da6bcd445748d19c903d1)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb) ()  
| returns a Python dictionary containing the exception data
[More...](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb)  
  
[bool](../../d9/db9/classbool.html) | [getReported](../../d8/df7/classBase_1_1Exception.html#ad82759cc946e2441cadef6776727be05) () const  
[bool](../../d9/db9/classbool.html) | [getTranslatable](../../d8/df7/classBase_1_1Exception.html#ae930eea23c340668b6621701b70c0e54) () const  
virtual [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getTypeId](../../d8/df7/classBase_1_1Exception.html#ad6856a6fd1d296adfcb2972d4cdf33ee) (void) const  
[Exception](../../d8/df7/classBase_1_1Exception.html) & | [operator=](../../d8/df7/classBase_1_1Exception.html#a73deac583ceab824678f8bdd7f0ea40c) (const [Exception](../../d8/df7/classBase_1_1Exception.html) &inst)  
virtual void | [ReportException](../../d8/df7/classBase_1_1Exception.html#a5703117e47253fbf07d86b702f9fdae4) () const  
| Reports exception. It includes a mechanism to only report an exception once.
[More...](../../d8/df7/classBase_1_1Exception.html#a5703117e47253fbf07d86b702f9fdae4)  
  
void | [setDebugInformation](../../d8/df7/classBase_1_1Exception.html#ae7e93feb4245a77e067796b480cea0c6) (const std::string &file, const [int](../../d1/da0/classint.html) line, const std::string &function)  
| setter methods for including debug information intended to use via macro for
autofilling of debugging information
[More...](../../d8/df7/classBase_1_1Exception.html#ae7e93feb4245a77e067796b480cea0c6)  
  
void | [setMessage](../../d8/df7/classBase_1_1Exception.html#ac112f8e1e18aa8bccc4902daae47c446) (const char *sMessage)  
void | [setMessage](../../d8/df7/classBase_1_1Exception.html#a4ea8dd5f1dea35e138bea6ebcefba850) (const std::string &sMessage)  
virtual void | [setPyException](../../d8/df7/classBase_1_1Exception.html#a58855227991a1be783d3a1e15f1ab7da) () const  
| Sets the Python error indicator and an error message.
[More...](../../d8/df7/classBase_1_1Exception.html#a58855227991a1be783d3a1e15f1ab7da)  
  
virtual void | [setPyObject](../../d8/df7/classBase_1_1Exception.html#afdfd5b57a05575d1ec05297e2f6e656e) ([PyObject](../../df/d1b/classPyObject.html) *pydict)  
| returns sets the exception data from a Python dictionary
[More...](../../d8/df7/classBase_1_1Exception.html#afdfd5b57a05575d1ec05297e2f6e656e)  
  
void | [setReported](../../d8/df7/classBase_1_1Exception.html#a66b0937f234eacc2716c594acbe3ec94) ([bool](../../d9/db9/classbool.html) reported)  
void | [setTranslatable](../../d8/df7/classBase_1_1Exception.html#a776e57a0e4877acfd47b2e2a225a83a9) ([bool](../../d9/db9/classbool.html) translatable)  
virtual const char * | [what](../../d8/df7/classBase_1_1Exception.html#aa330aa854000f17a93919417d977bcac) () const throw ()  
virtual | [~Exception](../../d8/df7/classBase_1_1Exception.html#a9e6152e43a70c1318c392c4dc107281f) () throw ()  
![-](../../closed.png) Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
|
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a84b1d36d0060e74a7b48255bca0d1928)
()  
| Construction.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a84b1d36d0060e74a7b48255bca0d1928)  
  
|
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html#ae41bc09a1498fbd4e952e7a7dd9de791)
(const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) &)=default  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514) ()  
| This method returns the Python wrapper for a C++ object.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514)  
  
virtual [Type](../../dc/dee/classBase_1_1Type.html) | [getTypeId](../../df/d4d/classBase_1_1BaseClass.html#addbd3a4f09fce7ce5c6bf021e4c1d566) () const  
[bool](../../d9/db9/classbool.html) | [isDerivedFrom](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html) & | [operator=](../../df/d4d/classBase_1_1BaseClass.html#ad334dfcaf7aa8b86993eaefac41207c2) (const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) &)=default  
virtual void | [setPyObject](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e) ([PyObject](../../df/d1b/classPyObject.html) *)  
virtual | [~BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a7bd44242e16f121ed78718ee8c234f49) ()  
| Destruction.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a7bd44242e16f121ed78718ee8c234f49)  
  
  
##  Static Public Member Functions  
  
---  
static void | [ThrowException](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130) ()  
| this method determines if the original exception can be reconstructed or
not, if yes throws the reconstructed version if not, throws a generic
[PyException](../../d6/d92/classBase_1_1PyException.html).
[More...](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130)  
  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html)  
static void * | [create](../../d8/df7/classBase_1_1Exception.html#a414ab988781cc35011247bf89a2ab998) (void)  
static [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../d8/df7/classBase_1_1Exception.html#aba0b86e61e79e9ccfd2f572d5162531e) (void)  
static void | [init](../../d8/df7/classBase_1_1Exception.html#aa5f325f865abb611f5fd93277905f978) (void)  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Protected Member Functions inherited from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html)  
|
[Exception](../../d8/df7/classBase_1_1Exception.html#a1b78336bb26edf8e784783cc150c5801)
()  
|
[Exception](../../d8/df7/classBase_1_1Exception.html#a5ce04114a730cb532695f09d772286a2)
(const char *sMessage)  
|
[Exception](../../d8/df7/classBase_1_1Exception.html#ac5574f4372bed4081146df21053affaf)
(const [Exception](../../d8/df7/classBase_1_1Exception.html) &inst)  
|
[Exception](../../d8/df7/classBase_1_1Exception.html#a959cb3b6f6373185b22965b4352ec3d4)
(const std::string &sMessage)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Constructor & Destructor Documentation

## ◆ PyException() [1/2]

PyException::PyException  | ( | | ) |   
---|---|---|---|---  
  
constructor does the whole job

References
[Base::Exception::setPyObject()](../../d8/df7/classBase_1_1Exception.html#afdfd5b57a05575d1ec05297e2f6e656e).

## ◆ PyException() [2/2]

PyException::PyException  | ( | const Py::Object & | _obj_| ) |   
---|---|---|---|---|---  
  
## ◆ ~PyException()

PyException::~PyException  | ( | | ) |   
---|---|---|---|---  
throw | (|   
| )| |   
  
## Member Function Documentation

## ◆ getErrorType()

const std::string & Base::PyException::getErrorType  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[setPyException()](../../d6/d92/classBase_1_1PyException.html#a78dc7a21d8f08e9afc9997fb142c4253).

## ◆ getPyExceptionType()

| virtual [PyObject](../../df/d1b/classPyObject.html) * Base::PyException::getPyExceptionType  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
returns the corresponding python exception type

Reimplemented from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#a8e85d132bd8da6bcd445748d19c903d1).

Referenced by
[setPyException()](../../d6/d92/classBase_1_1PyException.html#a78dc7a21d8f08e9afc9997fb142c4253).

## ◆ getStackTrace()

const std::string & Base::PyException::getStackTrace  | ( | | ) |  const  
---|---|---|---|---  
  
this function returns the stack trace

Referenced by
[setPyException()](../../d6/d92/classBase_1_1PyException.html#a78dc7a21d8f08e9afc9997fb142c4253).

## ◆ raiseException()

void PyException::raiseException  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::ExceptionFactory::Instance()](../../de/d60/classBase_1_1ExceptionFactory.html#a6d9d2a60381ece442b213d7fad30a605),
[Base::PyExc_FC_FreeCADAbort](../../db/d07/namespaceBase.html#a88fbf97a5034eb681198ed1d6d5d050b),
and
[Base::ExceptionFactory::raiseException()](../../de/d60/classBase_1_1ExceptionFactory.html#a026955dc51bc6bdfad999fc684393b43).

Referenced by
[ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

## ◆ ReportException()

| void PyException::ReportException  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Reports exception. It includes a mechanism to only report an exception once.

Reimplemented from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#a5703117e47253fbf07d86b702f9fdae4).

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
and
[Base::Exception::what()](../../d8/df7/classBase_1_1Exception.html#aa330aa854000f17a93919417d977bcac).

Referenced by
[Gui::GestureNavigationStyle::onRollGesture()](../../dd/df8/classGui_1_1GestureNavigationStyle.html#aea1942b7bbfc657cbfe2ae892811b802),
and
[ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

## ◆ setPyException()

| void PyException::setPyException  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Sets the Python error indicator and an error message.

Reimplemented from
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#a58855227991a1be783d3a1e15f1ab7da).

References
[getErrorType()](../../d6/d92/classBase_1_1PyException.html#a51070481bbd1a6e09d0726dc8f9a8f2a),
[getPyExceptionType()](../../d6/d92/classBase_1_1PyException.html#a0ba2ac9a473c1e8f344b92d2639130f8),
[getStackTrace()](../../d6/d92/classBase_1_1PyException.html#aa3fe9375162dff818a3b524a71beef81),
and
[Base::Exception::what()](../../d8/df7/classBase_1_1Exception.html#aa330aa854000f17a93919417d977bcac).

## ◆ ThrowException()

| void PyException::ThrowException  | ( | | ) |   
---|---|---|---|---  
static  
  
this method determines if the original exception can be reconstructed or not,
if yes throws the reconstructed version if not, throws a generic
[PyException](../../d6/d92/classBase_1_1PyException.html).

References
[raiseException()](../../d6/d92/classBase_1_1PyException.html#a8f4e6f2c289fb9af6af8315ce6538c29),
and
[ReportException()](../../d6/d92/classBase_1_1PyException.html#ae319a800388911635841231b22e7be61).

Referenced by
[App::ObjectIdentifier::Component::del()](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ad38cc5ffd0fb239b9045c184ec2b855a),
[Gui::ViewProviderPythonFeatureImp::dropObject()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a63435f3e63ff0a2bd34f8349c416445a),
[Gui::ViewProviderPythonFeatureImp::dropObjectEx()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#ad8b0939f5e8dce59a6217e27a5ff70f7),
[App::FeaturePythonImp::execute()](../../de/d49/classApp_1_1FeaturePythonImp.html#ac1d17c03bc1f7d0fc643444b0a2fd069),
[App::ObjectIdentifier::Component::get()](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ad99dffa416e065802811bcccd62bf0f7),
[App::ObjectIdentifier::getPyValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a51896520089a0ba883333f2a6bcb56c6),
[App::ObjectIdentifier::getValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c),
[Base::InterpreterSingleton::runString()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a2cabac4e610e966ebc33a1e1aa5d94b6),
[Base::InterpreterSingleton::runStringWithKey()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a4c280c31dede4ae71e9170f5a868c703),
[App::ObjectIdentifier::Component::set()](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ac9f438dcde3d18fac9f14fe5d2bd7bfa),
and
[App::ObjectIdentifier::setValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a208a7e99d236e98ca3e6165ce858480b).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Interpreter.h
  * FreeCAD/src/Base/Interpreter.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

