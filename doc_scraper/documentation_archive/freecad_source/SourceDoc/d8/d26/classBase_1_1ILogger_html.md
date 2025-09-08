---
url: https://freecad.github.io/SourceDoc/d8/d26/classBase_1_1ILogger.html
scraped_at: 2025-09-08T15:16:24.866180
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [ILogger](../../d8/d26/classBase_1_1ILogger.html)

[List of all members](../../d4/d4d/classBase_1_1ILogger-members.html) | Public Member Functions | Public Attributes

Base::ILogger Class Referenceabstract

The Logger Interface This class describes an Interface for logging within
FreeCAD. [More...](../../d8/d26/classBase_1_1ILogger.html#details)

`#include <Console.h>`

##  Public Member Functions  
  
---  
|
[ILogger](../../d8/d26/classBase_1_1ILogger.html#ac6ab069f5327e525757cf0e648ebd011)
()  
virtual const char * | [Name](../../d8/d26/classBase_1_1ILogger.html#ac947ca3f680d948d3dff92fce524659c) ()  
virtual void | [SendLog](../../d8/d26/classBase_1_1ILogger.html#a6de9b82c247a06262f8e592b427f3be7) (const std::string &msg, [LogStyle](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126) [level](../../d1/da0/classint.html))=0  
| Used to send a Log message at the given level.
[More...](../../d8/d26/classBase_1_1ILogger.html#a6de9b82c247a06262f8e592b427f3be7)  
  
virtual | [~ILogger](../../d8/d26/classBase_1_1ILogger.html#a467b41fa3b41e36e33d03fd0519687ec) ()=0  
  
##  Public Attributes  
  
---  
[bool](../../d9/db9/classbool.html) | [bErr](../../d8/d26/classBase_1_1ILogger.html#a4a39644f9509a9d4bff1d201c3878748)  
[bool](../../d9/db9/classbool.html) | [bLog](../../d8/d26/classBase_1_1ILogger.html#a8753678619bcabcddc21d0da955ecdce)  
[bool](../../d9/db9/classbool.html) | [bMsg](../../d8/d26/classBase_1_1ILogger.html#aca879668d459839a2bd65524cf38fbf6)  
[bool](../../d9/db9/classbool.html) | [bWrn](../../d8/d26/classBase_1_1ILogger.html#a4eb0f75d0a65ffad264bd0bb610f026a)  
  
## Detailed Description

The Logger Interface This class describes an Interface for logging within
FreeCAD.

If you want to add a new "sink" to FreeCAD's logging mechanism, then inherit
this class. You'll also need to register your derived class with
[ConsoleSingleton](../../df/dca/classBase_1_1ConsoleSingleton.html "The
console class This class manage all the stdio stuff.").

See also

    [ConsoleSingleton](../../df/dca/classBase_1_1ConsoleSingleton.html "The console class This class manage all the stdio stuff.")

## Constructor & Destructor Documentation

## ◆ ILogger()

Base::ILogger::ILogger  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~ILogger()

| Base::ILogger::~ILogger  | ( | | ) |   
---|---|---|---|---  
pure virtual  
  
## Member Function Documentation

## ◆ Name()

| virtual const char * Base::ILogger::Name  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[ILoggerBlockerTest](../../d3/d59/classILoggerBlockerTest.html#aa46233f20068b6f12d067a06d568a2ad),
[Gui::SplashObserver](../../d4/d46/classGui_1_1SplashObserver.html#a620d404c4d479db52dab9c7e58c4185b),
[Base::ConsoleObserverFile](../../d9/dae/classBase_1_1ConsoleObserverFile.html#a5e44e2c066876952adadedd78e542621),
[Base::ConsoleObserverStd](../../d0/d06/classBase_1_1ConsoleObserverStd.html#a19c71b389c3fca7c97bdaa5d746b0541),
[Gui::GUIConsole](../../d2/d45/classGui_1_1GUIConsole.html#a5dcf5322e208f27c71291069c19faddd),
[Gui::StatusBarObserver](../../de/da6/classGui_1_1StatusBarObserver.html#a5f5e66c3862e6ed0fbbb58de0e053d0f),
and
[Gui::DockWnd::ReportOutput](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#ada4db4c53c4a3a8a899b29d0bf2541ef).

Referenced by
[Base::ConsoleSingleton::Get()](../../df/dca/classBase_1_1ConsoleSingleton.html#ae4ca9fea6787c5acd17c66dbfbbe374b).

## ◆ SendLog()

| virtual void Base::ILogger::SendLog  | ( | const std::string & | _msg_ ,   
---|---|---|---  
|  | [LogStyle](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126) | _level_  
| ) | |   
pure virtual  
  
Used to send a Log message at the given level.

Implemented in
[Base::ConsoleObserverFile](../../d9/dae/classBase_1_1ConsoleObserverFile.html#a22a34d14d271dae40d34325809d3f0a3),
[Base::ConsoleObserverStd](../../d0/d06/classBase_1_1ConsoleObserverStd.html#a7ff0b92a290e44bc7e1dbbabbed377df),
[Gui::TestConsoleObserver](../../df/d59/classGui_1_1TestConsoleObserver.html#ad220e9925e1946893a1a00409e9bc765),
[ILoggerBlockerTest](../../d3/d59/classILoggerBlockerTest.html#a44d6c219b9d2681b2cfdd74e3f40220b),
[Gui::GUIConsole](../../d2/d45/classGui_1_1GUIConsole.html#a96254e4719ad99b471baad4aa65c6ee7),
[Gui::StatusBarObserver](../../de/da6/classGui_1_1StatusBarObserver.html#a0f8b3572bb21af1300786f02385f4c6e),
[Gui::DockWnd::ReportOutput](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a0e1370d2bcd9297652169b1bb41727df),
and
[Gui::SplashObserver](../../d4/d46/classGui_1_1SplashObserver.html#a595a7c4db731b2d79445d029a815bd3b).

Referenced by
[Base::Builder3D::saveToLog()](../../d6/d1b/classBase_1_1Builder3D.html#a219f6a61f1f9f0216ab0b47e0efddfa6).

## Member Data Documentation

## ◆ bErr

[bool](../../d9/db9/classbool.html) Base::ILogger::bErr  
---  
  
Referenced by
[Gui::DockWnd::ReportOutput::contextMenuEvent()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a39abeea98de575f380c2fe463a8f36ad),
[Gui::DockWnd::ReportOutput::isError()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a24b75ea19647b617a513ad6051b18810),
[Base::ConsoleSingleton::IsMsgTypeEnabled()](../../df/dca/classBase_1_1ConsoleSingleton.html#a139867f1225d10047562f6aa964e0d22),
[Gui::DockWnd::ReportOutput::OnChange()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a2cc6fa8a2c5e658397b7ef09861e799e),
[Gui::DockWnd::ReportOutput::onToggleError()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a38031c483b8cd81d4f0782c43ae70393),
[Base::ConsoleSingleton::SetEnabledMsgType()](../../df/dca/classBase_1_1ConsoleSingleton.html#ad7f0fab600123b5a812f364e058fde09),
[Base::ConsoleSingleton::sPyGetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#ac31064289a9d46191b3fe33692bb3483),
and
[Base::ConsoleSingleton::sPySetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#a38ebfd3e6dd742dd3cfc180bc03025e3).

## ◆ bLog

[bool](../../d9/db9/classbool.html) Base::ILogger::bLog  
---  
  
Referenced by
[Base::ConsoleObserverStd::ConsoleObserverStd()](../../d0/d06/classBase_1_1ConsoleObserverStd.html#aa778d314d8db84ff0fe8360e52b2b4f9),
[Gui::DockWnd::ReportOutput::contextMenuEvent()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a39abeea98de575f380c2fe463a8f36ad),
[Gui::DockWnd::ReportOutput::isLogMessage()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#aa9b3e5a1c5e57597b9d8df7c825c7ba5),
[Base::ConsoleSingleton::IsMsgTypeEnabled()](../../df/dca/classBase_1_1ConsoleSingleton.html#a139867f1225d10047562f6aa964e0d22),
[Gui::DockWnd::ReportOutput::OnChange()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a2cc6fa8a2c5e658397b7ef09861e799e),
[Gui::DockWnd::ReportOutput::onToggleLogMessage()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a869ff8ca717ffee7bde0765e62d0fd81),
[Gui::DockWnd::ReportOutput::ReportOutput()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a33a19a15d61085fb3211e7fb522c5fe3),
[Base::ConsoleSingleton::SetEnabledMsgType()](../../df/dca/classBase_1_1ConsoleSingleton.html#ad7f0fab600123b5a812f364e058fde09),
[Base::ConsoleSingleton::sPyGetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#ac31064289a9d46191b3fe33692bb3483),
and
[Base::ConsoleSingleton::sPySetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#a38ebfd3e6dd742dd3cfc180bc03025e3).

## ◆ bMsg

[bool](../../d9/db9/classbool.html) Base::ILogger::bMsg  
---  
  
Referenced by
[Gui::DockWnd::ReportOutput::contextMenuEvent()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a39abeea98de575f380c2fe463a8f36ad),
[Base::ConsoleSingleton::IsMsgTypeEnabled()](../../df/dca/classBase_1_1ConsoleSingleton.html#a139867f1225d10047562f6aa964e0d22),
[Gui::DockWnd::ReportOutput::isNormalMessage()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#aeeddb9b4a3f89eff4f3c5a5659411f5a),
[Gui::DockWnd::ReportOutput::OnChange()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a2cc6fa8a2c5e658397b7ef09861e799e),
[Gui::DockWnd::ReportOutput::onToggleNormalMessage()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#ab1bd0569990676cd5e28ddfe6069d863),
[Base::ConsoleSingleton::SetEnabledMsgType()](../../df/dca/classBase_1_1ConsoleSingleton.html#ad7f0fab600123b5a812f364e058fde09),
[Base::ConsoleSingleton::sPyGetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#ac31064289a9d46191b3fe33692bb3483),
and
[Base::ConsoleSingleton::sPySetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#a38ebfd3e6dd742dd3cfc180bc03025e3).

## ◆ bWrn

[bool](../../d9/db9/classbool.html) Base::ILogger::bWrn  
---  
  
Referenced by
[Gui::DockWnd::ReportOutput::contextMenuEvent()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a39abeea98de575f380c2fe463a8f36ad),
[Base::ConsoleSingleton::IsMsgTypeEnabled()](../../df/dca/classBase_1_1ConsoleSingleton.html#a139867f1225d10047562f6aa964e0d22),
[Gui::DockWnd::ReportOutput::isWarning()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a0de2c35e51533ff14c467e7e740ffb0a),
[Gui::DockWnd::ReportOutput::OnChange()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a2cc6fa8a2c5e658397b7ef09861e799e),
[Gui::DockWnd::ReportOutput::onToggleWarning()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a24b60fc9d8cc36a9d53ba1ad4afc739a),
[Base::ConsoleSingleton::SetEnabledMsgType()](../../df/dca/classBase_1_1ConsoleSingleton.html#ad7f0fab600123b5a812f364e058fde09),
[Base::ConsoleSingleton::sPyGetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#ac31064289a9d46191b3fe33692bb3483),
and
[Base::ConsoleSingleton::sPySetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#a38ebfd3e6dd742dd3cfc180bc03025e3).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Console.h
  * FreeCAD/src/Base/Console.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

