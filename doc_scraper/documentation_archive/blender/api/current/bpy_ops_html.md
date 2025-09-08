---
url: https://docs.blender.org/api/current/bpy.ops.html
scraped_at: 2025-09-08T14:17:47.361901
title: Operators (bpy.ops)¶
---

# Operators (bpy.ops)¶

## Calling Operators¶

Provides Python access to calling operators, this includes operators written
in C++, Python or macros.

Only keyword arguments can be used to pass operator properties.

Operators don’t have return values as you might expect, instead they return a
set() which is made up of: `{'RUNNING_MODAL', 'CANCELLED', 'FINISHED',
'PASS_THROUGH'}`. Common return values are `{'FINISHED'}` and `{'CANCELLED'}`,
the latter meaning that the operator execution was aborted without making any
changes or saving an undo history entry.

If operator was cancelled but there wasn’t any reports from it with
`{'ERROR'}` type, it will just return `{'CANCELLED'}` without raising any
exceptions. However, if there are error reports, a `RuntimeError` will be
raised after the operator finishes execution, including all error report
messages, regardless of the return status (even if it was `{'FINISHED'}`).

Calling an operator in the wrong context will raise a `RuntimeError`, there is
a poll() method to avoid this problem.

Note that the operator ID (bl_idname) in this example is `mesh.subdivide`,
`bpy.ops` is just the access path for Python.

### Keywords and Positional Arguments¶

For calling operators keywords are used for operator properties and positional
arguments are used to define how the operator is called.

There are 2 optional positional arguments (documented in detail below).

    
    
    bpy.ops.test.operator(execution_context, undo)
    

  * execution_context - `str` (enum).

  * undo - `bool` type.

Each of these arguments is optional, but must be given in the order above.

    
    
    import bpy
    
    # Calling an operator.
    bpy.ops.mesh.subdivide(number_cuts=3, smoothness=0.5)
    
    
    # Check poll() to avoid exception.
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='EDIT')
    

## Overriding Context¶

It is possible to override context members that the operator sees, so that
they act on specified rather than the selected or active data, or to execute
an operator in the different part of the user interface.

The context overrides are passed in as keyword arguments, with keywords
matching the context member names in `bpy.context`. For example to override
`bpy.context.active_object`, you would pass `active_object=object` to
[`bpy.types.Context.temp_override`](bpy.types.Context.html#bpy.types.Context.temp_override
"bpy.types.Context.temp_override").

Note

You will nearly always want to use a copy of the actual current context as
basis (otherwise, you’ll have to find and gather all needed data yourself).

Note

Context members are names which Blender uses for data access, overrides do not
extend to overriding methods or any Python specific functionality.

    
    
    # Remove all objects in scene rather than the selected ones.
    import bpy
    from bpy import context
    context_override = context.copy()
    context_override["selected_objects"] = list(context.scene.objects)
    with context.temp_override(**context_override):
        bpy.ops.object.delete()
    

## Execution Context¶

When calling an operator you may want to pass the execution context.

This determines the context that is given for the operator to run in, and
whether invoke() is called or only execute().

`EXEC_DEFAULT` is used by default, running only the `execute()` method, but
you may want the operator to take user interaction with `INVOKE_DEFAULT` which
will also call invoke() if existing.

The execution context is one of:

  * `INVOKE_DEFAULT`

  * `INVOKE_REGION_WIN`

  * `INVOKE_REGION_CHANNELS`

  * `INVOKE_REGION_PREVIEW`

  * `INVOKE_AREA`

  * `INVOKE_SCREEN`

  * `EXEC_DEFAULT`

  * `EXEC_REGION_WIN`

  * `EXEC_REGION_CHANNELS`

  * `EXEC_REGION_PREVIEW`

  * `EXEC_AREA`

  * `EXEC_SCREEN`

    
    
    # Collection add popup.
    import bpy
    bpy.ops.object.collection_instance_add('INVOKE_DEFAULT')
    

It is also possible to run an operator in a particular part of the user
interface. For this we need to pass the window, area and sometimes a region.

    
    
    # Maximize 3d view in all windows.
    import bpy
    from bpy import context
    
    for window in context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                with context.temp_override(window=window, area=area):
                    bpy.ops.screen.screen_full_area()
                break
    

