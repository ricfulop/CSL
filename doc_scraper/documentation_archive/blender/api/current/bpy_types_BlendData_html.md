---
url: https://docs.blender.org/api/current/bpy.types.BlendData.html
scraped_at: 2025-09-08T14:20:07.949443
title: BlendData(bpy_struct)¶
---

# BlendData(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.BlendData(_bpy_struct_)¶

    

Main data structure representing a .blend file and all its data-blocks

actions¶

    

Action data-blocks

Type:

    

[`BlendDataActions`](bpy.types.BlendDataActions.html#bpy.types.BlendDataActions
"bpy.types.BlendDataActions")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Action`](bpy.types.Action.html#bpy.types.Action "bpy.types.Action"),
(readonly)

armatures¶

    

Armature data-blocks

Type:

    

[`BlendDataArmatures`](bpy.types.BlendDataArmatures.html#bpy.types.BlendDataArmatures
"bpy.types.BlendDataArmatures")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Armature`](bpy.types.Armature.html#bpy.types.Armature "bpy.types.Armature"),
(readonly)

brushes¶

    

Brush data-blocks

Type:

    

[`BlendDataBrushes`](bpy.types.BlendDataBrushes.html#bpy.types.BlendDataBrushes
"bpy.types.BlendDataBrushes")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Brush`](bpy.types.Brush.html#bpy.types.Brush "bpy.types.Brush"), (readonly)

cache_files¶

    

Cache Files data-blocks

Type:

    

[`BlendDataCacheFiles`](bpy.types.BlendDataCacheFiles.html#bpy.types.BlendDataCacheFiles
"bpy.types.BlendDataCacheFiles")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`CacheFile`](bpy.types.CacheFile.html#bpy.types.CacheFile
"bpy.types.CacheFile"), (readonly)

cameras¶

    

Camera data-blocks

Type:

    

[`BlendDataCameras`](bpy.types.BlendDataCameras.html#bpy.types.BlendDataCameras
"bpy.types.BlendDataCameras")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Camera`](bpy.types.Camera.html#bpy.types.Camera "bpy.types.Camera"),
(readonly)

collections¶

    

Collection data-blocks

Type:

    

[`BlendDataCollections`](bpy.types.BlendDataCollections.html#bpy.types.BlendDataCollections
"bpy.types.BlendDataCollections")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Collection`](bpy.types.Collection.html#bpy.types.Collection
"bpy.types.Collection"), (readonly)

curves¶

    

Curve data-blocks

Type:

    

[`BlendDataCurves`](bpy.types.BlendDataCurves.html#bpy.types.BlendDataCurves
"bpy.types.BlendDataCurves")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Curve`](bpy.types.Curve.html#bpy.types.Curve "bpy.types.Curve"), (readonly)

filepath¶

    

Path to the .blend file

Type:

    

string, default “”, (readonly, never None)

fonts¶

    

Vector font data-blocks

Type:

    

[`BlendDataFonts`](bpy.types.BlendDataFonts.html#bpy.types.BlendDataFonts
"bpy.types.BlendDataFonts")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`VectorFont`](bpy.types.VectorFont.html#bpy.types.VectorFont
"bpy.types.VectorFont"), (readonly)

grease_pencils¶

    

Annotation data-blocks (legacy Grease Pencil)

Type:

    

[`BlendDataGreasePencils`](bpy.types.BlendDataGreasePencils.html#bpy.types.BlendDataGreasePencils
"bpy.types.BlendDataGreasePencils")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`GreasePencil`](bpy.types.GreasePencil.html#bpy.types.GreasePencil
"bpy.types.GreasePencil"), (readonly)

grease_pencils_v3¶

    

Grease Pencil data-blocks

Type:

    

[`BlendDataGreasePencilsV3`](bpy.types.BlendDataGreasePencilsV3.html#bpy.types.BlendDataGreasePencilsV3
"bpy.types.BlendDataGreasePencilsV3")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`GreasePencilv3`](bpy.types.GreasePencilv3.html#bpy.types.GreasePencilv3
"bpy.types.GreasePencilv3"), (readonly)

hair_curves¶

    

Hair curve data-blocks

Type:

    

