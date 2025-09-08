---
url: https://docs.blender.org/api/current/bpy.types.FileHandler.html
scraped_at: 2025-09-08T14:25:17.290238
title: FileHandler(bpy_struct)¶
---

# FileHandler(bpy_struct)¶  
  
## Basic FileHandler for importing a single file¶

A file handler allows custom ‘drag-and-drop’ behavior to be associated with a
given `Operator` (`FileHandler.bl_import_operator`) and set of file extensions
(`FileHandler.bl_file_extensions`). Control over which area of the UI accepts
the drag-in-drop action is specified using the `FileHandler.poll_drop` method.

Similar to operators that use a file select window, operators participating in
‘drag-and-drop’, and only accepting a single file, must define the following
property:

    
    
    filepath: bpy.props.StringProperty(subtype='FILE_PATH', options={'SKIP_SAVE'})
    

This `filepath` property will be set to the full path of the file dropped by
the user.

    
    
    import bpy
    
    
    class CurveTextImport(bpy.types.Operator):
        """
        Creates a text object from a text file.
        """
        bl_idname = "curve.text_import"
        bl_label = "Import a text file as text object"
    
        # This Operator supports processing one `.txt` file at a time. The following file-path
        # property must be defined.
        filepath: bpy.props.StringProperty(subtype='FILE_PATH', options={'SKIP_SAVE'})
    
        @classmethod
        def poll(cls, context):
            return (context.area and context.area.type == "VIEW_3D")
    
        def execute(self, context):
            # Direct calls to this Operator may use unsupported file-paths. Ensure the incoming
            # file-path is one that is supported.
            if not self.filepath or not self.filepath.endswith(".txt"):
                return {'CANCELLED'}
    
            # Create a Blender Text object from the contents of the provided file.
            with open(self.filepath) as file:
                text_curve = bpy.data.curves.new(type="FONT", name="Text")
                text_curve.body = ''.join(file.readlines())
                text_object = bpy.data.objects.new(name="Text", object_data=text_curve)
                bpy.context.scene.collection.objects.link(text_object)
            return {'FINISHED'}
    
        # By default the file handler invokes the operator with the file-path property set. If the
        # operator also supports being invoked with no file-path set, and allows the user to pick from a
        # file select window instead, the following logic can be used.
        #
        # Note: It is important to use `options={'SKIP_SAVE'}` when defining the file-path property to
        # avoid prior values from being reused on subsequent calls.
    
        def invoke(self, context, event):
            if self.filepath:
                return self.execute(context)
            context.window_manager.fileselect_add(self)
            return {'RUNNING_MODAL'}
    
    
    # Define a file handler that supports the following set of conditions:
    #  - Execute the `curve.text_import` operator
    #  - When `.txt` files are dropped in the 3D Viewport
    class CURVE_FH_text_import(bpy.types.FileHandler):
        bl_idname = "CURVE_FH_text_import"
        bl_label = "File handler for curve text object import"
        bl_import_operator = "curve.text_import"
        bl_file_extensions = ".txt"
    
        @classmethod
        def poll_drop(cls, context):
            return (context.area and context.area.type == 'VIEW_3D')
    
    
    bpy.utils.register_class(CurveTextImport)
    bpy.utils.register_class(CURVE_FH_text_import)
    

## FileHandler for Importing multiple files and exposing Operator options¶

Operators which support being executed with multiple files from ‘drag-and-
drop’ require the following properties be defined:

    
    
    directory: StringProperty(subtype='DIR_PATH', options={'SKIP_SAVE', 'HIDDEN'})
    files: CollectionProperty(type=OperatorFileListElement, options={'SKIP_SAVE', 'HIDDEN'})
    

These `directory` and `files` properties will be set with the necessary data
from the drag-and-drop operation.