Submodules

  * [Action Operators](bpy.ops.action.html)
  * [Anim Operators](bpy.ops.anim.html)
  * [Armature Operators](bpy.ops.armature.html)
  * [Asset Operators](bpy.ops.asset.html)
  * [Boid Operators](bpy.ops.boid.html)
  * [Brush Operators](bpy.ops.brush.html)
  * [Buttons Operators](bpy.ops.buttons.html)
  * [Cachefile Operators](bpy.ops.cachefile.html)
  * [Camera Operators](bpy.ops.camera.html)
  * [Clip Operators](bpy.ops.clip.html)
  * [Cloth Operators](bpy.ops.cloth.html)
  * [Collection Operators](bpy.ops.collection.html)
  * [Console Operators](bpy.ops.console.html)
  * [Constraint Operators](bpy.ops.constraint.html)
  * [Curve Operators](bpy.ops.curve.html)
  * [Curves Operators](bpy.ops.curves.html)
  * [Cycles Operators](bpy.ops.cycles.html)
  * [Dpaint Operators](bpy.ops.dpaint.html)
  * [Ed Operators](bpy.ops.ed.html)
  * [Export Anim Operators](bpy.ops.export_anim.html)
  * [Export Scene Operators](bpy.ops.export_scene.html)
  * [Extensions Operators](bpy.ops.extensions.html)
  * [File Operators](bpy.ops.file.html)
  * [Fluid Operators](bpy.ops.fluid.html)
  * [Font Operators](bpy.ops.font.html)
  * [Geometry Operators](bpy.ops.geometry.html)
  * [Gizmogroup Operators](bpy.ops.gizmogroup.html)
  * [Gpencil Operators](bpy.ops.gpencil.html)
  * [Graph Operators](bpy.ops.graph.html)
  * [Grease Pencil Operators](bpy.ops.grease_pencil.html)
  * [Image Operators](bpy.ops.image.html)
  * [Import Anim Operators](bpy.ops.import_anim.html)
  * [Import Curve Operators](bpy.ops.import_curve.html)
  * [Import Scene Operators](bpy.ops.import_scene.html)
  * [Info Operators](bpy.ops.info.html)
  * [Lattice Operators](bpy.ops.lattice.html)
  * [Marker Operators](bpy.ops.marker.html)
  * [Mask Operators](bpy.ops.mask.html)
  * [Material Operators](bpy.ops.material.html)
  * [Mball Operators](bpy.ops.mball.html)
  * [Mesh Operators](bpy.ops.mesh.html)
  * [Nla Operators](bpy.ops.nla.html)
  * [Node Operators](bpy.ops.node.html)
  * [Object Operators](bpy.ops.object.html)
  * [Outliner Operators](bpy.ops.outliner.html)
  * [Paint Operators](bpy.ops.paint.html)
  * [Paintcurve Operators](bpy.ops.paintcurve.html)
  * [Palette Operators](bpy.ops.palette.html)
  * [Particle Operators](bpy.ops.particle.html)
  * [Pointcloud Operators](bpy.ops.pointcloud.html)
  * [Pose Operators](bpy.ops.pose.html)
  * [Poselib Operators](bpy.ops.poselib.html)
  * [Preferences Operators](bpy.ops.preferences.html)
  * [Ptcache Operators](bpy.ops.ptcache.html)
  * [Render Operators](bpy.ops.render.html)
  * [Rigidbody Operators](bpy.ops.rigidbody.html)
  * [Scene Operators](bpy.ops.scene.html)
  * [Screen Operators](bpy.ops.screen.html)
  * [Script Operators](bpy.ops.script.html)
  * [Sculpt Operators](bpy.ops.sculpt.html)
  * [Sculpt Curves Operators](bpy.ops.sculpt_curves.html)
  * [Sequencer Operators](bpy.ops.sequencer.html)
  * [Sound Operators](bpy.ops.sound.html)
  * [Spreadsheet Operators](bpy.ops.spreadsheet.html)
  * [Surface Operators](bpy.ops.surface.html)
  * [Text Operators](bpy.ops.text.html)
  * [Text Editor Operators](bpy.ops.text_editor.html)
  * [Texture Operators](bpy.ops.texture.html)
  * [Transform Operators](bpy.ops.transform.html)
  * [Ui Operators](bpy.ops.ui.html)
  * [Uilist Operators](bpy.ops.uilist.html)
  * [Uv Operators](bpy.ops.uv.html)
  * [View2D Operators](bpy.ops.view2d.html)
  * [View3D Operators](bpy.ops.view3d.html)
  * [Wm Operators](bpy.ops.wm.html)
  * [Workspace Operators](bpy.ops.workspace.html)
  * [World Operators](bpy.ops.world.html)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

