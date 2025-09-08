---
url: https://docs.blender.org/api/current/bpy.types.Depsgraph.html
scraped_at: 2025-09-08T14:24:31.984282
title: Depsgraph(bpy_struct)¶
---

# Depsgraph(bpy_struct)¶  
  
## Dependency graph: Evaluated ID example¶

This example demonstrates access to the evaluated ID (such as object,
material, etc.) state from an original ID. This is needed every time one needs
to access state with animation, constraints, and modifiers taken into account.

    
    
    import bpy
    
    
    class OBJECT_OT_evaluated_example(bpy.types.Operator):
        """Access evaluated object state and do something with it"""
        bl_label = "DEG Access Evaluated Object"
        bl_idname = "object.evaluated_example"
    
        def execute(self, context):
            # This is an original object. Its data does not have any modifiers applied.
            obj = context.object
            if obj is None or obj.type != 'MESH':
                self.report({'INFO'}, "No active mesh object to get info from")
                return {'CANCELLED'}
            # Evaluated object exists within a specific dependency graph.
            # We will request evaluated object from the dependency graph which corresponds to the
            # current scene and view layer.
            #
            # NOTE: This call ensure the dependency graph is fully evaluated. This might be expensive
            # if changes were made to the scene, but is needed to ensure no dangling or incorrect
            # pointers are exposed.
            depsgraph = context.evaluated_depsgraph_get()
            # Actually request evaluated object.
            #
            # This object has animation and drivers applied on it, together with constraints and
            # modifiers.
            #
            # For mesh objects the object.data will be a mesh with all modifiers applied.
            # This means that in access to vertices or faces after modifier stack happens via fields of
            # object_eval.object.
            #
            # For other types of objects the object_eval.data does not have modifiers applied on it,
            # but has animation applied.
            #
            # NOTE: All ID types have `evaluated_get()`, including materials, node trees, worlds.
            object_eval = obj.evaluated_get(depsgraph)
            mesh_eval = object_eval.data
            self.report({'INFO'}, f"Number of evaluated vertices: {len(mesh_eval.vertices)}")
            return {'FINISHED'}
    
    
    def register():
        bpy.utils.register_class(OBJECT_OT_evaluated_example)
    
    
    def unregister():
        bpy.utils.unregister_class(OBJECT_OT_evaluated_example)
    
    
    if __name__ == "__main__":
        register()
    

## Dependency graph: Original object example¶

This example demonstrates access to the original ID. Such access is needed to
check whether object is selected, or to compare pointers.

    
    
    import bpy
    
    
    class OBJECT_OT_original_example(bpy.types.Operator):
        """Access original object and do something with it"""
        bl_label = "DEG Access Original Object"
        bl_idname = "object.original_example"
    
        def check_object_selected(self, object_eval):
            # Selection depends on a context and is only valid for original objects. This means we need
            # to request the original object from the known evaluated one.
            #
            # NOTE: All ID types have an `original` field.
            obj = object_eval.original
            return obj.select_get()
    
        def execute(self, context):
            # NOTE: It seems redundant to iterate over original objects to request evaluated ones
            # just to get original back. But we want to keep example as short as possible, but in real
            # world there are cases when evaluated object is coming from a more meaningful source.
            depsgraph = context.evaluated_depsgraph_get()
            for obj in context.editable_objects:
                object_eval = obj.evaluated_get(depsgraph)
                if self.check_object_selected(object_eval):
                    self.report({'INFO'}, f"Object is selected: {object_eval.name}")
            return {'FINISHED'}
    
    
    def register():
        bpy.utils.register_class(OBJECT_OT_original_example)
    
    
    def unregister():
        bpy.utils.unregister_class(OBJECT_OT_original_example)
    
    
    if __name__ == "__main__":
        register()
    

## Dependency graph: Iterate over all object instances¶

