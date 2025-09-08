---
url: https://docs.blender.org/api/current/bpy.ops.ui.html
scraped_at: 2025-09-08T14:18:57.666359
title: Ui Operators¶
---

# Ui Operators¶

bpy.ops.ui.assign_default_button()¶

    

Set this property’s current value as the new default

bpy.ops.ui.button_execute(_*_ , _skip_depressed =False_)¶

    

Presses active button

Parameters:

    

**skip_depressed** (_boolean_ _,__(__optional_ _)_) – Skip Depressed

bpy.ops.ui.button_string_clear()¶

    

Unsets the text of the active button

bpy.ops.ui.copy_as_driver_button()¶

    

Create a new driver with this property as input, and copy it to the internal
clipboard. Use Paste Driver to add it to the target property, or Paste Driver
Variables to extend an existing driver

bpy.ops.ui.copy_data_path_button(_*_ , _full_path =False_)¶

    

Copy the RNA data path for this property to the clipboard

Parameters:

    

**full_path** (_boolean_ _,__(__optional_ _)_) – full_path, Copy full data
path

bpy.ops.ui.copy_driver_to_selected_button(_*_ , _all =False_)¶

    

Copy the property’s driver from the active item to the same property of all
selected items, if the same property exists

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Copy to selected the drivers
of all elements of the array

bpy.ops.ui.copy_python_command_button()¶

    

Copy the Python command matching this button

bpy.ops.ui.copy_to_selected_button(_*_ , _all =True_)¶

    

Copy the property’s value from the active item to the same property of all
selected items if the same property exists

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Copy to selected all elements
of the array

bpy.ops.ui.drop_color(_*_ , _color =(0.0, 0.0, 0.0, 0.0)_, _gamma =False_,
_has_alpha =False_)¶

    

Drop colors to buttons

Parameters:

    

  * **color** (_float array_ _of_ _4 items in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Color, Source color

  * **gamma** (_boolean_ _,__(__optional_ _)_) – Gamma Corrected, The source color is gamma corrected

  * **has_alpha** (_boolean_ _,__(__optional_ _)_) – Has Alpha, The source color contains an Alpha component

bpy.ops.ui.drop_material(_*_ , _session_uid =0_)¶

    

Drag material to Material slots in Properties

Parameters:

    

**session_uid** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Session UID, Session UID of the data-block to use by the operator

bpy.ops.ui.drop_name(_*_ , _string =''_)¶

    

Drop name to button

Parameters:

    

**string** (_string_ _,__(__optional_ _,__never None_ _)_) – String, The
string value to drop into the button

bpy.ops.ui.editsource()¶

    

Edit UI source code of the active button

bpy.ops.ui.eyedropper_bone()¶

    

Sample a bone from the 3D View or the Outliner to store in a property

bpy.ops.ui.eyedropper_color(_*_ , _prop_data_path =''_)¶

    

Sample a color from the Blender window to store in a property

Parameters:

    

**prop_data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Data
Path, Path of property to be set with the depth

bpy.ops.ui.eyedropper_colorramp()¶

    

Sample a color band

bpy.ops.ui.eyedropper_colorramp_point()¶

    

Point-sample a color band

bpy.ops.ui.eyedropper_depth(_*_ , _prop_data_path =''_)¶

    

Sample depth from the 3D view

Parameters:

    

**prop_data_path** (_string_ _,__(__optional_ _,__never None_ _)_) – Data
Path, Path of property to be set with the depth

bpy.ops.ui.eyedropper_driver(_*_ , _mapping_type =SINGLE_MANY_)¶

    

Pick a property to use as a driver target

Parameters:

    

**mapping_type** (enum in [`SINGLE_MANY`, `DIRECT`, `MATCH`, `NONE_ALL`,
`NONE_SINGLE`], (optional)) –

Mapping Type, Method used to match target and driven properties

  * `SINGLE_MANY` All from Target – Drive all components of this property using the target picked.

  * `DIRECT` Single from Target – Drive this component of this property using the target picked.

  * `MATCH` Match Indices – Create drivers for each pair of corresponding elements.

  * `NONE_ALL` Manually Create Later – Create drivers for all properties without assigning any targets yet.

  * `NONE_SINGLE` Manually Create Later (Single) – Create driver for this property only and without assigning any targets yet.

bpy.ops.ui.eyedropper_grease_pencil_color(_*_ , _mode =MATERIAL_,
_material_mode =STROKE_)¶

    

Sample a color from the Blender Window and create Grease Pencil material

Parameters:

    

  * **mode** (enum in [`MATERIAL`, `PALETTE`, `BRUSH`], (optional)) – Mode

  * **material_mode** (enum in [`STROKE`, `FILL`, `BOTH`], (optional)) – Material Mode

bpy.ops.ui.eyedropper_id()¶

    

Sample a data-block from the 3D View to store in a property

bpy.ops.ui.jump_to_target_button()¶

    

Switch to the target object or bone

bpy.ops.ui.list_start_filter()¶

    

Start entering filter text for the list in focus

bpy.ops.ui.override_idtemplate_clear()¶

    

Delete the selected local override and relink its usages to the linked data-
block if possible, else reset it and mark it as non editable

bpy.ops.ui.override_idtemplate_make()¶

    

Create a local override of the selected linked data-block, and its hierarchy
of dependencies

bpy.ops.ui.override_idtemplate_reset()¶

    

Reset the selected local override to its linked reference values

bpy.ops.ui.override_remove_button(_*_ , _all =True_)¶

    

Remove an override operation

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Reset to default values all
elements of the array

bpy.ops.ui.override_type_set_button(_*_ , _all =True_, _type =REPLACE_)¶

    

Create an override operation, or set the type of an existing one

Parameters:

    

  * **all** (_boolean_ _,__(__optional_ _)_) – All, Reset to default values all elements of the array

  * **type** (enum in [`NOOP`, `REPLACE`, `DIFFERENCE`, `FACTOR`], (optional)) – 

Type, Type of override operation

    * `NOOP` NoOp – ‘No-Operation’, place holder preventing automatic override to ever affect the property.

    * `REPLACE` Replace – Completely replace value from linked data by local one.

    * `DIFFERENCE` Difference – Store difference to linked data value.

    * `FACTOR` Factor – Store factor to linked data value (useful e.g. for scale).

bpy.ops.ui.reloadtranslation()¶

    

Force a full reload of UI translation

bpy.ops.ui.reset_default_button(_*_ , _all =True_)¶

    

Reset this property’s value to its default value

Parameters:

    

**all** (_boolean_ _,__(__optional_ _)_) – All, Reset to default values all
elements of the array

bpy.ops.ui.unset_property_button()¶

    

Clear the property and use default or generated value in operators

bpy.ops.ui.view_drop()¶

    

Drag and drop onto a data-set or item within the data-set

bpy.ops.ui.view_item_rename()¶

    

Rename the active item in the data-set view

bpy.ops.ui.view_scroll()¶

    

Undocumented, consider [contributing](https://developer.blender.org/).

bpy.ops.ui.view_start_filter()¶

    

Start entering filter text for the data-set in focus

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

