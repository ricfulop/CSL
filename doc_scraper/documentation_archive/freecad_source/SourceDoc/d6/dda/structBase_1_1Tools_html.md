---
url: https://freecad.github.io/SourceDoc/d6/dda/structBase_1_1Tools.html
scraped_at: 2025-09-08T15:17:30.137878
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Tools](../../d6/dda/structBase_1_1Tools.html)

[List of all members](../../d0/d96/structBase_1_1Tools-members.html) | Static Public Member Functions

Base::Tools Struct Reference

`#include <Tools.h>`

##  Static Public Member Functions  
  
---  
static std::string | [addNumber](../../d6/dda/structBase_1_1Tools.html#ae9b1cf7a5204a76c0637d92374a9f8c4) (const std::string &, unsigned [int](../../d1/da0/classint.html), [int](../../d1/da0/classint.html) d=0)  
static std::string | [escapedUnicodeFromUtf8](../../d6/dda/structBase_1_1Tools.html#a2cfe13d9b5c340ec5dc8a7b34fff8645) (const char *s)  
static std::string | [escapedUnicodeToUtf8](../../d6/dda/structBase_1_1Tools.html#a14843043c2ae4cafbbf512b19f9ad527) (const std::string &s)  
static QString | [escapeEncodeFilename](../../d6/dda/structBase_1_1Tools.html#a8bc9d995425fdc0f2e54c1782d10a431) (const QString &s)  
static std::string | [escapeEncodeFilename](../../d6/dda/structBase_1_1Tools.html#ad67b53db193261bda0264f028dc3051d) (const std::string &s)  
static QString | [escapeEncodeString](../../d6/dda/structBase_1_1Tools.html#a67e30e10d282ebd5bc96647c3bd8d619) (const QString &s)  
static std::string | [escapeEncodeString](../../d6/dda/structBase_1_1Tools.html#a904d7f6708c87463306639a8a4af9696) (const std::string &s)  
static QString | [fromStdString](../../d6/dda/structBase_1_1Tools.html#ae15b439f14e64b5ccbe6e1e300ae5921) (const std::string &s)  
| fromStdString Convert a std::string encoded as UTF-8 into a QString.
[More...](../../d6/dda/structBase_1_1Tools.html#ae15b439f14e64b5ccbe6e1e300ae5921)  
  
static std::string | [getIdentifier](../../d6/dda/structBase_1_1Tools.html#a49653de3f8677d06572f26f1f002641d) (const std::string &)  
static std::string | [getUniqueName](../../d6/dda/structBase_1_1Tools.html#a2e5fcd4db818dbcce127c0695ffe937b) (const std::string &, const std::vector< std::string > &, [int](../../d1/da0/classint.html) d=0)  
static std::string | [narrow](../../d6/dda/structBase_1_1Tools.html#a8e3e3e12393d860b49d0d0e74bf809ab) (const std::wstring &[str](../../d9/d36/classstr.html))  
static std::string | [toStdString](../../d6/dda/structBase_1_1Tools.html#a7532aeb4ad2f004bab3620e475b9e757) (const QString &s)  
| toStdString Convert a QString into a UTF-8 encoded std::string.
[More...](../../d6/dda/structBase_1_1Tools.html#a7532aeb4ad2f004bab3620e475b9e757)  
  
static std::wstring | [widen](../../d6/dda/structBase_1_1Tools.html#a8d7e9fd7ba7933e95b8e4758af30d6af) (const std::string &[str](../../d9/d36/classstr.html))  
  
## Member Function Documentation

## ◆ addNumber()

| std::string Base::Tools::addNumber  | ( | const std::string & | _name_ ,   
---|---|---|---  
|  | unsigned [int](../../d1/da0/classint.html) | _num_ ,   
|  | [int](../../d1/da0/classint.html) | _d_ = `0`  
| ) | |   
static  
  
## ◆ escapedUnicodeFromUtf8()

| std::string Base::Tools::escapedUnicodeFromUtf8  | ( | const char *  | _s_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[PartGui::Mirroring::accept()](../../db/d41/classPartGui_1_1Mirroring.html#a65b4bef12c8f1db83eee1cd6799f2794),
[SpreadsheetGui::PropertiesDialog::apply()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a5aa7098c11c9d893cb9b30cd6541939d),
[Gui::Application::exportTo()](../../d9/da8/classGui_1_1Application.html#a276a5171d44ac9162f39a69fc92f137f),
[Gui::ExpressionBinding::getEscapedExpressionString()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a0ba45b73907acd2f4857de4fc613cbe1),
[App::SubObjectT::getSubObjectPython()](../../dd/d78/classApp_1_1SubObjectT.html#afc63dfe396a3a3cbd15a0b421df53662),
[Gui::Application::importFrom()](../../d9/da8/classGui_1_1Application.html#a8d8a9ad9495f79b4813c2b97d2e33e86),
[Gui::Dialog::DlgPropertyLink::linksToPython()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#a74421b48c0cdcebd55f00a858489a861),
[StartGui::Workbench::loadStartPage()](../../dc/d4c/classStartGui_1_1Workbench.html#a44d732f24cca88363d161155407973a6),
[SketcherGui::TaskSketcherConstraints::on_listWidgetConstraints_itemChanged()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#aa782aa7f44ac5962f91d0379dd4d6ce7),
[Gui::Application::open()](../../d9/da8/classGui_1_1Application.html#a7035ec948a4d7a823668fb29d706faa8),
[App::Application::processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939),
[Gui::Document::saveAs()](../../de/d4e/classGui_1_1Document.html#ac2c94d85366e44a09c35563a3848c852),
[MeshCore::MeshOutput::SaveOBJ()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3d771358cea3ae77d666c54aba2692b5),
[Gui::PropertyEditor::PropertyEnumItem::setValue()](../../d1/dd0/classGui_1_1PropertyEditor_1_1PropertyEnumItem.html#a7c1251bfd5e2a2133e9fd826a7a33983),
[SketcherGui::ConstraintView::swapNamedOfSelectedItems()](../../df/d7b/classSketcherGui_1_1ConstraintView.html#a2ef795bfde4fc5d342d3bba939346c86),
and
[App::ObjectIdentifier::toEscapedString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9c8aaa7cfadced7f02366ca502c53029).

## ◆ escapedUnicodeToUtf8()

| std::string Base::Tools::escapedUnicodeToUtf8  | ( | const std::string & | _s_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[MeshCore::MeshInput::LoadMTL()](../../d9/d08/classMeshCore_1_1MeshInput.html#ad0111057ebea537a54f286e117787454),
and
[MeshCore::MeshInput::LoadOBJ()](../../d9/d08/classMeshCore_1_1MeshInput.html#a7799edf1fa4b6fb4e05d8f374e3d8c4d).

## ◆ escapeEncodeFilename() [1/2]

| QString Base::Tools::escapeEncodeFilename  | ( | const QString & | _s_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[TechDrawGui::TaskActiveView::createActiveView()](../../dd/dea/classTechDrawGui_1_1TaskActiveView.html#a06f867ac197d21160c2b15c19b71718d),
[Gui::Application::exportTo()](../../d9/da8/classGui_1_1Application.html#a276a5171d44ac9162f39a69fc92f137f),
[Gui::Application::importFrom()](../../d9/da8/classGui_1_1Application.html#a8d8a9ad9495f79b4813c2b97d2e33e86),
[Gui::Application::open()](../../d9/da8/classGui_1_1Application.html#a7035ec948a4d7a823668fb29d706faa8),
[App::Application::processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa),
[App::Application::processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939),
[Gui::Document::saveAs()](../../de/d4e/classGui_1_1Document.html#ac2c94d85366e44a09c35563a3848c852),
[Gui::Document::saveCopy()](../../de/d4e/classGui_1_1Document.html#a27866ed0852198802f9889404d46dffb),
[TechDrawGui::MDIViewPage::saveDXF()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a2bfe93567b8e55b5bcda419d70b57a8e),
and
[WebGui::BrowserView::urlFilter()](../../db/d47/classWebGui_1_1BrowserView.html#a94993bbc570924530a3c6a4af2844859).

## ◆ escapeEncodeFilename() [2/2]

| std::string Base::Tools::escapeEncodeFilename  | ( | const std::string & | _s_| ) |   
---|---|---|---|---|---  
static  
  
## ◆ escapeEncodeString() [1/2]

| QString Base::Tools::escapeEncodeString  | ( | const QString & | _s_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[TechDrawGui::TaskWeldingSymbol::createWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#a687a7f75b421ef414ad8e8ae46dc7889),
[TechDrawGui::TaskWeldingSymbol::updateTiles()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#aac480071122ff57d72a8cba865b1c94c),
and
[TechDrawGui::TaskWeldingSymbol::updateWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#ae2c10ae5d73a0018daaa7b088b67fdf9).

## ◆ escapeEncodeString() [2/2]

| std::string Base::Tools::escapeEncodeString  | ( | const std::string & | _s_| ) |   
---|---|---|---|---|---  
static  
  
## ◆ fromStdString()

| static QString Base::Tools::fromStdString  | ( | const std::string & | _s_| ) |   
---|---|---|---|---|---  
static  
  
fromStdString Convert a std::string encoded as UTF-8 into a QString.

Parameters

     s| std::string, expected to be UTF-8 encoded.   
---|---  
  
Returns

    String represented as a QString. 

Referenced by
[StdCmdDelete::activated()](../../da/dc8/classStdCmdDelete.html#a120710ae4a8c0f26451596002a176ee7),
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[ConstraintItem::data()](../../d3/d0f/classConstraintItem.html#a58e0ecc1824934b77e25bc0b319b6c51),
[Gui::Dialog::DlgExpressionInput::DlgExpressionInput()](../../d5/d26/classGui_1_1Dialog_1_1DlgExpressionInput.html#aa41178b425873712e0c599430c5e79b8),
[TechDrawGui::QGIWeldSymbol::drawTailText()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#ade5f6fb54a953f66e157e6d363160707),
[Gui::QuantitySpinBox::event()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#a1c2ffac01c0b7934971b71bb2af3275f),
[SketcherGui::EditDatumDialog::exec()](../../d6/d55/classSketcherGui_1_1EditDatumDialog.html#ae2acb3ba391ab2b817662e85aa8134fd),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDrawGui::TaskSectionView::failNoObject()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#abc37bd6db173d7e9619a35d5011e7d3b),
[TechDraw::DrawViewDimension::getDefaultFormatSpec()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ae6868b300206d4acd693965dbf059bc5),
[MRichTextEdit::getDefFont()](../../d0/d27/classMRichTextEdit.html#a5ba9fdff928fa6b6d3e285947b78d863),
[Spreadsheet::Cell::getFormattedQuantity()](../../d5/d22/classSpreadsheet_1_1Cell.html#a66a4fb5ffaa93232823dfbe49833ab7b),
[TechDrawGui::TaskLineDecor::initUi()](../../d5/d87/classTechDrawGui_1_1TaskLineDecor.html#a58ab677c87cd4089a322fc2bc523b570),
[TechDrawGui::DlgPrefsTechDrawDimensionsImp::loadSettings()](../../d7/d7d/classTechDrawGui_1_1DlgPrefsTechDrawDimensionsImp.html#adfec19e74cf7fbe819110206438ec740),
[SpreadsheetGui::PropertiesDialog::PropertiesDialog()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a1a48a3dff37267c81257bf75efc33fdf),
[Gui::ExpLineEdit::resizeEvent()](../../d0/d05/classGui_1_1ExpLineEdit.html#ab4370763f20b014e2402c6231aa37a8d),
[TechDrawGui::QGITile::setFont()](../../d6/d9b/classTechDrawGui_1_1QGITile.html#a9af25ac31e02bef9352925524f6a0f10),
[TechDrawGui::TaskHatch::setUiEdit()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#aae6e162e74354c8d160865c07d91d1c5),
[TechDrawGui::TaskSectionView::setUiEdit()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a43dc3542cf896d0778a028ae2be230ce),
[TechDrawGui::TaskCenterLine::setUiEdit()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a44074b04e6f03fde63d2f4ac7a3f0c33),
[TechDrawGui::TaskCustomizeFormat::setUiEdit()](../../db/dde/classTechDrawGui_1_1TaskCustomizeFormat.html#a20843f7f5568b6ecfe6615b367235aea),
[TechDrawGui::TaskLeaderLine::setUiEdit()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0eed6886711ee111f1ee0a8e314d6e21),
[TechDrawGui::TaskRichAnno::setUiEdit()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a3659e9cb13bc53ae36a3d7d16479d017),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[TechDrawGui::TaskHatch::setUiPrimary()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#afaa5596988bde48f568b08765a669e4c),
[TechDrawGui::TaskSectionView::setUiPrimary()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a07485a3822d8c672d6e4580fe4bf858c),
[TechDrawGui::TaskCenterLine::setUiPrimary()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a87a1eafc1c37ac2e6c0bbf8bfb73717a),
[TechDrawGui::TaskCosVertex::setUiPrimary()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#af4b9b21bba51de589fd14887b3b82150),
[TechDrawGui::TaskLeaderLine::setUiPrimary()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#ae4079f062fea88e52c9e7242cc8ecead),
[TechDrawGui::TaskRichAnno::setUiPrimary()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ae2285e8fe902c048c0c4d27ee93b42ec),
[SpreadsheetGui::SheetModel::SheetModel()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aca374b8f387985ec3756f86f3cac2c45),
[Gui::ExpressionSpinBox::showValidExpression()](../../d7/d1b/classGui_1_1ExpressionSpinBox.html#a98d67e4a5b08e6c703981f7317bddb35),
[Gui::ExpressionCompleter::slotUpdate()](../../da/d8d/classGui_1_1ExpressionCompleter.html#a7bfb60694144331e93a4816efd450e1a),
and
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1).

## ◆ getIdentifier()

| std::string Base::Tools::getIdentifier  | ( | const std::string & | _name_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[Gui::Dialog::DlgAddProperty::accept()](../../d3/d89/classGui_1_1Dialog_1_1DlgAddProperty.html#abec1eb0c6613b0f93b760bac73a92f9d),
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[App::Application::getUniqueDocumentName()](../../da/dbf/classApp_1_1Application.html#a59cb1d32f2baee9436cbee0ab4253030),
and
[App::Document::getUniqueObjectName()](../../d8/d3e/classApp_1_1Document.html#a8bc7c3b871147cf18529b0a1e9f44ac9).

## ◆ getUniqueName()

| std::string Base::Tools::getUniqueName  | ( | const std::string & | _name_ ,   
---|---|---|---  
|  | const std::vector< std::string > & | _names_ ,   
|  | [int](../../d1/da0/classint.html) | _d_ = `0`  
| ) | |   
static  
  
References
[Base::string_comp::increment()](../../d7/d4a/structBase_1_1string__comp.html#a2e401b5c4f982319236c3663c7ec42a8).

Referenced by
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[App::Document::getStandardObjectName()](../../d8/d3e/classApp_1_1Document.html#a3d17fc869ebcefabfa83b1adb5665ec5),
[App::Application::getUniqueDocumentName()](../../da/dbf/classApp_1_1Application.html#a59cb1d32f2baee9436cbee0ab4253030),
[Base::Writer::getUniqueFileName()](../../dd/d4d/classBase_1_1Writer.html#a5f42876fd6d991fd34f2de3ca657f9cc),
[App::Document::getUniqueObjectName()](../../d8/d3e/classApp_1_1Document.html#a8bc7c3b871147cf18529b0a1e9f44ac9),
[App::Application::newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b),
and
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

## ◆ narrow()

| std::string Base::Tools::narrow  | ( | const std::wstring & | _str_| ) |   
---|---|---|---|---|---  
static  
  
## ◆ toStdString()

| static std::string Base::Tools::toStdString  | ( | const QString & | _s_| ) |   
---|---|---|---|---|---  
static  
  
toStdString Convert a QString into a UTF-8 encoded std::string.

Parameters

     s| String to convert.   
---|---  
  
Returns

    A std::string encoded as UTF-8. 

Referenced by
[SpreadsheetGui::SheetView::aliasChanged()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a6c30b3c8c5b9d51ea194e419e5052561),
[TechDrawGui::TaskSectionView::apply()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a226f1c136253d3921545858eb107b4d5),
[SpreadsheetGui::SheetView::confirmAliasChanged()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a417a33ce8aa3a831fed85c08876f84ba),
[TechDrawGui::TaskActiveView::createActiveView()](../../dd/dea/classTechDrawGui_1_1TaskActiveView.html#a06f867ac197d21160c2b15c19b71718d),
[TechDrawGui::TaskHatch::createHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ac9d417f22f5d5ed524f63d10cd4e63ef),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[FemGui::TaskFemConstraintFluidBoundary::getBoundaryType()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a362bb762c02e70e0d34bd7f2d3538714),
[TechDraw::DrawViewDimension::getDefaultFormatSpec()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ae6868b300206d4acd693965dbf059bc5),
[Spreadsheet::Cell::getFormattedQuantity()](../../d5/d22/classSpreadsheet_1_1Cell.html#a66a4fb5ffaa93232823dfbe49833ab7b),
[FemGui::TaskFemConstraintFluidBoundary::getSubtype()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a2d112cbb1d92d79e9670bee01bf1b6b1),
[FemGui::TaskFemConstraintFluidBoundary::getThermalBoundaryType()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a997b8f9586c5529d8053e750f0d223bd),
[FemGui::TaskFemConstraintFluidBoundary::getTurbulenceSpecification()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a88489027cefed88fd134b1868ce3d20b),
[SketcherGui::TaskSketcherConstraints::on_listWidgetConstraints_itemChanged()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#aa782aa7f44ac5962f91d0379dd4d6ce7),
[TechDrawGui::TaskHatch::onFileChanged()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#af7d8b08c3e9ec885fe0e6ba8c176ca81),
[Spreadsheet::Sheet::recomputeCell()](../../d0/da8/classSpreadsheet_1_1Sheet.html#ae13fa16166fcbbceb100aea98147b700),
[Gui::ExpressionCompleter::slotUpdate()](../../da/d8d/classGui_1_1ExpressionCompleter.html#a7bfb60694144331e93a4816efd450e1a),
[TechDrawGui::TaskDetail::updateDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a9531ab9a77b992bbde7893f620cddd9f),
[TechDrawGui::TaskHatch::updateHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#a885b8fcb16ca312a825e37d5f4ee11b4),
and
[TechDrawGui::TaskSectionView::updateSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#ade2a27d8889164e2b81d166289744e35).

## ◆ widen()

| std::wstring Base::Tools::widen  | ( | const std::string & | _str_| ) |   
---|---|---|---|---|---  
static  
  
* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/Base/Tools.h
  * FreeCAD/src/Base/Tools.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

