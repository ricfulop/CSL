---
url: https://freecad.github.io/SourceDoc/d8/d62/classautomotive__design_1_1index__expression.html
scraped_at: 2025-09-08T15:06:35.459050
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [index_expression](../../d8/d62/classautomotive__design_1_1index__expression.html)

[List of all members](../../dc/d4d/classautomotive__design_1_1index__expression-members.html) | Public Member Functions

automotive_design.index_expression Class Reference

##  Public Member Functions  
  
---  
def | [index](../../d8/d62/classautomotive__design_1_1index__expression.html#a6023c810ab7d51105f5348ee5a9634d3) ()  
def | [operand](../../d8/d62/classautomotive__design_1_1index__expression.html#aafcdd43ed52e191ad1f9215db73c4e9e) ()  
def | [wr1](../../d8/d62/classautomotive__design_1_1index__expression.html#a33cd6562421dd35dd68ed821911fa212) (self)  
def | [wr2](../../d8/d62/classautomotive__design_1_1index__expression.html#ae866ecb4f6c498eb2e14ad96dc658713) (self)  
def | [wr1](../../d3/d52/classautomotive__design_1_1generic__expression.html#aea35213a5e29cdc6cc6a201099976f3e) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.binary_generic_expression](../../da/d4f/classautomotive__design_1_1binary__generic__expression.html)  
def | [operands](../../da/d4f/classautomotive__design_1_1binary__generic__expression.html#a02f66c9c0ff94333142e937c1bf28407) ()  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.binary_generic_expression](../../da/d4f/classautomotive__design_1_1binary__generic__expression.html)  
|
[operands](../../da/d4f/classautomotive__design_1_1binary__generic__expression.html#aabaa4a6ce4f17d067b7db22ee116a6fc)  
  
## Detailed Description

    
    
    Entity index_expression definition.
    
        :param operand
        :type operand:generic_expression
    
        :param index
        :type index:generic_expression

## Member Function Documentation

## ◆ index()

def automotive_design.index_expression.index  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.addSegment()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#a73f34ba120a3641c2169927f34d29564),
[Dice3DS.dom3ds.FileLikeBuffer.advance()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#a8e06865a859e1dbb164c3b03d4065553),
[Mod.PartDesign.WizardShaft.SegmentFunction.IntervalFunction.begin()](../../d9/d57/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1IntervalFunction.html#a47ba646581acaa91288aea691b21fbc8),
[Spreadsheet_legacy.MathParser.getValue()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#ac5fdee74cba034671b868afb23fdb6c6),
[Spreadsheet_legacy.MathParser.hasNext()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a880d2d2a50b45fc7d1a43f93920d7543),
[Mod.PartDesign.WizardShaft.SegmentFunction.IntervalFunction.interval()](../../d9/d57/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1IntervalFunction.html#a5ef34aa51bb69c8d1b3b2a2af9e061b7),
[PathScripts.PathJobDlg.JobCreate.item1ValueChanged()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a973f7ff4f6d5bb4e3ea6632d7d125168),
[Mod.PartDesign.WizardShaft.SegmentFunction.IntervalFunction.length()](../../d9/d57/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1IntervalFunction.html#a4302e1c0e5212af68db0bdb774baae43),
[Spreadsheet_legacy.MathParser.parseAddition()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#ac9b55b1f210107c748b4d4ef7a8018d8),
[Spreadsheet_legacy.MathParser.parseMultiplication()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a1f8617cb8b1a0d73fcc0eeeedcc45821),
[Spreadsheet_legacy.MathParser.parseNegative()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a386a29370720b05a97d131446ac8e231),
[Spreadsheet_legacy.MathParser.parseNumber()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#ad79b517ebec8674487871468c8fb92da),
[Spreadsheet_legacy.MathParser.parseParenthesis()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a311e806ef369d66874faaa4a0a782e7f),
[Spreadsheet_legacy.MathParser.parseVariable()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#aefe029c854bcd7243748b2f5332e3011),
[Spreadsheet_legacy.MathParser.peek()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a56d2b8422c194d4440df5d1ae85e04ef),
[Dice3DS.dom3ds.FileLikeBuffer.read()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#accc58fbe7199d97a99f80702add1353f),
[Dice3DS.dom3ds.FileLikeBuffer.read_fbuf()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#aec1ecdfd6ce0846d69ac0760c1944040),
[Dice3DS.dom3ds.FileLikeBuffer.read_rest()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#a9d6c356ba5bfee8c51fa348f902c3852),
[Dice3DS.dom3ds.FileLikeBuffer.read_to_nul()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#a51bc6a89a08cde8df68b553656931ee4),
[Dice3DS.dom3ds.FileLikeBuffer.room_for_chunks()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#ab01563eb0dff95345b47c98a398ab33f),
[Dice3DS.dom3ds.FileLikeBuffer.seek()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#a14ec480a1bd8005ee16364c883d63d8b),
[package_list.PackageListItemModel.setData()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#ae93144aca21b886d805bd1517cbc68f9),
[PathScripts.PathJobDlg.JobCreate.setupColumnEditor()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#abe2f1a94b2473feed55932660a7d4c64),
[Spreadsheet_legacy.MathParser.skipWhitespace()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a696f1682e443f2e488b2eea3f208aa5c),
[Dice3DS.dom3ds.FileLikeBuffer.tell()](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#aafe9a2d6713d74fa10d7860ab9b2a031),
[package_list.PackageListItemModel.update_item_icon()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#ac42a6bdc52fbbd4b036906f263ec2007),
[package_list.PackageListItemModel.update_item_status()](../../d0/d1c/classpackage__list_1_1PackageListItemModel.html#a4d22be53f021c227b368ac920544263c),
[automotive_design.index_expression.wr1()](../../d8/d62/classautomotive__design_1_1index__expression.html#a33cd6562421dd35dd68ed821911fa212),
and
[automotive_design.index_expression.wr2()](../../d8/d62/classautomotive__design_1_1index__expression.html#ae866ecb4f6c498eb2e14ad96dc658713).

## ◆ operand()

def automotive_design.index_expression.operand  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.index_expression.wr1()](../../d8/d62/classautomotive__design_1_1index__expression.html#a33cd6562421dd35dd68ed821911fa212),
and
[automotive_design.substring_expression.wr1()](../../d7/daa/classautomotive__design_1_1substring__expression.html#ae42f045ef3b42b7bdfe476af38354c92).

## ◆ wr1()

def automotive_design.index_expression.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.generic_expression](../../d3/d52/classautomotive__design_1_1generic__expression.html#aea35213a5e29cdc6cc6a201099976f3e).

References
[kdtreeNode.index](../../d7/d3b/structkdtreeNode.html#ab298a2f7e92115b842200e8f6e57179a),
SMDS_FaceOfEdges_MyIterator.index, SMDS_VolumeOfFaces_MyIterator.index,
[App::LinkBaseExtension::PropInfo.index](../../d5/d5c/structApp_1_1LinkBaseExtension_1_1PropInfo.html#af3f6a6c5662582aca276038957560e70),
App::VRMLObject.index, Base::Type.index,
[ExpressionCompleterModel.index()](../../d8/d22/classExpressionCompleterModel.html#a5b1dd78e8fc67b4bf5528ca9b308ddd2),
[NetworkManager.QueueItem.index](../../d8/d41/classNetworkManager_1_1QueueItem.html#a5d1408e476eec17c2621a77e7136fdaa),
[Dice3DS.dom3ds.FileLikeBuffer.index](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#a5b405add3cfb451a459f887ea8d57769),
[automotive_design.index_expression.index()](../../d8/d62/classautomotive__design_1_1index__expression.html#a6023c810ab7d51105f5348ee5a9634d3),
DrawingGui::OrthoViews.index(),
[Gui::Dialog::CommandModel.index()](../../d4/d98/classGui_1_1Dialog_1_1CommandModel.html#ace505ef9347dcc9fe18835f6f34eea60),
[Gui::DocumentModel.index()](../../dc/dc8/classGui_1_1DocumentModel.html#ac6d131dd0836ebb051247bbd6fc8b404),
[Gui::PropertyEditor::PropertyModel.index()](../../d3/da0/classGui_1_1PropertyEditor_1_1PropertyModel.html#a79df2ecc46f8c67cf00d3876c24c9d2b),
[MeshGui::ViewProviderFace.index](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#abb31cc04031aeaf67ea685728bf38cde),
[MeshGui::SoFCMeshSegmentShape.index](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#af0e5452b5f69290a5d7d58a06e2c14ec),
[PartGui::ResultModel.index()](../../d5/d51/classPartGui_1_1ResultModel.html#a124078a0756daba5a3915dc9b3d00830),
[PartGui::FaceColors::Private.index](../../d4/d4b/classFaceColors_1_1Private.html#a9256cb92d704011014d1247a4c10896c),
[Path::Voronoi::diagram_type.index()](../../d8/d4a/classPath_1_1Voronoi_1_1diagram__type.html#adbb9d0f80d9fb8ce131086b4a6aaecc4),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.index()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#acdbb4a0cb4437b86f5f1a57d9b9759d0),
[Mod.PartDesign.WizardShaft.SegmentFunction.IntervalFunction.index()](../../d9/d57/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1IntervalFunction.html#adb8db318ff83543635bee199ad83f0bf),
SMDS_MeshInfo.index(),
[Path::VoronoiCell.index](../../da/d69/classPath_1_1VoronoiCell.html#a2683824c83cd5c7236b8daa7be4dada4),
[Path::VoronoiEdge.index](../../d0/dfc/classPath_1_1VoronoiEdge.html#a243b5e03eb992b72fcc3e4fb593a7bb2),
[Path::VoronoiVertex.index](../../d5/df3/classPath_1_1VoronoiVertex.html#a5297db3141e1d0ccd6676793e853d9d1),
[geoff_geometry::SpanVertex.index](../../de/dc5/classgeoff__geometry_1_1SpanVertex.html#a12561691d2c91c1aa2637e70f629a486),
[PathScripts.PathJobDlg.JobCreate.index](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a57e748ea17766caf28a19238009d7cb1),
[PathScripts.PathUtils.depth_params.index](../../d7/d7f/classPathScripts_1_1PathUtils_1_1depth__params.html#a3f22ad63608d9829ed1fcd743b402fb4),
[Sketcher::Sketch::GeoDef.index](../../d2/db8/structSketcher_1_1Sketch_1_1GeoDef.html#a08fb33515562fc866b369b9dd69edf37),
[Spreadsheet_legacy.MathParser.index](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a091de267669a3465d055634146dea962),
[TechDraw::GeometryUtils::ReturnType.index](../../de/d9f/structTechDraw_1_1GeometryUtils_1_1ReturnType.html#a6299914dce87cc0dd3387e578e7f3c8b),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.unary_generic_expression.operand,
[automotive_design.unary_generic_expression.operand](../../d0/d3e/classautomotive__design_1_1unary__generic__expression.html#a7c62536d30a150a503d090d2a0dfed36),
[automotive_design.index_expression.operand()](../../d8/d62/classautomotive__design_1_1index__expression.html#aafcdd43ed52e191ad1f9215db73c4e9e),
and
[automotive_design.substring_expression.operand()](../../d7/daa/classautomotive__design_1_1substring__expression.html#af41ff3117f63d3a5fc31b5334f872344).

## ◆ wr2()

def automotive_design.index_expression.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[kdtreeNode.index](../../d7/d3b/structkdtreeNode.html#ab298a2f7e92115b842200e8f6e57179a),
SMDS_FaceOfEdges_MyIterator.index, SMDS_VolumeOfFaces_MyIterator.index,
[App::LinkBaseExtension::PropInfo.index](../../d5/d5c/structApp_1_1LinkBaseExtension_1_1PropInfo.html#af3f6a6c5662582aca276038957560e70),
App::VRMLObject.index, Base::Type.index,
[Gui::Dialog::CommandModel.index()](../../d4/d98/classGui_1_1Dialog_1_1CommandModel.html#ace505ef9347dcc9fe18835f6f34eea60),
[Gui::DocumentModel.index()](../../dc/dc8/classGui_1_1DocumentModel.html#ac6d131dd0836ebb051247bbd6fc8b404),
[ExpressionCompleterModel.index()](../../d8/d22/classExpressionCompleterModel.html#a5b1dd78e8fc67b4bf5528ca9b308ddd2),
[Gui::PropertyEditor::PropertyModel.index()](../../d3/da0/classGui_1_1PropertyEditor_1_1PropertyModel.html#a79df2ecc46f8c67cf00d3876c24c9d2b),
[NetworkManager.QueueItem.index](../../d8/d41/classNetworkManager_1_1QueueItem.html#a5d1408e476eec17c2621a77e7136fdaa),
[Dice3DS.dom3ds.FileLikeBuffer.index](../../d5/d71/classDice3DS_1_1dom3ds_1_1FileLikeBuffer.html#a5b405add3cfb451a459f887ea8d57769),
[automotive_design.index_expression.index()](../../d8/d62/classautomotive__design_1_1index__expression.html#a6023c810ab7d51105f5348ee5a9634d3),
DrawingGui::OrthoViews.index(),
[MeshGui::ViewProviderFace.index](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#abb31cc04031aeaf67ea685728bf38cde),
[MeshGui::SoFCMeshSegmentShape.index](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#af0e5452b5f69290a5d7d58a06e2c14ec),
[PartGui::ResultModel.index()](../../d5/d51/classPartGui_1_1ResultModel.html#a124078a0756daba5a3915dc9b3d00830),
[PartGui::FaceColors::Private.index](../../d4/d4b/classFaceColors_1_1Private.html#a9256cb92d704011014d1247a4c10896c),
[Path::Voronoi::diagram_type.index()](../../d8/d4a/classPath_1_1Voronoi_1_1diagram__type.html#adbb9d0f80d9fb8ce131086b4a6aaecc4),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.index()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#acdbb4a0cb4437b86f5f1a57d9b9759d0),
[Mod.PartDesign.WizardShaft.SegmentFunction.IntervalFunction.index()](../../d9/d57/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1IntervalFunction.html#adb8db318ff83543635bee199ad83f0bf),
SMDS_MeshInfo.index(),
[Path::VoronoiCell.index](../../da/d69/classPath_1_1VoronoiCell.html#a2683824c83cd5c7236b8daa7be4dada4),
[Path::VoronoiEdge.index](../../d0/dfc/classPath_1_1VoronoiEdge.html#a243b5e03eb992b72fcc3e4fb593a7bb2),
[Path::VoronoiVertex.index](../../d5/df3/classPath_1_1VoronoiVertex.html#a5297db3141e1d0ccd6676793e853d9d1),
[geoff_geometry::SpanVertex.index](../../de/dc5/classgeoff__geometry_1_1SpanVertex.html#a12561691d2c91c1aa2637e70f629a486),
[PathScripts.PathJobDlg.JobCreate.index](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a57e748ea17766caf28a19238009d7cb1),
[PathScripts.PathUtils.depth_params.index](../../d7/d7f/classPathScripts_1_1PathUtils_1_1depth__params.html#a3f22ad63608d9829ed1fcd743b402fb4),
[Sketcher::Sketch::GeoDef.index](../../d2/db8/structSketcher_1_1Sketch_1_1GeoDef.html#a08fb33515562fc866b369b9dd69edf37),
[Spreadsheet_legacy.MathParser.index](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a091de267669a3465d055634146dea962),
[TechDraw::GeometryUtils::ReturnType.index](../../de/d9f/structTechDraw_1_1GeometryUtils_1_1ReturnType.html#a6299914dce87cc0dd3387e578e7f3c8b),
and
[automotive_design.is_int_expr()](../../d4/ddf/namespaceautomotive__design.html#ae2d12b4b398f78fc93cc2db4c84f380a).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

