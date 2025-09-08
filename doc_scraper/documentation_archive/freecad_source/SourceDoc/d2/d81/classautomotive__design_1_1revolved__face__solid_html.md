---
url: https://freecad.github.io/SourceDoc/d2/d81/classautomotive__design_1_1revolved__face__solid.html
scraped_at: 2025-09-08T15:12:00.764951
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [revolved_face_solid](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html)

[List of all members](../../d1/dc4/classautomotive__design_1_1revolved__face__solid-members.html) | Public Member Functions | Public Attributes

automotive_design.revolved_face_solid Class Reference

##  Public Member Functions  
  
---  
def | [angle](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a2051423cdf1fb355d182bc1816af20a9) ()  
def | [axis](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#aa3d239994a9b90da8f91b251f80ea15e) ()  
def | [axis_line](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a88ba8cae1c9e693beda33bf96a0423ca) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.swept_face_solid](../../d1/d64/classautomotive__design_1_1swept__face__solid.html)  
def | [swept_face](../../d1/d64/classautomotive__design_1_1swept__face__solid.html#aa66713ac491c44290176d613289d2872) ()  
def | [wr1](../../d1/d64/classautomotive__design_1_1swept__face__solid.html#a6ba90dcc401b0d407dd0ba8128a71e4f) (self)  
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
[angle](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#afb7c4b95c7a38470ef8f3e03ad2fdd2a)  
|
[axis](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a15252a12f28f2819969c4600b7bdac50)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.swept_face_solid](../../d1/d64/classautomotive__design_1_1swept__face__solid.html)  
|
[swept_face](../../d1/d64/classautomotive__design_1_1swept__face__solid.html#ae3ab19b94fa38ab7330d319128a88152)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity revolved_face_solid definition.
    
        :param axis
        :type axis:axis1_placement
    
        :param angle
        :type angle:plane_angle_measure
    
        :param axis_line
        :type axis_line:line

## Member Function Documentation

## ◆ angle()

def automotive_design.revolved_face_solid.angle  | ( | | ) |   
---|---|---|---|---  
  
References Base::Rotation._angle,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.revolved_area_solid._angle,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.polar_complex_number_literal._angle,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.runout_zone_orientation._angle,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.revolved_face_solid._angle,
automotive_design.revolved_area_solid._angle,
automotive_design.runout_zone_orientation._angle,
automotive_design.revolved_face_solid._angle,
ifc2x3.ifcrevolvedareasolid._angle, and ifc4.ifcrevolvedareasolid._angle.

Referenced by
[drafttaskpanels.task_polararray.TaskPanelPolarArray.accept()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a06d6d931e4259dbe2214c68fea65bbe2),
[PathScripts.PathDressupDogbone.Bone.adaptiveLength()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#adde010e67251dab408b4c9737e25f0f8),
[draftguitools.gui_rotate.Rotate.build_copy_subelements_command()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a86c65f9a4f091a33d4476b26d5b5eaa2),
[draftguitools.gui_rotate.Rotate.build_rotate_subelements_command()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a62bb9191db4528d134ccb5aff0a52bf0),
[DraftGui.DraftToolBar.changeAngleValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ae8d4452f0bfbe152e17eacd89ff9043a),
[PathScripts.PathDressupDogbone.Bone.corner()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#a3020aa4704bbeca155e81158067a80d2),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.create_object()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a9bb3c55a3c2f34ab5d8a1f16b15c836d),
[PathScripts.PathDressupHoldingTags.Tag.createSolidsAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a2cb6cc02ae81caafbb137dfe20ebfdd8),
[PathScripts.PathDressupDogbone.Bone.distance()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#a118d2570fa29c8b6bda119a9e3ceb1e8),
[draftguitools.gui_arcs.Arc.drawArc()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a5abd3b89ce588c5761f8ecdbe95f73a5),
[PathScripts.PathDressupRampEntry.ObjectDressup.execute()](../../d4/d77/classPathScripts_1_1PathDressupRampEntry_1_1ObjectDressup.html#a6e5b12e06a02c6d2a2ec8116d7d751bd),
[PathScripts.PathDressupRampEntry.ObjectDressup.generateRamps()](../../d4/d77/classPathScripts_1_1PathDressupRampEntry_1_1ObjectDressup.html#a0f648732d60ede47ef6ed09e4ec10c42),
[PathScripts.PathArray.PathArray.getPath()](../../d1/d34/classPathScripts_1_1PathArray_1_1PathArray.html#acb90e897db610a16380ddd0dd5ae08bd),
[draftguitools.gui_arcs.Arc.numericRadius()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a3a55830e1e08f60be95ed81d73759e52),
[draftguitools.gui_rotate.Rotate.numericRadius()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a9233be8153158528af33797d19c7dffd),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.print_messages()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a42d45474bbe1d0dbee13ea60e251ac42),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[draftguitools.gui_rotate.Rotate.rotate_object()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#adfb7c1f87286e994cf85344a2614d2d0),
[DraftGui.DraftToolBar.toggleAngle()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a5776d8daaca23479b3afc5555ccdd3bb),
[DraftGui.DraftToolBar.update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[draftguitools.gui_arcs.Arc.updateAngle()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#ae2d984538453c4be92e31c39e162613c),
and
[drafttaskpanels.task_polararray.TaskPanelPolarArray.validate_input()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#ac504fbf48bb8962308c66cb053e3e89a).

## ◆ axis()

def automotive_design.revolved_face_solid.axis  | ( | | ) |   
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

## ◆ axis_line()

def automotive_design.revolved_face_solid.axis_line  | ( | | ) |   
---|---|---|---|---  
  
References
[PartDesignGui::Ui_TaskHelixParameters.axis](../../da/db2/classPartDesignGui_1_1Ui__TaskHelixParameters.html#affa56c163a413c40b9198abfb2a60e9c),
[PartDesignGui::Ui_TaskRevolutionParameters.axis](../../de/d09/classPartDesignGui_1_1Ui__TaskRevolutionParameters.html#ac41b7a0aa9d35808a430f314eb426281),
Base::CoordinateSystem.axis,
[drafttaskpanels.task_circulararray.TaskPanelCircularArray.axis](../../dd/d3a/classdrafttaskpanels_1_1task__circulararray_1_1TaskPanelCircularArray.html#a4d02d5145254fa88fa7e0e441bb83ffa),
[WorkingPlane.Plane.axis](../../d3/d93/classWorkingPlane_1_1Plane.html#a53226c4e4ca4bd022111e06043e8504f),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.axis1_placement.axis,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.revolved_area_solid.axis,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.revolved_face_solid.axis,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.axis2_placement_3d.axis,
[automotive_design.axis1_placement.axis](../../dd/d41/classautomotive__design_1_1axis1__placement.html#add6a92fbaa2fc74d2f925af5fcf7f3c5),
[automotive_design.revolved_area_solid.axis](../../d4/ded/classautomotive__design_1_1revolved__area__solid.html#a46ad9bb8fc843f62c4fab8506fa13560),
[automotive_design.axis2_placement_3d.axis](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#aeee6b3b4851869c95c1c1fc9850ba05f),
[automotive_design.revolved_face_solid.axis](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a15252a12f28f2819969c4600b7bdac50),
[config_control_design.axis1_placement.axis](../../d7/df7/classconfig__control__design_1_1axis1__placement.html#a425f406a2193625c2037a2e19c7fb961),
[config_control_design.axis2_placement_3d.axis](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#ae9a6bc489b2be75d49ffb4108a39b531),
[ifc2x3.ifcrevolvedareasolid.axis](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#abdf90da9cc48d2be2ce025e26d9ebeb7),
[ifc2x3.ifcaxis1placement.axis](../../df/db1/classifc2x3_1_1ifcaxis1placement.html#a169d678aebf4256ea2f7ff4e5f69bb34),
[ifc2x3.ifcaxis2placement3d.axis](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#a85b1f910b7aa716bf83996d10ca29c7d),
[ifc4.ifcrevolvedareasolid.axis](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a1a9fa2f9984e303e7c38275745340ae3),
[ifc4.ifcaxis1placement.axis](../../dd/ddf/classifc4_1_1ifcaxis1placement.html#a724b0637dac8a0e756d9430e8dfdf166),
[ifc4.ifcaxis2placement3d.axis](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#a3a4c2953e32114e635b36c7dbcb67a70),
[ifc4.ifcstructuralcurveconnection.axis](../../d2/d9b/classifc4_1_1ifcstructuralcurveconnection.html#a26449bc0123ee9a134febde984a6e309),
[ifc4.ifcstructuralcurvemember.axis](../../d9/d60/classifc4_1_1ifcstructuralcurvemember.html#a0ab1912155c4d729b2a9dafc7be052cb),
MeshCore::CylinderSurfaceFit.axis, KDL::Joint.axis,
[App::Meta::Url.location](../../d7/de5/structApp_1_1Meta_1_1Url.html#aa40afabdf8d53cdd4f29dd5594effeda),
[draftguitools.gui_circulararray.CircularArray.location](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#a0884f374b9ab70c333fafb73816b12e1),
[draftguitools.gui_polararray.PolarArray.location](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#a55e120c5eacdc1d6a9ffc2ee868b97a5),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.placement.location,
[automotive_design.placement.location](../../d8/d8c/classautomotive__design_1_1placement.html#aade15ec8d9163d4f50f6ebd55bf9e306),
[config_control_design.placement.location](../../da/d34/classconfig__control__design_1_1placement.html#a82d8e902f6a2bbfa6de928032d40bd1d),
[ifc2x3.ifcexternalreference.location](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#a7a533b0d9fdb23c15223ab3ebc86d066),
[ifc2x3.ifcplacement.location](../../dd/dfd/classifc2x3_1_1ifcplacement.html#ab0f26a3cde0ba583e2d87ec02900e82c),
[ifc4.ifcexternalreference.location](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a25390cf1c6b26090737c9d27429454f0),
[ifc4.ifcplacement.location](../../d4/da3/classifc4_1_1ifcplacement.html#ade56cca150b4b11e254d432caa231454),
[ifc4.ifcdocumentinformation.location](../../da/dbf/classifc4_1_1ifcdocumentinformation.html#af5b9773ffd2c248cbf06821180c75fce),
[ifc4.ifcclassification.location](../../db/d11/classifc4_1_1ifcclassification.html#a600169c34a2d9021964df0780fd070b4),
[ifc4.ifclibraryinformation.location](../../d9/d68/classifc4_1_1ifclibraryinformation.html#ab3c13281ded938f6115df119255d0005),
PartGui::TaskPrimitives.location, PartGui::TaskPrimitivesEdit.location,
[PathScripts.PathDressupDogbone.Bone.location()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#a0810be25de1e0e54c88c3e39cc787d06),
[e57::Translation.z](../../de/d18/structe57_1_1Translation.html#a9445e1de70a2b4414fc5afdb8b5549d0),
[e57::Quaternion.z](../../d9/da9/structe57_1_1Quaternion.html#a0f203d24b9c9dfc9c2112daf41301ca3),
[R3.z](../../d4/d0e/classR3.html#afda83a4e3cf0442476aad4dc44a8eda2),
[Multitype.z](../../db/df2/unionMultitype.html#aa031f83e1db7e8f751458cebe7b9d897),
XYZ.z,
[Base::DualQuat.z](../../d4/d13/classBase_1_1DualQuat.html#a2299a66bb636cd1ec8f243e00ea97015),
[Base::Vector3< double
>.z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da),
[Base::Vector3< float
>.z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da),
[Base::Vector3< _Precision
>.z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da),
[Gui::PropertyEditor::PropertyVectorItem.z](../../dc/d86/classGui_1_1PropertyEditor_1_1PropertyVectorItem.html#ab8a9241764da877209aaa36696338a17),
[Gui::PropertyEditor::PropertyVectorDistanceItem.z](../../db/dd4/classGui_1_1PropertyEditor_1_1PropertyVectorDistanceItem.html#aef25ba0c263dc6ced80ebdadeaf6dab4),
[Gui::SelectionChanges.z](../../d5/d50/classGui_1_1SelectionChanges.html#a73c5fd0103bbbc388762557e06796a10),
[Gui::SelectionSingleton::SelObj.z](../../d3/ddf/structGui_1_1SelectionSingleton_1_1SelObj.html#a1b506759c2b744396c5e8c2fb33133b6),
Gui::SelectionSingleton::_SelObj.z, Gui::DockWnd::SelectionView.z,
[importSH3D.SH3DHandler.z](../../d8/de6/classimportSH3D_1_1SH3DHandler.html#aa31e8c79dbd7c6258a08a2c14fbeceba),
[DraftGui.DraftToolBar.z](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ac76e8ed6c241bb3330b126dade09e950),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.axis1_placement.z(),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_angular_wedge.z,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.block.z,
[automotive_design.axis1_placement.z()](../../dd/d41/classautomotive__design_1_1axis1__placement.html#a0728a3baec495fbfb93954e7a8350658),
[automotive_design.right_angular_wedge.z](../../d4/df4/classautomotive__design_1_1right__angular__wedge.html#a5782b3772f1d57274d8ac89134b05378),
[automotive_design.block.z](../../d5/da2/classautomotive__design_1_1block.html#aa13f6909f4db29e3f4b558377285c2e2),
[config_control_design.axis1_placement.z()](../../d7/df7/classconfig__control__design_1_1axis1__placement.html#a2e286d9765dffb9a06686a29f273b3be),
[point3D.z](../../d4/d7b/structpoint3D.html#ae7370c9a05b6fb32d54c2b37a8b87d91),
[ifc2x3.ifcaxis1placement.z()](../../df/db1/classifc2x3_1_1ifcaxis1placement.html#a67f5cce20ad3eed02520d3db096a7cb2),
[ifc4.ifcaxis1placement.z()](../../dd/ddf/classifc4_1_1ifcaxis1placement.html#a11c43803bb9668bb02a978b8e2f60d22),
[MeshCore::MeshFastBuilder::Private::Vertex.z](../../de/d72/structMeshFastBuilder_1_1Private_1_1Vertex.html#afb7fbc6fc5ca843afdf5332b2ad89d6d),
MeshCore::MeshGridIterator::GridElement.z,
[MeshCore::NODE.z](../../d1/d49/structMeshCore_1_1NODE.html#aa20b952a1f25e07a738a00c48be97a7b),
[MeshPart::Vertex.z](../../db/d6a/structMeshPart_1_1Vertex.html#a36d6a2865faefc22aace974717ded766),
MeshPartGui::MeshCrossSection.z,
[Part::MeshVertex.z](../../d5/d5f/structPart_1_1MeshVertex.html#a4deafd4854178511879d10f2cb36f25d),
[PartGui::DimSelections::DimSelection.z](../../d1/d15/structPartGui_1_1DimSelections_1_1DimSelection.html#a394ea94b98840717954a922220ae9624),
[Mod.PartDesign.Scripts.FilletArc.Vector.z](../../dd/d11/classMod_1_1PartDesign_1_1Scripts_1_1FilletArc_1_1Vector.html#a78547896dd50c7a79dafebb62295468e),
[rotation_generator.refAxis.z](../../d6/d29/classrotation__generator_1_1refAxis.html#adf1630890e1b4e04a7d67c74b4fb18f1),
[geoff_geometry::Point3d.z](../../d0/ddc/classgeoff__geometry_1_1Point3d.html#ac5f155c60f62e1fe3ff64d0998e07ada),
[PathScripts.PathDressupHoldingTags.Tag.z](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a080b6f3741f1771a227b810d05ca5be2),
[PathScripts.PathDressupTag.TagSolid.z](../../d2/dc0/classPathScripts_1_1PathDressupTag_1_1TagSolid.html#a344dfd1f36a6bd9100d819b6dbe02d47),
[Point3D.z](../../d5/d01/structPoint3D.html#a6e72b27633aeb7ed2e6f4b98da554b39),
Points::PointsGridIterator::GridElement.z, KDL::Vector.z(), and
[Param.z](../../da/da2/structParam.html#a5f25c71f9cbf36ac46357c743e1ca968).

## Member Data Documentation

## ◆ angle

automotive_design.revolved_face_solid.angle  
---  
  
Referenced by
[drafttaskpanels.task_polararray.TaskPanelPolarArray.accept()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a06d6d931e4259dbe2214c68fea65bbe2),
[PathScripts.PathDressupDogbone.Bone.adaptiveLength()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#adde010e67251dab408b4c9737e25f0f8),
[draftguitools.gui_rotate.Rotate.build_copy_subelements_command()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a86c65f9a4f091a33d4476b26d5b5eaa2),
[draftguitools.gui_rotate.Rotate.build_rotate_subelements_command()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a62bb9191db4528d134ccb5aff0a52bf0),
[DraftGui.DraftToolBar.changeAngleValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ae8d4452f0bfbe152e17eacd89ff9043a),
[PathScripts.PathDressupDogbone.Bone.corner()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#a3020aa4704bbeca155e81158067a80d2),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.create_object()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a9bb3c55a3c2f34ab5d8a1f16b15c836d),
[PathScripts.PathDressupHoldingTags.Tag.createSolidsAt()](../../d1/d3b/classPathScripts_1_1PathDressupHoldingTags_1_1Tag.html#a2cb6cc02ae81caafbb137dfe20ebfdd8),
[PathScripts.PathDressupDogbone.Bone.distance()](../../d6/d5c/classPathScripts_1_1PathDressupDogbone_1_1Bone.html#a118d2570fa29c8b6bda119a9e3ceb1e8),
[draftguitools.gui_arcs.Arc.drawArc()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a5abd3b89ce588c5761f8ecdbe95f73a5),
[PathScripts.PathDressupRampEntry.ObjectDressup.execute()](../../d4/d77/classPathScripts_1_1PathDressupRampEntry_1_1ObjectDressup.html#a6e5b12e06a02c6d2a2ec8116d7d751bd),
[PathScripts.PathDressupRampEntry.ObjectDressup.generateRamps()](../../d4/d77/classPathScripts_1_1PathDressupRampEntry_1_1ObjectDressup.html#a0f648732d60ede47ef6ed09e4ec10c42),
[PathScripts.PathArray.PathArray.getPath()](../../d1/d34/classPathScripts_1_1PathArray_1_1PathArray.html#acb90e897db610a16380ddd0dd5ae08bd),
[draftguitools.gui_arcs.Arc.numericRadius()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#a3a55830e1e08f60be95ed81d73759e52),
[draftguitools.gui_rotate.Rotate.numericRadius()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#a9233be8153158528af33797d19c7dffd),
[drafttaskpanels.task_polararray.TaskPanelPolarArray.print_messages()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#a42d45474bbe1d0dbee13ea60e251ac42),
[DraftGui.DraftToolBar.reset_ui_values()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a11a4795405a81e99d4ef83da82a65b9e),
[draftguitools.gui_rotate.Rotate.rotate_object()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#adfb7c1f87286e994cf85344a2614d2d0),
[DraftGui.DraftToolBar.toggleAngle()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a5776d8daaca23479b3afc5555ccdd3bb),
[DraftGui.DraftToolBar.update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0),
[draftguitools.gui_arcs.Arc.updateAngle()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#ae2d984538453c4be92e31c39e162613c),
and
[drafttaskpanels.task_polararray.TaskPanelPolarArray.validate_input()](../../d7/d8d/classdrafttaskpanels_1_1task__polararray_1_1TaskPanelPolarArray.html#ac504fbf48bb8962308c66cb053e3e89a).

## ◆ axis

automotive_design.revolved_face_solid.axis  
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

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

