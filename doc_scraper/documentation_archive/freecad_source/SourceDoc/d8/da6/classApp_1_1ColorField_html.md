---
url: https://freecad.github.io/SourceDoc/d8/da6/classApp_1_1ColorField.html
scraped_at: 2025-09-08T14:53:51.312027
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ColorField](../../d8/da6/classApp_1_1ColorField.html)

[List of all members](../../de/d6d/classApp_1_1ColorField-members.html) | Public Member Functions | Protected Member Functions | Protected Attributes

App::ColorField Class Reference

`#include <ColorModel.h>`

##  Public Member Functions  
  
---  
|
[ColorField](../../d8/da6/classApp_1_1ColorField.html#a9afe6d9934f9930846447d5ff4d8bf49)
()  
|
[ColorField](../../d8/da6/classApp_1_1ColorField.html#a7ba48bb8e9a6b632afc5fc7964cf5584)
(const [ColorField](../../d8/da6/classApp_1_1ColorField.html) &rclCF)  
|
[ColorField](../../d8/da6/classApp_1_1ColorField.html#a35e9076e7412bfc9f57b79a5b28e53ed)
(const [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) &rclModel, float
[fMin](../../d8/da6/classApp_1_1ColorField.html#a7e7772c5e950948e43a02234e419c3ff),
float
[fMax](../../d8/da6/classApp_1_1ColorField.html#ae7b050facb4851e90c520be715446805),
std::size_t usCt)  
[Color](../../d3/d3a/classApp_1_1Color.html) | [getColor](../../d8/da6/classApp_1_1ColorField.html#a61694c18f7bc4929a2dd57baf03da7b9) (float fVal) const  
[Color](../../d3/d3a/classApp_1_1Color.html) | [getColor](../../d8/da6/classApp_1_1ColorField.html#a16e4ed9e7e7546fb954325154e7b558d) (std::size_t usIndex) const  
std::size_t | [getColorIndex](../../d8/da6/classApp_1_1ColorField.html#a9d49ee35d33bdb1224cd3323d5c75fd4) (float fVal) const  
const [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) & | [getColorModel](../../d8/da6/classApp_1_1ColorField.html#aa7ba5f71091428ab6bb15d3d8e02dfae) () const  
std::size_t | [getCountColors](../../d8/da6/classApp_1_1ColorField.html#a591b9c855412effec4c0a8fbeb1bac65) () const  
float | [getMaxValue](../../d8/da6/classApp_1_1ColorField.html#a5545ae2173efa9d9b558c848f38d94ef) () const  
std::size_t | [getMinColors](../../d8/da6/classApp_1_1ColorField.html#a1bd15de22d566099550fad78dda190a7) () const  
float | [getMinValue](../../d8/da6/classApp_1_1ColorField.html#a2d1ca36173b366970b7802a9aa2c9551) () const  
void | [getRange](../../d8/da6/classApp_1_1ColorField.html#a665f99639f1116478eee384ab4eca2ae) (float &rfMin, float &rfMax)  
[ColorField](../../d8/da6/classApp_1_1ColorField.html) & | [operator=](../../d8/da6/classApp_1_1ColorField.html#a96b6bf7e5f94cbaffdc25a1754ce2a77) (const [ColorField](../../d8/da6/classApp_1_1ColorField.html) &rclCF)  
void | [set](../../d8/da6/classApp_1_1ColorField.html#ac917f8dbb792ec7ab99ceae64e61a7e0) (const [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) &rclModel, float [fMin](../../d8/da6/classApp_1_1ColorField.html#a7e7772c5e950948e43a02234e419c3ff), float [fMax](../../d8/da6/classApp_1_1ColorField.html#ae7b050facb4851e90c520be715446805), std::size_t usCt)  
void | [setColorModel](../../d8/da6/classApp_1_1ColorField.html#a9c7c8385af89ac38951e73c6227b2260) (const [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) &rclModel)  
void | [setCountColors](../../d8/da6/classApp_1_1ColorField.html#a523505747d0f637e14bb4d7e5f12d4e0) (std::size_t usCt)  
void | [setDirect](../../d8/da6/classApp_1_1ColorField.html#a222a52dc9510a6b5dc58b0a861e45168) (std::size_t usInd, [Color](../../d3/d3a/classApp_1_1Color.html) clCol)  
void | [setRange](../../d8/da6/classApp_1_1ColorField.html#a9b2b89c1a482010c22a88ab4217da272) (float [fMin](../../d8/da6/classApp_1_1ColorField.html#a7e7772c5e950948e43a02234e419c3ff), float [fMax](../../d8/da6/classApp_1_1ColorField.html#ae7b050facb4851e90c520be715446805))  
virtual | [~ColorField](../../d8/da6/classApp_1_1ColorField.html#a24c4cf688f628730dfac8d72c5e30240) ()=default  
  
##  Protected Member Functions  
  
---  
void | [interpolate](../../d8/da6/classApp_1_1ColorField.html#a290f75780235047fb37c172ca5d6304f) ([Color](../../d3/d3a/classApp_1_1Color.html) clCol1, std::size_t usPos1, [Color](../../d3/d3a/classApp_1_1Color.html) clCol2, std::size_t usPos2)  
void | [rebuild](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25) ()  
  
##  Protected Attributes  
  
---  
std::vector< [Color](../../d3/d3a/classApp_1_1Color.html) > | [colorField](../../d8/da6/classApp_1_1ColorField.html#a3711da7b125b67a43520fffd208062f3)  
[ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) | [colorModel](../../d8/da6/classApp_1_1ColorField.html#a1c2e6ecf9074f48ad3ac31b67c11a977)  
std::size_t | [ctColors](../../d8/da6/classApp_1_1ColorField.html#a86fd5bbb2c7abea6e96505bc14444a5e)  
float | [fAscent](../../d8/da6/classApp_1_1ColorField.html#a93f154760e6a2b029d4de7bde0b4b876)  
float | [fConstant](../../d8/da6/classApp_1_1ColorField.html#a21f35f15a0524b61a4b26cc8abc7cc4b)  
float | [fMax](../../d8/da6/classApp_1_1ColorField.html#ae7b050facb4851e90c520be715446805)  
float | [fMin](../../d8/da6/classApp_1_1ColorField.html#a7e7772c5e950948e43a02234e419c3ff)  
  
## Constructor & Destructor Documentation

## ◆ ColorField() [1/3]

ColorField::ColorField  | ( | | ) |   
---|---|---|---|---  
  
References
[set()](../../d8/da6/classApp_1_1ColorField.html#ac917f8dbb792ec7ab99ceae64e61a7e0).

## ◆ ColorField() [2/3]

ColorField::ColorField  | ( | const [ColorField](../../d8/da6/classApp_1_1ColorField.html) & | _rclCF_| ) |   
---|---|---|---|---|---  
  
## ◆ ColorField() [3/3]

ColorField::ColorField  | ( | const [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) & | _rclModel_ ,   
---|---|---|---  
|  | float  | _fMin_ ,   
|  | float  | _fMax_ ,   
|  | std::size_t  | _usCt_  
| ) | |   
  
References
[fMax](../../d8/da6/classApp_1_1ColorField.html#ae7b050facb4851e90c520be715446805),
[fMin](../../d8/da6/classApp_1_1ColorField.html#a7e7772c5e950948e43a02234e419c3ff),
and
[set()](../../d8/da6/classApp_1_1ColorField.html#ac917f8dbb792ec7ab99ceae64e61a7e0).

## ◆ ~ColorField()

| virtual App::ColorField::~ColorField  | ( | | ) |   
---|---|---|---|---  
virtualdefault  
  
## Member Function Documentation

## ◆ getColor() [1/2]

[Color](../../d3/d3a/classApp_1_1Color.html) App::ColorField::getColor  | ( | float  | _fVal_| ) |  const  
---|---|---|---|---|---  
  
References
[App::Color::b](../../d3/d3a/classApp_1_1Color.html#a80db35212156aad08612f92a82d60340),
[colorModel](../../d8/da6/classApp_1_1ColorField.html#a1c2e6ecf9074f48ad3ac31b67c11a977),
[App::ColorModel::colors](../../d4/d9e/classApp_1_1ColorModel.html#acc565fde34e6d1d547728a8417756f2a),
[fMax](../../d8/da6/classApp_1_1ColorField.html#ae7b050facb4851e90c520be715446805),
[fMin](../../d8/da6/classApp_1_1ColorField.html#a7e7772c5e950948e43a02234e419c3ff),
[App::Color::g](../../d3/d3a/classApp_1_1Color.html#a95e979ab4c74614e16a24752023b3910),
[App::ColorModel::getCountColors()](../../d4/d9e/classApp_1_1ColorModel.html#a78855a38757909a3c963d340fcb50c9a),
and
[App::Color::r](../../d3/d3a/classApp_1_1Color.html#ac6aecf7a9aabad5c63b67ef031ec6df4).

Referenced by
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::getPrefColor()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aed0d2ca7140c357c09c3aae8f4bba159),
and
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::setValues()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aeae62102b8bdfc483bfee73586df265d).

## ◆ getColor() [2/2]

[Color](../../d3/d3a/classApp_1_1Color.html) App::ColorField::getColor  | ( | std::size_t  | _usIndex_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::getPrefColor()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aed0d2ca7140c357c09c3aae8f4bba159),
and
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::setValues()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aeae62102b8bdfc483bfee73586df265d).

## ◆ getColorIndex()

std::size_t App::ColorField::getColorIndex  | ( | float  | _fVal_| ) |  const  
---|---|---|---|---|---  
  
References
[ctColors](../../d8/da6/classApp_1_1ColorField.html#a86fd5bbb2c7abea6e96505bc14444a5e),
[fAscent](../../d8/da6/classApp_1_1ColorField.html#a93f154760e6a2b029d4de7bde0b4b876),
and
[fConstant](../../d8/da6/classApp_1_1ColorField.html#a21f35f15a0524b61a4b26cc8abc7cc4b).

Referenced by
[App::ColorGradient::getColorIndex()](../../dc/df4/classApp_1_1ColorGradient.html#a3245c8dccd95dcfc82fb6de95d03d8a7).

## ◆ getColorModel()

const [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) & App::ColorField::getColorModel  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getCountColors()

std::size_t App::ColorField::getCountColors  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::ColorGradient::getColorIndex()](../../dc/df4/classApp_1_1ColorGradient.html#a3245c8dccd95dcfc82fb6de95d03d8a7).

## ◆ getMaxValue()

float App::ColorField::getMaxValue  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getMinColors()

std::size_t App::ColorField::getMinColors  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::ColorGradient::getMinColors()](../../dc/df4/classApp_1_1ColorGradient.html#ae6a8116d98df073189b07a90316c8510).

## ◆ getMinValue()

float App::ColorField::getMinValue  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getRange()

void App::ColorField::getRange  | ( | float & | _rfMin_ ,   
---|---|---|---  
|  | float & | _rfMax_  
| ) | |   
  
## ◆ interpolate()

| void ColorField::interpolate  | ( | [Color](../../d3/d3a/classApp_1_1Color.html) | _clCol1_ ,   
---|---|---|---  
|  | std::size_t  | _usPos1_ ,   
|  | [Color](../../d3/d3a/classApp_1_1Color.html) | _clCol2_ ,   
|  | std::size_t  | _usPos2_  
| ) | |   
protected  
  
References
[App::Color::b](../../d3/d3a/classApp_1_1Color.html#a80db35212156aad08612f92a82d60340),
[colorField](../../d8/da6/classApp_1_1ColorField.html#a3711da7b125b67a43520fffd208062f3),
[App::Color::g](../../d3/d3a/classApp_1_1Color.html#a95e979ab4c74614e16a24752023b3910),
and
[App::Color::r](../../d3/d3a/classApp_1_1Color.html#ac6aecf7a9aabad5c63b67ef031ec6df4).

Referenced by
[rebuild()](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25).

## ◆ operator=()

[ColorField](../../d8/da6/classApp_1_1ColorField.html) & ColorField::operator=  | ( | const [ColorField](../../d8/da6/classApp_1_1ColorField.html) & | _rclCF_| ) |   
---|---|---|---|---|---  
  
References
[colorField](../../d8/da6/classApp_1_1ColorField.html#a3711da7b125b67a43520fffd208062f3).

## ◆ rebuild()

| void ColorField::rebuild  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[colorField](../../d8/da6/classApp_1_1ColorField.html#a3711da7b125b67a43520fffd208062f3),
[colorModel](../../d8/da6/classApp_1_1ColorField.html#a1c2e6ecf9074f48ad3ac31b67c11a977),
[App::ColorModel::colors](../../d4/d9e/classApp_1_1ColorModel.html#acc565fde34e6d1d547728a8417756f2a),
[ctColors](../../d8/da6/classApp_1_1ColorField.html#a86fd5bbb2c7abea6e96505bc14444a5e),
[fAscent](../../d8/da6/classApp_1_1ColorField.html#a93f154760e6a2b029d4de7bde0b4b876),
[fConstant](../../d8/da6/classApp_1_1ColorField.html#a21f35f15a0524b61a4b26cc8abc7cc4b),
[fMax](../../d8/da6/classApp_1_1ColorField.html#ae7b050facb4851e90c520be715446805),
[fMin](../../d8/da6/classApp_1_1ColorField.html#a7e7772c5e950948e43a02234e419c3ff),
[App::ColorModel::getCountColors()](../../d4/d9e/classApp_1_1ColorModel.html#a78855a38757909a3c963d340fcb50c9a),
and
[interpolate()](../../d8/da6/classApp_1_1ColorField.html#a290f75780235047fb37c172ca5d6304f).

Referenced by
[set()](../../d8/da6/classApp_1_1ColorField.html#ac917f8dbb792ec7ab99ceae64e61a7e0),
and
[setColorModel()](../../d8/da6/classApp_1_1ColorField.html#a9c7c8385af89ac38951e73c6227b2260).

## ◆ set()

void ColorField::set  | ( | const [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) & | _rclModel_ ,   
---|---|---|---  
|  | float  | _fMin_ ,   
|  | float  | _fMax_ ,   
|  | std::size_t  | _usCt_  
| ) | |   
  
References
[colorModel](../../d8/da6/classApp_1_1ColorField.html#a1c2e6ecf9074f48ad3ac31b67c11a977),
[ctColors](../../d8/da6/classApp_1_1ColorField.html#a86fd5bbb2c7abea6e96505bc14444a5e),
[fMax](../../d8/da6/classApp_1_1ColorField.html#ae7b050facb4851e90c520be715446805),
[fMin](../../d8/da6/classApp_1_1ColorField.html#a7e7772c5e950948e43a02234e419c3ff),
[App::ColorModel::getCountColors()](../../d4/d9e/classApp_1_1ColorModel.html#a78855a38757909a3c963d340fcb50c9a),
and
[rebuild()](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25).

Referenced by
[ColorField()](../../d8/da6/classApp_1_1ColorField.html#a9afe6d9934f9930846447d5ff4d8bf49),
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297),
and
[App::ColorGradient::rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907).

## ◆ setColorModel()

void ColorField::setColorModel  | ( | const [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) & | _rclModel_| ) |   
---|---|---|---|---|---  
  
References
[colorModel](../../d8/da6/classApp_1_1ColorField.html#a1c2e6ecf9074f48ad3ac31b67c11a977),
and
[rebuild()](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25).

Referenced by
[App::ColorGradient::setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e).

## ◆ setCountColors()

void App::ColorField::setCountColors  | ( | std::size_t  | _usCt_| ) |   
---|---|---|---|---|---  
  
## ◆ setDirect()

void App::ColorField::setDirect  | ( | std::size_t  | _usInd_ ,   
---|---|---|---  
|  | [Color](../../d3/d3a/classApp_1_1Color.html) | _clCol_  
| ) | |   
  
## ◆ setRange()

void App::ColorField::setRange  | ( | float  | _fMin_ ,   
---|---|---|---  
|  | float  | _fMax_  
| ) | |   
  
## Member Data Documentation

## ◆ colorField

| std::vector<[Color](../../d3/d3a/classApp_1_1Color.html)>
App::ColorField::colorField  
---  
protected  
  
Referenced by
[interpolate()](../../d8/da6/classApp_1_1ColorField.html#a290f75780235047fb37c172ca5d6304f),
[operator=()](../../d8/da6/classApp_1_1ColorField.html#a96b6bf7e5f94cbaffdc25a1754ce2a77),
and
[rebuild()](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25).

## ◆ colorModel

| [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html)
App::ColorField::colorModel  
---  
protected  
  
Referenced by
[getColor()](../../d8/da6/classApp_1_1ColorField.html#a61694c18f7bc4929a2dd57baf03da7b9),
[rebuild()](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25),
[set()](../../d8/da6/classApp_1_1ColorField.html#ac917f8dbb792ec7ab99ceae64e61a7e0),
and
[setColorModel()](../../d8/da6/classApp_1_1ColorField.html#a9c7c8385af89ac38951e73c6227b2260).

## ◆ ctColors

| std::size_t App::ColorField::ctColors  
---  
protected  
  
Referenced by
[getColorIndex()](../../d8/da6/classApp_1_1ColorField.html#a9d49ee35d33bdb1224cd3323d5c75fd4),
[rebuild()](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25),
and
[set()](../../d8/da6/classApp_1_1ColorField.html#ac917f8dbb792ec7ab99ceae64e61a7e0).

## ◆ fAscent

| float App::ColorField::fAscent  
---  
protected  
  
Referenced by
[getColorIndex()](../../d8/da6/classApp_1_1ColorField.html#a9d49ee35d33bdb1224cd3323d5c75fd4),
and
[rebuild()](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25).

## ◆ fConstant

| float App::ColorField::fConstant  
---  
protected  
  
Referenced by
[getColorIndex()](../../d8/da6/classApp_1_1ColorField.html#a9d49ee35d33bdb1224cd3323d5c75fd4),
and
[rebuild()](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25).

## ◆ fMax

| float App::ColorField::fMax  
---  
protected  
  
Referenced by
[ColorField()](../../d8/da6/classApp_1_1ColorField.html#a35e9076e7412bfc9f57b79a5b28e53ed),
[getColor()](../../d8/da6/classApp_1_1ColorField.html#a61694c18f7bc4929a2dd57baf03da7b9),
[rebuild()](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25),
and
[set()](../../d8/da6/classApp_1_1ColorField.html#ac917f8dbb792ec7ab99ceae64e61a7e0).

## ◆ fMin

| float App::ColorField::fMin  
---  
protected  
  
Referenced by
[ColorField()](../../d8/da6/classApp_1_1ColorField.html#a35e9076e7412bfc9f57b79a5b28e53ed),
[getColor()](../../d8/da6/classApp_1_1ColorField.html#a61694c18f7bc4929a2dd57baf03da7b9),
[rebuild()](../../d8/da6/classApp_1_1ColorField.html#a1b16471c6fbd6112a5ef0150a7baab25),
and
[set()](../../d8/da6/classApp_1_1ColorField.html#ac917f8dbb792ec7ab99ceae64e61a7e0).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ColorModel.h
  * FreeCAD/src/App/ColorModel.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

