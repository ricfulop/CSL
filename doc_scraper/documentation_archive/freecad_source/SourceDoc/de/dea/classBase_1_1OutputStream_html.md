---
url: https://freecad.github.io/SourceDoc/de/dea/classBase_1_1OutputStream.html
scraped_at: 2025-09-08T15:16:45.959175
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [OutputStream](../../de/dea/classBase_1_1OutputStream.html)

[List of all members](../../da/d60/classBase_1_1OutputStream-members.html) | Public Member Functions

Base::OutputStream Class Reference

The [OutputStream](../../de/dea/classBase_1_1OutputStream.html "The
OutputStream class provides writing of binary data to an ostream.") class
provides writing of binary data to an ostream.
[More...](../../de/dea/classBase_1_1OutputStream.html#details)

`#include <Stream.h>`

##  Public Member Functions  
  
---  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#afada7e209b4209379e968744d0038ecb) ([bool](../../d9/db9/classbool.html) b)  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#ae39b3cbf872a51486b743a79247d594e) (double d)  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#af222b70c07b9111b0351f7a638af113a) (float f)  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#a5e5a285acd0028442a14ae776a317de5) (int16_t s)  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#a9653555721879901f92ee559bca422c1) (int32_t i)  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#a370fb1f345080d9edcf6f2444cea5aee) (int64_t l)  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#a401d4b6ac54b30899e55cc4329e4657b) (int8_t ch)  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#aaeb5e2e910ef4d2656bb64172df74a48) (uint16_t us)  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#a77467d946d5c7717e8a34fade1989c6f) (uint32_t ui)  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#af4a50989cf3e3808be15db4021f70b2f) (uint64_t ul)  
[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & | [operator<<](../../de/dea/classBase_1_1OutputStream.html#a1459681fc18ba2ffcc48c20ef1355f0e) (uint8_t uch)  
|
[OutputStream](../../de/dea/classBase_1_1OutputStream.html#af0d3a380190d487d1b1d8113ac563f5d)
(std::ostream &rout)  
|
[~OutputStream](../../de/dea/classBase_1_1OutputStream.html#a0e63481676582adb93cae5970d16d37a)
()  
![-](../../closed.png) Public Member Functions inherited from
[Base::Stream](../../dd/d4f/classBase_1_1Stream.html)  
[ByteOrder](../../dd/d4f/classBase_1_1Stream.html#a8f120f4ab7c73f2d80f21a2be7a0f3f7) | [byteOrder](../../dd/d4f/classBase_1_1Stream.html#ae5a156858b79be7d9fdbf7e2dcd2afbc) () const  
void | [setByteOrder](../../dd/d4f/classBase_1_1Stream.html#a39b0baf7bb4637238d0fd70959329310) ([ByteOrder](../../dd/d4f/classBase_1_1Stream.html#a8f120f4ab7c73f2d80f21a2be7a0f3f7))  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Types inherited from
[Base::Stream](../../dd/d4f/classBase_1_1Stream.html)  
enum | [ByteOrder](../../dd/d4f/classBase_1_1Stream.html#a8f120f4ab7c73f2d80f21a2be7a0f3f7) { [BigEndian](../../dd/d4f/classBase_1_1Stream.html#a8f120f4ab7c73f2d80f21a2be7a0f3f7a0b23650462729513c459e1f39ec1b9b5) , [LittleEndian](../../dd/d4f/classBase_1_1Stream.html#a8f120f4ab7c73f2d80f21a2be7a0f3f7aad5fc931f0fd074ef8e0f873de46652c) }  
![-](../../closed.png) Protected Member Functions inherited from
[Base::Stream](../../dd/d4f/classBase_1_1Stream.html)  
[Stream](../../dd/d4f/classBase_1_1Stream.html) & | [operator=](../../dd/d4f/classBase_1_1Stream.html#a65c52ef9cc45a39c8639f36d4204e43a) (const [Stream](../../dd/d4f/classBase_1_1Stream.html) &)=default  
|
[Stream](../../dd/d4f/classBase_1_1Stream.html#a8c3f05bd00361ec92627fa41f330a39b)
()  
|
[Stream](../../dd/d4f/classBase_1_1Stream.html#a8606c2c505356cc614c404db4a466d13)
(const [Stream](../../dd/d4f/classBase_1_1Stream.html) &)=default  
virtual | [~Stream](../../dd/d4f/classBase_1_1Stream.html#a6dc4517a9e6a87abb662fcd14c2ea969) ()  
  
## Detailed Description

The [OutputStream](../../de/dea/classBase_1_1OutputStream.html "The
OutputStream class provides writing of binary data to an ostream.") class
provides writing of binary data to an ostream.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ OutputStream()

OutputStream::OutputStream  | ( | std::ostream & | _rout_| ) |   
---|---|---|---|---|---  
  
## ◆ ~OutputStream()

OutputStream::~OutputStream  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ operator<<() [1/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | [bool](../../d9/db9/classbool.html) | _b_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<<() [2/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | double  | _d_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<<() [3/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | float  | _f_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<<() [4/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | int16_t  | _s_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<<() [5/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | int32_t  | _i_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<<() [6/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | int64_t  | _l_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<<() [7/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | int8_t  | _ch_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<<() [8/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | uint16_t  | _us_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<<() [9/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | uint32_t  | _ui_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<<() [10/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | uint64_t  | _ul_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<<() [11/11]

[OutputStream](../../de/dea/classBase_1_1OutputStream.html) & OutputStream::operator<< | ( | uint8_t  | _uch_| ) |   
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Stream.h
  * FreeCAD/src/Base/Stream.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

