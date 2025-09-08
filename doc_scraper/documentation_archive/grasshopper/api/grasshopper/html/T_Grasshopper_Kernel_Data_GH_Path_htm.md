---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_Path.htm
scraped_at: 2025-09-08T16:19:06.008456
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm
"Grasshopper.Kernel.Data")

[GH_Path Class](../html/T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Class")

[GH_Path Constructor
](../html/Overload_Grasshopper_Kernel_Data_GH_Path__ctor.htm "GH_Path
Constructor ")

[GH_Path Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_Path.htm
"GH_Path Properties")

[GH_Path Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Path.htm
"GH_Path Methods")

[GH_Path Operators](../html/Operators_T_Grasshopper_Kernel_Data_GH_Path.htm
"GH_Path Operators")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Path Class  
  
---  
  
Describes the path in structure space of a data item or a list of items. A
path consists of a series of integers, each one of which represents an index
in a branch structure.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.DataGH_Path  

**Namespace:** [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Path : IComparable<GH_Path>, 
    	IComparer<GH_Path>, GH_ISerializable
    
    
    Public Class GH_Path
    	Implements IComparable(Of GH_Path), IComparer(Of GH_Path), 
    	GH_ISerializable

The GH_Path type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Path](M_Grasshopper_Kernel_Data_GH_Path__ctor.htm)|  Default constructor,
creates a path with zero elements.  
![Public method](../icons/pubmethod.gif)|
[GH_Path(GH_Path)](M_Grasshopper_Kernel_Data_GH_Path__ctor_1.htm)|  Creates an
exact copy of another path.  
![Public method](../icons/pubmethod.gif)|
[GH_Path(Int32)](M_Grasshopper_Kernel_Data_GH_Path__ctor_2.htm)|  Creates a
new path with a single element.  
![Public method](../icons/pubmethod.gif)|
[GH_Path(Int32)](M_Grasshopper_Kernel_Data_GH_Path__ctor_3.htm)|  Creates a
new path from a series of elements.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Indices](P_Grasshopper_Kernel_Data_GH_Path_Indices.htm)|  Gets or sets the
entire index space; the path that identifies an element in structure space.
You should not change the index space when the path is used inside a structure
since it will invalidate the sort order. If you don't know what you're doing,
for Pete's sake don't touch this.  
![Public property](../icons/pubproperty.gif)|
[Length](P_Grasshopper_Kernel_Data_GH_Path_Length.htm)|  Returns the number of
dimensions in the path.  
![Public property](../icons/pubproperty.gif)|
[Valid](P_Grasshopper_Kernel_Data_GH_Path_Valid.htm)|  Gets whether this path
is valid. Invalid paths either have no elements or negative elements.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AppendElement](M_Grasshopper_Kernel_Data_GH_Path_AppendElement.htm)|  Create
a new path by appending a new index value to this path.  
![Public method](../icons/pubmethod.gif)|
[Compare](M_Grasshopper_Kernel_Data_GH_Path_Compare.htm)|  Compare two paths.
This function determines the Sorting behaviour of paths.  
![Public method](../icons/pubmethod.gif)|
[CompareTo](M_Grasshopper_Kernel_Data_GH_Path_CompareTo.htm)|  Compare this
path to another path. This function determines the Sorting behaviour of paths.  
![Public method](../icons/pubmethod.gif)|
[CullElement](M_Grasshopper_Kernel_Data_GH_Path_CullElement.htm)|  Removes the
last index value from the path. If the path is already empty, nothing will
happen.  
![Public method](../icons/pubmethod.gif)|
[CullFirstElement](M_Grasshopper_Kernel_Data_GH_Path_CullFirstElement.htm)|
Removes the first index value from the path. If the path is already empty,
nothing will happen.  
![Public method](../icons/pubmethod.gif)|
[Format](M_Grasshopper_Kernel_Data_GH_Path_Format.htm)|  Format a path.  
![Public method](../icons/pubmethod.gif)|
[FromString](M_Grasshopper_Kernel_Data_GH_Path_FromString.htm)|  Try to
deserialize a GH_Path from a String.  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Kernel_Data_GH_Path_GetHashCode.htm)|  Specialized
Hash code pattern.  (Overrides
[ObjectGetHashCode](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[Increment(Int32)](M_Grasshopper_Kernel_Data_GH_Path_Increment.htm)|
Increment a specific index in this path by one.  
![Public method](../icons/pubmethod.gif)| [Increment(Int32,
Int32)](M_Grasshopper_Kernel_Data_GH_Path_Increment_1.htm)|  Increment a
specific index in this path by one.  
![Public method](../icons/pubmethod.gif)|
[IsAncestor](M_Grasshopper_Kernel_Data_GH_Path_IsAncestor.htm)|  Test another
path to see if it is an ancestor of this path. For a path to be considered an
ancestor, it must share the initial dimensions.  
![Public method](../icons/pubmethod.gif)|
[IsCoincident(GH_Path)](M_Grasshopper_Kernel_Data_GH_Path_IsCoincident.htm)|
Test to see if this path is coincident with another path.  
![Public method](../icons/pubmethod.gif)|
[IsCoincident(Int32)](M_Grasshopper_Kernel_Data_GH_Path_IsCoincident_1.htm)|
Test to see if this path is coincident with set of integers.  
![Public method](../icons/pubmethod.gif)|
[PrependElement](M_Grasshopper_Kernel_Data_GH_Path_PrependElement.htm)|
Create a new path by prepending a new index value to this path.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Data_GH_Path_Read.htm)|  Read this path from an
archive.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SplitPathLikeString](M_Grasshopper_Kernel_Data_GH_Path_SplitPathLikeString.htm)|
Try to split up a path-like formatted string "{A;B;C}(i)" into component
parts.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Data_GH_Path_ToString.htm)|  Concatenates the
indices in the path.  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Public method](../icons/pubmethod.gif)|
[ToString(Boolean)](M_Grasshopper_Kernel_Data_GH_Path_ToString_1.htm)|
Concatenates the indices in the path.  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Data_GH_Path_Write.htm)|  Write this path to an
archive.  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Equality](M_Grasshopper_Kernel_Data_GH_Path_op_Equality.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[GreaterThan](M_Grasshopper_Kernel_Data_GH_Path_op_GreaterThan.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Inequality](M_Grasshopper_Kernel_Data_GH_Path_op_Inequality.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[LessThan](M_Grasshopper_Kernel_Data_GH_Path_op_LessThan.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