Additionally, if the operator provides operator properties that need to be
accessible to the user, the `ImportHelper.invoke_popup` method can be used to
show a dialog leveraging the standard
[`Operator.draw`](bpy.types.Operator.html#bpy.types.Operator.draw
"bpy.types.Operator.draw") method for layout and display.

    
    
    import bpy
    from bpy_extras.io_utils import ImportHelper
    from mathutils import Vector
    
    
    class ShaderScriptImport(bpy.types.Operator, ImportHelper):
        """
        Creates one or more Shader Script nodes from text files.
        """
        bl_idname = "shader.script_import"
        bl_label = "Import a text file as a script node"
    
        # This Operator supports processing multiple `.txt` files at a time. The following properties
        # must be defined.
        directory: bpy.props.StringProperty(subtype='DIR_PATH', options={'SKIP_SAVE', 'HIDDEN'})
        files: bpy.props.CollectionProperty(type=bpy.types.OperatorFileListElement, options={'SKIP_SAVE', 'HIDDEN'})
    
        # Allow the user to choose whether the node's label is set or not
        set_label: bpy.props.BoolProperty(name="Set Label", default=False)
    
        @classmethod
        def poll(cls, context):
            return (
                context.region and context.region.type == 'WINDOW' and
                context.area and context.area.ui_type == 'ShaderNodeTree' and
                context.object and context.object.type == 'MESH' and
                context.material
            )
    
        def execute(self, context):
            # The directory property must be set.
            if not self.directory:
                return {'CANCELLED'}
    
            x = 0.0
            y = 0.0
            for file in self.files:
                # Direct calls to this Operator may use unsupported file-paths. Ensure the incoming
                # files are ones that are supported.
                if file.name.endswith(".txt"):
                    import os
                    filepath = os.path.join(self.directory, file.name)
    
                    node_tree = context.material.node_tree
                    text_node = node_tree.nodes.new(type="ShaderNodeScript")
                    text_node.mode = 'EXTERNAL'
                    text_node.filepath = filepath
                    text_node.location = Vector((x, y))
    
                    # Set the node's title to the file name.
                    if self.set_label:
                        text_node.label = file.name
    
                    x += 20.0
                    y -= 20.0
    
            return {'FINISHED'}
    
        # Use ImportHelper's invoke_popup() to handle the invocation so that this operator's properties
        # are shown in a popup. This allows the user to configure additional settings on the operator
        # like the `set_label` property. Consider having a draw() method on the operator in order to
        # layout the properties in the UI appropriately.
        #
        # If filepath information is not provided the file select window will be invoked instead.
    
        def invoke(self, context, event):
            return self.invoke_popup(context)
    
    
    # Define a file handler that supports the following set of conditions:
    #  - Execute the `shader.script_import` operator
    #  - When `.txt` files are dropped in the Shader Editor
    class SHADER_FH_script_import(bpy.types.FileHandler):
        bl_idname = "SHADER_FH_script_import"
        bl_label = "File handler for shader script node import"
        bl_import_operator = "shader.script_import"
        bl_file_extensions = ".txt"
    
        @classmethod
        def poll_drop(cls, context):
            return (
                context.region and context.region.type == 'WINDOW' and
                context.area and context.area.ui_type == 'ShaderNodeTree'
            )
    
    
    bpy.utils.register_class(ShaderScriptImport)
    bpy.utils.register_class(SHADER_FH_script_import)
    

base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

subclasses —
[`IMAGE_FH_drop_handler`](bpy.types.IMAGE_FH_drop_handler.html#bpy.types.IMAGE_FH_drop_handler
"bpy.types.IMAGE_FH_drop_handler"),
[`IO_FH_fbx`](bpy.types.IO_FH_fbx.html#bpy.types.IO_FH_fbx
"bpy.types.IO_FH_fbx"),
[`IO_FH_gltf2`](bpy.types.IO_FH_gltf2.html#bpy.types.IO_FH_gltf2
"bpy.types.IO_FH_gltf2"),
[`NODE_FH_image_node`](bpy.types.NODE_FH_image_node.html#bpy.types.NODE_FH_image_node
"bpy.types.NODE_FH_image_node"),
[`SEQUENCER_FH_image_strip`](bpy.types.SEQUENCER_FH_image_strip.html#bpy.types.SEQUENCER_FH_image_strip
"bpy.types.SEQUENCER_FH_image_strip"),
[`SEQUENCER_FH_movie_strip`](bpy.types.SEQUENCER_FH_movie_strip.html#bpy.types.SEQUENCER_FH_movie_strip
"bpy.types.SEQUENCER_FH_movie_strip"),
[`SEQUENCER_FH_sound_strip`](bpy.types.SEQUENCER_FH_sound_strip.html#bpy.types.SEQUENCER_FH_sound_strip
"bpy.types.SEQUENCER_FH_sound_strip"),
[`VIEW3D_FH_camera_background_image`](bpy.types.VIEW3D_FH_camera_background_image.html#bpy.types.VIEW3D_FH_camera_background_image
"bpy.types.VIEW3D_FH_camera_background_image"),
[`VIEW3D_FH_empty_image`](bpy.types.VIEW3D_FH_empty_image.html#bpy.types.VIEW3D_FH_empty_image
"bpy.types.VIEW3D_FH_empty_image"),
[`VIEW3D_FH_vdb_volume`](bpy.types.VIEW3D_FH_vdb_volume.html#bpy.types.VIEW3D_FH_vdb_volume
"bpy.types.VIEW3D_FH_vdb_volume")

_class _bpy.types.FileHandler(_bpy_struct_)¶

    

Extends functionality to operators that manages files, such as adding drag and
drop support

bl_export_operator¶

    

Operator that can handle export for files with the extensions given in
bl_file_extensions

Type:

    

string, default “”, (never None)

bl_file_extensions¶

    

Formatted string of file extensions supported by the file handler, each
extension should start with a “.” and be separated by “;”. For Example:
“.blend;.ble”

Type:

    

string, default “”, (never None)

bl_idname¶

    

If this is set, the file handler gets a custom ID, otherwise it takes the name
of the class used to define the file handler (for example, if the class name
is “OBJECT_FH_hello”, and bl_idname is not set by the script, then bl_idname =
“OBJECT_FH_hello”)

Type:

    

string, default “”, (never None)

bl_import_operator¶

    

Operator that can handle import for files with the extensions given in
bl_file_extensions

Type:

    

string, default “”, (never None)

bl_label¶

    

The file handler label

Type:

    

string, default “”, (never None)

_classmethod _poll_drop(_context_)¶

    

If this method returns True, can be used to handle the drop of a drag-and-drop
action

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

## Inherited Properties¶

  * [`bpy_struct.id_data`](bpy.types.bpy_struct.html#bpy.types.bpy_struct.id_data "bpy.types.bpy_struct.id_data")

|

  
---|---  
  
## Inherited Functions¶

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
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

