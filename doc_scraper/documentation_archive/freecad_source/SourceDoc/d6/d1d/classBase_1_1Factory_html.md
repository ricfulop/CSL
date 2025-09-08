---
url: https://freecad.github.io/SourceDoc/d6/d1d/classBase_1_1Factory.html
scraped_at: 2025-09-08T15:16:08.779946
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Factory](../../d6/d1d/classBase_1_1Factory.html)

[List of all members](../../db/d07/classBase_1_1Factory-members.html) | Public Member Functions | Protected Member Functions

Base::Factory Class Reference

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all factories This class has the purpose to
produce at runtime instances of classes not known at compile time.
[More...](../../d6/d1d/classBase_1_1Factory.html#details)

`#include <Factory.h>`

##  Public Member Functions  
  
---  
void | [AddProducer](../../d6/d1d/classBase_1_1Factory.html#a33b1e2368929bda1a9342999f838d5fb) (const char *sClassName, [AbstractProducer](../../d8/dd4/classBase_1_1AbstractProducer.html) *pcProducer)  
| Adds a new prducer instance.
[More...](../../d6/d1d/classBase_1_1Factory.html#a33b1e2368929bda1a9342999f838d5fb)  
  
std::list< std::string > | [CanProduce](../../d6/d1d/classBase_1_1Factory.html#a6af06bc0c9b04e59895ed9ad5ce22a03) () const  
| returns a list of all registered producer
[More...](../../d6/d1d/classBase_1_1Factory.html#a6af06bc0c9b04e59895ed9ad5ce22a03)  
  
[bool](../../d9/db9/classbool.html) | [CanProduce](../../d6/d1d/classBase_1_1Factory.html#a4baaab61e852d8e4539a1038edc9b01f) (const char *sClassName) const  
| returns true if there is a producer for this class registered
[More...](../../d6/d1d/classBase_1_1Factory.html#a4baaab61e852d8e4539a1038edc9b01f)  
  
  
##  Protected Member Functions  
  
---  
|
[Factory](../../d6/d1d/classBase_1_1Factory.html#a9d626ac579a4cb45a40f04d652b71aed)
()  
| construction
[More...](../../d6/d1d/classBase_1_1Factory.html#a9d626ac579a4cb45a40f04d652b71aed)  
  
void * | [Produce](../../d6/d1d/classBase_1_1Factory.html#ab74aa0c7391041ca5f033f747283ab29) (const char *sClassName) const  
| produce a class with the given name
[More...](../../d6/d1d/classBase_1_1Factory.html#ab74aa0c7391041ca5f033f747283ab29)  
  
virtual | [~Factory](../../d6/d1d/classBase_1_1Factory.html#a8f71456f48e4df402c778a44191ff40e) ()  
| destruction
[More...](../../d6/d1d/classBase_1_1Factory.html#a8f71456f48e4df402c778a44191ff40e)  
  
  
## Detailed Description

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all factories This class has the purpose to
produce at runtime instances of classes not known at compile time.

It holds a map of so called producers which are able to produce an instance of
a special class. Producer can be registered at runtime through e.g.
application modules

## Constructor & Destructor Documentation

## ◆ Factory()

| Base::Factory::Factory  | ( | | ) |   
---|---|---|---|---  
protected  
  
construction

## ◆ ~Factory()

| Factory::~Factory  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
destruction

## Member Function Documentation

## ◆ AddProducer()

void Factory::AddProducer  | ( | const char *  | _sClassName_ ,   
---|---|---|---  
|  | [AbstractProducer](../../d8/dd4/classBase_1_1AbstractProducer.html) *  | _pcProducer_  
| ) | |   
  
Adds a new prducer instance.

Referenced by [Gui::CustomPageProducer< CLASS
>::CustomPageProducer()](../../d8/d2e/classGui_1_1CustomPageProducer.html#a2672313d106a75876e4cf4c48d8df9cd),
[Base::ExceptionProducer< CLASS
>::ExceptionProducer()](../../de/d9d/classBase_1_1ExceptionProducer.html#afdb2661e5f5dac69ecde2a40321997c9),
[Gui::PrefPageProducer< CLASS
>::PrefPageProducer()](../../d2/d48/classGui_1_1PrefPageProducer.html#a4a3b71509ff3603c96d1ac39b9c1c253),
[Gui::PrefPagePyProducer::PrefPagePyProducer()](../../d9/dcf/classGui_1_1PrefPagePyProducer.html#a29595c77dd4cf83a352326c030ace0bf),
[Gui::PrefPageUiProducer::PrefPageUiProducer()](../../d7/d56/classGui_1_1PrefPageUiProducer.html#adfe3b80787a4f5139181f2d83a70d454),
[Gui::PropertyEditor::PropertyItemProducer< CLASS
>::PropertyItemProducer()](../../df/d33/classGui_1_1PropertyEditor_1_1PropertyItemProducer.html#a05c4b3d717c2b6df202a38096e201ac4),
[Base::ScriptProducer::ScriptProducer()](../../d8/de0/classBase_1_1ScriptProducer.html#a73596515fbc1fd6c98cfd9f908ca05c6),
and [Gui::WidgetProducer< CLASS
>::WidgetProducer()](../../d9/db1/classGui_1_1WidgetProducer.html#a3bc662daed07d458e73ac9b007067192).

## ◆ CanProduce() [1/2]

std::list< std::string > Factory::CanProduce  | ( | | ) |  const  
---|---|---|---|---  
  
returns a list of all registered producer

## ◆ CanProduce() [2/2]

[bool](../../d9/db9/classbool.html) Factory::CanProduce  | ( | const char *  | _sClassName_| ) |  const  
---|---|---|---|---|---  
  
returns true if there is a producer for this class registered

## ◆ Produce()

| void * Factory::Produce  | ( | const char *  | _sClassName_| ) |  const  
---|---|---|---|---|---  
protected  
  
produce a class with the given name

Referenced by
[Gui::WidgetFactoryInst::createPreferencePage()](../../d5/d83/classGui_1_1WidgetFactoryInst.html#a3cc9e4ee3575cfdf3398d3b7150190a4),
[Gui::PropertyEditor::PropertyItemFactory::createPropertyItem()](../../dc/d1b/classGui_1_1PropertyEditor_1_1PropertyItemFactory.html#aed6c3b86369cce666592b4c8a6464004),
[Gui::WidgetFactoryInst::createWidget()](../../d5/d83/classGui_1_1WidgetFactoryInst.html#a8a166efde23cd16fb19b84de63abf3b3),
[Gui::WorkbenchFactoryInst::createWorkbench()](../../d7/d35/classGui_1_1WorkbenchFactoryInst.html#a41f4d7a2ae03ed7057b1217b643117a2),
and
[Base::ScriptFactorySingleton::ProduceScript()](../../d3/dba/classBase_1_1ScriptFactorySingleton.html#a2e1d1349ea431e05c7c5c95c20e17e07).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Factory.h
  * FreeCAD/src/Base/Factory.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

