---
url: https://freecad.github.io/SourceDoc/d1/d31/classBase_1_1ClassTemplate.html
scraped_at: 2025-09-08T15:15:50.739195
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [ClassTemplate](../../d1/d31/classBase_1_1ClassTemplate.html)

[List of all members](../../dd/da9/classBase_1_1ClassTemplate-members.html) | Public Types | Public Member Functions | Public Attributes

Base::ClassTemplate Class Referenceabstract

A test class. [More...](../../d1/d31/classBase_1_1ClassTemplate.html#details)

`#include <FileTemplate.h>`

##  Public Types  
  
---  
enum | [TEnum](../../d1/d31/classBase_1_1ClassTemplate.html#a3e19a98814bf4bb167661cdb8e3df154) { [TVal1](../../d1/d31/classBase_1_1ClassTemplate.html#a3e19a98814bf4bb167661cdb8e3df154a0e96e3b9d184da5c07495dde0cbe2119) , [TVal2](../../d1/d31/classBase_1_1ClassTemplate.html#a3e19a98814bf4bb167661cdb8e3df154a77fc81ebdad6e1372e702e7b80caa7d8) , [TVal3](../../d1/d31/classBase_1_1ClassTemplate.html#a3e19a98814bf4bb167661cdb8e3df154a737e899d71110582372e9c2e511f0f32) }  
| An enum.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#a3e19a98814bf4bb167661cdb8e3df154)  
  
  
##  Public Member Functions  
  
---  
|
[ClassTemplate](../../d1/d31/classBase_1_1ClassTemplate.html#adfe87f94a240d35f2e8b3798cf4459a8)
()  
| Construction.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#adfe87f94a240d35f2e8b3798cf4459a8)  
  
[int](../../d1/da0/classint.html) | [testMe](../../d1/d31/classBase_1_1ClassTemplate.html#a9d34342af286674450db35978b6ba81a) ([int](../../d1/da0/classint.html) a, const char *s)  
| a normal member taking two arguments and returning an integer value.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#a9d34342af286674450db35978b6ba81a)  
  
virtual void | [testMeToo](../../d1/d31/classBase_1_1ClassTemplate.html#afcac4f1499a1d278797aafc82ba55303) (char c1, char c2)=0  
| A pure virtual member.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#afcac4f1499a1d278797aafc82ba55303)  
  
virtual | [~ClassTemplate](../../d1/d31/classBase_1_1ClassTemplate.html#ab41a43cb1673c0c1e06c911b85f17651) ()  
| Destruction.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#ab41a43cb1673c0c1e06c911b85f17651)  
  
  
##  Public Attributes  
  
---  
enum [Base::ClassTemplate::TEnum](../../d1/d31/classBase_1_1ClassTemplate.html#a3e19a98814bf4bb167661cdb8e3df154) * | [enumPtr](../../d1/d31/classBase_1_1ClassTemplate.html#a78f4f9ad0dea4251c451a49abc850603)  
| enum pointer.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#a78f4f9ad0dea4251c451a49abc850603)  
  
enum [Base::ClassTemplate::TEnum](../../d1/d31/classBase_1_1ClassTemplate.html#a3e19a98814bf4bb167661cdb8e3df154) | [enumVar](../../d1/d31/classBase_1_1ClassTemplate.html#a9081b3b0bfa2ecbd3a9c47da6e76b24b)  
| enum variable.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#a9081b3b0bfa2ecbd3a9c47da6e76b24b)  
  
  
## a group of methods  
  
---  
[int](../../d1/da0/classint.html) | [publicVar](../../d1/d31/classBase_1_1ClassTemplate.html#a6fdf31e09717a9c0cd96a35938bc5bfe)  
| a public variable.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#a6fdf31e09717a9c0cd96a35938bc5bfe)  
  
[int](../../d1/da0/classint.html)(* | [handler](../../d1/d31/classBase_1_1ClassTemplate.html#a76401a8af5ab3991ebc11c1c7465a63d) )([int](../../d1/da0/classint.html) a, [int](../../d1/da0/classint.html) b)  
| a function variable.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#a76401a8af5ab3991ebc11c1c7465a63d)  
  
std::string | [something](../../d1/d31/classBase_1_1ClassTemplate.html#a119b561e787e73bbef64dbd1734a6b50)  
virtual void | [one](../../d1/d31/classBase_1_1ClassTemplate.html#a35a2d7836e9b4a7777306abdee907126) ()=0  
| I am method one.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#a35a2d7836e9b4a7777306abdee907126)  
  
virtual void | [two](../../d1/d31/classBase_1_1ClassTemplate.html#a8c4a1141086f447a9023c92b80c597bb) ()=0  
| I am method two.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#a8c4a1141086f447a9023c92b80c597bb)  
  
virtual void | [three](../../d1/d31/classBase_1_1ClassTemplate.html#aa1b7c9ed984320617f01901c5b5caa0a) ()=0  
| I am method three.
[More...](../../d1/d31/classBase_1_1ClassTemplate.html#aa1b7c9ed984320617f01901c5b5caa0a)  
  
  
## Detailed Description

A test class.

A more elaborate class description. Detailed description with some formatting:

    bla blablablablablablabl: 

#include <Base/Console.h>

[Base::Console](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729
"Access to the Console This method is used to gain access to the one and only
instance of the
ConsoleS...")().[Log](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964
"Prints a log Message.")("Stage: %d",i);

    another blablablablablablablablablabl: Text before the list

  * list item 1
    * sub item 1
      * sub sub item 1
      * sub sub item 2
The dot above ends the sub sub item list. More text for the first sub item

The dot above ends the first sub item. More text for the first list item

    * sub item 2
    * sub item 3
  * list item 2

More text in the same paragraph.

More text in a new paragraph. Also with HTML tags:

  * mouse events 
    1. mouse move event 
    2. mouse click event More info about the click event. 
    3. mouse double click event 
  * keyboard events 
    1. key down event 
    2. key up event 

More text here.

Author

    YOUR NAME 

## Member Enumeration Documentation

## ◆ TEnum

enum
[Base::ClassTemplate::TEnum](../../d1/d31/classBase_1_1ClassTemplate.html#a3e19a98814bf4bb167661cdb8e3df154)  
---  
  
An enum.

More detailed enum description.

Enumerator  
---  
TVal1 | enum value TVal1.   
TVal2 | enum value TVal2.   
TVal3 | enum value TVal3.   
  
## Constructor & Destructor Documentation

## ◆ ClassTemplate()

ClassTemplate::ClassTemplate  | ( | | ) |   
---|---|---|---|---  
  
Construction.

A constructor.

A more elaborate description of the constructor.

## ◆ ~ClassTemplate()

| ClassTemplate::~ClassTemplate  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Destruction.

A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ one()

| virtual void Base::ClassTemplate::one  | ( | | ) |   
---|---|---|---|---  
pure virtual  
  
I am method one.

## ◆ testMe()

[int](../../d1/da0/classint.html) ClassTemplate::testMe  | ( | [int](../../d1/da0/classint.html) | _a_ ,   
---|---|---|---  
|  | const char *  | _s_  
| ) | |   
  
a normal member taking two arguments and returning an integer value.

    You can use a printf like interface like: 

GetConsole().Warning("Some defects in %s, loading
anyway\n",[str](../../d9/d36/classstr.html));

Parameters

     a| an integer argument.   
---|---  
s| a constant character pointer.  
  
See also

    [ClassTemplate()](../../d1/d31/classBase_1_1ClassTemplate.html#adfe87f94a240d35f2e8b3798cf4459a8 "Construction.")
     [~ClassTemplate()](../../d1/d31/classBase_1_1ClassTemplate.html#ab41a43cb1673c0c1e06c911b85f17651 "Destruction.")
     [testMeToo()](../../d1/d31/classBase_1_1ClassTemplate.html#afcac4f1499a1d278797aafc82ba55303 "A pure virtual member.")
     [publicVar()](../../d1/d31/classBase_1_1ClassTemplate.html#a6fdf31e09717a9c0cd96a35938bc5bfe "a public variable.")

Returns

    The test results 

## ◆ testMeToo()

| virtual void Base::ClassTemplate::testMeToo  | ( | char  | _c1_ ,   
---|---|---|---  
|  | char  | _c2_  
| ) | |   
pure virtual  
  
A pure virtual member.

See also

    [testMe()](../../d1/d31/classBase_1_1ClassTemplate.html#a9d34342af286674450db35978b6ba81a "a normal member taking two arguments and returning an integer value.")

Parameters

     c1| the first argument.   
---|---  
c2| the second argument.  
  
## ◆ three()

| virtual void Base::ClassTemplate::three  | ( | | ) |   
---|---|---|---|---  
pure virtual  
  
I am method three.

## ◆ two()

| virtual void Base::ClassTemplate::two  | ( | | ) |   
---|---|---|---|---  
pure virtual  
  
I am method two.

## Member Data Documentation

## ◆ enumPtr

enum
[Base::ClassTemplate::TEnum](../../d1/d31/classBase_1_1ClassTemplate.html#a3e19a98814bf4bb167661cdb8e3df154)
* Base::ClassTemplate::enumPtr  
---  
  
enum pointer.

Details.

## ◆ enumVar

enum
[Base::ClassTemplate::TEnum](../../d1/d31/classBase_1_1ClassTemplate.html#a3e19a98814bf4bb167661cdb8e3df154)
Base::ClassTemplate::enumVar  
---  
  
enum variable.

Details.

## ◆ handler

[int](../../d1/da0/classint.html)(* Base::ClassTemplate::handler)
([int](../../d1/da0/classint.html) a, [int](../../d1/da0/classint.html) b)  
---  
  
a function variable.

Details.

## ◆ publicVar

[int](../../d1/da0/classint.html) Base::ClassTemplate::publicVar  
---  
  
a public variable.

Details.

## ◆ something

std::string Base::ClassTemplate::something  
---  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/FileTemplate.h
  * FreeCAD/src/Base/FileTemplate.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