Sometimes it is needed to know all the instances with their matrices (for
example, when writing an exporter or a custom render engine). This example
shows how to access all objects and instances in the scene.

    
    
    import bpy
    
    
    class OBJECT_OT_object_instances(bpy.types.Operator):
        """Access original object and do something with it"""
        bl_label = "DEG Iterate Object Instances"
        bl_idname = "object.object_instances"
    
        def execute(self, context):
            depsgraph = context.evaluated_depsgraph_get()
            for object_instance in depsgraph.object_instances:
                # This is an object which is being instanced.
                obj = object_instance.object
                # `is_instance` denotes whether the object is coming from instances (as an opposite of
                # being an emitting object. )
                if not object_instance.is_instance:
                    print(f"Object {obj.name} at {object_instance.matrix_world}")
                else:
                    # Instanced will additionally have fields like uv, random_id and others which are
                    # specific for instances. See Python API for DepsgraphObjectInstance for details,
                    print(f"Instance of {obj.name} at {object_instance.matrix_world}")
            return {'FINISHED'}
    
    
    def register():
        bpy.utils.register_class(OBJECT_OT_object_instances)
    
    
    def unregister():
        bpy.utils.unregister_class(OBJECT_OT_object_instances)
    
    
    if __name__ == "__main__":
        register()
    

## Dependency graph: Object.to_mesh()¶

Function to get a mesh from any object with geometry. It is typically used by
exporters, render engines and tools that need to access the evaluated mesh as
displayed in the viewport.

Object.to_mesh() is closely interacting with dependency graph: its behavior
depends on whether it is used on original or evaluated object.

When is used on original object, the result mesh is calculated from the object
without taking animation or modifiers into account:

  * For meshes this is similar to duplicating the source mesh.

  * For curves this disables own modifiers, and modifiers of objects used as bevel and taper.

  * For meta-balls this produces an empty mesh since polygonization is done as a modifier evaluation.

When is used on evaluated object all modifiers are taken into account.

Note

The result mesh is owned by the object. It can be freed by calling
[`to_mesh_clear()`](bpy.types.Object.html#bpy.types.Object.to_mesh_clear
"bpy.types.Object.to_mesh_clear").

Note

The result mesh must be treated as temporary, and cannot be referenced from
objects in the main database. If the mesh intended to be used in a persistent
manner use
[`new_from_object()`](bpy.types.BlendDataMeshes.html#bpy.types.BlendDataMeshes.new_from_object
"bpy.types.BlendDataMeshes.new_from_object") instead.

Note

