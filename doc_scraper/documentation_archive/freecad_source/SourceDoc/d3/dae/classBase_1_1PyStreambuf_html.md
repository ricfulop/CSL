---
url: https://freecad.github.io/SourceDoc/d3/dae/classBase_1_1PyStreambuf.html
scraped_at: 2025-09-08T15:17:01.006328
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [PyStreambuf](../../d3/dae/classBase_1_1PyStreambuf.html)

[List of all members](../../dd/d42/classBase_1_1PyStreambuf-members.html) | Public Types | Public Member Functions | Protected Member Functions

Base::PyStreambuf Class Reference

`#include <Stream.h>`

##  Public Types  
  
---  
enum | [Type](../../d3/dae/classBase_1_1PyStreambuf.html#a3a352cb46d0b720c2d737f62dcd43f50) { [StringIO](../../d3/dae/classBase_1_1PyStreambuf.html#a3a352cb46d0b720c2d737f62dcd43f50a0845a1653d6115635ac1283318d58175) , [BytesIO](../../d3/dae/classBase_1_1PyStreambuf.html#a3a352cb46d0b720c2d737f62dcd43f50add715ce8a40ca45f32bc45d33b7644b4) , [Unknown](../../d3/dae/classBase_1_1PyStreambuf.html#a3a352cb46d0b720c2d737f62dcd43f50af8869596044a7acd667a6a398348f6cf) }  
  
##  Public Member Functions  
  
---  
|
[PyStreambuf](../../d3/dae/classBase_1_1PyStreambuf.html#af0cacd6c0ced082bd5bdc115aae7534a)
([PyObject](../../df/d1b/classPyObject.html) *o, std::size_t buf_size=256,
std::size_t put_back=8)  
void | [setType](../../d3/dae/classBase_1_1PyStreambuf.html#a9408d7dd9d34f2377ccf070181d50c29) ([Type](../../d3/dae/classBase_1_1PyStreambuf.html#a3a352cb46d0b720c2d737f62dcd43f50) t)  
virtual | [~PyStreambuf](../../d3/dae/classBase_1_1PyStreambuf.html#ae3099623ddc8c7fdf7a850192e40de8c) ()  
  
##  Protected Member Functions  
  
---  
int_type | [overflow](../../d3/dae/classBase_1_1PyStreambuf.html#a8931133a57e2e6a065967acf3576702b) (int_type c=EOF)  
pos_type | [seekoff](../../d3/dae/classBase_1_1PyStreambuf.html#a0b26f93e8cf780e8e0576a34714727b1) (off_type offset, seekdir dir, openmode)  
pos_type | [seekpos](../../d3/dae/classBase_1_1PyStreambuf.html#a615ac899f38e545831cc84cc42ca2713) (pos_type offset, openmode mode)  
[int](../../d1/da0/classint.html) | [sync](../../d3/dae/classBase_1_1PyStreambuf.html#a477b57109c47cb01f04ce62304078ec5) ()  
int_type | [underflow](../../d3/dae/classBase_1_1PyStreambuf.html#a221b7b998a03058d5638c59bccee694f) ()  
std::streamsize | [xsputn](../../d3/dae/classBase_1_1PyStreambuf.html#ac293ec5ca194b0bd6497b1886bcd2964) (const char *s, std::streamsize num)  
  
## Member Enumeration Documentation

## ◆ Type

enum
[Base::PyStreambuf::Type](../../d3/dae/classBase_1_1PyStreambuf.html#a3a352cb46d0b720c2d737f62dcd43f50)  
---  
  
Enumerator  
---  
StringIO |   
BytesIO |   
Unknown |   
  
## Constructor & Destructor Documentation

## ◆ PyStreambuf()

PyStreambuf::PyStreambuf  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _o_ ,   
---|---|---|---  
|  | std::size_t  | _buf_size_ = `256`,   
|  | std::size_t  | _put_back_ = `8`  
| ) | |   
  
## ◆ ~PyStreambuf()

| PyStreambuf::~PyStreambuf  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[sync()](../../d3/dae/classBase_1_1PyStreambuf.html#a477b57109c47cb01f04ce62304078ec5).

## Member Function Documentation

## ◆ overflow()

| PyStreambuf::int_type PyStreambuf::overflow  | ( | PyStreambuf::int_type  | _ch_ = `EOF`| ) |   
---|---|---|---|---|---  
protected  
  
References
[sync()](../../d3/dae/classBase_1_1PyStreambuf.html#a477b57109c47cb01f04ce62304078ec5).

## ◆ seekoff()

| PyStreambuf::pos_type PyStreambuf::seekoff  | ( | PyStreambuf::off_type  | _offset_ ,   
---|---|---|---  
|  | PyStreambuf::seekdir  | _dir_ ,   
|  | PyStreambuf::openmode  |   
| ) | |   
protected  
  
Referenced by
[seekpos()](../../d3/dae/classBase_1_1PyStreambuf.html#a615ac899f38e545831cc84cc42ca2713).

## ◆ seekpos()

| PyStreambuf::pos_type PyStreambuf::seekpos  | ( | PyStreambuf::pos_type  | _offset_ ,   
---|---|---|---  
|  | PyStreambuf::openmode  | _mode_  
| ) | |   
protected  
  
References
[seekoff()](../../d3/dae/classBase_1_1PyStreambuf.html#a0b26f93e8cf780e8e0576a34714727b1).

## ◆ setType()

void Base::PyStreambuf::setType  | ( | [Type](../../d3/dae/classBase_1_1PyStreambuf.html#a3a352cb46d0b720c2d737f62dcd43f50) | _t_| ) |   
---|---|---|---|---|---  
  
## ◆ sync()

| [int](../../d1/da0/classint.html) PyStreambuf::sync  | ( | | ) |   
---|---|---|---|---  
protected  
  
Referenced by
[overflow()](../../d3/dae/classBase_1_1PyStreambuf.html#a8931133a57e2e6a065967acf3576702b),
and
[~PyStreambuf()](../../d3/dae/classBase_1_1PyStreambuf.html#ae3099623ddc8c7fdf7a850192e40de8c).

## ◆ underflow()

| PyStreambuf::int_type PyStreambuf::underflow  | ( | | ) |   
---|---|---|---|---  
protected  
  
## ◆ xsputn()

| std::streamsize PyStreambuf::xsputn  | ( | const char *  | _s_ ,   
---|---|---|---  
|  | std::streamsize  | _num_  
| ) | |   
protected  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Stream.h
  * FreeCAD/src/Base/Stream.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

