---
url: https://freecad.github.io/SourceDoc/dc/dc3/group__DRAFTVECUTILS.html
scraped_at: 2025-09-08T14:52:24.973556
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Functions

DraftVecUtils

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Utility
modules](../../da/d56/group__UTILITIES.html)

Vector math utilities used in [Draft](../../d4/d1a/namespaceDraft.html)
workbench. More...

##  Functions  
  
---  
def | [DraftVecUtils.angle](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9) (u, v=Vector(1, 0, 0), normal=Vector(0, 0, 1))  
def | [DraftVecUtils.closest](../../dc/dc3/group__DRAFTVECUTILS.html#ga8035ae4425c9330b9ba7a75ba7735749) (vector, vlist, return_length=False)  
def | [DraftVecUtils.dist](../../dc/dc3/group__DRAFTVECUTILS.html#ga2af953a65bfefb422584aa67c55dbc39) (u, v)  
def | [DraftVecUtils.equals](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33) (u, v)  
def | [DraftVecUtils.find](../../dc/dc3/group__DRAFTVECUTILS.html#gaf764683bba7871d8f3d64db4fb2a41a9) (vector, vlist)  
def | [DraftVecUtils.get_cartesian_coords](../../dc/dc3/group__DRAFTVECUTILS.html#gafbeb1b81f0c8c66bf473d7f5e5bacfd0) (radius, theta, phi)  
def | [DraftVecUtils.get_spherical_coords](../../dc/dc3/group__DRAFTVECUTILS.html#gac9a8c09b44c3d53809ec187936115c04) (x, y, z)  
def | [DraftVecUtils.getPlaneRotation](../../dc/dc3/group__DRAFTVECUTILS.html#ga8ac4fe6e7590ab515d4f1287a79ee88f) (u, v, w=None)  
def | [DraftVecUtils.getRotation](../../dc/dc3/group__DRAFTVECUTILS.html#gabde55e892e8108caa17c42ac86560b6f) (vector, [reference](../../d1/da0/classint.html)=Vector(1, 0, 0))  
def | [DraftVecUtils.isColinear](../../dc/dc3/group__DRAFTVECUTILS.html#ga5af8ac969e7561440b80810e9fbd5194) (vlist)  
def | [DraftVecUtils.isNull](../../dc/dc3/group__DRAFTVECUTILS.html#gaaccdee2ed1226b010ac7b3e04c42a687) (vector)  
def | [DraftVecUtils.neg](../../dc/dc3/group__DRAFTVECUTILS.html#gadc85e420d51ac389c376dadd8b68e558) (u)  
def | [DraftVecUtils.precision](../../dc/dc3/group__DRAFTVECUTILS.html#ga1dde8544b2fa3998691eb2adb39a100d) ()  
def | [DraftVecUtils.project](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc) (u, v)  
def | [DraftVecUtils.removeDoubles](../../dc/dc3/group__DRAFTVECUTILS.html#ga7d65c2df29e414c0ca1ad2c8fd34c3b7) (vlist)  
def | [DraftVecUtils.rotate](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1) (u, [angle](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9), axis=Vector(0, 0, 1))  
def | [DraftVecUtils.rotate2D](../../dc/dc3/group__DRAFTVECUTILS.html#gadab5cb4c181c37673ecf621f75b57e95) (u, [angle](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9))  
def | [DraftVecUtils.rounded](../../dc/dc3/group__DRAFTVECUTILS.html#ga01d690601ec188428f45cb244c78a4ed) (v, d=None)  
def | [DraftVecUtils.scale](../../dc/dc3/group__DRAFTVECUTILS.html#ga21ac4cbf94f2ea5f128cea89ed5dfca2) (u, scalar)  
def | [DraftVecUtils.scaleTo](../../dc/dc3/group__DRAFTVECUTILS.html#ga6b1b9879299d28cb689cbee684e9d5f3) (u, l)  
def | [DraftVecUtils.toString](../../dc/dc3/group__DRAFTVECUTILS.html#gaf4889ceb585ea38ecf58d3f2af95b39a) (u)  
def | [DraftVecUtils.tup](../../dc/dc3/group__DRAFTVECUTILS.html#gada8f1f6ff2e9aca9a3ff9384ae3bbd27) (u, array=False)  
def | [DraftVecUtils.typecheck](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689) (args_and_types, name="?")  
  
## Detailed Description

Vector math utilities used in [Draft](../../d4/d1a/namespaceDraft.html)
workbench.

Vector math utilities used primarily in the
[Draft](../../d4/d1a/namespaceDraft.html) workbench but which can also be used
in other workbenches and in macros.

## Function Documentation

## ◆ angle()

def DraftVecUtils.angle  | ( |  | _u_ ,   
---|---|---|---  
|  |  | _v_ = `Vector(1, 0, 0)`,   
|  |  | _normal_ = `Vector(0, 0, 1)`  
| ) | |   
      
    
    Return the angle in radians between the two vectors.
    
    It uses the definition of the dot product
    ::
        A * B = |A||B| cos(angle)
    
    If only one vector is given, the angle is between that one and the
    horizontal (+X).
    
    If a third vector is given, it is the normal used to determine
    the sign of the angle.
    This normal is used to calculate a `factor` as the dot product
    with the cross product of the first two vectors.
    ::
        C = A x B
        factor = normal * C
    
    If the `factor` is positive the angle is positive, otherwise
    it is the opposite sign.
    
    Parameters
    ----------
    u : Base::Vector3
        The first vector.
    v : Base::Vector3, optional
        The second vector to test against the first one.
        It defaults to `(1, 0, 0)`, or +X.
    normal : Base::Vector3, optional
        The vector indicating the normal.
        It defaults to `(0, 0, 1)`, or +Z.
    
    Returns
    -------
    float
        The angle in radians between the vectors.
        It is zero if the magnitude of one of the vectors is zero,
        or if they are colinear.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[draftguitools.gui_offset.Offset.action()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#af6fe1d529ed82fe117bb430a75844ec5),
[importDXF.addText()](../../d7/dbf/namespaceimportDXF.html#a9542af2528d721e677018e7705990190),
[draftgeoutils.intersections.angleBisection()](../../d9/dfd/group__draftgeoutils.html#ga692ff72eee5139e832fb1fc6f5ee949e),
[importSVG.arcend2center()](../../d1/d33/namespaceimportSVG.html#a50fc279fb9fa987a96925aa05ac2a3ca),
[Gui::PropertyEditor::RotationHelper.assignProperty()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#ac33aed562242424b692098b02ff8e956),
[StdMeshers_Quadrangle_2D.check()](../../d1/db4/classStdMeshers__Quadrangle__2D.html#a54d4e01d3c35d1a2492a21a74127e875),
[draftgeoutils.circles.circleFrom2LinesRadius()](../../d9/dfd/group__draftgeoutils.html#gac123fb7d62899d609a3206597da6e734),
[AdaptivePath::Interpolation.clampAngle()](../../d1/d41/classAdaptivePath_1_1Interpolation.html#a5bfd2677e2d7b16fa7e7f05445888c2b),
[Path::Voronoi.colorColinear()](../../d8/dfd/classPath_1_1Voronoi.html#aa9417cbd3fd3e71613152a05064633f3),
[draftguitools.gui_labels.Label.create()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a3eb18f4a13e2c3c5be440173e20576a7),
[exportIFC.createCurve()](../../d8/d5d/namespaceexportIFC.html#a619ad8294a46ea5516667f513d04c003),
[Import::ExportOCAF.createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[draftguitools.gui_rectangles.Rectangle.createObject()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a8a64aeb6e0f8e7d9036f7b1b795c3567),
[draftgeoutils.geometry.findDistance()](../../d9/dfd/group__draftgeoutils.html#gadb5e321267b39af75b106d101359e2ca),
[draftfunctions.svg.format_point()](../../d2/d57/group__draftfunctions.html#ga8f27938b7ca9e7515f875ef70690525a),
[importIFCHelper.get2DShape()](../../d6/d78/namespaceimportIFCHelper.html#a5604c6416a97e1beb1dc51b7ee69822b),
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5),
[Gui::PropertyEditor::RotationHelper.getAngle()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#a0d43932325b2af59c4ada6488039ada4),
[SMESH_MesherHelper.GetAngle()](../../db/dc6/classSMESH__MesherHelper.html#a80980a8d54347257b21672fac4f5d6c3),
[draftguitools.gui_trackers.arcTracker.getAngle()](../../da/d31/classdraftguitools_1_1gui__trackers_1_1arcTracker.html#a221bdf6365a43fc6c7b5f851b1d9b1dc),
[importDXF.getArcData()](../../d7/dbf/namespaceimportDXF.html#a4e379964eac7c45567318e781830a5b5),
[draftgeoutils.cuboids.getCubicDimensions()](../../d9/dfd/group__draftgeoutils.html#ga594409c27f69bd528d72d25ee42321ca),
[WorkingPlane.Plane.getDeviation()](../../d3/d93/classWorkingPlane_1_1Plane.html#a2ae22a5c95a907b888beaab5f220dcef),
[draftfunctions.svgshapes.getDiscretized()](../../d2/d57/group__draftfunctions.html#ga68258a215202f02c01dc3b0f47791ebf),
[importIFClegacy.getIfcExtrusionData()](../../db/d15/namespaceimportIFClegacy.html#a7889bb7a501c72e2d644331b90e0a16c),
[Part::Feature.getLocation()](../../d7/d7e/classPart_1_1Feature.html#a84164b4adfe9b6ecef87da8d7aa1ac9d),
[Part::FeatureReference.getLocation()](../../d2/da1/classPart_1_1FeatureReference.html#aee6f4d426e17d5a0193108fd06f7309c),
[App::PropertyPlacement.getPyPathValue()](../../da/d51/classApp_1_1PropertyPlacement.html#a462af42ef4eadd19ca7645e961432b1c),
[App::PropertyRotation.getPyPathValue()](../../df/d76/classApp_1_1PropertyRotation.html#ab180787d5004b7196676ba10863f49f5),
[exportIFC.getRepresentation()](../../d8/d5d/namespaceexportIFC.html#ab7e3a822724c9bbdbb26e769f5e89bef),
[TechDraw::DrawProjGroupItem.getRotateAngle()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a7089aa4623e73d602fe97394d22ac6de),
[FCSphereSheetProjector.getRotation()](../../d6/def/classFCSphereSheetProjector.html#ae1ed1f4b7796261aeef608558818c308),
[draftgeoutils.geometry.getRotation()](../../d9/dfd/group__draftgeoutils.html#ga8b265d6e556f0015d0e732088d6ad1bd),
[Part::TopoShape.getShapePlacement()](../../d8/ded/classPart_1_1TopoShape.html#ab7c6c6769583e8fb7c7a0d8129d52b8e),
[TechDraw::PATLineSpec.getSlope()](../../d0/d63/classTechDraw_1_1PATLineSpec.html#a527decccd6008cfaca86b2fc5ef1917c),
[importIFClegacy.getTuples()](../../db/d15/namespaceimportIFClegacy.html#a7fc42bf336f708c10ef39e50e781e6b1),
[PartGui.goDimensionAngularNoTask()](../../d5/d49/namespacePartGui.html#a22a4e967d614ba7959dc90e89f6e76dc),
[draftgeoutils.arcs.isClockwise()](../../d9/dfd/group__draftgeoutils.html#gacc819a72923773e1ec59cf14f2f87f78),
[draftmake.make_sketch.make_sketch()](../../d5/d7f/group__draftmake.html#gaaf5211b1c0c5f62d13897195ec2d1e6b),
[TechDrawGui::QGISectionLine.makeArrowsISO()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#a8f2cce08f6be3eb56a19c7de258ea884),
[TechDrawGui::QGISectionLine.makeArrowsTrad()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#aaa7b66291c65ca1fd3de5a83aa2cdf68),
[TechDraw::DrawGeomHatch.makeEdgeOverlay()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#ad42d700267fb44056f1c72515659170c),
[ArchRoof.makeRoof()](../../d4/d2a/namespaceArchRoof.html#ad19f0e53e9c0a79c7ac5d7cf86f73c65),
[TechDrawGui::QGISectionLine.makeSymbolsISO()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#ac20091d52978917cd18aa37c17df9d6c),
[TechDrawGui::QGISectionLine.makeSymbolsTrad()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#ad784a67840ecc73314d932f8c3f523d9),
[draftobjects.dimension.measure_two_obj_angles()](../../de/de1/group__draftobjects.html#ga857acaba699b33a174f5f634e3be6da2),
[PathScripts.PathJobGui.TaskPanel.modelSetAxis()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a4904ab5fadddc3d1a7ad649ccc132d00),
[draftgeoutils.edges.orientEdge()](../../d9/dfd/group__draftgeoutils.html#ga13b05c710ac80b4c3669ac1ae1529906),
[SketcherGui::EditModeConstraintCoinManager.processConstraints()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a86abd481aa8756c9ea61b10d2e624804),
[draftguitools.gui_trimex.Trimex.redraw()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a6c61910ba86ef48101475e9ecdd6f958),
[Part::Geometry.rotate()](../../dc/df0/classPart_1_1Geometry.html#a3c7ebf21592da6737fccb28bf9508a75),
[Import::ExportOCAF.saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[MeshCore::MeshOutput.SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
[Gui::PropertyEditor::RotationHelper.setAngle()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#a513883344181063d90dbd754039d33d3),
[Gui::PropertyEditor::RotationHelper.setAxis()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#a3b49948e5ac8d72ce290c36b98f94bc3),
[Part::TopoShape.setShapePlacement()](../../d8/ded/classPart_1_1TopoShape.html#a8ae38d04353d5ccc4c60beaad3a4a497),
[Gui::PropertyEditor::RotationHelper.setValue()](../../db/dbe/classGui_1_1PropertyEditor_1_1RotationHelper.html#a192d344ea0dbb102eae69b60a889045b),
[Gui::PropertyEditor::PropertyRotationItem.setValue()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a65660d1593a8c2f7dabca98e9464c6cc),
[Gui::PropertyEditor::PropertyPlacementItem.setValue()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a7f8e70acbf194633b6b3422b87a07ab3),
[TechDraw::DrawProjGroup.spin()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#ad43779ef237f0848e22c8b8e5a4184b6),
[Gui::PropertyEditor::PropertyRotationItem.toolTip()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#abbb3c671e82d0c8d54f1f6f2b95abe5d),
[Gui::PropertyEditor::PropertyPlacementItem.toolTip()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#add11217c79e909fa0d6a5fa97d739d2f),
[Gui::PropertyEditor::PropertyRotationItem.toString()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a13b41010f83aeb8833bf251d9f1a652a),
[Gui::PropertyEditor::PropertyPlacementItem.toString()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a4866bdcbed09d39f47781b1b5aba4cec),
[draftguitools.gui_trimex.Trimex.trimObjects()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a039209de5464aa216735c747791838b0),
[draftguitools.gui_edit_draft_objects.DraftCircleGuiTools.update_object_from_edit_points()](../../d6/dd2/classdraftguitools_1_1gui__edit__draft__objects_1_1DraftCircleGuiTools.html#ab007d40a588bd74cc48d7544b10f4602),
[Gui::PropertyEditor::PropertyRotationItem.value()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a863981824fc5e2a970540f4e707913d1),
[Gui::PropertyEditor::PropertyPlacementItem.value()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a02b71a4429874d510e780c4a2375a1be),
and
[Path::PathSegmentWalker.walk()](../../d0/d7b/classPath_1_1PathSegmentWalker.html#a2d2253be4424a16caf28ec136b658dc6).

## ◆ closest()

def DraftVecUtils.closest  | ( |  | _vector_ ,   
---|---|---|---  
|  |  | _vlist_ ,   
|  |  | _return_length_ = `False`  
| ) | |   
      
    
    Find the closest point to one point in a list of points (vectors).
    
    The scalar distance between the original point and one point in the list
    is calculated. If the distance is smaller than a previously calculated
    value, its index is saved, otherwise the next point in the list is tested.
    
    Parameters
    ----------
    vector: Base::Vector3
        The tested point or vector.
    
    vlist: list
        A list of points or vectors.
    
    return_length: bool, optional
        It defaults to `False`.
        If it is `True`, the value of the smallest distance will be returned.
    
    Returns
    -------
    int
        The index of the list where the closest point is found.
    
    int, float
        If `return_length` is `True`, it returns both the index
        and the length to the closest point.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by [Base::BoundBox3< _Precision
>.ClosestPoint()](../../d8/d12/classBase_1_1BoundBox3.html#a9f500110c95df8ca0b5e71e371d64149),
[draftgeoutils.intersections.connect()](../../d9/dfd/group__draftgeoutils.html#ga0b7c0fe418afd94ab4e966fe53b88960),
and
[draftguitools.gui_trimex.Trimex.trimObjects()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a039209de5464aa216735c747791838b0).

## ◆ dist()

def DraftVecUtils.dist  | ( |  | _u_ ,   
---|---|---|---  
|  |  | _v_  
| ) | |   
      
    
    Return the distance between two points (or vectors).
    
    Parameters
    ----------
    u : Base::Vector3
        First point, defined by a vector.
    v : Base::Vector3
        Second point, defined by a vector.
    
    Returns
    -------
    float
        The scalar distance from one point to the other.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[draftguitools.gui_arcs.Arc.action()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#ac0bc0c5e1181c3cb676f6056439c4197),
[draftguitools.gui_polygons.Polygon.action()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a55821ba30d78a07ea9fee61b97c5d052),
[CmdSketcherConstrainAngle.activated()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a0d48a74c0960a5a240c1a39137f070a3),
[CmdSketcherConstrainAngle.applyConstraint()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a5602881a59f6c0a0a83a30641560aeb7),
[Drawing::DrawingOutput.asCircle()](../../d0/d85/classDrawing_1_1DrawingOutput.html#a4b843b882da4d2963f480f5128e387fb),
[TechDraw::TechDrawOutput.asCircle()](../../d7/d9e/classTechDraw_1_1TechDrawOutput.html#aada6d1650cdf7e6b18014cfae625ab85),
[Attacher::AttachEngineLine.calculateAttachedPlacement()](../../dc/dd1/classAttacher_1_1AttachEngineLine.html#a7485dd5ab5a0c4259cf4a724738a475d),
[CArea.ChangeStartToNearest()](../../d3/d52/classCArea.html#a0ae370647b32e2ac47e5a668944207a5),
[StdMeshers_QuadToTriaAdaptor.CheckIntersection()](../../d3/d81/classStdMeshers__QuadToTriaAdaptor.html#a35567e2d36255376e85e173d845daa7a),
[SMESH_MesherHelper.CheckNodeU()](../../db/dc6/classSMESH__MesherHelper.html#a9fdb0f23cad6cec85fba477d01f08bd2),
[SMESH_MesherHelper.CheckNodeUV()](../../db/dc6/classSMESH__MesherHelper.html#a47b5e94e74687d6c596288e2c2f374e9),
[VISCOUS_3D::_LayerEdge.ChooseSmooFunction()](../../d9/df6/structVISCOUS__3D_1_1__LayerEdge.html#af3c5c13db9dc894fce734a830c8871d0),
[draftgeoutils.circles.circlefrom1Line2Points()](../../d9/dfd/group__draftgeoutils.html#ga62f4e19d1f4b45e85467ccefd5dd8a50),
[draftgeoutils.circles.circleFrom2PointsRadius()](../../d9/dfd/group__draftgeoutils.html#gac5ca6e04d961e3751606a1e4ccf378b4),
[draftgeoutils.circles.circleFromPointLineRadius()](../../d9/dfd/group__draftgeoutils.html#ga163b5f31d9b814e500670ab9cec198b5),
[draftgeoutils.circle_inversion.circleInversion()](../../d9/dfd/group__draftgeoutils.html#gaf83de47d0b318d570f1ca51dcc9cbefb),
[StdMeshers_QuadToTriaAdaptor.Compute()](../../d3/d81/classStdMeshers__QuadToTriaAdaptor.html#a666f2ab33b2cdfde11319df8d7ed066c),
[SMESH_Block.ComputeParameters()](../../d2/d98/classSMESH__Block.html#a9f4f9ebaf0496cca708a681c356bb96a),
[StdMeshers_Quadrangle_2D.computeQuadDominant()](../../d1/db4/classStdMeshers__Quadrangle__2D.html#a32366f3bed1dc62990f5f848f49115c9),
[ConstraintItem.data()](../../d3/d0f/classConstraintItem.html#a58e0ecc1824934b77e25bc0b319b6c51),
[geoff_geometry.Dist()](../../de/d5d/namespacegeoff__geometry.html#a3c3fdf494e81774d4b162888a616fed3),
[triplet.distance_to()](../../d0/dd3/structtriplet.html#aa7eca51b1b881b69909bd62dcf37f1e4),
[Base::Vector3< _Precision
>.DistanceToLineSegment()](../../d1/d13/classBase_1_1Vector3.html#afded3c26fdac4b7b199bcb0cc61d464f),
[GCS::ConstraintP2PDistance.error()](../../d5/d0e/classGCS_1_1ConstraintP2PDistance.html#ad2de62ce3e9519106f3316c52d04e43e),
[GCS::ConstraintP2LDistance.error()](../../da/d8d/classGCS_1_1ConstraintP2LDistance.html#a816c4745f305d010e77c6e513c1c2336),
[Mesh::SegmentByMesh.execute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#a0fd4604225620a5902f526c867f0a7ed),
[Sketcher::SketchObject.fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[TechDraw::DrawDimHelper.findClosestPoint()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#aaf687698d99b3e2c52eea1c773d28003),
[SMESH_ElementSearcherImpl.FindClosestTo()](../../dd/d4c/structSMESH__ElementSearcherImpl.html#af1de7930a1d320b6e48c65cc1ab0657b),
[VISCOUS_3D::_LayerEdge.FindIntersection()](../../d9/df6/structVISCOUS__3D_1_1__LayerEdge.html#a32897cfd9a14875af5bbd2de96eb40dc),
[MeshCore::MeshKDTree.FindNearest()](../../d2/d5b/classMeshCore_1_1MeshKDTree.html#a7c8783435614c6dff1f5c8eade97d52b),
[draftgeoutils.circles.findRadicalAxis()](../../d9/dfd/group__draftgeoutils.html#gace97041b9159300c6ca150e0373b274c),
[SMESH_Block.findUVAround()](../../d2/d98/classSMESH__Block.html#a692f591665fd66c82256241b80605d36),
[TechDraw::GeometryObject.findVertex()](../../dc/dbe/classTechDraw_1_1GeometryObject.html#aa66a1fc2774f07a54b99e2d31f14f5d7),
[lscmrelax.get_max_distance()](../../d6/d0e/namespacelscmrelax.html#a3802f4ba4ec96c01601fa68e18a0e2b9),
[Fem::Constraint.getBasePoint()](../../d0/d11/classFem_1_1Constraint.html#a53b58263b54f9ab82afbc002761ccd24),
[MeshCore::CylinderFit.GetBounding()](../../df/d1a/classMeshCore_1_1CylinderFit.html#a3734c42623f68d247d50773e242c5727),
[SMESH_MeshAlgos.GetDistance()](../../dd/d76/namespaceSMESH__MeshAlgos.html#a5823659eb0c933a35c2860b5a07eae14),
[MeshCore::CylinderSurfaceFit.GetDistanceToSurface()](../../d1/d68/classMeshCore_1_1CylinderSurfaceFit.html#ab17cc09afa4390ea5b1fa631b6f33e30),
[MeshCore::SphereSurfaceFit.GetDistanceToSurface()](../../d2/de9/classMeshCore_1_1SphereSurfaceFit.html#aab6a34ea0bdcfed273ad90fa3db4e37d),
[GEOMUtils.GetMinDistance()](../../db/daf/namespaceGEOMUtils.html#ac8ecbda28c300c94da6fc75c30808331),
[SMESH_MesherHelper.GetNodeUV()](../../db/dc6/classSMESH__MesherHelper.html#a6756f5d6f15c2cd7dbb65cf3dfc0ee7c),
[Gui::AxisOrigin.getPlane()](../../dd/de4/classGui_1_1AxisOrigin.html#a0bc449edd2127d462550d034cc0f8cbb),
[SandboxGui::SoWidgetShape.getQuad()](../../d6/dc7/classSandboxGui_1_1SoWidgetShape.html#a779ce69e92689d20914972b54e87b5e2),
[MeshCoreFit::CylinderFit.GetStdDeviation()](../../de/db8/classMeshCoreFit_1_1CylinderFit.html#a4293f1de728e3e86d79dd9b928d8a51f),
[MeshCoreFit::SphereFit.GetStdDeviation()](../../dd/d10/classMeshCoreFit_1_1SphereFit.html#a8cb03c62c6f269e2e54c0d7720553430),
[SMESH_ElementSearcherImpl.getTolerance()](../../dd/d4c/structSMESH__ElementSearcherImpl.html#af6e24c285b438e472605b72b7c804bb6),
[nlohmann::detail::dtoa_impl.grisu2_digit_gen()](../../dc/d41/namespacenlohmann_1_1detail_1_1dtoa__impl.html#a9b899c72b0e1e3dd46d75c2b4e6bcdfb),
[nlohmann::detail::dtoa_impl.grisu2_round()](../../dc/d41/namespacenlohmann_1_1detail_1_1dtoa__impl.html#a5bc841e0bee12fd6489d49cf7bd07bb4),
[draftguitools.gui_rotate.Rotate.handle_mouse_move_event()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a9bf281ceb1e44564a7740b5cd1b6261e),
[InspectionGui::ViewProviderInspection.inspectDistance()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac0352eb6e4af339e08975b253269b0ab),
[MeshCore::MeshGeomFacet.IsCoplanar()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a9fa0f20f53cf18d1ea9dcc51e3a38650),
[TechDraw::Vertex.isEqual()](../../dd/db1/classTechDraw_1_1Vertex.html#a568ae6efb7c2908c4ebc7fb01481663e),
[Fem::Tools.isLinear()](../../d3/d28/classFem_1_1Tools.html#affb9bf4553ad4a36918b3352d7e7d36f),
[TechDraw::DrawProjectSplit.isOnEdge()](../../d8/ded/classTechDraw_1_1DrawProjectSplit.html#a5b512ff511e727022201f489ac54672b),
[SMESH_MeshAlgos.IsOut()](../../dd/d76/namespaceSMESH__MeshAlgos.html#ac7d51627396929bdb66b3bfd642d1226),
[Fem::Tools.isPlanar()](../../d3/d28/classFem_1_1Tools.html#a02429bad48ad6a9e4cb6777b26fb7d7e),
[MeshCore::MeshGeomFacet.IsPointOfSphere()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#aed36d6e2670b5cf5c1083911b2252a09),
[VISCOUS_3D::_Curvature.lenDeltaByDist()](../../d0/d71/structVISCOUS__3D_1_1__Curvature.html#a090b8503840fb8093dde7ad62b8cc464),
[SMESH_Pattern.Load()](../../d0/d7d/classSMESH__Pattern.html#aada1481358a8eedfa7a175da392b9308),
[TechDrawGui::QGISectionLine.makeSymbolsISO()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#ac20091d52978917cd18aa37c17df9d6c),
[GCS::ConstraintP2PDistance.maxStep()](../../d5/d0e/classGCS_1_1ConstraintP2PDistance.html#aa2ed1ad7964cca954ebdb330119fedf9),
[CArea.NearestPoint()](../../d3/d52/classCArea.html#a22869874f09943893ea0d461bcac86e0),
[CCurve.NearestPoint()](../../da/ddb/classCCurve.html#a6174a87fd19bae383c2125fe211966ed),
[MeshCore::MeshNearestIndexToPlane< T
>.operator()()](../../da/df3/classMeshCore_1_1MeshNearestIndexToPlane.html#a74faa2862e3ed20716040ae5f35a5f26),
[geoff_geometry::Plane.Plane()](../../d6/de6/classgeoff__geometry_1_1Plane.html#acf4c6405448b6046b32d21572b4455d8),
[cLineSegment.PointAt()](../../dc/dff/structcLineSegment.html#aa6a58c2b15d8dd198b670addb98a3863),
[draftgeoutils.circle_inversion.pointInversion()](../../d9/dfd/group__draftgeoutils.html#ga2e9e5f6e50364165f9e6e1f8f5d5d8f8),
[CCurve.PointToPerim()](../../da/ddb/classCCurve.html#ae0fa734306fed71e78c4c18db44d1c9a),
[AdaptivePath.PopPathWithClosestPoint()](../../d5/d7f/namespaceAdaptivePath.html#a42481360e50af9d93ddfabe9d89bc66b),
[MeshCore::MeshOutput.SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
[SketcherGui::ViewProviderSketch.setEditViewer()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a7ecefc8f26a51435051a12a6fb73f333),
[SMESH_MeshEditor.SewFreeBorder()](../../da/d31/classSMESH__MeshEditor.html#a4ea2a113155223c7f98b40373e04e0d2),
[SMESH_MeshEditor.SewSideElements()](../../da/d31/classSMESH__MeshEditor.html#a4cd223989e2ce5af01f700a8c33cbbca),
[PathScripts.PathUtils.sort_locations()](../../dc/dea/namespacePathScripts_1_1PathUtils.html#a398148181ad2a1750b8b73ce56b06a17),
[Sketcher::SketchObject.split()](../../d9/dad/classSketcher_1_1SketchObject.html#ab73e7a53a704168c004b9aa6c9ad7a68),
and
[Gui::SoFCDB.writeToX3D()](../../d3/d6d/classGui_1_1SoFCDB.html#a74087449b07374d47d38f12a7d25a7f1).

## ◆ equals()

def DraftVecUtils.equals  | ( |  | _u_ ,   
---|---|---|---  
|  |  | _v_  
| ) | |   
      
    
    Check for equality between two vectors.
    
    Due to rounding errors, two vectors will rarely be `equal`.
    Therefore, this function checks that the corresponding elements
    of the two vectors differ by less than the decimal `precision` established
    in the parameter database, accessed through `FreeCAD.ParamGet()`.
    ::
        x1 - x2 < precision
        y1 - y2 < precision
        z1 - z2 < precision
    
    Parameters
    ----------
    u : Base::Vector3
        The first vector.
    v : Base::Vector3
        The second vector.
    
    Returns
    -------
    bool
        `True` if the vectors are within the precision, `False` otherwise.
    

References
[DraftVecUtils.isNull()](../../dc/dc3/group__DRAFTVECUTILS.html#gaaccdee2ed1226b010ac7b3e04c42a687),
and
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[WorkingPlane.Plane.alignToFace()](../../d3/d93/classWorkingPlane_1_1Plane.html#aac15aec2ff8ab925af8ff8d893c5486d),
[draftguitools.gui_trackers.dimTracker.calc()](../../d2/d2f/classdraftguitools_1_1gui__trackers_1_1dimTracker.html#a55b0af8e2e595d3cdf7d7129b8f3b7c0),
[draftgeoutils.circles.circleFrom2PointsRadius()](../../d9/dfd/group__draftgeoutils.html#gac5ca6e04d961e3751606a1e4ccf378b4),
[draftgeoutils.circles.circleFrom3LineTangents()](../../d9/dfd/group__draftgeoutils.html#gacc0f0f89c65bda5546b24a2513ed592c),
[draftgeoutils.circle_inversion.circleInversion()](../../d9/dfd/group__draftgeoutils.html#gaf83de47d0b318d570f1ca51dcc9cbefb),
[exportIFC.createCurve()](../../d8/d5d/namespaceexportIFC.html#a619ad8294a46ea5516667f513d04c003),
[importDXF.drawLine()](../../d7/dbf/namespaceimportDXF.html#ab2e149382ac3efb022359880f8cf1918),
[importDXF.drawPolyline()](../../d7/dbf/namespaceimportDXF.html#ae7f17585472e688a94e6b6b601f4d5b9),
[draftguitools.gui_lines.Line.drawSegment()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#ab56a5f53732aa9bc6cbe201b940f4790),
[draftgeoutils.general.edg()](../../d9/dfd/group__draftgeoutils.html#gad3f6b7a08027b908170525ef5b6da7fe),
[draftobjects.clone.Clone.execute()](../../df/d9d/classdraftobjects_1_1clone_1_1Clone.html#a989a485bf24e2e5e5faa1d70fc906646),
[draftobjects.patharray.PathArray.execute()](../../de/dbe/classdraftobjects_1_1patharray_1_1PathArray.html#a8b9f1d9f89824942906f0461df9b5b44),
[draftobjects.wire.Wire.execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[App::LinkBaseExtension.extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a),
[DraftVecUtils.find()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf764683bba7871d8f3d64db4fb2a41a9),
[draftgeoutils.edges.findEdge()](../../d9/dfd/group__draftgeoutils.html#gacde7110bb9761e0a00c4f3393181d1c7),
[draftgeoutils.circles.findHomotheticCenterOfCircles()](../../d9/dfd/group__draftgeoutils.html#ga8a2f5385b2e75457e5b317f7ba170816),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.circles.findRadicalAxis()](../../d9/dfd/group__draftgeoutils.html#gace97041b9159300c6ca150e0373b274c),
[draftgeoutils.wires.findWiresOld2()](../../d9/dfd/group__draftgeoutils.html#ga263bbbeab564aced2232f8134c17a7fb),
[draftobjects.patharray.get_parameter_from_v0()](../../de/de1/group__draftobjects.html#gaeb7ce8c2e2be91d5e3886ba93bad75c9),
[Gui::ViewProviderLink.getDetailPath()](../../d6/d59/classGui_1_1ViewProviderLink.html#a631a96d7ef6239aabe05c86cf3c20d31),
[App::LinkBaseExtension.getElementIndex()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a821848868bd4ad652e3d1b61fedd057b),
[importIFClegacy.getIfcExtrusionData()](../../db/d15/namespaceimportIFClegacy.html#a7889bb7a501c72e2d644331b90e0a16c),
[App::LinkBaseExtension.getOnChangeCopyObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a20adee6736980e9459b96c6306986d56),
[PartDesign::SubShapeBinder.getSubObject()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#afb7e01deac9646afcd5dc1b2aa07042b),
[draftgeoutils.wires.isReallyClosed()](../../d9/dfd/group__draftgeoutils.html#gaefe28a41fe05def007e8f1fd6247f247),
[draftgeoutils.edges.isSameLine()](../../d9/dfd/group__draftgeoutils.html#gab4ae86b3ec0b393f14d2cc9910ce7dbb),
[draftfunctions.join.join_two_wires()](../../d2/d57/group__draftfunctions.html#ga8b7573fa746b69be82d73768bb04a557),
[Gui::LinkView.linkGetDetailPath()](../../da/d11/classGui_1_1LinkView.html#ae5489d900837b0dca02cf4f610e8a2b0),
[draftmake.make_sketch.make_sketch()](../../d5/d7f/group__draftmake.html#gaaf5211b1c0c5f62d13897195ec2d1e6b),
[ArchFloor.makeFloor()](../../df/d16/namespaceArchFloor.html#a6c27d8dc5a92ad8079677e720e783191),
[draftguitools.gui_arcs.Arc.numericRadius()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a3a55830e1e08f60be95ed81d73759e52),
[draftgeoutils.circle_inversion.pointInversion()](../../d9/dfd/group__draftgeoutils.html#ga2e9e5f6e50364165f9e6e1f8f5d5d8f8),
[DraftVecUtils.removeDoubles()](../../dc/dc3/group__DRAFTVECUTILS.html#ga7d65c2df29e414c0ca1ad2c8fd34c3b7),
and
[draftguitools.gui_snapper.Snapper.snapToCrossExtensions()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#acee40380387892206a064e5b4b878275).

## ◆ find()

def DraftVecUtils.find  | ( |  | _vector_ ,   
---|---|---|---  
|  |  | _vlist_  
| ) | |   
      
    
    Find a vector in a list of vectors, and return the index.
    
    Finding a vector tests for `equality` which depends on the `precision`
    parameter in the parameter database.
    
    Parameters
    ----------
    vector : Base::Vector3
        The tested vector.
    vlist : list
        A list of Base::Vector3 vectors.
    
    Returns
    -------
    int
        The index of the list where the vector is found,
        or `None` if the vector is not found.
    
    See Also
    --------
    equals : test for equality between two vectors
    

References
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
and
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[Gui::Dialog::DlgCreateNewPreferencePackImp.accept()](../../d8/d9e/classGui_1_1Dialog_1_1DlgCreateNewPreferencePackImp.html#a3f8567c6cb8c4e4f03824fe6373aa436),
[StdCmdOpen.activated()](../../d8/d6a/classStdCmdOpen.html#a9c9f69468076298c2a265906b3594a9d),
[Gui::Translator.activateLanguage()](../../de/db4/classGui_1_1Translator.html#a6466c42d9fdc2e586bb1e255792bf45a),
[Sketcher::SketchObject.addCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#a2ae92a618d60a264ed20d7a359b89f98),
[SMESHDS_Mesh.AddHypothesis()](../../d5/dbd/classSMESHDS__Mesh.html#ad9a00cb4ade512025edeb42b659f8de4),
[Gui::ViewProviderVRMLObject.addResource()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a90119133e310080de7e7ba113e5c4ea8),
[Sketcher::SketchObject.addSymmetric()](../../d9/dad/classSketcher_1_1SketchObject.html#afcbb1d6f5a99e52a70fdf6d9d3c9d361),
[Gui::HistoryList.append()](../../d6/ddd/classGui_1_1HistoryList.html#a4e1f4b72fc03a75d4dec0f43b6a32c53),
[PointsGui::ViewProviderScattered.attach()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#ab6910e935629c8fe18fed5409c9521a0),
[PointsGui::ViewProviderStructured.attach()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#aabe6e709079ef4dd2d44b687db5f1dd7),
[Gui::Dialog::DlgSettingsLazyLoadedImp.buildUnloadedWorkbenchList()](../../de/d4f/classGui_1_1Dialog_1_1DlgSettingsLazyLoadedImp.html#acc1e36963dc7e364ffc50df9ea31080a),
[NETGENPlugin_NETGEN_2D3D.CheckHypothesis()](../../dc/dd1/classNETGENPlugin__NETGEN__2D3D.html#af15f32195773990ac5d81198d90c8e7b),
[draftgeoutils.faces.cleanFaces()](../../d9/dfd/group__draftgeoutils.html#gadc094c875468b72613ed04077996cc56),
[TechDraw::DrawViewSpreadsheet.colInList()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#ad044b61c0ad8258423ebb75e3a3ebc3f),
[MeshCore::MeshTopoAlgorithm.CollapseEdge()](../../d6/d22/classMeshCore_1_1MeshTopoAlgorithm.html#af7ce97fec748badc748e22dda224727e),
[MeshCore::MeshTopoAlgorithm.CollapseVertex()](../../d6/d22/classMeshCore_1_1MeshTopoAlgorithm.html#a611a35a28b2130f11e51115137ca97d4),
[StdMeshers_Projection_2D.Compute()](../../d5/daf/classStdMeshers__Projection__2D.html#a14cb61d65b34cd86526725ea5eb7d96b),
[StdMeshers_Regular_1D.Compute()](../../df/d00/classStdMeshers__Regular__1D.html#a076e79df9dadc31f36b1975ee8120d62),
[SMESH_ProxyMesh::SubMesh.Contains()](../../d4/d21/classSMESH__ProxyMesh_1_1SubMesh.html#aa689963302f7cc12e80344e692228230),
[Sketcher::SketchObject.delGeometries()](../../d9/dad/classSketcher_1_1SketchObject.html#a24b86dbe8a4d56cfa90fb523f4afbcb1),
[Gui::Document.detachView()](../../de/d4e/classGui_1_1Document.html#a320afb4cc20d4c593cbe18accc44e3e5),
[PartGui::DlgPrimitives.DlgPrimitives()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a27827c66a9f047547fe0b7169251b97d),
[TechDrawGui::QGIViewClip.drawClip()](../../d4/dcc/classTechDrawGui_1_1QGIViewClip.html#a272bbbc60a11ba7d9c687cff260df23d),
[SketcherGui::EditModeCoinManager.drawEditMarkers()](../../de/dc2/classSketcherGui_1_1EditModeCoinManager.html#a04eeda638bc67ed5298a6ebcbd6bc002),
[KDTree::KDTree< __K, _Val, _Acc, _Dist, _Cmp, _Alloc
>.erase()](../../d2/d4c/classKDTree_1_1KDTree.html#a75f3cc0a9eb575a99f9ae451d5839bde),
[Drawing::FeatureViewSpreadsheet.execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Fem::FemPostScalarClipFilter.execute()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a0aa1f4898cacdd829920492771a3931b),
[Fem::FemPostWarpVectorFilter.execute()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#abfd97dfc34d290355149f487d5c93f66),
[App::Document.exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
[App::PropertyLinkList.find()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa04ccf0ffcdd71c616504fc836bacf9b),
[App::DocumentP.findAllPathsAt()](../../d1/da5/structApp_1_1DocumentP.html#a028ece0723e817ca53c9b27ac1d3b555),
[StdMeshers_ProjectionUtils.FindFaceAssociation()](../../d2/d9a/namespaceStdMeshers__ProjectionUtils.html#a879fcfcb260227cb7a7086122f8bcb90),
[Gui::DocumentItem.findItem()](../../df/d15/classGui_1_1DocumentItem.html#ac20f1bb6efdbc301be559e6a0260ca28),
[SMESH_HypoFilter::IsMoreLocalThanPredicate.findPreferable()](../../df/d65/structSMESH__HypoFilter_1_1IsMoreLocalThanPredicate.html#ae04b42b9fd8f40a35f4b7133b04ab47e),
[MeshCore::MeshSurfaceSegment.FindSegment()](../../d8/dcb/classMeshCore_1_1MeshSurfaceSegment.html#ac85f90897aa955bb5b9f1947d9c59367),
[MeshCore::MeshPointArray.Get()](../../db/d5c/classMeshCore_1_1MeshPointArray.html#a9fbc369d6c4f8212881da1f2b2e4b2ca),
[Fem::FemMesh.getccxVolumesByFace()](../../d3/d2e/classFem_1_1FemMesh.html#afbf000dd38c7bb08c0a21d27813c0770),
[PartDesign::DressUp.getContinuousEdges()](../../df/de5/classPartDesign_1_1DressUp.html#aa86571be903ef7877081417df55d7b36),
[StdMeshers_CompositeSegment_1D.GetFaceSide()](../../d6/d55/classStdMeshers__CompositeSegment__1D.html#ab7e6e7e535d4d0a1bc3c7956eab56c43),
[MeshCore::MeshEvalTopology.GetFacetManifolds()](../../db/d16/classMeshCore_1_1MeshEvalTopology.html#a12ee41e4a129bb5069ffa325f97d6242),
[Gui::ExpressionBinding.getIcon()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a8bd7d65253e833ce9e8af7e39a1fade6),
[ExpressionDelegate.getIcon()](../../d1/df5/classExpressionDelegate.html#aac6202673cbdc7ec1198731ffbc09276),
[SketcherGui::CoinMapping.getIndexLayer()](../../d5/de5/structSketcherGui_1_1CoinMapping.html#a11c9a38fa8d6d35390fbdb0c6560f04e),
[Gui::ViewProviderVRMLObject.getLocalResources()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#aa0fe6cef5a3c60180ab22ad678ab7b2b),
[PartDesign::Body.getNextSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#a0c9db11c1cca8a2a0c7247d7d3498242),
[App::Document.getPathsByOutList()](../../d8/d3e/classApp_1_1Document.html#a6c4fd3b7f7700be4e25980669d35a108),
[PartDesign::Body.getPrevSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#aface61e57526fc0ce72faff92c3e0841),
[importIFClegacy.IfcEntity.getProperties()](../../d0/df2/classimportIFClegacy_1_1IfcEntity.html#aa57d8841d195c0c50014568479330ffd),
[importIFClegacy.IfcEntity.getProperty()](../../d0/df2/classimportIFClegacy_1_1IfcEntity.html#ac6c54d841f3a19e8ef5842f30c3d15ed),
[TechDraw::DrawViewSpreadsheet.getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[DriverMED.GetSMDSType()](../../db/d95/namespaceDriverMED.html#a6232c777ec5c553af525cff22a98c084),
[Base::Writer.getUniqueFileName()](../../dd/d4d/classBase_1_1Writer.html#a5f42876fd6d991fd34f2de3ca657f9cc),
[App::Branding.getUserDefines()](../../df/d1b/classApp_1_1Branding.html#ac0c27f384850dca5f455d86e8e8b077b),
[Spreadsheet::PropertyColumnWidths.getValue()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a8393e3b196de4f09417183dfbffdf28d),
[Spreadsheet::PropertyRowHeights.getValue()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#adb9db6c35c8d222c8ba9f33d3c5bd370),
[Sketcher::GeoListModel< T
>.getVertexIdFromGeoElementId()](../../df/d90/classSketcher_1_1GeoListModel.html#a9432170ae1a545bb15b81750d09c1055),
[App::Origin.hasObject()](../../d9/d8b/classApp_1_1Origin.html#afd6b442d0bd144e6389fee183c41fc94),
[Gui::PropertyEditor::PropertyItem.hasProperty()](../../d6/db3/classGui_1_1PropertyEditor_1_1PropertyItem.html#a47a27004aa0553b440c34055eaf269b0),
[PartDesign::Body.insertObject()](../../dd/db8/classPartDesign_1_1Body.html#a5cbb7aa1f902c8b111a9c9a428072c09),
[Part::BodyBase.isAfter()](../../da/dc8/classPart_1_1BodyBase.html#a9a200c47ffd7f95eb5584fd6bf54dfe3),
[PartDesignGui.isAnyNonPartDesignLinksTo()](../../dc/d12/namespacePartDesignGui.html#a763622795328f1193ce61804dc4c61b6),
[StdMeshers_Prism_3D.IsApplicable()](../../dd/d6d/classStdMeshers__Prism__3D.html#aebf97e723b5e6c64d48bec03c6ee1028),
[SMDS_VolumeTool.IsLinked()](../../da/d22/classSMDS__VolumeTool.html#a8787b34561db079ad204610952e3d17d),
[Gui::ProgressBarPrivate.isModalDialog()](../../d9/dc4/structGui_1_1ProgressBarPrivate.html#aae5a6a30b5334b94b6f04a1ba94538d5),
[Gui::WaitCursorP.isModalDialog()](../../d3/d9f/classGui_1_1WaitCursorP.html#a6a7d3a250e44671fee7b507b51e1e63c),
[SMESH_Mesh.IsOrderOK()](../../d5/d97/classSMESH__Mesh.html#a7e6c1a10e1a8ceb4b80818b963b3e1a1),
[StdMeshers_ViscousLayers.IsShapeWithLayers()](../../da/d03/classStdMeshers__ViscousLayers.html#a0964ff5d5cf71baa9cd499bcaffa5617),
[SMESHDS_Mesh.IsUsedHypothesis()](../../d5/dbd/classSMESHDS__Mesh.html#aa9bfa09c76c069b4cdf06bc53d1cde25),
[SMESH_Mesh.IsUsedHypothesis()](../../d5/d97/classSMESH__Mesh.html#abaf5ab12bf4c4b6f89cf8a241f876adb),
[SMESH_Block.LoadMeshBlock()](../../d2/d98/classSMESH__Block.html#ad1e63d85c92eff7a9c145d370f26b0cb),
[SMESH_ProxyMesh.NbFaces()](../../dd/d21/classSMESH__ProxyMesh.html#a1a53593a58ad6ec9d59b80b57c934c62),
[SMESH_Mesh.NotifySubMeshesHypothesisModification()](../../d5/d97/classSMESH__Mesh.html#aa7a0056b3d73d69b53b84e3cccacb466),
[PartDesignGui::TaskBooleanParameters.onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[PartDesignGui::TaskTransformedParameters.originalSelected()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#adb918122e8572632cc17114506d98ccd),
[PathScripts.post.marlin_post.parse()](../../df/d59/namespacePathScripts_1_1post_1_1marlin__post.html#a964a6c9dc88ecb8c410d6d592e8a79dc),
[PathScripts.post.rrf_post.parse()](../../d3/de0/namespacePathScripts_1_1post_1_1rrf__post.html#af71b1776a683369c06e8a2976f92c639),
[Points::PlyReader.read()](../../d4/d25/classPoints_1_1PlyReader.html#a7b8432b5da0356d2fc4269c5a926ae94),
[Points::PcdReader.read()](../../d1/da3/classPoints_1_1PcdReader.html#ab7ee26c11617aff96332fdd092ebe0e7),
[gzip_utf8.GzipFile.readline()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a17112c17fb6431a0d56b0108931c73e0),
[Gui::Dialog::DocumentRecoveryPrivate.readXmlFile()](../../db/dab/classGui_1_1Dialog_1_1DocumentRecoveryPrivate.html#a3c2d7b73614f4e29aaf9fd45cf61a6cc),
[PartDesignGui::TaskDressUpParameters.referenceSelected()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a4cbc9c9a3ab11fc80333ddf36ad442aa),
[PartDesignGui::TaskPipeParameters.referenceSelected()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a0c0361901e8218cb0848f5c13d58bb3d),
[PartDesignGui::TaskPipeOrientation.referenceSelected()](../../d8/df3/classPartDesignGui_1_1TaskPipeOrientation.html#a37effe2b23a30b99a63c7184b2175f21),
[PartDesignGui::TaskPipeScaling.referenceSelected()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#ac9f1c0754a7abf2a4e59c0218c73829a),
[PartDesignGui::TaskShapeBinder.referenceSelected()](../../d0/d2a/classPartDesignGui_1_1TaskShapeBinder.html#a4821e3f83b3b3cccc89fc2da1b7cd441),
[GCS::System.removeConstraint()](../../db/d28/classGCS_1_1System.html#ae27709cb985f7587a874a5848750172a),
[SMESHDS_Mesh.RemoveHypothesis()](../../d5/dbd/classSMESHDS__Mesh.html#a96cde4433ea5bb0852dc0899d0847bc1),
[Base::SequencerP.removeInstance()](../../d1/dd0/structBase_1_1SequencerP.html#a294b0ebb9f3c4644a65fe2df79c9ed70),
[PartDesign::Body.removeObject()](../../dd/db8/classPartDesign_1_1Body.html#a207956cf2a361690d971c7e604fc8bf1),
[Gui::PropertyEditor::PropertyEditor.removeProperty()](../../d5/d10/classGui_1_1PropertyEditor_1_1PropertyEditor.html#a1c19235c643097df71c3e8aa217313b6),
[Gui::PropertyEditor::PropertyItem.removeProperty()](../../d6/db3/classGui_1_1PropertyEditor_1_1PropertyItem.html#a6b17adb4278055aadd51378a91abc293),
[StdMeshers_ViscousLayers2D.RestoreListeners()](../../dc/d19/classStdMeshers__ViscousLayers2D.html#ad9b466b23ac8936ca61c97fd86bcaeb3),
[MeshCore::MeshOutput.SaveOBJ()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3d771358cea3ae77d666c54aba2692b5),
[Gui::Document.setActiveWindow()](../../de/d4e/classGui_1_1Document.html#ab7ad944368ddb1220919c088f87e32bb),
[StdMeshers_ProjectionUtils.SetEventListener()](../../d2/d9a/namespaceStdMeshers__ProjectionUtils.html#aea13495c86d91ead38084fa893720f2a),
[App::LinkBaseExtension.setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4),
[PartGui::DlgFilletEdges.setupFillet()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a1276cdf00c4f3436317932a8da913a5e),
[App::PropertyString.setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[Gui::Application.sGetMarkerIndex()](../../d9/da8/classGui_1_1Application.html#ac0d20b8eb675a3b6be74823f114dd3f7),
[FaceQuadStruct.shift()](../../d4/d10/structFaceQuadStruct.html#adf3c293dfbd9f961f0657b9142c6f591),
[PartDesignGui::TaskFeaturePick.slotDeletedObject()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a7ec2ecffd81993de90d27271f43e9a85),
[SMESH_Mesh.SortByMeshOrder()](../../d5/d97/classSMESH__Mesh.html#ade08e34b1c70fa0c5b17962ced53d19a),
[ArchRebar.strprocessOfCustomSpacing()](../../dd/de9/namespaceArchRebar.html#ae1155c41fe683f641981ee4bb70c494f),
[Gui::SelectionFilter.test()](../../d3/de7/classGui_1_1SelectionFilter.html#a5e11b2a1c8e404cf6236ee475fe5e0dc),
[VISCOUS_3D.ToClearSubWithMain()](../../d6/d23/namespaceVISCOUS__3D.html#ab04321b76ceff40044ad8a6f78cb59f2),
[App::Origin.unsetupObject()](../../d9/d8b/classApp_1_1Origin.html#ace2a648f85e06a55346df50a6fad40fe),
and
[SketcherGui::TaskDlgEditSketch.~TaskDlgEditSketch()](../../d3/dcd/classSketcherGui_1_1TaskDlgEditSketch.html#a9e18b97ae79b0928a429ead3ef7aad5c).

## ◆ get_cartesian_coords()

def DraftVecUtils.get_cartesian_coords  | ( |  | _radius_ ,   
---|---|---|---  
|  |  | _theta_ ,   
|  |  | _phi_  
| ) | |   
      
    
    Get the three-dimensional Cartesian coordinates of the vector
    represented by Spherical coordinates (radius, theta, phi).
    
    Parameters
    ----------
    radius : float, int
        Radial coordinate of the vector.
    theta : float, int
        Polar coordinate of the vector in radians.
    phi : float, int
        Azimuthal coordinate of the vector in radians.
    
    Returns
    -------
    tuple of float :
        Tuple (x, y, z) with the Cartesian coordinates.
    

Referenced by
[DraftGui.DraftToolBar.update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
and
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0).

## ◆ get_spherical_coords()

def DraftVecUtils.get_spherical_coords  | ( |  | _x_ ,   
---|---|---|---  
|  |  | _y_ ,   
|  |  | _z_  
| ) | |   
      
    
    Get the Spherical coordinates of the vector represented
    by Cartesian coordinates (x, y, z).
    
    Parameters
    ----------
    vector : Base::Vector3
        The input vector.
    
    Returns
    -------
    tuple of float
        Tuple (radius, theta, phi) with the Spherical coordinates.
        Radius is the radial coordinate, theta the polar angle and
        phi the azimuthal angle in radians.
    
    Notes
    -----
    The vector (0, 0, 0) has undefined values for theta and phi, while
    points on the z axis has undefined value for phi. The following
    conventions are used (useful in DraftToolBar methods):
    (0, 0, 0) -> (0, pi/2, 0)
    (0, 0, z) -> (radius, theta, 0)
    

Referenced by
[DraftGui.DraftToolBar.displayPoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ab9273fdf843210eaac76d6c00be3a658),
and
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0).

## ◆ getPlaneRotation()

def DraftVecUtils.getPlaneRotation  | ( |  | _u_ ,   
---|---|---|---  
|  |  | _v_ ,   
|  |  | _w_ = `None`  
| ) | |   
      
    
    Return a rotation matrix defining the (u,v,w) coordinate system.
    
    The rotation matrix uses the elements from each vector.
    ::
            (u.x  v.x  w.x  0  )
        R = (u.y  v.y  w.y  0  )
            (u.z  v.z  w.z  0  )
            (0    0    0    1.0)
    
    Parameters
    ----------
    u : Base::Vector3
        The first vector.
    v : Base::Vector3
        The second vector.
    w : Base::Vector3, optional
        The third vector. It defaults to `None`, in which case
        it is calculated as the cross product of `u` and `v`.
        ::
            w = u.cross(v)
    
    Returns
    -------
    Base::Matrix4D
        The new rotation matrix defining a new coordinate system,
        or `None` if `u`, or `v`, is `None`.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[importDXF.drawEllipse()](../../d7/dbf/namespaceimportDXF.html#a75596d1e9323dbe898137ab768337c56),
[importIFClegacy.getPlacement()](../../db/d15/namespaceimportIFClegacy.html#ae8eaa56d4100fee463010af3a0f9706a),
[importIFCHelper.getPlacement()](../../d6/d78/namespaceimportIFCHelper.html#ae9359911138ccf673190c0d606f4ef99),
and
[WorkingPlane.Plane.getRotation()](../../d3/d93/classWorkingPlane_1_1Plane.html#aa6f928c6a6a4719ea9c699e7a9a3a77b).

## ◆ getRotation()

def DraftVecUtils.getRotation  | ( |  | _vector_ ,   
---|---|---|---  
|  |  | _reference_ = `Vector(1, 0, 0)`  
| ) | |   
      
    
    Return a quaternion rotation between a vector and a reference.
    
    If the reference is omitted, the +X axis is used.
    
    Parameters
    ----------
    vector : Base::Vector3
        The original vector.
    reference : Base::Vector3, optional
        The reference vector. It defaults to `(1, 0, 0)`, the +X axis.
    
    Returns
    -------
    (x, y, z, Q)
        A tuple with the unit elements (normalized) of the cross product
        between the `vector` and the `reference`, and a `Q` value,
        which is the sum of the products of the magnitudes,
        and of the dot product of those vectors.
        ::
            Q = |A||B| + |A||B| cos(angle)
    
        It returns `(0, 0, 0, 1.0)`
        if the cross product between the `vector` and the `reference`
        is null.
    
    See Also
    --------
    rotate2D, rotate
    

References
[DraftVecUtils.isNull()](../../dc/dc3/group__DRAFTVECUTILS.html#gaaccdee2ed1226b010ac7b3e04c42a687).

## ◆ isColinear()

def DraftVecUtils.isColinear  | ( |  | _vlist_| ) |   
---|---|---|---|---|---  
      
    
    Check if the vectors in the list are colinear.
    
    Colinear vectors are those whose angle between them is zero.
    
    This function tests for colinearity between the difference
    of the first two vectors, and the difference of the nth vector with
    the first vector.
    ::
        vlist = [a, b, c, d, ..., n]
    
        k = b - a
        k2 = c - a
        k3 = d - a
        kn = n - a
    
    Then test
    ::
        angle(k2, k) == 0
        angle(k3, k) == 0
        angle(kn, k) == 0
    
    Parameters
    ----------
    vlist : list
        List of Base::Vector3 vectors.
        At least three elements must be present.
    
    Returns
    -------
    bool
        `True` if the vector differences are colinear,
        or if the list only has two vectors.
        `False` otherwise.
    
    Notes
    -----
    Due to rounding errors, the angle may not be exactly zero;
    therefore, it rounds the angle by the number
    of decimals specified in the `precision` parameter
    in the parameter database, and then compares the value to zero.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[importDXF.drawPolyline()](../../d7/dbf/namespaceimportDXF.html#ae7f17585472e688a94e6b6b601f4d5b9).

## ◆ isNull()

def DraftVecUtils.isNull  | ( |  | _vector_| ) |   
---|---|---|---|---|---  
      
    
    Return False if each of the components of the vector is zero.
    
    Due to rounding errors, an element is probably never going to be
    exactly zero. Therefore, it rounds the element by the number
    of decimals specified in the `precision` parameter
    in the parameter database, accessed through `FreeCAD.ParamGet()`.
    It then compares the rounded numbers against zero.
    
    Parameters
    ----------
    vector : Base::Vector3
        The tested vector.
    
    Returns
    -------
    bool
        `True` if each of the elements is zero within the precision.
        `False` otherwise.
    

Referenced by
[draftguitools.gui_arcs.Arc.action()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#ac0bc0c5e1181c3cb676f6056439c4197),
[draftguitools.gui_polygons.Polygon.action()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a55821ba30d78a07ea9fee61b97c5d052),
[importDXF.addText()](../../d7/dbf/namespaceimportDXF.html#a9542af2528d721e677018e7705990190),
[draftgeoutils.general.areColinear()](../../d9/dfd/group__draftgeoutils.html#ga9f5ec2b0065bccf89ab1700b8aebe673),
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
[importDXF.calcBulge()](../../d7/dbf/namespaceimportDXF.html#a21cae0153b98f5e461fbf777d07a2a9d),
[ArchVRM.Renderer.compare()](../../d5/dfd/classArchVRM_1_1Renderer.html#a78f4e0b92707209bcfeb72db372e044a),
[draftguitools.gui_stretch.Stretch.doStretch()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#ad50fddc20a1db1ac28f2b7dabd455dfc),
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
[draftobjects.shape2dview.Shape2DView.execute()](../../dc/d42/classdraftobjects_1_1shape2dview_1_1Shape2DView.html#ad34e4d7707f7c6f8cc23e61bc7082e97),
[ArchRoof.find_inters()](../../d4/d2a/namespaceArchRoof.html#ad6c2764c962fd9e59c8b69fabc16a529),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftfunctions.dxf.get_dxf()](../../d2/d57/group__draftfunctions.html#ga90ba94edeb5cbf46870b8d1b10c2fa81),
[draftgeoutils.circles.getCircleFromSpline()](../../d9/dfd/group__draftgeoutils.html#gacde5b7f0b59d56ae852c77f40889913e),
[exportIFC.getRepresentation()](../../d8/d5d/namespaceexportIFC.html#ab7e3a822724c9bbdbb26e769f5e89bef),
[DraftVecUtils.getRotation()](../../dc/dc3/group__DRAFTVECUTILS.html#gabde55e892e8108caa17c42ac86560b6f),
[draftguitools.gui_rotate.Rotate.handle_mouse_move_event()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a9bf281ceb1e44564a7740b5cd1b6261e),
[draftgeoutils.arcs.isClockwise()](../../d9/dfd/group__draftgeoutils.html#gacc819a72923773e1ec59cf14f2f87f78),
[ArchFrame.makeFrame()](../../d8/db6/namespaceArchFrame.html#a43a080855e00e52afc61334b48c48290),
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d),
[draftobjects.array.polar_placements()](../../de/de1/group__draftobjects.html#ga74bc873095b07ddb71d854a00b109b61),
[ArchWindow.recolorize()](../../d3/db7/namespaceArchWindow.html#a8a46c0e437e0f7099531f4bf88290aed),
[ArchSpace.removeSpaceBoundaries()](../../d8/d6a/namespaceArchSpace.html#aca020b8800ac48fabbf4fce2a0f16cee),
[draftguitools.gui_snapper.Snapper.snapToExtensions()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ae1f59975a9ed59a52c5c72b11a89e8c3),
[draftguitools.gui_snapper.Snapper.snapToPolar()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a5a30c9877875867157703325b090e21f),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.updateData()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a4c05a27ed86505f250f2efe7bac7967f),
and
[draftviewproviders.view_wire.ViewProviderWire.updateData()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a593b4fb5aed224be64e186060dc0b79a).

## ◆ neg()

def DraftVecUtils.neg  | ( |  | _u_| ) |   
---|---|---|---|---|---  
      
    
    Return the negative of a given vector.
    
    Parameters
    ----------
    u : Base::Vector3
        A FreeCAD.Vector.
    
    Returns
    -------
    Base::Vector3
        A vector in which each element has the opposite sign of
        the original element.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[ArchPanel.PanelView.execute()](../../dd/da0/classArchPanel_1_1PanelView.html#a3115adf9c7b5bc6fd6e2305d2b34e19f),
[importIFClegacy.getIfcBrepFacesData()](../../db/d15/namespaceimportIFClegacy.html#a0376ef062387284a7df3e985e46ba8fa),
[exportIFC.getRepresentation()](../../d8/d5d/namespaceexportIFC.html#ab7e3a822724c9bbdbb26e769f5e89bef),
[ArchStairs.makeRailing()](../../dc/d06/namespaceArchStairs.html#a37c92f2db600fd86adc3ac386c6fa211),
[Fem::ConstraintPulley.onChanged()](../../d3/dec/classFem_1_1ConstraintPulley.html#a6c23af9b8ba29b03f25163da9b75a41f),
and
[Base::Rotation.slerp()](../../d4/d18/classBase_1_1Rotation.html#ad8eeefc5709d927b052bf0199c49be3c).

## ◆ precision()

def DraftVecUtils.precision  | ( | | ) |   
---|---|---|---|---  
      
    
    Get the number of decimal numbers used for precision.
    
    Returns
    -------
    int
        Return the number of decimal places set up in the preferences,
        or a standard value (6), if the parameter is missing.
    

Referenced by
[ArchVRM.Renderer.getPathData()](../../d5/dfd/classArchVRM_1_1Renderer.html#aa3913ebcc8242d58d7bad0d885cbca09),
and
[WorkingPlane.Plane.projectPointOld()](../../d3/d93/classWorkingPlane_1_1Plane.html#a8371ff42986f6bc3a4747b1281ff83b9).

## ◆ project()

def DraftVecUtils.project  | ( |  | _u_ ,   
---|---|---|---  
|  |  | _v_  
| ) | |   
      
    
    Project the first vector onto the second one.
    
    The projection is just the second vector scaled by a factor.
    This factor is the dot product divided by the square
    of the second vector's magnitude.
    ::
        f = A * B / |B|**2 = |A||B| cos(angle) / |B|**2
        f = |A| cos(angle)/|B|
    
    Parameters
    ----------
    u : Base::Vector3
        The first vector.
    v : Base::Vector3
        The second vector.
    
    Returns
    -------
    Base::Vector3
        The new vector, which is the same vector `v` scaled by a factor.
        Return `Vector(0, 0, 0)`, if the magnitude of the second vector
        is zero.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[draftguitools.gui_arcs.Arc.action()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#ac0bc0c5e1181c3cb676f6056439c4197),
[draftguitools.gui_dimensions.Dimension.action()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a96494d2774d1c1c9b0973c27fa7e37d2),
[draftguitools.gui_polygons.Polygon.action()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a55821ba30d78a07ea9fee61b97c5d052),
[StdCmdMergeProjects.activated()](../../dc/d16/classStdCmdMergeProjects.html#a4044e49d39d63eb5cf4ee3885609642a),
[ArchSectionPlane.closeViewer()](../../d8/d49/namespaceArchSectionPlane.html#aa159e2389526d677138c754c18152c1c),
[ArchVRM.Renderer.compare()](../../d5/dfd/classArchVRM_1_1Renderer.html#a78f4e0b92707209bcfeb72db372e044a),
[draftguitools.gui_snapper.Snapper.constrain()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a3ebf277a348cf5e8228460beb63d2583),
[draftguitools.gui_ellipses.Ellipse.createObject()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#a45e8f0dc8ce41d63c874cf79bc6807bd),
[draftguitools.gui_rectangles.Rectangle.createObject()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a8a64aeb6e0f8e7d9036f7b1b795c3567),
[draftgeoutils.geometry.findDistance()](../../d9/dfd/group__draftgeoutils.html#gadb5e321267b39af75b106d101359e2ca),
[draftfunctions.svgshapes.get_proj()](../../d2/d57/group__draftfunctions.html#ga6c24cc9f0e4e0ebdafffbfc582db0c2e),
[draftguitools.gui_selectplane.Draft_SelectPlane.getCenterPoint()](../../dc/d53/classdraftguitools_1_1gui__selectplane_1_1Draft__SelectPlane.html#a5166200cf411a6092fd2e1c5046dc1fc),
[ArchSectionPlane.getCoinSVG()](../../d8/d49/namespaceArchSectionPlane.html#ad78e5453cf2b7d1746bf6520f9b9018a),
[ArchCommands.getCutVolume()](../../d4/d52/namespaceArchCommands.html#aa9bddbee3691ffd7b3cba2f35e55ce77),
[StdMeshers_Quadrangle_2D.getEnforcedUV()](../../d1/db4/classStdMeshers__Quadrangle__2D.html#a1bbffcada6260cde3d9a3341cc1fcbb7),
[WorkingPlane.Plane.getLocalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab4027587aa29bc4393a52df8159376e1),
[WorkingPlane.Plane.getLocalRot()](../../d3/d93/classWorkingPlane_1_1Plane.html#ac6d4009cbda9d7d73c9eda40206c5c44),
[draftguitools.gui_snapper.Snapper.getPerpendicular()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a28a2745e84210bdea1d1a39c88984f87),
[ArchCurtainWall.CurtainWall.getProjectedLength()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a0d62eb627e15558f1220ac54999b3358),
[draftguitools.gui_trackers.rectangleTracker.getSize()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#afc397a50b7aff2b85bd34fec4f3577f3),
[draftguitools.gui_rotate.Rotate.handle_mouse_move_event()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a9bf281ceb1e44564a7740b5cd1b6261e),
[draftguitools.gui_trackers.rectangleTracker.isInside()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a228a5fce20903baa872be30d7d392a6e),
[SMESH_Pattern.Load()](../../d0/d7d/classSMESH__Pattern.html#aada1481358a8eedfa7a175da392b9308),
[draftfunctions.offset.offset()](../../d2/d57/group__draftfunctions.html#ga15bf04dc2feebf4fe453ff6b9a3a7492),
[ArchBuildingPart.ViewProviderBuildingPart.onChanged()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#ab521b855d25a75f28c70a1cc42889546),
[ArchNesting.Nester.order()](../../d0/df4/classArchNesting_1_1Nester.html#a31f3390689c0459bc70d4423d6ca3f86),
[FCSphereSheetProjector.project()](../../d6/def/classFCSphereSheetProjector.html#a7ed463e71e4548ea28189fd1a8ad738a),
[ArchCommands.projectToVector()](../../d4/d52/namespaceArchCommands.html#a0f73f9076e0b2e2d1d651348d008522a),
[ArchWindow.recolorize()](../../d3/db7/namespaceArchWindow.html#a8a46c0e437e0f7099531f4bf88290aed),
[draftguitools.gui_trimex.Trimex.redraw()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a6c61910ba86ef48101475e9ecdd6f958),
[draftfunctions.scale.scale()](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10),
[draftguitools.gui_rotate.Rotate.set_rotation_angle()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a6c37aa491f9c996f40362bcdc860f296),
[SMESH_MeshEditor.Smooth()](../../da/d31/classSMESH__MeshEditor.html#a5272d9db1cbe2b2b1526a476e41c817f),
[draftguitools.gui_trackers.rectangleTracker.update()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#acedcfce459af33f633a1aa7e57501a7f),
[draftguitools.gui_edit_arch_objects.ArchWallGuiTools.update_object_from_edit_points()](../../d1/d46/classdraftguitools_1_1gui__edit__arch__objects_1_1ArchWallGuiTools.html#a1340bdc87e40eb0a04ba856255ae0f93),
[draftguitools.gui_edit_draft_objects.DraftRectangleGuiTools.update_object_from_edit_points()](../../d5/d75/classdraftguitools_1_1gui__edit__draft__objects_1_1DraftRectangleGuiTools.html#afbd0a806c0b9b244f31c44a3262b2642),
[draftguitools.gui_edit_draft_objects.DraftCircleGuiTools.update_object_from_edit_points()](../../d6/dd2/classdraftguitools_1_1gui__edit__draft__objects_1_1DraftCircleGuiTools.html#ab007d40a588bd74cc48d7544b10f4602),
[draftguitools.gui_edit_part_objects.PartBoxGuiTools.update_object_from_edit_points()](../../dd/d11/classdraftguitools_1_1gui__edit__part__objects_1_1PartBoxGuiTools.html#a810558eaa2408ab79a2a8b96ed0edab4),
[draftguitools.gui_edit_part_objects.PartCylinderGuiTools.update_object_from_edit_points()](../../db/dfa/classdraftguitools_1_1gui__edit__part__objects_1_1PartCylinderGuiTools.html#a22d593022a6772a3429d1a2a489ecf95),
[draftguitools.gui_edit_part_objects.PartConeGuiTools.update_object_from_edit_points()](../../db/d9c/classdraftguitools_1_1gui__edit__part__objects_1_1PartConeGuiTools.html#a56162ae844fb1229b11ed1ba73e50932),
and
[draftguitools.gui_edit_draft_objects.DraftCircleGuiTools.update_preview_object()](../../d6/dd2/classdraftguitools_1_1gui__edit__draft__objects_1_1DraftCircleGuiTools.html#a6433a14d2b37865cbe257322a0219577).

## ◆ removeDoubles()

def DraftVecUtils.removeDoubles  | ( |  | _vlist_| ) |   
---|---|---|---|---|---  
      
    
    Remove duplicated vectors from a list of vectors.
    
    It removes only the duplicates that are next to each other in the list.
    
    It tests the `i` element, and compares it to the `i+1` element.
    If the former one is different from the latter,
    the former is added to the new list, otherwise it is skipped.
    The last element is always included.
    ::
        [a, b, b, c, c] -> [a, b, c]
        [a, a, b, a, a, b] -> [a, b, a, b]
    
    Finding duplicated vectors tests for `equality` which depends
    on the `precision` parameter in the parameter database.
    
    Parameters
    ----------
    vlist : list of Base::Vector3
        List with vectors.
    
    Returns
    -------
    list of Base::Vector3
        New list with sequential duplicates removed,
        or the original `vlist` if there is only one element in the list.
    
    See Also
    --------
    equals : test for equality between two vectors
    

References
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
and
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[ArchRoof.face_from_points()](../../d4/d2a/namespaceArchRoof.html#abe32c5b766f22eb4210fe0024dbd7293).

## ◆ rotate()

def DraftVecUtils.rotate  | ( |  | _u_ ,   
---|---|---|---  
|  |  | _angle_ ,   
|  |  | _axis_ = `Vector(0, 0, 1)`  
| ) | |   
      
    
    Rotate the vector by the specified angle, around the given axis.
    
    If the axis is omitted, the rotation is made around the Z axis
    (on the XY plane).
    
    It uses a 3x3 rotation matrix.
    ::
        u_rot = R u
    
                (c + x*x*t    xyt - zs     xzt + ys )
        u_rot = (xyt + zs     c + y*y*t    yzt - xs ) * u
                (xzt - ys     yzt + xs     c + z*z*t)
    
    Where `x`, `y`, `z` indicate unit components of the axis;
    `c` denotes a cosine of the angle; `t` indicates a complement
    of that cosine; `xs`, `ys`, `zs` indicate products of the unit
    components and the sine of the angle; and `xyt`, `xzt`, `yzt`
    indicate products of two unit components and the complement
    of the cosine.
    
    Parameters
    ----------
    u : Base::Vector3
        The vector.
    angle : float
        The angle of rotation given in radians.
    axis : Base::Vector3, optional
        The vector specifying the axis of rotation.
        It defaults to `(0, 0, 1)`, the +Z axis.
    
    Returns
    -------
    Base::Vector3
        The new rotated vector.
        If the `angle` is zero, return the original vector `u`.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[draftguitools.gui_offset.Offset.action()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#af6fe1d529ed82fe117bb430a75844ec5),
[WorkingPlane.Plane.alignToPointAndAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab85860830e3debec48d3cdb58d30621a),
[WorkingPlane.Plane.alignToPointAndAxis_SVG()](../../d3/d93/classWorkingPlane_1_1Plane.html#a53cb561d317b813ea9a22ef8e319104d),
[draftgeoutils.intersections.angleBisection()](../../d9/dfd/group__draftgeoutils.html#ga692ff72eee5139e832fb1fc6f5ee949e),
[draftgeoutils.circles.circleFrom2LinesRadius()](../../d9/dfd/group__draftgeoutils.html#gac123fb7d62899d609a3206597da6e734),
[draftgeoutils.circles.circleFrom3LineTangents()](../../d9/dfd/group__draftgeoutils.html#gacc0f0f89c65bda5546b24a2513ed592c),
[draftfunctions.svg.format_point()](../../d2/d57/group__draftfunctions.html#ga8f27938b7ca9e7515f875ef70690525a),
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5),
[draftgeoutils.circles.getCircleFromSpline()](../../d9/dfd/group__draftgeoutils.html#gacde5b7f0b59d56ae852c77f40889913e),
[draftguitools.gui_arcs.Arc.numericRadius()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a3a55830e1e08f60be95ed81d73759e52),
[draftfunctions.offset.offset()](../../d2/d57/group__draftfunctions.html#ga15bf04dc2feebf4fe453ff6b9a3a7492),
[ArchWindow.recolorize()](../../d3/db7/namespaceArchWindow.html#a8a46c0e437e0f7099531f4bf88290aed),
[draftguitools.gui_trimex.Trimex.redraw()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a6c61910ba86ef48101475e9ecdd6f958),
[draftfunctions.rotate.rotate()](../../d2/d57/group__draftfunctions.html#ga0429017dad7951a61c04221ce72b32fb),
[draftfunctions.rotate.rotate_vector_from_center()](../../d2/d57/group__draftfunctions.html#ga183986f7cd09d522dd82a38b522c2353),
[draftguitools.gui_snapper.Snapper.snapToPolar()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a5a30c9877875867157703325b090e21f),
and
[ArchPanel.ViewProviderPanelSheet.updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093).

## ◆ rotate2D()

def DraftVecUtils.rotate2D  | ( |  | _u_ ,   
---|---|---|---  
|  |  | _angle_  
| ) | |   
      
    
    Rotate the given vector around the Z axis by the specified angle.
    
    The rotation occurs in two dimensions only by means of
    a rotation matrix.
    ::
         u_rot                R                 u
        (x_rot) = (cos(-angle) -sin(-angle)) * (x)
        (y_rot)   (sin(-angle)  cos(-angle))   (y)
    
    Normally the angle is positive, but in this case it is negative.
    
    `"Such non-standard orientations are rarely used in mathematics
    but are common in 2D computer graphics, which often have the origin
    in the top left corner and the y-axis pointing down."`
    W3C Recommendations (2003), Scalable Vector Graphics: the initial
    coordinate system.
    
    Parameters
    ----------
    u : Base::Vector3
        The vector.
    angle : float
        The angle of rotation given in radians.
    
    Returns
    -------
    Base::Vector3
        The new rotated vector.
    

## ◆ rounded()

def DraftVecUtils.rounded  | ( |  | _v_ ,   
---|---|---|---  
|  |  | _d_ = `None`  
| ) | |   
      
    
    Return a vector rounded to the `precision` in the parameter database
    or to the given decimals value
    
    Each of the components of the vector is rounded to the decimal
    precision set in the parameter database.
    
    Parameters
    ----------
    v : Base::Vector3
        The input vector.
    d : (Optional) the number of decimals to round to
    
    Returns
    -------
    Base::Vector3
        The new vector where each element `x`, `y`, `z` has been rounded
        to the number of decimals specified in the `precision` parameter
        in the parameter database.
    

Referenced by
[ArchEquipment.createMeshView()](../../db/d00/namespaceArchEquipment.html#a7325bf277971b5b271fa96eebb2d83c7),
[importIFClegacy.getIfcExtrusionData()](../../db/d15/namespaceimportIFClegacy.html#a7889bb7a501c72e2d644331b90e0a16c),
and
[importIFClegacy.getTuples()](../../db/d15/namespaceimportIFClegacy.html#a7fc42bf336f708c10ef39e50e781e6b1).

## ◆ scale()

def DraftVecUtils.scale  | ( |  | _u_ ,   
---|---|---|---  
|  |  | _scalar_  
| ) | |   
      
    
    Scales (multiplies) a vector by a scalar factor.
    
    Parameters
    ----------
    u : Base::Vector3
        The FreeCAD.Vector to scale.
    scalar : float
        The scaling factor.
    
    Returns
    -------
    Base::Vector3
        The new vector with each of its elements multiplied by `scalar`.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[ArchStairs.makeRailing()](../../dc/d06/namespaceArchStairs.html#a37c92f2db600fd86adc3ac386c6fa211),
and
[ArchWindow.recolorize()](../../d3/db7/namespaceArchWindow.html#a8a46c0e437e0f7099531f4bf88290aed).

## ◆ scaleTo()

def DraftVecUtils.scaleTo  | ( |  | _u_ ,   
---|---|---|---  
|  |  | _l_  
| ) | |   
      
    
    Scale a vector so that its magnitude is equal to a given length.
    
    The magnitude of a vector is
    ::
        L = sqrt(x**2 + y**2 + z**2)
    
    This function multiplies each coordinate, `x`, `y`, `z`,
    by a factor to produce the desired magnitude `L`.
    This factor is the ratio of the new magnitude to the old magnitude,
    ::
        x_scaled = x * (L_new/L_old)
    
    Parameters
    ----------
    u : Base::Vector3
        The vector to scale.
    l : int or float
        The new magnitude of the vector in standard units (mm).
    
    Returns
    -------
    Base::Vector3
        The new vector with each of its elements scaled by a factor.
        Or the same input vector `u`, if it is `(0, 0, 0)`.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[importDXF.addText()](../../d7/dbf/namespaceimportDXF.html#a9542af2528d721e677018e7705990190),
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
[ArchRebar.CalculatePlacement()](../../dd/de9/namespaceArchRebar.html#ad2d794825c3b65e586027b2eba490642),
[draftgeoutils.circles.circleFromPointLineRadius()](../../d9/dfd/group__draftgeoutils.html#ga163b5f31d9b814e500670ab9cec198b5),
[ArchRebar.CustomSpacingPlacement()](../../dd/de9/namespaceArchRebar.html#a2579602c2f55c70ae0dd36de62851e02),
[draftobjects.wire.Wire.execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[draftfunctions.svg.format_point()](../../d2/d57/group__draftfunctions.html#ga8f27938b7ca9e7515f875ef70690525a),
[draftguitools.gui_selectplane.Draft_SelectPlane.getCenterPoint()](../../dc/d53/classdraftguitools_1_1gui__selectplane_1_1Draft__SelectPlane.html#a5166200cf411a6092fd2e1c5046dc1fc),
[ArchCommands.getCutVolume()](../../d4/d52/namespaceArchCommands.html#aa9bddbee3691ffd7b3cba2f35e55ce77),
[ArchStairs.makeRailing()](../../dc/d06/namespaceArchStairs.html#a37c92f2db600fd86adc3ac386c6fa211),
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d),
[draftobjects.dimension.measure_one_obj_edge()](../../de/de1/group__draftobjects.html#ga929b4c920430cd6ac84336ecd1e66938),
[draftguitools.gui_arcs.Arc.numericRadius()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a3a55830e1e08f60be95ed81d73759e52),
[draftgeoutils.offsets.offsetWire()](../../d9/dfd/group__draftgeoutils.html#ga05bacae1f1c67ceaba7aa1c37c8f758f),
[draftobjects.wire.Wire.onChanged()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#a2832beac9526a31b90bc4da2dec506ce),
[ArchCommands.projectToVector()](../../d4/d52/namespaceArchCommands.html#a0f73f9076e0b2e2d1d651348d008522a),
[ArchWindow.recolorize()](../../d3/db7/namespaceArchWindow.html#a8a46c0e437e0f7099531f4bf88290aed),
[draftguitools.gui_trimex.Trimex.redraw()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a6c61910ba86ef48101475e9ecdd6f958),
[draftguitools.gui_trackers.boxTracker.update()](../../d5/dca/classdraftguitools_1_1gui__trackers_1_1boxTracker.html#a17b09ebf946c0767ce1236e269f5a518),
and
[importDXF.writeShape()](../../d7/dbf/namespaceimportDXF.html#afb8ab0d3ed82033509940a68c47867af).

## ◆ toString()

def DraftVecUtils.toString  | ( |  | _u_| ) |   
---|---|---|---|---|---  
      
    
    Return a string with the Python command to recreate this vector.
    
    Parameters
    ----------
    u : list, or Base::Vector3
        A list of FreeCAD.Vectors, or a single vector.
    
    Returns
    -------
    str
        The string with the code that can be used in the Python console
        to create the same list of vectors, or single vector.
    

Referenced by
[drafttaskpanels.task_shapestring.ShapeStringTaskPanelEdit.accept()](../../d7/da9/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanelEdit.html#a9201c29e738ab0b73095e222421cdfc3),
[draftguitools.gui_offset.Offset.action()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#af6fe1d529ed82fe117bb430a75844ec5),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftguitools.gui_move.Move.build_copy_subelements_command()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#ac31bdceb581d30f275f557e439789605),
[draftguitools.gui_rotate.Rotate.build_copy_subelements_command()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a86c65f9a4f091a33d4476b26d5b5eaa2),
[draftguitools.gui_scale.Scale.build_copy_subelements_command()](../../d5/d4f/classdraftguitools_1_1gui__scale_1_1Scale.html#a5edead2233d818ad3114cb17c4f600ec),
[draftguitools.gui_move.Move.build_move_subelements_command()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#affade6b6b2ac9f96864ca0f520583048),
[draftguitools.gui_rotate.Rotate.build_rotate_subelements_command()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a62bb9191db4528d134ccb5aff0a52bf0),
[draftguitools.gui_scale.Scale.build_scale_subelements_command()](../../d5/d4f/classdraftguitools_1_1gui__scale_1_1Scale.html#ae4f0935268ca1b3b271aa63684b19eb0),
[draftguitools.gui_labels.Label.create()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a3eb18f4a13e2c3c5be440173e20576a7),
[draftguitools.gui_dimensions.Dimension.create_angle_dimension()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a93e737809e65027a2c59d9a6578bd68b),
[draftguitools.gui_dimensions.Dimension.create_linear_dimension()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a495fbfb19776360d275ec5c788c089eb),
[draftguitools.gui_dimensions.Dimension.create_linear_dimension_obj()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a09524e3cf20de8032c097a07e7e06287),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.create_object()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#ac99628c4fa3165b5162bb6abac2b8936),
[drafttaskpanels.task_orthoarray.TaskPanelOrthoArray.create_object()](../../d6/dfa/classdrafttaskpanels_1_1task__orthoarray_1_1TaskPanelOrthoArray.html#aa0fd34d81616c74156ab4f1192f1b580),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.create_object()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a9bb3c55a3c2f34ab5d8a1f16b15c836d),
[draftguitools.gui_dimensions.Dimension.create_radial_dimension_obj()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#adf27abb48ee0c5c9f3902a86eefab1e8),
[draftguitools.gui_dimensions.Dimension.create_with_app_measure()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a8813b8f053ebcc3f96fed8eae06fde2e),
[draftguitools.gui_ellipses.Ellipse.createObject()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#a45e8f0dc8ce41d63c874cf79bc6807bd),
[draftguitools.gui_rectangles.Rectangle.createObject()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a8a64aeb6e0f8e7d9036f7b1b795c3567),
[draftguitools.gui_shapestrings.ShapeString.createObject()](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#aa6351c9498c8b08effd1a43f542369c3),
[drafttaskpanels.task_shapestring.ShapeStringTaskPanelCmd.createObject()](../../df/d8e/classdrafttaskpanels_1_1task__shapestring_1_1ShapeStringTaskPanelCmd.html#a2bf73c981ede5444c97bd0d33af8eace),
[change_branch.ChangeBranchDialogModel.data()](../../d1/d0e/classchange__branch_1_1ChangeBranchDialogModel.html#aeb42e63ba760cbcdaa58d35d89299e0c),
[package_details.PackageDetails.display_repo_status()](../../d1/df5/classpackage__details_1_1PackageDetails.html#abafff14948ac22d38fe00e5cf8110900),
[draftguitools.gui_arcs.Arc.drawArc()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a5abd3b89ce588c5761f8ecdbe95f73a5),
[draftguitools.gui_polygons.Polygon.drawPolygon()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a8f4ddb1f0ebe6e684173a9b6c60c700c),
[Gui::QuantitySpinBox.event()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#a1c2ffac01c0b7934971b71bb2af3275f),
[draftguitools.gui_lines.Line.finish()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#a622af4e1166f892f860b86d3d1e3f053),
[TechDrawGui::TaskProjGroup.formatVector()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#ad5149a1165041927bffa169566e0b61e),
[package_list.PackageListItemDelegate.get_expanded_update_string()](../../da/dfb/classpackage__list_1_1PackageListItemDelegate.html#a555491804edbc598e11e3dcbe11ff4ca),
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[PartGui::DlgExtrusion.getShapesToExtrude()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a2e05cea8f2a72a8c3ec08d760416cc7a),
[PartGui::DlgRevolution.getShapesToRevolve()](../../d1/d83/classPartGui_1_1DlgRevolution.html#af847882d2e684d1f219a9353aec25281),
[draftguitools.gui_base_original.DraftTool.getStrings()](../../da/d09/classdraftguitools_1_1gui__base__original_1_1DraftTool.html#a940881c2458a5ec52c3e7eda58a7296d),
[draftguitools.gui_mirror.Mirror.mirror()](../../d8/dbd/classdraftguitools_1_1gui__mirror_1_1Mirror.html#a6d13547fe690668596ffedceabfcaea3),
[draftguitools.gui_move.Move.move_object()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#aad1a83d2b6aa28ec1ed14f8357feef1c),
[draftguitools.gui_offset.Offset.numericRadius()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#ae08617dcd80297f9e33139b0cfb5589f),
[draftguitools.gui_patharray.PathArray.proceed()](../../dd/d56/classdraftguitools_1_1gui__patharray_1_1PathArray.html#a62c7a8f3f99aa118be2866db53c82265),
[draftguitools.gui_shape2dview.Shape2DView.proceed()](../../d5/d96/classdraftguitools_1_1gui__shape2dview_1_1Shape2DView.html#a98747eb9bb42dc98ac8fa58911e5d200),
[draftguitools.gui_split.Split.proceed()](../../db/d21/classdraftguitools_1_1gui__split_1_1Split.html#ac4cf14c119bc3f5d22f8ed1b8aca71ba),
[Gui::ExpLineEdit.resizeEvent()](../../d0/d05/classGui_1_1ExpLineEdit.html#ab4370763f20b014e2402c6231aa37a8d),
[draftguitools.gui_rotate.Rotate.rotate_object()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#adfb7c1f87286e994cf85344a2614d2d0),
[draftguitools.gui_scale.Scale.scale_object()](../../d5/d4f/classdraftguitools_1_1gui__scale_1_1Scale.html#a6bc1f4f4c6c541917b4b5d130c958825),
[draftguitools.gui_scale.Scale.scale_with_clone()](../../d5/d4f/classdraftguitools_1_1gui__scale_1_1Scale.html#a627ccc5d883037091060fd88e265c17e),
[Gui::Dialog::DlgRevertToBackupConfigImp.showEvent()](../../d1/d47/classGui_1_1Dialog_1_1DlgRevertToBackupConfigImp.html#a0063a3ac64ccc1eb7c0aaa7309471ed9),
[Gui::ExpressionSpinBox.showValidExpression()](../../d7/d1b/classGui_1_1ExpressionSpinBox.html#a98d67e4a5b08e6c703981f7317bddb35),
and
[Gui::SoFCOffscreenRenderer.writeToImageFile()](../../d9/dc4/classGui_1_1SoFCOffscreenRenderer.html#a9492ac7c39b49b35f6ce5ed674f8bf4a).

## ◆ tup()

def DraftVecUtils.tup  | ( |  | _u_ ,   
---|---|---|---  
|  |  | _array_ = `False`  
| ) | |   
      
    
    Return a tuple or a list with the coordinates of a vector.
    
    Parameters
    ----------
    u : Base::Vector3
        A FreeCAD.Vector.
    array : bool, optional
        Defaults to `False`, and the output is a tuple.
        If `True` the output is a list.
    
    Returns
    -------
    tuple or list
        The coordinates of the vector in a tuple `(x, y, z)`
        or in a list `[x, y, z]`, if `array=True`.
    

References
[DraftVecUtils.typecheck()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9595482b5e5fa3960992e502a5544689).

Referenced by
[draftguitools.gui_trackers.dimTracker.calc()](../../d2/d2f/classdraftguitools_1_1gui__trackers_1_1dimTracker.html#a55b0af8e2e595d3cdf7d7129b8f3b7c0),
[importDXF.export()](../../d7/dbf/namespaceimportDXF.html#ae90d02ee42cc3c2b7daa7138cc8d02a4),
[importDXF.getArcData()](../../d7/dbf/namespaceimportDXF.html#a4e379964eac7c45567318e781830a5b5),
[App::PropertyLinkSub.getPyObject()](../../d3/d76/classApp_1_1PropertyLinkSub.html#ad1b1f9c557f1e474722b0cd37ccb4a96),
[App::PropertyLinkSubList.getPyObject()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a07c5d74e2725f2d1e804d3706d239e2e),
[App::PropertyXLinkSubList.getPyObject()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#aa9ee16bcedb194655b91e5d93730bf22),
[importIFC.insert()](../../d4/d4b/namespaceimportIFC.html#a0a5eb3c8368cd2d7a14ca964ad41258f),
[ArchComponent.Component.onChanged()](../../de/d87/classArchComponent_1_1Component.html#ac10328dd9515bdac2dd7e11861c4609e),
[draftobjects.array.polar_placements()](../../de/de1/group__draftobjects.html#ga74bc873095b07ddb71d854a00b109b61),
[draftguitools.gui_trackers.boxTracker.pos()](../../d5/dca/classdraftguitools_1_1gui__trackers_1_1boxTracker.html#a7103a4ad3e7a50363c67272befebeffb),
[draftfunctions.rotate.rotate()](../../d2/d57/group__draftfunctions.html#ga0429017dad7951a61c04221ce72b32fb),
[draftguitools.gui_trackers.ghostTracker.rotate()](../../d9/dc6/classdraftguitools_1_1gui__trackers_1_1ghostTracker.html#a41e3af358c2f0d86796cd1570ebe627d),
and
[importDXF.writeShape()](../../d7/dbf/namespaceimportDXF.html#afb8ab0d3ed82033509940a68c47867af).

## ◆ typecheck()

def DraftVecUtils.typecheck  | ( |  | _args_and_types_ ,   
---|---|---|---  
|  |  | _name_ = `"?"`  
| ) | |   
      
    
    Check that the arguments are instances of certain types.
    
    Parameters
    ----------
    args_and_types : list
        A list of tuples. The first element of a tuple is tested as being
        an instance of the second element.
        ::
            args_and_types = [(a, Type), (b, Type2), ...]
    
        Then
        ::
            isinstance(a, Type)
            isinstance(b, Type2)
    
        A `Type` can also be a tuple of many types, in which case
        the check is done for any of them.
        ::
            args_and_types = [(a, (Type3, int, float)), ...]
    
            isinstance(a, (Type3, int, float))
    
    name : str, optional
        Defaults to `'?'`. The name of the check.
    
    Raises
    ------
    TypeError
        If the first element in the tuple is not an instance of the second
        element.
    

Referenced by
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
[DraftVecUtils.closest()](../../dc/dc3/group__DRAFTVECUTILS.html#ga8035ae4425c9330b9ba7a75ba7735749),
[DraftVecUtils.dist()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2af953a65bfefb422584aa67c55dbc39),
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
[DraftVecUtils.find()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf764683bba7871d8f3d64db4fb2a41a9),
[DraftVecUtils.getPlaneRotation()](../../dc/dc3/group__DRAFTVECUTILS.html#ga8ac4fe6e7590ab515d4f1287a79ee88f),
[DraftVecUtils.isColinear()](../../dc/dc3/group__DRAFTVECUTILS.html#ga5af8ac969e7561440b80810e9fbd5194),
[DraftVecUtils.neg()](../../dc/dc3/group__DRAFTVECUTILS.html#gadc85e420d51ac389c376dadd8b68e558),
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc),
[DraftVecUtils.removeDoubles()](../../dc/dc3/group__DRAFTVECUTILS.html#ga7d65c2df29e414c0ca1ad2c8fd34c3b7),
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1),
[DraftVecUtils.scale()](../../dc/dc3/group__DRAFTVECUTILS.html#ga21ac4cbf94f2ea5f128cea89ed5dfca2),
[DraftVecUtils.scaleTo()](../../dc/dc3/group__DRAFTVECUTILS.html#ga6b1b9879299d28cb689cbee684e9d5f3),
and
[DraftVecUtils.tup()](../../dc/dc3/group__DRAFTVECUTILS.html#gada8f1f6ff2e9aca9a3ff9384ae3bbd27).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