[`BlendDataHairCurves`](bpy.types.BlendDataHairCurves.html#bpy.types.BlendDataHairCurves
"bpy.types.BlendDataHairCurves")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Curves`](bpy.types.Curves.html#bpy.types.Curves "bpy.types.Curves"),
(readonly)

images¶

    

Image data-blocks

Type:

    

[`BlendDataImages`](bpy.types.BlendDataImages.html#bpy.types.BlendDataImages
"bpy.types.BlendDataImages")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Image`](bpy.types.Image.html#bpy.types.Image "bpy.types.Image"), (readonly)

is_dirty¶

    

Have recent edits been saved to disk

Type:

    

boolean, default False, (readonly)

is_saved¶

    

Has the current session been saved to disk as a .blend file

Type:

    

boolean, default False, (readonly)

lattices¶

    

Lattice data-blocks

Type:

    

[`BlendDataLattices`](bpy.types.BlendDataLattices.html#bpy.types.BlendDataLattices
"bpy.types.BlendDataLattices")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Lattice`](bpy.types.Lattice.html#bpy.types.Lattice "bpy.types.Lattice"),
(readonly)

libraries¶

    

Library data-blocks

Type:

    

[`BlendDataLibraries`](bpy.types.BlendDataLibraries.html#bpy.types.BlendDataLibraries
"bpy.types.BlendDataLibraries")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Library`](bpy.types.Library.html#bpy.types.Library "bpy.types.Library"),
(readonly)

lightprobes¶

    

Light Probe data-blocks

Type:

    

[`BlendDataProbes`](bpy.types.BlendDataProbes.html#bpy.types.BlendDataProbes
"bpy.types.BlendDataProbes")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`LightProbe`](bpy.types.LightProbe.html#bpy.types.LightProbe
"bpy.types.LightProbe"), (readonly)

lights¶

    

Light data-blocks

Type:

    

[`BlendDataLights`](bpy.types.BlendDataLights.html#bpy.types.BlendDataLights
"bpy.types.BlendDataLights")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Light`](bpy.types.Light.html#bpy.types.Light "bpy.types.Light"), (readonly)

linestyles¶

    

Line Style data-blocks

Type:

    

[`BlendDataLineStyles`](bpy.types.BlendDataLineStyles.html#bpy.types.BlendDataLineStyles
"bpy.types.BlendDataLineStyles")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`FreestyleLineStyle`](bpy.types.FreestyleLineStyle.html#bpy.types.FreestyleLineStyle
"bpy.types.FreestyleLineStyle"), (readonly)

masks¶

    

Masks data-blocks

Type:

    

[`BlendDataMasks`](bpy.types.BlendDataMasks.html#bpy.types.BlendDataMasks
"bpy.types.BlendDataMasks")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Mask`](bpy.types.Mask.html#bpy.types.Mask "bpy.types.Mask"), (readonly)

materials¶

    

Material data-blocks

Type:

    

[`BlendDataMaterials`](bpy.types.BlendDataMaterials.html#bpy.types.BlendDataMaterials
"bpy.types.BlendDataMaterials")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Material`](bpy.types.Material.html#bpy.types.Material "bpy.types.Material"),
(readonly)

meshes¶

    

Mesh data-blocks

Type:

    

[`BlendDataMeshes`](bpy.types.BlendDataMeshes.html#bpy.types.BlendDataMeshes
"bpy.types.BlendDataMeshes")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Mesh`](bpy.types.Mesh.html#bpy.types.Mesh "bpy.types.Mesh"), (readonly)

metaballs¶

    

Metaball data-blocks

Type:

    

[`BlendDataMetaBalls`](bpy.types.BlendDataMetaBalls.html#bpy.types.BlendDataMetaBalls
"bpy.types.BlendDataMetaBalls")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`MetaBall`](bpy.types.MetaBall.html#bpy.types.MetaBall "bpy.types.MetaBall"),
(readonly)

movieclips¶

    

Movie Clip data-blocks

Type:

    

[`BlendDataMovieClips`](bpy.types.BlendDataMovieClips.html#bpy.types.BlendDataMovieClips
"bpy.types.BlendDataMovieClips")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`MovieClip`](bpy.types.MovieClip.html#bpy.types.MovieClip
"bpy.types.MovieClip"), (readonly)

node_groups¶

    

Node group data-blocks

Type:

    

