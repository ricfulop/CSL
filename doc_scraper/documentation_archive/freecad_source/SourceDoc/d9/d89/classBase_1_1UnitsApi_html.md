---
url: https://freecad.github.io/SourceDoc/d9/d89/classBase_1_1UnitsApi.html
scraped_at: 2025-09-08T15:17:39.210961
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [UnitsApi](../../d9/d89/classBase_1_1UnitsApi.html)

[List of all members](../../d8/d8f/classBase_1_1UnitsApi-members.html) | Static Public Member Functions | Static Public Attributes | Static Protected Member Functions | Static Protected Attributes

Base::UnitsApi Class Reference

The [UnitsApi](../../d9/d89/classBase_1_1UnitsApi.html "The UnitsApi.").
[More...](../../d9/d89/classBase_1_1UnitsApi.html#details)

`#include <UnitsApi.h>`

##  Static Public Member Functions  
  
---  
static [UnitsSchemaPtr](../../db/d07/namespaceBase.html#afc09c3320e308275ccc558d940d23d82) | [createSchema](../../d9/d89/classBase_1_1UnitsApi.html#a00b7c68f240fe64f078b839784f852bb) ([UnitSystem](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4) s)  
| return an instance of the given enum value
[More...](../../d9/d89/classBase_1_1UnitsApi.html#a00b7c68f240fe64f078b839784f852bb)  
  
static [int](../../d1/da0/classint.html) | [getDecimals](../../d9/d89/classBase_1_1UnitsApi.html#a7943af964989d408fde55b6b9c10ee55) ()  
static const char * | [getDescription](../../d9/d89/classBase_1_1UnitsApi.html#acdebcacc6cf6b3689c370e28e1763e4d) ([UnitSystem](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4))  
| Returns a brief description of a schema.
[More...](../../d9/d89/classBase_1_1UnitsApi.html#acdebcacc6cf6b3689c370e28e1763e4d)  
  
static [UnitSystem](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4) | [getSchema](../../d9/d89/classBase_1_1UnitsApi.html#adb0b4d16152a9163d8b8b3ad5fff2270) ()  
| return the active schema
[More...](../../d9/d89/classBase_1_1UnitsApi.html#adb0b4d16152a9163d8b8b3ad5fff2270)  
  
static QString | [schemaTranslate](../../d9/d89/classBase_1_1UnitsApi.html#a0f45bfff408d222fb36a04c9c96c3b17) (const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) &quant)  
static QString | [schemaTranslate](../../d9/d89/classBase_1_1UnitsApi.html#a4eee4ddbeb846ca0711919848eb53f63) (const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) &quant, double &factor, QString &unitString)  
static void | [setDecimals](../../d9/d89/classBase_1_1UnitsApi.html#a5d3e2de74a17b7fa8c57132c9191c755) ([int](../../d1/da0/classint.html))  
static void | [setSchema](../../d9/d89/classBase_1_1UnitsApi.html#af7f98f49a6e2b5fcf1089d679a79ab2f) ([UnitSystem](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4) s)  
| set Schema set the [UnitsSchema](../../d9/dc7/classBase_1_1UnitsSchema.html
"The UnitSchema class The subclasses of this class define the stuff for a
certain units schema.") of the Application this a represented by a class of
type UnitSchema which defines a set of standard units for that schema and
rules for representative strings.
[More...](../../d9/d89/classBase_1_1UnitsApi.html#af7f98f49a6e2b5fcf1089d679a79ab2f)  
  
static double | [toDouble](../../d9/d89/classBase_1_1UnitsApi.html#af49c92c2bcd9925f0d2c8d3a4a469525) ([PyObject](../../df/d1b/classPyObject.html) *args, const [Base::Unit](../../d2/d37/classBase_1_1Unit.html) &u=[Base::Unit](../../d2/d37/classBase_1_1Unit.html)())  
| generate a value for a quantity with default user preferred system
[More...](../../d9/d89/classBase_1_1UnitsApi.html#af49c92c2bcd9925f0d2c8d3a4a469525)  
  
static QString | [toNumber](../../d9/d89/classBase_1_1UnitsApi.html#a4165d414771ff35b19ace249f486098a) (const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) &q, const [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html) &f=[QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html)([QuantityFormat::Default](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679a4decd52211cc4ee023d485a6f8c78ea0)))  
| Get a number as string for a quantity of a given format.
[More...](../../d9/d89/classBase_1_1UnitsApi.html#a4165d414771ff35b19ace249f486098a)  
  
static QString | [toNumber](../../d9/d89/classBase_1_1UnitsApi.html#a972deb3023d5801fcdc30fec674ee094) (double d, const [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html) &f=[QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html)([QuantityFormat::Default](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679a4decd52211cc4ee023d485a6f8c78ea0)))  
| Get a number as string for a double of a given format.
[More...](../../d9/d89/classBase_1_1UnitsApi.html#a972deb3023d5801fcdc30fec674ee094)  
  
static [Quantity](../../d8/d18/classBase_1_1Quantity.html) | [toQuantity](../../d9/d89/classBase_1_1UnitsApi.html#a57451bfd07916cd5041e899e33d17d8a) ([PyObject](../../df/d1b/classPyObject.html) *args, const [Base::Unit](../../d2/d37/classBase_1_1Unit.html) &u=[Base::Unit](../../d2/d37/classBase_1_1Unit.html)())  
| generate a value for a quantity with default user preferred system
[More...](../../d9/d89/classBase_1_1UnitsApi.html#a57451bfd07916cd5041e899e33d17d8a)  
  
static QString | [toString](../../d9/d89/classBase_1_1UnitsApi.html#adb69f0d5dd0db7aa95352bfa7676d098) (const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) &q, const [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html) &f=[QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html)([QuantityFormat::Default](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679a4decd52211cc4ee023d485a6f8c78ea0)))  
| Get a number as string for a quantity of a given format.
[More...](../../d9/d89/classBase_1_1UnitsApi.html#adb69f0d5dd0db7aa95352bfa7676d098)  
  
  
##  Static Public Attributes  
  
---  
static [PyMethodDef](../../da/dab/classPyMethodDef.html) | [Methods](../../d9/d89/classBase_1_1UnitsApi.html#a566cbebcfb6020beae7d6cffbcdd079f) []  
  
##  Static Protected Member Functions  
  
---  
static [PyObject](../../df/d1b/classPyObject.html) * | [sGetSchema](../../d9/d89/classBase_1_1UnitsApi.html#ac342ec32495d2fe69a603bb279b45702) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
static [PyObject](../../df/d1b/classPyObject.html) * | [sListSchemas](../../d9/d89/classBase_1_1UnitsApi.html#ae65d10e24301760e90514ac3844ab48e) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
static [PyObject](../../df/d1b/classPyObject.html) * | [sParseQuantity](../../d9/d89/classBase_1_1UnitsApi.html#a2a6b87ba7a38e42cb3634df0c7838703) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
static [PyObject](../../df/d1b/classPyObject.html) * | [sSchemaTranslate](../../d9/d89/classBase_1_1UnitsApi.html#a1ea1525fca8642d93f32f72d2bb04faa) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
static [PyObject](../../df/d1b/classPyObject.html) * | [sSetSchema](../../d9/d89/classBase_1_1UnitsApi.html#a116abfd59f4f90c21780189781a859eb) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
static [PyObject](../../df/d1b/classPyObject.html) * | [sToNumber](../../d9/d89/classBase_1_1UnitsApi.html#a29ba3277698f56d720819a191df758c6) ([PyObject](../../df/d1b/classPyObject.html) *self, [PyObject](../../df/d1b/classPyObject.html) *args)  
  
##  Static Protected Attributes  
  
---  
static [UnitSystem](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4) | [currentSystem](../../d9/d89/classBase_1_1UnitsApi.html#af00a6451d4ff512f581cf8ce04160541) = [UnitSystem::SI1](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4ad2b1710a33fab31544708bb1df0c19ed)  
static [int](../../d1/da0/classint.html) | [UserPrefDecimals](../../d9/d89/classBase_1_1UnitsApi.html#a1bee00a41d4011c55b64ea15aceab074) = 2  
| number of decimals for floats
[More...](../../d9/d89/classBase_1_1UnitsApi.html#a1bee00a41d4011c55b64ea15aceab074)  
  
static [UnitsSchemaPtr](../../db/d07/namespaceBase.html#afc09c3320e308275ccc558d940d23d82) | [UserPrefSystem](../../d9/d89/classBase_1_1UnitsApi.html#a1feaf145a3bbdd518e71b5c26d0131c2)  
  
## Detailed Description

The [UnitsApi](../../d9/d89/classBase_1_1UnitsApi.html "The UnitsApi.").

## Member Function Documentation

## ◆ createSchema()

| [UnitsSchemaPtr](../../db/d07/namespaceBase.html#afc09c3320e308275ccc558d940d23d82) UnitsApi::createSchema  | ( | [UnitSystem](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4) | _s_| ) |   
---|---|---|---|---|---  
static  
  
return an instance of the given enum value

References
[Base::Centimeters](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4a3040cc6624f5c309963dee141936b299),
[Base::FemMilliMeterNewton](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4aeee26f52b6826fe605fcf031b117d40b),
[Base::Imperial1](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4a7b534ca5d5f718b249930e1f569ee7c7),
[Base::ImperialBuilding](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4af00e6d16925979eb8fe19aaca958deec),
[Base::ImperialCivil](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4acd941e313047250995de5e69433f6c6d),
[Base::ImperialDecimal](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4a75555f1e9864b0d07167859371f58930),
[Base::MmMin](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4a129b5e22b32d022f36ee255b70bf47b5),
[Base::SI1](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4ad2b1710a33fab31544708bb1df0c19ed),
and
[Base::SI2](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4a711347ca2c01758a9359157c47ebc286).

Referenced by
[Gui::QuantitySpinBox::setSchema()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#a7276eef84530599c829d2c95ed5d5f43),
[setSchema()](../../d9/d89/classBase_1_1UnitsApi.html#af7f98f49a6e2b5fcf1089d679a79ab2f),
and
[sSchemaTranslate()](../../d9/d89/classBase_1_1UnitsApi.html#a1ea1525fca8642d93f32f72d2bb04faa).

## ◆ getDecimals()

| [int](../../d1/da0/classint.html) UnitsApi::getDecimals  | ( | | ) |   
---|---|---|---|---  
static  
  
References
[UserPrefDecimals](../../d9/d89/classBase_1_1UnitsApi.html#a1bee00a41d4011c55b64ea15aceab074).

Referenced by
[PartGui::DlgFilletEdges::accept()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#aa1cd2ae4ca0d1438188a366f36cdb552),
[PartGui::CircleFromThreePoints::command()](../../d6/d79/classPartGui_1_1CircleFromThreePoints.html#a2aba41c7949df6cd2eacbd0d42722d96),
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[PartGui::DlgExtrusion::DlgExtrusion()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a7d11626ecae8d02d4421aa4fdd640dc8),
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[TechDraw::DrawViewDimension::getDefaultFormatSpec()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ae6868b300206d4acd693965dbf059bc5),
[Spreadsheet::Cell::getFormattedQuantity()](../../d5/d22/classSpreadsheet_1_1Cell.html#a66a4fb5ffaa93232823dfbe49833ab7b),
[TechDrawGui::QGIDatumLabel::getPrecision()](../../d7/d0c/classTechDrawGui_1_1QGIDatumLabel.html#a56fc799073be6ccf0e45e538d1db75fe),
[Gui::LocationWidget::getUserDirection()](../../d9/d9a/classGui_1_1LocationWidget.html#a928aeb60d1d1a95d4d336c6901fb950b),
[Gui::LocationDialog::getUserDirection()](../../dc/d22/classGui_1_1LocationDialog.html#aa52301a6aec2f1b750929d7444765c33),
[Gui::Dialog::DlgSettingsUnitsImp::loadSettings()](../../d0/df7/classGui_1_1Dialog_1_1DlgSettingsUnitsImp.html#a7127945a0e61f55905a60f534f9aca72),
[PartGui::SectionCut::onCutXHSsliderMoved()](../../de/dd6/classPartGui_1_1SectionCut.html#acc25762befae1a19f82119d97f1b9963),
[PartGui::SectionCut::onCutYHSsliderMoved()](../../de/dd6/classPartGui_1_1SectionCut.html#a5e882170dcedf2295bdb56009180096c),
[PartGui::SectionCut::onCutZHSsliderMoved()](../../de/dd6/classPartGui_1_1SectionCut.html#afcbbb1af3df218b407bfd84ac90a2531),
[FemGui::PlaneWidget::PlaneWidget()](../../dc/dc4/classFemGui_1_1PlaneWidget.html#ad277250040f2f1dbc27dfde2cd156abd),
[Gui::PropertyEditor::PropertyItem::PropertyItem()](../../d6/db3/classGui_1_1PropertyEditor_1_1PropertyItem.html#ab46675ef8847fc7e04a6000ce6f01f48),
[PartDesignGui::TaskBoxPrimitives::setPrimitive()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a0dfd3009478f17d59285f4952f42abc2),
[TechDrawGui::TaskCenterLine::setUiEdit()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a44074b04e6f03fde63d2f4ac7a3f0c33),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[TechDrawGui::TaskCenterLine::setUiPrimary()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a87a1eafc1c37ac2e6c0bbf8bfb73717a),
[TechDrawGui::TaskCosVertex::setUiPrimary()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#af4b9b21bba51de589fd14887b3b82150),
[PartDesignGui::TaskExtrudeParameters::setupDialog()](../../d7/d0a/classPartDesignGui_1_1TaskExtrudeParameters.html#a392344b2eb054d600f5c81befdc0595b),
[PartGui::ShapeFromMesh::ShapeFromMesh()](../../d2/d82/classPartGui_1_1ShapeFromMesh.html#a59f54f87861ed3464c094f2f1b372558),
[FemGui::SphereWidget::SphereWidget()](../../d6/dfe/classFemGui_1_1SphereWidget.html#a71880b94214e186681351d0231a9bdde),
[FemGui::TaskPostDataAlongLine::TaskPostDataAlongLine()](../../db/dfe/classFemGui_1_1TaskPostDataAlongLine.html#a63d24585168c09609383c5025fc02c61),
[FemGui::TaskPostDataAtPoint::TaskPostDataAtPoint()](../../d9/da7/classFemGui_1_1TaskPostDataAtPoint.html#a442bb680fc74fbe236c0415717eb94a4),
[PartGui::Location::toPlacement()](../../db/d6f/classPartGui_1_1Location.html#a3a6283d802f45e675b6ddf9c714c8f47),
[PartGui::Picker::toPlacement()](../../d0/dda/classPartGui_1_1Picker.html#ab049c434087b2c6480f56563dac530e5),
and
[Gui::Dialog::DlgUnitsCalculator::valueChanged()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a32bc446c35a2e71d1cb25fca0bafba08).

## ◆ getDescription()

| const char * UnitsApi::getDescription  | ( | [UnitSystem](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4) | _system_| ) |   
---|---|---|---|---|---  
static  
  
Returns a brief description of a schema.

References
[Base::Centimeters](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4a3040cc6624f5c309963dee141936b299),
[Base::FemMilliMeterNewton](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4aeee26f52b6826fe605fcf031b117d40b),
[Base::Imperial1](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4a7b534ca5d5f718b249930e1f569ee7c7),
[Base::ImperialBuilding](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4af00e6d16925979eb8fe19aaca958deec),
[Base::ImperialCivil](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4acd941e313047250995de5e69433f6c6d),
[Base::ImperialDecimal](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4a75555f1e9864b0d07167859371f58930),
[Base::MmMin](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4a129b5e22b32d022f36ee255b70bf47b5),
[Base::SI1](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4ad2b1710a33fab31544708bb1df0c19ed),
and
[Base::SI2](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4a711347ca2c01758a9359157c47ebc286).

Referenced by
[Gui::Dialog::DlgSettingsUnitsImp::DlgSettingsUnitsImp()](../../d0/df7/classGui_1_1Dialog_1_1DlgSettingsUnitsImp.html#ac886c5432f7c86dad32783dbdd310a46),
[Gui::Dialog::DlgUnitsCalculator::DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
and
[sListSchemas()](../../d9/d89/classBase_1_1UnitsApi.html#ae65d10e24301760e90514ac3844ab48e).

## ◆ getSchema()

| static [UnitSystem](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4) Base::UnitsApi::getSchema  | ( | | ) |   
---|---|---|---|---  
static  
  
return the active schema

Referenced by
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
and
[TechDraw::DrawViewDimension::isMultiValueSchema()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ad8d876c061bedc8250001349758b1d4d).

## ◆ schemaTranslate() [1/2]

| static QString Base::UnitsApi::schemaTranslate  | ( | const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _quant_| ) |   
---|---|---|---|---|---  
static  
  
References
[schemaTranslate()](../../d9/d89/classBase_1_1UnitsApi.html#a4eee4ddbeb846ca0711919848eb53f63).

## ◆ schemaTranslate() [2/2]

| QString UnitsApi::schemaTranslate  | ( | const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _quant_ ,   
---|---|---|---  
|  | double & | _factor_ ,   
|  | QString & | _unitString_  
| ) | |   
static  
  
References
[UserPrefSystem](../../d9/d89/classBase_1_1UnitsApi.html#a1feaf145a3bbdd518e71b5c26d0131c2).

Referenced by
[Base::Quantity::getUserString()](../../d8/d18/classBase_1_1Quantity.html#aea6567cde1ec7087c71c3cacb9d385eb),
[Gui::View3DInventorViewer::printDimension()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a1b066921ad0a7a3e9e3fb53fb5657993),
[schemaTranslate()](../../d9/d89/classBase_1_1UnitsApi.html#a0f45bfff408d222fb36a04c9c96c3b17),
[Gui::schemaTranslatePoint()](../../d9/dad/namespaceGui.html#a79417ca85a106b7d7b516d99443fd81f),
and
[Gui::QuantitySpinBoxPrivate::validate()](../../dd/d08/classGui_1_1QuantitySpinBoxPrivate.html#a3a7b86da24888398add92a65193c9b62).

## ◆ setDecimals()

| void UnitsApi::setDecimals  | ( | [int](../../d1/da0/classint.html) | _prec_| ) |   
---|---|---|---|---|---  
static  
  
References
[UserPrefDecimals](../../d9/d89/classBase_1_1UnitsApi.html#a1bee00a41d4011c55b64ea15aceab074).

Referenced by
[Gui::Dialog::DlgSettingsUnitsImp::saveSettings()](../../d0/df7/classGui_1_1Dialog_1_1DlgSettingsUnitsImp.html#a8d256a71443e4ab9de3df9e072c2f67e).

## ◆ setSchema()

| void UnitsApi::setSchema  | ( | [UnitSystem](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4) | _s_| ) |   
---|---|---|---|---|---  
static  
  
set Schema set the [UnitsSchema](../../d9/dc7/classBase_1_1UnitsSchema.html
"The UnitSchema class The subclasses of this class define the stuff for a
certain units schema.") of the Application this a represented by a class of
type UnitSchema which defines a set of standard units for that schema and
rules for representative strings.

References
[createSchema()](../../d9/d89/classBase_1_1UnitsApi.html#a00b7c68f240fe64f078b839784f852bb),
[currentSystem](../../d9/d89/classBase_1_1UnitsApi.html#af00a6451d4ff512f581cf8ce04160541),
[Base::SI1](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4ad2b1710a33fab31544708bb1df0c19ed),
and
[UserPrefSystem](../../d9/d89/classBase_1_1UnitsApi.html#a1feaf145a3bbdd518e71b5c26d0131c2).

Referenced by
[sSetSchema()](../../d9/d89/classBase_1_1UnitsApi.html#a116abfd59f4f90c21780189781a859eb).

## ◆ sGetSchema()

| [PyObject](../../df/d1b/classPyObject.html) * UnitsApi::sGetSchema  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[currentSystem](../../d9/d89/classBase_1_1UnitsApi.html#af00a6451d4ff512f581cf8ce04160541).

## ◆ sListSchemas()

| [PyObject](../../df/d1b/classPyObject.html) * UnitsApi::sListSchemas  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[getDescription()](../../d9/d89/classBase_1_1UnitsApi.html#acdebcacc6cf6b3689c370e28e1763e4d),
and
[Base::NumUnitSystemTypes](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4ae826a43876ebbcaac80b68a051e6f560).

## ◆ sParseQuantity()

| [PyObject](../../df/d1b/classPyObject.html) * UnitsApi::sParseQuantity  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[Base::Quantity::parse()](../../d8/d18/classBase_1_1Quantity.html#ae1fd875bacec268fcb40771b60c6386a).

## ◆ sSchemaTranslate()

| [PyObject](../../df/d1b/classPyObject.html) * UnitsApi::sSchemaTranslate  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[createSchema()](../../d9/d89/classBase_1_1UnitsApi.html#a00b7c68f240fe64f078b839784f852bb).

## ◆ sSetSchema()

| [PyObject](../../df/d1b/classPyObject.html) * UnitsApi::sSetSchema  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[Base::NumUnitSystemTypes](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4ae826a43876ebbcaac80b68a051e6f560),
and
[setSchema()](../../d9/d89/classBase_1_1UnitsApi.html#af7f98f49a6e2b5fcf1089d679a79ab2f).

## ◆ sToNumber()

| [PyObject](../../df/d1b/classPyObject.html) * UnitsApi::sToNumber  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _self_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _args_  
| ) | |   
staticprotected  
  
References
[Base::QuantityFormat::format](../../d9/d33/structBase_1_1QuantityFormat.html#a72c5baf9b89c433716e8ea6f1072c520),
[Base::QuantityFormat::precision](../../d9/d33/structBase_1_1QuantityFormat.html#a675cc8c56f715e59297ca516f68fca38),
[Base::QuantityFormat::toFormat()](../../d9/d33/structBase_1_1QuantityFormat.html#a018fbf0aa222725335a74d62be39a834),
and
[toNumber()](../../d9/d89/classBase_1_1UnitsApi.html#a4165d414771ff35b19ace249f486098a).

## ◆ toDouble()

| double UnitsApi::toDouble  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _args_ ,   
---|---|---|---  
|  | const [Base::Unit](../../d2/d37/classBase_1_1Unit.html) & | _u_ = `[Base::Unit](../../d2/d37/classBase_1_1Unit.html)()`  
| ) | |   
static  
  
generate a value for a quantity with default user preferred system

References
[Base::Quantity::parse()](../../d8/d18/classBase_1_1Quantity.html#ae1fd875bacec268fcb40771b60c6386a).

## ◆ toNumber() [1/2]

| QString UnitsApi::toNumber  | ( | const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _q_ ,   
---|---|---|---  
|  | const [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html) & | _f_ = `[QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html)([QuantityFormat::Default](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679a4decd52211cc4ee023d485a6f8c78ea0))`  
| ) | |   
static  
  
Get a number as string for a quantity of a given format.

The string is a number in C locale (i.e. the decimal separator is always a
dot) and if needed represented in scientific notation. The string doesn't
include the unit of the quantity.

References
[toNumber()](../../d9/d89/classBase_1_1UnitsApi.html#a4165d414771ff35b19ace249f486098a).

Referenced by
[MeshGui::DlgRegularSolidImp::on_createSolidButton_clicked()](../../d2/d14/classMeshGui_1_1DlgRegularSolidImp.html#abef574440e936e39b317fccf3653ea55),
[PartDesignGui::TaskBoxPrimitives::setPrimitive()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a0dfd3009478f17d59285f4952f42abc2),
[Gui::PropertyEditor::PropertyVectorDistanceItem::setValue()](../../db/dd4/classGui_1_1PropertyEditor_1_1PropertyVectorDistanceItem.html#ad9ef59b35c09aee6c230e37e2032028e),
[Gui::PropertyEditor::PropertyRotationItem::setValue()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a65660d1593a8c2f7dabca98e9464c6cc),
[Gui::PropertyEditor::PropertyPlacementItem::setValue()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a7f8e70acbf194633b6b3422b87a07ab3),
[sToNumber()](../../d9/d89/classBase_1_1UnitsApi.html#a29ba3277698f56d720819a191df758c6),
and
[toNumber()](../../d9/d89/classBase_1_1UnitsApi.html#a4165d414771ff35b19ace249f486098a).

## ◆ toNumber() [2/2]

| QString UnitsApi::toNumber  | ( | double  | _d_ ,   
---|---|---|---  
|  | const [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html) & | _f_ = `[QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html)([QuantityFormat::Default](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679a4decd52211cc4ee023d485a6f8c78ea0))`  
| ) | |   
static  
  
Get a number as string for a double of a given format.

The string is a number in C locale (i.e. the decimal separator is always a
dot) and if needed represented in scientific notation. The string doesn't
include the unit of the quantity.

## ◆ toQuantity()

| [Quantity](../../d8/d18/classBase_1_1Quantity.html) UnitsApi::toQuantity  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _args_ ,   
---|---|---|---  
|  | const [Base::Unit](../../d2/d37/classBase_1_1Unit.html) & | _u_ = `[Base::Unit](../../d2/d37/classBase_1_1Unit.html)()`  
| ) | |   
static  
  
generate a value for a quantity with default user preferred system

References
[Base::Quantity::parse()](../../d8/d18/classBase_1_1Quantity.html#ae1fd875bacec268fcb40771b60c6386a).

## ◆ toString()

| QString UnitsApi::toString  | ( | const [Base::Quantity](../../d8/d18/classBase_1_1Quantity.html) & | _q_ ,   
---|---|---|---  
|  | const [QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html) & | _f_ = `[QuantityFormat](../../d9/d33/structBase_1_1QuantityFormat.html)([QuantityFormat::Default](../../d9/d33/structBase_1_1QuantityFormat.html#a641a7fc3213507b6257321a9be37c679a4decd52211cc4ee023d485a6f8c78ea0))`  
| ) | |   
static  
  
Get a number as string for a quantity of a given format.

The string is a number in C locale (i.e. the decimal separator is always a
dot) and if needed represented in scientific notation. The string also
includes the unit of the quantity.

Referenced by
[Gui::PropertyEditor::PropertyUnitItem::setValue()](../../d7/d5d/classGui_1_1PropertyEditor_1_1PropertyUnitItem.html#ad533525499b4fe616f531f0c4e9caa52).

## Member Data Documentation

## ◆ currentSystem

|
[UnitSystem](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4)
UnitsApi::currentSystem =
[UnitSystem::SI1](../../db/d07/namespaceBase.html#ab4a8545e7fe2d41a448df3941cd229e4ad2b1710a33fab31544708bb1df0c19ed)  
---  
staticprotected  
  
Referenced by
[setSchema()](../../d9/d89/classBase_1_1UnitsApi.html#af7f98f49a6e2b5fcf1089d679a79ab2f),
and
[sGetSchema()](../../d9/d89/classBase_1_1UnitsApi.html#ac342ec32495d2fe69a603bb279b45702).

## ◆ Methods

| [PyMethodDef](../../da/dab/classPyMethodDef.html) UnitsApi::Methods  
---  
static  
  
## ◆ UserPrefDecimals

| [int](../../d1/da0/classint.html) UnitsApi::UserPrefDecimals = 2  
---  
staticprotected  
  
number of decimals for floats

Referenced by
[getDecimals()](../../d9/d89/classBase_1_1UnitsApi.html#a7943af964989d408fde55b6b9c10ee55),
and
[setDecimals()](../../d9/d89/classBase_1_1UnitsApi.html#a5d3e2de74a17b7fa8c57132c9191c755).

## ◆ UserPrefSystem

|
[UnitsSchemaPtr](../../db/d07/namespaceBase.html#afc09c3320e308275ccc558d940d23d82)
UnitsApi::UserPrefSystem  
---  
staticprotected  
  
Referenced by
[schemaTranslate()](../../d9/d89/classBase_1_1UnitsApi.html#a4eee4ddbeb846ca0711919848eb53f63),
and
[setSchema()](../../d9/d89/classBase_1_1UnitsApi.html#af7f98f49a6e2b5fcf1089d679a79ab2f).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/UnitsApi.h
  * FreeCAD/src/Base/UnitsApi.cpp
  * FreeCAD/src/Base/UnitsApiPy.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

