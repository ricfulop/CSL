---
url: https://freecad.github.io/SourceDoc/d6/d13/classBase_1_1IODeviceIStreambuf.html
scraped_at: 2025-09-08T15:16:31.898315
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [IODeviceIStreambuf](../../d6/d13/classBase_1_1IODeviceIStreambuf.html)

[List of all members](../../d0/ddb/classBase_1_1IODeviceIStreambuf-members.html) | Public Member Functions | Protected Member Functions | Protected Attributes | Static Protected Attributes

Base::IODeviceIStreambuf Class Reference

Simple class to read data directly from Qt's QIODevice.
[More...](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#details)

`#include <Stream.h>`

##  Public Member Functions  
  
---  
|
[IODeviceIStreambuf](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a40e58aa2e959e0797cea7a35f87548fa)
(QIODevice *dev)  
|
[~IODeviceIStreambuf](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#ae71c8410a48024ebd657592d354235ea)
()  
  
##  Protected Member Functions  
  
---  
virtual pos_type | [seekoff](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a24e316107d4c0f08735056169afbd1cb) (std::streambuf::off_type off, std::ios_base::seekdir way, std::ios_base::openmode which=std::ios::in|std::ios::out)  
virtual pos_type | [seekpos](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a9c541174b162bc07abfb71c6aac3372b) (std::streambuf::pos_type sp, std::ios_base::openmode which=std::ios::in|std::ios::out)  
virtual int_type | [underflow](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a244969d1da0d96a76a200188cc6189cf) ()  
  
##  Protected Attributes  
  
---  
char | [buffer](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a680aa58fcf47b909ef9e4822773ab22c) [[bufSize](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a7e928ef9421fce71eadae9272b836712)+[pbSize](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#aef69de3d11ef2f74ff547b21053b309b)]  
QIODevice * | [device](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#aeb2d00146bba18df64166f5b9558cf9b)  
  
##  Static Protected Attributes  
  
---  
static const [int](../../d1/da0/classint.html) | [bufSize](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a7e928ef9421fce71eadae9272b836712) = 1024  
static const [int](../../d1/da0/classint.html) | [pbSize](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#aef69de3d11ef2f74ff547b21053b309b) = 4  
  
## Detailed Description

Simple class to read data directly from Qt's QIODevice.

This class can only be used for readihg but not writing purposes.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ IODeviceIStreambuf()

IODeviceIStreambuf::IODeviceIStreambuf  | ( | QIODevice *  | _dev_| ) |   
---|---|---|---|---|---  
  
References
[pbSize](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#aef69de3d11ef2f74ff547b21053b309b).

## ◆ ~IODeviceIStreambuf()

IODeviceIStreambuf::~IODeviceIStreambuf  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ seekoff()

| std::streambuf::pos_type IODeviceIStreambuf::seekoff  | ( | std::streambuf::off_type  | _off_ ,   
---|---|---|---  
|  | std::ios_base::seekdir  | _way_ ,   
|  | std::ios_base::openmode  | _which_ = `std::ios::in | std::ios::out`  
| ) | |   
protectedvirtual  
  
References
[device](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#aeb2d00146bba18df64166f5b9558cf9b).

Referenced by
[seekpos()](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a9c541174b162bc07abfb71c6aac3372b).

## ◆ seekpos()

| std::streambuf::pos_type IODeviceIStreambuf::seekpos  | ( | std::streambuf::pos_type  | _sp_ ,   
---|---|---|---  
|  | std::ios_base::openmode  | _which_ = `std::ios::in | std::ios::out`  
| ) | |   
protectedvirtual  
  
References
[seekoff()](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a24e316107d4c0f08735056169afbd1cb).

## ◆ underflow()

| std::streambuf::int_type IODeviceIStreambuf::underflow  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
References
[device](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#aeb2d00146bba18df64166f5b9558cf9b),
and
[pbSize](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#aef69de3d11ef2f74ff547b21053b309b).

## Member Data Documentation

## ◆ buffer

| char
Base::IODeviceIStreambuf::buffer[[bufSize](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a7e928ef9421fce71eadae9272b836712)+[pbSize](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#aef69de3d11ef2f74ff547b21053b309b)]  
---  
protected  
  
## ◆ bufSize

| const [int](../../d1/da0/classint.html) Base::IODeviceIStreambuf::bufSize =
1024  
---  
staticprotected  
  
## ◆ device

| QIODevice* Base::IODeviceIStreambuf::device  
---  
protected  
  
Referenced by
[seekoff()](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a24e316107d4c0f08735056169afbd1cb),
and
[underflow()](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a244969d1da0d96a76a200188cc6189cf).

## ◆ pbSize

| const [int](../../d1/da0/classint.html) Base::IODeviceIStreambuf::pbSize = 4  
---  
staticprotected  
  
Referenced by
[IODeviceIStreambuf()](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a40e58aa2e959e0797cea7a35f87548fa),
and
[underflow()](../../d6/d13/classBase_1_1IODeviceIStreambuf.html#a244969d1da0d96a76a200188cc6189cf).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Stream.h
  * FreeCAD/src/Base/Stream.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

