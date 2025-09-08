---
url: https://freecad.github.io/SourceDoc/d2/d91/structApp_1_1ColorModelPack.html
scraped_at: 2025-09-08T14:54:06.331043
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html)

[List of all members](../../d9/d1a/structApp_1_1ColorModelPack-members.html) | Static Public Member Functions | Public Attributes

App::ColorModelPack Struct Reference

`#include <ColorModel.h>`

##  Static Public Member Functions  
  
---  
static [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) | [createBlackWhite](../../d2/d91/structApp_1_1ColorModelPack.html#aa6c336e098cf85d09d368b02e8a873c8) ()  
static [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) | [createBlueGreenRed](../../d2/d91/structApp_1_1ColorModelPack.html#a751de21f74df8a182f09ab36ccfcc660) ()  
static [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) | [createRedGreenBlue](../../d2/d91/structApp_1_1ColorModelPack.html#a8459719674240c3f3380239bfaeec745) ()  
static [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) | [createRedWhiteBlue](../../d2/d91/structApp_1_1ColorModelPack.html#a39660ef0ed8383622fabf3ab530fa97d) ()  
static [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) | [createWhiteBlack](../../d2/d91/structApp_1_1ColorModelPack.html#aa53b5737c7769e404d21712ade79aa13) ()  
  
##  Public Attributes  
  
---  
[ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) | [bottomModel](../../d2/d91/structApp_1_1ColorModelPack.html#a1164f89d8e9b9f1450b06d069799d74d) = [ColorModelBlueCyanGreen](../../d1/deb/classApp_1_1ColorModelBlueCyanGreen.html)()  
std::string | [description](../../d2/d91/structApp_1_1ColorModelPack.html#ac38ca50f3a1e22df47bd7fec540627b0)  
[ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) | [topModel](../../d2/d91/structApp_1_1ColorModelPack.html#ac342004df7980cf827544f087e90be45) = [ColorModelGreenYellowRed](../../d2/dfc/classApp_1_1ColorModelGreenYellowRed.html)()  
[ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) | [totalModel](../../d2/d91/structApp_1_1ColorModelPack.html#a947456dc7b944b0f44f904d56ec81ad5) = [ColorModelBlueGreenRed](../../d4/d4a/classApp_1_1ColorModelBlueGreenRed.html)()  
  
## Member Function Documentation

## ◆ createBlackWhite()

| [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) ColorModelPack::createBlackWhite  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[App::ColorGradient::createStandardPacks()](../../dc/df4/classApp_1_1ColorGradient.html#a03da7234b839faecab45d5f07eacdd08).

## ◆ createBlueGreenRed()

| [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) ColorModelPack::createBlueGreenRed  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[App::ColorGradient::createStandardPacks()](../../dc/df4/classApp_1_1ColorGradient.html#a03da7234b839faecab45d5f07eacdd08).

## ◆ createRedGreenBlue()

| [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) ColorModelPack::createRedGreenBlue  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[App::ColorGradient::createStandardPacks()](../../dc/df4/classApp_1_1ColorGradient.html#a03da7234b839faecab45d5f07eacdd08).

## ◆ createRedWhiteBlue()

| [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) ColorModelPack::createRedWhiteBlue  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[App::ColorGradient::createStandardPacks()](../../dc/df4/classApp_1_1ColorGradient.html#a03da7234b839faecab45d5f07eacdd08).

## ◆ createWhiteBlack()

| [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) ColorModelPack::createWhiteBlack  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[App::ColorGradient::createStandardPacks()](../../dc/df4/classApp_1_1ColorGradient.html#a03da7234b839faecab45d5f07eacdd08).

## Member Data Documentation

## ◆ bottomModel

[ColorModel](../../d4/d9e/classApp_1_1ColorModel.html)
App::ColorModelPack::bottomModel =
[ColorModelBlueCyanGreen](../../d1/deb/classApp_1_1ColorModelBlueCyanGreen.html)()  
---  
  
Referenced by
[App::ColorGradient::getColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#abaceddeba5cb2334d719d79ef7bcbde1),
[App::ColorGradient::rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
and
[App::ColorGradient::setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e).

## ◆ description

std::string App::ColorModelPack::description  
---  
  
Referenced by
[Addon.Addon::set_metadata()](../../d8/d91/classAddon_1_1Addon.html#a799523f4861c30f1516a59602d5b77cd),
and
[Addon.Addon::to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5).

## ◆ topModel

[ColorModel](../../d4/d9e/classApp_1_1ColorModel.html)
App::ColorModelPack::topModel =
[ColorModelGreenYellowRed](../../d2/dfc/classApp_1_1ColorModelGreenYellowRed.html)()  
---  
  
Referenced by
[App::ColorGradient::getColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#abaceddeba5cb2334d719d79ef7bcbde1),
[App::ColorGradient::rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
and
[App::ColorGradient::setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e).

## ◆ totalModel

[ColorModel](../../d4/d9e/classApp_1_1ColorModel.html)
App::ColorModelPack::totalModel =
[ColorModelBlueGreenRed](../../d4/d4a/classApp_1_1ColorModelBlueGreenRed.html)()  
---  
  
Referenced by
[App::ColorGradient::getColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#abaceddeba5cb2334d719d79ef7bcbde1),
[App::ColorGradient::rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
and
[App::ColorGradient::setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e).

* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/App/ColorModel.h
  * FreeCAD/src/App/ColorModel.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

