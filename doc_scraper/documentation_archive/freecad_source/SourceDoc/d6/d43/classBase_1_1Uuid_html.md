---
url: https://freecad.github.io/SourceDoc/d6/d43/classBase_1_1Uuid.html
scraped_at: 2025-09-08T15:17:53.232421
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Uuid](../../d6/d43/classBase_1_1Uuid.html)

[List of all members](../../d5/df9/classBase_1_1Uuid-members.html) | Public Member Functions | Static Public Member Functions

Base::Uuid Class Reference

Creates a [Uuid](../../d6/d43/classBase_1_1Uuid.html "Creates a Uuid.").
[More...](../../d6/d43/classBase_1_1Uuid.html#details)

`#include <Uuid.h>`

##  Public Member Functions  
  
---  
const std::string & | [getValue](../../d6/d43/classBase_1_1Uuid.html#a95e42ab3b423ce44ba132708f1def69f) () const  
[bool](../../d9/db9/classbool.html) | [operator<](../../d6/d43/classBase_1_1Uuid.html#a9449c9bf763b23a34b6be07444ace281) (const [Uuid](../../d6/d43/classBase_1_1Uuid.html) &other) const  
[Uuid](../../d6/d43/classBase_1_1Uuid.html) & | [operator=](../../d6/d43/classBase_1_1Uuid.html#a709fe253ae709644e63105d836213746) (const [Uuid](../../d6/d43/classBase_1_1Uuid.html) &)=default  
[bool](../../d9/db9/classbool.html) | [operator==](../../d6/d43/classBase_1_1Uuid.html#a8c0bcf34287fed779f667864fc957c57) (const [Uuid](../../d6/d43/classBase_1_1Uuid.html) &other) const  
void | [setValue](../../d6/d43/classBase_1_1Uuid.html#abbb79ec432410a0a814458fa8c6902f4) (const char *sString)  
void | [setValue](../../d6/d43/classBase_1_1Uuid.html#a27147703e808c79d636d96ac78067d07) (const std::string &sString)  
|
[Uuid](../../d6/d43/classBase_1_1Uuid.html#a55663b31db8d26c71fa1b0258ccc34f9)
()  
| Construction.
[More...](../../d6/d43/classBase_1_1Uuid.html#a55663b31db8d26c71fa1b0258ccc34f9)  
  
|
[Uuid](../../d6/d43/classBase_1_1Uuid.html#add26d057fd6e0d7317048baa5c1bc956)
(const [Uuid](../../d6/d43/classBase_1_1Uuid.html) &)=default  
virtual | [~Uuid](../../d6/d43/classBase_1_1Uuid.html#a60727110b70ec35c6d8b8d1f70629355) ()  
| Destruction.
[More...](../../d6/d43/classBase_1_1Uuid.html#a60727110b70ec35c6d8b8d1f70629355)  
  
  
##  Static Public Member Functions  
  
---  
static std::string | [createUuid](../../d6/d43/classBase_1_1Uuid.html#a4f0fb93733c226a06e1401083b6071ec) ()  
  
## Detailed Description

Creates a [Uuid](../../d6/d43/classBase_1_1Uuid.html "Creates a Uuid.").

Author

    Jürgen Riegel 

## Constructor & Destructor Documentation

## ◆ Uuid() [1/2]

Uuid::Uuid  | ( | | ) |   
---|---|---|---|---  
  
Construction.

A constructor.

A more elaborate description of the constructor.

References
[createUuid()](../../d6/d43/classBase_1_1Uuid.html#a4f0fb93733c226a06e1401083b6071ec).

Referenced by
[createUuid()](../../d6/d43/classBase_1_1Uuid.html#a4f0fb93733c226a06e1401083b6071ec).

## ◆ Uuid() [2/2]

| Base::Uuid::Uuid  | ( | const [Uuid](../../d6/d43/classBase_1_1Uuid.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## ◆ ~Uuid()

| Uuid::~Uuid  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Destruction.

A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ createUuid()

| std::string Uuid::createUuid  | ( | | ) |   
---|---|---|---|---  
static  
  
References
[Uuid()](../../d6/d43/classBase_1_1Uuid.html#a55663b31db8d26c71fa1b0258ccc34f9).

Referenced by
[App::Document::exportObjects()](../../d8/d3e/classApp_1_1Document.html#a7ebc166fbd54e4c0088cd06ad006e739),
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
[Sandbox::DocumentSaverThread::run()](../../d9/d1c/classSandbox_1_1DocumentSaverThread.html#a4eda162d7f2ad445c7e4ef89b8071ed6),
[App::Document::saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d),
and
[Uuid()](../../d6/d43/classBase_1_1Uuid.html#a55663b31db8d26c71fa1b0258ccc34f9).

## ◆ getValue()

const std::string & Uuid::getValue  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::PropertyFileIncluded::getUniqueFileName()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ac6b94c77254825a17621686c38efd006).

## ◆ operator<()

[bool](../../d9/db9/classbool.html) Base::Uuid::operator< | ( | const [Uuid](../../d6/d43/classBase_1_1Uuid.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator=()

| [Uuid](../../d6/d43/classBase_1_1Uuid.html) & Base::Uuid::operator=  | ( | const [Uuid](../../d6/d43/classBase_1_1Uuid.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## ◆ operator==()

[bool](../../d9/db9/classbool.html) Base::Uuid::operator==  | ( | const [Uuid](../../d6/d43/classBase_1_1Uuid.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
## ◆ setValue() [1/2]

void Uuid::setValue  | ( | const char *  | _sString_| ) |   
---|---|---|---|---|---  
  
Referenced by
[setValue()](../../d6/d43/classBase_1_1Uuid.html#a27147703e808c79d636d96ac78067d07).

## ◆ setValue() [2/2]

void Uuid::setValue  | ( | const std::string & | _sString_| ) |   
---|---|---|---|---|---  
  
References
[setValue()](../../d6/d43/classBase_1_1Uuid.html#abbb79ec432410a0a814458fa8c6902f4).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Uuid.h
  * FreeCAD/src/Base/Uuid.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

