---
url: https://freecad.github.io/SourceDoc/df/dca/classBase_1_1ConsoleSingleton.html
scraped_at: 2025-09-08T15:15:58.865096
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [ConsoleSingleton](../../df/dca/classBase_1_1ConsoleSingleton.html)

[List of all members](../../d0/d5d/classBase_1_1ConsoleSingleton-members.html) | Public Types | Public Member Functions | Static Public Member Functions | Static Public Attributes | Protected Member Functions | Static Protected Member Functions | Protected Attributes | Friends

Base::ConsoleSingleton Class Reference

The console class This class manage all the stdio stuff.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#details)

`#include <Console.h>`

##  Public Types  
  
---  
enum | [ConnectionMode](../../df/dca/classBase_1_1ConsoleSingleton.html#ab636a2b52258e7eb996862ff06d9157f) { [Direct](../../df/dca/classBase_1_1ConsoleSingleton.html#ab636a2b52258e7eb996862ff06d9157faa79964e785fc39b5726c0a4c6cc03599) = 0 , [Queued](../../df/dca/classBase_1_1ConsoleSingleton.html#ab636a2b52258e7eb996862ff06d9157fa9ef54d51ac196670ac5578731895e70d) =1 }  
enum | [ConsoleMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a2605ebb32e2df24f044f0d95df87e4fb) { [Verbose](../../df/dca/classBase_1_1ConsoleSingleton.html#a2605ebb32e2df24f044f0d95df87e4fba5c83abe71dc5d95a0598a974c3b87b13) = 1 }  
| enumaration for the console modes
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#a2605ebb32e2df24f044f0d95df87e4fb)  
  
enum | [FreeCAD_ConsoleMsgType](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399d) { [MsgType_Txt](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dae3438ada440361f8f7bfe29451754b99) = 1 , [MsgType_Log](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da4c8d83da40448a24fd37469122037dfb) = 2 , [MsgType_Wrn](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dadf5163026958f3c10c1c064c405b3e95) = 4 , [MsgType_Err](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da9adf564b5bca3813e28e053f8d208731) = 8 }  
  
##  Public Member Functions  
  
---  
void | [AttachObserver](../../df/dca/classBase_1_1ConsoleSingleton.html#a262cc6be91420e5d64943f40296c8850) ([ILogger](../../d8/d26/classBase_1_1ILogger.html) *pcObserver)  
| Attaches an [Observer](../../de/d63/classBase_1_1Observer.html "Observer
class Implementation of the well known Observer Design Pattern.") to
FCConsole.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#a262cc6be91420e5d64943f40296c8850)  
  
void | [DetachObserver](../../df/dca/classBase_1_1ConsoleSingleton.html#ad4de0de58604c504687caadd42059cd6) ([ILogger](../../d8/d26/classBase_1_1ILogger.html) *pcObserver)  
| Detaches an [Observer](../../de/d63/classBase_1_1Observer.html "Observer
class Implementation of the well known Observer Design Pattern.") from
FCConsole.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#ad4de0de58604c504687caadd42059cd6)  
  
void | [EnableRefresh](../../df/dca/classBase_1_1ConsoleSingleton.html#ae960c2eb9f4dc8d0538ce3f53bed5156) ([bool](../../d9/db9/classbool.html) enable)  
virtual void | [Error](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644) (const char *pMsg,...)  
| Prints a error Message.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644)  
  
[ILogger](../../d8/d26/classBase_1_1ILogger.html) * | [Get](../../df/dca/classBase_1_1ConsoleSingleton.html#ae4ca9fea6787c5acd17c66dbfbbe374b) (const char *Name) const  
[int](../../d1/da0/classint.html) * | [GetLogLevel](../../df/dca/classBase_1_1ConsoleSingleton.html#af6f3be3a7ce02232bb5e7c505d413d91) (const char *tag, [bool](../../d9/db9/classbool.html) create=true)  
[bool](../../d9/db9/classbool.html) | [IsMsgTypeEnabled](../../df/dca/classBase_1_1ConsoleSingleton.html#a139867f1225d10047562f6aa964e0d22) (const char *sObs, [FreeCAD_ConsoleMsgType](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399d) [type](../../d9/d98/classtype.html)) const  
| Enables or disables message types of a certain console observer.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#a139867f1225d10047562f6aa964e0d22)  
  
virtual void | [Log](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964) (const char *pMsg,...)  
| Prints a log Message.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964)  
  
[int](../../d1/da0/classint.html) | [LogLevel](../../df/dca/classBase_1_1ConsoleSingleton.html#a90e43022cf609ba385f4c05ecebad58d) ([int](../../d1/da0/classint.html) [level](../../d1/da0/classint.html)) const  
virtual void | [Message](../../df/dca/classBase_1_1ConsoleSingleton.html#a322664077d1c391e11e07ec903c99e25) (const char *pMsg,...)  
| Prints a Message.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#a322664077d1c391e11e07ec903c99e25)  
  
void | [NotifyError](../../df/dca/classBase_1_1ConsoleSingleton.html#a318de947395635872c44d7dcbab008e9) (const char *sMsg)  
void | [NotifyLog](../../df/dca/classBase_1_1ConsoleSingleton.html#a995c87231e31e1217305cb6edda2c956) (const char *sMsg)  
void | [NotifyMessage](../../df/dca/classBase_1_1ConsoleSingleton.html#a783b072d0c212602f8fedcda067a540c) (const char *sMsg)  
void | [NotifyWarning](../../df/dca/classBase_1_1ConsoleSingleton.html#a4d7cff5f0526f0820a754d47cedcd3b2) (const char *sMsg)  
void | [Refresh](../../df/dca/classBase_1_1ConsoleSingleton.html#a068a6a7499c94bc198bd81471476226d) ()  
void | [SetConnectionMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a48e7205de536c5cebc7048a42fc2157f) ([ConnectionMode](../../df/dca/classBase_1_1ConsoleSingleton.html#ab636a2b52258e7eb996862ff06d9157f) mode)  
void | [SetConsoleMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a43ca5d8af887a90a3af31b327f20fef9) ([ConsoleMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a2605ebb32e2df24f044f0d95df87e4fb) m)  
| Change mode.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#a43ca5d8af887a90a3af31b327f20fef9)  
  
void | [SetDefaultLogLevel](../../df/dca/classBase_1_1ConsoleSingleton.html#a7f5fdbe57a15cb8f919bb2ff361da067) ([int](../../d1/da0/classint.html) [level](../../d1/da0/classint.html))  
ConsoleMsgFlags | [SetEnabledMsgType](../../df/dca/classBase_1_1ConsoleSingleton.html#ad7f0fab600123b5a812f364e058fde09) (const char *sObs, ConsoleMsgFlags [type](../../d9/d98/classtype.html), [bool](../../d9/db9/classbool.html) b)  
| Enables or disables message types of a certain console observer.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#ad7f0fab600123b5a812f364e058fde09)  
  
void | [UnsetConsoleMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a6de533eb2ecb50f6d04a6105a9081236) ([ConsoleMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a2605ebb32e2df24f044f0d95df87e4fb) m)  
| Change mode.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#a6de533eb2ecb50f6d04a6105a9081236)  
  
virtual void | [Warning](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326) (const char *pMsg,...)  
| Prints a warning Message.
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326)  
  
  
##  Static Public Member Functions  
  
---  
static [ConsoleSingleton](../../df/dca/classBase_1_1ConsoleSingleton.html) & | [Instance](../../df/dca/classBase_1_1ConsoleSingleton.html#a12194f03be46abe3cbe3faa2a1c23d43) ()  
| singleton
[More...](../../df/dca/classBase_1_1ConsoleSingleton.html#a12194f03be46abe3cbe3faa2a1c23d43)  
  
  
##  Static Public Attributes  
  
---  
static const unsigned [int](../../d1/da0/classint.html) | [BufferSize](../../df/dca/classBase_1_1ConsoleSingleton.html#a12735efe999dc85636740faa19813efe) = 4024  
static [PyMethodDef](../../da/dab/classPyMethodDef.html) | [Methods](../../df/dca/classBase_1_1ConsoleSingleton.html#aec2685dc0b0250034cb981e8a6f03ffc) []  
  
##  Protected Member Functions  
  
---  
|
[ConsoleSingleton](../../df/dca/classBase_1_1ConsoleSingleton.html#ae6ad9dd7f8d6a266394ace772e25bbaf)
()  
virtual | [~ConsoleSingleton](../../df/dca/classBase_1_1ConsoleSingleton.html#a83bef8152b25f48540c4ca3c00a71037) ()  
  
##  Static Protected Member Functions  
  
---  
static [PyObject](../../df/d1b/classPyObject.html) * | [sPyError](../../df/dca/classBase_1_1ConsoleSingleton.html#a8676363ed03277ee2403a7cd9bf18c5f) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
static [PyObject](../../df/d1b/classPyObject.html) * | [sPyGetStatus](../../df/dca/classBase_1_1ConsoleSingleton.html#ac31064289a9d46191b3fe33692bb3483) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
static [PyObject](../../df/d1b/classPyObject.html) * | [sPyLog](../../df/dca/classBase_1_1ConsoleSingleton.html#a8921316e836ee1f7c2dfc47f033c2c01) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
static [PyObject](../../df/d1b/classPyObject.html) * | [sPyMessage](../../df/dca/classBase_1_1ConsoleSingleton.html#a2e67159961c8ac1b21ba4d528acdc37f) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
static [PyObject](../../df/d1b/classPyObject.html) * | [sPySetStatus](../../df/dca/classBase_1_1ConsoleSingleton.html#a38ebfd3e6dd742dd3cfc180bc03025e3) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
static [PyObject](../../df/d1b/classPyObject.html) * | [sPyWarning](../../df/dca/classBase_1_1ConsoleSingleton.html#a7d356c1cafd385001e50cde27c18d58f) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
  
##  Protected Attributes  
  
---  
[ConnectionMode](../../df/dca/classBase_1_1ConsoleSingleton.html#ab636a2b52258e7eb996862ff06d9157f) | [connectionMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a91ebbf1a2a05d2d70aecfdbceeadcc73)  
  
##  Friends  
  
---  
class | [ConsoleOutput](../../df/dca/classBase_1_1ConsoleSingleton.html#a8dc97c76955165afb204ae2754f09e38)  
  
## Detailed Description

The console class This class manage all the stdio stuff.

This includes Messages, Warnings, Log entries and Errors. The incoming
Messages are distributed with the FCConsoleObserver. The FCConsole class
itself makes no IO, it's more like a manager.

    [ConsoleSingleton](../../df/dca/classBase_1_1ConsoleSingleton.html "The console class This class manage all the stdio stuff.") is a singleton! That means you can access the only instance of the class from every where in c++ by simply using: 

#include <Base/Console.h>

[Base::Console](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729
"Access to the Console This method is used to gain access to the one and only
instance of the
ConsoleS...")().[Log](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964
"Prints a log Message.")("Stage: %d",i);

    [ConsoleSingleton](../../df/dca/classBase_1_1ConsoleSingleton.html "The console class This class manage all the stdio stuff.") is able to switch between several modes to, e.g. switch the logging on or off, or treat Warnings as Errors, and so on... 

See also

    ConsoleObserver 

## Member Enumeration Documentation

## ◆ ConnectionMode

enum
[Base::ConsoleSingleton::ConnectionMode](../../df/dca/classBase_1_1ConsoleSingleton.html#ab636a2b52258e7eb996862ff06d9157f)  
---  
  
Enumerator  
---  
Direct |   
Queued |   
  
## ◆ ConsoleMode

enum
[Base::ConsoleSingleton::ConsoleMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a2605ebb32e2df24f044f0d95df87e4fb)  
---  
  
enumaration for the console modes

Enumerator  
---  
Verbose |   
  
## ◆ FreeCAD_ConsoleMsgType

enum
[Base::ConsoleSingleton::FreeCAD_ConsoleMsgType](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399d)  
---  
  
Enumerator  
---  
MsgType_Txt |   
MsgType_Log |   
MsgType_Wrn |   
MsgType_Err |   
  
## Constructor & Destructor Documentation

## ◆ ConsoleSingleton()

| ConsoleSingleton::ConsoleSingleton  | ( | | ) |   
---|---|---|---|---  
protected  
  
Referenced by
[Instance()](../../df/dca/classBase_1_1ConsoleSingleton.html#a12194f03be46abe3cbe3faa2a1c23d43).

## ◆ ~ConsoleSingleton()

| ConsoleSingleton::~ConsoleSingleton  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
References
[Base::ConsoleOutput::destruct()](../../d5/dea/classBase_1_1ConsoleOutput.html#af6d3b626f1387630323d7a84cb20d427).

## Member Function Documentation

## ◆ AttachObserver()

void ConsoleSingleton::AttachObserver  | ( | [ILogger](../../d8/d26/classBase_1_1ILogger.html) *  | _pcObserver_| ) |   
---|---|---|---|---|---  
  
Attaches an [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") to FCConsole.

Attaches an [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") to Console Use
this method to attach a [ILogger](../../d8/d26/classBase_1_1ILogger.html "The
Logger Interface This class describes an Interface for logging within
FreeCAD.") derived class to the Console.

After the observer is attached all messages will also be forwarded to it.

See also

    [ILogger](../../d8/d26/classBase_1_1ILogger.html "The Logger Interface This class describes an Interface for logging within FreeCAD.")

Referenced by
[CmdTestConsoleOutput::activated()](../../d1/d11/classCmdTestConsoleOutput.html#a06e1202b04d8d4977c36c067be884f4e),
[Gui::DockWnd::ReportOutput::ReportOutput()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a33a19a15d61085fb3211e7fb522c5fe3),
[Gui::SplashObserver::SplashObserver()](../../d4/d46/classGui_1_1SplashObserver.html#a1c90fea7442c16e6ad438308b4c79b9d),
and
[Gui::StatusBarObserver::StatusBarObserver()](../../de/da6/classGui_1_1StatusBarObserver.html#ab05c62ce1106cffcd17c95732f6fd84d).

## ◆ DetachObserver()

void ConsoleSingleton::DetachObserver  | ( | [ILogger](../../d8/d26/classBase_1_1ILogger.html) *  | _pcObserver_| ) |   
---|---|---|---|---|---  
  
Detaches an [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") from FCConsole.

Detaches an [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") from Console Use
this method to detach a [ILogger](../../d8/d26/classBase_1_1ILogger.html "The
Logger Interface This class describes an Interface for logging within
FreeCAD.") derived class.

After detaching you can destruct the
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") or reinsert it
later.

See also

    [ILogger](../../d8/d26/classBase_1_1ILogger.html "The Logger Interface This class describes an Interface for logging within FreeCAD.")

Referenced by
[CmdTestConsoleOutput::activated()](../../d1/d11/classCmdTestConsoleOutput.html#a06e1202b04d8d4977c36c067be884f4e),
[App::Application::destructObserver()](../../da/dbf/classApp_1_1Application.html#a8ba7d824857a33ccb20839ec0ae19e44),
[ILoggerBlockerTest::~ILoggerBlockerTest()](../../d3/d59/classILoggerBlockerTest.html#a871be169df958da1144a1b12deb5624e),
[Gui::DockWnd::ReportOutput::~ReportOutput()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#ab46b58f001ac3135ce4c6a97f225d556),
[Gui::SplashObserver::~SplashObserver()](../../d4/d46/classGui_1_1SplashObserver.html#aa2f2e0a8a30e1854b68206bd4c6e6fd7),
and
[Gui::StatusBarObserver::~StatusBarObserver()](../../de/da6/classGui_1_1StatusBarObserver.html#a5223f31e9b6ac7e865e66b413525a8c2).

## ◆ EnableRefresh()

void ConsoleSingleton::EnableRefresh  | ( | [bool](../../d9/db9/classbool.html) | _enable_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Base::ConsoleRefreshDisabler::ConsoleRefreshDisabler()](../../de/dea/classBase_1_1ConsoleRefreshDisabler.html#a5c64a4de4633478d772bb006714c1df4),
and
[Base::ConsoleRefreshDisabler::~ConsoleRefreshDisabler()](../../de/dea/classBase_1_1ConsoleRefreshDisabler.html#af46f6d76f7ea406ab0a098b223d8df9e).

## ◆ Error()

| void ConsoleSingleton::Error  | ( | const char *  | _pMsg_ ,   
---|---|---|---  
|  |  | _..._  
| ) | |   
virtual  
  
Prints a error Message.

Prints a Message This method issues an Error which makes some execution
impossible.

Errors are used to get the users attention. That means when FreeCAD is running
in GUI mode an Error Message Box pops up. In console mode a colored message is
printed to the console! Don't use this carelessly. For information purposes
the 'Log' or 'Message' methods are more appropriate.

    You can use a printf like interface like: 

[Console](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729
"Access to the Console This method is used to gain access to the one and only
instance of the
ConsoleS...")().[Error](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644
"Prints a error Message.")("Something really bad in %s
happened\n",[str](../../d9/d36/classstr.html));

See also

    [Message](../../df/dca/classBase_1_1ConsoleSingleton.html#a322664077d1c391e11e07ec903c99e25 "Prints a Message.")
     [Warning](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326 "Prints a warning Message.")
     [Log](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964 "Prints a log Message.")

References
[Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644).

Referenced by
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[TechDrawGui::TaskWeldingSymbol::accept()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#ad91ef56ef584a69a7b67e440066ebec8),
[Gui::Dialog::DlgRevertToBackupConfigImp::accept()](../../d1/d47/classGui_1_1Dialog_1_1DlgRevertToBackupConfigImp.html#adb85fea9a78b916a6ca589464b3007e0),
[Gui::PythonCommand::activated()](../../d3/d3a/classGui_1_1PythonCommand.html#ae2ed8b5ea87ffdbf33e43d5d867cac08),
[Gui::PythonGroupCommand::activated()](../../dc/dbb/classGui_1_1PythonGroupCommand.html#ae583c63a82f41e38a36d8304d0b31fad),
[CmdTestConsoleOutput::activated()](../../d1/d11/classCmdTestConsoleOutput.html#a06e1202b04d8d4977c36c067be884f4e),
[Gui::StdCmdDownloadOnlineHelp::activated()](../../dc/d22/classGui_1_1StdCmdDownloadOnlineHelp.html#a29c4d53cfdd555b2a313eaa38cfa18be),
[CmdSketcherConstrainBlock::activated()](../../d9/d19/classCmdSketcherConstrainBlock.html#a9aae799a29f3aac8783c1f99d1ebb21e),
[CmdSketcherConstrainPerpendicular::activated()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#ae4b39128a2a69168a71c214a6632f6fa),
[CmdSketcherConstrainTangent::activated()](../../d8/d80/classCmdSketcherConstrainTangent.html#a49b68ec579dfa3ac0410539e34096f90),
[Gui::Application::activateWorkbench()](../../d9/da8/classGui_1_1Application.html#ac3b3b8a91ba204c6180dab0dccc1a6d8),
[Sketcher::Sketch::addAngleAtPointConstraint()](../../d9/d9b/classSketcher_1_1Sketch.html#aa25c241f5a94019abefb8da3e65e7999),
[TechDraw::DrawViewPart::addCenterLinesToGeom()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a62ef8a93630027fb4c596847a67f5be4),
[Sketcher::Sketch::addConstraints()](../../d9/d9b/classSketcher_1_1Sketch.html#a3a97c0510117baf59db1d91b7302f0f1),
[Sketcher::SketchObject::addCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#a2ae92a618d60a264ed20d7a359b89f98),
[Sketcher::SketchObject::addExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#a700c729d94352b4b144eb083980a702c),
[TechDraw::DrawProjGroup::addProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acfc4e756c8714973996318393180f483),
[Sketcher::Sketch::addSnellsLawConstraint()](../../d9/d9b/classSketcher_1_1Sketch.html#acbe026d46e5e82f2368f0bd36a2aeca7),
[Sketcher::SketchObject::addSymmetric()](../../d9/dad/classSketcher_1_1SketchObject.html#afcbb1d6f5a99e52a70fdf6d9d3c9d361),
[Sketcher::Sketch::addTangentConstraint()](../../d9/d9b/classSketcher_1_1Sketch.html#a167b82b74c453f5766b2bef0d2764c7a),
[Gui::CommandManager::addTo()](../../d1/da7/classGui_1_1CommandManager.html#aae4cdddda8b7ae4d320835fdb3b61b73),
[TechDrawGui::QGSPage::addWeldSymbol()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#ab4551ef1803974a53ffb7a2d9d993e2a),
[Measure::Measurement::angle()](../../d6/d84/classMeasure_1_1Measurement.html#a14819c13176bdf930004bef6f290385b),
[TechDraw::AOE::AOE()](../../d6/d99/classTechDraw_1_1AOE.html#a685a68e866911f9d4fea28a4a24043c5),
[TechDrawGui::TaskSectionView::apply()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a226f1c136253d3921545858eb107b4d5),
[CmdSketcherConstrainBlock::applyConstraint()](../../d9/d19/classCmdSketcherConstrainBlock.html#a44714bcb118510d4f3edb4ab2c65192d),
[CmdSketcherConstrainPerpendicular::applyConstraint()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#aa62bab542b8f016bd752fdef90110778),
[CmdSketcherConstrainTangent::applyConstraint()](../../d8/d80/classCmdSketcherConstrainTangent.html#a90a8595e30112cb64ddb61088c3af96b),
[TechDraw::DrawProjGroup::arrangeViewPointers()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a8a8bdca0831ea0e16e664ad17f0a04f8),
[TechDraw::BaseGeom::baseFactory()](../../db/d3c/classTechDraw_1_1BaseGeom.html#a35837d9934e075eacd49f551155140ce),
[TechDrawGui::QGIFace::buildPixHatch()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#ab8baaa5bce257d6131474520bd84b566),
[TechDraw::CenterLine::calcEndPoints()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a34df15a8a959516ecc49512c3ec5a73c),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[SurfaceGui::GeomFillSurface::changeFillType()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#aa2180cd7b8c690d2addc40f808eefafc),
[ParameterManager::CheckDocument()](../../db/daa/classParameterManager.html#a8e9fd75cb78b5ed8e1906f9648889417),
[Cloud::Module::cloudRestore()](../../d9/d80/classCloud_1_1Module.html#aa40c76175c8f2a0eed92b8a81696a7c4),
[Gui::cmdAppDocumentArgs()](../../d9/dad/namespaceGui.html#ae18764cea1e06b17b2d1bd076e518a8c),
[Gui::cmdAppObjectArgs()](../../d9/dad/namespaceGui.html#ae65adbb72603b47cab814ee2edd77af7),
[Gui::cmdGuiObjectArgs()](../../d9/dad/namespaceGui.html#a47b8cb6aa6de7cd0fcd5809a430edc7f),
[Gui::MacroManager::commit()](../../d8/dc6/classGui_1_1MacroManager.html#a083bd160df4ba3fc4e313cb6c9870cb1),
[SpreadsheetGui::SheetView::confirmAliasChanged()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a417a33ce8aa3a831fed85c08876f84ba),
[TechDrawGui::QGIViewDimension::constructDimensionArc()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a46189f004d7a87822d44aaf7d34824c0),
[TechDrawGui::QGIViewDimension::constructDimensionLine()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#aba70a6532f229c80844d4c191794e088),
[Sketcher::SketchObject::convertToNURBS()](../../d9/dad/classSketcher_1_1SketchObject.html#a23e6660388fbe498a07b07a8c4f065fe),
[TechDrawGui::Grabber3d::copyActiveViewToSvgFile()](../../d7/d83/classTechDrawGui_1_1Grabber3d.html#a44f769bea9d4e116b3667e59bec4e6da),
[Gui::PythonCommand::createAction()](../../d3/d3a/classGui_1_1PythonCommand.html#a3486dbad9b20ec8df29e467219eed099),
[Gui::PythonGroupCommand::createAction()](../../dc/dbb/classGui_1_1PythonGroupCommand.html#af21c8f002781f535ebd59995b294c23a),
[TechDrawGui::TaskActiveView::createActiveView()](../../dd/dea/classTechDrawGui_1_1TaskActiveView.html#a06f867ac197d21160c2b15c19b71718d),
[TechDrawGui::QGISVGTemplate::createClickHandles()](../../d4/d36/classTechDrawGui_1_1QGISVGTemplate.html#a2bcf2fb5e0c80557b727afaaadbb2777),
[TechDrawGui::TaskHatch::createHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ac9d417f22f5d5ed524f63d10cd4e63ef),
[Gui::WidgetFactoryInst::createPreferencePage()](../../d5/d83/classGui_1_1WidgetFactoryInst.html#a3cc9e4ee3575cfdf3398d3b7150190a4),
[Gui::WidgetFactoryInst::createPrefWidget()](../../d5/d83/classGui_1_1WidgetFactoryInst.html#ad74d83f701a7989e321f5dd755960475),
[Part::ExtrusionHelper::createTaperedPrismOffset()](../../d4/dd3/classPart_1_1ExtrusionHelper.html#a739d561ceb259e1a301b840c578d8a3c),
[Gui::WidgetFactoryInst::createWidget()](../../d5/d83/classGui_1_1WidgetFactoryInst.html#a8a166efde23cd16fb19b84de63abf3b3),
[SketcherGui::CurveConverter::CurveConverter()](../../d9/d49/classSketcherGui_1_1CurveConverter.html#aedc47aa90240b39482d98c65c03197b3),
[Sketcher::SketchObject::decreaseBSplineDegree()](../../d9/dad/classSketcher_1_1SketchObject.html#ace68bb529eeba8cd3e39e3418213d044),
[Sketcher::SketchObject::delAllExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#ae20c5b24ce66380931e7da7299dabd6e),
[Sketcher::SketchObject::delExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#a51f4b69d9928669abe729269157d2224),
[Measure::Measurement::delta()](../../d6/d84/classMeasure_1_1Measurement.html#ae7ad27b4e881bd7ad077a64018fed4eb),
[Gui::doCommandT()](../../d9/dad/namespaceGui.html#ac0574bb1f20ec3d7ef2d307071238f6f),
[FemGui::ViewProviderFemPostObject::doubleClicked()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#abe833e8299e59bd079273f4c30af4067),
[PartGui::ViewProviderPart::doubleClicked()](../../d0/dd0/classPartGui_1_1ViewProviderPart.html#af84f7e3575cbacaf3750d005dce3b9e5),
[TechDrawGui::QGIViewDimension::draw()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a5a804977a329425219739213bc82ec70),
[TechDrawGui::QGIViewDimension::drawAngle()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a27c4e7cb613ec0563614d25f802cf6e9),
[TechDrawGui::QGIViewDimension::drawDiameter()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4f99cea83cd1e147dee58d5e4d2c9a65),
[TechDrawGui::QGIViewDimension::drawDistanceExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a4c326f29804428bfd7c9760856dc4f38),
[TechDrawGui::QGIViewDimension::drawDistanceOverride()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#acb3689d2c898c66fe3fde8dd3fbc3978),
[TechDrawGui::QGIViewDimension::drawRadiusExecutive()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a042db9b374ca5344728e534fef6cc4c4),
[TechDrawGui::TaskDetail::editByHighlight()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a171522a8c058fe7bfc31035677757e54),
[Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[Gui::ViewProvider::eventCallback()](../../d3/db3/classGui_1_1ViewProvider.html#a2c9bbafc597aa5e02ebe9f8aac8a2c99),
[Import::FeatureImportIges::Execute()](../../d7/dac/classImport_1_1FeatureImportIges.html#a458fb556aa3581534c7a713c960ded7b),
[Import::FeatureImportStep::Execute()](../../da/dde/classImport_1_1FeatureImportStep.html#a42d170d40ce67819f931b5894145d229),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[Sketcher::SketchObject::execute()](../../d9/dad/classSketcher_1_1SketchObject.html#a06d72232cfde4ef56fd23515cf8434c4),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDraw::DrawViewPart::execute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[Fem::FemVTKTools::exportFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a37e8a3dd86851c4ce056f3cfa7ad0d89),
[Part::AttachExtension::extensionOnChanged()](../../dc/d47/classPart_1_1AttachExtension.html#ac73db2d8f32ca41b89157b47edce44c1),
[PartDesignGui::TaskTransformedParameters::fillAxisCombo()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#ad6ce430d06e602964cd7f12725873b88),
[PartDesignGui::TaskTransformedParameters::fillPlanesCombo()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#ac32c32a42e710f2ec1aa6f5e7f6a8d9b),
[TechDrawGui::QGIViewPart::geomToPainterPath()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#aea20fa3e1100ec52240032c108712790),
[TechDraw::DrawGeomHatch::getDecodedSpecsFromFile()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a554ea0b075dd29378c7a20bc4a76bb54),
[TechDraw::DrawProjGroup::getDirsFromFront()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a66cbbc8038fcab5532278784cbac867b),
[TechDraw::DrawViewDimension::getPointsEdgeVert()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#af66b90afc565ab105dff3a850b9ccbc0),
[TechDraw::DrawViewDimension::getPointsOneEdge()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a74fb8170cf274981663bb1989bb972ca),
[TechDraw::DrawViewDimension::getPointsTwoEdges()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f77703f9d3c576d674a7468b231e1ae),
[TechDraw::DrawViewDimension::getPointsTwoVerts()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a3aeea1b6e40d2eba51a724b38db66455),
[TechDraw::LineGroup::getRecordFromFile()](../../da/d19/classTechDraw_1_1LineGroup.html#aa161197a1988c328173d1a8689f13059),
[TechDraw::ShapeExtractor::getShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#ae76c98b8a90588bf6515ac4738f5e16b),
[TechDraw::ShapeExtractor::getShapesFromObject()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4043c946e78f533e4f060cb3b87b5691),
[TechDraw::ShapeExtractor::getShapesFused()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a95849c53fc6bb91d9d44baf094dae6d3),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[TechDraw::DrawViewPart::getSourceShape()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aeb0d7bbe7418b86053f38713d4c91fa9),
[TechDraw::DrawViewPart::getSourceShapeFused()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a259e1a941c8e6a0651089bfa4111e3bd),
[Fem::FemVTKTools::importFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a06964ad44830b32163bedb9351fad2c8),
[Fem::FemVTKTools::importVTKMesh()](../../d6/d26/classFem_1_1FemVTKTools.html#ac7876551086da83400e8a950ea433b04),
[Sketcher::SketchObject::increaseBSplineDegree()](../../d9/dad/classSketcher_1_1SketchObject.html#a3daba3e80990ea7e01b8b4a9bde2217a),
[Gui::Application::initApplication()](../../d9/da8/classGui_1_1Application.html#af7364610acb272a9be0e6296b64e1d83),
[Sketcher::SketchObject::insertBSplineKnot()](../../d9/dad/classSketcher_1_1SketchObject.html#a48c6d4c74904307c87c4e8f65a9e89af),
[TechDraw::DrawProjectSplit::isOnEdge()](../../d8/ded/classTechDraw_1_1DrawProjectSplit.html#a5b512ff511e727022201f489ac54672b),
[Measure::Measurement::length()](../../d6/d84/classMeasure_1_1Measurement.html#a3f3068c7bbf6c06438658dea6f675c17),
[TechDraw::LineGroup::lineGroupFactory()](../../da/d19/classTechDraw_1_1LineGroup.html#adf6fead98b25f146b8c7470caa27d264),
[MeshCore::MeshInput::LoadNastran()](../../d9/d08/classMeshCore_1_1MeshInput.html#a33bc94cc3daf0fc3a6b9352fbf87b4e1),
[StartGui::Workbench::loadStartPage()](../../dc/d4c/classStartGui_1_1Workbench.html#a44d732f24cca88363d161155407973a6),
[TechDrawGui::QGIFace::loadSvgHatch()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#ae62a9f454f6009d4c5cc46e7c2ac0225),
[PartDesignGui::TaskSketchBasedParameters::make2DLabel()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#abe69c78ef76010267804b7bfb977e00d),
[TechDrawGui::QGITile::makeSymbol()](../../d6/d9b/classTechDrawGui_1_1QGITile.html#a5851fb4b25a7accc37d273a1c924a4b1),
[SketcherGui::makeTangentToArcOfEllipseviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#ade2d18eb05327cda22e2eb86409e4642),
[SketcherGui::makeTangentToArcOfHyperbolaviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a2d88b81b020ee6003474b180fad75a3b),
[SketcherGui::makeTangentToArcOfParabolaviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a8153db87ad16afe18f0f5e0a01bf5251),
[SketcherGui::makeTangentToEllipseviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a0221a346db6666022488335587d92562),
[Measure::Measurement::massCenter()](../../d6/d84/classMeasure_1_1Measurement.html#a1c65790f4b19fbcd61b814beaad8f4bc),
[Sketcher::SketchObject::modifyBSplineKnotMultiplicity()](../../d9/dad/classSketcher_1_1SketchObject.html#ae318b60c226c883e53725f9ebef29991),
[SketcherGui::ViewProviderSketch::mouseButtonPressed()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a265a44a9f18bd9ac103c0dd048a455e3),
[Base::Subject< _MessageType
>::Notify()](../../dd/d73/classBase_1_1Subject.html#aa5353b733daa35b204f2990b34300b28),
[Gui::GUIApplication::notify()](../../d2/da0/classGui_1_1GUIApplication.html#a386680fea5f056ea829d11f9f0476ca2),
[Sketcher::SketchObject::onChanged()](../../d9/dad/classSketcher_1_1SketchObject.html#a838e11f3f3d9b47452ece92f8057bff1),
[Gui::ViewProviderOrigin::onChanged()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
[SketcherGui::ViewProviderSketch::onDelete()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a83277547707db7a956f740a550845361),
[PartDesignGui::TaskExtrudeParameters::onDirectionCBChanged()](../../d7/d0a/classPartDesignGui_1_1TaskExtrudeParameters.html#a1d0537a96a94c5e1e440dfc25e5e81cd),
[PartGui::SectionCut::onFlipXclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a5fbc3a06b93ca2cc623e4c60b2d8b0cd),
[PartGui::SectionCut::onFlipYclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a086343100aa8f33a1f885130b13fa4ad),
[PartGui::SectionCut::onFlipZclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a56a8cd5a5ec5c2228e4d5a5f8a8c232a),
[Gui::Application::onLastWindowClosed()](../../d9/da8/classGui_1_1Application.html#ab6fa833663f9f2e51031af52fe34865b),
[PartGui::SectionCut::onRefreshCutPBclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a27de80c7c591178a8f37bef034294d8a),
[Gui::GestureNavigationStyle::onRollGesture()](../../dd/df8/classGui_1_1GestureNavigationStyle.html#aea1942b7bbfc657cbfe2ae892811b802),
[SketcherGui::DrawSketchHandlerCarbonCopy::onSelectionChanged()](../../d8/dcc/classSketcherGui_1_1DrawSketchHandlerCarbonCopy.html#a0abe4b682958afcce6e53de58d3225fa),
[SketcherGui::DrawSketchHandlerExternal::onSelectionChanged()](../../d5/d95/classSketcherGui_1_1DrawSketchHandlerExternal.html#aab1764f7bd2af3f2cf49a7131a443253),
[TechDrawGui::TaskLeaderLine::onTrackerClicked()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a581dcc144a5b4017a6356a89dda30abe),
[TechDrawGui::TaskCosVertex::onTrackerFinished()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#a70cc99622328e6c5e42c84caec735981),
[TechDrawGui::TaskLeaderLine::onTrackerFinished()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a3834c86229e7732145d671a0546087ea),
[App::Application::openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728),
[Gui::Dialog::PreferenceUiForm::PreferenceUiForm()](../../dc/d23/classGui_1_1Dialog_1_1PreferenceUiForm.html#af6a6ab0b22aaf6b544fa1642479a28b6),
[SketcherGui::DrawSketchHandlerBSpline::pressButton()](../../d7/d7f/classSketcherGui_1_1DrawSketchHandlerBSpline.html#aa7b3de965a523113d29f73f4b71fe6c8),
[MeshPartGui::Tessellation::process()](../../d7/d65/classMeshPartGui_1_1Tessellation.html#ad6b6d37618da6068570a0c38ae764aba),
[App::Application::processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa),
[SketcherGui::EditModeConstraintCoinManager::processConstraints()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a86abd481aa8756c9ea61b10d2e624804),
[App::Application::processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939),
[TechDraw::GeometryObject::projectShape()](../../dc/dbe/classTechDraw_1_1GeometryObject.html#a3ca84de7bd7a452ec16097a0a8710cac),
[TechDraw::GeometryObject::projectShapeWithPolygonAlgo()](../../dc/dbe/classTechDraw_1_1GeometryObject.html#a59091a76cdbb7a70b8e39e41eb61fa71),
[Measure::Measurement::radius()](../../d6/d84/classMeasure_1_1Measurement.html#aad95ee25271e89c1fe3618604b5a07af),
[Points::E57Reader::read()](../../d2/dfb/classPoints_1_1E57Reader.html#a7af6bb0bc50ff56c203f0cb0aa04d458),
[Base::XMLReader::readFiles()](../../dc/d95/classBase_1_1XMLReader.html#a53b94bea9a61011f67ee6f5e98e53f16),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
[Fem::FemVTKTools::readVTKMesh()](../../d6/d26/classFem_1_1FemVTKTools.html#a5c072865883df9f3a7141773d33534e6),
[App::Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
[SketcherGui::DrawSketchHandlerBSpline::registerPressedKey()](../../d7/d7f/classSketcherGui_1_1DrawSketchHandlerBSpline.html#affad87364d78df54ac588230c9fcec62),
[DrawSketchHandlerBSplineInsertKnot::releaseButton()](../../d2/df2/classDrawSketchHandlerBSplineInsertKnot.html#ad1bd5e637ff894fb66b09fcf914bd49b),
[DrawSketchHandlerCopy::releaseButton()](../../d0/d19/classDrawSketchHandlerCopy.html#ae8955bcf2ad603ca908dbde0ca52042a),
[DrawSketchHandlerRectangularArray::releaseButton()](../../db/da6/classDrawSketchHandlerRectangularArray.html#acad62cdf5d8d411d55beff22a12fac28),
[SketcherGui::DrawSketchHandlerArc::releaseButton()](../../d4/d83/classSketcherGui_1_1DrawSketchHandlerArc.html#ab283932a602b4b135259d8ec565cbe1a),
[SketcherGui::DrawSketchHandler3PointArc::releaseButton()](../../d3/d84/classSketcherGui_1_1DrawSketchHandler3PointArc.html#ad9123e0df6dfcbca72fb0a45e63bb822),
[SketcherGui::DrawSketchHandlerArcOfEllipse::releaseButton()](../../d4/d0e/classSketcherGui_1_1DrawSketchHandlerArcOfEllipse.html#ae0f1ecd2fac7f0ee7d7b57610009dc1d),
[SketcherGui::DrawSketchHandlerCircle::releaseButton()](../../db/daa/classSketcherGui_1_1DrawSketchHandlerCircle.html#aac71ee5f645be6cc4b0ac8cb49777b67),
[SketcherGui::DrawSketchHandler3PointCircle::releaseButton()](../../db/dbc/classSketcherGui_1_1DrawSketchHandler3PointCircle.html#a3393a6d51aed0b745e44e60f55e4c96a),
[SketcherGui::DrawSketchHandlerExtend::releaseButton()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#a3e947849d6dc89b7f93e87a1ebd9b160),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[SketcherGui::DrawSketchHandlerLine::releaseButton()](../../dd/d65/classSketcherGui_1_1DrawSketchHandlerLine.html#a9ee080f22c2c3bf2f6e826f4cc36f91a),
[SketcherGui::DrawSketchHandlerLineSet::releaseButton()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a040aa2a8cc28c52db550115a16ef693c),
[SketcherGui::DrawSketchHandlerPoint::releaseButton()](../../df/da1/classSketcherGui_1_1DrawSketchHandlerPoint.html#a733f6bcea854c88e77f73e0a1b377f53),
[SketcherGui::DrawSketchHandlerRegularPolygon::releaseButton()](../../db/d5f/classSketcherGui_1_1DrawSketchHandlerRegularPolygon.html#a676a473ddbfd8fd7f2e214ffc43352b5),
[SketcherGui::DrawSketchHandlerBox::releaseButton()](../../dc/d09/classSketcherGui_1_1DrawSketchHandlerBox.html#a1ee8ff08af23b1ad1d9fd48170889315),
[SketcherGui::DrawSketchHandlerOblong::releaseButton()](../../dc/dac/classSketcherGui_1_1DrawSketchHandlerOblong.html#a8e2b792d2ce80795c2808e6276bdd6dc),
[SketcherGui::DrawSketchHandlerSlot::releaseButton()](../../d5/dd5/classSketcherGui_1_1DrawSketchHandlerSlot.html#aa93e01a33ed89216e53c3c8886b21a35),
[SketcherGui::DrawSketchHandlerSplitting::releaseButton()](../../d1/d6f/classSketcherGui_1_1DrawSketchHandlerSplitting.html#a0766956ef48057437eca84c83e1b3521),
[SketcherGui::DrawSketchHandlerTrimming::releaseButton()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a19ae638451e1d23b50c23409a6eeded1),
[SketcherGui::DrawSketchHandlerArcOfHyperbola::releaseButton()](../../d0/dcd/classSketcherGui_1_1DrawSketchHandlerArcOfHyperbola.html#a691e8ff0661b5c0f36bd5ad8c8fe8fa3),
[SketcherGui::DrawSketchHandlerArcOfParabola::releaseButton()](../../d3/dd4/classSketcherGui_1_1DrawSketchHandlerArcOfParabola.html#a17a69b223beded8cad2a7319ef4cffe6),
[Base::PyException::ReportException()](../../d6/d92/classBase_1_1PyException.html#ae319a800388911635841231b22e7be61),
[Gui::View3DInventorViewer::resetEditingRoot()](../../d5/d29/classGui_1_1View3DInventorViewer.html#aab89c5619d8a9f8f32b5610f6f48662a),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[Part::PropertyGeometryList::Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[TechDraw::PropertyCenterLineList::Restore()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList::Restore()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList::Restore()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
[TechDraw::PropertyGeomFormatList::Restore()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807),
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
[Gui::Document::RestoreDocFile()](../../de/d4e/classGui_1_1Document.html#ac4b89a171b3259b15facb5b1b85b0d09),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[App::ExtensionContainer::restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab),
[Gui::ConsoleErrorTask::run()](../../dc/d6e/classGui_1_1ConsoleErrorTask.html#a990c101f71df4fc34a5ef056ff9a694c),
[Sandbox::PythonThread::run()](../../da/d9e/classSandbox_1_1PythonThread.html#a4c26a11ab7160b84ecebd4403ad406b6),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[ILoggerBlockerTest::runSingleTest()](../../d3/d59/classILoggerBlockerTest.html#aedb272178e3388617450e67220287e65),
[TechDraw::CenterLine::Save()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[App::PropertyContainer::Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482),
[Fem::PropertyPostDataObject::SaveDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a3ed0c0500e1d89813d4d6854ce5b388b),
[App::ExtensionContainer::saveExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#a8f71a6ea625198e2d2e3067f2a367df0),
[TechDraw::CenterLine::scaledGeometry()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a104bfe6bf49d7b364f65000352e670ea),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[SketcherGui::ViewProviderSketch::setEdit()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ad28c651e806a00fca15332d4c04b47c9),
[SketcherGui::ViewProviderSketch::setEditViewer()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a7ecefc8f26a51435051a12a6fb73f333),
[Gui::PropertyEditor::PropertyItem::setPropertyValue()](../../d6/db3/classGui_1_1PropertyEditor_1_1PropertyItem.html#a9e936f305d42674e1ef1f93d5ed8c539),
[Gui::ViewProviderOrigin::setTemporaryVisibility()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#abb766d6f4587e4a16c4d929200944ca1),
[Gui::Application::sExport()](../../d9/da8/classGui_1_1Application.html#ade16ea2f01b001288ff3cd962a85b8b5),
[Gui::Application::sInsert()](../../d9/da8/classGui_1_1Application.html#aca6ab0f62cf4fb268ea9a87ce3cebaf2),
[Sketcher::SketchObject::solve()](../../d9/dad/classSketcher_1_1SketchObject.html#a0bcef04719586a7122d762061b2d4ac4),
[Gui::Application::sOpen()](../../d9/da8/classGui_1_1Application.html#a3402c81d1a56dbb72d84e74047fc53e8),
[sPyError()](../../df/dca/classBase_1_1ConsoleSingleton.html#a8676363ed03277ee2403a7cd9bf18c5f),
[Gui::NetworkRetriever::startDownload()](../../d9/d5c/classGui_1_1NetworkRetriever.html#a25307bec2b9a46124b9e093bcd55d2f3),
[TechDrawGui::QGIViewSymbol::symbolToSvg()](../../d1/da0/classTechDrawGui_1_1QGIViewSymbol.html#a2cdd41686c73a5fa94290c5a437cf360),
[Base::RedirectStdError::sync()](../../d5/d74/classBase_1_1RedirectStdError.html#a26d7d25547ae7e999b3b49b221c34454),
[MeshPart::MeshingOutput::sync()](../../d1/df0/classMeshPart_1_1MeshingOutput.html#a1b817ed643f88a3dc67963ecc3c7ddcd),
[PartDesignGui::TaskBoxPrimitives::TaskBoxPrimitives()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aee4936dd78a78c4d0f6fcc168d1a9c13),
[TechDrawGui::TaskCenterLine::TaskCenterLine()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a5b942888fa00c64e72a692710da1d65f),
[TechDrawGui::TaskCosmeticLine::TaskCosmeticLine()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#adfd721ad8274cb37c3bfa38494aedc6e),
[TechDrawGui::TaskDetail::TaskDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a2017c373db55e0b43d386b536b34bc75),
[Gui::TaskView::TaskDialogPython::TaskDialogPython()](../../d1/d71/classGui_1_1TaskView_1_1TaskDialogPython.html#a604b06851bd8d38e84b7c886e183820f),
[TechDrawGui::TaskLeaderLine::TaskLeaderLine()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a873d04472b6a0de7f250ac13eef14913),
[TechDrawGui::TaskRichAnno::TaskRichAnno()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#acfd26140dce1c41560c4391c78b2fb06),
[TechDrawGui::TaskWeldingSymbol::TaskWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#aaf7cb244a051a9f8977d8ca2e0f00a17),
[TechDrawGui::QGIFace::textureFromBitmap()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#a23f23c89d9f6ec0542b941d5c588fde5),
[Gui::AutoSaver::timerEvent()](../../d6/d8b/classGui_1_1AutoSaver.html#ade136417c31f9773cfcbd7112aebf01c),
[App::PropertyPythonObject::toString()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a99e230754db8a47dfb3e59f92493db1d),
[SketcherGui::ViewProviderSketch::unsetEdit()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a292cf2c15b300787b74fa8b2bc248388),
[PartDesignGui::ViewProviderAddSub::updateAddSubShapeIndicator()](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#a27d23424ce72a0f362904d73928fbc6c),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[FemGui::ViewProviderFemConstraintBearing::updateData()](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#a3b3cf2fa05760751890d9e1cf51f178f),
[PartGui::ViewProviderCurveNet::updateData()](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#ac10fc8ddaf0e0f8b4fed8ed9f957073a),
[TechDrawGui::TaskDetail::updateDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a9531ab9a77b992bbde7893f620cddd9f),
[PartDesignGui::ViewProviderBody::updateOriginDatumSize()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3c7c680a5e55c6cc695c82c8b45935c0),
[Gui::ViewProviderOriginGroupExtension::updateOriginSize()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a254bd812cc1814ed270f1d92e445ad8e),
[Gui::OutputStderr::write()](../../d2/d07/classGui_1_1OutputStderr.html#aec95ffee0cf02a004f4275f4873f655e),
[Gui::PythonDebugStderr::write()](../../de/d00/classGui_1_1PythonDebugStderr.html#ae411e68fcb06ed94baed5cbad2492398),
[Fem::FemVTKTools::writeResult()](../../d6/d26/classFem_1_1FemVTKTools.html#afe10808623915c79b6e74786a6f6d0e3),
[Fem::FemVTKTools::writeVTKMesh()](../../d6/d26/classFem_1_1FemVTKTools.html#afd566b7765038482398e5775f8babc02),
[SketcherGui::CurveConverter::~CurveConverter()](../../d9/d49/classSketcherGui_1_1CurveConverter.html#ac4b31b0695f009bdc0e6464928d87c37),
[PartDesignGui::TaskBoxPrimitives::~TaskBoxPrimitives()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a999b4dee6e102f972f0c3b3bb1307d7e),
[PartDesignGui::TaskLinearPatternParameters::~TaskLinearPatternParameters()](../../da/d31/classPartDesignGui_1_1TaskLinearPatternParameters.html#abd8fe23f24b1d9df85617e19073b621e),
[PartDesignGui::TaskMirroredParameters::~TaskMirroredParameters()](../../d8/d3c/classPartDesignGui_1_1TaskMirroredParameters.html#a9076e03f1dd9d1c76cf8005459c68a98),
and
[PartDesignGui::TaskPolarPatternParameters::~TaskPolarPatternParameters()](../../d7/d72/classPartDesignGui_1_1TaskPolarPatternParameters.html#afb1b6200d5c009f245e1f5bb4e82e79d).

## ◆ Get()

[ILogger](../../d8/d26/classBase_1_1ILogger.html) * ConsoleSingleton::Get  | ( | const char *  | _Name_| ) |  const  
---|---|---|---|---|---  
  
References
[Base::ILogger::Name()](../../d8/d26/classBase_1_1ILogger.html#ac947ca3f680d948d3dff92fce524659c).

Referenced by
[IsMsgTypeEnabled()](../../df/dca/classBase_1_1ConsoleSingleton.html#a139867f1225d10047562f6aa964e0d22),
[Base::Builder3D::saveToLog()](../../d6/d1b/classBase_1_1Builder3D.html#a219f6a61f1f9f0216ab0b47e0efddfa6),
[SetEnabledMsgType()](../../df/dca/classBase_1_1ConsoleSingleton.html#ad7f0fab600123b5a812f364e058fde09),
[sPyGetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#ac31064289a9d46191b3fe33692bb3483),
and
[sPySetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#a38ebfd3e6dd742dd3cfc180bc03025e3).

## ◆ GetLogLevel()

[int](../../d1/da0/classint.html) * ConsoleSingleton::GetLogLevel  | ( | const char *  | _tag_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _create_ = `true`  
| ) | |   
  
References
[femsolver.elmer.equations.elasticity::create()](../../dc/de2/group__FEM.html#ga1011d50c1014de9888c82c5f0f41eed3).

## ◆ Instance()

| [ConsoleSingleton](../../df/dca/classBase_1_1ConsoleSingleton.html) & ConsoleSingleton::Instance  | ( | | ) |   
---|---|---|---|---  
static  
  
singleton

References
[ConsoleSingleton()](../../df/dca/classBase_1_1ConsoleSingleton.html#ae6ad9dd7f8d6a266394ace772e25bbaf).

Referenced by
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[sPyError()](../../df/dca/classBase_1_1ConsoleSingleton.html#a8676363ed03277ee2403a7cd9bf18c5f),
[sPyGetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#ac31064289a9d46191b3fe33692bb3483),
[sPyLog()](../../df/dca/classBase_1_1ConsoleSingleton.html#a8921316e836ee1f7c2dfc47f033c2c01),
[sPyMessage()](../../df/dca/classBase_1_1ConsoleSingleton.html#a2e67159961c8ac1b21ba4d528acdc37f),
[sPySetStatus()](../../df/dca/classBase_1_1ConsoleSingleton.html#a38ebfd3e6dd742dd3cfc180bc03025e3),
and
[sPyWarning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a7d356c1cafd385001e50cde27c18d58f).

## ◆ IsMsgTypeEnabled()

[bool](../../d9/db9/classbool.html) ConsoleSingleton::IsMsgTypeEnabled  | ( | const char *  | _sObs_ ,   
---|---|---|---  
|  | [FreeCAD_ConsoleMsgType](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399d) | _type_  
| ) | |  const  
  
Enables or disables message types of a certain console observer.

References
[Base::ILogger::bErr](../../d8/d26/classBase_1_1ILogger.html#a4a39644f9509a9d4bff1d201c3878748),
[Base::ILogger::bLog](../../d8/d26/classBase_1_1ILogger.html#a8753678619bcabcddc21d0da955ecdce),
[Base::ILogger::bMsg](../../d8/d26/classBase_1_1ILogger.html#aca879668d459839a2bd65524cf38fbf6),
[Base::ILogger::bWrn](../../d8/d26/classBase_1_1ILogger.html#a4eb0f75d0a65ffad264bd0bb610f026a),
[Get()](../../df/dca/classBase_1_1ConsoleSingleton.html#ae4ca9fea6787c5acd17c66dbfbbe374b),
[MsgType_Err](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da9adf564b5bca3813e28e053f8d208731),
[MsgType_Log](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da4c8d83da40448a24fd37469122037dfb),
[MsgType_Txt](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dae3438ada440361f8f7bfe29451754b99),
and
[MsgType_Wrn](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dadf5163026958f3c10c1c064c405b3e95).

## ◆ Log()

| void ConsoleSingleton::Log  | ( | const char *  | _pMsg_ ,   
---|---|---|---  
|  |  | _..._  
| ) | |   
virtual  
  
Prints a log Message.

Prints a Message This method is appropriate for development and tracking
purposes.

It can be used to track execution of algorithms and functions. The normal user
doesn't need to see it, it's more for developers and experienced users. So in
normal user mode the logging is switched off.

    You can use a printf-like interface for example: 

[Console](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729
"Access to the Console This method is used to gain access to the one and only
instance of the
ConsoleS...")().[Log](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964
"Prints a log Message.")("Execute part %d in algorithm
%s\n",i,[str](../../d9/d36/classstr.html));

See also

    [Message](../../df/dca/classBase_1_1ConsoleSingleton.html#a322664077d1c391e11e07ec903c99e25 "Prints a Message.")
     [Warning](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326 "Prints a warning Message.")
     [Error](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644 "Prints a error Message.")

References
[Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964).

Referenced by
[Gui::Application::activateWorkbench()](../../d9/da8/classGui_1_1Application.html#ac3b3b8a91ba204c6180dab0dccc1a6d8),
[TechDraw::GeometryObject::addGeomFromCompound()](../../dc/dbe/classTechDraw_1_1GeometryObject.html#ac8836a681ac0143814d46ef62bf34986),
[TechDraw::DrawProjGroup::addProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acfc4e756c8714973996318393180f483),
[TechDraw::DrawProjGroup::arrangeViewPointers()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a8a8bdca0831ea0e16e664ad17f0a04f8),
[TechDraw::BSpline::asCircle()](../../d6/d09/classTechDraw_1_1BSpline.html#a2c628716c3a1e784abbe9f399786386f),
[TechDrawGui::ViewProviderPage::attach()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ac4ba78ec2544fc891ed71efbfef08160),
[TechDrawGui::MDIViewPage::attachView()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#abe1a2c160e4954c76faa254383387772),
[Sketcher::SketchAnalysis::autoconstraint()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a593a8426260651db5e7a7fc942b9a647),
[Gui::NS::AwaitingMoveState::AwaitingMoveState()](../../d2/d54/classGui_1_1NS_1_1AwaitingMoveState.html#a61493dec20c2ae2a95a4fd6424ac9dac),
[Gui::NS::AwaitingReleaseState::AwaitingReleaseState()](../../db/dcd/classGui_1_1NS_1_1AwaitingReleaseState.html#aef8a7d8230d239b937bd7943231e938b),
[TechDraw::BezierSegment::BezierSegment()](../../d1/db7/classTechDraw_1_1BezierSegment.html#a27e9eea9be1080915116009ca0fc324c),
[TechDraw::BSpline::BSpline()](../../d6/d09/classTechDraw_1_1BSpline.html#ab0d19db0c31b1dd84f5bdefcb2303443),
[TechDraw::DrawViewPart::buildGeometryObject()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a859efd3dcccfd849656ff8b436ce6d58),
[TechDraw::GeometryObject::calcBoundingBox()](../../dc/dbe/classTechDraw_1_1GeometryObject.html#a219f8cf7cc4846f8ffcfbb04d2db5e38),
[TechDraw::DrawProjGroup::calculateAutomaticScale()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#af5bbe9c992fa0e9fc83461af6931f0e0),
[Gui::MacroManager::cancel()](../../d8/dc6/classGui_1_1MacroManager.html#aa94b76ce0fb62a7ef10c5ba80f6a1dd2),
[Gui::ViewProvider::canDropObject()](../../d3/db3/classGui_1_1ViewProvider.html#a4e729f5e7bcfadb98dcf324cf1f4e78f),
[TechDraw::GeometryUtils::chainGeoms()](../../d5/d83/classTechDraw_1_1GeometryUtils.html#af7233d8da286a9af5c37b400eb85aa39),
[Sketcher::SketchObject::changeConstraintsLocking()](../../d9/dad/classSketcher_1_1SketchObject.html#ac693bddc46ae81ee5490ebe387604b50),
[PartDesignGui::TaskHoleParameters::changedObject()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#af6c0941c01c80d87e2f97344958003be),
[TechDraw::DrawViewDimension::checkReferences2D()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a6b3599cd70d672c8aa6e16e304bbb1a4),
[TechDraw::DrawViewPart::checkXDirection()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a602f73fc08211bfc4edfa1382bc0ee64),
[Gui::MacroManager::commit()](../../d8/dc6/classGui_1_1MacroManager.html#a083bd160df4ba3fc4e313cb6c9870cb1),
[App::PropertyFileIncluded::Copy()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a8357945cf4e3e84abd535ef6d53d4f99),
[TechDrawGui::Grabber3d::copyActiveViewToSvgFile()](../../d7/d83/classTechDrawGui_1_1Grabber3d.html#a44f769bea9d4e116b3667e59bec4e6da),
[TechDrawGui::TaskCenterLine::createCenterLine()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a9fb5dd30626ee43ec4671c9ea2ce150b),
[Mesh::GTSAlgos::createGTSSurface()](../../dc/dd3/classMesh_1_1GTSAlgos.html#a4319ac819440da9984a5239f9f3cdaaa),
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[Gui::WidgetFactoryInst::createPreferencePage()](../../d5/d83/classGui_1_1WidgetFactoryInst.html#a3cc9e4ee3575cfdf3398d3b7150190a4),
[Gui::WidgetFactoryInst::createWidget()](../../d5/d83/classGui_1_1WidgetFactoryInst.html#a8a166efde23cd16fb19b84de63abf3b3),
[Gui::Dialog::ButtonModel::data()](../../d4/d68/classGui_1_1Dialog_1_1ButtonModel.html#afb6a6209b558bf89fb41f2f36b2e42ce),
[App::Application::destruct()](../../da/dbf/classApp_1_1Application.html#a2429ab2a8f4255a5ce2d970aa74ba7f3),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[GCS::System::diagnose()](../../db/d28/classGCS_1_1System.html#ae239feb89ff7b144d842d954d5fbcf74),
[App::Document::Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[MeshGui::ViewProviderMeshTransformDemolding::DragEndCallback()](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#ae5c7b3bbeaf7c8fbaa789333824cd762),
[TechDrawGui::QGIViewDimension::draw()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a5a804977a329425219739213bc82ec70),
[TechDrawGui::QGIViewBalloon::drawBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6d26eb06a692339e02c1b57545903f29),
[SketcherGui::ViewProviderSketch::editDoubleClicked()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#abdbeadcb7528aec366231ca51b1ffb46),
[Gui::ViewerEventFilter::eventFilter()](../../dc/d1d/classGui_1_1ViewerEventFilter.html#a03c5db053bf086d38650e7ffa2325bf6),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Fem::FemMeshShapeNetgenObject::execute()](../../d9/df4/classFem_1_1FemMeshShapeNetgenObject.html#ad38e08d369e0a9c44588e98bc5ffb3ed),
[Import::FeatureImportIges::Execute()](../../d7/dac/classImport_1_1FeatureImportIges.html#a458fb556aa3581534c7a713c960ded7b),
[Import::FeatureImportStep::Execute()](../../da/dde/classImport_1_1FeatureImportStep.html#a42d170d40ce67819f931b5894145d229),
[Part::CurveNet::execute()](../../d9/d41/classPart_1_1CurveNet.html#ab3d3703fdaab33d94b764c62d6739ce6),
[Part::ImportBrep::execute()](../../d8/d3e/classPart_1_1ImportBrep.html#a3fbd619fb350dff418fffd6b6f185ca7),
[Part::ImportIges::execute()](../../d2/d1d/classPart_1_1ImportIges.html#a1d947e212fdeb8ed2b8bb8ef3fae1041),
[Part::ImportStep::execute()](../../d4/de2/classPart_1_1ImportStep.html#a3c81f94deddd927756144ef4e8040678),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDraw::DrawViewMulti::execute()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a9d04a96ccac9fad6d125e478b91b7f30),
[TechDraw::DrawViewSymbol::execute()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a44eea88d3e8522c41e9dcee9acff10ce),
[Fem::exportFemMeshCells()](../../dd/d72/namespaceFem.html#a1404eba0333226c8033236fd955af7fd),
[Fem::exportFemMeshFaces()](../../dd/d72/namespaceFem.html#a0980b3ab420f026fdcd6eaf30c742c12),
[Fem::FemVTKTools::exportFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a37e8a3dd86851c4ce056f3cfa7ad0d89),
[Fem::FemVTKTools::exportVTKMesh()](../../d6/d26/classFem_1_1FemVTKTools.html#a0c455d00a2e141a7ec067b55dbfd8488),
[Gui::ViewProviderGroupExtension::extensionCanDropObject()](../../d2/d69/classGui_1_1ViewProviderGroupExtension.html#a147fbe325cf8c816be9cdcaca1c5247a),
[TechDraw::DrawGeomHatch::extractFace()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#ab159db77de5ced0a636b87c86e150a2d),
[TechDraw::DrawViewPart::extractFaces()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aaaaf9f3bc41bcad927258ed1fdb53baa),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[MeshCore::MeshAlgorithm::FillupHole()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a17f6cba79cffddde89c7f20db33fe652),
[MeshCore::MeshTopoAlgorithm::FillupHoles()](../../d6/d22/classMeshCore_1_1MeshTopoAlgorithm.html#a111d0e86a9482ba269f402955087c3e5),
[MeshCore::CylinderFit::Fit()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a2b728f7c295c98d85f6159610ff36bc4),
[MeshGui::SoFCMeshFaceSet::generatePrimitives()](../../d2/d7f/classMeshGui_1_1SoFCMeshFaceSet.html#af820796c2a30bb9699784a235f724ca0),
[MeshGui::SoFCMeshObjectShape::generatePrimitives()](../../d6/d4f/classMeshGui_1_1SoFCMeshObjectShape.html#ae65792d4d027d0c074e0951106c0e2e7),
[MeshGui::SoFCMeshSegmentShape::generatePrimitives()](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#a81e11061b42c3ccebccdbca75cadc9eb),
[Gui::NS::GestureState::GestureState()](../../db/d04/classGui_1_1NS_1_1GestureState.html#ad0ae304b135bd8fe413df565c4448087),
[TechDrawGui::DrawGuiUtil::get3DDirAndRot()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a6c011651124bc645ff71d71e7bd64f4d),
[TechDraw::DrawProjGroup::getAnchorDirection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a6b386f82419d9dff8f039eb92b53cd31),
[TechDraw::DrawLeaderLine::getBaseScale()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#acab08d27991c64b4f4d19d097d8e7c26),
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686),
[TechDraw::BSpline::getCircleParms()](../../d6/d09/classTechDraw_1_1BSpline.html#aaa7798e96fb7f0f2ec6232da70fc5df4),
[TechDrawGui::QGIView::getClipGroup()](../../d1/d99/classTechDrawGui_1_1QGIView.html#ae0acde24df99154dc292772e5c5fb814),
[TechDraw::DrawViewSection::getCSFromBase()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a761c0e9c4fe742ad0f6250428875ecd4),
[TechDraw::DrawProjectSplit::getEdges()](../../d8/ded/classTechDraw_1_1DrawProjectSplit.html#ac943560b70b1fa2e0a7f1a80fa976f2b),
[TechDraw::DrawSVGTemplate::getEditableTextsFromTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a5d4fd489066be062afb816f45960c214),
[TechDraw::DrawViewPart::getFaceEdgesByIndex()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ab95aa0f6d3cb7b61a0901132ae9649a1),
[TechDraw::DrawGeomHatch::getFaceOverlay()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a64b931ea5f365c039b0e956a46877f9b),
[TechDraw::DrawViewPart::getGeomByIndex()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ad2f71e34041972633b09f71320c55d11),
[TechDraw::DrawUtil::getIndexFromName()](../../da/d23/classTechDraw_1_1DrawUtil.html#aacfde195e06313dd3d9959f1e2dc2259),
[TechDrawGui::ViewProviderPage::getMDIViewPage()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#aee8569c22c8425e28f2888491a3710ef),
[Fem::FemMesh::getNodesBySolid()](../../d3/d2e/classFem_1_1FemMesh.html#a287b45f44f6d612bd439bfc6506e2f92),
[TechDrawGui::Grabber3d::getPaperScale()](../../d7/d83/classTechDrawGui_1_1Grabber3d.html#a9c088deb2adaa18fb00920beab8b9d3b),
[TechDraw::LineSet::getPatternStartPoint()](../../d7/d2f/classTechDraw_1_1LineSet.html#aba20266c9fd3898beef7917120751246),
[TechDrawGui::DrawGuiUtil::getProjDirFromFace()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a1e16c708a7e2a33bd36999a5f02ae63b),
[TechDraw::DrawProjGroup::getProjItem()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a717b725aa8d44d5699087bc1401e26e1),
[TechDraw::DrawProjGroup::getProjObj()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a20beaf391d87e04ad8b2cd1db7c78b6d),
[TechDraw::DrawViewPart::getProjVertexByCosTag()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ae453c5d7378424c6891926ee450ace85),
[TechDraw::DrawViewPart::getProjVertexByIndex()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a62d675755684647d29d1c339e07586c7),
[TechDraw::DrawView::getScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#afc22d0aa3cc132a6c14323a50082ab1e),
[TechDraw::DrawLeaderLine::getScale()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a5df9ab095a761eaef57045a431cbb972),
[TechDraw::DrawProjGroupItem::getScale()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a8f2e3744991fded06c52c4e817aed862),
[TechDraw::DrawViewSection::getSectionCS()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aefc378d8464959b191ac4ff96f6bca12),
[TechDraw::ShapeExtractor::getShapesFromObject()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4043c946e78f533e4f060cb3b87b5691),
[TechDraw::PATLineSpec::getSpecsForPattern()](../../d0/d63/classTechDraw_1_1PATLineSpec.html#ab2bfa1a86102af85a7e7f42c8625718b),
[TechDraw::DrawGeomHatch::getTrimmedLines()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9282d24bc775c7b8870bcbda7dce8cff),
[TechDraw::DrawPage::handleChangedPropertyType()](../../d9/d5a/classTechDraw_1_1DrawPage.html#adde1799122996153278b2c68d4fa9b80),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[PartGui::ViewProviderCurveNet::handleEvent()](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#a25e02102632cd852c5932d2326dbb946),
[TechDraw::DrawProjGroup::hasProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a90a7b1897caccb65feab45425c10448d),
[Gui::NS::IdleState::IdleState()](../../da/dcb/classGui_1_1NS_1_1IdleState.html#a0a527518f11a54eed44c3f29ae3a876d),
[Fem::FemVTKTools::importFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a06964ad44830b32163bedb9351fad2c8),
[Base::Type::importModule()](../../dc/dee/classBase_1_1Type.html#a7e5b01ed0f09e28b038003caa13c3830),
[Part::ImportStepParts()](../../d2/db9/namespacePart.html#a4da179b4c198cc0c74884eb8693d1619),
[Fem::FemVTKTools::importVTKMesh()](../../d6/d26/classFem_1_1FemVTKTools.html#ac7876551086da83400e8a950ea433b04),
[Gui::GuiNativeEvent::initSpaceball()](../../d6/d61/classGui_1_1GuiNativeEvent.html#aaca1647ae76006a032ef62f5eb99f858),
[Gui::NS::InteractState::InteractState()](../../dc/dd6/classGui_1_1NS_1_1InteractState.html#ac098ce63ce38175c1b54736ff1141367),
[Gui::Command::invoke()](../../d2/dff/classGui_1_1Command.html#ae87c26eb21dcefae55ffa59d07280bd8),
[TechDraw::DrawUtil::isCrazy()](../../da/d23/classTechDraw_1_1DrawUtil.html#ae600fe4a2fc97d4c5a1729597b606061),
[Fem::FemPostPipeline::load()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a6b8a523a3afbb19474bf90fa955f1a41),
[Mesh::MeshObject::load()](../../d8/dcc/classMesh_1_1MeshObject.html#a0a08f40f39b5c78345146ac8b8f639f9),
[Gui::NS::Event::log()](../../dd/d93/classGui_1_1NS_1_1Event.html#a083f1be82cc0aa3a29187da8d7880450),
[Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964),
[GCS::SolverReportingManager::LogToConsole()](../../d7/d2a/classGCS_1_1SolverReportingManager.html#ae9062222c2d3e8efa384e50f5cd74fc1),
[MeshPart::CurveProjectorWithToolMesh::makeToolMesh()](../../d8/dd2/classMeshPart_1_1CurveProjectorWithToolMesh.html#aa0428e1cea062658a882b2b5e3b9e05b),
[TechDraw::mirrorShape()](../../d7/d31/namespaceTechDraw.html#a3c2b4ce53834bd402747846125bdcab1),
[TechDrawGui::QGIPrimPath::mousePressEvent()](../../dd/dc6/classTechDrawGui_1_1QGIPrimPath.html#a11b1a03671da6bae73b74186537fc912),
[TechDraw::moveShape()](../../d7/d31/namespaceTechDraw.html#a6984b4017e3ad0b59304844e743f064a),
[Gui::GUIApplication::notify()](../../d2/da0/classGui_1_1GUIApplication.html#a386680fea5f056ea829d11f9f0476ca2),
[Gui::WindowParameter::OnChange()](../../d4/dcc/classGui_1_1WindowParameter.html#aac6d670422bcdc8a1b5df57e994f7c9d),
[TechDraw::DrawProjGroup::onChanged()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[TechDraw::DrawViewSymbol::onChanged()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#adb3364984aac5da2ff804a43845ceee4),
[Gui::Document::onRelabel()](../../de/d4e/classGui_1_1Document.html#a66200958cbf0c0bd2376d9f126b33076),
[Gui::GestureNavigationStyle::onRollGesture()](../../dd/df8/classGui_1_1GestureNavigationStyle.html#aea1942b7bbfc657cbfe2ae892811b802),
[TechDrawGui::MDIViewPage::onSelectionChanged()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a41cff4fd37a6ddb55d5c40e9c044a9f0),
[Gui::GestureNavigationStyle::onSetRotationCenter()](../../dd/df8/classGui_1_1GestureNavigationStyle.html#a13442f4bd3bfd715c0ab7a08d64fd631),
[Gui::Document::onUpdate()](../../de/d4e/classGui_1_1Document.html#a2d0eaab94bbc61718f58e0a976ebd221),
[Gui::View3DInventor::onUpdate()](../../da/d75/classGui_1_1View3DInventor.html#a290eb11e914417b45fe6fb8cba58b31a),
[Gui::MacroManager::open()](../../d8/dc6/classGui_1_1MacroManager.html#ac24fb255e7defcfe365ec4e1ef83f5ba),
[Gui::NS::PanState::PanState()](../../da/d14/classGui_1_1NS_1_1PanState.html#a6972d9de5a35e86d4779a772c97070c6),
[TechDraw::DrawViewPart::partExec()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#acd86eaca34db64b94858f1baeb1e227f),
[TechDraw::EdgeWalker::perform()](../../d0/d49/classTechDraw_1_1EdgeWalker.html#ab8b30e7077326603844029c537a7ece2),
[Sketcher::SketchObject::port_reversedExternalArcs()](../../d9/dad/classSketcher_1_1SketchObject.html#a7a63cf359bdc3559fb9911559f4d1cd7),
[Gui::GestureNavigationStyle::EventQueue::post()](../../d2/d2e/classGui_1_1GestureNavigationStyle_1_1EventQueue.html#a4eb05be57389f66f1549db48e4e428af),
[App::Application::processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939),
[Gui::MayaGestureNavigationStyle::processSoEvent()](../../db/da6/classGui_1_1MayaGestureNavigationStyle.html#a2043be02699a03e62277c18b68dcc834),
[TechDraw::DrawSVGTemplate::processTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a9b2032d4f9db58231ae4ad79ca5b3778),
[MeshPart::CurveProjectorSimple::projectCurve()](../../db/d5f/classMeshPart_1_1CurveProjectorSimple.html#a5932b3a0d0a1ee7119cc7f7b5f180ef8),
[MeshPart::CurveProjectorShape::projectCurve()](../../dc/d83/classMeshPart_1_1CurveProjectorShape.html#a78cb49a17db5b6adcb772e9589d32580),
[MeshPart::MeshProjection::projectEdgeToEdge()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#a322496a26bba88d2ff370beef12fdc3b),
[TechDraw::GeometryObject::projectShape()](../../dc/dbe/classTechDraw_1_1GeometryObject.html#a3ca84de7bd7a452ec16097a0a8710cac),
[TechDraw::GeometryObject::projectShapeWithPolygonAlgo()](../../dc/dbe/classTechDraw_1_1GeometryObject.html#a59091a76cdbb7a70b8e39e41eb61fa71),
[TechDraw::DrawProjGroup::purgeProjections()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a59234a939935212324d52d31af4c479b),
[Base::PyObjectBase::PyObjectBase()](../../d0/d61/classBase_1_1PyObjectBase.html#a5c865a0d688a88082e358afa12c55dd0),
[TestJtReader::read()](../../de/d52/classTestJtReader.html#a274b3a2e0ef81f151a40792f2060f752),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
[Fem::FemVTKTools::readVTKMesh()](../../d6/d26/classFem_1_1FemVTKTools.html#a5c072865883df9f3a7141773d33534e6),
[TechDrawGui::TaskProjGroup::reject()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a3a27ff7496637f0d772d15140a8ab238),
[TechDrawGui::TaskLeaderLine::removeFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a3966869ef8faf23d5293b16f335de34c),
[TechDrawGui::TaskRichAnno::removeFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a8fbd082bee0ba6db50f0a83a504f2b0b),
[TechDraw::DrawProjGroup::removeProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a23d2d0cb8a3447cdb912202f46f27aae),
[TechDraw::rotateShape()](../../d7/d31/namespaceTechDraw.html#a53da8c17c6c0c661efabb7de1a0d9083),
[Gui::NS::RotateState::RotateState()](../../da/d94/classGui_1_1NS_1_1RotateState.html#a8cd978c4f40d00ac626a2d0a3317dce8),
[Gui::ConsoleLogTask::run()](../../de/dad/classGui_1_1ConsoleLogTask.html#ade7e6c6542a8d62ee49c0b372b97d37b),
[App::Application::runApplication()](../../da/dbf/classApp_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[ILoggerBlockerTest::runSingleTest()](../../d3/d59/classILoggerBlockerTest.html#aedb272178e3388617450e67220287e65),
[Gui::AutoSaver::saveDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a6820c336cb0be4164736f27729fed059),
[TechDraw::scaleShape()](../../d7/d31/namespaceTechDraw.html#ae76416fd2251642cf47fd9332632b3d3),
[TechDrawGui::TaskProjGroup::scaleTypeChanged()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#ae8aa2696c9c438de8e953eee7ada9b9c),
[TechDrawGui::TaskSectionView::scaleTypeChanged()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#aafc15acce6a04dd460d5c2f2877e7ca9),
[Gui::Application::setActiveDocument()](../../d9/da8/classGui_1_1Application.html#a689d6d547879b12ded7364fa0fb7953c),
[TechDrawGui::QGTracker::setCircleFromPoints()](../../da/d66/classTechDrawGui_1_1QGTracker.html#a66918ab97218bd72952f1caf258a998e),
[Gui::Translator::setLocale()](../../de/db4/classGui_1_1Translator.html#a7702529e14af524d33a2cc056b4747ee),
[TechDrawGui::QGTracker::setPathFromPoints()](../../da/d66/classTechDrawGui_1_1QGTracker.html#a729c7b2288b0a8f086e61b18f180db46),
[TechDrawGui::QGTracker::setSquareFromPoints()](../../da/d66/classTechDrawGui_1_1QGTracker.html#aaec5a89097f2f1247d5d881c3f6c3f0e),
[Sketcher::Sketch::setUpSketch()](../../d9/d9b/classSketcher_1_1Sketch.html#aecd77c1e32780817ae5b1f15036993d2),
[Gui::Application::slotDeleteDocument()](../../d9/da8/classGui_1_1Application.html#a71271061511f12b53a3fb590f62b427f),
[Sketcher::Sketch::solve()](../../d9/d9b/classSketcher_1_1Sketch.html#a1c59ce1dfdd62862e4ef98fe0aad50d5),
[TechDraw::EdgeWalker::sortStrip()](../../d0/d49/classTechDraw_1_1EdgeWalker.html#a512121c43602d703acbcf732fd35bf65),
[sPyLog()](../../df/dca/classBase_1_1ConsoleSingleton.html#a8921316e836ee1f7c2dfc47f033c2c01),
[FcLodHandler::startLod()](../../d1/df3/classFcLodHandler.html#a9ef771199d2eb9619cc1f847a88144d9),
[Gui::GUISingleApplication::Private::startServer()](../../de/d95/classGUISingleApplication_1_1Private.html#ad33dc4616092d90874986bc68ca3acde),
[Gui::NS::StickyPanState::StickyPanState()](../../d7/df4/classGui_1_1NS_1_1StickyPanState.html#aacfd4f1df7dcc9ba2b1fef201ef93a4f),
[Base::RedirectStdOutput::sync()](../../d5/dbd/classBase_1_1RedirectStdOutput.html#a3713e2b63aa69c65adad42d97fbd2dc1),
[Base::RedirectStdLog::sync()](../../d0/d28/classBase_1_1RedirectStdLog.html#a8ccc07e73f68d21208717716cffde21c),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[FemGui::TaskPostDisplay::TaskPostDisplay()](../../d8/d53/classFemGui_1_1TaskPostDisplay.html#a0029720836a0bcab92cedaa9366165e5),
[FemGui::TaskPostScalarClip::TaskPostScalarClip()](../../df/d2a/classFemGui_1_1TaskPostScalarClip.html#ab3c128515f1c8b3ab10aef3edd773832),
[FemGui::TaskPostWarpVector::TaskPostWarpVector()](../../d9/dc4/classFemGui_1_1TaskPostWarpVector.html#a63fe1a9b92a9a794810bc9d8a020df54),
[Gui::NS::TiltState::TiltState()](../../d9/dfb/classGui_1_1NS_1_1TiltState.html#a91556b0b6e279c880bebacef13c3b0b1),
[SpaceNavigatorDevice::translateEvent()](../../dc/dae/classSpaceNavigatorDevice.html#aaddfad819897364d8fe38fa4ec69bb9f),
[MeshCore::AbstractPolygonTriangulator::TriangulatePolygon()](../../d9/d6e/classMeshCore_1_1AbstractPolygonTriangulator.html#a88e14056e94795467011f6fb90c1a30d),
[Sketcher::SketchObject::trim()](../../d9/dad/classSketcher_1_1SketchObject.html#a55c244742ef90c7bc339e6c0285e2027),
[TechDraw::DrawPage::unsetupObject()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ad65529c32a2d36f88a87e6734f093fcf),
[TechDraw::DrawProjGroup::updateChildrenEnforce()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a53d6b329649586210ae8e5f6eb6e6a2c),
[TechDraw::DrawProjGroup::updateChildrenLock()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aa9ea74d38f2710c6690b5a69879ae23b),
[TechDraw::DrawProjGroup::updateChildrenScale()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a34817922d5abecc72163f2b968e3a627),
[TechDraw::DrawProjGroup::updateChildrenSource()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5765aa3026040998e1c20dd4b71123f4),
[TechDrawGui::MDIViewPage::updateTemplate()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5dad0574c1df0a7c6398e90173300461),
[TechDrawGui::QGIRichAnno::updateView()](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#aee328b85a25c94184b846f491aa87d6a),
[TechDraw::DrawProjGroup::updateViews()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a080b64dfe4a1d4456558102c2c8def62),
[PartGui::ViewProviderPartExt::updateVisual()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a96cb6b96c8dfb082a135a31c4f554167),
[Gui::Application::viewActivated()](../../d9/da8/classGui_1_1Application.html#a5751289bd7e2bb88975f2390e343acd9),
[TechDraw::Wire::Wire()](../../d8/db4/classTechDraw_1_1Wire.html#a14864c362a0cd8fc129c9c67915b7f9f),
[Fem::FemMesh::write()](../../d3/d2e/classFem_1_1FemMesh.html#aae76fd7da094c3497f08daafa044afc0),
[Fem::FemVTKTools::writeResult()](../../d6/d26/classFem_1_1FemVTKTools.html#afe10808623915c79b6e74786a6f6d0e3),
[Raytracing::LuxTools::writeShape()](../../df/d50/classRaytracing_1_1LuxTools.html#ae5e2c25c3216bd520322b92ff59b4024),
[Raytracing::PovTools::writeShape()](../../d8/dea/classRaytracing_1_1PovTools.html#ad4d1b78b49ac76c10b29747c29074469),
[Raytracing::PovTools::writeShapeCSV()](../../d8/dea/classRaytracing_1_1PovTools.html#ae8dda49406724df95d7687d57c3a2ebc),
[Fem::FemVTKTools::writeVTKMesh()](../../d6/d26/classFem_1_1FemVTKTools.html#afd566b7765038482398e5775f8babc02),
[Fem::FemMesh::writeZ88()](../../d3/d2e/classFem_1_1FemMesh.html#a3376bdded6a403a170b8800558390fe1),
[Gui::Application::~Application()](../../d9/da8/classGui_1_1Application.html#a748bca84fefb9c12661cfaa2f623748d),
[App::Document::~Document()](../../d8/d3e/classApp_1_1Document.html#ac2e3f62307dc22baac21ddc10fa1609c),
[TechDraw::DrawTemplate::~DrawTemplate()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a82b33cc1ffccea85d73e5237759ce355),
[Gui::GuiNativeEvent::~GuiNativeEvent()](../../d6/d61/classGui_1_1GuiNativeEvent.html#ac1ef114bcc5330aabfbeb794aaf5d4cd),
and
[Base::PyObjectBase::~PyObjectBase()](../../d0/d61/classBase_1_1PyObjectBase.html#aa1693883212cb6724dbb2ed587bf8057).

## ◆ LogLevel()

[int](../../d1/da0/classint.html) Base::ConsoleSingleton::LogLevel  | ( | [int](../../d1/da0/classint.html) | _level_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[Base::LogLevel::level()](../../d8/d7a/classBase_1_1LogLevel.html#a6ccb16622078cef5ac6af025f55923a3).

## ◆ Message()

| void ConsoleSingleton::Message  | ( | const char *  | _pMsg_ ,   
---|---|---|---  
|  |  | _..._  
| ) | |   
virtual  
  
Prints a Message.

Prints a Message This method issues a Message.

Messages are used to show some non vital information. That means when FreeCAD
is running in GUI mode a Message appears on the status bar. In console mode a
message is printed to the console.

    You can use a printf like interface like: 

[Console](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729
"Access to the Console This method is used to gain access to the one and only
instance of the
ConsoleS...")().[Message](../../df/dca/classBase_1_1ConsoleSingleton.html#a322664077d1c391e11e07ec903c99e25
"Prints a Message.")("Doing something important %d times\n",i);

See also

    [Warning](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326 "Prints a warning Message.")
     [Error](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644 "Prints a error Message.")
     [Log](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964 "Prints a log Message.")

References
[Message()](../../df/dca/classBase_1_1ConsoleSingleton.html#a322664077d1c391e11e07ec903c99e25).

Referenced by
[StdCmdViewIvIssueCamPos::activated()](../../d9/d9e/classStdCmdViewIvIssueCamPos.html#a5e0f6316f8f26768e48b04ce9830224e),
[CmdSandboxEventLoop::activated()](../../dd/ddb/classCmdSandboxEventLoop.html#a1855363f3c57092086db6e6711015e01),
[TechDraw::DrawViewPart::add1CEToGE()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a171dc319489465651146e2e1bdc95f96),
[TechDraw::DrawViewPart::add1CLToGE()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a44c38c7b85158f4ba9742f933e29406a),
[TechDraw::DrawViewPart::add1CVToGV()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a7b7b03f642c8f94b1d25cab033aeba2c),
[TechDraw::GeometryObject::addCosmeticVertex()](../../dc/dbe/classTechDraw_1_1GeometryObject.html#a7edfe3afd46e8104ef52e508714b1845),
[TechDraw::DrawUtil::angleWithX()](../../da/d23/classTechDraw_1_1DrawUtil.html#afa770b85407535a96f2102f4f4962a7a),
[Gui::PreferencePack::apply()](../../d3/d54/classGui_1_1PreferencePack.html#ad5cbfc85d280322a52250e42b0dfbcf2),
[TechDrawGui::TaskSectionView::applyAligned()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#ac30a398dbb4e604970e911ceb26f01a3),
[TechDraw::BaseGeom::baseFactory()](../../db/d3c/classTechDraw_1_1BaseGeom.html#a35837d9934e075eacd49f551155140ce),
[PartGui::TaskMeasureLinear::buildDimension()](../../d7/ddf/classPartGui_1_1TaskMeasureLinear.html#ad770594bd530db44c7225b6995865174),
[PartGui::TaskMeasureAngular::buildDimension()](../../d7/dea/classPartGui_1_1TaskMeasureAngular.html#a6415acf0b23c450508d55d94363508e7),
[TechDraw::CenterLine::calcEndPoints()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a34df15a8a959516ecc49512c3ec5a73c),
[TechDraw::CenterLine::calcEndPoints2Lines()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a54d1cc5e3f8aa8923c2c28bdbe25c262),
[TechDrawGui::TaskRichAnno::calcTextStartPos()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ae1abe86bd3bc257ecd36cc0212763a37),
[TechDraw::DrawUtil::copyFile()](../../da/d23/classTechDraw_1_1DrawUtil.html#ae9807e29f390c2fe10bad030edb01a37),
[TechDraw::DrawUtil::countEdges()](../../da/d23/classTechDraw_1_1DrawUtil.html#ad75079f690ff4373024772b48d817ce6),
[TechDraw::DrawUtil::countFaces()](../../da/d23/classTechDraw_1_1DrawUtil.html#ab4e320fe6e6486271b6cbf1400981803),
[TechDraw::DrawUtil::countWires()](../../da/d23/classTechDraw_1_1DrawUtil.html#ae841e4dcb012eb169787cc97194f495b),
[TechDrawGui::QGISVGTemplate::createClickHandles()](../../d4/d36/classTechDrawGui_1_1QGISVGTemplate.html#a2bcf2fb5e0c80557b727afaaadbb2777),
[Fem::createObjectByType()](../../dd/d72/namespaceFem.html#af3663ac69e66763d50fbbd579cb9024a),
[MeshGui::ViewProviderMeshCurvature::curvatureInfoCallback()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd81924b9ccb33db4d9fb1fe49f1f934),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[TechDrawGui::QGIWeldSymbol::drawTile()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a95de553829cc9844a9e95b1bdbd36e76),
[TechDrawGui::QGIViewPart::drawViewPart()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#add7c40ff3fc3fcc84308bb29225f8cc9),
[TechDraw::LineFormat::dump()](../../d6/d5f/classTechDraw_1_1LineFormat.html#a8482d9313fbd9fd37dc3165283e41a71),
[TechDraw::CosmeticVertex::dump()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a8b193d5dcb4d2a81d9c46bbfec5838a2),
[TechDraw::CosmeticEdge::dump()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#aa192bc360969b17112b4d69226d26205),
[TechDraw::CenterLine::dump()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a9587a0e152229866e302451ae80aac7f),
[TechDraw::DashSpec::dump()](../../d4/da2/classTechDraw_1_1DashSpec.html#a1fbb11a0cf9e2da5e50a238d2d2296ad),
[TechDraw::PATLineSpec::dump()](../../d0/d63/classTechDraw_1_1PATLineSpec.html#afd75832e21187226d13ec5eb50a1fdea),
[TechDraw::LineGroup::dump()](../../da/d19/classTechDraw_1_1LineGroup.html#a8606eb00acd29710020c20809d70f86b),
[TechDraw::GeomFormat::dump()](../../d7/d64/classTechDraw_1_1GeomFormat.html#a79aba35084cd9566dfb0ab9b1b8af0a1),
[TechDraw::Vertex::dump()](../../dd/db1/classTechDraw_1_1Vertex.html#a565b22a3ec5fe8c3eb27be9e4d07ce09),
[TechDraw::DrawUtil::dump1Vertex()](../../da/d23/classTechDraw_1_1DrawUtil.html#abfce92e9172c26b8a0c7ab0a0354b6ba),
[TechDraw::DrawViewPart::dumpCosEdges()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a67139004b7350a527af4b4b243089263),
[TechDraw::DrawViewPart::dumpCosVerts()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a6a092755bc9a45074e4b61d8a098e65a),
[TechDraw::DrawUtil::dumpCS()](../../da/d23/classTechDraw_1_1DrawUtil.html#a7b9d505f97e9f0310bed8aa2c3f692d3),
[TechDraw::DrawUtil::dumpCS3()](../../da/d23/classTechDraw_1_1DrawUtil.html#a7bdb8d65779d28dbe77fcdac4da6a007),
[TechDraw::DrawUtil::dumpEdge()](../../da/d23/classTechDraw_1_1DrawUtil.html#a10dadcf1585553431f3f81049d56bbfb),
[TechDraw::DrawUtil::dumpEdges()](../../da/d23/classTechDraw_1_1DrawUtil.html#affbe01f929949734d04d39621d509f4c),
[TechDrawGui::QGEPath::dumpGhostPoints()](../../d9/da7/classTechDrawGui_1_1QGEPath.html#a260588d9eddedfe45b8863a56003cd7d),
[TechDraw::DrawProjGroup::dumpISO()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a64c8445dbe972e26619f07afbe560a6f),
[PartGui::dumpLinearResults()](../../d5/d49/namespacePartGui.html#a4189ca02fa37799a62cf6cc3a5c8ef5a),
[TechDrawGui::QGEPath::dumpMarkerPos()](../../d9/da7/classTechDrawGui_1_1QGEPath.html#aec95f9811a6325bfd7384b74def2c5fe),
[TechDrawGui::QGIViewPart::dumpPath()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#af7a9e8e4067fe78d5f31b991cac7673c),
[TechDrawGui::DrawGuiUtil::dumpPointF()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a2cd471f15898fda5d9ffc7c616e95a35),
[TechDrawGui::QGIView::dumpRect()](../../d1/d99/classTechDrawGui_1_1QGIView.html#a9f3c65fefc7fecf8a65cc516e70ea79a),
[TechDrawGui::DrawGuiUtil::dumpRectF()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a741e024574ef46ab724c1d02981a3f69),
[TechDraw::DrawUtil::dumpVertexes()](../../da/d23/classTechDraw_1_1DrawUtil.html#aff6ff76e2571c3ae7815822e621a292e),
[TechDraw::DrawViewPart::dumpVerts()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1702482a57bc091665acb7022405286a),
[TechDraw::Ellipse::Ellipse()](../../d8/da6/classTechDraw_1_1Ellipse.html#a1d34c019e27a9250f109b94c19936a52),
[PartGui::evaluateAngularPreSelection()](../../d5/d49/namespacePartGui.html#af0dc1ad1549a7fac118db816447cb551),
[Base::Debugger::exec()](../../df/d4a/classBase_1_1Debugger.html#a381a3624cbf84286e071d1305c3ed81b),
[Inspection::Feature::execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[Sandbox::SandboxObject::execute()](../../da/dd9/classSandbox_1_1SandboxObject.html#a96b3044625736c856e807edd11e1bc00),
[Import::ImpExpDxfWrite::exportBCurve()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a84c25d10b4fcf3e43409208fea7f0a5f),
[Import::ImpExpDxfWrite::exportBSpline()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a7b8a3d3407ae1549e8bdb5d5b6f23b91),
[MeshGui::ViewProviderMesh::faceInfo()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a82e7c934502545ca07cefba12d6d00e9),
[MeshGui::ViewProviderMesh::faceInfoCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae3d2f360b9f432962521c1bb1b77dd98),
[MeshGui::ViewProviderMesh::fillHoleCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ad3cdb2b5549c092780ef6b1bb252cc02),
[TechDraw::BaseGeom::findEndPoints()](../../db/d3c/classTechDraw_1_1BaseGeom.html#a70af486379e8d084366ccc86c35dad7e),
[TechDrawGui::QGIViewDimension::findIsoExt()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a3888081268b10065d4854b4fee7b69c0),
[MeshCore::SphereFit::Fit()](../../dc/dce/classMeshCore_1_1SphereFit.html#a0fd2369a3f6d7a286033add8fad3c30c),
[TechDrawGui::TaskDetail::getAnchorScene()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ac47e200bf1be3381e59b3c6c4610494d),
[TechDrawGui::QGILeaderLine::getAttachFromFeature()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#abe5ebf7cb3ea4310c9b8012b78605819),
[TechDraw::CosmeticExtension::getCosmeticEdge()](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#abc908dfc748bdceab0a41f04a9031dc0),
[TechDrawGui::QGEPath::getDeltasFromLeader()](../../d9/da7/classTechDrawGui_1_1QGEPath.html#a59c9f7dddcda624bf7724c39938353f2),
[TechDrawGui::ViewProviderPage::getDrawPage()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a8d21be188e915b567971559b6c1bf512),
[TechDraw::DrawProjectSplit::getEdges()](../../d8/ded/classTechDraw_1_1DrawProjectSplit.html#ac943560b70b1fa2e0a7f1a80fa976f2b),
[TechDraw::DrawSVGTemplate::getEditableTextsFromTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a5d4fd489066be062afb816f45960c214),
[TechDraw::BaseGeom::getEndPoint()](../../db/d3c/classTechDraw_1_1BaseGeom.html#a3a858dca70ce63497500aa59cfface00),
[MeshGui::ViewProviderMesh::getFacetsFromPolygon()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a52b52077209751cf866a17cfa3898e8e),
[TechDraw::LineGroup::getGroupNamesFromFile()](../../da/d19/classTechDraw_1_1LineGroup.html#a966f9d0b784c905a4ee67aff8f307f8d),
[Fem::getObjectByType()](../../dd/d72/namespaceFem.html#a1d62957fae198eb1c03b3ce2c2503c3c),
[MeshGui::CylinderFitParameter::getParameter()](../../d6/d6d/classMeshGui_1_1CylinderFitParameter.html#ab93a68400083131e275c6f9d3af94fab),
[TechDraw::PATLineSpec::getPatternList()](../../d0/d63/classTechDraw_1_1PATLineSpec.html#a641ffbb724d1981fbf9a43363fed7c85),
[CDxfWrite::getPlateFile()](../../d6/d47/classCDxfWrite.html#a1a6d27cd40ddcd75bad06f9fb94b195d),
[TechDraw::LineGroup::getRecordFromFile()](../../da/d19/classTechDraw_1_1LineGroup.html#aa161197a1988c328173d1a8689f13059),
[TechDrawGui::TaskAlignViews::getSelectedEdges()](../../d8/d23/classTechDrawGui_1_1TaskAlignViews.html#a748566d07ecc0ca6df66f78ceca681a5),
[TechDraw::PATLineSpec::getSpecsForPattern()](../../d0/d63/classTechDraw_1_1PATLineSpec.html#ab2bfa1a86102af85a7e7f42c8625718b),
[TechDraw::BaseGeom::getStartPoint()](../../db/d3c/classTechDraw_1_1BaseGeom.html#a15028d4acf40331bf87b74d19beb95b0),
[TechDraw::DrawViewPart::getViewAxis()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a8c60f90e904e9ad5f0ee0afb13d8a2d2),
[TechDraw::DrawProjGroupItem::getViewAxis()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a66cab4b4ebd52d41889c7fdb9c854821),
[TechDrawGui::QGILeaderLine::getWayPointsFromFeature()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#a1f75c823bd5229f85a626e8846c4bb24),
[TechDraw::DrawProjGroupItem::getXDirection()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a86b744ee5d2b7ff5de819b0f23488498),
[TechDraw::ShapeExtractor::getXShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4e820635335afa9ce7506faaf4274cbd),
[TechDraw::DrawProjGroup::getXYPosition()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aaeadc17847095c9f9d5ff6db786e04bd),
[PartGui::goDimensionAngularNoTask()](../../d5/d49/namespacePartGui.html#a22a4e967d614ba7959dc90e89f6e76dc),
[MeshGui::ViewProviderMeshNode::handleEvent()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a51230ac2fb2c967f42ef5dfb134f0562),
[TechDrawGui::QGVNavStyle::handleKeyPressEvent()](../../dc/d63/classTechDrawGui_1_1QGVNavStyle.html#aa422ee6ac941f62a5c445a3e02c3c24b),
[TechDrawGui::QGVNavStyle::handleKeyReleaseEvent()](../../dc/d63/classTechDrawGui_1_1QGVNavStyle.html#aa20dc0f33c8332a83d052a2cfc45e4db),
[Fem::FemVTKTools::importFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a06964ad44830b32163bedb9351fad2c8),
[InspectionGui::ViewProviderInspection::inspectCallback()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a4e6895f19ff09d06e34c94fe7df62517),
[TechDraw::DrawUtil::Intersect2d()](../../da/d23/classTechDraw_1_1DrawUtil.html#afe855bd12c8cea41eb2af19ab79ba99d),
[ModelRefine::FaceTypedBSpline::isEqual()](../../d2/ded/classModelRefine_1_1FaceTypedBSpline.html#adf256b29be3e0efc99eed6bf3f2697ad),
[TechDraw::DrawProjectSplit::isOnEdge()](../../d8/ded/classTechDraw_1_1DrawProjectSplit.html#a5b512ff511e727022201f489ac54672b),
[TechDraw::PATLineSpec::load()](../../d0/d63/classTechDraw_1_1PATLineSpec.html#a2796f05515ba2428f6abf6a4e45744cc),
[Gui::MainWindow::loadUrls()](../../d5/d2f/classGui_1_1MainWindow.html#ac49add8806641195abfd2d92d738fb35),
[TechDrawGui::QGILeaderLine::makeLeaderPath()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#a0e58599dd22e5be45969ff2847d43522),
[TechDraw::DrawViewSection::makeLineSets()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a8673a58822bb65ebe493c128d2aef29e),
[Part::TopoShape::makeLoft()](../../d8/ded/classPart_1_1TopoShape.html#ab76949f558f233617fedb98d19c01afb),
[MeshGui::ViewProviderMesh::markPartCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a6eb548accf81ef25b6aa376ac7fa53a8),
[Gui::ViewProviderMeasureDistance::measureDistanceCallback()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a4eed79e1261f82642767853d3715baec),
[Message()](../../df/dca/classBase_1_1ConsoleSingleton.html#a322664077d1c391e11e07ec903c99e25),
[MeshGui::DlgEvaluateMeshImp::on_analyzeSelfIntersectionButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a0163b2f6722f270d8c39e379287d4dbb),
[Fem::ConstraintFluidBoundary::onChanged()](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Sandbox::SandboxObject::onChanged()](../../da/dd9/classSandbox_1_1SandboxObject.html#ae3e3d04a08a28cb8060a72df914f3685),
[PartDesignGui::ViewProviderBody::onChanged()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922),
[TechDraw::DrawPage::onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDrawGui::TaskDetail::onHighlightMoved()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a3381234d250275d524d73913667bbe23),
[TechDrawGui::TaskAlignViews::onHorizontallyClicked()](../../d8/d23/classTechDrawGui_1_1TaskAlignViews.html#adf509060233971d1d1e25aa59b79349a),
[FemGui::TaskCreateNodeSet::onSelectionChanged()](../../da/d68/classFemGui_1_1TaskCreateNodeSet.html#ad2deb16f6c0659bcef35f11d21ea6972),
[TechDrawGui::TaskLeaderLine::onTrackerClicked()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a581dcc144a5b4017a6356a89dda30abe),
[TechDrawGui::TaskCosVertex::onTrackerFinished()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#a70cc99622328e6c5e42c84caec735981),
[TechDrawGui::TaskLeaderLine::onTrackerFinished()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a3834c86229e7732145d671a0546087ea),
[MeshGui::ViewProviderMesh::partMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a252f3b9789355271cbc9ff56a65ba495),
[FemGui::TaskPostDataAlongLine::pointCallback()](../../db/dfe/classFemGui_1_1TaskPostDataAlongLine.html#aa3bd9ec395c25e0c5a7fbc9af43ffbe5),
[FemGui::TaskPostDataAtPoint::pointCallback()](../../d9/da7/classFemGui_1_1TaskPostDataAtPoint.html#a9d1755b4bb772f7b5dc2dacf96f4b585),
[TechDrawGui::QGSPage::postProcessXml()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#ac4055009ba04a7f89f6c9a935e4ce0a5),
[TechDraw::DrawSVGTemplate::processTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a9b2032d4f9db58231ae4ad79ca5b3778),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
[TechDraw::DrawProjectSplit::removeDuplicateEdges()](../../d8/ded/classTechDraw_1_1DrawProjectSplit.html#a429be04b0297cfd15a68f1462eaada7c),
[TechDrawGui::TaskLeaderLine::removeFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a3966869ef8faf23d5293b16f335de34c),
[TechDraw::CosmeticExtension::replaceCenterLine()](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#adf6210c3558801bedaf181180d39554e),
[TechDraw::CosmeticExtension::replaceCosmeticEdge()](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#a507578f9055e5c6728c0af30ca5110b0),
[TechDraw::CosmeticExtension::replaceCosmeticVertex()](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#ad9c50033034aca2ee516ab3984b24de4),
[TechDraw::CosmeticExtension::replaceGeomFormat()](../../d4/d9c/classTechDraw_1_1CosmeticExtension.html#aa8fdc31807f2d793e32dfd79092bc145),
[TechDraw::DrawViewImage::replaceImageIncluded()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#af2f2591cbc41f4175f8bcee32049e81d),
[Sandbox::SandboxObject::resetValue()](../../da/dd9/classSandbox_1_1SandboxObject.html#a9cf9176b0f4b455d64dea16575b4846c),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[TechDrawGui::TaskProjGroup::restoreGroupState()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a348f413a63a7fd86ebf8978fee5d028f),
[Part::TopoShape::revolve()](../../d8/ded/classPart_1_1TopoShape.html#ae541fa0768491d5d3e4123fcdd1296a8),
[BarThread::run()](../../d8/d7c/classBarThread.html#a8c0683b02f7de1024ed7a69daef8b132),
[Gui::ConsoleMessageTask::run()](../../da/d7f/classGui_1_1ConsoleMessageTask.html#a54a16e02dd5bd4afa25abb170fffd38a),
[Sandbox::DocumentTestThread::run()](../../d5/d8a/classSandbox_1_1DocumentTestThread.html#a27751a48ad75c90b8b678641eb975cde),
[MeshTestJob::run()](../../d3/de2/classMeshTestJob.html#a91b8f6906c883abf342c18bcddea5d53),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[ILoggerBlockerTest::runSingleTest()](../../d3/d59/classILoggerBlockerTest.html#aedb272178e3388617450e67220287e65),
[TechDraw::CenterLine::Save()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[TechDraw::DrawViewSection::sectionExec()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a79c8f60f63dd54684af4cad42f91ee4e),
[MeshGui::ViewProviderMesh::segmMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#af03a51bed2f5b62f24d2aecf1e03c4b4),
[Sandbox::SandboxObject::setIntValue()](../../da/dd9/classSandbox_1_1SandboxObject.html#a4a9142b5ebbbf3927c628df3423dbda8),
[TechDrawGui::QGTracker::setPoint()](../../da/d66/classTechDrawGui_1_1QGTracker.html#a837af38259b898c6ccb9f6e00846da2c),
[TechDraw::DrawViewImage::setupImageIncluded()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a70665b6da416755ac2cdb36d9c9ecf6d),
[TechDrawGui::QGEPath::showMarkers()](../../d9/da7/classTechDrawGui_1_1QGEPath.html#a916b69472635ba66e9e8f01a76b8b540),
[TechDraw::DrawUtil::simpleMinDist()](../../da/d23/classTechDraw_1_1DrawUtil.html#abaddb7eee1b533578917e763227a1ae1),
[TechDraw::DrawProjectSplit::split1Edge()](../../d8/ded/classTechDraw_1_1DrawProjectSplit.html#a19c7589d531e7d8c5b87f3b71152baa1),
[sPyMessage()](../../df/dca/classBase_1_1ConsoleSingleton.html#a2e67159961c8ac1b21ba4d528acdc37f),
[TechDrawGui::TaskAlignViews::TaskAlignViews()](../../d8/d23/classTechDrawGui_1_1TaskAlignViews.html#aea5d022e5e9edef8cba6f76e23327c20),
[TechDraw::DrawProjGroup::updateSecondaryDirs()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aab0e5d4fa1e0eaf890c7c6cb2eb06766),
[TechDrawGui::TaskWeldingSymbol::updateTiles()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#aac480071122ff57d72a8cba865b1c94c),
[Gui::OutputStdout::write()](../../df/d6a/classGui_1_1OutputStdout.html#a085180837c38cc708bb518560db36ded),
and
[Fem::FemVTKTools::writeResult()](../../d6/d26/classFem_1_1FemVTKTools.html#afe10808623915c79b6e74786a6f6d0e3).

## ◆ NotifyError()

void ConsoleSingleton::NotifyError  | ( | const char *  | _sMsg_| ) |   
---|---|---|---|---|---  
  
References
[Base::Error](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126a902b0d55fddef6f8d651fe1035b7d4bd).

Referenced by
[Base::ConsoleOutput::customEvent()](../../d5/dea/classBase_1_1ConsoleOutput.html#a40edafab0b89a345d146e6ab6284d580).

## ◆ NotifyLog()

void ConsoleSingleton::NotifyLog  | ( | const char *  | _sMsg_| ) |   
---|---|---|---|---|---  
  
References
[Base::Log](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126ace0be71e33226e4c1db2bcea5959f16b).

Referenced by
[Base::ConsoleOutput::customEvent()](../../d5/dea/classBase_1_1ConsoleOutput.html#a40edafab0b89a345d146e6ab6284d580).

## ◆ NotifyMessage()

void ConsoleSingleton::NotifyMessage  | ( | const char *  | _sMsg_| ) |   
---|---|---|---|---|---  
  
References
[Base::Message](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126a4c2a8fe7eaf24721cc7a9f0175115bd4).

Referenced by
[Base::ConsoleOutput::customEvent()](../../d5/dea/classBase_1_1ConsoleOutput.html#a40edafab0b89a345d146e6ab6284d580).

## ◆ NotifyWarning()

void ConsoleSingleton::NotifyWarning  | ( | const char *  | _sMsg_| ) |   
---|---|---|---|---|---  
  
References
[Base::Warning](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126a0eaadb4fcb48a0a0ed7bc9868be9fbaa).

Referenced by
[Base::ConsoleOutput::customEvent()](../../d5/dea/classBase_1_1ConsoleOutput.html#a40edafab0b89a345d146e6ab6284d580).

## ◆ Refresh()

void ConsoleSingleton::Refresh  | ( | | ) |   
---|---|---|---|---  
  
## ◆ SetConnectionMode()

void ConsoleSingleton::SetConnectionMode  | ( | [ConnectionMode](../../df/dca/classBase_1_1ConsoleSingleton.html#ab636a2b52258e7eb996862ff06d9157f) | _mode_| ) |   
---|---|---|---|---|---  
  
References
[connectionMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a91ebbf1a2a05d2d70aecfdbceeadcc73),
[Base::ConsoleOutput::getInstance()](../../d5/dea/classBase_1_1ConsoleOutput.html#ac8df68aed9f974d34e37ee0b945743bc),
and
[Queued](../../df/dca/classBase_1_1ConsoleSingleton.html#ab636a2b52258e7eb996862ff06d9157fa9ef54d51ac196670ac5578731895e70d).

## ◆ SetConsoleMode()

void ConsoleSingleton::SetConsoleMode  | ( | [ConsoleMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a2605ebb32e2df24f044f0d95df87e4fb) | _m_| ) |   
---|---|---|---|---|---  
  
Change mode.

sets the console in a special mode

References
[Verbose](../../df/dca/classBase_1_1ConsoleSingleton.html#a2605ebb32e2df24f044f0d95df87e4fba5c83abe71dc5d95a0598a974c3b87b13).

## ◆ SetDefaultLogLevel()

void Base::ConsoleSingleton::SetDefaultLogLevel  | ( | [int](../../d1/da0/classint.html) | _level_| ) |   
---|---|---|---|---|---  
  
## ◆ SetEnabledMsgType()

ConsoleMsgFlags ConsoleSingleton::SetEnabledMsgType  | ( | const char *  | _sObs_ ,   
---|---|---|---  
|  | ConsoleMsgFlags  | _type_ ,   
|  | [bool](../../d9/db9/classbool.html) | _b_  
| ) | |   
  
Enables or disables message types of a certain console observer.

_type_ can be OR'ed with any of the FreeCAD_ConsoleMsgType flags to enable –
if _b_ is true – or to disable – if _b_ is false – a console observer with
name _sObs_.

The return value is an OR'ed value of all message types that have changed
their state. For example

// switch off warnings and error messages

ConsoleMsgFlags ret =
[Base::Console](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729
"Access to the Console This method is used to gain access to the one and only
instance of the
ConsoleS...")().[SetEnabledMsgType](../../df/dca/classBase_1_1ConsoleSingleton.html#ad7f0fab600123b5a812f364e058fde09
"Enables or disables message types of a certain console observer.")("myObs",

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++
API\)"):[ConsoleSingleton::MsgType_Wrn](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dadf5163026958f3c10c1c064c405b3e95)|[Base::ConsoleSingleton::MsgType_Err](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da9adf564b5bca3813e28e053f8d208731),
false);

// do something without notifying observer myObs

...

// restore the former configuration again

Base::Console().SetEnabledMsgType("myObs", ret, true);

switches off warnings and error messages and restore the state before the
modification. If the observer _sObs_ doesn't exist then nothing happens.

References
[Base::ILogger::bErr](../../d8/d26/classBase_1_1ILogger.html#a4a39644f9509a9d4bff1d201c3878748),
[Base::ILogger::bLog](../../d8/d26/classBase_1_1ILogger.html#a8753678619bcabcddc21d0da955ecdce),
[Base::ILogger::bMsg](../../d8/d26/classBase_1_1ILogger.html#aca879668d459839a2bd65524cf38fbf6),
[Base::ILogger::bWrn](../../d8/d26/classBase_1_1ILogger.html#a4eb0f75d0a65ffad264bd0bb610f026a),
[Get()](../../df/dca/classBase_1_1ConsoleSingleton.html#ae4ca9fea6787c5acd17c66dbfbbe374b),
[MsgType_Err](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da9adf564b5bca3813e28e053f8d208731),
[MsgType_Log](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da4c8d83da40448a24fd37469122037dfb),
[MsgType_Txt](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dae3438ada440361f8f7bfe29451754b99),
and
[MsgType_Wrn](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dadf5163026958f3c10c1c064c405b3e95).

Referenced by
[Base::ILoggerBlocker::ILoggerBlocker()](../../dc/d2a/classBase_1_1ILoggerBlocker.html#aecd240f0fff37058949244ddd7ebff50),
[ILoggerBlockerTest::runTest()](../../d3/d59/classILoggerBlockerTest.html#ac4d9a42873dec078f2c284ac300f5553),
and
[Base::ILoggerBlocker::~ILoggerBlocker()](../../dc/d2a/classBase_1_1ILoggerBlocker.html#aee44d9ee3af66ad06a1928391e32da11).

## ◆ sPyError()

| [PyObject](../../df/d1b/classPyObject.html) * ConsoleSingleton::sPyError  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
and
[Instance()](../../df/dca/classBase_1_1ConsoleSingleton.html#a12194f03be46abe3cbe3faa2a1c23d43).

## ◆ sPyGetStatus()

| [PyObject](../../df/d1b/classPyObject.html) * ConsoleSingleton::sPyGetStatus  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[Base::ILogger::bErr](../../d8/d26/classBase_1_1ILogger.html#a4a39644f9509a9d4bff1d201c3878748),
[Base::ILogger::bLog](../../d8/d26/classBase_1_1ILogger.html#a8753678619bcabcddc21d0da955ecdce),
[Base::ILogger::bMsg](../../d8/d26/classBase_1_1ILogger.html#aca879668d459839a2bd65524cf38fbf6),
[Base::ILogger::bWrn](../../d8/d26/classBase_1_1ILogger.html#a4eb0f75d0a65ffad264bd0bb610f026a),
[Get()](../../df/dca/classBase_1_1ConsoleSingleton.html#ae4ca9fea6787c5acd17c66dbfbbe374b),
and
[Instance()](../../df/dca/classBase_1_1ConsoleSingleton.html#a12194f03be46abe3cbe3faa2a1c23d43).

## ◆ sPyLog()

| [PyObject](../../df/d1b/classPyObject.html) * ConsoleSingleton::sPyLog  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[Instance()](../../df/dca/classBase_1_1ConsoleSingleton.html#a12194f03be46abe3cbe3faa2a1c23d43),
and
[Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964).

## ◆ sPyMessage()

| [PyObject](../../df/d1b/classPyObject.html) * ConsoleSingleton::sPyMessage  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[Instance()](../../df/dca/classBase_1_1ConsoleSingleton.html#a12194f03be46abe3cbe3faa2a1c23d43),
and
[Message()](../../df/dca/classBase_1_1ConsoleSingleton.html#a322664077d1c391e11e07ec903c99e25).

## ◆ sPySetStatus()

| [PyObject](../../df/d1b/classPyObject.html) * ConsoleSingleton::sPySetStatus  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[Base::ILogger::bErr](../../d8/d26/classBase_1_1ILogger.html#a4a39644f9509a9d4bff1d201c3878748),
[Base::ILogger::bLog](../../d8/d26/classBase_1_1ILogger.html#a8753678619bcabcddc21d0da955ecdce),
[Base::ILogger::bMsg](../../d8/d26/classBase_1_1ILogger.html#aca879668d459839a2bd65524cf38fbf6),
[Base::ILogger::bWrn](../../d8/d26/classBase_1_1ILogger.html#a4eb0f75d0a65ffad264bd0bb610f026a),
[Get()](../../df/dca/classBase_1_1ConsoleSingleton.html#ae4ca9fea6787c5acd17c66dbfbbe374b),
[Instance()](../../df/dca/classBase_1_1ConsoleSingleton.html#a12194f03be46abe3cbe3faa2a1c23d43),
and
[Base::PyExc_FC_GeneralError](../../db/d07/namespaceBase.html#ae4527426552a441e3158bafd69b0561f).

## ◆ sPyWarning()

| [PyObject](../../df/d1b/classPyObject.html) * ConsoleSingleton::sPyWarning  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[Instance()](../../df/dca/classBase_1_1ConsoleSingleton.html#a12194f03be46abe3cbe3faa2a1c23d43),
and
[Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

## ◆ UnsetConsoleMode()

void ConsoleSingleton::UnsetConsoleMode  | ( | [ConsoleMode](../../df/dca/classBase_1_1ConsoleSingleton.html#a2605ebb32e2df24f044f0d95df87e4fb) | _m_| ) |   
---|---|---|---|---|---  
  
Change mode.

unsets the console from a special mode

References
[Verbose](../../df/dca/classBase_1_1ConsoleSingleton.html#a2605ebb32e2df24f044f0d95df87e4fba5c83abe71dc5d95a0598a974c3b87b13).

## ◆ Warning()

| void ConsoleSingleton::Warning  | ( | const char *  | _pMsg_ ,   
---|---|---|---  
|  |  | _..._  
| ) | |   
virtual  
  
Prints a warning Message.

Prints a Message This method issues a Warning.

Messages are used to get the users attention. That means when FreeCAD is in
GUI mode a Message Box pops up. In console mode a colored message is returned
to the console! Don't use this carelessly. For information purposes the 'Log'
or 'Message' methods are more appropriate.

    You can use a printf like interface like: 

[Console](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729
"Access to the Console This method is used to gain access to the one and only
instance of the
ConsoleS...")().[Warning](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326
"Prints a warning Message.")("Some defects in %s, loading
anyway\n",[str](../../d9/d36/classstr.html));

See also

    [Message](../../df/dca/classBase_1_1ConsoleSingleton.html#a322664077d1c391e11e07ec903c99e25 "Prints a Message.")
     [Error](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644 "Prints a error Message.")
     [Log](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964 "Prints a log Message.")

References
[Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

Referenced by
[Gui::TaskView::TaskView::accept()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#a91119b21ac8c18c973bfe6fdc63bbde4),
[FemGui::TaskDlgCreateNodeSet::accept()](../../d9/d8f/classFemGui_1_1TaskDlgCreateNodeSet.html#aae7b7afa431004b899003fe789f532bb),
[FemGui::TaskDlgMeshShapeNetgen::accept()](../../dc/db4/classFemGui_1_1TaskDlgMeshShapeNetgen.html#aa88c49eb6c4ad7cd760e8fcb2c3181be),
[FemGui::TaskDlgFemConstraintFluidBoundary::accept()](../../da/d17/classFemGui_1_1TaskDlgFemConstraintFluidBoundary.html#a92106711f12fb0fb783c7e411d8f3923),
[MeshGui::GmshWidget::accept()](../../d0/de7/classMeshGui_1_1GmshWidget.html#a44b9e083650491827760d585d7e046d6),
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[RobotGui::TaskDlgEdge2Trac::accept()](../../d6/da9/classRobotGui_1_1TaskDlgEdge2Trac.html#a8fae3bae30ab8e9c0bcb0034113f72a1),
[Sketcher::Sketch::addEqualConstraint()](../../d9/d9b/classSketcher_1_1Sketch.html#a5a93fa3f636cb082e7b71f2e3e0a2f12),
[Sketcher::Sketch::addPerpendicularConstraint()](../../d9/d9b/classSketcher_1_1Sketch.html#ab2711ee8c39b9f1f72f1020066817152),
[Gui::CommandManager::addTo()](../../d1/da7/classGui_1_1CommandManager.html#aae4cdddda8b7ae4d320835fdb3b61b73),
[TechDraw::DrawPage::addView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ac3e23be3a1fe6b9e35a45c680e33dd8a),
[Sketcher::SketchAnalysis::analyseMissingPointOnPointCoincident()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a353f09f64b5882c26cc62b5560299383),
[TechDraw::DrawUtil::angleWithX()](../../da/d23/classTechDraw_1_1DrawUtil.html#afa770b85407535a96f2102f4f4962a7a),
[TechDraw::DrawProjGroup::arrangeViewPointers()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a8a8bdca0831ea0e16e664ad17f0a04f8),
[TechDrawGui::ViewProviderDrawingView::attach()](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#ab6efd26a6629d730940224f8ee8788b6),
[TechDraw::Preferences::bitmapFill()](../../d6/dde/classTechDraw_1_1Preferences.html#aaa59c01070e04cb1f547cc0d0fca41b8),
[PartDesignGui::TaskFeaturePick::buildFeatures()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a10945e14aca2a56d0f5ac9e4b0064379),
[TechDrawGui::QGIFace::buildPixHatch()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#ab8baaa5bce257d6131474520bd84b566),
[TechDrawGui::QGIFace::buildSvgHatch()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#a7bbf273a370f0a8cba34655cc32d026e),
[Gui::PropertyEditor::PropertyEditor::buildUp()](../../d5/d10/classGui_1_1PropertyEditor_1_1PropertyEditor.html#a00d6964123d5c1c51b41538befbe5ca6),
[TechDraw::CenterLine::calcEndPoints()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a34df15a8a959516ecc49512c3ec5a73c),
[TechDraw::CenterLine::calcEndPoints2Lines()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a54d1cc5e3f8aa8923c2c28bdbe25c262),
[TechDraw::CenterLine::calcEndPoints2Points()](../../d5/dd5/classTechDraw_1_1CenterLine.html#aedb72634306a11f9eb49ffac16eb7e2b),
[Attacher::AttachEngine3D::calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
[Attacher::AttachEngineLine::calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[TechDraw::CenterLine::CenterLineBuilder()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a0669426226ba9f14e5509c484b3ee6c8),
[Gui::Application::checkForPreviousCrashes()](../../d9/da8/classGui_1_1Application.html#aacd77a596b9b2d8221fb7900e48e0336),
[Part::ExtrusionHelper::checkInnerWires()](../../d4/dd3/classPart_1_1ExtrusionHelper.html#a0ef9be3ca23bc91b1751e7a71c989c88),
[FemGui::TaskDlgMeshShapeNetgen::clicked()](../../dc/db4/classFemGui_1_1TaskDlgMeshShapeNetgen.html#ae8b504fa8135ac1fdfaf55dbdf8e4e6e),
[RobotGui::TaskDlgEdge2Trac::clicked()](../../d6/da9/classRobotGui_1_1TaskDlgEdge2Trac.html#a49a8080fac071229f4461ab7e3fd86cd),
[Base::ConsoleObserverFile::ConsoleObserverFile()](../../d9/dae/classBase_1_1ConsoleObserverFile.html#acfd8465fccf0256f177a708ba5a0ff36),
[TechDrawGui::Grabber3d::copyActiveViewToSvgFile()](../../d7/d83/classTechDrawGui_1_1Grabber3d.html#a44f769bea9d4e116b3667e59bec4e6da),
[TechDrawGui::QGISVGTemplate::createClickHandles()](../../d4/d36/classTechDrawGui_1_1QGISVGTemplate.html#a2bcf2fb5e0c80557b727afaaadbb2777),
[PartGui::ViewProvider2DObjectGrid::createGrid()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a6872b82ce1aa46b6532e864681e262ae),
[Gui::DocumentItem::createNewItem()](../../df/d15/classGui_1_1DocumentItem.html#a4e6783245b87938a4c176782e188a75c),
[Gui::WidgetFactoryInst::createPreferencePage()](../../d5/d83/classGui_1_1WidgetFactoryInst.html#a3cc9e4ee3575cfdf3398d3b7150190a4),
[Gui::WidgetFactoryInst::createWidget()](../../d5/d83/classGui_1_1WidgetFactoryInst.html#a8a166efde23cd16fb19b84de63abf3b3),
[TechDrawGui::QGIFace::dashedPPath()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#ac893b16b4130c990b40e45750d31b9a9),
[TechDraw::Preferences::defaultTemplate()](../../d6/dde/classTechDraw_1_1Preferences.html#aa2ba4e5c813143e90316673e9073e586),
[TechDraw::Preferences::defaultTemplateDir()](../../d6/dde/classTechDraw_1_1Preferences.html#abe38defbf2f6314b882b30707b5bde06),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[GCS::System::diagnose()](../../db/d28/classGCS_1_1System.html#ae239feb89ff7b144d842d954d5fbcf74),
[TechDrawGui::QGIViewAnnotation::drawAnnotation()](../../d4/d5b/classTechDrawGui_1_1QGIViewAnnotation.html#a1da6a03b5c446d2593b9dea4492b07b6),
[TechDrawGui::QGIViewClip::drawClip()](../../d4/dcc/classTechDrawGui_1_1QGIViewClip.html#a272bbbc60a11ba7d9c687cff260df23d),
[SketcherGui::EditModeConstraintCoinManager::drawConstraintIcons()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a20c4280c68dc704bd2652d6097b0383a),
[TechDrawGui::QGIViewSection::drawSectionFace()](../../d7/d73/classTechDrawGui_1_1QGIViewSection.html#a23b734cc85fce28a0a42c4d061686cb4),
[PartDesign::Transformed::execute()](../../dd/de1/classPartDesign_1_1Transformed.html#aef9667071a3f6bb2ed13226f84629049),
[Sketcher::SketchObjectSF::execute()](../../de/da4/classSketcher_1_1SketchObjectSF.html#aee2e5bb2b2aa00817df40cae0574ef36),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDraw::DrawViewPart::execute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[TechDraw::DrawViewSymbol::execute()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a44eea88d3e8522c41e9dcee9acff10ce),
[Import::ImpExpDxfWrite::exportShape()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a1609a1c83ed4629589b3ff32428340a1),
[TechDraw::DrawViewPart::extractFaces()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aaaaf9f3bc41bcad927258ed1fdb53baa),
[TechDraw::GeometryObject::extractGeometry()](../../dc/dbe/classTechDraw_1_1GeometryObject.html#a259d4c302cfd20d7b03a508fbfec10e7),
[Gui::PrefWidget::failedToRestore()](../../d9/d6b/classGui_1_1PrefWidget.html#ac60549e5da5f88c80a094e4b7a0c0bab),
[Gui::PrefWidget::failedToSave()](../../d9/d6b/classGui_1_1PrefWidget.html#a55356c2abfba09f4fe7d809a542c0945),
[ParameterGrp::FindElement()](../../d4/d97/classParameterGrp.html#a6b04f3ec7569d900c594ad3c9bf114ce),
[ParameterGrp::FindOrCreateElement()](../../d4/d97/classParameterGrp.html#a4cb72c5224b94a07642acf1054a6e1f4),
[TechDraw::DrawViewSection::findSectionPlaneIntersections()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a251a6093a1e7bf37a5b5a768f4f13db5),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[Path::Toolpath::getCycleTime()](../../d6/d0c/classPath_1_1Toolpath.html#a6adb7debbb92c2d09e8b280b00003696),
[TechDrawGui::QGEPath::getDeltasFromLeader()](../../d9/da7/classTechDrawGui_1_1QGEPath.html#a59c9f7dddcda624bf7724c39938353f2),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[TechDraw::DrawProjGroup::getDirsFromFront()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a66cbbc8038fcab5532278784cbac867b),
[TechDraw::DrawLeaderLine::getKinkPoint()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a9ad287a5d948a9644b7cbe79528e16be),
[TechDraw::DrawViewDimension::getPrefixSuffixSpec()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a6a8d79939b1d5346af1f436ce34dafcf),
[TechDrawGui::DrawGuiUtil::getProjDirFromFace()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a1e16c708a7e2a33bd36999a5f02ae63b),
[TechDraw::DrawViewPart::getProjectionCS()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ae1dd72b98fa563bf72d6c39f49577632),
[TechDraw::DrawViewPart::getSourceShape()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aeb0d7bbe7418b86053f38713d4c91fa9),
[TechDraw::DrawViewPart::getSourceShapeFused()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a259e1a941c8e6a0651089bfa4111e3bd),
[TechDraw::DrawLeaderLine::getTailPoint()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#adad4a832160f419f1980e51367240499),
[TechDraw::DrawLeaderLine::getTileOrigin()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a550fc46519d2e26a13302aa7cb0b8a8e),
[AttacherGui::getUIStrings()](../../d9/d53/namespaceAttacherGui.html#a4633c8769798583ed5a439779508c2cc),
[TechDraw::DrawProjGroupItem::getViewAxis()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a66cab4b4ebd52d41889c7fdb9c854821),
[TechDraw::DrawProjGroup::getViewIndex()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a92924eedc2c197844d6012d822d0bb7b),
[TechDrawGui::QGILeaderLine::getWayPointsFromFeature()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#a1f75c823bd5229f85a626e8846c4bb24),
[Gui::View3DInventorViewer::imageFromFramebuffer()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a04e9b1105f2ab632a6a2b50ae00e0c4a),
[Gui::View3DInventorViewer::init()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a8688bb92e0dcb56b6b5ed7d095e07071),
[TechDrawGui::TaskGeomHatch::initUi()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#acfee83bfb4690c933dc1f4149fd4c054),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
[Sketcher::SketchObject::isExternalAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a15854bee280f512f617c7f34752ab823),
[TechDraw::Preferences::lineGroupFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a9c538c5e2ad7c65962a5dd44dd26b17c),
[TechDrawGui::QGIFace::lineSetToFillItems()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#af53e0be46e34bf69b446f1f9bd03e259),
[Mesh::MeshObject::load()](../../d8/dcc/classMesh_1_1MeshObject.html#a0a08f40f39b5c78345146ac8b8f639f9),
[MeshCore::MeshInput::LoadAny()](../../d9/d08/classMeshCore_1_1MeshInput.html#a6abd637db3c98170463307577f165a06),
[MeshCore::MeshInput::LoadNastran()](../../d9/d08/classMeshCore_1_1MeshInput.html#a33bc94cc3daf0fc3a6b9352fbf87b4e1),
[Spreadsheet::PropertySheet::mergeCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad33ba60621c10ca7fbfa5f257ab351e1),
[Gui::SelectionSingleton::notify()](../../d4/dca/classGui_1_1SelectionSingleton.html#a50ab2367fb54a9eba65380550698d811),
[Gui::Dialog::DlgCustomKeyboardImp::on_editShortcut_textChanged()](../../df/d9c/classGui_1_1Dialog_1_1DlgCustomKeyboardImp.html#af8947ac0e47556c56e2749e2d1ed5856),
[Gui::Dialog::DlgMacroExecuteImp::on_toolbarButton_clicked()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#a1607697dc3b346332ce658cdc277df6e),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewSymbol::onChanged()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#adb3364984aac5da2ff804a43845ceee4),
[App::Document::onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
[PartGui::SectionCut::onFlipXclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a5fbc3a06b93ca2cc623e4c60b2d8b0cd),
[PartGui::SectionCut::onFlipYclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a086343100aa8f33a1f885130b13fa4ad),
[PartGui::SectionCut::onFlipZclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a56a8cd5a5ec5c2228e4d5a5f8a8c232a),
[Import::ImpExpDxfRead::OnReadArc()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#a0850a3ddff938af3097fbec1e53b5f64),
[Import::ImpExpDxfRead::OnReadCircle()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#a6f45bf1239131187c293cc915997f43c),
[Import::ImpExpDxfRead::OnReadEllipse()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#a6669fbe86c5cd1adbc4dccfd51028192),
[Import::ImpExpDxfRead::OnReadSpline()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#ae11bb190131ad497e54bac982ec59cb7),
[TechDrawGui::QGILeaderLine::onSourceChange()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#ab3073068dad776704ac7652e79ab594d),
[TechDraw::Preferences::patFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a603db0a17ac567dd7dc8b20fbe51c609),
[Gui::BitmapFactoryInst::pixmap()](../../dc/da1/classGui_1_1BitmapFactoryInst.html#ad975d06ee42f3798e14ba48f7d58e0a0),
[Gui::Command::printConflictingAccelerators()](../../d2/dff/classGui_1_1Command.html#a2a23279eb85adf78347140f2b0f466da),
[TechDrawGui::MDIViewPage::printPdf()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a8117703a961c995317f9634a1b0c5e9e),
[App::Application::processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa),
[App::Application::processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939),
[Base::ScriptFactorySingleton::ProduceScript()](../../d3/dba/classBase_1_1ScriptFactorySingleton.html#a2e1d1349ea431e05c7c5c95c20e17e07),
[Gui::NS::GestureState::react()](../../db/d04/classGui_1_1NS_1_1GestureState.html#a392b8358a525725530ce8365c7adc121),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Gui::TaskView::TaskView::reject()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#a342fe11922c6b973615772a63676927d),
[TechDrawGui::TaskRichAnno::removeFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a8fbd082bee0ba6db50f0a83a504f2b0b),
[Gui::View3DInventorViewer::resetEditingRoot()](../../d5/d29/classGui_1_1View3DInventorViewer.html#aab89c5619d8a9f8f32b5610f6f48662a),
[TechDraw::CosmeticEdge::Restore()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a393b837a069a0baa76e15088e1fe49a0),
[TechDraw::CenterLine::Restore()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
[App::PropertyPythonObject::Restore()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a7c4c1053b780d2f149cc99c86d3e39ff),
[App::PropertyEnumeration::Restore()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[TechDrawGui::QGIProjGroup::rotateView()](../../db/d20/classTechDrawGui_1_1QGIProjGroup.html#a096f68ce65a30c6174d643cc7fb5062a),
[Gui::ConsoleWarningTask::run()](../../d6/d79/classGui_1_1ConsoleWarningTask.html#a1971a6f96f0d098fda57f6a9a7e56354),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[Gui::PythonDebugger::runFile()](../../d6/d11/classGui_1_1PythonDebugger.html#abc87bde9333762be5102ca6d99b14be6),
[ILoggerBlockerTest::runSingleTest()](../../d3/d59/classILoggerBlockerTest.html#aedb272178e3388617450e67220287e65),
[TechDraw::CosmeticEdge::Save()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a31c75a92b51476f8968d584e6be31d6c),
[MeshCore::MeshOutput::SaveOBJ()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3d771358cea3ae77d666c54aba2692b5),
[MeshCore::MeshOutput::SaveOFF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8b4f5b020dd2b94b087ff831b7aee3c4),
[TechDrawGui::MDIViewPage::saveSVG()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#ae6e21e88891cfc2149e03e480ed935e9),
[TechDraw::CenterLine::scaledGeometry()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a104bfe6bf49d7b364f65000352e670ea),
[TechDraw::DrawViewSection::sectionExec()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a79c8f60f63dd54684af4cad42f91ee4e),
[Gui::Application::setActiveDocument()](../../d9/da8/classGui_1_1Application.html#a689d6d547879b12ded7364fa0fb7953c),
[SketcherGui::ViewProviderSketch::setEdit()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ad28c651e806a00fca15332d4c04b47c9),
[Gui::PrefWidget::setParamGrpPath()](../../d9/d6b/classGui_1_1PrefWidget.html#ab28015e438a648affba1609c94b67861),
[Gui::SelectionSingleton::slotSelectionChanged()](../../d4/dca/classGui_1_1SelectionSingleton.html#ae0bb1709723ef769a331ac020f67d7b0),
[Sketcher::SketchObject::solve()](../../d9/dad/classSketcher_1_1SketchObject.html#a0bcef04719586a7122d762061b2d4ac4),
[TechDraw::LineGroup::split()](../../da/d19/classTechDraw_1_1LineGroup.html#a4e869ac6174fd65bd55d882670f920d2),
[sPyWarning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a7d356c1cafd385001e50cde27c18d58f),
[Gui::Application::sSendActiveView()](../../d9/da8/classGui_1_1Application.html#abfd3318756a4a0aaa2610148c1090f38),
[Gui::Application::sSendFocusView()](../../d9/da8/classGui_1_1Application.html#a0af4b5682fe80b43b03eab55cd435c60),
[TechDraw::Preferences::svgFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a7948f1f445732b3f5720eaa35de03d8d),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[Gui::TaskView::TaskSelectLinkProperty::TaskSelectLinkProperty()](../../d3/d1b/classGui_1_1TaskView_1_1TaskSelectLinkProperty.html#a6ec8c7b8e4d45bde4f8ce5968bdd91b4),
[TechDraw::DrawPage::unsetupObject()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ad65529c32a2d36f88a87e6734f093fcf),
[TechDraw::DrawProjGroupItem::unsetupObject()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a74c1e831d9704f99007d0b9398001f90),
[TechDrawGui::QGILeaderLine::updateView()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#aedc0bf02a116913c31d09ee665f7f546),
[TechDrawGui::QGIWeldSymbol::updateView()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#ac030e5933126ff6da26a3ae1a78c061f),
[Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326),
[TechDrawGui::PreferencesGui::weldingDirectory()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#ae8f758711778daab1558370f25fa519f),
[PartGui::DlgProjectionOnSurface::~DlgProjectionOnSurface()](../../d2/da4/classPartGui_1_1DlgProjectionOnSurface.html#a7d2e3355dfa8759dd537d765c4bc8e96),
[DocOpenGuard::~DocOpenGuard()](../../d9/dfb/classDocOpenGuard.html#a844a33a41c99c401dec94a8737a8c1e8),
[Base::ILoggerBlocker::~ILoggerBlocker()](../../dc/d2a/classBase_1_1ILoggerBlocker.html#aee44d9ee3af66ad06a1928391e32da11),
and
[App::Application::TransactionSignaller::~TransactionSignaller()](../../dc/d13/classApp_1_1Application_1_1TransactionSignaller.html#a1f32327336057334e85f616aeb14ca7d).

## Friends And Related Function Documentation

## ◆ ConsoleOutput

| [friend](../../d7/d23/classfriend.html) class
[ConsoleOutput](../../d5/dea/classBase_1_1ConsoleOutput.html)  
---  
friend  
  
## Member Data Documentation

## ◆ BufferSize

| const unsigned [int](../../d1/da0/classint.html)
Base::ConsoleSingleton::BufferSize = 4024  
---  
static  
  
Referenced by
[GCS::SolverReportingManager::LogToConsole()](../../d7/d2a/classGCS_1_1SolverReportingManager.html#ae9062222c2d3e8efa384e50f5cd74fc1).

## ◆ connectionMode

|
[ConnectionMode](../../df/dca/classBase_1_1ConsoleSingleton.html#ab636a2b52258e7eb996862ff06d9157f)
Base::ConsoleSingleton::connectionMode  
---  
protected  
  
Referenced by
[SetConnectionMode()](../../df/dca/classBase_1_1ConsoleSingleton.html#a48e7205de536c5cebc7048a42fc2157f).

## ◆ Methods

| [PyMethodDef](../../da/dab/classPyMethodDef.html) ConsoleSingleton::Methods  
---  
static  
  
**Initial value:**

= {

{"PrintMessage",
[ConsoleSingleton::sPyMessage](../../df/dca/classBase_1_1ConsoleSingleton.html#a2e67159961c8ac1b21ba4d528acdc37f),
METH_VARARGS,

"PrintMessage(string) -- Print a message to the output"},

{"PrintLog",
[ConsoleSingleton::sPyLog](../../df/dca/classBase_1_1ConsoleSingleton.html#a8921316e836ee1f7c2dfc47f033c2c01),
METH_VARARGS,

"PrintLog(string) -- Print a log message to the output"},

{"PrintError" ,
[ConsoleSingleton::sPyError](../../df/dca/classBase_1_1ConsoleSingleton.html#a8676363ed03277ee2403a7cd9bf18c5f),
METH_VARARGS,

"PrintError(string) -- Print an error message to the output"},

{"PrintWarning",
[ConsoleSingleton::sPyWarning](../../df/dca/classBase_1_1ConsoleSingleton.html#a7d356c1cafd385001e50cde27c18d58f),
METH_VARARGS,

"PrintWarning -- Print a warning to the output"},

{"SetStatus",
[ConsoleSingleton::sPySetStatus](../../df/dca/classBase_1_1ConsoleSingleton.html#a38ebfd3e6dd742dd3cfc180bc03025e3),
METH_VARARGS,

"Set the status for either Log, Msg, Wrn or Error for an observer"},

{"GetStatus",
[ConsoleSingleton::sPyGetStatus](../../df/dca/classBase_1_1ConsoleSingleton.html#ac31064289a9d46191b3fe33692bb3483),
METH_VARARGS,

"Get the status for either Log, Msg, Wrn or Error for an observer"},

{nullptr, nullptr, 0, nullptr}

}

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Console.h
  * FreeCAD/src/Base/Console.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

