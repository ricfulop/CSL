---
url: https://freecad.github.io/SourceDoc/dc/d0d/classautomotive__design_1_1derived__unit.html
scraped_at: 2025-09-08T15:03:34.646724
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [derived_unit](../../dc/d0d/classautomotive__design_1_1derived__unit.html)

[List of all members](../../d3/da9/classautomotive__design_1_1derived__unit-members.html) | Public Member Functions | Public Attributes

automotive_design.derived_unit Class Reference

##  Public Member Functions  
  
---  
def | [elements](../../dc/d0d/classautomotive__design_1_1derived__unit.html#aab874c247306dcd7abced1235d2876c3) ()  
def | [name](../../dc/d0d/classautomotive__design_1_1derived__unit.html#ae954fc1416da969a5c203742bba99cb6) ()  
def | [wr1](../../dc/d0d/classautomotive__design_1_1derived__unit.html#a0f657919a22adecb60367513268f0487) (self)  
def | [wr2](../../dc/d0d/classautomotive__design_1_1derived__unit.html#a7f1e061d4f5d9248683e8561454fe588) (self)  
  
##  Public Attributes  
  
---  
|
[elements](../../dc/d0d/classautomotive__design_1_1derived__unit.html#a2465083a99c70793fc515bce4a11ccd3)  
  
## Detailed Description

    
    
    Entity derived_unit definition.
    
        :param elements
        :type elements:SET(1,None,'derived_unit_element', scope = schema_scope)
    
        :param name
        :type name:label

## Member Function Documentation

## ◆ elements()

def automotive_design.derived_unit.elements  | ( | | ) |   
---|---|---|---|---  
  
References SMESH_ProxyMesh::SubMesh._elements, ElementBndBoxTree._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.derived_unit._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.data_environment._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.procedural_representation_sequence._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_plane._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.geometric_set._elements,
automotive_design.data_environment._elements,
automotive_design.derived_unit._elements,
automotive_design.annotation_plane._elements,
automotive_design.geometric_set._elements,
config_control_design.geometric_set._elements,
ifc2x3.ifcgeometricset._elements, ifc2x3.ifcderivedunit._elements,
ifc4.ifcgeometricset._elements, and ifc4.ifcderivedunit._elements.

Referenced by
[ifc2x3.ifcgeometricset.dim()](../../dc/dab/classifc2x3_1_1ifcgeometricset.html#af569a780b93b69b4dce81b08ddd66f89),
[ifc4.ifcgeometricset.dim()](../../d1/d95/classifc4_1_1ifcgeometricset.html#a795b14ef2879e9acc0c066d66e122b9b),
[ifc2x3.ifcderivedunit.dimensions()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#abfb7d2614cbad7ba363d5b3c5eb5d470),
[ifc4.ifcderivedunit.dimensions()](../../d3/d76/classifc4_1_1ifcderivedunit.html#aa316302961670925c24a6da591f61b31),
[automotive_design.derived_unit.wr1()](../../dc/d0d/classautomotive__design_1_1derived__unit.html#a0f657919a22adecb60367513268f0487),
[ifc2x3.ifcderivedunit.wr1()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#a9187776e238d15570720320bf6875864),
and
[ifc4.ifcderivedunit.wr1()](../../d3/d76/classifc4_1_1ifcderivedunit.html#a3c29186705cf96c60831affaf117186e).

## ◆ name()

def automotive_design.derived_unit.name  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.get_name_value()](../../d4/ddf/namespaceautomotive__design.html#ae730b907f9032c797025ed6d3d4fb54e).

Referenced by
[draftguitools.gui_groups.Ui_AddNamedGroup.accept()](../../d3/df7/classdraftguitools_1_1gui__groups_1_1Ui__AddNamedGroup.html#a9ea5973817eab7d74792f5b109a01466),
[prototype.Node.addtofreecad()](../../d2/d62/classprototype_1_1Node.html#adc095cc5636da029d1e0d9cef8859701),
[Addon.Addon.disable()](../../d8/d91/classAddon_1_1Addon.html#ae714705a38afe9f13cd2b17580178b31),
[Addon.Addon.enable()](../../d8/d91/classAddon_1_1Addon.html#a79d327ec9a0b4e85e9e96cfad4003ed6),
[addonmanager_macro.Macro.filename()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a5de4e6a1f3c41dce24066111955cd706),
[gzip_utf8.GzipFile.filename()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ab56fe84a4eb08c44e7a0026280c01229),
[addonmanager_macro.Macro.fill_details_from_code()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a49b8d021a9b8255f8a490e880eb15489),
[addonmanager_macro.Macro.fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[Addon.Addon.get_cached_icon_filename()](../../d8/d91/classAddon_1_1Addon.html#a7b026027a2904028032edbe3e99e2cbd),
[ifc4.ifcapproval.hasidentifierorname()](../../df/d91/classifc4_1_1ifcapproval.html#a54f558ba3b17fad5fc6579e9d5f50947),
[addonmanager_macro.Macro.install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
[Addon.Addon.is_disabled()](../../d8/d91/classAddon_1_1Addon.html#a5752a95fcf0c51ed06f9841b381d3e50),
[femsolver.elmer.sifio.Section.keys()](../../db/dab/classfemsolver_1_1elmer_1_1sifio_1_1Section.html#ab5b099447f66f33743850697f0e20de4),
[automotive_design.si_unit.named_unit_dimensions()](../../d5/d77/classautomotive__design_1_1si__unit.html#a68eb7954eb09daa334bc8f2c2abbe5f9),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.output()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aeedd5f59969cc27432880d1916f3d7f9),
[prototype.Node.pprint()](../../d2/d62/classprototype_1_1Node.html#a5ae181c34e48238d2364b0ba4960c252),
[prototype.Node.pprint2()](../../d2/d62/classprototype_1_1Node.html#aaedcc4ba1fb305c7ddcc025235043cd5),
[PathScripts.PathSetupSheetGui.OpTaskPanel.propertyGroup()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a69cbbaadcb9cff7b526af2c743041d7b),
[PathScripts.PathSetupSheetGui.OpTaskPanel.propertyName()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#ad9bd0e0149d1bc42fc8e89a290de4910),
[PathScripts.PathJobGui.TaskPanel.reject()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a54fd97ba9b0060fa8fed8a43c360da0c),
[addonmanager_macro.Macro.remove()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ad13245288f8beb62d92cb458a2d2ce05),
[Addon.Addon.to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
[ifc2x3.ifcexternalreference.wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc2x3.ifcdocumentreference.wr1()](../../df/dd6/classifc2x3_1_1ifcdocumentreference.html#a7d5fdb1cb0dee567c44834b868c5cdad),
[ifc4.ifcexternalreference.wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
[ifc4.ifcdocumentreference.wr1()](../../d7/d2b/classifc4_1_1ifcdocumentreference.html#a8779d74c67e647441d1fb20c76f44f97),
and
[automotive_design.general_property_association.wr2()](../../d2/df3/classautomotive__design_1_1general__property__association.html#ae7f46462c59bc4e541a5d2511631eb65).

## ◆ wr1()

def automotive_design.derived_unit.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented in
[automotive_design.area_unit](../../de/da4/classautomotive__design_1_1area__unit.html#ae26534b05093b7a6079a48cf6977d24e),
and
[automotive_design.volume_unit](../../d7/d75/classautomotive__design_1_1volume__unit.html#a88641d4fb8f77c5ee5bef035f2a7bc21).

References std::deque< T >.elements, std::list< T >.elements, std::deque<
App::Color >.elements, std::map< CutDimensionKey, CutDimensionSet >.elements,
std::vector< featureStatus >.elements, std::deque< std::string >.elements,
std::map< QString, GroupInfo >.elements, std::map< int, App::Transaction *
>.elements, std::vector< ObjectPtr >.elements, std::unordered_map< SoAction *,
Gui::SoFCSelectionRoot::Stack >.elements, std::unordered_multimap< K, T
>.elements, std::list< const SMDS_MeshGroup * >.elements, std::unordered_map<
SoNode *, int >.elements, std::unordered_map< App::DocumentObject *,
DocumentObjectDataPtr >.elements, std::vector< QCheckBox * >.elements,
std::vector< MeshHelpPoint >.elements, std::list< App::SubObjectT >.elements,
std::vector< TEdge * >.elements, std::priority_queue< T >.elements,
std::vector< std::pair< std::string, std::vector< App::Property * > >
>.elements, std::map< int, Handle(ShapeAnalysis_Surface)>.elements, std::map<
TNodeSet, std::list< std::list< int > > >.elements, std::vector<
RestoredExpression >.elements, std::list< Cloud::CloudReader::FileEntry *
>.elements, std::vector< Sketcher::Sketch::ConstrDef >.elements, std::map<
Marker, int >.elements, std::vector< Simplify::Triangle >.elements, std::list<
QTranslator * >.elements, std::vector< QListWidgetItem * >.elements,
std::vector< std::string >.elements, std::list< std::vector< Base::Vector3 >
>.elements, std::vector< Vector2f >.elements, std::unordered_map<
App::DocumentObject *, std::set< DocumentObjectDataPtr > >.elements,
std::vector< Base::Placement >.elements, std::span< T >.elements, std::list<
Gui::GLGraphicsItem * >.elements, std::forward_list< T >.elements, std::map<
int, PSurface >.elements, std::map< App::ObjectIdentifier, bool >.elements,
std::map< const Gui::Document *, std::shared_ptr< Model > >.elements,
std::list< App::Transaction * >.elements, std::map< eMapMode,
refTypeStringList >.elements, std::vector< BasicJsonType * >.elements,
std::stack< T >.elements, std::vector< vtkIdType >.elements, std::vector< Path
>.elements, std::vector< Mesh::PointIndex >.elements, std::list< Gui::BaseView
* >.elements, std::map< QString, ConstrIconBBVec >.elements, std::deque<
Gui::SelectionChanges >.elements, std::vector< App::Expression * >.elements,
std::map< SMDS_MeshGroup *, std::string >.elements, std::list< IslandAndOffset
* >.elements, std::vector< unsigned long >.elements, std::vector<
std::shared_ptr< Sketcher::SolverGeometryExtension > >.elements, std::list<
std::vector< int > >.elements, std::map< Sketcher::GeoElementId, int
>.elements, std::map< qint64, QIcon >.elements, std::vector< App::Color
>.elements, std::map< const App::Property *, Gui::ViewProvider * >.elements,
std::array< std::char_traits< char >::int_type, 4 >.elements, std::vector<
TechDraw::LineSet >.elements, std::vector< StdMeshers_IJNodeMap >.elements,
std::map< const App::DocumentObject *, boost::signals2::scoped_connection
>.elements, std::list< std::shared_ptr< QTranslator > >.elements, std::vector<
Connection >.elements, std::vector< SMDS_MeshNode * >.elements, std::map< int,
GLuint >.elements, std::vector< std::vector< double * > >.elements,
std::vector< CounterSinkDimension >.elements, std::vector<
TechDrawGui::QGMarker * >.elements, std::map< std::string, App::Document *
>.elements, std::vector< TDF_Label >.elements, std::list< PyObject *
>.elements, std::map< int, App::Color >.elements, std::vector<
e57::SourceDestBuffer >.elements, std::unordered_map< K, T >.elements,
std::list< AdaptivePath::AdaptiveOutput >.elements, std::vector< VertexPtr
>.elements, std::map< App::ObjectIdentifier, App::ObjectIdentifier >.elements,
std::vector< TechDraw::VertexPtr >.elements, std::allocator< T >.elements,
std::list< SMESHDS_Command * >.elements, std::list< SMESH_HypothesisPtr
>.elements, std::vector< std::unique_ptr< App::PropertyLinkSub > >.elements,
std::map< int, std::string >.elements, std::vector< string >.elements,
std::list< const SMESHDS_Hypothesis * >.elements, std::deque< gp_Pnt
>.elements, std::vector< T >.elements, std::multimap< K, T >.elements,
std::map< double *, std::tuple< int, Sketcher::PointPos, int > >.elements,
std::vector< Vertex >.elements, std::map< const App::DocumentObject *,
Mesh::MeshObject >.elements, std::map< int, int >.elements, std::queue< T
>.elements, std::map< SMDS_MeshGroup *, int >.elements, std::vector<
FaceQuadStruct::Side::Contact >.elements, std::array< char, 512 >.elements,
std::vector< bool >.elements, std::valarray< T >.elements, std::deque<
App::ObjectIdentifier::Component >.elements, std::vector<
TechDraw::BaseGeomPtr >.elements, std::map< std::string, std::string
>.elements, std::list< constSMDS_MeshGroup * >.elements, std::vector<
std::vector< std::size_t > >.elements, std::map< uint32_t,
SoBrepFaceSet::VBO::Buffer >.elements, std::map< int, DriverMED_FamilyPtr
>.elements, std::deque< float >.elements, std::vector< App::Property *
>.elements, std::vector< GeomAdaptor_Curve >.elements, std::stack< PropertyTag
>.elements, std::unordered_map< std::string, int >.elements, std::vector<
MeshCore::MeshGeomFacet >.elements, std::map< Gui::ViewProvider *, bool
>.elements, std::list< CurveTree * >.elements, std::map< int, SMESH_Hypothesis
* >.elements, std::unordered_map< const App::Document *, std::map< std::pair<
const App::DocumentObject *, std::string >, TopoShape > >.elements,
std::unordered_map< std::string, std::vector< App::ObjectIdentifier >
>.elements, std::unordered_map< TDF_Label, std::string, Import::LabelHasher
>.elements, std::vector< Vector3f >.elements, std::unordered_map< TDF_Label,
std::vector< std::string >, Import::LabelHasher >.elements, std::vector<
segment_type >.elements, std::vector< _Tp, std::allocator< _Tp > >.elements,
std::unordered_map< std::string, std::vector< long > >.elements,
std::unordered_map< App::Property *, QPointer<
Gui::PropertyEditor::PropertyItem > >.elements, std::unordered_map< SoNode *,
Pointer >.elements, std::map< SoNode *, TBoundary >.elements,
std::unordered_map< const App::DocumentObject *,
boost::signals2::scoped_connection >.elements, std::list< CVertex >.elements,
std::unordered_map< long, App::DocumentObject * >.elements, std::array<
Gui::CoinPtr< SoSeparator >, LinkView::SnapshotMax >.elements, std::map<
Prism_3D::TNode, TNodeColumn >.elements, std::map< double, gp_XY >.elements,
std::map< int, std::pair< TParam2ColumnMap *, bool > >.elements, std::vector<
char, std::allocator< char > >.elements, std::map< std::string, SheetObserver
* >.elements, std::map< const App::Property *, App::CellAddress >.elements,
std::vector< PartGui::DimSelections::DimSelection >.elements, std::vector<
App::DocumentObjectT >.elements, std::map< HANDLE, TInputData >.elements,
std::vector< StdMeshers_Quadrangle_2D::ForcedPoint >.elements, std::map<
App::CellAddress, std::string >.elements, std::vector< TInt, std::allocator<
TInt > >.elements, std::map< App::CellAddress, std::set< std::string >
>.elements, std::vector< FemFace * >.elements, std::vector<
App::ObjectIdentifier::Component >.elements, std::list< std::unique_ptr<
std::string > >.elements, std::vector< boost::signals2::scoped_connection
>.elements, std::vector< App::DocumentObject * >.elements, std::list< double
>.elements, std::vector< App::ColorModelPack >.elements, std::vector< double
>.elements, std::vector< TPath >.elements, std::vector< IntPoint >.elements,
std::vector< unsigned char >.elements, std::vector< SMESH_subMesh *
>.elements, std::vector< SbVec2s >.elements, std::vector< SoFCSelectionRoot *
>.elements, std::deque< Base::Vector3 >.elements, std::map< App::CellAddress,
App::CellAddress >.elements, std::map< const Gui::ViewProviderDocumentObject
*, IndexSet >.elements, std::vector< ButtonIconPairType >.elements,
std::array< const char *, GeometryMode::NumGeometryMode >.elements, std::map<
EGeometrieElement, PTMeshValue >.elements, std::vector< TopoDS_Shape
>.elements, std::array< const char *, InternalType::NumInternalGeometryType
>.elements, std::array< const char *, NumFlags >.elements, std::array< const
char *, ConstraintType::NumConstraintTypes >.elements, std::vector<
Part::TopoShape * >.elements, std::array< Gui::CoinPtr< SoSwitch >,
LinkView::SnapshotMax >.elements, std::list< TopoDS_Edge >.elements,
std::unordered_map< const App::DocumentObject *, Gui::ViewProvider *
>.elements, std::vector< std::vector< TopoDS_Edge > >.elements, std::map<
Stack, SoFCSelectionContextBasePtr, StackComp >.elements, std::vector< Join *
>.elements, std::map< int, std::vector< int > >.elements, std::array< T
>.elements, std::vector< std::pair< Gui::Command *, size_t > >.elements,
std::map< GeomAbs_SurfaceType, FaceVectorType >.elements, std::unordered_map<
const void *, PyObject * >.elements, std::vector< Gui::Breakpoint >.elements,
std::map< TopoDS_Edge, std::vector< FaceSplitEdge >, TopoDSLess< TopoDS_Edge >
>.elements, std::map< const App::DocumentObject *, std::vector< std::string >
>.elements, std::map< Standard_Integer, std::string >.elements, std::map<
double *, int >.elements, std::vector< TechDraw::WalkerEdge >.elements,
std::map< Standard_Integer, Quantity_ColorRGBA >.elements, std::map<
ObjectIdentifier, ObjectIdentifier >.elements, std::map< long, std::vector<
App::Color > >.elements, std::map< int, ToolPtr >.elements, std::map<
uint32_t, GLuint >.elements, std::vector< SMDS_MeshFace * >.elements,
std::map< std::string, std::unique_ptr< LinkView::SubInfo > >.elements,
std::vector< const SMESHDS_SubMesh * >.elements, std::vector< gp_Pnt
>.elements, std::map< HANDLE, unsigned long >.elements, std::map<
EGeometrieElement, PProfileInfo >.elements, std::list< std::string >.elements,
std::map< int, SMESH_subMesh * >.elements, std::vector< std::unique_ptr<
LinkView::Element > >.elements, std::unordered_map< App::DocumentObject *,
std::bitset< 32 > >.elements, std::list< GetCurveItem >.elements, std::map<
int, bool >.elements, std::vector< TechDraw::Wire * >.elements, std::vector<
geoff_geometry::SpanVertex * >.elements, std::vector< Component * >.elements,
std::map< Part::Feature *, std::vector< App::Color > >.elements, std::map<
App::CellAddress, Spreadsheet::Cell * >.elements, std::map< std::string,
std::tuple< std::function< void(const std::string &string, App::Property *)>,
App::Property * > >.elements, std::list< std::list< int > >.elements,
std::list< TPoint * >.elements, std::vector< ShapePairType >.elements,
std::map< Sketcher::GeoElementId, SketcherGui::MultiFieldId >.elements,
std::map< EGeometrieElement, TInt >.elements, std::map< std::pair< const
App::DocumentObject *, std::string >, TopoShape >.elements,
std::unordered_map< std::string, bool >.elements, std::map< int, std::list<
TPoint * > >.elements, std::map< TInt, TFloatVector >.elements, std::map<
size_t, App::Color >.elements, std::vector< Sketcher::ConstraintIds
>.elements, std::map< int, GeomAPI_ProjectPointOnSurf * >.elements, std::map<
int, double >.elements, std::map< TBiQuad, const SMDS_MeshNode * >.elements,
std::map< std::string, App::CellAddress >.elements, std::map< int, const
SMDS_MeshNode * >.elements, std::map< int, SUBMESH * >.elements, std::map<
int, SMESHDS_Mesh * >.elements, std::map< SMDS_MeshFace *, int >.elements,
std::map< std::string, double >.elements, std::vector< float >.elements,
std::map< Link, int >.elements, std::vector< Py::Object >.elements,
std::vector< QWidget * >.elements, std::vector< NodeImplSharedPtr >.elements,
std::vector< Gui::TaskView::TaskWatcher * >.elements, std::vector< SbVec2f
>.elements, std::vector< long >.elements, std::vector< const char *
>.elements, std::vector< std::pair< std::string, std::string > >.elements,
std::vector< Inspection::InspectNominalGeometry * >.elements, std::vector<
TOC_Entry >.elements, std::vector< GCS::ArcOfParabola >.elements, std::vector<
point3D >.elements, std::vector< TFloat, std::allocator< TFloat > >.elements,
std::vector< Sketcher::GeoElementId >.elements, std::vector< FacetIndex
>.elements, std::vector< PointIndex >.elements, std::vector< std::vector<
Gui::SelectionObject > >.elements, std::vector< unsigned int >.elements,
std::vector< std::pair< FacetIndex, FacetIndex > >.elements, std::vector<
MeshSegment >.elements, std::vector< int32_t >.elements, std::vector< uint32_t
>.elements, std::vector< FaceSplitEdge >.elements, std::vector< FaceVectorType
>.elements, std::vector< Handle(Geom2d_Curve)>.elements, std::vector< GLubyte
>.elements, std::vector< Face * >.elements, std::vector< QOpenGLTexture *
>.elements, std::vector< std::vector< Base::Vector3 > >.elements, std::vector<
TopoDS_Edge >.elements, std::vector< TopoDS_Wire >.elements, std::vector<
GCS::Constraint * >.elements, std::vector< SMESHDS_SubMesh * >.elements,
std::vector< TechDraw::embedItem >.elements, std::vector< const
SMDS_MeshElement * >.elements, std::vector< FaceQuadStruct::Side >.elements,
std::vector< uvPtStruct >.elements, std::vector< vtkSmartPointer< vtkAlgorithm
> >.elements, std::vector< std::set< std::pair< int, Sketcher::PointPos > >
>.elements, std::vector< FemGui::TaskPostBox * >.elements, std::vector< Point
>.elements, std::vector< std::vector< int > >.elements, std::vector< double *
>.elements, std::vector< int >.elements, std::vector< MAP_pD_pD >.elements,
std::vector< TParam2ColumnMap >.elements, std::vector< std::shared_ptr<
Part::GeometryExtension > >.elements, std::vector< class Gui::SignalConnect *
>.elements, std::vector< GCS::SubSystem * >.elements, std::vector< VEC_pD
>.elements, std::vector< std::vector< GCS::Constraint * > >.elements,
std::vector< QBrush >.elements, std::vector< std::shared_ptr< FilterBase >
>.elements, std::vector< TNodeColumn * >.elements, std::vector<
Gui::ViewProvider * >.elements, std::vector< App::SubObjectT >.elements,
std::vector< Gui::SelectionObject >.elements, std::vector< QTreeWidgetItem *
>.elements, std::vector< std::pair< LineType, std::string > >.elements,
std::vector< Simplify::Ref >.elements, std::vector< Node_ObjectPtr >.elements,
std::vector< TechDraw::incidenceItem >.elements, std::vector< PointPos
>.elements, std::vector< SketcherGui::AutoConstraint >.elements, std::vector<
std::vector< SketcherGui::AutoConstraint > >.elements, std::vector<
Sketcher::ConstraintType >.elements, std::vector< std::vector< unsigned int >
>.elements, std::vector< Vector3< double > >.elements, std::vector< SoMaterial
* >.elements, std::vector< SoCoordinate3 * >.elements, std::vector<
SoMarkerSet * >.elements, std::vector< SoLineSet * >.elements, std::vector<
App::Range >.elements, std::vector< std::pair< double, double > >.elements,
std::vector< TSideFace * >.elements, std::vector< TechDraw::FacePtr
>.elements, std::vector< FacePtr >.elements, std::vector< GCS::BSpline
>.elements, std::vector< TechDraw::ewWire >.elements, std::vector< QPointF
>.elements, std::vector< QGraphicsPathItem * >.elements, std::vector<
TechDrawGui::TemplateTextField * >.elements, std::vector< e57::DecodeChannel
>.elements, std::vector< std::shared_ptr< e57::Encoder > >.elements,
std::vector< e57::NameSpace >.elements, std::vector<
e57::PacketReadCache::CacheEntry >.elements, std::vector< char_type
>.elements, std::vector< CharType >.elements, std::vector< std::function<
double(double)> >.elements, std::queue< SoMouseButtonEvent >.elements,
std::priority_queue< cInt >.elements, std::stack< status >.elements,
std::vector< int * >.elements, std::vector< CounterBoreDimension >.elements,
std::vector< App::PropertyLinkSub * >.elements, std::vector<
Gui::ViewProviderOrigin * >.elements, std::vector< QString >.elements,
std::vector< TechDraw::BezierSegment >.elements, std::vector< SShapeStore
>.elements, std::vector< Attacher::eMapMode >.elements, std::vector<
FunctionMapType >.elements, std::vector< size_t >.elements, std::vector<
point_type >.elements, std::vector< TQuadList >.elements, std::vector<
App::ObjectIdentifier >.elements, std::vector< Simplify::Vertex >.elements,
std::vector< SMDS_MeshCell * >.elements, std::vector< MeshCore::CurvatureInfo
>.elements, std::vector< const SMDS_MeshNode * >.elements, std::vector<
TClassifier * >.elements, std::stack< ParseInfo >.elements, std::vector<
gp_XYZ >.elements, std::vector< SUBMESH * >.elements, std::vector< TPoint
>.elements, std::vector< GCS::Point >.elements, std::vector< GCS::Line
>.elements, std::vector< GCS::Arc >.elements, std::vector< BaseGeomPtr
>.elements, std::vector< GCS::Circle >.elements, std::vector< GCS::Ellipse
>.elements, std::vector< SoDrawStyle * >.elements, std::vector<
GCS::ArcOfHyperbola >.elements, std::map< gp_Pnt, tEdgeVector,
Edgesort_gp_Pnt_Less >.elements, std::map< std::string, SoNode * >.elements,
std::map< const App::ObjectIdentifier, ExpressionInfo >.elements, std::list<
const SMDS_MeshElement * >.elements, std::map< App::SubObjectT, std::vector<
QTreeWidgetItem * > >.elements, std::deque< int >.elements, std::list<
TElemDef >.elements, std::list< TElemDef * >.elements, std::unordered_map<
App::DocumentObject *, App::PropertyPlacement * >.elements, std::map<
EGeometrieElement, PGaussInfo >.elements, std::vector< SbVec3f >.elements,
std::unordered_map< TopoDS_Shape, Info, Import::ShapeHasher >.elements,
std::vector< ParameterStatus >.elements, std::map< QByteArray, QTreeWidgetItem
* >.elements, std::map< SMESH_TLink, const SMDS_MeshNode * >.elements,
std::list< SMESH_subMesh * >.elements, std::list< WireInfo >.elements,
std::list< ShapeInfo >.elements, std::list< const IslandAndOffset *
>.elements, std::vector< OutRec * >.elements, std::list< const SMDS_MeshNode *
>.elements, std::list< SketcherGui::SketchSelection::SketchSelectionItem
>.elements, std::map< K, T >.elements, std::map< const App::Document *,
Gui::Document * >.elements, std::map< App::SubObjectT, QTreeWidgetItem *
>.elements, std::vector< TechDraw::DashSpec >.elements, std::list< EdgeInfo
>.elements, std::map< int, SMESH_Mesh * >.elements, std::vector<
Base::XMLReader::FileEntry >.elements, std::map< std::string,
Gui::AutoSaveProperty * >.elements, std::list< std::vector< FacetIndex >
>.elements, std::vector< TopoDS_Compound >.elements, std::array< const char *,
InternalAlignmentType::NumInternalAlignmentType >.elements, std::map<
std::string, std::function< void(const std::string &)> >.elements,
std::vector< Gui::PropertyEditor::PropertyItem * >.elements, std::vector<
ustring >.elements, std::list< FaceQuadStruct::Ptr >.elements, std::vector<
SMDS_MeshElement * >.elements, std::list< std::pair< QString, float >
>.elements, std::array< char, 64 >.elements, std::list< std::pair<
TopoDS_Shape, TopLoc_Location > >.elements, std::list< const
App::DocumentObject * >.elements, std::vector< SelIdPair >.elements, std::map<
int, GeomAPI_ProjectPointOnCurve * >.elements, std::map< intptr_t, int
>.elements, std::list< PartGui::ViewProviderCurveNet::Node >.elements,
std::vector< StdMeshers_TNode >.elements, std::map< std::string, Gui::CoinPtr<
SoNode > >.elements, std::map< App::Document *, QTreeWidgetItem * >.elements,
std::list< Path::Area::Shape >.elements, std::map< std::string,
Fem::FemPostFilter::FilterPipeline >.elements, std::vector<
CurveOnMeshHandler::Private::PickedPoint >.elements, std::list< SMDS_Mesh *
>.elements, std::map< std::string, Aci_t >.elements, std::vector<
Sketcher::Sketch::GeoDef >.elements, std::vector< Part::Geometry * >.elements,
std::unordered_map< std::string, DocumentItem::ExpandInfoPtr >.elements,
std::map< std::string, std::vector< Part::TopoShape * > >.elements, std::map<
std::string, QListWidgetItem * >.elements, std::vector< std::shared_ptr<
Path::Area > >.elements, std::map< double *, std::vector< GCS::Constraint * >
>.elements, std::list< int >.elements, std::map< App::SubObjectT,
Qt::CheckState >.elements, std::map< Standard_Integer, TopoDS_Shape
>.elements, std::vector< refTypeStringList >.elements, std::vector< eMapMode
>.elements, std::vector< eRefType >.elements, std::vector< char >.elements,
std::vector< Base::TypeData * >.elements, std::vector< Base::Writer::FileEntry
>.elements, std::map< App::DocumentObject *, QTreeWidgetItem * >.elements,
std::vector< toolShapePoint >.elements, std::vector< IntersectNode *
>.elements, std::vector< LocalMinimum >.elements, std::vector<
ClipperLib::DoublePoint >.elements, std::vector< ModelRefine::FaceTypedBase *
>.elements, std::vector< PolyNode * >.elements, std::vector< Robot::Waypoint *
>.elements, std::vector< Base::Vector3 >.elements, std::vector<
Data::ComplexGeoData::Facet >.elements, std::vector< GCS::ArcOfEllipse
>.elements, std::vector< Mesh::FacetIndex >.elements, std::vector<
Base::Vector2d >.elements, std::vector< DrawingGui::orthoview * >.elements,
std::map< std::string, unsigned int >.elements, std::map< Base::Type,
Base::AbstractProducer * >.elements, std::vector< std::vector<
SketcherGui::SelType > >.elements, std::map< int, SMESHDS_Hypothesis *
>.elements, std::vector< Path::Command * >.elements, std::map< std::string,
ParameterManager * >.elements, std::unordered_map< std::string,
App::DocumentObject * >.elements, std::unordered_map< App::DocumentObject *,
TDF_Label >.elements, std::map< std::string, std::set< App::CellAddress >
>.elements, std::map< int, std::list< TElemDef * > >.elements, std::vector<
AutoConstraint >.elements, std::list< SMESHDS_GroupBase * >.elements,
std::vector< QDoubleSpinBox * >.elements, std::map< int, const SMESHDS_SubMesh
* >.elements, std::map< GCS::Constraint *, VEC_pD >.elements,
std::unordered_map< const Gui::Document *, Gui::DocumentItem * >.elements,
std::list< TopoDS_Shape >.elements, std::list< CCurve >.elements, std::map<
const App::Document *, Workflow >.elements, std::vector< MeshHelpBuilderEdge
>.elements, std::map< std::string, MeshGui::ViewProviderMeshDefects *
>.elements, std::map< double *, double * >.elements,
[Gui::ElementColors::Private.elements](../../d8/dc9/classElementColors_1_1Private.html#a453c5ab210a55c176a3d815186f227f1),
NastranElement.elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.derived_unit.elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.data_environment.elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.procedural_representation_sequence.elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_plane.elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.geometric_set.elements,
[automotive_design.data_environment.elements](../../df/d8e/classautomotive__design_1_1data__environment.html#a0375cefd24a71bd92eee6fec64a4c578),
[automotive_design.derived_unit.elements](../../dc/d0d/classautomotive__design_1_1derived__unit.html#a2465083a99c70793fc515bce4a11ccd3),
[automotive_design.annotation_plane.elements](../../df/dcb/classautomotive__design_1_1annotation__plane.html#a73656954e26a599a5b6dd85b8557d59d),
[automotive_design.geometric_set.elements](../../d0/dab/classautomotive__design_1_1geometric__set.html#ad06652bbec606c86088132c579f53c8b),
[config_control_design.geometric_set.elements](../../d9/d9b/classconfig__control__design_1_1geometric__set.html#a7340f5f8a0bcbcb9c626e8b79717e667),
[ifc2x3.ifcgeometricset.elements](../../dc/dab/classifc2x3_1_1ifcgeometricset.html#ae33d155e00fdcd9ccb2d5c6eb15bd099),
[ifc2x3.ifcderivedunit.elements](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#a4220861b852d70a66f8f25bbd58338f2),
[ifc4.ifcgeometricset.elements](../../d1/d95/classifc4_1_1ifcgeometricset.html#abbf373e832db6c1ce0809b549ee7443b),
[ifc4.ifcderivedunit.elements](../../d3/d76/classifc4_1_1ifcderivedunit.html#a336910d63cc0d3a356edac4756c8f6ec),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.derived_unit_element.exponent,
[automotive_design.derived_unit_element.exponent](../../d9/d3c/classautomotive__design_1_1derived__unit__element.html#a4b0bd5ba25dbe46f18a50f5e7bf46a10),
[ifc2x3.ifcderivedunitelement.exponent](../../d7/da8/classifc2x3_1_1ifcderivedunitelement.html#aed56e8070bdb7185593edfdb48b44169),
[ifc4.ifcderivedunitelement.exponent](../../d3/df7/classifc4_1_1ifcderivedunitelement.html#ac70e218471455ce98080b6e4a817e773),
and
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunctionSegment.exponent](../../d4/dac/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunctionSegment.html#af7658541e958baf3f4c22098d891ec44).

## ◆ wr2()

def automotive_design.derived_unit.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ elements

automotive_design.derived_unit.elements  
---  
  
Referenced by
[ifc2x3.ifcgeometricset.dim()](../../dc/dab/classifc2x3_1_1ifcgeometricset.html#af569a780b93b69b4dce81b08ddd66f89),
[ifc4.ifcgeometricset.dim()](../../d1/d95/classifc4_1_1ifcgeometricset.html#a795b14ef2879e9acc0c066d66e122b9b),
[ifc2x3.ifcderivedunit.dimensions()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#abfb7d2614cbad7ba363d5b3c5eb5d470),
[ifc4.ifcderivedunit.dimensions()](../../d3/d76/classifc4_1_1ifcderivedunit.html#aa316302961670925c24a6da591f61b31),
[automotive_design.derived_unit.wr1()](../../dc/d0d/classautomotive__design_1_1derived__unit.html#a0f657919a22adecb60367513268f0487),
[ifc2x3.ifcderivedunit.wr1()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#a9187776e238d15570720320bf6875864),
and
[ifc4.ifcderivedunit.wr1()](../../d3/d76/classifc4_1_1ifcderivedunit.html#a3c29186705cf96c60831affaf117186e).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

