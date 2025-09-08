---
url: https://docs.blender.org/api/current/bpy.ops.outliner.html
scraped_at: 2025-09-08T14:18:32.613793
title: Outliner Operators¶
---

# Outliner Operators¶

bpy.ops.outliner.action_set(_*_ , _action_)¶

    

Change the active action used

Parameters:

    

**action** (_enum in_ _[__]__,__(__optional_ _)_) – Action

bpy.ops.outliner.animdata_operation(_*_ , _type =CLEAR_ANIMDATA_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**type** (enum in [`CLEAR_ANIMDATA`, `SET_ACT`, `CLEAR_ACT`,
`REFRESH_DRIVERS`, `CLEAR_DRIVERS`], (optional)) –

Animation Operation

  * `CLEAR_ANIMDATA` Clear Animation Data – Remove this animation data container.

  * `SET_ACT` Set Action.

  * `CLEAR_ACT` Unlink Action.

  * `REFRESH_DRIVERS` Refresh Drivers.

  * `CLEAR_DRIVERS` Clear Drivers.

bpy.ops.outliner.clear_filter()¶

    

Clear the search filter

bpy.ops.outliner.collection_color_tag_set(_*_ , _color =NONE_)¶

    

Set a color tag for the selected collections

Parameters:

    

**color** (enum in [Collection Color
Items](bpy_types_enum_items/collection_color_items.html#rna-enum-collection-
color-items), (optional)) – Color Tag

bpy.ops.outliner.collection_disable()¶

    

Disable viewport display in the view layers

bpy.ops.outliner.collection_disable_render()¶

    

Do not render this collection

bpy.ops.outliner.collection_drop()¶

    

Drag to move to collection in Outliner

bpy.ops.outliner.collection_duplicate()¶

    

Recursively duplicate the collection, all its children, objects and object
data

bpy.ops.outliner.collection_duplicate_linked()¶

    

Recursively duplicate the collection, all its children and objects, with
linked object data

bpy.ops.outliner.collection_enable()¶

    

Enable viewport display in the view layers

bpy.ops.outliner.collection_enable_render()¶

    

Render the collection

bpy.ops.outliner.collection_exclude_clear()¶

    

Include collection in the active view layer

bpy.ops.outliner.collection_exclude_set()¶

    

Exclude collection from the active view layer

bpy.ops.outliner.collection_hide()¶

    

Hide the collection in this view layer

bpy.ops.outliner.collection_hide_inside()¶

    

Hide all the objects and collections inside the collection

bpy.ops.outliner.collection_hierarchy_delete()¶

    

Delete selected collection hierarchies

bpy.ops.outliner.collection_holdout_clear()¶

    

Clear masking of collection in the active view layer

bpy.ops.outliner.collection_holdout_set()¶

    

Mask collection in the active view layer

bpy.ops.outliner.collection_indirect_only_clear()¶

    

Clear collection contributing only indirectly in the view layer

bpy.ops.outliner.collection_indirect_only_set()¶

    

Set collection to only contribute indirectly (through shadows and reflections)
in the view layer

bpy.ops.outliner.collection_instance()¶

    

Instance selected collections to active scene

bpy.ops.outliner.collection_isolate(_*_ , _extend =False_)¶

    

Hide all but this collection and its parents

Parameters:

    

**extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend current visible
collections

bpy.ops.outliner.collection_link()¶

    

Link selected collections to active scene

bpy.ops.outliner.collection_new(_*_ , _nested =True_)¶

    

Add a new collection inside selected collection

Parameters:

    

**nested** (_boolean_ _,__(__optional_ _)_) – Nested, Add as child of selected
collection

bpy.ops.outliner.collection_objects_deselect()¶

    

Deselect objects in collection

bpy.ops.outliner.collection_objects_select()¶

    

Select objects in collection

bpy.ops.outliner.collection_show()¶

    

Show the collection in this view layer

bpy.ops.outliner.collection_show_inside()¶

    

Show all the objects and collections inside the collection

bpy.ops.outliner.constraint_operation(_*_ , _type =ENABLE_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**type** (enum in [`ENABLE`, `DISABLE`, `DELETE`], (optional)) – Constraint
Operation

bpy.ops.outliner.data_operation(_*_ , _type =DEFAULT_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**type** (enum in [`DEFAULT`], (optional)) – Data Operation

bpy.ops.outliner.datastack_drop()¶

    

Copy or reorder modifiers, constraints, and effects

bpy.ops.outliner.delete(_*_ , _hierarchy =False_)¶

    

Delete selected objects and collections

Parameters:

    

**hierarchy** (_boolean_ _,__(__optional_ _)_) – Hierarchy, Delete child
objects and collections

bpy.ops.outliner.drivers_add_selected()¶

    

Add drivers to selected items

bpy.ops.outliner.drivers_delete_selected()¶

    

Delete drivers assigned to selected items

bpy.ops.outliner.expanded_toggle()¶

    

Expand/Collapse all items

bpy.ops.outliner.hide()¶

    

Hide selected objects and collections

bpy.ops.outliner.highlight_update()¶

    

Update the item highlight based on the current mouse position

bpy.ops.outliner.id_copy()¶

    

Copy the selected data-blocks to the internal clipboard

bpy.ops.outliner.id_delete()¶

    

Delete the ID under cursor

bpy.ops.outliner.id_linked_relocate()¶

    

Replace the active linked ID (and its dependencies if any) by another one,
from the same or a different library

bpy.ops.outliner.id_operation(_*_ , _type =UNLINK_)¶

    

General data-block management operations

Parameters:

    

**type** (enum in [`UNLINK`, `LOCAL`, `SINGLE`, `DELETE`, `REMAP`, `COPY`,
`PASTE`, `ADD_FAKE`, `CLEAR_FAKE`, `RENAME`, `SELECT_LINKED`], (optional)) –

ID Data Operation

  * `UNLINK` Unlink.

  * `LOCAL` Make Local.

  * `SINGLE` Make Single User.

  * `DELETE` Delete.

  * `REMAP` Remap Users – Make all users of selected data-blocks to use instead current (clicked) one.

  * `COPY` Copy.

  * `PASTE` Paste.

  * `ADD_FAKE` Add Fake User – Ensure data-block gets saved even if it isn’t in use (e.g. for motion and material libraries).

  * `CLEAR_FAKE` Clear Fake User.

  * `RENAME` Rename.

  * `SELECT_LINKED` Select Linked.

bpy.ops.outliner.id_paste()¶

    

Paste data-blocks from the internal clipboard

bpy.ops.outliner.id_remap(_*_ , _id_type =OBJECT_, _old_id_ , _new_id_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

  * **id_type** (enum in [Id Type Items](bpy_types_enum_items/id_type_items.html#rna-enum-id-type-items), (optional)) – ID Type

  * **old_id** (_enum in_ _[__]__,__(__optional_ _)_) – Old ID, Old ID to replace

  * **new_id** (_enum in_ _[__]__,__(__optional_ _)_) – New ID, New ID to remap all selected IDs’ users to

bpy.ops.outliner.item_activate(_*_ , _extend =False_, _extend_range =False_,
_deselect_all =False_, _recurse =False_)¶

    

Handle mouse clicks to select and activate items

Parameters:

    

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection for activation

  * **extend_range** (_boolean_ _,__(__optional_ _)_) – Extend Range, Select a range from active element

  * **deselect_all** (_boolean_ _,__(__optional_ _)_) – Deselect On Nothing, Deselect all when nothing under the cursor

  * **recurse** (_boolean_ _,__(__optional_ _)_) – Recurse, Select objects recursively from active element

bpy.ops.outliner.item_drag_drop()¶

    

Drag and drop element to another place

bpy.ops.outliner.item_openclose(_*_ , _all =False_)¶

    

Toggle whether item under cursor is enabled or closed

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Close or open all items

bpy.ops.outliner.item_rename(_*_ , _use_active =False_)¶

    

Rename the active element

Parameters:

    

**use_active** (_boolean_ _,__(__optional_ _)_) – Use Active, Rename the
active item, rather than the one the mouse is over

bpy.ops.outliner.keyingset_add_selected()¶

    

Add selected items (blue-gray rows) to active Keying Set

bpy.ops.outliner.keyingset_remove_selected()¶

    

Remove selected items (blue-gray rows) from active Keying Set

bpy.ops.outliner.lib_operation(_*_ , _type =DELETE_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**type** (enum in [`DELETE`, `RELOCATE`, `RELOAD`], (optional)) –

Library Operation

  * `DELETE` Delete – Delete this library and all its items.

  * `RELOCATE` Relocate – Select a new path for this library, and reload all its data.

  * `RELOAD` Reload – Reload all data from this library.

bpy.ops.outliner.lib_relocate()¶

    

Relocate the library under cursor

bpy.ops.outliner.liboverride_operation(_*_ , _type
=OVERRIDE_LIBRARY_CREATE_HIERARCHY_, _selection_set =SELECTED_)¶

    

Create, reset or clear library override hierarchies

Parameters:

    

  * **type** (enum in [`OVERRIDE_LIBRARY_CREATE_HIERARCHY`, `OVERRIDE_LIBRARY_RESET`, `OVERRIDE_LIBRARY_CLEAR_SINGLE`], (optional)) – 

Library Override Operation

    * `OVERRIDE_LIBRARY_CREATE_HIERARCHY` Make – Create a local override of the selected linked data-blocks, and their hierarchy of dependencies.

    * `OVERRIDE_LIBRARY_RESET` Reset – Reset the selected local overrides to their linked references values.

    * `OVERRIDE_LIBRARY_CLEAR_SINGLE` Clear – Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable.

  * **selection_set** (enum in [`SELECTED`, `CONTENT`, `SELECTED_AND_CONTENT`], (optional)) – 

Selection Set, Over which part of the tree items to apply the operation

    * `SELECTED` Selected – Apply the operation over selected data-blocks only.

    * `CONTENT` Content – Apply the operation over content of the selected items only (the data-blocks in their sub-tree).

    * `SELECTED_AND_CONTENT` Selected & Content – Apply the operation over selected data-blocks and all their dependencies.

bpy.ops.outliner.liboverride_troubleshoot_operation(_*_ , _type
=OVERRIDE_LIBRARY_RESYNC_HIERARCHY_, _selection_set =SELECTED_)¶

    

Advanced operations over library override to help fix broken hierarchies

Parameters:

    

  * **type** (enum in [`OVERRIDE_LIBRARY_RESYNC_HIERARCHY`, `OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE`, `OVERRIDE_LIBRARY_DELETE_HIERARCHY`], (optional)) – 

Library Override Troubleshoot Operation

    * `OVERRIDE_LIBRARY_RESYNC_HIERARCHY` Resync – Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies.

    * `OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE` Resync Enforce – Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies, enforcing these hierarchies to match the linked data (i.e. ignoring existing overrides on data-blocks pointer properties).

    * `OVERRIDE_LIBRARY_DELETE_HIERARCHY` Delete – Delete the selected local overrides (including their hierarchies of override dependencies) and relink their usages to the linked data-blocks.

  * **selection_set** (enum in [`SELECTED`, `CONTENT`, `SELECTED_AND_CONTENT`], (optional)) – 

Selection Set, Over which part of the tree items to apply the operation

    * `SELECTED` Selected – Apply the operation over selected data-blocks only.

    * `CONTENT` Content – Apply the operation over content of the selected items only (the data-blocks in their sub-tree).

    * `SELECTED_AND_CONTENT` Selected & Content – Apply the operation over selected data-blocks and all their dependencies.

bpy.ops.outliner.material_drop()¶

    

Drag material to object in Outliner

bpy.ops.outliner.modifier_operation(_*_ , _type =APPLY_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**type** (enum in [`APPLY`, `DELETE`, `TOGVIS`, `TOGREN`], (optional)) –
Modifier Operation

bpy.ops.outliner.object_operation(_*_ , _type =SELECT_)¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

Parameters:

    

**type** (enum in [`SELECT`, `DESELECT`, `SELECT_HIERARCHY`, `REMAP`,
`RENAME`], (optional)) –

Object Operation

  * `SELECT` Select.

  * `DESELECT` Deselect.

  * `SELECT_HIERARCHY` Select Hierarchy.

  * `REMAP` Remap Users – Make all users of selected data-blocks to use instead a new chosen one.

  * `RENAME` Rename.

bpy.ops.outliner.operation()¶

    

Context menu for item operations

bpy.ops.outliner.orphans_manage()¶

    

Open a window to manage unused data

bpy.ops.outliner.orphans_purge(_*_ , _do_local_ids =True_, _do_linked_ids
=True_, _do_recursive =True_)¶

    

Clear all orphaned data-blocks without any users from the file

Parameters:

    

  * **do_local_ids** (_boolean_ _,__(__optional_ _)_) – Local Data-blocks, Include unused local data-blocks into deletion

  * **do_linked_ids** (_boolean_ _,__(__optional_ _)_) – Linked Data-blocks, Include unused linked data-blocks into deletion

  * **do_recursive** (_boolean_ _,__(__optional_ _)_) – Recursive Delete, Recursively check for indirectly unused data-blocks, ensuring that no orphaned data-blocks remain after execution

bpy.ops.outliner.parent_clear()¶

    

Drag to clear parent in Outliner

bpy.ops.outliner.parent_drop()¶

    

Drag to parent in Outliner

bpy.ops.outliner.scene_drop()¶

    

Drag object to scene in Outliner

bpy.ops.outliner.scene_operation(_*_ , _type =DELETE_)¶

    

Context menu for scene operations

Parameters:

    

**type** (enum in [`DELETE`], (optional)) – Scene Operation

bpy.ops.outliner.scroll_page(_*_ , _up =False_)¶

    

Scroll page up or down

Parameters:

    

**up** (_boolean_ _,__(__optional_ _)_) – Up, Scroll up one page

bpy.ops.outliner.select_all(_*_ , _action =TOGGLE_)¶

    

Toggle the Outliner selection of items

Parameters:

    

**action** (enum in [`TOGGLE`, `SELECT`, `DESELECT`, `INVERT`], (optional)) –

Action, Selection action to execute

  * `TOGGLE` Toggle – Toggle selection for all elements.

  * `SELECT` Select – Select all elements.

  * `DESELECT` Deselect – Deselect all elements.

  * `INVERT` Invert – Invert selection of all elements.

bpy.ops.outliner.select_box(_*_ , _tweak =False_, _xmin =0_, _xmax =0_, _ymin
=0_, _ymax =0_, _wait_for_input =True_, _mode =SET_)¶

    

Use box selection to select tree elements

Parameters:

    

  * **tweak** (_boolean_ _,__(__optional_ _)_) – Tweak, Tweak gesture from empty space for box selection

  * **xmin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Min

  * **xmax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – X Max

  * **ymin** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Min

  * **ymax** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) – Y Max

  * **wait_for_input** (_boolean_ _,__(__optional_ _)_) – Wait for Input

  * **mode** (enum in [`SET`, `ADD`, `SUB`], (optional)) – 

Mode

    * `SET` Set – Set a new selection.

    * `ADD` Extend – Extend existing selection.

    * `SUB` Subtract – Subtract existing selection.

bpy.ops.outliner.select_walk(_*_ , _direction =UP_, _extend =False_,
_toggle_all =False_)¶

    

Use walk navigation to select tree elements

Parameters:

    

  * **direction** (enum in [`UP`, `DOWN`, `LEFT`, `RIGHT`], (optional)) – Walk Direction, Select/Deselect element in this direction

  * **extend** (_boolean_ _,__(__optional_ _)_) – Extend, Extend selection on walk

  * **toggle_all** (_boolean_ _,__(__optional_ _)_) – Toggle All, Toggle open/close hierarchy

bpy.ops.outliner.show_active()¶

    

Open up the tree and adjust the view so that the active object is shown
centered

bpy.ops.outliner.show_hierarchy()¶

    

Open all object entries and close all others

bpy.ops.outliner.show_one_level(_*_ , _open =True_)¶

    

Expand/collapse all entries by one level

Parameters:

    

**open** (_boolean_ _,__(__optional_ _)_) – Open, Expand all entries one level
deep

bpy.ops.outliner.start_filter()¶

    

Start entering filter text

bpy.ops.outliner.unhide_all()¶

    

Unhide all objects and collections

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

