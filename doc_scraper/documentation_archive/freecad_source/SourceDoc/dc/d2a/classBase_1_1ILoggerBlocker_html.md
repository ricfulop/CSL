---
url: https://freecad.github.io/SourceDoc/dc/d2a/classBase_1_1ILoggerBlocker.html
scraped_at: 2025-09-08T15:16:25.870670
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html)

[List of all members](../../d9/da5/classBase_1_1ILoggerBlocker-members.html) | Public Member Functions

Base::ILoggerBlocker Class Reference

The [ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html "The
ILoggerBlocker class This class allows to temporary block then automatically
restore arbitrary me...") class This class allows to temporary block then
automatically restore arbitrary message types on a particular console
observer. [More...](../../dc/d2a/classBase_1_1ILoggerBlocker.html#details)

`#include <ConsoleObserver.h>`

##  Public Member Functions  
  
---  
|
[ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html#aecd240f0fff37058949244ddd7ebff50)
(const char *co, ConsoleMsgFlags
msgTypes=[ConsoleSingleton::MsgType_Txt](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dae3438ada440361f8f7bfe29451754b99)|[ConsoleSingleton::MsgType_Log](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da4c8d83da40448a24fd37469122037dfb)|[ConsoleSingleton::MsgType_Wrn](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dadf5163026958f3c10c1c064c405b3e95)|[ConsoleSingleton::MsgType_Err](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da9adf564b5bca3813e28e053f8d208731))  
|
[ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html#a8a8c0744cfb5fe7edd3d763aaecf3642)
([ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) const
&&)=delete  
|
[ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html#a0d2bd3e535dadf82e5eea9ee0f7b2f70)
([ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) const
&)=delete  
[ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) & | [operator=](../../dc/d2a/classBase_1_1ILoggerBlocker.html#a0b680c6426228f1eed85e005d355572d) ([ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) const &&)=delete  
[ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) & | [operator=](../../dc/d2a/classBase_1_1ILoggerBlocker.html#a61606d80082351fa77c387518e2f53bf) ([ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) const &)=delete  
|
[~ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html#aee44d9ee3af66ad06a1928391e32da11)
()  
  
## Detailed Description

The [ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html "The
ILoggerBlocker class This class allows to temporary block then automatically
restore arbitrary me...") class This class allows to temporary block then
automatically restore arbitrary message types on a particular console
observer.

## Constructor & Destructor Documentation

## ◆ ILoggerBlocker() [1/3]

| Base::ILoggerBlocker::ILoggerBlocker  | ( | const char *  | _co_ ,   
---|---|---|---  
|  | ConsoleMsgFlags  | _msgTypes_ = `[ConsoleSingleton::MsgType_Txt](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dae3438ada440361f8f7bfe29451754b99) | [ConsoleSingleton::MsgType_Log](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da4c8d83da40448a24fd37469122037dfb) | [ConsoleSingleton::MsgType_Wrn](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399dadf5163026958f3c10c1c064c405b3e95) | [ConsoleSingleton::MsgType_Err](../../df/dca/classBase_1_1ConsoleSingleton.html#a26769165baa8e10aa96d68a89d75399da9adf564b5bca3813e28e053f8d208731)`  
| ) | |   
explicit  
  
References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
and
[Base::ConsoleSingleton::SetEnabledMsgType()](../../df/dca/classBase_1_1ConsoleSingleton.html#ad7f0fab600123b5a812f364e058fde09).

## ◆ ILoggerBlocker() [2/3]

| Base::ILoggerBlocker::ILoggerBlocker  | ( | [ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) const & | | ) |   
---|---|---|---|---|---  
delete  
  
## ◆ ILoggerBlocker() [3/3]

| Base::ILoggerBlocker::ILoggerBlocker  | ( | [ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) const && | | ) |   
---|---|---|---|---|---  
delete  
  
## ◆ ~ILoggerBlocker()

Base::ILoggerBlocker::~ILoggerBlocker  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::SetEnabledMsgType()](../../df/dca/classBase_1_1ConsoleSingleton.html#ad7f0fab600123b5a812f364e058fde09),
and
[Base::ConsoleSingleton::Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

## Member Function Documentation

## ◆ operator=() [1/2]

| [ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) & Base::ILoggerBlocker::operator=  | ( | [ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) const && | | ) |   
---|---|---|---|---|---  
delete  
  
## ◆ operator=() [2/2]

| [ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) & Base::ILoggerBlocker::operator=  | ( | [ILoggerBlocker](../../dc/d2a/classBase_1_1ILoggerBlocker.html) const & | | ) |   
---|---|---|---|---|---  
delete  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Base/ConsoleObserver.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

