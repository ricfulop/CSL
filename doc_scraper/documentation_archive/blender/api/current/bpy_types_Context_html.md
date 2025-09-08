---
url: https://docs.blender.org/api/current/bpy.types.Context.html
scraped_at: 2025-09-08T14:24:03.852892
title: Context(bpy_struct)¶
---

# Context(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.Context(_bpy_struct_)¶

    

Current windowmanager and data context

area¶

    

Type:

    

[`Area`](bpy.types.Area.html#bpy.types.Area "bpy.types.Area"), (readonly)

asset¶

    

Type:

    

[`AssetRepresentation`](bpy.types.AssetRepresentation.html#bpy.types.AssetRepresentation
"bpy.types.AssetRepresentation"), (readonly)

blend_data¶

    

Type:

    

[`BlendData`](bpy.types.BlendData.html#bpy.types.BlendData
"bpy.types.BlendData"), (readonly)

collection¶

    

Type:

    

[`Collection`](bpy.types.Collection.html#bpy.types.Collection
"bpy.types.Collection"), (readonly)

engine¶

    

Type:

    

string, default “”, (readonly, never None)

gizmo_group¶

    

Type:

    

[`GizmoGroup`](bpy.types.GizmoGroup.html#bpy.types.GizmoGroup
"bpy.types.GizmoGroup"), (readonly)

layer_collection¶

    

Type:

    

[`LayerCollection`](bpy.types.LayerCollection.html#bpy.types.LayerCollection
"bpy.types.LayerCollection"), (readonly)

mode¶

    

Type:

    

enum in [Context Mode Items](bpy_types_enum_items/context_mode_items.html#rna-
enum-context-mode-items), default `EDIT_MESH`, (readonly)

preferences¶

    

Type:

    

[`Preferences`](bpy.types.Preferences.html#bpy.types.Preferences
"bpy.types.Preferences"), (readonly)

region¶

    

Type:

    

[`Region`](bpy.types.Region.html#bpy.types.Region "bpy.types.Region"),
(readonly)

region_data¶

    

Type:

    

[`RegionView3D`](bpy.types.RegionView3D.html#bpy.types.RegionView3D
"bpy.types.RegionView3D"), (readonly)

region_popup¶

    

The temporary region for pop-ups (including menus and pop-overs)

Type:

    

[`Region`](bpy.types.Region.html#bpy.types.Region "bpy.types.Region"),
(readonly)

scene¶

    

Type:

    

[`Scene`](bpy.types.Scene.html#bpy.types.Scene "bpy.types.Scene"), (readonly)

screen¶

    

Type:

    

[`Screen`](bpy.types.Screen.html#bpy.types.Screen "bpy.types.Screen"),
(readonly)

space_data¶

    

The current space, may be None in background-mode, when the cursor is outside
the window or when using menu-search

Type:

    

[`Space`](bpy.types.Space.html#bpy.types.Space "bpy.types.Space"), (readonly)

tool_settings¶

    

Type:

    

[`ToolSettings`](bpy.types.ToolSettings.html#bpy.types.ToolSettings
"bpy.types.ToolSettings"), (readonly)

view_layer¶

    

Type:

    

[`ViewLayer`](bpy.types.ViewLayer.html#bpy.types.ViewLayer
"bpy.types.ViewLayer"), (readonly)

window¶

    

Type:

    

[`Window`](bpy.types.Window.html#bpy.types.Window "bpy.types.Window"),
(readonly)

window_manager¶

    

Type:

    

[`WindowManager`](bpy.types.WindowManager.html#bpy.types.WindowManager
"bpy.types.WindowManager"), (readonly)

workspace¶

    

Type:

    

[`WorkSpace`](bpy.types.WorkSpace.html#bpy.types.WorkSpace
"bpy.types.WorkSpace"), (readonly)

evaluated_depsgraph_get()¶

    

Get the dependency graph for the current scene and view layer, to access to
data-blocks with animation and modifiers applied. If any data-blocks have been
edited, the dependency graph will be updated. This invalidates all references
to evaluated data-blocks from the dependency graph.

Returns:

    

Evaluated dependency graph

Return type:

    

[`Depsgraph`](bpy.types.Depsgraph.html#bpy.types.Depsgraph
"bpy.types.Depsgraph")

copy()¶

    

Get context members as a dictionary.

> rtype:
>  
>
> dict[str, Any]

path_resolve(_path_ , _coerce =True_)¶

    

Returns the property from the path, raise an exception when not found.

Parameters:

    

  * **path** (_str_) – patch which this property resolves.

  * **coerce** (_bool_) – optional argument, when True, the property will be converted into its Python representation.

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

temp_override(_*_ , _window =None_, _area =None_, _region =None_, _**
keywords_)¶

    

Context manager to temporarily override members in the context.

Parameters:

    

  * **window** ([`bpy.types.Window`](bpy.types.Window.html#bpy.types.Window "bpy.types.Window")) – Window override or None.

  * **screen** ([`bpy.types.Screen`](bpy.types.Screen.html#bpy.types.Screen "bpy.types.Screen")) – 

Screen override or None.

Note

Switching to or away from full-screen areas & temporary screens isn’t
supported. Passing in these screens will raise an exception, actions that
leave the context such screens won’t restore the prior screen.

Note

Changing the screen has wider implications than other arguments as it will
also change the works-space and potentially the scene (when pinned).

  * **area** ([`bpy.types.Area`](bpy.types.Area.html#bpy.types.Area "bpy.types.Area")) – Area override or None.

  * **region** ([`bpy.types.Region`](bpy.types.Region.html#bpy.types.Region "bpy.types.Region")) – Region override or None.

  * **keywords** – Additional keywords override context members.

Returns:

    

The context manager .

Return type:

    

ContextTempOverride

Overriding the context can be used to temporarily activate another `window` /
`area` & `region`, as well as other members such as the `active_object` or
`bone`.

Notes:

  * When overriding window, area and regions: the arguments must be consistent, so any region argument that’s passed in must be contained by the current area or the area passed in. The same goes for the area needing to be contained in the current window.

  * Temporary context overrides may be nested, when this is done, members will be added to the existing overrides.

  * Context members are restored outside the scope of the context-manager. The only exception to this is when the data is no longer available.

In the event windowing data was removed (for example), the state of the
context is left as-is. While this isn’t likely to happen, explicit window
operation such as closing windows or loading a new file remove the windowing
data that was set before the temporary context was created.

Overriding the context can be useful to set the context after loading files
(which would otherwise by None). For example:

    
    
    import bpy
    from bpy import context
    
    # Reload the current file and select all.
    bpy.ops.wm.open_mainfile(filepath=bpy.data.filepath)
    window = context.window_manager.windows[0]
    with context.temp_override(window=window):
        bpy.ops.mesh.primitive_uv_sphere_add()
        # The context override is needed so it's possible to set edit-mode.
        bpy.ops.object.mode_set(mode='EDIT')
    

This example shows how it’s possible to add an object to the scene in another
window.

    
    
    import bpy
    from bpy import context
    
    win_active = context.window
    win_other = None
    for win_iter in context.window_manager.windows:
        if win_iter != win_active:
            win_other = win_iter
            break
    
    # Add cube in the other window.
    with context.temp_override(window=win_other):
        bpy.ops.mesh.primitive_cube_add()
    

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
  
## References¶

  * [`AssetShelf.draw_context_menu`](bpy.types.AssetShelf.html#bpy.types.AssetShelf.draw_context_menu "bpy.types.AssetShelf.draw_context_menu")
  * [`AssetShelf.poll`](bpy.types.AssetShelf.html#bpy.types.AssetShelf.poll "bpy.types.AssetShelf.poll")
  * [`FileHandler.poll_drop`](bpy.types.FileHandler.html#bpy.types.FileHandler.poll_drop "bpy.types.FileHandler.poll_drop")
  * [`Gizmo.draw`](bpy.types.Gizmo.html#bpy.types.Gizmo.draw "bpy.types.Gizmo.draw")
  * [`Gizmo.draw_select`](bpy.types.Gizmo.html#bpy.types.Gizmo.draw_select "bpy.types.Gizmo.draw_select")
  * [`Gizmo.exit`](bpy.types.Gizmo.html#bpy.types.Gizmo.exit "bpy.types.Gizmo.exit")
  * [`Gizmo.invoke`](bpy.types.Gizmo.html#bpy.types.Gizmo.invoke "bpy.types.Gizmo.invoke")
  * [`Gizmo.modal`](bpy.types.Gizmo.html#bpy.types.Gizmo.modal "bpy.types.Gizmo.modal")
  * [`Gizmo.test_select`](bpy.types.Gizmo.html#bpy.types.Gizmo.test_select "bpy.types.Gizmo.test_select")
  * [`GizmoGroup.draw_prepare`](bpy.types.GizmoGroup.html#bpy.types.GizmoGroup.draw_prepare "bpy.types.GizmoGroup.draw_prepare")
  * [`GizmoGroup.invoke_prepare`](bpy.types.GizmoGroup.html#bpy.types.GizmoGroup.invoke_prepare "bpy.types.GizmoGroup.invoke_prepare")
  * [`GizmoGroup.poll`](bpy.types.GizmoGroup.html#bpy.types.GizmoGroup.poll "bpy.types.GizmoGroup.poll")
  * [`GizmoGroup.refresh`](bpy.types.GizmoGroup.html#bpy.types.GizmoGroup.refresh "bpy.types.GizmoGroup.refresh")
  * [`GizmoGroup.setup`](bpy.types.GizmoGroup.html#bpy.types.GizmoGroup.setup "bpy.types.GizmoGroup.setup")
  * [`Header.draw`](bpy.types.Header.html#bpy.types.Header.draw "bpy.types.Header.draw")
  * [`KeyingSetInfo.generate`](bpy.types.KeyingSetInfo.html#bpy.types.KeyingSetInfo.generate "bpy.types.KeyingSetInfo.generate")
  * [`KeyingSetInfo.iterator`](bpy.types.KeyingSetInfo.html#bpy.types.KeyingSetInfo.iterator "bpy.types.KeyingSetInfo.iterator")
  * [`KeyingSetInfo.poll`](bpy.types.KeyingSetInfo.html#bpy.types.KeyingSetInfo.poll "bpy.types.KeyingSetInfo.poll")
  * [`Macro.draw`](bpy.types.Macro.html#bpy.types.Macro.draw "bpy.types.Macro.draw")
  * [`Macro.poll`](bpy.types.Macro.html#bpy.types.Macro.poll "bpy.types.Macro.poll")
  * [`Menu.draw`](bpy.types.Menu.html#bpy.types.Menu.draw "bpy.types.Menu.draw")
  * [`Menu.poll`](bpy.types.Menu.html#bpy.types.Menu.poll "bpy.types.Menu.poll")
  * [`Node.draw_buttons`](bpy.types.Node.html#bpy.types.Node.draw_buttons "bpy.types.Node.draw_buttons")
  * [`Node.draw_buttons_ext`](bpy.types.Node.html#bpy.types.Node.draw_buttons_ext "bpy.types.Node.draw_buttons_ext")
  * [`Node.init`](bpy.types.Node.html#bpy.types.Node.init "bpy.types.Node.init")
  * [`Node.socket_value_update`](bpy.types.Node.html#bpy.types.Node.socket_value_update "bpy.types.Node.socket_value_update")
  * [`NodeInternal.draw_buttons`](bpy.types.NodeInternal.html#bpy.types.NodeInternal.draw_buttons "bpy.types.NodeInternal.draw_buttons")
  * [`NodeInternal.draw_buttons_ext`](bpy.types.NodeInternal.html#bpy.types.NodeInternal.draw_buttons_ext "bpy.types.NodeInternal.draw_buttons_ext")
  * [`NodeSocket.draw`](bpy.types.NodeSocket.html#bpy.types.NodeSocket.draw "bpy.types.NodeSocket.draw")
  * [`NodeSocket.draw_color`](bpy.types.NodeSocket.html#bpy.types.NodeSocket.draw_color "bpy.types.NodeSocket.draw_color")
  * [`NodeSocketStandard.draw`](bpy.types.NodeSocketStandard.html#bpy.types.NodeSocketStandard.draw "bpy.types.NodeSocketStandard.draw")
  * [`NodeSocketStandard.draw_color`](bpy.types.NodeSocketStandard.html#bpy.types.NodeSocketStandard.draw_color "bpy.types.NodeSocketStandard.draw_color")
  * [`NodeTree.get_from_context`](bpy.types.NodeTree.html#bpy.types.NodeTree.get_from_context "bpy.types.NodeTree.get_from_context")
  * [`NodeTree.interface_update`](bpy.types.NodeTree.html#bpy.types.NodeTree.interface_update "bpy.types.NodeTree.interface_update")
  * [`NodeTree.poll`](bpy.types.NodeTree.html#bpy.types.NodeTree.poll "bpy.types.NodeTree.poll")
  * [`NodeTreeInterfaceSocket.draw`](bpy.types.NodeTreeInterfaceSocket.html#bpy.types.NodeTreeInterfaceSocket.draw "bpy.types.NodeTreeInterfaceSocket.draw")
  * [`NodeTreeInterfaceSocketBool.draw`](bpy.types.NodeTreeInterfaceSocketBool.html#bpy.types.NodeTreeInterfaceSocketBool.draw "bpy.types.NodeTreeInterfaceSocketBool.draw")
  * [`NodeTreeInterfaceSocketBundle.draw`](bpy.types.NodeTreeInterfaceSocketBundle.html#bpy.types.NodeTreeInterfaceSocketBundle.draw "bpy.types.NodeTreeInterfaceSocketBundle.draw")
  * [`NodeTreeInterfaceSocketClosure.draw`](bpy.types.NodeTreeInterfaceSocketClosure.html#bpy.types.NodeTreeInterfaceSocketClosure.draw "bpy.types.NodeTreeInterfaceSocketClosure.draw")
  * [`NodeTreeInterfaceSocketCollection.draw`](bpy.types.NodeTreeInterfaceSocketCollection.html#bpy.types.NodeTreeInterfaceSocketCollection.draw "bpy.types.NodeTreeInterfaceSocketCollection.draw")
  * [`NodeTreeInterfaceSocketColor.draw`](bpy.types.NodeTreeInterfaceSocketColor.html#bpy.types.NodeTreeInterfaceSocketColor.draw "bpy.types.NodeTreeInterfaceSocketColor.draw")
  * [`NodeTreeInterfaceSocketFloat.draw`](bpy.types.NodeTreeInterfaceSocketFloat.html#bpy.types.NodeTreeInterfaceSocketFloat.draw "bpy.types.NodeTreeInterfaceSocketFloat.draw")
  * [`NodeTreeInterfaceSocketFloatAngle.draw`](bpy.types.NodeTreeInterfaceSocketFloatAngle.html#bpy.types.NodeTreeInterfaceSocketFloatAngle.draw "bpy.types.NodeTreeInterfaceSocketFloatAngle.draw")
  * [`NodeTreeInterfaceSocketFloatColorTemperature.draw`](bpy.types.NodeTreeInterfaceSocketFloatColorTemperature.html#bpy.types.NodeTreeInterfaceSocketFloatColorTemperature.draw "bpy.types.NodeTreeInterfaceSocketFloatColorTemperature.draw")
  * [`NodeTreeInterfaceSocketFloatDistance.draw`](bpy.types.NodeTreeInterfaceSocketFloatDistance.html#bpy.types.NodeTreeInterfaceSocketFloatDistance.draw "bpy.types.NodeTreeInterfaceSocketFloatDistance.draw")
  * [`NodeTreeInterfaceSocketFloatFactor.draw`](bpy.types.NodeTreeInterfaceSocketFloatFactor.html#bpy.types.NodeTreeInterfaceSocketFloatFactor.draw "bpy.types.NodeTreeInterfaceSocketFloatFactor.draw")
  * [`NodeTreeInterfaceSocketFloatFrequency.draw`](bpy.types.NodeTreeInterfaceSocketFloatFrequency.html#bpy.types.NodeTreeInterfaceSocketFloatFrequency.draw "bpy.types.NodeTreeInterfaceSocketFloatFrequency.draw")
  * [`NodeTreeInterfaceSocketFloatPercentage.draw`](bpy.types.NodeTreeInterfaceSocketFloatPercentage.html#bpy.types.NodeTreeInterfaceSocketFloatPercentage.draw "bpy.types.NodeTreeInterfaceSocketFloatPercentage.draw")
  * [`NodeTreeInterfaceSocketFloatTime.draw`](bpy.types.NodeTreeInterfaceSocketFloatTime.html#bpy.types.NodeTreeInterfaceSocketFloatTime.draw "bpy.types.NodeTreeInterfaceSocketFloatTime.draw")
  * [`NodeTreeInterfaceSocketFloatTimeAbsolute.draw`](bpy.types.NodeTreeInterfaceSocketFloatTimeAbsolute.html#bpy.types.NodeTreeInterfaceSocketFloatTimeAbsolute.draw "bpy.types.NodeTreeInterfaceSocketFloatTimeAbsolute.draw")
  * [`NodeTreeInterfaceSocketFloatUnsigned.draw`](bpy.types.NodeTreeInterfaceSocketFloatUnsigned.html#bpy.types.NodeTreeInterfaceSocketFloatUnsigned.draw "bpy.types.NodeTreeInterfaceSocketFloatUnsigned.draw")
  * [`NodeTreeInterfaceSocketFloatWavelength.draw`](bpy.types.NodeTreeInterfaceSocketFloatWavelength.html#bpy.types.NodeTreeInterfaceSocketFloatWavelength.draw "bpy.types.NodeTreeInterfaceSocketFloatWavelength.draw")
  * [`NodeTreeInterfaceSocketGeometry.draw`](bpy.types.NodeTreeInterfaceSocketGeometry.html#bpy.types.NodeTreeInterfaceSocketGeometry.draw "bpy.types.NodeTreeInterfaceSocketGeometry.draw")
  * [`NodeTreeInterfaceSocketImage.draw`](bpy.types.NodeTreeInterfaceSocketImage.html#bpy.types.NodeTreeInterfaceSocketImage.draw "bpy.types.NodeTreeInterfaceSocketImage.draw")
  * [`NodeTreeInterfaceSocketInt.draw`](bpy.types.NodeTreeInterfaceSocketInt.html#bpy.types.NodeTreeInterfaceSocketInt.draw "bpy.types.NodeTreeInterfaceSocketInt.draw")
  * [`NodeTreeInterfaceSocketIntFactor.draw`](bpy.types.NodeTreeInterfaceSocketIntFactor.html#bpy.types.NodeTreeInterfaceSocketIntFactor.draw "bpy.types.NodeTreeInterfaceSocketIntFactor.draw")
  * [`NodeTreeInterfaceSocketIntPercentage.draw`](bpy.types.NodeTreeInterfaceSocketIntPercentage.html#bpy.types.NodeTreeInterfaceSocketIntPercentage.draw "bpy.types.NodeTreeInterfaceSocketIntPercentage.draw")
  * [`NodeTreeInterfaceSocketIntUnsigned.draw`](bpy.types.NodeTreeInterfaceSocketIntUnsigned.html#bpy.types.NodeTreeInterfaceSocketIntUnsigned.draw "bpy.types.NodeTreeInterfaceSocketIntUnsigned.draw")
  * [`NodeTreeInterfaceSocketMaterial.draw`](bpy.types.NodeTreeInterfaceSocketMaterial.html#bpy.types.NodeTreeInterfaceSocketMaterial.draw "bpy.types.NodeTreeInterfaceSocketMaterial.draw")
  * [`NodeTreeInterfaceSocketMatrix.draw`](bpy.types.NodeTreeInterfaceSocketMatrix.html#bpy.types.NodeTreeInterfaceSocketMatrix.draw "bpy.types.NodeTreeInterfaceSocketMatrix.draw")
  * [`NodeTreeInterfaceSocketMenu.draw`](bpy.types.NodeTreeInterfaceSocketMenu.html#bpy.types.NodeTreeInterfaceSocketMenu.draw "bpy.types.NodeTreeInterfaceSocketMenu.draw")
  * [`NodeTreeInterfaceSocketObject.draw`](bpy.types.NodeTreeInterfaceSocketObject.html#bpy.types.NodeTreeInterfaceSocketObject.draw "bpy.types.NodeTreeInterfaceSocketObject.draw")
  * [`NodeTreeInterfaceSocketRotation.draw`](bpy.types.NodeTreeInterfaceSocketRotation.html#bpy.types.NodeTreeInterfaceSocketRotation.draw "bpy.types.NodeTreeInterfaceSocketRotation.draw")

|

  * [`NodeTreeInterfaceSocketShader.draw`](bpy.types.NodeTreeInterfaceSocketShader.html#bpy.types.NodeTreeInterfaceSocketShader.draw "bpy.types.NodeTreeInterfaceSocketShader.draw")
  * [`NodeTreeInterfaceSocketString.draw`](bpy.types.NodeTreeInterfaceSocketString.html#bpy.types.NodeTreeInterfaceSocketString.draw "bpy.types.NodeTreeInterfaceSocketString.draw")
  * [`NodeTreeInterfaceSocketStringFilePath.draw`](bpy.types.NodeTreeInterfaceSocketStringFilePath.html#bpy.types.NodeTreeInterfaceSocketStringFilePath.draw "bpy.types.NodeTreeInterfaceSocketStringFilePath.draw")
  * [`NodeTreeInterfaceSocketTexture.draw`](bpy.types.NodeTreeInterfaceSocketTexture.html#bpy.types.NodeTreeInterfaceSocketTexture.draw "bpy.types.NodeTreeInterfaceSocketTexture.draw")
  * [`NodeTreeInterfaceSocketVector.draw`](bpy.types.NodeTreeInterfaceSocketVector.html#bpy.types.NodeTreeInterfaceSocketVector.draw "bpy.types.NodeTreeInterfaceSocketVector.draw")
  * [`NodeTreeInterfaceSocketVector2D.draw`](bpy.types.NodeTreeInterfaceSocketVector2D.html#bpy.types.NodeTreeInterfaceSocketVector2D.draw "bpy.types.NodeTreeInterfaceSocketVector2D.draw")
  * [`NodeTreeInterfaceSocketVector4D.draw`](bpy.types.NodeTreeInterfaceSocketVector4D.html#bpy.types.NodeTreeInterfaceSocketVector4D.draw "bpy.types.NodeTreeInterfaceSocketVector4D.draw")
  * [`NodeTreeInterfaceSocketVectorAcceleration.draw`](bpy.types.NodeTreeInterfaceSocketVectorAcceleration.html#bpy.types.NodeTreeInterfaceSocketVectorAcceleration.draw "bpy.types.NodeTreeInterfaceSocketVectorAcceleration.draw")
  * [`NodeTreeInterfaceSocketVectorAcceleration2D.draw`](bpy.types.NodeTreeInterfaceSocketVectorAcceleration2D.html#bpy.types.NodeTreeInterfaceSocketVectorAcceleration2D.draw "bpy.types.NodeTreeInterfaceSocketVectorAcceleration2D.draw")
  * [`NodeTreeInterfaceSocketVectorAcceleration4D.draw`](bpy.types.NodeTreeInterfaceSocketVectorAcceleration4D.html#bpy.types.NodeTreeInterfaceSocketVectorAcceleration4D.draw "bpy.types.NodeTreeInterfaceSocketVectorAcceleration4D.draw")
  * [`NodeTreeInterfaceSocketVectorDirection.draw`](bpy.types.NodeTreeInterfaceSocketVectorDirection.html#bpy.types.NodeTreeInterfaceSocketVectorDirection.draw "bpy.types.NodeTreeInterfaceSocketVectorDirection.draw")
  * [`NodeTreeInterfaceSocketVectorDirection2D.draw`](bpy.types.NodeTreeInterfaceSocketVectorDirection2D.html#bpy.types.NodeTreeInterfaceSocketVectorDirection2D.draw "bpy.types.NodeTreeInterfaceSocketVectorDirection2D.draw")
  * [`NodeTreeInterfaceSocketVectorDirection4D.draw`](bpy.types.NodeTreeInterfaceSocketVectorDirection4D.html#bpy.types.NodeTreeInterfaceSocketVectorDirection4D.draw "bpy.types.NodeTreeInterfaceSocketVectorDirection4D.draw")
  * [`NodeTreeInterfaceSocketVectorEuler.draw`](bpy.types.NodeTreeInterfaceSocketVectorEuler.html#bpy.types.NodeTreeInterfaceSocketVectorEuler.draw "bpy.types.NodeTreeInterfaceSocketVectorEuler.draw")
  * [`NodeTreeInterfaceSocketVectorEuler2D.draw`](bpy.types.NodeTreeInterfaceSocketVectorEuler2D.html#bpy.types.NodeTreeInterfaceSocketVectorEuler2D.draw "bpy.types.NodeTreeInterfaceSocketVectorEuler2D.draw")
  * [`NodeTreeInterfaceSocketVectorEuler4D.draw`](bpy.types.NodeTreeInterfaceSocketVectorEuler4D.html#bpy.types.NodeTreeInterfaceSocketVectorEuler4D.draw "bpy.types.NodeTreeInterfaceSocketVectorEuler4D.draw")
  * [`NodeTreeInterfaceSocketVectorFactor.draw`](bpy.types.NodeTreeInterfaceSocketVectorFactor.html#bpy.types.NodeTreeInterfaceSocketVectorFactor.draw "bpy.types.NodeTreeInterfaceSocketVectorFactor.draw")
  * [`NodeTreeInterfaceSocketVectorFactor2D.draw`](bpy.types.NodeTreeInterfaceSocketVectorFactor2D.html#bpy.types.NodeTreeInterfaceSocketVectorFactor2D.draw "bpy.types.NodeTreeInterfaceSocketVectorFactor2D.draw")
  * [`NodeTreeInterfaceSocketVectorFactor4D.draw`](bpy.types.NodeTreeInterfaceSocketVectorFactor4D.html#bpy.types.NodeTreeInterfaceSocketVectorFactor4D.draw "bpy.types.NodeTreeInterfaceSocketVectorFactor4D.draw")
  * [`NodeTreeInterfaceSocketVectorPercentage.draw`](bpy.types.NodeTreeInterfaceSocketVectorPercentage.html#bpy.types.NodeTreeInterfaceSocketVectorPercentage.draw "bpy.types.NodeTreeInterfaceSocketVectorPercentage.draw")
  * [`NodeTreeInterfaceSocketVectorPercentage2D.draw`](bpy.types.NodeTreeInterfaceSocketVectorPercentage2D.html#bpy.types.NodeTreeInterfaceSocketVectorPercentage2D.draw "bpy.types.NodeTreeInterfaceSocketVectorPercentage2D.draw")
  * [`NodeTreeInterfaceSocketVectorPercentage4D.draw`](bpy.types.NodeTreeInterfaceSocketVectorPercentage4D.html#bpy.types.NodeTreeInterfaceSocketVectorPercentage4D.draw "bpy.types.NodeTreeInterfaceSocketVectorPercentage4D.draw")
  * [`NodeTreeInterfaceSocketVectorTranslation.draw`](bpy.types.NodeTreeInterfaceSocketVectorTranslation.html#bpy.types.NodeTreeInterfaceSocketVectorTranslation.draw "bpy.types.NodeTreeInterfaceSocketVectorTranslation.draw")
  * [`NodeTreeInterfaceSocketVectorTranslation2D.draw`](bpy.types.NodeTreeInterfaceSocketVectorTranslation2D.html#bpy.types.NodeTreeInterfaceSocketVectorTranslation2D.draw "bpy.types.NodeTreeInterfaceSocketVectorTranslation2D.draw")
  * [`NodeTreeInterfaceSocketVectorTranslation4D.draw`](bpy.types.NodeTreeInterfaceSocketVectorTranslation4D.html#bpy.types.NodeTreeInterfaceSocketVectorTranslation4D.draw "bpy.types.NodeTreeInterfaceSocketVectorTranslation4D.draw")
  * [`NodeTreeInterfaceSocketVectorVelocity.draw`](bpy.types.NodeTreeInterfaceSocketVectorVelocity.html#bpy.types.NodeTreeInterfaceSocketVectorVelocity.draw "bpy.types.NodeTreeInterfaceSocketVectorVelocity.draw")
  * [`NodeTreeInterfaceSocketVectorVelocity2D.draw`](bpy.types.NodeTreeInterfaceSocketVectorVelocity2D.html#bpy.types.NodeTreeInterfaceSocketVectorVelocity2D.draw "bpy.types.NodeTreeInterfaceSocketVectorVelocity2D.draw")
  * [`NodeTreeInterfaceSocketVectorVelocity4D.draw`](bpy.types.NodeTreeInterfaceSocketVectorVelocity4D.html#bpy.types.NodeTreeInterfaceSocketVectorVelocity4D.draw "bpy.types.NodeTreeInterfaceSocketVectorVelocity4D.draw")
  * [`NodeTreeInterfaceSocketVectorXYZ.draw`](bpy.types.NodeTreeInterfaceSocketVectorXYZ.html#bpy.types.NodeTreeInterfaceSocketVectorXYZ.draw "bpy.types.NodeTreeInterfaceSocketVectorXYZ.draw")
  * [`NodeTreeInterfaceSocketVectorXYZ2D.draw`](bpy.types.NodeTreeInterfaceSocketVectorXYZ2D.html#bpy.types.NodeTreeInterfaceSocketVectorXYZ2D.draw "bpy.types.NodeTreeInterfaceSocketVectorXYZ2D.draw")
  * [`NodeTreeInterfaceSocketVectorXYZ4D.draw`](bpy.types.NodeTreeInterfaceSocketVectorXYZ4D.html#bpy.types.NodeTreeInterfaceSocketVectorXYZ4D.draw "bpy.types.NodeTreeInterfaceSocketVectorXYZ4D.draw")
  * [`Operator.cancel`](bpy.types.Operator.html#bpy.types.Operator.cancel "bpy.types.Operator.cancel")
  * [`Operator.check`](bpy.types.Operator.html#bpy.types.Operator.check "bpy.types.Operator.check")
  * [`Operator.description`](bpy.types.Operator.html#bpy.types.Operator.description "bpy.types.Operator.description")
  * [`Operator.draw`](bpy.types.Operator.html#bpy.types.Operator.draw "bpy.types.Operator.draw")
  * [`Operator.execute`](bpy.types.Operator.html#bpy.types.Operator.execute "bpy.types.Operator.execute")
  * [`Operator.invoke`](bpy.types.Operator.html#bpy.types.Operator.invoke "bpy.types.Operator.invoke")
  * [`Operator.modal`](bpy.types.Operator.html#bpy.types.Operator.modal "bpy.types.Operator.modal")
  * [`Operator.poll`](bpy.types.Operator.html#bpy.types.Operator.poll "bpy.types.Operator.poll")
  * [`Panel.draw`](bpy.types.Panel.html#bpy.types.Panel.draw "bpy.types.Panel.draw")
  * [`Panel.draw_header`](bpy.types.Panel.html#bpy.types.Panel.draw_header "bpy.types.Panel.draw_header")
  * [`Panel.draw_header_preset`](bpy.types.Panel.html#bpy.types.Panel.draw_header_preset "bpy.types.Panel.draw_header_preset")
  * [`Panel.poll`](bpy.types.Panel.html#bpy.types.Panel.poll "bpy.types.Panel.poll")
  * [`RenderEngine.draw`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.draw "bpy.types.RenderEngine.draw")
  * [`RenderEngine.view_draw`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.view_draw "bpy.types.RenderEngine.view_draw")
  * [`RenderEngine.view_update`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.view_update "bpy.types.RenderEngine.view_update")
  * [`UIList.draw_filter`](bpy.types.UIList.html#bpy.types.UIList.draw_filter "bpy.types.UIList.draw_filter")
  * [`UIList.draw_item`](bpy.types.UIList.html#bpy.types.UIList.draw_item "bpy.types.UIList.draw_item")
  * [`UIList.filter_items`](bpy.types.UIList.html#bpy.types.UIList.filter_items "bpy.types.UIList.filter_items")
  * [`XrSessionState.action_binding_create`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.action_binding_create "bpy.types.XrSessionState.action_binding_create")
  * [`XrSessionState.action_create`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.action_create "bpy.types.XrSessionState.action_create")
  * [`XrSessionState.action_set_create`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.action_set_create "bpy.types.XrSessionState.action_set_create")
  * [`XrSessionState.action_state_get`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.action_state_get "bpy.types.XrSessionState.action_state_get")
  * [`XrSessionState.active_action_set_set`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.active_action_set_set "bpy.types.XrSessionState.active_action_set_set")
  * [`XrSessionState.controller_aim_location_get`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.controller_aim_location_get "bpy.types.XrSessionState.controller_aim_location_get")
  * [`XrSessionState.controller_aim_rotation_get`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.controller_aim_rotation_get "bpy.types.XrSessionState.controller_aim_rotation_get")
  * [`XrSessionState.controller_grip_location_get`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.controller_grip_location_get "bpy.types.XrSessionState.controller_grip_location_get")
  * [`XrSessionState.controller_grip_rotation_get`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.controller_grip_rotation_get "bpy.types.XrSessionState.controller_grip_rotation_get")
  * [`XrSessionState.controller_pose_actions_set`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.controller_pose_actions_set "bpy.types.XrSessionState.controller_pose_actions_set")
  * [`XrSessionState.haptic_action_apply`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.haptic_action_apply "bpy.types.XrSessionState.haptic_action_apply")
  * [`XrSessionState.haptic_action_stop`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.haptic_action_stop "bpy.types.XrSessionState.haptic_action_stop")
  * [`XrSessionState.is_running`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.is_running "bpy.types.XrSessionState.is_running")
  * [`XrSessionState.reset_to_base_pose`](bpy.types.XrSessionState.html#bpy.types.XrSessionState.reset_to_base_pose "bpy.types.XrSessionState.reset_to_base_pose")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

