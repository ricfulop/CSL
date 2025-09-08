---
url: https://docs.blender.org/api/current/bpy.ops.palette.html
scraped_at: 2025-09-08T14:18:35.535629
title: Palette Operators¶
---

# Palette Operators¶

bpy.ops.palette.color_add()¶

    

Add new color to active palette

bpy.ops.palette.color_delete()¶

    

Remove active color from palette

bpy.ops.palette.color_move(_*_ , _type =UP_)¶

    

Move the active Color up/down in the list

Parameters:

    

**type** (enum in [`UP`, `DOWN`], (optional)) – Type

bpy.ops.palette.extract_from_image(_*_ , _threshold =1_)¶

    

Extract all colors used in Image and create a Palette

Parameters:

    

**threshold** (_int in_ _[__-inf_ _,__inf_ _]__,__(__optional_ _)_) –
Threshold

bpy.ops.palette.join(_*_ , _palette =''_)¶

    

Join Palette Swatches

Parameters:

    

**palette** (_string_ _,__(__optional_ _,__never None_ _)_) – Palette, Name of
the Palette

bpy.ops.palette.new()¶

    

Add new palette

bpy.ops.palette.sort(_*_ , _type =HSV_)¶

    

Sort Palette Colors

Parameters:

    

**type** (enum in [`HSV`, `SVH`, `VHS`, `LUMINANCE`], (optional)) – Type

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

