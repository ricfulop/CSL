---
url: https://freecad.github.io/SourceDoc/d8/d18/classBase_1_1Quantity.html
scraped_at: 2025-09-08T15:17:02.179476
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Quantity](../../d8/d18/classBase_1_1Quantity.html)

[List of all members](../../da/d9c/classBase_1_1Quantity-members.html) | Public Member Functions | Static Public Member Functions | Static Public Attributes

Base::Quantity Class Reference

The [Quantity](../../d8/d18/classBase_1_1Quantity.html "The Quantity class.")
class. [More...](../../d8/d18/classBase_1_1Quantity.html#details)

`#include <Quantity.h>`

##  Public Member Functions  
  
---  
const [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html) & | [getFormat](../../d8/d18/classBase_1_1Quantity.html#a5674edba6d0574ed73bb2610fb590656) () const  
const [Unit](../../d2/d37/classBase_1_1Unit.html) & | [getUnit](../../d8/d18/classBase_1_1Quantity.html#acf401f989cc46b7c864565e89113ede4) () const  
| returns the unit of the quantity
[More...](../../d8/d18/classBase_1_1Quantity.html#acf401f989cc46b7c864565e89113ede4)  
  
QString | [getUserString](../../d8/d18/classBase_1_1Quantity.html#a9ff28abe8a99ea98ffc3261142fceb9c) () const  
QString | [getUserString](../../d8/d18/classBase_1_1Quantity.html#aea6567cde1ec7087c71c3cacb9d385eb) (double &factor, QString &unitString) const  
| transfer to user preferred unit/potence
[More...](../../d8/d18/classBase_1_1Quantity.html#aea6567cde1ec7087c71c3cacb9d385eb)  
  
QString | [getUserString](../../d8/d18/classBase_1_1Quantity.html#adbec8b893054c2ca1cd04d88c421ab45) ([UnitsSchema](../../d9/dc7/classBase_1_1UnitsSchema.html) *schema, double &factor, QString &unitString) const  
double | [getValue](../../d8/d18/classBase_1_1Quantity.html#a692b9e4043999d2c24737886639df7d0) () const  
| get the Value of the quantity
[More...](../../d8/d18/classBase_1_1Quantity.html#a692b9e4043999d2c24737886639df7d0)  
  
double | [getValueAs](../../d8/d18/classBase_1_1Quantity.html#aadfdb7ce8bd7c879237dd4904712b7de) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &) const  
| get the Value in a special unit given as quantity.
[More...](../../d8/d18/classBase_1_1Quantity.html#aadfdb7ce8bd7c879237dd4904712b7de)  
  
[bool](../../d9/db9/classbool.html) | [isDimensionless](../../d8/d18/classBase_1_1Quantity.html#abae817184245a734a29b5bbb261958b7) () const  
| true if it has a number without a unit
[More...](../../d8/d18/classBase_1_1Quantity.html#abae817184245a734a29b5bbb261958b7)  
  
[bool](../../d9/db9/classbool.html) | [isQuantity](../../d8/d18/classBase_1_1Quantity.html#a7e39882b2a5359ff53b2f7f0a85f510b) () const  
| true if it has a number and a valid unit
[More...](../../d8/d18/classBase_1_1Quantity.html#a7e39882b2a5359ff53b2f7f0a85f510b)  
  
[bool](../../d9/db9/classbool.html) | [isValid](../../d8/d18/classBase_1_1Quantity.html#a085bb0d9a01b323009b018810bf03f91) () const  
| true if it has a number with or without a unit
[More...](../../d8/d18/classBase_1_1Quantity.html#a085bb0d9a01b323009b018810bf03f91)  
  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) | [operator*](../../d8/d18/classBase_1_1Quantity.html#a6d32504cd86ee5d1540bc79a8be822a7) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &p) const  
| Operators.
[More...](../../d8/d18/classBase_1_1Quantity.html#a6d32504cd86ee5d1540bc79a8be822a7)  
  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) | [operator*](../../d8/d18/classBase_1_1Quantity.html#a4faadcef28dc8436ee41c608639faa3c) (double p) const  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) | [operator+](../../d8/d18/classBase_1_1Quantity.html#a1a751b6834e43092bf8d2e359e26a2b0) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &p) const  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) & | [operator+=](../../d8/d18/classBase_1_1Quantity.html#a83d01360dc17373314d930cd4ea6f241) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &p)  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) | [operator-](../../d8/d18/classBase_1_1Quantity.html#af9556024c748148cf181f41b9c325cb6) () const  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) | [operator-](../../d8/d18/classBase_1_1Quantity.html#a3aafef28e0436a9b8b77b26187b7c28b) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &p) const  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) & | [operator-=](../../d8/d18/classBase_1_1Quantity.html#a9e88d52292ceca8aa2f97625fb635aea) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &p)  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) | [operator/](../../d8/d18/classBase_1_1Quantity.html#a52004505b3c927e8b037480a24a28f24) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &p) const  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) | [operator/](../../d8/d18/classBase_1_1Quantity.html#aadc7a6dc7b9c67873d62c1a14a2e0d78) (double p) const  
[bool](../../d9/db9/classbool.html) | [operator<](../../d8/d18/classBase_1_1Quantity.html#a7dfcb314d4fae31ed2cdd3985b20d7da) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &) const  
[bool](../../d9/db9/classbool.html) | [operator<=](../../d8/d18/classBase_1_1Quantity.html#ab7fc04e1b1719988ea1258bf9da46f04) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &) const  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) & | [operator=](../../d8/d18/classBase_1_1Quantity.html#a69efcd6903d22313c95837438ba48838) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &)  
[bool](../../d9/db9/classbool.html) | [operator==](../../d8/d18/classBase_1_1Quantity.html#a47d33d0a7069ae31810a3ba51810cd44) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &) const  
[bool](../../d9/db9/classbool.html) | [operator>](../../d8/d18/classBase_1_1Quantity.html#a701eb9e31ee7fcc6e17bcea04f71cdaf) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &) const  
[bool](../../d9/db9/classbool.html) | [operator>=](../../d8/d18/classBase_1_1Quantity.html#a8ee5a0f9cc602dbb462c98357b7b567d) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &) const  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) | [pow](../../d8/d18/classBase_1_1Quantity.html#a348caa60e6551629f335239e361f28b8) (const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &) const  
[Quantity](../../d8/d18/classBase_1_1Quantity.html) | [pow](../../d8/d18/classBase_1_1Quantity.html#a85ba604cdeded6fb42989c109a8aa061) (double) const  
|
[Quantity](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1)
()  
| default constructor
[More...](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1)  
  
|
[Quantity](../../d8/d18/classBase_1_1Quantity.html#af1b64a617320cef27375d1ae218ca5ac)
(const [Quantity](../../d8/d18/classBase_1_1Quantity.html) &)  
|
[Quantity](../../d8/d18/classBase_1_1Quantity.html#a372908a1fc1cc656c746637f712e55f7)
(double value, const QString &unit)  
|
[Quantity](../../d8/d18/classBase_1_1Quantity.html#a29c36a0c8d19138fa38e0a86f16f33b0)
(double value, const [Unit](../../d2/d37/classBase_1_1Unit.html)
&unit=[Unit](../../d2/d37/classBase_1_1Unit.html)())  
void | [setFormat](../../d8/d18/classBase_1_1Quantity.html#add12ce66fba83018c5ae8f35e1924100) (const [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html) &f)  
void | [setInvalid](../../d8/d18/classBase_1_1Quantity.html#a0dd6e226ceaaa66ef7dda49159178117) ()  
| sets the quantity invalid
[More...](../../d8/d18/classBase_1_1Quantity.html#a0dd6e226ceaaa66ef7dda49159178117)  
  
void | [setUnit](../../d8/d18/classBase_1_1Quantity.html#a1c259a327168c439806915612a2256bc) (const [Unit](../../d2/d37/classBase_1_1Unit.html) &un)  
| set the unit of the quantity
[More...](../../d8/d18/classBase_1_1Quantity.html#a1c259a327168c439806915612a2256bc)  
  
void | [setValue](../../d8/d18/classBase_1_1Quantity.html#a22d3da3215928275b0c3b88cd4c78d65) (double val)  
| set the value of the quantity
[More...](../../d8/d18/classBase_1_1Quantity.html#a22d3da3215928275b0c3b88cd4c78d65)  
  
|
[~Quantity](../../d8/d18/classBase_1_1Quantity.html#aa894484c62ee81498092b22de74f4d6d)
()  
| Destruction.
[More...](../../d8/d18/classBase_1_1Quantity.html#aa894484c62ee81498092b22de74f4d6d)  
  
  
##  Static Public Member Functions  
  
---  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [parse](../../d8/d18/classBase_1_1Quantity.html#ae1fd875bacec268fcb40771b60c6386a) (const QString &string)  
  
##  Static Public Attributes  
  
---  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Ampere](../../d8/d18/classBase_1_1Quantity.html#a2052d22efa49393de9a6f85f30b24643)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [AngMinute](../../d8/d18/classBase_1_1Quantity.html#af8b81c8a6dc3ca4a2d24f770c5a48622)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [AngSecond](../../d8/d18/classBase_1_1Quantity.html#a531aba759471138ae885566c720700cd)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Bar](../../d8/d18/classBase_1_1Quantity.html#aab3a91c75f70e5667b3cb779468df225)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Calorie](../../d8/d18/classBase_1_1Quantity.html#a5088293a38b76e4d0e2199f7b3a1009b)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Candela](../../d8/d18/classBase_1_1Quantity.html#a095451968a50817ba323e372d5611f99)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [CentiMetre](../../d8/d18/classBase_1_1Quantity.html#a9a256ac5baeb7ca34d4da1642f4f8fba)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Coulomb](../../d8/d18/classBase_1_1Quantity.html#a706d195540313fd808a5c636e77bf6ff)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [CubicFoot](../../d8/d18/classBase_1_1Quantity.html#a2f669ec4cfed69c750626e463592687a)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [DeciMetre](../../d8/d18/classBase_1_1Quantity.html#aa94c6fe7a3e247ee5c720ecd5cc20fb5)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Degree](../../d8/d18/classBase_1_1Quantity.html#a406544daf200f53f736de491679b5ae2)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [ElectronVolt](../../d8/d18/classBase_1_1Quantity.html#ad5704d5c351f1ac23bd95cebf8b0a09b)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Farad](../../d8/d18/classBase_1_1Quantity.html#a337e6be2631331613dd6cc03499b1ad7)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Foot](../../d8/d18/classBase_1_1Quantity.html#ae97cb3bca62a8088b98e9299a8d62806)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Gauss](../../d8/d18/classBase_1_1Quantity.html#a061b3a82d26306eb653263b9d2b5b88f)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [GigaHertz](../../d8/d18/classBase_1_1Quantity.html#a0422b358f9c6d8c999cea12fede326d9)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [GigaPascal](../../d8/d18/classBase_1_1Quantity.html#adf44cd5178095ab3843151c96d896baa)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Gon](../../d8/d18/classBase_1_1Quantity.html#a9af5cf6b0ffe786754d7578033e2bc7a)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Gram](../../d8/d18/classBase_1_1Quantity.html#a0659cf27d33fdd10c64b5b6823ca7227)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Henry](../../d8/d18/classBase_1_1Quantity.html#a838c24750f8617a0340000b8b9e2f785)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Hertz](../../d8/d18/classBase_1_1Quantity.html#a18dd47d9c6a158e9c881a86f758d1d21)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Hour](../../d8/d18/classBase_1_1Quantity.html#a8d4ee03d994b57e9bf951100fa8d5f1f)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Hundredweights](../../d8/d18/classBase_1_1Quantity.html#aa7ab413fe1247d2d6e59c9f9f9b7c33b)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Inch](../../d8/d18/classBase_1_1Quantity.html#a413777faf05ddc51d3fec728858fe558)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Joule](../../d8/d18/classBase_1_1Quantity.html#a633d8d109f5878a976a3d65520570fab)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Kelvin](../../d8/d18/classBase_1_1Quantity.html#ac94b21ea97f0812dbf7c28a78191279c)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloAmpere](../../d8/d18/classBase_1_1Quantity.html#a59861aee563111ff9ed3dcb9aa572a7e)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloCalorie](../../d8/d18/classBase_1_1Quantity.html#ae399e1ac565450c69a590456f18d9b4b)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloElectronVolt](../../d8/d18/classBase_1_1Quantity.html#ad5fcd173fc6046951556c205647a650e)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloGram](../../d8/d18/classBase_1_1Quantity.html#a44972a9e538b2b1b9de6b8dcc9f263d6)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloHertz](../../d8/d18/classBase_1_1Quantity.html#ad4dd2f716ae88f89d4d6748fde5d68d9)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloJoule](../../d8/d18/classBase_1_1Quantity.html#a225c37b6158f72a495e7e968625ce878)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloMetre](../../d8/d18/classBase_1_1Quantity.html#aadb3d631a565ba0d270035b17e4ee713)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloNewton](../../d8/d18/classBase_1_1Quantity.html#a29b334666640a206d40fb8a630269fe2)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloNewtonPerMeter](../../d8/d18/classBase_1_1Quantity.html#af2539a70c48e30fde185d0b5514fe60b)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloOhm](../../d8/d18/classBase_1_1Quantity.html#a79aaa3543b1020fdbc60b6b5bd4d292b)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloPascal](../../d8/d18/classBase_1_1Quantity.html#a7f2157917f77b9d2073e95f773d5f138)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloSiemens](../../d8/d18/classBase_1_1Quantity.html#a70f845285729d57c49814e8aed8893c2)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloVolt](../../d8/d18/classBase_1_1Quantity.html#af6f794f8bab88d2b46937ecee486a311)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloWatt](../../d8/d18/classBase_1_1Quantity.html#aebe088e11d0d8cb0efb6c92b8c83c3c2)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KiloWattHour](../../d8/d18/classBase_1_1Quantity.html#a8c89a43f458a7ae7df70498e0dccba6e)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KMH](../../d8/d18/classBase_1_1Quantity.html#a23e882715d92cd38db0cf6306da8a5fc)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [KSI](../../d8/d18/classBase_1_1Quantity.html#a3568aee317cd25829b0dffb1b48d11e7)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Liter](../../d8/d18/classBase_1_1Quantity.html#aca23e97c9b7347f9c9c9a6bf06a1e5dc)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MegaAmpere](../../d8/d18/classBase_1_1Quantity.html#aab9a0c364e587c743ce4906219a1c733)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MegaElectronVolt](../../d8/d18/classBase_1_1Quantity.html#a796815b868d2f806733e854296ddc395)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MegaHertz](../../d8/d18/classBase_1_1Quantity.html#a833a370e7558feafd4eef96198c72914)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MegaNewton](../../d8/d18/classBase_1_1Quantity.html#aa2efff7543da3a881412c9f699d9df40)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MegaNewtonPerMeter](../../d8/d18/classBase_1_1Quantity.html#a83730b47af7df32babd5b51fc043b526)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MegaOhm](../../d8/d18/classBase_1_1Quantity.html#aa00eeec704dcee6cf6ae236073a9b4e7)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MegaPascal](../../d8/d18/classBase_1_1Quantity.html#a85fbb26718f08d0897187ae9b133a471)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MegaSiemens](../../d8/d18/classBase_1_1Quantity.html#a1a7c1c8e9d372639e9310b4ebaa78ae3)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Metre](../../d8/d18/classBase_1_1Quantity.html#ac7869d6c1d54048534051e3bff0e6f5e)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MicroFarad](../../d8/d18/classBase_1_1Quantity.html#a3d8a53b12bd2619cdbd4a8d088d0a932)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MicroGram](../../d8/d18/classBase_1_1Quantity.html#a6a875996ec9c373d0a4a2c7852bbb5e7)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MicroHenry](../../d8/d18/classBase_1_1Quantity.html#ae2db2cfac3e6c311a3a2cbabcbeacb6b)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MicroKelvin](../../d8/d18/classBase_1_1Quantity.html#a36be089dd474254ed525004e52e909b4)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MicroMetre](../../d8/d18/classBase_1_1Quantity.html#a47833d5da5f11f9b7a180ffb9163d1e4)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MicroSiemens](../../d8/d18/classBase_1_1Quantity.html#a2d7d5ac9ba5f7936e962a56c47d9d82c)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Mile](../../d8/d18/classBase_1_1Quantity.html#a65b39c43b52436566d2290201190715a)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilePerHour](../../d8/d18/classBase_1_1Quantity.html#af2e2a3c8dc968b2b8539c0718d1fb5ea)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliAmpere](../../d8/d18/classBase_1_1Quantity.html#a2a3952d982c8848f31712bb94a402ad8)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliBar](../../d8/d18/classBase_1_1Quantity.html#a6ee1de532b56fbcc7cb531480cb9b7c5)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliFarad](../../d8/d18/classBase_1_1Quantity.html#a8496859381ddd2ca9b581f691d2773a7)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliGram](../../d8/d18/classBase_1_1Quantity.html#abf24d4e36c35db56db094f889c81ba39)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliHenry](../../d8/d18/classBase_1_1Quantity.html#a47fa1c950af56101c84da577980a376c)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliJoule](../../d8/d18/classBase_1_1Quantity.html#a72e8d8af58eb6b4e5edc79cd5eb60590)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliKelvin](../../d8/d18/classBase_1_1Quantity.html#ae7a2429852802bf54b4351a58bdf52bc)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliLiter](../../d8/d18/classBase_1_1Quantity.html#a2abcc174810ae71674f21f7d648e2581)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliMetre](../../d8/d18/classBase_1_1Quantity.html#a1a7815763386cdc154f3b6d816d38ed4)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliMole](../../d8/d18/classBase_1_1Quantity.html#ae9a73d5c454092d689b1a8312acc5cc9)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliNewton](../../d8/d18/classBase_1_1Quantity.html#abb6c008b26798470f20e63a99b3ff773)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliNewtonPerMeter](../../d8/d18/classBase_1_1Quantity.html#a0fcc064784de957013104f57c4a7280f)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliSiemens](../../d8/d18/classBase_1_1Quantity.html#ae6b00913418940448c8cf5701c2857e7)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliVolt](../../d8/d18/classBase_1_1Quantity.html#a0fbccecb4d73ddbb295911b659ecaa64)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MilliWatt](../../d8/d18/classBase_1_1Quantity.html#a9dc7a4d2af6b2a13ee29fdfcf5d71b93)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Minute](../../d8/d18/classBase_1_1Quantity.html#a37d67a32e627acc51274a847a4039dd6)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Mole](../../d8/d18/classBase_1_1Quantity.html#a584c8357111885df15c4668b15e310c3)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MPH](../../d8/d18/classBase_1_1Quantity.html#ad572a0f838c7674365f0a67eb272e63b)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [MPSI](../../d8/d18/classBase_1_1Quantity.html#acbd7fd5d9a1341abe878fc5c83383131)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [mTorr](../../d8/d18/classBase_1_1Quantity.html#a930d6ab769037c0b53331430ae89f60c)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [NanoFarad](../../d8/d18/classBase_1_1Quantity.html#a9bb896ef9d353a95271ec98bb83c0039)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [NanoHenry](../../d8/d18/classBase_1_1Quantity.html#a2bbc2e955ccdc03cef3950122034be89)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [NanoMetre](../../d8/d18/classBase_1_1Quantity.html#a3f9bab5307093bbc3a6e0b9ef52fb834)  
| Predefined [Unit](../../d2/d37/classBase_1_1Unit.html "The Unit class.")
types.
[More...](../../d8/d18/classBase_1_1Quantity.html#a3f9bab5307093bbc3a6e0b9ef52fb834)  
  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Newton](../../d8/d18/classBase_1_1Quantity.html#a184911f6d5cc585c738d86ca7cd3a52d)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [NewtonMeter](../../d8/d18/classBase_1_1Quantity.html#a02349a65bef36749db9ed9934a86d823)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [NewtonPerMeter](../../d8/d18/classBase_1_1Quantity.html#ad8a1722b6b4f12f7834bfc3d0a29a9c6)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Oersted](../../d8/d18/classBase_1_1Quantity.html#a5510f268995b22478d1c383e9ab486d0)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Ohm](../../d8/d18/classBase_1_1Quantity.html#a805c85ac0640f4380143d1a0650b1199)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Ounce](../../d8/d18/classBase_1_1Quantity.html#afae51515acb80582fc8f93c0d37d39b3)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Pascal](../../d8/d18/classBase_1_1Quantity.html#a6104817027584bae8c581442644d81fb)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [PicoFarad](../../d8/d18/classBase_1_1Quantity.html#a552a3558fd41d3f34b87812b78c43e05)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Pound](../../d8/d18/classBase_1_1Quantity.html#a77761378ae4a2db7a1f9603865ddba7b)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [PoundForce](../../d8/d18/classBase_1_1Quantity.html#ae10747c00ea0251ddf7b38e344b0a228)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [PSI](../../d8/d18/classBase_1_1Quantity.html#abc4bd48dc9fbf73a29a422ed36e0dda8)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Radian](../../d8/d18/classBase_1_1Quantity.html#aa0778aa575e6b3adfd048dbb001c114d)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Second](../../d8/d18/classBase_1_1Quantity.html#a91bd6104ee6936e56519edea3a9ecef6)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Siemens](../../d8/d18/classBase_1_1Quantity.html#af30e42af90fd9d9281c315c1077980c7)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [SquareFoot](../../d8/d18/classBase_1_1Quantity.html#a3fb27498a066e02d55a70c60a5eb4eae)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Stone](../../d8/d18/classBase_1_1Quantity.html#a13bb4c3615a786b08d0fbef1dbd52757)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [TeraHertz](../../d8/d18/classBase_1_1Quantity.html#ac191efffeb7319c9660e2651debe8844)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Tesla](../../d8/d18/classBase_1_1Quantity.html#ad5d607f9594cc497444e48e90173d695)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Thou](../../d8/d18/classBase_1_1Quantity.html#a3e11488c3b17bb628b0f22bed97caf0b)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Ton](../../d8/d18/classBase_1_1Quantity.html#a0d5ea3ecf8b56b56304134a118b6a90d)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Torr](../../d8/d18/classBase_1_1Quantity.html#a805cfff89fd7106786c5c657774b1dd8)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Volt](../../d8/d18/classBase_1_1Quantity.html#a845c72e594b389347582e2d2c89b7963)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [VoltAmpere](../../d8/d18/classBase_1_1Quantity.html#ad13ae050771959da4e2b3b085086248e)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [VoltAmpereSecond](../../d8/d18/classBase_1_1Quantity.html#aec8d0f1cdfc8686ccd1a75e5e84c1cf4)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Watt](../../d8/d18/classBase_1_1Quantity.html#a488e52cae09734d299f5c8e94aca301d)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [WattSecond](../../d8/d18/classBase_1_1Quantity.html#a24fb60406b765da0aeb7ecc72dc622be)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Weber](../../d8/d18/classBase_1_1Quantity.html#a946d33a4f6532cb4665594adfe75d485)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [Yard](../../d8/d18/classBase_1_1Quantity.html#a715e29805751f8ca67d97756c7b4b90c)  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [yTorr](../../d8/d18/classBase_1_1Quantity.html#a35e6fe2da4e957080eb40432f89ebe87)  
  
## Detailed Description

The [Quantity](../../d8/d18/classBase_1_1Quantity.html "The Quantity class.")
class.

## Constructor & Destructor Documentation

## ◆ Quantity() [1/4]

Quantity::Quantity  | ( | | ) |   
---|---|---|---|---  
  
default constructor

Referenced by
[operator*()](../../d8/d18/classBase_1_1Quantity.html#a6d32504cd86ee5d1540bc79a8be822a7),
[operator+()](../../d8/d18/classBase_1_1Quantity.html#a1a751b6834e43092bf8d2e359e26a2b0),
[operator-()](../../d8/d18/classBase_1_1Quantity.html#a3aafef28e0436a9b8b77b26187b7c28b),
[operator/()](../../d8/d18/classBase_1_1Quantity.html#a52004505b3c927e8b037480a24a28f24),
[parse()](../../d8/d18/classBase_1_1Quantity.html#ae1fd875bacec268fcb40771b60c6386a),
and
[pow()](../../d8/d18/classBase_1_1Quantity.html#a348caa60e6551629f335239e361f28b8).

## ◆ Quantity() [2/4]

Quantity::Quantity  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _that_| ) |   
---|---|---|---|---|---  
  
## ◆ Quantity() [3/4]

| Quantity::Quantity  | ( | double  | _value_ ,   
---|---|---|---  
|  | const [Unit](../../d2/d37/classBase_1_1Unit.html) & | _unit_ = `[Unit](../../d2/d37/classBase_1_1Unit.html)()`  
| ) | |   
explicit  
  
## ◆ Quantity() [4/4]

| Quantity::Quantity  | ( | double  | _value_ ,   
---|---|---|---  
|  | const QString & | _unit_  
| ) | |   
explicit  
  
References
[parse()](../../d8/d18/classBase_1_1Quantity.html#ae1fd875bacec268fcb40771b60c6386a).

## ◆ ~Quantity()

Base::Quantity::~Quantity  | ( | | ) |   
---|---|---|---|---  
  
Destruction.

## Member Function Documentation

## ◆ getFormat()

const [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html) & Base::Quantity::getFormat  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Gui::InputField::getFormat()](../../da/dfa/classGui_1_1InputField.html#a829971d0d777421c8572b1c0786044bc),
[Gui::InputField::getPrecision()](../../da/dfa/classGui_1_1InputField.html#ad5dbff9b9e32c81853213819aef1ec07),
[Sketcher::Constraint::getPresentationValue()](../../d6/def/classSketcher_1_1Constraint.html#a9be53639cd1e5e49f23c61862430874b),
[Gui::InputField::newInput()](../../da/dfa/classGui_1_1InputField.html#a979a9f877e44ccb708716f8de610c22a),
[Base::UnitsSchemaImperialBuilding::schemaTranslate()](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1),
[Gui::InputField::selectNumber()](../../da/dfa/classGui_1_1InputField.html#a2ef97ec6fa3cd0afc02bbe2938e136ba),
[Gui::InputField::setFormat()](../../da/dfa/classGui_1_1InputField.html#a25118d14b9aa233f5b604fdd6ae35abe),
[Gui::InputField::setPrecision()](../../da/dfa/classGui_1_1InputField.html#aa5214b250f577c5f53ce0f4e74140566),
[Base::UnitsSchema::toLocale()](../../d9/dc7/classBase_1_1UnitsSchema.html#aacde4020d5617f0e65769350940f0a44),
and
[Gui::QuantitySpinBoxPrivate::validate()](../../dd/d08/classGui_1_1QuantitySpinBoxPrivate.html#a3a7b86da24888398add92a65193c9b62).

## ◆ getUnit()

const [Unit](../../d2/d37/classBase_1_1Unit.html) & Base::Quantity::getUnit  | ( | | ) |  const  
---|---|---|---|---  
  
returns the unit of the quantity

Referenced by
[App::pyFromQuantity()](../../dd/dc2/namespaceApp.html#a1f508e13586e74f78640fce6b915e8ca),
[Base::UnitsSchemaCentimeters::schemaTranslate()](../../dc/d0e/classBase_1_1UnitsSchemaCentimeters.html#a289742693cf4466036aa1db1ba78959b),
[Base::UnitsSchemaFemMilliMeterNewton::schemaTranslate()](../../df/d2f/classBase_1_1UnitsSchemaFemMilliMeterNewton.html#aa6c39631dcc2e8da9b8212a34b00d785),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialDecimal::schemaTranslate()](../../df/d8e/classBase_1_1UnitsSchemaImperialDecimal.html#ace7832695de9e3b504dbdd06aa7a987c),
[Base::UnitsSchemaImperialBuilding::schemaTranslate()](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
[Base::UnitsSchemaMmMin::schemaTranslate()](../../d6/d67/classBase_1_1UnitsSchemaMmMin.html#afe8833459a266486009381109786e8cb),
[App::PropertyQuantity::setPyObject()](../../d4/d65/classApp_1_1PropertyQuantity.html#a72be43d71c5e5a5e0a174c01df176dc9),
[App::PropertyQuantityConstraint::setPyObject()](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#a299ac9ee7870f29d5c3640a14114fcbe),
[Gui::InputField::setUnitText()](../../da/dfa/classGui_1_1InputField.html#afe9df9976a2874ec346f633925874daf),
[Gui::QuantitySpinBox::setUnitText()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#ab7f8050e8114c81fc3b5336685c67a34),
[Gui::InputField::setValue()](../../da/dfa/classGui_1_1InputField.html#a781543765d484715f02462acc7f3522a),
[Base::Unit::Unit()](../../d2/d37/classBase_1_1Unit.html#abbfe43509b2db5c3403ae90c3ef0b5d8),
and
[Gui::Dialog::DlgUnitsCalculator::valueChanged()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a32bc446c35a2e71d1cb25fca0bafba08).

## ◆ getUserString() [1/3]

QString Base::Quantity::getUserString  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getUserString() [2/3]

QString Quantity::getUserString  | ( | double & | _factor_ ,   
---|---|---|---  
|  | QString & | _unitString_  
| ) | |  const  
  
transfer to user preferred unit/potence

References
[Base::UnitsApi::schemaTranslate()](../../d9/d89/classBase_1_1UnitsApi.html#a4eee4ddbeb846ca0711919848eb53f63).

Referenced by
[PartGui::createLinearDimension()](../../d5/d49/namespacePartGui.html#aef5ad6d90fba8fb11fa94870c2fa805c),
[Gui::PointMarker::customEvent()](../../d6/deb/classGui_1_1PointMarker.html#af3aff66aa9cfaaff337386e66a61c0f4),
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[ConstraintItem::data()](../../d3/d0f/classConstraintItem.html#a58e0ecc1824934b77e25bc0b319b6c51),
[Gui::TDragger::drag()](../../d3/d8c/classGui_1_1TDragger.html#aa44ea79797fa47a7bd4605d19702a211),
[Gui::RDragger::drag()](../../d2/d5d/classGui_1_1RDragger.html#a173db197d450098991bf36fb83e85844),
[PartGui::dumpLinearResults()](../../d5/d49/namespacePartGui.html#a4189ca02fa37799a62cf6cc3a5c8ef5a),
[Gui::InputField::focusOutEvent()](../../da/dfa/classGui_1_1InputField.html#a2cf2d3890afc5a81e3579cb739d4b611),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[Gui::InputField::getQuantityString()](../../da/dfa/classGui_1_1InputField.html#aa6d828dbfe3ce1f5de71d00f458142e8),
[Gui::InputField::getUnitText()](../../da/dfa/classGui_1_1InputField.html#a9db6130eef65125c5318b21312566ead),
[Gui::InputField::keyPressEvent()](../../da/dfa/classGui_1_1InputField.html#ab73256a9df5973c9a41ab6515b0c202d),
[Gui::InputField::setRawText()](../../da/dfa/classGui_1_1InputField.html#addbe1c46fd12e6963054603cd5442acb),
[Gui::PropertyEditor::PropertyPlacementItem::toolTip()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#add11217c79e909fa0d6a5fa97d739d2f),
[Gui::PropertyEditor::PropertyVectorDistanceItem::toString()](../../db/dd4/classGui_1_1PropertyEditor_1_1PropertyVectorDistanceItem.html#a52151afd2af821db0099f65f6f41e47a),
[Gui::PropertyEditor::PropertyRotationItem::toString()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a13b41010f83aeb8833bf251d9f1a652a),
[Gui::PropertyEditor::PropertyPlacementItem::toString()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a4866bdcbed09d39f47781b1b5aba4cec),
and
[Gui::InputField::wheelEvent()](../../da/dfa/classGui_1_1InputField.html#af295bed6b89cc4e4d485e6a4dc046516).

## ◆ getUserString() [3/3]

QString Quantity::getUserString  | ( | [UnitsSchema](../../d9/dc7/classBase_1_1UnitsSchema.html) *  | _schema_ ,   
---|---|---|---  
|  | double & | _factor_ ,   
|  | QString & | _unitString_  
| ) | |  const  
  
References
[Base::UnitsSchema::schemaTranslate()](../../d9/dc7/classBase_1_1UnitsSchema.html#a8ff374bff7ebc4f654ed3978080052d7).

## ◆ getValue()

double Base::Quantity::getValue  | ( | | ) |  const  
---|---|---|---|---  
  
get the Value of the quantity

Referenced by
[ImageGui::ImageOrientationDialog::accept()](../../d0/dfa/classImageGui_1_1ImageOrientationDialog.html#a65393732ed8de93c798defb4cada7621),
[InspectionGui::VisualInspection::accept()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#a9f3542df70a4b485aebffadb7c9d9d6d),
[PartGui::DlgFilletEdges::accept()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#aa1cd2ae4ca0d1438188a366f36cdb552),
[PartGui::OffsetWidget::accept()](../../d9/d6d/classPartGui_1_1OffsetWidget.html#a791a744197288c394c011dbb879a143c),
[PartGui::ThicknessWidget::accept()](../../d5/d25/classPartGui_1_1ThicknessWidget.html#a56dbb59f2cea1ccb8c8b842997c35f48),
[MeshPartGui::CrossSections::apply()](../../d1/d27/classMeshPartGui_1_1CrossSections.html#a448e9bda9e7d893edf0520bbcff985b0),
[Gui::QuantitySpinBox::apply()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#ac3ec986d0729752d078f3c57a18f7cca),
[ConstraintItem::data()](../../d3/d0f/classConstraintItem.html#a58e0ecc1824934b77e25bc0b319b6c51),
[PartGui::DlgPrimitives::DlgPrimitives()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a27827c66a9f047547fe0b7169251b97d),
[SketcherGui::PropertyConstraintListItem::event()](../../dd/d04/classSketcherGui_1_1PropertyConstraintListItem.html#a846f5f3af8e0ee30f4d89ef894e7f60d),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[FemGui::TaskFemConstraintForce::getForce()](../../d2/d46/classFemGui_1_1TaskFemConstraintForce.html#ae8a5b9e668dd50280d1b33cefca6ffdd),
[Gui::LocationWidget::getPosition()](../../d9/d9a/classGui_1_1LocationWidget.html#a768cc96a3eafbedc4ee8ebb2821990c5),
[InspectionGui::VisualInspection::loadSettings()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#a81be250d84f75296fbe4a4a26272f5f9),
[MeshGui::DlgSettingsImportExport::loadSettings()](../../d4/d21/classMeshGui_1_1DlgSettingsImportExport.html#ac86b335632ce0ebd73b0994e6e59b491),
[TechDraw::DrawSVGTemplate::processTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a9b2032d4f9db58231ae4ad79ca5b3778),
[App::pyFromQuantity()](../../dd/dc2/namespaceApp.html#a1f508e13586e74f78640fce6b915e8ca),
[Gui::InputField::rawValue()](../../da/dfa/classGui_1_1InputField.html#a35eef38fa759893c9237becc3e25dbf6),
[InspectionGui::VisualInspection::saveSettings()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#a9967250b51cfede16509f732267a3a05),
[MeshGui::DlgSettingsImportExport::saveSettings()](../../d4/d21/classMeshGui_1_1DlgSettingsImportExport.html#aedf19f8cce93c37815ffefc51672fb61),
[Base::UnitsSchemaImperial1::schemaTranslate()](../../d5/de7/classBase_1_1UnitsSchemaImperial1.html#ac00ea4fe3402ac6533d780cbadbf730e),
[Base::UnitsSchemaImperialBuilding::schemaTranslate()](../../d6/dbc/classBase_1_1UnitsSchemaImperialBuilding.html#a1a40db59db95824550d13a75a0f9d7b1),
[Base::UnitsSchemaImperialCivil::schemaTranslate()](../../dd/db3/classBase_1_1UnitsSchemaImperialCivil.html#a51365e26e85ced53aa9a2c8421f098bc),
[Base::UnitsSchemaInternal::schemaTranslate()](../../db/d09/classBase_1_1UnitsSchemaInternal.html#a69c2732a4e9dd5d35ef7a7529985a49d),
[Base::UnitsSchemaMKS::schemaTranslate()](../../d0/dd5/classBase_1_1UnitsSchemaMKS.html#a97e76321d16eb1a817d24df99e23c7e2),
[Gui::InputField::setMaximum()](../../da/dfa/classGui_1_1InputField.html#a0adb6cc5e152513b67c34de516233bcf),
[Gui::InputField::setMinimum()](../../da/dfa/classGui_1_1InputField.html#a8c232ad5b7df7f8389eba65f0dc1e34e),
[App::PropertyQuantity::setPyObject()](../../d4/d65/classApp_1_1PropertyQuantity.html#a72be43d71c5e5a5e0a174c01df176dc9),
[App::PropertyQuantityConstraint::setPyObject()](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#a299ac9ee7870f29d5c3640a14114fcbe),
[Gui::InputField::setValue()](../../da/dfa/classGui_1_1InputField.html#a781543765d484715f02462acc7f3522a),
[Base::UnitsSchema::toLocale()](../../d9/dc7/classBase_1_1UnitsSchema.html#aacde4020d5617f0e65769350940f0a44),
and
[Gui::Dialog::DlgUnitsCalculator::valueChanged()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a32bc446c35a2e71d1cb25fca0bafba08).

## ◆ getValueAs()

double Quantity::getValueAs  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _q_| ) |  const  
---|---|---|---|---|---  
  
get the Value in a special unit given as quantity.

One can use one of the predifeined quantity units in this class

Referenced by
[FemGui::TaskFemConstraintTemperature::get_cflux()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a4eeda78f7f4c6353c9f5fa6727e4d273),
[FemGui::TaskFemConstraintSpring::get_normalStiffness()](../../d9/d3e/classFemGui_1_1TaskFemConstraintSpring.html#a7282a19d7810c7b5bbb0636732999051),
[FemGui::TaskFemConstraintPressure::get_Pressure()](../../dc/dd9/classFemGui_1_1TaskFemConstraintPressure.html#a45b78410db3eba292d027478754af4d3),
[FemGui::TaskFemConstraintSpring::get_tangentialStiffness()](../../d9/d3e/classFemGui_1_1TaskFemConstraintSpring.html#a4805d89f9573e443517335bf918193c3),
[FemGui::TaskFemConstraintInitialTemperature::get_temperature()](../../dd/d2a/classFemGui_1_1TaskFemConstraintInitialTemperature.html#a8eaf9311781406e3ce5df8b9a9e6d73c),
[FemGui::TaskFemConstraintTemperature::get_temperature()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a7f40dc26175aafedf920aedda36ef20b),
[FemGui::TaskFemConstraintHeatflux::getAmbientTemp()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a0569d894da587f350bb34490a70cdaab),
and
[FemGui::TaskFemConstraintHeatflux::getFilmCoef()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a579c61f84074d340e8f69d95e6403443).

## ◆ isDimensionless()

[bool](../../d9/db9/classbool.html) Quantity::isDimensionless  | ( | | ) |  const  
---|---|---|---|---  
  
true if it has a number without a unit

References
[isValid()](../../d8/d18/classBase_1_1Quantity.html#a085bb0d9a01b323009b018810bf03f91).

## ◆ isQuantity()

[bool](../../d9/db9/classbool.html) Quantity::isQuantity  | ( | | ) |  const  
---|---|---|---|---  
  
true if it has a number and a valid unit

References
[isValid()](../../d8/d18/classBase_1_1Quantity.html#a085bb0d9a01b323009b018810bf03f91).

## ◆ isValid()

[bool](../../d9/db9/classbool.html) Quantity::isValid  | ( | | ) |  const  
---|---|---|---|---  
  
true if it has a number with or without a unit

Referenced by
[isDimensionless()](../../d8/d18/classBase_1_1Quantity.html#abae817184245a734a29b5bbb261958b7),
and
[isQuantity()](../../d8/d18/classBase_1_1Quantity.html#a7e39882b2a5359ff53b2f7f0a85f510b).

## ◆ operator*() [1/2]

[Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::operator*  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _p_| ) |  const  
---|---|---|---|---|---  
  
Operators.

References
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1).

## ◆ operator*() [2/2]

[Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::operator*  | ( | double  | _p_| ) |  const  
---|---|---|---|---|---  
  
References
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1).

## ◆ operator+()

[Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::operator+  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _p_| ) |  const  
---|---|---|---|---|---  
  
References
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1).

## ◆ operator+=()

[Quantity](../../d8/d18/classBase_1_1Quantity.html) & Quantity::operator+=  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _p_| ) |   
---|---|---|---|---|---  
  
## ◆ operator-() [1/2]

[Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::operator-  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1).

## ◆ operator-() [2/2]

[Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::operator-  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _p_| ) |  const  
---|---|---|---|---|---  
  
References
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1).

## ◆ operator-=()

[Quantity](../../d8/d18/classBase_1_1Quantity.html) & Quantity::operator-=  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _p_| ) |   
---|---|---|---|---|---  
  
## ◆ operator/() [1/2]

[Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::operator/  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _p_| ) |  const  
---|---|---|---|---|---  
  
References
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1).

## ◆ operator/() [2/2]

[Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::operator/  | ( | double  | _p_| ) |  const  
---|---|---|---|---|---  
  
References
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1).

## ◆ operator<()

[bool](../../d9/db9/classbool.html) Quantity::operator< | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator<=()

[bool](../../d9/db9/classbool.html) Quantity::operator<=  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator=()

[Quantity](../../d8/d18/classBase_1_1Quantity.html) & Quantity::operator=  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _New_| ) |   
---|---|---|---|---|---  
  
## ◆ operator==()

[bool](../../d9/db9/classbool.html) Quantity::operator==  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator>()

[bool](../../d9/db9/classbool.html) Quantity::operator> | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator>=()

[bool](../../d9/db9/classbool.html) Quantity::operator>=  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _that_| ) |  const  
---|---|---|---|---|---  
  
## ◆ parse()

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::parse  | ( | const QString & | _string_| ) |   
---|---|---|---|---|---  
static  
  
References
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1).

Referenced by
[BOPTools.GeneralFuseResult.GeneralFuseResult::explodeCompounds()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#acaa64b16d29f0065ce1379f8dc572649),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[Gui::QuantitySpinBoxPrivate::parseString()](../../dd/d08/classGui_1_1QuantitySpinBoxPrivate.html#afe56518034e47b6facd52081c434a585),
[TechDraw::DrawSVGTemplate::processTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a9b2032d4f9db58231ae4ad79ca5b3778),
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a372908a1fc1cc656c746637f712e55f7),
[Gui::InputField::setRawText()](../../da/dfa/classGui_1_1InputField.html#addbe1c46fd12e6963054603cd5442acb),
[Gui::InputField::setUnitText()](../../da/dfa/classGui_1_1InputField.html#afe9df9976a2874ec346f633925874daf),
[Gui::QuantitySpinBox::setUnitText()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#ab7f8050e8114c81fc3b5336685c67a34),
[Base::UnitsApi::sParseQuantity()](../../d9/d89/classBase_1_1UnitsApi.html#a2a6b87ba7a38e42cb3634df0c7838703),
[BOPTools.GeneralFuseResult.GeneralFuseResult::splitAggregates()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ac2dd77595b00ad1c612310df00438702),
[Base::UnitsApi::toDouble()](../../d9/d89/classBase_1_1UnitsApi.html#af49c92c2bcd9925f0d2c8d3a4a469525),
[Base::UnitsApi::toQuantity()](../../d9/d89/classBase_1_1UnitsApi.html#a57451bfd07916cd5041e899e33d17d8a),
[Base::Unit::Unit()](../../d2/d37/classBase_1_1Unit.html#abbfe43509b2db5c3403ae90c3ef0b5d8),
and
[Gui::Dialog::DlgUnitsCalculator::valueChanged()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a32bc446c35a2e71d1cb25fca0bafba08).

## ◆ pow() [1/2]

[Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::pow  | ( | const [Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _p_| ) |  const  
---|---|---|---|---|---  
  
References
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1).

## ◆ pow() [2/2]

[Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::pow  | ( | double  | _p_| ) |  const  
---|---|---|---|---|---  
  
References
[Quantity()](../../d8/d18/classBase_1_1Quantity.html#a8f8e97615d1a60464a9af75c9c7ec9b1).

## ◆ setFormat()

void Base::Quantity::setFormat  | ( | const [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html) & | _f_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Sketcher::Constraint::getPresentationValue()](../../d6/def/classSketcher_1_1Constraint.html#a9be53639cd1e5e49f23c61862430874b),
[PathScripts.PathInspect.GCodeHighlighter::highlightBlock()](../../d4/d51/classPathScripts_1_1PathInspect_1_1GCodeHighlighter.html#aa55fcf99e6ca5c8f43ea6ab7fdbfe723),
[PathScripts.PostUtils.GCodeHighlighter::highlightBlock()](../../d4/d7c/classPathScripts_1_1PostUtils_1_1GCodeHighlighter.html#acd6d804f8a6f69abf0d41cd853e2ebd6),
[Gui::InputField::setFormat()](../../da/dfa/classGui_1_1InputField.html#a25118d14b9aa233f5b604fdd6ae35abe),
and
[Gui::InputField::setPrecision()](../../da/dfa/classGui_1_1InputField.html#aa5214b250f577c5f53ce0f4e74140566).

## ◆ setInvalid()

void Quantity::setInvalid  | ( | | ) |   
---|---|---|---|---  
  
sets the quantity invalid

## ◆ setUnit()

void Base::Quantity::setUnit  | ( | const [Unit](../../d2/d37/classBase_1_1Unit.html) & | _un_| ) |   
---|---|---|---|---|---  
  
set the unit of the quantity

Referenced by
[SketcherGui::EditDatumDialog::exec()](../../d6/d55/classSketcherGui_1_1EditDatumDialog.html#ae2acb3ba391ab2b817662e85aa8134fd),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[Sketcher::Constraint::getPresentationValue()](../../d6/def/classSketcher_1_1Constraint.html#a9be53639cd1e5e49f23c61862430874b),
[TechDraw::DrawSVGTemplate::processTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a9b2032d4f9db58231ae4ad79ca5b3778),
[TechDrawGui::TaskCenterLine::setUiEdit()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a44074b04e6f03fde63d2f4ac7a3f0c33),
[TechDrawGui::TaskCenterLine::setUiPrimary()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a87a1eafc1c37ac2e6c0bbf8bfb73717a),
[Gui::InputField::setUnit()](../../da/dfa/classGui_1_1InputField.html#a368ce42b96026b9cccc6dfdb5b348516),
[Gui::QuantitySpinBoxPrivate::validate()](../../dd/d08/classGui_1_1QuantitySpinBoxPrivate.html#a3a7b86da24888398add92a65193c9b62),
and
[SketcherGui::PropertyConstraintListItem::value()](../../dd/d04/classSketcherGui_1_1PropertyConstraintListItem.html#afbd28ea5bf2d11eedc5c916575b9a5a1).

## ◆ setValue()

void Base::Quantity::setValue  | ( | double  | _val_| ) |   
---|---|---|---|---|---  
  
set the value of the quantity

Referenced by
[SketcherGui::EditDatumDialog::exec()](../../d6/d55/classSketcherGui_1_1EditDatumDialog.html#ae2acb3ba391ab2b817662e85aa8134fd),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[Sketcher::Constraint::getPresentationValue()](../../d6/def/classSketcher_1_1Constraint.html#a9be53639cd1e5e49f23c61862430874b),
[Gui::View3DInventorViewer::printDimension()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a1b066921ad0a7a3e9e3fb53fb5657993),
[Gui::schemaTranslatePoint()](../../d9/dad/namespaceGui.html#a79417ca85a106b7d7b516d99443fd81f),
[Gui::InputField::setMaximum()](../../da/dfa/classGui_1_1InputField.html#a0adb6cc5e152513b67c34de516233bcf),
[Gui::InputField::setMinimum()](../../da/dfa/classGui_1_1InputField.html#a8c232ad5b7df7f8389eba65f0dc1e34e),
[App::PropertyQuantityConstraint::setPyObject()](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#a299ac9ee7870f29d5c3640a14114fcbe),
[TechDrawGui::TaskCenterLine::setUiEdit()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a44074b04e6f03fde63d2f4ac7a3f0c33),
[TechDrawGui::TaskCenterLine::setUiPrimary()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a87a1eafc1c37ac2e6c0bbf8bfb73717a),
[Gui::InputField::setValue()](../../da/dfa/classGui_1_1InputField.html#a781543765d484715f02462acc7f3522a),
[Gui::QuantitySpinBox::setValue()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#adbe27d2f5e0112c988c7f0a5855527f9),
and
[SketcherGui::PropertyConstraintListItem::value()](../../dd/d04/classSketcherGui_1_1PropertyConstraintListItem.html#afbd28ea5bf2d11eedc5c916575b9a5a1).

## Member Data Documentation

## ◆ Ampere

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Ampere  
---  
static  
  
## ◆ AngMinute

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::AngMinute  
---  
static  
  
## ◆ AngSecond

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::AngSecond  
---  
static  
  
## ◆ Bar

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Bar  
---  
static  
  
## ◆ Calorie

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Calorie  
---  
static  
  
## ◆ Candela

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Candela  
---  
static  
  
## ◆ CentiMetre

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::CentiMetre  
---  
static  
  
## ◆ Coulomb

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Coulomb  
---  
static  
  
## ◆ CubicFoot

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::CubicFoot  
---  
static  
  
## ◆ DeciMetre

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::DeciMetre  
---  
static  
  
## ◆ Degree

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Degree  
---  
static  
  
Referenced by
[PartGui::DlgRevolution::getAngle()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a6d1ef61d9b84c138c48c61f20772d94e).

## ◆ ElectronVolt

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::ElectronVolt  
---  
static  
  
## ◆ Farad

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Farad  
---  
static  
  
## ◆ Foot

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Foot  
---  
static  
  
## ◆ Gauss

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Gauss  
---  
static  
  
## ◆ GigaHertz

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::GigaHertz  
---  
static  
  
## ◆ GigaPascal

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::GigaPascal  
---  
static  
  
## ◆ Gon

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Gon  
---  
static  
  
## ◆ Gram

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Gram  
---  
static  
  
## ◆ Henry

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Henry  
---  
static  
  
## ◆ Hertz

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Hertz  
---  
static  
  
## ◆ Hour

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Hour  
---  
static  
  
## ◆ Hundredweights

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Hundredweights  
---  
static  
  
## ◆ Inch

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Inch  
---  
static  
  
## ◆ Joule

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Joule  
---  
static  
  
## ◆ Kelvin

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Kelvin  
---  
static  
  
Referenced by
[FemGui::TaskFemConstraintInitialTemperature::get_temperature()](../../dd/d2a/classFemGui_1_1TaskFemConstraintInitialTemperature.html#a8eaf9311781406e3ce5df8b9a9e6d73c),
[FemGui::TaskFemConstraintTemperature::get_temperature()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a7f40dc26175aafedf920aedda36ef20b),
and
[FemGui::TaskFemConstraintHeatflux::getAmbientTemp()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a0569d894da587f350bb34490a70cdaab).

## ◆ KiloAmpere

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloAmpere  
---  
static  
  
## ◆ KiloCalorie

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloCalorie  
---  
static  
  
## ◆ KiloElectronVolt

| [Quantity](../../d8/d18/classBase_1_1Quantity.html)
Quantity::KiloElectronVolt  
---  
static  
  
## ◆ KiloGram

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloGram  
---  
static  
  
## ◆ KiloHertz

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloHertz  
---  
static  
  
## ◆ KiloJoule

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloJoule  
---  
static  
  
## ◆ KiloMetre

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloMetre  
---  
static  
  
## ◆ KiloNewton

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloNewton  
---  
static  
  
## ◆ KiloNewtonPerMeter

| [Quantity](../../d8/d18/classBase_1_1Quantity.html)
Quantity::KiloNewtonPerMeter  
---  
static  
  
## ◆ KiloOhm

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloOhm  
---  
static  
  
## ◆ KiloPascal

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloPascal  
---  
static  
  
## ◆ KiloSiemens

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloSiemens  
---  
static  
  
## ◆ KiloVolt

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloVolt  
---  
static  
  
## ◆ KiloWatt

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloWatt  
---  
static  
  
## ◆ KiloWattHour

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KiloWattHour  
---  
static  
  
## ◆ KMH

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KMH  
---  
static  
  
## ◆ KSI

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::KSI  
---  
static  
  
## ◆ Liter

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Liter  
---  
static  
  
## ◆ MegaAmpere

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MegaAmpere  
---  
static  
  
## ◆ MegaElectronVolt

| [Quantity](../../d8/d18/classBase_1_1Quantity.html)
Quantity::MegaElectronVolt  
---  
static  
  
## ◆ MegaHertz

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MegaHertz  
---  
static  
  
## ◆ MegaNewton

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MegaNewton  
---  
static  
  
## ◆ MegaNewtonPerMeter

| [Quantity](../../d8/d18/classBase_1_1Quantity.html)
Quantity::MegaNewtonPerMeter  
---  
static  
  
## ◆ MegaOhm

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MegaOhm  
---  
static  
  
## ◆ MegaPascal

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MegaPascal  
---  
static  
  
Referenced by
[FemGui::TaskFemConstraintPressure::get_Pressure()](../../dc/dd9/classFemGui_1_1TaskFemConstraintPressure.html#a45b78410db3eba292d027478754af4d3).

## ◆ MegaSiemens

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MegaSiemens  
---  
static  
  
## ◆ Metre

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Metre  
---  
static  
  
## ◆ MicroFarad

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MicroFarad  
---  
static  
  
## ◆ MicroGram

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MicroGram  
---  
static  
  
## ◆ MicroHenry

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MicroHenry  
---  
static  
  
## ◆ MicroKelvin

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MicroKelvin  
---  
static  
  
## ◆ MicroMetre

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MicroMetre  
---  
static  
  
## ◆ MicroSiemens

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MicroSiemens  
---  
static  
  
## ◆ Mile

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Mile  
---  
static  
  
## ◆ MilePerHour

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilePerHour  
---  
static  
  
## ◆ MilliAmpere

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliAmpere  
---  
static  
  
## ◆ MilliBar

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliBar  
---  
static  
  
## ◆ MilliFarad

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliFarad  
---  
static  
  
## ◆ MilliGram

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliGram  
---  
static  
  
## ◆ MilliHenry

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliHenry  
---  
static  
  
## ◆ MilliJoule

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliJoule  
---  
static  
  
## ◆ MilliKelvin

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliKelvin  
---  
static  
  
## ◆ MilliLiter

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliLiter  
---  
static  
  
## ◆ MilliMetre

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliMetre  
---  
static  
  
Referenced by
[PartGui::DlgRevolution::getPosition()](../../d1/d83/classPartGui_1_1DlgRevolution.html#ac1ba85519d9e6919df6e693493f9fa79),
[Gui::View3DInventorViewer::printDimension()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a1b066921ad0a7a3e9e3fb53fb5657993),
and
[Gui::schemaTranslatePoint()](../../d9/dad/namespaceGui.html#a79417ca85a106b7d7b516d99443fd81f).

## ◆ MilliMole

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliMole  
---  
static  
  
## ◆ MilliNewton

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliNewton  
---  
static  
  
## ◆ MilliNewtonPerMeter

| [Quantity](../../d8/d18/classBase_1_1Quantity.html)
Quantity::MilliNewtonPerMeter  
---  
static  
  
## ◆ MilliSiemens

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliSiemens  
---  
static  
  
## ◆ MilliVolt

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliVolt  
---  
static  
  
## ◆ MilliWatt

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MilliWatt  
---  
static  
  
## ◆ Minute

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Minute  
---  
static  
  
## ◆ Mole

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Mole  
---  
static  
  
## ◆ MPH

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MPH  
---  
static  
  
## ◆ MPSI

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::MPSI  
---  
static  
  
## ◆ mTorr

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::mTorr  
---  
static  
  
## ◆ NanoFarad

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::NanoFarad  
---  
static  
  
## ◆ NanoHenry

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::NanoHenry  
---  
static  
  
## ◆ NanoMetre

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::NanoMetre  
---  
static  
  
Predefined [Unit](../../d2/d37/classBase_1_1Unit.html "The Unit class.")
types.

## ◆ Newton

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Newton  
---  
static  
  
## ◆ NewtonMeter

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::NewtonMeter  
---  
static  
  
## ◆ NewtonPerMeter

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::NewtonPerMeter  
---  
static  
  
Referenced by
[FemGui::TaskFemConstraintSpring::get_normalStiffness()](../../d9/d3e/classFemGui_1_1TaskFemConstraintSpring.html#a7282a19d7810c7b5bbb0636732999051),
and
[FemGui::TaskFemConstraintSpring::get_tangentialStiffness()](../../d9/d3e/classFemGui_1_1TaskFemConstraintSpring.html#a4805d89f9573e443517335bf918193c3).

## ◆ Oersted

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Oersted  
---  
static  
  
## ◆ Ohm

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Ohm  
---  
static  
  
## ◆ Ounce

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Ounce  
---  
static  
  
## ◆ Pascal

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Pascal  
---  
static  
  
## ◆ PicoFarad

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::PicoFarad  
---  
static  
  
## ◆ Pound

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Pound  
---  
static  
  
## ◆ PoundForce

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::PoundForce  
---  
static  
  
## ◆ PSI

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::PSI  
---  
static  
  
## ◆ Radian

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Radian  
---  
static  
  
## ◆ Second

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Second  
---  
static  
  
## ◆ Siemens

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Siemens  
---  
static  
  
## ◆ SquareFoot

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::SquareFoot  
---  
static  
  
## ◆ Stone

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Stone  
---  
static  
  
## ◆ TeraHertz

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::TeraHertz  
---  
static  
  
## ◆ Tesla

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Tesla  
---  
static  
  
## ◆ Thou

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Thou  
---  
static  
  
## ◆ Ton

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Ton  
---  
static  
  
## ◆ Torr

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Torr  
---  
static  
  
## ◆ Volt

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Volt  
---  
static  
  
## ◆ VoltAmpere

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::VoltAmpere  
---  
static  
  
## ◆ VoltAmpereSecond

| [Quantity](../../d8/d18/classBase_1_1Quantity.html)
Quantity::VoltAmpereSecond  
---  
static  
  
## ◆ Watt

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Watt  
---  
static  
  
Referenced by
[FemGui::TaskFemConstraintTemperature::get_cflux()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a4eeda78f7f4c6353c9f5fa6727e4d273).

## ◆ WattSecond

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::WattSecond  
---  
static  
  
## ◆ Weber

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Weber  
---  
static  
  
## ◆ Yard

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::Yard  
---  
static  
  
## ◆ yTorr

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) Quantity::yTorr  
---  
static  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Quantity.h
  * FreeCAD/src/Base/Quantity.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

