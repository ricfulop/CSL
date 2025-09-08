---
url: https://developer.rhino3d.com/guides/opennurbs/traverse-instance-definitions/
scraped_at: 2025-09-08T15:38:17.266363
title: Untitled
---

[RhinoDeveloper®](/)

[design, model, present, analyze, realize...](/)

[![Rhino Logo](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account
](https://www.rhino3d.com/my-account/ "Manage your account, licenses, and
teams")

[Traversing Instance
Definitions](https://developer.rhino3d.com/guides/opennurbs/traverse-instance-
definitions/)

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Traversing Instance Definitions

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

If you are developing software to read .3dm files, you might also read
instance, or block, definitions, in addition to standard geometry.

Instances are named groups of objects that act as a single object in your
model. They are useful for repeated objects such as symbols or components.
Instances save you time since you can reuse the components instead of re-
drawing them each time. An advantage of using instances for repeated content
is that using instances requires less memory.

The definition of a instance object is represented by the
`ON_InstanceDefinition` class. An instance definition object maintains list of
object ids.

An `ON_InstanceRef` is a reference to an instance definition, long with
transformation to apply to the definition.

If you are referencing the `Example_read` sample included with the openNURBS
toolkit, then after the 3DM file has been read, you can traverse a model’s
instance references as follows:

    
    
    ONX_Model model = ...
    
    ON_wString writer;
    ON_TextLog dump(writer);
    dump.SetIndentSize(2);
    
    ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::InstanceDefinition);
    const ON_ModelComponent* model_component = nullptr;
    for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
    {
      const ON_InstanceDefinition* idef = ON_InstanceDefinition::Cast(model_component);
      if (nullptr != idef)
        DumpInstanceDefinition(model, idef->Id(), dump, true);
    }
    
    wprintf(static_cast<const wchar_t*>(writer));
    

In this example, `DumpInstanceDefinition` is a recursive function, as it is
possible to construct instance references whose definition geometry contains
one or more instance references.

    
    
    static void DumpInstanceDefinition(ONX_Model& model, const ON_UUID& idef_id, ON_TextLog& dump, bool bRoot)
    {
      const ON_ModelComponentReference& idef_component_ref = model.ComponentFromId(ON_ModelComponent::Type::InstanceDefinition, idef_id);
      const ON_InstanceDefinition* idef = ON_InstanceDefinition::Cast(idef_component_ref.ModelComponent());
      if (idef)
      {
        dump.Print(L"Instance definition %d = %s\n", idef->Index(), static_cast<const wchar_t*>(idef->Name()));
    
        const ON_SimpleArray<ON_UUID>& geometry_id_list = idef->InstanceGeometryIdList();
        const int geometry_id_count = geometry_id_list.Count();
        if (geometry_id_count > 0)
        {
          dump.PushIndent();
          for (int i = 0; i < geometry_id_count; i++)
          {
            const ON_ModelComponentReference& model_component_ref = model.ComponentFromId(ON_ModelComponent::Type::ModelGeometry, geometry_id_list[i]);
            const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component_ref.ModelComponent());
            if (nullptr != model_geometry)
            {
              const ON_Geometry* geometry = model_geometry->Geometry(nullptr);
              if (nullptr != geometry)
              {
                const ON_InstanceRef* iref = ON_InstanceRef::Cast(geometry);
                if (iref)
                {
                  DumpInstanceDefinition(model, iref->m_instance_definition_uuid, dump, false);
                }
                else
                {
                  ON_wString type = ObjectTypeToString(geometry->ObjectType());
                  dump.Print(L"Object %d = %s\n", i, static_cast<const wchar_t*>(type));
                }
              }
            }
          }
          dump.PopIndent();
        }
      }
    }
    
    static ON_wString ObjectTypeToString(ON::object_type type)
    {
      ON_wString rc = L"Unknown";
      switch (type)
      {
      case ON::object_type::point_object: rc = L"point"; break;
      case ON::pointset_object: rc = L"pointset"; break;
      case ON::curve_object: rc = L"curve"; break;
      case ON::surface_object: rc = L"surface"; break;
      case ON::brep_object: rc = L"brep"; break;
      case ON::mesh_object: rc = L"mesh"; break;
      case ON::layer_object: rc = L"layer"; break;
      case ON::material_object: rc = L"material"; break;
      case ON::light_object: rc = L"light"; break;
      case ON::annotation_object: rc = L"annotation"; break;
      case ON::userdata_object: rc = L"userdata"; break;
      case ON::instance_definition: rc = L"instance_definition"; break;
      case ON::instance_reference: rc = L"instance_reference"; break;
      case ON::text_dot: rc = L"text_dot"; break;
      case ON::grip_object: rc = L"grip"; break;
      case ON::detail_object: rc = L"detail"; break;
      case ON::hatch_object: rc = L"hatch"; break;
      case ON::morph_control_object: rc = L"morph_control"; break;
      case ON::subd_object: rc = L"subd"; break;
      case ON::cage_object: rc = L"cage"; break;
      case ON::phantom_object: rc = L"phantom"; break;
      case ON::clipplane_object: rc = L"clipplane"; break;
      case ON::extrusion_object: rc = L"extrusion"; break;
      }
      return rc;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/traverse-
instance-definitions/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/traverse-
instance-definitions/index.md) [ Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2025 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/user/RhinoGuide/videos) [](https://vimeo.com/rhino)
[![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

