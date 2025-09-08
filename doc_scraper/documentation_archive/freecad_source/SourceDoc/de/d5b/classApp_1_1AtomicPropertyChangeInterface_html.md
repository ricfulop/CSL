---
url: https://freecad.github.io/SourceDoc/de/d5b/classApp_1_1AtomicPropertyChangeInterface.html
scraped_at: 2025-09-08T14:53:44.226397
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)

[List of all members](../../de/dc0/classApp_1_1AtomicPropertyChangeInterface-members.html) | Classes | Protected Member Functions | Protected Attributes

App::AtomicPropertyChangeInterface< P > Class Template Reference

A template class that is used to inhibit multiple nested calls to
aboutToSetValue/hasSetValue for properties.
[More...](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#details)

`#include <Property.h>`

##  Classes  
  
---  
class | [AtomicPropertyChange](../../d6/d47/classApp_1_1AtomicPropertyChangeInterface_1_1AtomicPropertyChange.html)  
  
##  Protected Member Functions  
  
---  
|
[AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#aab004d1fbf131c11d570dcfcad7c22e1)
()  
  
##  Protected Attributes  
  
---  
[bool](../../d9/db9/classbool.html) | [hasChanged](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a1e6d78782f81aef5d1efe58ac219e2df)  
[int](../../d1/da0/classint.html) | [signalCounter](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a07e13a81f4f601365b04cc8806d075f9)  
| Counter for invoking transaction start/stop.
[More...](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html#a07e13a81f4f601365b04cc8806d075f9)  
  
  
## Detailed Description

template<class P>  
class App::AtomicPropertyChangeInterface< P >

A template class that is used to inhibit multiple nested calls to
aboutToSetValue/hasSetValue for properties.

A template class that is used to inhibit multiple nested calls to
aboutToSetValue/hasSetValue for properties, and only invoke it on change and
last time it is needed. This is useful in cases where you want to change
multiple values in a property "atomically", using possibly multiple primitive
functions that normally would trigger aboutToSetValue/hasSetValue calls on
their own.

To use, inherit privately from the
[AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html
"A template class that is used to inhibit multiple nested calls to
aboutToSetValue/hasSetValue for pro...") class, using your class name as the
template argument. In all cases where you normally would call
aboutToSetValue/hasSetValue before and after a change, create an
[AtomicPropertyChange](../../d6/d47/classApp_1_1AtomicPropertyChangeInterface_1_1AtomicPropertyChange.html)
object. The default constructor assume you are about to change the property
and will call property's aboutToSetValue() if the property has not been marked
as changed before by any other
[AtomicPropertyChange](../../d6/d47/classApp_1_1AtomicPropertyChangeInterface_1_1AtomicPropertyChange.html)
instances in current call stack. You can pass 'false' as the a second argument
to the constructor, and manually call
[AtomicPropertyChange::aboutToChange()](../../d6/d47/classApp_1_1AtomicPropertyChangeInterface_1_1AtomicPropertyChange.html#a06550212fd1676db805f5fb07550c2cc
"Mark the property as changed.") before actual change, this enables you to
prevent unnecessary property copy for undo/redo where there is actual changes.
[AtomicPropertyChange](../../d6/d47/classApp_1_1AtomicPropertyChangeInterface_1_1AtomicPropertyChange.html)
will guaranetee calling hasSetValue() when the last instance in the current
call stack is destroyed.

One thing to take note is that, because C++ does not allow throwing exception
in destructor, any exception thrown when calling property's hasSetValue() will
be caught and swallowed. To allow exception propagation, you can manually call
[AtomicPropertyChange::tryInvoke()](../../d6/d47/classApp_1_1AtomicPropertyChangeInterface_1_1AtomicPropertyChange.html#aea1f8110dc9360b614cf110f210bd1c5
"Check and invoke property's hasSetValue\(\)"). If the condition is satisfied,
it will call hasSetValue() that allows exception propagation.

## Constructor & Destructor Documentation

## ◆ AtomicPropertyChangeInterface()

template<class P >

| [App::AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)< P >::AtomicPropertyChangeInterface  | ( | | ) |   
---|---|---|---|---  
protected  
  
## Member Data Documentation

## ◆ hasChanged

template<class P >

| [bool](../../d9/db9/classbool.html)
[App::AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)<
P >::hasChanged  
---  
protected  
  
## ◆ signalCounter

template<class P >

| [int](../../d1/da0/classint.html)
[App::AtomicPropertyChangeInterface](../../de/d5b/classApp_1_1AtomicPropertyChangeInterface.html)<
P >::signalCounter  
---  
protected  
  
Counter for invoking transaction start/stop.

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/Property.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

