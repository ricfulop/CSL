---
url: https://docs.blender.org/api/current/bpy.ops.render.html
scraped_at: 2025-09-08T14:18:42.586498
title: Render Operators¶
---

# Render Operators¶

bpy.ops.render.color_management_white_balance_preset_add(_*_ , _name =''_,
_remove_name =False_, _remove_active =False_)¶

    

Add or remove a white balance preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.render.cycles_integrator_preset_add(_*_ , _name =''_, _remove_name
=False_, _remove_active =False_)¶

    

Add an Integrator Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.render.cycles_performance_preset_add(_*_ , _name =''_, _remove_name
=False_, _remove_active =False_)¶

    

Add an Performance Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.render.cycles_sampling_preset_add(_*_ , _name =''_, _remove_name
=False_, _remove_active =False_)¶

    

Add a Sampling Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.render.cycles_viewport_sampling_preset_add(_*_ , _name =''_,
_remove_name =False_, _remove_active =False_)¶

    

Add a Viewport Sampling Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.render.eevee_raytracing_preset_add(_*_ , _name =''_, _remove_name
=False_, _remove_active =False_)¶

    

Add or remove an EEVEE ray-tracing preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.render.opengl(_*_ , _animation =False_, _render_keyed_only =False_,
_sequencer =False_, _write_still =False_, _view_context =True_)¶

    

Take a snapshot of the active viewport

Parameters:

    

  * **animation** (_boolean_ _,__(__optional_ _)_) – Animation, Render files from the animation range of this scene

  * **render_keyed_only** (_boolean_ _,__(__optional_ _)_) – Render Keyframes Only, Render only those frames where selected objects have a key in their animation data. Only used when rendering animation

  * **sequencer** (_boolean_ _,__(__optional_ _)_) – Sequencer, Render using the sequencer’s OpenGL display

  * **write_still** (_boolean_ _,__(__optional_ _)_) – Write Image, Save the rendered image to the output path (used only when animation is disabled)

  * **view_context** (_boolean_ _,__(__optional_ _)_) – View Context, Use the current 3D view for rendering, else use scene settings

bpy.ops.render.play_rendered_anim()¶

    

Play back rendered frames/movies using an external player

File:

    

[startup/bl_operators/screen_play_rendered_anim.py:87](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/screen_play_rendered_anim.py#L87)

bpy.ops.render.preset_add(_*_ , _name =''_, _remove_name =False_,
_remove_active =False_)¶

    

Add or remove a Render Preset

Parameters:

    

  * **name** (_string_ _,__(__optional_ _,__never None_ _)_) – Name, Name of the preset, used to make the path name

  * **remove_name** (_boolean_ _,__(__optional_ _)_) – remove_name

  * **remove_active** (_boolean_ _,__(__optional_ _)_) – remove_active

File:

    

[startup/bl_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.render.render(_*_ , _animation =False_, _write_still =False_,
_use_viewport =False_, _layer =''_, _scene =''_)¶

    

Render active scene

Parameters:

    

  * **animation** (_boolean_ _,__(__optional_ _)_) – Animation, Render files from the animation range of this scene

  * **write_still** (_boolean_ _,__(__optional_ _)_) – Write Image, Save the rendered image to the output path (used only when animation is disabled)

  * **use_viewport** (_boolean_ _,__(__optional_ _)_) – Use 3D Viewport, When inside a 3D viewport, use layers and camera of the viewport

  * **layer** (_string_ _,__(__optional_ _,__never None_ _)_) – Render Layer, Single render layer to re-render (used only when animation is disabled)

  * **scene** (_string_ _,__(__optional_ _,__never None_ _)_) – Scene, Scene to render, current scene if not specified

bpy.ops.render.shutter_curve_preset(_*_ , _shape =SMOOTH_)¶

    

Set shutter curve

Parameters:

    

**shape** (enum in [`SHARP`, `SMOOTH`, `MAX`, `LINE`, `ROUND`, `ROOT`],
(optional)) – Mode

bpy.ops.render.view_cancel()¶

    

Cancel show render view

bpy.ops.render.view_show()¶

    

Toggle show render view

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

