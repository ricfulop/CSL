---
url: https://freecad.github.io/SourceDoc/d4/dbf/classArchGrid_1_1ViewProviderArchGrid.html
scraped_at: 2025-09-08T14:57:47.232186
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchGrid](../../d7/d70/namespaceArchGrid.html)
  * [ViewProviderArchGrid](../../d4/dbf/classArchGrid_1_1ViewProviderArchGrid.html)

[List of all members](../../d4/d2c/classArchGrid_1_1ViewProviderArchGrid-members.html) | Public Member Functions

ArchGrid.ViewProviderArchGrid Class Reference

##  Public Member Functions  
  
---  
def | [doubleClicked](../../d4/dbf/classArchGrid_1_1ViewProviderArchGrid.html#a35948c50ff2dccdada47d584d8bf32bd) (self, vobj)  
def | [getIcon](../../d4/dbf/classArchGrid_1_1ViewProviderArchGrid.html#a4750f5e63bf35315588b68d81adf4607) (self)  
def | [setEdit](../../d4/dbf/classArchGrid_1_1ViewProviderArchGrid.html#ab678ebc5a0472704be09f9341557d24b) (self, vobj, mode=0)  
def | [unsetEdit](../../d4/dbf/classArchGrid_1_1ViewProviderArchGrid.html#a43c83113ebfab08826970e7a63709c5b) (self, vobj, mode)  
  
## Member Function Documentation

## ◆ doubleClicked()

def ArchGrid.ViewProviderArchGrid.doubleClicked  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_  
| ) | |   
  
References
[Gui::Document.setEdit()](../../de/d4e/classGui_1_1Document.html#a2064c6eb4172240d40a7f409febc81a9),
[Gui::ViewProvider.setEdit()](../../d3/db3/classGui_1_1ViewProvider.html#a99bfa17a3eedcec978d56b252a653fea),
[Gui::ViewProviderAnnotationLabel.setEdit()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a9e6d7fb0b017900b7ac12e21c88ceabc),
[Gui::ViewProviderPythonFeatureImp.setEdit()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a13e8deb11e95b3cb730e9d105ffc8517),
[DrawingGui::ViewProviderDrawingPage.setEdit()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a332f677694e4eb770dccc6698df4a27e),
[FemGui::ViewProviderFemAnalysis.setEdit()](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#ad43efa79b2a2ae8acb280614155105a6),
[FemGui::ViewProviderFemConstraint.setEdit()](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#afccdf7d794c7c6eb07c06404574c0b45),
[FemGui::ViewProviderFemConstraintBearing.setEdit()](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#ada0e85289207db1bc3b9ca4b1f03e6fc),
[FemGui::ViewProviderFemConstraintContact.setEdit()](../../d9/d3d/classFemGui_1_1ViewProviderFemConstraintContact.html#ab6aafc618f8c7b4737ef4d06dca0b739),
[FemGui::ViewProviderFemConstraintDisplacement.setEdit()](../../d7/d3f/classFemGui_1_1ViewProviderFemConstraintDisplacement.html#aa763ff22c3aa35dc8c6f3265b307287e),
[FemGui::ViewProviderFemConstraintFixed.setEdit()](../../d4/d9c/classFemGui_1_1ViewProviderFemConstraintFixed.html#a813e76666d3bc3aca1e3e47565c872e7),
[FemGui::ViewProviderFemConstraintFluidBoundary.setEdit()](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#adce6e7f53edbdcfdae6d45365ba57f0f),
[FemGui::ViewProviderFemConstraintForce.setEdit()](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#a39e8664ff886cf249a80a72df142ffa9),
[FemGui::ViewProviderFemConstraintGear.setEdit()](../../d1/d2f/classFemGui_1_1ViewProviderFemConstraintGear.html#aeaddd287de5da327467599e4fd5db37b),
[FemGui::ViewProviderFemConstraintHeatflux.setEdit()](../../d0/dea/classFemGui_1_1ViewProviderFemConstraintHeatflux.html#a097b2df936bd0057bc591268cff63859),
[FemGui::ViewProviderFemConstraintInitialTemperature.setEdit()](../../d8/d07/classFemGui_1_1ViewProviderFemConstraintInitialTemperature.html#a009f5341493d283dbd42b82f7fd27b68),
[FemGui::ViewProviderFemConstraintPlaneRotation.setEdit()](../../d7/d0a/classFemGui_1_1ViewProviderFemConstraintPlaneRotation.html#a206254f1c763260f072c36a215456a3d),
[FemGui::ViewProviderFemConstraintPressure.setEdit()](../../d4/d18/classFemGui_1_1ViewProviderFemConstraintPressure.html#a263f869ac7b10ee53176680a362e308a),
[FemGui::ViewProviderFemConstraintPulley.setEdit()](../../d8/dfc/classFemGui_1_1ViewProviderFemConstraintPulley.html#af3e6550cd186ed7c85d3a1e5a1ed5034),
[FemGui::ViewProviderFemConstraintSpring.setEdit()](../../d5/d4f/classFemGui_1_1ViewProviderFemConstraintSpring.html#a7707003f9949bc205321d51c3fa2307b),
[FemGui::ViewProviderFemConstraintTemperature.setEdit()](../../d1/df6/classFemGui_1_1ViewProviderFemConstraintTemperature.html#aeda5483ccbf96c4fe6eb2ca7a9613d67),
[FemGui::ViewProviderFemConstraintTransform.setEdit()](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#aa18e9edaaaca3d70ecaa70c7324d9cb8),
[FemGui::ViewProviderFemMeshShapeNetgen.setEdit()](../../df/db3/classFemGui_1_1ViewProviderFemMeshShapeNetgen.html#aadc0d17d1ae76eb0a0ea3e5aca6cd5bd),
[FemGui::ViewProviderFemPostFunction.setEdit()](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#a6b9d37dcfe0a7353636f93a552e26e31),
[FemGui::ViewProviderFemPostObject.setEdit()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a0061e5e27869609b71c4ea0c5af8b619),
[FemGui::ViewProviderSetElements.setEdit()](../../dd/d62/classFemGui_1_1ViewProviderSetElements.html#a73a081f3347b902c5dab471685962630),
[FemGui::ViewProviderSetFaces.setEdit()](../../d9/d46/classFemGui_1_1ViewProviderSetFaces.html#ad00b9493187b0c5a672120f53335c253),
[FemGui::ViewProviderSetGeometry.setEdit()](../../dd/d48/classFemGui_1_1ViewProviderSetGeometry.html#a273f5ea4cda8beaca861257a9cabb556),
[FemGui::ViewProviderSetNodes.setEdit()](../../d5/d44/classFemGui_1_1ViewProviderSetNodes.html#afa5974e28b2cc9cf53c07adad3170aae),
[MeshGui::ViewProviderMesh.setEdit()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a40deb657f9bdff42591951bab87920d0),
[PartGui::ViewProvider2DObjectGrid.setEdit()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a9fa0acb41e43ce0dd79d58330cd10ffe),
[PartGui::ViewProviderCurveNet.setEdit()](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#aff7108f2d0ef7759484b9446b252b917),
[PartGui::ViewProviderImport.setEdit()](../../d0/d76/classPartGui_1_1ViewProviderImport.html#a3f7d8b2fd75fb4f36bdbb7d4ce14b26c),
[PartGui::ViewProviderMirror.setEdit()](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a1f2db7361989a26090e6071227f1562a),
[PartGui::ViewProviderFillet.setEdit()](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#ac9dbcc3535eb12550c5825593f533e25),
[PartGui::ViewProviderChamfer.setEdit()](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a955c6e923d41c98de7aed8ee8ea8b2ba),
[PartGui::ViewProviderOffset.setEdit()](../../df/ded/classPartGui_1_1ViewProviderOffset.html#aba844b2a4f4129a7ed239641d7978851),
[PartGui::ViewProviderThickness.setEdit()](../../d1/d8f/classPartGui_1_1ViewProviderThickness.html#a6cabec4fc1ea58cd5ba6a66f8b279fc6),
[PartGui::ViewProviderPrimitive.setEdit()](../../dd/dfd/classPartGui_1_1ViewProviderPrimitive.html#a830586f4badf80a1ec8e9e2d02f280d5),
[PartDesignGui::ViewProviderBase.setEdit()](../../d7/d54/classPartDesignGui_1_1ViewProviderBase.html#a4609b7dfe7e5fdc6ae721a101bccfd4e),
[PartDesignGui::ViewProviderDressUp.setEdit()](../../dd/dfd/classPartDesignGui_1_1ViewProviderDressUp.html#a4119fd1599c9378ba7b4e9185637c51c),
[PartDesignGui::ViewProviderHelix.setEdit()](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#a2fe0852e9a26cb1e399ac84be8251d9c),
[PartDesignGui::ViewProviderHole.setEdit()](../../df/dda/classPartDesignGui_1_1ViewProviderHole.html#aa1c50b1c4e8d2446e8f91b3d79c2d9b4),
[PartDesignGui::ViewProviderLoft.setEdit()](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#ae908f2000b0bed946505fd8d96a20236),
[PartDesignGui::ViewProviderPipe.setEdit()](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#acc714758bdf79639a8a30c99e1e8e21b),
[PartDesignGui::ViewProviderPrimitive.setEdit()](../../d9/d7a/classPartDesignGui_1_1ViewProviderPrimitive.html#a830586f4badf80a1ec8e9e2d02f280d5),
[PathGui::ViewProviderPathCompound.setEdit()](../../db/d9a/classPathGui_1_1ViewProviderPathCompound.html#a98bbbb533d93a02c594c80f10ce780db),
[PointsGui::ViewProviderPoints.setEdit()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a0b86e870101c6db6e59da6632b15da1a),
[RaytracingGui::ViewProviderLux.setEdit()](../../d4/d95/classRaytracingGui_1_1ViewProviderLux.html#a559d010dd9902addb4de84170aac9f51),
[RaytracingGui::ViewProviderPovray.setEdit()](../../d4/d94/classRaytracingGui_1_1ViewProviderPovray.html#a76685922c30f4f6a92a74fafcc800fa2),
[RobotGui::ViewProviderEdge2TracObject.setEdit()](../../da/d5e/classRobotGui_1_1ViewProviderEdge2TracObject.html#af62127f819ab7dd2f1cb94e041f04381),
[RobotGui::ViewProviderTrajectoryCompound.setEdit()](../../d7/d47/classRobotGui_1_1ViewProviderTrajectoryCompound.html#aef2ee5ba2388c7dd85aef72656a6c297),
[RobotGui::ViewProviderTrajectoryDressUp.setEdit()](../../da/dff/classRobotGui_1_1ViewProviderTrajectoryDressUp.html#aba54ff221e761e23bd2c887b39fd876e),
[SurfaceGui::ViewProviderFilling.setEdit()](../../d0/dac/classSurfaceGui_1_1ViewProviderFilling.html#a5f6e7210301bf80e264d2209c92e67d4),
[SurfaceGui::ViewProviderGeomFillSurface.setEdit()](../../d8/d03/classSurfaceGui_1_1ViewProviderGeomFillSurface.html#ae59f5b76efea8f8d54f7eb93fb42b7b6),
[SurfaceGui::ViewProviderSections.setEdit()](../../da/dd0/classSurfaceGui_1_1ViewProviderSections.html#a2c85256da171bcbd0547974f29ead549),
[TechDrawGui::ViewProviderBalloon.setEdit()](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a2e025ddacfaa37230ff483b91d273338),
[TechDrawGui::ViewProviderDimension.setEdit()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#ad0f391bd413a036384a01912569d5bc4),
[TechDrawGui::ViewProviderLeader.setEdit()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9e6409e4b7a5516b47b05ed3945fca40),
[TechDrawGui::ViewProviderProjGroup.setEdit()](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#ac5dcab3a423587bd0dc448c46a7b6d35),
[TechDrawGui::ViewProviderProjGroupItem.setEdit()](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#a765bef926a390295b2440caf41c7001e),
[TechDrawGui::ViewProviderRichAnno.setEdit()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#abe7e29edccb3b64c78291d246c9d22b1),
[TechDrawGui::ViewProviderViewPart.setEdit()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a758558e7e660c02f277bc621cb7e2e61),
[TechDrawGui::ViewProviderViewSection.setEdit()](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a38606dd2e773bcb04de0fa4be2c4c0b7),
[TechDrawGui::ViewProviderWeld.setEdit()](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#ad9430bcd1a82544e7d00ed2b2ebeffdc),
[Gui::ViewProviderDragger.setEdit()](../../d3/d04/classGui_1_1ViewProviderDragger.html#ae112bfbf937f2ec8a8efd24fd432acc5),
[Gui::ViewProviderLink.setEdit()](../../d6/d59/classGui_1_1ViewProviderLink.html#a72f3abcc67100d8740725e3344df323d),
[Gui::ViewProviderPythonFeatureT< ViewProviderT
>.setEdit()](../../dc/d41/classGui_1_1ViewProviderPythonFeatureT.html#ac76e613b31b405cd78dc8191390430a7),
[PartGui::ViewProviderPartExt.setEdit()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a1181d53d0a1c61ea05d59905c4b4e0cd),
[PartDesignGui::ViewProvider.setEdit()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a6f3f1f8893820843dd51f280ca8a3dec),
[PartDesignGui::ViewProviderBoolean.setEdit()](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#a8332deec17f6d74c084a3b935c9aa6a0),
[PartDesignGui::ViewProviderDatum.setEdit()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#ac56d3ca4da8d5573b3496ee332304919),
[PartDesignGui::ViewProviderShapeBinder.setEdit()](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#a8ab60c5d127611b0a984fedcc5d286a9),
[PartDesignGui::ViewProviderSubShapeBinder.setEdit()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#ab69265d464691c650bb6bd89015af92e),
[PartDesignGui::ViewProviderTransformed.setEdit()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a5d37e6ba0bf8efbd6ebea83c4c331bb2),
[SketcherGui::ViewProviderSketch.setEdit()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ad28c651e806a00fca15332d4c04b47c9),
[SpreadsheetGui::ViewProviderSheet.setEdit()](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a2bc7d2572d6e443dd7e60728404aa8bb),
[TechDrawGui::ViewProviderGeomHatch.setEdit()](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a28afe467eff5280ce4f2f4c06c334403),
[TechDrawGui::ViewProviderHatch.setEdit()](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a9e2a641e6843356f975b70dc8327411d),
[TechDrawGui::ViewProviderPage.setEdit()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#aa4d620f567a62273aff719609d2e0590),
[MeshGui::ViewProviderMeshNode.setEdit()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a17780fa2e133a40608c422364b034e25),
[Gui::ViewProviderOriginFeature.setEdit()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a454f195000fee3cbed596d1b4c20fa49),
[ArchIFCView.IfcContextView.setEdit()](../../d6/d1b/classArchIFCView_1_1IfcContextView.html#a2a1bf7071dce4cc8111c33e18b44e2b5),
[BasicShapes.ViewProviderShapes.ViewProviderTube.setEdit()](../../dc/dad/classBasicShapes_1_1ViewProviderShapes_1_1ViewProviderTube.html#a7457e7db7f6d3b56f283f0f8da2fdca3),
[ArchComponent.ViewProviderComponent.setEdit()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#aead5dc101b4fb331c6905a022017846d),
ArchMaterial._ViewProviderArchMaterial.setEdit(),
[ArchPanel.ViewProviderPanelSheet.setEdit()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#ae867e3595c276c8e66b8650c8d1a9344),
ArchPrecast._ViewProviderPrecast.setEdit(),
[ArchProfile.ViewProviderProfile.setEdit()](../../d9/d44/classArchProfile_1_1ViewProviderProfile.html#ad360a2e390790ea06a318de4fdc22ef3),
ArchRebar._ViewProviderRebar.setEdit(),
ArchSectionPlane._ViewProviderSectionPlane.setEdit(),
ArchSite._ViewProviderSite.setEdit(), ArchSpace._ViewProviderSpace.setEdit(),
ArchStructure._ViewProviderStructure.setEdit(),
ArchWindow._ViewProviderWindow.setEdit(),
[draftviewproviders.view_facebinder.ViewProviderFacebinder.setEdit()](../../d0/dc8/classdraftviewproviders_1_1view__facebinder_1_1ViewProviderFacebinder.html#a7c996c94c74aedd3c98563354f6264e4),
[draftviewproviders.view_hatch.ViewProviderDraftHatch.setEdit()](../../dd/d75/classdraftviewproviders_1_1view__hatch_1_1ViewProviderDraftHatch.html#afcc040238c3aec08065582ff70b362fc),
[draftviewproviders.view_shapestring.ViewProviderShapeString.setEdit()](../../df/d92/classdraftviewproviders_1_1view__shapestring_1_1ViewProviderShapeString.html#a2fda6b0878fe67d58129295d8841ddda),
[draftviewproviders.view_text.ViewProviderText.setEdit()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#a63ed7d1ab46f5edf47c6c5ac145f855c),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh.setEdit()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#a3a78092889a4c95eccb6be557e1ae0dc),
JoinFeatures._ViewProviderPartJoinFeature.setEdit(),
Mod.PartDesign.InvoluteGearFeature._ViewProviderInvoluteGear.setEdit(),
[Mod.PartDesign.SprocketFeature.ViewProviderSprocket.setEdit()](../../da/d59/classMod_1_1PartDesign_1_1SprocketFeature_1_1ViewProviderSprocket.html#aa6d4cdd2dac11b7da5f1e3332a28c1fc),
PathScripts.PathFixture._ViewProviderFixture.setEdit(),
PathScripts.PathPlane._ViewProviderPlane.setEdit(),
ArchAxis._ViewProviderAxis.setEdit(),
ArchAxisSystem._ViewProviderAxisSystem.setEdit(),
[ArchGrid.ViewProviderArchGrid.setEdit()](../../d4/dbf/classArchGrid_1_1ViewProviderArchGrid.html#ab678ebc5a0472704be09f9341557d24b),
ArchMaterial._ViewProviderArchMultiMaterial.setEdit(),
[ArchReference.ViewProviderArchReference.setEdit()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#ab3b586040db301e1fb7a1239c52c8c33),
ArchRoof._ViewProviderRoof.setEdit(),
ArchSchedule._ViewProviderArchSchedule.setEdit(),
[draftviewproviders.view_base.ViewProviderDraft.setEdit()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#adebff004d86674246b09cb8adf7eb658),
[draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation.setEdit()](../../d2/d24/classdraftviewproviders_1_1view__draft__annotation_1_1ViewProviderDraftAnnotation.html#a12b97cb07c5c6fa60db0766c7d26747c),
[femsolver.elmer.equations.equation.ViewProxy.setEdit()](../../d7/d0b/classfemsolver_1_1elmer_1_1equations_1_1equation_1_1ViewProxy.html#a4a9253701e25ea047f2dcc2796a2791e),
[femsolver.solverbase.ViewProxy.setEdit()](../../d5/d90/classfemsolver_1_1solverbase_1_1ViewProxy.html#a4429c7e7877778c7637b8b5a7796e77e),
[femviewprovider.view_constraint_centrif.VPConstraintCentrif.setEdit()](../../d7/db7/classfemviewprovider_1_1view__constraint__centrif_1_1VPConstraintCentrif.html#a20087c7960f39832194fdc1868bf6c81),
[femviewprovider.view_constraint_electrostaticpotential.VPConstraintElectroStaticPotential.setEdit()](../../df/d9f/classfemviewprovider_1_1view__constraint__electrostaticpotential_1_1VPConstraintElectroStaticPotential.html#aad0fe720edc89b21902dd6b5877782cc),
[femviewprovider.view_constraint_flowvelocity.VPConstraintFlowVelocity.setEdit()](../../d0/dfd/classfemviewprovider_1_1view__constraint__flowvelocity_1_1VPConstraintFlowVelocity.html#afc835a8865f553d189da7eeab7939795),
[femviewprovider.view_constraint_initialflowvelocity.VPConstraintInitialFlowVelocity.setEdit()](../../d2/df6/classfemviewprovider_1_1view__constraint__initialflowvelocity_1_1VPConstraintInitialFlowVelocity.html#ade9c7ed74a22baf7020e03f6b8050886),
[femviewprovider.view_constraint_sectionprint.VPConstraintSectionPrint.setEdit()](../../d9/df8/classfemviewprovider_1_1view__constraint__sectionprint_1_1VPConstraintSectionPrint.html#a1ac91f5fefcccae1996db79675a90c39),
[femviewprovider.view_constraint_tie.VPConstraintTie.setEdit()](../../da/dc2/classfemviewprovider_1_1view__constraint__tie_1_1VPConstraintTie.html#adde736c91057702d5981d6381226bd34),
[femviewprovider.view_element_fluid1D.VPElementFluid1D.setEdit()](../../dc/d82/classfemviewprovider_1_1view__element__fluid1D_1_1VPElementFluid1D.html#a0711f4bfff228363d1d3c8428960ba9a),
[femviewprovider.view_element_geometry1D.VPElementGeometry1D.setEdit()](../../d6/d15/classfemviewprovider_1_1view__element__geometry1D_1_1VPElementGeometry1D.html#aae5a773aea5bf0a8bdb647711a76f7dc),
[femviewprovider.view_element_geometry2D.VPElementGeometry2D.setEdit()](../../df/d9f/classfemviewprovider_1_1view__element__geometry2D_1_1VPElementGeometry2D.html#a271170b859369f4a9788d69269e99b37),
[femviewprovider.view_material_common.VPMaterialCommon.setEdit()](../../d8/df6/classfemviewprovider_1_1view__material__common_1_1VPMaterialCommon.html#accca7b13d2fc5041a8f15b3b65c0b251),
[femviewprovider.view_material_reinforced.VPMaterialReinforced.setEdit()](../../dc/dfe/classfemviewprovider_1_1view__material__reinforced_1_1VPMaterialReinforced.html#a8399acabdb132c409f577c7199872d31),
[femviewprovider.view_mesh_boundarylayer.VPMeshBoundaryLayer.setEdit()](../../d4/d3e/classfemviewprovider_1_1view__mesh__boundarylayer_1_1VPMeshBoundaryLayer.html#a04cb227fa3a229daf50d89abf72cc0d9),
[femviewprovider.view_mesh_group.VPMeshGroup.setEdit()](../../d3/da6/classfemviewprovider_1_1view__mesh__group_1_1VPMeshGroup.html#aaddad7df7e2d25ba841407b1fadfd1f9),
[femviewprovider.view_mesh_region.VPMeshRegion.setEdit()](../../de/d04/classfemviewprovider_1_1view__mesh__region_1_1VPMeshRegion.html#a0c89eee155f784460a4ea507f5856661),
[femviewprovider.view_result_mechanical.VPResultMechanical.setEdit()](../../d7/d8f/classfemviewprovider_1_1view__result__mechanical_1_1VPResultMechanical.html#ab6743e8383333e6ac2be4cd000fd163e),
[femviewprovider.view_solver_ccxtools.VPSolverCcxTools.setEdit()](../../d6/dbd/classfemviewprovider_1_1view__solver__ccxtools_1_1VPSolverCcxTools.html#ac261c8c943ed0b2fbb6a5c80b5618f6f),
PathScripts.PathCollision._ViewProviderCollisionSim.setEdit(),
[PathScripts.PathDressupAxisMap.ViewProviderDressup.setEdit()](../../d7/d13/classPathScripts_1_1PathDressupAxisMap_1_1ViewProviderDressup.html#a1ee170d7f1e361a6cc907b06dd0a488e),
[PathScripts.PathDressupDogbone.ViewProviderDressup.setEdit()](../../df/ddb/classPathScripts_1_1PathDressupDogbone_1_1ViewProviderDressup.html#a0e3d84853f71a45bec3815eb681bf96d),
[PathScripts.PathDressupDragknife.ViewProviderDressup.setEdit()](../../dc/d40/classPathScripts_1_1PathDressupDragknife_1_1ViewProviderDressup.html#a1f4de29a6182039f63a6726947b81096),
[PathScripts.PathDressupLeadInOut.ViewProviderDressup.setEdit()](../../d7/d49/classPathScripts_1_1PathDressupLeadInOut_1_1ViewProviderDressup.html#a53407544b547936e778368473e00180b),
[PathScripts.PathDressupPathBoundaryGui.DressupPathBoundaryViewProvider.setEdit()](../../dc/d69/classPathScripts_1_1PathDressupPathBoundaryGui_1_1DressupPathBoundaryViewProvider.html#a389415d8c78b63bd3bdaf4f19ef22394),
[PathScripts.PathDressupTagGui.PathDressupTagViewProvider.setEdit()](../../dc/d08/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagViewProvider.html#a4277f9c839850cb2f901282f0744a30d),
[PathScripts.PathDressupZCorrect.ViewProviderDressup.setEdit()](../../d1/df1/classPathScripts_1_1PathDressupZCorrect_1_1ViewProviderDressup.html#a64e64b6a43b15ca1e1f48f7b0b06d676),
[PathScripts.PathPropertyBagGui.ViewProvider.setEdit()](../../d5/d77/classPathScripts_1_1PathPropertyBagGui_1_1ViewProvider.html#a81213ee3113bc104538b92aecaace365),
[PathScripts.PathSetupSheetGui.ViewProvider.setEdit()](../../dc/dc3/classPathScripts_1_1PathSetupSheetGui_1_1ViewProvider.html#ad02129a6f0221a546f4000ee40a2d285),
[PathScripts.PathToolBitGui.ViewProvider.setEdit()](../../d0/d90/classPathScripts_1_1PathToolBitGui_1_1ViewProvider.html#acea324d87111bfc0b8bed576c2113325),
[Spreadsheet_legacy.ViewProviderSpreadsheet.setEdit()](../../d6/d84/classSpreadsheet__legacy_1_1ViewProviderSpreadsheet.html#a519d7387029bfa6c1876e3eb98e9242a),
[femviewprovider.view_base_femobject.VPBaseFemObject.setEdit()](../../d0/d48/classfemviewprovider_1_1view__base__femobject_1_1VPBaseFemObject.html#a8f78148451493225a5489334501d7102),
[PathScripts.PathIconViewProvider.ViewProvider.setEdit()](../../d6/d55/classPathScripts_1_1PathIconViewProvider_1_1ViewProvider.html#a06b679993b4a60773b28433c830e5cf7),
[PathScripts.PathJobGui.ViewProvider.setEdit()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#a05289ef2f32b3f020037d070e153ab09),
[PathScripts.PathOpGui.ViewProvider.setEdit()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#ace25f1c736f4ee55ea809f27c3e2a4f3),
[PathScripts.PathToolControllerGui.ViewProvider.setEdit()](../../db/db5/classPathScripts_1_1PathToolControllerGui_1_1ViewProvider.html#a073d3bfd1223e6d35f9ff81d5cf9a12e),
and
[Mod.PartDesign.FeatureHole.ViewProviderHole.ViewProviderHole.setEdit()](../../de/d6b/classMod_1_1PartDesign_1_1FeatureHole_1_1ViewProviderHole_1_1ViewProviderHole.html#a001a7075862d0154388b155206c8f1cc).

## ◆ getIcon()

def ArchGrid.ViewProviderArchGrid.getIcon  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ArchAxisSystem.AxisSystemTaskPanel.update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchComponent.ComponentTaskPanel.update()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#af95b36032a3837b4bf1b92fe7c6a47e0),
and
[ArchSectionPlane.SectionPlaneTaskPanel.update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162).

## ◆ setEdit()

def ArchGrid.ViewProviderArchGrid.setEdit  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_ ,   
|  |  | _mode_ = `0`  
| ) | |   
  
Referenced by
[ArchGrid.ViewProviderArchGrid.doubleClicked()](../../d4/dbf/classArchGrid_1_1ViewProviderArchGrid.html#a35948c50ff2dccdada47d584d8bf32bd),
[ArchReference.ViewProviderArchReference.doubleClicked()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#a921a71a757c5853c3331216eefb23703),
[draftviewproviders.view_dimension.ViewProviderDimensionBase.doubleClicked()](../../d6/d45/classdraftviewproviders_1_1view__dimension_1_1ViewProviderDimensionBase.html#a164ae40613358c396be3f6b9fae3937d),
[draftviewproviders.view_hatch.ViewProviderDraftHatch.doubleClicked()](../../dd/d75/classdraftviewproviders_1_1view__hatch_1_1ViewProviderDraftHatch.html#a9274ff72268d6c1a4337118b5db8bcc4),
[draftviewproviders.view_text.ViewProviderText.doubleClicked()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#adc22c64d135df407787ca53f9029c3a0),
[PathScripts.PathPropertyBagGui.ViewProvider.doubleClicked()](../../d5/d77/classPathScripts_1_1PathPropertyBagGui_1_1ViewProvider.html#a915f858e0483981f8124bdf4df7e02d4),
[PathScripts.PathSetupSheetGui.ViewProvider.doubleClicked()](../../dc/dc3/classPathScripts_1_1PathSetupSheetGui_1_1ViewProvider.html#a9b1b82571f01e8e740eadabfec88b9f3),
[PathScripts.PathToolBitGui.ViewProvider.doubleClicked()](../../d0/d90/classPathScripts_1_1PathToolBitGui_1_1ViewProvider.html#a7265835d9e6286fa1e48f47a0f2b82f0),
[Spreadsheet_legacy.ViewProviderSpreadsheet.doubleClicked()](../../d6/d84/classSpreadsheet__legacy_1_1ViewProviderSpreadsheet.html#aa89fcb2be2b67b2f1d210bd06ea9e55a),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[PathScripts.PathIconViewProvider.ViewProvider.setupContextMenu()](../../d6/d55/classPathScripts_1_1PathIconViewProvider_1_1ViewProvider.html#a9a8ca3029fe2523b0d7736c1d4e611a7),
[PathScripts.PathJobGui.ViewProvider.setupContextMenu()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#ab8dd16390af82dadddf816c3a85cae0b),
[PathScripts.PathOpGui.ViewProvider.setupContextMenu()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a79f8f54d1d96c0a29b00b0775e5231ac),
and
[PathScripts.PathToolControllerGui.ViewProvider.setupContextMenu()](../../db/db5/classPathScripts_1_1PathToolControllerGui_1_1ViewProvider.html#a2f21a1b07712507aedc89ac30d8379c5).

## ◆ unsetEdit()

def ArchGrid.ViewProviderArchGrid.unsetEdit  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _vobj_ ,   
|  |  | _mode_  
| ) | |   
  
Referenced by
[PathScripts.PathJobGui.ViewProvider.uneditObject()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#aa663c276d96715669b3d07c7d2e34790).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchGrid.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