[`BlendDataNodeTrees`](bpy.types.BlendDataNodeTrees.html#bpy.types.BlendDataNodeTrees
"bpy.types.BlendDataNodeTrees")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`NodeTree`](bpy.types.NodeTree.html#bpy.types.NodeTree "bpy.types.NodeTree"),
(readonly)

objects¶

    

Object data-blocks

Type:

    

[`BlendDataObjects`](bpy.types.BlendDataObjects.html#bpy.types.BlendDataObjects
"bpy.types.BlendDataObjects")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Object`](bpy.types.Object.html#bpy.types.Object "bpy.types.Object"),
(readonly)

paint_curves¶

    

Paint Curves data-blocks

Type:

    

[`BlendDataPaintCurves`](bpy.types.BlendDataPaintCurves.html#bpy.types.BlendDataPaintCurves
"bpy.types.BlendDataPaintCurves")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`PaintCurve`](bpy.types.PaintCurve.html#bpy.types.PaintCurve
"bpy.types.PaintCurve"), (readonly)

palettes¶

    

Palette data-blocks

Type:

    

[`BlendDataPalettes`](bpy.types.BlendDataPalettes.html#bpy.types.BlendDataPalettes
"bpy.types.BlendDataPalettes")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Palette`](bpy.types.Palette.html#bpy.types.Palette "bpy.types.Palette"),
(readonly)

particles¶

    

Particle data-blocks

Type:

    

[`BlendDataParticles`](bpy.types.BlendDataParticles.html#bpy.types.BlendDataParticles
"bpy.types.BlendDataParticles")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`ParticleSettings`](bpy.types.ParticleSettings.html#bpy.types.ParticleSettings
"bpy.types.ParticleSettings"), (readonly)

pointclouds¶

    

Point cloud data-blocks

Type:

    

[`BlendDataPointClouds`](bpy.types.BlendDataPointClouds.html#bpy.types.BlendDataPointClouds
"bpy.types.BlendDataPointClouds")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`PointCloud`](bpy.types.PointCloud.html#bpy.types.PointCloud
"bpy.types.PointCloud"), (readonly)

scenes¶

    

Scene data-blocks

Type:

    

[`BlendDataScenes`](bpy.types.BlendDataScenes.html#bpy.types.BlendDataScenes
"bpy.types.BlendDataScenes")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Scene`](bpy.types.Scene.html#bpy.types.Scene "bpy.types.Scene"), (readonly)

screens¶

    

Screen data-blocks

Type:

    

[`BlendDataScreens`](bpy.types.BlendDataScreens.html#bpy.types.BlendDataScreens
"bpy.types.BlendDataScreens")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Screen`](bpy.types.Screen.html#bpy.types.Screen "bpy.types.Screen"),
(readonly)

shape_keys¶

    

Shape Key data-blocks

Type:

    

[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of [`Key`](bpy.types.Key.html#bpy.types.Key
"bpy.types.Key"), (readonly)

sounds¶

    

Sound data-blocks

Type:

    

[`BlendDataSounds`](bpy.types.BlendDataSounds.html#bpy.types.BlendDataSounds
"bpy.types.BlendDataSounds")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Sound`](bpy.types.Sound.html#bpy.types.Sound "bpy.types.Sound"), (readonly)

speakers¶

    

Speaker data-blocks

Type:

    

[`BlendDataSpeakers`](bpy.types.BlendDataSpeakers.html#bpy.types.BlendDataSpeakers
"bpy.types.BlendDataSpeakers")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Speaker`](bpy.types.Speaker.html#bpy.types.Speaker "bpy.types.Speaker"),
(readonly)

texts¶

    

Text data-blocks

Type:

    

[`BlendDataTexts`](bpy.types.BlendDataTexts.html#bpy.types.BlendDataTexts
"bpy.types.BlendDataTexts")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Text`](bpy.types.Text.html#bpy.types.Text "bpy.types.Text"), (readonly)

textures¶

    

Texture data-blocks

Type:

    

[`BlendDataTextures`](bpy.types.BlendDataTextures.html#bpy.types.BlendDataTextures
"bpy.types.BlendDataTextures")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Texture`](bpy.types.Texture.html#bpy.types.Texture "bpy.types.Texture"),
(readonly)

use_autopack¶

    

Automatically pack all external data into .blend file

Type:

    

boolean, default False

version¶

    

File format version the .blend file was saved with

Type:

    

int array of 3 items in [0, inf], default (0, 0, 0), (readonly)

volumes¶

    

Volume data-blocks

Type:

    

[`BlendDataVolumes`](bpy.types.BlendDataVolumes.html#bpy.types.BlendDataVolumes
"bpy.types.BlendDataVolumes")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`Volume`](bpy.types.Volume.html#bpy.types.Volume "bpy.types.Volume"),
(readonly)

window_managers¶

    

Window manager data-blocks

Type:

    

[`BlendDataWindowManagers`](bpy.types.BlendDataWindowManagers.html#bpy.types.BlendDataWindowManagers
"bpy.types.BlendDataWindowManagers")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`WindowManager`](bpy.types.WindowManager.html#bpy.types.WindowManager
"bpy.types.WindowManager"), (readonly)

workspaces¶

    

Workspace data-blocks

Type:

    

[`BlendDataWorkSpaces`](bpy.types.BlendDataWorkSpaces.html#bpy.types.BlendDataWorkSpaces
"bpy.types.BlendDataWorkSpaces")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`WorkSpace`](bpy.types.WorkSpace.html#bpy.types.WorkSpace
"bpy.types.WorkSpace"), (readonly)

