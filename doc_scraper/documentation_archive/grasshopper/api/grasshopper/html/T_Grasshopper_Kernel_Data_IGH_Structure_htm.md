---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_IGH_Structure.htm
scraped_at: 2025-09-08T16:19:28.101165
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm
"Grasshopper.Kernel.Data")

[IGH_Structure Interface](../html/T_Grasshopper_Kernel_Data_IGH_Structure.htm
"IGH_Structure Interface")

[IGH_Structure
Properties](../html/Properties_T_Grasshopper_Kernel_Data_IGH_Structure.htm
"IGH_Structure Properties")

[IGH_Structure
Methods](../html/Methods_T_Grasshopper_Kernel_Data_IGH_Structure.htm
"IGH_Structure Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_Structure Interface  
  
---  
  
Base interface for all GH_Structure types.

**Namespace:** [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_Structure
    
    
    Public Interface IGH_Structure

The IGH_Structure type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[BranchGH_Path](P_Grasshopper_Kernel_Data_IGH_Structure_Branch.htm)|  Gets a
limited access pointer to the data list associated with a certain path.  
![Public property](../icons/pubproperty.gif)|
[BranchInt32](P_Grasshopper_Kernel_Data_IGH_Structure_Branch_1.htm)|  Gets a
limited access pointer to the data list at the specified index.  
![Public property](../icons/pubproperty.gif)|
[DataCount](P_Grasshopper_Kernel_Data_IGH_Structure_DataCount.htm)|  Gets the
total number of data items stored in all paths.  
![Public property](../icons/pubproperty.gif)|
[IsEmpty](P_Grasshopper_Kernel_Data_IGH_Structure_IsEmpty.htm)|  Gets the
Empty state of the structure. If the structure is Empty when it contains no
paths and no branches.  
![Public property](../icons/pubproperty.gif)|
[Path](P_Grasshopper_Kernel_Data_IGH_Structure_Path.htm)|  Gets the data path
at the specified index.  
![Public property](../icons/pubproperty.gif)|
[PathCount](P_Grasshopper_Kernel_Data_IGH_Structure_PathCount.htm)|  Gets the
number of paths defined in this structure.  
![Public property](../icons/pubproperty.gif)|
[Paths](P_Grasshopper_Kernel_Data_IGH_Structure_Paths.htm)|  Gets a list of
all the paths in this structure.  
![Public property](../icons/pubproperty.gif)|
[StructureProxy](P_Grasshopper_Kernel_Data_IGH_Structure_StructureProxy.htm)|
Gets a proxy list of all the data-arrays in this structure  
![Public property](../icons/pubproperty.gif)|
[TopologyDescription](P_Grasshopper_Kernel_Data_IGH_Structure_TopologyDescription.htm)|
Gets a description of the topology of the structure. Useful for debugging
purposes.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AllData](M_Grasshopper_Kernel_Data_IGH_Structure_AllData.htm)|  Gets an
enumerator for all the data items in this structure.  
![Public method](../icons/pubmethod.gif)|
[Clear](M_Grasshopper_Kernel_Data_IGH_Structure_Clear.htm)|  Clears the entire
structure.  
![Public method](../icons/pubmethod.gif)|
[ClearData](M_Grasshopper_Kernel_Data_IGH_Structure_ClearData.htm)|  Removes
all data from all paths without affecting the structure topology.  
![Public method](../icons/pubmethod.gif)|
[DataDescription](M_Grasshopper_Kernel_Data_IGH_Structure_DataDescription.htm)|
Gets a description of the data contained in this structure.  
![Public method](../icons/pubmethod.gif)|
[EnsureCapacity](M_Grasshopper_Kernel_Data_IGH_Structure_EnsureCapacity.htm)|
Ensures that all branches have a certain capacity  
![Public method](../icons/pubmethod.gif)|
[ExpandPath](M_Grasshopper_Kernel_Data_IGH_Structure_ExpandPath.htm)|  Expand
a path in this structure by appending an element.  
![Public method](../icons/pubmethod.gif)|
[Flatten](M_Grasshopper_Kernel_Data_IGH_Structure_Flatten.htm)|  Flattens the
entire structure into a single path.  
![Public method](../icons/pubmethod.gif)|
[Graft(GH_GraftMode)](M_Grasshopper_Kernel_Data_IGH_Structure_Graft.htm)|
Grafts all paths by reallocating all data into child paths.  
![Public method](../icons/pubmethod.gif)| [Graft(GH_GraftMode,
GH_Path)](M_Grasshopper_Kernel_Data_IGH_Structure_Graft_1.htm)|  Grafts a
specific path by reallocating all data into child paths. If a grafted path
coincides with an existing path, the data item in question will be appended to
the existing path.  
![Public method](../icons/pubmethod.gif)|
[LongestPathIndex](M_Grasshopper_Kernel_Data_IGH_Structure_LongestPathIndex.htm)|
Finds the path in this structure with the most dimensions. In case of multiple
equally long longest paths, the last one will be returned.  
![Public method](../icons/pubmethod.gif)|
[PathExists](M_Grasshopper_Kernel_Data_IGH_Structure_PathExists.htm)|  Returns
True if the specified path is already defined inside the structure.  
![Public method](../icons/pubmethod.gif)|
[PathIndex](M_Grasshopper_Kernel_Data_IGH_Structure_PathIndex.htm)|  Find the
indices that delineate the given path domain.  
![Public method](../icons/pubmethod.gif)|
[RemovePath](M_Grasshopper_Kernel_Data_IGH_Structure_RemovePath.htm)|  Removes
a path and all associated data from the structure. If the path doesn't exist,
nothing will happen.  
![Public method](../icons/pubmethod.gif)|
[ReplacePath](M_Grasshopper_Kernel_Data_IGH_Structure_ReplacePath.htm)|
Replace an existing path with a different one. If the operation is
successfull, then the 'find' path will be deleted. If the 'replace' path is
already defined, the items in 'find' will be appended to the existing path.  
![Public method](../icons/pubmethod.gif)|
[ShortestPathIndex](M_Grasshopper_Kernel_Data_IGH_Structure_ShortestPathIndex.htm)|
Finds the path in this structure with the least dimensions. In case of
multiple equally long longest paths, the first one will be returned.  
![Public method](../icons/pubmethod.gif)|
[Simplify](M_Grasshopper_Kernel_Data_IGH_Structure_Simplify.htm)|  Simplify
the data structure by removing path indices shared by all branches.  
![Public method](../icons/pubmethod.gif)|
[TrimExcess](M_Grasshopper_Kernel_Data_IGH_Structure_TrimExcess.htm)|  Trims
the excess allocated memory in all branches  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

