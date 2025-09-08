---
url: https://freecad.github.io/SourceDoc/dc/df4/classApp_1_1ColorGradient.html
scraped_at: 2025-09-08T14:53:52.318104
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ColorGradient](../../dc/df4/classApp_1_1ColorGradient.html)

[List of all members](../../d7/d10/classApp_1_1ColorGradient-members.html) | Public Member Functions | Protected Member Functions | Protected Attributes

App::ColorGradient Class Reference

`#include <ColorModel.h>`

##  Public Member Functions  
  
---  
|
[ColorGradient](../../dc/df4/classApp_1_1ColorGradient.html#a4acdb3ea165dfe1e1be1644e16622934)
()  
|
[ColorGradient](../../dc/df4/classApp_1_1ColorGradient.html#aefa1345f98db1562e31fd6dccf198633)
(const [ColorGradient](../../dc/df4/classApp_1_1ColorGradient.html) &)=default  
|
[ColorGradient](../../dc/df4/classApp_1_1ColorGradient.html#a40b2acb178ca70d76dbb667d1f868fb1)
(float fMin, float fMax, std::size_t usCtColors,
[ColorBarStyle](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02)
tS,
[VisibilityFlags](../../dd/dc2/namespaceApp.html#aad0f0a595677192ca0ecd0f891538f18)
fl=[Visibility::Default](../../dd/dc2/namespaceApp.html#aa5c64359788d4ae6612cda3aa51227c6a7a1920d61156abc05a60135aefe8bc67))  
[Color](../../d3/d3a/classApp_1_1Color.html) | [getColor](../../dc/df4/classApp_1_1ColorGradient.html#aa6208810fe7eee146cd097696ed5ca60) (float fVal) const  
std::size_t | [getColorIndex](../../dc/df4/classApp_1_1ColorGradient.html#a3245c8dccd95dcfc82fb6de95d03d8a7) (float fVal) const  
const [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) & | [getColorModel](../../dc/df4/classApp_1_1ColorGradient.html#abaceddeba5cb2334d719d79ef7bcbde1) () const  
std::vector< std::string > | [getColorModelNames](../../dc/df4/classApp_1_1ColorGradient.html#aef1af55fe4badb4a6a735fba21e82591) () const  
std::size_t | [getColorModelType](../../dc/df4/classApp_1_1ColorGradient.html#acbc5f18072118fe46e8006003d8b2036) () const  
std::size_t | [getCountColors](../../dc/df4/classApp_1_1ColorGradient.html#a121fbc7cc830d6794f47fc830c9ee7b3) () const  
float | [getMaxValue](../../dc/df4/classApp_1_1ColorGradient.html#a5f5e020e446bf69774191ad148bec826) () const  
std::size_t | [getMinColors](../../dc/df4/classApp_1_1ColorGradient.html#ae6a8116d98df073189b07a90316c8510) () const  
float | [getMinValue](../../dc/df4/classApp_1_1ColorGradient.html#abba77bea9c5f2ee60faa4ae316432e87) () const  
const [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) & | [getProfile](../../dc/df4/classApp_1_1ColorGradient.html#a27c9fbe3b343d2952b1b5ebc8c855046) () const  
void | [getRange](../../dc/df4/classApp_1_1ColorGradient.html#a1716b58126a7a91ffbfb6a9a3edaa6b9) (float &rfMin, float &rfMax) const  
[ColorBarStyle](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02) | [getStyle](../../dc/df4/classApp_1_1ColorGradient.html#ab08a55bd9831fdf5c8c628c1f4653031) () const  
[bool](../../d9/db9/classbool.html) | [isOutOfRange](../../dc/df4/classApp_1_1ColorGradient.html#a10dbd3ff50be8cb20c9aa00658a7d304) (float fVal) const  
[bool](../../d9/db9/classbool.html) | [isOutsideGrayed](../../dc/df4/classApp_1_1ColorGradient.html#adf86d536ac9914b727ce7fb8461827c2) () const  
[bool](../../d9/db9/classbool.html) | [isOutsideInvisible](../../dc/df4/classApp_1_1ColorGradient.html#aa9ff837e587d0bf56b6a489a2bf654c6) () const  
[ColorGradient](../../dc/df4/classApp_1_1ColorGradient.html) & | [operator=](../../dc/df4/classApp_1_1ColorGradient.html#aa8a6e174860f5945ec6edd57e3caa9a6) (const [ColorGradient](../../dc/df4/classApp_1_1ColorGradient.html) &)=default  
void | [set](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f) (float fMin, float fMax, std::size_t usCt, [ColorBarStyle](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02) tS, [VisibilityFlags](../../dd/dc2/namespaceApp.html#aad0f0a595677192ca0ecd0f891538f18) fl)  
void | [setColorModel](../../dc/df4/classApp_1_1ColorGradient.html#a781330b536c3c39ef1b71d4136177377) (std::size_t tModel)  
void | [setCountColors](../../dc/df4/classApp_1_1ColorGradient.html#ab71546ca91e8667b78b5cad1494f9976) (std::size_t usCt)  
void | [setOutsideGrayed](../../dc/df4/classApp_1_1ColorGradient.html#aea25f88d559cebb0ff00bb9a3f4bd727) ([bool](../../d9/db9/classbool.html) value)  
void | [setOutsideInvisible](../../dc/df4/classApp_1_1ColorGradient.html#a59201ff1dd5a893d755c853a7eb81ec9) ([bool](../../d9/db9/classbool.html) value)  
void | [setProfile](../../dc/df4/classApp_1_1ColorGradient.html#a605d3f2985788c9e89257724c21ee029) (const [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) &pro)  
void | [setRange](../../dc/df4/classApp_1_1ColorGradient.html#aabbc0bd38a1b699c697ebfaa309adab5) (float fMin, float fMax)  
void | [setStyle](../../dc/df4/classApp_1_1ColorGradient.html#a09032ac3b02d8657b78d085ecdcfc193) ([ColorBarStyle](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02) tS)  
  
##  Protected Member Functions  
  
---  
void | [createStandardPacks](../../dc/df4/classApp_1_1ColorGradient.html#a03da7234b839faecab45d5f07eacdd08) ()  
void | [rebuild](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907) ()  
void | [setColorModel](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e) ()  
  
##  Protected Attributes  
  
---  
[ColorField](../../d8/da6/classApp_1_1ColorField.html) | [colorField1](../../dc/df4/classApp_1_1ColorGradient.html#a95015c9d532e42c8f831c17a67e394dc)  
[ColorField](../../d8/da6/classApp_1_1ColorField.html) | [colorField2](../../dc/df4/classApp_1_1ColorGradient.html#a09319612bd0ba3d923767be5c3cc3bc7)  
[ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) | [currentModelPack](../../dc/df4/classApp_1_1ColorGradient.html#a382b516bcfeefdbba4a5398f9eab99bf)  
std::vector< [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html) > | [modelPacks](../../dc/df4/classApp_1_1ColorGradient.html#aa063e5d2eb452da11535f725609c106c)  
[ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) | [profile](../../dc/df4/classApp_1_1ColorGradient.html#a0609197eb2ad8ba0142139cf40bc5d95)  
  
## Constructor & Destructor Documentation

## ◆ ColorGradient() [1/3]

ColorGradient::ColorGradient  | ( | | ) |   
---|---|---|---|---  
  
References
[createStandardPacks()](../../dc/df4/classApp_1_1ColorGradient.html#a03da7234b839faecab45d5f07eacdd08),
[App::Default](../../dd/dc2/namespaceApp.html#aa5c64359788d4ae6612cda3aa51227c6a7a1920d61156abc05a60135aefe8bc67),
[set()](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f),
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e),
and
[App::ZERO_BASED](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a9c9fef803506783391e99dfa8ee00dbc).

## ◆ ColorGradient() [2/3]

ColorGradient::ColorGradient  | ( | float  | _fMin_ ,   
---|---|---|---  
|  | float  | _fMax_ ,   
|  | std::size_t  | _usCtColors_ ,   
|  | [ColorBarStyle](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02) | _tS_ ,   
|  | [VisibilityFlags](../../dd/dc2/namespaceApp.html#aad0f0a595677192ca0ecd0f891538f18) | _fl_ = `[Visibility::Default](../../dd/dc2/namespaceApp.html#aa5c64359788d4ae6612cda3aa51227c6a7a1920d61156abc05a60135aefe8bc67)`  
| ) | |   
  
References
[createStandardPacks()](../../dc/df4/classApp_1_1ColorGradient.html#a03da7234b839faecab45d5f07eacdd08),
[set()](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f),
and
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e).

## ◆ ColorGradient() [3/3]

| App::ColorGradient::ColorGradient  | ( | const [ColorGradient](../../dc/df4/classApp_1_1ColorGradient.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## Member Function Documentation

## ◆ createStandardPacks()

| void ColorGradient::createStandardPacks  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[App::ColorModelPack::createBlackWhite()](../../d2/d91/structApp_1_1ColorModelPack.html#aa6c336e098cf85d09d368b02e8a873c8),
[App::ColorModelPack::createBlueGreenRed()](../../d2/d91/structApp_1_1ColorModelPack.html#a751de21f74df8a182f09ab36ccfcc660),
[App::ColorModelPack::createRedGreenBlue()](../../d2/d91/structApp_1_1ColorModelPack.html#a8459719674240c3f3380239bfaeec745),
[App::ColorModelPack::createRedWhiteBlue()](../../d2/d91/structApp_1_1ColorModelPack.html#a39660ef0ed8383622fabf3ab530fa97d),
[App::ColorModelPack::createWhiteBlack()](../../d2/d91/structApp_1_1ColorModelPack.html#aa53b5737c7769e404d21712ade79aa13),
and
[modelPacks](../../dc/df4/classApp_1_1ColorGradient.html#aa063e5d2eb452da11535f725609c106c).

Referenced by
[ColorGradient()](../../dc/df4/classApp_1_1ColorGradient.html#a4acdb3ea165dfe1e1be1644e16622934).

## ◆ getColor()

[Color](../../d3/d3a/classApp_1_1Color.html) App::ColorGradient::getColor  | ( | float  | _fVal_| ) |  const  
---|---|---|---|---|---  
  
References
[isOutOfRange()](../../dc/df4/classApp_1_1ColorGradient.html#a10dbd3ff50be8cb20c9aa00658a7d304),
and
[isOutsideInvisible()](../../dc/df4/classApp_1_1ColorGradient.html#aa9ff837e587d0bf56b6a489a2bf654c6).

Referenced by
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::getPrefColor()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aed0d2ca7140c357c09c3aae8f4bba159),
and
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::setValues()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#aeae62102b8bdfc483bfee73586df265d).

## ◆ getColorIndex()

std::size_t App::ColorGradient::getColorIndex  | ( | float  | _fVal_| ) |  const  
---|---|---|---|---|---  
  
References
[colorField1](../../dc/df4/classApp_1_1ColorGradient.html#a95015c9d532e42c8f831c17a67e394dc),
[colorField2](../../dc/df4/classApp_1_1ColorGradient.html#a09319612bd0ba3d923767be5c3cc3bc7),
[App::FLOW](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a38b13c5b8b7fa5cdbe5e49dbea3cd5b1),
[App::ColorGradientProfile::fMax](../../d3/d16/structApp_1_1ColorGradientProfile.html#a3d62ee50eacfe162f98fd6c5bdf38b43),
[App::ColorGradientProfile::fMin](../../d3/d16/structApp_1_1ColorGradientProfile.html#a8f9cd4700d585d95ca6c84533a046dc7),
[App::ColorField::getColorIndex()](../../d8/da6/classApp_1_1ColorField.html#a9d49ee35d33bdb1224cd3323d5c75fd4),
[App::ColorField::getCountColors()](../../d8/da6/classApp_1_1ColorField.html#a591b9c855412effec4c0a8fbeb1bac65),
[profile](../../dc/df4/classApp_1_1ColorGradient.html#a0609197eb2ad8ba0142139cf40bc5d95),
[App::ColorGradientProfile::tStyle](../../d3/d16/structApp_1_1ColorGradientProfile.html#a392b964ca797dbe7f77a6ca0f4e7fdb0),
and
[App::ZERO_BASED](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a9c9fef803506783391e99dfa8ee00dbc).

## ◆ getColorModel()

const [ColorModel](../../d4/d9e/classApp_1_1ColorModel.html) & App::ColorGradient::getColorModel  | ( | | ) |  const  
---|---|---|---|---  
  
References
[App::ColorModelPack::bottomModel](../../d2/d91/structApp_1_1ColorModelPack.html#a1164f89d8e9b9f1450b06d069799d74d),
[currentModelPack](../../dc/df4/classApp_1_1ColorGradient.html#a382b516bcfeefdbba4a5398f9eab99bf),
[App::ColorGradientProfile::fMax](../../d3/d16/structApp_1_1ColorGradientProfile.html#a3d62ee50eacfe162f98fd6c5bdf38b43),
[App::ColorGradientProfile::fMin](../../d3/d16/structApp_1_1ColorGradientProfile.html#a8f9cd4700d585d95ca6c84533a046dc7),
[profile](../../dc/df4/classApp_1_1ColorGradient.html#a0609197eb2ad8ba0142139cf40bc5d95),
[App::ColorModelPack::topModel](../../d2/d91/structApp_1_1ColorModelPack.html#ac342004df7980cf827544f087e90be45),
[App::ColorModelPack::totalModel](../../d2/d91/structApp_1_1ColorModelPack.html#a947456dc7b944b0f44f904d56ec81ad5),
[App::ColorGradientProfile::tStyle](../../d3/d16/structApp_1_1ColorGradientProfile.html#a392b964ca797dbe7f77a6ca0f4e7fdb0),
and
[App::ZERO_BASED](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a9c9fef803506783391e99dfa8ee00dbc).

## ◆ getColorModelNames()

std::vector< std::string > ColorGradient::getColorModelNames  | ( | | ) |  const  
---|---|---|---|---  
  
References
[modelPacks](../../dc/df4/classApp_1_1ColorGradient.html#aa063e5d2eb452da11535f725609c106c).

Referenced by
[Gui::Dialog::DlgSettingsColorGradientImp::DlgSettingsColorGradientImp()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#ae3f7700b908e7408b3b3eff701dc2f67).

## ◆ getColorModelType()

std::size_t App::ColorGradient::getColorModelType  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getCountColors()

std::size_t App::ColorGradient::getCountColors  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getMaxValue()

float App::ColorGradient::getMaxValue  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getMinColors()

std::size_t ColorGradient::getMinColors  | ( | | ) |  const  
---|---|---|---|---  
  
References
[colorField1](../../dc/df4/classApp_1_1ColorGradient.html#a95015c9d532e42c8f831c17a67e394dc),
[colorField2](../../dc/df4/classApp_1_1ColorGradient.html#a09319612bd0ba3d923767be5c3cc3bc7),
[App::FLOW](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a38b13c5b8b7fa5cdbe5e49dbea3cd5b1),
[App::ColorGradientProfile::fMax](../../d3/d16/structApp_1_1ColorGradientProfile.html#a3d62ee50eacfe162f98fd6c5bdf38b43),
[App::ColorGradientProfile::fMin](../../d3/d16/structApp_1_1ColorGradientProfile.html#a8f9cd4700d585d95ca6c84533a046dc7),
[App::ColorField::getMinColors()](../../d8/da6/classApp_1_1ColorField.html#a1bd15de22d566099550fad78dda190a7),
[profile](../../dc/df4/classApp_1_1ColorGradient.html#a0609197eb2ad8ba0142139cf40bc5d95),
[App::ColorGradientProfile::tStyle](../../d3/d16/structApp_1_1ColorGradientProfile.html#a392b964ca797dbe7f77a6ca0f4e7fdb0),
and
[App::ZERO_BASED](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a9c9fef803506783391e99dfa8ee00dbc).

Referenced by
[set()](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f).

## ◆ getMinValue()

float App::ColorGradient::getMinValue  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getProfile()

const [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) & App::ColorGradient::getProfile  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Gui::Dialog::DlgSettingsColorGradientImp::DlgSettingsColorGradientImp()](../../d7/d7e/classGui_1_1Dialog_1_1DlgSettingsColorGradientImp.html#ae3f7700b908e7408b3b3eff701dc2f67).

## ◆ getRange()

void App::ColorGradient::getRange  | ( | float & | _rfMin_ ,   
---|---|---|---  
|  | float & | _rfMax_  
| ) | |  const  
  
## ◆ getStyle()

[ColorBarStyle](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02) App::ColorGradient::getStyle  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isOutOfRange()

[bool](../../d9/db9/classbool.html) App::ColorGradient::isOutOfRange  | ( | float  | _fVal_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[getColor()](../../dc/df4/classApp_1_1ColorGradient.html#aa6208810fe7eee146cd097696ed5ca60).

## ◆ isOutsideGrayed()

[bool](../../d9/db9/classbool.html) App::ColorGradient::isOutsideGrayed  | ( | | ) |  const  
---|---|---|---|---  
  
References
[App::Grayed](../../dd/dc2/namespaceApp.html#aa5c64359788d4ae6612cda3aa51227c6aa64f9335355b36f6b526e22f7e3fc783).

## ◆ isOutsideInvisible()

[bool](../../d9/db9/classbool.html) App::ColorGradient::isOutsideInvisible  | ( | | ) |  const  
---|---|---|---|---  
  
References
[App::Invisible](../../dd/dc2/namespaceApp.html#aa5c64359788d4ae6612cda3aa51227c6a8bcda43732b0928d269955e0f09ff76f).

Referenced by
[getColor()](../../dc/df4/classApp_1_1ColorGradient.html#aa6208810fe7eee146cd097696ed5ca60).

## ◆ operator=()

| [ColorGradient](../../dc/df4/classApp_1_1ColorGradient.html) & App::ColorGradient::operator=  | ( | const [ColorGradient](../../dc/df4/classApp_1_1ColorGradient.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## ◆ rebuild()

| void ColorGradient::rebuild  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[App::ColorModelPack::bottomModel](../../d2/d91/structApp_1_1ColorModelPack.html#a1164f89d8e9b9f1450b06d069799d74d),
[colorField1](../../dc/df4/classApp_1_1ColorGradient.html#a95015c9d532e42c8f831c17a67e394dc),
[colorField2](../../dc/df4/classApp_1_1ColorGradient.html#a09319612bd0ba3d923767be5c3cc3bc7),
[App::ColorGradientProfile::ctColors](../../d3/d16/structApp_1_1ColorGradientProfile.html#aff3eb9c58def0f2b1af0fe3f2bd3cf52),
[currentModelPack](../../dc/df4/classApp_1_1ColorGradient.html#a382b516bcfeefdbba4a5398f9eab99bf),
[App::FLOW](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a38b13c5b8b7fa5cdbe5e49dbea3cd5b1),
[App::ColorGradientProfile::fMax](../../d3/d16/structApp_1_1ColorGradientProfile.html#a3d62ee50eacfe162f98fd6c5bdf38b43),
[App::ColorGradientProfile::fMin](../../d3/d16/structApp_1_1ColorGradientProfile.html#a8f9cd4700d585d95ca6c84533a046dc7),
[profile](../../dc/df4/classApp_1_1ColorGradient.html#a0609197eb2ad8ba0142139cf40bc5d95),
[App::ColorField::set()](../../d8/da6/classApp_1_1ColorField.html#ac917f8dbb792ec7ab99ceae64e61a7e0),
[App::ColorModelPack::topModel](../../d2/d91/structApp_1_1ColorModelPack.html#ac342004df7980cf827544f087e90be45),
[App::ColorModelPack::totalModel](../../d2/d91/structApp_1_1ColorModelPack.html#a947456dc7b944b0f44f904d56ec81ad5),
[App::ColorGradientProfile::tStyle](../../d3/d16/structApp_1_1ColorGradientProfile.html#a392b964ca797dbe7f77a6ca0f4e7fdb0),
and
[App::ZERO_BASED](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a9c9fef803506783391e99dfa8ee00dbc).

Referenced by
[set()](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f),
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a781330b536c3c39ef1b71d4136177377),
and
[setProfile()](../../dc/df4/classApp_1_1ColorGradient.html#a605d3f2985788c9e89257724c21ee029).

## ◆ set()

void ColorGradient::set  | ( | float  | _fMin_ ,   
---|---|---|---  
|  | float  | _fMax_ ,   
|  | std::size_t  | _usCt_ ,   
|  | [ColorBarStyle](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02) | _tS_ ,   
|  | [VisibilityFlags](../../dd/dc2/namespaceApp.html#aad0f0a595677192ca0ecd0f891538f18) | _fl_  
| ) | |   
  
References
[App::ColorGradientProfile::ctColors](../../d3/d16/structApp_1_1ColorGradientProfile.html#aff3eb9c58def0f2b1af0fe3f2bd3cf52),
[App::ColorGradientProfile::fMax](../../d3/d16/structApp_1_1ColorGradientProfile.html#a3d62ee50eacfe162f98fd6c5bdf38b43),
[App::ColorGradientProfile::fMin](../../d3/d16/structApp_1_1ColorGradientProfile.html#a8f9cd4700d585d95ca6c84533a046dc7),
[getMinColors()](../../dc/df4/classApp_1_1ColorGradient.html#ae6a8116d98df073189b07a90316c8510),
[profile](../../dc/df4/classApp_1_1ColorGradient.html#a0609197eb2ad8ba0142139cf40bc5d95),
[rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
[App::ColorGradientProfile::tStyle](../../d3/d16/structApp_1_1ColorGradientProfile.html#a392b964ca797dbe7f77a6ca0f4e7fdb0),
and
[App::ColorGradientProfile::visibility](../../d3/d16/structApp_1_1ColorGradientProfile.html#add005b330c426798b3582a89fce8e8c2).

Referenced by
[ColorGradient()](../../dc/df4/classApp_1_1ColorGradient.html#a4acdb3ea165dfe1e1be1644e16622934),
and
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297).

## ◆ setColorModel() [1/2]

| void ColorGradient::setColorModel  | ( | | ) |   
---|---|---|---|---  
protected  
  
References
[App::ColorModelPack::bottomModel](../../d2/d91/structApp_1_1ColorModelPack.html#a1164f89d8e9b9f1450b06d069799d74d),
[colorField1](../../dc/df4/classApp_1_1ColorGradient.html#a95015c9d532e42c8f831c17a67e394dc),
[colorField2](../../dc/df4/classApp_1_1ColorGradient.html#a09319612bd0ba3d923767be5c3cc3bc7),
[currentModelPack](../../dc/df4/classApp_1_1ColorGradient.html#a382b516bcfeefdbba4a5398f9eab99bf),
[App::FLOW](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a38b13c5b8b7fa5cdbe5e49dbea3cd5b1),
[modelPacks](../../dc/df4/classApp_1_1ColorGradient.html#aa063e5d2eb452da11535f725609c106c),
[profile](../../dc/df4/classApp_1_1ColorGradient.html#a0609197eb2ad8ba0142139cf40bc5d95),
[App::ColorField::setColorModel()](../../d8/da6/classApp_1_1ColorField.html#a9c7c8385af89ac38951e73c6227b2260),
[App::ColorGradientProfile::tColorModel](../../d3/d16/structApp_1_1ColorGradientProfile.html#ab0d04c4d1aacde397d0976836d626c3b),
[App::ColorModelPack::topModel](../../d2/d91/structApp_1_1ColorModelPack.html#ac342004df7980cf827544f087e90be45),
[App::ColorModelPack::totalModel](../../d2/d91/structApp_1_1ColorModelPack.html#a947456dc7b944b0f44f904d56ec81ad5),
[App::ColorGradientProfile::tStyle](../../d3/d16/structApp_1_1ColorGradientProfile.html#a392b964ca797dbe7f77a6ca0f4e7fdb0),
and
[App::ZERO_BASED](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02a9c9fef803506783391e99dfa8ee00dbc).

Referenced by
[ColorGradient()](../../dc/df4/classApp_1_1ColorGradient.html#a4acdb3ea165dfe1e1be1644e16622934),
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a781330b536c3c39ef1b71d4136177377),
and
[setProfile()](../../dc/df4/classApp_1_1ColorGradient.html#a605d3f2985788c9e89257724c21ee029).

## ◆ setColorModel() [2/2]

void ColorGradient::setColorModel  | ( | std::size_t  | _tModel_| ) |   
---|---|---|---|---|---  
  
References
[profile](../../dc/df4/classApp_1_1ColorGradient.html#a0609197eb2ad8ba0142139cf40bc5d95),
[rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e),
and
[App::ColorGradientProfile::tColorModel](../../d3/d16/structApp_1_1ColorGradientProfile.html#ab0d04c4d1aacde397d0976836d626c3b).

## ◆ setCountColors()

void App::ColorGradient::setCountColors  | ( | std::size_t  | _usCt_| ) |   
---|---|---|---|---|---  
  
## ◆ setOutsideGrayed()

void App::ColorGradient::setOutsideGrayed  | ( | [bool](../../d9/db9/classbool.html) | _value_| ) |   
---|---|---|---|---|---  
  
References
[App::Grayed](../../dd/dc2/namespaceApp.html#aa5c64359788d4ae6612cda3aa51227c6aa64f9335355b36f6b526e22f7e3fc783).

## ◆ setOutsideInvisible()

void App::ColorGradient::setOutsideInvisible  | ( | [bool](../../d9/db9/classbool.html) | _value_| ) |   
---|---|---|---|---|---  
  
References
[App::Invisible](../../dd/dc2/namespaceApp.html#aa5c64359788d4ae6612cda3aa51227c6a8bcda43732b0928d269955e0f09ff76f).

## ◆ setProfile()

void ColorGradient::setProfile  | ( | const [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html) & | _pro_| ) |   
---|---|---|---|---|---  
  
References
[profile](../../dc/df4/classApp_1_1ColorGradient.html#a0609197eb2ad8ba0142139cf40bc5d95),
[rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
and
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e).

## ◆ setRange()

void App::ColorGradient::setRange  | ( | float  | _fMin_ ,   
---|---|---|---  
|  | float  | _fMax_  
| ) | |   
  
## ◆ setStyle()

void App::ColorGradient::setStyle  | ( | [ColorBarStyle](../../dd/dc2/namespaceApp.html#a3550e4a05bc51b10c97a7a4d52685c02) | _tS_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ colorField1

| [ColorField](../../d8/da6/classApp_1_1ColorField.html)
App::ColorGradient::colorField1  
---  
protected  
  
Referenced by
[getColorIndex()](../../dc/df4/classApp_1_1ColorGradient.html#a3245c8dccd95dcfc82fb6de95d03d8a7),
[getMinColors()](../../dc/df4/classApp_1_1ColorGradient.html#ae6a8116d98df073189b07a90316c8510),
[rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
and
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e).

## ◆ colorField2

| [ColorField](../../d8/da6/classApp_1_1ColorField.html)
App::ColorGradient::colorField2  
---  
protected  
  
Referenced by
[getColorIndex()](../../dc/df4/classApp_1_1ColorGradient.html#a3245c8dccd95dcfc82fb6de95d03d8a7),
[getMinColors()](../../dc/df4/classApp_1_1ColorGradient.html#ae6a8116d98df073189b07a90316c8510),
[rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
and
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e).

## ◆ currentModelPack

| [ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html)
App::ColorGradient::currentModelPack  
---  
protected  
  
Referenced by
[getColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#abaceddeba5cb2334d719d79ef7bcbde1),
[rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
and
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e).

## ◆ modelPacks

| std::vector<[ColorModelPack](../../d2/d91/structApp_1_1ColorModelPack.html)>
App::ColorGradient::modelPacks  
---  
protected  
  
Referenced by
[createStandardPacks()](../../dc/df4/classApp_1_1ColorGradient.html#a03da7234b839faecab45d5f07eacdd08),
[getColorModelNames()](../../dc/df4/classApp_1_1ColorGradient.html#aef1af55fe4badb4a6a735fba21e82591),
and
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a4ef04c5e732031f0eb5446e4476dd58e).

## ◆ profile

| [ColorGradientProfile](../../d3/d16/structApp_1_1ColorGradientProfile.html)
App::ColorGradient::profile  
---  
protected  
  
Referenced by
[getColorIndex()](../../dc/df4/classApp_1_1ColorGradient.html#a3245c8dccd95dcfc82fb6de95d03d8a7),
[getColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#abaceddeba5cb2334d719d79ef7bcbde1),
[getMinColors()](../../dc/df4/classApp_1_1ColorGradient.html#ae6a8116d98df073189b07a90316c8510),
[rebuild()](../../dc/df4/classApp_1_1ColorGradient.html#aa8647e21112a9fea341705f24fa77907),
[set()](../../dc/df4/classApp_1_1ColorGradient.html#aebc47495766dcb05abfadb4870fdf37f),
[setColorModel()](../../dc/df4/classApp_1_1ColorGradient.html#a781330b536c3c39ef1b71d4136177377),
and
[setProfile()](../../dc/df4/classApp_1_1ColorGradient.html#a605d3f2985788c9e89257724c21ee029).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ColorModel.h
  * FreeCAD/src/App/ColorModel.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

