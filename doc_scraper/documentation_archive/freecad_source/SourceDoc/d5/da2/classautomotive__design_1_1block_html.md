---
url: https://freecad.github.io/SourceDoc/d5/da2/classautomotive__design_1_1block.html
scraped_at: 2025-09-08T15:00:57.006768
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [block](../../d5/da2/classautomotive__design_1_1block.html)

[List of all members](../../d8/d5c/classautomotive__design_1_1block-members.html) | Public Member Functions | Public Attributes

automotive_design.block Class Reference

##  Public Member Functions  
  
---  
def | [position](../../d5/da2/classautomotive__design_1_1block.html#a998f9b7a43e7bbbad3a561adc6de24a3) ()  
def | [x](../../d5/da2/classautomotive__design_1_1block.html#a0421bfd2a1d0655dbad5d19f0cb496a2) ()  
def | [y](../../d5/da2/classautomotive__design_1_1block.html#abeb750b3215d27ccfc2662002289aa0d) ()  
def | [z](../../d5/da2/classautomotive__design_1_1block.html#af0c1cabf19e90f0b8256e456e7c0421b) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html)  
def | [dim](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#aef245618450610e88788dcaea46ad742) ()  
def | [wr1](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[position](../../d5/da2/classautomotive__design_1_1block.html#a9115131b2ca2b16f12f4229774c1de80)  
|
[x](../../d5/da2/classautomotive__design_1_1block.html#a61579e457e98f25bf681ac6c2eee0117)  
|
[y](../../d5/da2/classautomotive__design_1_1block.html#ad34538b5498fd4ce1f217efac141c372)  
|
[z](../../d5/da2/classautomotive__design_1_1block.html#aa13f6909f4db29e3f4b558377285c2e2)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity block definition.
    
        :param position
        :type position:axis2_placement_3d
    
        :param x
        :type x:positive_length_measure
    
        :param y
        :type y:positive_length_measure
    
        :param z
        :type z:positive_length_measure

## Member Function Documentation

## ◆ position()

def automotive_design.block.position  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.conic._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_positional._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.elementary_surface._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cylinder._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_angular_wedge._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cone._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_spot._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.block._position,
automotive_design.conic._position,
automotive_design.light_source_positional._position,
automotive_design.elementary_surface._position,
automotive_design.right_circular_cylinder._position,
automotive_design.right_angular_wedge._position,
automotive_design.torus._position,
automotive_design.right_circular_cone._position,
automotive_design.light_source_spot._position,
automotive_design.block._position, config_control_design.conic._position,
config_control_design.elementary_surface._position,
ifc2x3.ifcsweptsurface._position, ifc2x3.ifcparameterizedprofiledef._position,
ifc2x3.ifcsweptareasolid._position, ifc2x3.ifccsgprimitive3d._position,
ifc2x3.ifcconic._position, ifc2x3.ifcpolygonalboundedhalfspace._position,
ifc2x3.ifcelementarysurface._position,
ifc2x3.ifclightsourcepositional._position,
ifc2x3.ifclightsourcegoniometric._position, ifc4.ifcsweptsurface._position,
ifc4.ifcparameterizedprofiledef._position, ifc4.ifcsweptareasolid._position,
ifc4.ifccsgprimitive3d._position, ifc4.ifcconic._position,
ifc4.ifcpolygonalboundedhalfspace._position,
ifc4.ifcelementarysurface._position, ifc4.ifclightsourcepositional._position,
ifc4.ifclightsourcegoniometric._position, and
ifc4.ifcrecurrencepattern._position.

Referenced by
[WorkingPlane.Plane.alignToPointAndAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab85860830e3debec48d3cdb58d30621a),
[WorkingPlane.Plane.alignToPointAndAxis_SVG()](../../d3/d93/classWorkingPlane_1_1Plane.html#a53cb561d317b813ea9a22ef8e319104d),
[WorkingPlane.Plane.copy()](../../d3/d93/classWorkingPlane_1_1Plane.html#ad5a25c4e17593442d7a38bd51cf7167a),
[ifc2x3.ifcsweptsurface.dim()](../../d6/df8/classifc2x3_1_1ifcsweptsurface.html#a5eb3187a1e204615771d1c71c0e05346),
[ifc2x3.ifcelementarysurface.dim()](../../dc/d78/classifc2x3_1_1ifcelementarysurface.html#aa9fc1e4bb64357615bba0ad16fa6bc10),
[WorkingPlane.Plane.getGlobalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1b8410be9ee2eefb1e5c3902d4d1a230),
[WorkingPlane.Plane.getLocalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab4027587aa29bc4393a52df8159376e1),
[WorkingPlane.Plane.getParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a22bffbf8caab92f815500ed57b857427),
[WorkingPlane.Plane.getPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#aeb4cd9d5da24076f5984cfd0994ed75f),
[WorkingPlane.Plane.offsetToPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#accc43f410bbe85c53bfad80b68903c6c),
[WorkingPlane.Plane.projectPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1918c0d5d231f78520826f24326111e6),
[WorkingPlane.Plane.restore()](../../d3/d93/classWorkingPlane_1_1Plane.html#abe9dafedd4a855a65c40666b5391f4a3),
[WorkingPlane.Plane.save()](../../d3/d93/classWorkingPlane_1_1Plane.html#a5f765f888050e49b7ee71785e689d0fd),
[WorkingPlane.Plane.setFromParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a417c10c501c570723b1c6b471da3fa13),
and
[WorkingPlane.Plane.setFromPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab9f10a2a72fa2ba198adbfad26ec26c2).

## ◆ x()

def automotive_design.block.x  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_angular_wedge._x,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.block._x,
automotive_design.right_angular_wedge._x, and automotive_design.block._x.

Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector.add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[DraftGui.DraftToolBar.changeXValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a2264e5b2058aeec75cb9044b36485378),
[importSVG.svgHandler.characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[PathScripts.PathInspect.GCodeEditorDialog.cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[Mod.PartDesign.Scripts.FilletArc.Vector.cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[PathScripts.PostUtils.GCodeEditorDialog.done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Mod.PartDesign.Scripts.FilletArc.Vector.dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[Mod.PartDesign.Scripts.FilletArc.Vector.length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Mod.PartDesign.Scripts.FilletArc.Vector.mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector.norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[PathScripts.PathDressupHoldingTags.Tag.originAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aa1cbd48305f117e5197555822fd45f3f),
[DraftGui.DraftToolBar.pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[Mod.PartDesign.Scripts.FilletArc.Vector.sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[DraftGui.DraftToolBar.update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar.updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
[DraftGui.DraftToolBar.validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
and
[automotive_design.right_angular_wedge.wr1()](../../d4/df4/classautomotive__design_1_1right__angular__wedge.html#a08ba5a830562d7f45bb10fe924c7b534).

## ◆ y()

def automotive_design.block.y  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_angular_wedge._y,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.block._y,
automotive_design.right_angular_wedge._y, and automotive_design.block._y.

Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector.add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[DraftGui.DraftToolBar.changeYValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a245f69442c47aa69844d30313e68b2b7),
[importSVG.svgHandler.characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[PathScripts.PathInspect.GCodeEditorDialog.cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[Mod.PartDesign.Scripts.FilletArc.Vector.cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[PathScripts.PostUtils.GCodeEditorDialog.done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Mod.PartDesign.Scripts.FilletArc.Vector.dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[Mod.PartDesign.Scripts.FilletArc.Vector.length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Mod.PartDesign.Scripts.FilletArc.Vector.mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector.norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[PathScripts.PathDressupHoldingTags.Tag.originAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aa1cbd48305f117e5197555822fd45f3f),
[DraftGui.DraftToolBar.pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[Mod.PartDesign.Scripts.FilletArc.Vector.sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[DraftGui.DraftToolBar.update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar.updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
and
[DraftGui.DraftToolBar.validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de).

## ◆ z()

def automotive_design.block.z  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_angular_wedge._z,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.block._z,
automotive_design.right_angular_wedge._z, and automotive_design.block._z.

Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector.add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[automotive_design.revolved_area_solid.axis_line()](../../d4/ded/classautomotive__design_1_1revolved__area__solid.html#ae7714359aef57b10dc9d110c4c95109c),
[automotive_design.surface_of_revolution.axis_line()](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#ac11430bfca20d807bd7fbb1de4555324),
[automotive_design.revolved_face_solid.axis_line()](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a88ba8cae1c9e693beda33bf96a0423ca),
[ifc4.ifcrevolvedareasolid.axisdirectioninxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a34e620e30709c7c4e2c619daa7704ece),
[ifc2x3.ifcsurfaceofrevolution.axisline()](../../db/d1b/classifc2x3_1_1ifcsurfaceofrevolution.html#a0689126db6a08f9f1183f65515b53370),
[ifc2x3.ifcrevolvedareasolid.axisline()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#ad7a180e86495ea93d5acb25ffcc33ffa),
[ifc4.ifcsurfaceofrevolution.axisline()](../../d4/de7/classifc4_1_1ifcsurfaceofrevolution.html#adf527bd278ddce78734fc2b01bec7b37),
[ifc4.ifcrevolvedareasolid.axisline()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a45efcb80c8963331649e13f991ec7534),
[PathScripts.PathDressupHoldingTags.Tag.bottom()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aaae502deebbb0cc7adf2f1dd338d9ac8),
[DraftGui.DraftToolBar.changeZValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a33ea2715914aa73b36107598fe5702c5),
[PathScripts.PathDressupTag.TagSolid.cloneAt()](../../d2/dc0/classPathScripts_1_1PathDressupTag_1_1TagSolid.html#a0da4c220cd1980731ce8fbb646cc8e13),
[PathScripts.PathDressupHoldingTags.Tag.createSolidsAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a2cb6cc02ae81caafbb137dfe20ebfdd8),
[Mod.PartDesign.Scripts.FilletArc.Vector.cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[Mod.PartDesign.Scripts.FilletArc.Vector.dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[Mod.PartDesign.Scripts.FilletArc.Vector.length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Mod.PartDesign.Scripts.FilletArc.Vector.mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector.norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[DraftGui.DraftToolBar.pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[importSH3D.SH3DHandler.startElement()](../../d8/de6/classimportSH3D_1_1SH3DHandler.html#a9a512563447c10428d4e0e65fbbc95f7),
[Mod.PartDesign.Scripts.FilletArc.Vector.sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[PathScripts.PathDressupHoldingTags.Tag.top()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#abe7b229a9b4e1207f20627c3546cfe1c),
[DraftGui.DraftToolBar.update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar.updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
[DraftGui.DraftToolBar.validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
and
[ifc2x3.ifcrevolvedareasolid.wr32()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a2d005a905b9bcd1b1d7fc934f7085073).

## Member Data Documentation

## ◆ position

automotive_design.block.position  
---  
  
Referenced by
[WorkingPlane.Plane.alignToPointAndAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab85860830e3debec48d3cdb58d30621a),
[WorkingPlane.Plane.alignToPointAndAxis_SVG()](../../d3/d93/classWorkingPlane_1_1Plane.html#a53cb561d317b813ea9a22ef8e319104d),
[WorkingPlane.Plane.copy()](../../d3/d93/classWorkingPlane_1_1Plane.html#ad5a25c4e17593442d7a38bd51cf7167a),
[ifc2x3.ifcsweptsurface.dim()](../../d6/df8/classifc2x3_1_1ifcsweptsurface.html#a5eb3187a1e204615771d1c71c0e05346),
[ifc2x3.ifcelementarysurface.dim()](../../dc/d78/classifc2x3_1_1ifcelementarysurface.html#aa9fc1e4bb64357615bba0ad16fa6bc10),
[WorkingPlane.Plane.getGlobalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1b8410be9ee2eefb1e5c3902d4d1a230),
[WorkingPlane.Plane.getLocalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab4027587aa29bc4393a52df8159376e1),
[WorkingPlane.Plane.getParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a22bffbf8caab92f815500ed57b857427),
[WorkingPlane.Plane.getPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#aeb4cd9d5da24076f5984cfd0994ed75f),
[WorkingPlane.Plane.offsetToPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#accc43f410bbe85c53bfad80b68903c6c),
[WorkingPlane.Plane.projectPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1918c0d5d231f78520826f24326111e6),
[WorkingPlane.Plane.restore()](../../d3/d93/classWorkingPlane_1_1Plane.html#abe9dafedd4a855a65c40666b5391f4a3),
[WorkingPlane.Plane.save()](../../d3/d93/classWorkingPlane_1_1Plane.html#a5f765f888050e49b7ee71785e689d0fd),
[WorkingPlane.Plane.setFromParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a417c10c501c570723b1c6b471da3fa13),
and
[WorkingPlane.Plane.setFromPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab9f10a2a72fa2ba198adbfad26ec26c2).

## ◆ x

automotive_design.block.x  
---  
  
Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector.add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[DraftGui.DraftToolBar.changeXValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a2264e5b2058aeec75cb9044b36485378),
[importSVG.svgHandler.characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[PathScripts.PathInspect.GCodeEditorDialog.cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[Mod.PartDesign.Scripts.FilletArc.Vector.cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[PathScripts.PostUtils.GCodeEditorDialog.done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Mod.PartDesign.Scripts.FilletArc.Vector.dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[Mod.PartDesign.Scripts.FilletArc.Vector.length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Mod.PartDesign.Scripts.FilletArc.Vector.mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector.norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[PathScripts.PathDressupHoldingTags.Tag.originAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aa1cbd48305f117e5197555822fd45f3f),
[DraftGui.DraftToolBar.pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[Mod.PartDesign.Scripts.FilletArc.Vector.sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[DraftGui.DraftToolBar.update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar.updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
[DraftGui.DraftToolBar.validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
and
[automotive_design.right_angular_wedge.wr1()](../../d4/df4/classautomotive__design_1_1right__angular__wedge.html#a08ba5a830562d7f45bb10fe924c7b534).

## ◆ y

automotive_design.block.y  
---  
  
Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector.add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[DraftGui.DraftToolBar.changeYValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a245f69442c47aa69844d30313e68b2b7),
[importSVG.svgHandler.characters()](../../dc/d45/classimportSVG_1_1svgHandler.html#ac7be43f49fd582e0df6cebefe4fca23b),
[PathScripts.PathInspect.GCodeEditorDialog.cleanup()](../../d6/d67/classPathScripts_1_1PathInspect_1_1GCodeEditorDialog.html#a0c015fefd66a03b656d701124d9333c7),
[Mod.PartDesign.Scripts.FilletArc.Vector.cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[PathScripts.PostUtils.GCodeEditorDialog.done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
[Mod.PartDesign.Scripts.FilletArc.Vector.dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[Mod.PartDesign.Scripts.FilletArc.Vector.length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Mod.PartDesign.Scripts.FilletArc.Vector.mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector.norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[PathScripts.PathDressupHoldingTags.Tag.originAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aa1cbd48305f117e5197555822fd45f3f),
[DraftGui.DraftToolBar.pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[Mod.PartDesign.Scripts.FilletArc.Vector.sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[DraftGui.DraftToolBar.update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar.updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
and
[DraftGui.DraftToolBar.validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de).

## ◆ z

automotive_design.block.z  
---  
  
Referenced by
[Mod.PartDesign.Scripts.FilletArc.Vector.add()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1841a45d4f89d500fa3b90f23571d21b),
[automotive_design.revolved_area_solid.axis_line()](../../d4/ded/classautomotive__design_1_1revolved__area__solid.html#ae7714359aef57b10dc9d110c4c95109c),
[automotive_design.surface_of_revolution.axis_line()](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#ac11430bfca20d807bd7fbb1de4555324),
[automotive_design.revolved_face_solid.axis_line()](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a88ba8cae1c9e693beda33bf96a0423ca),
[ifc4.ifcrevolvedareasolid.axisdirectioninxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a34e620e30709c7c4e2c619daa7704ece),
[ifc2x3.ifcsurfaceofrevolution.axisline()](../../db/d1b/classifc2x3_1_1ifcsurfaceofrevolution.html#a0689126db6a08f9f1183f65515b53370),
[ifc2x3.ifcrevolvedareasolid.axisline()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#ad7a180e86495ea93d5acb25ffcc33ffa),
[ifc4.ifcsurfaceofrevolution.axisline()](../../d4/de7/classifc4_1_1ifcsurfaceofrevolution.html#adf527bd278ddce78734fc2b01bec7b37),
[ifc4.ifcrevolvedareasolid.axisline()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a45efcb80c8963331649e13f991ec7534),
[PathScripts.PathDressupHoldingTags.Tag.bottom()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#aaae502deebbb0cc7adf2f1dd338d9ac8),
[DraftGui.DraftToolBar.changeZValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a33ea2715914aa73b36107598fe5702c5),
[PathScripts.PathDressupTag.TagSolid.cloneAt()](../../d2/dc0/classPathScripts_1_1PathDressupTag_1_1TagSolid.html#a0da4c220cd1980731ce8fbb646cc8e13),
[PathScripts.PathDressupHoldingTags.Tag.createSolidsAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a2cb6cc02ae81caafbb137dfe20ebfdd8),
[Mod.PartDesign.Scripts.FilletArc.Vector.cross()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a77c73dde4146f8599532959c6f748d98),
[Mod.PartDesign.Scripts.FilletArc.Vector.dot()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#ad040c136bcb0b948d29ca586e41e8363),
[Mod.PartDesign.Scripts.FilletArc.Vector.length()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a5517156960d089d79fa8b0b4cc2d051c),
[Mod.PartDesign.Scripts.FilletArc.Vector.mult()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#aee98bd6bc5bb4a15cecd1586c2d40c78),
[Mod.PartDesign.Scripts.FilletArc.Vector.norm()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a1746a8cb810a626e2b9f850e86d6ad20),
[DraftGui.DraftToolBar.pointUi()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a9961ebfaad834af409ff96a355e5ffc8),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[importSH3D.SH3DHandler.startElement()](../../d8/de6/classimportSH3D_1_1SH3DHandler.html#a9a512563447c10428d4e0e65fbbc95f7),
[Mod.PartDesign.Scripts.FilletArc.Vector.sub()](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a7949f5bb3dabb7c390cabbdf0bd39b5c),
[PathScripts.PathDressupHoldingTags.Tag.top()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#abe7b229a9b4e1207f20627c3546cfe1c),
[DraftGui.DraftToolBar.update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[DraftGui.DraftToolBar.updateSnapper()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ad12c818f12031e99bfe64f4b74a57b90),
[DraftGui.DraftToolBar.validatePoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a523e58d22f5a7ba329c92d8ffd0c75de),
and
[ifc2x3.ifcrevolvedareasolid.wr32()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a2d005a905b9bcd1b1d7fc934f7085073).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

