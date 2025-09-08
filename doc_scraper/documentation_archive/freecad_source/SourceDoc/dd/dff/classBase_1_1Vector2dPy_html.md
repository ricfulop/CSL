---
url: https://freecad.github.io/SourceDoc/dd/dff/classBase_1_1Vector2dPy.html
scraped_at: 2025-09-08T15:18:09.345192
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Vector2dPy](../../dd/dff/classBase_1_1Vector2dPy.html)

[List of all members](../../d4/d16/classBase_1_1Vector2dPy-members.html) | Public Member Functions | Static Public Member Functions

Base::Vector2dPy Class Reference

`#include <GeometryPyCXX.h>`

##  Public Member Functions  
  
---  
Py::Object | [getattro](../../dd/dff/classBase_1_1Vector2dPy.html#ad3f96c7f3e6382f7fffbac01348fd74c) (const Py::String &name_)  
virtual Py::Object | [repr](../../dd/dff/classBase_1_1Vector2dPy.html#a2009f32e214d51eba4aea503c7515114) ()  
[int](../../d1/da0/classint.html) | [setattro](../../dd/dff/classBase_1_1Vector2dPy.html#aa3398bdfb19b8a6dbc58907ca4ead24a) (const Py::String &name_, const Py::Object &[value](../../dd/dff/classBase_1_1Vector2dPy.html#af9432fa276819908ba23b0bfbfa6059b))  
void | [setValue](../../dd/dff/classBase_1_1Vector2dPy.html#ae435c1c17612416638add8d9cafcc753) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &n)  
void | [setValue](../../dd/dff/classBase_1_1Vector2dPy.html#a096a0daa83bc34e888240bd7cb79ab7e) (double x, double y)  
const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | [value](../../dd/dff/classBase_1_1Vector2dPy.html#af9432fa276819908ba23b0bfbfa6059b) () const  
|
[Vector2dPy](../../dd/dff/classBase_1_1Vector2dPy.html#a42be5b939cf969d8f2a4748f2056123d)
(Py::PythonClassInstance *self, Py::Tuple &args, Py::Dict &kwds)  
virtual | [~Vector2dPy](../../dd/dff/classBase_1_1Vector2dPy.html#a1da577569104ee44ec316c8c6065db29) ()  
  
##  Static Public Member Functions  
  
---  
static Py::PythonType & | [behaviors](../../dd/dff/classBase_1_1Vector2dPy.html#ac2cd7c000a75bc758ed6abfd18a6cfd7) ()  
static [bool](../../d9/db9/classbool.html) | [check](../../dd/dff/classBase_1_1Vector2dPy.html#a01818250d3448422ba91c4f3de3f3fab) ([PyObject](../../df/d1b/classPyObject.html) *p)  
static Py::PythonClassObject< [Vector2dPy](../../dd/dff/classBase_1_1Vector2dPy.html) > | [create](../../dd/dff/classBase_1_1Vector2dPy.html#a2ff9f7e167d84cee5e2e83c4382575ec) (const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) &)  
static Py::PythonClassObject< [Vector2dPy](../../dd/dff/classBase_1_1Vector2dPy.html) > | [create](../../dd/dff/classBase_1_1Vector2dPy.html#ad607a71df15a9a5a98086e32b7c031fc) (double x, double y)  
static void | [init_type](../../dd/dff/classBase_1_1Vector2dPy.html#a2e059c53efba7f535487af05ce4961f4) ()  
static PyTypeObject * | [type_object](../../dd/dff/classBase_1_1Vector2dPy.html#a345868f84b558d96d7479f2d6005a84e) ()  
  
## methods for group handling  
  
---  
virtual Py::Object | [number_negative](../../dd/dff/classBase_1_1Vector2dPy.html#adbb4bb3b1ebdef0c7ec9bb60daf3b43e) ()  
virtual Py::Object | [number_positive](../../dd/dff/classBase_1_1Vector2dPy.html#a3887d3074ddc43b4fe90a574041861ba) ()  
virtual Py::Object | [number_absolute](../../dd/dff/classBase_1_1Vector2dPy.html#adc30aa4f59cb70b5f56d943ccf9de308) ()  
virtual Py::Object | [number_invert](../../dd/dff/classBase_1_1Vector2dPy.html#aa0370cd743b4c1c3ffb5bf7c1e07fa0e) ()  
virtual Py::Object | [number_int](../../dd/dff/classBase_1_1Vector2dPy.html#a8c1b7904f4d452ab1e7b8535b85c159a) ()  
virtual Py::Object | [number_float](../../dd/dff/classBase_1_1Vector2dPy.html#a65ba1d2d814f834e32f375ede7b6e4a7) ()  
virtual Py::Object | [number_long](../../dd/dff/classBase_1_1Vector2dPy.html#a064b3f287d559856e9a8a681e7f244d5) ()  
virtual Py::Object | [number_add](../../dd/dff/classBase_1_1Vector2dPy.html#aa71ecfdbce45f4c12f4be49470ba1e58) (const Py::Object &)  
virtual Py::Object | [number_subtract](../../dd/dff/classBase_1_1Vector2dPy.html#a6126101bbebe04ffec59889e23e30d7f) (const Py::Object &)  
virtual Py::Object | [number_multiply](../../dd/dff/classBase_1_1Vector2dPy.html#aa3044fcc6630b8bca02276e75a8f8f69) (const Py::Object &)  
virtual Py::Object | [number_remainder](../../dd/dff/classBase_1_1Vector2dPy.html#a18f414628b8e1b9a0230861b77d8c152) (const Py::Object &)  
virtual Py::Object | [number_divmod](../../dd/dff/classBase_1_1Vector2dPy.html#a55665dfa390d20d29278b88054ac5205) (const Py::Object &)  
virtual Py::Object | [number_lshift](../../dd/dff/classBase_1_1Vector2dPy.html#aa5c6d66e0acec739d469ef3d12c11eb0) (const Py::Object &)  
virtual Py::Object | [number_rshift](../../dd/dff/classBase_1_1Vector2dPy.html#a6187249c61be795e68d05ab42484e82f) (const Py::Object &)  
virtual Py::Object | [number_and](../../dd/dff/classBase_1_1Vector2dPy.html#a3becbb81ec0de0840ee517dbb19047ea) (const Py::Object &)  
virtual Py::Object | [number_xor](../../dd/dff/classBase_1_1Vector2dPy.html#a2df2f472cb69a3643a462afbe32aeb5d) (const Py::Object &)  
virtual Py::Object | [number_or](../../dd/dff/classBase_1_1Vector2dPy.html#afa023780932e6fb679a8b0e04b50d824) (const Py::Object &)  
virtual Py::Object | [number_power](../../dd/dff/classBase_1_1Vector2dPy.html#af97998597b79b87501e07ec778555ba7) (const Py::Object &, const Py::Object &)  
Py::Object | [isNull](../../dd/dff/classBase_1_1Vector2dPy.html#a43a11db4fac701ce6851aeba7a469cf9) (const Py::Tuple &)  
Py::Object | [length](../../dd/dff/classBase_1_1Vector2dPy.html#a7e1a5d534c27871651442ed0500680ca) (const Py::Tuple &)  
Py::Object | [atan2](../../dd/dff/classBase_1_1Vector2dPy.html#a7729e53c53902d3861bff9a1f62e6bdc) (const Py::Tuple &)  
Py::Object | [square](../../dd/dff/classBase_1_1Vector2dPy.html#a06f92cb707f3b47a0b6ddf53b397d600) (const Py::Tuple &)  
Py::Object | [scale](../../dd/dff/classBase_1_1Vector2dPy.html#add05ee8300c7a2bfd1958ed30011d250) (const Py::Tuple &)  
Py::Object | [rotate](../../dd/dff/classBase_1_1Vector2dPy.html#a126397ed00cab092454ff76342e0fe9a) (const Py::Tuple &)  
Py::Object | [normalize](../../dd/dff/classBase_1_1Vector2dPy.html#a1e3c051402cc394cabe8688b8ac4fe12) (const Py::Tuple &)  
Py::Object | [perpendicular](../../dd/dff/classBase_1_1Vector2dPy.html#aa699cf47abedf46be4bb3e180e04cc50) (const Py::Tuple &)  
Py::Object | [distance](../../dd/dff/classBase_1_1Vector2dPy.html#ac197d9d8dbdca9414c04e40671255c1f) (const Py::Tuple &)  
Py::Object | [isEqual](../../dd/dff/classBase_1_1Vector2dPy.html#a26ddd9179e23c8dc495e54196bb03eeb) (const Py::Tuple &)  
Py::Object | [getAngle](../../dd/dff/classBase_1_1Vector2dPy.html#a31f9b63c1174b8c8e08b31ba4cd5c544) (const Py::Tuple &)  
Py::Object | [projectToLine](../../dd/dff/classBase_1_1Vector2dPy.html#a4e9315292369bf25d18039b3962aff82) (const Py::Tuple &)  
  
## Constructor & Destructor Documentation

## ◆ Vector2dPy()

Base::Vector2dPy::Vector2dPy  | ( | Py::PythonClassInstance *  | _self_ ,   
---|---|---|---  
|  | Py::Tuple & | _args_ ,   
|  | Py::Dict & | _kwds_  
| ) | |   
  
## ◆ ~Vector2dPy()

| Base::Vector2dPy::~Vector2dPy  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ atan2()

Py::Object Base::Vector2dPy::atan2  | ( | const Py::Tuple & | | ) |   
---|---|---|---|---|---  
  
## ◆ behaviors()

| Py::PythonType & Base::Vector2dPy::behaviors  | ( | | ) |   
---|---|---|---|---  
static  
  
## ◆ check()

| [bool](../../d9/db9/classbool.html) Base::Vector2dPy::check  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _p_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[femsolver.run.Machine::reset()](../../d2/d54/classfemsolver_1_1run_1_1Machine.html#a343e584f0f5dfc40861c957397bd8952).

## ◆ create() [1/2]

| Py::PythonClassObject< [Vector2dPy](../../dd/dff/classBase_1_1Vector2dPy.html) > Base::Vector2dPy::create  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _v_| ) |   
---|---|---|---|---|---  
static  
  
References
[create()](../../dd/dff/classBase_1_1Vector2dPy.html#a2ff9f7e167d84cee5e2e83c4382575ec).

Referenced by
[draftguitools.gui_labels.Label::action()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a31d95b9c0428e8e5e2fc2c0e5ba1f9cf),
[create()](../../dd/dff/classBase_1_1Vector2dPy.html#a2ff9f7e167d84cee5e2e83c4382575ec),
[number_absolute()](../../dd/dff/classBase_1_1Vector2dPy.html#adc30aa4f59cb70b5f56d943ccf9de308),
[number_add()](../../dd/dff/classBase_1_1Vector2dPy.html#aa71ecfdbce45f4c12f4be49470ba1e58),
[number_multiply()](../../dd/dff/classBase_1_1Vector2dPy.html#aa3044fcc6630b8bca02276e75a8f8f69),
[number_negative()](../../dd/dff/classBase_1_1Vector2dPy.html#adbb4bb3b1ebdef0c7ec9bb60daf3b43e),
[number_positive()](../../dd/dff/classBase_1_1Vector2dPy.html#a3887d3074ddc43b4fe90a574041861ba),
and
[number_subtract()](../../dd/dff/classBase_1_1Vector2dPy.html#a6126101bbebe04ffec59889e23e30d7f).

## ◆ create() [2/2]

| Py::PythonClassObject< [Vector2dPy](../../dd/dff/classBase_1_1Vector2dPy.html) > Base::Vector2dPy::create  | ( | double  | _x_ ,   
---|---|---|---  
|  | double  | _y_  
| ) | |   
static  
  
Referenced by
[draftguitools.gui_labels.Label::action()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a31d95b9c0428e8e5e2fc2c0e5ba1f9cf).

## ◆ distance()

Py::Object Base::Vector2dPy::distance  | ( | const Py::Tuple & | _args_| ) |   
---|---|---|---|---|---  
  
Referenced by
[PathScripts.PathDressupDogbone.Bone::adaptiveLength()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#adde010e67251dab408b4c9737e25f0f8),
and
[PathScripts.PathDressupDogbone.Bone::corner()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#a3020aa4704bbeca155e81158067a80d2).

## ◆ getAngle()

Py::Object Base::Vector2dPy::getAngle  | ( | const Py::Tuple & | _args_| ) |   
---|---|---|---|---|---  
  
Referenced by
[PathScripts.PathDressupDogbone.Chord::getAngleXY()](../../de/dae/classPathScripts_1_1PathDressupDogbone_1_1Chord.html#a136f7141375ba1bfb89b4bdb75e45a1d),
[draftguitools.gui_trackers.arcTracker::setEndPoint()](../../da/d31/classdraftguitools_1_1gui__trackers_1_1arcTracker.html#aee82546a991bcc82d4bf0b3728aca8e7),
and
[draftguitools.gui_trackers.arcTracker::setStartPoint()](../../da/d31/classdraftguitools_1_1gui__trackers_1_1arcTracker.html#a28e7810138d3a50976ee404ca6ec8a8a).

## ◆ getattro()

Py::Object Base::Vector2dPy::getattro  | ( | const Py::String & | _name__| ) |   
---|---|---|---|---|---  
  
## ◆ init_type()

| void Base::Vector2dPy::init_type  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
References
[draftgeoutils.general::isNull()](../../d9/dfd/group__draftgeoutils.html#ga46bc138943ec567affb4334962cb64c5).

## ◆ isEqual()

Py::Object Base::Vector2dPy::isEqual  | ( | const Py::Tuple & | _args_| ) |   
---|---|---|---|---|---  
  
## ◆ isNull()

Py::Object Base::Vector2dPy::isNull  | ( | const Py::Tuple & | _args_| ) |   
---|---|---|---|---|---  
  
## ◆ length()

Py::Object Base::Vector2dPy::length  | ( | const Py::Tuple & | | ) |   
---|---|---|---|---|---  
  
Referenced by
[PathScripts.PathStock.StockFromBase::execute()](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#a9fa59e6edf99801ba45c953b49561ae2),
[PathScripts.PathDressupDogbone.ObjectDressup::execute()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a039b27cd647d900f54eb26078667be9b),
[PathScripts.PathFeatureExtensions.Extension::getSubLink()](../../d7/d86/classPathScripts_1_1PathFeatureExtensions_1_1Extension.html#a39e2f64b82ca08c5145654ac03f10cd8),
[PathScripts.PathFeatureExtensions.Extension::getWire()](../../d7/d86/classPathScripts_1_1PathFeatureExtensions_1_1Extension.html#a97954317b571ddd2f898d82a86db87ea),
and
[Mod.PartDesign.Scripts.FilletArc.Vector::norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20).

## ◆ normalize()

Py::Object Base::Vector2dPy::normalize  | ( | const Py::Tuple & | | ) |   
---|---|---|---|---|---  
  
Referenced by
[PathScripts.PathDressupLeadInOut.ObjectDressup::getLeadEnd()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#ac4be8c95d4aa1440fb03c096c4e44e57),
and
[PathScripts.PathDressupLeadInOut.ObjectDressup::getLeadStart()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#a2d9de34620ee069b425e7f99f0efe9da).

## ◆ number_absolute()

| Py::Object Base::Vector2dPy::number_absolute  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[create()](../../dd/dff/classBase_1_1Vector2dPy.html#a2ff9f7e167d84cee5e2e83c4382575ec).

## ◆ number_add()

| Py::Object Base::Vector2dPy::number_add  | ( | const Py::Object & | _py_| ) |   
---|---|---|---|---|---  
virtual  
  
References
[create()](../../dd/dff/classBase_1_1Vector2dPy.html#a2ff9f7e167d84cee5e2e83c4382575ec).

## ◆ number_and()

| Py::Object Base::Vector2dPy::number_and  | ( | const Py::Object & | | ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ number_divmod()

| Py::Object Base::Vector2dPy::number_divmod  | ( | const Py::Object & | | ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ number_float()

| Py::Object Base::Vector2dPy::number_float  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## ◆ number_int()

| Py::Object Base::Vector2dPy::number_int  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## ◆ number_invert()

| Py::Object Base::Vector2dPy::number_invert  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## ◆ number_long()

| Py::Object Base::Vector2dPy::number_long  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## ◆ number_lshift()

| Py::Object Base::Vector2dPy::number_lshift  | ( | const Py::Object & | | ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ number_multiply()

| Py::Object Base::Vector2dPy::number_multiply  | ( | const Py::Object & | _py_| ) |   
---|---|---|---|---|---  
virtual  
  
References
[create()](../../dd/dff/classBase_1_1Vector2dPy.html#a2ff9f7e167d84cee5e2e83c4382575ec),
and
[type_object()](../../dd/dff/classBase_1_1Vector2dPy.html#a345868f84b558d96d7479f2d6005a84e).

## ◆ number_negative()

| Py::Object Base::Vector2dPy::number_negative  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[create()](../../dd/dff/classBase_1_1Vector2dPy.html#a2ff9f7e167d84cee5e2e83c4382575ec).

## ◆ number_or()

| Py::Object Base::Vector2dPy::number_or  | ( | const Py::Object & | | ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ number_positive()

| Py::Object Base::Vector2dPy::number_positive  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[create()](../../dd/dff/classBase_1_1Vector2dPy.html#a2ff9f7e167d84cee5e2e83c4382575ec).

## ◆ number_power()

| Py::Object Base::Vector2dPy::number_power  | ( | const Py::Object & | ,   
---|---|---|---  
|  | const Py::Object & |   
| ) | |   
virtual  
  
## ◆ number_remainder()

| Py::Object Base::Vector2dPy::number_remainder  | ( | const Py::Object & | | ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ number_rshift()

| Py::Object Base::Vector2dPy::number_rshift  | ( | const Py::Object & | | ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ number_subtract()

| Py::Object Base::Vector2dPy::number_subtract  | ( | const Py::Object & | _py_| ) |   
---|---|---|---|---|---  
virtual  
  
References
[create()](../../dd/dff/classBase_1_1Vector2dPy.html#a2ff9f7e167d84cee5e2e83c4382575ec).

## ◆ number_xor()

| Py::Object Base::Vector2dPy::number_xor  | ( | const Py::Object & | | ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ perpendicular()

Py::Object Base::Vector2dPy::perpendicular  | ( | const Py::Tuple & | _args_| ) |   
---|---|---|---|---|---  
  
References
[femsolver.elmer.equations.elasticity::create()](../../dc/de2/group__FEM.html#ga1011d50c1014de9888c82c5f0f41eed3),
and
[Base::Vector2d::Perpendicular()](../../db/da7/classBase_1_1Vector2d.html#abdb2e2cf8278b63d20016982f23909f7).

## ◆ projectToLine()

Py::Object Base::Vector2dPy::projectToLine  | ( | const Py::Tuple & | _args_| ) |   
---|---|---|---|---|---  
  
## ◆ repr()

| Py::Object Base::Vector2dPy::repr  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## ◆ rotate()

Py::Object Base::Vector2dPy::rotate  | ( | const Py::Tuple & | _args_| ) |   
---|---|---|---|---|---  
  
Referenced by
[PathScripts.PathDressupLeadInOut.ObjectDressup::getLeadEnd()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#ac4be8c95d4aa1440fb03c096c4e44e57),
[PathScripts.PathDressupLeadInOut.ObjectDressup::getLeadStart()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#a2d9de34620ee069b425e7f99f0efe9da),
[draftguitools.gui_rotate.Rotate::numericRadius()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a9233be8153158528af33797d19c7dffd),
[ArchSectionPlane.SectionPlaneTaskPanel::rotateX()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a7d1ba8918bf98848d9ba29440e7c084d),
[ArchSectionPlane.SectionPlaneTaskPanel::rotateY()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#af9398626ca18b43945fc07cd1161d7cf),
and
[ArchSectionPlane.SectionPlaneTaskPanel::rotateZ()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a0a097c582cee6fcdab575dfb800e7d6d).

## ◆ scale()

Py::Object Base::Vector2dPy::scale  | ( | const Py::Tuple & | _args_| ) |   
---|---|---|---|---|---  
  
Referenced by
[automotive_design.cartesian_transformation_operator::scl()](../../d7/d5c/classautomotive__design_1_1cartesian__transformation__operator.html#a607065ae6d7bb5dacfd7c75bd6711dc5),
[config_control_design.cartesian_transformation_operator::scl()](../../d5/de5/classconfig__control__design_1_1cartesian__transformation__operator.html#a0f720927aeb8f85e823ae00966334520),
[ifc2x3.ifccartesiantransformationoperator::scl()](../../d8/d5d/classifc2x3_1_1ifccartesiantransformationoperator.html#a1230d04a4e6e505a3ea5cbb23a36f383),
and
[ifc4.ifccartesiantransformationoperator::scl()](../../d4/d39/classifc4_1_1ifccartesiantransformationoperator.html#a7a36aec732fadc2ec945b4ad3bc1570d).

## ◆ setattro()

[int](../../d1/da0/classint.html) Base::Vector2dPy::setattro  | ( | const Py::String & | _name__ ,   
---|---|---|---  
|  | const Py::Object & | _value_  
| ) | |   
  
## ◆ setValue() [1/2]

void Base::Vector2dPy::setValue  | ( | const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & | _n_| ) |   
---|---|---|---|---|---  
  
## ◆ setValue() [2/2]

void Base::Vector2dPy::setValue  | ( | double  | _x_ ,   
---|---|---|---  
|  | double  | _y_  
| ) | |   
  
## ◆ square()

Py::Object Base::Vector2dPy::square  | ( | const Py::Tuple & | | ) |   
---|---|---|---|---|---  
  
## ◆ type_object()

| PyTypeObject * Base::Vector2dPy::type_object  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[number_multiply()](../../dd/dff/classBase_1_1Vector2dPy.html#aa3044fcc6630b8bca02276e75a8f8f69).

## ◆ value()

const [Vector2d](../../db/da7/classBase_1_1Vector2d.html) & Base::Vector2dPy::value  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[PathScripts.PathProperty.Property::displayString()](../../d3/ddd/classPathScripts_1_1PathProperty_1_1Property.html#a173a46d5a9f2f780b67036cf91b44ac1),
[PathScripts.PathProperty.PropertyQuantity::displayString()](../../d7/db5/classPathScripts_1_1PathProperty_1_1PropertyQuantity.html#af9a746ffdfbbc9540ff8b12085256211),
[PathScripts.PathSetupSheetOpPrototype.Property::displayString()](../../d2/d60/classPathScripts_1_1PathSetupSheetOpPrototype_1_1Property.html#a248ab3fd35ec6b00fe1ef7e33522a605),
[PathScripts.PathSetupSheetOpPrototype.PropertyQuantity::displayString()](../../dc/d20/classPathScripts_1_1PathSetupSheetOpPrototype_1_1PropertyQuantity.html#ae82432702480407f52a44b6b626228cc),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction::evaluate()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a53b2bca87ec4a37fbc548844bc74212d),
[PathScripts.PathProperty.Property::getValue()](../../d3/ddd/classPathScripts_1_1PathProperty_1_1Property.html#a80dbf20503ac54ecb31d235ceb634978),
[PathScripts.PathSetupSheetOpPrototype.Property::getValue()](../../d2/d60/classPathScripts_1_1PathSetupSheetOpPrototype_1_1Property.html#a71e7b49240931f932458d78d61eec895),
[Mod.PartDesign.WizardShaft.SegmentFunction.IntervalFunction::lowervalue()](../../d9/d57/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1IntervalFunction.html#a0a29ae4528775248edef27893e9c34e9),
[PathScripts.PathProperty.Property::setValue()](../../d3/ddd/classPathScripts_1_1PathProperty_1_1Property.html#a48b66d08ffe443f72ff1f62667acf0e5),
and
[PathScripts.PathSetupSheetOpPrototype.Property::setValue()](../../d2/d60/classPathScripts_1_1PathSetupSheetOpPrototype_1_1Property.html#a18403b3b5b1d88520d51fa29a4fe86b1).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/GeometryPyCXX.h
  * FreeCAD/src/Base/GeometryPyCXX.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

