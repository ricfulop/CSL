---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_DataTree_1.htm
scraped_at: 2025-09-08T16:03:08.703607
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[DataTree(T) Class](../html/T_Grasshopper_DataTree_1.htm "DataTree\(T\)
Class")

[DataTree(T) Constructor ](../html/Overload_Grasshopper_DataTree_1__ctor.htm
"DataTree\(T\) Constructor ")

[DataTree(T) Properties](../html/Properties_T_Grasshopper_DataTree_1.htm
"DataTree\(T\) Properties")

[DataTree(T) Methods](../html/Methods_T_Grasshopper_DataTree_1.htm
"DataTree\(T\) Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# DataTreeT Class  
  
---  
  
Implements basic Grasshopper Data Tree functionality in an easy-to-use class.
This class is used primarily in Scripting components. If you're using the
Grasshopper SDK you should consider using the
[GH_StructureT](T_Grasshopper_Kernel_Data_GH_Structure_1.htm) class instead.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
GrasshopperDataTreeT  

**Namespace:** [Grasshopper](N_Grasshopper.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class DataTree<T> : IGH_DataTree
    
    
    
    Public Class DataTree(Of T)
    	Implements IGH_DataTree

#### Type Parameters

T

    Data type of this class.

The DataTreeT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[DataTreeT](M_Grasshopper_DataTree_1__ctor.htm)|  Default constructor, create
an empty data tree.  
![Public method](../icons/pubmethod.gif)|
[DataTreeT(DataTreeT)](M_Grasshopper_DataTree_1__ctor_1.htm)|  Create a
shallow duplicate of another data tree. This means it will create a new tree
that contains the same items.  
![Public method](../icons/pubmethod.gif)| [DataTreeT(DataTreeT,
DataTreeTDuplicateT)](M_Grasshopper_DataTree_1__ctor_2.htm)|  Create a true
duplicate of another data tree.  
![Public method](../icons/pubmethod.gif)| [DataTreeT(IEnumerableT,
GH_Path)](M_Grasshopper_DataTree_1__ctor_3.htm)|  Create a tree with a single
branch  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[BranchCount](P_Grasshopper_DataTree_1_BranchCount.htm)|  Gets the number of
branches defined in this tree.  
![Public property](../icons/pubproperty.gif)|
[Branches](P_Grasshopper_DataTree_1_Branches.htm)|  Gets a list of all the
data-arrays in this tree  
![Public property](../icons/pubproperty.gif)|
[DataCount](P_Grasshopper_DataTree_1_DataCount.htm)|  Gets the total number of
data items (including nulls) stored in all branches.  
![Public property](../icons/pubproperty.gif)|
[Item](P_Grasshopper_DataTree_1_Item.htm)|  Gets or set the data item at the
specified path and index.  
![Public property](../icons/pubproperty.gif)|
[Paths](P_Grasshopper_DataTree_1_Paths.htm)|  Gets a list of all the branch
paths in this tree.  
![Public property](../icons/pubproperty.gif)|
[TopologyDescription](P_Grasshopper_DataTree_1_TopologyDescription.htm)|  Gets
a description of the topology of the tree. Useful for debugging purposes.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Add(T)](M_Grasshopper_DataTree_1_Add.htm)|  Add (append) a data item to the
last branch in the tree. If no branches exist yet, a new one will be created
with [path = {0}]  
![Public method](../icons/pubmethod.gif)| [Add(T,
GH_Path)](M_Grasshopper_DataTree_1_Add_1.htm)|  Add (append) a data item to
the specified branch in the tree. If the branch doesn't exist yet, it will be
created.  
![Public method](../icons/pubmethod.gif)|
[AddRange(IEnumerableT)](M_Grasshopper_DataTree_1_AddRange.htm)|  Add (append)
a list of data items to the last branch in the tree. If no branch exists yet,
a new one will be created.  
![Public method](../icons/pubmethod.gif)| [AddRange(IEnumerableT,
GH_Path)](M_Grasshopper_DataTree_1_AddRange_1.htm)|  Add (append) a list of
data items to the specified branch in the tree. If the branch doesn't exist
yet, it will be created.  
![Public method](../icons/pubmethod.gif)|
[AllData](M_Grasshopper_DataTree_1_AllData.htm)|  Collects all data in the
tree in a single list. Does not alter the topology of this tree.  
![Public method](../icons/pubmethod.gif)|
[Branch(GH_Path)](M_Grasshopper_DataTree_1_Branch.htm)|  Gets the list of data
which belongs to a given Branch path.  
![Public method](../icons/pubmethod.gif)|
[Branch(Int32)](M_Grasshopper_DataTree_1_Branch_1.htm)|  Gets the list of data
which belongs to the branch path at the given index.  
![Public method](../icons/pubmethod.gif)|
[Branch(Int32)](M_Grasshopper_DataTree_1_Branch_2.htm)|  Gets the list of data
which belongs to a given Branch path.  
![Public method](../icons/pubmethod.gif)|
[Clear](M_Grasshopper_DataTree_1_Clear.htm)|  Clears the entire tree.  
![Public method](../icons/pubmethod.gif)|
[ClearData](M_Grasshopper_DataTree_1_ClearData.htm)|  Removes all data from
all branches without affecting the tree topology.  
![Public method](../icons/pubmethod.gif)|
[EnsurePath(GH_Path)](M_Grasshopper_DataTree_1_EnsurePath.htm)|  Create a new
branch with the specified path if it doesn't already exists.  
![Public method](../icons/pubmethod.gif)|
[EnsurePath(Int32)](M_Grasshopper_DataTree_1_EnsurePath_1.htm)|  Create a new
branch with the specified path if it doesn't already exists.  
![Public method](../icons/pubmethod.gif)|
[Flatten](M_Grasshopper_DataTree_1_Flatten.htm)|  Flattens the entire tree
into a single path.  
![Public method](../icons/pubmethod.gif)|
[Graft(Boolean)](M_Grasshopper_DataTree_1_Graft_1.htm)|  Graft all paths in
this tree. "Grafting" means appending a new branch for every item in an
existing branch.  
![Public method](../icons/pubmethod.gif)| [Graft(GH_Path,
Boolean)](M_Grasshopper_DataTree_1_Graft.htm)|  Graft a single path in the
tree. "Grafting" means appending a new branch for every item in an existing
branch.  
![Public method](../icons/pubmethod.gif)|
[Insert](M_Grasshopper_DataTree_1_Insert.htm)|  Insert a data item to the
specified branch in the tree. If the branch doesn't exist yet, it will be
created.  
![Public method](../icons/pubmethod.gif)|
[ItemExists](M_Grasshopper_DataTree_1_ItemExists.htm)|  Test if the specified
path + item index are defined inside the tree.  
![Public method](../icons/pubmethod.gif)|
[MergeTree](M_Grasshopper_DataTree_1_MergeTree.htm)|  Merges two trees
together. Data inside similar branches will be merged into single lists and
unique paths will be appended. The other tree will not be altered, so beware
that data is now shared among both trees.  
![Public method](../icons/pubmethod.gif)|
[Path](M_Grasshopper_DataTree_1_Path.htm)|  Gets the data path at the
specified index.  
![Public method](../icons/pubmethod.gif)|
[PathExists(GH_Path)](M_Grasshopper_DataTree_1_PathExists.htm)|  Test if the
specified path is already defined inside the tree.  
![Public method](../icons/pubmethod.gif)|
[PathExists(Int32)](M_Grasshopper_DataTree_1_PathExists_1.htm)|  Test if the
specified path is already defined inside the tree.  
![Public method](../icons/pubmethod.gif)|
[RemovePath(GH_Path)](M_Grasshopper_DataTree_1_RemovePath.htm)|  Removes a
path and all associated data from the structure. If the path doesn't exist,
nothing will happen.  
![Public method](../icons/pubmethod.gif)|
[RemovePath(Int32)](M_Grasshopper_DataTree_1_RemovePath_1.htm)|  Removes a
path and all associated data from the structure. If the path doesn't exist,
nothing will happen.  
![Public method](../icons/pubmethod.gif)|
[RenumberPaths](M_Grasshopper_DataTree_1_RenumberPaths.htm)|  Renumber all
paths in this data tree, using a single incrementing path index.  
![Public method](../icons/pubmethod.gif)|
[RenumberPaths(String)](M_Grasshopper_DataTree_1_RenumberPaths_1.htm)|
Renumber all paths in this data tree, using a single incrementing path index.  
![Public method](../icons/pubmethod.gif)|
[SimplifyPaths](M_Grasshopper_DataTree_1_SimplifyPaths.htm)|  Simplify the
branches in this tree by removing all identical path entries. The length of
the shortest path will be indicative of the similarity search depth. If this
tree only contains a single branch, the branch wil be simplified to its last
index.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_DataTree_1_ToString.htm)|  Creates a brief
description of the tree.  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Public method](../icons/pubmethod.gif)|
[TrimExcess](M_Grasshopper_DataTree_1_TrimExcess.htm)|  Trims the excess
allocated memory in all branches  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

