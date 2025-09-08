---
url: https://freecad.github.io/SourceDoc/d7/dcd/classautomotive__design_1_1view__volume.html
scraped_at: 2025-09-08T15:15:23.583536
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [view_volume](../../d7/dcd/classautomotive__design_1_1view__volume.html)

[List of all members](../../d5/dca/classautomotive__design_1_1view__volume-members.html) | Public Member Functions | Public Attributes

automotive_design.view_volume Class Reference

##  Public Member Functions  
  
---  
def | [back_plane_clipping](../../d7/dcd/classautomotive__design_1_1view__volume.html#adf01712b4b11b4632abf33f0cd95989f) ()  
def | [back_plane_distance](../../d7/dcd/classautomotive__design_1_1view__volume.html#adc12b99bfc675231e95af94f5d0cedda) ()  
def | [front_plane_clipping](../../d7/dcd/classautomotive__design_1_1view__volume.html#a4406d52657cd43574274f7a86963a3da) ()  
def | [front_plane_distance](../../d7/dcd/classautomotive__design_1_1view__volume.html#abb072798b1ddab37db154a96a88a7bb6) ()  
def | [projection_point](../../d7/dcd/classautomotive__design_1_1view__volume.html#a11ab8c1cb96d486ef30725dc7f7208b2) ()  
def | [projection_type](../../d7/dcd/classautomotive__design_1_1view__volume.html#a82cc23ad0b91c1f5098caedc882b8268) ()  
def | [view_plane_distance](../../d7/dcd/classautomotive__design_1_1view__volume.html#acec91fd4886ebe4461a5dd362f29ccd3) ()  
def | [view_volume_sides_clipping](../../d7/dcd/classautomotive__design_1_1view__volume.html#a2f9f7d52cebcc1c5f2175470895dcd17) ()  
def | [view_window](../../d7/dcd/classautomotive__design_1_1view__volume.html#af9054e11085972a40f029cf9a42f499c) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.founded_item](../../d4/d12/classautomotive__design_1_1founded__item.html)  
def | [users](../../d4/d12/classautomotive__design_1_1founded__item.html#a0299c3fccdb8223cc8c9f590f7cee9a5) ()  
def | [wr1](../../d4/d12/classautomotive__design_1_1founded__item.html#a0668b2127d1c208daa93b2d435855a7f) (self)  
def | [wr2](../../d4/d12/classautomotive__design_1_1founded__item.html#a1ef4a4f4c94d46b616c25ec02609838f) (self)  
  
##  Public Attributes  
  
---  
|
[back_plane_clipping](../../d7/dcd/classautomotive__design_1_1view__volume.html#a89881a5ab06474248012bd7979543995)  
|
[back_plane_distance](../../d7/dcd/classautomotive__design_1_1view__volume.html#a9cf41d9b6ca320ed8d295c6a52d69311)  
|
[front_plane_clipping](../../d7/dcd/classautomotive__design_1_1view__volume.html#a50a95bfec056404d720fb3bcc41a7bea)  
|
[front_plane_distance](../../d7/dcd/classautomotive__design_1_1view__volume.html#a1846691b5f709db271758a44e9e07ffe)  
|
[projection_point](../../d7/dcd/classautomotive__design_1_1view__volume.html#ac951cb68023343eeb756ee948283a495)  
|
[projection_type](../../d7/dcd/classautomotive__design_1_1view__volume.html#afeb495636d54cd3e7e7e42d5bd4b75c1)  
|
[view_plane_distance](../../d7/dcd/classautomotive__design_1_1view__volume.html#ad93b855d4fb987b933a0b49bbc188e41)  
|
[view_volume_sides_clipping](../../d7/dcd/classautomotive__design_1_1view__volume.html#a653b34fc36858c578815d43443a9d62e)  
|
[view_window](../../d7/dcd/classautomotive__design_1_1view__volume.html#a26722d1eee7b5e45fd333421a4659524)  
  
## Detailed Description

    
    
    Entity view_volume definition.
    
        :param projection_type
        :type projection_type:central_or_parallel
    
        :param projection_point
        :type projection_point:cartesian_point
    
        :param view_plane_distance
        :type view_plane_distance:length_measure
    
        :param front_plane_distance
        :type front_plane_distance:length_measure
    
        :param front_plane_clipping
        :type front_plane_clipping:BOOLEAN
    
        :param back_plane_distance
        :type back_plane_distance:length_measure
    
        :param back_plane_clipping
        :type back_plane_clipping:BOOLEAN
    
        :param view_volume_sides_clipping
        :type view_volume_sides_clipping:BOOLEAN
    
        :param view_window
        :type view_window:planar_box

## Member Function Documentation

## ◆ back_plane_clipping()

def automotive_design.view_volume.back_plane_clipping  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.view_volume._back_plane_clipping,
and automotive_design.view_volume._back_plane_clipping.

## ◆ back_plane_distance()

def automotive_design.view_volume.back_plane_distance  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.view_volume._back_plane_distance,
and automotive_design.view_volume._back_plane_distance.

## ◆ front_plane_clipping()

def automotive_design.view_volume.front_plane_clipping  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.view_volume._front_plane_clipping,
and automotive_design.view_volume._front_plane_clipping.

## ◆ front_plane_distance()

def automotive_design.view_volume.front_plane_distance  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.view_volume._front_plane_distance,
and automotive_design.view_volume._front_plane_distance.

## ◆ projection_point()

def automotive_design.view_volume.projection_point  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.view_volume._projection_point,
and automotive_design.view_volume._projection_point.

## ◆ projection_type()

def automotive_design.view_volume.projection_type  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.view_volume._projection_type,
and automotive_design.view_volume._projection_type.

## ◆ view_plane_distance()

def automotive_design.view_volume.view_plane_distance  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.view_volume._view_plane_distance,
and automotive_design.view_volume._view_plane_distance.

## ◆ view_volume_sides_clipping()

def automotive_design.view_volume.view_volume_sides_clipping  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.view_volume._view_volume_sides_clipping,
and automotive_design.view_volume._view_volume_sides_clipping.

## ◆ view_window()

def automotive_design.view_volume.view_window  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.view_volume._view_window,
automotive_design.camera_model_d2._view_window, and
automotive_design.view_volume._view_window.

## Member Data Documentation

## ◆ back_plane_clipping

automotive_design.view_volume.back_plane_clipping  
---  
  
## ◆ back_plane_distance

automotive_design.view_volume.back_plane_distance  
---  
  
## ◆ front_plane_clipping

automotive_design.view_volume.front_plane_clipping  
---  
  
## ◆ front_plane_distance

automotive_design.view_volume.front_plane_distance  
---  
  
## ◆ projection_point

automotive_design.view_volume.projection_point  
---  
  
## ◆ projection_type

automotive_design.view_volume.projection_type  
---  
  
## ◆ view_plane_distance

automotive_design.view_volume.view_plane_distance  
---  
  
## ◆ view_volume_sides_clipping

automotive_design.view_volume.view_volume_sides_clipping  
---  
  
## ◆ view_window

automotive_design.view_volume.view_window  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

