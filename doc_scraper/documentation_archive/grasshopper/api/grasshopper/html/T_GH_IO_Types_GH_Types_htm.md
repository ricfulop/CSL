---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_Types_GH_Types.htm
scraped_at: 2025-09-08T16:11:00.926121
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO.Types](../html/N_GH_IO_Types.htm "GH_IO.Types")

[GH_BoundingBox Structure](../html/T_GH_IO_Types_GH_BoundingBox.htm
"GH_BoundingBox Structure")

[GH_Interval1D Structure](../html/T_GH_IO_Types_GH_Interval1D.htm
"GH_Interval1D Structure")

[GH_Interval2D Structure](../html/T_GH_IO_Types_GH_Interval2D.htm
"GH_Interval2D Structure")

[GH_Item Class](../html/T_GH_IO_Types_GH_Item.htm "GH_Item Class")

[GH_Line Structure](../html/T_GH_IO_Types_GH_Line.htm "GH_Line Structure")

[GH_Plane Structure](../html/T_GH_IO_Types_GH_Plane.htm "GH_Plane Structure")

[GH_Point2D Structure](../html/T_GH_IO_Types_GH_Point2D.htm "GH_Point2D
Structure")

[GH_Point3D Structure](../html/T_GH_IO_Types_GH_Point3D.htm "GH_Point3D
Structure")

[GH_Point4D Structure](../html/T_GH_IO_Types_GH_Point4D.htm "GH_Point4D
Structure")

[GH_Types Enumeration](../html/T_GH_IO_Types_GH_Types.htm "GH_Types
Enumeration")

[GH_Version Structure](../html/T_GH_IO_Types_GH_Version.htm "GH_Version
Structure")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Types Enumeration  
  
---  
  
Contains flags for all data types currently supported by GH_IO.dll

**Namespace:** [GH_IO.Types](N_GH_IO_Types.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public enum GH_Types
    
    
    Public Enumeration GH_Types

![](../icons/SectionExpanded.png)Members

| Member name| Value| Description  
---|---|---|---  
| unset| 0| Represents an unset type. GH_Items with this type will throw
exceptions during serialization.  
| gh_bool| 1| boolean  
| gh_byte| 2| byte  
| gh_int32| 3| 32 bit integer  
| gh_int64| 4| 64 bit integer  
| gh_single| 5| single precision floating point number  
| gh_double| 6| double precision floating point number  
| gh_decimal| 7| decimal number  
| gh_date| 8| date time structure  
| gh_guid| 9| 128 bit globally unique identifier  
| gh_string| 10| unicode string  
| gh_bytearray| 20| an array of bytes  
| gh_doublearray| 21| an array of doubles  
| gh_drawing_point| 30| gdi+ integer precision point  
| gh_drawing_pointf| 31| gdi+ single precision point  
| gh_drawing_size| 32| gdi+ integer precision size  
| gh_drawing_sizef| 33| gdi+ single precision size  
| gh_drawing_rectangle| 34| gdi+ integer precision rectangle  
| gh_drawing_rectanglef| 35| gdi+ single precision rectangle  
| gh_drawing_color| 36| gdi+ argb color  
| gh_drawing_bitmap| 37| gdi+ bitmap (png format bytestream)  
| gh_point2d| 50| double precision two-dimensional point  
| gh_point3d| 51| double precision three-dimensional point  
| gh_point4d| 52| double precision four-dimensional point  
| gh_interval1d| 60| double precision one-dimensional numeric interval  
| gh_interval2d| 61| double precision two-dimensional numeric interval  
| gh_line| 70| double precision three-dimensional line segment  
| gh_boundingbox| 71| double precision three-dimensional box volume  
| gh_plane| 72| double precision three-dimensional plane construct  
| gh_version| 80| version structure with major, minor and revision fields  
  
![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO.Types Namespace](N_GH_IO_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

