---
url: https://freecad.github.io/SourceDoc/de/d97/classClipperLib_1_1Int128.html
scraped_at: 2025-09-08T15:19:10.590099
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ClipperLib](../../df/db2/namespaceClipperLib.html)
  * [Int128](../../de/d97/classClipperLib_1_1Int128.html)

[List of all members](../../df/d33/classClipperLib_1_1Int128-members.html) | Public Member Functions | Public Attributes

ClipperLib::Int128 Class Reference

##  Public Member Functions  
  
---  
|
[Int128](../../de/d97/classClipperLib_1_1Int128.html#ac23a17a6a5ea143f0297b7ba0dd1830e)
(const
[long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a)
&_hi, const
[ulong64](../../df/db2/namespaceClipperLib.html#a031fec5e97eb7e08708f1cafa53a232d)
&_lo)  
|
[Int128](../../de/d97/classClipperLib_1_1Int128.html#acb7953a56e0ddb6d3245268e457f9e37)
([long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a)
_lo=0)  
| [operator
double](../../de/d97/classClipperLib_1_1Int128.html#aff43efe690619303c4b0a513834d5296)
() const  
[bool](../../d9/db9/classbool.html) | [operator!=](../../de/d97/classClipperLib_1_1Int128.html#ae7437e8f6dcb611e8b33e5e7c9c8fbc0) (const [Int128](../../de/d97/classClipperLib_1_1Int128.html) &val) const  
[Int128](../../de/d97/classClipperLib_1_1Int128.html) | [operator+](../../de/d97/classClipperLib_1_1Int128.html#ad32b1394a82ddf0d9f7da299b91212bd) (const [Int128](../../de/d97/classClipperLib_1_1Int128.html) &rhs) const  
[Int128](../../de/d97/classClipperLib_1_1Int128.html) & | [operator+=](../../de/d97/classClipperLib_1_1Int128.html#a03f0aa7a3e960c260dbd8bf0c16b905c) (const [Int128](../../de/d97/classClipperLib_1_1Int128.html) &rhs)  
[Int128](../../de/d97/classClipperLib_1_1Int128.html) | [operator-](../../de/d97/classClipperLib_1_1Int128.html#a10758b3c62928c3ed45298465b43992c) () const  
[Int128](../../de/d97/classClipperLib_1_1Int128.html) | [operator-](../../de/d97/classClipperLib_1_1Int128.html#a8e8d49476d9cecd1f585790f55dcd8da) (const [Int128](../../de/d97/classClipperLib_1_1Int128.html) &rhs) const  
[Int128](../../de/d97/classClipperLib_1_1Int128.html) & | [operator-=](../../de/d97/classClipperLib_1_1Int128.html#ab3fbc4ec0a8227d9f894678416684cef) (const [Int128](../../de/d97/classClipperLib_1_1Int128.html) &rhs)  
[bool](../../d9/db9/classbool.html) | [operator<](../../de/d97/classClipperLib_1_1Int128.html#ab55bb6a363e7ced8e5e64a1eefac6000) (const [Int128](../../de/d97/classClipperLib_1_1Int128.html) &val) const  
[bool](../../d9/db9/classbool.html) | [operator<=](../../de/d97/classClipperLib_1_1Int128.html#ab3667a2abe7b05841b8004496e4e5ddd) (const [Int128](../../de/d97/classClipperLib_1_1Int128.html) &val) const  
[Int128](../../de/d97/classClipperLib_1_1Int128.html) & | [operator=](../../de/d97/classClipperLib_1_1Int128.html#acf25c74e0da66626dfb3682229fdde24) (const [long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a) &val)  
[bool](../../d9/db9/classbool.html) | [operator==](../../de/d97/classClipperLib_1_1Int128.html#a8946a96471d06371fd5ea4f4f65cb4c9) (const [Int128](../../de/d97/classClipperLib_1_1Int128.html) &val) const  
[bool](../../d9/db9/classbool.html) | [operator>](../../de/d97/classClipperLib_1_1Int128.html#ac3d844564066e223483f9393ba050daa) (const [Int128](../../de/d97/classClipperLib_1_1Int128.html) &val) const  
[bool](../../d9/db9/classbool.html) | [operator>=](../../de/d97/classClipperLib_1_1Int128.html#af01cfcc3d7bdeffc25e2efb855cd196e) (const [Int128](../../de/d97/classClipperLib_1_1Int128.html) &val) const  
  
##  Public Attributes  
  
---  
[long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a) | [hi](../../de/d97/classClipperLib_1_1Int128.html#a167643d0860a14fb563e055511e15e14)  
[ulong64](../../df/db2/namespaceClipperLib.html#a031fec5e97eb7e08708f1cafa53a232d) | [lo](../../de/d97/classClipperLib_1_1Int128.html#a991b9da6e53c777a94fca640e505b258)  
  
## Constructor & Destructor Documentation

## ◆ Int128() [1/2]

ClipperLib::Int128::Int128  | ( | [long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a) | __lo_ = `0`| ) |   
---|---|---|---|---|---  
  
References
[hi](../../de/d97/classClipperLib_1_1Int128.html#a167643d0860a14fb563e055511e15e14),
and
[lo](../../de/d97/classClipperLib_1_1Int128.html#a991b9da6e53c777a94fca640e505b258).

Referenced by
[operator-()](../../de/d97/classClipperLib_1_1Int128.html#a10758b3c62928c3ed45298465b43992c).

## ◆ Int128() [2/2]

ClipperLib::Int128::Int128  | ( | const [long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a) & | __hi_ ,   
---|---|---|---  
|  | const [ulong64](../../df/db2/namespaceClipperLib.html#a031fec5e97eb7e08708f1cafa53a232d) & | __lo_  
| ) | |   
  
## Member Function Documentation

## ◆ operator double()

ClipperLib::Int128::operator double  | ( | | ) |  const  
---|---|---|---|---  
  
References
[hi](../../de/d97/classClipperLib_1_1Int128.html#a167643d0860a14fb563e055511e15e14),
and
[lo](../../de/d97/classClipperLib_1_1Int128.html#a991b9da6e53c777a94fca640e505b258).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) ClipperLib::Int128::operator!=  | ( | const [Int128](../../de/d97/classClipperLib_1_1Int128.html) & | _val_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator+()

[Int128](../../de/d97/classClipperLib_1_1Int128.html) ClipperLib::Int128::operator+  | ( | const [Int128](../../de/d97/classClipperLib_1_1Int128.html) & | _rhs_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator+=()

[Int128](../../de/d97/classClipperLib_1_1Int128.html) & ClipperLib::Int128::operator+=  | ( | const [Int128](../../de/d97/classClipperLib_1_1Int128.html) & | _rhs_| ) |   
---|---|---|---|---|---  
  
References
[hi](../../de/d97/classClipperLib_1_1Int128.html#a167643d0860a14fb563e055511e15e14),
and
[lo](../../de/d97/classClipperLib_1_1Int128.html#a991b9da6e53c777a94fca640e505b258).

## ◆ operator-() [1/2]

[Int128](../../de/d97/classClipperLib_1_1Int128.html) ClipperLib::Int128::operator-  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
References
[hi](../../de/d97/classClipperLib_1_1Int128.html#a167643d0860a14fb563e055511e15e14),
[Int128()](../../de/d97/classClipperLib_1_1Int128.html#acb7953a56e0ddb6d3245268e457f9e37),
and
[lo](../../de/d97/classClipperLib_1_1Int128.html#a991b9da6e53c777a94fca640e505b258).

## ◆ operator-() [2/2]

[Int128](../../de/d97/classClipperLib_1_1Int128.html) ClipperLib::Int128::operator-  | ( | const [Int128](../../de/d97/classClipperLib_1_1Int128.html) & | _rhs_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator-=()

[Int128](../../de/d97/classClipperLib_1_1Int128.html) & ClipperLib::Int128::operator-=  | ( | const [Int128](../../de/d97/classClipperLib_1_1Int128.html) & | _rhs_| ) |   
---|---|---|---|---|---  
  
## ◆ operator<()

[bool](../../d9/db9/classbool.html) ClipperLib::Int128::operator< | ( | const [Int128](../../de/d97/classClipperLib_1_1Int128.html) & | _val_| ) |  const  
---|---|---|---|---|---  
  
References
[hi](../../de/d97/classClipperLib_1_1Int128.html#a167643d0860a14fb563e055511e15e14),
and
[lo](../../de/d97/classClipperLib_1_1Int128.html#a991b9da6e53c777a94fca640e505b258).

## ◆ operator<=()

[bool](../../d9/db9/classbool.html) ClipperLib::Int128::operator<=  | ( | const [Int128](../../de/d97/classClipperLib_1_1Int128.html) & | _val_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator=()

[Int128](../../de/d97/classClipperLib_1_1Int128.html) & ClipperLib::Int128::operator=  | ( | const [long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a) & | _val_| ) |   
---|---|---|---|---|---  
  
References
[hi](../../de/d97/classClipperLib_1_1Int128.html#a167643d0860a14fb563e055511e15e14),
and
[lo](../../de/d97/classClipperLib_1_1Int128.html#a991b9da6e53c777a94fca640e505b258).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) ClipperLib::Int128::operator==  | ( | const [Int128](../../de/d97/classClipperLib_1_1Int128.html) & | _val_| ) |  const  
---|---|---|---|---|---  
  
References
[hi](../../de/d97/classClipperLib_1_1Int128.html#a167643d0860a14fb563e055511e15e14),
and
[lo](../../de/d97/classClipperLib_1_1Int128.html#a991b9da6e53c777a94fca640e505b258).

## ◆ operator>()

[bool](../../d9/db9/classbool.html) ClipperLib::Int128::operator> | ( | const [Int128](../../de/d97/classClipperLib_1_1Int128.html) & | _val_| ) |  const  
---|---|---|---|---|---  
  
References
[hi](../../de/d97/classClipperLib_1_1Int128.html#a167643d0860a14fb563e055511e15e14),
and
[lo](../../de/d97/classClipperLib_1_1Int128.html#a991b9da6e53c777a94fca640e505b258).

## ◆ operator>=()

[bool](../../d9/db9/classbool.html) ClipperLib::Int128::operator>=  | ( | const [Int128](../../de/d97/classClipperLib_1_1Int128.html) & | _val_| ) |  const  
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ hi

[long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a)
ClipperLib::Int128::hi  
---  
  
Referenced by
[Int128()](../../de/d97/classClipperLib_1_1Int128.html#acb7953a56e0ddb6d3245268e457f9e37),
[ClipperLib::Int128Mul()](../../df/db2/namespaceClipperLib.html#a54fd38efeb2ae1bb84d1390bff3cf6bc),
[operator
double()](../../de/d97/classClipperLib_1_1Int128.html#aff43efe690619303c4b0a513834d5296),
[operator+=()](../../de/d97/classClipperLib_1_1Int128.html#a03f0aa7a3e960c260dbd8bf0c16b905c),
[operator-()](../../de/d97/classClipperLib_1_1Int128.html#a10758b3c62928c3ed45298465b43992c),
[operator<()](../../de/d97/classClipperLib_1_1Int128.html#ab55bb6a363e7ced8e5e64a1eefac6000),
[operator=()](../../de/d97/classClipperLib_1_1Int128.html#acf25c74e0da66626dfb3682229fdde24),
[operator==()](../../de/d97/classClipperLib_1_1Int128.html#a8946a96471d06371fd5ea4f4f65cb4c9),
and
[operator>()](../../de/d97/classClipperLib_1_1Int128.html#ac3d844564066e223483f9393ba050daa).

## ◆ lo

[ulong64](../../df/db2/namespaceClipperLib.html#a031fec5e97eb7e08708f1cafa53a232d)
ClipperLib::Int128::lo  
---  
  
Referenced by
[Int128()](../../de/d97/classClipperLib_1_1Int128.html#acb7953a56e0ddb6d3245268e457f9e37),
[ClipperLib::Int128Mul()](../../df/db2/namespaceClipperLib.html#a54fd38efeb2ae1bb84d1390bff3cf6bc),
[operator
double()](../../de/d97/classClipperLib_1_1Int128.html#aff43efe690619303c4b0a513834d5296),
[operator+=()](../../de/d97/classClipperLib_1_1Int128.html#a03f0aa7a3e960c260dbd8bf0c16b905c),
[operator-()](../../de/d97/classClipperLib_1_1Int128.html#a10758b3c62928c3ed45298465b43992c),
[operator<()](../../de/d97/classClipperLib_1_1Int128.html#ab55bb6a363e7ced8e5e64a1eefac6000),
[operator=()](../../de/d97/classClipperLib_1_1Int128.html#acf25c74e0da66626dfb3682229fdde24),
[operator==()](../../de/d97/classClipperLib_1_1Int128.html#a8946a96471d06371fd5ea4f4f65cb4c9),
and
[operator>()](../../de/d97/classClipperLib_1_1Int128.html#ac3d844564066e223483f9393ba050daa).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Path/libarea/clipper.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

