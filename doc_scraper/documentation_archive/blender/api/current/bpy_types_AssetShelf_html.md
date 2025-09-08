---
url: https://docs.blender.org/api/current/bpy.types.AssetShelf.html
scraped_at: 2025-09-08T14:19:54.869125
title: AssetShelf(bpy_struct)¶
---

# AssetShelf(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

subclasses —
[`IMAGE_AST_brush_paint`](bpy.types.IMAGE_AST_brush_paint.html#bpy.types.IMAGE_AST_brush_paint
"bpy.types.IMAGE_AST_brush_paint"),
[`VIEW3D_AST_brush_gpencil_paint`](bpy.types.VIEW3D_AST_brush_gpencil_paint.html#bpy.types.VIEW3D_AST_brush_gpencil_paint
"bpy.types.VIEW3D_AST_brush_gpencil_paint"),
[`VIEW3D_AST_brush_gpencil_sculpt`](bpy.types.VIEW3D_AST_brush_gpencil_sculpt.html#bpy.types.VIEW3D_AST_brush_gpencil_sculpt
"bpy.types.VIEW3D_AST_brush_gpencil_sculpt"),
[`VIEW3D_AST_brush_gpencil_vertex`](bpy.types.VIEW3D_AST_brush_gpencil_vertex.html#bpy.types.VIEW3D_AST_brush_gpencil_vertex
"bpy.types.VIEW3D_AST_brush_gpencil_vertex"),
[`VIEW3D_AST_brush_gpencil_weight`](bpy.types.VIEW3D_AST_brush_gpencil_weight.html#bpy.types.VIEW3D_AST_brush_gpencil_weight
"bpy.types.VIEW3D_AST_brush_gpencil_weight"),
[`VIEW3D_AST_brush_sculpt`](bpy.types.VIEW3D_AST_brush_sculpt.html#bpy.types.VIEW3D_AST_brush_sculpt
"bpy.types.VIEW3D_AST_brush_sculpt"),
[`VIEW3D_AST_brush_sculpt_curves`](bpy.types.VIEW3D_AST_brush_sculpt_curves.html#bpy.types.VIEW3D_AST_brush_sculpt_curves
"bpy.types.VIEW3D_AST_brush_sculpt_curves"),
[`VIEW3D_AST_brush_texture_paint`](bpy.types.VIEW3D_AST_brush_texture_paint.html#bpy.types.VIEW3D_AST_brush_texture_paint
"bpy.types.VIEW3D_AST_brush_texture_paint"),
[`VIEW3D_AST_brush_vertex_paint`](bpy.types.VIEW3D_AST_brush_vertex_paint.html#bpy.types.VIEW3D_AST_brush_vertex_paint
"bpy.types.VIEW3D_AST_brush_vertex_paint"),
[`VIEW3D_AST_brush_weight_paint`](bpy.types.VIEW3D_AST_brush_weight_paint.html#bpy.types.VIEW3D_AST_brush_weight_paint
"bpy.types.VIEW3D_AST_brush_weight_paint"),
[`VIEW3D_AST_pose_library`](bpy.types.VIEW3D_AST_pose_library.html#bpy.types.VIEW3D_AST_pose_library
"bpy.types.VIEW3D_AST_pose_library")

_class _bpy.types.AssetShelf(_bpy_struct_)¶

    

Regions for quick access to assets

asset_library_reference¶

    

Choose the asset library to display assets from

  * `ALL` All Libraries – Show assets from all of the listed asset libraries.

  * `LOCAL` Current File – Show the assets currently available in this Blender session.

  * `ESSENTIALS` Essentials – Show the basic building blocks and utilities coming with Blender.

  * `CUSTOM` Custom – Show assets from the asset libraries configured in the Preferences.

Type:

    

enum in [`ALL`, `LOCAL`, `ESSENTIALS`, `CUSTOM`], default `ALL`

bl_activate_operator¶

    

Operator to call when activating an item with asset reference properties

Type:

    

string, default “”, (never None)

bl_default_preview_size¶

    

Default size of the asset preview thumbnails in pixels

Type:

    

int in [32, 256], default 0

bl_idname¶

    

If this is set, the asset gets a custom ID, otherwise it takes the name of the
class used to define the asset (for example, if the class name is
“OBJECT_AST_hello”, and bl_idname is not set by the script, then bl_idname =
“OBJECT_AST_hello”)

Type:

    

string, default “”, (never None)

bl_options¶

    

Options for this asset shelf type

  * `NO_ASSET_DRAG` No Asset Dragging – Disable the default asset dragging on drag events. Useful for implementing custom dragging via custom key-map items..

  * `DEFAULT_VISIBLE` Visible by Default – Unhide the asset shelf when it’s available for the first time, otherwise it will be hidden.

  * `STORE_ENABLED_CATALOGS_IN_PREFERENCES` Store Enabled Catalogs in Preferences – Store the shelf’s enabled catalogs in the preferences rather than the local asset shelf settings.

Type:

    

enum set in {`NO_ASSET_DRAG`, `DEFAULT_VISIBLE`,
`STORE_ENABLED_CATALOGS_IN_PREFERENCES`}, default `{'NO_ASSET_DRAG'}`

bl_space_type¶

    

The space where the asset shelf is going to be used in

Type:

    

enum in [Space Type Items](bpy_types_enum_items/space_type_items.html#rna-
enum-space-type-items), default `EMPTY`

preview_size¶

    

Size of the asset preview thumbnails in pixels

Type:

    

int in [32, 256], default 0

search_filter¶

    

Filter assets by name

Type:

    

string, default “”, (never None)

show_names¶

    

Show the asset name together with the preview. Otherwise only the preview will
be visible.

Type:

    

boolean, default False

_classmethod _poll(_context_)¶

    

If this method returns a non-null output, the asset shelf will be visible

Return type:

    

boolean

_classmethod _asset_poll(_asset_)¶

    

Determine if an asset should be visible in the asset shelf. If this method
returns a non-null output, the asset will be visible.

Return type:

    

boolean

_classmethod _get_active_asset()¶

    

Return a reference to the asset that should be highlighted as active in the
asset shelf

Returns:

    

The weak reference to the asset to be hightlighted as active, or None

Return type:

    

[`AssetWeakReference`](bpy.types.AssetWeakReference.html#bpy.types.AssetWeakReference
"bpy.types.AssetWeakReference")

_classmethod _draw_context_menu(_context_ , _asset_ , _layout_)¶

    

Draw UI elements into the context menu UI layout displayed on right click

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

