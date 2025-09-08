---
url: https://freecad.github.io/SourceDoc/df/d3c/classApp_1_1TransactionLocker.html
scraped_at: 2025-09-08T14:57:13.093490
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [TransactionLocker](../../df/d3c/classApp_1_1TransactionLocker.html)

[List of all members](../../d9/db7/classApp_1_1TransactionLocker-members.html) | Public Member Functions | Static Public Member Functions | Friends

App::TransactionLocker Class Reference

Helper class to lock a transaction from being closed or aborted.
[More...](../../df/d3c/classApp_1_1TransactionLocker.html#details)

`#include <AutoTransaction.h>`

##  Public Member Functions  
  
---  
void | [activate](../../df/d3c/classApp_1_1TransactionLocker.html#a1f96608a8ad20ffb50de613395430113) ([bool](../../d9/db9/classbool.html) enable)  
| Activate or deactivate this locker.
[More...](../../df/d3c/classApp_1_1TransactionLocker.html#a1f96608a8ad20ffb50de613395430113)  
  
[bool](../../d9/db9/classbool.html) | [isActive](../../df/d3c/classApp_1_1TransactionLocker.html#a6332aaa074554c283b2ba8c96f5453e7) () const  
| Check if the locker is active.
[More...](../../df/d3c/classApp_1_1TransactionLocker.html#a6332aaa074554c283b2ba8c96f5453e7)  
  
|
[TransactionLocker](../../df/d3c/classApp_1_1TransactionLocker.html#a6e52de3f4e789250d18272a4fe316da5)
([bool](../../d9/db9/classbool.html) lock=true)  
| Constructor.
[More...](../../df/d3c/classApp_1_1TransactionLocker.html#a6e52de3f4e789250d18272a4fe316da5)  
  
|
[~TransactionLocker](../../df/d3c/classApp_1_1TransactionLocker.html#a6ba6c93b13bc2f0f9e824af4da387374)
()  
| Destructor Unlock the transaction is this locker is active.
[More...](../../df/d3c/classApp_1_1TransactionLocker.html#a6ba6c93b13bc2f0f9e824af4da387374)  
  
  
##  Static Public Member Functions  
  
---  
static [bool](../../d9/db9/classbool.html) | [isLocked](../../df/d3c/classApp_1_1TransactionLocker.html#a6405ee36ea75feca507db867ac1d5b19) ()  
| Check if transaction is being locked.
[More...](../../df/d3c/classApp_1_1TransactionLocker.html#a6405ee36ea75feca507db867ac1d5b19)  
  
  
##  Friends  
  
---  
class | [Application](../../df/d3c/classApp_1_1TransactionLocker.html#a23f25bcc02a0e94c2f5a4188496b04d0)  
  
## Detailed Description

Helper class to lock a transaction from being closed or aborted.

The helper class is used to protect some critical transaction from being
closed prematurely, e.g. when deleting some object.

## Constructor & Destructor Documentation

## ◆ TransactionLocker()

TransactionLocker::TransactionLocker  | ( | [bool](../../d9/db9/classbool.html) | _lock_ = `true`| ) |   
---|---|---|---|---|---  
  
Constructor.

Parameters

     lock| whether to activate the lock   
---|---  
  
## ◆ ~TransactionLocker()

TransactionLocker::~TransactionLocker  | ( | | ) |   
---|---|---|---|---  
  
Destructor Unlock the transaction is this locker is active.

References
[activate()](../../df/d3c/classApp_1_1TransactionLocker.html#a1f96608a8ad20ffb50de613395430113).

## Member Function Documentation

## ◆ activate()

void TransactionLocker::activate  | ( | [bool](../../d9/db9/classbool.html) | _enable_| ) |   
---|---|---|---|---|---  
  
Activate or deactivate this locker.

Parameters

     enable| whether to activate the locker  
---|---  
  
An internal counter is used to support recursive locker. When activated, the
current active transaction cannot be closed or aborted. But the closing call
([Application::closeActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a65f9fb03ff7053cfb14dd230451ae0a9
"Commit/abort current active transactions.")) will be remembered, and
performed when the internal lock counter reaches zero.

References
[App::Application::closeActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a65f9fb03ff7053cfb14dd230451ae0a9),
and
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4).

Referenced by
[ArchBuildingPart.ViewProviderBuildingPart::doubleClicked()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a8ff583320283dfcfde71ed048de5906f),
[draftviewproviders.view_layer.ViewProviderLayer::setupContextMenu()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#aa51cc2c02981cd9c075c182577d30b4f),
and
[~TransactionLocker()](../../df/d3c/classApp_1_1TransactionLocker.html#a6ba6c93b13bc2f0f9e824af4da387374).

## ◆ isActive()

[bool](../../d9/db9/classbool.html) App::TransactionLocker::isActive  | ( | | ) |  const  
---|---|---|---|---  
  
Check if the locker is active.

## ◆ isLocked()

| [bool](../../d9/db9/classbool.html) TransactionLocker::isLocked  | ( | | ) |   
---|---|---|---|---  
static  
  
Check if transaction is being locked.

## Friends And Related Function Documentation

## ◆ Application

| [friend](../../d7/d23/classfriend.html) class
[Application](../../da/dbf/classApp_1_1Application.html)  
---  
friend  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/AutoTransaction.h
  * FreeCAD/src/App/AutoTransaction.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

