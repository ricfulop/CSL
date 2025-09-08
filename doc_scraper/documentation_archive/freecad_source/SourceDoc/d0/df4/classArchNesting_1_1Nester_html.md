---
url: https://freecad.github.io/SourceDoc/d0/df4/classArchNesting_1_1Nester.html
scraped_at: 2025-09-08T14:57:59.293584
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchNesting](../../d1/df6/namespaceArchNesting.html)
  * [Nester](../../d0/df4/classArchNesting_1_1Nester.html)

[List of all members](../../d9/d9e/classArchNesting_1_1Nester-members.html) | Public Member Functions | Public Attributes

ArchNesting.Nester Class Reference

##  Public Member Functions  
  
---  
def | [addContainer](../../d0/df4/classArchNesting_1_1Nester.html#a80f37ff12d1d5e1ddb848a57fae78eca) (self, [container](../../d0/df4/classArchNesting_1_1Nester.html#af1b163fa45a0da2bb89dbf23548595f5))  
def | [addObjects](../../d0/df4/classArchNesting_1_1Nester.html#a1f946b09a59e8cbfa07786ad9efd1c1e) (self, [objects](../../d0/df4/classArchNesting_1_1Nester.html#a71fb6b461a18039fbefc657cfda2628e))  
def | [apply](../../d0/df4/classArchNesting_1_1Nester.html#a5a54761a94bf3b3a500582014b33a8bc) (self, result=None)  
def | [clear](../../d0/df4/classArchNesting_1_1Nester.html#a5a000afd19e4cceaa9b0cea8be980f92) (self)  
def | [getPlacements](../../d0/df4/classArchNesting_1_1Nester.html#a24f5650e8c530e09ddd0dcbc4c92cee8) (self, result=None)  
def | [order](../../d0/df4/classArchNesting_1_1Nester.html#a31f3390689c0459bc70d4423d6ca3f86) (self, face, right=False)  
def | [run](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102) (self)  
def | [show](../../d0/df4/classArchNesting_1_1Nester.html#aadb46093c1b96874f1b2e427ddd3f1a5) (self, result=None)  
def | [stop](../../d0/df4/classArchNesting_1_1Nester.html#aaebbb77aef4e56a2ab7331f4874c85f4) (self)  
def | [update](../../d0/df4/classArchNesting_1_1Nester.html#ad7736f2ff11e9e1a0c886a3e55b74ad6) (self)  
  
##  Public Attributes  
  
---  
|
[container](../../d0/df4/classArchNesting_1_1Nester.html#af1b163fa45a0da2bb89dbf23548595f5)  
|
[indexedFaces](../../d0/df4/classArchNesting_1_1Nester.html#aef6e850836b9cd6ef00163101c8f66ea)  
|
[indexedfaces](../../d0/df4/classArchNesting_1_1Nester.html#a677c1bd01ad8e1f581774919e7649b2c)  
|
[objects](../../d0/df4/classArchNesting_1_1Nester.html#a71fb6b461a18039fbefc657cfda2628e)  
|
[progress](../../d0/df4/classArchNesting_1_1Nester.html#a08ac3079604c69edfc8e3382a677d6d8)  
|
[results](../../d0/df4/classArchNesting_1_1Nester.html#a345b57475506635cb4ab5bb8651d077e)  
|
[running](../../d0/df4/classArchNesting_1_1Nester.html#a3c9d77ec3ccf563dde6bacc82c6f7cd6)  
|
[setCounter](../../d0/df4/classArchNesting_1_1Nester.html#aa9404fce92570c3c8d342bb39e02b62a)  
|
[shapes](../../d0/df4/classArchNesting_1_1Nester.html#aed7787ad1f42e7e27147330762081bfb)  
  
## Member Function Documentation

## ◆ addContainer()

def ArchNesting.Nester.addContainer  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _container_  
| ) | |   
      
    
    addContainer(object): adds a FreeCAD DocumentObject as the container

References
[ArchNesting.Nester.container](../../d0/df4/classArchNesting_1_1Nester.html#af1b163fa45a0da2bb89dbf23548595f5),
[ArchPanel.NestTaskPanel.container](../../da/d77/classArchPanel_1_1NestTaskPanel.html#af4752ba237d06aadc692f555cbda3c66),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.hidden_element_over_riding_styled_item.container(),
and nlohmann::detail::iteration_proxy< IteratorType >.container.

## ◆ addObjects()

def ArchNesting.Nester.addObjects  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _objects_  
| ) | |   
      
    
    addObjects(objects): adds FreeCAD DocumentObjects to the nester

References App::MergeDocuments.objects, Gui::MergeDocuments.objects,
[ArchNesting.Nester.objects](../../d0/df4/classArchNesting_1_1Nester.html#a71fb6b461a18039fbefc657cfda2628e),
[ArchVRM.Renderer.objects](../../d5/dfd/classArchVRM_1_1Renderer.html#acb7fcee04d6acbec95828793cc7735fa),
[exportIFCHelper.ContextCreator.objects](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#affe82dba355ac1fcde6142df2dbc88fb),
[importIFCHelper.ProjectImporter.objects](../../d0/d2c/classimportIFCHelper_1_1ProjectImporter.html#ad45d68ab09fc5ee8f99e06cd423d58f8),
[PartGui::Ui_Mirroring.shapes](../../d7/d25/classPartGui_1_1Ui__Mirroring.html#a14237f21c9d1b595b129bb6d1152a2ef),
[ArchNesting.Nester.shapes](../../d0/df4/classArchNesting_1_1Nester.html#aed7787ad1f42e7e27147330762081bfb),
[ArchPanel.NestTaskPanel.shapes](../../da/d77/classArchPanel_1_1NestTaskPanel.html#aea539396a62cf1e98ae5e20bf671c070),
[ArchVRM.Renderer.shapes](../../d5/dfd/classArchVRM_1_1Renderer.html#aa8cca10507837180c0cfea82a1d67f9e),
[MeshPartGui::Mesh2ShapeGmsh::Private.shapes](../../db/dff/classMesh2ShapeGmsh_1_1Private.html#aa141e7e29a8bff58da6a9c0d93e1e071),
and
[PathScripts.PathDressupDogbone.ObjectDressup.shapes](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a46bb0b891c7ada9669ed3ff732084a80).

Referenced by
[ArchNesting.Nester.apply()](../../d0/df4/classArchNesting_1_1Nester.html#a5a54761a94bf3b3a500582014b33a8bc).

## ◆ apply()

def ArchNesting.Nester.apply  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _result_ = `None`  
| ) | |   
      
    
    apply([result]): Applies the computed placements of the given
    result, or the last computed result if none is given, to the
    document objects given to the nester via addObjects() before
    running.

References
[ArchNesting.Nester.addObjects()](../../d0/df4/classArchNesting_1_1Nester.html#a1f946b09a59e8cbfa07786ad9efd1c1e),
[ArchNesting.Nester.getPlacements()](../../d0/df4/classArchNesting_1_1Nester.html#a24f5650e8c530e09ddd0dcbc4c92cee8),
App::MergeDocuments.objects, Gui::MergeDocuments.objects,
[ArchNesting.Nester.objects](../../d0/df4/classArchNesting_1_1Nester.html#a71fb6b461a18039fbefc657cfda2628e),
[ArchVRM.Renderer.objects](../../d5/dfd/classArchVRM_1_1Renderer.html#acb7fcee04d6acbec95828793cc7735fa),
[exportIFCHelper.ContextCreator.objects](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#affe82dba355ac1fcde6142df2dbc88fb),
and
[importIFCHelper.ProjectImporter.objects](../../d0/d2c/classimportIFCHelper_1_1ProjectImporter.html#ad45d68ab09fc5ee8f99e06cd423d58f8).

## ◆ clear()

def ArchNesting.Nester.clear  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    clear(): Removes all objects and shape from the nester

References App::MergeDocuments.objects, Gui::MergeDocuments.objects,
[ArchNesting.Nester.objects](../../d0/df4/classArchNesting_1_1Nester.html#a71fb6b461a18039fbefc657cfda2628e),
[ArchVRM.Renderer.objects](../../d5/dfd/classArchVRM_1_1Renderer.html#acb7fcee04d6acbec95828793cc7735fa),
[exportIFCHelper.ContextCreator.objects](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#affe82dba355ac1fcde6142df2dbc88fb),
[importIFCHelper.ProjectImporter.objects](../../d0/d2c/classimportIFCHelper_1_1ProjectImporter.html#ad45d68ab09fc5ee8f99e06cd423d58f8),
[PartGui::Ui_Mirroring.shapes](../../d7/d25/classPartGui_1_1Ui__Mirroring.html#a14237f21c9d1b595b129bb6d1152a2ef),
[ArchNesting.Nester.shapes](../../d0/df4/classArchNesting_1_1Nester.html#aed7787ad1f42e7e27147330762081bfb),
[ArchPanel.NestTaskPanel.shapes](../../da/d77/classArchPanel_1_1NestTaskPanel.html#aea539396a62cf1e98ae5e20bf671c070),
[ArchVRM.Renderer.shapes](../../d5/dfd/classArchVRM_1_1Renderer.html#aa8cca10507837180c0cfea82a1d67f9e),
[MeshPartGui::Mesh2ShapeGmsh::Private.shapes](../../db/dff/classMesh2ShapeGmsh_1_1Private.html#aa141e7e29a8bff58da6a9c0d93e1e071),
and
[PathScripts.PathDressupDogbone.ObjectDressup.shapes](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a46bb0b891c7ada9669ed3ff732084a80).

## ◆ getPlacements()

def ArchNesting.Nester.getPlacements  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _result_ = `None`  
| ) | |   
      
    
    getPlacements([result]): returns a dictionary of hashCode:Placement
    pairs from the given result or the last computed result if none
    is given. The Placement contains a translation vector and a rotation
    to be given to the final object.

References
[ArchNesting.Nester.container](../../d0/df4/classArchNesting_1_1Nester.html#af1b163fa45a0da2bb89dbf23548595f5),
[ArchPanel.NestTaskPanel.container](../../da/d77/classArchPanel_1_1NestTaskPanel.html#af4752ba237d06aadc692f555cbda3c66),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.hidden_element_over_riding_styled_item.container(),
nlohmann::detail::iteration_proxy< IteratorType >.container,
[ArchNesting.Nester.indexedfaces](../../d0/df4/classArchNesting_1_1Nester.html#a677c1bd01ad8e1f581774919e7649b2c),
[ArchNesting.Nester.results](../../d0/df4/classArchNesting_1_1Nester.html#a345b57475506635cb4ab5bb8651d077e),
[femsolver.run.Machine.results](../../d2/d54/classfemsolver_1_1run_1_1Machine.html#a58e976fdf9ab89d6d485c24ac1656424),
AdaptivePath::Adaptive2d.results, and KDL::ChainIdSolver_Vereshchagin.results.

Referenced by
[ArchNesting.Nester.apply()](../../d0/df4/classArchNesting_1_1Nester.html#a5a54761a94bf3b3a500582014b33a8bc).

## ◆ order()

def ArchNesting.Nester.order  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _face_ ,   
|  |  | _right_ = `False`  
| ) | |   
      
    
    order(face,[right]): returns a list of vertices
    ordered clockwise. The first vertex will be the
    lefmost one, unless right is True, in which case the
    first vertex will be the rightmost one

References
[WorkingPlane.plane](../../d8/d4a/namespaceWorkingPlane.html#acd818647b5d80bd53b91ee7d60184f68),
and
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc).

Referenced by
[femtaskpanels.task_mesh_gmsh._TaskPanel.choose_order()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a1675090caa83cf98146c3ebcf59f482d),
[femtaskpanels.task_mesh_gmsh._TaskPanel.set_mesh_params()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a23ddf7b0852aa5fc2e9b156d40c10348),
[femmesh.gmshtools.GmshTools.start_logs()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#a104c2b9029c0449985fa2dc07b6d82e1),
[femtaskpanels.task_mesh_gmsh._TaskPanel.update()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a684d236263b413e2d04839f3ce9cacb7),
and
[femmesh.gmshtools.GmshTools.write_geo()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#a33c814384f75e15c1d5316754b9ff3bf).

## ◆ run()

def ArchNesting.Nester.run  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    run(): Runs a nesting operation. Returns a list of lists of
       shapes, each primary list being one filled container, or None
       if the operation failed.

References
[ArchNesting.Nester.container](../../d0/df4/classArchNesting_1_1Nester.html#af1b163fa45a0da2bb89dbf23548595f5),
[ArchPanel.NestTaskPanel.container](../../da/d77/classArchPanel_1_1NestTaskPanel.html#af4752ba237d06aadc692f555cbda3c66),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.hidden_element_over_riding_styled_item.container(),
nlohmann::detail::iteration_proxy< IteratorType >.container,
[ArchNesting.Nester.progress](../../d0/df4/classArchNesting_1_1Nester.html#a08ac3079604c69edfc8e3382a677d6d8),
App::PropertyExpressionEngine.running,
[Gui::GUISingleApplication::Private.running](../../de/d95/classGUISingleApplication_1_1Private.html#a234dd9850ce81fb2fc2b4f3e5dc0f1f1),
[Gui::PythonDebuggerP.running](../../dd/d38/structGui_1_1PythonDebuggerP.html#a329cefdb0a36e18393686125b4f1a161),
[ArchNesting.Nester.running](../../d0/df4/classArchNesting_1_1Nester.html#a3c9d77ec3ccf563dde6bacc82c6f7cd6),
[draftguitools.gui_edit.Edit.running](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#abf1810a90fc3c1f2b643732c550c46ed),
[draftguitools.gui_line_add_delete.AddPoint.running](../../d2/d9e/classdraftguitools_1_1gui__line__add__delete_1_1AddPoint.html#a329aee08b773c79de011e27174ecbfec),
[draftguitools.gui_line_add_delete.DelPoint.running](../../df/d89/classdraftguitools_1_1gui__line__add__delete_1_1DelPoint.html#a822a8fa16762013e84276301c3355cd2),
[draftguitools.gui_offset.Offset.running](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#ae110940840334cdf45eb724e0c9819eb),
[draftguitools.gui_snapper.Snapper.running](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#aebc3cfd274c8cf3c0b21ea89a9cdca80),
[draftguitools.gui_wire2spline.WireToBSpline.running](../../d4/dd5/classdraftguitools_1_1gui__wire2spline_1_1WireToBSpline.html#a5eb297420e1b5de6a33384b85233b781),
[femsolver.task.Task.running](../../de/d04/classfemsolver_1_1task_1_1Task.html#af48a1d33b3e78f68630b652123a4f698),
AdaptivePath::PerfCounter.running,
[qtunittest.BaseGUITestRunner.running](../../d3/d45/classqtunittest_1_1BaseGUITestRunner.html#abf0ceb25f6f4ea86ef24c810267d6e35),
[Mod.Test.unittestgui.BaseGUITestRunner.running](../../d0/db5/classMod_1_1Test_1_1unittestgui_1_1BaseGUITestRunner.html#a1399d55b56d4b54022bc9188831295f4),
[PartGui::Ui_Mirroring.shapes](../../d7/d25/classPartGui_1_1Ui__Mirroring.html#a14237f21c9d1b595b129bb6d1152a2ef),
[ArchNesting.Nester.shapes](../../d0/df4/classArchNesting_1_1Nester.html#aed7787ad1f42e7e27147330762081bfb),
[ArchPanel.NestTaskPanel.shapes](../../da/d77/classArchPanel_1_1NestTaskPanel.html#aea539396a62cf1e98ae5e20bf671c070),
[ArchVRM.Renderer.shapes](../../d5/dfd/classArchVRM_1_1Renderer.html#aa8cca10507837180c0cfea82a1d67f9e),
[MeshPartGui::Mesh2ShapeGmsh::Private.shapes](../../db/dff/classMesh2ShapeGmsh_1_1Private.html#aa141e7e29a8bff58da6a9c0d93e1e071),
[PathScripts.PathDressupDogbone.ObjectDressup.shapes](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a46bb0b891c7ada9669ed3ff732084a80),
[Gui::LinkInfo.update()](../../d4/da4/classGui_1_1LinkInfo.html#a7dd19269fe6dd6676db6bfea88888bd2),
[package_details.PackageDetails.update](../../d1/df5/classpackage__details_1_1PackageDetails.html#af7f6a235f71273a50cad0ffa84d01f0b),
[MeshGui::MeshRenderer::Private.update()](../../d9/d1e/classMeshRenderer_1_1Private.html#a5bf2d339a50ea2b972fab5e6797dc0aa),
[MeshGui::MeshRenderer.update()](../../df/dcd/classMeshGui_1_1MeshRenderer.html#aa455c44c36b1458ecf4c65afc3cf0f49),
[TechDrawGui::TaskDlgActiveView.update()](../../da/d0b/classTechDrawGui_1_1TaskDlgActiveView.html#a495ee05844089b3fc687560d70605be7),
[TechDrawGui::TaskDlgBalloon.update()](../../d5/d4f/classTechDrawGui_1_1TaskDlgBalloon.html#a5d3f6a432e7586aaaf8217a90b775131),
[TechDrawGui::TaskDlgCenterLine.update()](../../d8/d49/classTechDrawGui_1_1TaskDlgCenterLine.html#ae53b60f20f8b1905ed4db0d3d410c096),
[TechDrawGui::TaskDlgCosmeticLine.update()](../../d6/d1e/classTechDrawGui_1_1TaskDlgCosmeticLine.html#aa29c782de688b21662ad29b976282d63),
[TechDrawGui::TaskDlgCosVertex.update()](../../d1/d66/classTechDrawGui_1_1TaskDlgCosVertex.html#a4bf633f7130cdb22372f772b61535a5b),
[TechDrawGui::TaskDlgCustomizeFormat.update()](../../d8/d2e/classTechDrawGui_1_1TaskDlgCustomizeFormat.html#a9b795fe5d04ad5e9eaa6fd416f09551d),
[TechDrawGui::TaskDlgDetail.update()](../../dd/d8e/classTechDrawGui_1_1TaskDlgDetail.html#a19f4ec27593a7f16fd62d75238ad3bc7),
[TechDrawGui::TaskDlgDimension.update()](../../d8/d6e/classTechDrawGui_1_1TaskDlgDimension.html#af8bb7e7af20845d87f1332ec4a034055),
[TechDrawGui::TaskDlgGeomHatch.update()](../../d0/da0/classTechDrawGui_1_1TaskDlgGeomHatch.html#a3b67a35c97caa5ca81aace6347b21e13),
[TechDrawGui::TaskDlgHatch.update()](../../d8/d00/classTechDrawGui_1_1TaskDlgHatch.html#ab270d3bc62071dce6fb1360dd2254751),
[TechDrawGui::TaskDlgLeaderLine.update()](../../dc/d59/classTechDrawGui_1_1TaskDlgLeaderLine.html#a2f4f14d9d1bc52caa8abc461d951f65e),
[TechDrawGui::TaskDlgLinkDim.update()](../../dd/d18/classTechDrawGui_1_1TaskDlgLinkDim.html#a1ce19f8c096441e58dcf37f0475ed0ba),
[TechDrawGui::TaskDlgProjection.update()](../../d0/dc4/classTechDrawGui_1_1TaskDlgProjection.html#a9ab0538115e8e78ee12c5f93dd26f389),
[TechDrawGui::TaskDlgProjGroup.update()](../../df/df7/classTechDrawGui_1_1TaskDlgProjGroup.html#acd286a79f6b95689a58baffb50486886),
[TechDrawGui::TaskDlgRichAnno.update()](../../d7/d2b/classTechDrawGui_1_1TaskDlgRichAnno.html#ae074289720e076dd5c918431f98e52ee),
[TechDrawGui::TaskDlgSectionView.update()](../../d5/d7e/classTechDrawGui_1_1TaskDlgSectionView.html#a8773fe58eddc6c5d017576c2ffd5e65c),
[TechDrawGui::TaskDlgSelectLineAttributes.update()](../../df/d4a/classTechDrawGui_1_1TaskDlgSelectLineAttributes.html#a0d9c0d69fe47ffe5950edd734bfe1041),
[TechDrawGui::TaskDlgWeldingSymbol.update()](../../d8/da3/classTechDrawGui_1_1TaskDlgWeldingSymbol.html#abd5f53733ad5661baa179d968b7c220e),
SMESHDS_GroupOnFilter.update(),
[App::LinkBaseExtension.update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979),
[Gui::ViewProvider.update()](../../d3/db3/classGui_1_1ViewProvider.html#abe1fb2bbe6e5b05d95bb6dc9798016d8),
[Gui::ViewProviderDocumentObject.update()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a6e0dd163d7555c35d78c29a504c0b2ce),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.update()](../../d9/dcc/classnlohmann_1_1basic__json.html#a377819905d567f6f523dcbc592cb6356),
ArchAxis._AxisTaskPanel.update(),
[ArchAxisSystem.AxisSystemTaskPanel.update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchComponent.ComponentTaskPanel.update()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#af95b36032a3837b4bf1b92fe7c6a47e0),
[ArchGrid.ArchGridTaskPanel.update()](../../d6/da7/classArchGrid_1_1ArchGridTaskPanel.html#aa5b897c2d0a3062c697b216ab65fbbff),
[ArchNesting.Nester.update()](../../d0/df4/classArchNesting_1_1Nester.html#ad7736f2ff11e9e1a0c886a3e55b74ad6),
ArchRoof._RoofTaskPanel.update(),
[ArchSectionPlane.SectionPlaneTaskPanel.update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162),
ArchWindow._ArchWindowTaskPanel.update(),
[DraftGui.FacebinderTaskPanel.update()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a191f43aa777ae22c42a00d118688bafe),
[draftguitools.gui_trackers.gridTracker.update()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a6231ad421262eeb1def5b0eda4ddadcc),
[femtaskpanels.task_mesh_gmsh._TaskPanel.update()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a684d236263b413e2d04839f3ce9cacb7),
[femtaskpanels.task_result_mechanical._TaskPanel.update()](../../d1/d11/classfemtaskpanels_1_1task__result__mechanical_1_1__TaskPanel.html#a9f80527a25c6dbe7e9452f4f7b6ac487),
[femtaskpanels.task_solver_ccxtools._TaskPanel.update()](../../da/df4/classfemtaskpanels_1_1task__solver__ccxtools_1_1__TaskPanel.html#ab71f275d8aa529999c628cf0435e9874),
Mod.PartDesign.InvoluteGearFeature._InvoluteGearTaskPanel.update(),
[Mod.PartDesign.SprocketFeature.SprocketTaskPanel.update()](../../db/d2b/classMod_1_1PartDesign_1_1SprocketFeature_1_1SprocketTaskPanel.html#a2d51a2444ae596a584086c459f0fabe1),
[Plot.Plot.update()](../../d3/d54/classPlot_1_1Plot.html#a8d1d0cc9752804c98f5edf85fe98afc0),
[Spreadsheet_legacy.SpreadsheetView.update()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a6b8b5507ed8e99fba528d939acab02fc),
[DocumentObject.ViewProvider.update()](../../d8/dd7/classDocumentObject_1_1ViewProvider.html#a9372f6952d94e76cf28462c1957a77d4),
[AddonManager.CommandAddonManager.update()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#a9fb1423755e16ebc88ece93f8c1a3a9a),
[draftguitools.gui_trackers.radiusTracker.update()](../../d2/d08/classdraftguitools_1_1gui__trackers_1_1radiusTracker.html#a341367490258777e1800a1c205e072bf),
[ArchCommands.SurveyTaskPanel.update()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a77685c35ce185891696d5ac525070003),
[Mod.PartDesign.WizardShaft.ShaftDiagram.Diagram.update()](../../d9/d97/classMod_1_1PartDesign_1_1WizardShaft_1_1ShaftDiagram_1_1Diagram.html#a7dbcfc52379def311707bc63d73d8edc),
[addonmanager_workers.GitProgressMonitor.update()](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#a792da2433df991c6af7f84aa5d557918),
[draftguitools.gui_trackers.boxTracker.update()](../../d5/dca/classdraftguitools_1_1gui__trackers_1_1boxTracker.html#a17b09ebf946c0767ce1236e269f5a518),
[draftguitools.gui_edit.Edit.update()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#a0c2dd06059cea69710a97ceb2fbc8d0a),
[draftguitools.gui_trackers.rectangleTracker.update()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#acedcfce459af33f633a1aa7e57501a7f),
[ArchPanel.CommandPanel.update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c),
ArchStructure._CommandStructure.update(), ArchWall._CommandWall.update(),
ArchWindow._CommandWindow.update(),
[draftguitools.gui_trackers.bsplineTracker.update()](../../d4/d09/classdraftguitools_1_1gui__trackers_1_1bsplineTracker.html#a780d90044fb459aa47487afc9d7979c9),
[draftguitools.gui_trackers.bezcurveTracker.update()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#a768d7d59cf62a7cfe8fbdc4486a17a63),
[draftguitools.gui_trackers.dimTracker.update()](../../d2/d2f/classdraftguitools_1_1gui__trackers_1_1dimTracker.html#a111e856fb5d7812ce0034fb5eb400a29),
[draftguitools.gui_trackers.wireTracker.update()](../../dc/dfc/classdraftguitools_1_1gui__trackers_1_1wireTracker.html#a06640e7b526a420f36ef66f5e2c516fb),
and
[PartDesign::SubShapeBinder.update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83).

Referenced by
[femexamples.examplesgui.FemExamples.clicked()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ad3b96de3e075bb69e51539a3c99dfd14),
and
[femsolver.task.Task.protector()](../../de/d04/classfemsolver_1_1task_1_1Task.html#a913c60a87594a8bfe76580d27effcb51).

## ◆ show()

def ArchNesting.Nester.show  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _result_ = `None`  
| ) | |   
      
    
    show([result]): creates shapes in the document, showing
       the given result (list of sheets) or the last result if
       none is provided

References
[ArchNesting.Nester.container](../../d0/df4/classArchNesting_1_1Nester.html#af1b163fa45a0da2bb89dbf23548595f5),
[ArchPanel.NestTaskPanel.container](../../da/d77/classArchPanel_1_1NestTaskPanel.html#af4752ba237d06aadc692f555cbda3c66),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.hidden_element_over_riding_styled_item.container(),
nlohmann::detail::iteration_proxy< IteratorType >.container,
[ArchNesting.Nester.results](../../d0/df4/classArchNesting_1_1Nester.html#a345b57475506635cb4ab5bb8651d077e),
[femsolver.run.Machine.results](../../d2/d54/classfemsolver_1_1run_1_1Machine.html#a58e976fdf9ab89d6d485c24ac1656424),
AdaptivePath::Adaptive2d.results, and KDL::ChainIdSolver_Vereshchagin.results.

Referenced by
[Mod.Show.mTempoVis.TempoVis.show_all_dependencies()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a7ccd7b0b980b37bc61025400bcddc632),
and
[Mod.Show.mTempoVis.TempoVis.show_all_dependent()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#aebdf1f88e101dc1a927b20477f6e5730).

## ◆ stop()

def ArchNesting.Nester.stop  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    stop((): stops the computation

References App::PropertyExpressionEngine.running,
[Gui::GUISingleApplication::Private.running](../../de/d95/classGUISingleApplication_1_1Private.html#a234dd9850ce81fb2fc2b4f3e5dc0f1f1),
[Gui::PythonDebuggerP.running](../../dd/d38/structGui_1_1PythonDebuggerP.html#a329cefdb0a36e18393686125b4f1a161),
[ArchNesting.Nester.running](../../d0/df4/classArchNesting_1_1Nester.html#a3c9d77ec3ccf563dde6bacc82c6f7cd6),
[draftguitools.gui_edit.Edit.running](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#abf1810a90fc3c1f2b643732c550c46ed),
[draftguitools.gui_line_add_delete.AddPoint.running](../../d2/d9e/classdraftguitools_1_1gui__line__add__delete_1_1AddPoint.html#a329aee08b773c79de011e27174ecbfec),
[draftguitools.gui_line_add_delete.DelPoint.running](../../df/d89/classdraftguitools_1_1gui__line__add__delete_1_1DelPoint.html#a822a8fa16762013e84276301c3355cd2),
[draftguitools.gui_offset.Offset.running](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#ae110940840334cdf45eb724e0c9819eb),
[draftguitools.gui_snapper.Snapper.running](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#aebc3cfd274c8cf3c0b21ea89a9cdca80),
[draftguitools.gui_wire2spline.WireToBSpline.running](../../d4/dd5/classdraftguitools_1_1gui__wire2spline_1_1WireToBSpline.html#a5eb297420e1b5de6a33384b85233b781),
[femsolver.task.Task.running](../../de/d04/classfemsolver_1_1task_1_1Task.html#af48a1d33b3e78f68630b652123a4f698),
AdaptivePath::PerfCounter.running,
[qtunittest.BaseGUITestRunner.running](../../d3/d45/classqtunittest_1_1BaseGUITestRunner.html#abf0ceb25f6f4ea86ef24c810267d6e35),
and
[Mod.Test.unittestgui.BaseGUITestRunner.running](../../d0/db5/classMod_1_1Test_1_1unittestgui_1_1BaseGUITestRunner.html#a1399d55b56d4b54022bc9188831295f4).

Referenced by
[ArchPanel.NestTaskPanel.accept()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ad42cd95d7c0a23ddf59be8c4b2b4c85f),
and
[ArchPanel.NestTaskPanel.reject()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ae3ce3d1461b9cfc20c6bf6091114a8ce).

## ◆ update()

def ArchNesting.Nester.update  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    update(): internal function to verify if computation can
    go on

References
[ArchNesting.Nester.progress](../../d0/df4/classArchNesting_1_1Nester.html#a08ac3079604c69edfc8e3382a677d6d8),
App::PropertyExpressionEngine.running,
[Gui::GUISingleApplication::Private.running](../../de/d95/classGUISingleApplication_1_1Private.html#a234dd9850ce81fb2fc2b4f3e5dc0f1f1),
[Gui::PythonDebuggerP.running](../../dd/d38/structGui_1_1PythonDebuggerP.html#a329cefdb0a36e18393686125b4f1a161),
[ArchNesting.Nester.running](../../d0/df4/classArchNesting_1_1Nester.html#a3c9d77ec3ccf563dde6bacc82c6f7cd6),
[draftguitools.gui_edit.Edit.running](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#abf1810a90fc3c1f2b643732c550c46ed),
[draftguitools.gui_line_add_delete.AddPoint.running](../../d2/d9e/classdraftguitools_1_1gui__line__add__delete_1_1AddPoint.html#a329aee08b773c79de011e27174ecbfec),
[draftguitools.gui_line_add_delete.DelPoint.running](../../df/d89/classdraftguitools_1_1gui__line__add__delete_1_1DelPoint.html#a822a8fa16762013e84276301c3355cd2),
[draftguitools.gui_offset.Offset.running](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#ae110940840334cdf45eb724e0c9819eb),
[draftguitools.gui_snapper.Snapper.running](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#aebc3cfd274c8cf3c0b21ea89a9cdca80),
[draftguitools.gui_wire2spline.WireToBSpline.running](../../d4/dd5/classdraftguitools_1_1gui__wire2spline_1_1WireToBSpline.html#a5eb297420e1b5de6a33384b85233b781),
[femsolver.task.Task.running](../../de/d04/classfemsolver_1_1task_1_1Task.html#af48a1d33b3e78f68630b652123a4f698),
AdaptivePath::PerfCounter.running,
[qtunittest.BaseGUITestRunner.running](../../d3/d45/classqtunittest_1_1BaseGUITestRunner.html#abf0ceb25f6f4ea86ef24c810267d6e35),
[Mod.Test.unittestgui.BaseGUITestRunner.running](../../d0/db5/classMod_1_1Test_1_1unittestgui_1_1BaseGUITestRunner.html#a1399d55b56d4b54022bc9188831295f4),
[ArchNesting.Nester.setCounter](../../d0/df4/classArchNesting_1_1Nester.html#aa9404fce92570c3c8d342bb39e02b62a),
and
[ArchPanel.NestTaskPanel.setCounter()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ac7c67ca72068f6667c2fd40430960757).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchAxisSystem.AxisSystemTaskPanel.addElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a68544065aac91fa78a8bddb3e6ed5a99),
[ArchComponent.ComponentTaskPanel.addElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a21a385085defc9e8ccca8b2261a57314),
[ArchSectionPlane.SectionPlaneTaskPanel.addElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a6317c0ca7eb0c28e60b863f96ddeb81f),
[DraftGui.FacebinderTaskPanel.addElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a7642fdc6d6fa90afec25930af3b0a66e),
[femtaskpanels.task_result_mechanical._TaskPanel.calculate()](../../d1/d11/classfemtaskpanels_1_1task__result__mechanical_1_1__TaskPanel.html#aa2b98b5a9e12d62038ea9cc00366ecb6),
[Spreadsheet_legacy.SpreadsheetView.changeCell()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a897cda21a4a4f34431c371a31579706e),
[draftguitools.gui_edit.Edit.endEditing()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#ab9797631ba43c7855016e2552c21834f),
[draftguitools.gui_trackers.boxTracker.height()](../../d5/dca/classdraftguitools_1_1gui__trackers_1_1boxTracker.html#a25f7d7bbd56b5ff5ef5da124e515dd00),
[draftguitools.gui_trackers.rectangleTracker.p3()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a1bf47cdde1ea165a58946f1a5fdc6c8e),
[Plot.Plot.plot()](../../d3/d54/classPlot_1_1Plot.html#a8b670f38324a7fae1c7128e117cba688),
[Spreadsheet_legacy.SpreadsheetView.recompute()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a1d8b8256ad183347aedaf40a269c2d3a),
[ArchAxisSystem.AxisSystemTaskPanel.removeElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a27e3fe8ffbc52acfd92f2d333626a76d),
[ArchComponent.ComponentTaskPanel.removeElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#ad9d18ffd3ef7556affab6b62a6acceb5),
[ArchSectionPlane.SectionPlaneTaskPanel.removeElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a544dbf3def03e06b86e6f32c390fd46a),
[DraftGui.FacebinderTaskPanel.removeElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a8ce5c644e81d1fbb3907e351e2050a0a),
[draftguitools.gui_trackers.gridTracker.reset()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a2c6f7e1d0a817adacef8297962691a9c),
[ArchNesting.Nester.run()](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102),
[draftguitools.gui_trackers.gridTracker.setMainlines()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#ac1c96a4a6282724211bc61a37ffa5a05),
[draftguitools.gui_trackers.gridTracker.setSize()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a6bb2d86a97781159c083a23a30f9fb9a),
[draftguitools.gui_trackers.gridTracker.setSpacing()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a67fe5637d9f2b95d4c6c6a717f41e6e4),
and
[draftguitools.gui_edit_arch_objects.ArchWallGuiTools.update_object_from_edit_points()](../../d1/d46/classdraftguitools_1_1gui__edit__arch__objects_1_1ArchWallGuiTools.html#a1340bdc87e40eb0a04ba856255ae0f93).

## Member Data Documentation

## ◆ container

ArchNesting.Nester.container  
---  
  
Referenced by
[ArchNesting.Nester.addContainer()](../../d0/df4/classArchNesting_1_1Nester.html#a80f37ff12d1d5e1ddb848a57fae78eca),
[ArchPanel.NestTaskPanel.getContainer()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ad25ef9b5aade32a390de4a8bd34bafda),
[ArchNesting.Nester.getPlacements()](../../d0/df4/classArchNesting_1_1Nester.html#a24f5650e8c530e09ddd0dcbc4c92cee8),
[ArchPanel.NestTaskPanel.getShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a52edae24a9d124678d48b157749b5f04),
[ArchNesting.Nester.run()](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102),
[ArchNesting.Nester.show()](../../d0/df4/classArchNesting_1_1Nester.html#aadb46093c1b96874f1b2e427ddd3f1a5),
and
[ArchPanel.NestTaskPanel.start()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ae94d1620245089dea3da24cffad8f785).

## ◆ indexedFaces

ArchNesting.Nester.indexedFaces  
---  
  
## ◆ indexedfaces

ArchNesting.Nester.indexedfaces  
---  
  
Referenced by
[ArchNesting.Nester.getPlacements()](../../d0/df4/classArchNesting_1_1Nester.html#a24f5650e8c530e09ddd0dcbc4c92cee8).

## ◆ objects

ArchNesting.Nester.objects  
---  
  
Referenced by
[ArchNesting.Nester.addObjects()](../../d0/df4/classArchNesting_1_1Nester.html#a1f946b09a59e8cbfa07786ad9efd1c1e),
[ArchVRM.Renderer.addObjects()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae9d5501f6f159004a5735e337c03ef1e),
[ArchNesting.Nester.apply()](../../d0/df4/classArchNesting_1_1Nester.html#a5a54761a94bf3b3a500582014b33a8bc),
[ArchNesting.Nester.clear()](../../d0/df4/classArchNesting_1_1Nester.html#a5a000afd19e4cceaa9b0cea8be980f92),
and
[exportIFCHelper.ContextCreator.getProjectObject()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#aa3ac63346b1513523c069e16745f66c1).

## ◆ progress

ArchNesting.Nester.progress  
---  
  
Referenced by
[ArchNesting.Nester.run()](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102),
and
[ArchNesting.Nester.update()](../../d0/df4/classArchNesting_1_1Nester.html#ad7736f2ff11e9e1a0c886a3e55b74ad6).

## ◆ results

ArchNesting.Nester.results  
---  
  
Referenced by
[ArchNesting.Nester.getPlacements()](../../d0/df4/classArchNesting_1_1Nester.html#a24f5650e8c530e09ddd0dcbc4c92cee8),
[femsolver.run.Machine.reset()](../../d2/d54/classfemsolver_1_1run_1_1Machine.html#a343e584f0f5dfc40861c957397bd8952),
and
[ArchNesting.Nester.show()](../../d0/df4/classArchNesting_1_1Nester.html#aadb46093c1b96874f1b2e427ddd3f1a5).

## ◆ running

ArchNesting.Nester.running  
---  
  
Referenced by
[draftguitools.gui_edit.Edit.Activated()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#a9abe09a3ee3186ff88f606678ddc2ad6),
[draftguitools.gui_wire2spline.WireToBSpline.Activated()](../../d4/dd5/classdraftguitools_1_1gui__wire2spline_1_1WireToBSpline.html#afc3604f707c18d3e48b42d06a1ad4b5c),
[draftguitools.gui_edit.Edit.finish()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#a8d8bc8079f6beae1158a282fe64a9f02),
[draftguitools.gui_offset.Offset.finish()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a3dbf357ad9d4221f1802ab00c4d3d85b),
[draftguitools.gui_snapper.Snapper.off()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#abd73f787754ba838ce877bfcd2bbd59b),
[ArchNesting.Nester.run()](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102),
[draftguitools.gui_snapper.Snapper.snap()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#aa4079da5e5b0c5452130550a330d6891),
[draftguitools.gui_snapper.Snapper.snapToObject()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a2c5eb552fed1dc7a61c628dc393ae869),
[femsolver.task.Task.start()](../../de/d04/classfemsolver_1_1task_1_1Task.html#ae07e561f5593cd11cfca05e976bc023a),
[ArchNesting.Nester.stop()](../../d0/df4/classArchNesting_1_1Nester.html#aaebbb77aef4e56a2ab7331f4874c85f4),
and
[ArchNesting.Nester.update()](../../d0/df4/classArchNesting_1_1Nester.html#ad7736f2ff11e9e1a0c886a3e55b74ad6).

## ◆ setCounter

ArchNesting.Nester.setCounter  
---  
  
Referenced by
[ArchPanel.NestTaskPanel.start()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ae94d1620245089dea3da24cffad8f785),
and
[ArchNesting.Nester.update()](../../d0/df4/classArchNesting_1_1Nester.html#ad7736f2ff11e9e1a0c886a3e55b74ad6).

## ◆ shapes

ArchNesting.Nester.shapes  
---  
  
Referenced by
[ArchNesting.Nester.addObjects()](../../d0/df4/classArchNesting_1_1Nester.html#a1f946b09a59e8cbfa07786ad9efd1c1e),
[ArchVRM.Renderer.addObjects()](../../d5/dfd/classArchVRM_1_1Renderer.html#ae9d5501f6f159004a5735e337c03ef1e),
[ArchVRM.Renderer.addShapes()](../../d5/dfd/classArchVRM_1_1Renderer.html#aec9719059fd4a06e2cd43792827a985c),
[ArchNesting.Nester.clear()](../../d0/df4/classArchNesting_1_1Nester.html#a5a000afd19e4cceaa9b0cea8be980f92),
[ArchVRM.Renderer.cut()](../../d5/dfd/classArchVRM_1_1Renderer.html#a42a08e8de6110aefc78bdfd483206b10),
[ArchPanel.NestTaskPanel.getContainer()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ad25ef9b5aade32a390de4a8bd34bafda),
[ArchPanel.NestTaskPanel.getShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a52edae24a9d124678d48b157749b5f04),
[PathScripts.PathDressupDogbone.ObjectDressup.insertBone()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a5d52eb985f34b6eb0d161bc6e25de874),
[ArchPanel.NestTaskPanel.removeShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a14b88173115d5a126ac1d5a0bc973395),
[ArchNesting.Nester.run()](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102),
[PathScripts.PathDressupDogbone.ObjectDressup.setup()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#a810152e1fbb2f48646297c091e52d6a1),
and
[ArchPanel.NestTaskPanel.start()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ae94d1620245089dea3da24cffad8f785).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchNesting.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

