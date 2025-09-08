---
url: https://freecad.github.io/SourceDoc/d8/df7/classBase_1_1Exception.html
scraped_at: 2025-09-08T15:16:04.810443
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Exception](../../d8/df7/classBase_1_1Exception.html)

[List of all members](../../d1/d53/classBase_1_1Exception-members.html) | Public Member Functions | Static Public Member Functions | Protected Member Functions

Base::Exception Class Reference

`#include <Exception.h>`

##  Public Member Functions  
  
---  
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
static void * | [create](../../d8/df7/classBase_1_1Exception.html#a414ab988781cc35011247bf89a2ab998) (void)  
static [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../d8/df7/classBase_1_1Exception.html#aba0b86e61e79e9ccfd2f572d5162531e) (void)  
static void | [init](../../d8/df7/classBase_1_1Exception.html#aa5f325f865abb611f5fd93277905f978) (void)  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
  
##  Protected Member Functions  
  
---  
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
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Constructor & Destructor Documentation

## ◆ ~Exception()

| virtual Base::Exception::~Exception  | ( | | ) |   
---|---|---|---|---  
throw | (|   
| )| |   
virtual  
  
## ◆ Exception() [1/4]

| Exception::Exception  | ( | const char *  | _sMessage_| ) |   
---|---|---|---|---|---  
protected  
  
## ◆ Exception() [2/4]

| Exception::Exception  | ( | const std::string & | _sMessage_| ) |   
---|---|---|---|---|---  
protected  
  
## ◆ Exception() [3/4]

| Exception::Exception  | ( | | ) |   
---|---|---|---|---  
protected  
  
## ◆ Exception() [4/4]

| Exception::Exception  | ( | const [Exception](../../d8/df7/classBase_1_1Exception.html) & | _inst_| ) |   
---|---|---|---|---|---  
protected  
  
## Member Function Documentation

## ◆ create()

| void * Exception::create  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[draftguitools.gui_labels.Label::action()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a31d95b9c0428e8e5e2fc2c0e5ba1f9cf).

## ◆ getClassTypeId()

| [Base::Type](../../dc/dee/classBase_1_1Type.html) Exception::getClassTypeId  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[App::FeatureTestException::FeatureTestException()](../../d5/d03/classApp_1_1FeatureTestException.html#a9485b2b9df4dbdc8e3506511fe7261f2),
and
[Spreadsheet::Sheet::recomputeCell()](../../d0/da8/classSpreadsheet_1_1Sheet.html#ae13fa16166fcbbceb100aea98147b700).

## ◆ getFile()

std::string Exception::getFile  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[ArchReference.ArchReference::execute()](../../d3/d06/classArchReference_1_1ArchReference.html#a27a1a28e3f9c702d7a66c61e66523256),
[ArchReference.ArchReference::getColors()](../../d3/d06/classArchReference_1_1ArchReference.html#ab5326c319a124dd5b03ae6126e663da2),
[ArchReference.ArchReference::getPartsList()](../../d3/d06/classArchReference_1_1ArchReference.html#a6e3b0c7e58d8e58cfc3ec7fc177499c5),
and
[getPyObject()](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb).

## ◆ getFunction()

std::string Exception::getFunction  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[getPyObject()](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb).

## ◆ getLine()

[int](../../d1/da0/classint.html) Exception::getLine  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[getPyObject()](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb).

## ◆ getMessage()

std::string Exception::getMessage  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[getPyObject()](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb).

## ◆ getPyExceptionType()

| [PyObject](../../df/d1b/classPyObject.html) * Exception::getPyExceptionType  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
returns the corresponding python exception type

Reimplemented in
[Base::BadGraphError](../../da/da7/classBase_1_1BadGraphError.html#acdd8fef04e410a398d2720c08a8e213f),
[Base::CADKernelError](../../db/d7a/classBase_1_1CADKernelError.html#a4f5e17650ada6865673ac4057b09829a),
[Base::AbortException](../../de/dce/classBase_1_1AbortException.html#a211c513bca2e08ed48902fea283f7241),
[Base::XMLBaseException](../../d5/dc7/classBase_1_1XMLBaseException.html#a2bbdc32211767472dd6123894d882c5c),
[Base::XMLParseException](../../da/d97/classBase_1_1XMLParseException.html#a883312d16aef49eb16ab2995f90b0b16),
[Base::XMLAttributeError](../../d1/dc9/classBase_1_1XMLAttributeError.html#a3be4b5aea5a7afdbabff95627d77038e),
[Base::FileException](../../d1/dc2/classBase_1_1FileException.html#a96ff5d1876f039597f1a483964622ebd),
[Base::FileSystemError](../../d1/d45/classBase_1_1FileSystemError.html#a079a6e86f5dd4787d3d80931a8226538),
[Base::BadFormatError](../../dc/d45/classBase_1_1BadFormatError.html#a2b7255bcce82a86bc86b6a1efa3578d4),
[Base::MemoryException](../../db/d26/classBase_1_1MemoryException.html#a9735c5e84047586557eae19c24c8934f),
[Base::AccessViolation](../../db/d9c/classBase_1_1AccessViolation.html#a3a31b40eeb4fa2898111a657c587c8b8),
[Base::AbnormalProgramTermination](../../d6/d2b/classBase_1_1AbnormalProgramTermination.html#aed80575be4a6d5b55d43abfc382e0a92),
[Base::UnknownProgramOption](../../de/d21/classBase_1_1UnknownProgramOption.html#ab1dac541dd20e61e0b156cf6c9238550),
[Base::TypeError](../../dd/d62/classBase_1_1TypeError.html#ae02be623600417728aa9cc22c15c7fe2),
[Base::ValueError](../../db/d20/classBase_1_1ValueError.html#aab848bfdb4b25dc0a0349c5280823341),
[Base::IndexError](../../df/d99/classBase_1_1IndexError.html#a500ca95c00c890289c457fcb467fd762),
[Base::NameError](../../de/d2f/classBase_1_1NameError.html#a54bfe4857366923b2a9f6e09bbfaa4ef),
[Base::ImportError](../../d6/d1d/classBase_1_1ImportError.html#a23727f7ce3ee213d092f94d25f54e795),
[Base::AttributeError](../../dd/d37/classBase_1_1AttributeError.html#abb0f7c71ba237e71208b5256fe3e0540),
[Base::RuntimeError](../../db/d57/classBase_1_1RuntimeError.html#a466948712f4d5594968ef2d771fd66c5),
[Base::NotImplementedError](../../d5/d6a/classBase_1_1NotImplementedError.html#a75e9218c250c2d750d9138e0f491e6d5),
[Base::ZeroDivisionError](../../d0/d9b/classBase_1_1ZeroDivisionError.html#a29c8e9ea7779d20e4217d767a65a6f47),
[Base::ReferenceError](../../d9/d46/classBase_1_1ReferenceError.html#ab82c8b4b10f3c6ec35fd227dc52a3ea4),
[Base::ExpressionError](../../d8/d15/classBase_1_1ExpressionError.html#a5082aff9114dbe2481005a2ce77cd1e5),
[Base::ParserError](../../d0/d16/classBase_1_1ParserError.html#a6f8ee4b621d80ebeb270e412b7f0f2dc),
[Base::UnicodeError](../../d7/d74/classBase_1_1UnicodeError.html#acfdbb679649c46ded22ed1bacdfd550c),
[Base::OverflowError](../../d9/dff/classBase_1_1OverflowError.html#a5d65c273f261884748db20bc01381146),
[Base::UnderflowError](../../d9/d07/classBase_1_1UnderflowError.html#a39a6fcbfec18fcf2b29ed95732605f79),
[Base::UnitsMismatchError](../../d9/d9d/classBase_1_1UnitsMismatchError.html#a40f1642e296c453e73e7b3705fd3b25c),
[Base::RestoreError](../../d0/dd2/classBase_1_1RestoreError.html#a8b0f362b935bc876bfdad118d40d4254),
and
[Base::PyException](../../d6/d92/classBase_1_1PyException.html#a0ba2ac9a473c1e8f344b92d2639130f8).

References
[Base::PyExc_FC_GeneralError](../../db/d07/namespaceBase.html#ae4527426552a441e3158bafd69b0561f).

Referenced by
[setPyException()](../../d8/df7/classBase_1_1Exception.html#a58855227991a1be783d3a1e15f1ab7da).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * Exception::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
returns a Python dictionary containing the exception data

Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514).

Reimplemented in
[Base::FileException](../../d1/dc2/classBase_1_1FileException.html#af518f2b1282226fb40c4367c3aca0ae6).

References
[getFile()](../../d8/df7/classBase_1_1Exception.html#adb6e652d6ee9cf2000a0ffeb9ce50597),
[getFunction()](../../d8/df7/classBase_1_1Exception.html#a6c5aa03a617f967abd79221910344718),
[getLine()](../../d8/df7/classBase_1_1Exception.html#add9b14e9f5a48bdaf05487d6a13378be),
[getMessage()](../../d8/df7/classBase_1_1Exception.html#acea06c50f6eeaaaae36f187d99ef9226),
[getTranslatable()](../../d8/df7/classBase_1_1Exception.html#ae930eea23c340668b6621701b70c0e54),
and
[what()](../../d8/df7/classBase_1_1Exception.html#aa330aa854000f17a93919417d977bcac).

Referenced by
[Base::FileException::getPyObject()](../../d1/dc2/classBase_1_1FileException.html#af518f2b1282226fb40c4367c3aca0ae6).

## ◆ getReported()

[bool](../../d9/db9/classbool.html) Base::Exception::getReported  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getTranslatable()

[bool](../../d9/db9/classbool.html) Exception::getTranslatable  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[getPyObject()](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb).

## ◆ getTypeId()

| [Base::Type](../../dc/dee/classBase_1_1Type.html) Exception::getTypeId  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#addbd3a4f09fce7ce5c6bf021e4c1d566).

## ◆ init()

| void Exception::init  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[App::Application::initTypes()](../../da/dbf/classApp_1_1Application.html#a7fd51c3ba729d368d8f150a720af49e1),
and
[DocumentObject.DocumentObject::onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882).

## ◆ operator=()

[Exception](../../d8/df7/classBase_1_1Exception.html) & Exception::operator=  | ( | const [Exception](../../d8/df7/classBase_1_1Exception.html) & | _inst_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Base::FileException::operator=()](../../d1/dc2/classBase_1_1FileException.html#a3205d260dde6b88a6f8b7b6ca32552eb),
and
[Base::MemoryException::operator=()](../../db/d26/classBase_1_1MemoryException.html#a3f2885796dbcbbb70e0d06ddb2425108).

## ◆ ReportException()

| void Exception::ReportException  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reports exception. It includes a mechanism to only report an exception once.

Reimplemented in
[Base::FileException](../../d1/dc2/classBase_1_1FileException.html#aaad485c53871c810d664df1fa89e8368),
and
[Base::PyException](../../d6/d92/classBase_1_1PyException.html#ae319a800388911635841231b22e7be61).

Referenced by
[PartDesignGui::TaskRevolutionParameters::fillAxisCombo()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#ac4453a2dda324c1b0e365a7c9d0afb91),
[PartDesignGui::TaskRevolutionParameters::TaskRevolutionParameters()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#a5509b04d5cfc1da7d5314c4a038a01e2),
[PartDesignGui::TaskHelixParameters::~TaskHelixParameters()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#a98cb4720622cec66c85d46a27b65df3b),
and
[PartDesignGui::TaskRevolutionParameters::~TaskRevolutionParameters()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#a8599459f7437088540a4a0bcb2fbd986).

## ◆ setDebugInformation()

void Exception::setDebugInformation  | ( | const std::string & | _file_ ,   
---|---|---|---  
|  | const [int](../../d1/da0/classint.html) | _line_ ,   
|  | const std::string & | _function_  
| ) | |   
  
setter methods for including debug information intended to use via macro for
autofilling of debugging information

## ◆ setMessage() [1/2]

void Exception::setMessage  | ( | const char *  | _sMessage_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Attacher::ExceptionCancel::ExceptionCancel()](../../d6/dd2/classAttacher_1_1ExceptionCancel.html#aaa77013ce2cbf94f5fcd69d6a5ce90fe),
[SketcherGui::ExceptionWrongInput::ExceptionWrongInput()](../../df/dfb/classSketcherGui_1_1ExceptionWrongInput.html#a0cd16cb476589ee52efe79a371b713e4),
and
[Base::InterpreterSingleton::runInteractiveString()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ad1959d99451e06fdc2c20da250235de8).

## ◆ setMessage() [2/2]

void Exception::setMessage  | ( | const std::string & | _sMessage_| ) |   
---|---|---|---|---|---  
  
## ◆ setPyException()

| void Exception::setPyException  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Sets the Python error indicator and an error message.

Reimplemented in
[Base::PyException](../../d6/d92/classBase_1_1PyException.html#a78dc7a21d8f08e9afc9997fb142c4253).

References
[getPyExceptionType()](../../d8/df7/classBase_1_1Exception.html#a8e85d132bd8da6bcd445748d19c903d1),
[Base::PyExc_FC_GeneralError](../../db/d07/namespaceBase.html#ae4527426552a441e3158bafd69b0561f),
and
[what()](../../d8/df7/classBase_1_1Exception.html#aa330aa854000f17a93919417d977bcac).

## ◆ setPyObject()

| void Exception::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _pydict_| ) |   
---|---|---|---|---|---  
virtual  
  
returns sets the exception data from a Python dictionary

Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

Reimplemented in
[Base::FileException](../../d1/dc2/classBase_1_1FileException.html#ae17c092fdac1087551869fd28dc9d6d4).

Referenced by
[Base::PyException::PyException()](../../d6/d92/classBase_1_1PyException.html#a8fabfe8bd217541fc4c1f5ad217ce95e),
and
[Base::FileException::setPyObject()](../../d1/dc2/classBase_1_1FileException.html#ae17c092fdac1087551869fd28dc9d6d4).

## ◆ setReported()

void Base::Exception::setReported  | ( | [bool](../../d9/db9/classbool.html) | _reported_| ) |   
---|---|---|---|---|---  
  
## ◆ setTranslatable()

void Exception::setTranslatable  | ( | [bool](../../d9/db9/classbool.html) | _translatable_| ) |   
---|---|---|---|---|---  
  
## ◆ what()

| const char * Exception::what  | ( | void  | | ) |  const  
---|---|---|---|---|---  
throw | (|   
| )| |   
virtual  
  
Reimplemented in
[Base::AbortException](../../de/dce/classBase_1_1AbortException.html#add6816e9940cbdab6d412ebfa4f47771),
[Base::XMLParseException](../../da/d97/classBase_1_1XMLParseException.html#a5af1efd5cf1bca6789a49cfbbf191c3d),
[Base::XMLAttributeError](../../d1/dc9/classBase_1_1XMLAttributeError.html#aa79c55500e31fe6ea67488e2c83ccc7a),
and
[Base::FileException](../../d1/dc2/classBase_1_1FileException.html#ae6dc5fb38c5d24c07c2b625dd8c77792).

Referenced by
[PartGui::DlgRevolution::accept()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a92a90c8ff44e8e2f6774d0713d47bbbd),
[PartGui::DlgExtrusion::apply()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a6428c7ac6585ad41ed9792aeea96d2f7),
[App::Origin::execute()](../../d9/d8b/classApp_1_1Origin.html#ae8015373defe4fb60c2a44da46721c84),
[App::OriginGroupExtension::extensionExecute()](../../da/d09/classApp_1_1OriginGroupExtension.html#ae02f4d3ece4b2ce9710f93692832a4c3),
[PartDesignGui::TaskTransformedParameters::fillAxisCombo()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#ad6ce430d06e602964cd7f12725873b88),
[PartDesignGui::TaskTransformedParameters::fillPlanesCombo()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#ac32c32a42e710f2ec1aa6f5e7f6a8d9b),
[getPyObject()](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb),
[Gui::ViewProviderOrigin::onChanged()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[Base::PyException::ReportException()](../../d6/d92/classBase_1_1PyException.html#ae319a800388911635841231b22e7be61),
[setPyException()](../../d8/df7/classBase_1_1Exception.html#a58855227991a1be783d3a1e15f1ab7da),
[Base::PyException::setPyException()](../../d6/d92/classBase_1_1PyException.html#a78dc7a21d8f08e9afc9997fb142c4253),
[Gui::ViewProviderOrigin::setTemporaryVisibility()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#abb766d6f4587e4a16c4d929200944ca1),
[PartDesignGui::TaskBoxPrimitives::TaskBoxPrimitives()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aee4936dd78a78c4d0f6fcc168d1a9c13),
[PartDesignGui::ViewProviderBody::updateOriginDatumSize()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3c7c680a5e55c6cc695c82c8b45935c0),
[Gui::ViewProviderOriginGroupExtension::updateOriginSize()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a254bd812cc1814ed270f1d92e445ad8e),
[PartGui::DlgExtrusion::validate()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a9434547a26c67894da218387403f1c86),
[PartGui::DlgRevolution::validate()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a46d010b2d22c69a04bb9ede6a9d71c77),
[Base::AbortException::what()](../../de/dce/classBase_1_1AbortException.html#add6816e9940cbdab6d412ebfa4f47771),
[Base::XMLParseException::what()](../../da/d97/classBase_1_1XMLParseException.html#a5af1efd5cf1bca6789a49cfbbf191c3d),
[Base::XMLAttributeError::what()](../../d1/dc9/classBase_1_1XMLAttributeError.html#aa79c55500e31fe6ea67488e2c83ccc7a),
[PartDesignGui::TaskBoxPrimitives::~TaskBoxPrimitives()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a999b4dee6e102f972f0c3b3bb1307d7e),
[PartDesignGui::TaskLinearPatternParameters::~TaskLinearPatternParameters()](../../da/d31/classPartDesignGui_1_1TaskLinearPatternParameters.html#abd8fe23f24b1d9df85617e19073b621e),
[PartDesignGui::TaskMirroredParameters::~TaskMirroredParameters()](../../d8/d3c/classPartDesignGui_1_1TaskMirroredParameters.html#a9076e03f1dd9d1c76cf8005459c68a98),
and
[PartDesignGui::TaskPolarPatternParameters::~TaskPolarPatternParameters()](../../d7/d72/classPartDesignGui_1_1TaskPolarPatternParameters.html#afb1b6200d5c009f245e1f5bb4e82e79d).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Exception.h
  * FreeCAD/src/Base/Exception.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

