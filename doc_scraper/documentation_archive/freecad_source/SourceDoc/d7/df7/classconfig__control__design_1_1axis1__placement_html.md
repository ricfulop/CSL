---
url: https://freecad.github.io/SourceDoc/d7/df7/classconfig__control__design_1_1axis1__placement.html
scraped_at: 2025-09-08T15:20:16.849886
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [axis1_placement](../../d7/df7/classconfig__control__design_1_1axis1__placement.html)

[List of all members](../../db/d7f/classconfig__control__design_1_1axis1__placement-members.html) | Public Member Functions | Public Attributes

config_control_design.axis1_placement Class Reference

##  Public Member Functions  
  
---  
def | [axis](../../d7/df7/classconfig__control__design_1_1axis1__placement.html#ab57460263b7ec67dee4912aef34d097a) ()  
def | [wr1](../../d7/df7/classconfig__control__design_1_1axis1__placement.html#a2b3bad17a685bd44d94f254992a1a550) (self)  
def | [z](../../d7/df7/classconfig__control__design_1_1axis1__placement.html#a2e286d9765dffb9a06686a29f273b3be) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.placement](../../da/d34/classconfig__control__design_1_1placement.html)  
def | [location](../../da/d34/classconfig__control__design_1_1placement.html#adf77ece548901b24af889e0b83726763) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html)  
def | [dim](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#aac385fb99d009b699d0d77f10ebdc5f1) ()  
def | [wr1](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
  
##  Public Attributes  
  
---  
|
[axis](../../d7/df7/classconfig__control__design_1_1axis1__placement.html#a425f406a2193625c2037a2e19c7fb961)  
|
[dim](../../d7/df7/classconfig__control__design_1_1axis1__placement.html#ab8663be4cfb6b0da0a3298d8d3a20bc6)  
|
[dummy_gri](../../d7/df7/classconfig__control__design_1_1axis1__placement.html#a91de1a1076e788dc527e7af308c74dec)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.placement](../../da/d34/classconfig__control__design_1_1placement.html)  
|
[location](../../da/d34/classconfig__control__design_1_1placement.html#a82d8e902f6a2bbfa6de928032d40bd1d)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity axis1_placement definition.
    
        :param axis
        :type axis:direction
    
        :param z
        :type z:direction

## Member Function Documentation

## ◆ axis()

def config_control_design.axis1_placement.axis  | ( | | ) |   
---|---|---|---|---  
  
References Base::Rotation._axis,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.axis1_placement._axis,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.revolved_area_solid._axis,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.revolved_face_solid._axis,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.axis2_placement_3d._axis,
automotive_design.axis1_placement._axis,
automotive_design.revolved_area_solid._axis,
automotive_design.axis2_placement_3d._axis,
automotive_design.revolved_face_solid._axis,
config_control_design.axis1_placement._axis,
config_control_design.axis2_placement_3d._axis,
ifc2x3.ifcrevolvedareasolid._axis, ifc2x3.ifcaxis1placement._axis,
ifc2x3.ifcaxis2placement3d._axis, ifc4.ifcrevolvedareasolid._axis,
ifc4.ifcaxis1placement._axis, ifc4.ifcaxis2placement3d._axis,
ifc4.ifcstructuralcurveconnection._axis, and
ifc4.ifcstructuralcurvemember._axis.

Referenced by
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.accept()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#aa70cf8b6adb6840c697d649f1bbeaa3f),
[WorkingPlane.Plane.alignToEdges()](../../d3/d93/classWorkingPlane_1_1Plane.html#a2b0086560d271d6958820d7f84b0d789),
[WorkingPlane.Plane.alignToFace()](../../d3/d93/classWorkingPlane_1_1Plane.html#aac15aec2ff8ab925af8ff8d893c5486d),
[WorkingPlane.Plane.alignToPointAndAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab85860830e3debec48d3cdb58d30621a),
[WorkingPlane.Plane.alignToPointAndAxis_SVG()](../../d3/d93/classWorkingPlane_1_1Plane.html#a53cb561d317b813ea9a22ef8e319104d),
[automotive_design.revolved_area_solid.axis_line()](../../d4/ded/classautomotive__design_1_1revolved__area__solid.html#ae7714359aef57b10dc9d110c4c95109c),
[automotive_design.revolved_face_solid.axis_line()](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a88ba8cae1c9e693beda33bf96a0423ca),
[ifc4.ifcaxis2placement3d.axisandrefdirprovision()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#ab9ae9f1a02e82414c656aed63f295321),
[ifc4.ifcrevolvedareasolid.axisdirectioninxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a34e620e30709c7c4e2c619daa7704ece),
[ifc4.ifcaxis2placement3d.axisis3d()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#ab2f3c3d035505e73f4c12cbceeeae151),
[ifc2x3.ifcrevolvedareasolid.axisline()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#ad7a180e86495ea93d5acb25ffcc33ffa),
[ifc4.ifcrevolvedareasolid.axisline()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a45efcb80c8963331649e13f991ec7534),
[ifc4.ifcrevolvedareasolid.axisstartinxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a76b11dffac1f3f7f53c5dfeef5227626),
[ifc4.ifcaxis2placement3d.axistorefdirposition()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#a1ba847e352152530b214a783a8171193),
[WorkingPlane.Plane.copy()](../../d3/d93/classWorkingPlane_1_1Plane.html#ad5a25c4e17593442d7a38bd51cf7167a),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.create_object()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#ac99628c4fa3165b5162bb6abac2b8936),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.get_axis()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#a709baa00ef11f678516a3b0e549e31a1),
[WorkingPlane.Plane.getClosestAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab3435ec06fdc07f4589cc099b222f346),
[WorkingPlane.Plane.getGlobalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1b8410be9ee2eefb1e5c3902d4d1a230),
[WorkingPlane.Plane.getGlobalRot()](../../d3/d93/classWorkingPlane_1_1Plane.html#a8b62e2ed891883d73463f7a799afc44a),
[WorkingPlane.Plane.getLocalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab4027587aa29bc4393a52df8159376e1),
[WorkingPlane.Plane.getLocalRot()](../../d3/d93/classWorkingPlane_1_1Plane.html#ac6d4009cbda9d7d73c9eda40206c5c44),
[WorkingPlane.Plane.getNormal()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1f85bb50a88a8336ed8c3d6b9ef64214),
[WorkingPlane.Plane.getParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a22bffbf8caab92f815500ed57b857427),
[WorkingPlane.Plane.getPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#aeb4cd9d5da24076f5984cfd0994ed75f),
[WorkingPlane.Plane.getRotation()](../../d3/d93/classWorkingPlane_1_1Plane.html#aa6f928c6a6a4719ea9c699e7a9a3a77b),
[WorkingPlane.Plane.inverse()](../../d3/d93/classWorkingPlane_1_1Plane.html#a20d2c59edaae7ee2f89658d1d73b7b9d),
[WorkingPlane.Plane.isGlobal()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab22fb0193373902a72efe7c9d287879c),
[WorkingPlane.Plane.isOrtho()](../../d3/d93/classWorkingPlane_1_1Plane.html#a223b1c266d05af427d39ecd06acfcb05),
[WorkingPlane.Plane.offsetToPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#accc43f410bbe85c53bfad80b68903c6c),
[automotive_design.axis2_placement_3d.p()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#aab66cdd3e3219a485a1d700a6bc8661f),
[config_control_design.axis2_placement_3d.p()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#ad2a448d4e07c9eb37ecd1abd490de827),
[ifc2x3.ifcaxis2placement3d.p()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#ae74a01c0495027bcf41e154aa7741c81),
[ifc4.ifcaxis2placement3d.p()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#a76a27e1e24395f50d01699e211089403),
[WorkingPlane.Plane.projectPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1918c0d5d231f78520826f24326111e6),
[WorkingPlane.Plane.projectPointOld()](../../d3/d93/classWorkingPlane_1_1Plane.html#a8371ff42986f6bc3a4747b1281ff83b9),
[WorkingPlane.Plane.restore()](../../d3/d93/classWorkingPlane_1_1Plane.html#abe9dafedd4a855a65c40666b5391f4a3),
[WorkingPlane.Plane.save()](../../d3/d93/classWorkingPlane_1_1Plane.html#a5f765f888050e49b7ee71785e689d0fd),
[WorkingPlane.Plane.setFromParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a417c10c501c570723b1c6b471da3fa13),
[WorkingPlane.Plane.setFromPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab9f10a2a72fa2ba198adbfad26ec26c2),
[WorkingPlane.Plane.setup()](../../d3/d93/classWorkingPlane_1_1Plane.html#aff570509d64f91a619fa59d06920fded),
[automotive_design.axis2_placement_3d.wr2()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a53e4146e50cdc12f6f425f5ae2a015e7),
[config_control_design.axis2_placement_3d.wr2()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8510a502b056a9261c4b9cf7323f51b4),
[ifc2x3.ifcaxis2placement3d.wr2()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#aab8fcc584ec7c8fa06ffd345c95b8663),
[ifc2x3.ifcrevolvedareasolid.wr31()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a16ccd5dc8889fd10923e40182318836b),
[ifc2x3.ifcrevolvedareasolid.wr32()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a2d005a905b9bcd1b1d7fc934f7085073),
[automotive_design.axis2_placement_3d.wr4()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a958dfcfe4ab4e5a077320cb4e34bbb4d),
[config_control_design.axis2_placement_3d.wr4()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8bec18bae8e6717f6914141ff0f73deb),
[ifc2x3.ifcaxis2placement3d.wr4()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#af6680b5dd24bd5ec433f4dd35da87a91),
[ifc2x3.ifcaxis2placement3d.wr5()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#a3bc2a1ddf745e062d17b10dcd9ac6450),
[ifc2x3.ifcaxis1placement.z()](../../df/db1/classifc2x3_1_1ifcaxis1placement.html#a67f5cce20ad3eed02520d3db096a7cb2),
and
[ifc4.ifcaxis1placement.z()](../../dd/ddf/classifc4_1_1ifcaxis1placement.html#a11c43803bb9668bb02a978b8e2f60d22).

## ◆ wr1()

def config_control_design.axis1_placement.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13).

## ◆ z()

def config_control_design.axis1_placement.z  | ( | | ) |   
---|---|---|---|---  
  
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

## ◆ axis

config_control_design.axis1_placement.axis  
---  
  
Referenced by
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.accept()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#aa70cf8b6adb6840c697d649f1bbeaa3f),
[WorkingPlane.Plane.alignToEdges()](../../d3/d93/classWorkingPlane_1_1Plane.html#a2b0086560d271d6958820d7f84b0d789),
[WorkingPlane.Plane.alignToFace()](../../d3/d93/classWorkingPlane_1_1Plane.html#aac15aec2ff8ab925af8ff8d893c5486d),
[WorkingPlane.Plane.alignToPointAndAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab85860830e3debec48d3cdb58d30621a),
[WorkingPlane.Plane.alignToPointAndAxis_SVG()](../../d3/d93/classWorkingPlane_1_1Plane.html#a53cb561d317b813ea9a22ef8e319104d),
[automotive_design.revolved_area_solid.axis_line()](../../d4/ded/classautomotive__design_1_1revolved__area__solid.html#ae7714359aef57b10dc9d110c4c95109c),
[automotive_design.revolved_face_solid.axis_line()](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a88ba8cae1c9e693beda33bf96a0423ca),
[ifc4.ifcaxis2placement3d.axisandrefdirprovision()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#ab9ae9f1a02e82414c656aed63f295321),
[ifc4.ifcrevolvedareasolid.axisdirectioninxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a34e620e30709c7c4e2c619daa7704ece),
[ifc4.ifcaxis2placement3d.axisis3d()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#ab2f3c3d035505e73f4c12cbceeeae151),
[ifc2x3.ifcrevolvedareasolid.axisline()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#ad7a180e86495ea93d5acb25ffcc33ffa),
[ifc4.ifcrevolvedareasolid.axisline()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a45efcb80c8963331649e13f991ec7534),
[ifc4.ifcrevolvedareasolid.axisstartinxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a76b11dffac1f3f7f53c5dfeef5227626),
[ifc4.ifcaxis2placement3d.axistorefdirposition()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#a1ba847e352152530b214a783a8171193),
[WorkingPlane.Plane.copy()](../../d3/d93/classWorkingPlane_1_1Plane.html#ad5a25c4e17593442d7a38bd51cf7167a),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.create_object()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#ac99628c4fa3165b5162bb6abac2b8936),
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.get_axis()](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#a709baa00ef11f678516a3b0e549e31a1),
[WorkingPlane.Plane.getClosestAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab3435ec06fdc07f4589cc099b222f346),
[WorkingPlane.Plane.getGlobalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1b8410be9ee2eefb1e5c3902d4d1a230),
[WorkingPlane.Plane.getGlobalRot()](../../d3/d93/classWorkingPlane_1_1Plane.html#a8b62e2ed891883d73463f7a799afc44a),
[WorkingPlane.Plane.getLocalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab4027587aa29bc4393a52df8159376e1),
[WorkingPlane.Plane.getLocalRot()](../../d3/d93/classWorkingPlane_1_1Plane.html#ac6d4009cbda9d7d73c9eda40206c5c44),
[WorkingPlane.Plane.getNormal()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1f85bb50a88a8336ed8c3d6b9ef64214),
[WorkingPlane.Plane.getParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a22bffbf8caab92f815500ed57b857427),
[WorkingPlane.Plane.getPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#aeb4cd9d5da24076f5984cfd0994ed75f),
[WorkingPlane.Plane.getRotation()](../../d3/d93/classWorkingPlane_1_1Plane.html#aa6f928c6a6a4719ea9c699e7a9a3a77b),
[WorkingPlane.Plane.inverse()](../../d3/d93/classWorkingPlane_1_1Plane.html#a20d2c59edaae7ee2f89658d1d73b7b9d),
[WorkingPlane.Plane.isGlobal()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab22fb0193373902a72efe7c9d287879c),
[WorkingPlane.Plane.isOrtho()](../../d3/d93/classWorkingPlane_1_1Plane.html#a223b1c266d05af427d39ecd06acfcb05),
[WorkingPlane.Plane.offsetToPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#accc43f410bbe85c53bfad80b68903c6c),
[automotive_design.axis2_placement_3d.p()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#aab66cdd3e3219a485a1d700a6bc8661f),
[config_control_design.axis2_placement_3d.p()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#ad2a448d4e07c9eb37ecd1abd490de827),
[ifc2x3.ifcaxis2placement3d.p()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#ae74a01c0495027bcf41e154aa7741c81),
[ifc4.ifcaxis2placement3d.p()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#a76a27e1e24395f50d01699e211089403),
[WorkingPlane.Plane.projectPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1918c0d5d231f78520826f24326111e6),
[WorkingPlane.Plane.projectPointOld()](../../d3/d93/classWorkingPlane_1_1Plane.html#a8371ff42986f6bc3a4747b1281ff83b9),
[WorkingPlane.Plane.restore()](../../d3/d93/classWorkingPlane_1_1Plane.html#abe9dafedd4a855a65c40666b5391f4a3),
[WorkingPlane.Plane.save()](../../d3/d93/classWorkingPlane_1_1Plane.html#a5f765f888050e49b7ee71785e689d0fd),
[WorkingPlane.Plane.setFromParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a417c10c501c570723b1c6b471da3fa13),
[WorkingPlane.Plane.setFromPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab9f10a2a72fa2ba198adbfad26ec26c2),
[WorkingPlane.Plane.setup()](../../d3/d93/classWorkingPlane_1_1Plane.html#aff570509d64f91a619fa59d06920fded),
[automotive_design.axis2_placement_3d.wr2()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a53e4146e50cdc12f6f425f5ae2a015e7),
[config_control_design.axis2_placement_3d.wr2()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8510a502b056a9261c4b9cf7323f51b4),
[ifc2x3.ifcaxis2placement3d.wr2()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#aab8fcc584ec7c8fa06ffd345c95b8663),
[ifc2x3.ifcrevolvedareasolid.wr31()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a16ccd5dc8889fd10923e40182318836b),
[ifc2x3.ifcrevolvedareasolid.wr32()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a2d005a905b9bcd1b1d7fc934f7085073),
[automotive_design.axis2_placement_3d.wr4()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a958dfcfe4ab4e5a077320cb4e34bbb4d),
[config_control_design.axis2_placement_3d.wr4()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8bec18bae8e6717f6914141ff0f73deb),
[ifc2x3.ifcaxis2placement3d.wr4()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#af6680b5dd24bd5ec433f4dd35da87a91),
[ifc2x3.ifcaxis2placement3d.wr5()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#a3bc2a1ddf745e062d17b10dcd9ac6450),
[ifc2x3.ifcaxis1placement.z()](../../df/db1/classifc2x3_1_1ifcaxis1placement.html#a67f5cce20ad3eed02520d3db096a7cb2),
and
[ifc4.ifcaxis1placement.z()](../../dd/ddf/classifc4_1_1ifcaxis1placement.html#a11c43803bb9668bb02a978b8e2f60d22).

## ◆ dim

config_control_design.axis1_placement.dim  
---  
  
Referenced by
[ifc4.ifccartesiantransformationoperator3d.axis3is3d()](../../d0/d2f/classifc4_1_1ifccartesiantransformationoperator3d.html#ad896e8cc3cd14db5cdcec81e4786eec1),
[ifc4.ifcaxis2placement3d.axisis3d()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#ab2f3c3d035505e73f4c12cbceeeae151),
[ifc2x3.ifcsweptsurface.dim()](../../d6/df8/classifc2x3_1_1ifcsweptsurface.html#a5eb3187a1e204615771d1c71c0e05346),
[ifc2x3.ifcplacement.dim()](../../dd/dfd/classifc2x3_1_1ifcplacement.html#ac4dbcef9f43207432d3fa6d838dbdfb7),
[ifc2x3.ifccartesiantransformationoperator.dim()](../../d8/d5d/classifc2x3_1_1ifccartesiantransformationoperator.html#ad46e1f75ce8f2e0d1937c900059809bb),
[ifc2x3.ifccurveboundedplane.dim()](../../d2/dff/classifc2x3_1_1ifccurveboundedplane.html#a4b77cf901367c1cd92ffe6ef787c2f69),
[ifc2x3.ifccompositecurvesegment.dim()](../../dd/d6e/classifc2x3_1_1ifccompositecurvesegment.html#a6014167f48b54f55af87dec16702de32),
[ifc2x3.ifcgeometricset.dim()](../../dc/dab/classifc2x3_1_1ifcgeometricset.html#af569a780b93b69b4dce81b08ddd66f89),
[ifc2x3.ifcrectangulartrimmedsurface.dim()](../../d6/d82/classifc2x3_1_1ifcrectangulartrimmedsurface.html#a9864cd346a9caa1e4e8cf5a282192889),
[ifc2x3.ifcbooleanresult.dim()](../../dd/d21/classifc2x3_1_1ifcbooleanresult.html#aa2c029e00fa7348f4841b70fb651f921),
[ifc2x3.ifcelementarysurface.dim()](../../dc/d78/classifc2x3_1_1ifcelementarysurface.html#aa9fc1e4bb64357615bba0ad16fa6bc10),
[ifc2x3.ifcpointoncurve.dim()](../../d4/dfb/classifc2x3_1_1ifcpointoncurve.html#a97ff0b230b758d8c719d3dbe23a653a8),
[ifc2x3.ifcpointonsurface.dim()](../../d0/d83/classifc2x3_1_1ifcpointonsurface.html#a470f7e831cabe7ab72d99a5afbcb5906),
[ifc2x3.ifcvector.dim()](../../d3/d7f/classifc2x3_1_1ifcvector.html#acba206090ebaf1068c18b522050ab356),
[ifc4.ifccompositecurvesegment.dim()](../../da/d5c/classifc4_1_1ifccompositecurvesegment.html#af5316372982441eb627ec543094e86aa),
[ifc4.ifcplacement.dim()](../../d4/da3/classifc4_1_1ifcplacement.html#a4ff119d99b8ac53bebec7145128d0452),
[ifc4.ifccartesiantransformationoperator.dim()](../../d4/d39/classifc4_1_1ifccartesiantransformationoperator.html#a0a344ffdcb72a602de421822f59573dc),
[ifc4.ifcgeometricset.dim()](../../d1/d95/classifc4_1_1ifcgeometricset.html#a795b14ef2879e9acc0c066d66e122b9b),
[ifc4.ifcbooleanresult.dim()](../../d0/d2c/classifc4_1_1ifcbooleanresult.html#aa87cd3a0d4ac5e137c88d13ce336ba19),
[ifc4.ifcpointoncurve.dim()](../../d3/d46/classifc4_1_1ifcpointoncurve.html#ab0edcecba3e98c552d95d8ec2cbfd963),
[ifc4.ifcpointonsurface.dim()](../../d5/df4/classifc4_1_1ifcpointonsurface.html#a400416d6b069afa2e89e5d43ec6a37f1),
[ifc4.ifcvector.dim()](../../d0/d94/classifc4_1_1ifcvector.html#a472491a5b13134e67210054e2ac45890),
[ifc4.ifcaxis2placement3d.refdiris3d()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#a2249e08fb14d97b33009f9638979ba10),
[ifc4.ifcfillareastylehatching.refhatchline2d()](../../d3/d40/classifc4_1_1ifcfillareastylehatching.html#a775eb971d46de59a558c12d4cbf073d2),
[automotive_design.axis2_placement_3d.wr2()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a53e4146e50cdc12f6f425f5ae2a015e7),
[config_control_design.axis2_placement_3d.wr2()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8510a502b056a9261c4b9cf7323f51b4),
[ifc2x3.ifcaxis2placement3d.wr2()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#aab8fcc584ec7c8fa06ffd345c95b8663),
[ifc2x3.ifcfillareastylehatching.wr23()](../../da/d61/classifc2x3_1_1ifcfillareastylehatching.html#a8a321538b336a12f4d031b3c01cb3784),
[automotive_design.axis2_placement_3d.wr3()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#aef9f7d5b239a07bf44a95014ce73b61d),
[config_control_design.axis2_placement_3d.wr3()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#aea36ab2e3de9512bb5d028dfeaea109b),
[ifc2x3.ifcaxis2placement3d.wr3()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#a6df2d82e8ad19735331147ae1689c8be),
and
[ifc2x3.ifccartesiantransformationoperator3d.wr4()](../../de/d03/classifc2x3_1_1ifccartesiantransformationoperator3d.html#a68b1818b4a81ee6941337c29f3f4d8d7).

## ◆ dummy_gri

config_control_design.axis1_placement.dummy_gri  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

