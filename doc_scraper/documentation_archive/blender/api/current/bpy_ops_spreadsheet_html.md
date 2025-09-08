---
url: https://docs.blender.org/api/current/bpy.ops.spreadsheet.html
scraped_at: 2025-09-08T14:18:51.609166
title: Spreadsheet Operators¶
---

# Spreadsheet Operators¶

bpy.ops.spreadsheet.add_row_filter_rule()¶

    

Add a filter to remove rows from the displayed data

bpy.ops.spreadsheet.change_spreadsheet_data_source(_*_ , _component_type =0_,
_attribute_domain_type =0_)¶

    

Change visible data source in the spreadsheet

Parameters:

    

  * **component_type** (_int in_ _[__0_ _,__32767_ _]__,__(__optional_ _)_) – Component Type

  * **attribute_domain_type** (_int in_ _[__0_ _,__32767_ _]__,__(__optional_ _)_) – Attribute Domain Type

bpy.ops.spreadsheet.fit_column()¶

    

Resize a spreadsheet column to the width of the data

bpy.ops.spreadsheet.remove_row_filter_rule(_*_ , _index =0_)¶

    

Remove a row filter from the rules

Parameters:

    

**index** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Index

bpy.ops.spreadsheet.reorder_columns()¶

    

Change the order of columns

bpy.ops.spreadsheet.resize_column()¶

    

Resize a spreadsheet column

bpy.ops.spreadsheet.toggle_pin()¶

    

Turn on or off pinning

File:

    

[startup/bl_operators/spreadsheet.py:21](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/spreadsheet.py#L21)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

