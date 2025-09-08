---
url: https://freecad.github.io/SourceDoc/df/d4d/classBase_1_1BaseClass.html
scraped_at: 2025-09-08T15:15:40.759471
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [BaseClass](../../df/d4d/classBase_1_1BaseClass.html)

[List of all members](../../d8/de8/classBase_1_1BaseClass-members.html) | Public Member Functions | Static Public Member Functions | Static Protected Member Functions

Base::BaseClass Class Reference

[BaseClass](../../df/d4d/classBase_1_1BaseClass.html "BaseClass class and root
of the type system.") class and root of the type system.
[More...](../../df/d4d/classBase_1_1BaseClass.html#details)

`#include <BaseClass.h>`

##  Public Member Functions  
  
---  
|
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a84b1d36d0060e74a7b48255bca0d1928)
()  
| Construction.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a84b1d36d0060e74a7b48255bca0d1928)  
  
|
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html#ae41bc09a1498fbd4e952e7a7dd9de791)
(const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) &)=default  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514) ()  
| This method returns the Python wrapper for a C++ object.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514)  
  
virtual [Type](../../dc/dee/classBase_1_1Type.html) | [getTypeId](../../df/d4d/classBase_1_1BaseClass.html#addbd3a4f09fce7ce5c6bf021e4c1d566) () const  
[bool](../../d9/db9/classbool.html) | [isDerivedFrom](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html) & | [operator=](../../df/d4d/classBase_1_1BaseClass.html#ad334dfcaf7aa8b86993eaefac41207c2) (const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) &)=default  
virtual void | [setPyObject](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e) ([PyObject](../../df/d1b/classPyObject.html) *)  
virtual | [~BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a7bd44242e16f121ed78718ee8c234f49) ()  
| Destruction.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a7bd44242e16f121ed78718ee8c234f49)  
  
  
##  Static Public Member Functions  
  
---  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
  
##  Static Protected Member Functions  
  
---  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

[BaseClass](../../df/d4d/classBase_1_1BaseClass.html "BaseClass class and root
of the type system.") class and root of the type system.

## Constructor & Destructor Documentation

## ◆ BaseClass() [1/2]

BaseClass::BaseClass  | ( | | ) |   
---|---|---|---|---  
  
Construction.

A constructor.

A more elaborate description of the constructor.

## ◆ BaseClass() [2/2]

| Base::BaseClass::BaseClass  | ( | const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## ◆ ~BaseClass()

| BaseClass::~BaseClass  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Destruction.

A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ create()

| static void * Base::BaseClass::create  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[draftguitools.gui_labels.Label::action()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a31d95b9c0428e8e5e2fc2c0e5ba1f9cf),
and
[init()](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7).

## ◆ getClassTypeId()

| [Type](../../dc/dee/classBase_1_1Type.html) BaseClass::getClassTypeId  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[DrawingGui::TaskProjection::accept()](../../d8/dc3/classDrawingGui_1_1TaskProjection.html#abc007288878ca57e8a8b2a8b9801bf45),
[SpreadsheetGui::DlgSheetConf::accept()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#aa4fefe42d2485471443e738600091ce0),
[TechDrawGui::TaskProjection::accept()](../../d5/def/classTechDrawGui_1_1TaskProjection.html#abc007288878ca57e8a8b2a8b9801bf45),
[StdCmdImport::activated()](../../d5/d4f/classStdCmdImport.html#a7ac453df0ea7389aa72fe651020ec1d4),
[StdCmdEdit::activated()](../../dd/d46/classStdCmdEdit.html#a0f64d05832844dd0219624d2807c8331),
[StdCmdToggleNavigation::activated()](../../d4/d4e/classStdCmdToggleNavigation.html#a798c62a37186af1f888fa6e0a8a4c13e),
[Gui::Application::activateWorkbench()](../../d9/da8/classGui_1_1Application.html#ac3b3b8a91ba204c6180dab0dccc1a6d8),
[InspectionGui::ViewProviderProxyObject::addFlag()](../../d8/dae/classInspectionGui_1_1ViewProviderProxyObject.html#a2c73ee7e0459de3e04e6d6ab6f306505),
[SpreadsheetGui::ViewProviderSheet::beforeDelete()](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a1de1e7f7c64eaad7bdba94ee03783e20),
[Gui::Document::cloneView()](../../de/d4e/classGui_1_1Document.html#a15336e7b0fa188bc17ea1e10f9bb3068),
[Part::FaceMaker::ConstructFromType()](../../df/dde/classPart_1_1FaceMaker.html#aab4d2b29f21f39db71ad32db31032681),
[Gui::Document::createView()](../../de/d4e/classGui_1_1Document.html#a1235bbc0ddca0b8c9465d9d491d79541),
[Gui::WorkbenchManager::createWorkbench()](../../d1/daa/classGui_1_1WorkbenchManager.html#a39b8fc7724a24f5e7c63d9d4268f09dd),
[SketcherGui::DrawSketchHandler::devicePixelRatio()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a10d477cda0227120510e7cbff9cb6897),
[SketcherGui::ViewProviderSketch::draw()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#afaf25efa0d4439559d7157e472ac3630),
[Sketcher::GeometryFacade::ensureSketchGeometryExtension()](../../d1/d73/classSketcher_1_1GeometryFacade.html#a769c9a5e3ccd707e41620fc2dc533e37),
[Sketcher::ExternalGeometryFacade::ensureSketchGeometryExtensions()](../../dd/d90/classSketcher_1_1ExternalGeometryFacade.html#a60ad747405c2d24f21e8f22a1ca55c42),
[App::FunctionExpression::evalAggregate()](../../d6/da3/classApp_1_1FunctionExpression.html#ad9267dc1decdafaaa129f1bd51de07e4),
[App::FunctionExpression::evaluate()](../../d6/da3/classApp_1_1FunctionExpression.html#aea533bde72fab9803b76f53f0b02aac0),
[MeshGui::ViewProviderMesh::faceInfoCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae3d2f360b9f432962521c1bb1b77dd98),
[Gui::Document::getActiveView()](../../de/d4e/classGui_1_1Document.html#a99544adc1b5501dfe086e73747d6b386),
[Gui::ViewProvider::getBoundingBox()](../../d3/db3/classGui_1_1ViewProvider.html#a2c50bc8a5a70a3c5b696c6c60bf3b4d3),
[TechDrawGui::QGVPage::getDevicePixelRatio()](../../dd/dba/classTechDrawGui_1_1QGVPage.html#a572065f0bbcaf76ebb88fa317a0e30e8),
[Gui::Document::getEditingViewOfViewProvider()](../../de/d4e/classGui_1_1Document.html#a39f85fc80d3435d6cb0eb8fa960fc640),
[Mesh::MeshObject::getFacesFromSubElement()](../../d8/dcc/classMesh_1_1MeshObject.html#abaa9c1e9fcf74901afb9ef5a7bc020d9),
[Part::TopoShape::getFacesFromSubElement()](../../d8/ded/classPart_1_1TopoShape.html#af27da9405b017f60101ba35b142fd3b9),
[Sketcher::SketchObject::getGeometryWithDependentParameters()](../../d9/dad/classSketcher_1_1SketchObject.html#a9ae67a28b3f40f3eb812f848b0467e8f),
[Part::TopoShape::getLinesFromSubElement()](../../d8/ded/classPart_1_1TopoShape.html#a8d8615859a7efefad8409388675b50c0),
[Gui::ViewProviderTextDocument::getMDIView()](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a53a587aed195ed229d4e3bd990c6f019),
[SketcherGui::ViewProviderSketch::getScaleFactor()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a98a854b6d2621eb48c51614b4cea53df),
[Gui::UserNavigationStyle::getUserFriendlyNames()](../../d3/de8/classGui_1_1UserNavigationStyle.html#a6182d45703e51b60a19f87af927fbc86),
[MeshGui::MeshSelection::getViewer()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a5ec10e7c84177ce0509eb8c17929952f),
[Gui::Document::getViewOfNode()](../../de/d4e/classGui_1_1Document.html#a92ffe450be8431c98f283aea4d9d7e70),
[StdViewScreenShot::isActive()](../../d9/da6/classStdViewScreenShot.html#a565cc32fb5635b78a64ad8bd5d48cacd),
[StdCmdToggleNavigation::isActive()](../../d4/d4e/classStdCmdToggleNavigation.html#a2703bb81fe701b71e020113de8721e21),
[StdCmdMeasureDistance::isActive()](../../db/dfc/classStdCmdMeasureDistance.html#ae34eeedc376782cacdd1d9b6745864ad),
[StdCmdTextureMapping::isActive()](../../d7/d63/classStdCmdTextureMapping.html#a0470f23667d34ea267470db466c13385),
[Gui::View3DInventorPy::listNavigationTypes()](../../d3/df7/classGui_1_1View3DInventorPy.html#af405ff4c12945637c92230889b88754f),
[Gui::Dialog::DlgSettingsNavigation::loadSettings()](../../d4/de0/classGui_1_1Dialog_1_1DlgSettingsNavigation.html#a535eb9332f21990bd1099737af28e64e),
[Sketcher::SketchObject::migrateSketch()](../../d9/dad/classSketcher_1_1SketchObject.html#aaafb8589473a3087af97dde1bbf276fb),
[SketcherGui::ViewProviderSketch::mouseButtonPressed()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a265a44a9f18bd9ac103c0dd048a455e3),
[Gui::TreeWidget::mouseDoubleClickEvent()](../../de/de0/classGui_1_1TreeWidget.html#aa3c3121b950b3f9b0d134710879cf820),
[SketcherGui::ViewProviderSketch::mouseMove()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a4816546877fe55b4571250f5a6ff9afa),
[Gui::TreeWidget::onActivateDocument()](../../de/de0/classGui_1_1TreeWidget.html#a4d8a559d38fe8b128ff5d66f1822bffd),
[Gui::View3DInventor::OnChange()](../../da/d75/classGui_1_1View3DInventor.html#ab90bd3cd58679e0b888a0bf930791e24),
[Gui::GraphicsView3D::OnChange()](../../df/d0b/classGui_1_1GraphicsView3D.html#a2ced2b0dd60f0a3c0d6b2a7c627a182a),
[Gui::Application::onLastWindowClosed()](../../d9/da8/classGui_1_1Application.html#ab6fa833663f9f2e51031af52fe34865b),
[SpreadsheetGui::DlgSheetConf::prepare()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#abfbeb695362f8ae8074215c61a254de3),
[Gui::Application::reopen()](../../d9/da8/classGui_1_1Application.html#a7a21dfd4379a11fd6babb3a2a14d4b1a),
[Part::Geometry::Restore()](../../dc/df0/classPart_1_1Geometry.html#a1aae6b35e6fba2cbf794c5391847c77b),
[Gui::Application::sActiveView()](../../d9/da8/classGui_1_1Application.html#a395485b4d2f85231d2762749059164f1),
[Part::Geometry::Save()](../../dc/df0/classPart_1_1Geometry.html#afdca307efd3460ac12d9d11212e1019e),
[Gui::Document::Save()](../../de/d4e/classGui_1_1Document.html#a17dba40a2ef0e606900ad09fadca20f5),
[Gui::Document::setActiveView()](../../de/d4e/classGui_1_1Document.html#a1933003b2ee08a001a5858c0e8d71e93),
[SketcherGui::DrawSketchHandler::setCursor()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a8cf59d4479ba8141f5f2ec47014faa65),
[Gui::View3DInventorViewer::setNavigationType()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a989c1b0476cdaa63adadbc7ee70a84a3),
[Gui::Application::setupContextMenu()](../../d9/da8/classGui_1_1Application.html#a926aeecf53a279bac2bc10675733c48d),
[Gui::Application::slotNewDocument()](../../d9/da8/classGui_1_1Application.html#ab61252ad46efb80f5fd98cc3957e83eb),
[SketcherGui::DrawSketchHandler::suggestedConstraintsPixmaps()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#ac79ccc66c40320bf240a9a7d8d20dd30),
[SketcherGui::DrawSketchHandler::unsetCursor()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#af92d1d2c6a6c2e47bba74149dec50e75),
[SketcherGui::ViewProviderSketch::updateData()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#aa3039dd97c10d7c17a0c9e193ff059f4),
and
[SketcherGui::EditModeGeometryCoinManager::updateGeometryColor()](../../d2/d97/classSketcherGui_1_1EditModeGeometryCoinManager.html#a4b2ba186bb93e2b535c65ba180ab0682).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * BaseClass::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
This method returns the Python wrapper for a C++ object.

It's in the responsibility of the programmer to do the correct reference
counting. Basically there are two ways how to implement that: Either always
return a new Python object then reference counting is not a matter or return
always the same Python object then the reference counter must be incremented
by one. However, it's absolutely forbidden to return always the same Python
object without incrementing the reference counter.

The default implementation returns 'None'.

Reimplemented in
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a6b927db483c9f01bd4cfca56fabfbd7f),
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#a7a5bddc284f02d87897e8dc0b69a24fb),
[Gui::AlignmentView](../../dc/dcb/classGui_1_1AlignmentView.html#a97fdea0d5c6ebb376f97671f3517aecc),
[Gui::MDIView](../../df/d23/classGui_1_1MDIView.html#a351cdc46039c40f7655996c971b9a42b),
[Gui::SelectionObject](../../d1/d4e/classGui_1_1SelectionObject.html#acac79a7c3fd6ce3e525560bcf5cb442e),
[Gui::ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html#aedc8b6ee0d29756e6be6d0c3ed0a0aee),
[Gui::Workbench](../../d0/d97/classGui_1_1Workbench.html#a0a557a7b4893cdc9fc87a458c1559ff7),
[Gui::PythonBaseWorkbench](../../dd/dc4/classGui_1_1PythonBaseWorkbench.html#ad3f408b4d0c85402d52cf957d79f28a2),
[DrawingGui::DrawingView](../../da/d65/classDrawingGui_1_1DrawingView.html#ad971ffe5afd987d0f342a8101d887b45),
[Fem::FemPostPipeline](../../d5/d4b/classFem_1_1FemPostPipeline.html#a4b39fb08f59a125dcc783cf93e25d86d),
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a8717b8a5a6c79e899c780233348941de),
[Mesh::Feature](../../dd/dce/classMesh_1_1Feature.html#a7a700a82e66b15d3eb4845ad75c194ab),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#a8080f5c166f3c5d7be77cb908fea27cf),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a655feaca4b489f6dbb6156e702100000),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#ab078ee89f55ad31b12c9602d9f37c3bd),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a491c9250dd9372b18d0296cedfb01701),
[Part::TopoShape](../../d8/ded/classPart_1_1TopoShape.html#a218a19417db2576dbfba9238c87fbd64),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#aae495c7b9a2da93fa8a199b0cf344b35),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a8080f5c166f3c5d7be77cb908fea27cf),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a655feaca4b489f6dbb6156e702100000),
[Points::PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a896ae2285a1a7d1ff32df7599481af82),
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#a57333609c76e9d1469163c8d70f75053),
[TechDrawGui::MDIViewPage](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#ae24c5544a1c7c949db3a146270dcc10a),
[App::DocumentObjectGroup](../../d8/d75/classApp_1_1DocumentObjectGroup.html#a8c2a18ad6bd291d0f6657e877c4f7a92),
[App::Part](../../da/d8d/classApp_1_1Part.html#a8efaf38ed9d96a1207ff4b6bb05955e5),
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#a3751b7ed7df916e214a537dd98a5a2c3),
[Base::FileException](../../d1/dc2/classBase_1_1FileException.html#af518f2b1282226fb40c4367c3aca0ae6),
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a256b755ac0eba62bb50670e75874bed9),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#ae9a76a67e95cadc3bbf289d9e5a3ad84),
[Part::BodyBase](../../da/dc8/classPart_1_1BodyBase.html#a9e28639037238df4c8dafb4518ee86c4),
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#ae23b16d8ba14ec40c3cd74aca0634f2e),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#a666f699fb9530523ef6467717f385096),
[PartDesign::FeaturePrimitive](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a49b5d225e27f3adf2cb0b8452fa84ef8),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a31c2af0bf22d66f737d3ed06bf7a5a1c),
[App::GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html#a6837f9af91a2619c420f361033ab0da5),
[App::InventorObject](../../da/d11/classApp_1_1InventorObject.html#adb3523042b8befd61616bc05fedd290f),
[App::PropertyMatrix](../../d8/d77/classApp_1_1PropertyMatrix.html#a3ec870c7151da4383944d6b918cb6c79),
[App::PropertyPythonObject](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a8aad93153a5c2cf912d6ea3c356c0b00),
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#a3d8ee4bcbcec07a42be8a5af16644ba9),
[App::PropertyPath](../../dc/d24/classApp_1_1PropertyPath.html#ad302c40144fe3213c9a1205bc640e5c0),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a0ec441a65e99e532943b16cc889214dd),
[App::PropertyIntegerSet](../../d0/df3/classApp_1_1PropertyIntegerSet.html#ad8f36fbde4c05abf04bfef2976719751),
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html#a6d4f388202762e37339feb73a2440b4c),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a5b0bcb3b6460df02b89fb8469b1738c9),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#aa6e72d76ecb8d448e1e8016f72f0dd66),
[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html#a6611bfe444b0d347234096b9f3e45613),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#a163886db763f486562607f282dab5c43),
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#a582beb9405c28ab69e9e52f70b99ce5b),
[App::PropertyMaterial](../../d0/df5/classApp_1_1PropertyMaterial.html#ad074fc131ed144d4baf008bf4ef67b05),
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#af17e8d34d40a187543b30789adef4cc7),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#a5a9445b1375ded9f86617e15151ec389),
[Gui::Document](../../de/d4e/classGui_1_1Document.html#adfe08fca04a128b958de54d32ef64219),
[Gui::AbstractSplitView](../../d1/d0b/classGui_1_1AbstractSplitView.html#aacdc2f01d64dfd69198278ffba5d8629),
[Gui::View3DInventor](../../da/d75/classGui_1_1View3DInventor.html#af3ddfdafddf77280279486bb47e12537),
[Fem::FemMeshObject](../../d5/d68/classFem_1_1FemMeshObject.html#abb0ba3282d7a1b42eaeaaee6364afd42),
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#a0399b5ea77220e57ffc878eb298640d1),
[Fem::FemResultObject](../../d3/d81/classFem_1_1FemResultObject.html#af6645066e6371ce9460ca9836cd5af6b),
[Fem::FemSetElementsObject](../../df/d49/classFem_1_1FemSetElementsObject.html#a5ea9bd5b13b1f95a0058d800a6166ab1),
[Fem::FemSetFacesObject](../../df/d72/classFem_1_1FemSetFacesObject.html#a4754f40e1edf8bc0a5701fa58a525625),
[Fem::FemSetGeometryObject](../../df/d59/classFem_1_1FemSetGeometryObject.html#a96a9315d631398747b4c9fcfc784ee9a),
[Fem::FemSetNodesObject](../../dc/d59/classFem_1_1FemSetNodesObject.html#a879bdd1e2d66688ae040e2a4d51772a3),
[Fem::FemSetObject](../../d8/dbe/classFem_1_1FemSetObject.html#ac7ab5f7744ff44d8d4f6f4bb6e022f66),
[Fem::FemSolverObject](../../d1/dd0/classFem_1_1FemSolverObject.html#abf5e279df0983cef9533c8f3095e5574),
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#ae353d3afd26deb124670a18e8a0182ba),
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#ac5d5948ef90f76141fe393437632c611),
[Measure::Measurement](../../d6/d84/classMeasure_1_1Measurement.html#a8013a2e1a5432e7f7d1df0d7ca731863),
[Part::GeomPoint](../../d2/dfb/classPart_1_1GeomPoint.html#a614908136ce111c6ff4766318c917b6c),
[Part::GeomBezierCurve](../../d5/d40/classPart_1_1GeomBezierCurve.html#a719401ec32c061f1fa98e353af18b3de),
[Part::GeomBSplineCurve](../../df/dfe/classPart_1_1GeomBSplineCurve.html#af44f7f164c40bf2b585b9d4d6c65be6a),
[Part::GeomTrimmedCurve](../../df/d24/classPart_1_1GeomTrimmedCurve.html#a393390439ec92ebb2c2db01433a313e0),
[Part::GeomCircle](../../d0/dde/classPart_1_1GeomCircle.html#a491691298434863a8aceba7677fcc2c0),
[Part::GeomArcOfCircle](../../de/d1f/classPart_1_1GeomArcOfCircle.html#a4ac33332556c95da23ef33c5b6913e86),
[Part::GeomEllipse](../../db/d52/classPart_1_1GeomEllipse.html#aaeb62a7f3ea313c3c041de0e81be55b5),
[Part::GeomArcOfEllipse](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#a1acdadc586021d7e9ba3def56fc9f995),
[Part::GeomHyperbola](../../d7/d9e/classPart_1_1GeomHyperbola.html#adaf0d8ce1262e0205d19b54e2aa633e3),
[Part::GeomArcOfHyperbola](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#afc02d939247459f357ae6d4ece0186f6),
[Part::GeomParabola](../../d9/ddf/classPart_1_1GeomParabola.html#a5ffe2936d906f097bf47067e6737b1ca),
[Part::GeomArcOfParabola](../../db/ddc/classPart_1_1GeomArcOfParabola.html#a1477e6065e04d58f7dea822e9277c7f4),
[Part::GeomLine](../../d5/d30/classPart_1_1GeomLine.html#aa2edd3d546690e1c2a6b22207d010ffd),
[Part::GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html#ad070805a5a11519db597eff0f87bcb9f),
[Part::GeomOffsetCurve](../../d0/d36/classPart_1_1GeomOffsetCurve.html#ae5d610fc722a0f6a93bec62a0c4ab744),
[Part::GeomBezierSurface](../../df/dab/classPart_1_1GeomBezierSurface.html#a9a4af6a18dc9bb1daf8addf9a00f5565),
[Part::GeomBSplineSurface](../../d1/d27/classPart_1_1GeomBSplineSurface.html#aa2ee30f54525728cfe2228b30288862d),
[Part::GeomCylinder](../../de/dc7/classPart_1_1GeomCylinder.html#a316cf0da705b6711c3e07a0ce9016d28),
[Part::GeomCone](../../d0/d7c/classPart_1_1GeomCone.html#ae930322078d517802199fa54ca2c8cd2),
[Part::GeomSphere](../../dc/da5/classPart_1_1GeomSphere.html#a6ef59972f16a3e95afd8489feeb7e77a),
[Part::GeomToroid](../../da/d8f/classPart_1_1GeomToroid.html#a7bbef55fa701c99f352d41fa7b8eb707),
[Part::GeomPlane](../../d2/d0e/classPart_1_1GeomPlane.html#ac08d7c2c1f6413dc7fa6edf54cc12ef3),
[Part::GeomOffsetSurface](../../dc/d14/classPart_1_1GeomOffsetSurface.html#aa22b3e5edbb3996df050ad34ca7edee1),
[Part::GeomPlateSurface](../../d7/db9/classPart_1_1GeomPlateSurface.html#ad9371ef844791b783255e44cee6af596),
[Part::GeomTrimmedSurface](../../de/dd0/classPart_1_1GeomTrimmedSurface.html#a6b737c07fd93929717571e62d3ab4555),
[Part::GeomSurfaceOfRevolution](../../df/dc7/classPart_1_1GeomSurfaceOfRevolution.html#aaa101def366bf4f758a0802deb63fc69),
[Part::GeomSurfaceOfExtrusion](../../de/dd5/classPart_1_1GeomSurfaceOfExtrusion.html#ad844ef985f4eced0eed77a7004bd76c9),
[Part::Geom2dPoint](../../d8/da9/classPart_1_1Geom2dPoint.html#a18407fdb5242fb4223445e5349c43f1e),
[Part::Geom2dBezierCurve](../../d6/d50/classPart_1_1Geom2dBezierCurve.html#a67259b8b3a0302ba9b4c744042a081bf),
[Part::Geom2dBSplineCurve](../../dd/d59/classPart_1_1Geom2dBSplineCurve.html#a6503fdcc0c5f12bed9fb1e922018d329),
[Part::Geom2dCircle](../../d7/d4e/classPart_1_1Geom2dCircle.html#a6033ddee77f3ed5078e7f687978167f8),
[Part::Geom2dArcOfCircle](../../de/d96/classPart_1_1Geom2dArcOfCircle.html#ab30ccbbe1ab601a499c0d4d5037c35e9),
[Part::Geom2dEllipse](../../db/db9/classPart_1_1Geom2dEllipse.html#a93eaa85428078e5a973df6b5be841b57),
[Part::Geom2dArcOfEllipse](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#afd91c9bb91d4850b3c2302c313b1854a),
[Part::Geom2dHyperbola](../../d2/d95/classPart_1_1Geom2dHyperbola.html#aae940033f3c6697ca22cbebb5e269ecf),
[Part::Geom2dArcOfHyperbola](../../dc/db7/classPart_1_1Geom2dArcOfHyperbola.html#acecc2fac530f1442b90e7eff71a2271f),
[Part::Geom2dParabola](../../d9/dff/classPart_1_1Geom2dParabola.html#ab184f8d3159c308d9b7b5bd042273af1),
[Part::Geom2dArcOfParabola](../../d3/d95/classPart_1_1Geom2dArcOfParabola.html#a4c9fd308965f6ee7834cb28094a67936),
[Part::Geom2dLine](../../d2/d27/classPart_1_1Geom2dLine.html#a210d2810dcb244856a1a65ee806a7e9b),
[Part::Geom2dLineSegment](../../df/ded/classPart_1_1Geom2dLineSegment.html#a28989e0d3e92aff477dd97b417b9b18f),
[Part::Geom2dOffsetCurve](../../d5/de5/classPart_1_1Geom2dOffsetCurve.html#a8bdb5a7b5c24ffde5f70a393b8ab2676),
[Part::Geom2dTrimmedCurve](../../d8/da3/classPart_1_1Geom2dTrimmedCurve.html#a40a1c6859eafee4c1e426fda6a6fe90e),
[Part::GeometryDefaultExtension< T
>](../../d6/d66/classPart_1_1GeometryDefaultExtension.html#ab164e563cb747cd1410d1c67ffbb3da9),
[Part::GeometryDefaultExtension< T
>](../../d6/d66/classPart_1_1GeometryDefaultExtension.html#a17c7a326b48180fb4cd418c14e2bb601),
[Part::GeometryDefaultExtension< T
>](../../d6/d66/classPart_1_1GeometryDefaultExtension.html#a7e5dc60e80f1166465c2f90f0e0c9d7a),
[Part::GeometryDefaultExtension< T
>](../../d6/d66/classPart_1_1GeometryDefaultExtension.html#a7401f0d4bfc2769d84ee74d69543f233),
[Part::PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html#a477381c439b6f365d7f0689c8619f284),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#a9881f558fdd16ec00fa7bbdbd9c17158),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#a2f33d7906ad2d4fec1635cfb5a99ad8f),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a96cc3cb794f0fc993b841425c8ab8fed),
[PartDesign::Feature](../../d7/d51/classPartDesign_1_1Feature.html#a7b572936974ad2fb3d78fe729d3e1757),
[Path::FeatureArea](../../da/d1e/classPath_1_1FeatureArea.html#a71e18a904362f9e20f126aca4f13b8e8),
[Path::Feature](../../d5/dd9/classPath_1_1Feature.html#ab7f800e910601271c9a4bc2480dad5f2),
[Path::FeatureCompound](../../d2/d43/classPath_1_1FeatureCompound.html#a08d674d0a02ef64d5572e51c3689fd2d),
[Path::PropertyPath](../../da/d75/classPath_1_1PropertyPath.html#ad302c40144fe3213c9a1205bc640e5c0),
[Path::PropertyTool](../../d4/d51/classPath_1_1PropertyTool.html#a29624f945bf91fc31a7db03c394caaa1),
[Path::PropertyTooltable](../../d4/d86/classPath_1_1PropertyTooltable.html#ad078eb5b3abeecca00b8882f9b7eb713),
[Robot::PropertyTrajectory](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#ac05b39f0e066ac6fcb903a7ea18a1c61),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#a5b35961553442da622521648b1f50365),
[Robot::TrajectoryObject](../../d7/db5/classRobot_1_1TrajectoryObject.html#aa511366030cf224da9a3a0d17b07606e),
[Spreadsheet::PropertyColumnWidths](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#affb41a34eb340eb4d6aad596c3248aaa),
[Spreadsheet::PropertyRowHeights](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#afcbe5fed0bdb53301d1a2950e2510097),
[SpreadsheetGui::SheetView](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#aa9f11203065200b624cd36dbb10793e3),
[TechDraw::CosmeticVertex](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a54c9ef2fe2c36006804762c9d6a75810),
[TechDraw::CosmeticEdge](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a234fc93576393fbcfebf7ce8424b62a4),
[TechDraw::CenterLine](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad373419587c731e5d3ba962306f5b25c),
[TechDraw::GeomFormat](../../d7/d64/classTechDraw_1_1GeomFormat.html#a09d39d5302825598417bc29effa2f013),
[TechDraw::DrawParametricTemplate](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#a446f297751fa8bd5511d4d48f6dc75ed),
[TechDraw::DrawRichAnno](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#a206b0ca34b87f79762924fedec8c7fd1),
[TechDraw::DrawSVGTemplate](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#ad0a08bbe311a5147f49ab0f3647c88dd),
[TechDraw::DrawTemplate](../../d8/d95/classTechDraw_1_1DrawTemplate.html#aead757612a7d1a557eeeb43e0caec8bd),
[TechDraw::DrawTile](../../da/d56/classTechDraw_1_1DrawTile.html#a0e979b8f73ef5fea5997dc8e8e12b9d4),
[TechDraw::DrawTileWeld](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a00b92083449ce106a622bf7b0ca3fdea),
[TechDraw::DrawViewClip](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a4e296aa3a79c48e108afe2d9db30731f),
[TechDraw::DrawViewDimExtent](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#a9a71017db88391c3248e29a3931be915),
[TechDraw::DrawWeldSymbol](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#ad9e24e34ca274c67e594e384a37e2cb9),
[TechDraw::PropertyCenterLineList](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#ab94ded1a61348267fff1a76132d0dad7),
[TechDraw::PropertyCosmeticEdgeList](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a54de065863147b2cdbe2f39c661c0780),
[TechDraw::PropertyCosmeticVertexList](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#ac28eb836cafbe4d36cb4730376751317),
[TechDraw::PropertyGeomFormatList](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a68aa1f06181de2cd0a69b82f03a3594f),
[WebGui::BrowserView](../../db/d47/classWebGui_1_1BrowserView.html#ae7b719cac6bf7a8d8a3a78860767da5e),
[App::Document](../../d8/d3e/classApp_1_1Document.html#a3eafa7c3d20b42cb6c41d9623c2476c7),
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#a1adfcfb2169b5c31374e07346256648f),
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0e2e176a32a6eda05d5c18a319ecd255),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a6955692424d3ff25b5330b487de3e0e0),
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#a79e687e5afd79b802e00f1aa7bbffeb6),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a2c1f9fc6fd155b2c5886ea61c37ea689),
[App::PropertyPlacementList](../../d1/d76/classApp_1_1PropertyPlacementList.html#a47b44071f21bf2e6d61cfa0eff866871),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#accebd677bd5e10d5f9b576e2d0d72bf6),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a1535c7935ad3a7545e41ac293f9eca11),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#ad1b1f9c557f1e474722b0cd37ccb4a96),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a07c5d74e2725f2d1e804d3706d239e2e),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#ac41751baabdd2bcb04a996719004377e),
[App::PropertyXLinkSub](../../d4/da0/classApp_1_1PropertyXLinkSub.html#ad996567330d5c7b6255da532d74ae9b5),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#aa9ee16bcedb194655b91e5d93730bf22),
[App::PropertyXLinkList](../../df/d17/classApp_1_1PropertyXLinkList.html#a91d0fb67e3e4623edf333125710ff985),
[App::PropertyIntegerList](../../d7/daa/classApp_1_1PropertyIntegerList.html#a95fa756c336190854adae0c993d249c8),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#a1936aa922f5a5acb971305b057d3d068),
[App::PropertyStringList](../../d8/d55/classApp_1_1PropertyStringList.html#aabb738ab4b3a877fe15890639f3e07df),
[App::PropertyBoolList](../../d1/dcf/classApp_1_1PropertyBoolList.html#af31b8393b113fa9f5e982348bdcaa737),
[App::PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#a07d36d2877e6004fba77c18f6a6e5610),
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a21a99adbdf606ed977b02c51d8f1847d),
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#afd3cb0bbe7979346fb4b2e39cf7b076f),
[Gui::LinkView](../../da/d11/classGui_1_1LinkView.html#a28d68969192962a20aabdc07a666d642),
[Part::GeometryDefaultExtension< T
>](../../d6/d66/classPart_1_1GeometryDefaultExtension.html#a8dcc9546ebbe3f02df5c515e64aeff12),
[Part::GeometryMigrationExtension](../../d7/d36/classPart_1_1GeometryMigrationExtension.html#a40afc824305c0bd2e6bc84e48cf3f7a9),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#a9579e5a76ef1c70cc24701d4bba32c6c),
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ac03971ba790eda722f46e82c1126300f),
[Sketcher::Constraint](../../d6/def/classSketcher_1_1Constraint.html#ae425cdaeec5182f32013500d39c40899),
[Sketcher::ExternalGeometryExtension](../../d5/dea/classSketcher_1_1ExternalGeometryExtension.html#a8d1234cc19df82be978fddb82d788c33),
[Sketcher::ExternalGeometryFacade](../../dd/d90/classSketcher_1_1ExternalGeometryFacade.html#a1fe80346aff8bfcb90f9550504d6673e),
[Sketcher::GeometryFacade](../../d1/d73/classSketcher_1_1GeometryFacade.html#a58595eb9e8fcd2da4995e412784d171c),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a9b8c7b24aba099009c2026143d06efcd),
[Sketcher::SketchGeometryExtension](../../d7/db4/classSketcher_1_1SketchGeometryExtension.html#a7bcea018a7279e763ef2ceaa3b0eae87),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a7a2970aaacc965d3d4c3b3a949fcb21f),
[Sketcher::SolverGeometryExtension](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#af8590935507d3163060551a71bd5069e),
[SketcherGui::ViewProviderSketchGeometryExtension](../../d3/d23/classSketcherGui_1_1ViewProviderSketchGeometryExtension.html#a77e422bf4a550b0d038a3e3c4f096170),
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a7c0999f0f09184f0955da288423fc2f8),
[TechDraw::DrawGeomHatch](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#aa02555ef8da0ade9bf32d826683869d6),
[TechDraw::DrawHatch](../../d0/d97/classTechDraw_1_1DrawHatch.html#a206dea2db611b805e68fc860a1032597),
[TechDraw::DrawLeaderLine](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a87cddb7857e5d66215c929844d3bd438),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#a55ad5df210dcaeadeaf5b8504dfdc736),
[TechDraw::DrawProjGroup](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acaf6822e5ff679aae0ff66759d7135dc),
[TechDraw::DrawProjGroupItem](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a28fc999e36c9404361ca24453f424678),
[TechDraw::DrawView](../../d6/d1c/classTechDraw_1_1DrawView.html#af82b1daff82fedafa74673a607bc38a4),
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a3e332a5c716d9cc5145fa9afa7fcacff),
[TechDraw::DrawViewPart](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ab0f733c1df0bd35133eb9d61e5670fe4),
[TechDraw::DrawViewSymbol](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a6406ae57714b08e7d99c03f1bb4d652c),
[Part::GeomConic](../../d1/d86/classPart_1_1GeomConic.html#af93ac18dcf2e7833cfeee963701df592),
[Part::GeomArcOfConic](../../db/d48/classPart_1_1GeomArcOfConic.html#a8608fb1eb97648013b756b8f5919cf08),
[Part::Geom2dConic](../../d8/d0d/classPart_1_1Geom2dConic.html#a0b1c95db1650f49a8a2af7b05bef6685),
[Part::Geom2dArcOfConic](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html#acb4c4f0cd47ecf25055b83a524a88948),
and
[Part::GeometryExtension](../../da/d7d/classPart_1_1GeometryExtension.html#a89aae21812df5618672b23960a473194).

Referenced by
[Sandbox::DocumentObjectProtectorPy::getattr()](../../d3/d95/classSandbox_1_1DocumentObjectProtectorPy.html#a0aa8def74fdf4b4644dbf147c9132b96),
and
[Spreadsheet::PropertySheet::getPyValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a345cfadf9398442bb9a94bd6d1fc10f0).

## ◆ getTypeId()

| [Type](../../dc/dee/classBase_1_1Type.html) BaseClass::getTypeId  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#ad6856a6fd1d296adfcb2972d4cdf33ee),
and
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596).

Referenced by
[Gui::Document::cloneView()](../../de/d4e/classGui_1_1Document.html#a15336e7b0fa188bc17ea1e10f9bb3068),
[Mesh::MeshObject::getFacesFromSubElement()](../../d8/dcc/classMesh_1_1MeshObject.html#abaa9c1e9fcf74901afb9ef5a7bc020d9),
[Part::TopoShape::getFacesFromSubElement()](../../d8/ded/classPart_1_1TopoShape.html#af27da9405b017f60101ba35b142fd3b9),
[Part::TopoShape::getLinesFromSubElement()](../../d8/ded/classPart_1_1TopoShape.html#a8d8615859a7efefad8409388675b50c0),
[Gui::View3DInventorPy::getNavigationType()](../../d3/df7/classGui_1_1View3DInventorPy.html#a94606713a2f513eaecc2cb27066d18da),
[App::Expression::isSame()](../../dc/d5c/classApp_1_1Expression.html#a0629cfd92afb2d9aff38fda6d3b30c24),
[Gui::TreeView::mouseDoubleClickEvent()](../../d9/ddf/classGui_1_1TreeView.html#ad2e4760d9a018ee92f83e36adbadcfa7),
[Gui::NavigationStyle::openPopupMenu()](../../d2/d1c/classGui_1_1NavigationStyle.html#a6831ec68eec376f2b9e8f4ea5a54f7bc),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Gui::TreeView::rowsInserted()](../../d9/ddf/classGui_1_1TreeView.html#a14fe0e1762ce6ca1f12f092b7d9477f0),
[Part::GeometryPersistenceExtension::Save()](../../de/db6/classPart_1_1GeometryPersistenceExtension.html#af4b4cb8e926350eb9cf1f7c78ce2a7c8),
[Part::AttachExtension::setAttacher()](../../dc/d47/classPart_1_1AttachExtension.html#a1e4d65c3b672b1760b037891d419e065),
[Gui::View3DInventorViewer::setNavigationType()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a989c1b0476cdaa63adadbc7ee70a84a3),
and
[Gui::Application::setupContextMenu()](../../d9/da8/classGui_1_1Application.html#a926aeecf53a279bac2bc10675733c48d).

## ◆ init()

| void BaseClass::init  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
References
[Base::Type::badType()](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76),
[create()](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a),
and
[Base::Type::createType()](../../dc/dee/classBase_1_1Type.html#abdc2ccb5c9c300a5278b39db5e321cc0).

Referenced by
[Gui::DocumentModel::DocumentModel()](../../dc/dc8/classGui_1_1DocumentModel.html#a91f260cdfeeb43d912f106418916223c),
[WebGui::BrowserView::getPyObject()](../../db/d47/classWebGui_1_1BrowserView.html#ae7b719cac6bf7a8d8a3a78860767da5e),
[Gui::SoFCDB::init()](../../d3/d6d/classGui_1_1SoFCDB.html#a43392b9f4792edcae4cbfa8d11a38eba),
[App::Application::initTypes()](../../da/dbf/classApp_1_1Application.html#a7fd51c3ba729d368d8f150a720af49e1),
[Gui::Application::initTypes()](../../d9/da8/classGui_1_1Application.html#a7fd51c3ba729d368d8f150a720af49e1),
and
[DocumentObject.DocumentObject::onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882).

## ◆ initSubclass()

| void BaseClass::initSubclass  | ( | [Base::Type](../../dc/dee/classBase_1_1Type.html) & | _toInit_ ,   
---|---|---|---  
|  | const char *  | _ClassName_ ,   
|  | const char *  | _ParentName_ ,   
|  | [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) | _method_ = `nullptr`  
| ) | |   
staticprotected  
  
References
[Base::Type::badType()](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76),
[Base::Type::createType()](../../dc/dee/classBase_1_1Type.html#abdc2ccb5c9c300a5278b39db5e321cc0),
and
[Base::Type::fromName()](../../dc/dee/classBase_1_1Type.html#a7fd6fce9272b7886af7a58d2af987c42).

## ◆ isDerivedFrom()

[bool](../../d9/db9/classbool.html) Base::BaseClass::isDerivedFrom  | ( | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |  const  
---|---|---|---|---|---  
  
References
[Base::Type::isDerivedFrom()](../../dc/dee/classBase_1_1Type.html#abb24fc578ec80e158584f46d4a5042c7).

Referenced by
[StdCmdToggleSelectability::activated()](../../d6/d27/classStdCmdToggleSelectability.html#a0ce2e8138a2c546adb161b8804521a28),
[Gui::Application::activateView()](../../d9/da8/classGui_1_1Application.html#aba63faa841669d06200561f6fa8b2ee4),
[PartDesign::Body::addObject()](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605),
[TechDraw::DrawPage::addView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ac3e23be3a1fe6b9e35a45c680e33dd8a),
[SurfaceGui::FillingPanel::ShapeSelection::allow()](../../df/d8f/classSurfaceGui_1_1FillingPanel_1_1ShapeSelection.html#a3cb549a7831215516813455581b60860),
[SurfaceGui::FillingEdgePanel::ShapeSelection::allow()](../../d7/d97/classSurfaceGui_1_1FillingEdgePanel_1_1ShapeSelection.html#a7d65698bcdefe88bc739c97a70a2e2b0),
[SurfaceGui::FillingVertexPanel::VertexSelection::allow()](../../d0/de5/classSurfaceGui_1_1FillingVertexPanel_1_1VertexSelection.html#a5d7e3b9dae02ef51b26955df36344b74),
[SurfaceGui::SectionsPanel::ShapeSelection::allow()](../../d0/d13/classSurfaceGui_1_1SectionsPanel_1_1ShapeSelection.html#aff2fc432cece76367f9e7018d511f9f9),
[SurfaceGui::GeomFillSurface::EdgeSelection::allow()](../../d7/d85/classSurfaceGui_1_1GeomFillSurface_1_1EdgeSelection.html#a9db046f5cffbdc64fc7cf1743c72b592),
[TechDrawGui::ViewProviderDimension::attach()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a074916255bd70c0cd57d36b717586f4d),
[Gui::ViewProviderLink::attach()](../../d6/d59/classGui_1_1ViewProviderLink.html#ab31e41e9a24ec097be019cdff4fb969b),
[TechDrawGui::TaskRichAnno::calcTextStartPos()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ae1abe86bd3bc257ecd36cc0212763a37),
[Part::Extrusion::calculateShapeNormal()](../../db/d6c/classPart_1_1Extrusion.html#a9068fcaf96e864a90a04b860140de9c9),
[Gui::ViewProviderDocumentObject::canDelete()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#af693d465f282457e260eed5092506cf1),
[App::PropertyExpressionEngine::canonicalPath()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a21b797539c8eef459b505be492c17f09),
[PartDesignGui::ViewProviderHelix::claimChildren()](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#a27d75e659da5ae824301907d1f95fe4d),
[PartDesignGui::ViewProviderPipe::claimChildren()](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a4c581523b2a518090737db2569d91dfa),
[PartDesignGui::ViewProviderSketchBased::claimChildren()](../../d3/d7d/classPartDesignGui_1_1ViewProviderSketchBased.html#a4552ed8301193054b5f18e6d1b445b89),
[TechDrawGui::ViewProviderPage::claimChildren()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#abaf1943763d885917f20c4a78a8e2ef5),
[Gui::TreeWidget::contextMenuEvent()](../../de/de0/classGui_1_1TreeWidget.html#a1973cd275eac94af842ffd66ab4fbadd),
[Sketcher::SketchObject::convertToNURBS()](../../d9/dad/classSketcher_1_1SketchObject.html#a23e6660388fbe498a07b07a8c4f065fe),
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[Gui::SoFCUnifiedSelection::doAction()](../../dd/d97/classGui_1_1SoFCUnifiedSelection.html#a6df6c46d47a0e7d092d2df18c2da9160),
[TechDrawGui::QGIViewDimension::draw()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a5a804977a329425219739213bc82ec70),
[SketcherGui::ViewProviderSketch::draw()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#afaf25efa0d4439559d7157e472ac3630),
[TechDrawGui::QGIViewBalloon::drawBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6d26eb06a692339e02c1b57545903f29),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[PartDesign::FeatureBase::execute()](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a7cc09059c368f65475f0fa3f05bc06f5),
[PartDesign::Loft::execute()](../../d0/deb/classPartDesign_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[PartDesign::Pipe::execute()](../../da/d61/classPartDesign_1_1Pipe.html#a860c1038a89156936a4d1fd44481cfbd),
[Path::FeatureAreaView::execute()](../../d3/db4/classPath_1_1FeatureAreaView.html#a181be122ea1283aac8cb22d51edc5686),
[Surface::Cut::execute()](../../d4/d17/classSurface_1_1Cut.html#adade24c19d386572d09157489463f785),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[Fem::FemVTKTools::exportFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a37e8a3dd86851c4ce056f3cfa7ad0d89),
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
[Spreadsheet::Sheet::exportToFile()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a4f73202312594e8b11200a83f677c57c),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[ImportGui::ExportOCAFGui::findColors()](../../d7/dd1/classImportGui_1_1ExportOCAFGui.html#a1c4f907241651d44fa92f9d57984d5b6),
[App::Origin::getAxis()](../../d9/d8b/classApp_1_1Origin.html#a22ff56dd7f14783a94fe81dbb5ac648c),
[PartDesign::ProfileBased::getBaseObject()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a401f7d69c600f553aa66a01f8414ef5b),
[PartDesign::Transformed::getBaseObject()](../../dd/de1/classPartDesign_1_1Transformed.html#aba5db649de61d67db332e2cd71a86d09),
[PartDesign::Feature::getBaseShape()](../../d7/d51/classPartDesign_1_1Feature.html#ad6682cb08a683af75dc2b9de5bbcc13f),
[PartDesign::Feature::getBaseTopoShape()](../../d7/d51/classPartDesign_1_1Feature.html#a17c6163f5824ed676fab0cd92e9794e3),
[App::PropertyFileIncluded::getDocTransientPath()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5f4e5ed4004ee3084755508e6c3b071a),
[Spreadsheet::Cell::getFormattedQuantity()](../../d5/d22/classSpreadsheet_1_1Cell.html#a66a4fb5ffaa93232823dfbe49833ab7b),
[App::OriginGroupExtension::getGroupOfObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#aefe03f3ec93fce064aeca10ea5593d1b),
[Gui::View3DInventorPy::getObjectInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a713b1bf47110fdea7202e2fd7c592ca0),
[Gui::View3DInventorPy::getObjectsInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a2eff2f6d5d7072fa1b728eb307a215a1),
[App::OriginGroupExtension::getOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2),
[TechDrawGui::QGIDrawingTemplate::getParametricTemplate()](../../d3/d23/classTechDrawGui_1_1QGIDrawingTemplate.html#aa35d8e88fa3a262776ef10b8caa1e603),
[App::Origin::getPlane()](../../d9/d8b/classApp_1_1Origin.html#a9079a145e03b6fb0715db0246ace036b),
[PartDesign::ProfileBased::getProfileWires()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#ac961ce965c86590b3d865e3cf87ab019),
[PartDesignGui::getReferencedSelection()](../../dc/d12/namespacePartDesignGui.html#a3f00fb1f14bb1e8917fe623cecd8ab59),
[SketcherGui::ViewProviderSketch::getScaleFactor()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a98a854b6d2621eb48c51614b4cea53df),
[Path::FeatureAreaView::getShapes()](../../d3/db4/classPath_1_1FeatureAreaView.html#a8bdeb47d6e84b6cfb93ce2eb43e7bbe9),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[PartDesign::Transformed::getSketchObject()](../../dd/de1/classPartDesign_1_1Transformed.html#a7b52a3658c0f24c04278bc8c1fcc55fd),
[TechDrawGui::QGISVGTemplate::getSVGTemplate()](../../d4/d36/classTechDrawGui_1_1QGISVGTemplate.html#a31406f43b09ce7700a787ce3a1c42880),
[Gui::LinkInfo::getView()](../../d4/da4/classGui_1_1LinkInfo.html#a860b0cea7256187c0f3325e7359e29e2),
[Part::Part2DObject::handleChangedPropertyType()](../../d9/d57/classPart_1_1Part2DObject.html#a3b4551d03504c25446ede14dcf2309e3),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[PartDesignGui::ViewProviderShapeBinder::highlightReferences()](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#a88fdfde939bae5a7f7d2ed7d3865a9a8),
[PartDesign::Body::insertObject()](../../dd/db8/classPartDesign_1_1Body.html#a5cbb7aa1f902c8b111a9c9a428072c09),
[App::GeoFeatureGroupExtension::isLinkValid()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a89659fb6caa61f4cf9971b0170efcdc7),
[App::PropertyLinkBase::isSame()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a80edc3aa77b975c9862ca4ff78179407),
[Import::ImportOCAF2::loadShapes()](../../d9/ddd/classImport_1_1ImportOCAF2.html#afa667a1c5c88cd6565d91740bf38ea61),
[PartGui::OffsetWidget::OffsetWidget()](../../d9/d6d/classPartGui_1_1OffsetWidget.html#ae7bb4b5d03b3c78115b8e3943bb318d1),
[App::Document::onBeforeChangeProperty()](../../d8/d3e/classApp_1_1Document.html#a92ee224a3cd40ef4da74e81d732c8fcb),
[Fem::FemPostClipFilter::onChanged()](../../dc/d06/classFem_1_1FemPostClipFilter.html#a696285744236a6bf6e8c14f735034705),
[Fem::FemPostCutFilter::onChanged()](../../da/d89/classFem_1_1FemPostCutFilter.html#a682758b8e3c1c8cf8b272d2244321913),
[App::OriginGroupExtension::onExtendedSetupObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cbdf0475e8306ed1f6fab7bb2a071cb),
[PartDesignGui::TaskLinearPatternParameters::onSelectionChanged()](../../da/d31/classPartDesignGui_1_1TaskLinearPatternParameters.html#a865b9046f3a77031028528e8330e7bcc),
[PartDesignGui::TaskMirroredParameters::onSelectionChanged()](../../d8/d3c/classPartDesignGui_1_1TaskMirroredParameters.html#a5b8572d198c9289b07e5223b5ab90578),
[PartDesignGui::TaskPolarPatternParameters::onSelectionChanged()](../../d7/d72/classPartDesignGui_1_1TaskPolarPatternParameters.html#a100a716e1bd223ef70db3b1961b6ed49),
[Gui::PropertyView::onTimer()](../../d8/d18/classGui_1_1PropertyView.html#aa53958cefcade980c3ffe795f787d6de),
[Gui::Dialog::find_placement::operator()()](../../db/d20/classGui_1_1Dialog_1_1find__placement.html#a52917723bad2ec3993bd7adbe3804722),
[App::DocumentObjectT::operator=()](../../d5/d07/classApp_1_1DocumentObjectT.html#aa6d6b6131b81ccd65364482dd799199b),
[PartDesignGui::TaskTransformedParameters::originalSelected()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#adb918122e8572632cc17114506d98ccd),
[App::PropertyLink::Paste()](../../d4/d77/classApp_1_1PropertyLink.html#a31b305bd16358bc6459e33bf47e1c2b6),
[App::PropertyLinkList::Paste()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a4395718ac6e9c8f221569c4de1933ba9),
[App::PropertyLinkSub::Paste()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a5514822b7ffa4a3ebaf2c8a569d0df67),
[App::PropertyLinkSubList::Paste()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a3dfbcd135189c2b3e6e7c6136ed572a1),
[App::PropertyXLink::Paste()](../../d2/de2/classApp_1_1PropertyXLink.html#a6d593eed6217cccfdad4a79a4c752c27),
[App::PropertyXLinkSubList::Paste()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4ac663947ed88fa49f3a874273098fe4),
[PartDesign::ProfileBased::positionByPrevious()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#acdddc3b78089a2b2dbd5c567998c9039),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[PartDesign::Body::removeObject()](../../dd/db8/classPartDesign_1_1Body.html#a207956cf2a361690d971c7e604fc8bf1),
[TechDraw::DrawPage::removeView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a47c86c19ddcbaabe9a680e836c437012),
[App::PropertyLink::resetLink()](../../d4/d77/classApp_1_1PropertyLink.html#a0461c85fa8e082a75df6e848f94d8c39),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[Path::PropertyPath::RestoreDocFile()](../../da/d75/classPath_1_1PropertyPath.html#a6ee2ea90ed9f02be32225df050ee9034),
[Gui::Application::sActiveView()](../../d9/da8/classGui_1_1Application.html#a395485b4d2f85231d2762749059164f1),
[Fem::PropertyPostDataObject::SaveDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a3ed0c0500e1d89813d4d6854ce5b388b),
[Part::Part2DObject::seekTrimPoints()](../../d9/d57/classPart_1_1Part2DObject.html#a7f5beeba90cfa4cdf7a72f7827bae9f1),
[App::PropertyLinkList::set1Value()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a7a16fe45fc1c04feba8b79c9cd463f4d),
[PartDesign::Body::setBaseProperty()](../../dd/db8/classPartDesign_1_1Body.html#abbb8bb2a283a57b6d6f2230dcacd7be3),
[Gui::ViewProviderDragger::setEdit()](../../d3/d04/classGui_1_1ViewProviderDragger.html#ae112bfbf937f2ec8a8efd24fd432acc5),
[App::LinkBaseExtension::setProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770),
[PartDesignGui::Workbench::setupContextMenu()](../../d4/d0c/classPartDesignGui_1_1Workbench.html#adf13eeb6b7f53fc0ce4c900cbca9712e),
[App::Origin::setupObject()](../../d9/d8b/classApp_1_1Origin.html#af5708fed01b27a82a33d8b06d02e89e6),
[Gui::RecoveryWriter::shouldWrite()](../../d9/d25/classGui_1_1RecoveryWriter.html#aec0a593c8a632c1e1700c4b8e851372f),
[Gui::Document::slotActivatedObject()](../../de/d4e/classGui_1_1Document.html#af83f915830c8075a246b5424caaa4d2c),
[Gui::Document::slotChangedObject()](../../de/d4e/classGui_1_1Document.html#a3886f48ebea3c1a519f8f0f1cf3f9d3e),
[Gui::ViewProviderOriginGroupExtension::slotChangedObjectGui()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a302efc5ec7a5b6a38ba690fbb2ba18af),
[PartDesignGui::ViewProviderBody::slotChangedObjectGui()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ad65bd2facfeba3ad583f89bcbbb4fdb4),
[Gui::Document::slotFinishRestoreDocument()](../../de/d4e/classGui_1_1Document.html#a63ad8aad31e89cca0651086cf3fd93d2),
[Gui::Document::slotRelabelObject()](../../de/d4e/classGui_1_1Document.html#af01aad30e324bdccd072f0550b2b9628),
[Gui::Document::slotTransactionAppend()](../../de/d4e/classGui_1_1Document.html#a8f4d208373fe26556f80553a8aa062f1),
[Sketcher::SketchObject::split()](../../d9/dad/classSketcher_1_1SketchObject.html#ab73e7a53a704168c004b9aa6c9ad7a68),
[App::PropertyXLink::supportXLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a3eec738eb9480c2a52fc5791de8a6d80),
[PartDesignGui::TaskRevolutionParameters::TaskRevolutionParameters()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#a5509b04d5cfc1da7d5314c4a038a01e2),
[Sketcher::SketchObject::trim()](../../d9/dad/classSketcher_1_1SketchObject.html#a55c244742ef90c7bc339e6c0285e2027),
[Gui::ViewProviderGeometryObject::updateData()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a4818bdc22e4b19444d703d72bec9d7ca),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[FemGui::ViewProviderFemMesh::updateData()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a2b42be80762272d7f6be0b30e7d6a3f5),
[Gui::ViewProviderDragger::updateData()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a6d433c9fe9d47fa7ab9be6d7e01d6509),
[SketcherGui::ViewProviderSketch::updateData()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#aa3039dd97c10d7c17a0c9e193ff059f4),
[TechDrawGui::ViewProviderTemplate::updateData()](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#af08c8e552302f0c07734e06211b6fb17),
[PartDesignGui::ViewProviderBody::updateData()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a2a541fb893a7130314f3c7161c33477e),
[PartDesignGui::ViewProviderBody::updateOriginDatumSize()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3c7c680a5e55c6cc695c82c8b45935c0),
[Gui::ViewProviderOriginGroupExtension::updateOriginSize()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a254bd812cc1814ed270f1d92e445ad8e),
[TechDrawGui::MDIViewPage::updateTemplate()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5dad0574c1df0a7c6398e90173300461),
[Gui::RecoveryWriter::writeFiles()](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c),
[App::PropertyLinkList::~PropertyLinkList()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aef7be25314c8c5441d9baa207ddd51c1),
[App::PropertyLinkSub::~PropertyLinkSub()](../../d3/d76/classApp_1_1PropertyLinkSub.html#ac2366078790473115b614fdc02345a4a),
[App::PropertyLinkSubList::~PropertyLinkSubList()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17189b0ae71b797884f1ca041cfe263f),
and
[PartDesignGui::TaskDatumParameters::~TaskDatumParameters()](../../d1/d52/classPartDesignGui_1_1TaskDatumParameters.html#a5a7f379ad21fc1a6ffa05fbd0ae2ac7a).

## ◆ operator=()

| [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) & Base::BaseClass::operator=  | ( | const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) & | | ) |   
---|---|---|---|---|---  
default  
  
## ◆ setPyObject()

| void BaseClass::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | | ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a885362f14defce5319c6408c6d3e6619),
[App::PropertyMatrix](../../d8/d77/classApp_1_1PropertyMatrix.html#acafac46829f35ee8d5ba1a0c8f93699a),
[App::PropertyPythonObject](../../d7/d1d/classApp_1_1PropertyPythonObject.html#abc4c47fe0adc00e73cf00e56223d058e),
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#a01766b286f7ee23f14008042a2465044),
[App::PropertyPath](../../dc/d24/classApp_1_1PropertyPath.html#a92d1b2427c49697efcfafd14d3334dec),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#aa715a8742ad95f4288e987f2f20d4719),
[App::PropertyIntegerConstraint](../../d2/dc8/classApp_1_1PropertyIntegerConstraint.html#a59de0c197b75f6ad9e00c93bb02611b3),
[App::PropertyIntegerSet](../../d0/df3/classApp_1_1PropertyIntegerSet.html#aa0d982d5ea1afa7166b371fea264a46c),
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html#aa54c6966882b6efda54747614cf046ce),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#aaf2edab1753863426d8b78dd15dab006),
[App::PropertyFloatConstraint](../../da/d0f/classApp_1_1PropertyFloatConstraint.html#acb90ab8757a5dfcc66fbe2e468f0d342),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#ac9b0f60fd6949cfd514653838e78840b),
[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html#ad5e4def7b10ab58f03abac6d29d40ea4),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#addcd7e7adacdc4cbbf4140b2f81e6066),
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#a6e633e7e63cde42f29ea066464910433),
[App::PropertyMaterial](../../d0/df5/classApp_1_1PropertyMaterial.html#a94fac01cb99c56b31e5ab8714e805c6a),
[App::PropertyQuantity](../../d4/d65/classApp_1_1PropertyQuantity.html#a72be43d71c5e5a5e0a174c01df176dc9),
[App::PropertyQuantityConstraint](../../dc/d51/classApp_1_1PropertyQuantityConstraint.html#a299ac9ee7870f29d5c3640a14114fcbe),
[Gui::AbstractSplitView](../../d1/d0b/classGui_1_1AbstractSplitView.html#a28ef18f0d2e7d0df1ad988c260be2ef0),
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a92c31c8879ec3267f07ba7c1b3833a40),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#ac56284294ef247339824c9af04dd6041),
[Part::PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html#a97ddf273f653e0c221d3c2195936383f),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#a474fea9679d300308bf22f966059dc6c),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a42361ce1e334ae05f364979de6d07fe0),
[Part::TopoShape](../../d8/ded/classPart_1_1TopoShape.html#aeedacd07a37185889171e75fa611a48b),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#abd2653a13c2d2f67c0956254c9c53cc9),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#ac56284294ef247339824c9af04dd6041),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#aacaab8574af8c691f4dce84ac11dcb44),
[TechDraw::PropertyCenterLineList](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a6f82ec0dc8ffa3315489f1600e86361b),
[TechDraw::PropertyCosmeticEdgeList](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a8c121ece9540d44ea36cf5fa2e0c6a1a),
[TechDraw::PropertyCosmeticVertexList](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#adc11907d4af9484d2a8b66275650d60e),
[TechDraw::PropertyGeomFormatList](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9e3ce8e86d86a734529407952a8926b4),
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a4b33a8605c64957b260f12dde55fb000),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a4e4eae3cb50d20fece89b7aac9fa6324),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a30868378554db499b38da470bfa520d7),
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#a636fa584705a1852eeab7e32e09f0846),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a8df27dbc0e724558a372f813a7eda649),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9965507bfcc6e28d251ffb62f234df77),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a495ec38be0d7ceb20aa9b3d5a520fdfa),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#adb26821a0a3916e6252bc6b4f0c5637e),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a7160ec1120efe0609b40286324fc861f),
[App::PropertyXLinkList](../../df/d17/classApp_1_1PropertyXLinkList.html#a2f618a6e3542cb338064a4d268277290),
[App::PropertyBoolList](../../d1/dcf/classApp_1_1PropertyBoolList.html#a4ab8f10b4974f5651b2cb3779de59543),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a6a9c116d0d7fe34797e507ad9b721ab4),
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#abe5101ec8034e76ef365e44f117b1f52),
[App::PropertyLists](../../d4/da1/classApp_1_1PropertyLists.html#a47e37fe20890a5258c0351c6f3244d60),
[App::PropertyLinkListBase](../../d7/d87/classApp_1_1PropertyLinkListBase.html#abb19832fb17826dbd569fe899db6a31f),
[Base::Exception](../../d8/df7/classBase_1_1Exception.html#afdfd5b57a05575d1ec05297e2f6e656e),
[Base::FileException](../../d1/dc2/classBase_1_1FileException.html#ae17c092fdac1087551869fd28dc9d6d4),
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#add817102ce4512bfbd7f185a7a0735f7),
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a2677acc3bef4dd4bccc8f07b4347b3ef),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#ae028342b89927960121a0d442b339367),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#adcc52946d50ff84a60f9cf1a4f463d74),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#aeddab8ff96cef05fb3dbaf7a7c36e584),
[Path::PropertyPath](../../da/d75/classPath_1_1PropertyPath.html#af4297e61552ea9c6726b298dc9844c23),
[Path::PropertyTool](../../d4/d51/classPath_1_1PropertyTool.html#aed0a7a6cd94103bac077c879be1b4d40),
[Path::PropertyTooltable](../../d4/d86/classPath_1_1PropertyTooltable.html#a54000b865f69a5f681f2297e523444f8),
[Points::PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a8bf9bdf3ba31ddfc289e30dbfaa3ee53),
[Robot::PropertyTrajectory](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#a7c387e5c6b344bae413e1325212cdced),
[App::PropertyListsT< T, ListT, ParentT
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
[App::PropertyListsT< bool, boost::dynamic_bitset<>
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
[App::PropertyListsT< Color
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
[App::PropertyListsT< double
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
[App::PropertyListsT< long
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
[App::PropertyListsT< DocumentObject *, std::vector< DocumentObject * >,
PropertyLinkListBase
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
[App::PropertyListsT< Material
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
[App::PropertyListsT< Base::Placement
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
[App::PropertyListsT< std::string
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2),
and [App::PropertyListsT< Base::Vector3d
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a167e678a8bbda0fc86d12052442501b2).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/BaseClass.h
  * FreeCAD/src/Base/BaseClass.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

