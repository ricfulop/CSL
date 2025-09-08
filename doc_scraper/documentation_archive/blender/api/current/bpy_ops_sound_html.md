---
url: https://docs.blender.org/api/current/bpy.ops.sound.html
scraped_at: 2025-09-08T14:18:50.625261
title: Sound Operators¶
---

# Sound Operators¶

bpy.ops.sound.bake_animation()¶

    

Update the audio animation cache

bpy.ops.sound.mixdown(_*_ , _filepath =''_, _check_existing =True_,
_filter_blender =False_, _filter_backup =False_, _filter_image =False_,
_filter_movie =False_, _filter_python =False_, _filter_font =False_,
_filter_sound =True_, _filter_text =False_, _filter_archive =False_,
_filter_btx =False_, _filter_collada =False_, _filter_alembic =False_,
_filter_usd =False_, _filter_obj =False_, _filter_volume =False_,
_filter_folder =True_, _filter_blenlib =False_, _filemode =9_, _relative_path
=True_, _display_type =DEFAULT_, _sort_method_ , _accuracy =1024_, _container
=FLAC_, _codec =FLAC_, _channels =STEREO_, _format =S16_, _mixrate =48000_,
_bitrate =192_, _split_channels =False_)¶

    

Mix the scene’s audio to a sound file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **check_existing** (_boolean_ _,__(__optional_ _)_) – Check Existing, Check and warn on overwriting existing files

  * **filter_blender** (_boolean_ _,__(__optional_ _)_) – Filter .blend files

  * **filter_backup** (_boolean_ _,__(__optional_ _)_) – Filter .blend files

  * **filter_image** (_boolean_ _,__(__optional_ _)_) – Filter image files

  * **filter_movie** (_boolean_ _,__(__optional_ _)_) – Filter movie files

  * **filter_python** (_boolean_ _,__(__optional_ _)_) – Filter Python files

  * **filter_font** (_boolean_ _,__(__optional_ _)_) – Filter font files

  * **filter_sound** (_boolean_ _,__(__optional_ _)_) – Filter sound files

  * **filter_text** (_boolean_ _,__(__optional_ _)_) – Filter text files

  * **filter_archive** (_boolean_ _,__(__optional_ _)_) – Filter archive files

  * **filter_btx** (_boolean_ _,__(__optional_ _)_) – Filter btx files

  * **filter_collada** (_boolean_ _,__(__optional_ _)_) – Filter COLLADA files

  * **filter_alembic** (_boolean_ _,__(__optional_ _)_) – Filter Alembic files

  * **filter_usd** (_boolean_ _,__(__optional_ _)_) – Filter USD files

  * **filter_obj** (_boolean_ _,__(__optional_ _)_) – Filter OBJ files

  * **filter_volume** (_boolean_ _,__(__optional_ _)_) – Filter OpenVDB volume files

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_blenlib** (_boolean_ _,__(__optional_ _)_) – Filter Blender IDs

  * **filemode** (_int in_ _[__1_ _,__9_ _]__,__(__optional_ _)_) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

  * **relative_path** (_boolean_ _,__(__optional_ _)_) – Relative Path, Select the file relative to the blend file

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **accuracy** (_int in_ _[__1_ _,__inf_ _]__,__(__optional_ _)_) – Accuracy, Sample accuracy, important for animation data (the lower the value, the more accurate)

  * **container** (enum in [`AAC`, `AC3`, `FLAC`, `MATROSKA`, `MP2`, `MP3`, `OGG`, `WAV`], (optional)) – 

Container, File format

    * `AAC` AAC – Advanced Audio Coding.

    * `AC3` AC3 – Dolby Digital ATRAC 3.

    * `FLAC` FLAC – Free Lossless Audio Codec.

    * `MATROSKA` MKV – Matroska.

    * `MP2` MP2 – MPEG-1 Audio Layer II.

    * `MP3` MP3 – MPEG-2 Audio Layer III.

    * `OGG` OGG – Xiph.Org Ogg Container.

    * `WAV` WAV – Waveform Audio File Format.

  * **codec** (enum in [`AAC`, `AC3`, `FLAC`, `MP2`, `MP3`, `PCM`, `VORBIS`], (optional)) – 

Codec, Audio Codec

    * `AAC` AAC – Advanced Audio Coding.

    * `AC3` AC3 – Dolby Digital ATRAC 3.

    * `FLAC` FLAC – Free Lossless Audio Codec.

    * `MP2` MP2 – MPEG-1 Audio Layer II.

    * `MP3` MP3 – MPEG-2 Audio Layer III.

    * `PCM` PCM – Pulse Code Modulation (RAW).

    * `VORBIS` Vorbis – Xiph.Org Vorbis Codec.

  * **channels** (enum in [`MONO`, `STEREO`, `STEREO_LFE`, `SURROUND4`, `SURROUND5`, `SURROUND51`, `SURROUND61`, `SURROUND71`], (optional)) – 

