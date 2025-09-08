---
url: https://freecad.github.io/SourceDoc/d1/d97/classApp_1_1WeakPtrT.html
scraped_at: 2025-09-08T14:57:21.142260
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)

[List of all members](../../dc/d2f/classApp_1_1WeakPtrT-members.html) | Public Member Functions

App::WeakPtrT< T > Class Template Reference

The [WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html "The WeakPtrT class.")
class. [More...](../../d1/d97/classApp_1_1WeakPtrT.html#details)

`#include <DocumentObserver.h>`

##  Public Member Functions  
  
---  
[bool](../../d9/db9/classbool.html) | [expired](../../d1/d97/classApp_1_1WeakPtrT.html#a0d69f3d46cf52fe7f17d271167dd552e) () const  
| expired
[More...](../../d1/d97/classApp_1_1WeakPtrT.html#a0d69f3d46cf52fe7f17d271167dd552e)  
  
T * | [get](../../d1/d97/classApp_1_1WeakPtrT.html#a27a27e13f63e249b825a7e00702d6447) () const noexcept  
[bool](../../d9/db9/classbool.html) | [operator!=](../../d1/d97/classApp_1_1WeakPtrT.html#a3561547b7da2be6885db44b6758b8bb6) (const [WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T > &p) const  
| operator !=
[More...](../../d1/d97/classApp_1_1WeakPtrT.html#a3561547b7da2be6885db44b6758b8bb6)  
  
T * | [operator*](../../d1/d97/classApp_1_1WeakPtrT.html#a6ba20e91d7dd78e5acbe51885be6bbda) () const  
| operator ->
[More...](../../d1/d97/classApp_1_1WeakPtrT.html#a6ba20e91d7dd78e5acbe51885be6bbda)  
  
T * | [operator->](../../d1/d97/classApp_1_1WeakPtrT.html#aa9b80e51bffaea4087f8db329c364a8c) () const  
| operator ->
[More...](../../d1/d97/classApp_1_1WeakPtrT.html#aa9b80e51bffaea4087f8db329c364a8c)  
  
[WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T > & | [operator=](../../d1/d97/classApp_1_1WeakPtrT.html#a98ea40c06e37d350bd0cf09c9355f887) (T *p)  
| operator = Assignment operator
[More...](../../d1/d97/classApp_1_1WeakPtrT.html#a98ea40c06e37d350bd0cf09c9355f887)  
  
[bool](../../d9/db9/classbool.html) | [operator==](../../d1/d97/classApp_1_1WeakPtrT.html#aacd3d04418288ff795e9bc352cbf9db0) (const [WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T > &p) const  
| operator ==
[More...](../../d1/d97/classApp_1_1WeakPtrT.html#aacd3d04418288ff795e9bc352cbf9db0)  
  
void | [reset](../../d1/d97/classApp_1_1WeakPtrT.html#a6a6cb6b5cec0367af57dc5419c32039d) ()  
| reset Releases the reference to the managed object. After the call *this
manages no object.
[More...](../../d1/d97/classApp_1_1WeakPtrT.html#a6a6cb6b5cec0367af57dc5419c32039d)  
  
|
[WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html#a5723beb45fcb4bba0284b5662b87782e)
(T *t)  
|
[~WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html#a10bbcc6b0f88b218d514de2c79e3c865)
()  
  
## Detailed Description

template<class T>  
class App::WeakPtrT< T >

The [WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html "The WeakPtrT class.")
class.

## Constructor & Destructor Documentation

## ◆ WeakPtrT()

template<class T >

[App::WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T >::WeakPtrT  | ( | T *  | _t_| ) |   
---|---|---|---|---|---  
  
## ◆ ~WeakPtrT()

template<class T >

[App::WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T >::~[WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html) | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ expired()

template<class T >

[bool](../../d9/db9/classbool.html) [App::WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T >::expired  | ( | | ) |  const  
---|---|---|---|---  
  
expired

Returns

    true if the managed object has already been deleted, false otherwise. 

## ◆ get()

template<class T >

| T * [App::WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T >::get  | ( | | ) |  const  
---|---|---|---|---  
noexcept  
  
Get a pointer to the object or 0 if it doesn't exist any more.

Referenced by
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297).

## ◆ operator!=()

template<class T >

[bool](../../d9/db9/classbool.html) [App::WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T >::operator!=  | ( | const [WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T > & | _p_| ) |  const  
---|---|---|---|---|---  
  
operator !=

Returns

    true if both objects are inequal, false otherwise 

## ◆ operator*()

template<class T >

T * [App::WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T >::operator*  | ( | | ) |  const  
---|---|---|---|---  
  
operator ->

Returns

    pointer to the document object 

## ◆ operator->()

template<class T >

T * [App::WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T >::operator-> | ( | | ) |  const  
---|---|---|---|---  
  
operator ->

Returns

    pointer to the document object 

## ◆ operator=()

template<class T >

[WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T > & [App::WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T >::operator=  | ( | T *  | _p_| ) |   
---|---|---|---|---|---  
  
operator = Assignment operator

## ◆ operator==()

template<class T >

[bool](../../d9/db9/classbool.html) [App::WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T >::operator==  | ( | const [WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T > & | _p_| ) |  const  
---|---|---|---|---|---  
  
operator ==

Returns

    true if both objects are equal, false otherwise 

## ◆ reset()

template<class T >

void [App::WeakPtrT](../../d1/d97/classApp_1_1WeakPtrT.html)< T >::reset  | ( | | ) |   
---|---|---|---|---  
  
reset Releases the reference to the managed object. After the call *this
manages no object.

Referenced by
[draftguitools.gui_trackers.gridTracker::set()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a1499cdcfd43fe110d46cd9c72c52b356).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/DocumentObserver.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

