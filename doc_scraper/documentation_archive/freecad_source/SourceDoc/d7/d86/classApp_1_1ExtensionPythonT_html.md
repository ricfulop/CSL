---
url: https://freecad.github.io/SourceDoc/d7/d86/classApp_1_1ExtensionPythonT.html
scraped_at: 2025-09-08T14:54:42.472941
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)

[List of all members](../../d9/d2e/classApp_1_1ExtensionPythonT-members.html) | Public Types | Public Member Functions

App::ExtensionPythonT< ExtensionT > Class Template Reference

Generic Python extension class which allows every extension derived class to
behave as a Python extension – simply by subclassing.
[More...](../../d7/d86/classApp_1_1ExtensionPythonT.html#details)

`#include <ExtensionPython.h>`

##  Public Types  
  
---  
typedef [ExtensionT](../../df/d73/classExtensionT.html) | [Inherited](../../d7/d86/classApp_1_1ExtensionPythonT.html#ad5783aceb37f1f091b9f89fca88e6788)  
  
##  Public Member Functions  
  
---  
|
[ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html#ac3d7d542ad5713280063fdd7d894ea2b)
()  
|
[ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html#a9e5b2991cd35376e68db4bf3bd80933b)
(const [ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)
&)=delete  
|
[ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html#a39bd523c4a40f5bc96b08cb3334d6db9)
([ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html) &&)=delete  
[ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html) & | [operator=](../../d7/d86/classApp_1_1ExtensionPythonT.html#aa06ed1daf13c928caa9d4555fe829d59) (const [ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html) &)=delete  
[ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html) & | [operator=](../../d7/d86/classApp_1_1ExtensionPythonT.html#a897b7ac2ae43d54c8b09db8cfcd196e6) ([ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html) &&)=delete  
virtual | [~ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html#a3d2589f1a8fd7f118fdfc42b179e1d76) ()  
  
## Detailed Description

template<class [ExtensionT](../../df/d73/classExtensionT.html)>  
class App::ExtensionPythonT< ExtensionT >

Generic Python extension class which allows every extension derived class to
behave as a Python extension – simply by subclassing.

## Member Typedef Documentation

## ◆ Inherited

template<class [ExtensionT](../../df/d73/classExtensionT.html) >

typedef [ExtensionT](../../df/d73/classExtensionT.html)
[App::ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)<
[ExtensionT](../../df/d73/classExtensionT.html) >::Inherited  
---  
  
## Constructor & Destructor Documentation

## ◆ ExtensionPythonT() [1/3]

template<class [ExtensionT](../../df/d73/classExtensionT.html) >

[App::ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [ExtensionT](../../df/d73/classExtensionT.html) >::ExtensionPythonT  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~ExtensionPythonT()

template<class [ExtensionT](../../df/d73/classExtensionT.html) >

| virtual [App::ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [ExtensionT](../../df/d73/classExtensionT.html) >::~[ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html) | ( | | ) |   
---|---|---|---|---  
virtual  
  
## ◆ ExtensionPythonT() [2/3]

template<class [ExtensionT](../../df/d73/classExtensionT.html) >

| [App::ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [ExtensionT](../../df/d73/classExtensionT.html) >::ExtensionPythonT  | ( | const [ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [ExtensionT](../../df/d73/classExtensionT.html) > & | | ) |   
---|---|---|---|---|---  
delete  
  
## ◆ ExtensionPythonT() [3/3]

template<class [ExtensionT](../../df/d73/classExtensionT.html) >

| [App::ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [ExtensionT](../../df/d73/classExtensionT.html) >::ExtensionPythonT  | ( | [ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [ExtensionT](../../df/d73/classExtensionT.html) > && | | ) |   
---|---|---|---|---|---  
delete  
  
## Member Function Documentation

## ◆ operator=() [1/2]

template<class [ExtensionT](../../df/d73/classExtensionT.html) >

| [ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html) & [App::ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [ExtensionT](../../df/d73/classExtensionT.html) >::operator=  | ( | const [ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [ExtensionT](../../df/d73/classExtensionT.html) > & | | ) |   
---|---|---|---|---|---  
delete  
  
## ◆ operator=() [2/2]

template<class [ExtensionT](../../df/d73/classExtensionT.html) >

| [ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html) & [App::ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [ExtensionT](../../df/d73/classExtensionT.html) >::operator=  | ( | [ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [ExtensionT](../../df/d73/classExtensionT.html) > && | | ) |   
---|---|---|---|---|---  
delete  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/ExtensionPython.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

