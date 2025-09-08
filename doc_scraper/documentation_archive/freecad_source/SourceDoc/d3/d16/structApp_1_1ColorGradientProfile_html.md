---
url: https://freecad.github.io/SourceDoc/d3/d16/structApp_1_1ColorGradientProfile.html
scraped_at: 2025-09-08T14:53:53.268289
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html)

[List of all members](../../de/d1b/structApp_1_1ColorGradientProfile-members.html) | Public Member Functions | Public Attributes

App::ColorGradientProfile Struct Reference

`#include <ColorModel.h>`

##  Public Member Functions  
  
---  
|
[ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html#a4913bd75cea63b2d36698ad46a0a2a40)
()  
|
[ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html#a005a835cd3b7433eb1947c32532c5601)
(const
[ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html)
&)=default  
[bool](../../d9/db9/classbool.html) | [isEqual](../../d3/d16/structApp_1_1ColorGradientProfile.html#adf0dd6db258ce590c377d77adc077589) (const [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) &) const  
[ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) & | [operator=](../../d3/d16/structApp_1_1ColorGradientProfile.html#a6b918d6b0d989fcbb2a8267127daa4d2) (const [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) &)=default  
  
##  Public Attributes  
  
---  
std::size_t | [ctColors](../../d3/d16/structApp_1_1ColorGradientProfile.html#aff3eb9c58def0f2b1af0fe3f2bd3cf52)  
float | [fMax](../../d3/d16/structApp_1_1ColorGradientProfile.html#a3d62ee50eacfe162f98fd6c5bdf38b43)  
float | [fMin](../../d3/d16/structApp_1_1ColorGradientProfile.html#a8f9cd4700d585d95ca6c84533a046dc7)  
std::size_t | [tColorModel](../../d3/d16/structApp_1_1ColorGradientProfile.html#ab0d04c4d1aacde397d0976836d626c3b)  
[ColorBarStyle](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02) | [tStyle](../../d3/d16/structApp_1_1ColorGradientProfile.html#a392b964ca797dbe7f77a6ca0f4e7fdb0)  
[VisibilityFlags](../../dd/dc2/namespaceApp.html#aad0f0a595677192ca0ecd0f891538f18) | [visibility](../../d3/d16/structApp_1_1ColorGradientProfile.html#add005b330c426798b3582a89fce8e8c2)  
  
## Constructor & Destructor Documentation

## ◆ ColorGradientProfile() [1/2]

ColorGradientProfile::ColorGradientProfile  | ( | | ) |   
---|---|---|---|---  
  
References
[App::Default](../../dd/dc2/namespaceApp.html#aa5c64359788d4ae6612cda3aa51227c6a7a1920d61156abc05a60135aefe8bc67),
and
[App::FLOW](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a38b13c5b8b7fa5cdbe5e49dbea3cd5b1).

## ◆ ColorGradientProfile() [2/2]

| App::ColorGradientProfile::ColorGradientProfile  | ( | const [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## Member Function Documentation

## ◆ isEqual()

[bool](../../d9/db9/classbool.html) ColorGradientProfile::isEqual  | ( | const [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) & | _cg_| ) |  const  
---|---|---|---|---|---  
  
References
[fMax](../../d3/d16/structApp_1_1ColorGradientProfile.html#a3d62ee50eacfe162f98fd6c5bdf38b43),
[fMin](../../d3/d16/structApp_1_1ColorGradientProfile.html#a8f9cd4700d585d95ca6c84533a046dc7),
[Base::Flags< Enum
>::isEqual()](../../dd/d19/classBase_1_1Flags.html#aba0760c706552c8b0972c95e62229817),
[tColorModel](../../d3/d16/structApp_1_1ColorGradientProfile.html#ab0d04c4d1aacde397d0976836d626c3b),
[tStyle](../../d3/d16/structApp_1_1ColorGradientProfile.html#a392b964ca797dbe7f77a6ca0f4e7fdb0),
and
[visibility](../../d3/d16/structApp_1_1ColorGradientProfile.html#add005b330c426798b3582a89fce8e8c2).

Referenced by
[Gui::SoFCColorGradient::customize()](../../d0/de7/classGui_1_1SoFCColorGradient.html#af1c20488dfa1c3ec77da20bc8caf30a9).

## ◆ operator=()

| [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) & App::ColorGradientProfile::operator=  | ( | const [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## Member Data Documentation

## ◆ ctColors

std::size_t App::ColorGradientProfile::ctColors  
---  
  
Referenced by
[Gui::Dialog::DlgSettingsColorGradientImp::getProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#abf3c0fb20fb355447a2eec5bb7c174b7),
[App::ColorGradient::rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
[App::ColorGradient::set()](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f),
and
[Gui::Dialog::DlgSettingsColorGradientImp::setProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#ac6e9fe32a9810b0e682bf91c07911517).

## ◆ fMax

float App::ColorGradientProfile::fMax  
---  
  
Referenced by
[Gui::SoFCColorGradient::customize()](../../d0/de7/classGui_1_1SoFCColorGradient.html#af1c20488dfa1c3ec77da20bc8caf30a9),
[App::ColorGradient::getColorIndex()](../../dc/df4/classApp_1_1ColorGradient.html#a3245c8dccd95dcfc82fb6de95d03d8a7),
[App::ColorGradient::getColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#abaceddeba5cb2334d719d79ef7bcbde1),
[App::ColorGradient::getMinColors()](../../dc/df4/classApp_1_1ColorGradient.html#ae6a8116d98df073189b07a90316c8510),
[Gui::Dialog::DlgSettingsColorGradientImp::getProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#abf3c0fb20fb355447a2eec5bb7c174b7),
[isEqual()](../../d3/d16/structApp_1_1ColorGradientProfile.html#adf0dd6db258ce590c377d77adc077589),
[App::ColorGradient::rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
[App::ColorGradient::set()](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f),
and
[Gui::Dialog::DlgSettingsColorGradientImp::setProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#ac6e9fe32a9810b0e682bf91c07911517).

## ◆ fMin

float App::ColorGradientProfile::fMin  
---  
  
Referenced by
[Gui::SoFCColorGradient::customize()](../../d0/de7/classGui_1_1SoFCColorGradient.html#af1c20488dfa1c3ec77da20bc8caf30a9),
[App::ColorGradient::getColorIndex()](../../dc/df4/classApp_1_1ColorGradient.html#a3245c8dccd95dcfc82fb6de95d03d8a7),
[App::ColorGradient::getColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#abaceddeba5cb2334d719d79ef7bcbde1),
[App::ColorGradient::getMinColors()](../../dc/df4/classApp_1_1ColorGradient.html#ae6a8116d98df073189b07a90316c8510),
[Gui::Dialog::DlgSettingsColorGradientImp::getProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#abf3c0fb20fb355447a2eec5bb7c174b7),
[isEqual()](../../d3/d16/structApp_1_1ColorGradientProfile.html#adf0dd6db258ce590c377d77adc077589),
[App::ColorGradient::rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
[App::ColorGradient::set()](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f),
and
[Gui::Dialog::DlgSettingsColorGradientImp::setProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#ac6e9fe32a9810b0e682bf91c07911517).

## ◆ tColorModel

std::size_t App::ColorGradientProfile::tColorModel  
---  
  
Referenced by
[Gui::Dialog::DlgSettingsColorGradientImp::getProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#abf3c0fb20fb355447a2eec5bb7c174b7),
[isEqual()](../../d3/d16/structApp_1_1ColorGradientProfile.html#adf0dd6db258ce590c377d77adc077589),
[App::ColorGradient::setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a781330b536c3c39ef1b71d4136177377),
and
[Gui::Dialog::DlgSettingsColorGradientImp::setProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#ac6e9fe32a9810b0e682bf91c07911517).

## ◆ tStyle

[ColorBarStyle](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02)
App::ColorGradientProfile::tStyle  
---  
  
Referenced by
[App::ColorGradient::getColorIndex()](../../dc/df4/classApp_1_1ColorGradient.html#a3245c8dccd95dcfc82fb6de95d03d8a7),
[App::ColorGradient::getColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#abaceddeba5cb2334d719d79ef7bcbde1),
[App::ColorGradient::getMinColors()](../../dc/df4/classApp_1_1ColorGradient.html#ae6a8116d98df073189b07a90316c8510),
[Gui::Dialog::DlgSettingsColorGradientImp::getProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#abf3c0fb20fb355447a2eec5bb7c174b7),
[isEqual()](../../d3/d16/structApp_1_1ColorGradientProfile.html#adf0dd6db258ce590c377d77adc077589),
[App::ColorGradient::rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
[App::ColorGradient::set()](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f),
[App::ColorGradient::setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e),
and
[Gui::Dialog::DlgSettingsColorGradientImp::setProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#ac6e9fe32a9810b0e682bf91c07911517).

## ◆ visibility

[VisibilityFlags](../../dd/dc2/namespaceApp.html#aad0f0a595677192ca0ecd0f891538f18)
App::ColorGradientProfile::visibility  
---  
  
Referenced by
[Gui::Dialog::DlgSettingsColorGradientImp::getProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#abf3c0fb20fb355447a2eec5bb7c174b7),
[isEqual()](../../d3/d16/structApp_1_1ColorGradientProfile.html#adf0dd6db258ce590c377d77adc077589),
[PathScripts.PathOpGui.TaskPanel::preCleanup()](../../da/d7e/classPathScripts_1_1PathOpGui_1_1TaskPanel.html#a2226cccc7fd6b29f4c822d94cd2ec267),
[App::ColorGradient::set()](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f),
and
[Gui::Dialog::DlgSettingsColorGradientImp::setProfile()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#ac6e9fe32a9810b0e682bf91c07911517).

* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/App/ColorModel.h
  * FreeCAD/src/App/ColorModel.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

