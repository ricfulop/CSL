---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_Types_GH_Item.htm
scraped_at: 2025-09-08T16:10:54.918653
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO.Types](../html/N_GH_IO_Types.htm "GH_IO.Types")

[GH_Item Class](../html/T_GH_IO_Types_GH_Item.htm "GH_Item Class")

[GH_Item Constructor ](../html/Overload_GH_IO_Types_GH_Item__ctor.htm "GH_Item
Constructor ")

[GH_Item Properties](../html/Properties_T_GH_IO_Types_GH_Item.htm "GH_Item
Properties")

[GH_Item Methods](../html/Methods_T_GH_IO_Types_GH_Item.htm "GH_Item Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Item Class  
  
---  
  
Represents a single data item in a chunk.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
GH_IO.TypesGH_Item  

**Namespace:** [GH_IO.Types](N_GH_IO_Types.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Item : GH_IBinarySupport, GH_IXmlSupport
    
    
    Public Class GH_Item
    	Implements GH_IBinarySupport, GH_IXmlSupport

The GH_Item type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
GH_BoundingBox)](M_GH_IO_Types_GH_Item__ctor.htm)|  Construct a new instance
of GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
GH_Interval1D)](M_GH_IO_Types_GH_Item__ctor_1.htm)|  Construct a new instance
of GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
GH_Interval2D)](M_GH_IO_Types_GH_Item__ctor_2.htm)|  Construct a new instance
of GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
GH_Line)](M_GH_IO_Types_GH_Item__ctor_3.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
GH_Plane)](M_GH_IO_Types_GH_Item__ctor_4.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
GH_Point2D)](M_GH_IO_Types_GH_Item__ctor_5.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
GH_Point3D)](M_GH_IO_Types_GH_Item__ctor_6.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
GH_Point4D)](M_GH_IO_Types_GH_Item__ctor_7.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
GH_Version)](M_GH_IO_Types_GH_Item__ctor_8.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Boolean)](M_GH_IO_Types_GH_Item__ctor_9.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Byte)](M_GH_IO_Types_GH_Item__ctor_10.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Byte)](M_GH_IO_Types_GH_Item__ctor_11.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
DateTime)](M_GH_IO_Types_GH_Item__ctor_12.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Decimal)](M_GH_IO_Types_GH_Item__ctor_13.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Double)](M_GH_IO_Types_GH_Item__ctor_14.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Double)](M_GH_IO_Types_GH_Item__ctor_15.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Bitmap)](M_GH_IO_Types_GH_Item__ctor_16.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Color)](M_GH_IO_Types_GH_Item__ctor_17.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Point)](M_GH_IO_Types_GH_Item__ctor_18.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
PointF)](M_GH_IO_Types_GH_Item__ctor_19.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Rectangle)](M_GH_IO_Types_GH_Item__ctor_20.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
RectangleF)](M_GH_IO_Types_GH_Item__ctor_21.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Size)](M_GH_IO_Types_GH_Item__ctor_22.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
SizeF)](M_GH_IO_Types_GH_Item__ctor_23.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Guid)](M_GH_IO_Types_GH_Item__ctor_24.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Int32)](M_GH_IO_Types_GH_Item__ctor_25.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Int64)](M_GH_IO_Types_GH_Item__ctor_55.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
Single)](M_GH_IO_Types_GH_Item__ctor_56.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String,
String)](M_GH_IO_Types_GH_Item__ctor_57.htm)|  Construct a new instance of
GH_Item with the specified name and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
GH_BoundingBox)](M_GH_IO_Types_GH_Item__ctor_26.htm)|  Construct a new
instance of GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
GH_Interval1D)](M_GH_IO_Types_GH_Item__ctor_27.htm)|  Construct a new instance
of GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
GH_Interval2D)](M_GH_IO_Types_GH_Item__ctor_28.htm)|  Construct a new instance
of GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
GH_Line)](M_GH_IO_Types_GH_Item__ctor_29.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
GH_Plane)](M_GH_IO_Types_GH_Item__ctor_30.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
GH_Point2D)](M_GH_IO_Types_GH_Item__ctor_31.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
GH_Point3D)](M_GH_IO_Types_GH_Item__ctor_32.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
GH_Point4D)](M_GH_IO_Types_GH_Item__ctor_33.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
GH_Version)](M_GH_IO_Types_GH_Item__ctor_34.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Boolean)](M_GH_IO_Types_GH_Item__ctor_35.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Byte)](M_GH_IO_Types_GH_Item__ctor_36.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Byte)](M_GH_IO_Types_GH_Item__ctor_37.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
DateTime)](M_GH_IO_Types_GH_Item__ctor_38.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Decimal)](M_GH_IO_Types_GH_Item__ctor_39.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Double)](M_GH_IO_Types_GH_Item__ctor_40.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Double)](M_GH_IO_Types_GH_Item__ctor_41.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Bitmap)](M_GH_IO_Types_GH_Item__ctor_42.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Color)](M_GH_IO_Types_GH_Item__ctor_43.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Point)](M_GH_IO_Types_GH_Item__ctor_44.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
PointF)](M_GH_IO_Types_GH_Item__ctor_45.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Rectangle)](M_GH_IO_Types_GH_Item__ctor_46.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
RectangleF)](M_GH_IO_Types_GH_Item__ctor_47.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Size)](M_GH_IO_Types_GH_Item__ctor_48.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
SizeF)](M_GH_IO_Types_GH_Item__ctor_49.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Guid)](M_GH_IO_Types_GH_Item__ctor_50.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Int32)](M_GH_IO_Types_GH_Item__ctor_51.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Int64)](M_GH_IO_Types_GH_Item__ctor_52.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
Single)](M_GH_IO_Types_GH_Item__ctor_53.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
![Public method](../icons/pubmethod.gif)| [GH_Item(String, Int32,
String)](M_GH_IO_Types_GH_Item__ctor_54.htm)|  Construct a new instance of
GH_Item with the specified name, index and value.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[_bool](P_GH_IO_Types_GH_Item__bool.htm)|  Returns the internal data of this
item cast to a Boolean. If the data is not stored as a Boolean, a conversion
exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_boundingbox](P_GH_IO_Types_GH_Item__boundingbox.htm)|  Returns the internal
data of this item cast to a BoundingBox. If the data is not stored as a
BoundingBox, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_byte](P_GH_IO_Types_GH_Item__byte.htm)|  Returns the internal data of this
item cast to a Byte. If the data is not stored as a Byte, a conversion
exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_bytearray](P_GH_IO_Types_GH_Item__bytearray.htm)|  Returns the internal data
of this item cast to a Byte array. If the data is not stored as a Byte array,
a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_date](P_GH_IO_Types_GH_Item__date.htm)|  Returns the internal data of this
item cast to a DateTime. If the data is not stored as a DateTime, a conversion
exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_decimal](P_GH_IO_Types_GH_Item__decimal.htm)|  Returns the internal data of
this item cast to a Decimal. If the data is not stored as a Decimal, a
conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_double](P_GH_IO_Types_GH_Item__double.htm)|  Returns the internal data of
this item cast to a Double. If the data is not stored as a Double, a
conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_doublearray](P_GH_IO_Types_GH_Item__doublearray.htm)|  Returns the internal
data of this item cast to a Byte array. If the data is not stored as a Byte
array, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_drawing_bitmap](P_GH_IO_Types_GH_Item__drawing_bitmap.htm)|  Returns the
internal data of this item cast to a Bitmap. If the data is not stored as a
Bitmap, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_drawing_color](P_GH_IO_Types_GH_Item__drawing_color.htm)|  Returns the
internal data of this item cast to a Color. If the data is not stored as a
Color, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_drawing_point](P_GH_IO_Types_GH_Item__drawing_point.htm)|  Returns the
internal data of this item cast to a Point. If the data is not stored as a
Point, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_drawing_pointf](P_GH_IO_Types_GH_Item__drawing_pointf.htm)|  Returns the
internal data of this item cast to a PointF. If the data is not stored as a
PointF, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_drawing_rectangle](P_GH_IO_Types_GH_Item__drawing_rectangle.htm)|  Returns
the internal data of this item cast to a Rectangle. If the data is not stored
as a Rectangle, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_drawing_rectanglef](P_GH_IO_Types_GH_Item__drawing_rectanglef.htm)|  Returns
the internal data of this item cast to a RectangleF. If the data is not stored
as a RectangleF, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_drawing_size](P_GH_IO_Types_GH_Item__drawing_size.htm)|  Returns the
internal data of this item cast to a Size. If the data is not stored as a
Size, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_drawing_sizef](P_GH_IO_Types_GH_Item__drawing_sizef.htm)|  Returns the
internal data of this item cast to a SizeF. If the data is not stored as a
SizeF, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_guid](P_GH_IO_Types_GH_Item__guid.htm)|  Returns the internal data of this
item cast to a Guid. If the data is not stored as a Guid, a conversion
exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_int32](P_GH_IO_Types_GH_Item__int32.htm)|  Returns the internal data of this
item cast to an Int32. If the data is not stored as an Int32, a conversion
exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_int64](P_GH_IO_Types_GH_Item__int64.htm)|  Returns the internal data of this
item cast to an Int64. If the data is not stored as an Int64, a conversion
exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_interval1d](P_GH_IO_Types_GH_Item__interval1d.htm)|  Returns the internal
data of this item cast to an Interval1D. If the data is not stored as an
Interval1D, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_interval2d](P_GH_IO_Types_GH_Item__interval2d.htm)|  Returns the internal
data of this item cast to an Interval2D. If the data is not stored as an
Interval2D, a conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_line](P_GH_IO_Types_GH_Item__line.htm)|  Returns the internal data of this
item cast to a Line. If the data is not stored as a Line, a conversion
exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_plane](P_GH_IO_Types_GH_Item__plane.htm)|  Returns the internal data of this
item cast to a Plane. If the data is not stored as a Plane, a conversion
exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_point2d](P_GH_IO_Types_GH_Item__point2d.htm)|  Returns the internal data of
this item cast to a Point2D. If the data is not stored as a Point2D, a
conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_point3d](P_GH_IO_Types_GH_Item__point3d.htm)|  Returns the internal data of
this item cast to a Point3D. If the data is not stored as a Point3D, a
conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_point4d](P_GH_IO_Types_GH_Item__point4d.htm)|  Returns the internal data of
this item cast to a Point4D. If the data is not stored as a Point4D, a
conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_single](P_GH_IO_Types_GH_Item__single.htm)|  Returns the internal data of
this item cast to a Single. If the data is not stored as a Single, a
conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_string](P_GH_IO_Types_GH_Item__string.htm)|  Returns the internal data of
this item cast to a String. If the data is not stored as a String, a
conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[_version](P_GH_IO_Types_GH_Item__version.htm)|  Returns the internal data of
this item cast to a Version. If the data is not stored as a Version, a
conversion exception might be thrown.  
![Public property](../icons/pubproperty.gif)|
[HasIndex](P_GH_IO_Types_GH_Item_HasIndex.htm)|  Gets the index existence
implication. The item is considered to have an index qualifier if the index
value is larger than or equal to zero.  
![Public property](../icons/pubproperty.gif)|
[HasName](P_GH_IO_Types_GH_Item_HasName.htm)|  Gets the name validity of this
item. The item is considered to have an invalid name if
string.IsNullOrEmpty(name)  
![Public property](../icons/pubproperty.gif)|
[HasType](P_GH_IO_Types_GH_Item_HasType.htm)|  Gets the type set validity of
this item. The item is considered to have a type if type != GH_Types.unset  
![Public property](../icons/pubproperty.gif)|
[Index](P_GH_IO_Types_GH_Item_Index.htm)|  Gets or sets the index of an item.
Typically, indices are set at construction and do not change. If you change
indices after construction, you could corrupt an archive.  
![Public property](../icons/pubproperty.gif)|
[InternalData](P_GH_IO_Types_GH_Item_InternalData.htm)|  Retrieves the
internal data of this item. No type casting is performed.  
![Public property](../icons/pubproperty.gif)|
[Name](P_GH_IO_Types_GH_Item_Name.htm)|  Gets or sets the name of this item.
Typically, names are set at construction and do not change. If you change
names after construction, you could corrupt an archive.  
![Public property](../icons/pubproperty.gif)|
[Type](P_GH_IO_Types_GH_Item_Type.htm)|  Gets the type of this item. Type
flags are set during construction and cannot be altered.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateFrom(BinaryReader)](M_GH_IO_Types_GH_Item_CreateFrom.htm)|  Creates a
new instance of GH_Item and sets the fields from a reader object.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateFrom(XmlNode)](M_GH_IO_Types_GH_Item_CreateFrom_1.htm)|  Creates a new
instance of GH_Item and sets the fields from an Xml node object.  
![Public method](../icons/pubmethod.gif)|
[Read(BinaryReader)](M_GH_IO_Types_GH_Item_Read.htm)|  Deserialize this item
from a binary stream.  
![Public method](../icons/pubmethod.gif)|
[Read(XmlNode)](M_GH_IO_Types_GH_Item_Read_1.htm)|  Deserialize this item from
an Xml node.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_GH_IO_Types_GH_Item_ToString.htm)|  Converts the struct into a
human readable format.  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Public method](../icons/pubmethod.gif)|
[Write(BinaryWriter)](M_GH_IO_Types_GH_Item_Write.htm)|  Serialize this item
into a binary stream.  
![Public method](../icons/pubmethod.gif)|
[Write(XmlWriter)](M_GH_IO_Types_GH_Item_Write_1.htm)|  Serialize this item
into an Xml stream.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO.Types Namespace](N_GH_IO_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

