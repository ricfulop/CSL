---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_Skin.htm
scraped_at: 2025-09-08T16:14:47.887309
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_Skin Class](../html/T_Grasshopper_GUI_Canvas_GH_Skin.htm "GH_Skin Class")

[GH_Skin Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Skin.htm
"GH_Skin Methods")

[GH_Skin Fields](../html/Fields_T_Grasshopper_GUI_Canvas_GH_Skin.htm "GH_Skin
Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Skin Class  
  
---  
  
Provides static access to typical Palletes and other GUI colours.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.CanvasGH_Skin  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_Skin
    
    
    Public NotInheritable Class GH_Skin

The GH_Skin type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[LoadSkin](M_Grasshopper_GUI_Canvas_GH_Skin_LoadSkin.htm)|  Instantiate all
palette and gui defaults. This function reads the colour values out of
grasshopper_gui.xml settings database if it exists.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SaveSkin](M_Grasshopper_GUI_Canvas_GH_Skin_SaveSkin.htm)|  Store all palette
and gui defaults. This function writes the colour values out to
grasshopper_gui.xml settings database.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[canvas_back](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_back.htm)|  Specifies
canvas background colour.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[canvas_edge](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_edge.htm)|  Specifies
canvas edge colour.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[canvas_grid](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_grid.htm)|  Specifies
canvas grid colour.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[canvas_grid_col](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_grid_col.htm)|
Specifies the interval of the canvas grid columns.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[canvas_grid_row](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_grid_row.htm)|
Specifies the interval of the canvas grid rows.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[canvas_mono](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_mono.htm)|  Canvas
monochromatic flag. If True, the canvas background is a solid colour.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[canvas_mono_color](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_mono_color.htm)|
If canvas_mono is set to true, this colour specified the solid background fill
for the canvas.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[canvas_shade](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_shade.htm)|  Specifies
the colour of the canvas drop shadow.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[canvas_shade_size](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_shade_size.htm)|
Specifies the size of the canvas drop shadow.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[group_back](F_Grasshopper_GUI_Canvas_GH_Skin_group_back.htm)|  Specifies the
default fill colour for Group objects.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_black_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_black_selected.htm)|
Black palette, selected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_black_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_black_standard.htm)|
Black palette, unselected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_blue_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_blue_selected.htm)|
Blue palette, selected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_blue_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_blue_standard.htm)|
Blue palette, unselected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_brown_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_brown_selected.htm)|
Brown palette, selected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_brown_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_brown_standard.htm)|
Brown palette, unselected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_error_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_error_selected.htm)|
Errors, selected palette. Default background for parameters and components
that carry errors.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_error_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_error_standard.htm)|
Errors, unselected palette. Default background for parameters and components
that carry errors.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_grey_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_grey_selected.htm)|
Grey palette, selected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_grey_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_grey_standard.htm)|
Grey palette, unselected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_hidden_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_hidden_selected.htm)|
Hidden, selected palette. Default background for PanelHidden (preview=off)
parameters and components.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_hidden_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_hidden_standard.htm)|
Hidden, unselected palette. Default background for PanelHidden (preview=off)
parameters and components.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_locked_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_locked_selected.htm)|
Locked, selected palette. Default background for locked parameters and
components.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_locked_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_locked_standard.htm)|
Locked, unselected palette. Default background for locked parameters and
components.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_normal_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_normal_selected.htm)|
Normal, selected palette. Default background for parameters and components.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_normal_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_normal_standard.htm)|
Normal, unselected palette. Default background for parameters and components.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_pink_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_pink_selected.htm)|
Pink palette, selected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_pink_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_pink_standard.htm)|
Pink palette, unselected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_trans_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_trans_selected.htm)|
Transparent palette, selected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_trans_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_trans_standard.htm)|
Transparent palette, unselected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_warning_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_warning_selected.htm)|
Warnings, selected palette. Default background for parameters and components
that carry warnings.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_warning_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_warning_standard.htm)|
Warnings, unselected palette. Default background for parameters and components
that carry warnings.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_white_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_white_selected.htm)|
White palette, selected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[palette_white_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_white_standard.htm)|
White palette, unselected.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[panel_back](F_Grasshopper_GUI_Canvas_GH_Skin_panel_back.htm)|  Specifies the
default fill colour for Panel objects.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[wire_default](F_Grasshopper_GUI_Canvas_GH_Skin_wire_default.htm)|  Specifies
the default wire colour.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[wire_empty](F_Grasshopper_GUI_Canvas_GH_Skin_wire_empty.htm)|  Specifies the
colour for empty (null) wires.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[wire_selected_a](F_Grasshopper_GUI_Canvas_GH_Skin_wire_selected_a.htm)|
Specifies the colour for wires at the selected end.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[wire_selected_b](F_Grasshopper_GUI_Canvas_GH_Skin_wire_selected_b.htm)|
Specifies the colour for wires at the unselected end.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[zui_edge](F_Grasshopper_GUI_Canvas_GH_Skin_zui_edge.htm)|  Specifies the
default edge colour for ZUI elements.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[zui_edge_highlight](F_Grasshopper_GUI_Canvas_GH_Skin_zui_edge_highlight.htm)|
Specifies the default edge colour for highlighted ZUI elements.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[zui_fill](F_Grasshopper_GUI_Canvas_GH_Skin_zui_fill.htm)|  Specifies the
default fill colour for ZUI elements.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[zui_fill_highlight](F_Grasshopper_GUI_Canvas_GH_Skin_zui_fill_highlight.htm)|
Specifies the default fill colour for highlighted ZUI elements.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