worlds¶

    

World data-blocks

Type:

    

[`BlendDataWorlds`](bpy.types.BlendDataWorlds.html#bpy.types.BlendDataWorlds
"bpy.types.BlendDataWorlds")
[`bpy_prop_collection`](bpy.types.bpy_prop_collection.html#bpy.types.bpy_prop_collection
"bpy.types.bpy_prop_collection") of
[`World`](bpy.types.World.html#bpy.types.World "bpy.types.World"), (readonly)

batch_remove(_ids_)¶

    

Remove (delete) several IDs at once.

Note that this function is quicker than individual calls to `remove()` (from
`bpy.types.BlendData` ID collections), but less safe/versatile (it can break
Blender, e.g. by removing all scenes…).

Parameters:

    

**ids** (Sequence[[`bpy.types.ID`](bpy.types.ID.html#bpy.types.ID
"bpy.types.ID")]) – Sequence of IDs (types can be mixed).

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

file_path_map(_subset =None_, _key_types =None_, _include_libraries =False_)¶

    

Returns a mapping of all ID data-blocks in current `bpy.data` to a set of all
file paths used by them.

For list of valid set members for key_types, see:
[`bpy.types.KeyingSetPath.id_type`](bpy.types.KeyingSetPath.html#bpy.types.KeyingSetPath.id_type
"bpy.types.KeyingSetPath.id_type").

Parameters:

    

  * **subset** (_sequence_) – When given, only these data-blocks and their used file paths will be included as keys/values in the map.

  * **key_types** (_set_ _of_ _strings_) – When given, filter the keys mapped by ID types. Ignored if `subset` is also given.

  * **include_libraries** (_bool_) – Include library file paths of linked data. False by default.

Returns:

    

dictionary of [`bpy.types.ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")
instances, with sets of file path strings as their values.

Return type:

    

dict

orphans_purge()¶

    

Remove (delete) all IDs with no user.

Parameters:

    

  * **do_local_ids** (_bool_ _,__optional_) – Include unused local IDs in the deletion, defaults to True

  * **do_linked_ids** (_bool_ _,__optional_) – Include unused linked IDs in the deletion, defaults to True

  * **do_recursive** (_bool_ _,__optional_) – Recursively check for unused IDs, ensuring no orphaned one remain after a single run of that function, defaults to False

Returns:

    

The number of deleted IDs.

temp_data(_filepath =None_)¶

    

A context manager that temporarily creates blender file data.

Parameters:

    

**filepath** (_str_ _|__bytes_ _|__None_) – The file path for the newly
temporary data. When None, the path of the currently open file is used.

Returns:

    

Blend file data which is freed once the context exists.

Return type:

    

`bpy.types.BlendData`

user_map(_*_ , _subset =None_, _key_types =None_, _value_types =None_)¶

    

Returns a mapping of all ID data-blocks in current `bpy.data` to a set of all
data-blocks using them.

For list of valid set members for key_types & value_types, see:
[`bpy.types.KeyingSetPath.id_type`](bpy.types.KeyingSetPath.html#bpy.types.KeyingSetPath.id_type
"bpy.types.KeyingSetPath.id_type").

Parameters:

    

  * **subset** (Sequence[[`bpy.types.ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")]) – When passed, only these data-blocks and their users will be included as keys/values in the map.

  * **key_types** (_set_ _[__str_ _]_) – Filter the keys mapped by ID types.

  * **value_types** (_set_ _[__str_ _]_) – Filter the values in the set by ID types.

Returns:

    

dictionary that maps data-blocks ID’s to their users.

Return type:

    

dict[[`bpy.types.ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID"),
set[[`bpy.types.ID`](bpy.types.ID.html#bpy.types.ID "bpy.types.ID")]]

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

  * [`Context.blend_data`](bpy.types.Context.html#bpy.types.Context.blend_data "bpy.types.Context.blend_data")

|

  * [`RenderEngine.update`](bpy.types.RenderEngine.html#bpy.types.RenderEngine.update "bpy.types.RenderEngine.update")

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

