---
url: https://freecad.github.io/SourceDoc/d9/dc7/classBase_1_1UnitsSchema.html
scraped_at: 2025-09-08T15:17:42.186777
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [UnitsSchema](../../d9/dc7/classBase_1_1UnitsSchema.html)

[List of all members](../../d9/d3e/classBase_1_1UnitsSchema-members.html) | Public Member Functions

Base::UnitsSchema Class Referenceabstract

The UnitSchema class The subclasses of this class define the stuff for a
certain units schema.
[More...](../../d9/dc7/classBase_1_1UnitsSchema.html#details)

`#include <UnitsSchema.h>`

##  Public Member Functions  
  
---  
virtual void | [resetSchemaUnits](../../d9/dc7/classBase_1_1UnitsSchema.html#a35f563d52fd70672d5a0573387fce90a) ()  
| If you use
[setSchemaUnits()](../../d9/dc7/classBase_1_1UnitsSchema.html#aabcec42ea804cfdde39daf5ee817c8d6
"Gets called if this schema gets activated.") you also have to impment this
method to undo your changes!
[More...](../../d9/dc7/classBase_1_1UnitsSchema.html#a35f563d52fd70672d5a0573387fce90a)  
  
virtual QString | [schemaTranslate](../../d9/dc7/classBase_1_1UnitsSchema.html#a8ff374bff7ebc4f654ed3978080052d7) (const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) &quant, double &factor, QString &unitString)=0  
| This method translates the quantity in a string as the user may expect it.
[More...](../../d9/dc7/classBase_1_1UnitsSchema.html#a8ff374bff7ebc4f654ed3978080052d7)  
  
virtual void | [setSchemaUnits](../../d9/dc7/classBase_1_1UnitsSchema.html#aabcec42ea804cfdde39daf5ee817c8d6) ()  
| Gets called if this schema gets activated.
[More...](../../d9/dc7/classBase_1_1UnitsSchema.html#aabcec42ea804cfdde39daf5ee817c8d6)  
  
QString | [toLocale](../../d9/dc7/classBase_1_1UnitsSchema.html#aacde4020d5617f0e65769350940f0a44) (const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) &quant, double factor, const QString &unitString) const  
virtual | [~UnitsSchema](../../d9/dc7/classBase_1_1UnitsSchema.html#a9ce6e264f497d11e3fdc467a228cafed) ()  
  
## Detailed Description

The UnitSchema class The subclasses of this class define the stuff for a
certain units schema.

## Constructor & Destructor Documentation

## ◆ ~UnitsSchema()

| virtual Base::UnitsSchema::~UnitsSchema  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ resetSchemaUnits()

| virtual void Base::UnitsSchema::resetSchemaUnits  | ( | | ) |   
---|---|---|---|---  
virtual  
  
If you use
[setSchemaUnits()](../../d9/dc7/classBase_1_1UnitsSchema.html#aabcec42ea804cfdde39daf5ee817c8d6
"Gets called if this schema gets activated.") you also have to impment this
method to undo your changes!

## ◆ schemaTranslate()

| virtual QString Base::UnitsSchema::schemaTranslate  | ( | const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _quant_ ,   
---|---|---|---  
|  | double & | _factor_ ,   
|  | QString & | _unitString_  
| ) | |   
pure virtual  
  
This method translates the quantity in a string as the user may expect it.

Implemented in
[Base::UnitsSchemaCentimeters](../../dc/d0e/classBase_1_1UnitsSchemaCentimeters.html#a289742693cf4466036aa1db1ba78959b),
[Base::UnitsSchemaFemMilliMeterNewton](../../df/d2f/classBase_1_1UnitsSchemaFemMilliMeterNewton.html#aa6c39631dcc2e8da9b8212a34b00d785),
[Base::UnitsSchemaImperial1](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialBuilding](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1),
[Base::UnitsSchemaImperialCivil](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
and
[Base::UnitsSchemaMmMin](../../d6/d67/classBase_1_1UnitsSchemaMmMin.html#afe8833459a266486009381109786e8cb).

Referenced by
[Base::Quantity::getUserString()](../../d8/d18/classBase_1_1Quantity.html#adbec8b893054c2ca1cd04d88c421ab45).

## ◆ setSchemaUnits()

| virtual void Base::UnitsSchema::setSchemaUnits  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Gets called if this schema gets activated.

Here it's theoretically possible that you can change the static factors for
certain units (e.g. mi = 1,8km instead of mi=1.6km).

## ◆ toLocale()

QString UnitsSchema::toLocale  | ( | const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _quant_ ,   
---|---|---|---  
|  | double  | _factor_ ,   
|  | const QString & | _unitString_  
| ) | |  const  
  
References
[Base::Quantity::getFormat()](../../d8/d18/classBase_1_1Quantity.html#a5674edba6d0574ed73bb2610fb590656),
[Base::Quantity::getValue()](../../d8/d18/classBase_1_1Quantity.html#a692b9e4043999d2c24737886639df7d0),
and
[Base::QuantityFormat::option](../../d9/d33/structBase_1_1QuantityFormat.html#a339a8b78ab2735dce6966e877eb72c8f).

Referenced by
[Base::UnitsSchemaCentimeters::schemaTranslate()](../../dc/d0e/classBase_1_1UnitsSchemaCentimeters.html#a289742693cf4466036aa1db1ba78959b),
[Base::UnitsSchemaFemMilliMeterNewton::schemaTranslate()](../../df/d2f/classBase_1_1UnitsSchemaFemMilliMeterNewton.html#aa6c39631dcc2e8da9b8212a34b00d785),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialBuilding::schemaTranslate()](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
and
[Base::UnitsSchemaMmMin::schemaTranslate()](../../d6/d67/classBase_1_1UnitsSchemaMmMin.html#afe8833459a266486009381109786e8cb).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/UnitsSchema.h
  * FreeCAD/src/Base/UnitsSchema.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

