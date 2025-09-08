---
url: https://freecad.github.io/SourceDoc/d1/d74/classApp_1_1ColorLegend.html
scraped_at: 2025-09-08T14:53:54.289060
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html)

[List of all members](../../db/da2/classApp_1_1ColorLegend-members.html) | Public Member Functions | Protected Attributes

App::ColorLegend Class Reference

`#include <ColorModel.h>`

##  Public Member Functions  
  
---  
std::size_t | [addMax](../../d1/d74/classApp_1_1ColorLegend.html#af001cb74d8bbe5e56f36118a967b77c8) (const std::string &rclName)  
std::size_t | [addMin](../../d1/d74/classApp_1_1ColorLegend.html#a94c8640f299f9f38e58c909456d172e2) (const std::string &rclName)  
|
[ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html#a234064f1d9527bf1837c5f3c3c75656e)
()  
|
[ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html#aee62b96916fbafc8c7b9c57ef350dff0)
(const [ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html) &rclCL)  
[Color](../../d3/d3a/classApp_1_1Color.html) | [getColor](../../d1/d74/classApp_1_1ColorLegend.html#ad90a9ecc58480e3cb9e17f01685e8c31) (float fVal) const  
[Color](../../d3/d3a/classApp_1_1Color.html) | [getColor](../../d1/d74/classApp_1_1ColorLegend.html#a81d7684f0af0eead7de013808ec7ebbf) (std::size_t ulPos) const  
std::size_t | [getColorIndex](../../d1/d74/classApp_1_1ColorLegend.html#aede1a91cd863ce7291624e1146979b7b) (float fVal) const  
float | [getMaxValue](../../d1/d74/classApp_1_1ColorLegend.html#ac1a87f777f61eb6c373eae9ed645c666) () const  
float | [getMinValue](../../d1/d74/classApp_1_1ColorLegend.html#a064f4571bdf9c15f882794c76216fabd) () const  
uint32_t | [getPackedColor](../../d1/d74/classApp_1_1ColorLegend.html#a84e3c65fa2c3e3eeb6be4eae90391524) (std::size_t ulPos) const  
std::string | [getText](../../d1/d74/classApp_1_1ColorLegend.html#aa2b4effd429160a8a2bc087079735f8c) (std::size_t ulPos) const  
float | [getValue](../../d1/d74/classApp_1_1ColorLegend.html#a68c8ada4fd4504ff8f6e249f7562466b) (std::size_t ulPos) const  
std::size_t | [hasNumberOfFields](../../d1/d74/classApp_1_1ColorLegend.html#aea0769c168b32022a59fba036304ae6f) () const  
[bool](../../d9/db9/classbool.html) | [isOutsideGrayed](../../d1/d74/classApp_1_1ColorLegend.html#aff9576edd2b6f2117e91c6b11b4db748) () const  
[bool](../../d9/db9/classbool.html) | [operator!=](../../d1/d74/classApp_1_1ColorLegend.html#aa2c0a33c7e64ef85b1c9218c685ef922) (const [ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html) &rclCL) const  
[ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html) & | [operator=](../../d1/d74/classApp_1_1ColorLegend.html#a90084d5a8ba373f87fd65f4fda249617) (const [ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html) &rclCL)  
[bool](../../d9/db9/classbool.html) | [operator==](../../d1/d74/classApp_1_1ColorLegend.html#af8f6607d22896d2afbbd8637f7e2d9f4) (const [ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html) &rclCL) const  
[bool](../../d9/db9/classbool.html) | [remove](../../d1/d74/classApp_1_1ColorLegend.html#ac7f27653f234d7efdf6fad9f3bf415fc) (std::size_t ulPos)  
void | [removeFirst](../../d1/d74/classApp_1_1ColorLegend.html#a6361e6e80fb15d1bcf704b1a1e2dc3cc) ()  
void | [removeLast](../../d1/d74/classApp_1_1ColorLegend.html#afb45913acfca62131109a8ae50da44cd) ()  
void | [resize](../../d1/d74/classApp_1_1ColorLegend.html#a671f1a013a9bba6367a01a11b8d433a8) (std::size_t ulN)  
[bool](../../d9/db9/classbool.html) | [setColor](../../d1/d74/classApp_1_1ColorLegend.html#ad7ed9231f82f53627ef40f1f391128e3) (std::size_t ulPos, float ucRed, float ucGreen, float ucBlue)  
[bool](../../d9/db9/classbool.html) | [setColor](../../d1/d74/classApp_1_1ColorLegend.html#af6688bcfbf49425819a2a9a8adef6050) (std::size_t ulPos, unsigned long ulColor)  
void | [setOutsideGrayed](../../d1/d74/classApp_1_1ColorLegend.html#a4a59c66033f78421cbba8fedbe6011e8) ([bool](../../d9/db9/classbool.html) bOS)  
[bool](../../d9/db9/classbool.html) | [setText](../../d1/d74/classApp_1_1ColorLegend.html#ac30f8351b6ed6f7fc7e35d36a7c7ea69) (std::size_t ulPos, const std::string &rclName)  
[bool](../../d9/db9/classbool.html) | [setValue](../../d1/d74/classApp_1_1ColorLegend.html#aabb24d508c2f0ae3dec7b2bbbc4b921a) (std::size_t ulPos, float fVal)  
virtual | [~ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html#aa043e9cc6219b4021891ff6932f34cc5) ()  
  
##  Protected Attributes  
  
---  
std::deque< [Color](../../d3/d3a/classApp_1_1Color.html) > | [colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748)  
std::deque< std::string > | [names](../../d1/d74/classApp_1_1ColorLegend.html#a69fe1b8199b14e54d6454ac5f7b38efd)  
[bool](../../d9/db9/classbool.html) | [outsideGrayed](../../d1/d74/classApp_1_1ColorLegend.html#a86a36b71311672f32e575f8de0530a3e)  
std::deque< float > | [values](../../d1/d74/classApp_1_1ColorLegend.html#ae945411ca0f123e546ba5d01aa7c9eee)  
  
## Constructor & Destructor Documentation

## ◆ ColorLegend() [1/2]

ColorLegend::ColorLegend  | ( | | ) |   
---|---|---|---|---  
  
References
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748).

## ◆ ColorLegend() [2/2]

ColorLegend::ColorLegend  | ( | const [ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html) & | _rclCL_| ) |   
---|---|---|---|---|---  
  
## ◆ ~ColorLegend()

| virtual App::ColorLegend::~ColorLegend  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ addMax()

std::size_t ColorLegend::addMax  | ( | const std::string & | _rclName_| ) |   
---|---|---|---|---|---  
  
References
[App::Color::b](../../d3/d3a/classApp_1_1Color.html#a80db35212156aad08612f92a82d60340),
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748),
[App::Color::g](../../d3/d3a/classApp_1_1Color.html#a95e979ab4c74614e16a24752023b3910),
and
[App::Color::r](../../d3/d3a/classApp_1_1Color.html#ac6aecf7a9aabad5c63b67ef031ec6df4).

## ◆ addMin()

std::size_t ColorLegend::addMin  | ( | const std::string & | _rclName_| ) |   
---|---|---|---|---|---  
  
References
[App::Color::b](../../d3/d3a/classApp_1_1Color.html#a80db35212156aad08612f92a82d60340),
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748),
[App::Color::g](../../d3/d3a/classApp_1_1Color.html#a95e979ab4c74614e16a24752023b3910),
and
[App::Color::r](../../d3/d3a/classApp_1_1Color.html#ac6aecf7a9aabad5c63b67ef031ec6df4).

Referenced by
[resize()](../../d1/d74/classApp_1_1ColorLegend.html#a671f1a013a9bba6367a01a11b8d433a8).

## ◆ getColor() [1/2]

[Color](../../d3/d3a/classApp_1_1Color.html) App::ColorLegend::getColor  | ( | float  | _fVal_| ) |  const  
---|---|---|---|---|---  
  
References
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748),
and
[outsideGrayed](../../d1/d74/classApp_1_1ColorLegend.html#a86a36b71311672f32e575f8de0530a3e).

Referenced by
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::getPrefColor()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aed0d2ca7140c357c09c3aae8f4bba159),
and
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::setValues()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aeae62102b8bdfc483bfee73586df265d).

## ◆ getColor() [2/2]

[Color](../../d3/d3a/classApp_1_1Color.html) ColorLegend::getColor  | ( | std::size_t  | _ulPos_| ) |  const  
---|---|---|---|---|---  
  
References
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748).

Referenced by
[getPackedColor()](../../d1/d74/classApp_1_1ColorLegend.html#a84e3c65fa2c3e3eeb6be4eae90391524),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::getPrefColor()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aed0d2ca7140c357c09c3aae8f4bba159),
and
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::setValues()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aeae62102b8bdfc483bfee73586df265d).

## ◆ getColorIndex()

std::size_t App::ColorLegend::getColorIndex  | ( | float  | _fVal_| ) |  const  
---|---|---|---|---|---  
  
References
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748).

## ◆ getMaxValue()

float App::ColorLegend::getMaxValue  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getMinValue()

float App::ColorLegend::getMinValue  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getPackedColor()

uint32_t ColorLegend::getPackedColor  | ( | std::size_t  | _ulPos_| ) |  const  
---|---|---|---|---|---  
  
References
[getColor()](../../d1/d74/classApp_1_1ColorLegend.html#a81d7684f0af0eead7de013808ec7ebbf),
and
[App::Color::getPackedValue()](../../d3/d3a/classApp_1_1Color.html#a38a46423f244f19f0adece1b69a9fd70).

## ◆ getText()

std::string ColorLegend::getText  | ( | std::size_t  | _ulPos_| ) |  const  
---|---|---|---|---|---  
  
## ◆ getValue()

float ColorLegend::getValue  | ( | std::size_t  | _ulPos_| ) |  const  
---|---|---|---|---|---  
  
## ◆ hasNumberOfFields()

std::size_t App::ColorLegend::hasNumberOfFields  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isOutsideGrayed()

[bool](../../d9/db9/classbool.html) App::ColorLegend::isOutsideGrayed  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ operator!=()

[bool](../../d9/db9/classbool.html) App::ColorLegend::operator!=  | ( | const [ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html) & | _rclCL_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator=()

[ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html) & ColorLegend::operator=  | ( | const [ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html) & | _rclCL_| ) |   
---|---|---|---|---|---  
  
References
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748),
[names](../../d1/d74/classApp_1_1ColorLegend.html#a69fe1b8199b14e54d6454ac5f7b38efd),
[outsideGrayed](../../d1/d74/classApp_1_1ColorLegend.html#a86a36b71311672f32e575f8de0530a3e),
and
[values](../../d1/d74/classApp_1_1ColorLegend.html#ae945411ca0f123e546ba5d01aa7c9eee).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) ColorLegend::operator==  | ( | const [ColorLegend](../../d1/d74/classApp_1_1ColorLegend.html) & | _rclCL_| ) |  const  
---|---|---|---|---|---  
  
References
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748),
[names](../../d1/d74/classApp_1_1ColorLegend.html#a69fe1b8199b14e54d6454ac5f7b38efd),
[outsideGrayed](../../d1/d74/classApp_1_1ColorLegend.html#a86a36b71311672f32e575f8de0530a3e),
and
[values](../../d1/d74/classApp_1_1ColorLegend.html#ae945411ca0f123e546ba5d01aa7c9eee).

## ◆ remove()

[bool](../../d9/db9/classbool.html) ColorLegend::remove  | ( | std::size_t  | _ulPos_| ) |   
---|---|---|---|---|---  
  
References
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748).

## ◆ removeFirst()

void ColorLegend::removeFirst  | ( | | ) |   
---|---|---|---|---  
  
References
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748).

## ◆ removeLast()

void ColorLegend::removeLast  | ( | | ) |   
---|---|---|---|---  
  
References
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748).

Referenced by
[resize()](../../d1/d74/classApp_1_1ColorLegend.html#a671f1a013a9bba6367a01a11b8d433a8).

## ◆ resize()

void ColorLegend::resize  | ( | std::size_t  | _ulN_| ) |   
---|---|---|---|---|---  
  
References
[addMin()](../../d1/d74/classApp_1_1ColorLegend.html#a94c8640f299f9f38e58c909456d172e2),
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748),
and
[removeLast()](../../d1/d74/classApp_1_1ColorLegend.html#afb45913acfca62131109a8ae50da44cd).

## ◆ setColor() [1/2]

[bool](../../d9/db9/classbool.html) ColorLegend::setColor  | ( | std::size_t  | _ulPos_ ,   
---|---|---|---  
|  | float  | _ucRed_ ,   
|  | float  | _ucGreen_ ,   
|  | float  | _ucBlue_  
| ) | |   
  
References
[colorFields](../../d1/d74/classApp_1_1ColorLegend.html#a64c9368b56b85a2cf46074e4eef5b748).

Referenced by
[setColor()](../../d1/d74/classApp_1_1ColorLegend.html#af6688bcfbf49425819a2a9a8adef6050).

## ◆ setColor() [2/2]

[bool](../../d9/db9/classbool.html) ColorLegend::setColor  | ( | std::size_t  | _ulPos_ ,   
---|---|---|---  
|  | unsigned long  | _ulColor_  
| ) | |   
  
References
[setColor()](../../d1/d74/classApp_1_1ColorLegend.html#ad7ed9231f82f53627ef40f1f391128e3).

## ◆ setOutsideGrayed()

void App::ColorLegend::setOutsideGrayed  | ( | [bool](../../d9/db9/classbool.html) | _bOS_| ) |   
---|---|---|---|---|---  
  
## ◆ setText()

[bool](../../d9/db9/classbool.html) ColorLegend::setText  | ( | std::size_t  | _ulPos_ ,   
---|---|---|---  
|  | const std::string & | _rclName_  
| ) | |   
  
## ◆ setValue()

[bool](../../d9/db9/classbool.html) ColorLegend::setValue  | ( | std::size_t  | _ulPos_ ,   
---|---|---|---  
|  | float  | _fVal_  
| ) | |   
  
## Member Data Documentation

## ◆ colorFields

| std::deque<[Color](../../d3/d3a/classApp_1_1Color.html)>
App::ColorLegend::colorFields  
---  
protected  
  
Referenced by
[addMax()](../../d1/d74/classApp_1_1ColorLegend.html#af001cb74d8bbe5e56f36118a967b77c8),
[addMin()](../../d1/d74/classApp_1_1ColorLegend.html#a94c8640f299f9f38e58c909456d172e2),
[ColorLegend()](../../d1/d74/classApp_1_1ColorLegend.html#a234064f1d9527bf1837c5f3c3c75656e),
[getColor()](../../d1/d74/classApp_1_1ColorLegend.html#a81d7684f0af0eead7de013808ec7ebbf),
[getColorIndex()](../../d1/d74/classApp_1_1ColorLegend.html#aede1a91cd863ce7291624e1146979b7b),
[operator=()](../../d1/d74/classApp_1_1ColorLegend.html#a90084d5a8ba373f87fd65f4fda249617),
[operator==()](../../d1/d74/classApp_1_1ColorLegend.html#af8f6607d22896d2afbbd8637f7e2d9f4),
[remove()](../../d1/d74/classApp_1_1ColorLegend.html#ac7f27653f234d7efdf6fad9f3bf415fc),
[removeFirst()](../../d1/d74/classApp_1_1ColorLegend.html#a6361e6e80fb15d1bcf704b1a1e2dc3cc),
[removeLast()](../../d1/d74/classApp_1_1ColorLegend.html#afb45913acfca62131109a8ae50da44cd),
[resize()](../../d1/d74/classApp_1_1ColorLegend.html#a671f1a013a9bba6367a01a11b8d433a8),
and
[setColor()](../../d1/d74/classApp_1_1ColorLegend.html#ad7ed9231f82f53627ef40f1f391128e3).

## ◆ names

| std::deque<std::string> App::ColorLegend::names  
---  
protected  
  
Referenced by
[operator=()](../../d1/d74/classApp_1_1ColorLegend.html#a90084d5a8ba373f87fd65f4fda249617),
and
[operator==()](../../d1/d74/classApp_1_1ColorLegend.html#af8f6607d22896d2afbbd8637f7e2d9f4).

## ◆ outsideGrayed

| [bool](../../d9/db9/classbool.html) App::ColorLegend::outsideGrayed  
---  
protected  
  
Referenced by
[getColor()](../../d1/d74/classApp_1_1ColorLegend.html#ad90a9ecc58480e3cb9e17f01685e8c31),
[operator=()](../../d1/d74/classApp_1_1ColorLegend.html#a90084d5a8ba373f87fd65f4fda249617),
and
[operator==()](../../d1/d74/classApp_1_1ColorLegend.html#af8f6607d22896d2afbbd8637f7e2d9f4).

## ◆ values

| std::deque<float> App::ColorLegend::values  
---  
protected  
  
Referenced by
[Mod.PartDesign.WizardShaft.SegmentFunction.IntervalFunction::addInterval()](../../d9/d57/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1IntervalFunction.html#a77314ec65a9c8886ae903bce504ed02d),
[operator=()](../../d1/d74/classApp_1_1ColorLegend.html#a90084d5a8ba373f87fd65f4fda249617),
[operator==()](../../d1/d74/classApp_1_1ColorLegend.html#af8f6607d22896d2afbbd8637f7e2d9f4),
[ifc4.ifcstructuralloadconfiguration::validlistsize()](../../df/d70/classifc4_1_1ifcstructuralloadconfiguration.html#a192a2217a60ec2129c4fc5e31ebe9b7b),
and
[Mod.PartDesign.WizardShaft.SegmentFunction.IntervalFunction::value()](../../d9/d57/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1IntervalFunction.html#a6ec4a5f2e9d44d8f5986b7ee9ab6df42).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ColorModel.h
  * FreeCAD/src/App/ColorModel.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

