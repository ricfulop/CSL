---
url: https://freecad.github.io/SourceDoc/d9/dae/classBase_1_1ConsoleObserverFile.html
scraped_at: 2025-09-08T15:15:53.713782
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [ConsoleObserverFile](../../d9/dae/classBase_1_1ConsoleObserverFile.html)

[List of all members](../../de/d98/classBase_1_1ConsoleObserverFile-members.html) | Public Member Functions | Protected Attributes

Base::ConsoleObserverFile Class Reference

The LoggingConsoleObserver class This class is used by the main modules to
write Console messages and logs to a file.
[More...](../../d9/dae/classBase_1_1ConsoleObserverFile.html#details)

`#include <ConsoleObserver.h>`

##  Public Member Functions  
  
---  
|
[ConsoleObserverFile](../../d9/dae/classBase_1_1ConsoleObserverFile.html#acfd8465fccf0256f177a708ba5a0ff36)
(const char *sFileName)  
const char * | [Name](../../d9/dae/classBase_1_1ConsoleObserverFile.html#a5e44e2c066876952adadedd78e542621) (void) override  
void | [SendLog](../../d9/dae/classBase_1_1ConsoleObserverFile.html#a22a34d14d271dae40d34325809d3f0a3) (const std::string &message, [LogStyle](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126) [level](../../d1/da0/classint.html)) override  
| Used to send a Log message at the given level.
[More...](../../d9/dae/classBase_1_1ConsoleObserverFile.html#a22a34d14d271dae40d34325809d3f0a3)  
  
|
[~ConsoleObserverFile](../../d9/dae/classBase_1_1ConsoleObserverFile.html#aa78836ca0e4db8281009a3e43352c6ee)
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
[Base::ofstream](../../d5/d44/classBase_1_1ofstream.html) | [cFileStream](../../d9/dae/classBase_1_1ConsoleObserverFile.html#ad46eaf6baee468e569be2660259bc567)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Attributes inherited from
[Base::ILogger](../../d8/d26/classBase_1_1ILogger.html)  
[bool](../../d9/db9/classbool.html) | [bErr](../../d8/d26/classBase_1_1ILogger.html#a4a39644f9509a9d4bff1d201c3878748)  
[bool](../../d9/db9/classbool.html) | [bLog](../../d8/d26/classBase_1_1ILogger.html#a8753678619bcabcddc21d0da955ecdce)  
[bool](../../d9/db9/classbool.html) | [bMsg](../../d8/d26/classBase_1_1ILogger.html#aca879668d459839a2bd65524cf38fbf6)  
[bool](../../d9/db9/classbool.html) | [bWrn](../../d8/d26/classBase_1_1ILogger.html#a4eb0f75d0a65ffad264bd0bb610f026a)  
  
## Detailed Description

The LoggingConsoleObserver class This class is used by the main modules to
write Console messages and logs to a file.

## Constructor & Destructor Documentation

## ◆ ConsoleObserverFile()

ConsoleObserverFile::ConsoleObserverFile  | ( | const char *  | _sFileName_| ) |   
---|---|---|---|---|---  
  
References
[cFileStream](../../d9/dae/classBase_1_1ConsoleObserverFile.html#ad46eaf6baee468e569be2660259bc567),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
and
[Base::ConsoleSingleton::Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

## ◆ ~ConsoleObserverFile()

| ConsoleObserverFile::~ConsoleObserverFile  | ( | | ) |   
---|---|---|---|---  
override  
  
References
[cFileStream](../../d9/dae/classBase_1_1ConsoleObserverFile.html#ad46eaf6baee468e569be2660259bc567).

## Member Function Documentation

## ◆ Name()

| const char * Base::ConsoleObserverFile::Name  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[Base::ILogger](../../d8/d26/classBase_1_1ILogger.html#ac947ca3f680d948d3dff92fce524659c).

## ◆ SendLog()

| void ConsoleObserverFile::SendLog  | ( | const std::string & | _msg_ ,   
---|---|---|---  
|  | [LogStyle](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126) | _level_  
| ) | |   
overridevirtual  
  
Used to send a Log message at the given level.

Implements
[Base::ILogger](../../d8/d26/classBase_1_1ILogger.html#a6de9b82c247a06262f8e592b427f3be7).

References
[cFileStream](../../d9/dae/classBase_1_1ConsoleObserverFile.html#ad46eaf6baee468e569be2660259bc567),
[Base::Error](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126a902b0d55fddef6f8d651fe1035b7d4bd),
[Base::Log](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126ace0be71e33226e4c1db2bcea5959f16b),
[Base::Message](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126a4c2a8fe7eaf24721cc7a9f0175115bd4),
and
[Base::Warning](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126a0eaadb4fcb48a0a0ed7bc9868be9fbaa).

## Member Data Documentation

## ◆ cFileStream

| [Base::ofstream](../../d5/d44/classBase_1_1ofstream.html)
Base::ConsoleObserverFile::cFileStream  
---  
protected  
  
Referenced by
[ConsoleObserverFile()](../../d9/dae/classBase_1_1ConsoleObserverFile.html#acfd8465fccf0256f177a708ba5a0ff36),
[SendLog()](../../d9/dae/classBase_1_1ConsoleObserverFile.html#a22a34d14d271dae40d34325809d3f0a3),
and
[~ConsoleObserverFile()](../../d9/dae/classBase_1_1ConsoleObserverFile.html#aa78836ca0e4db8281009a3e43352c6ee).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/ConsoleObserver.h
  * FreeCAD/src/Base/ConsoleObserver.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

