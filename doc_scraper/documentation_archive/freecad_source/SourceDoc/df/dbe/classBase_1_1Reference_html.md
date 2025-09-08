---
url: https://freecad.github.io/SourceDoc/df/dbe/classBase_1_1Reference.html
scraped_at: 2025-09-08T15:17:08.055237
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Reference](../../df/dbe/classBase_1_1Reference.html)

[List of all members](../../d1/d90/classBase_1_1Reference-members.html) | Public Member Functions

Base::Reference< T > Class Template Reference

[Reference](../../df/dbe/classBase_1_1Reference.html "Reference class
Implementation of the reference counting pattern.") class Implementation of
the reference counting pattern.
[More...](../../df/dbe/classBase_1_1Reference.html#details)

`#include <Handle.h>`

##  Public Member Functions  
  
---  
[int](../../d1/da0/classint.html) | [getRefCount](../../df/dbe/classBase_1_1Reference.html#a5ae9c7385259e65e6bc60af782d60105) () const  
| Get number of references on the object, including this one.
[More...](../../df/dbe/classBase_1_1Reference.html#a5ae9c7385259e65e6bc60af782d60105)  
  
[bool](../../d9/db9/classbool.html) | [isNull](../../df/dbe/classBase_1_1Reference.html#abae4371f64e99ab658a0bb99fe1e9a06) () const  
| Test if it does not handle anything.
[More...](../../df/dbe/classBase_1_1Reference.html#abae4371f64e99ab658a0bb99fe1e9a06)  
  
[bool](../../d9/db9/classbool.html) | [isValid](../../df/dbe/classBase_1_1Reference.html#ace0fb81d327209253d5daefc41b8400e) () const  
| Test if it handles something.
[More...](../../df/dbe/classBase_1_1Reference.html#ace0fb81d327209253d5daefc41b8400e)  
  
| [operator
T*](../../df/dbe/classBase_1_1Reference.html#a63047071868f54182b2e243677484af8)
() const  
[bool](../../d9/db9/classbool.html) | [operator!=](../../df/dbe/classBase_1_1Reference.html#afd018dea74b5bfa9da06a7c275cf6129) (const [Reference](../../df/dbe/classBase_1_1Reference.html)< T > &p) const  
T & | [operator*](../../df/dbe/classBase_1_1Reference.html#a7d337217f74622811e31de56ee4ad80e) () const  
| Dereference operator.
[More...](../../df/dbe/classBase_1_1Reference.html#a7d337217f74622811e31de56ee4ad80e)  
  
T * | [operator->](../../df/dbe/classBase_1_1Reference.html#aa2972c7d371d57bf659586391329c561) () const  
| Dereference operator.
[More...](../../df/dbe/classBase_1_1Reference.html#aa2972c7d371d57bf659586391329c561)  
  
[bool](../../d9/db9/classbool.html) | [operator<](../../df/dbe/classBase_1_1Reference.html#a32aa13c7f953f3cfc298ae13a84894cb) (const [Reference](../../df/dbe/classBase_1_1Reference.html)< T > &p) const  
| Lower operator, needed for sorting in maps and sets.
[More...](../../df/dbe/classBase_1_1Reference.html#a32aa13c7f953f3cfc298ae13a84894cb)  
  
[Reference](../../df/dbe/classBase_1_1Reference.html)< T > & | [operator=](../../df/dbe/classBase_1_1Reference.html#a79e384ef7ea6cd436c75bcbad2073f14) (const [Reference](../../df/dbe/classBase_1_1Reference.html)< T > &p)  
| Assign operator from a handle.
[More...](../../df/dbe/classBase_1_1Reference.html#a79e384ef7ea6cd436c75bcbad2073f14)  
  
[Reference](../../df/dbe/classBase_1_1Reference.html)< T > & | [operator=](../../df/dbe/classBase_1_1Reference.html#a098224cf2d56fa1e4554d6b6c58c5c0f) (T *p)  
| Assign operator from a pointer.
[More...](../../df/dbe/classBase_1_1Reference.html#a098224cf2d56fa1e4554d6b6c58c5c0f)  
  
[bool](../../d9/db9/classbool.html) | [operator==](../../df/dbe/classBase_1_1Reference.html#a87ecc78a0c448564eb1c33688491aa13) (const [Reference](../../df/dbe/classBase_1_1Reference.html)< T > &p) const  
| Equal operator.
[More...](../../df/dbe/classBase_1_1Reference.html#a87ecc78a0c448564eb1c33688491aa13)  
  
|
[Reference](../../df/dbe/classBase_1_1Reference.html#a38701e8bdaf3672b265ace1da5fbd473)
()  
| Pointer and default constructor.
[More...](../../df/dbe/classBase_1_1Reference.html#a38701e8bdaf3672b265ace1da5fbd473)  
  
|
[Reference](../../df/dbe/classBase_1_1Reference.html#a133f345b92109802506e1e55100ab5d1)
(const [Reference](../../df/dbe/classBase_1_1Reference.html)< T > &p)  
| Copy constructor.
[More...](../../df/dbe/classBase_1_1Reference.html#a133f345b92109802506e1e55100ab5d1)  
  
|
[Reference](../../df/dbe/classBase_1_1Reference.html#a541e44bf9ed72a9d519e01a2ec13827c)
(T *p)  
|
[~Reference](../../df/dbe/classBase_1_1Reference.html#a3ca234c816bf9d0c9d87d40bb3593974)
()  
| destructor Release the reference counter which causes, in case of the last
one, the referenced object to be destructed!
[More...](../../df/dbe/classBase_1_1Reference.html#a3ca234c816bf9d0c9d87d40bb3593974)  
  
  
## Detailed Description

template<class T>  
class Base::Reference< T >

[Reference](../../df/dbe/classBase_1_1Reference.html "Reference class
Implementation of the reference counting pattern.") class Implementation of
the reference counting pattern.

Only able to instantiate with a class inheriting
[Base::Handled](../../d6/d99/classBase_1_1Handled.html "Handled class
Implementation of the reference counting pattern.").

## Constructor & Destructor Documentation

## ◆ Reference() [1/3]

template<class T >

[Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::Reference  | ( | | ) |   
---|---|---|---|---  
  
Pointer and default constructor.

## ◆ Reference() [2/3]

template<class T >

[Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::Reference  | ( | T *  | _p_| ) |   
---|---|---|---|---|---  
  
## ◆ Reference() [3/3]

template<class T >

[Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::Reference  | ( | const [Reference](../../df/dbe/classBase_1_1Reference.html)< T > & | _p_| ) |   
---|---|---|---|---|---  
  
Copy constructor.

## ◆ ~Reference()

template<class T >

[Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::~[Reference](../../df/dbe/classBase_1_1Reference.html) | ( | | ) |   
---|---|---|---|---  
  
destructor Release the reference counter which causes, in case of the last
one, the referenced object to be destructed!

## Member Function Documentation

## ◆ getRefCount()

template<class T >

[int](../../d1/da0/classint.html) [Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::getRefCount  | ( | | ) |  const  
---|---|---|---|---  
  
Get number of references on the object, including this one.

## ◆ isNull()

template<class T >

[bool](../../d9/db9/classbool.html) [Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::isNull  | ( | | ) |  const  
---|---|---|---|---  
  
Test if it does not handle anything.

## ◆ isValid()

template<class T >

[bool](../../d9/db9/classbool.html) [Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::isValid  | ( | | ) |  const  
---|---|---|---|---  
  
Test if it handles something.

## ◆ operator T*()

template<class T >

[Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::operator T*  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ operator!=()

template<class T >

[bool](../../d9/db9/classbool.html) [Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::operator!=  | ( | const [Reference](../../df/dbe/classBase_1_1Reference.html)< T > & | _p_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator*()

template<class T >

T & [Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::operator*  | ( | | ) |  const  
---|---|---|---|---  
  
Dereference operator.

## ◆ operator->()

template<class T >

T * [Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::operator-> | ( | | ) |  const  
---|---|---|---|---  
  
Dereference operator.

## ◆ operator<()

template<class T >

[bool](../../d9/db9/classbool.html) [Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::operator< | ( | const [Reference](../../df/dbe/classBase_1_1Reference.html)< T > & | _p_| ) |  const  
---|---|---|---|---|---  
  
Lower operator, needed for sorting in maps and sets.

## ◆ operator=() [1/2]

template<class T >

[Reference](../../df/dbe/classBase_1_1Reference.html)< T > & [Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::operator=  | ( | const [Reference](../../df/dbe/classBase_1_1Reference.html)< T > & | _p_| ) |   
---|---|---|---|---|---  
  
Assign operator from a handle.

## ◆ operator=() [2/2]

template<class T >

[Reference](../../df/dbe/classBase_1_1Reference.html)< T > & [Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::operator=  | ( | T *  | _p_| ) |   
---|---|---|---|---|---  
  
Assign operator from a pointer.

## ◆ operator==()

template<class T >

[bool](../../d9/db9/classbool.html) [Base::Reference](../../df/dbe/classBase_1_1Reference.html)< T >::operator==  | ( | const [Reference](../../df/dbe/classBase_1_1Reference.html)< T > & | _p_| ) |  const  
---|---|---|---|---|---  
  
Equal operator.

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Base/Handle.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

