---
url: https://freecad.github.io/SourceDoc/d2/db9/namespacePart.html
scraped_at: 2025-09-08T14:51:38.851604
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Typedefs | Functions | Variables

Part Namespace Reference

AttachExtensionh, .cpp contain a extension class to derive other features
from, to make them attachable.
[More...](../../d2/db9/namespacePart.html#details)

##  Classes  
  
---  
class | [AttachEngineException](../../dd/d63/classPart_1_1AttachEngineException.html)  
class | [AttachExtension](../../dc/d47/classPart_1_1AttachExtension.html)  
| The AttachableObject class is the thing to extend an object with that should
be attachable.
[More...](../../dc/d47/classPart_1_1AttachExtension.html#details)  
  
class | [BodyBase](../../da/dc8/classPart_1_1BodyBase.html)  
| [Base](../../db/d07/namespaceBase.html "Basic structures used by other
FreeCAD components \(C++ API\)") class of all body objects in FreeCAD A body
is used, e.g. [More...](../../da/dc8/classPart_1_1BodyBase.html#details)  
  
class | [Boolean](../../da/d3a/classPart_1_1Boolean.html)  
class | [BooleanException](../../d1/d8c/classPart_1_1BooleanException.html)  
class | [Box](../../dc/d80/classPart_1_1Box.html)  
class | [BRepBuilderAPI_RefineModel](../../d8/d31/classPart_1_1BRepBuilderAPI__RefineModel.html)  
class | [BRepFeatModule](../../da/de2/classPart_1_1BRepFeatModule.html)  
class | [BRepOffsetAPI_MakeOffsetFix](../../d8/dff/classPart_1_1BRepOffsetAPI__MakeOffsetFix.html)  
| The
[BRepOffsetAPI_MakeOffsetFix](../../d8/dff/classPart_1_1BRepOffsetAPI__MakeOffsetFix.html
"The BRepOffsetAPI_MakeOffsetFix class This class works around a limitation of
the BRepOffsetAPI_MakeO...") class This class works around a limitation of the
BRepOffsetAPI_MakeOffset which returns unexpected results when an input wire
has set a placement and consists of a single edge only.
[More...](../../d8/dff/classPart_1_1BRepOffsetAPI__MakeOffsetFix.html#details)  
  
class | [BRepOffsetAPIModule](../../de/d36/classPart_1_1BRepOffsetAPIModule.html)  
class | [BSplineCurveBiArcs](../../d2/d61/classPart_1_1BSplineCurveBiArcs.html)  
class | [Chamfer](../../d7/d75/classPart_1_1Chamfer.html)  
class | [ChFi2dModule](../../dd/da0/classPart_1_1ChFi2dModule.html)  
class | [Circle](../../de/de4/classPart_1_1Circle.html)  
class | [Common](../../d1/d2f/classPart_1_1Common.html)  
class | [Compound](../../d7/d98/classPart_1_1Compound.html)  
class | [Compound2](../../d5/dab/classPart_1_1Compound2.html)  
| Same as [Part::Compound](../../d7/d98/classPart_1_1Compound.html), except it
marks the Shape as transient, and rebuild it during restore.
[More...](../../d5/dab/classPart_1_1Compound2.html#details)  
  
class | [Cone](../../d2/d8f/classPart_1_1Cone.html)  
class | [CrossSection](../../d3/dc3/classPart_1_1CrossSection.html)  
class | [CurveNet](../../d9/d41/classPart_1_1CurveNet.html)  
class | [CustomFeature](../../da/d46/classPart_1_1CustomFeature.html)  
| [Base](../../db/d07/namespaceBase.html "Basic structures used by other
FreeCAD components \(C++ API\)") class of all custom feature classes which are
almost used as base for python feature classes.
[More...](../../da/d46/classPart_1_1CustomFeature.html#details)  
  
class | [Cut](../../d9/d65/classPart_1_1Cut.html)  
struct | [cutFaces](../../df/d39/structPart_1_1cutFaces.html)  
| Find all faces cut by a line through the centre of gravity of a given face
Useful for the "up to face" options to pocket or pad.
[More...](../../df/d39/structPart_1_1cutFaces.html#details)  
  
class | [Cylinder](../../dd/d12/classPart_1_1Cylinder.html)  
class | [Datum](../../db/d0b/classPart_1_1Datum.html)  
class | [Edgecluster](../../d0/d58/classPart_1_1Edgecluster.html)  
struct | [EdgePoints](../../db/dda/structPart_1_1EdgePoints.html)  
struct | [Edgesort_gp_Pnt_Less](../../d4/d19/structPart_1_1Edgesort__gp__Pnt__Less.html)  
class | [Ellipse](../../d6/d22/classPart_1_1Ellipse.html)  
class | [Ellipsoid](../../d4/dc8/classPart_1_1Ellipsoid.html)  
class | [Extrusion](../../db/d6c/classPart_1_1Extrusion.html)  
class | [ExtrusionHelper](../../d4/dd3/classPart_1_1ExtrusionHelper.html)  
class | [Face](../../dc/dbf/classPart_1_1Face.html)  
class | [FaceMaker](../../df/dde/classPart_1_1FaceMaker.html)  
| [FaceMaker](../../df/dde/classPart_1_1FaceMaker.html "FaceMaker class is the
base class for implementing various "smart" face making routines.") class is
the base class for implementing various "smart" face making routines.
[More...](../../df/dde/classPart_1_1FaceMaker.html#details)  
  
class | [FaceMakerBullseye](../../de/d69/classPart_1_1FaceMakerBullseye.html)  
| The [FaceMakerBullseye](../../de/d69/classPart_1_1FaceMakerBullseye.html
"The FaceMakerBullseye class is a tool to make planar faces with holes, where
there can be additional ...") class is a tool to make planar faces with holes,
where there can be additional faces inside holes and they can have holes too
and so on. [More...](../../de/d69/classPart_1_1FaceMakerBullseye.html#details)  
  
class | [FaceMakerCheese](../../d0/d37/classPart_1_1FaceMakerCheese.html)  
| The [FaceMakerCheese](../../d0/d37/classPart_1_1FaceMakerCheese.html "The
FaceMakerCheese class is a legacy face maker that was extracted from Part
Extrude.") class is a legacy face maker that was extracted from
[Part](../../d2/db9/namespacePart.html "AttachExtensionh, .cpp contain a
extension class to derive other features from, to make them attachab...")
Extrude. [More...](../../d0/d37/classPart_1_1FaceMakerCheese.html#details)  
  
class | [FaceMakerExtrusion](../../d2/d2e/classPart_1_1FaceMakerExtrusion.html)  
| [FaceMakerExtrusion](../../d2/d2e/classPart_1_1FaceMakerExtrusion.html
"FaceMakerExtrusion provides legacy compounding-structure-ignorant behavior of
facemaker of Part Extru...") provides legacy compounding-structure-ignorant
behavior of facemaker of [Part](../../d2/db9/namespacePart.html
"AttachExtensionh, .cpp contain a extension class to derive other features
from, to make them attachab...") Extrude.
[More...](../../d2/d2e/classPart_1_1FaceMakerExtrusion.html#details)  
  
class | [FaceMakerPublic](../../d5/d17/classPart_1_1FaceMakerPublic.html)  
| The [FaceMakerPublic](../../d5/d17/classPart_1_1FaceMakerPublic.html "The
FaceMakerPublic class: derive from it if you want the face maker to be listed
in tools that allow...") class: derive from it if you want the face maker to
be listed in tools that allow choosing one.
[More...](../../d5/d17/classPart_1_1FaceMakerPublic.html#details)  
  
class | [FaceMakerSimple](../../d3/d64/classPart_1_1FaceMakerSimple.html)  
| The [FaceMakerSimple](../../d3/d64/classPart_1_1FaceMakerSimple.html "The
FaceMakerSimple class: make plane faces from all closed wires supplied,
ignoring overlaps.") class: make plane faces from all closed wires supplied,
ignoring overlaps.
[More...](../../d3/d64/classPart_1_1FaceMakerSimple.html#details)  
  
class | [Feature](../../d7/d7e/classPart_1_1Feature.html)  
| [Base](../../db/d07/namespaceBase.html "Basic structures used by other
FreeCAD components \(C++ API\)") class of all shape feature classes in
FreeCAD. [More...](../../d7/d7e/classPart_1_1Feature.html#details)  
  
class | [FeatureExt](../../d5/de3/classPart_1_1FeatureExt.html)  
| [Base](../../db/d07/namespaceBase.html "Basic structures used by other
FreeCAD components \(C++ API\)") class of all shape feature classes in
FreeCAD. [More...](../../d5/de3/classPart_1_1FeatureExt.html#details)  
  
class | [FeatureGeometrySet](../../d6/d80/classPart_1_1FeatureGeometrySet.html)  
class | [FeatureReference](../../d2/da1/classPart_1_1FeatureReference.html)  
| [Base](../../db/d07/namespaceBase.html "Basic structures used by other
FreeCAD components \(C++ API\)") class of all shape feature classes in
FreeCAD. [More...](../../d2/da1/classPart_1_1FeatureReference.html#details)  
  
class | [Fillet](../../d4/da4/classPart_1_1Fillet.html)  
class | [FilletBase](../../df/d7d/classPart_1_1FilletBase.html)  
struct | [FilletElement](../../d2/d8f/structPart_1_1FilletElement.html)  
| A property class to store hash codes and two radii for the fillet algorithm.
[More...](../../d2/d8f/structPart_1_1FilletElement.html#details)  
  
class | [Fuse](../../d5/d01/classPart_1_1Fuse.html)  
class | [Geom2dArcOfCircle](../../de/d96/classPart_1_1Geom2dArcOfCircle.html)  
class | [Geom2dArcOfConic](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html)  
class | [Geom2dArcOfEllipse](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html)  
class | [Geom2dArcOfHyperbola](../../dc/db7/classPart_1_1Geom2dArcOfHyperbola.html)  
class | [Geom2dArcOfParabola](../../d3/d95/classPart_1_1Geom2dArcOfParabola.html)  
class | [Geom2dBezierCurve](../../d6/d50/classPart_1_1Geom2dBezierCurve.html)  
class | [Geom2dBSplineCurve](../../dd/d59/classPart_1_1Geom2dBSplineCurve.html)  
class | [Geom2dCircle](../../d7/d4e/classPart_1_1Geom2dCircle.html)  
class | [Geom2dConic](../../d8/d0d/classPart_1_1Geom2dConic.html)  
class | [Geom2dCurve](../../d4/da9/classPart_1_1Geom2dCurve.html)  
class | [Geom2dEllipse](../../db/db9/classPart_1_1Geom2dEllipse.html)  
class | [Geom2dHyperbola](../../d2/d95/classPart_1_1Geom2dHyperbola.html)  
class | [Geom2dLine](../../d2/d27/classPart_1_1Geom2dLine.html)  
class | [Geom2dLineSegment](../../df/ded/classPart_1_1Geom2dLineSegment.html)  
class | [Geom2dModule](../../db/d5a/classPart_1_1Geom2dModule.html)  
class | [Geom2dOffsetCurve](../../d5/de5/classPart_1_1Geom2dOffsetCurve.html)  
class | [Geom2dParabola](../../d9/dff/classPart_1_1Geom2dParabola.html)  
class | [Geom2dPoint](../../d8/da9/classPart_1_1Geom2dPoint.html)  
class | [Geom2dTrimmedCurve](../../d8/da3/classPart_1_1Geom2dTrimmedCurve.html)  
class | [GeomArcOfCircle](../../de/d1f/classPart_1_1GeomArcOfCircle.html)  
class | [GeomArcOfConic](../../db/d48/classPart_1_1GeomArcOfConic.html)  
class | [GeomArcOfEllipse](../../df/d3f/classPart_1_1GeomArcOfEllipse.html)  
class | [GeomArcOfHyperbola](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html)  
class | [GeomArcOfParabola](../../db/ddc/classPart_1_1GeomArcOfParabola.html)  
class | [GeomBezierCurve](../../d5/d40/classPart_1_1GeomBezierCurve.html)  
class | [GeomBezierSurface](../../df/dab/classPart_1_1GeomBezierSurface.html)  
class | [GeomBoundedCurve](../../da/dbb/classPart_1_1GeomBoundedCurve.html)  
class | [GeomBSplineCurve](../../df/dfe/classPart_1_1GeomBSplineCurve.html)  
class | [GeomBSplineSurface](../../d1/d27/classPart_1_1GeomBSplineSurface.html)  
class | [GeomCircle](../../d0/dde/classPart_1_1GeomCircle.html)  
class | [GeomCone](../../d0/d7c/classPart_1_1GeomCone.html)  
class | [GeomConic](../../d1/d86/classPart_1_1GeomConic.html)  
class | [GeomCurve](../../d4/dc1/classPart_1_1GeomCurve.html)  
class | [GeomCylinder](../../de/dc7/classPart_1_1GeomCylinder.html)  
class | [GeomEllipse](../../db/d52/classPart_1_1GeomEllipse.html)  
class | [Geometry](../../dc/df0/classPart_1_1Geometry.html)  
class | [Geometry2d](../../d1/dad/classPart_1_1Geometry2d.html)  
class | [GeometryDefaultExtension](../../d6/d66/classPart_1_1GeometryDefaultExtension.html)  
class | [GeometryExtension](../../da/d7d/classPart_1_1GeometryExtension.html)  
class | [GeometryMigrationExtension](../../d7/d36/classPart_1_1GeometryMigrationExtension.html)  
class | [GeometryPersistenceExtension](../../de/db6/classPart_1_1GeometryPersistenceExtension.html)  
class | [GeomHyperbola](../../d7/d9e/classPart_1_1GeomHyperbola.html)  
class | [GeomLine](../../d5/d30/classPart_1_1GeomLine.html)  
class | [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html)  
class | [GeomOffsetCurve](../../d0/d36/classPart_1_1GeomOffsetCurve.html)  
class | [GeomOffsetSurface](../../dc/d14/classPart_1_1GeomOffsetSurface.html)  
class | [GeomParabola](../../d9/ddf/classPart_1_1GeomParabola.html)  
class | [GeomPlane](../../d2/d0e/classPart_1_1GeomPlane.html)  
class | [GeomPlateModule](../../d4/d3b/classPart_1_1GeomPlateModule.html)  
class | [GeomPlateSurface](../../d7/db9/classPart_1_1GeomPlateSurface.html)  
class | [GeomPoint](../../d2/dfb/classPart_1_1GeomPoint.html)  
class | [GeomSphere](../../dc/da5/classPart_1_1GeomSphere.html)  
class | [GeomSurface](../../d7/d6d/classPart_1_1GeomSurface.html)  
class | [GeomSurfaceOfExtrusion](../../de/dd5/classPart_1_1GeomSurfaceOfExtrusion.html)  
class | [GeomSurfaceOfRevolution](../../df/dc7/classPart_1_1GeomSurfaceOfRevolution.html)  
class | [GeomToroid](../../da/d8f/classPart_1_1GeomToroid.html)  
class | [GeomTrimmedCurve](../../df/d24/classPart_1_1GeomTrimmedCurve.html)  
class | [GeomTrimmedSurface](../../de/dd0/classPart_1_1GeomTrimmedSurface.html)  
class | [Helix](../../df/d49/classPart_1_1Helix.html)  
class | [HLRBRepModule](../../dd/d04/classPart_1_1HLRBRepModule.html)  
class | [ImportBrep](../../d8/d3e/classPart_1_1ImportBrep.html)  
class | [ImportIges](../../d2/d1d/classPart_1_1ImportIges.html)  
class | [ImportStep](../../d4/de2/classPart_1_1ImportStep.html)  
class | [Line](../../d3/dfe/classPart_1_1Line.html)  
class | [Loft](../../d3/d52/classPart_1_1Loft.html)  
struct | [MeshVertex](../../d5/d5f/structPart_1_1MeshVertex.html)  
class | [Mirroring](../../dc/dac/classPart_1_1Mirroring.html)  
class | [Module](../../db/de4/classPart_1_1Module.html)  
class | [MultiCommon](../../d1/df7/classPart_1_1MultiCommon.html)  
class | [MultiFuse](../../df/dbc/classPart_1_1MultiFuse.html)  
class | [NullShapeException](../../d0/d8e/classPart_1_1NullShapeException.html)  
class | [Offset](../../d0/dda/classPart_1_1Offset.html)  
class | [Offset2D](../../d7/dcf/classPart_1_1Offset2D.html)  
class | [Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html)  
| 2D Shape This is a specialized version of the PartShape for use with flat
(2D) geometry. [More...](../../d9/d57/classPart_1_1Part2DObject.html#details)  
  
class | [Plane](../../d0/d1c/classPart_1_1Plane.html)  
class | [Polygon](../../d3/db3/classPart_1_1Polygon.html)  
class | [Primitive](../../d2/d31/classPart_1_1Primitive.html)  
class | [Prism](../../dc/d69/classPart_1_1Prism.html)  
class | [PrismExtension](../../d3/dbb/classPart_1_1PrismExtension.html)  
class | [ProgressIndicator](../../d9/df8/classPart_1_1ProgressIndicator.html)  
class | [PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html)  
class | [PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html)  
class | [PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html)  
| The part shape property class.
[More...](../../d7/d28/classPart_1_1PropertyPartShape.html#details)  
  
class | [PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html)  
class | [Refine](../../d4/d0a/classPart_1_1Refine.html)  
class | [RegularPolygon](../../d2/d69/classPart_1_1RegularPolygon.html)  
class | [Reverse](../../d4/d24/classPart_1_1Reverse.html)  
class | [Revolution](../../d3/d17/classPart_1_1Revolution.html)  
class | [RuledSurface](../../d1/d41/classPart_1_1RuledSurface.html)  
class | [Section](../../d8/dea/classPart_1_1Section.html)  
class | [ShapeFixModule](../../d8/d78/classPart_1_1ShapeFixModule.html)  
struct | [ShapeHistory](../../d3/dec/structPart_1_1ShapeHistory.html)  
class | [ShapeSegment](../../d9/d3c/classPart_1_1ShapeSegment.html)  
class | [ShapeUpgradeModule](../../d8/d53/classPart_1_1ShapeUpgradeModule.html)  
class | [Sphere](../../dc/d57/classPart_1_1Sphere.html)  
class | [Spiral](../../d2/d3f/classPart_1_1Spiral.html)  
class | [Spline](../../da/d0b/classPart_1_1Spline.html)  
class | [Sweep](../../df/dc6/classPart_1_1Sweep.html)  
class | [TangentialArc](../../d2/d99/classPart_1_1TangentialArc.html)  
class | [Thickness](../../db/d73/classPart_1_1Thickness.html)  
class | [Tools](../../d9/d36/classPart_1_1Tools.html)  
class | [TopoShape](../../d8/ded/classPart_1_1TopoShape.html)  
| The representation for a CAD Shape.
[More...](../../d8/ded/classPart_1_1TopoShape.html#details)  
  
class | [Torus](../../db/d42/classPart_1_1Torus.html)  
class | [Vertex](../../de/d96/classPart_1_1Vertex.html)  
class | [Wedge](../../d5/dc5/classPart_1_1Wedge.html)  
  
##  Typedefs  
  
---  
typedef [App::ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)< [AttachExtension](../../dc/d47/classPart_1_1AttachExtension.html) > | [AttachExtensionPython](../../d2/db9/namespacePart.html#ae396d06ef98b0995cfcb0747b9bf382f)  
typedef [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [CustomFeature](../../da/d46/classPart_1_1CustomFeature.html) > | [CustomFeaturePython](../../d2/db9/namespacePart.html#ac6fafa7a6affd4494f3c44e1bcfbd415)  
typedef [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [Feature](../../d7/d7e/classPart_1_1Feature.html) > | [FeaturePython](../../d2/db9/namespacePart.html#aa3a6fc9fd54bbd3394b810fccdbc9dd7)  
using | [GeometryBoolExtension](../../d2/db9/namespacePart.html#a845bc05f7b0ce483de113bc2a1f1f50a) = [GeometryDefaultExtension](../../d6/d66/classPart_1_1GeometryDefaultExtension.html)< [bool](../../d9/db9/classbool.html) >  
using | [GeometryDoubleExtension](../../d2/db9/namespacePart.html#a89ee3abee7bd3c049699df90afd07cff) = [GeometryDefaultExtension](../../d6/d66/classPart_1_1GeometryDefaultExtension.html)< double >  
using | [GeometryIntExtension](../../d2/db9/namespacePart.html#aa37b088b4c46252162c18f07dea2f21f) = [GeometryDefaultExtension](../../d6/d66/classPart_1_1GeometryDefaultExtension.html)< long >  
using | [GeometryStringExtension](../../d2/db9/namespacePart.html#aecbc5f1423dbc92050f9e133d973689f) = [GeometryDefaultExtension](../../d6/d66/classPart_1_1GeometryDefaultExtension.html)< std::string >  
typedef [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html) > | [Part2DObjectPython](../../d2/db9/namespacePart.html#a13bf980ca80846199b60a9e23a023d43)  
typedef std::vector< std::vector< TopoDS_Edge > > | [tEdgeClusterVector](../../d2/db9/namespacePart.html#af1a1d279943c7841082203dc4b81b100)  
typedef std::vector< TopoDS_Edge > | [tEdgeVector](../../d2/db9/namespacePart.html#ac99453e21c6f8a0552b70bb124709bc8)  
typedef std::map< gp_Pnt, [tEdgeVector](../../d2/db9/namespacePart.html#ac99453e21c6f8a0552b70bb124709bc8), [Edgesort_gp_Pnt_Less](../../d4/d19/structPart_1_1Edgesort__gp__Pnt__Less.html) > | [tMapPntEdge](../../d2/db9/namespacePart.html#ac4f90766804e172f3206a721c144c21b)  
typedef std::pair< gp_Pnt, [tEdgeVector](../../d2/db9/namespacePart.html#ac99453e21c6f8a0552b70bb124709bc8) > | [tMapPntEdgePair](../../d2/db9/namespacePart.html#ac8d6597487c921149a9c47538943e436)  
  
##  Functions  
  
---  
std::vector< std::string > | [buildBOPCheckResultVector](../../d2/db9/namespacePart.html#aefc587f6ef10312032e733720c7dfce8) ()  
std::vector< std::string > | [buildShapeEnumVector](../../d2/db9/namespacePart.html#a0e01c25923878222330430dc0b804617) ()  
[bool](../../d9/db9/classbool.html) | [checkIntersection](../../d2/db9/namespacePart.html#a26dca6f5d95248a6a7e10eb3a29cd748) (const TopoDS_Shape &[first](../../d1/da0/classint.html), const TopoDS_Shape &second, const [bool](../../d9/db9/classbool.html) quick, const [bool](../../d9/db9/classbool.html) touch_is_intersection)  
| Check for intersection between the two shapes.
[More...](../../d2/db9/namespacePart.html#a26dca6f5d95248a6a7e10eb3a29cd748)  
  
void | [closestPointsOnLines](../../d2/db9/namespacePart.html#a389ea20c7863562ce3513947b319f9d3) (const gp_Lin &lin1, const gp_Lin &lin2, gp_Pnt &p1, gp_Pnt &p2)  
TopoDS_Edge | [create3dCurve](../../d2/db9/namespacePart.html#a1d1d4893bee69c9beb6bc1851b97adac) (const TopoDS_Edge &edge)  
[GeomArcOfCircle](../../de/d1f/classPart_1_1GeomArcOfCircle.html) * | [createFilletGeometry](../../d2/db9/namespacePart.html#a4e47966fd6c762b34824b98614b76541) (const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *lineSeg1, const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *lineSeg2, const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &center, double radius)  
std::string | [encodeFilename](../../d2/db9/namespacePart.html#a510125d6f7d56e01089f48ef55409621) (std::string fn)  
[bool](../../d9/db9/classbool.html) | [find2DLinesIntersection](../../d2/db9/namespacePart.html#a0dd46c09269433a805588c348a585bb0) (const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &orig1, const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &dir1, const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &orig2, const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &dir2, [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &point)  
[bool](../../d9/db9/classbool.html) | [find2DLinesIntersection](../../d2/db9/namespacePart.html#a3976a9432420fb14f7f555b63ea3398a) (const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *lineSeg1, const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *lineSeg2, [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &point)  
std::vector< [cutFaces](../../df/d39/structPart_1_1cutFaces.html) > | [findAllFacesCutBy](../../d2/db9/namespacePart.html#a7a0d857a437bd1e2415d775f88f5bd59) (const TopoDS_Shape &shape, const TopoDS_Shape &face, const gp_Dir &dir)  
[bool](../../d9/db9/classbool.html) | [findFilletCenter](../../d2/db9/namespacePart.html#a95cddeb6bcff6c5a4f668e5c976fcfd9) (const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *lineSeg1, const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *lineSeg2, double radius, [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &center)  
[bool](../../d9/db9/classbool.html) | [findFilletCenter](../../d2/db9/namespacePart.html#ab01c47ee6de2dab1626ab457c264b394) (const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *lineSeg1, const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *lineSeg2, double radius, const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &refPnt1, const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &refPnt2, [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &center)  
std::vector< [TopoShape](../../d8/ded/classPart_1_1TopoShape.html) > | [getPyShapes](../../d2/db9/namespacePart.html#a48e080b087cffd68a633ef266b177263) ([PyObject](../../df/d1b/classPyObject.html) *obj)  
void | [getPyShapes](../../d2/db9/namespacePart.html#aad31b61eb5c4c2e25ac87ed29d043cb1) ([PyObject](../../df/d1b/classPyObject.html) *obj, std::vector< [TopoShape](../../d8/ded/classPart_1_1TopoShape.html) > &shapes)  
[int](../../d1/da0/classint.html) | [ImportIgesParts](../../d2/db9/namespacePart.html#a10322b892abc3b1779054dacf1a49e53) ([App::Document](../../d8/d3e/classApp_1_1Document.html) *pcDoc, const char *Name)  
[int](../../d1/da0/classint.html) | [ImportStepParts](../../d2/db9/namespacePart.html#a4da179b4c198cc0c74884eb8693d1619) ([App::Document](../../d8/d3e/classApp_1_1Document.html) *pcDoc, const char *Name)  
| The part shape property.
[More...](../../d2/db9/namespacePart.html#a4da179b4c198cc0c74884eb8693d1619)  
  
[PyObject](../../df/d1b/classPyObject.html) * | [initModule](../../d2/db9/namespacePart.html#af3669c97a7993f5da5f772300703523f) ()  
[bool](../../d9/db9/classbool.html) | [intersect](../../d2/db9/namespacePart.html#ae528b2bf4eca3b55cee601b84af58f8c) (const gp_Pln &pln1, const gp_Pln &pln2, gp_Lin &lin)  
std::unique_ptr< [GeomCurve](../../d4/dc1/classPart_1_1GeomCurve.html) > | [makeFromCurve](../../d2/db9/namespacePart.html#a541c4ec8e2e1179b048904f67f21605f) (const Handle(Geom_Curve)&c)  
std::unique_ptr< [Geom2dCurve](../../d4/da9/classPart_1_1Geom2dCurve.html) > | [makeFromCurve2d](../../d2/db9/namespacePart.html#a0663fbfcd3da6b4a5175a7da6504c9fe) (Handle(Geom2d_Curve) curve)  
std::unique_ptr< [GeomCurve](../../d4/dc1/classPart_1_1GeomCurve.html) > | [makeFromCurveAdaptor](../../d2/db9/namespacePart.html#a8c468c061fa8a64a649fcc83bb195292) (const [Adaptor3d_Curve](../../dc/d15/classAdaptor3d__Curve.html) &adapt)  
std::unique_ptr< [Geom2dCurve](../../d4/da9/classPart_1_1Geom2dCurve.html) > | [makeFromCurveAdaptor2d](../../d2/db9/namespacePart.html#aedc41c350e793ba243c3388dd2cde48f) (const [Adaptor2d_Curve2d](../../d6/da1/classAdaptor2d__Curve2d.html) &adapt)  
std::unique_ptr< [GeomSurface](../../d7/d6d/classPart_1_1GeomSurface.html) > | [makeFromSurface](../../d2/db9/namespacePart.html#a02852fe9ee218e35da27904a4c857655) (const Handle(Geom_Surface)&s)  
std::unique_ptr< [GeomCurve](../../d4/dc1/classPart_1_1GeomCurve.html) > | [makeFromTrimmedCurve](../../d2/db9/namespacePart.html#a87bbc69cb6d56aff7525ea6d696f44cd) (const Handle(Geom_Curve)&c, double f, double l)  
std::unique_ptr< [Geom2dCurve](../../d4/da9/classPart_1_1Geom2dCurve.html) > | [makeFromTrimmedCurve2d](../../d2/db9/namespacePart.html#a0f150892a72445c03ea12bebf7fb4f63) (const Handle(Geom2d_Curve)&c, double f, double l)  
const Py::Object | [makeGeometryCurvePy](../../d2/db9/namespacePart.html#aad18ba984c332dd91b111ce23f558d84) (const Handle(Geom_Curve)&c)  
const Py::Object | [makeTrimmedCurvePy](../../d2/db9/namespacePart.html#ab8440af3725a265f76bf3acad03b4bad) (const Handle(Geom_Curve)&c, double f, double l)  
const std::map< PyTypeObject *, TopAbs_ShapeEnum > | [mapTypeShape](../../d2/db9/namespacePart.html#a82114be61f28aeb57bb554f2403cae40) (vecTypeShape.begin(), vecTypeShape.end())  
[bool](../../d9/db9/classbool.html) | [ReadColors](../../d2/db9/namespacePart.html#ab596f048df47b8ce1555a96dd34d4521) (const Handle(XSControl_WorkSession) &WS, std::map< [int](../../d1/da0/classint.html), Quantity_Color > &hash_col)  
[bool](../../d9/db9/classbool.html) | [ReadNames](../../d2/db9/namespacePart.html#abe20933c961dababdab415179a371aaf) (const Handle(XSControl_WorkSession) &WS)  
Py::Object | [shape2pyshape](../../d2/db9/namespacePart.html#a7ddedec80f61edb78bd71990c25fe2da) (const TopoDS_Shape &shape)  
Py::Object | [shape2pyshape](../../d2/db9/namespacePart.html#a66d5751cbb6dccdc68d02cd2f928609e) (const [TopoShape](../../d8/ded/classPart_1_1TopoShape.html) &shape)  
static TopAbs_ShapeEnum | [ShapeTypeFromPyType](../../d2/db9/namespacePart.html#a8e1161389f1704ff900df16fa7f95d17) (PyTypeObject *pyType)  
std::list< TopoDS_Edge > | [sort_Edges](../../d2/db9/namespacePart.html#aa946b85ff6428be04494c8eda714ce2c) (double tol3d, std::list< TopoDS_Edge > &edges)  
double | [suggestFilletRadius](../../d2/db9/namespacePart.html#a1903069f8259f815f24930b78481a785) (const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *lineSeg1, const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *lineSeg2, const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &refPnt1, const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) &refPnt2)  
std::list< std::string > | [supportedSTEPSchemes](../../d2/db9/namespacePart.html#acc928ae0040584464c6b886672d015ba) ()  
[bool](../../d9/db9/classbool.html) | [tangentialArc](../../d2/db9/namespacePart.html#a39d5d9d990efef3e6581398defbda87d) (const gp_Pnt &p0, const gp_Vec &v0, const gp_Pnt &p1, gp_Pnt &c, gp_Dir &axis)  
  
##  Variables  
  
---  
const [App::PropertyQuantityConstraint::Constraints](../../df/dd1/structApp_1_1PropertyQuantityConstraint_1_1Constraints.html) | [angleRangeU](../../d2/db9/namespacePart.html#aaa81897ce99dd1a78503d1b5a130f208) = {0.0, 360.0, 1.0}  
const [App::PropertyQuantityConstraint::Constraints](../../df/dd1/structApp_1_1PropertyQuantityConstraint_1_1Constraints.html) | [angleRangeV](../../d2/db9/namespacePart.html#a45fe95e880bb5f0291855ced5eeea5b4) = {-90.0, 90.0, 1.0}  
const [App::PropertyQuantityConstraint::Constraints](../../df/dd1/structApp_1_1PropertyQuantityConstraint_1_1Constraints.html) | [apexRange](../../d2/db9/namespacePart.html#a5bb8f65e738128399c1b4f09de267973) = {-90.0, 90.0, 0.1}  
[PyObject](../../df/d1b/classPyObject.html) * | [PartExceptionOCCConstructionError](../../d2/db9/namespacePart.html#a8bc5b55fb3aaa2e7a44b2cc46f8f7f39)  
[PyObject](../../df/d1b/classPyObject.html) * | [PartExceptionOCCDimensionError](../../d2/db9/namespacePart.html#a2d0962463f2ea1d4440e651a107c8493)  
[PyObject](../../df/d1b/classPyObject.html) * | [PartExceptionOCCDomainError](../../d2/db9/namespacePart.html#a2ef302be8ca0fec356ccc324ceb9a4bb)  
[PyObject](../../df/d1b/classPyObject.html) * | [PartExceptionOCCError](../../d2/db9/namespacePart.html#a539a7cbe400e3f45c588a9189440303f)  
[PyObject](../../df/d1b/classPyObject.html) * | [PartExceptionOCCRangeError](../../d2/db9/namespacePart.html#a5db1ddc03d2fd430cc211afe893ef146)  
const [App::PropertyQuantityConstraint::Constraints](../../df/dd1/structApp_1_1PropertyQuantityConstraint_1_1Constraints.html) | [quantityRange](../../d2/db9/namespacePart.html#a7e0d9d0573ac8d383026c4ef1bf25008) = {0.0, FLT_MAX, 0.1}  
const [App::PropertyQuantityConstraint::Constraints](../../df/dd1/structApp_1_1PropertyQuantityConstraint_1_1Constraints.html) | [torusRangeV](../../d2/db9/namespacePart.html#a3a178c2cb72b6224a910e5822a08292b) = {-180.0, 180.0, 1.0}  
const std::vector< std::pair< PyTypeObject *, TopAbs_ShapeEnum > > | [vecTypeShape](../../d2/db9/namespacePart.html#a76bcb91c8af6fdcec5a6c46a5af3e7a2)  
  
## Detailed Description

AttachExtensionh, .cpp contain a extension class to derive other features
from, to make them attachable.

## Typedef Documentation

## ◆ AttachExtensionPython

typedef
[App::ExtensionPythonT](../../d7/d86/classApp_1_1ExtensionPythonT.html)<[AttachExtension](../../dc/d47/classPart_1_1AttachExtension.html)>
[Part::AttachExtensionPython](../../d2/db9/namespacePart.html#ae396d06ef98b0995cfcb0747b9bf382f)  
---  
  
## ◆ CustomFeaturePython

typedef
[App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)<[CustomFeature](../../da/d46/classPart_1_1CustomFeature.html)>
[Part::CustomFeaturePython](../../d2/db9/namespacePart.html#ac6fafa7a6affd4494f3c44e1bcfbd415)  
---  
  
## ◆ FeaturePython

typedef
[App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)<[Feature](../../d7/d7e/classPart_1_1Feature.html)>
[Part::FeaturePython](../../d2/db9/namespacePart.html#aa3a6fc9fd54bbd3394b810fccdbc9dd7)  
---  
  
## ◆ GeometryBoolExtension

using
[Part::GeometryBoolExtension](../../d2/db9/namespacePart.html#a845bc05f7b0ce483de113bc2a1f1f50a)
= typedef
[GeometryDefaultExtension](../../d6/d66/classPart_1_1GeometryDefaultExtension.html)<[bool](../../d9/db9/classbool.html)>  
---  
  
## ◆ GeometryDoubleExtension

using
[Part::GeometryDoubleExtension](../../d2/db9/namespacePart.html#a89ee3abee7bd3c049699df90afd07cff)
= typedef
[GeometryDefaultExtension](../../d6/d66/classPart_1_1GeometryDefaultExtension.html)<double>  
---  
  
## ◆ GeometryIntExtension

using
[Part::GeometryIntExtension](../../d2/db9/namespacePart.html#aa37b088b4c46252162c18f07dea2f21f)
= typedef
[GeometryDefaultExtension](../../d6/d66/classPart_1_1GeometryDefaultExtension.html)<long>  
---  
  
## ◆ GeometryStringExtension

using
[Part::GeometryStringExtension](../../d2/db9/namespacePart.html#aecbc5f1423dbc92050f9e133d973689f)
= typedef
[GeometryDefaultExtension](../../d6/d66/classPart_1_1GeometryDefaultExtension.html)<std::string>  
---  
  
## ◆ Part2DObjectPython

typedef
[App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)<[Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html)>
[Part::Part2DObjectPython](../../d2/db9/namespacePart.html#a13bf980ca80846199b60a9e23a023d43)  
---  
  
## ◆ tEdgeClusterVector

typedef std::vector<std::vector<TopoDS_Edge> >
[Part::tEdgeClusterVector](../../d2/db9/namespacePart.html#af1a1d279943c7841082203dc4b81b100)  
---  
  
## ◆ tEdgeVector

typedef std::vector<TopoDS_Edge>
[Part::tEdgeVector](../../d2/db9/namespacePart.html#ac99453e21c6f8a0552b70bb124709bc8)  
---  
  
## ◆ tMapPntEdge

typedef
std::map<gp_Pnt,[tEdgeVector](../../d2/db9/namespacePart.html#ac99453e21c6f8a0552b70bb124709bc8),[Edgesort_gp_Pnt_Less](../../d4/d19/structPart_1_1Edgesort__gp__Pnt__Less.html)>
[Part::tMapPntEdge](../../d2/db9/namespacePart.html#ac4f90766804e172f3206a721c144c21b)  
---  
  
## ◆ tMapPntEdgePair

typedef
std::pair<gp_Pnt,[tEdgeVector](../../d2/db9/namespacePart.html#ac99453e21c6f8a0552b70bb124709bc8)>
[Part::tMapPntEdgePair](../../d2/db9/namespacePart.html#ac8d6597487c921149a9c47538943e436)  
---  
  
## Function Documentation

## ◆ buildBOPCheckResultVector()

std::vector< std::string > Part::buildBOPCheckResultVector  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[Part::TopoShape::analyze()](../../d8/ded/classPart_1_1TopoShape.html#a3bd8f58104d5ef1732627ebf27fe1f8f).

## ◆ buildShapeEnumVector()

std::vector< std::string > Part::buildShapeEnumVector  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[Part::TopoShape::analyze()](../../d8/ded/classPart_1_1TopoShape.html#a3bd8f58104d5ef1732627ebf27fe1f8f).

## ◆ checkIntersection()

[bool](../../d9/db9/classbool.html) Part::checkIntersection  | ( | const TopoDS_Shape & | _first_ ,   
---|---|---|---  
|  | const TopoDS_Shape & | _second_ ,   
|  | const [bool](../../d9/db9/classbool.html) | _quick_ ,   
|  | const [bool](../../d9/db9/classbool.html) | _touch_is_intersection_  
| ) | |   
  
Check for intersection between the two shapes.

Only solids are guaranteed to work properly There are two modes:

  1. Bounding box check only - quick but inaccurate
  2. Bounding box check plus (if necessary) boolean operation - costly but accurate Return true if the shapes intersect, false if they don't The flag touch_is_intersection decides whether shapes touching at distance zero are regarded as intersecting or not

  1. If set to true, a true check result means that a boolean fuse operation between the two shapes will return a single solid
  2. If set to false, a true check result means that a boolean common operation will return a valid solid If there is any error in the boolean operations, the check always returns false 

## ◆ closestPointsOnLines()

void Part::closestPointsOnLines  | ( | const gp_Lin & | _lin1_ ,   
---|---|---|---  
|  | const gp_Lin & | _lin2_ ,   
|  | gp_Pnt & | _p1_ ,   
|  | gp_Pnt & | _p2_  
| ) | |   
  
References
[draftgeoutils.general::v1()](../../d9/dfd/group__draftgeoutils.html#ga07ad5262ee7b26511c5c3592f2681804).

Referenced by
[tangentialArc()](../../d2/db9/namespacePart.html#a39d5d9d990efef3e6581398defbda87d).

## ◆ create3dCurve()

TopoDS_Edge Part::create3dCurve  | ( | const TopoDS_Edge & | _edge_| ) |   
---|---|---|---|---|---  
  
## ◆ createFilletGeometry()

[GeomArcOfCircle](../../de/d1f/classPart_1_1GeomArcOfCircle.html) * Part::createFilletGeometry  | ( | const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *  | _lineSeg1_ ,   
---|---|---|---  
|  | const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *  | _lineSeg2_ ,   
|  | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _center_ ,   
|  | double  | _radius_  
| ) | |   
  
References
[find2DLinesIntersection()](../../d2/db9/namespacePart.html#a0dd46c09269433a805588c348a585bb0),
[Part::GeomLineSegment::getEndPoint()](../../d9/d6f/classPart_1_1GeomLineSegment.html#aaf6159595594b03452c9eb286282af32),
[Part::GeomLineSegment::getStartPoint()](../../d9/d6f/classPart_1_1GeomLineSegment.html#a208c44a23f9a01d9bb90994a7def3e03),
[Base::Vector3< _Precision
>::ProjectToLine()](../../d1/d13/classBase_1_1Vector3.html#afa7f4034959748405a9a53ae6e70dece),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
and [Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6).

Referenced by
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a).

## ◆ encodeFilename()

std::string Part::encodeFilename  | ( | std::string  | _fn_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Part::TopoShape::exportBrep()](../../d8/ded/classPart_1_1TopoShape.html#aab82fd9a86784f6953397c7e61861e33),
[Part::TopoShape::exportIges()](../../d8/ded/classPart_1_1TopoShape.html#acb51e22e5c24bf679efa2c1c1e6aebbc),
[Part::TopoShape::exportStep()](../../d8/ded/classPart_1_1TopoShape.html#a1f63ead273a699d7808cb8895797a2db),
[Part::TopoShape::exportStl()](../../d8/ded/classPart_1_1TopoShape.html#ad53b8851884371990c63142713b6b885),
[Part::TopoShape::importBrep()](../../d8/ded/classPart_1_1TopoShape.html#ac793cb0bf22baf32c07d0ad0db9eda81),
[Part::TopoShape::importIges()](../../d8/ded/classPart_1_1TopoShape.html#a9eefe54bbb30824e956514de8407dde0),
[Part::TopoShape::importStep()](../../d8/ded/classPart_1_1TopoShape.html#a580c742597911a2ad0b772c14bad16a3),
and
[ImportStepParts()](../../d2/db9/namespacePart.html#a4da179b4c198cc0c74884eb8693d1619).

## ◆ find2DLinesIntersection() [1/2]

[bool](../../d9/db9/classbool.html) Part::find2DLinesIntersection  | ( | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _orig1_ ,   
---|---|---|---  
|  | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _dir1_ ,   
|  | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _orig2_ ,   
|  | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _dir2_ ,   
|  | [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _point_  
| ) | |   
  
References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
and [Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6).

Referenced by
[createFilletGeometry()](../../d2/db9/namespacePart.html#a4e47966fd6c762b34824b98614b76541),
[find2DLinesIntersection()](../../d2/db9/namespacePart.html#a3976a9432420fb14f7f555b63ea3398a),
[findFilletCenter()](../../d2/db9/namespacePart.html#ab01c47ee6de2dab1626ab457c264b394),
and
[suggestFilletRadius()](../../d2/db9/namespacePart.html#a1903069f8259f815f24930b78481a785).

## ◆ find2DLinesIntersection() [2/2]

[bool](../../d9/db9/classbool.html) Part::find2DLinesIntersection  | ( | const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *  | _lineSeg1_ ,   
---|---|---|---  
|  | const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *  | _lineSeg2_ ,   
|  | [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _point_  
| ) | |   
  
References
[find2DLinesIntersection()](../../d2/db9/namespacePart.html#a0dd46c09269433a805588c348a585bb0),
[Part::GeomLineSegment::getEndPoint()](../../d9/d6f/classPart_1_1GeomLineSegment.html#aaf6159595594b03452c9eb286282af32),
and
[Part::GeomLineSegment::getStartPoint()](../../d9/d6f/classPart_1_1GeomLineSegment.html#a208c44a23f9a01d9bb90994a7def3e03).

## ◆ findAllFacesCutBy()

std::vector< [Part::cutFaces](../../df/d39/structPart_1_1cutFaces.html) > Part::findAllFacesCutBy  | ( | const TopoDS_Shape & | _shape_ ,   
---|---|---|---  
|  | const TopoDS_Shape & | _face_ ,   
|  | const gp_Dir & | _dir_  
| ) | |   
  
References
[Part::cutFaces::distsq](../../df/d39/structPart_1_1cutFaces.html#ad6e978a37f9a2bea5cf6cfa3f4a65fbd),
and
[Part::cutFaces::face](../../df/d39/structPart_1_1cutFaces.html#a16840b9d39a287a0fab9ed4b0ee8d31c).

Referenced by
[PartDesign::ProfileBased::getUpToFace()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a53eafe6e2060b9409681ea2b1443139e).

## ◆ findFilletCenter() [1/2]

[bool](../../d9/db9/classbool.html) Part::findFilletCenter  | ( | const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *  | _lineSeg1_ ,   
---|---|---|---  
|  | const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *  | _lineSeg2_ ,   
|  | double  | _radius_ ,   
|  | [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _center_  
| ) | |   
  
References
[findFilletCenter()](../../d2/db9/namespacePart.html#a95cddeb6bcff6c5a4f668e5c976fcfd9),
[Part::GeomLineSegment::getEndPoint()](../../d9/d6f/classPart_1_1GeomLineSegment.html#aaf6159595594b03452c9eb286282af32),
and
[Part::GeomLineSegment::getStartPoint()](../../d9/d6f/classPart_1_1GeomLineSegment.html#a208c44a23f9a01d9bb90994a7def3e03).

Referenced by
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
and
[findFilletCenter()](../../d2/db9/namespacePart.html#a95cddeb6bcff6c5a4f668e5c976fcfd9).

## ◆ findFilletCenter() [2/2]

[bool](../../d9/db9/classbool.html) Part::findFilletCenter  | ( | const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *  | _lineSeg1_ ,   
---|---|---|---  
|  | const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *  | _lineSeg2_ ,   
|  | double  | _radius_ ,   
|  | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _refPnt1_ ,   
|  | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _refPnt2_ ,   
|  | [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _center_  
| ) | |   
  
References
[find2DLinesIntersection()](../../d2/db9/namespacePart.html#a0dd46c09269433a805588c348a585bb0),
[Part::GeomLineSegment::getEndPoint()](../../d9/d6f/classPart_1_1GeomLineSegment.html#aaf6159595594b03452c9eb286282af32),
[Part::GeomLineSegment::getStartPoint()](../../d9/d6f/classPart_1_1GeomLineSegment.html#a208c44a23f9a01d9bb90994a7def3e03),
[Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[Base::Vector3< _Precision
>::ProjectToLine()](../../d1/d13/classBase_1_1Vector3.html#afa7f4034959748405a9a53ae6e70dece),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
and [Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6).

## ◆ getPyShapes() [1/2]

std::vector< [TopoShape](../../d8/ded/classPart_1_1TopoShape.html) > Part::getPyShapes  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
References
[getPyShapes()](../../d2/db9/namespacePart.html#aad31b61eb5c4c2e25ac87ed29d043cb1).

## ◆ getPyShapes() [2/2]

void Part::getPyShapes  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _obj_ ,   
---|---|---|---  
|  | std::vector< [TopoShape](../../d8/ded/classPart_1_1TopoShape.html) > & | _shapes_  
| ) | |   
  
Referenced by
[getPyShapes()](../../d2/db9/namespacePart.html#a48e080b087cffd68a633ef266b177263).

## ◆ ImportIgesParts()

[int](../../d1/da0/classint.html) Part::ImportIgesParts  | ( | [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _pcDoc_ ,   
---|---|---|---  
|  | const char *  | _Name_  
| ) | |   
  
References
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[Base::FileInfo::fileNamePure()](../../dd/d34/classBase_1_1FileInfo.html#aee95cfa273dadbe71b450f3b834a4894),
[App::DocumentObject::Label](../../d2/de4/classApp_1_1DocumentObject.html#a7259f450fea1a74073e626115d46110d),
[Base::SequencerLauncher::next()](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab82c78eee0e3e0f79b3d99950e689b4a),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[Part::PropertyPartShape::setValue()](../../d7/d28/classPart_1_1PropertyPartShape.html#a57ceb747ef13922fe2d4cce37f351c38),
and
[Part::Feature::Shape](../../d7/d7e/classPart_1_1Feature.html#a8a46c66c75a7543cf876b649f442f66a).

## ◆ ImportStepParts()

[int](../../d1/da0/classint.html) Part::ImportStepParts  | ( | [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _pcDoc_ ,   
---|---|---|---  
|  | const char *  | _Name_  
| ) | |   
  
The part shape property.

References
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[encodeFilename()](../../d2/db9/namespacePart.html#a510125d6f7d56e01089f48ef55409621),
[Base::FileInfo::exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[Base::FileInfo::fileNamePure()](../../dd/d34/classBase_1_1FileInfo.html#aee95cfa273dadbe71b450f3b834a4894),
[Part::Feature::getPyObject()](../../d7/d7e/classPart_1_1Feature.html#ae23b16d8ba14ec40c3cd74aca0634f2e),
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964),
[Part::PropertyPartShape::setValue()](../../d7/d28/classPart_1_1PropertyPartShape.html#a57ceb747ef13922fe2d4cce37f351c38),
and
[Part::Feature::Shape](../../d7/d7e/classPart_1_1Feature.html#a8a46c66c75a7543cf876b649f442f66a).

## ◆ initModule()

[PyObject](../../df/d1b/classPyObject.html) * Part::initModule  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::InterpreterSingleton::addModule()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#af556d495376be43c3d93c9a44e6c15d3),
and
[Base::Interpreter()](../../db/d07/namespaceBase.html#a2ee9c987b769c5d1ed5f2fe69b21d2c9).

## ◆ intersect()

[bool](../../d9/db9/classbool.html) Part::intersect  | ( | const gp_Pln & | _pln1_ ,   
---|---|---|---  
|  | const gp_Pln & | _pln2_ ,   
|  | gp_Lin & | _lin_  
| ) | |   
  
Referenced by
[tangentialArc()](../../d2/db9/namespacePart.html#a39d5d9d990efef3e6581398defbda87d).

## ◆ makeFromCurve()

std::unique_ptr< [GeomCurve](../../d4/dc1/classPart_1_1GeomCurve.html) > Part::makeFromCurve  | ( | const Handle(Geom_Curve)& | _c_| ) |   
---|---|---|---|---|---  
  
References
[makeFromTrimmedCurve()](../../d2/db9/namespacePart.html#a87bbc69cb6d56aff7525ea6d696f44cd).

Referenced by
[makeGeometryCurvePy()](../../d2/db9/namespacePart.html#aad18ba984c332dd91b111ce23f558d84).

## ◆ makeFromCurve2d()

std::unique_ptr< [Geom2dCurve](../../d4/da9/classPart_1_1Geom2dCurve.html) > Part::makeFromCurve2d  | ( | Handle(Geom2d_Curve)  | _curve_| ) |   
---|---|---|---|---|---  
  
## ◆ makeFromCurveAdaptor()

std::unique_ptr< [GeomCurve](../../d4/dc1/classPart_1_1GeomCurve.html) > Part::makeFromCurveAdaptor  | ( | const [Adaptor3d_Curve](../../dc/d15/classAdaptor3d__Curve.html) & | _adapt_| ) |   
---|---|---|---|---|---  
  
References
[makeFromTrimmedCurve()](../../d2/db9/namespacePart.html#a87bbc69cb6d56aff7525ea6d696f44cd).

## ◆ makeFromCurveAdaptor2d()

std::unique_ptr< [Geom2dCurve](../../d4/da9/classPart_1_1Geom2dCurve.html) > Part::makeFromCurveAdaptor2d  | ( | const [Adaptor2d_Curve2d](../../d6/da1/classAdaptor2d__Curve2d.html) & | _adapt_| ) |   
---|---|---|---|---|---  
  
References
[makeFromTrimmedCurve2d()](../../d2/db9/namespacePart.html#a0f150892a72445c03ea12bebf7fb4f63).

## ◆ makeFromSurface()

std::unique_ptr< [GeomSurface](../../d7/d6d/classPart_1_1GeomSurface.html) > Part::makeFromSurface  | ( | const Handle(Geom_Surface)& | _s_| ) |   
---|---|---|---|---|---  
  
## ◆ makeFromTrimmedCurve()

std::unique_ptr< [GeomCurve](../../d4/dc1/classPart_1_1GeomCurve.html) > Part::makeFromTrimmedCurve  | ( | const Handle(Geom_Curve)& | _c_ ,   
---|---|---|---  
|  | double  | _f_ ,   
|  | double  | _l_  
| ) | |   
  
References
[makeFromTrimmedCurve()](../../d2/db9/namespacePart.html#a87bbc69cb6d56aff7525ea6d696f44cd).

Referenced by
[makeFromCurve()](../../d2/db9/namespacePart.html#a541c4ec8e2e1179b048904f67f21605f),
[makeFromCurveAdaptor()](../../d2/db9/namespacePart.html#a8c468c061fa8a64a649fcc83bb195292),
[makeFromTrimmedCurve()](../../d2/db9/namespacePart.html#a87bbc69cb6d56aff7525ea6d696f44cd),
and
[makeTrimmedCurvePy()](../../d2/db9/namespacePart.html#ab8440af3725a265f76bf3acad03b4bad).

## ◆ makeFromTrimmedCurve2d()

std::unique_ptr< [Geom2dCurve](../../d4/da9/classPart_1_1Geom2dCurve.html) > Part::makeFromTrimmedCurve2d  | ( | const Handle(Geom2d_Curve)& | _c_ ,   
---|---|---|---  
|  | double  | _f_ ,   
|  | double  | _l_  
| ) | |   
  
References
[makeFromTrimmedCurve2d()](../../d2/db9/namespacePart.html#a0f150892a72445c03ea12bebf7fb4f63).

Referenced by
[makeFromCurveAdaptor2d()](../../d2/db9/namespacePart.html#aedc41c350e793ba243c3388dd2cde48f),
and
[makeFromTrimmedCurve2d()](../../d2/db9/namespacePart.html#a0f150892a72445c03ea12bebf7fb4f63).

## ◆ makeGeometryCurvePy()

const Py::Object Part::makeGeometryCurvePy  | ( | const Handle(Geom_Curve)& | _c_| ) |   
---|---|---|---|---|---  
  
References
[makeFromCurve()](../../d2/db9/namespacePart.html#a541c4ec8e2e1179b048904f67f21605f).

## ◆ makeTrimmedCurvePy()

const Py::Object Part::makeTrimmedCurvePy  | ( | const Handle(Geom_Curve)& | _c_ ,   
---|---|---|---  
|  | double  | _f_ ,   
|  | double  | _l_  
| ) | |   
  
References
[makeFromTrimmedCurve()](../../d2/db9/namespacePart.html#a87bbc69cb6d56aff7525ea6d696f44cd).

## ◆ mapTypeShape()

const std::map< PyTypeObject *, TopAbs_ShapeEnum > Part::mapTypeShape  | ( | vecTypeShape.  | _begin_(),   
---|---|---|---  
|  | vecTypeShape.  | _end_()   
| ) | |   
  
## ◆ ReadColors()

[bool](../../d9/db9/classbool.html) Part::ReadColors  | ( | const Handle(XSControl_WorkSession) & | _WS_ ,   
---|---|---|---  
|  | std::map< [int](../../d1/da0/classint.html), Quantity_Color > & | _hash_col_  
| ) | |   
  
## ◆ ReadNames()

[bool](../../d9/db9/classbool.html) Part::ReadNames  | ( | const Handle(XSControl_WorkSession) & | _WS_| ) |   
---|---|---|---|---|---  
  
## ◆ shape2pyshape() [1/2]

Py::Object Part::shape2pyshape  | ( | const TopoDS_Shape & | _shape_| ) |   
---|---|---|---|---|---  
  
References
[shape2pyshape()](../../d2/db9/namespacePart.html#a7ddedec80f61edb78bd71990c25fe2da).

Referenced by
[Part::TopoShape::getPySubShape()](../../d8/ded/classPart_1_1TopoShape.html#a1a27a174e71043c90bbc832fddc895f5),
[Part::Datum::getSubObject()](../../db/d0b/classPart_1_1Datum.html#ac5c48627e7edd4fde0e66a86603a0ca8),
[Part::Feature::getSubObject()](../../d7/d7e/classPart_1_1Feature.html#adf8612028b19407896b5ba0e1fab0d5d),
[PartDesign::CoordinateSystem::getSubObject()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#aeb5d09866ebc21adafb8ee43acc9205b),
and
[shape2pyshape()](../../d2/db9/namespacePart.html#a7ddedec80f61edb78bd71990c25fe2da).

## ◆ shape2pyshape() [2/2]

Py::Object Part::shape2pyshape  | ( | const [TopoShape](../../d8/ded/classPart_1_1TopoShape.html) & | _shape_| ) |   
---|---|---|---|---|---  
  
## ◆ ShapeTypeFromPyType()

| static TopAbs_ShapeEnum Part::ShapeTypeFromPyType  | ( | PyTypeObject *  | _pyType_| ) |   
---|---|---|---|---|---  
static  
  
References
[vecTypeShape](../../d2/db9/namespacePart.html#a76bcb91c8af6fdcec5a6c46a5af3e7a2).

## ◆ sort_Edges()

std::list< TopoDS_Edge > Part::sort_Edges  | ( | double  | _tol3d_ ,   
---|---|---|---  
|  | std::list< TopoDS_Edge > & | _edges_  
| ) | |   
  
References
[Part::EdgePoints::edge](../../db/dda/structPart_1_1EdgePoints.html#a077190e8d524a7d5cc30182e2505f1b2),
[Part::EdgePoints::it](../../db/dda/structPart_1_1EdgePoints.html#a4e2bafa8701655d2502a04352a5661eb),
[Part::EdgePoints::v1](../../db/dda/structPart_1_1EdgePoints.html#aebfdd41a8f4ca6b3d31264c4c86d71b2),
and
[Part::EdgePoints::v2](../../db/dda/structPart_1_1EdgePoints.html#a4d62ea88a24625865e0730d383f9dff9).

## ◆ suggestFilletRadius()

double Part::suggestFilletRadius  | ( | const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *  | _lineSeg1_ ,   
---|---|---|---  
|  | const [GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html) *  | _lineSeg2_ ,   
|  | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _refPnt1_ ,   
|  | const [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) & | _refPnt2_  
| ) | |   
  
References
[find2DLinesIntersection()](../../d2/db9/namespacePart.html#a0dd46c09269433a805588c348a585bb0),
[Part::GeomLineSegment::getEndPoint()](../../d9/d6f/classPart_1_1GeomLineSegment.html#aaf6159595594b03452c9eb286282af32),
[Part::GeomLineSegment::getStartPoint()](../../d9/d6f/classPart_1_1GeomLineSegment.html#a208c44a23f9a01d9bb90994a7def3e03),
[Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[Base::Vector3< _Precision
>::ProjectToLine()](../../d1/d13/classBase_1_1Vector3.html#afa7f4034959748405a9a53ae6e70dece),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
and [Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6).

Referenced by
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084).

## ◆ supportedSTEPSchemes()

std::list< std::string > Part::supportedSTEPSchemes  | ( | | ) |   
---|---|---|---|---  
  
## ◆ tangentialArc()

[bool](../../d9/db9/classbool.html) Part::tangentialArc  | ( | const gp_Pnt & | _p0_ ,   
---|---|---|---  
|  | const gp_Vec & | _v0_ ,   
|  | const gp_Pnt & | _p1_ ,   
|  | gp_Pnt & | _c_ ,   
|  | gp_Dir & | _axis_  
| ) | |   
  
References
[closestPointsOnLines()](../../d2/db9/namespacePart.html#a389ea20c7863562ce3513947b319f9d3),
[intersect()](../../d2/db9/namespacePart.html#ae528b2bf4eca3b55cee601b84af58f8c),
and
[draftgeoutils.general::v1()](../../d9/dfd/group__draftgeoutils.html#ga07ad5262ee7b26511c5c3592f2681804).

Referenced by
[Part::TangentialArc::TangentialArc()](../../d2/d99/classPart_1_1TangentialArc.html#a651ddd6b49960fc4bbdc341de994bd37).

## Variable Documentation

## ◆ angleRangeU

const
[App::PropertyQuantityConstraint::Constraints](../../df/dd1/structApp_1_1PropertyQuantityConstraint_1_1Constraints.html)
Part::angleRangeU = {0.0, 360.0, 1.0}  
---  
  
Referenced by
[Part::Cone::Cone()](../../d2/d8f/classPart_1_1Cone.html#aec709e915b3271a750d420b14b215bfb),
[Part::Cylinder::Cylinder()](../../dd/d12/classPart_1_1Cylinder.html#a01dc978cb576f834b9545e43d4dad2a2),
[Part::Ellipsoid::Ellipsoid()](../../d4/dc8/classPart_1_1Ellipsoid.html#a8aba92dbd635c581c3a5e96f285dd651),
[Part::Revolution::Revolution()](../../d3/d17/classPart_1_1Revolution.html#ad4ecc2008e08f7c54b4fe92215c77bbb),
[Part::Sphere::Sphere()](../../dc/d57/classPart_1_1Sphere.html#a890a63ff583cb88e7ec4e840b4ef5eb9),
and
[Part::Torus::Torus()](../../db/d42/classPart_1_1Torus.html#ac1767993341e35d3a38676727a80047e).

## ◆ angleRangeV

const
[App::PropertyQuantityConstraint::Constraints](../../df/dd1/structApp_1_1PropertyQuantityConstraint_1_1Constraints.html)
Part::angleRangeV = {-90.0, 90.0, 1.0}  
---  
  
Referenced by
[Part::Ellipsoid::Ellipsoid()](../../d4/dc8/classPart_1_1Ellipsoid.html#a8aba92dbd635c581c3a5e96f285dd651),
and
[Part::Sphere::Sphere()](../../dc/d57/classPart_1_1Sphere.html#a890a63ff583cb88e7ec4e840b4ef5eb9).

## ◆ apexRange

const
[App::PropertyQuantityConstraint::Constraints](../../df/dd1/structApp_1_1PropertyQuantityConstraint_1_1Constraints.html)
Part::apexRange = {-90.0, 90.0, 0.1}  
---  
  
Referenced by
[Part::Helix::Helix()](../../df/d49/classPart_1_1Helix.html#af5b3edc469728ac5981e35e29412b61c).

## ◆ PartExceptionOCCConstructionError

| [PyObject](../../df/d1b/classPyObject.html) *
Part::PartExceptionOCCConstructionError  
---  
extern  
  
## ◆ PartExceptionOCCDimensionError

| [PyObject](../../df/d1b/classPyObject.html) *
Part::PartExceptionOCCDimensionError  
---  
extern  
  
## ◆ PartExceptionOCCDomainError

| [PyObject](../../df/d1b/classPyObject.html) *
Part::PartExceptionOCCDomainError  
---  
extern  
  
## ◆ PartExceptionOCCError

| [PyObject](../../df/d1b/classPyObject.html) * Part::PartExceptionOCCError  
---  
extern  
  
## ◆ PartExceptionOCCRangeError

| [PyObject](../../df/d1b/classPyObject.html) *
Part::PartExceptionOCCRangeError  
---  
extern  
  
## ◆ quantityRange

const
[App::PropertyQuantityConstraint::Constraints](../../df/dd1/structApp_1_1PropertyQuantityConstraint_1_1Constraints.html)
Part::quantityRange = {0.0, FLT_MAX, 0.1}  
---  
  
Referenced by
[Part::Ellipsoid::Ellipsoid()](../../d4/dc8/classPart_1_1Ellipsoid.html#a8aba92dbd635c581c3a5e96f285dd651),
[Part::Helix::Helix()](../../df/d49/classPart_1_1Helix.html#af5b3edc469728ac5981e35e29412b61c),
[Part::Sphere::Sphere()](../../dc/d57/classPart_1_1Sphere.html#a890a63ff583cb88e7ec4e840b4ef5eb9),
[Part::Spiral::Spiral()](../../d2/d3f/classPart_1_1Spiral.html#aa484d105df5310c5e70d0bee2b494e6b),
and
[Part::Torus::Torus()](../../db/d42/classPart_1_1Torus.html#ac1767993341e35d3a38676727a80047e).

## ◆ torusRangeV

const
[App::PropertyQuantityConstraint::Constraints](../../df/dd1/structApp_1_1PropertyQuantityConstraint_1_1Constraints.html)
Part::torusRangeV = {-180.0, 180.0, 1.0}  
---  
  
Referenced by
[Part::Torus::Torus()](../../db/d42/classPart_1_1Torus.html#ac1767993341e35d3a38676727a80047e).

## ◆ vecTypeShape

const std::vector<std::pair<PyTypeObject*, TopAbs_ShapeEnum> >
Part::vecTypeShape  
---  
  
**Initial value:**

= {

{&TopoShapeCompoundPy::Type, TopAbs_COMPOUND},

{&TopoShapeCompSolidPy::Type, TopAbs_COMPSOLID},

{&TopoShapeSolidPy::Type, TopAbs_SOLID},

{&TopoShapeShellPy::Type, TopAbs_SHELL},

{&TopoShapeFacePy::Type, TopAbs_FACE},

{&TopoShapeWirePy::Type, TopAbs_WIRE},

{&TopoShapeEdgePy::Type, TopAbs_EDGE},

{&TopoShapeVertexPy::Type, TopAbs_VERTEX},

{&TopoShapePy::Type, TopAbs_SHAPE}

}

Referenced by
[ShapeTypeFromPyType()](../../d2/db9/namespacePart.html#a8e1161389f1704ff900df16fa7f95d17).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

