---
url: https://freecad.github.io/SourceDoc/d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html
scraped_at: 2025-09-08T14:57:40.189658
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchCurtainWall](../../d7/dd3/namespaceArchCurtainWall.html)
  * [CommandArchCurtainWall](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html)

[List of all members](../../dc/da2/classArchCurtainWall_1_1CommandArchCurtainWall-members.html) | Public Member Functions | Public Attributes

ArchCurtainWall.CommandArchCurtainWall Class Reference

##  Public Member Functions  
  
---  
def | [Activated](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#af52cfef9ec45b213d701a86b937538b7) (self)  
def | [getPoint](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#ae21c6277cadac9992ad426960f203392) (self, point=None, obj=None)  
def | [GetResources](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#a615aefaf67e0751a2893a0dbfddb165c) (self)  
def | [IsActive](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#a7f0975ac1da7b7461c5665869ec17055) (self)  
  
##  Public Attributes  
  
---  
|
[points](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#ab09aac56300281080c3df33b1bc579cd)  
  
## Member Function Documentation

## ◆ Activated()

def ArchCurtainWall.CommandArchCurtainWall.Activated  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftguitools.gui_arcs.Arc.finish()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a2262d966a879bfa9b71d9c699e6929b2),
[draftguitools.gui_beziers.BezCurve.finish()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a6b4598d09cb7c1f0b06fe1b96cc9096f),
[draftguitools.gui_beziers.CubicBezCurve.finish()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#abadcbdae43b1e54d516d249c71fc0991),
[draftguitools.gui_ellipses.Ellipse.finish()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#aa534628f13f8ad6effacb1fcbd76bb2a),
[draftguitools.gui_lines.Line.finish()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#a622af4e1166f892f860b86d3d1e3f053),
[draftguitools.gui_mirror.Mirror.finish()](../../d8/dbd/classdraftguitools_1_1gui__mirror_1_1Mirror.html#a73d8f0dba4d186590485bf972fa8e25d),
[draftguitools.gui_move.Move.finish()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#aa2c8c371106351f316c238f67bf7accf),
[draftguitools.gui_polygons.Polygon.finish()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a06317245940b6d99d62b0823d657dcb2),
[draftguitools.gui_rectangles.Rectangle.finish()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a7ba174f4093affb5af55e58c804a527d),
[draftguitools.gui_rotate.Rotate.finish()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#ad60faae5b86f1d2c74f045c2291ae6dd),
[draftguitools.gui_splines.BSpline.finish()](../../d1/d3f/classdraftguitools_1_1gui__splines_1_1BSpline.html#ab00ba1111a2b9d2afcee43a0396a4cd5),
[draftguitools.gui_texts.Text.finish()](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a3fe64be64c77319af1f265609dd8e985),
[draftguitools.gui_points.Point.finish()](../../d7/dc7/classdraftguitools_1_1gui__points_1_1Point.html#ac55499c15db7b01680f41b3f3dd32477),
[draftguitools.gui_shapestrings.ShapeString.finish()](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#af7a14bf7135177bc521cfa7a9123b2bf),
[draftguitools.gui_arcs.Arc_3Points.getPoint()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#addd65326b504c7bf765526ef2db14321),
and
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb).

## ◆ getPoint()

def ArchCurtainWall.CommandArchCurtainWall.getPoint  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _point_ = `None`,   
|  |  | _obj_ = `None`  
| ) | |   
      
    
    Callback for clicks during interactive mode

References
[PartDesign::Point.getPoint()](../../da/d0d/classPartDesign_1_1Point.html#a425bd8831010df262ca4482511fca22a),
[Sketcher::SolverGeometryExtension.getPoint()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#aa504b70e1e8bf7aeb397cfc31cc4f9be),
[Points::PointKernel.getPoint()](../../dc/de1/classPoints_1_1PointKernel.html#a55849aaf8aff4c818fba7d9918c0ece5),
[SMESH_MAT2d::Branch.getPoint()](../../de/ddb/classSMESH__MAT2d_1_1Branch.html#a871f17ae4f318ac2b3f9be3fb020342c),
[Sketcher::Sketch.getPoint()](../../d9/d9b/classSketcher_1_1Sketch.html#a802408327f37cd31123bebcfe1004d73),
[Sketcher::SketchObject.getPoint()](../../d9/dad/classSketcher_1_1SketchObject.html#a8c0707e1362b0b4214aea676a125332c),
[Sketcher::GeoListModel< T
>.getPoint()](../../df/d90/classSketcher_1_1GeoListModel.html#a694e726de859c4b69a2b591396a83790),
[Mesh::MeshObject.getPoint()](../../d8/dcc/classMesh_1_1MeshObject.html#a3b5cfb389c3be7ecad0809494f54418d),
[draftguitools.gui_snapper.Snapper.getPoint()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a4d53d3953b035a41f086e3db5c0ab20b),
[draftguitools.gui_arcs.Arc_3Points.getPoint()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#addd65326b504c7bf765526ef2db14321),
[ArchCurtainWall.CommandArchCurtainWall.getPoint()](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#ae21c6277cadac9992ad426960f203392),
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[ArchProfile.Arch_Profile.getPoint()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#adba04e55c6f0800f15566d4246397582),
ArchStructure._CommandStructure.getPoint(),
[ArchTruss.CommandArchTruss.getPoint()](../../dc/d2c/classArchTruss_1_1CommandArchTruss.html#aee560d06232a65dbd5f410bcac5c0318),
ArchWall._CommandWall.getPoint(), ArchWindow._CommandWindow.getPoint(),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.getPoint](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a46d611994ef5db3a015908085bdfa117),
[PathScripts.PathGetPoint.TaskPanel.getPoint()](../../d8/d28/classPathScripts_1_1PathGetPoint_1_1TaskPanel.html#a887ab8742a503f9a0c4c177498f518f4),
[SMESH_MAT2d::Boundary.getPoint()](../../d7/dbe/classSMESH__MAT2d_1_1Boundary.html#aee6e6645bc69b2aa2b1d79ef7e39afb4),
[Inspection::InspectActualMesh.getPoint()](../../d1/d64/classInspection_1_1InspectActualMesh.html#ad2cc7f18f04c0b95b2f6a8d32e3a876a),
[Inspection::InspectActualPoints.getPoint()](../../d3/d83/classInspection_1_1InspectActualPoints.html#acfd8d8c21c9f33c0ed721d527ac1fe31),
[Inspection::InspectActualShape.getPoint()](../../d8/d95/classInspection_1_1InspectActualShape.html#a3cf3eae488e9dd2a9d16a71176ba356f),
[Inspection::InspectActualGeometry.getPoint()](../../d6/db1/classInspection_1_1InspectActualGeometry.html#a0a1ca32a2b808408372f301e24daad95),
[Part::GeomPoint.getPoint()](../../d2/dfb/classPart_1_1GeomPoint.html#ae8f4424f6e1498fd986ab667a7d2cd3c),
[Part::Geom2dPoint.getPoint()](../../d8/da9/classPart_1_1Geom2dPoint.html#a25ac6607d7ab1aa8932d3f7e077f159a),
[PathScripts.PathOpGui.TaskPanelBaseLocationPage.getPoint](../../d6/d50/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseLocationPage.html#a972ec73045a01d0ef02e4ce990856c4c),
[Data::ComplexGeoData::Domain.points](../../d7/d46/structData_1_1ComplexGeoData_1_1Domain.html#a36261bff507a33609ed97caadec3cf6a),
[ArchCurtainWall.CommandArchCurtainWall.points](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#ab09aac56300281080c3df33b1bc579cd),
[ArchPanel.CommandPanel.points](../../d9/d86/classArchPanel_1_1CommandPanel.html#a84150c5b41f0eac464b49d1c5d914333),
ArchStructure._CommandStructure.points,
[ArchTruss.CommandArchTruss.points](../../dc/d2c/classArchTruss_1_1CommandArchTruss.html#a95ed5e0ec29c727e4606afe54e3a468d),
ArchWall._CommandWall.points,
[draftguitools.gui_arcs.Arc_3Points.points](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#ae17b3c4fc57f4a6355cb5de8434d0bd4),
[draftguitools.gui_trackers.bsplineTracker.points](../../d4/d09/classdraftguitools_1_1gui__trackers_1_1bsplineTracker.html#a5853ab2bec9a086cb9dd15201e3e6705),
[draftguitools.gui_trackers.bezcurveTracker.points](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#a4afebb3fb8c9ba7e4710c2d1f76c4ab8),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.polyline.points,
[automotive_design.polyline.points](../../dd/d6a/classautomotive__design_1_1polyline.html#a7869ee5769747722642e5c95fd978000),
[config_control_design.polyline.points](../../db/d17/classconfig__control__design_1_1polyline.html#a9f08e8c099ff25df034677ca60852e89),
[ifc2x3.ifcpolyline.points](../../d9/d78/classifc2x3_1_1ifcpolyline.html#a542006e311ab22b8185183a7c0e47001),
[ifc4.ifcpolyline.points](../../d3/df6/classifc4_1_1ifcpolyline.html#afcd597dc3822e1a3652170954bd6b85e),
Inspection::InspectActualShape.points,
[MeshGui::FitParameter::Points.points](../../d7/d7f/structMeshGui_1_1FitParameter_1_1Points.html#ad1799f8b13c64627d5a0039451a26245),
[MeshPart::MeshProjection::PolyLine.points](../../d1/d3d/structMeshPart_1_1MeshProjection_1_1PolyLine.html#af66fe08cf5ea1947ecaa13d8f4028cde),
PartGui::CircleFromThreePoints.points,
[PartGui::ArcEngine.points](../../d8/d2e/classPartGui_1_1ArcEngine.html#a92e35a5a570cb9d4f9e13c6a0214d02b),
[WireInfo.points](../../d4/df6/structWireInfo.html#a6240510ea1b3afea5026b5e2f3d3cdbc),
[Path::Voronoi::diagram_type.points](../../d8/d4a/classPath_1_1Voronoi_1_1diagram__type.html#a4f8580988e0e3bc190c025a1958a4533),
VisualPathSegmentVisitor.points,
[Triangle3D.points](../../d6/de9/structTriangle3D.html#af525f7707afab7adcfe122fc64cd1628),
[Points::Reader.points](../../dc/d70/classPoints_1_1Reader.html#abf5909927d46d04be9fa03861f8cd7cb),
[Points::Writer.points](../../d1/de9/classPoints_1_1Writer.html#a71ea7a1dc050e89b527cd8ddf1ffbc61),
and
[TechDraw::Generic.points](../../dd/d23/classTechDraw_1_1Generic.html#afba8eb15a338fbdec6d126c258056b63).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[PathScripts.PathOpGui.TaskPanelBaseLocationPage.addLocation()](../../d6/d50/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseLocationPage.html#ab5f56b9ada560aab1c7ec52da82887e2),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.addNewTag()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#ad5c4ec1bd21c22bd83a9ef4c2cf7b2a8),
[PathScripts.PathOpGui.TaskPanelBaseLocationPage.editLocation()](../../d6/d50/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseLocationPage.html#a6eaff94ff9e615e8dacac7241fb3229d),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.editTag()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a66963fb0f8fbff5f5b1f0de6d92aa468),
[draftguitools.gui_arcs.Arc_3Points.getPoint()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#addd65326b504c7bf765526ef2db14321),
[ArchCurtainWall.CommandArchCurtainWall.getPoint()](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#ae21c6277cadac9992ad426960f203392),
[ArchTruss.CommandArchTruss.getPoint()](../../dc/d2c/classArchTruss_1_1CommandArchTruss.html#aee560d06232a65dbd5f410bcac5c0318),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.modifyStandardButtons()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a7e92a13bef37b0a1ba80f6ee14501147),
and
[PathScripts.PathOpGui.TaskPanelBaseLocationPage.modifyStandardButtons()](../../d6/d50/classPathScripts_1_1PathOpGui_1_1TaskPanelBaseLocationPage.html#aac091052db42e260ae961d00e55aa4a0).

## ◆ GetResources()

def ArchCurtainWall.CommandArchCurtainWall.GetResources  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4).

## ◆ IsActive()

def ArchCurtainWall.CommandArchCurtainWall.IsActive  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ points

ArchCurtainWall.CommandArchCurtainWall.points  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftguitools.gui_arcs.Arc_3Points.drawArc()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#ad2b5ab087c3acf911c62b7d6816bd083),
[draftguitools.gui_arcs.Arc_3Points.getPoint()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#addd65326b504c7bf765526ef2db14321),
[ArchCurtainWall.CommandArchCurtainWall.getPoint()](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#ae21c6277cadac9992ad426960f203392),
[ArchTruss.CommandArchTruss.getPoint()](../../dc/d2c/classArchTruss_1_1CommandArchTruss.html#aee560d06232a65dbd5f410bcac5c0318),
[draftguitools.gui_trackers.bsplineTracker.recompute()](../../d4/d09/classdraftguitools_1_1gui__trackers_1_1bsplineTracker.html#a5d3df8a04be660bfc6a6e6613285c145),
[draftguitools.gui_trackers.bezcurveTracker.recompute()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#abb21c673d4078ec0eafdaa2ce727520d),
[draftguitools.gui_trackers.bsplineTracker.update()](../../d4/d09/classdraftguitools_1_1gui__trackers_1_1bsplineTracker.html#a780d90044fb459aa47487afc9d7979c9),
[draftguitools.gui_trackers.bezcurveTracker.update()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#a768d7d59cf62a7cfe8fbdc4486a17a63),
[automotive_design.advanced_face.wr10()](../../d1/d62/classautomotive__design_1_1advanced__face.html#aa08adf112660acfb17f4847e837bdf6d),
and
[config_control_design.advanced_face.wr10()](../../db/d65/classconfig__control__design_1_1advanced__face.html#a0118e22d47858317fa0dff7407854d05).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchCurtainWall.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

