---
url: https://freecad.github.io/SourceDoc/dd/d19/classApp_1_1AutoTransaction.html
scraped_at: 2025-09-08T14:53:46.244673
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [AutoTransaction](../../dd/d19/classApp_1_1AutoTransaction.html)

[List of all members](../../d4/d08/classApp_1_1AutoTransaction-members.html) | Public Member Functions | Static Public Member Functions

App::AutoTransaction Class Reference

Helper class to manager transaction (i.e. undo/redo)
[More...](../../dd/d19/classApp_1_1AutoTransaction.html#details)

`#include <AutoTransaction.h>`

##  Public Member Functions  
  
---  
|
[AutoTransaction](../../dd/d19/classApp_1_1AutoTransaction.html#a7cf288a8744e6ed274d91dfdc59acbff)
(const char *name=nullptr, [bool](../../d9/db9/classbool.html) tmpName=false)  
| Constructor.
[More...](../../dd/d19/classApp_1_1AutoTransaction.html#a7cf288a8744e6ed274d91dfdc59acbff)  
  
void | [close](../../dd/d19/classApp_1_1AutoTransaction.html#a78f86284384fbf21e95706b6e5dd3ddb) ([bool](../../d9/db9/classbool.html) abort=false)  
| Close or abort the transaction.
[More...](../../dd/d19/classApp_1_1AutoTransaction.html#a78f86284384fbf21e95706b6e5dd3ddb)  
  
|
[~AutoTransaction](../../dd/d19/classApp_1_1AutoTransaction.html#aaf43f5abb3673c1fb1b3d2aa610d5158)
()  
| Destructor.
[More...](../../dd/d19/classApp_1_1AutoTransaction.html#aaf43f5abb3673c1fb1b3d2aa610d5158)  
  
  
##  Static Public Member Functions  
  
---  
static void | [setEnable](../../dd/d19/classApp_1_1AutoTransaction.html#a239a24d16e7a12deecd08b102212a6d2) ([bool](../../d9/db9/classbool.html) enable)  
| Enable/Disable any
[AutoTransaction](../../dd/d19/classApp_1_1AutoTransaction.html "Helper class
to manager transaction \(i.e. undo/redo\)") instance in the current stack.
[More...](../../dd/d19/classApp_1_1AutoTransaction.html#a239a24d16e7a12deecd08b102212a6d2)  
  
  
## Detailed Description

Helper class to manager transaction (i.e. undo/redo)

## Constructor & Destructor Documentation

## ◆ AutoTransaction()

AutoTransaction::AutoTransaction  | ( | const char *  | _name_ = `nullptr`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _tmpName_ = `false`  
| ) | |   
  
Constructor.

Parameters

     name| optional new transaction name on construction   
---|---  
tmpName| if true and a new transaction is setup, the name given is considered
as temporary, and subsequent construction of this class (or calling
[Application::setActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a78fddfc24e060908e047c5472857c3ff
"Setup a pending application-wide active transaction.")) can override the
transaction name.  
  
The constructor increments an internal counter
(Application::_activeTransactionGuard). The counter prevents any new active
transaction being setup. It also prevents close (i.e. commits) the current
active transaction until it reaches zero. It does not have any effect on
aborting transaction, though.

References
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4).

## ◆ ~AutoTransaction()

AutoTransaction::~AutoTransaction  | ( | | ) |   
---|---|---|---|---  
  
Destructor.

This destructor decrease an internal counter
(Application::_activeTransactionGuard), and will commit any current active
transaction when the counter reaches zero.

References
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4).

## Member Function Documentation

## ◆ close()

void AutoTransaction::close  | ( | [bool](../../d9/db9/classbool.html) | _abort_ = `false`| ) |   
---|---|---|---|---|---  
  
Close or abort the transaction.

This function can be used to explicitly close (i.e. commit) the transaction,
if the current transaction ID matches the one created inside the constructor.
For aborting, it will abort any current transaction

References
[App::Application::closeActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a65f9fb03ff7053cfb14dd230451ae0a9),
and
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4).

Referenced by
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[femexamples.examplesgui.FemExamples::reject()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ade2cd979d737a9fa26b1e5f5ff8ebfcf),
and
[setEnable()](../../dd/d19/classApp_1_1AutoTransaction.html#a239a24d16e7a12deecd08b102212a6d2).

## ◆ setEnable()

| void AutoTransaction::setEnable  | ( | [bool](../../d9/db9/classbool.html) | _enable_| ) |   
---|---|---|---|---|---  
static  
  
Enable/Disable any
[AutoTransaction](../../dd/d19/classApp_1_1AutoTransaction.html "Helper class
to manager transaction \(i.e. undo/redo\)") instance in the current stack.

Once disabled, any empty temporary named transaction is closed. If there are
non-empty or non-temporary named active transaction, it will not be auto
closed.

This function may be used in, for example,
[Gui::Document::setEdit()](../../de/d4e/classGui_1_1Document.html#a2064c6eb4172240d40a7f409febc81a9
"set the ViewProvider in special edit mode") to allow a transaction live past
any command scope.

References
[close()](../../dd/d19/classApp_1_1AutoTransaction.html#a78f86284384fbf21e95706b6e5dd3ddb),
and
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4).

Referenced by
[Gui::TreeWidget::mouseDoubleClickEvent()](../../de/de0/classGui_1_1TreeWidget.html#aa3c3121b950b3f9b0d134710879cf820),
[App::Application::setActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a78fddfc24e060908e047c5472857c3ff),
[Gui::Document::setEdit()](../../de/d4e/classGui_1_1Document.html#a2064c6eb4172240d40a7f409febc81a9),
and
[Gui::ControlSingleton::showDialog()](../../d6/d65/classGui_1_1ControlSingleton.html#a0b47653e251fa9b636d6f0f04f557020).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/AutoTransaction.h
  * FreeCAD/src/App/AutoTransaction.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

