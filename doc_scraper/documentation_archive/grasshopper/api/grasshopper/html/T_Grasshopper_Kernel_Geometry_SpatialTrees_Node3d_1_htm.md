---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm
scraped_at: 2025-09-08T16:19:54.230659
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm
"Grasshopper.Kernel.Geometry.SpatialTrees")

[Node3d(T)
Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm
"Node3d\(T\) Class")

[Node3d(T) Constructor
](../html/Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor.htm
"Node3d\(T\) Constructor ")

[Node3d(T)
Properties](../html/Properties_T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm
"Node3d\(T\) Properties")

[Node3d(T)
Methods](../html/Methods_T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm
"Node3d\(T\) Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Node3dT Class  
  
---  
  
Basic node in a Tree3d structure. Nodes in tree structures maintain a local
region and either a list of content indices or a list of up to 8 child nodes.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.Geometry.SpatialTreesNode3dT  

**Namespace:**
[Grasshopper.Kernel.Geometry.SpatialTrees](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class Node3d<T>
    
    
    
    Public NotInheritable Class Node3d(Of T)

#### Type Parameters

T

    

The Node3dT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [Node3dT(Coordinates3dT,
BoundingBox)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor.htm)|
Create a new spatial tree root.  
![Public method](../icons/pubmethod.gif)| [Node3dT(Coordinates3dT,
BoundingBox,
Int32)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor_1.htm)|
Create a new spatial tree root.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Center](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Center.htm)|
Gets the center of the spatial region of this node. If the node contains no
children the center is always in the middle of the Region. If the node does
contain child-nodes, the center may be anywhere within the region.  
![Public property](../icons/pubproperty.gif)|
[ChildCount](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ChildCount.htm)|
Gets the number of defined child nodes. Leaf nodes have no children. Root and
twig nodes can have anywhere between 1 and 8 children.  
![Public property](../icons/pubproperty.gif)|
[ChildNode](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ChildNode.htm)|
Gets the child node at the given index.  
![Public property](../icons/pubproperty.gif)|
[ContentAverage](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ContentAverage.htm)|
Returns the average coordinate of all items in this node. If this node does
not contain any items, Point3d.Unset is returned.  
![Public property](../icons/pubproperty.gif)|
[ContentBoundingBox](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ContentBoundingBox.htm)|
Returns the boundingbox of all items in this node. If this node does not
contain any items, BoundingBox.Empty is returned.  
![Public property](../icons/pubproperty.gif)|
[IndicesLocal](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IndicesLocal.htm)|
Gets the list of item indices that are contained within this node.  
![Public property](../icons/pubproperty.gif)|
[IndicesRecursive](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IndicesRecursive.htm)|
Gets the list of item indices that are contained within this node and any
child nodes.  
![Public property](../icons/pubproperty.gif)|
[IsLeaf](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsLeaf.htm)|
Gets whether this node is a leaf node. Leaf nodes have no child nodes.  
![Public property](../icons/pubproperty.gif)|
[IsMutable](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsMutable.htm)|
Gets whether this tree is mutable. You can only add items to mutable trees. We
don't recommend removing items from unmutable trees, though that shouldn't
necessarily lead to problems. Trees become unmutable after a call to
ShrinkRegions(), CollapseNodes() or OptimizeTree().  
![Public property](../icons/pubproperty.gif)|
[IsRoot](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsRoot.htm)|
Gets whether this node is a root node. Root nodes have no parent node and
depth zero.  
![Public property](../icons/pubproperty.gif)|
[IsTwig](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsTwig.htm)|
Gets whether this node is a twig node. Twig nodes have both parents and at
least one child.  
![Public property](../icons/pubproperty.gif)|
[ItemCount](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ItemCount.htm)|
Gets the total number of items stored directly in this node.  
![Public property](../icons/pubproperty.gif)|
[ItemsGlobal](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ItemsGlobal.htm)|
Gets the list of all items stored inside this entire tree. Do not modify this
collection unless you know what you are doing.  
![Public property](../icons/pubproperty.gif)|
[ItemsLocal](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ItemsLocal.htm)|
Gets a list of all the items stored directly in this node. This list is
constructed every time you access this property, so keep it down to a minimum.  
![Public property](../icons/pubproperty.gif)|
[Limit](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Limit.htm)|  Gets
the subdivision limit for this tree. This limit can only be set once when you
create a new tree. It is fixed forever after.  
![Public property](../icons/pubproperty.gif)|
[MemoryConsumption](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_MemoryConsumption.htm)|
Gets the estimated memory consumption of the (sub)tree structure. Items inside
the global list are not included in this estimate.  
![Public property](../icons/pubproperty.gif)|
[NextNode](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NextNode.htm)|
Gets the logical neighbour to the right of this node. There is no spatial
relationships between logical neighbours, this is purely an iteration aid.  
![Public property](../icons/pubproperty.gif)|
[NodeDepth](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NodeDepth.htm)|
Gets the recursive depth of this node. The tree root is at depth zero. The
first subdivision is at depth one, and so on and so forth.  
![Public property](../icons/pubproperty.gif)|
[ParentNode](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ParentNode.htm)|
Gets the immediate parent of this node. Root nodes have no parent.  
![Public property](../icons/pubproperty.gif)|
[Region](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Region.htm)|
Gets the spatial region of this node.  
![Public property](../icons/pubproperty.gif)|
[RootNode](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_RootNode.htm)|
Gets the ultimate root node for this tree.  
![Public property](../icons/pubproperty.gif)|
[WeightedSubdivision](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_WeightedSubdivision.htm)|
Gets or sets whether subdivision is weighted based on content averages.
Setting this value will only affect future subdivisions, not existing ones.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Add](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Add.htm)|  Insert
another item into the tree. The item should be within the region of this node.  
![Public method](../icons/pubmethod.gif)|
[AddRange](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_AddRange.htm)|
Insert a collection of items into the tree. The items should all be within the
region of this node.  
![Public method](../icons/pubmethod.gif)|
[AddToRhinoDocument](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_AddToRhinoDocument.htm)|  
![Public method](../icons/pubmethod.gif)|
[CollapseNodes](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_CollapseNodes.htm)|
Collapse the (sub)tree rooted at this node. Collapsing happens when a node
only has a single child, in which case the child usurps the position
previously held by the parent. Do not collapse a (sub)tree if you still plan
to add items later.  
![Public method](../icons/pubmethod.gif)|
[FurthestItem(T)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_4.htm)|
Find the furtest item.  
![Public method](../icons/pubmethod.gif)|
[FurthestItem(Point3d)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem.htm)|
Find the furtest item.  
![Public method](../icons/pubmethod.gif)| [FurthestItem(Double, Double,
Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_2.htm)|
Find the furtest item.  
![Public method](../icons/pubmethod.gif)| [FurthestItem(T, Double,
Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_5.htm)|
Find the furtest item.  
![Public method](../icons/pubmethod.gif)| [FurthestItem(Point3d, Double,
Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_1.htm)|
Find the furtest item.  
![Public method](../icons/pubmethod.gif)| [FurthestItem(Double, Double,
Double, Double,
Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_3.htm)|
Find the furtest item.  
![Public method](../icons/pubmethod.gif)|
[NearestItem(T)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_5.htm)|
Find the nearest item.  
![Public method](../icons/pubmethod.gif)|
[NearestItem(Point3d)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem.htm)|
Find the nearest item.  
![Public method](../icons/pubmethod.gif)| [NearestItem(Double, Double,
Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_2.htm)|
Find the nearest item.  
![Public method](../icons/pubmethod.gif)| [NearestItem(T, Double,
Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_6.htm)|
Find the nearest item.  
![Public method](../icons/pubmethod.gif)| [NearestItem(Point3d, Double,
Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_1.htm)|
Find the nearest item.  
![Public method](../icons/pubmethod.gif)| [NearestItem(Double, Double, Double,
Validation3dT)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_3.htm)|
Find the nearest item using custom validation criteria.  
![Public method](../icons/pubmethod.gif)| [NearestItem(Double, Double, Double,
Double,
Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_4.htm)|
Find the nearest item.  
![Public method](../icons/pubmethod.gif)| [NearestItems(T,
Int32)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems_2.htm)|
Find the N nearest items.  
![Public method](../icons/pubmethod.gif)| [NearestItems(Double, Double,
Double,
Int32)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems.htm)|
Find the N nearest items.  
![Public method](../icons/pubmethod.gif)| [NearestItems(T, Int32, Double,
Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems_3.htm)|
Find the N nearest items.  
![Public method](../icons/pubmethod.gif)| [NearestItems(Double, Double,
Double, Int32, Double,
Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems_1.htm)|
Find the N nearest items.  
![Public method](../icons/pubmethod.gif)|
[OptimizeTree](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_OptimizeTree.htm)|
Optimize this tree for fast searches. Do not call this method if you still
plan to add items in the future. You can no longer modify this tree once it
has been optimized.  
![Public method](../icons/pubmethod.gif)|
[Remove(Index3dT)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Remove.htm)|
Remove the item with the given index from the entire tree. It doesn't matter
on which node you call this function, it is a tree-wide operation.  
![Public method](../icons/pubmethod.gif)|
[Remove(Int32)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Remove_1.htm)|
Remove the item with the given index from the entire tree. It doesn't matter
on which node you call this function, it is a tree-wide operation.  
![Public method](../icons/pubmethod.gif)|
[ShrinkRegions](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ShrinkRegions.htm)|
Shrink the region for this node and all child nodes. Do not use this method if
you intend to add more items later as it creates spatial gaps in the tree
structure. You can shrink nodes if you're done adding items and want to start
searching the tree.  
![Public method](../icons/pubmethod.gif)|
[SubTree](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_SubTree.htm)|
Gets an iterator for all nodes in this (sub)tree.  
![Public method](../icons/pubmethod.gif)|
[TrimExcess](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_TrimExcess.htm)|
Trim the excess space on all index lists. You can call this method to reduce
memory usage. It will not modify the tree in any functional way.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Geometry.SpatialTrees
Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

