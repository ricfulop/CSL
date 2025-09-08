---
url: https://freecad.github.io/SourceDoc/df/d42/classApp_1_1DocumentObjectObserver.html
scraped_at: 2025-09-08T14:54:22.382749
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocumentObjectObserver](../../df/d42/classApp_1_1DocumentObjectObserver.html)

[List of all members](../../d6/da3/classApp_1_1DocumentObjectObserver-members.html) | Public Types | Public Member Functions

App::DocumentObjectObserver Class Reference

The
[DocumentObjectObserver](../../df/d42/classApp_1_1DocumentObjectObserver.html
"The DocumentObjectObserver class checks for a list of objects which of them
get removed.") class checks for a list of objects which of them get removed.
[More...](../../df/d42/classApp_1_1DocumentObjectObserver.html#details)

`#include <DocumentObserver.h>`

##  Public Types  
  
---  
typedef std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * >::const_iterator | [const_iterator](../../df/d42/classApp_1_1DocumentObjectObserver.html#a3719eda393774b5bbd78d029f5216a6a)  
  
##  Public Member Functions  
  
---  
void | [addToObservation](../../df/d42/classApp_1_1DocumentObjectObserver.html#ae030863c85a1ab9bec50678b6610aaf7) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
[const_iterator](../../df/d42/classApp_1_1DocumentObjectObserver.html#a3719eda393774b5bbd78d029f5216a6a) | [begin](../../df/d42/classApp_1_1DocumentObjectObserver.html#a4c71d98502bf5891dab4c290d4bafe5b) () const  
|
[DocumentObjectObserver](../../df/d42/classApp_1_1DocumentObjectObserver.html#a827c156616819dedaf1e0a6b19d017f7)
()  
| Constructor.
[More...](../../df/d42/classApp_1_1DocumentObjectObserver.html#a827c156616819dedaf1e0a6b19d017f7)  
  
[const_iterator](../../df/d42/classApp_1_1DocumentObjectObserver.html#a3719eda393774b5bbd78d029f5216a6a) | [end](../../df/d42/classApp_1_1DocumentObjectObserver.html#a7d295f7a5f653e1e64e7d14aa0fa2dbd) () const  
void | [removeFromObservation](../../df/d42/classApp_1_1DocumentObjectObserver.html#a6f8ea76cdee57ccdc8c2460108cfd5f0) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
virtual | [~DocumentObjectObserver](../../df/d42/classApp_1_1DocumentObjectObserver.html#a29550748ffba8d42b8bd4a44e0608bba) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html)  
void | [attachDocument](../../d5/d52/classApp_1_1DocumentObserver.html#a7b62ebc00f12f189dd1338cbd9817ac1) ([Document](../../d8/d3e/classApp_1_1Document.html) *)  
| Attaches to another document, the old document is not longer observed then.
[More...](../../d5/d52/classApp_1_1DocumentObserver.html#a7b62ebc00f12f189dd1338cbd9817ac1)  
  
void | [detachDocument](../../d5/d52/classApp_1_1DocumentObserver.html#a47fa57aec4571b9e8e844bcc56962546) ()  
| Detaches from the current document, the document is not longer observed
then.
[More...](../../d5/d52/classApp_1_1DocumentObserver.html#a47fa57aec4571b9e8e844bcc56962546)  
  
|
[DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html#a413aef62f11ee673feff12fb7968cd71)
()  
| Constructor.
[More...](../../d5/d52/classApp_1_1DocumentObserver.html#a413aef62f11ee673feff12fb7968cd71)  
  
|
[DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html#aede80a503f96172d392f86ab3047a4da)
([Document](../../d8/d3e/classApp_1_1Document.html) *)  
virtual | [~DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html#ae777e9e5f17925e2740c3d126336c6ff) ()  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Protected Member Functions inherited from
[App::DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html)  
[Document](../../d8/d3e/classApp_1_1Document.html) * | [getDocument](../../d5/d52/classApp_1_1DocumentObserver.html#adda884e1c97f6d107ce0723a4ad6316c) () const  
  
## Detailed Description

The
[DocumentObjectObserver](../../df/d42/classApp_1_1DocumentObjectObserver.html
"The DocumentObjectObserver class checks for a list of objects which of them
get removed.") class checks for a list of objects which of them get removed.

Author

    Werner Mayer 

## Member Typedef Documentation

## ◆ const_iterator

typedef
std::set<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>::const_iterator
[App::DocumentObjectObserver::const_iterator](../../df/d42/classApp_1_1DocumentObjectObserver.html#a3719eda393774b5bbd78d029f5216a6a)  
---  
  
## Constructor & Destructor Documentation

## ◆ DocumentObjectObserver()

DocumentObjectObserver::DocumentObjectObserver  | ( | | ) |   
---|---|---|---|---  
  
Constructor.

## ◆ ~DocumentObjectObserver()

| DocumentObjectObserver::~DocumentObjectObserver  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ addToObservation()

void DocumentObjectObserver::addToObservation  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
## ◆ begin()

[DocumentObjectObserver::const_iterator](../../df/d42/classApp_1_1DocumentObjectObserver.html#a3719eda393774b5bbd78d029f5216a6a) DocumentObjectObserver::begin  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ end()

[DocumentObjectObserver::const_iterator](../../df/d42/classApp_1_1DocumentObjectObserver.html#a3719eda393774b5bbd78d029f5216a6a) DocumentObjectObserver::end  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Dice3DS.dom3ds.FileLikeBuffer::advance()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#a8e06865a859e1dbb164c3b03d4065553),
[Dice3DS.dom3ds.FileLikeBuffer::read_rest()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#a9d6c356ba5bfee8c51fa348f902c3852),
[Dice3DS.dom3ds.FileLikeBuffer::read_to_nul()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#a51bc6a89a08cde8df68b553656931ee4),
[Dice3DS.dom3ds.FileLikeBuffer::room_for_chunks()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#ab01563eb0dff95345b47c98a398ab33f),
and
[Dice3DS.dom3ds.FileLikeBuffer::seek()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#a14ec480a1bd8005ee16364c883d63d8b).

## ◆ removeFromObservation()

void DocumentObjectObserver::removeFromObservation  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/DocumentObserver.h
  * FreeCAD/src/App/DocumentObserver.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

