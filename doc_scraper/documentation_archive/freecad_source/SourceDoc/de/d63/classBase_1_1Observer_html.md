---
url: https://freecad.github.io/SourceDoc/de/d63/classBase_1_1Observer.html
scraped_at: 2025-09-08T15:16:42.934178
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Observer](../../de/d63/classBase_1_1Observer.html)

[List of all members](../../db/d4f/classBase_1_1Observer-members.html) | Public Member Functions

Base::Observer< _MessageType > Class Template Referenceabstract

[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") class
Implementation of the well known
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") Design Pattern.
[More...](../../de/d63/classBase_1_1Observer.html#details)

`#include <Observer.h>`

##  Public Member Functions  
  
---  
virtual const char * | [Name](../../de/d63/classBase_1_1Observer.html#a91856837576fad34aeeb7456186b5d63) ()  
| This method can be reimplemented from the concrete
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") and returns the
name of the observer.
[More...](../../de/d63/classBase_1_1Observer.html#a91856837576fad34aeeb7456186b5d63)  
  
|
[Observer](../../de/d63/classBase_1_1Observer.html#aeff9fea6e16ab74509eac95828d56155)
()  
| A constructor.
[More...](../../de/d63/classBase_1_1Observer.html#aeff9fea6e16ab74509eac95828d56155)  
  
virtual void | [OnChange](../../de/d63/classBase_1_1Observer.html#ae3957e8309e28871cb7eaeffa17f9fe5) ([Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType > &rCaller, _MessageType rcReason)=0  
| This method need to be reimplemented from the concrete
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") and get called by
the observed class.
[More...](../../de/d63/classBase_1_1Observer.html#ae3957e8309e28871cb7eaeffa17f9fe5)  
  
virtual void | [OnDestroy](../../de/d63/classBase_1_1Observer.html#a153ae9277f140fed5512bcf4d651e636) ([Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType > &rCaller)  
| This method need to be reimplemented from the concrete
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") and get called by
the observed class.
[More...](../../de/d63/classBase_1_1Observer.html#a153ae9277f140fed5512bcf4d651e636)  
  
virtual | [~Observer](../../de/d63/classBase_1_1Observer.html#a3ec67159e4e3fc374885c932bc04dca2) ()  
| A destructor.
[More...](../../de/d63/classBase_1_1Observer.html#a3ec67159e4e3fc374885c932bc04dca2)  
  
  
## Detailed Description

template<class _MessageType>  
class Base::Observer< _MessageType >

[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") class
Implementation of the well known
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") Design Pattern.

The observed object, which inherit FCSubject, will call all its observers in
case of changes. A observer class has to Attach itself to the observed object.

See also

    FCSubject 

## Constructor & Destructor Documentation

## ◆ Observer()

template<class _MessageType >

[Base::Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType >::Observer  | ( | | ) |   
---|---|---|---|---  
  
A constructor.

No special function so far.

## ◆ ~Observer()

template<class _MessageType >

| virtual [Base::Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType >::~[Observer](../../de/d63/classBase_1_1Observer.html) | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

No special function so far.

## Member Function Documentation

## ◆ Name()

template<class _MessageType >

| virtual const char * [Base::Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType >::Name  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
This method can be reimplemented from the concrete
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") and returns the
name of the observer.

Needed to use the Get Method of the
[Subject](../../dd/d73/classBase_1_1Subject.html "Subject class Implementation
of the well known Observer Design Pattern.").

## ◆ OnChange()

template<class _MessageType >

| virtual void [Base::Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType >::OnChange  | ( | [Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType > & | _rCaller_ ,   
---|---|---|---  
|  | _MessageType  | _rcReason_  
| ) | |   
pure virtual  
  
This method need to be reimplemented from the concrete
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") and get called by
the observed class.

Parameters

     rCaller| a reference to the calling object   
---|---  
rcReason|  
  
Implemented in
[Gui::StatefulLabel](../../d8/d55/classGui_1_1StatefulLabel.html#abf2f7b1157e77636b026eae9f8384812),
[Gui::MacroManager](../../d8/dc6/classGui_1_1MacroManager.html#a7ac03f5529cff75758145de021039518),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#ab4676168c268d47ee7bf819a203c04a9),
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#adaf6c5b0aa42268c9f3ea2a5d5ab2065),
and
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#af99e45be3638b3271bcfc96f84d68481).

## ◆ OnDestroy()

template<class _MessageType >

| virtual void [Base::Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType >::OnDestroy  | ( | [Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType > & | _rCaller_| ) |   
---|---|---|---|---|---  
virtual  
  
This method need to be reimplemented from the concrete
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") and get called by
the observed class.

Parameters

     rCaller| a reference to the calling object   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Base/Observer.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

