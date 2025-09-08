---
url: https://freecad.github.io/SourceDoc/dd/d72/classBase_1_1InputStream.html
scraped_at: 2025-09-08T15:16:28.958109
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [InputStream](../../dd/d72/classBase_1_1InputStream.html)

[List of all members](../../dc/d40/classBase_1_1InputStream-members.html) | Public Member Functions

Base::InputStream Class Reference

The [InputStream](../../dd/d72/classBase_1_1InputStream.html "The InputStream
class provides reading of binary data from an istream.") class provides
reading of binary data from an istream.
[More...](../../dd/d72/classBase_1_1InputStream.html#details)

`#include <Stream.h>`

##  Public Member Functions  
  
---  
|
[InputStream](../../dd/d72/classBase_1_1InputStream.html#ae9fc0df00b3273304b8028b78f713ba7)
(std::istream &rin)  
| [operator
bool](../../dd/d72/classBase_1_1InputStream.html#adf102b563658089ad2802ecbc4801930)
() const  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#aede2043865bf7454e5732cb738b7bca9) ([bool](../../d9/db9/classbool.html) &b)  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#a1981baef71a4c512274ce9fc9b8ee777) (double &d)  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#a8df7f3842e6f71dd6809659bba1f3e9f) (float &f)  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#a61404ee65cafebf183827ac30419012c) (int16_t &s)  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#ab36b63d7897ee24d1f88a91db3a1ff0a) (int32_t &i)  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#a22e634afce5c0f8e0cddb287afccc77d) (int64_t &l)  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#a6ce527be21d4233cf1f5d2bc0251c1a6) (int8_t &ch)  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#abd1eb2d06ed61c461df9ac7ada81f673) (uint16_t &us)  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#a638d46982846649048fa0cfce5bdcd76) (uint32_t &ui)  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#a6bc6a7f17a69104380991f6debcb68b6) (uint64_t &ul)  
[InputStream](../../dd/d72/classBase_1_1InputStream.html) & | [operator>>](../../dd/d72/classBase_1_1InputStream.html#a1032952af4bdfc94e2858ccc10cd28a8) (uint8_t &uch)  
|
[~InputStream](../../dd/d72/classBase_1_1InputStream.html#ae71831adce618d60783c287a2ac7075a)
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

The [InputStream](../../dd/d72/classBase_1_1InputStream.html "The InputStream
class provides reading of binary data from an istream.") class provides
reading of binary data from an istream.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ InputStream()

InputStream::InputStream  | ( | std::istream & | _rin_| ) |   
---|---|---|---|---|---  
  
## ◆ ~InputStream()

InputStream::~InputStream  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ operator bool()

Base::InputStream::operator [bool](../../d9/db9/classbool.html) | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ operator>>() [1/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | [bool](../../d9/db9/classbool.html) & | _b_| ) |   
---|---|---|---|---|---  
  
## ◆ operator>>() [2/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | double & | _d_| ) |   
---|---|---|---|---|---  
  
## ◆ operator>>() [3/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | float & | _f_| ) |   
---|---|---|---|---|---  
  
## ◆ operator>>() [4/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | int16_t & | _s_| ) |   
---|---|---|---|---|---  
  
## ◆ operator>>() [5/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | int32_t & | _i_| ) |   
---|---|---|---|---|---  
  
## ◆ operator>>() [6/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | int64_t & | _l_| ) |   
---|---|---|---|---|---  
  
## ◆ operator>>() [7/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | int8_t & | _ch_| ) |   
---|---|---|---|---|---  
  
## ◆ operator>>() [8/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | uint16_t & | _us_| ) |   
---|---|---|---|---|---  
  
## ◆ operator>>() [9/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | uint32_t & | _ui_| ) |   
---|---|---|---|---|---  
  
## ◆ operator>>() [10/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | uint64_t & | _ul_| ) |   
---|---|---|---|---|---  
  
## ◆ operator>>() [11/11]

[InputStream](../../dd/d72/classBase_1_1InputStream.html) & InputStream::operator>> | ( | uint8_t & | _uch_| ) |   
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Stream.h
  * FreeCAD/src/Base/Stream.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

