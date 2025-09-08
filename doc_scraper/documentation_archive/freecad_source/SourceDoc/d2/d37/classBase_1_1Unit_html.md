---
url: https://freecad.github.io/SourceDoc/d2/d37/classBase_1_1Unit.html
scraped_at: 2025-09-08T15:17:38.270624
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Unit](../../d2/d37/classBase_1_1Unit.html)

[List of all members](../../de/df3/classBase_1_1Unit-members.html) | Public Member Functions | Static Public Attributes | Protected Attributes

Base::Unit Class Reference

The [Unit](../../d2/d37/classBase_1_1Unit.html "The Unit class.") class.
[More...](../../d2/d37/classBase_1_1Unit.html#details)

`#include <Unit.h>`

##  Public Member Functions  
  
---  
const [UnitSignature](../../d0/d2c/structBase_1_1UnitSignature.html) & | [getSignature](../../d2/d37/classBase_1_1Unit.html#aace9457aa3c8fcedf649db9f00b6dd5a) () const  
| get the unit signature
[More...](../../d2/d37/classBase_1_1Unit.html#aace9457aa3c8fcedf649db9f00b6dd5a)  
  
QString | [getString](../../d2/d37/classBase_1_1Unit.html#ae403a424663d4df4b4a4886093ed07d1) () const  
QString | [getTypeString](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89) () const  
| get the type as an string such as "Area", "Length" or "Pressure".
[More...](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89)  
  
[bool](../../d9/db9/classbool.html) | [isEmpty](../../d2/d37/classBase_1_1Unit.html#ada74af04cdf593999be6be0ae39b22ba) () const  
[bool](../../d9/db9/classbool.html) | [operator!=](../../d2/d37/classBase_1_1Unit.html#a5583334a1659da9e8c9cda2dca303a30) (const [Unit](../../d2/d37/classBase_1_1Unit.html) &that) const  
[Unit](../../d2/d37/classBase_1_1Unit.html) | [operator*](../../d2/d37/classBase_1_1Unit.html#a043243f070571191708527ba23ac071e) (const [Unit](../../d2/d37/classBase_1_1Unit.html) &) const  
[Unit](../../d2/d37/classBase_1_1Unit.html) & | [operator*=](../../d2/d37/classBase_1_1Unit.html#a6474ce97c100e46598a0971c769c05fb) (const [Unit](../../d2/d37/classBase_1_1Unit.html) &that)  
| Operators.
[More...](../../d2/d37/classBase_1_1Unit.html#a6474ce97c100e46598a0971c769c05fb)  
  
[Unit](../../d2/d37/classBase_1_1Unit.html) | [operator/](../../d2/d37/classBase_1_1Unit.html#a6109f301f1e75c08096d1ca42279f219) (const [Unit](../../d2/d37/classBase_1_1Unit.html) &) const  
[Unit](../../d2/d37/classBase_1_1Unit.html) & | [operator/=](../../d2/d37/classBase_1_1Unit.html#a690fe8be29f0ab75cf6318655cc2ef6f) (const [Unit](../../d2/d37/classBase_1_1Unit.html) &that)  
[Unit](../../d2/d37/classBase_1_1Unit.html) & | [operator=](../../d2/d37/classBase_1_1Unit.html#a1981d99d235268e51895f8bf3944d4a7) (const [Unit](../../d2/d37/classBase_1_1Unit.html) &)  
[bool](../../d9/db9/classbool.html) | [operator==](../../d2/d37/classBase_1_1Unit.html#a1742f0ce386adb69a82f9230251e7aed) (const [Unit](../../d2/d37/classBase_1_1Unit.html) &) const  
[Unit](../../d2/d37/classBase_1_1Unit.html) | [pow](../../d2/d37/classBase_1_1Unit.html#a0b551d733e192f041457de60a3573341) (signed char exp) const  
|
[Unit](../../d2/d37/classBase_1_1Unit.html#a8e46f663a95736c8002d85ab271a7581)
()  
|
[Unit](../../d2/d37/classBase_1_1Unit.html#abbfe43509b2db5c3403ae90c3ef0b5d8)
(const QString &expr)  
|
[Unit](../../d2/d37/classBase_1_1Unit.html#ae7351c99c228ee3bad29e47a8716aa22)
(const [Unit](../../d2/d37/classBase_1_1Unit.html) &)  
|
[Unit](../../d2/d37/classBase_1_1Unit.html#a333922c4cc697ff97090f5dedf911660)
(int8_t
[Length](../../d2/d37/classBase_1_1Unit.html#ae7af32a08ea9a0e1501571a2902c84bd),
int8_t
[Mass](../../d2/d37/classBase_1_1Unit.html#a0487599b7ddcb19c431b2e5522af173a)=0,
int8_t Time=0, int8_t
[ElectricCurrent](../../d2/d37/classBase_1_1Unit.html#a70bf7f2abeded9984fcf653866a7ae8c)=0,
int8_t ThermodynamicTemperature=0, int8_t
[AmountOfSubstance](../../d2/d37/classBase_1_1Unit.html#a19646ae3d87766a019c9077fbd0fe4fa)=0,
int8_t
[LuminousIntensity](../../d2/d37/classBase_1_1Unit.html#a6651f96686f2c2b533307d3c419edcc3)=0,
int8_t
[Angle](../../d2/d37/classBase_1_1Unit.html#a650f972468df9938bacbcafdd4b443e1)=0)  
| default constructor
[More...](../../d2/d37/classBase_1_1Unit.html#a333922c4cc697ff97090f5dedf911660)  
  
|
[~Unit](../../d2/d37/classBase_1_1Unit.html#af280fb5d9d07cfaad4ee63f370c3341c)
()  
| Destruction.
[More...](../../d2/d37/classBase_1_1Unit.html#af280fb5d9d07cfaad4ee63f370c3341c)  
  
  
##  Static Public Attributes  
  
---  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Acceleration](../../d2/d37/classBase_1_1Unit.html#ad982b0bf22eca89df35f10143c001d8a)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [AmountOfSubstance](../../d2/d37/classBase_1_1Unit.html#a19646ae3d87766a019c9077fbd0fe4fa)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Angle](../../d2/d37/classBase_1_1Unit.html#a650f972468df9938bacbcafdd4b443e1)  
| Angle.
[More...](../../d2/d37/classBase_1_1Unit.html#a650f972468df9938bacbcafdd4b443e1)  
  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [AngleOfFriction](../../d2/d37/classBase_1_1Unit.html#a027495072dbcd4431b779e1e44a6deeb)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Area](../../d2/d37/classBase_1_1Unit.html#ab3d42609406d023f6818a88433f685c4)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [CompressiveStrength](../../d2/d37/classBase_1_1Unit.html#af9667c3341cfd1ddd021e4f9aae8eb9d)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Density](../../d2/d37/classBase_1_1Unit.html#ab892acba15d70afcb6f1750f5d43c872)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [DynamicViscosity](../../d2/d37/classBase_1_1Unit.html#a58a99db29eda15c2e8078d57627c74a4)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ElectricalCapacitance](../../d2/d37/classBase_1_1Unit.html#ab6b968419a79de2df25c93d80245a301)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ElectricalConductance](../../d2/d37/classBase_1_1Unit.html#a6bf7a95ca4739d61dfd0a09c99ea0562)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ElectricalConductivity](../../d2/d37/classBase_1_1Unit.html#a4c3a665642892f0b37a2c36067816195)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ElectricalInductance](../../d2/d37/classBase_1_1Unit.html#a0b8ddf7c558b2ef2c48fcbc209d7b441)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ElectricalResistance](../../d2/d37/classBase_1_1Unit.html#a630e9d931f2bced410b5a31e16a32ce8)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ElectricCharge](../../d2/d37/classBase_1_1Unit.html#a4b45018a18e2998bf656373194da4b7f)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ElectricCurrent](../../d2/d37/classBase_1_1Unit.html#a70bf7f2abeded9984fcf653866a7ae8c)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ElectricPotential](../../d2/d37/classBase_1_1Unit.html#a6ccd1a3bf9174cfa07613b3158c63845)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Force](../../d2/d37/classBase_1_1Unit.html#a310daf6b91125572541d4fad81832d42)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Frequency](../../d2/d37/classBase_1_1Unit.html#a7539ffede82a01fb8eedeb5a532a0d75)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [HeatFlux](../../d2/d37/classBase_1_1Unit.html#a7966aba69328a335f7821ff0a18fd116)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [KinematicViscosity](../../d2/d37/classBase_1_1Unit.html#ab862d4dc1e0c4b573f1e85bb2f7509bc)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Length](../../d2/d37/classBase_1_1Unit.html#ae7af32a08ea9a0e1501571a2902c84bd)  
| Predefined [Unit](../../d2/d37/classBase_1_1Unit.html "The Unit class.")
types.
[More...](../../d2/d37/classBase_1_1Unit.html#ae7af32a08ea9a0e1501571a2902c84bd)  
  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [LuminousIntensity](../../d2/d37/classBase_1_1Unit.html#a6651f96686f2c2b533307d3c419edcc3)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [MagneticFieldStrength](../../d2/d37/classBase_1_1Unit.html#aa5568a2eef26248858f8828b86185c36)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [MagneticFlux](../../d2/d37/classBase_1_1Unit.html#a8109c4e89e27270a40a062f3ced30ee0)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [MagneticFluxDensity](../../d2/d37/classBase_1_1Unit.html#a040d981e6addd904e5d34b03be6dee82)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Mass](../../d2/d37/classBase_1_1Unit.html#a0487599b7ddcb19c431b2e5522af173a)  
| Mass unit.
[More...](../../d2/d37/classBase_1_1Unit.html#a0487599b7ddcb19c431b2e5522af173a)  
  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Power](../../d2/d37/classBase_1_1Unit.html#a6136199d4b9d4233a1df216e84f72fe0)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Pressure](../../d2/d37/classBase_1_1Unit.html#ab0df485d964692e00f0b0006afb2068f)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ShearModulus](../../d2/d37/classBase_1_1Unit.html#ac0f4fcfb3effa0dc0468c439072f0a7b)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [SpecificEnergy](../../d2/d37/classBase_1_1Unit.html#aadff4085546b98c8766526c873c98bc7)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [SpecificHeat](../../d2/d37/classBase_1_1Unit.html#ab81d44e306380c8e1dac197bcea5d71d)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Stiffness](../../d2/d37/classBase_1_1Unit.html#a76655c5122e0c7b016cdabd9d41785ee)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Stress](../../d2/d37/classBase_1_1Unit.html#a2f0238ae4983fe1a1e5bc639607f35e7)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Temperature](../../d2/d37/classBase_1_1Unit.html#a2ef93d33b9d08b1c44d3324fde41af56)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ThermalConductivity](../../d2/d37/classBase_1_1Unit.html#a7e056814cbd902bdb02586b8950b54a4)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ThermalExpansionCoefficient](../../d2/d37/classBase_1_1Unit.html#a57b0f88cac2a96eccb99d55753d248a5)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [ThermalTransferCoefficient](../../d2/d37/classBase_1_1Unit.html#a17131da1b00f1bdc0a85e685752ee24a)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [TimeSpan](../../d2/d37/classBase_1_1Unit.html#ad667348b5bcef2a7a03de73580ef3827)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [UltimateTensileStrength](../../d2/d37/classBase_1_1Unit.html#ae00d4241224ec38975de5f1cfd955684)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [VacuumPermittivity](../../d2/d37/classBase_1_1Unit.html#adce70257023fc90d88fc2b0d8557a51c)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Velocity](../../d2/d37/classBase_1_1Unit.html#ac8f332f96770356aa6c6712a108b3410)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Volume](../../d2/d37/classBase_1_1Unit.html#a0384d7597ade62ef6c880f84918a672f)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [VolumetricThermalExpansionCoefficient](../../d2/d37/classBase_1_1Unit.html#a579b2c39261f82d71ccf4835fa117208)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [Work](../../d2/d37/classBase_1_1Unit.html#a3a3ef1053b57fe85182b8befe4cb1984)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [YieldStrength](../../d2/d37/classBase_1_1Unit.html#abe82124eb877b11f843099e8d9343034)  
static [Unit](../../d2/d37/classBase_1_1Unit.html) | [YoungsModulus](../../d2/d37/classBase_1_1Unit.html#a53b50638ce4cdfcda9658c506ccd3012)  
  
##  Protected Attributes  
  
---  
[UnitSignature](../../d0/d2c/structBase_1_1UnitSignature.html) | [Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6)  
  
## Detailed Description

The [Unit](../../d2/d37/classBase_1_1Unit.html "The Unit class.") class.

## Constructor & Destructor Documentation

## ◆ Unit() [1/4]

Unit::Unit  | ( | int8_t  | _Length_ ,   
---|---|---|---  
|  | int8_t  | _Mass_ = `0`,   
|  | int8_t  | _Time_ = `0`,   
|  | int8_t  | _ElectricCurrent_ = `0`,   
|  | int8_t  | _ThermodynamicTemperature_ = `0`,   
|  | int8_t  | _AmountOfSubstance_ = `0`,   
|  | int8_t  | _LuminousIntensity_ = `0`,   
|  | int8_t  | _Angle_ = `0`  
| ) | |   
  
default constructor

References
[Base::UnitSignature::AmountOfSubstance](../../d0/d2c/structBase_1_1UnitSignature.html#adbda0d439a7e93b43b4783d0bb326f49),
[AmountOfSubstance](../../d2/d37/classBase_1_1Unit.html#a19646ae3d87766a019c9077fbd0fe4fa),
[Base::UnitSignature::Angle](../../d0/d2c/structBase_1_1UnitSignature.html#ab0c72a128c708fb38392cb8b29e0b14d),
[Angle](../../d2/d37/classBase_1_1Unit.html#a650f972468df9938bacbcafdd4b443e1),
[Base::UnitSignature::ElectricCurrent](../../d0/d2c/structBase_1_1UnitSignature.html#a28e50326f63c30a25293bbdee189f76c),
[ElectricCurrent](../../d2/d37/classBase_1_1Unit.html#a70bf7f2abeded9984fcf653866a7ae8c),
[Base::UnitSignature::Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Length](../../d2/d37/classBase_1_1Unit.html#ae7af32a08ea9a0e1501571a2902c84bd),
[Base::UnitSignature::LuminousIntensity](../../d0/d2c/structBase_1_1UnitSignature.html#af0120f04df20be40248efc75ec9fc00a),
[LuminousIntensity](../../d2/d37/classBase_1_1Unit.html#a6651f96686f2c2b533307d3c419edcc3),
[Base::UnitSignature::Mass](../../d0/d2c/structBase_1_1UnitSignature.html#a9a0beec4a0fc85341679bed98c5c979f),
[Mass](../../d2/d37/classBase_1_1Unit.html#a0487599b7ddcb19c431b2e5522af173a),
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6),
[Base::UnitSignature::ThermodynamicTemperature](../../d0/d2c/structBase_1_1UnitSignature.html#a171c9b90aff6d96c99fe77f951efd62a),
and
[Base::UnitSignature::Time](../../d0/d2c/structBase_1_1UnitSignature.html#a984f0b070a4e3a1bfd1c123d85644106).

## ◆ Unit() [2/4]

Unit::Unit  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::UnitSignature::AmountOfSubstance](../../d0/d2c/structBase_1_1UnitSignature.html#adbda0d439a7e93b43b4783d0bb326f49),
[Base::UnitSignature::Angle](../../d0/d2c/structBase_1_1UnitSignature.html#ab0c72a128c708fb38392cb8b29e0b14d),
[Base::UnitSignature::ElectricCurrent](../../d0/d2c/structBase_1_1UnitSignature.html#a28e50326f63c30a25293bbdee189f76c),
[Base::UnitSignature::Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::UnitSignature::LuminousIntensity](../../d0/d2c/structBase_1_1UnitSignature.html#af0120f04df20be40248efc75ec9fc00a),
[Base::UnitSignature::Mass](../../d0/d2c/structBase_1_1UnitSignature.html#a9a0beec4a0fc85341679bed98c5c979f),
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6),
[Base::UnitSignature::ThermodynamicTemperature](../../d0/d2c/structBase_1_1UnitSignature.html#a171c9b90aff6d96c99fe77f951efd62a),
and
[Base::UnitSignature::Time](../../d0/d2c/structBase_1_1UnitSignature.html#a984f0b070a4e3a1bfd1c123d85644106).

## ◆ Unit() [3/4]

Unit::Unit  | ( | const [Unit](../../d2/d37/classBase_1_1Unit.html) & | _that_| ) |   
---|---|---|---|---|---  
  
References
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6).

## ◆ Unit() [4/4]

| Unit::Unit  | ( | const QString & | _expr_| ) |   
---|---|---|---|---|---  
explicit  
  
References
[Base::UnitSignature::AmountOfSubstance](../../d0/d2c/structBase_1_1UnitSignature.html#adbda0d439a7e93b43b4783d0bb326f49),
[Base::UnitSignature::Angle](../../d0/d2c/structBase_1_1UnitSignature.html#ab0c72a128c708fb38392cb8b29e0b14d),
[Base::UnitSignature::ElectricCurrent](../../d0/d2c/structBase_1_1UnitSignature.html#a28e50326f63c30a25293bbdee189f76c),
[Base::Quantity::getUnit()](../../d8/d18/classBase_1_1Quantity.html#acf401f989cc46b7c864565e89113ede4),
[Base::UnitSignature::Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::UnitSignature::LuminousIntensity](../../d0/d2c/structBase_1_1UnitSignature.html#af0120f04df20be40248efc75ec9fc00a),
[Base::UnitSignature::Mass](../../d0/d2c/structBase_1_1UnitSignature.html#a9a0beec4a0fc85341679bed98c5c979f),
[Base::Quantity::parse()](../../d8/d18/classBase_1_1Quantity.html#ae1fd875bacec268fcb40771b60c6386a),
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6),
[Base::UnitSignature::ThermodynamicTemperature](../../d0/d2c/structBase_1_1UnitSignature.html#a171c9b90aff6d96c99fe77f951efd62a),
and
[Base::UnitSignature::Time](../../d0/d2c/structBase_1_1UnitSignature.html#a984f0b070a4e3a1bfd1c123d85644106).

## ◆ ~Unit()

Base::Unit::~Unit  | ( | | ) |   
---|---|---|---|---  
  
Destruction.

## Member Function Documentation

## ◆ getSignature()

const [UnitSignature](../../d0/d2c/structBase_1_1UnitSignature.html) & Base::Unit::getSignature  | ( | | ) |  const  
---|---|---|---|---  
  
get the unit signature

## ◆ getString()

QString Unit::getString  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Base::UnitSignature::AmountOfSubstance](../../d0/d2c/structBase_1_1UnitSignature.html#adbda0d439a7e93b43b4783d0bb326f49),
[Base::UnitSignature::Angle](../../d0/d2c/structBase_1_1UnitSignature.html#ab0c72a128c708fb38392cb8b29e0b14d),
[Base::UnitSignature::ElectricCurrent](../../d0/d2c/structBase_1_1UnitSignature.html#a28e50326f63c30a25293bbdee189f76c),
[isEmpty()](../../d2/d37/classBase_1_1Unit.html#ada74af04cdf593999be6be0ae39b22ba),
[Base::UnitSignature::Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::UnitSignature::LuminousIntensity](../../d0/d2c/structBase_1_1UnitSignature.html#af0120f04df20be40248efc75ec9fc00a),
[Base::UnitSignature::Mass](../../d0/d2c/structBase_1_1UnitSignature.html#a9a0beec4a0fc85341679bed98c5c979f),
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6),
[Base::UnitSignature::ThermodynamicTemperature](../../d0/d2c/structBase_1_1UnitSignature.html#a171c9b90aff6d96c99fe77f951efd62a),
and
[Base::UnitSignature::Time](../../d0/d2c/structBase_1_1UnitSignature.html#a984f0b070a4e3a1bfd1c123d85644106).

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

## ◆ getTypeString()

QString Unit::getTypeString  | ( | | ) |  const  
---|---|---|---|---  
  
get the type as an string such as "Area", "Length" or "Pressure".

References
[Acceleration](../../d2/d37/classBase_1_1Unit.html#ad982b0bf22eca89df35f10143c001d8a),
[AmountOfSubstance](../../d2/d37/classBase_1_1Unit.html#a19646ae3d87766a019c9077fbd0fe4fa),
[Angle](../../d2/d37/classBase_1_1Unit.html#a650f972468df9938bacbcafdd4b443e1),
[Area](../../d2/d37/classBase_1_1Unit.html#ab3d42609406d023f6818a88433f685c4),
[Density](../../d2/d37/classBase_1_1Unit.html#ab892acba15d70afcb6f1750f5d43c872),
[DynamicViscosity](../../d2/d37/classBase_1_1Unit.html#a58a99db29eda15c2e8078d57627c74a4),
[ElectricalCapacitance](../../d2/d37/classBase_1_1Unit.html#ab6b968419a79de2df25c93d80245a301),
[ElectricalConductance](../../d2/d37/classBase_1_1Unit.html#a6bf7a95ca4739d61dfd0a09c99ea0562),
[ElectricalConductivity](../../d2/d37/classBase_1_1Unit.html#a4c3a665642892f0b37a2c36067816195),
[ElectricalInductance](../../d2/d37/classBase_1_1Unit.html#a0b8ddf7c558b2ef2c48fcbc209d7b441),
[ElectricalResistance](../../d2/d37/classBase_1_1Unit.html#a630e9d931f2bced410b5a31e16a32ce8),
[ElectricCharge](../../d2/d37/classBase_1_1Unit.html#a4b45018a18e2998bf656373194da4b7f),
[ElectricCurrent](../../d2/d37/classBase_1_1Unit.html#a70bf7f2abeded9984fcf653866a7ae8c),
[ElectricPotential](../../d2/d37/classBase_1_1Unit.html#a6ccd1a3bf9174cfa07613b3158c63845),
[Force](../../d2/d37/classBase_1_1Unit.html#a310daf6b91125572541d4fad81832d42),
[Frequency](../../d2/d37/classBase_1_1Unit.html#a7539ffede82a01fb8eedeb5a532a0d75),
[HeatFlux](../../d2/d37/classBase_1_1Unit.html#a7966aba69328a335f7821ff0a18fd116),
[KinematicViscosity](../../d2/d37/classBase_1_1Unit.html#ab862d4dc1e0c4b573f1e85bb2f7509bc),
[Length](../../d2/d37/classBase_1_1Unit.html#ae7af32a08ea9a0e1501571a2902c84bd),
[LuminousIntensity](../../d2/d37/classBase_1_1Unit.html#a6651f96686f2c2b533307d3c419edcc3),
[MagneticFieldStrength](../../d2/d37/classBase_1_1Unit.html#aa5568a2eef26248858f8828b86185c36),
[MagneticFlux](../../d2/d37/classBase_1_1Unit.html#a8109c4e89e27270a40a062f3ced30ee0),
[MagneticFluxDensity](../../d2/d37/classBase_1_1Unit.html#a040d981e6addd904e5d34b03be6dee82),
[Mass](../../d2/d37/classBase_1_1Unit.html#a0487599b7ddcb19c431b2e5522af173a),
[Power](../../d2/d37/classBase_1_1Unit.html#a6136199d4b9d4233a1df216e84f72fe0),
[Pressure](../../d2/d37/classBase_1_1Unit.html#ab0df485d964692e00f0b0006afb2068f),
[SpecificEnergy](../../d2/d37/classBase_1_1Unit.html#aadff4085546b98c8766526c873c98bc7),
[SpecificHeat](../../d2/d37/classBase_1_1Unit.html#ab81d44e306380c8e1dac197bcea5d71d),
[Stiffness](../../d2/d37/classBase_1_1Unit.html#a76655c5122e0c7b016cdabd9d41785ee),
[Temperature](../../d2/d37/classBase_1_1Unit.html#a2ef93d33b9d08b1c44d3324fde41af56),
[ThermalConductivity](../../d2/d37/classBase_1_1Unit.html#a7e056814cbd902bdb02586b8950b54a4),
[ThermalExpansionCoefficient](../../d2/d37/classBase_1_1Unit.html#a57b0f88cac2a96eccb99d55753d248a5),
[ThermalTransferCoefficient](../../d2/d37/classBase_1_1Unit.html#a17131da1b00f1bdc0a85e685752ee24a),
[TimeSpan](../../d2/d37/classBase_1_1Unit.html#ad667348b5bcef2a7a03de73580ef3827),
[VacuumPermittivity](../../d2/d37/classBase_1_1Unit.html#adce70257023fc90d88fc2b0d8557a51c),
[Velocity](../../d2/d37/classBase_1_1Unit.html#ac8f332f96770356aa6c6712a108b3410),
[Volume](../../d2/d37/classBase_1_1Unit.html#a0384d7597ade62ef6c880f84918a672f),
[VolumetricThermalExpansionCoefficient](../../d2/d37/classBase_1_1Unit.html#a579b2c39261f82d71ccf4835fa117208),
and
[Work](../../d2/d37/classBase_1_1Unit.html#a3a3ef1053b57fe85182b8befe4cb1984).

Referenced by
[Gui::Dialog::DlgUnitsCalculator::valueChanged()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a32bc446c35a2e71d1cb25fca0bafba08).

## ◆ isEmpty()

[bool](../../d9/db9/classbool.html) Unit::isEmpty  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Base::UnitSignature::AmountOfSubstance](../../d0/d2c/structBase_1_1UnitSignature.html#adbda0d439a7e93b43b4783d0bb326f49),
[Base::UnitSignature::Angle](../../d0/d2c/structBase_1_1UnitSignature.html#ab0c72a128c708fb38392cb8b29e0b14d),
[Base::UnitSignature::ElectricCurrent](../../d0/d2c/structBase_1_1UnitSignature.html#a28e50326f63c30a25293bbdee189f76c),
[Base::UnitSignature::Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::UnitSignature::LuminousIntensity](../../d0/d2c/structBase_1_1UnitSignature.html#af0120f04df20be40248efc75ec9fc00a),
[Base::UnitSignature::Mass](../../d0/d2c/structBase_1_1UnitSignature.html#a9a0beec4a0fc85341679bed98c5c979f),
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6),
[Base::UnitSignature::ThermodynamicTemperature](../../d0/d2c/structBase_1_1UnitSignature.html#a171c9b90aff6d96c99fe77f951efd62a),
and
[Base::UnitSignature::Time](../../d0/d2c/structBase_1_1UnitSignature.html#a984f0b070a4e3a1bfd1c123d85644106).

Referenced by
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[Spreadsheet::Cell::getFormattedQuantity()](../../d5/d22/classSpreadsheet_1_1Cell.html#a66a4fb5ffaa93232823dfbe49833ab7b),
[getString()](../../d2/d37/classBase_1_1Unit.html#ae403a424663d4df4b4a4886093ed07d1),
[Gui::InputField::newInput()](../../da/dfa/classGui_1_1InputField.html#a979a9f877e44ccb708716f8de610c22a),
[App::pyFromQuantity()](../../dd/dc2/namespaceApp.html#a1f508e13586e74f78640fce6b915e8ca),
and
[Spreadsheet::Cell::setComputedUnit()](../../d5/d22/classSpreadsheet_1_1Cell.html#a710db829a1918e2f367f3a3962877bc2).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) Base::Unit::operator!=  | ( | const [Unit](../../d2/d37/classBase_1_1Unit.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator*()

[Unit](../../d2/d37/classBase_1_1Unit.html) Unit::operator*  | ( | const [Unit](../../d2/d37/classBase_1_1Unit.html) & | _right_| ) |  const  
---|---|---|---|---|---  
  
References
[Base::UnitSignature::AmountOfSubstance](../../d0/d2c/structBase_1_1UnitSignature.html#adbda0d439a7e93b43b4783d0bb326f49),
[Base::UnitSignature::Angle](../../d0/d2c/structBase_1_1UnitSignature.html#ab0c72a128c708fb38392cb8b29e0b14d),
[Base::UnitSignature::ElectricCurrent](../../d0/d2c/structBase_1_1UnitSignature.html#a28e50326f63c30a25293bbdee189f76c),
[Base::UnitSignature::Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::UnitSignature::LuminousIntensity](../../d0/d2c/structBase_1_1UnitSignature.html#af0120f04df20be40248efc75ec9fc00a),
[Base::UnitSignature::Mass](../../d0/d2c/structBase_1_1UnitSignature.html#a9a0beec4a0fc85341679bed98c5c979f),
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6),
[Base::UnitSignature::ThermodynamicTemperature](../../d0/d2c/structBase_1_1UnitSignature.html#a171c9b90aff6d96c99fe77f951efd62a),
and
[Base::UnitSignature::Time](../../d0/d2c/structBase_1_1UnitSignature.html#a984f0b070a4e3a1bfd1c123d85644106).

## ◆ operator*=()

[Unit](../../d2/d37/classBase_1_1Unit.html) & Base::Unit::operator*=  | ( | const [Unit](../../d2/d37/classBase_1_1Unit.html) & | _that_| ) |   
---|---|---|---|---|---  
  
Operators.

## ◆ operator/()

[Unit](../../d2/d37/classBase_1_1Unit.html) Unit::operator/  | ( | const [Unit](../../d2/d37/classBase_1_1Unit.html) & | _right_| ) |  const  
---|---|---|---|---|---  
  
References
[Base::UnitSignature::AmountOfSubstance](../../d0/d2c/structBase_1_1UnitSignature.html#adbda0d439a7e93b43b4783d0bb326f49),
[Base::UnitSignature::Angle](../../d0/d2c/structBase_1_1UnitSignature.html#ab0c72a128c708fb38392cb8b29e0b14d),
[Base::UnitSignature::ElectricCurrent](../../d0/d2c/structBase_1_1UnitSignature.html#a28e50326f63c30a25293bbdee189f76c),
[Base::UnitSignature::Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::UnitSignature::LuminousIntensity](../../d0/d2c/structBase_1_1UnitSignature.html#af0120f04df20be40248efc75ec9fc00a),
[Base::UnitSignature::Mass](../../d0/d2c/structBase_1_1UnitSignature.html#a9a0beec4a0fc85341679bed98c5c979f),
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6),
[Base::UnitSignature::ThermodynamicTemperature](../../d0/d2c/structBase_1_1UnitSignature.html#a171c9b90aff6d96c99fe77f951efd62a),
and
[Base::UnitSignature::Time](../../d0/d2c/structBase_1_1UnitSignature.html#a984f0b070a4e3a1bfd1c123d85644106).

## ◆ operator/=()

[Unit](../../d2/d37/classBase_1_1Unit.html) & Base::Unit::operator/=  | ( | const [Unit](../../d2/d37/classBase_1_1Unit.html) & | _that_| ) |   
---|---|---|---|---|---  
  
## ◆ operator=()

[Unit](../../d2/d37/classBase_1_1Unit.html) & Unit::operator=  | ( | const [Unit](../../d2/d37/classBase_1_1Unit.html) & | _New_| ) |   
---|---|---|---|---|---  
  
References
[Base::UnitSignature::AmountOfSubstance](../../d0/d2c/structBase_1_1UnitSignature.html#adbda0d439a7e93b43b4783d0bb326f49),
[Base::UnitSignature::Angle](../../d0/d2c/structBase_1_1UnitSignature.html#ab0c72a128c708fb38392cb8b29e0b14d),
[Base::UnitSignature::ElectricCurrent](../../d0/d2c/structBase_1_1UnitSignature.html#a28e50326f63c30a25293bbdee189f76c),
[Base::UnitSignature::Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::UnitSignature::LuminousIntensity](../../d0/d2c/structBase_1_1UnitSignature.html#af0120f04df20be40248efc75ec9fc00a),
[Base::UnitSignature::Mass](../../d0/d2c/structBase_1_1UnitSignature.html#a9a0beec4a0fc85341679bed98c5c979f),
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6),
[Base::UnitSignature::ThermodynamicTemperature](../../d0/d2c/structBase_1_1UnitSignature.html#a171c9b90aff6d96c99fe77f951efd62a),
and
[Base::UnitSignature::Time](../../d0/d2c/structBase_1_1UnitSignature.html#a984f0b070a4e3a1bfd1c123d85644106).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) Unit::operator==  | ( | const [Unit](../../d2/d37/classBase_1_1Unit.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
References
[Base::UnitSignature::AmountOfSubstance](../../d0/d2c/structBase_1_1UnitSignature.html#adbda0d439a7e93b43b4783d0bb326f49),
[Base::UnitSignature::Angle](../../d0/d2c/structBase_1_1UnitSignature.html#ab0c72a128c708fb38392cb8b29e0b14d),
[Base::UnitSignature::ElectricCurrent](../../d0/d2c/structBase_1_1UnitSignature.html#a28e50326f63c30a25293bbdee189f76c),
[Base::UnitSignature::Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::UnitSignature::LuminousIntensity](../../d0/d2c/structBase_1_1UnitSignature.html#af0120f04df20be40248efc75ec9fc00a),
[Base::UnitSignature::Mass](../../d0/d2c/structBase_1_1UnitSignature.html#a9a0beec4a0fc85341679bed98c5c979f),
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6),
[Base::UnitSignature::ThermodynamicTemperature](../../d0/d2c/structBase_1_1UnitSignature.html#a171c9b90aff6d96c99fe77f951efd62a),
and
[Base::UnitSignature::Time](../../d0/d2c/structBase_1_1UnitSignature.html#a984f0b070a4e3a1bfd1c123d85644106).

## ◆ pow()

[Unit](../../d2/d37/classBase_1_1Unit.html) Unit::pow  | ( | signed char  | _exp_| ) |  const  
---|---|---|---|---|---  
  
References
[Base::UnitSignature::AmountOfSubstance](../../d0/d2c/structBase_1_1UnitSignature.html#adbda0d439a7e93b43b4783d0bb326f49),
[Base::UnitSignature::Angle](../../d0/d2c/structBase_1_1UnitSignature.html#ab0c72a128c708fb38392cb8b29e0b14d),
[Base::UnitSignature::ElectricCurrent](../../d0/d2c/structBase_1_1UnitSignature.html#a28e50326f63c30a25293bbdee189f76c),
[Base::UnitSignature::Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::UnitSignature::LuminousIntensity](../../d0/d2c/structBase_1_1UnitSignature.html#af0120f04df20be40248efc75ec9fc00a),
[Base::UnitSignature::Mass](../../d0/d2c/structBase_1_1UnitSignature.html#a9a0beec4a0fc85341679bed98c5c979f),
[Sig](../../d2/d37/classBase_1_1Unit.html#af119830178c6cebc821f3ccd8a274cf6),
[Base::UnitSignature::ThermodynamicTemperature](../../d0/d2c/structBase_1_1UnitSignature.html#a171c9b90aff6d96c99fe77f951efd62a),
and
[Base::UnitSignature::Time](../../d0/d2c/structBase_1_1UnitSignature.html#a984f0b070a4e3a1bfd1c123d85644106).

## Member Data Documentation

## ◆ Acceleration

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Acceleration  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[App::PropertyAcceleration::PropertyAcceleration()](../../dc/df9/classApp_1_1PropertyAcceleration.html#a327531458d1be41f3345a9bd0fabb0f3),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ AmountOfSubstance

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::AmountOfSubstance  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
and
[Unit()](../../d2/d37/classBase_1_1Unit.html#a333922c4cc697ff97090f5dedf911660).

## ◆ Angle

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Angle  
---  
static  
  
Angle.

Referenced by
[PartDesign::Chamfer::Chamfer()](../../da/d6f/classPartDesign_1_1Chamfer.html#a75b4114d662ce32435766510a7daef43),
[PartGui::DlgExtrusion::DlgExtrusion()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a7d11626ecae8d02d4421aa4fdd640dc8),
[PartGui::DlgRevolution::DlgRevolution()](../../d1/d83/classPartGui_1_1DlgRevolution.html#ad75370b34cc9b2f2ddb1439faa282f0d),
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[Gui::RDragger::drag()](../../d2/d5d/classGui_1_1RDragger.html#a173db197d450098991bf36fb83e85844),
[SketcherGui::EditDatumDialog::exec()](../../d6/d55/classSketcherGui_1_1EditDatumDialog.html#ae2acb3ba391ab2b817662e85aa8134fd),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[PartGui::goDimensionAngularNoTask()](../../d5/d49/namespacePartGui.html#a22a4e967d614ba7959dc90e89f6e76dc),
[PartGui::Location::Location()](../../db/d6f/classPartGui_1_1Location.html#a2f77946d77e8f18590ccf3f7e73a18b4),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewDimension::onDocumentRestored()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a899ec15c087cd8a0c38e05fda6f4a647),
[Gui::Dialog::Placement::Placement()](../../d8/d6c/classGui_1_1Dialog_1_1Placement.html#a61902824aa6953c8333e8d319eab8374),
[App::PropertyAngle::PropertyAngle()](../../d1/d5d/classApp_1_1PropertyAngle.html#a145a34ccd663f1fcf0eb8c04af7b6118),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialBuilding::schemaTranslate()](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMmMin::schemaTranslate()](../../d6/d67/classBase_1_1UnitsSchemaMmMin.html#afe8833459a266486009381109786e8cb),
[TechDrawGui::TaskCenterLine::setUiEdit()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a44074b04e6f03fde63d2f4ac7a3f0c33),
[TechDrawGui::TaskCenterLine::setUiPrimary()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a87a1eafc1c37ac2e6c0bbf8bfb73717a),
[TechDrawGui::TaskDimension::TaskDimension()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a01dec85a4db02858073f304508300ff3),
[Gui::PropertyEditor::PropertyRotationItem::toolTip()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#abbb3c671e82d0c8d54f1f6f2b95abe5d),
[Gui::PropertyEditor::PropertyPlacementItem::toolTip()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#add11217c79e909fa0d6a5fa97d739d2f),
[Gui::PropertyEditor::PropertyRotationItem::toString()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a13b41010f83aeb8833bf251d9f1a652a),
[Gui::PropertyEditor::PropertyPlacementItem::toString()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a4866bdcbed09d39f47781b1b5aba4cec),
[Unit()](../../d2/d37/classBase_1_1Unit.html#a333922c4cc697ff97090f5dedf911660),
and
[SketcherGui::PropertyConstraintListItem::value()](../../dd/d04/classSketcherGui_1_1PropertyConstraintListItem.html#afbd28ea5bf2d11eedc5c916575b9a5a1).

## ◆ AngleOfFriction

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::AngleOfFriction  
---  
static  
  
## ◆ Area

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Area  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[App::PropertyArea::PropertyArea()](../../d8/d06/classApp_1_1PropertyArea.html#a4792e6eec27493cc2b709d3df5873ed8),
[Base::UnitsSchemaCentimeters::schemaTranslate()](../../dc/d0e/classBase_1_1UnitsSchemaCentimeters.html#a289742693cf4466036aa1db1ba78959b),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialBuilding::schemaTranslate()](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ CompressiveStrength

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::CompressiveStrength  
---  
static  
  
## ◆ Density

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Density  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ DynamicViscosity

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::DynamicViscosity  
---  
static  
  
Referenced by
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ ElectricalCapacitance

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ElectricalCapacitance  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ ElectricalConductance

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ElectricalConductance  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ ElectricalConductivity

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ElectricalConductivity  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ ElectricalInductance

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ElectricalInductance  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ ElectricalResistance

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ElectricalResistance  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ ElectricCharge

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ElectricCharge  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ ElectricCurrent

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ElectricCurrent  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
and
[Unit()](../../d2/d37/classBase_1_1Unit.html#a333922c4cc697ff97090f5dedf911660).

## ◆ ElectricPotential

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ElectricPotential  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[App::PropertyElectricPotential::PropertyElectricPotential()](../../de/dc4/classApp_1_1PropertyElectricPotential.html#acc41a82b0378549ff2fac7a2c68bc2ce),
[Base::UnitsSchemaCentimeters::schemaTranslate()](../../dc/d0e/classBase_1_1UnitsSchemaCentimeters.html#a289742693cf4466036aa1db1ba78959b),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ Force

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Force  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[App::PropertyForce::PropertyForce()](../../dd/dcd/classApp_1_1PropertyForce.html#a2588df3b3005c7d8a26f0d863635ac7c),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ Frequency

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Frequency  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[App::PropertyFrequency::PropertyFrequency()](../../df/d12/classApp_1_1PropertyFrequency.html#ac3066a07aee7ae5f13e1fba69c98a603),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ HeatFlux

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::HeatFlux  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaCentimeters::schemaTranslate()](../../dc/d0e/classBase_1_1UnitsSchemaCentimeters.html#a289742693cf4466036aa1db1ba78959b),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
and
[FemGui::TaskFemConstraintHeatflux::TaskFemConstraintHeatflux()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a8e9e2cb04cc453f24e9d3ea5794cacc1).

## ◆ KinematicViscosity

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::KinematicViscosity  
---  
static  
  
Referenced by
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ Length

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Length  
---  
static  
  
Predefined [Unit](../../d2/d37/classBase_1_1Unit.html "The Unit class.")
types.

Length unit

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[PartDesign::Chamfer::Chamfer()](../../da/d6f/classPartDesign_1_1Chamfer.html#a75b4114d662ce32435766510a7daef43),
[PartGui::FilletRadiusDelegate::createEditor()](../../d7/d9d/classPartGui_1_1FilletRadiusDelegate.html#ac6160fa5baeda7ca462fd148d4a98b47),
[PartGui::createLinearDimension()](../../d5/d49/namespacePartGui.html#aef5ad6d90fba8fb11fa94870c2fa805c),
[MeshPartGui::CrossSections::CrossSections()](../../d1/d27/classMeshPartGui_1_1CrossSections.html#a884529081216e2c462f3f2906f602c68),
[PartGui::CrossSections::CrossSections()](../../dc/d84/classPartGui_1_1CrossSections.html#a884529081216e2c462f3f2906f602c68),
[Gui::PointMarker::customEvent()](../../d6/deb/classGui_1_1PointMarker.html#af3aff66aa9cfaaff337386e66a61c0f4),
[PartGui::DlgExtrusion::DlgExtrusion()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a7d11626ecae8d02d4421aa4fdd640dc8),
[PartGui::DlgFilletEdges::DlgFilletEdges()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a16463a511a5a288028ef96edb2b3aef6),
[TechDrawGui::DlgPrefsTechDrawAnnotationImp::DlgPrefsTechDrawAnnotationImp()](../../dc/dc6/classTechDrawGui_1_1DlgPrefsTechDrawAnnotationImp.html#a197023e8042b43e98001a2f29a81425c),
[TechDrawGui::DlgPrefsTechDrawDimensionsImp::DlgPrefsTechDrawDimensionsImp()](../../d7/d7d/classTechDrawGui_1_1DlgPrefsTechDrawDimensionsImp.html#aa994f8cec87f2fefa9c9def928563cbe),
[TechDrawGui::DlgPrefsTechDrawGeneralImp::DlgPrefsTechDrawGeneralImp()](../../d1/d38/classTechDrawGui_1_1DlgPrefsTechDrawGeneralImp.html#a385111ac8fa1feff7ee7c428f1763317),
[TechDrawGui::DlgPrefsTechDrawScaleImp::DlgPrefsTechDrawScaleImp()](../../da/d6c/classTechDrawGui_1_1DlgPrefsTechDrawScaleImp.html#acc5e3e627455093efa497ff694e83f2e),
[PartGui::DlgRevolution::DlgRevolution()](../../d1/d83/classPartGui_1_1DlgRevolution.html#ad75370b34cc9b2f2ddb1439faa282f0d),
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[Gui::TDragger::drag()](../../d3/d8c/classGui_1_1TDragger.html#aa44ea79797fa47a7bd4605d19702a211),
[TechDraw::DrawViewDimension::DrawViewDimension()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#aa6fad2118f8e0478d358978ef57e2dc4),
[PartGui::dumpLinearResults()](../../d5/d49/namespacePartGui.html#a4189ca02fa37799a62cf6cc3a5c8ef5a),
[SketcherGui::EditDatumDialog::exec()](../../d6/d55/classSketcherGui_1_1EditDatumDialog.html#ae2acb3ba391ab2b817662e85aa8134fd),
[App::FeatureTest::FeatureTest()](../../df/dea/classApp_1_1FeatureTest.html#a71e331e5bda8a32669e0da873fb28c31),
[PartDesign::Fillet::Fillet()](../../d0/d50/classPartDesign_1_1Fillet.html#a92e209863666263c8d36c82a3c7fed15),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[ArchPanel.CommandPanel::getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[App::PropertyVectorDistance::getUnit()](../../d7/d1e/classApp_1_1PropertyVectorDistance.html#a13cf48198fa25c599e0b196be979b17b),
[App::PropertyPosition::getUnit()](../../dd/dc2/classApp_1_1PropertyPosition.html#a75a28e99f348f7085449cacccb6fb57d),
[App::PropertyDirection::getUnit()](../../d8/d4c/classApp_1_1PropertyDirection.html#a82a05ebee91913141af4a785076e853e),
[PartGui::Location::Location()](../../db/d6f/classPartGui_1_1Location.html#a2f77946d77e8f18590ccf3f7e73a18b4),
[Gui::LocationWidget::LocationWidget()](../../d9/d9a/classGui_1_1LocationWidget.html#a4a7a3f5156e1c2defce954bb3c171c27),
[PartGui::Mirroring::Mirroring()](../../db/d41/classPartGui_1_1Mirroring.html#a37c415d13595eeeaa2f1a1fa54a5f740),
[PartGui::OffsetWidget::OffsetWidget()](../../d9/d6d/classPartGui_1_1OffsetWidget.html#ae7bb4b5d03b3c78115b8e3943bb318d1),
[Gui::Dialog::Transform::on_applyButton_clicked()](../../d0/d8f/classGui_1_1Dialog_1_1Transform.html#aa736a36e69d76427b945f434e46f3a2a),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[Gui::Dialog::Placement::Placement()](../../d8/d6c/classGui_1_1Dialog_1_1Placement.html#a61902824aa6953c8333e8d319eab8374),
[TechDraw::DrawSVGTemplate::processTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a9b2032d4f9db58231ae4ad79ca5b3778),
[App::PropertyDistance::PropertyDistance()](../../de/d43/classApp_1_1PropertyDistance.html#ae08a8a16ef05b721acc133e961511ad5),
[App::PropertyLength::PropertyLength()](../../d0/d44/classApp_1_1PropertyLength.html#a206837445861c363df2bc9cdcb209436),
[Base::UnitsSchemaCentimeters::schemaTranslate()](../../dc/d0e/classBase_1_1UnitsSchemaCentimeters.html#a289742693cf4466036aa1db1ba78959b),
[Base::UnitsSchemaFemMilliMeterNewton::schemaTranslate()](../../df/d2f/classBase_1_1UnitsSchemaFemMilliMeterNewton.html#aa6c39631dcc2e8da9b8212a34b00d785),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialBuilding::schemaTranslate()](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
[Base::UnitsSchemaMmMin::schemaTranslate()](../../d6/d67/classBase_1_1UnitsSchemaMmMin.html#afe8833459a266486009381109786e8cb),
[SketcherGui::SketcherGeneralWidget::setGridSize()](../../da/d36/classSketcherGui_1_1SketcherGeneralWidget.html#a46e96f68f9136357930cac055849dd03),
[ArchPanel.CommandPanel::setLength()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a324c9bdbfec0dd8eacfb7d0cea302998),
[Gui::Dialog::Transform::setTransformStrategy()](../../d0/d8f/classGui_1_1Dialog_1_1Transform.html#ae3b140a0d601a95674bcbda4e88aa6d4),
[TechDrawGui::TaskSectionView::setUiEdit()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a43dc3542cf896d0778a028ae2be230ce),
[TechDrawGui::TaskCenterLine::setUiEdit()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a44074b04e6f03fde63d2f4ac7a3f0c33),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[TechDrawGui::TaskSectionView::setUiPrimary()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a07485a3822d8c672d6e4580fe4bf858c),
[TechDrawGui::TaskCenterLine::setUiPrimary()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a87a1eafc1c37ac2e6c0bbf8bfb73717a),
[TechDrawGui::TaskCosmeticLine::setUiPrimary()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a4b1f902a521e9cd5fdf56889d51e52a3),
[TechDrawGui::TaskCosVertex::setUiPrimary()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#af4b9b21bba51de589fd14887b3b82150),
[TechDrawGui::TaskLeaderLine::setUiPrimary()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#ae4079f062fea88e52c9e7242cc8ecead),
[TechDrawGui::TaskRichAnno::setUiPrimary()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ae2285e8fe902c048c0c4d27ee93b42ec),
[PartGui::DlgFilletEdges::setupFillet()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a1276cdf00c4f3436317932a8da913a5e),
[Gui::PropertyEditor::PropertyVectorDistanceItem::setValue()](../../db/dd4/classGui_1_1PropertyEditor_1_1PropertyVectorDistanceItem.html#ad9ef59b35c09aee6c230e37e2032028e),
[TechDrawGui::TaskActiveView::TaskActiveView()](../../dd/dea/classTechDrawGui_1_1TaskActiveView.html#a1180c1d7b95bde6eef5c27cd7d9a305e),
[TechDrawGui::TaskBalloon::TaskBalloon()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#a21f34d1bf15390ec9c984c7c75ab9996),
[TechDrawGui::TaskDimension::TaskDimension()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a01dec85a4db02858073f304508300ff3),
[PartDesignGui::TaskFilletParameters::TaskFilletParameters()](../../db/d91/classPartDesignGui_1_1TaskFilletParameters.html#a6d39adf6b643a77ee3cecf31cdac126d),
[TechDrawGui::TaskProjGroup::TaskProjGroup()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a81c03636578c0dd7befcb158dd86bc28),
[Part::Thickness::Thickness()](../../db/d73/classPart_1_1Thickness.html#af9acf05fa602567de8ff2d6ba6128ac0),
[Gui::PropertyEditor::PropertyPlacementItem::toolTip()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#add11217c79e909fa0d6a5fa97d739d2f),
[Gui::PropertyEditor::PropertyVectorDistanceItem::toString()](../../db/dd4/classGui_1_1PropertyEditor_1_1PropertyVectorDistanceItem.html#a52151afd2af821db0099f65f6f41e47a),
[Gui::PropertyEditor::PropertyPlacementItem::toString()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a4866bdcbed09d39f47781b1b5aba4cec),
[Unit()](../../d2/d37/classBase_1_1Unit.html#a333922c4cc697ff97090f5dedf911660),
[ArchPanel.CommandPanel::update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c),
[Gui::ViewProviderMeasureDistance::updateData()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a260762ea126ca4a70b60e5a825f2448d),
[SketcherGui::PropertyConstraintListItem::value()](../../dd/d04/classSketcherGui_1_1PropertyConstraintListItem.html#afbd28ea5bf2d11eedc5c916575b9a5a1),
and
[InspectionGui::VisualInspection::VisualInspection()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#aa13e595beac41fb1b077d794cd7fc0bc).

## ◆ LuminousIntensity

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::LuminousIntensity  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
and
[Unit()](../../d2/d37/classBase_1_1Unit.html#a333922c4cc697ff97090f5dedf911660).

## ◆ MagneticFieldStrength

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::MagneticFieldStrength  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ MagneticFlux

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::MagneticFlux  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ MagneticFluxDensity

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::MagneticFluxDensity  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ Mass

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Mass  
---  
static  
  
Mass unit.

Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaFemMilliMeterNewton::schemaTranslate()](../../df/d2f/classBase_1_1UnitsSchemaFemMilliMeterNewton.html#aa6c39631dcc2e8da9b8212a34b00d785),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
and
[Unit()](../../d2/d37/classBase_1_1Unit.html#a333922c4cc697ff97090f5dedf911660).

## ◆ Power

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Power  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaCentimeters::schemaTranslate()](../../dc/d0e/classBase_1_1UnitsSchemaCentimeters.html#a289742693cf4466036aa1db1ba78959b),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
and
[FemGui::TaskFemConstraintTemperature::TaskFemConstraintTemperature()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a33195abb4e64b5b8c79d39c7423d0a22).

## ◆ Pressure

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Pressure  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[App::PropertyPressure::PropertyPressure()](../../d7/d5b/classApp_1_1PropertyPressure.html#a8c67c767c373798fed726b95b794b2a8),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ ShearModulus

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ShearModulus  
---  
static  
  
## ◆ Sig

| [UnitSignature](../../d0/d2c/structBase_1_1UnitSignature.html)
Base::Unit::Sig  
---  
protected  
  
Referenced by
[getString()](../../d2/d37/classBase_1_1Unit.html#ae403a424663d4df4b4a4886093ed07d1),
[isEmpty()](../../d2/d37/classBase_1_1Unit.html#ada74af04cdf593999be6be0ae39b22ba),
[operator*()](../../d2/d37/classBase_1_1Unit.html#a043243f070571191708527ba23ac071e),
[operator/()](../../d2/d37/classBase_1_1Unit.html#a6109f301f1e75c08096d1ca42279f219),
[operator=()](../../d2/d37/classBase_1_1Unit.html#a1981d99d235268e51895f8bf3944d4a7),
[operator==()](../../d2/d37/classBase_1_1Unit.html#a1742f0ce386adb69a82f9230251e7aed),
[pow()](../../d2/d37/classBase_1_1Unit.html#a0b551d733e192f041457de60a3573341),
and
[Unit()](../../d2/d37/classBase_1_1Unit.html#a333922c4cc697ff97090f5dedf911660).

## ◆ SpecificEnergy

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::SpecificEnergy  
---  
static  
  
Referenced by
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ SpecificHeat

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::SpecificHeat  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ Stiffness

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Stiffness  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[App::PropertyStiffness::PropertyStiffness()](../../d2/d00/classApp_1_1PropertyStiffness.html#a35c4cd53f711eefe832571a61235dbbb),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
and
[FemGui::TaskFemConstraintSpring::TaskFemConstraintSpring()](../../d9/d3e/classFemGui_1_1TaskFemConstraintSpring.html#a0237d05805437799169e7d15e6c262fa).

## ◆ Stress

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Stress  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
and
[FemGui::TaskFemConstraintPressure::TaskFemConstraintPressure()](../../dc/dd9/classFemGui_1_1TaskFemConstraintPressure.html#a00c65ac2686efb36884dcf8c6a10d76e).

## ◆ Temperature

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Temperature  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[FemGui::TaskFemConstraintHeatflux::TaskFemConstraintHeatflux()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a8e9e2cb04cc453f24e9d3ea5794cacc1),
[FemGui::TaskFemConstraintInitialTemperature::TaskFemConstraintInitialTemperature()](../../dd/d2a/classFemGui_1_1TaskFemConstraintInitialTemperature.html#a7fdd937b1300d7fc2eefc92ab53ac673),
and
[FemGui::TaskFemConstraintTemperature::TaskFemConstraintTemperature()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a33195abb4e64b5b8c79d39c7423d0a22).

## ◆ ThermalConductivity

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ThermalConductivity  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ ThermalExpansionCoefficient

| [Unit](../../d2/d37/classBase_1_1Unit.html)
Unit::ThermalExpansionCoefficient  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ ThermalTransferCoefficient

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::ThermalTransferCoefficient  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[FemGui::TaskFemConstraintHeatflux::getFilmCoef()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a579c61f84074d340e8f69d95e6403443),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
and
[FemGui::TaskFemConstraintHeatflux::TaskFemConstraintHeatflux()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a8e9e2cb04cc453f24e9d3ea5794cacc1).

## ◆ TimeSpan

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::TimeSpan  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
and
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89).

## ◆ UltimateTensileStrength

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::UltimateTensileStrength  
---  
static  
  
## ◆ VacuumPermittivity

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::VacuumPermittivity  
---  
static  
  
Referenced by
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
and
[App::PropertyVacuumPermittivity::PropertyVacuumPermittivity()](../../d3/d71/classApp_1_1PropertyVacuumPermittivity.html#aa5f0eafa1a5efc8cc178211520117366).

## ◆ Velocity

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Velocity  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[App::PropertySpeed::PropertySpeed()](../../dc/dcb/classApp_1_1PropertySpeed.html#a7189e1c05e50828620429cf778e04086),
[Base::UnitsSchemaCentimeters::schemaTranslate()](../../dc/d0e/classBase_1_1UnitsSchemaCentimeters.html#a289742693cf4466036aa1db1ba78959b),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialBuilding::schemaTranslate()](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
and
[Base::UnitsSchemaMmMin::schemaTranslate()](../../d6/d67/classBase_1_1UnitsSchemaMmMin.html#afe8833459a266486009381109786e8cb).

## ◆ Volume

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Volume  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[App::PropertyVolume::PropertyVolume()](../../db/d37/classApp_1_1PropertyVolume.html#ad8ae5a32d893b4ecc32adf2d6f5a9d7c),
[Base::UnitsSchemaCentimeters::schemaTranslate()](../../dc/d0e/classBase_1_1UnitsSchemaCentimeters.html#a289742693cf4466036aa1db1ba78959b),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialBuilding::schemaTranslate()](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ VolumetricThermalExpansionCoefficient

| [Unit](../../d2/d37/classBase_1_1Unit.html)
Unit::VolumetricThermalExpansionCoefficient  
---  
static  
  
Referenced by
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ Work

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::Work  
---  
static  
  
Referenced by
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[getTypeString()](../../d2/d37/classBase_1_1Unit.html#a819451af6a1ce39aa33aaef042495e89),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
and
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2).

## ◆ YieldStrength

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::YieldStrength  
---  
static  
  
## ◆ YoungsModulus

| [Unit](../../d2/d37/classBase_1_1Unit.html) Unit::YoungsModulus  
---  
static  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Unit.h
  * FreeCAD/src/Base/Unit.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

