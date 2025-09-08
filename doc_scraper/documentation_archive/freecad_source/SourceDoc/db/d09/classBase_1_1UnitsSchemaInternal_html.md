---
url: https://freecad.github.io/SourceDoc/db/d09/classBase_1_1UnitsSchemaInternal.html
scraped_at: 2025-09-08T15:17:49.226901
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [UnitsSchemaInternal](../../db/d09/classBase_1_1UnitsSchemaInternal.html)

[List of all members](../../db/daf/classBase_1_1UnitsSchemaInternal-members.html) | Public Member Functions

Base::UnitsSchemaInternal Class Reference

The standard units schema Here is defined what internal (base) units FreeCAD
uses. [More...](../../db/d09/classBase_1_1UnitsSchemaInternal.html#details)

`#include <UnitsSchemaInternal.h>`

##  Public Member Functions  
  
---  
virtual QString | [schemaTranslate](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d) (const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) &quant, double &factor, QString &unitString)  
| This method translates the quantity in a string as the user may expect it.
[More...](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d)  
  
![-](../../closed.png) Public Member Functions inherited from
[Base::UnitsSchema](../../d9/dc7/classBase_1_1UnitsSchema.html)  
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

The standard units schema Here is defined what internal (base) units FreeCAD
uses.

FreeCAD uses a mm/kg/deg scala. Also it defines how the units get presented.

## Member Function Documentation

## ◆ schemaTranslate()

| QString UnitsSchemaInternal::schemaTranslate  | ( | const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _quant_ ,   
---|---|---|---  
|  | double & | _factor_ ,   
|  | QString & | _unitString_  
| ) | |   
virtual  
  
This method translates the quantity in a string as the user may expect it.

Implements
[Base::UnitsSchema](../../d9/dc7/classBase_1_1UnitsSchema.html#a8ff374bff7ebc4f654ed3978080052d7).

References
[Base::Unit::Angle](../../d2/d37/classBase_1_1Unit.html#a650f972468df9938bacbcafdd4b443e1),
[Base::Unit::Area](../../d2/d37/classBase_1_1Unit.html#ab3d42609406d023f6818a88433f685c4),
[Base::Unit::Density](../../d2/d37/classBase_1_1Unit.html#ab892acba15d70afcb6f1750f5d43c872),
[Base::Unit::DynamicViscosity](../../d2/d37/classBase_1_1Unit.html#a58a99db29eda15c2e8078d57627c74a4),
[Base::Unit::ElectricalCapacitance](../../d2/d37/classBase_1_1Unit.html#ab6b968419a79de2df25c93d80245a301),
[Base::Unit::ElectricalConductance](../../d2/d37/classBase_1_1Unit.html#a6bf7a95ca4739d61dfd0a09c99ea0562),
[Base::Unit::ElectricalConductivity](../../d2/d37/classBase_1_1Unit.html#a4c3a665642892f0b37a2c36067816195),
[Base::Unit::ElectricalInductance](../../d2/d37/classBase_1_1Unit.html#a0b8ddf7c558b2ef2c48fcbc209d7b441),
[Base::Unit::ElectricalResistance](../../d2/d37/classBase_1_1Unit.html#a630e9d931f2bced410b5a31e16a32ce8),
[Base::Unit::ElectricCharge](../../d2/d37/classBase_1_1Unit.html#a4b45018a18e2998bf656373194da4b7f),
[Base::Unit::ElectricPotential](../../d2/d37/classBase_1_1Unit.html#a6ccd1a3bf9174cfa07613b3158c63845),
[Base::Unit::Force](../../d2/d37/classBase_1_1Unit.html#a310daf6b91125572541d4fad81832d42),
[Base::Unit::Frequency](../../d2/d37/classBase_1_1Unit.html#a7539ffede82a01fb8eedeb5a532a0d75),
[Base::Unit::getString()](../../d2/d37/classBase_1_1Unit.html#ae403a424663d4df4b4a4886093ed07d1),
[Base::Quantity::getUnit()](../../d8/d18/classBase_1_1Quantity.html#acf401f989cc46b7c864565e89113ede4),
[Base::Quantity::getValue()](../../d8/d18/classBase_1_1Quantity.html#a692b9e4043999d2c24737886639df7d0),
[Base::Unit::HeatFlux](../../d2/d37/classBase_1_1Unit.html#a7966aba69328a335f7821ff0a18fd116),
[Base::Unit::KinematicViscosity](../../d2/d37/classBase_1_1Unit.html#ab862d4dc1e0c4b573f1e85bb2f7509bc),
[Base::Unit::Length](../../d2/d37/classBase_1_1Unit.html#ae7af32a08ea9a0e1501571a2902c84bd),
[Base::Unit::MagneticFieldStrength](../../d2/d37/classBase_1_1Unit.html#aa5568a2eef26248858f8828b86185c36),
[Base::Unit::MagneticFlux](../../d2/d37/classBase_1_1Unit.html#a8109c4e89e27270a40a062f3ced30ee0),
[Base::Unit::MagneticFluxDensity](../../d2/d37/classBase_1_1Unit.html#a040d981e6addd904e5d34b03be6dee82),
[Base::Unit::Mass](../../d2/d37/classBase_1_1Unit.html#a0487599b7ddcb19c431b2e5522af173a),
[Base::Unit::Power](../../d2/d37/classBase_1_1Unit.html#a6136199d4b9d4233a1df216e84f72fe0),
[Base::Unit::Pressure](../../d2/d37/classBase_1_1Unit.html#ab0df485d964692e00f0b0006afb2068f),
[Base::Unit::SpecificEnergy](../../d2/d37/classBase_1_1Unit.html#aadff4085546b98c8766526c873c98bc7),
[Base::Unit::SpecificHeat](../../d2/d37/classBase_1_1Unit.html#ab81d44e306380c8e1dac197bcea5d71d),
[Base::Unit::Stiffness](../../d2/d37/classBase_1_1Unit.html#a76655c5122e0c7b016cdabd9d41785ee),
[Base::Unit::Stress](../../d2/d37/classBase_1_1Unit.html#a2f0238ae4983fe1a1e5bc639607f35e7),
[Base::Unit::ThermalConductivity](../../d2/d37/classBase_1_1Unit.html#a7e056814cbd902bdb02586b8950b54a4),
[Base::Unit::ThermalExpansionCoefficient](../../d2/d37/classBase_1_1Unit.html#a57b0f88cac2a96eccb99d55753d248a5),
[Base::Unit::ThermalTransferCoefficient](../../d2/d37/classBase_1_1Unit.html#a17131da1b00f1bdc0a85e685752ee24a),
[Base::UnitsSchema::toLocale()](../../d9/dc7/classBase_1_1UnitsSchema.html#aacde4020d5617f0e65769350940f0a44),
[Base::Unit::Velocity](../../d2/d37/classBase_1_1Unit.html#ac8f332f96770356aa6c6712a108b3410),
[Base::Unit::Volume](../../d2/d37/classBase_1_1Unit.html#a0384d7597ade62ef6c880f84918a672f),
[Base::Unit::VolumetricThermalExpansionCoefficient](../../d2/d37/classBase_1_1Unit.html#a579b2c39261f82d71ccf4835fa117208),
and
[Base::Unit::Work](../../d2/d37/classBase_1_1Unit.html#a3a3ef1053b57fe85182b8befe4cb1984).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/UnitsSchemaInternal.h
  * FreeCAD/src/Base/UnitsSchemaInternal.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

