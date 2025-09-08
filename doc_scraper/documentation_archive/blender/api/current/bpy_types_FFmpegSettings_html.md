---
url: https://docs.blender.org/api/current/bpy.types.FFmpegSettings.html
scraped_at: 2025-09-08T14:25:01.074752
title: FFmpegSettings(bpy_struct)¶
---

# FFmpegSettings(bpy_struct)¶  
  
base class — [`bpy_struct`](bpy.types.bpy_struct.html#bpy.types.bpy_struct
"bpy.types.bpy_struct")

_class _bpy.types.FFmpegSettings(_bpy_struct_)¶

    

FFmpeg related settings for the scene

audio_bitrate¶

    

Audio bitrate (kb/s)

Type:

    

int in [32, 384], default 192

audio_channels¶

    

Audio channel count

  * `MONO` Mono – Set audio channels to mono.

  * `STEREO` Stereo – Set audio channels to stereo.

  * `SURROUND4` 4 Channels – Set audio channels to 4 channels.

  * `SURROUND51` 5.1 Surround – Set audio channels to 5.1 surround sound.

  * `SURROUND71` 7.1 Surround – Set audio channels to 7.1 surround sound.

Type:

    

enum in [`MONO`, `STEREO`, `SURROUND4`, `SURROUND51`, `SURROUND71`], default
`STEREO`

audio_codec¶

    

FFmpeg audio codec to use

  * `NONE` No Audio – Disables audio output, for video-only renders.

  * `AAC` AAC.

  * `AC3` AC3.

  * `FLAC` FLAC.

  * `MP2` MP2.

  * `MP3` MP3.

  * `OPUS` Opus.

  * `PCM` PCM.

  * `VORBIS` Vorbis.

Type:

    

enum in [`NONE`, `AAC`, `AC3`, `FLAC`, `MP2`, `MP3`, `OPUS`, `PCM`, `VORBIS`],
default `NONE`

audio_mixrate¶

    

Audio sample rate (samples/s)

Type:

    

int in [8000, 192000], default 48000

audio_volume¶

    

Audio volume

Type:

    

float in [0, 1], default 1.0

buffersize¶

    

Rate control: buffer size (kb)

Type:

    

int in [0, 2000], default 0

codec¶

    

FFmpeg codec to use for video output

  * `NONE` No Video – Disables video output, for audio-only renders.

  * `AV1` AV1.

  * `H264` H.264.

  * `H265` H.265 / HEVC.

  * `WEBM` WebM / VP9.

  * `DNXHD` DNxHD.

  * `DV` DV.

  * `FFV1` FFmpeg video codec #1.

  * `FLASH` Flash Video.

  * `HUFFYUV` HuffYUV.

  * `MPEG1` MPEG-1.

  * `MPEG2` MPEG-2.

  * `MPEG4` MPEG-4 (divx).

  * `PNG` PNG.

  * `PRORES` ProRes.

  * `QTRLE` QuickTime Animation.

  * `THEORA` Theora.

Type:

    

enum in [`NONE`, `AV1`, `H264`, `H265`, `WEBM`, `DNXHD`, `DV`, `FFV1`,
`FLASH`, `HUFFYUV`, `MPEG1`, `MPEG2`, `MPEG4`, `PNG`, `PRORES`, `QTRLE`,
`THEORA`], default `H264`

constant_rate_factor¶

    

Constant Rate Factor (CRF); tradeoff between video quality and file size

  * `NONE` Constant Bitrate – Configure constant bit rate, rather than constant output quality.

  * `LOSSLESS` Lossless.

  * `PERC_LOSSLESS` Perceptually Lossless.

  * `HIGH` High Quality.

  * `MEDIUM` Medium Quality.

  * `LOW` Low Quality.

  * `VERYLOW` Very Low Quality.

  * `LOWEST` Lowest Quality.

Type:

    

enum in [`NONE`, `LOSSLESS`, `PERC_LOSSLESS`, `HIGH`, `MEDIUM`, `LOW`,
`VERYLOW`, `LOWEST`], default `MEDIUM`

ffmpeg_preset¶

    

Tradeoff between encoding speed and compression ratio

  * `BEST` Slowest – Recommended if you have lots of time and want the best compression efficiency.

  * `GOOD` Good – The default and recommended for most applications.

  * `REALTIME` Realtime – Recommended for fast encoding.

Type:

    

enum in [`BEST`, `GOOD`, `REALTIME`], default `GOOD`

ffmpeg_prores_profile¶

    

ProRes Profile

Type:

    

enum in [`422_PROXY`, `422_LT`, `422_STD`, `422_HQ`, `4444`, `4444_XQ`],
default `422_STD`

format¶

    

Output file container

Type:

    

enum in [`MPEG4`, `MKV`, `WEBM`, `AVI`, `DV`, `FLASH`, `MPEG1`, `MPEG2`,
`OGG`, `QUICKTIME`], default `MKV`

gopsize¶

    

Distance between key frames, also known as GOP size; influences file size and
seekability

Type:

    

int in [0, 500], default 25

max_b_frames¶

    

Maximum number of B-frames between non-B-frames; influences file size and
seekability

Type:

    

int in [0, 16], default 0

maxrate¶

    

Rate control: max rate (kbit/s)

Type:

    

int in [-inf, inf], default 0

minrate¶

    

Rate control: min rate (kbit/s)

Type:

    

int in [-inf, inf], default 0

muxrate¶

    

Mux rate (bits/second)

Type:

    

int in [0, inf], default 0

packetsize¶

    

Mux packet size (byte)

Type:

    

int in [0, 16384], default 0

use_autosplit¶

    

Autosplit output at 2GB boundary

Type:

    

boolean, default False

use_lossless_output¶

    

Use lossless output for video streams

Type:

    

boolean, default False

use_max_b_frames¶

    

Set a maximum number of B-frames

Type:

    

boolean, default False

video_bitrate¶

    

Video bitrate (kbit/s)

Type:

    

int in [-inf, inf], default 0

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

  * [`RenderSettings.ffmpeg`](bpy.types.RenderSettings.html#bpy.types.RenderSettings.ffmpeg "bpy.types.RenderSettings.ffmpeg")

|

  
---|---
  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

