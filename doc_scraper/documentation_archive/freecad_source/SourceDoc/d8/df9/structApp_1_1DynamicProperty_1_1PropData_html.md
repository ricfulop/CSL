---
url: https://freecad.github.io/SourceDoc/d8/df9/structApp_1_1DynamicProperty_1_1PropData.html
scraped_at: 2025-09-08T14:54:33.457092
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html)
  * [PropData](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html)

[List of all members](../../d2/dc0/structApp_1_1DynamicProperty_1_1PropData-members.html) | Public Member Functions | Public Attributes

App::DynamicProperty::PropData Struct Reference

`#include <DynamicProperty.h>`

##  Public Member Functions  
  
---  
const char * | [getName](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#a6639933b1079948460e96a21896d8674) () const  
|
[PropData](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#a0c29ba9ccd82341262f8d44d39439c8f)
([Property](../../d0/da9/classApp_1_1Property.html) *prop=nullptr, std::string
&&n=std::string(), const char *pn=nullptr, const char *g=nullptr, const char
*d=nullptr, short a=0, [bool](../../d9/db9/classbool.html) ro=false,
[bool](../../d9/db9/classbool.html) h=false)  
  
##  Public Attributes  
  
---  
short | [attr](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#a33d50514fb8bb5efacd44496143a0c52)  
std::string | [doc](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#abfd4d64b2a0921a69a1f8824f6f99606)  
std::string | [group](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#a05833d926cb28b06b88da12ae3b699f7)  
[bool](../../d9/db9/classbool.html) | [hidden](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#a3f910f593fd2be514a4f4d0fa749d99f)  
std::string | [name](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#afd086a0cf36efdad217c173c2c45e915)  
const char * | [pName](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#afa552eb5e898e519d15d5c52ef117619)  
[Property](../../d0/da9/classApp_1_1Property.html) * | [property](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#a176e2cbcdbcaca063384507c694fe1c9)  
[bool](../../d9/db9/classbool.html) | [readonly](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html#a3cddd616af54dc5cee263020d91bce88)  
  
## Constructor & Destructor Documentation

## ◆ PropData()

App::DynamicProperty::PropData::PropData  | ( | [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_ = `nullptr`,   
---|---|---|---  
|  | std::string && | _n_ = `std::string()`,   
|  | const char *  | _pn_ = `nullptr`,   
|  | const char *  | _g_ = `nullptr`,   
|  | const char *  | _d_ = `nullptr`,   
|  | short  | _a_ = `0`,   
|  | [bool](../../d9/db9/classbool.html) | _ro_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _h_ = `false`  
| ) | |   
  
## Member Function Documentation

## ◆ getName()

const char * App::DynamicProperty::PropData::getName  | ( | | ) |  const  
---|---|---|---|---  
  
## Member Data Documentation

## ◆ attr

short App::DynamicProperty::PropData::attr  
---  
  
## ◆ doc

| std::string App::DynamicProperty::PropData::doc  
---  
mutable  
  
Referenced by
[draftguitools.gui_lineslope.LineSlope::accept()](../../d4/d0f/classdraftguitools_1_1gui__lineslope_1_1LineSlope.html#ad24df8c32ec0b77a393eb130b6f7ab57),
[draftguitools.gui_dimensions.Dimension::action()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a96494d2774d1c1c9b0973c27fa7e37d2),
[draftguitools.gui_base.GuiCommandSimplest::Activated()](../../d3/dbd/classdraftguitools_1_1gui__base_1_1GuiCommandSimplest.html#af9fb0fc3e536a8a068732630ea5634db),
[draftguitools.gui_beziers.BezCurve::Activated()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a784e5b3d22300d802916024986f3f8ba),
[draftguitools.gui_beziers.CubicBezCurve::Activated()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#a982a5341986fbd004390ea8902c0ba3d),
[draftguitools.gui_dimension_ops.FlipDimension::Activated()](../../de/d3e/classdraftguitools_1_1gui__dimension__ops_1_1FlipDimension.html#a43a2515fe4a13602f4cd9a705c04c8d2),
[draftguitools.gui_groups.AddToConstruction::Activated()](../../d3/d06/classdraftguitools_1_1gui__groups_1_1AddToConstruction.html#a36c267c4685ebb061b39cea882049759),
[draftguitools.gui_heal.Heal::Activated()](../../d5/d39/classdraftguitools_1_1gui__heal_1_1Heal.html#a229ca6fa356961bf5de5cb0bb2ff7fc7),
[draftguitools.gui_layers.Layer::Activated()](../../d1/da7/classdraftguitools_1_1gui__layers_1_1Layer.html#ab7afc624bbc1b314ec9c6306770d1ee5),
[draftguitools.gui_splines.BSpline::Activated()](../../d1/d3f/classdraftguitools_1_1gui__splines_1_1BSpline.html#a110d145a7b4c19d7d9006c99e78f5750),
[draftguitools.gui_wire2spline.WireToBSpline::Activated()](../../d4/dd5/classdraftguitools_1_1gui__wire2spline_1_1WireToBSpline.html#afc3604f707c18d3e48b42d06a1ad4b5c),
[draftguitools.gui_lines.Line::Activated()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#a8033f2b529eaa31c53d41d504eed52bc),
[WorkingPlane.Plane::alignToPointAndAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab85860830e3debec48d3cdb58d30621a),
[WorkingPlane.Plane::alignToPointAndAxis_SVG()](../../d3/d93/classWorkingPlane_1_1Plane.html#a53cb561d317b813ea9a22ef8e319104d),
[Mod.Show.SceneDetails.ClipPlane.ClipPlane::apply_data()](../../d2/dc5/classMod_1_1Show_1_1SceneDetails_1_1ClipPlane_1_1ClipPlane.html#ae7b38b4f79ac354357a5221f13c943d8),
[Mod.Show.SceneDetails.ObjectClipPlane.ObjectClipPlane::apply_data()](../../d0/dd9/classMod_1_1Show_1_1SceneDetails_1_1ObjectClipPlane_1_1ObjectClipPlane.html#aab91d8481e5410d0d58335fcfc2d8a84),
[Mod.Show.SceneDetails.Pickability.Pickability::apply_data()](../../d4/d87/classMod_1_1Show_1_1SceneDetails_1_1Pickability_1_1Pickability.html#a134878bb57b81a3efcb2e2bcbdae0bb6),
[Mod.Show.SceneDetails.VProperty.VProperty::apply_data()](../../d6/dc4/classMod_1_1Show_1_1SceneDetails_1_1VProperty_1_1VProperty.html#a31de062c701e6c5414bc169a1a9d5e77),
[importSVG.svgHandler::characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[draftguitools.gui_drawing.Drawing::createDefaultPage()](../../db/d99/classdraftguitools_1_1gui__drawing_1_1Drawing.html#afb9013170b36d4cd31714baab2349b49),
[draftguitools.gui_fillets.Fillet::draw_arc()](../../da/d40/classdraftguitools_1_1gui__fillets_1_1Fillet.html#a21e1343069408abfc862c5e16eec9e81),
[importSVG.svgHandler::endElement()](../../dc/d45/classimportSVG_1_1svgHandler.html#a1bd77a0a99233ef4a9075eefc2da04f3),
[draftguitools.gui_arcs.Arc_3Points::finish()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#a14de6ccfeaf7a3143b1db145756da598),
[draftguitools.gui_fillets.Fillet::finish()](../../da/d40/classdraftguitools_1_1gui__fillets_1_1Fillet.html#a6b8e06e5a26d68509b050c212ec0685f),
[draftguitools.gui_arcs.Arc::finish()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a2262d966a879bfa9b71d9c699e6929b2),
[draftguitools.gui_beziers.BezCurve::finish()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a6b4598d09cb7c1f0b06fe1b96cc9096f),
[draftguitools.gui_beziers.CubicBezCurve::finish()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#abadcbdae43b1e54d516d249c71fc0991),
[draftguitools.gui_polygons.Polygon::finish()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a06317245940b6d99d62b0823d657dcb2),
[draftguitools.gui_rotate.Rotate::finish()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#ad60faae5b86f1d2c74f045c2291ae6dd),
[draftguitools.gui_splines.BSpline::finish()](../../d1/d3f/classdraftguitools_1_1gui__splines_1_1BSpline.html#ab00ba1111a2b9d2afcee43a0396a4cd5),
[Mod.Show.SceneDetail.SceneDetail::full_key()](../../d6/d7f/classMod_1_1Show_1_1SceneDetail_1_1SceneDetail.html#a2a467627c9aea4e11698a0ee57580b29),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor::get_annotations()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a791cb6cdb0247be1eb02ec5537e14ed7),
[importIFClegacy.IfcEntity::getProperties()](../../d0/df2/classimportIFClegacy_1_1IfcEntity.html#aa57d8841d195c0c50014568479330ffd),
[importIFClegacy.IfcEntity::getProperty()](../../d0/df2/classimportIFClegacy_1_1IfcEntity.html#ac6c54d841f3a19e8ef5842f30c3d15ed),
[draftguitools.gui_groups.AddToGroup::proceed()](../../d8/d83/classdraftguitools_1_1gui__groups_1_1AddToGroup.html#a593a469720294390952479a7fed88727),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor::read_meta()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a6247b3c54e920c9d87e4154dd8889050),
[draftguitools.gui_trimex.Trimex::redraw()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a6c61910ba86ef48101475e9ecdd6f958),
[draftguitools.gui_lines.Line::removeTemporaryObject()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#ad5b1d5b92a1cb5284bd8440cf896e5db),
[WorkingPlane.Plane::reset()](../../d3/d93/classWorkingPlane_1_1Plane.html#addaef5dd4773d419c290bd6e7dbfbfa4),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor::save_meta()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a4843c14993658e8aad20503c5787fc6c),
[Mod.Show.SceneDetails.ObjectClipPlane.ObjectClipPlane::scene_value()](../../d0/dd9/classMod_1_1Show_1_1SceneDetails_1_1ObjectClipPlane_1_1ObjectClipPlane.html#ac296ee70b92bc436b2ea856316fc8f0d),
[Mod.Show.SceneDetails.Pickability.Pickability::scene_value()](../../d4/d87/classMod_1_1Show_1_1SceneDetails_1_1Pickability_1_1Pickability.html#a301ce25695581840794ede85d96c164b),
[Mod.Show.SceneDetails.VProperty.VProperty::scene_value()](../../d6/dc4/classMod_1_1Show_1_1SceneDetails_1_1VProperty_1_1VProperty.html#adc2dc95381f3e0ca347a4f1a39973d73),
[Mod.Show.SceneDetail.SceneDetail::set_doc()](../../d6/d7f/classMod_1_1Show_1_1SceneDetail_1_1SceneDetail.html#a556a7a4e22a7adf4cfe7d04e03e6a90b),
[drafttests.test_creation.DraftCreation::tearDown()](../../d7/d8b/classdrafttests_1_1test__creation_1_1DraftCreation.html#abb189a2fc8ca60923596614f8789aa21),
[PathTests.TestPathDrillable.TestPathDrillable::tearDown()](../../d4/d90/classPathTests_1_1TestPathDrillable_1_1TestPathDrillable.html#ad84063241af6cce8543f189aad192b8d),
[PathTests.TestPathHelix.TestPathHelix::tearDown()](../../d1/db0/classPathTests_1_1TestPathHelix_1_1TestPathHelix.html#a7b296da85a2077af0fbce56870515ea7),
[PathTests.TestPathPropertyBag.TestPathPropertyBag::tearDown()](../../d6/d6c/classPathTests_1_1TestPathPropertyBag_1_1TestPathPropertyBag.html#a0b7c1ae77f5a03c63e997d8237d993b6),
[PathTests.TestPathSetupSheet.TestPathSetupSheet::tearDown()](../../d7/db0/classPathTests_1_1TestPathSetupSheet_1_1TestPathSetupSheet.html#a449f57c085a4b9c5f36e6701998f90b9),
[PathTests.TestPathToolController.TestPathToolController::tearDown()](../../d8/d62/classPathTests_1_1TestPathToolController_1_1TestPathToolController.html#a6b4df2fabd7be750be2464acfb5e0520),
[TestSpreadsheet.SpreadsheetCases::tearDown()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a112bd4b6879b998315751a9565805c7f),
[PathTests.TestPathSetupSheet.TestPathSetupSheet::test00()](../../d7/db0/classPathTests_1_1TestPathSetupSheet_1_1TestPathSetupSheet.html#a2f302b34482e3ad9fe06369a6c7c466f),
[PathTests.TestPathUtil.TestPathUtil::test00()](../../d3/dc0/classPathTests_1_1TestPathUtil_1_1TestPathUtil.html#ab493c6fc6660bd5258c09cb75a6cde42),
[PathTests.TestPathPost.TestOutputNameSubstitution::test000()](../../d0/d6e/classPathTests_1_1TestPathPost_1_1TestOutputNameSubstitution.html#a7d439ecb303873678877ded54a99e66e),
[PathTests.TestPathSetupSheet.TestPathSetupSheet::test01()](../../d7/db0/classPathTests_1_1TestPathSetupSheet_1_1TestPathSetupSheet.html#a9596f8615b94d885e1210b2a93e6679e),
[PathTests.TestPathUtil.TestPathUtil::test01()](../../d3/dc0/classPathTests_1_1TestPathUtil_1_1TestPathUtil.html#a76e224955191acdd959eb7e40fca211e),
[PathTests.TestPathAdaptive.TestPathAdaptive::test02()](../../dd/d9c/classPathTests_1_1TestPathAdaptive_1_1TestPathAdaptive.html#a13d29e73da13447b9d1958fe97cc62d3),
[PathTests.TestPathUtil.TestPathUtil::test02()](../../d3/dc0/classPathTests_1_1TestPathUtil_1_1TestPathUtil.html#a82d4e9109fc34c24d87f7187a6f4eb39),
[PathTests.TestPathAdaptive.TestPathAdaptive::test03()](../../dd/d9c/classPathTests_1_1TestPathAdaptive_1_1TestPathAdaptive.html#a8b6620ea5c5a732f115c05115194a82b),
[PathTests.TestPathHelix.TestPathHelix::test03()](../../d1/db0/classPathTests_1_1TestPathHelix_1_1TestPathHelix.html#a4181733969e9043fbeccd5d603294940),
[PathTests.TestPathUtil.TestPathUtil::test03()](../../d3/dc0/classPathTests_1_1TestPathUtil_1_1TestPathUtil.html#abd8a83ff6a469eb00343ab79d7cbb54b),
[PathTests.TestPathAdaptive.TestPathAdaptive::test04()](../../dd/d9c/classPathTests_1_1TestPathAdaptive_1_1TestPathAdaptive.html#abc8ddcfcdee309e38abf87ce57be9477),
[PathTests.TestPathHelix.TestPathHelix::test04()](../../d1/db0/classPathTests_1_1TestPathHelix_1_1TestPathHelix.html#a066e090f9091bd970c6c42068313d441),
[PathTests.TestPathUtil.TestPathUtil::test04()](../../d3/dc0/classPathTests_1_1TestPathUtil_1_1TestPathUtil.html#a5c6837e8b4ba67e4c3cc4531f9a413e0),
[PathTests.TestPathAdaptive.TestPathAdaptive::test05()](../../dd/d9c/classPathTests_1_1TestPathAdaptive_1_1TestPathAdaptive.html#ae62c7ccd6d87147a233db7f25964baba),
[PathTests.TestPathAdaptive.TestPathAdaptive::test06()](../../dd/d9c/classPathTests_1_1TestPathAdaptive_1_1TestPathAdaptive.html#add9f8304a18c2e9a395ac55ac27e421c),
[PathTests.TestPathAdaptive.TestPathAdaptive::test07()](../../dd/d9c/classPathTests_1_1TestPathAdaptive_1_1TestPathAdaptive.html#ad92e6cdc896d20ed67eea764e9e1d04d),
[PathTests.TestPathSetupSheet.TestPathSetupSheet::test13()](../../d7/db0/classPathTests_1_1TestPathSetupSheet_1_1TestPathSetupSheet.html#abd599db0554b9a4bd5f7d61182485fcd),
[drafttests.test_creation.DraftCreation::test_dimension_linear_obj()](../../d7/d8b/classdrafttests_1_1test__creation_1_1DraftCreation.html#a5eb127fd90bb43c8d62133274e577575),
[drafttests.test_creation.DraftCreation::test_dimension_radial_obj()](../../d7/d8b/classdrafttests_1_1test__creation_1_1DraftCreation.html#abd4f1ff00aa06667e0179070c1453f88),
[drafttests.test_creation.DraftCreation::test_facebinder()](../../d7/d8b/classdrafttests_1_1test__creation_1_1DraftCreation.html#afbd38623a75b17225590c4cda60926cd),
[drafttests.test_creation.DraftCreation::test_fillet()](../../d7/d8b/classdrafttests_1_1test__creation_1_1DraftCreation.html#aec8669c4bb504cd50f65ec60fd1e1694),
[drafttests.test_creation.DraftCreation::test_label()](../../d7/d8b/classdrafttests_1_1test__creation_1_1DraftCreation.html#aa15922c6ebcac2d8eb988c261684078e),
[TestSpreadsheet.SpreadsheetCases::testAggregates()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a7046151887b376fdc597d9cf387f3d06),
[TestSpreadsheet.SpreadsheetCases::testAlias()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a8c7553dadb1f7d460f2cba7cf6fa2a5f),
[TestSpreadsheet.SpreadsheetCases::testAmbiguousAlias()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#afe690bc1b6dceb1e3a483408121d0c0d),
[TestSpreadsheet.SpreadsheetCases::testBindAcrossSheets()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a3554b70514fdd1be16d35b42ea340d9b),
[TestSpreadsheet.SpreadsheetCases::testBindHiddenRefAcrossSheets()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a03f970e39ddc17b46c8ec0cdbcdfead9),
[TestSpreadsheet.SpreadsheetCases::testClearAlias()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a374d8ece9368d36754676977c0d3c6c9),
[TestSpreadsheetGui.SpreadsheetGuiCases::testCopySingleCell()](../../dc/d90/classTestSpreadsheetGui_1_1SpreadsheetGuiCases.html#a6ee2fff7adcb90d30a283c103f388912),
[TestSpreadsheet.SpreadsheetCases::testCrossDocumentLinks()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a65a72392614d7a9c1ee5a29902c75c4f),
[TestSpreadsheet.SpreadsheetCases::testExpressionWithAlias()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a602674cf5cdbc12d2b627de386f467e9),
[TestSpreadsheet.SpreadsheetCases::testFixPR6843()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a4abb623c7814ec63e3d6b8c0c1f94bf8),
[TestSpreadsheet.SpreadsheetCases::testFunctions()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a7098f0a69a0ec55da1ef42cf2055a2ba),
[TestSpreadsheet.SpreadsheetCases::testInsertColumnsAlias()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a757b19fa6645f6c6ef182c9dd26fc75c),
[TestSpreadsheet.SpreadsheetCases::testInsertRows()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a67279f1a07baf36f1d0e1574e1e62470),
[TestSpreadsheet.SpreadsheetCases::testInsertRowsAlias()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a0507e5ac4e7b4106021e64ebf3fa3d0b),
[TestSpreadsheet.SpreadsheetCases::testInvoluteGear()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a2fc65243b0c82ac3149abc7a299cf986),
[TestSpreadsheet.SpreadsheetCases::testIssue3128()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#adefd5d19274210bd8d1bd2c5cfc38af6),
[TestSpreadsheet.SpreadsheetCases::testIssue3225()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#aec7b0242351607a50b2dd9c56fddc630),
[TestSpreadsheet.SpreadsheetCases::testIssue3363()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a7d900672dcba23c0335248f4147543e4),
[TestSpreadsheet.SpreadsheetCases::testIssue3432()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a4d3a7dc633bfde4c015c3cac14a573a9),
[TestSpreadsheet.SpreadsheetCases::testIssue4156()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#aa1f5ab454bcf3ed6a8e34818002bb2ca),
[TestSpreadsheet.SpreadsheetCases::testIssue6840()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a4f0dbe92611cd5d7a010133df2cc2359),
[TestSpreadsheet.SpreadsheetCases::testIssue6844()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#aaa71b1cf679745731cf365443d6076c3),
[TestSpreadsheet.SpreadsheetCases::testMatrix()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#aa708c7094e7187229b13fab7fa03ab54),
[TestSpreadsheet.SpreadsheetCases::testMergeCells()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#ad17b617642135ddf6de28dd3750952c0),
[TestSpreadsheet.SpreadsheetCases::testMergeCellsAndBind()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a351e843c70a95bc73beeda96bc4cfbdc),
[TestSpreadsheet.SpreadsheetCases::testNumbers()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a4288580e2bba9d4ef77f286d5d3e0590),
[TestSpreadsheet.SpreadsheetCases::testPlacementName()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#afbe752239ba0cf89369d612a9ed6ab30),
[TestSpreadsheet.SpreadsheetCases::testPrecedence()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a65c538b1ba5ca2995355a03aed0e272b),
[TestSpreadsheet.SpreadsheetCases::testQuantitiesAndFractionsAsNumbers()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#ad4935bf67c7b63537e8a69910ccc66f9),
[TestSpreadsheet.SpreadsheetCases::testRelationalOperators()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a9396f607a2b2e0097a371eb6ffbde67c),
[TestSpreadsheet.SpreadsheetCases::testRemoveColumnsAlias()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#af04cf9539b3fcd531dc8162b49ece1dc),
[TestSpreadsheet.SpreadsheetCases::testRemoveColumnsAliasReuseName()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a59fef03846d8bda64a8e44b2373c40e6),
[TestSpreadsheet.SpreadsheetCases::testRemoveRows()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#abfc251664e4ab303cae1586e5fc2b835),
[TestSpreadsheet.SpreadsheetCases::testRemoveRowsAlias()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#aa49f14a01618bdbd0631b8a3da0ae9b0),
[TestSpreadsheet.SpreadsheetCases::testRemoveRowsAliasReuseName()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a535b568e7703e71a3a23bf36fd75c644),
[TestSpreadsheet.SpreadsheetCases::testRenameAlias()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a2a3ff68128bbc814f39502efe300ffc7),
[TestSpreadsheet.SpreadsheetCases::testRenameAlias2()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a8959faee9fc3612acc13ab1f163797f3),
[TestSpreadsheet.SpreadsheetCases::testRenameAlias3()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a0e29b87ed7c4267f89c137b4f9a78eaf),
[TestSpreadsheet.SpreadsheetCases::testSetInvalidAlias()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#aa09c2e8c4596e40e0e393a67c18eaf62),
[TestSpreadsheet.SpreadsheetCases::testSetInvalidAlias2()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#ad59afbb407212d224aa56650384d172f),
[TestSpreadsheet.SpreadsheetCases::testSketcher()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#ad8474327c442dfd5b06c23cbac259432),
[TestSpreadsheet.SpreadsheetCases::testUndoAliasCreationReuseName()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a5705ff0f9147c6749fefb8e14d2cd9ed),
[TestSpreadsheet.SpreadsheetCases::testUnits()](../../d8/da2/classTestSpreadsheet_1_1SpreadsheetCases.html#a7bf22a0d0e3a9852a1f1c09c571a5fac),
[draftguitools.gui_trimex.Trimex::trimObject()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a5e72e325ef0a53c3fde6c75c2eb56ba6),
[draftguitools.gui_trimex.Trimex::trimObjects()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a039209de5464aa216735c747791838b0),
[Mod.PartDesign.WizardShaft.Shaft.Shaft::updateConstraint()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#ab68630f3abfd4af53b7a2ad324b48fc4),
[Mod.PartDesign.WizardShaft.Shaft.Shaft::updateEdge()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#a7c017faec427bdf440f3496f0eaf3fd9),
and
[Mod.Show.SceneDetails.ObjectClipPlane.ObjectClipPlane::val()](../../d0/dd9/classMod_1_1Show_1_1SceneDetails_1_1ObjectClipPlane_1_1ObjectClipPlane.html#ae47082e56701ff5b6f39265e00c2ce0a).

## ◆ group

| std::string App::DynamicProperty::PropData::group  
---  
mutable  
  
## ◆ hidden

[bool](../../d9/db9/classbool.html) App::DynamicProperty::PropData::hidden  
---  
  
## ◆ name

std::string App::DynamicProperty::PropData::name  
---  
  
Referenced by
[draftguitools.gui_groups.Ui_AddNamedGroup::accept()](../../d3/df7/classdraftguitools_1_1gui__groups_1_1Ui__AddNamedGroup.html#a9ea5973817eab7d74792f5b109a01466),
[prototype.Node::addtofreecad()](../../d2/d62/classprototype_1_1Node.html#adc095cc5636da029d1e0d9cef8859701),
[Addon.Addon::disable()](../../d8/d91/classAddon_1_1Addon.html#ae714705a38afe9f13cd2b17580178b31),
[Addon.Addon::enable()](../../d8/d91/classAddon_1_1Addon.html#a79d327ec9a0b4e85e9e96cfad4003ed6),
[addonmanager_macro.Macro::filename()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a5de4e6a1f3c41dce24066111955cd706),
[gzip_utf8.GzipFile::filename()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ab56fe84a4eb08c44e7a0026280c01229),
[addonmanager_macro.Macro::fill_details_from_code()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a49b8d021a9b8255f8a490e880eb15489),
[addonmanager_macro.Macro::fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[Addon.Addon::get_cached_icon_filename()](../../d8/d91/classAddon_1_1Addon.html#a7b026027a2904028032edbe3e99e2cbd),
[ifc4.ifcapproval::hasidentifierorname()](../../df/d91/classifc4_1_1ifcapproval.html#a54f558ba3b17fad5fc6579e9d5f50947),
[addonmanager_macro.Macro::install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
[Addon.Addon::is_disabled()](../../d8/d91/classAddon_1_1Addon.html#a5752a95fcf0c51ed06f9841b381d3e50),
[femsolver.elmer.sifio.Section::keys()](../../db/dab/classfemsolver_1_1elmer_1_1sifio_1_1Section.html#ab5b099447f66f33743850697f0e20de4),
[automotive_design.si_unit::named_unit_dimensions()](../../d5/d77/classautomotive__design_1_1si__unit.html#a68eb7954eb09daa334bc8f2c2abbe5f9),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction::output()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aeedd5f59969cc27432880d1916f3d7f9),
[prototype.Node::pprint()](../../d2/d62/classprototype_1_1Node.html#a5ae181c34e48238d2364b0ba4960c252),
[prototype.Node::pprint2()](../../d2/d62/classprototype_1_1Node.html#aaedcc4ba1fb305c7ddcc025235043cd5),
[PathScripts.PathSetupSheetGui.OpTaskPanel::propertyGroup()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a69cbbaadcb9cff7b526af2c743041d7b),
[PathScripts.PathSetupSheetGui.OpTaskPanel::propertyName()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#ad9bd0e0149d1bc42fc8e89a290de4910),
[PathScripts.PathJobGui.TaskPanel::reject()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a54fd97ba9b0060fa8fed8a43c360da0c),
[addonmanager_macro.Macro::remove()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ad13245288f8beb62d92cb458a2d2ce05),
[Addon.Addon::to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
[ifc2x3.ifcexternalreference::wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc2x3.ifcdocumentreference::wr1()](../../df/dd6/classifc2x3_1_1ifcdocumentreference.html#a7d5fdb1cb0dee567c44834b868c5cdad),
[ifc4.ifcexternalreference::wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
[ifc4.ifcdocumentreference::wr1()](../../d7/d2b/classifc4_1_1ifcdocumentreference.html#a8779d74c67e647441d1fb20c76f44f97),
and
[automotive_design.general_property_association::wr2()](../../d2/df3/classautomotive__design_1_1general__property__association.html#ae7f46462c59bc4e541a5d2511631eb65).

## ◆ pName

const char* App::DynamicProperty::PropData::pName  
---  
  
## ◆ property

[Property](../../d0/da9/classApp_1_1Property.html)*
App::DynamicProperty::PropData::property  
---  
  
Referenced by
[App::TransactionObject::addOrRemoveProperty()](../../d9/d02/classApp_1_1TransactionObject.html#a1a9c63db207f7e24ed6918877c134764).

## ◆ readonly

[bool](../../d9/db9/classbool.html) App::DynamicProperty::PropData::readonly  
---  
  
* * *

The documentation for this struct was generated from the following file:

  * FreeCAD/src/App/DynamicProperty.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

