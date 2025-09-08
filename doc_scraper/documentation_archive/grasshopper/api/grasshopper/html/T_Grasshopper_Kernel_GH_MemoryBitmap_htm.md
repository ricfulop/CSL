---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_MemoryBitmap.htm
scraped_at: 2025-09-08T16:17:10.478915
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_MemoryBitmap Class](../html/T_Grasshopper_Kernel_GH_MemoryBitmap.htm
"GH_MemoryBitmap Class")

[GH_MemoryBitmap Constructor
](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap__ctor.htm
"GH_MemoryBitmap Constructor ")

[GH_MemoryBitmap
Properties](../html/Properties_T_Grasshopper_Kernel_GH_MemoryBitmap.htm
"GH_MemoryBitmap Properties")

[GH_MemoryBitmap
Methods](../html/Methods_T_Grasshopper_Kernel_GH_MemoryBitmap.htm
"GH_MemoryBitmap Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_MemoryBitmap Class  
  
---  
  
Utility class for ultra-fast bitmap sampling and filters.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_MemoryBitmap  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_MemoryBitmap
    
    
    Public NotInheritable Class GH_MemoryBitmap

The GH_MemoryBitmap type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_MemoryBitmap(Bitmap)](M_Grasshopper_Kernel_GH_MemoryBitmap__ctor.htm)|
Default constructor.  
![Public method](../icons/pubmethod.gif)| [GH_MemoryBitmap(Bitmap,
WrapMode)](M_Grasshopper_Kernel_GH_MemoryBitmap__ctor_1.htm)|  Constructor
with Wrap mode override.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[HasAlphaChannel](P_Grasshopper_Kernel_GH_MemoryBitmap_HasAlphaChannel.htm)|
Gets a value indicating whether or not the local image has an alpha channel
defined.  
![Public property](../icons/pubproperty.gif)|
[Height](P_Grasshopper_Kernel_GH_MemoryBitmap_Height.htm)|  Gets the height
(in pixels) of the local image.  
![Public property](../icons/pubproperty.gif)|
[SizeOf](P_Grasshopper_Kernel_GH_MemoryBitmap_SizeOf.htm)|  Gets the size (in
bytes) of the local image.  
![Public property](../icons/pubproperty.gif)|
[Width](P_Grasshopper_Kernel_GH_MemoryBitmap_Width.htm)|  Gets the width (in
pixels) of the local image.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[A](M_Grasshopper_Kernel_GH_MemoryBitmap_A.htm)|  Gets the alpha channel value
at the given pixel coordinates.  
![Public method](../icons/pubmethod.gif)|
[B](M_Grasshopper_Kernel_GH_MemoryBitmap_B.htm)|  Gets the blue channel value
at the given pixel coordinates.  
![Public method](../icons/pubmethod.gif)| [Colour(Int32,
Int32)](M_Grasshopper_Kernel_GH_MemoryBitmap_Colour.htm)|  Gets the colour at
the given pixel coordinates.  
![Public method](../icons/pubmethod.gif)| [Colour(Int32, Int32,
Color)](M_Grasshopper_Kernel_GH_MemoryBitmap_Colour_1.htm)|  Sets the colour
at the given pixel coordinates.  
![Public method](../icons/pubmethod.gif)|
[CopyChannel](M_Grasshopper_Kernel_GH_MemoryBitmap_CopyChannel.htm)|  Copy the
contents of one channel into another.  
![Public method](../icons/pubmethod.gif)|
[Filter_AlphaEdges](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_AlphaEdges.htm)|
Set the alpha component on all edges to a specific value.  
![Public method](../icons/pubmethod.gif)|
[Filter_Blur](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur.htm)|  Blur the
image in both directions.  
![Public method](../icons/pubmethod.gif)|
[Filter_Blur(Int32)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur_1.htm)|
Blur the image N times in both directions.  
![Public method](../icons/pubmethod.gif)| [Filter_Blur(Int32,
Int32)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur_2.htm)|  Blur the
image in both directions.  
![Public method](../icons/pubmethod.gif)| [Filter_Blur(Int32, Int32,
Int32)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur_3.htm)|  Blur the
image N times in both directions.  
![Public method](../icons/pubmethod.gif)|
[Filter_BlurAlpha](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_BlurAlpha.htm)|
Blur the alpha channel of the image N times in both directions.  
![Public method](../icons/pubmethod.gif)|
[Filter_Contrast](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Contrast.htm)|
Adjust the contrast of a specific channel.  
![Public method](../icons/pubmethod.gif)|
[Filter_DitherPattern](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_DitherPattern.htm)|
Create a checkerboard dither pattern.  
![Public method](../icons/pubmethod.gif)|
[Filter_DropShadow](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_DropShadow.htm)|
Add a drop-shadow to the image. Image is not grown, so if you want the drop
shadow to extend beyond the image boundaries, you have to add padding to the
image first.  
![Public method](../icons/pubmethod.gif)|
[Filter_Dullify](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Dullify.htm)|
Reduces contrast based on opacity. This filter pulls all colours towards dull
grey, without wrecking drop-shadows.  
![Public method](../icons/pubmethod.gif)|
[Filter_Equalize](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Equalize.htm)|
Set all the values in a specific channel to a specific value.  
![Public method](../icons/pubmethod.gif)|
[Filter_GreyScale](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_GreyScale.htm)|
Convert the image to a greyscale shadow of its former self.  
![Public method](../icons/pubmethod.gif)|
[Filter_GreyScale(Double)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_GreyScale_1.htm)|
Convert the image to a greyscale shadow of its former self.  
![Public method](../icons/pubmethod.gif)|
[Filter_HueScale](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_HueScale.htm)|
Convert the image to a greyscale representation of the hues.  
![Public method](../icons/pubmethod.gif)|
[Filter_Invert](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Invert.htm)|
Invert all values in a specific channel.  
![Public method](../icons/pubmethod.gif)|
[Filter_LumScale](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_LumScale.htm)|
Convert the image to a greyscale representation of the luminance.  
![Public method](../icons/pubmethod.gif)| [Filter_Multiply(GH_BitmapChannel,
Double)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Multiply.htm)|  Multiply
all values in a specific channel with a specific factor.  
![Public method](../icons/pubmethod.gif)| [Filter_Multiply(GH_BitmapChannel,
Double, Byte)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Multiply_1.htm)|
Multiply all values in a specific channel with a specific factor, using a
custom scaling center anchor.  
![Public method](../icons/pubmethod.gif)|
[Filter_SatScale](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_SatScale.htm)|
Convert the image to a greyscale representation of the saturation.  
![Public method](../icons/pubmethod.gif)|
[Filter_Shift](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Shift.htm)|  Shift
all values in a specific channel with a specific amount.  
![Public method](../icons/pubmethod.gif)|
[Filter_SpectrumScale](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_SpectrumScale.htm)|
Convert the image to a spectral representation of the hues.  
![Public method](../icons/pubmethod.gif)|
[Filter_Tint](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Tint.htm)|  Colorize
the image using Hue and Saturation from a base colour.  
![Public method](../icons/pubmethod.gif)|
[G](M_Grasshopper_Kernel_GH_MemoryBitmap_G.htm)|  Gets the greeb channel value
at the given pixel coordinates.  
![Public method](../icons/pubmethod.gif)|
[OpaqueArea](M_Grasshopper_Kernel_GH_MemoryBitmap_OpaqueArea.htm)|  Find the
opaque area of a bitmap. The opaque area is the rectangle that contains pixels
with a colour that is not fully transparent.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[PadBitmap](M_Grasshopper_Kernel_GH_MemoryBitmap_PadBitmap.htm)|  Add padding
edges around a bitmap.  
![Public method](../icons/pubmethod.gif)|
[R](M_Grasshopper_Kernel_GH_MemoryBitmap_R.htm)|  Gets the red channel value
at the given pixel coordinates.  
![Public method](../icons/pubmethod.gif)|
[Release](M_Grasshopper_Kernel_GH_MemoryBitmap_Release.htm)|  Release the
locked bits. You **must** call this function when you are done with this
GH_MemoryBitmap instance.  
![Public method](../icons/pubmethod.gif)| [Sample(Double, Double,
Color)](M_Grasshopper_Kernel_GH_MemoryBitmap_Sample.htm)|  Top level sampling
function for interpolated sampling.  
![Public method](../icons/pubmethod.gif)| [Sample(Int32, Int32,
Color)](M_Grasshopper_Kernel_GH_MemoryBitmap_Sample_1.htm)|  Top level
sampling function.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ShrinkBitmap](M_Grasshopper_Kernel_GH_MemoryBitmap_ShrinkBitmap.htm)|  Shrink
an image by removing all outer columns and rows that contain only fully
transparent pixels.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