If object does not have geometry (i.e. camera) the functions returns None.

    
    
    import bpy
    
    
    class OBJECT_OT_object_to_mesh(bpy.types.Operator):
        """Convert selected object to mesh and show number of vertices"""
        bl_label = "DEG Object to Mesh"
        bl_idname = "object.object_to_mesh"
    
        def execute(self, context):
            # Access input original object.
            obj = context.object
            if obj is None:
                self.report({'INFO'}, "No active mesh object to convert to mesh")
                return {'CANCELLED'}
            # Avoid annoying None checks later on.
            if obj.type not in {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META'}:
                self.report({'INFO'}, "Object cannot be converted to mesh")
                return {'CANCELLED'}
            depsgraph = context.evaluated_depsgraph_get()
            # Invoke to_mesh() for original object.
            mesh_from_orig = obj.to_mesh()
            self.report({'INFO'}, f"{len(mesh_from_orig.vertices)} in new mesh without modifiers.")
            # Remove temporary mesh.
            obj.to_mesh_clear()
            # Invoke to_mesh() for evaluated object.
            object_eval = obj.evaluated_get(depsgraph)
            mesh_from_eval = object_eval.to_mesh()
            self.report({'INFO'}, f"{len(mesh_from_eval.vertices)} in new mesh with modifiers.")
            # Remove temporary mesh.
            object_eval.to_mesh_clear()
            return {'FINISHED'}
    
    
    def register():
        bpy.utils.register_class(OBJECT_OT_object_to_mesh)
    
    
    def unregister():
        bpy.utils.unregister_class(OBJECT_OT_object_to_mesh)
    
    
    if __name__ == "__main__":
        register()
    

## Dependency graph: bpy.data.meshes.new_from_object()¶

Function to copy a new mesh from any object with geometry. The mesh is added
to the main database and can be referenced by objects. Typically used by tools
that create new objects or apply modifiers.

When is used on original object, the result mesh is calculated from the object
without taking animation or modifiers into account:

  * For meshes this is similar to duplicating the source mesh.

  * For curves this disables own modifiers, and modifiers of objects used as bevel and taper.

  * For meta-balls this produces an empty mesh since polygonization is done as a modifier evaluation.

When is used on evaluated object all modifiers are taken into account.

All the references (such as materials) are re-mapped to original. This ensures
validity and consistency of the main database.

Note

If object does not have geometry (i.e. camera) the functions returns None.

    
    
    import bpy
    
    
    class OBJECT_OT_mesh_from_object(bpy.types.Operator):
        """Convert selected object to mesh and show number of vertices"""
        bl_label = "DEG Mesh From Object"
        bl_idname = "object.mesh_from_object"
    
        def execute(self, context):
            # Access input original object.
            obj = context.object
            if obj is None:
                self.report({'INFO'}, "No active mesh object to convert to mesh")
                return {'CANCELLED'}
            # Avoid annoying None checks later on.
            if obj.type not in {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META'}:
                self.report({'INFO'}, "Object cannot be converted to mesh")
                return {'CANCELLED'}
            depsgraph = context.evaluated_depsgraph_get()
            object_eval = obj.evaluated_get(depsgraph)
            mesh_from_eval = bpy.data.meshes.new_from_object(object_eval)
            self.report({'INFO'}, f"{len(mesh_from_eval.vertices)} in new mesh, and is ready for use!")
            return {'FINISHED'}
    
    
    def register():
        bpy.utils.register_class(OBJECT_OT_mesh_from_object)
    
    
    def unregister():
        bpy.utils.unregister_class(OBJECT_OT_mesh_from_object)
    
    
    if __name__ == "__main__":
        register()
    

## Dependency graph: Simple exporter¶

This example is a combination of all previous ones, and shows how to write a
simple exporter script.

    
    
    import bpy
    
    
    class OBJECT_OT_simple_exporter(bpy.types.Operator):
        """Simple (fake) exporter of selected objects"""
        bl_label = "DEG Export Selected"
        bl_idname = "object.simple_exporter"
    
        apply_modifiers: bpy.props.BoolProperty(name="Apply Modifiers")
    
        def execute(self, context):
            depsgraph = context.evaluated_depsgraph_get()
            for object_instance in depsgraph.object_instances:
                if not self.is_object_instance_from_selected(object_instance):
                    # We only export selected objects.
                    continue
                # NOTE: This will create a mesh for every instance, which is not ideal at all. In
                # reality destination format will support some sort of instancing mechanism, so the
                # code here will simply say "instance this object at object_instance.matrix_world".
                mesh = self.create_mesh_for_object_instance(object_instance)
                if mesh is None:
                    # Happens for non-geometry objects.
                    continue
                print(f"Exporting mesh with {len(mesh.vertices)} vertices "
                      f"at {object_instance.matrix_world}")
    
                self.clear_mesh_for_object_instance(object_instance)
    
            return {'FINISHED'}
    
        def is_object_instance_from_selected(self, object_instance):
            # For instanced objects we check selection of their instancer (more accurately: check
            # selection status of the original object corresponding to the instancer).
            if object_instance.parent:
                return object_instance.parent.original.select_get()
            # For non-instanced objects we check selection state of the original object.
            return object_instance.object.original.select_get()
    
        def create_mesh_for_object_instance(self, object_instance):
            if self.apply_modifiers:
                return object_instance.object.to_mesh()
            else:
                return object_instance.object.original.to_mesh()
    
        def clear_mesh_for_object_instance(self, object_instance):
            if self.apply_modifiers:
                return object_instance.object.to_mesh_clear()
            else:
                return object_instance.object.original.to_mesh_clear()
    
    
    def register():
        bpy.utils.register_class(OBJECT_OT_simple_exporter)
    
    
    def unregister():
        bpy.utils.unregister_class(OBJECT_OT_simple_exporter)
    
    
    if __name__ == "__main__":
        register()
    

## Dependency graph: Object.to_curve()¶

Function to get a curve from text and curve objects. It is typically used by
exporters, render engines, and tools that need to access the curve
representing the object.

The function takes the evaluated dependency graph as a required parameter and
optionally a boolean apply_modifiers which defaults to false. If
apply_modifiers is true and the object is a curve object, the spline deform
modifiers are applied on the control points. Note that constructive modifiers
and modifiers that are not spline-enabled will not be applied. So modifiers
like Array will not be applied and deform modifiers that have Apply On Spline
disabled will not be applied.

If the object is a text object. The text will be converted into a 3D curve and
returned. Modifiers are never applied on text objects and apply_modifiers will
be ignored. If the object is neither a curve nor a text object, an error will
be reported.

Note

The resulting curve is owned by the object. It can be freed by calling
[`to_curve_clear()`](bpy.types.Object.html#bpy.types.Object.to_curve_clear
"bpy.types.Object.to_curve_clear").

Note

The resulting curve must be treated as temporary, and cannot be referenced
from objects in the main database.

    
    
    import bpy
    
    
    class OBJECT_OT_object_to_curve(bpy.types.Operator):
        """Convert selected object to curve and show number of splines"""
        bl_label = "DEG Object to Curve"
        bl_idname = "object.object_to_curve"
    
        def execute(self, context):
            # Access input original object.
            obj = context.object
            if obj is None:
                self.report({'INFO'}, "No active object to convert to curve")
                return {'CANCELLED'}
            if obj.type not in {'CURVE', 'FONT'}:
                self.report({'INFO'}, "Object cannot be converted to curve")
                return {'CANCELLED'}
            depsgraph = context.evaluated_depsgraph_get()
            # Invoke to_curve() without applying modifiers.
            curve_without_modifiers = obj.to_curve(depsgraph)
            self.report({'INFO'}, f"{len(curve_without_modifiers.splines)} splines in a new curve without modifiers.")
            # Remove temporary curve.
            obj.to_curve_clear()
            # Invoke to_curve() with applying modifiers.
            curve_with_modifiers = obj.to_curve(depsgraph, apply_modifiers=True)
            self.report({'INFO'}, f"{len(curve_with_modifiers.splines)} splines in new curve with modifiers.")
            # Remove temporary curve.
            obj.to_curve_clear()
            return {'FINISHED'}
    
    
    def register():
        bpy.utils.register_class(OBJECT_OT_object_to_curve)
    
    
    def unregister():
        bpy.utils.unregister_class(OBJECT_OT_object_to_curve)
    
    
    if __name__ == "__main__":
        register()
    

base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.Depsgraph(_bpy_struct_)¶

    

ids¶

    

All evaluated data-blocks

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of [`ID`](bpy.types.ID.html#bpy.types.ID
"bpy.types.ID"), (readonly)

mode¶

    

Evaluation mode

  * `VIEWPORT` Viewport – Viewport non-rendered mode.

  * `RENDER` Render – Render.

Type:

    

enum in [`VIEWPORT`, `RENDER`], default `VIEWPORT`, (readonly)

object_instances¶

    

All object instances to display or render (Warning: Only use this as an
iterator, never as a sequence, and do not keep any references to its items)

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`DepsgraphObjectInstance`](bpy.types.DepsgraphObjectInstance.html#bpy.types.DepsgraphObjectInstance
"bpy.types.DepsgraphObjectInstance"), (readonly)

objects¶

    

Evaluated objects in the dependency graph

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object"),
(readonly)

scene¶

    

Original scene dependency graph is built for

Type:

    

[`Scene`](bpy.types.Scene.html#bpy.types.Scene "bpy.types.Scene"), (readonly)

scene_eval¶

    

Scene at its evaluated state

Type:

    

[`Scene`](bpy.types.Scene.html#bpy.types.Scene "bpy.types.Scene"), (readonly)

updates¶

    

Updates to data-blocks

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`DepsgraphUpdate`](bpy.types.DepsgraphUpdate.html#bpy.types.DepsgraphUpdate
"bpy.types.DepsgraphUpdate"), (readonly)

view_layer¶

    

Original view layer dependency graph is built for

Type:

    

[`ViewLayer`](bpy.types.ViewLayer.html#bpy.types.ViewLayer
"bpy.types.ViewLayer"), (readonly)

view_layer_eval¶

    

View layer at its evaluated state

Type:

    

[`ViewLayer`](bpy.types.ViewLayer.html#bpy.types.ViewLayer
"bpy.types.ViewLayer"), (readonly)

debug_relations_graphviz(_*_ , _filepath =''_)¶

    

debug_relations_graphviz

Parameters:

    

**filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Name,
Optional output path for the graphviz debug file

Returns:

    

Dot Graph, Graph in dot format

Return type:

    

string

debug_stats_gnuplot(_filepath_ , _output_filepath_)¶

    

debug_stats_gnuplot

Parameters:

    

  * **filepath** (_string_ _,__(__never None_ _)_) – File Name, Output path for the gnuplot debug file

  * **output_filepath** (_string_ _,__(__never None_ _)_) – Output File Name, File name where gnuplot script will save the result

debug_tag_update()¶

    

debug_tag_update

debug_stats()¶

    

Report the number of elements in the Dependency Graph

Returns:

    

result

Return type:

    

string, (never None)

update()¶

    

Re-evaluate any modified data-blocks, for example for animation or modifiers.
This invalidates all references to evaluated data-blocks from this dependency
graph.

id_eval_get(_id_)¶

    

id_eval_get

Parameters:

    

**id** ([`ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")) – Original ID
to get evaluated complementary part for

Returns:

    

Evaluated ID for the given original one

Return type:

    

[`ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")

id_type_updated(_id_type_)¶

    

id_type_updated

Parameters:

    

**id_type** (enum in [Id Type
Items](bpy_types_enum_items/id_type_items.html#rna-enum-id-type-items)) – ID
Type

Returns:

    

Updated, True if any datablock with this type was added, updated or removed

Return type:

    

boolean

_classmethod _bl_rna_get_subclass(_id_ , _default =None_, _/_)¶

    

Parameters:

    

**id** (_str_) – The RNA type identifier.

Returns:

    

The RNA type or default when not found.

Return type:

    

[`bpy.types.Struct`](bpy.types.Struct.html#bpy.types.Struct
"bpy.types.Struct") subclass

_classmethod _bl_rna_get_subclass_py(_id_ , _default =None_, _/_)¶

    

Parameters:

    

**id** (_str_) – The RNA type identifier.

Returns:

    

The class or default when not found.

Return type:

    

type

### Inherited Properties¶

  * [`bpy_struct.id_data`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_data "bpy.types.bpy_struct.id_data")

|

  
---|---  
  
### Inherited Functions¶

  * [`bpy_struct.as_pointer`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.as_pointer "bpy.types.bpy_struct.as_pointer")
  * [`bpy_struct.driver_add`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.driver_add "bpy.types.bpy_struct.driver_add")
  * [`bpy_struct.driver_remove`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.driver_remove "bpy.types.bpy_struct.driver_remove")
  * [`bpy_struct.get`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.get "bpy.types.bpy_struct.get")
  * [`bpy_struct.id_properties_clear`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_clear "bpy.types.bpy_struct.id_properties_clear")
  * [`bpy_struct.id_properties_ensure`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_ensure "bpy.types.bpy_struct.id_properties_ensure")
  * [`bpy_struct.id_properties_ui`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_properties_ui "bpy.types.bpy_struct.id_properties_ui")
  * [`bpy_struct.is_property_hidden`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_hidden "bpy.types.bpy_struct.is_property_hidden")
  * [`bpy_struct.is_property_overridable_library`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_overridable_library "bpy.types.bpy_struct.is_property_overridable_library")
  * [`bpy_struct.is_property_readonly`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_readonly "bpy.types.bpy_struct.is_property_readonly")
  * [`bpy_struct.is_property_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.is_property_set "bpy.types.bpy_struct.is_property_set")
  * [`bpy_struct.items`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.items "bpy.types.bpy_struct.items")

|

  * [`bpy_struct.keyframe_delete`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete")
  * [`bpy_struct.keyframe_insert`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert")
  * [`bpy_struct.keys`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys")
  * [`bpy_struct.path_from_id`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id")
  * [`bpy_struct.path_resolve`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve")
  * [`bpy_struct.pop`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop")
  * [`bpy_struct.property_overridable_library_set`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set")
  * [`bpy_struct.property_unset`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset")
  * [`bpy_struct.rna_ancestors`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.rna_ancestors "bpy.types.bpy_struct.rna_ancestors")
  * [`bpy_struct.type_recast`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast")
  * [`bpy_struct.values`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values")

  
---|---  
  
### References¶

  * [`BlendDataMeshes.new_from_object`](bpy.types.BlendDataMeshes.html#bpy.types.BlendDataMeshes.new_from_object "bpy.types.BlendDataMeshes.new_from_object")
  * [`Context.evaluated_depsgraph_get`](bpy.types.Context.html#bpy.types.Context.evaluated_depsgraph_get "bpy.types.Context.evaluated_depsgraph_get")
  * [`ID.evaluated_get`](bpy.types.ID.html#bpy.types.ID.evaluated_get "bpy.types.ID.evaluated_get")
  * [`Object.calc_matrix_camera`](bpy.types.Object.html#bpy.types.Object.calc_matrix_camera "bpy.types.Object.calc_matrix_camera")
  * [`Object.camera_fit_coords`](bpy.types.Object.html#bpy.types.Object.camera_fit_coords "bpy.types.Object.camera_fit_coords")
  * [`Object.closest_point_on_mesh`](bpy.types.Object.html#bpy.types.Object.closest_point_on_mesh "bpy.types.Object.closest_point_on_mesh")
  * [`Object.crazyspace_eval`](bpy.types.Object.html#bpy.types.Object.crazyspace_eval "bpy.types.Object.crazyspace_eval")
  * [`Object.ray_cast`](bpy.types.Object.html#bpy.types.Object.ray_cast "bpy.types.Object.ray_cast")
  * [`Object.to_curve`](bpy.types.Object.html#bpy.types.Object.to_curve "bpy.types.Object.to_curve")
  * [`Object.to_mesh`](bpy.types.Object.html#bpy.types.Object.to_mesh "bpy.types.Object.to_mesh")
  * [`RenderEngine.bake`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.bake "bpy.types.RenderEngine.bake")

|

  * [`RenderEngine.draw`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.draw "bpy.types.RenderEngine.draw")
  * [`RenderEngine.render`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.render "bpy.types.RenderEngine.render")
  * [`RenderEngine.update`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.update "bpy.types.RenderEngine.update")
  * [`RenderEngine.view_draw`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.view_draw "bpy.types.RenderEngine.view_draw")
  * [`RenderEngine.view_update`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.view_update "bpy.types.RenderEngine.view_update")
  * [`Scene.ray_cast`](bpy.types.Scene.html#bpy.types.Scene.ray_cast "bpy.types.Scene.ray_cast")
  * [`ShaderNodeTexPointDensity.cache_point_density`](bpy.types.ShaderNodeTexPointDensity.html#bpy.types.ShaderNodeTexPointDensity.cache_point_density "bpy.types.ShaderNodeTexPointDensity.cache_point_density")
  * [`ShaderNodeTexPointDensity.calc_point_density`](bpy.types.ShaderNodeTexPointDensity.html#bpy.types.ShaderNodeTexPointDensity.calc_point_density "bpy.types.ShaderNodeTexPointDensity.calc_point_density")
  * [`ShaderNodeTexPointDensity.calc_point_density_minmax`](bpy.types.ShaderNodeTexPointDensity.html#bpy.types.ShaderNodeTexPointDensity.calc_point_density_minmax "bpy.types.ShaderNodeTexPointDensity.calc_point_density_minmax")
  * [`ViewLayer.depsgraph`](bpy.types.ViewLayer.html#bpy.types.ViewLayer.depsgraph "bpy.types.ViewLayer.depsgraph")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

