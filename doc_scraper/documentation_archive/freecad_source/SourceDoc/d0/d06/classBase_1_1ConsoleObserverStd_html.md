---
url: https://freecad.github.io/SourceDoc/d0/d06/classBase_1_1ConsoleObserverStd.html
scraped_at: 2025-09-08T15:15:54.720846
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [ConsoleObserverStd](../../d0/d06/classBase_1_1ConsoleObserverStd.html)

[List of all members](../../dd/d7c/classBase_1_1ConsoleObserverStd-members.html) | Public Member Functions | Protected Attributes

Base::ConsoleObserverStd Class Reference

The CmdConsoleObserver class This class is used by the main modules to write
Console messages and logs the system con.
[More...](../../d0/d06/classBase_1_1ConsoleObserverStd.html#details)

`#include <ConsoleObserver.h>`

##  Public Member Functions  
  
---  
|
[ConsoleObserverStd](../../d0/d06/classBase_1_1ConsoleObserverStd.html#aa778d314d8db84ff0fe8360e52b2b4f9)
()  
const char * | [Name](../../d0/d06/classBase_1_1ConsoleObserverStd.html#a19c71b389c3fca7c97bdaa5d746b0541) (void) override  
void | [SendLog](../../d0/d06/classBase_1_1ConsoleObserverStd.html#a7ff0b92a290e44bc7e1dbbabbed377df) (const std::string &message, [LogStyle](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126) [level](../../d1/da0/classint.html)) override  
| Used to send a Log message at the given level.
[More...](../../d0/d06/classBase_1_1ConsoleObserverStd.html#a7ff0b92a290e44bc7e1dbbabbed377df)  
  
|
[~ConsoleObserverStd](../../d0/d06/classBase_1_1ConsoleObserverStd.html#aea0f83f45089167bc0ea7986faa4cf01)
() override  
![-](../../closed.png) Public Member Functions inherited from
[Base::ILogger](../../d8/d26/classBase_1_1ILogger.html)  
|
[ILogger](../../d8/d26/classBase_1_1ILogger.html#ac6ab069f5327e525757cf0e648ebd011)
()  
virtual const char * | [Name](../../d8/d26/classBase_1_1ILogger.html#ac947ca3f680d948d3dff92fce524659c) ()  
virtual void | [SendLog](../../d8/d26/classBase_1_1ILogger.html#a6de9b82c247a06262f8e592b427f3be7) (const std::string &msg, [LogStyle](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126) [level](../../d1/da0/classint.html))=0  
| Used to send a Log message at the given level.
[More...](../../d8/d26/classBase_1_1ILogger.html#a6de9b82c247a06262f8e592b427f3be7)  
  
virtual | [~ILogger](../../d8/d26/classBase_1_1ILogger.html#a467b41fa3b41e36e33d03fd0519687ec) ()=0  
  
##  Protected Attributes  
  
---  
[bool](../../d9/db9/classbool.html) | [useColorStderr](../../d0/d06/classBase_1_1ConsoleObserverStd.html#a3a8a0c8524766e5c720821064bd27ddd)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Attributes inherited from
[Base::ILogger](../../d8/d26/classBase_1_1ILogger.html)  
[bool](../../d9/db9/classbool.html) | [bErr](../../d8/d26/classBase_1_1ILogger.html#a4a39644f9509a9d4bff1d201c3878748)  
[bool](../../d9/db9/classbool.html) | [bLog](../../d8/d26/classBase_1_1ILogger.html#a8753678619bcabcddc21d0da955ecdce)  
[bool](../../d9/db9/classbool.html) | [bMsg](../../d8/d26/classBase_1_1ILogger.html#aca879668d459839a2bd65524cf38fbf6)  
[bool](../../d9/db9/classbool.html) | [bWrn](../../d8/d26/classBase_1_1ILogger.html#a4eb0f75d0a65ffad264bd0bb610f026a)  
  
## Detailed Description

The CmdConsoleObserver class This class is used by the main modules to write
Console messages and logs the system con.

## Constructor & Destructor Documentation

## ◆ ConsoleObserverStd()

ConsoleObserverStd::ConsoleObserverStd  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::ILogger::bLog](../../d8/d26/classBase_1_1ILogger.html#a8753678619bcabcddc21d0da955ecdce).

## ◆ ~ConsoleObserverStd()

| ConsoleObserverStd::~ConsoleObserverStd  | ( | | ) |   
---|---|---|---|---  
override  
  
## Member Function Documentation

## ◆ Name()

| const char * Base::ConsoleObserverStd::Name  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[Base::ILogger](../../d8/d26/classBase_1_1ILogger.html#ac947ca3f680d948d3dff92fce524659c).

## ◆ SendLog()

| void ConsoleObserverStd::SendLog  | ( | const std::string & | _msg_ ,   
---|---|---|---  
|  | [LogStyle](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126) | _level_  
| ) | |   
overridevirtual  
  
Used to send a Log message at the given level.

Implements
[Base::ILogger](../../d8/d26/classBase_1_1ILogger.html#a6de9b82c247a06262f8e592b427f3be7).

References
[Base::Error](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126a902b0d55fddef6f8d651fe1035b7d4bd),
[Base::Log](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126ace0be71e33226e4c1db2bcea5959f16b),
[Base::Message](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126a4c2a8fe7eaf24721cc7a9f0175115bd4),
and
[Base::Warning](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126a0eaadb4fcb48a0a0ed7bc9868be9fbaa).

## Member Data Documentation

## ◆ useColorStderr

| [bool](../../d9/db9/classbool.html) Base::ConsoleObserverStd::useColorStderr  
---  
protected  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/ConsoleObserver.h
  * FreeCAD/src/Base/ConsoleObserver.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

