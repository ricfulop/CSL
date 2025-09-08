---
url: https://freecad.github.io/SourceDoc/d9/d86/classArchPanel_1_1CommandPanel.html
scraped_at: 2025-09-08T14:58:02.338806
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchPanel](../../df/d76/namespaceArchPanel.html)
  * [CommandPanel](../../d9/d86/classArchPanel_1_1CommandPanel.html)

[List of all members](../../db/d09/classArchPanel_1_1CommandPanel-members.html) | Public Member Functions | Public Attributes

ArchPanel.CommandPanel Class Reference

##  Public Member Functions  
  
---  
def | [Activated](../../d9/d86/classArchPanel_1_1CommandPanel.html#a489359816e223a62507b109c2ddfef49) (self)  
def | [getPoint](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb) (self, point=None, obj=None)  
def | [GetResources](../../d9/d86/classArchPanel_1_1CommandPanel.html#ac67a7d85081050a063db28d13ac60cc5) (self)  
def | [IsActive](../../d9/d86/classArchPanel_1_1CommandPanel.html#afb435e2ed1c5f4132263a87338adce52) (self)  
def | [rotate](../../d9/d86/classArchPanel_1_1CommandPanel.html#ac8b0e4434f74c6e0a73e6b6a96ddb6b2) (self)  
def | [setContinue](../../d9/d86/classArchPanel_1_1CommandPanel.html#ae1212a57c8cea24a45f4c997d1c9e2e0) (self, i)  
def | [setLength](../../d9/d86/classArchPanel_1_1CommandPanel.html#a324c9bdbfec0dd8eacfb7d0cea302998) (self, d)  
def | [setPreset](../../d9/d86/classArchPanel_1_1CommandPanel.html#a8ee939633a1994367e81aaac4b9d1103) (self, i)  
def | [setThickness](../../d9/d86/classArchPanel_1_1CommandPanel.html#abe9208c3896b3024492b1ca2219786af) (self, d)  
def | [setWidth](../../d9/d86/classArchPanel_1_1CommandPanel.html#a32bea4e80ff9a4e8e91d89aead1d88e1) (self, d)  
def | [taskbox](../../d9/d86/classArchPanel_1_1CommandPanel.html#ae4ce0bc3a3306d76a850793f87b65d08) (self)  
def | [update](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c) (self, point, info)  
  
##  Public Attributes  
  
---  
|
[continueCmd](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad5408329191a0536d3f4d76f63a69367)  
|
[Length](../../d9/d86/classArchPanel_1_1CommandPanel.html#a216ea090679f3a79793493e52d677d69)  
|
[points](../../d9/d86/classArchPanel_1_1CommandPanel.html#a84150c5b41f0eac464b49d1c5d914333)  
|
[Profile](../../d9/d86/classArchPanel_1_1CommandPanel.html#ae6853ed51f834120710e01c60464f3f3)  
|
[rotated](../../d9/d86/classArchPanel_1_1CommandPanel.html#af080a575474187ffa84a13ab0b6ba40b)  
|
[Thickness](../../d9/d86/classArchPanel_1_1CommandPanel.html#a59c0667e69a9d522c52b897f96c3c7cc)  
|
[tracker](../../d9/d86/classArchPanel_1_1CommandPanel.html#a1e7eeca96127526224adc5fc23f2ca32)  
|
[vHeight](../../d9/d86/classArchPanel_1_1CommandPanel.html#a17d6ea726931a857118bfd35da626d05)  
|
[vLength](../../d9/d86/classArchPanel_1_1CommandPanel.html#adf6f59233ebb9efe0c2e230aaeef8959)  
|
[vWidth](../../d9/d86/classArchPanel_1_1CommandPanel.html#a20a9b66ad7e1c3bd2c571088695d12d2)  
|
[Width](../../d9/d86/classArchPanel_1_1CommandPanel.html#a3f3b80fcbef81f11aedf8b5f96568c65)  
  
## Member Function Documentation

## ◆ Activated()

def ArchPanel.CommandPanel.Activated  | ( |  | _self_| ) |   
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

def ArchPanel.CommandPanel.getPoint  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _point_ = `None`,   
|  |  | _obj_ = `None`  
| ) | |   
  
References
[AddonManager.CommandAddonManager.Activated()](../../d3/d48/classAddonManager_1_1CommandAddonManager.html#ad7c611053497eaa621def6c5d923a159),
ArchAxis._CommandAxis.Activated(),
ArchAxisSystem._CommandAxisSystem.Activated(),
ArchBuilding._CommandBuilding.Activated(),
[ArchBuildingPart.CommandBuildingPart.Activated()](../../d0/deb/classArchBuildingPart_1_1CommandBuildingPart.html#a163dcfbefdfee093e1d9f90374915737),
ArchCommands._CommandAdd.Activated(), ArchCommands._CommandRemove.Activated(),
ArchCommands._CommandSplitMesh.Activated(),
ArchCommands._CommandMeshToShape.Activated(),
ArchCommands._CommandSelectNonSolidMeshes.Activated(),
ArchCommands._CommandRemoveShape.Activated(),
ArchCommands._CommandCloseHoles.Activated(),
ArchCommands._CommandCheck.Activated(),
ArchCommands._CommandSurvey.Activated(),
ArchCommands._ToggleIfcBrepFlag.Activated(),
ArchCommands._CommandComponent.Activated(),
ArchCommands._CommandCloneComponent.Activated(),
ArchCommands._CommandIfcSpreadsheet.Activated(),
ArchCommands._ToggleSubs.Activated(),
[ArchCurtainWall.CommandArchCurtainWall.Activated()](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#af52cfef9ec45b213d701a86b937538b7),
ArchCutPlane._CommandCutLine.Activated(),
ArchCutPlane._CommandCutPlane.Activated(),
ArchEquipment._CommandEquipment.Activated(),
ArchEquipment._Command3Views.Activated(), ArchFence._CommandFence.Activated(),
ArchFloor._CommandFloor.Activated(), ArchFrame._CommandFrame.Activated(),
[ArchGrid.CommandArchGrid.Activated()](../../d9/d92/classArchGrid_1_1CommandArchGrid.html#a1ee587841c72b6fd35cd2fb13d43c160),
ArchMaterial._CommandArchMaterial.Activated(),
ArchMaterial._CommandArchMultiMaterial.Activated(),
[ArchPanel.CommandPanel.Activated()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a489359816e223a62507b109c2ddfef49),
[ArchPanel.CommandPanelCut.Activated()](../../de/d5b/classArchPanel_1_1CommandPanelCut.html#ac4780d11fcb1bf5690ab0b798e400183),
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchPanel.CommandNest.Activated()](../../d6/d6a/classArchPanel_1_1CommandNest.html#a5f2cfbdd4e046fc27d20bfbaab89a802),
ArchPipe._CommandPipe.Activated(), ArchPipe._CommandPipeConnector.Activated(),
[ArchProfile.Arch_Profile.Activated()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a763cf4009bc9139fb9ee7cf65d0cc65b),
ArchProject._CommandProject.Activated(), ArchRebar._CommandRebar.Activated(),
[ArchReference.ArchReferenceCommand.Activated()](../../dd/d7c/classArchReference_1_1ArchReferenceCommand.html#a973e4fbb1b1be2dc21d47c8eb0c8b99b),
ArchRoof._CommandRoof.Activated(),
[ArchSchedule.CommandArchSchedule.Activated()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#ac9ba099f901d2a97b798b389405cf81c),
ArchSectionPlane._CommandSectionPlane.Activated(),
ArchSite._CommandSite.Activated(), ArchSpace._CommandSpace.Activated(),
ArchStairs._CommandStairs.Activated(),
[ArchStructure.CommandStructuresFromSelection.Activated()](../../da/da1/classArchStructure_1_1CommandStructuresFromSelection.html#a075ce79ddeb48b71812bd6155d09c3b9),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
ArchStructure._CommandStructure.Activated(),
[ArchTruss.CommandArchTruss.Activated()](../../dc/d2c/classArchTruss_1_1CommandArchTruss.html#a1bd416fad9dfbaa35af6e3f8f40ee82f),
ArchWall._CommandWall.Activated(), ArchWall._CommandMergeWalls.Activated(),
ArchWindow._CommandWindow.Activated(),
[InitGui.ArchWorkbench.Activated()](../../db/de0/classInitGui_1_1ArchWorkbench.html#aad53f18d617a92e8c723e5accc43b36b),
[DraftGui.DraftToolBar.Activated()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a7a471622fb24e092cd091bf7ed8a53ef),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.Activated()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#ac7fe745faef8d402397cb0641e130965),
[draftguitools.gui_arcs.Arc.Activated()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#ab7c70926ad95129a06d6aa52bcc34309),
[draftguitools.gui_arcs.Arc_3Points.Activated()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#a3564866de73264ea697ba0296c117194),
[draftguitools.gui_array_simple.LinkArray.Activated()](../../d3/df7/classdraftguitools_1_1gui__array__simple_1_1LinkArray.html#af2fa710543a021dc67979dfdca132cd7),
[draftguitools.gui_base.GuiCommandSimplest.Activated()](../../d3/dbd/classdraftguitools_1_1gui__base_1_1GuiCommandSimplest.html#af9fb0fc3e536a8a068732630ea5634db),
[draftguitools.gui_beziers.BezCurve.Activated()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#a784e5b3d22300d802916024986f3f8ba),
[draftguitools.gui_beziers.CubicBezCurve.Activated()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#a982a5341986fbd004390ea8902c0ba3d),
[draftguitools.gui_circulararray.CircularArray.Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
[draftguitools.gui_clone.Clone.Activated()](../../df/d67/classdraftguitools_1_1gui__clone_1_1Clone.html#addc877a683b0c3c3861ff0793a3d973b),
[draftguitools.gui_dimension_ops.FlipDimension.Activated()](../../de/d3e/classdraftguitools_1_1gui__dimension__ops_1_1FlipDimension.html#a43a2515fe4a13602f4cd9a705c04c8d2),
[draftguitools.gui_dimensions.Dimension.Activated()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a2ee3353c649d7f6817f3aa2a056d3eaf),
[draftguitools.gui_downgrade.Downgrade.Activated()](../../de/d8b/classdraftguitools_1_1gui__downgrade_1_1Downgrade.html#a724c3827c15d821dde302e9bdf2fba25),
[draftguitools.gui_draft2sketch.Draft2Sketch.Activated()](../../dd/d7c/classdraftguitools_1_1gui__draft2sketch_1_1Draft2Sketch.html#a5c70d486873c26b45a12bd6adf296b1a),
[draftguitools.gui_drawing.Drawing.Activated()](../../db/d99/classdraftguitools_1_1gui__drawing_1_1Drawing.html#a9f9b818240f16e3577e35b398477b188),
[draftguitools.gui_edit.Edit.Activated()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#a9abe09a3ee3186ff88f606678ddc2ad6),
[draftguitools.gui_ellipses.Ellipse.Activated()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#aa9bbf52c8fbe9080ab25f4db93d0a8db),
[draftguitools.gui_facebinders.Facebinder.Activated()](../../da/dc9/classdraftguitools_1_1gui__facebinders_1_1Facebinder.html#a40b08b9d18731931aac3f121c9c140b8),
[draftguitools.gui_grid.ToggleGrid.Activated()](../../dd/d85/classdraftguitools_1_1gui__grid_1_1ToggleGrid.html#a05ab6984bfd486fb20704f21b610057b),
[draftguitools.gui_groups.AddToGroup.Activated()](../../d8/d83/classdraftguitools_1_1gui__groups_1_1AddToGroup.html#acedfb64f091e94d868e03f8f4400725c),
[draftguitools.gui_groups.SelectGroup.Activated()](../../d2/d7d/classdraftguitools_1_1gui__groups_1_1SelectGroup.html#a02cc68a19d36015c7dac630655c00a7f),
[draftguitools.gui_groups.SetAutoGroup.Activated()](../../d4/df8/classdraftguitools_1_1gui__groups_1_1SetAutoGroup.html#a355430439627471615875b686e22984e),
[draftguitools.gui_groups.AddToConstruction.Activated()](../../d3/d06/classdraftguitools_1_1gui__groups_1_1AddToConstruction.html#a36c267c4685ebb061b39cea882049759),
[draftguitools.gui_groups.AddNamedGroup.Activated()](../../db/d7d/classdraftguitools_1_1gui__groups_1_1AddNamedGroup.html#a11d636879ed4a6192180f6c64cab5908),
[draftguitools.gui_hatch.Draft_Hatch.Activated()](../../df/d17/classdraftguitools_1_1gui__hatch_1_1Draft__Hatch.html#a44fd00d75a84d16d5dcb95db40a99180),
[draftguitools.gui_heal.Heal.Activated()](../../d5/d39/classdraftguitools_1_1gui__heal_1_1Heal.html#a229ca6fa356961bf5de5cb0bb2ff7fc7),
[draftguitools.gui_join.Join.Activated()](../../d4/d50/classdraftguitools_1_1gui__join_1_1Join.html#a232ea198987b6ed19b57255408f2e9d4),
[draftguitools.gui_labels.Label.Activated()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a830012e085da122bb5c017ee356b22fb),
[draftguitools.gui_layers.Layer.Activated()](../../d1/da7/classdraftguitools_1_1gui__layers_1_1Layer.html#ab7afc624bbc1b314ec9c6306770d1ee5),
[draftguitools.gui_line_add_delete.AddPoint.Activated()](../../d2/d9e/classdraftguitools_1_1gui__line__add__delete_1_1AddPoint.html#aa3844e5a0377dec72912181e96b00a9f),
[draftguitools.gui_line_add_delete.DelPoint.Activated()](../../df/d89/classdraftguitools_1_1gui__line__add__delete_1_1DelPoint.html#a3b67ab628a554bcfcdbc4fc005145523),
[draftguitools.gui_lines.Wire.Activated()](../../d0/d34/classdraftguitools_1_1gui__lines_1_1Wire.html#a772e79bda027d59def2a96b248105710),
[draftguitools.gui_lineslope.LineSlope.Activated()](../../d4/d0f/classdraftguitools_1_1gui__lineslope_1_1LineSlope.html#afcbbe794d6df5fb2a081453b9100f2eb),
[draftguitools.gui_mirror.Mirror.Activated()](../../d8/dbd/classdraftguitools_1_1gui__mirror_1_1Mirror.html#a2057208e0e43a43638a56f014672f9e7),
[draftguitools.gui_move.Move.Activated()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#a8a8ca9b914e02c71f4a9530b6f82f8c0),
[draftguitools.gui_offset.Offset.Activated()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#ad9524bde393370bae7beab7669a6ad39),
[draftguitools.gui_orthoarray.OrthoArray.Activated()](../../dc/d0f/classdraftguitools_1_1gui__orthoarray_1_1OrthoArray.html#a2c082714ec66ef3b1f8195c1ac964846),
[draftguitools.gui_patharray.PathLinkArray.Activated()](../../d7/d19/classdraftguitools_1_1gui__patharray_1_1PathLinkArray.html#aebdaef49429904d233d77c3afe982041),
[draftguitools.gui_pathtwistedarray.PathTwistedLinkArray.Activated()](../../da/d6c/classdraftguitools_1_1gui__pathtwistedarray_1_1PathTwistedLinkArray.html#ac0e82f8f33b6b9c19a435bf5357ff6ea),
[draftguitools.gui_planeproxy.Draft_WorkingPlaneProxy.Activated()](../../d3/d70/classdraftguitools_1_1gui__planeproxy_1_1Draft__WorkingPlaneProxy.html#aa003277d1797955e320f5e5e95f069b1),
[draftguitools.gui_pointarray.PointLinkArray.Activated()](../../d6/df6/classdraftguitools_1_1gui__pointarray_1_1PointLinkArray.html#a6c40a84f67b31e7439920a6941e7c5bb),
[draftguitools.gui_points.Point.Activated()](../../d7/dc7/classdraftguitools_1_1gui__points_1_1Point.html#a7893a48db1325a21aeddaf7e9fd6f7cc),
[draftguitools.gui_polararray.PolarArray.Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6),
[draftguitools.gui_polygons.Polygon.Activated()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#a0a265363effba04f7d57678d77ead1c5),
[draftguitools.gui_rectangles.Rectangle.Activated()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a33116d563b8e2e63b9611de7b5978f80),
[draftguitools.gui_rotate.Rotate.Activated()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a05285f7eb37a8609cf45b8a0a571b0f3),
[draftguitools.gui_scale.Scale.Activated()](../../d5/d4f/classdraftguitools_1_1gui__scale_1_1Scale.html#a4ef892d2aa173b239100693df6da2402),
[draftguitools.gui_selectplane.Draft_SelectPlane.Activated()](../../dc/d53/classdraftguitools_1_1gui__selectplane_1_1Draft__SelectPlane.html#af07f27d96c779d186517797bfe791d1c),
[draftguitools.gui_setstyle.Draft_SetStyle.Activated()](../../db/d0e/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle.html#ab32238b776f4e1eecddc62c986e1b88c),
[draftguitools.gui_shape2dview.Shape2DView.Activated()](../../d5/d96/classdraftguitools_1_1gui__shape2dview_1_1Shape2DView.html#acbdcbafc208af6c024f899c90239b79a),
[draftguitools.gui_shapestrings.ShapeString.Activated()](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#a4431a6731cbd4339eed1b96c017d6c9a),
[draftguitools.gui_snaps.Draft_Snap_Base.Activated()](../../d4/d3e/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Base.html#a677ee500ca5ed54bdc2ead61e334cfc8),
[draftguitools.gui_snaps.Draft_Snap_Lock.Activated()](../../dc/d29/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Lock.html#a3a7a9141c356e203d303fe4acd896dfe),
[draftguitools.gui_snaps.Draft_Snap_Midpoint.Activated()](../../d9/d96/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Midpoint.html#ad893e274359971171a8b558c3c3f7247),
[draftguitools.gui_snaps.Draft_Snap_Perpendicular.Activated()](../../d3/d70/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Perpendicular.html#a73814f0041971c5bbd4473d95f319ec1),
[draftguitools.gui_snaps.Draft_Snap_Grid.Activated()](../../dd/d36/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Grid.html#ab7dbbfbec3d6edba30992fd6f7984260),
[draftguitools.gui_snaps.Draft_Snap_Intersection.Activated()](../../da/d40/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Intersection.html#a6ac681462f88f3579a2642e23b27dc5a),
[draftguitools.gui_snaps.Draft_Snap_Parallel.Activated()](../../d3/d14/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Parallel.html#a502306cb1961844991b3fda1755d61c4),
[draftguitools.gui_snaps.Draft_Snap_Endpoint.Activated()](../../da/d71/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Endpoint.html#a83d645cd16fbe9b1f18b134a5acc9481),
[draftguitools.gui_snaps.Draft_Snap_Angle.Activated()](../../df/d9d/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Angle.html#a18e99ecd1098b1a0646cea62800c49a6),
[draftguitools.gui_snaps.Draft_Snap_Center.Activated()](../../d1/d1a/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Center.html#aedac71946e680ec9a0a1708fd83dd635),
[draftguitools.gui_snaps.Draft_Snap_Extension.Activated()](../../d4/d11/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Extension.html#ae5465b948ae21efe69661e4b5c7214eb),
[draftguitools.gui_snaps.Draft_Snap_Near.Activated()](../../d4/d98/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Near.html#a5d51f53be7fd5c8ec3b2e40abe023c63),
[draftguitools.gui_snaps.Draft_Snap_Ortho.Activated()](../../d7/dc3/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Ortho.html#a6c95f6e2f3debbd2128abc260a5dcec7),
[draftguitools.gui_snaps.Draft_Snap_Special.Activated()](../../d3/d0c/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Special.html#a4012ce7481263d26a108bcd74b0b358c),
[draftguitools.gui_snaps.Draft_Snap_Dimensions.Activated()](../../d9/d55/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Dimensions.html#a08d4f92b35841edc1a3592b2699d7594),
[draftguitools.gui_snaps.Draft_Snap_WorkingPlane.Activated()](../../d6/df2/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__WorkingPlane.html#aa68dee4f2fc74de3ad52bb9b60a6f057),
[draftguitools.gui_snaps.ShowSnapBar.Activated()](../../d4/d15/classdraftguitools_1_1gui__snaps_1_1ShowSnapBar.html#af900e3c203a39b79a0f14a1f387d982f),
[draftguitools.gui_splines.BSpline.Activated()](../../d1/d3f/classdraftguitools_1_1gui__splines_1_1BSpline.html#a110d145a7b4c19d7d9006c99e78f5750),
[draftguitools.gui_split.Split.Activated()](../../db/d21/classdraftguitools_1_1gui__split_1_1Split.html#a7872ad5cd9031bb89498067eaa10321c),
[draftguitools.gui_stretch.Stretch.Activated()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#a97649bce2fc3d31ba64674b8dbb0a545),
[draftguitools.gui_styles.ApplyStyle.Activated()](../../d6/d90/classdraftguitools_1_1gui__styles_1_1ApplyStyle.html#a4203bafacf18db241693dc4d3bb1885c),
[draftguitools.gui_subelements.SubelementHighlight.Activated()](../../d4/db2/classdraftguitools_1_1gui__subelements_1_1SubelementHighlight.html#a7aff5f6ec58778d38fd98ed8b82c6ecf),
[draftguitools.gui_texts.Text.Activated()](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a3b5036e41120c03e82e1cc1a1de16a1d),
[draftguitools.gui_togglemodes.ToggleConstructionMode.Activated()](../../d5/d96/classdraftguitools_1_1gui__togglemodes_1_1ToggleConstructionMode.html#a016e46cddbed67b88b8e010a7eabd5f6),
[draftguitools.gui_togglemodes.ToggleContinueMode.Activated()](../../d1/dc5/classdraftguitools_1_1gui__togglemodes_1_1ToggleContinueMode.html#a7b73daafc751a3d47bda619fdaa717f2),
[draftguitools.gui_togglemodes.ToggleDisplayMode.Activated()](../../d6/dc5/classdraftguitools_1_1gui__togglemodes_1_1ToggleDisplayMode.html#ade7a232ee6388993347a170f55ff9ada),
[draftguitools.gui_trimex.Trimex.Activated()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#ae09ff560b73aa479d0b8380691b27dc8),
[draftguitools.gui_upgrade.Upgrade.Activated()](../../d2/dd7/classdraftguitools_1_1gui__upgrade_1_1Upgrade.html#a22679466e33d9185873405db23107116),
[draftguitools.gui_wire2spline.WireToBSpline.Activated()](../../d4/dd5/classdraftguitools_1_1gui__wire2spline_1_1WireToBSpline.html#afc3604f707c18d3e48b42d06a1ad4b5c),
[InitGui.DraftWorkbench.Activated()](../../d0/d4d/classInitGui_1_1DraftWorkbench.html#a771a5c04f8dfb18f0992aa50a63814fe),
[InitGui.DrawingWorkbench.Activated()](../../db/db6/classInitGui_1_1DrawingWorkbench.html#afcd002ac6bdab8c15586ce395cc1e3f2),
femcommands.commands._Analysis.Activated(),
femcommands.commands._ClippingPlaneAdd.Activated(),
femcommands.commands._ClippingPlaneRemoveAll.Activated(),
femcommands.commands._Examples.Activated(),
femcommands.commands._MaterialEditor.Activated(),
femcommands.commands._MaterialMechanicalNonlinear.Activated(),
femcommands.commands._FEMMesh2Mesh.Activated(),
femcommands.commands._MeshClear.Activated(),
femcommands.commands._MeshDisplayInfo.Activated(),
femcommands.commands._MeshGmshFromShape.Activated(),
femcommands.commands._MeshNetgenFromShape.Activated(),
femcommands.commands._ResultShow.Activated(),
femcommands.commands._ResultsPurge.Activated(),
femcommands.commands._SolverCxxtools.Activated(),
femcommands.commands._SolverControl.Activated(),
femcommands.commands._SolverRun.Activated(),
[femcommands.manager.CommandManager.Activated()](../../d3/d0d/classfemcommands_1_1manager_1_1CommandManager.html#a59ce3a58f5207a2328a58a889fe290e9),
ImageTools._CommandImageScaling._CommandImageScaling.Activated(),
[MeshFlatteningCommand.CreateFlatMesh.Activated()](../../db/d72/classMeshFlatteningCommand_1_1CreateFlatMesh.html#a5a7c98a68ad23dd80cd9da38ac803cbc),
[MeshFlatteningCommand.CreateFlatFace.Activated()](../../d4/dbe/classMeshFlatteningCommand_1_1CreateFlatFace.html#adcc38c08e0adfbbc2ddc255d59645677),
[OpenSCADCommands.ExplodeGroup.Activated()](../../d8/da3/classOpenSCADCommands_1_1ExplodeGroup.html#a0e668a6654c67cc5ea3c051263048473),
[OpenSCADCommands.ColorCodeShape.Activated()](../../da/d46/classOpenSCADCommands_1_1ColorCodeShape.html#aabd4b478d909309f77e2759ae85fa9f5),
[OpenSCADCommands.Edgestofaces.Activated()](../../d2/da4/classOpenSCADCommands_1_1Edgestofaces.html#a7763b7fc1696a7f6c86a7db1b5b8b23c),
[OpenSCADCommands.RefineShapeFeature.Activated()](../../da/d7a/classOpenSCADCommands_1_1RefineShapeFeature.html#abb456c0096d99791b92008ba222bca8c),
[OpenSCADCommands.MirrorMeshFeature.Activated()](../../db/de0/classOpenSCADCommands_1_1MirrorMeshFeature.html#ae2f318c3fd947f45cad423f50438f033),
[OpenSCADCommands.ScaleMeshFeature.Activated()](../../df/d31/classOpenSCADCommands_1_1ScaleMeshFeature.html#a163220f4e5c635c3033ebf0b5d8a59bc),
[OpenSCADCommands.ResizeMeshFeature.Activated()](../../d4/d16/classOpenSCADCommands_1_1ResizeMeshFeature.html#a643572ba0dce19f3fa27e5aa25333448),
[OpenSCADCommands.IncreaseToleranceFeature.Activated()](../../d4/d6e/classOpenSCADCommands_1_1IncreaseToleranceFeature.html#a7eb73352d3386092349e1fe031879158),
[OpenSCADCommands.ExpandPlacements.Activated()](../../d1/dab/classOpenSCADCommands_1_1ExpandPlacements.html#afce83d99023a1ae03e4ceb942a97d0b2),
[OpenSCADCommands.ReplaceObject.Activated()](../../d5/d2b/classOpenSCADCommands_1_1ReplaceObject.html#a3a2c5a0f60cc9b6ff2cac5def467ff85),
[OpenSCADCommands.RemoveSubtree.Activated()](../../d2/d3c/classOpenSCADCommands_1_1RemoveSubtree.html#ac8ba2b246c02cd8bcf1ca79c27fdab3f),
[OpenSCADCommands.AddOpenSCADElement.Activated()](../../d2/d2a/classOpenSCADCommands_1_1AddOpenSCADElement.html#abeb6be2dff999cc8d9bfd30b412ca9b8),
[OpenSCADCommands.OpenSCADMeshBoolean.Activated()](../../da/db3/classOpenSCADCommands_1_1OpenSCADMeshBoolean.html#afef3d7e3582404e8e881f00e147737a1),
[OpenSCADCommands.Hull.Activated()](../../df/dd9/classOpenSCADCommands_1_1Hull.html#a9173a8f93aee87ad7da5e9a74fa64fa3),
[OpenSCADCommands.Minkowski.Activated()](../../d8/d4c/classOpenSCADCommands_1_1Minkowski.html#ae66aabf498113bff8631e76bdf063e9f),
[AttachmentEditor.Commands.CommandEditAttachment.Activated()](../../db/d42/classAttachmentEditor_1_1Commands_1_1CommandEditAttachment.html#a9dd8510a6ed6c8d11a180d27e8b172a3),
[BasicShapes.CommandShapes.CommandTube.Activated()](../../d4/d8b/classBasicShapes_1_1CommandShapes_1_1CommandTube.html#a2f396e3cd07f8aa15c3f76fc7af744b3),
[BOPTools.JoinFeatures.CommandConnect.Activated()](../../d7/d5c/classBOPTools_1_1JoinFeatures_1_1CommandConnect.html#a3f7cda1bd19bf036f0fbcb99ed9a4c5b),
[BOPTools.JoinFeatures.CommandEmbed.Activated()](../../d2/d0c/classBOPTools_1_1JoinFeatures_1_1CommandEmbed.html#a8aeb75010c460d69f39512df8f88e5d8),
[BOPTools.JoinFeatures.CommandCutout.Activated()](../../d9/d9e/classBOPTools_1_1JoinFeatures_1_1CommandCutout.html#aea70bc7aa6ac82465e976f3dafbbc8f6),
[BOPTools.SplitFeatures.CommandBooleanFragments.Activated()](../../d3/d93/classBOPTools_1_1SplitFeatures_1_1CommandBooleanFragments.html#a7b9e5d1014ca80db52c61ec1d7b566fe),
[BOPTools.SplitFeatures.CommandSlice.Activated()](../../d5/d56/classBOPTools_1_1SplitFeatures_1_1CommandSlice.html#ac38f0353cffad07b63ce820b45db249a),
[BOPTools.SplitFeatures.CommandSliceApart.Activated()](../../d2/db2/classBOPTools_1_1SplitFeatures_1_1CommandSliceApart.html#a9fdd049797563a8aebd3a940b3d8f968),
[BOPTools.SplitFeatures.CommandXOR.Activated()](../../d1/d26/classBOPTools_1_1SplitFeatures_1_1CommandXOR.html#a20490f5a8071e5d3a140a6bc5f9c265e),
CompoundTools._CommandCompoundFilter._CommandCompoundFilter.Activated(),
CompoundTools._CommandExplodeCompound._CommandExplodeCompound.Activated(),
[Mod.PartDesign.FeatureHole.HoleGui.HoleGui.Activated()](../../de/df5/classMod_1_1PartDesign_1_1FeatureHole_1_1HoleGui_1_1HoleGui.html#ac8c74a3729cef7e2f17b4f9bdb7e2564),
Mod.PartDesign.InvoluteGearFeature._CommandInvoluteGear.Activated(),
[Mod.PartDesign.SprocketFeature.CommandSprocket.Activated()](../../d2/d1c/classMod_1_1PartDesign_1_1SprocketFeature_1_1CommandSprocket.html#a6d0c5be59d04609ad5945179361d65a3),
[Mod.PartDesign.WizardShaft.WizardShaft.WizardShaftGui.Activated()](../../d1/d98/classMod_1_1PartDesign_1_1WizardShaft_1_1WizardShaft_1_1WizardShaftGui.html#aaf429379e2c032156f274831685b067b),
[Mod.PartDesign.WizardShaft.WizardShaft.WizardShaftGuiCallback.Activated()](../../d3/d7e/classMod_1_1PartDesign_1_1WizardShaft_1_1WizardShaft_1_1WizardShaftGuiCallback.html#a0a898b916c2849dc03e9d5761de3be02),
[InitGui.PathWorkbench.Activated()](../../d8/d4b/classInitGui_1_1PathWorkbench.html#a26562746c1c2161eaacc3a5ff285b3ac),
PathCommands._CommandSelectLoop.Activated(),
PathCommands._ToggleOperation.Activated(),
PathCommands._CopyOperation.Activated(),
[PathScripts.PathArray.CommandPathArray.Activated()](../../d4/da0/classPathScripts_1_1PathArray_1_1CommandPathArray.html#a5fa5694279ad278aa542e929744def4f),
[PathScripts.PathCamoticsGui.CommandCamoticsSimulate.Activated()](../../d3/d30/classPathScripts_1_1PathCamoticsGui_1_1CommandCamoticsSimulate.html#ac3f0054fbfe423735963d5fb86f48f0b),
[PathScripts.PathComment.CommandPathComment.Activated()](../../d0/d5f/classPathScripts_1_1PathComment_1_1CommandPathComment.html#a10ba445877e70a710af6a25b25bc9f84),
[PathScripts.PathCopy.CommandPathCopy.Activated()](../../df/d75/classPathScripts_1_1PathCopy_1_1CommandPathCopy.html#a3b1446a10bfd186d6d4d76ade1776e05),
[PathScripts.PathDressupAxisMap.CommandPathDressup.Activated()](../../df/d57/classPathScripts_1_1PathDressupAxisMap_1_1CommandPathDressup.html#aaf492bea90c6e8f99961f5b81400b5ce),
[PathScripts.PathDressupDogbone.CommandDressupDogbone.Activated()](../../d9/dcd/classPathScripts_1_1PathDressupDogbone_1_1CommandDressupDogbone.html#a6def98bb11ecd7e6ade8245e7895e49a),
[PathScripts.PathDressupDragknife.CommandDressupDragknife.Activated()](../../da/db4/classPathScripts_1_1PathDressupDragknife_1_1CommandDressupDragknife.html#a03b6b6e699621a5d7cbdc5750e3d9a18),
[PathScripts.PathDressupLeadInOut.CommandPathDressupLeadInOut.Activated()](../../d6/d84/classPathScripts_1_1PathDressupLeadInOut_1_1CommandPathDressupLeadInOut.html#a02014c95f252d44ab8d4c9d1a47ca6fd),
[PathScripts.PathDressupPathBoundaryGui.CommandPathDressupPathBoundary.Activated()](../../d5/d5e/classPathScripts_1_1PathDressupPathBoundaryGui_1_1CommandPathDressupPathBoundary.html#a1191c73c5bf02984fcbc76d7ffd7b1f2),
[PathScripts.PathDressupRampEntry.CommandPathDressupRampEntry.Activated()](../../dd/d95/classPathScripts_1_1PathDressupRampEntry_1_1CommandPathDressupRampEntry.html#a33323f1ef0ffa6fae7bf89c12faf3af7),
[PathScripts.PathDressupTagGui.CommandPathDressupTag.Activated()](../../d9/dbf/classPathScripts_1_1PathDressupTagGui_1_1CommandPathDressupTag.html#af459da19fcfd46d888370a6b96693e90),
[PathScripts.PathDressupZCorrect.CommandPathDressup.Activated()](../../d3/d5a/classPathScripts_1_1PathDressupZCorrect_1_1CommandPathDressup.html#a386a0d998787d9624672e0536d2df83a),
[PathScripts.PathFixture.CommandPathFixture.Activated()](../../dc/d61/classPathScripts_1_1PathFixture_1_1CommandPathFixture.html#a823c6d9a030f88ddd9468eea5c086634),
[PathScripts.PathHop.CommandPathHop.Activated()](../../de/d08/classPathScripts_1_1PathHop_1_1CommandPathHop.html#a37b1642b0c067ab93c5c583ca759b1ff),
[PathScripts.PathInspect.CommandPathInspect.Activated()](../../d5/d86/classPathScripts_1_1PathInspect_1_1CommandPathInspect.html#ae7a2f1d10fdd269d7caad045cffbe6c0),
[PathScripts.PathJobCmd.CommandJobCreate.Activated()](../../db/d17/classPathScripts_1_1PathJobCmd_1_1CommandJobCreate.html#aac9d774ebbcda6c9840a1b776045fd2f),
[PathScripts.PathJobCmd.CommandJobTemplateExport.Activated()](../../d7/d23/classPathScripts_1_1PathJobCmd_1_1CommandJobTemplateExport.html#a46c6375673177f553908512c9d97a897),
[PathScripts.PathOpGui.CommandSetStartPoint.Activated()](../../d6/dbd/classPathScripts_1_1PathOpGui_1_1CommandSetStartPoint.html#a78350aa3fac8d98da91a007f2a9b0ec7),
[PathScripts.PathOpGui.CommandPathOp.Activated()](../../d9/d03/classPathScripts_1_1PathOpGui_1_1CommandPathOp.html#a38ddda904f03d2dc5eaab0e973c2a46e),
[PathScripts.PathPlane.CommandPathPlane.Activated()](../../d7/d45/classPathScripts_1_1PathPlane_1_1CommandPathPlane.html#a7b763ae516745e9b6d28359674022743),
[PathScripts.PathPost.CommandPathPost.Activated()](../../d3/d2b/classPathScripts_1_1PathPost_1_1CommandPathPost.html#a40bf2e64c5e9e7368fee709d5f77e038),
[PathScripts.PathPropertyBagGui.PropertyBagCreateCommand.Activated()](../../da/d55/classPathScripts_1_1PathPropertyBagGui_1_1PropertyBagCreateCommand.html#a46e354436cba14ee8cb8ab121ed98cf6),
[PathScripts.PathSanity.CommandPathSanity.Activated()](../../d1/d9f/classPathScripts_1_1PathSanity_1_1CommandPathSanity.html#a5a52208f24ef2fc321946005256c125f),
[PathScripts.PathSimpleCopy.CommandPathSimpleCopy.Activated()](../../d4/d36/classPathScripts_1_1PathSimpleCopy_1_1CommandPathSimpleCopy.html#a88f697dffc5a7cbf7f000daeccd5a60f),
[PathScripts.PathSimulatorGui.CommandPathSimulate.Activated()](../../d0/d75/classPathScripts_1_1PathSimulatorGui_1_1CommandPathSimulate.html#a4a199b71744438c10a74ac14dc36e06e),
[PathScripts.PathStop.CommandPathStop.Activated()](../../d3/d4b/classPathScripts_1_1PathStop_1_1CommandPathStop.html#ae987a1bfd07662ad788427d9863832b5),
[PathScripts.PathToolBitCmd.CommandToolBitCreate.Activated()](../../d4/d7f/classPathScripts_1_1PathToolBitCmd_1_1CommandToolBitCreate.html#a29874dd37355fe04cad5f09fda3c3f3b),
[PathScripts.PathToolBitCmd.CommandToolBitSave.Activated()](../../df/d30/classPathScripts_1_1PathToolBitCmd_1_1CommandToolBitSave.html#a47ec66f1759fa7000c0a90ba594732df),
[PathScripts.PathToolBitCmd.CommandToolBitLoad.Activated()](../../d4/d6b/classPathScripts_1_1PathToolBitCmd_1_1CommandToolBitLoad.html#a9dbc117e8bb10a77e1b255dd7be44072),
[PathScripts.PathToolBitLibraryCmd.CommandToolBitSelectorOpen.Activated()](../../dc/de6/classPathScripts_1_1PathToolBitLibraryCmd_1_1CommandToolBitSelectorOpen.html#a7d2bca876adc5ea45435344d13ab6e1d),
[PathScripts.PathToolBitLibraryCmd.CommandToolBitLibraryOpen.Activated()](../../d4/da0/classPathScripts_1_1PathToolBitLibraryCmd_1_1CommandToolBitLibraryOpen.html#af967be893fedfb63eeace33da3992d22),
[PathScripts.PathToolControllerGui.CommandPathToolController.Activated()](../../d2/d0a/classPathScripts_1_1PathToolControllerGui_1_1CommandPathToolController.html#a44278988a0e43a30cacd844a8a7dc0a3),
[PathScripts.PathToolLibraryEditor.CommandToolLibraryEdit.Activated()](../../da/dea/classPathScripts_1_1PathToolLibraryEditor_1_1CommandToolLibraryEdit.html#a02b9aef9be310f09fd0e601df13ec17e),
Profiles._CommandProfileHexagon1.Activated(),
[Spreadsheet_legacy._Command_Spreadsheet_Create.Activated()](../../d8/d6d/classSpreadsheet__legacy_1_1__Command__Spreadsheet__Create.html#acf358d5124bb3f96fca579e717837f6d),
[Spreadsheet_legacy._Command_Spreadsheet_Controller.Activated()](../../df/d02/classSpreadsheet__legacy_1_1__Command__Spreadsheet__Controller.html#a8fbc1dadf309ae9b9206843a9149f628),
[Spreadsheet_legacy._Command_Spreadsheet_PropertyController.Activated()](../../d4/d51/classSpreadsheet__legacy_1_1__Command__Spreadsheet__PropertyController.html#ad0f4a4cf07839d8ce4e5c050fabb267e),
[TechDrawTools.CommandMoveView.CommandMoveView.Activated()](../../dd/d52/classTechDrawTools_1_1CommandMoveView_1_1CommandMoveView.html#aed849ae06e47c074ef5a98b4d6224163),
[TechDrawTools.CommandShareView.CommandShareView.Activated()](../../de/d84/classTechDrawTools_1_1CommandShareView_1_1CommandShareView.html#a6b3459dfd4874b719271644231d7018a),
[Commands.TemplatePyMod_Cmd1.Activated()](../../d9/d04/classCommands_1_1TemplatePyMod__Cmd1.html#a79d60405fb5d595099913fdfe3f486b4),
[Commands.TemplatePyMod_Cmd2.Activated()](../../da/d5b/classCommands_1_1TemplatePyMod__Cmd2.html#a692b339dc4901e0ac3efa55914bb5d13),
[Commands.TemplatePyMod_Cmd3.Activated()](../../d8/d67/classCommands_1_1TemplatePyMod__Cmd3.html#a179ba41bf91e4bc3644986faa1ed43e7),
[Commands.TemplatePyMod_Cmd4.Activated()](../../d3/d0f/classCommands_1_1TemplatePyMod__Cmd4.html#a8c9769e3f4ec7929cdd88be14017c6a0),
[Commands.TemplatePyMod_Cmd5.Activated()](../../d0/df6/classCommands_1_1TemplatePyMod__Cmd5.html#ab3e2d396ec86206a0f1ce01fd26712ff),
[Commands.TemplatePyMod_Cmd6.Activated()](../../db/d77/classCommands_1_1TemplatePyMod__Cmd6.html#a67e7faf8c53d82cf49783aca3a931671),
[Commands.TemplatePyGrp_1.Activated()](../../d5/de4/classCommands_1_1TemplatePyGrp__1.html#a8137c7b8eb4d3fbbe116e223961c1642),
[Commands.TemplatePyGrp_2.Activated()](../../d6/df5/classCommands_1_1TemplatePyGrp__2.html#a9eddf524ea4e7f2b77610d3478737b6c),
[Commands.TemplatePyGrp_3.Activated()](../../dd/db2/classCommands_1_1TemplatePyGrp__3.html#ad6bfa1c89fdc1f4b238d3a7111a532a8),
[InitGui.TemplatePyModWorkbench.Activated()](../../d8/dd0/classInitGui_1_1TemplatePyModWorkbench.html#a28e215eccf09190ddf92910cdec9ff49),
[PythonQt.PythonQtWorkbench.Activated()](../../d5/d7c/classPythonQt_1_1PythonQtWorkbench.html#a85e3ac2d4233403f56f5a33e00b3bbb9),
[Mod.Test.TestGui.TestCmd.Activated()](../../da/d54/classMod_1_1Test_1_1TestGui_1_1TestCmd.html#ad5d095ac85e6faacd0e1f23f6b04fa52),
[Mod.Test.TestGui.TestAllCmd.Activated()](../../dd/d86/classMod_1_1Test_1_1TestGui_1_1TestAllCmd.html#ac9114fffc7de9bde73f09724b2c417de),
[Mod.Test.TestGui.TestDocCmd.Activated()](../../d3/de0/classMod_1_1Test_1_1TestGui_1_1TestDocCmd.html#a7bc626ff85c19842bd9e00f8e4f9eea3),
[Mod.Test.TestGui.TestBaseCmd.Activated()](../../d2/d04/classMod_1_1Test_1_1TestGui_1_1TestBaseCmd.html#a94e943a8e869064274bec0201bf9531d),
[Mod.Test.TestGui.TestAllTextCmd.Activated()](../../d1/d0f/classMod_1_1Test_1_1TestGui_1_1TestAllTextCmd.html#a8ea850f1cc6aa4596590e4d4a952cb15),
[Mod.Test.TestGui.TestDocTextCmd.Activated()](../../d0/da0/classMod_1_1Test_1_1TestGui_1_1TestDocTextCmd.html#ab9f51f682cdf0d70cc20d1ec9728598b),
[Mod.Test.TestGui.TestBaseTextCmd.Activated()](../../d6/db9/classMod_1_1Test_1_1TestGui_1_1TestBaseTextCmd.html#a4d10e1caded2f0121a810e295c793763),
[Mod.Test.TestGui.TestWorkbenchCmd.Activated()](../../d0/d76/classMod_1_1Test_1_1TestGui_1_1TestWorkbenchCmd.html#a388850a42e97196d4c25f13de74ca023),
[Mod.Test.TestGui.TestCreateMenuCmd.Activated()](../../de/d4f/classMod_1_1Test_1_1TestGui_1_1TestCreateMenuCmd.html#a29dc043164238b095a69ba94539c7bb2),
[Mod.Test.TestGui.TestDeleteMenuCmd.Activated()](../../d9/db5/classMod_1_1Test_1_1TestGui_1_1TestDeleteMenuCmd.html#a5096cbbd440573a23b8185430fab97f4),
[Mod.Test.TestGui.TestInsertFeatureCmd.Activated()](../../de/d49/classMod_1_1Test_1_1TestGui_1_1TestInsertFeatureCmd.html#ab8d50523f655da069deb9ad8e2501353),
[Commands.TemplatePyCheckable.Activated()](../../dc/dac/classCommands_1_1TemplatePyCheckable.html#a2d393fc2e07e333b2e2986c33f92f276),
[draftguitools.gui_togglemodes.BaseMode.Activated()](../../da/d37/classdraftguitools_1_1gui__togglemodes_1_1BaseMode.html#adb42773e305d85b7ad3f05cfd57cb224),
[draftguitools.gui_array_simple.Array.Activated()](../../da/d0e/classdraftguitools_1_1gui__array__simple_1_1Array.html#a0d39a890eaccfb43bae967e3d3a80eda),
[draftguitools.gui_fillets.Fillet.Activated()](../../da/d40/classdraftguitools_1_1gui__fillets_1_1Fillet.html#af67b23b90312ec91aff8c0429f57f0f0),
[draftguitools.gui_lines.Line.Activated()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#a8033f2b529eaa31c53d41d504eed52bc),
[draftguitools.gui_base_original.Creator.Activated()](../../d4/d3b/classdraftguitools_1_1gui__base__original_1_1Creator.html#afc40d922df79205ecf060aef3341e772),
[draftguitools.gui_base_original.DraftTool.Activated()](../../da/d09/classdraftguitools_1_1gui__base__original_1_1DraftTool.html#a8a6b2926e2c1ff916e99373d1195cdd1),
[draftguitools.gui_base_original.Modifier.Activated()](../../db/d34/classdraftguitools_1_1gui__base__original_1_1Modifier.html#a6f6a0f1601d8904f5743bfe2d690d34b),
[draftguitools.gui_patharray.PathArray.Activated()](../../dd/d56/classdraftguitools_1_1gui__patharray_1_1PathArray.html#a5a5cefde88477507e179ecd2d4990b8d),
[draftguitools.gui_pathtwistedarray.PathTwistedArray.Activated()](../../d2/d4f/classdraftguitools_1_1gui__pathtwistedarray_1_1PathTwistedArray.html#aed8f7a8c0cf8a54ae8f741fecad1c864),
[draftguitools.gui_pointarray.PointArray.Activated()](../../d1/d71/classdraftguitools_1_1gui__pointarray_1_1PointArray.html#a2361ea4cc1f72d7897e657a7f093cc13),
[ArchPanel.CommandPanel.continueCmd](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad5408329191a0536d3f4d76f63a69367),
ArchStructure._CommandStructure.continueCmd,
ArchWall._CommandWall.continueCmd,
[DraftGui.DraftToolBar.continueCmd](../../d0/d91/classDraftGui_1_1DraftToolBar.html#af3e4a9f00e58b5aab044c3c1843e9b16),
[StdMeshers_FaceSide.Length()](../../da/d30/classStdMeshers__FaceSide.html#ab10c91dbc23ce96cc957f21a9deaf735),
[Base::Vector2d.Length()](../../db/da7/classBase_1_1Vector2d.html#a4a196e3b30ef1eaf4069e6ee7984798d),
[Base::Line2d.Length()](../../d1/d69/classBase_1_1Line2d.html#a05f118183e69c67107e28cb3c1cf2d32),
[Base::UnitSignature.Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::Unit.Length](../../d2/d37/classBase_1_1Unit.html#ae7af32a08ea9a0e1501571a2902c84bd),
[Base::Vector3< _Precision
>.Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[Base::Vector3< float
>.Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[Base::Vector3< double
>.Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[FaceQuadStruct::Side.Length()](../../d7/d88/structFaceQuadStruct_1_1Side.html#aa7fd814714c3b66d22b2220024efc469),
[SMESH_Array1< TheItemType
>.Length()](../../d8/df2/classSMESH__Array1.html#a8525eba64e37ad5e4f73e0a579b6f16f),
[SMESH_Array2< TheItemType
>.Length()](../../d5/d8e/classSMESH__Array2.html#aa8123f1966456d487fd7ad892cf65283),
[ArchPanel.CommandPanel.Length](../../d9/d86/classArchPanel_1_1CommandPanel.html#a216ea090679f3a79793493e52d677d69),
ArchPrecast._DentsTaskPanel.Length, ArchStructure._CommandStructure.Length,
ArchWall._CommandWall.Length,
[Mesh::Cylinder.Length](../../df/def/classMesh_1_1Cylinder.html#a26a198edd5cd3394c3afcc52b6faef88),
[Mesh::Cone.Length](../../d4/dbc/classMesh_1_1Cone.html#aa667283a541d4ea937e3011a5d530120),
[Mesh::Cube.Length](../../df/d68/classMesh_1_1Cube.html#a3c60137b91bcc739f7ad2b1a29d9a5ec),
Wm4::GVector< Real >.Length(), Wm4::Quaternion< Real >.Length(), Wm4::Vector2<
Real >.Length(), Wm4::Vector3< Real >.Length(), Wm4::Vector4< Real >.Length(),
[Part::Box.Length](../../dc/d80/classPart_1_1Box.html#a05fa6a3189976f7ca8d53a7ab23007ab),
[Part::Plane.Length](../../d0/d1c/classPart_1_1Plane.html#a9a385fd52af097411c607714cc4caad6),
[PartDesign::Line.Length](../../d0/d2a/classPartDesign_1_1Line.html#ae35cfa78234d62672b21f56975585a13),
[PartDesign::Plane.Length](../../df/df0/classPartDesign_1_1Plane.html#ac1e1ce5919d1c9dfa12b15915a8ec2a2),
[PartDesign::FeatureExtrude.Length](../../da/d12/classPartDesign_1_1FeatureExtrude.html#af46a913fd8cc2eb695a51c0d584b586d),
[PartDesign::LinearPattern.Length](../../d2/d86/classPartDesign_1_1LinearPattern.html#a0ee6f99081f80492a8f53c4419160a2a),
[PartDesign::Box.Length](../../df/d97/classPartDesign_1_1Box.html#af1576f0f628a2c56a5ef74de71ee7c98),
[Span.Length()](../../d0/db3/classSpan.html#a25ad6e232cd12e143ef5e5deb0a61672),
[DocumentObject.Box.Length](../../d9/d5e/classDocumentObject_1_1Box.html#a954671db05e53755e8a6541b56dcda8d),
[ArchPanel.CommandPanel.Profile](../../d9/d86/classArchPanel_1_1CommandPanel.html#ae6853ed51f834120710e01c60464f3f3),
[ArchProfile.Arch_Profile.Profile](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a4810f8511de0e13f8ecd5d955c19c644),
ArchProfile._Profile.Profile,
[ArchProfile.ProfileTaskPanel.Profile](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a00eb3f90d2c95c384614b65cc9dde08b),
ArchStructure._CommandStructure.Profile,
[PartDesign::ProfileBased.Profile](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a43d980d965c8eb1f6e0cb6c1ce7be7dd),
[PartDesignGui::ViewProviderLoft.Profile](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#a967511bbda23b602ebc9e2df52372a3ea3a40eaf32c21ad73474836cff86b8b68),
[PartDesignGui::ViewProviderPipe.Profile](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a33e876ddcc94e710a86a041b38a407a5a451e0dea3c048d27a9ecf0294c99f141),
[ArchPanel.CommandPanel.rotated](../../d9/d86/classArchPanel_1_1CommandPanel.html#af080a575474187ffa84a13ab0b6ba40b),
[ArchPanel.CommandPanel.Thickness](../../d9/d86/classArchPanel_1_1CommandPanel.html#a59c0667e69a9d522c52b897f96c3c7cc),
ArchWindow._CommandWindow.Thickness,
[Inspection::Feature.Thickness](../../d6/d23/classInspection_1_1Feature.html#a34ebd2f0ec2b0e6a541e4f9727e03cbc),
[Part::Thickness.Thickness()](../../db/d73/classPart_1_1Thickness.html#af9acf05fa602567de8ff2d6ba6128ac0),
[PartDesign::Thickness.Thickness()](../../d4/d22/classPartDesign_1_1Thickness.html#af9acf05fa602567de8ff2d6ba6128ac0),
[Mod.PartDesign.PartDesignTests.TestThickness.TestThickness.Thickness](../../d4/db2/classMod_1_1PartDesign_1_1PartDesignTests_1_1TestThickness_1_1TestThickness.html#a3c39efe9b84c21a74eb2b398c7c3ddd6),
[DraftVecUtils.toString()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf4889ceb585ea38ecf58d3f2af95b39a),
[ArchPanel.CommandPanel.tracker](../../d9/d86/classArchPanel_1_1CommandPanel.html#a1e7eeca96127526224adc5fc23f2ca32),
ArchStructure._CommandStructure.tracker, ArchWall._CommandWall.tracker,
ArchWindow._CommandWindow.tracker,
[draftguitools.gui_arcs.Arc_3Points.tracker](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#a36025145a72c98ed8244589eec677c6a),
[draftguitools.gui_snapper.Snapper.tracker](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a30795a875d73ef7126807f4a721ed3b7),
[Base::BoundBox2d.Width()](../../de/db4/classBase_1_1BoundBox2d.html#a2ac4f7f142c631813a6ecc93882cc362),
[ArchPanel.CommandPanel.Width](../../d9/d86/classArchPanel_1_1CommandPanel.html#a3f3b80fcbef81f11aedf8b5f96568c65),
ArchPrecast._DentsTaskPanel.Width, ArchStructure._CommandStructure.Width,
ArchWall._CommandWall.Width, ArchWindow._CommandWindow.Width,
[Drawing::FeatureClip.Width](../../d5/d4a/classDrawing_1_1FeatureClip.html#a2a73d8dcd503728f1b646ee157a10fee),
[LWPolyDataOut.Width](../../d2/d0b/structLWPolyDataOut.html#acfc5bb32cdfcc1941c2924b67612c9ab),
[Mesh::Cube.Width](../../df/d68/classMesh_1_1Cube.html#a185905a13cf56d3d573f1561ef443209),
[Part::Box.Width](../../dc/d80/classPart_1_1Box.html#a514a50af9ed78a44badf340ff3599c30),
[Part::Plane.Width](../../d0/d1c/classPart_1_1Plane.html#a0a51e8e3e056325683b8da949a0a5e48),
[PartDesign::Plane.Width](../../df/df0/classPartDesign_1_1Plane.html#ae1700753ba6ad47a9e755c0a01fe7abe),
[PartDesign::Box.Width](../../df/d97/classPartDesign_1_1Box.html#aa3196833d52edfdc29f7a4ecf3b63068),
[CBox2D.Width()](../../d5/d81/classCBox2D.html#a58a0784e62386b5ca2e49786a06a62ec),
[Points::Structured.Width](../../d0/d43/classPoints_1_1Structured.html#a421f9824634b14e4b7e66eb3eb7e40df),
[TechDraw::DrawTemplate.Width](../../d8/d95/classTechDraw_1_1DrawTemplate.html#aa7baae7fbabe1b9291916dcbf9000380),
[TechDraw::DrawViewClip.Width](../../dd/de8/classTechDraw_1_1DrawViewClip.html#abb7889984a0da96998cc3cf1005afed3),
and
[TechDraw::DrawViewImage.Width](../../d0/d87/classTechDraw_1_1DrawViewImage.html#ad3b6ebf71493b472e56314d2ac783f01).

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

def ArchPanel.CommandPanel.GetResources  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4).

## ◆ IsActive()

def ArchPanel.CommandPanel.IsActive  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ rotate()

def ArchPanel.CommandPanel.rotate  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[ArchPanel.CommandPanel.rotated](../../d9/d86/classArchPanel_1_1CommandPanel.html#af080a575474187ffa84a13ab0b6ba40b).

Referenced by
[PathScripts.PathDressupLeadInOut.ObjectDressup.getLeadEnd()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#ac4be8c95d4aa1440fb03c096c4e44e57),
[PathScripts.PathDressupLeadInOut.ObjectDressup.getLeadStart()](../../de/dde/classPathScripts_1_1PathDressupLeadInOut_1_1ObjectDressup.html#a2d9de34620ee069b425e7f99f0efe9da),
[draftguitools.gui_rotate.Rotate.numericRadius()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a9233be8153158528af33797d19c7dffd),
[ArchSectionPlane.SectionPlaneTaskPanel.rotateX()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a7d1ba8918bf98848d9ba29440e7c084d),
[ArchSectionPlane.SectionPlaneTaskPanel.rotateY()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#af9398626ca18b43945fc07cd1161d7cf),
and
[ArchSectionPlane.SectionPlaneTaskPanel.rotateZ()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a0a097c582cee6fcdab575dfb800e7d6d).

## ◆ setContinue()

def ArchPanel.CommandPanel.setContinue  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _i_  
| ) | |   
  
References
[ArchPanel.CommandPanel.continueCmd](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad5408329191a0536d3f4d76f63a69367),
ArchStructure._CommandStructure.continueCmd,
ArchWall._CommandWall.continueCmd, and
[DraftGui.DraftToolBar.continueCmd](../../d0/d91/classDraftGui_1_1DraftToolBar.html#af3e4a9f00e58b5aab044c3c1843e9b16).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c).

## ◆ setLength()

def ArchPanel.CommandPanel.setLength  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _d_  
| ) | |   
  
References
[StdMeshers_FaceSide.Length()](../../da/d30/classStdMeshers__FaceSide.html#ab10c91dbc23ce96cc957f21a9deaf735),
[Base::Vector2d.Length()](../../db/da7/classBase_1_1Vector2d.html#a4a196e3b30ef1eaf4069e6ee7984798d),
[Base::Line2d.Length()](../../d1/d69/classBase_1_1Line2d.html#a05f118183e69c67107e28cb3c1cf2d32),
[Base::UnitSignature.Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::Unit.Length](../../d2/d37/classBase_1_1Unit.html#ae7af32a08ea9a0e1501571a2902c84bd),
[Base::Vector3< float
>.Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[Base::Vector3< _Precision
>.Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[Base::Vector3< double
>.Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[ArchPanel.CommandPanel.Length](../../d9/d86/classArchPanel_1_1CommandPanel.html#a216ea090679f3a79793493e52d677d69),
ArchPrecast._DentsTaskPanel.Length, ArchStructure._CommandStructure.Length,
ArchWall._CommandWall.Length,
[Mesh::Cylinder.Length](../../df/def/classMesh_1_1Cylinder.html#a26a198edd5cd3394c3afcc52b6faef88),
[Mesh::Cone.Length](../../d4/dbc/classMesh_1_1Cone.html#aa667283a541d4ea937e3011a5d530120),
[Mesh::Cube.Length](../../df/d68/classMesh_1_1Cube.html#a3c60137b91bcc739f7ad2b1a29d9a5ec),
Wm4::GVector< Real >.Length(), Wm4::Quaternion< Real >.Length(), Wm4::Vector2<
Real >.Length(), Wm4::Vector3< Real >.Length(), Wm4::Vector4< Real >.Length(),
[FaceQuadStruct::Side.Length()](../../d7/d88/structFaceQuadStruct_1_1Side.html#aa7fd814714c3b66d22b2220024efc469),
[SMESH_Array1< TheItemType
>.Length()](../../d8/df2/classSMESH__Array1.html#a8525eba64e37ad5e4f73e0a579b6f16f),
[SMESH_Array2< TheItemType
>.Length()](../../d5/d8e/classSMESH__Array2.html#aa8123f1966456d487fd7ad892cf65283),
[Part::Box.Length](../../dc/d80/classPart_1_1Box.html#a05fa6a3189976f7ca8d53a7ab23007ab),
[Part::Plane.Length](../../d0/d1c/classPart_1_1Plane.html#a9a385fd52af097411c607714cc4caad6),
[PartDesign::Line.Length](../../d0/d2a/classPartDesign_1_1Line.html#ae35cfa78234d62672b21f56975585a13),
[PartDesign::Plane.Length](../../df/df0/classPartDesign_1_1Plane.html#ac1e1ce5919d1c9dfa12b15915a8ec2a2),
[PartDesign::FeatureExtrude.Length](../../da/d12/classPartDesign_1_1FeatureExtrude.html#af46a913fd8cc2eb695a51c0d584b586d),
[PartDesign::LinearPattern.Length](../../d2/d86/classPartDesign_1_1LinearPattern.html#a0ee6f99081f80492a8f53c4419160a2a),
[PartDesign::Box.Length](../../df/d97/classPartDesign_1_1Box.html#af1576f0f628a2c56a5ef74de71ee7c98),
[Span.Length()](../../d0/db3/classSpan.html#a25ad6e232cd12e143ef5e5deb0a61672),
and
[DocumentObject.Box.Length](../../d9/d5e/classDocumentObject_1_1Box.html#a954671db05e53755e8a6541b56dcda8d).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c).

## ◆ setPreset()

def ArchPanel.CommandPanel.setPreset  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _i_  
| ) | |   
  
References
[ArchPanel.CommandPanel.vHeight](../../d9/d86/classArchPanel_1_1CommandPanel.html#a17d6ea726931a857118bfd35da626d05),
ArchStructure._CommandStructure.vHeight,
[PartGui::Ui_DlgPartBox.vLength](../../d4/db2/classPartGui_1_1Ui__DlgPartBox.html#a2555998b8eca86421ab19afc10b0722f),
[ArchPanel.CommandPanel.vLength](../../d9/d86/classArchPanel_1_1CommandPanel.html#adf6f59233ebb9efe0c2e230aaeef8959),
ArchStructure._CommandStructure.vLength,
[ArchPanel.CommandPanel.vWidth](../../d9/d86/classArchPanel_1_1CommandPanel.html#a20a9b66ad7e1c3bd2c571088695d12d2),
and ArchStructure._CommandStructure.vWidth.

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
and
[ArchProfile.Arch_Profile.setCategory()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#aeb374a3c40d75b04d7c3f37eba51ed31).

## ◆ setThickness()

def ArchPanel.CommandPanel.setThickness  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _d_  
| ) | |   
  
References
[ArchPanel.CommandPanel.Thickness](../../d9/d86/classArchPanel_1_1CommandPanel.html#a59c0667e69a9d522c52b897f96c3c7cc),
ArchWindow._CommandWindow.Thickness,
[Inspection::Feature.Thickness](../../d6/d23/classInspection_1_1Feature.html#a34ebd2f0ec2b0e6a541e4f9727e03cbc),
[Part::Thickness.Thickness()](../../db/d73/classPart_1_1Thickness.html#af9acf05fa602567de8ff2d6ba6128ac0),
[PartDesign::Thickness.Thickness()](../../d4/d22/classPartDesign_1_1Thickness.html#af9acf05fa602567de8ff2d6ba6128ac0),
and
[Mod.PartDesign.PartDesignTests.TestThickness.TestThickness.Thickness](../../d4/db2/classMod_1_1PartDesign_1_1PartDesignTests_1_1TestThickness_1_1TestThickness.html#a3c39efe9b84c21a74eb2b398c7c3ddd6).

## ◆ setWidth()

def ArchPanel.CommandPanel.setWidth  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _d_  
| ) | |   
  
References
[Base::BoundBox2d.Width()](../../de/db4/classBase_1_1BoundBox2d.html#a2ac4f7f142c631813a6ecc93882cc362),
[ArchPanel.CommandPanel.Width](../../d9/d86/classArchPanel_1_1CommandPanel.html#a3f3b80fcbef81f11aedf8b5f96568c65),
ArchPrecast._DentsTaskPanel.Width, ArchStructure._CommandStructure.Width,
ArchWall._CommandWall.Width, ArchWindow._CommandWindow.Width,
[Drawing::FeatureClip.Width](../../d5/d4a/classDrawing_1_1FeatureClip.html#a2a73d8dcd503728f1b646ee157a10fee),
[LWPolyDataOut.Width](../../d2/d0b/structLWPolyDataOut.html#acfc5bb32cdfcc1941c2924b67612c9ab),
[Mesh::Cube.Width](../../df/d68/classMesh_1_1Cube.html#a185905a13cf56d3d573f1561ef443209),
[Part::Box.Width](../../dc/d80/classPart_1_1Box.html#a514a50af9ed78a44badf340ff3599c30),
[Part::Plane.Width](../../d0/d1c/classPart_1_1Plane.html#a0a51e8e3e056325683b8da949a0a5e48),
[PartDesign::Plane.Width](../../df/df0/classPartDesign_1_1Plane.html#ae1700753ba6ad47a9e755c0a01fe7abe),
[PartDesign::Box.Width](../../df/d97/classPartDesign_1_1Box.html#aa3196833d52edfdc29f7a4ecf3b63068),
[CBox2D.Width()](../../d5/d81/classCBox2D.html#a58a0784e62386b5ca2e49786a06a62ec),
[Points::Structured.Width](../../d0/d43/classPoints_1_1Structured.html#a421f9824634b14e4b7e66eb3eb7e40df),
[TechDraw::DrawTemplate.Width](../../d8/d95/classTechDraw_1_1DrawTemplate.html#aa7baae7fbabe1b9291916dcbf9000380),
[TechDraw::DrawViewClip.Width](../../dd/de8/classTechDraw_1_1DrawViewClip.html#abb7889984a0da96998cc3cf1005afed3),
and
[TechDraw::DrawViewImage.Width](../../d0/d87/classTechDraw_1_1DrawViewImage.html#ad3b6ebf71493b472e56314d2ac783f01).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c).

## ◆ taskbox()

def ArchPanel.CommandPanel.taskbox  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c).

## ◆ update()

def ArchPanel.CommandPanel.update  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _point_ ,   
|  |  | _info_  
| ) | |   
  
References
[StdMeshers_FaceSide.Length()](../../da/d30/classStdMeshers__FaceSide.html#ab10c91dbc23ce96cc957f21a9deaf735),
[Base::Vector2d.Length()](../../db/da7/classBase_1_1Vector2d.html#a4a196e3b30ef1eaf4069e6ee7984798d),
[Base::Line2d.Length()](../../d1/d69/classBase_1_1Line2d.html#a05f118183e69c67107e28cb3c1cf2d32),
[Base::UnitSignature.Length](../../d0/d2c/structBase_1_1UnitSignature.html#ae4a473d949777742fa105349d2b3ea2a),
[Base::Unit.Length](../../d2/d37/classBase_1_1Unit.html#ae7af32a08ea9a0e1501571a2902c84bd),
[Base::Vector3< _Precision
>.Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[Base::Vector3< float
>.Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[Base::Vector3< double
>.Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
Wm4::GVector< Real >.Length(), [SMESH_Array1< TheItemType
>.Length()](../../d8/df2/classSMESH__Array1.html#a8525eba64e37ad5e4f73e0a579b6f16f),
ArchStructure._CommandStructure.Length, ArchWall._CommandWall.Length,
[Mesh::Cone.Length](../../d4/dbc/classMesh_1_1Cone.html#aa667283a541d4ea937e3011a5d530120),
Wm4::Quaternion< Real >.Length(), Wm4::Vector2< Real >.Length(), Wm4::Vector3<
Real >.Length(), Wm4::Vector4< Real >.Length(),
[FaceQuadStruct::Side.Length()](../../d7/d88/structFaceQuadStruct_1_1Side.html#aa7fd814714c3b66d22b2220024efc469),
[SMESH_Array2< TheItemType
>.Length()](../../d5/d8e/classSMESH__Array2.html#aa8123f1966456d487fd7ad892cf65283),
[ArchPanel.CommandPanel.Length](../../d9/d86/classArchPanel_1_1CommandPanel.html#a216ea090679f3a79793493e52d677d69),
ArchPrecast._DentsTaskPanel.Length,
[Mesh::Cylinder.Length](../../df/def/classMesh_1_1Cylinder.html#a26a198edd5cd3394c3afcc52b6faef88),
[Mesh::Cube.Length](../../df/d68/classMesh_1_1Cube.html#a3c60137b91bcc739f7ad2b1a29d9a5ec),
[Part::Box.Length](../../dc/d80/classPart_1_1Box.html#a05fa6a3189976f7ca8d53a7ab23007ab),
[Part::Plane.Length](../../d0/d1c/classPart_1_1Plane.html#a9a385fd52af097411c607714cc4caad6),
[PartDesign::Line.Length](../../d0/d2a/classPartDesign_1_1Line.html#ae35cfa78234d62672b21f56975585a13),
[PartDesign::Plane.Length](../../df/df0/classPartDesign_1_1Plane.html#ac1e1ce5919d1c9dfa12b15915a8ec2a2),
[PartDesign::FeatureExtrude.Length](../../da/d12/classPartDesign_1_1FeatureExtrude.html#af46a913fd8cc2eb695a51c0d584b586d),
[PartDesign::LinearPattern.Length](../../d2/d86/classPartDesign_1_1LinearPattern.html#a0ee6f99081f80492a8f53c4419160a2a),
[PartDesign::Box.Length](../../df/d97/classPartDesign_1_1Box.html#af1576f0f628a2c56a5ef74de71ee7c98),
[Span.Length()](../../d0/db3/classSpan.html#a25ad6e232cd12e143ef5e5deb0a61672),
[DocumentObject.Box.Length](../../d9/d5e/classDocumentObject_1_1Box.html#a954671db05e53755e8a6541b56dcda8d),
[ArchPanel.CommandPanel.rotated](../../d9/d86/classArchPanel_1_1CommandPanel.html#af080a575474187ffa84a13ab0b6ba40b),
[ArchPanel.CommandPanel.Thickness](../../d9/d86/classArchPanel_1_1CommandPanel.html#a59c0667e69a9d522c52b897f96c3c7cc),
ArchWindow._CommandWindow.Thickness,
[Inspection::Feature.Thickness](../../d6/d23/classInspection_1_1Feature.html#a34ebd2f0ec2b0e6a541e4f9727e03cbc),
[Part::Thickness.Thickness()](../../db/d73/classPart_1_1Thickness.html#af9acf05fa602567de8ff2d6ba6128ac0),
[PartDesign::Thickness.Thickness()](../../d4/d22/classPartDesign_1_1Thickness.html#af9acf05fa602567de8ff2d6ba6128ac0),
[Mod.PartDesign.PartDesignTests.TestThickness.TestThickness.Thickness](../../d4/db2/classMod_1_1PartDesign_1_1PartDesignTests_1_1TestThickness_1_1TestThickness.html#a3c39efe9b84c21a74eb2b398c7c3ddd6),
[ArchPanel.CommandPanel.tracker](../../d9/d86/classArchPanel_1_1CommandPanel.html#a1e7eeca96127526224adc5fc23f2ca32),
ArchStructure._CommandStructure.tracker, ArchWall._CommandWall.tracker,
ArchWindow._CommandWindow.tracker,
[draftguitools.gui_arcs.Arc_3Points.tracker](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#a36025145a72c98ed8244589eec677c6a),
[draftguitools.gui_snapper.Snapper.tracker](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a30795a875d73ef7126807f4a721ed3b7),
[Base::BoundBox2d.Width()](../../de/db4/classBase_1_1BoundBox2d.html#a2ac4f7f142c631813a6ecc93882cc362),
[ArchPanel.CommandPanel.Width](../../d9/d86/classArchPanel_1_1CommandPanel.html#a3f3b80fcbef81f11aedf8b5f96568c65),
ArchPrecast._DentsTaskPanel.Width, ArchStructure._CommandStructure.Width,
ArchWall._CommandWall.Width, ArchWindow._CommandWindow.Width,
[Drawing::FeatureClip.Width](../../d5/d4a/classDrawing_1_1FeatureClip.html#a2a73d8dcd503728f1b646ee157a10fee),
[LWPolyDataOut.Width](../../d2/d0b/structLWPolyDataOut.html#acfc5bb32cdfcc1941c2924b67612c9ab),
[Mesh::Cube.Width](../../df/d68/classMesh_1_1Cube.html#a185905a13cf56d3d573f1561ef443209),
[Part::Box.Width](../../dc/d80/classPart_1_1Box.html#a514a50af9ed78a44badf340ff3599c30),
[Part::Plane.Width](../../d0/d1c/classPart_1_1Plane.html#a0a51e8e3e056325683b8da949a0a5e48),
[PartDesign::Plane.Width](../../df/df0/classPartDesign_1_1Plane.html#ae1700753ba6ad47a9e755c0a01fe7abe),
[PartDesign::Box.Width](../../df/d97/classPartDesign_1_1Box.html#aa3196833d52edfdc29f7a4ecf3b63068),
[CBox2D.Width()](../../d5/d81/classCBox2D.html#a58a0784e62386b5ca2e49786a06a62ec),
[Points::Structured.Width](../../d0/d43/classPoints_1_1Structured.html#a421f9824634b14e4b7e66eb3eb7e40df),
[TechDraw::DrawTemplate.Width](../../d8/d95/classTechDraw_1_1DrawTemplate.html#aa7baae7fbabe1b9291916dcbf9000380),
[TechDraw::DrawViewClip.Width](../../dd/de8/classTechDraw_1_1DrawViewClip.html#abb7889984a0da96998cc3cf1005afed3),
and
[TechDraw::DrawViewImage.Width](../../d0/d87/classTechDraw_1_1DrawViewImage.html#ad3b6ebf71493b472e56314d2ac783f01).

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

## ◆ continueCmd

ArchPanel.CommandPanel.continueCmd  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[DraftGui.DraftToolBar.arcUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a57112e938abe78fa23f685487f7d7772),
[DraftGui.DraftToolBar.checkSpecialChars()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#adce6adaef00a1beedb03268ed3807ffa),
[DraftGui.DraftToolBar.escape()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a77e93c6d6cb9b94b783e63b8ca906844),
[DraftGui.DraftToolBar.extUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a4701754c552e1bd6f6395695a076a501),
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[DraftGui.DraftToolBar.lineUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a1c32bf97a72e48be2e7b80146fe24f14),
[DraftGui.DraftToolBar.modUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad48bd3fabcdc24ff731d49c0ad37772a),
[DraftGui.DraftToolBar.offUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a92313622580952e8a0a93369843f12d4),
[DraftGui.DraftToolBar.retranslateUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a4bb513675d44079e184d661fba122e63),
[ArchPanel.CommandPanel.setContinue()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ae1212a57c8cea24a45f4c997d1c9e2e0),
[DraftGui.DraftToolBar.setContinue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a5796409a55e80a6f6b09919bd9fd1f17),
[DraftGui.DraftToolBar.SSizeUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a24a868919f2f074d3b81ea9e34be53e5),
[DraftGui.DraftToolBar.SSUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#add56a8cf841deabd9cb3a6ed833b8f4a),
[DraftGui.DraftToolBar.toggleContinue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad142a5fe18898325a03095703bd647c5),
and
[DraftGui.DraftToolBar.wireUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a22ef193a2ad202f59a095e8b9a0bae78).

## ◆ Length

ArchPanel.CommandPanel.Length  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[ArchPanel.CommandPanel.setLength()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a324c9bdbfec0dd8eacfb7d0cea302998),
and
[ArchPanel.CommandPanel.update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c).

## ◆ points

ArchPanel.CommandPanel.points  
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

## ◆ Profile

ArchPanel.CommandPanel.Profile  
---  
  
Referenced by
[ArchProfile.ProfileTaskPanel.accept()](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a2506d93eee0ae9e8570d71e066425999),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchProfile.ProfileTaskPanel.changeProfile()](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a440683bf0e41eba72709320a7bd4c49b),
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[ArchProfile.Arch_Profile.getPoint()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#adba04e55c6f0800f15566d4246397582),
and
[ArchProfile.Arch_Profile.setPreset()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#ae128806d02925f8e8a82559c8dee3f8f).

## ◆ rotated

ArchPanel.CommandPanel.rotated  
---  
  
Referenced by
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[ArchPanel.CommandPanel.rotate()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ac8b0e4434f74c6e0a73e6b6a96ddb6b2),
and
[ArchPanel.CommandPanel.update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c).

## ◆ Thickness

ArchPanel.CommandPanel.Thickness  
---  
  
Referenced by
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[ArchPanel.CommandPanel.setThickness()](../../d9/d86/classArchPanel_1_1CommandPanel.html#abe9208c3896b3024492b1ca2219786af),
and
[ArchPanel.CommandPanel.update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c).

## ◆ tracker

ArchPanel.CommandPanel.tracker  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftguitools.gui_arcs.Arc_3Points.drawArc()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#ad2b5ab087c3acf911c62b7d6816bd083),
[draftguitools.gui_arcs.Arc_3Points.finish()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#a14de6ccfeaf7a3143b1db145756da598),
[draftguitools.gui_arcs.Arc_3Points.getPoint()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#addd65326b504c7bf765526ef2db14321),
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[draftguitools.gui_snapper.Snapper.off()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#abd73f787754ba838ce877bfcd2bbd59b),
[draftguitools.gui_snapper.Snapper.setTrackers()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a64c29baf97159e274d4e8ed69d141f8b),
[draftguitools.gui_snapper.Snapper.snapToCrossExtensions()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#acee40380387892206a064e5b4b878275),
[draftguitools.gui_snapper.Snapper.snapToExtensions()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ae1f59975a9ed59a52c5c72b11a89e8c3),
[draftguitools.gui_snapper.Snapper.snapToGrid()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ad33d36f945a15ec39fba7d0d5184dfbc),
[draftguitools.gui_snapper.Snapper.snapToObject()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a2c5eb552fed1dc7a61c628dc393ae869),
[draftguitools.gui_snapper.Snapper.snapToPolar()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a5a30c9877875867157703325b090e21f),
and
[ArchPanel.CommandPanel.update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c).

## ◆ vHeight

ArchPanel.CommandPanel.vHeight  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
and
[ArchPanel.CommandPanel.setPreset()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a8ee939633a1994367e81aaac4b9d1103).

## ◆ vLength

ArchPanel.CommandPanel.vLength  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
and
[ArchPanel.CommandPanel.setPreset()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a8ee939633a1994367e81aaac4b9d1103).

## ◆ vWidth

ArchPanel.CommandPanel.vWidth  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
and
[ArchPanel.CommandPanel.setPreset()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a8ee939633a1994367e81aaac4b9d1103).

## ◆ Width

ArchPanel.CommandPanel.Width  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchPanel.CommandPanel.getPoint()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ad968284b7adc2bee10d76a20c1a4c7fb),
[ArchPanel.CommandPanel.setWidth()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a32bea4e80ff9a4e8e91d89aead1d88e1),
and
[ArchPanel.CommandPanel.update()](../../d9/d86/classArchPanel_1_1CommandPanel.html#a2e34ede3be08f250ec800823ef76df1c).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchPanel.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

