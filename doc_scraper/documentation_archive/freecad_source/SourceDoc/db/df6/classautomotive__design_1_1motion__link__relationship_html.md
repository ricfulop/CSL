---
url: https://freecad.github.io/SourceDoc/db/df6/classautomotive__design_1_1motion__link__relationship.html
scraped_at: 2025-09-08T15:08:14.819604
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [motion_link_relationship](../../db/df6/classautomotive__design_1_1motion__link__relationship.html)

[List of all members](../../d8/d9b/classautomotive__design_1_1motion__link__relationship-members.html) | Public Member Functions | Public Attributes

automotive_design.motion_link_relationship Class Reference

##  Public Member Functions  
  
---  
def | [frame_link](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#aee5bcae927e86b7c17aa3a8ed7812901) ()  
def | [motion](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a388e43040d3583b4c7bd44e3aa5823ca) ()  
def | [related_frame](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#af06a33b2dc4e00dc3cf94ee799dcd9de) ()  
def | [representation_relationship_rep_1](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#afd7c9abef7269c350a7d7c7778240783) ()  
def | [representation_relationship_rep_2](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a7f5fae6b969342488697e890ec7b0967) ()  
def | [wr1](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a2a143a9c64a2508fbd7e804fc705c05a) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_relationship](../../d3/d47/classautomotive__design_1_1representation__relationship.html)  
def | [description](../../d3/d47/classautomotive__design_1_1representation__relationship.html#ad19763c0b195fdb86036c42f815fc0ec) ()  
def | [name](../../d3/d47/classautomotive__design_1_1representation__relationship.html#a0848115085605d8443d2871fc116dbd3) ()  
def | [rep_1](../../d3/d47/classautomotive__design_1_1representation__relationship.html#a3402a69089802fc9240c57346490ec4c) ()  
def | [rep_2](../../d3/d47/classautomotive__design_1_1representation__relationship.html#a7e0c4a8b1b3ed0b4a18dc04121eec47c) ()  
  
##  Public Attributes  
  
---  
|
[related_frame](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a09678bccf9e97c036301cd0b33a14e34)  
|
[representation_relationship_rep_1](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a47c19bd12c28bc79de33888194efa2e5)  
|
[representation_relationship_rep_2](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#ae39b5fa8fe83af53bbec3e7384a5317e)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_relationship](../../d3/d47/classautomotive__design_1_1representation__relationship.html)  
|
[description](../../d3/d47/classautomotive__design_1_1representation__relationship.html#a06f918f5bc436973cf2d5bb094436599)  
|
[name](../../d3/d47/classautomotive__design_1_1representation__relationship.html#ad596c73def5a04e3f9c16b475a61e3d9)  
|
[rep_1](../../d3/d47/classautomotive__design_1_1representation__relationship.html#a48aeeda7c357a7c5d27dfd5c728a4cc6)  
|
[rep_2](../../d3/d47/classautomotive__design_1_1representation__relationship.html#af36f53abfdcf74f240b09c7eef35d6ec)  
  
## Detailed Description

    
    
    Entity motion_link_relationship definition.
    
        :param representation_relationship_rep_1
        :type representation_relationship_rep_1:founded_kinematic_path
    
        :param representation_relationship_rep_2
        :type representation_relationship_rep_2:kinematic_link_representation
    
        :param related_frame
        :type related_frame:rigid_placement
    
        :param motion
        :type motion:founded_kinematic_path
    
        :param frame_link
        :type frame_link:kinematic_link_representation

## Member Function Documentation

## ◆ frame_link()

def automotive_design.motion_link_relationship.frame_link  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.motion_link_relationship.wr1()](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a2a143a9c64a2508fbd7e804fc705c05a).

## ◆ motion()

def automotive_design.motion_link_relationship.motion  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ related_frame()

def automotive_design.motion_link_relationship.related_frame  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.motion_link_relationship._related_frame, and
[automotive_design.rigid_placement](../../d4/ddf/namespaceautomotive__design.html#a309c1228c838496124ec2d4eb2d48f81).

Referenced by
[automotive_design.motion_link_relationship.wr1()](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a2a143a9c64a2508fbd7e804fc705c05a).

## ◆ representation_relationship_rep_1()

def automotive_design.motion_link_relationship.representation_relationship_rep_1  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.explicit_procedural_representation_relationship._representation_relationship_rep_1,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.explicit_procedural_shape_representation_relationship._representation_relationship_rep_1,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.mechanical_design_and_draughting_relationship._representation_relationship_rep_1,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.constructive_geometry_representation_relationship._representation_relationship_rep_1,
automotive_design.motion_link_relationship._representation_relationship_rep_1,
and
automotive_design.kinematic_link_representation_association._representation_relationship_rep_1.

## ◆ representation_relationship_rep_2()

def automotive_design.motion_link_relationship.representation_relationship_rep_2  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.explicit_procedural_shape_representation_relationship._representation_relationship_rep_2,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.mechanical_design_and_draughting_relationship._representation_relationship_rep_2,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.constructive_geometry_representation_relationship._representation_relationship_rep_2,
and
automotive_design.motion_link_relationship._representation_relationship_rep_2.

## ◆ wr1()

def automotive_design.motion_link_relationship.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.motion_link_relationship.frame_link()](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#aee5bcae927e86b7c17aa3a8ed7812901),
Py::MapBase< T >.items(),
[Gui::ElementColors::Private.items](../../d8/dc9/classElementColors_1_1Private.html#ac06b624b9c4165c0a6fc90aa8b319181),
[Gui::DocumentObjectData.items](../../d6/d82/classGui_1_1DocumentObjectData.html#a8848f66de88d9073d4a2abfd0677848d),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_document_usage_constraint_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_action_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_certification_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.representation.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_organization_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_action_method_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_date_and_time_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_attribute_classification_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.assigned_requirement.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_external_identification_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_event_occurrence_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.configured_effectivity_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.cc_design_person_and_organization_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_date_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.draughting_title.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_presented_item.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.change_request.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.instance_usage_context_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.document_identifier_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_action_request_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_group_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.breakdown_element_group_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.sourced_requirement.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_contract_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.requirement_assigned_object.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_classification_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.satisfying_item.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.product_definition_group_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_identification_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.start_request.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.cc_design_specification_reference.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_time_interval_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_organizational_project_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.change.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.source_for_requirement.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_approval_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_document_reference.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.configured_effectivity_context_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.product_concept_feature_category_usage.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.start_work.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.cc_design_approval.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.attribute_language_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.cc_design_contract.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.multi_language_attribute_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.cc_design_certification.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.class_usage_effectivity_context_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_effectivity_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.rule_superseded_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_security_classification_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.cc_design_security_classification.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.cc_design_date_and_time_assignment.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.satisfied_requirement.items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_person_and_organization_assignment.items,
[automotive_design.applied_certification_assignment.items](../../dd/d45/classautomotive__design_1_1applied__certification__assignment.html#afc07867189a9b5a985cfad25f07c5fa0),
[automotive_design.representation.items](../../d8/de0/classautomotive__design_1_1representation.html#aa8058fe959724be16897e4409e870128),
[automotive_design.applied_organization_assignment.items](../../dc/dbe/classautomotive__design_1_1applied__organization__assignment.html#a38b623dac08b52734a848acb4a368220),
[automotive_design.applied_date_and_time_assignment.items](../../d7/d48/classautomotive__design_1_1applied__date__and__time__assignment.html#a3683b15731cd5df5f12e9107f244876e),
[automotive_design.applied_external_identification_assignment.items](../../df/d97/classautomotive__design_1_1applied__external__identification__assignment.html#a3bfe720c46b0a03acbf09b737bcb1639),
[automotive_design.applied_event_occurrence_assignment.items](../../dc/d23/classautomotive__design_1_1applied__event__occurrence__assignment.html#a673b0e0ff0c4b9de832cf6788c37805a),
[automotive_design.configured_effectivity_assignment.items](../../d2/db6/classautomotive__design_1_1configured__effectivity__assignment.html#a0c01e15e0f456c393e26f53b5e76f08d),
[automotive_design.language_assignment.items](../../db/d85/classautomotive__design_1_1language__assignment.html#ac4272f2a7c71fd8116e8f6c875f41669),
[automotive_design.applied_date_assignment.items](../../df/d17/classautomotive__design_1_1applied__date__assignment.html#a470d84841318997be18a20e5e5baa187),
[automotive_design.draughting_title.items](../../d0/db5/classautomotive__design_1_1draughting__title.html#af4c215d612efced643cb1dc3370fd214),
[automotive_design.applied_presented_item.items](../../dc/d81/classautomotive__design_1_1applied__presented__item.html#a1ea4364ba92a6fc0e03a5f06c7efccd4),
[automotive_design.applied_action_request_assignment.items](../../dd/dc6/classautomotive__design_1_1applied__action__request__assignment.html#a698868336b177caf3017e5a10722190c),
[automotive_design.applied_group_assignment.items](../../d5/d50/classautomotive__design_1_1applied__group__assignment.html#a590195eba87185a05df0e60a7f3f3b22),
[automotive_design.applied_contract_assignment.items](../../dd/dc6/classautomotive__design_1_1applied__contract__assignment.html#acd7694777ebed2989edf19dd3e69037e),
[automotive_design.applied_classification_assignment.items](../../d6/dce/classautomotive__design_1_1applied__classification__assignment.html#afbc41c1116be738577157bf7860bc09a),
[automotive_design.applied_identification_assignment.items](../../df/dcd/classautomotive__design_1_1applied__identification__assignment.html#ace8826c142018b84e9d8da903829eacc),
[automotive_design.applied_time_interval_assignment.items](../../d8/d45/classautomotive__design_1_1applied__time__interval__assignment.html#a7cf9cf0865d54da5140684f248eabd25),
[automotive_design.applied_ineffectivity_assignment.items](../../d8/d1d/classautomotive__design_1_1applied__ineffectivity__assignment.html#a8625f8fc3a2838ce931204c12626c2c8),
[automotive_design.applied_organizational_project_assignment.items](../../dd/dfe/classautomotive__design_1_1applied__organizational__project__assignment.html#ac083c8f5ae5088516bbd8dd2407a09e2),
[automotive_design.applied_approval_assignment.items](../../d1/d8c/classautomotive__design_1_1applied__approval__assignment.html#a4cdf62612b9f9acb14e4167c253bca3d),
[automotive_design.applied_document_reference.items](../../d4/ddf/classautomotive__design_1_1applied__document__reference.html#a398f76353c1141393432cb1d14ab99a3),
[automotive_design.applied_name_assignment.items](../../d5/d73/classautomotive__design_1_1applied__name__assignment.html#a0a1f9f5f74d1874a3ee959c48dfbfa63),
[automotive_design.configured_effectivity_context_assignment.items](../../db/d57/classautomotive__design_1_1configured__effectivity__context__assignment.html#ad1a57c6c7092d35808ee9b1be9ac336e),
[automotive_design.product_concept_feature_category_usage.items](../../d3/d64/classautomotive__design_1_1product__concept__feature__category__usage.html#a8468fd5c9569d19f8bc7705494cec85f),
[automotive_design.attribute_language_assignment.items](../../d4/d38/classautomotive__design_1_1attribute__language__assignment.html#a5eaa9ec7178e95ec6ad72c472d7bfd09),
[automotive_design.multi_language_attribute_assignment.items](../../d8/d96/classautomotive__design_1_1multi__language__attribute__assignment.html#ae4faa367d7248e9e67dcae5ede8b1641),
[automotive_design.class_usage_effectivity_context_assignment.items](../../d2/de0/classautomotive__design_1_1class__usage__effectivity__context__assignment.html#a497f11ddf97b1e9ead750c0be2900f58),
[automotive_design.applied_effectivity_assignment.items](../../d0/d27/classautomotive__design_1_1applied__effectivity__assignment.html#a49fce97029da4d8bdab097accdca0197),
[automotive_design.applied_action_assignment.items](../../d8/d48/classautomotive__design_1_1applied__action__assignment.html#a1787a8d481bc5c5cdba3f40e57485d71),
[automotive_design.applied_security_classification_assignment.items](../../d4/d45/classautomotive__design_1_1applied__security__classification__assignment.html#a5aded10b9e9391f2e9f9c750ff760baf),
[automotive_design.applied_document_usage_constraint_assignment.items](../../d9/d45/classautomotive__design_1_1applied__document__usage__constraint__assignment.html#a5f2ed0c9627fc1ad08900038e670c596),
[automotive_design.applied_person_and_organization_assignment.items](../../dc/d2b/classautomotive__design_1_1applied__person__and__organization__assignment.html#a285786dbcf6a5a989812eb36bf70f952),
[config_control_design.representation.items](../../d4/d7a/classconfig__control__design_1_1representation.html#a5889d385cfc9fb2bc6209d9bd72f508e),
[config_control_design.cc_design_person_and_organization_assignment.items](../../d5/dd0/classconfig__control__design_1_1cc__design__person__and__organization__assignment.html#ad747daa2c000be5e6f4b1c28ecfdb4f1),
[config_control_design.change_request.items](../../d2/deb/classconfig__control__design_1_1change__request.html#aa3f028210ac33783717b05c371fab1e5),
[config_control_design.start_request.items](../../dc/d58/classconfig__control__design_1_1start__request.html#ac859408c32eb73b56020a761c565c84d),
[config_control_design.cc_design_specification_reference.items](../../db/df7/classconfig__control__design_1_1cc__design__specification__reference.html#aaa3dd2d787616ec2c5124d51826852ee),
[config_control_design.change.items](../../d5/da1/classconfig__control__design_1_1change.html#aa50230acb44b94c58b687d04db813faf),
[config_control_design.start_work.items](../../db/d53/classconfig__control__design_1_1start__work.html#a083c779f261d355e3312161926bd81b9),
[config_control_design.cc_design_approval.items](../../da/da7/classconfig__control__design_1_1cc__design__approval.html#ab0bad25523aecd6340904aa33e610b12),
[config_control_design.cc_design_contract.items](../../d3/da3/classconfig__control__design_1_1cc__design__contract.html#abeee4c10665d9ae80dcbd252f7a9bc61),
[config_control_design.cc_design_certification.items](../../de/dc3/classconfig__control__design_1_1cc__design__certification.html#ab4d616b3ca9333630451948ee0b3c7f0),
[config_control_design.cc_design_security_classification.items](../../d2/d55/classconfig__control__design_1_1cc__design__security__classification.html#a4cfbccfc11ae8116d7a4b517a6579b6a),
[config_control_design.cc_design_date_and_time_assignment.items](../../d6/d25/classconfig__control__design_1_1cc__design__date__and__time__assignment.html#a1a0c05092fb60e5c3f6e3d448a80b323),
[ifc2x3.ifcrepresentation.items](../../df/d50/classifc2x3_1_1ifcrepresentation.html#a8f3af20e58ebeeb74ea91a3b3365298d),
[ifc4.ifcrepresentation.items](../../d9/d6a/classifc4_1_1ifcrepresentation.html#a3633c0115d4adefebf15d983b39b1aca),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.items()](../../d9/dcc/classnlohmann_1_1basic__json.html#a02ed1d1f38310ccc2fbb02d2b75387a2),
ColorPickerPopup.items,
[automotive_design.motion_link_relationship.related_frame](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a09678bccf9e97c036301cd0b33a14e34),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.dimensional_characteristic_representation.representation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.action_property_representation.representation,
[automotive_design.resource_property_representation.representation](../../df/dd2/classautomotive__design_1_1resource__property__representation.html#aabf807f5a585e0dc65f6bde51a345193),
[automotive_design.dimensional_characteristic_representation.representation](../../d7/d06/classautomotive__design_1_1dimensional__characteristic__representation.html#aef8c6d21bfbb31e6ab5b842c3ebbfe8a),
[automotive_design.action_property_representation.representation](../../de/d37/classautomotive__design_1_1action__property__representation.html#a9838a5cf28e7f2839e5a3d33799dff8f),
[ifc2x3.ifcproduct.representation](../../d1/d19/classifc2x3_1_1ifcproduct.html#aad7175e7da72975e17051cf55140d82f),
[ifc4.ifcproduct.representation](../../d6/dab/classifc4_1_1ifcproduct.html#ac60a1507853e14d15199efeb5e03e31f),
and
[Mesh::MeshObject.representation()](../../d8/dcc/classMesh_1_1MeshObject.html#aa052a8f4b47816f1165132d577323aed).

## Member Data Documentation

## ◆ related_frame

automotive_design.motion_link_relationship.related_frame  
---  
  
Referenced by
[automotive_design.motion_link_relationship.wr1()](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a2a143a9c64a2508fbd7e804fc705c05a).

## ◆ representation_relationship_rep_1

automotive_design.motion_link_relationship.representation_relationship_rep_1  
---  
  
## ◆ representation_relationship_rep_2

automotive_design.motion_link_relationship.representation_relationship_rep_2  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

