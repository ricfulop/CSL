---
url: https://freecad.github.io/SourceDoc/d9/d33/structBase_1_1QuantityFormat.html
scraped_at: 2025-09-08T15:17:03.026610
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html)

[List of all members](../../dd/d87/structBase_1_1QuantityFormat-members.html) | Public Types | Public Member Functions | Static Public Member Functions | Public Attributes | Static Public Attributes

Base::QuantityFormat Struct Reference

`#include <Quantity.h>`

##  Public Types  
  
---  
enum | [NumberFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679) { [Default](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679a4decd52211cc4ee023d485a6f8c78ea0) = 0 , [Fixed](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679a0d3044ed8b3d5103428ea61e645e31ed) = 1 , [Scientific](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679a2cf5c90ec2a6ccf3ff53de835ae7f8b0) = 2 }  
enum | [NumberOption](../../d9/d33/structBase_1_1QuantityFormat.html#a392dcaf9aaa0a04b3e255505528929ec) { }  
typedef [int](../../d1/da0/classint.html) | [NumberOptions](../../d9/d33/structBase_1_1QuantityFormat.html#a223e02e19e138ab79a22ee2c40e57b7b)  
  
##  Public Member Functions  
  
---  
[int](../../d1/da0/classint.html) | [getDenominator](../../d9/d33/structBase_1_1QuantityFormat.html#a181a6782154d2561ca1409093fdbc98d) () const  
|
[QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a0a162675c4bd5b6e8763586e467b28bd)
()  
|
[QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a4715e9edb30bf3d337ca2779e4aec039)
([NumberFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679)
[format](../../d9/d33/structBase_1_1QuantityFormat.html#a72c5baf9b89c433716e8ea6f1072c520),
[int](../../d1/da0/classint.html) decimals=-1)  
void | [setDenominator](../../d9/d33/structBase_1_1QuantityFormat.html#a006e0569aec5bdb69dab0159aa69da98) ([int](../../d1/da0/classint.html) denom)  
char | [toFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a018fbf0aa222725335a74d62be39a834) () const  
  
##  Static Public Member Functions  
  
---  
static [int](../../d1/da0/classint.html) | [getDefaultDenominator](../../d9/d33/structBase_1_1QuantityFormat.html#a4b4f0be807e930e40ce9b723619aa51a) ()  
static void | [setDefaultDenominator](../../d9/d33/structBase_1_1QuantityFormat.html#aacb1b910b4aff02b865fca455e538778) ([int](../../d1/da0/classint.html) denom)  
static [NumberFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679) | [toFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a8a2153386791490dca38a5be4bb16e57) (char c, [bool](../../d9/db9/classbool.html) *ok=nullptr)  
  
##  Public Attributes  
  
---  
[int](../../d1/da0/classint.html) | [denominator](../../d9/d33/structBase_1_1QuantityFormat.html#ac8f7b4ab348d9fc5520997904ca7ad1b)  
[NumberFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679) | [format](../../d9/d33/structBase_1_1QuantityFormat.html#a72c5baf9b89c433716e8ea6f1072c520)  
[NumberOptions](../../d9/d33/structBase_1_1QuantityFormat.html#a223e02e19e138ab79a22ee2c40e57b7b) | [option](../../d9/d33/structBase_1_1QuantityFormat.html#a339a8b78ab2735dce6966e877eb72c8f)  
[int](../../d1/da0/classint.html) | [precision](../../d9/d33/structBase_1_1QuantityFormat.html#a675cc8c56f715e59297ca516f68fca38)  
  
##  Static Public Attributes  
  
---  
static [int](../../d1/da0/classint.html) | [defaultDenominator](../../d9/d33/structBase_1_1QuantityFormat.html#a9ce84814d7fc4a43af112fcd13500af6) = 8  
  
## Member Typedef Documentation

## ◆ NumberOptions

typedef [int](../../d1/da0/classint.html)
[Base::QuantityFormat::NumberOptions](../../d9/d33/structBase_1_1QuantityFormat.html#a223e02e19e138ab79a22ee2c40e57b7b)  
---  
  
## Member Enumeration Documentation

## ◆ NumberFormat

enum
[Base::QuantityFormat::NumberFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679)  
---  
  
Enumerator  
---  
Default |   
Fixed |   
Scientific |   
  
## ◆ NumberOption

enum
[Base::QuantityFormat::NumberOption](../../d9/d33/structBase_1_1QuantityFormat.html#a392dcaf9aaa0a04b3e255505528929ec)  
---  
  
Enumerator  
---  
OmitGroupSeparator |   
RejectGroupSeparator |   
  
## Constructor & Destructor Documentation

## ◆ QuantityFormat() [1/2]

QuantityFormat::QuantityFormat  | ( | | ) |   
---|---|---|---|---  
  
## ◆ QuantityFormat() [2/2]

QuantityFormat::QuantityFormat  | ( | [QuantityFormat::NumberFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679) | _format_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _decimals_ = `-1`  
| ) | |   
  
## Member Function Documentation

## ◆ getDefaultDenominator()

| static [int](../../d1/da0/classint.html) Base::QuantityFormat::getDefaultDenominator  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[Gui::Dialog::DlgSettingsUnitsImp::loadSettings()](../../d0/df7/classGui_1_1Dialog_1_1DlgSettingsUnitsImp.html#a7127945a0e61f55905a60f534f9aca72).

## ◆ getDenominator()

[int](../../d1/da0/classint.html) Base::QuantityFormat::getDenominator  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Base::UnitsSchemaImperialBuilding::schemaTranslate()](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1).

## ◆ setDefaultDenominator()

| static void Base::QuantityFormat::setDefaultDenominator  | ( | [int](../../d1/da0/classint.html) | _denom_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[Gui::Dialog::DlgSettingsUnitsImp::saveSettings()](../../d0/df7/classGui_1_1Dialog_1_1DlgSettingsUnitsImp.html#a8d256a71443e4ab9de3df9e072c2f67e).

## ◆ setDenominator()

void Base::QuantityFormat::setDenominator  | ( | [int](../../d1/da0/classint.html) | _denom_| ) |   
---|---|---|---|---|---  
  
## ◆ toFormat() [1/2]

char Base::QuantityFormat::toFormat  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Gui::InputField::getFormat()](../../da/dfa/classGui_1_1InputField.html#a829971d0d777421c8572b1c0786044bc),
[Gui::InputField::setFormat()](../../da/dfa/classGui_1_1InputField.html#a25118d14b9aa233f5b604fdd6ae35abe),
and
[Base::UnitsApi::sToNumber()](../../d9/d89/classBase_1_1UnitsApi.html#a29ba3277698f56d720819a191df758c6).

## ◆ toFormat() [2/2]

| static [NumberFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679) Base::QuantityFormat::toFormat  | ( | char  | _c_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) *  | _ok_ = `nullptr`  
| ) | |   
static  
  
## Member Data Documentation

## ◆ defaultDenominator

| [int](../../d1/da0/classint.html) QuantityFormat::defaultDenominator = 8  
---  
static  
  
## ◆ denominator

[int](../../d1/da0/classint.html) Base::QuantityFormat::denominator  
---  
  
## ◆ format

[NumberFormat](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679)
Base::QuantityFormat::format  
---  
  
Referenced by
[Gui::InputField::selectNumber()](../../da/dfa/classGui_1_1InputField.html#a2ef97ec6fa3cd0afc02bbe2938e136ba),
[Gui::InputField::setFormat()](../../da/dfa/classGui_1_1InputField.html#a25118d14b9aa233f5b604fdd6ae35abe),
and
[Base::UnitsApi::sToNumber()](../../d9/d89/classBase_1_1UnitsApi.html#a29ba3277698f56d720819a191df758c6).

## ◆ option

[NumberOptions](../../d9/d33/structBase_1_1QuantityFormat.html#a223e02e19e138ab79a22ee2c40e57b7b)
Base::QuantityFormat::option  
---  
  
Referenced by
[Sketcher::Constraint::getPresentationValue()](../../d6/def/classSketcher_1_1Constraint.html#a9be53639cd1e5e49f23c61862430874b),
and
[Base::UnitsSchema::toLocale()](../../d9/dc7/classBase_1_1UnitsSchema.html#aacde4020d5617f0e65769350940f0a44).

## ◆ precision

[int](../../d1/da0/classint.html) Base::QuantityFormat::precision  
---  
  
Referenced by
[Gui::InputField::getPrecision()](../../da/dfa/classGui_1_1InputField.html#ad5dbff9b9e32c81853213819aef1ec07),
[ifc2x3.ifcgeometricrepresentationsubcontext::ifcgeometricrepresentationcontext_precision()](../../d3/df1/classifc2x3_1_1ifcgeometricrepresentationsubcontext.html#a918da7dd0ad0b5069f69c8536d964b9a),
[ifc4.ifcgeometricrepresentationsubcontext::ifcgeometricrepresentationcontext_precision()](../../da/da9/classifc4_1_1ifcgeometricrepresentationsubcontext.html#abcdc404924af4e5b5e82a90c0acfe56f),
[Gui::QuantitySpinBox::setDecimals()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#a16561da1a6cdbeb3b4a1f87e8af69bbb),
[Gui::InputField::setPrecision()](../../da/dfa/classGui_1_1InputField.html#aa5214b250f577c5f53ce0f4e74140566),
and
[Base::UnitsApi::sToNumber()](../../d9/d89/classBase_1_1UnitsApi.html#a29ba3277698f56d720819a191df758c6).

* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/Base/Quantity.h
  * FreeCAD/src/Base/Quantity.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