Channels, Audio channel count

    * `MONO` Mono – Single audio channel.

    * `STEREO` Stereo – Stereo audio channels.

    * `STEREO_LFE` Stereo LFE – Stereo with LFE channel.

    * `SURROUND4` 4 Channels – 4 channel surround sound.

    * `SURROUND5` 5 Channels – 5 channel surround sound.

    * `SURROUND51` 5.1 Surround – 5.1 surround sound.

    * `SURROUND61` 6.1 Surround – 6.1 surround sound.

    * `SURROUND71` 7.1 Surround – 7.1 surround sound.

  * **format** (enum in [`U8`, `S16`, `S24`, `S32`, `F32`, `F64`], (optional)) – 

Format, Sample format

    * `U8` U8 – 8-bit unsigned.

    * `S16` S16 – 16-bit signed.

    * `S24` S24 – 24-bit signed.

    * `S32` S32 – 32-bit signed.

    * `F32` F32 – 32-bit floating-point.

    * `F64` F64 – 64-bit floating-point.

  * **mixrate** (_int in_ _[__8000_ _,__192000_ _]__,__(__optional_ _)_) – Sample Rate, Sample rate in samples/s

  * **bitrate** (_int in_ _[__32_ _,__512_ _]__,__(__optional_ _)_) – Bitrate, Bitrate in kbit/s

  * **split_channels** (_boolean_ _,__(__optional_ _)_) – Split channels, Each channel will be rendered into a mono file

bpy.ops.sound.open(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =False_, _filter_movie =True_, _filter_python =False_,
_filter_font =False_, _filter_sound =True_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _relative_path =True_, _show_multiview =False_, _use_multiview
=False_, _display_type =DEFAULT_, _sort_method_ , _cache =False_, _mono
=False_)¶

    

Load a sound file

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **hide_props_region** (_boolean_ _,__(__optional_ _)_) – Hide Operator Properties, Collapse the region displaying the operator settings

  * **check_existing** (_boolean_ _,__(__optional_ _)_) – Check Existing, Check and warn on overwriting existing files

  * **filter_blender** (_boolean_ _,__(__optional_ _)_) – Filter .blend files

  * **filter_backup** (_boolean_ _,__(__optional_ _)_) – Filter .blend files

  * **filter_image** (_boolean_ _,__(__optional_ _)_) – Filter image files

  * **filter_movie** (_boolean_ _,__(__optional_ _)_) – Filter movie files

  * **filter_python** (_boolean_ _,__(__optional_ _)_) – Filter Python files

  * **filter_font** (_boolean_ _,__(__optional_ _)_) – Filter font files

  * **filter_sound** (_boolean_ _,__(__optional_ _)_) – Filter sound files

  * **filter_text** (_boolean_ _,__(__optional_ _)_) – Filter text files

  * **filter_archive** (_boolean_ _,__(__optional_ _)_) – Filter archive files

  * **filter_btx** (_boolean_ _,__(__optional_ _)_) – Filter btx files

  * **filter_collada** (_boolean_ _,__(__optional_ _)_) – Filter COLLADA files

  * **filter_alembic** (_boolean_ _,__(__optional_ _)_) – Filter Alembic files

  * **filter_usd** (_boolean_ _,__(__optional_ _)_) – Filter USD files

  * **filter_obj** (_boolean_ _,__(__optional_ _)_) – Filter OBJ files

  * **filter_volume** (_boolean_ _,__(__optional_ _)_) – Filter OpenVDB volume files

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_blenlib** (_boolean_ _,__(__optional_ _)_) – Filter Blender IDs

  * **filemode** (_int in_ _[__1_ _,__9_ _]__,__(__optional_ _)_) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

  * **relative_path** (_boolean_ _,__(__optional_ _)_) – Relative Path, Select the file relative to the blend file

  * **show_multiview** (_boolean_ _,__(__optional_ _)_) – Enable Multi-View

  * **use_multiview** (_boolean_ _,__(__optional_ _)_) – Use Multi-View

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **cache** (_boolean_ _,__(__optional_ _)_) – Cache, Cache the sound in memory

  * **mono** (_boolean_ _,__(__optional_ _)_) – Mono, Merge all the sound’s channels into one

