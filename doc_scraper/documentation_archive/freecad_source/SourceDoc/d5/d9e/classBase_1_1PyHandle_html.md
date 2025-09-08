---
url: https://freecad.github.io/SourceDoc/d5/d9e/classBase_1_1PyHandle.html
scraped_at: 2025-09-08T15:16:59.004171
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)

[List of all members](../../d9/d19/classBase_1_1PyHandle-members.html) | Public Member Functions

Base::PyHandle< HandledType > Class Template Reference

The PyHandler class This class is the base class of all FreeCAD classes which
exports into the python space.
[More...](../../d5/d9e/classBase_1_1PyHandle.html#details)

`#include <PyExport.h>`

##  Public Member Functions  
  
---  
[PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d5/d9e/classBase_1_1PyHandle.html#a5ae971f97a2db2fa86b9a20b47f49a18) () const  
| returns the type as [PyObject](../../df/d1b/classPyObject.html)
[More...](../../d5/d9e/classBase_1_1PyHandle.html#a5ae971f97a2db2fa86b9a20b47f49a18)  
  
[bool](../../d9/db9/classbool.html) | [IsNull](../../d5/d9e/classBase_1_1PyHandle.html#af2ad3fe20d60d2bded680258449c42c4) () const  
| Test if it not handles something.
[More...](../../d5/d9e/classBase_1_1PyHandle.html#af2ad3fe20d60d2bded680258449c42c4)  
  
[bool](../../d9/db9/classbool.html) | [IsValid](../../d5/d9e/classBase_1_1PyHandle.html#a6de7e78e900a9b11867e79097cd91e7b) () const  
| Test if it handles something.
[More...](../../d5/d9e/classBase_1_1PyHandle.html#a6de7e78e900a9b11867e79097cd91e7b)  
  
HandledType & | [operator*](../../d5/d9e/classBase_1_1PyHandle.html#a8365343b7bdd4f41f2d7a2ee090a7673) ()  
| dereference operators
[More...](../../d5/d9e/classBase_1_1PyHandle.html#a8365343b7bdd4f41f2d7a2ee090a7673)  
  
const HandledType & | [operator*](../../d5/d9e/classBase_1_1PyHandle.html#acd0e06d6b7d56ced4e50cbf192ea540b) () const  
| dereference operators
[More...](../../d5/d9e/classBase_1_1PyHandle.html#acd0e06d6b7d56ced4e50cbf192ea540b)  
  
HandledType * | [operator->](../../d5/d9e/classBase_1_1PyHandle.html#a90fbedf032543d1a9b896b4d78003438) ()  
| dereference operators
[More...](../../d5/d9e/classBase_1_1PyHandle.html#a90fbedf032543d1a9b896b4d78003438)  
  
const HandledType * | [operator->](../../d5/d9e/classBase_1_1PyHandle.html#a84b89ead269a7598d0f12a83190cdaf4) () const  
| dereference operators
[More...](../../d5/d9e/classBase_1_1PyHandle.html#a84b89ead269a7598d0f12a83190cdaf4)  
  
[bool](../../d9/db9/classbool.html) | [operator<](../../d5/d9e/classBase_1_1PyHandle.html#a96a8717096b3595ed45cc141b62af5a3) (const [PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > &other) const  
| lower operator needed for sorting in maps and sets
[More...](../../d5/d9e/classBase_1_1PyHandle.html#a96a8717096b3595ed45cc141b62af5a3)  
  
[PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > & | [operator=](../../d5/d9e/classBase_1_1PyHandle.html#a10d481ab0ab14da51c0fe228c8899fab) (const [PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > &other)  
[PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > & | [operator=](../../d5/d9e/classBase_1_1PyHandle.html#a5560d115c35a95b11e5c878584b61345) (HandledType *other)  
[bool](../../d9/db9/classbool.html) | [operator==](../../d5/d9e/classBase_1_1PyHandle.html#a2772d6cbae88090492fa6a8586f5a617) (const [PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > &other) const  
| equal operator
[More...](../../d5/d9e/classBase_1_1PyHandle.html#a2772d6cbae88090492fa6a8586f5a617)  
  
|
[PyHandle](../../d5/d9e/classBase_1_1PyHandle.html#a5720c7331c5215cd300135924c108b2f)
(const [PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >
&ToHandle)  
| Copy constructor.
[More...](../../d5/d9e/classBase_1_1PyHandle.html#a5720c7331c5215cd300135924c108b2f)  
  
|
[PyHandle](../../d5/d9e/classBase_1_1PyHandle.html#ace0bbf398c2418e1faa5fd7378f6b7da)
(HandledType *ToHandle=0L)  
| pointer and default constructor the good way would be not using pointer
instead using a overwritten new operator in the HandledType class! But is not
easy to enforce!
[More...](../../d5/d9e/classBase_1_1PyHandle.html#ace0bbf398c2418e1faa5fd7378f6b7da)  
  
|
[~PyHandle](../../d5/d9e/classBase_1_1PyHandle.html#a840c135ee6915d3e05e96365b4b4d52d)
()  
| destructor Release the reference count which cause, if was the last one, the
referenced object to destruct!
[More...](../../d5/d9e/classBase_1_1PyHandle.html#a840c135ee6915d3e05e96365b4b4d52d)  
  
  
## Detailed Description

template<class HandledType>  
class Base::PyHandle< HandledType >

The PyHandler class This class is the base class of all FreeCAD classes which
exports into the python space.

This class handles the creation referencing of the python export object.

Remarks

    GetPyObject() returns the associated Python object to any C++ subclasses. As we cannot determine for sure if we can increment the returned Python object from outside of GetPyObject() we have specified that GetPyObject() does already the increment of the reference counter if needed.

E.g. if GetPyObject() always returns a new Python object then no increment is
necessary, because at construction time the reference counter is already set
to 1. If the Python interpreter stores this object pointer into a local
variable and destroys this variable then the reference counter gets
decremented (to 0) and the object gets destroyed automatically. In case we
didn't make this specification and increment the Python object from outside
once again then the reference counter would be set to 2 and there would be no
chance to destroy the object again.

The other case is that we have a member variable in our C++ class that holds
the Python object then we either can create this Python in the constructor or
create it the first time when GetPyObject() gets called. In the destructor
then we must decrement the Python object to avoid a memory leak while
GetPyObject() then increments the Python object every time it gets called.

Remarks

    One big consequence of this specification is that the programmer must know whether the Python interpreter gets the Python object or not. If the interpreter gets the object then it decrements the counter later on when the internal variable is freed. In case the interpreter doesn't get this object then the programmer must do the decrement on their own.

Note

    To not to undermine this specification the programmer must make sure to get the Python object always via GetPyObject().

See also

    [PyHandle](../../d5/d9e/classBase_1_1PyHandle.html "The PyHandler class This class is the base class of all FreeCAD classes which exports into the python...") @ Python Object handle class Using pointers on classes derived from [PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html "The PyObjectBase class, exports the class as a python type PyObjectBase is the base class for all C++...") would be potentionaly dangerous because you would have to take care of the reference counting of python by your self. Hence this class was designed. It takes care of references and as long as a [object](../../dc/dd8/classobject.html) of this class exists the handled class get not destructed. That means a [PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html "The PyObjectBase class, exports the class as a python type PyObjectBase is the base class for all C++...") derived [object](../../dc/dd8/classobject.html) you can only destruct by destructing all FCPyHandle and all python references on it! 
     [PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html "The PyObjectBase class, exports the class as a python type PyObjectBase is the base class for all C++...")

## Constructor & Destructor Documentation

## ◆ PyHandle() [1/2]

template<class HandledType >

[Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::PyHandle  | ( | HandledType *  | _ToHandle_ = `0L`| ) |   
---|---|---|---|---|---  
  
pointer and default constructor the good way would be not using pointer
instead using a overwritten new operator in the HandledType class! But is not
easy to enforce!

## ◆ PyHandle() [2/2]

template<class HandledType >

[Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::PyHandle  | ( | const [PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > & | _ToHandle_| ) |   
---|---|---|---|---|---  
  
Copy constructor.

## ◆ ~PyHandle()

template<class HandledType >

[Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::~[PyHandle](../../d5/d9e/classBase_1_1PyHandle.html) | ( | | ) |   
---|---|---|---|---  
  
destructor Release the reference count which cause, if was the last one, the
referenced object to destruct!

## Member Function Documentation

## ◆ getPyObject()

template<class HandledType >

[PyObject](../../df/d1b/classPyObject.html) * [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::getPyObject  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
returns the type as [PyObject](../../df/d1b/classPyObject.html)

References [Base::PyHandle< HandledType
>::getPyObject()](../../d5/d9e/classBase_1_1PyHandle.html#a5ae971f97a2db2fa86b9a20b47f49a18).

Referenced by [Base::PyHandle< HandledType
>::getPyObject()](../../d5/d9e/classBase_1_1PyHandle.html#a5ae971f97a2db2fa86b9a20b47f49a18).

## ◆ IsNull()

template<class HandledType >

[bool](../../d9/db9/classbool.html) [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::IsNull  | ( | | ) |  const  
---|---|---|---|---  
  
Test if it not handles something.

## ◆ IsValid()

template<class HandledType >

[bool](../../d9/db9/classbool.html) [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::IsValid  | ( | | ) |  const  
---|---|---|---|---  
  
Test if it handles something.

## ◆ operator*() [1/2]

template<class HandledType >

HandledType & [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::operator*  | ( | | ) |   
---|---|---|---|---  
  
dereference operators

## ◆ operator*() [2/2]

template<class HandledType >

const HandledType & [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::operator*  | ( | | ) |  const  
---|---|---|---|---  
  
dereference operators

## ◆ operator->() [1/2]

template<class HandledType >

HandledType * [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::operator-> | ( | | ) |   
---|---|---|---|---  
  
dereference operators

## ◆ operator->() [2/2]

template<class HandledType >

const HandledType * [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::operator-> | ( | | ) |  const  
---|---|---|---|---  
  
dereference operators

## ◆ operator<()

template<class HandledType >

[bool](../../d9/db9/classbool.html) [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::operator< | ( | const [PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > & | _other_| ) |  const  
---|---|---|---|---|---  
  
lower operator needed for sorting in maps and sets

## ◆ operator=() [1/2]

template<class HandledType >

[PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > & [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::operator=  | ( | const [PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > & | _other_| ) |   
---|---|---|---|---|---  
  
## ◆ operator=() [2/2]

template<class HandledType >

[PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > & [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::operator=  | ( | HandledType *  | _other_| ) |   
---|---|---|---|---|---  
  
## ◆ operator==()

template<class HandledType >

[bool](../../d9/db9/classbool.html) [Base::PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType >::operator==  | ( | const [PyHandle](../../d5/d9e/classBase_1_1PyHandle.html)< HandledType > & | _other_| ) |  const  
---|---|---|---|---|---  
  
equal operator

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Base/PyExport.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