bpy.ops.sound.open_mono(_*_ , _filepath =''_, _hide_props_region =True_,
_check_existing =False_, _filter_blender =False_, _filter_backup =False_,
_filter_image =False_, _filter_movie =True_, _filter_python =False_,
_filter_font =False_, _filter_sound =True_, _filter_text =False_,
_filter_archive =False_, _filter_btx =False_, _filter_collada =False_,
_filter_alembic =False_, _filter_usd =False_, _filter_obj =False_,
_filter_volume =False_, _filter_folder =True_, _filter_blenlib =False_,
_filemode =9_, _relative_path =True_, _show_multiview =False_, _use_multiview
=False_, _display_type =DEFAULT_, _sort_method_ , _cache =False_, _mono
=True_)¶

    

Load a sound file as mono

Parameters:

    

  * **filepath** (_string_ _,__(__optional_ _,__never None_ _)_) – File Path, Path to file

  * **hide_props_region** (_boolean_ _,__(__optional_ _)_) – Hide Operator Properties, Collapse the region displaying the operator settings

  * **check_existing** (_boolean_ _,__(__optional_ _)_) – Check Existing, Check and warn on overwriting existing files

  * **filter_blender** (_boolean_ _,__(__optional_ _)_) – Filter .blend files

  * **filter_backup** (_boolean_ _,__(__optional_ _)_) – Filter .blend files

  * **filter_image** (_boolean_ _,__(__optional_ _)_) – Filter image files

  * **filter_movie** (_boolean_ _,__(__optional_ _)_) – Filter movie files

  * **filter_python** (_boolean_ _,__(__optional_ _)_) – Filter Python files

  * **filter_font** (_boolean_ _,__(__optional_ _)_) – Filter font files

  * **filter_sound** (_boolean_ _,__(__optional_ _)_) – Filter sound files

  * **filter_text** (_boolean_ _,__(__optional_ _)_) – Filter text files

  * **filter_archive** (_boolean_ _,__(__optional_ _)_) – Filter archive files

  * **filter_btx** (_boolean_ _,__(__optional_ _)_) – Filter btx files

  * **filter_collada** (_boolean_ _,__(__optional_ _)_) – Filter COLLADA files

  * **filter_alembic** (_boolean_ _,__(__optional_ _)_) – Filter Alembic files

  * **filter_usd** (_boolean_ _,__(__optional_ _)_) – Filter USD files

  * **filter_obj** (_boolean_ _,__(__optional_ _)_) – Filter OBJ files

  * **filter_volume** (_boolean_ _,__(__optional_ _)_) – Filter OpenVDB volume files

  * **filter_folder** (_boolean_ _,__(__optional_ _)_) – Filter folders

  * **filter_blenlib** (_boolean_ _,__(__optional_ _)_) – Filter Blender IDs

  * **filemode** (_int in_ _[__1_ _,__9_ _]__,__(__optional_ _)_) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

  * **relative_path** (_boolean_ _,__(__optional_ _)_) – Relative Path, Select the file relative to the blend file

  * **show_multiview** (_boolean_ _,__(__optional_ _)_) – Enable Multi-View

  * **use_multiview** (_boolean_ _,__(__optional_ _)_) – Use Multi-View

  * **display_type** (enum in [`DEFAULT`, `LIST_VERTICAL`, `LIST_HORIZONTAL`, `THUMBNAIL`], (optional)) – 

Display Type

    * `DEFAULT` Default – Automatically determine display type for files.

    * `LIST_VERTICAL` Short List – Display files as short list.

    * `LIST_HORIZONTAL` Long List – Display files as a detailed list.

    * `THUMBNAIL` Thumbnails – Display files as thumbnails.

  * **sort_method** (_enum in_ _[__]__,__(__optional_ _)_) – File sorting mode

  * **cache** (_boolean_ _,__(__optional_ _)_) – Cache, Cache the sound in memory

  * **mono** (_boolean_ _,__(__optional_ _)_) – Mono, Mixdown the sound to mono

bpy.ops.sound.pack()¶

    

Pack the sound into the current blend file

bpy.ops.sound.unpack(_*_ , _method =USE_LOCAL_, _id =''_)¶

    

Unpack the sound to the samples filename

Parameters:

    

  * **method** (enum in [Unpack Method Items](bpy_types_enum_items/unpack_method_items.html#rna-enum-unpack-method-items), (optional)) – Method, How to unpack

  * **id** (_string_ _,__(__optional_ _,__never None_ _)_) – Sound Name, Sound data-block name to unpack

bpy.ops.sound.update_animation_flags()¶

    

Update animation flags

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

